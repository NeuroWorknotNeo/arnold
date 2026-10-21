"""Цикл непрерывной работы: ходы ``claude -p --resume <сессия>`` в одном постоянном диалоге.

Следующий ход начинается, когда закончился предыдущий и выдержана пауза (или агент сам попросил
подождать через ``board sleep``). Прямое обращение на доске будит раньше. Лимиты подписки,
ошибки и пауза владельца обрабатываются без лавины повторов.

Команды: ``board-runner`` (цикл), ``board-runner status``, ``board-runner reset-session``.
"""

from __future__ import annotations

import json
import logging
import os
import queue
import signal
import subprocess
import sys
import threading
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Optional

from . import prompts
from .api_client import BoardApiError, BoardClient, BoardUnavailable
from .config import AgentConfig, ConfigError

log = logging.getLogger("board.runner")

AUTH_MARKERS = (
    "not logged in", "login expired", "please run /login", "invalid api key", "authentication_error",
    "authentication failed", "oauth token has expired", "invalid bearer token", "401",
)
MISSING_SESSION_MARKERS = ("no conversation found", "session not found", "could not find session")
LIMIT_MARKERS = ("usage limit", "rate limit", "rate_limit", "limit reached", "hit your limit", "session limit")
RESULT_GRACE_SECONDS = 15


@dataclass
class TurnResult:
    session_id: Optional[str] = None
    subtype: str = ""
    is_error: bool = True
    text: str = ""
    num_turns: Optional[int] = None
    duration_ms: Optional[int] = None
    rate_limit: Optional[dict] = None
    exit_code: Optional[int] = None
    timed_out: bool = False
    stopped: bool = False
    stderr_tail: str = ""
    model: Optional[str] = None

    @property
    def blob(self) -> str:
        return f"{self.text}\n{self.stderr_tail}".lower()


@dataclass
class RunnerState:
    session_id: Optional[str] = None
    turns: int = 0
    turns_by_day: dict[str, int] = field(default_factory=dict)
    last_turn_started: Optional[int] = None
    last_turn_ended: Optional[int] = None
    soft_until: int = 0       # пауза между ходами: обращение может прервать
    hard_until: int = 0       # лимит подписки / ошибка: ждём в любом случае
    consecutive_errors: int = 0
    last_error: Optional[str] = None
    last_subtype: Optional[str] = None
    session_resets: int = 0
    pending_recovery: Optional[str] = None
    alerted: Optional[str] = None

    @classmethod
    def load(cls, path: Path) -> "RunnerState":
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return cls()
        known = {k: v for k, v in data.items() if k in cls.__dataclass_fields__}
        return cls(**known)

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.__dict__, ensure_ascii=False, indent=2), encoding="utf-8")
        tmp.replace(path)


def parse_stream(lines, on_event: Optional[Callable[[dict], None]] = None) -> TurnResult:
    """Разбор stream-json вывода ``claude -p``."""
    result = TurnResult()
    for line in lines:
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if on_event:
            on_event(event)
        kind = event.get("type")
        if kind == "system" and event.get("subtype") == "init":
            result.session_id = event.get("session_id") or result.session_id
            result.model = event.get("model") or result.model
        elif kind == "rate_limit_event" and isinstance(event.get("rate_limit_info"), dict):
            result.rate_limit = event["rate_limit_info"]
        elif kind == "result":
            result.session_id = event.get("session_id") or result.session_id
            result.subtype = str(event.get("subtype") or "")
            result.is_error = bool(event.get("is_error"))
            text = event.get("result")
            if not isinstance(text, str):
                errors = event.get("errors")
                text = "\n".join(map(str, errors)) if isinstance(errors, list) else ""
            result.text = text
            result.num_turns = event.get("num_turns")
            result.duration_ms = event.get("duration_ms")
    return result


def reset_time(info: Optional[dict]) -> Optional[int]:
    if not info:
        return None
    value = info.get("resetsAt")
    if isinstance(value, (int, float)):
        return int(value / 1000 if value > 1e12 else value)
    if isinstance(value, str):
        try:
            from datetime import datetime
            return int(datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp())
        except ValueError:
            return None
    return None


class Runner:
    def __init__(self, cfg: AgentConfig, client: BoardClient, clock: Callable[[], float] = time.time,
                 env: Optional[dict[str, str]] = None):
        self.cfg = cfg
        self.client = client
        self.clock = clock
        self.env = dict(os.environ if env is None else env)
        self.state = RunnerState.load(cfg.state_path)
        self.stop = threading.Event()
        self._board_info: Optional[dict] = None

    # ------------------------------------------------------------- helpers
    def now(self) -> int:
        return int(self.clock())

    def save(self) -> None:
        self.state.save(self.cfg.state_path)

    def today(self) -> str:
        return time.strftime("%Y-%m-%d", time.gmtime(self.now()))

    def log_turn(self, record: dict) -> None:
        path = self.cfg.turns_log_path
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")

    def heartbeat(self, state: str) -> None:
        try:
            self.client.call("heartbeat", {
                "state": state,
                "turns": self.state.turns,
                "session": (self.state.session_id or "")[:8],
                "last_error": self.state.last_error,
                "next_turn_at": max(self.state.soft_until, self.state.hard_until) or None,
            })
        except (BoardUnavailable, BoardApiError):
            pass

    def alert_owner(self, key: str, text: str) -> None:
        """Одно сообщение владельцу на каждую новую проблему (без повторов)."""
        if self.state.alerted == key:
            return
        try:
            self.client.call("notify_owner", {"text": text})
        except (BoardUnavailable, BoardApiError):
            return
        self.state.alerted = key
        self.save()

    def board_info(self) -> dict:
        if self._board_info is None:
            self._board_info = self.client.call("status")
        return self._board_info

    # ------------------------------------------------------------ workdir
    def ensure_workdir(self) -> bool:
        work = Path(self.cfg.workdir)
        if (work / ".git").exists() or (work.exists() and not self.cfg.repo_url):
            return True
        if not self.cfg.repo_url:
            work.mkdir(parents=True, exist_ok=True)
            return True
        work.parent.mkdir(parents=True, exist_ok=True)
        result = subprocess.run(["git", "clone", "-q", self.cfg.repo_url, str(work)],
                                capture_output=True, text=True, timeout=600, env=self.env)
        if result.returncode != 0:
            log.warning("Не удалось клонировать репозиторий задачи: %s", result.stderr.strip()[-300:])
            return False
        log.info("Репозиторий задачи склонирован в %s", work)
        return True

    # --------------------------------------------------------------- claude
    def build_command(self, prompt: str, resume: Optional[str]) -> list[str]:
        info = self.board_info()
        brief = prompts.runtime_brief(
            self.cfg.participant_id, info.get("bot_username") or "?", info.get("owner_ids") or [],
            self.cfg.min_pause, int(info.get("max_posts_per_hour") or 12), self.env.get("AGENT_MEM_LIMIT"),
        )
        cmd = [self.cfg.claude_bin, "-p", "--output-format", "stream-json", "--verbose", *self.cfg.extra_args]
        if resume:
            cmd += ["--resume", resume]
        if self.cfg.model:
            cmd += ["--model", self.cfg.model]
        if self.cfg.effort:
            cmd += ["--effort", self.cfg.effort]
        cmd += ["--dangerously-skip-permissions", "--append-system-prompt", brief, "--", prompt]
        return cmd

    def run_claude(self, cmd: list[str]) -> TurnResult:
        env = dict(self.env)
        env.setdefault("CLAUDE_CODE_MAX_OUTPUT_TOKENS", "64000")
        env.setdefault("DISABLE_AUTOUPDATER", "1")
        try:
            proc = subprocess.Popen(cmd, cwd=self.cfg.workdir, env=env, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, text=True, start_new_session=True)
        except OSError as exc:
            return TurnResult(subtype="spawn_error", text=f"не удалось запустить claude: {exc}")
        lines: "queue.Queue[Optional[str]]" = queue.Queue()
        stderr_tail: list[str] = []

        def read_stdout():
            for line in proc.stdout:
                lines.put(line)
            lines.put(None)

        def read_stderr():
            for line in proc.stderr:
                stderr_tail.append(line)
                del stderr_tail[:-40]

        threading.Thread(target=read_stdout, daemon=True).start()
        threading.Thread(target=read_stderr, daemon=True).start()
        deadline = time.monotonic() + self.cfg.turn_timeout
        collected: list[str] = []
        timed_out = stopped = False
        result_seen_at: Optional[float] = None
        while True:
            if self.stop.is_set():
                stopped = True
                break
            now = time.monotonic()
            if now > deadline:
                timed_out = True
                break
            if result_seen_at and now - result_seen_at > RESULT_GRACE_SECONDS:
                break
            try:
                line = lines.get(timeout=1)
            except queue.Empty:
                continue
            if line is None:
                break
            collected.append(line)
            if '"type":"result"' in line.replace(" ", ""):
                result_seen_at = time.monotonic()
        if proc.poll() is None:
            self._terminate(proc)
        result = parse_stream(collected)
        result.exit_code = proc.returncode
        result.timed_out = timed_out
        result.stopped = stopped
        result.stderr_tail = "".join(stderr_tail)[-2000:]
        if timed_out and not result.subtype:
            result.subtype = "timeout"
        if stopped and not result.subtype:
            result.subtype = "stopped"
        return result

    @staticmethod
    def _terminate(proc: subprocess.Popen) -> None:
        for sig, wait in ((signal.SIGINT, 20), (signal.SIGTERM, 10), (signal.SIGKILL, 5)):
            try:
                os.killpg(proc.pid, sig)
            except (ProcessLookupError, PermissionError):
                return
            try:
                proc.wait(timeout=wait)
                return
            except subprocess.TimeoutExpired:
                continue

    # ----------------------------------------------------------------- turn
    def compose_prompt(self, control: dict) -> tuple[str, str]:
        pid = self.cfg.participant_id
        if self.state.pending_recovery:
            return "recovery", prompts.recovery_prompt(pid, self.state.pending_recovery)
        if not self.state.session_id:
            return "first", prompts.first_prompt(pid)
        elapsed = (self.now() - (self.state.last_turn_ended or self.now())) // 60
        woke_early = bool(control.get("sleep_until")) and control["sleep_until"] > self.now()
        return "continue", prompts.continue_prompt(
            self.state.turns + 1, int(elapsed), int(control.get("unread") or 0),
            int(control.get("unread_mentions") or 0), control.get("sleep_reason"), woke_early,
        )

    def handle_result(self, res: TurnResult, kind: str) -> None:
        now = self.now()
        st = self.state
        st.last_turn_ended = now
        st.last_subtype = res.subtype
        blob = res.blob
        limit_hit = (res.rate_limit or {}).get("status") == "rejected" or (
            res.is_error and any(m in blob for m in LIMIT_MARKERS)
        )
        if res.session_id and not (res.is_error and res.subtype == "error_during_execution"):
            st.session_id = res.session_id
        if res.stopped:
            st.last_error = None
            return
        if not res.is_error and not res.timed_out:
            st.turns += 1
            day = self.today()
            st.turns_by_day = {day: st.turns_by_day.get(day, 0) + 1}
            st.consecutive_errors = 0
            st.last_error = None
            st.pending_recovery = None
            st.alerted = None
            st.soft_until = now + self.cfg.min_pause
            return
        if limit_hit:
            resets = reset_time(res.rate_limit) or now + 900
            st.hard_until = max(resets + 60, now + 300)
            st.last_error = f"лимит подписки, ожидание до {time.strftime('%H:%M UTC', time.gmtime(st.hard_until))}"
            log.warning(st.last_error)
            return
        if any(m in blob for m in AUTH_MARKERS) and res.subtype != "timeout":
            st.hard_until = now + 1800
            st.last_error = "Claude Code не авторизован"
            self.alert_owner("auth", "Claude Code не авторизован: проверьте CLAUDE_CODE_OAUTH_TOKEN в .env "
                                     "(значение из `claude setup-token`) и перезапустите контейнер agent.")
            return
        if st.session_id and (res.subtype == "error_during_execution" or "ede_diagnostic" in blob
                              or any(m in blob for m in MISSING_SESSION_MARKERS)):
            log.warning("Сессия %s не возобновляется (%s): начинаю новую", st.session_id, res.subtype)
            st.session_id = None
            st.session_resets += 1
            st.pending_recovery = "сессия оборвалась на вызове инструмента или не найдена"
            st.last_error = "сессия пересоздана"
            st.soft_until = now + 30
            self.alert_owner(f"reset-{st.session_resets}",
                             "Диалог участника не возобновился, начата новая сессия; участник восстановит "
                             "контекст по своим заметкам.")
            return
        if res.timed_out:
            st.last_error = f"ход превысил TURN_TIMEOUT_SECONDS={self.cfg.turn_timeout}"
            st.soft_until = now + self.cfg.min_pause
            return
        st.consecutive_errors += 1
        delay = min(self.cfg.error_backoff_max, 60 * 2 ** min(st.consecutive_errors - 1, 10))
        st.hard_until = now + delay
        st.last_error = (res.text or res.stderr_tail or res.subtype or "ошибка")[-300:]
        log.warning("Ход завершился ошибкой (%s), повтор через %s с", res.subtype, delay)
        if st.consecutive_errors == 5:
            self.alert_owner(f"errors-{st.session_resets}-{st.turns}",
                             f"Пять ходов подряд завершились ошибкой. Последняя: {st.last_error[:200]}")

    def step(self) -> float:
        """Один шаг цикла; возвращает, сколько секунд подождать до следующего шага."""
        try:
            control = self.client.call("control")
        except (BoardUnavailable, BoardApiError) as exc:
            log.info("Транспорт недоступен (%s), жду", exc)
            return 15
        now = self.now()
        st = self.state
        mentions = int(control.get("unread_mentions") or 0)
        if control.get("paused"):
            self.heartbeat("paused")
            return 30
        if st.hard_until > now:
            self.heartbeat("waiting_limit" if "лимит" in (st.last_error or "") else "backoff")
            return min(60, st.hard_until - now)
        sleep_until = int(control.get("sleep_until") or 0)
        if not mentions:
            if sleep_until > now:
                self.heartbeat("sleeping")
                return min(30, sleep_until - now)
            if st.soft_until > now:
                self.heartbeat("pause_between_turns")
                return min(30, st.soft_until - now)
            cap = self.cfg.max_turns_per_day
            if cap and st.turns_by_day.get(self.today(), 0) >= cap:
                self.heartbeat("daily_cap")
                return 300
        if not self.ensure_workdir():
            st.hard_until = now + 300
            st.last_error = "не удалось клонировать репозиторий задачи"
            self.save()
            return 60
        kind, prompt = self.compose_prompt(control)
        resume = st.session_id if kind == "continue" else None
        if sleep_until:
            try:
                self.client.call("wake")
            except (BoardUnavailable, BoardApiError):
                pass
        st.last_turn_started = now
        self.save()
        self.heartbeat("working")
        log.info("Ход #%s (%s)%s", st.turns + 1, kind, f", обращений: {mentions}" if mentions else "")
        res = self.run_claude(self.build_command(prompt, resume))
        self.handle_result(res, kind)
        self.save()
        self.log_turn({
            "started": st.last_turn_started, "ended": st.last_turn_ended, "kind": kind, "subtype": res.subtype,
            "is_error": res.is_error, "timed_out": res.timed_out, "num_turns": res.num_turns,
            "duration_ms": res.duration_ms, "session": (st.session_id or "")[:8], "model": res.model,
            "rate_limit": res.rate_limit, "error": st.last_error,
        })
        self.heartbeat("idle")
        return 1

    def run_forever(self) -> None:
        while not self.stop.is_set():
            try:
                delay = self.step()
            except Exception:
                log.exception("Сбой шага цикла")
                delay = 60
            self.stop.wait(max(1.0, float(delay)))


def main(argv: Optional[list[str]] = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    logging.basicConfig(level=os.environ.get("LOG_LEVEL", "INFO"),
                        format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    try:
        cfg = AgentConfig.from_env()
    except ConfigError as exc:
        log.error("Ошибка конфигурации: %s", exc)
        return 2
    if argv and argv[0] == "status":
        state = RunnerState.load(cfg.state_path)
        print(json.dumps(state.__dict__, ensure_ascii=False, indent=2))
        return 0
    if argv and argv[0] == "reset-session":
        state = RunnerState.load(cfg.state_path)
        state.session_id = None
        state.pending_recovery = "владелец попросил начать новую сессию"
        state.save(cfg.state_path)
        print("Следующий ход начнёт новую сессию (контекст восстановится по заметкам).")
        return 0
    if not os.environ.get("CLAUDE_CODE_OAUTH_TOKEN") and not os.environ.get("ANTHROPIC_API_KEY"):
        log.warning("Не задан CLAUDE_CODE_OAUTH_TOKEN: Claude Code попробует учётные данные из ~/.claude")
    if os.environ.get("ANTHROPIC_API_KEY"):
        log.warning("Задан ANTHROPIC_API_KEY: он главнее подписки, оплата пойдёт по тарифам API")
    runner = Runner(cfg, BoardClient())

    def _stop(signum, frame):  # noqa: ARG001
        runner.stop.set()

    signal.signal(signal.SIGTERM, _stop)
    signal.signal(signal.SIGINT, _stop)
    log.info("Цикл участника %s запущен (сессия %s)", cfg.participant_id, runner.state.session_id or "новая")
    runner.run_forever()
    runner.save()
    log.info("Цикл остановлен")
    return 0


if __name__ == "__main__":
    sys.exit(main())
