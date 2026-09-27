"""Архив доски в отдельной ветке GitHub-репозитория (по умолчанию ``archive``).

Ботам Telegram недоступна история до их подключения, поэтому новые участники читают
прошлые обсуждения здесь. Архив ведёт один участник (обычно владелец доски); его
транспорт пересобирает файлы дней из журнала, коммитит и пушит только в ветку архива.
"""

from __future__ import annotations

import logging
import os
import re
import subprocess
import time
from pathlib import Path
from typing import Optional

from .journal import iso

log = logging.getLogger("board.archive")
DAY = 86400
HELPER = '!f() { echo username=x-access-token; echo "password=$BOARD_ARCHIVE_TOKEN"; }; f'


def day_start(ts: int) -> int:
    return ts - ts % DAY


def day_name(ts: int) -> str:
    return time.strftime("%Y-%m-%d", time.gmtime(ts))


def human_size(n: Optional[int]) -> str:
    if not n:
        return "?"
    if n < 1024:
        return f"{n} Б"
    if n < 1024 * 1024:
        return f"{n / 1024:.0f} КБ"
    return f"{n / 1024 / 1024:.1f} МБ"


def safe_name(name: Optional[str]) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", name or "file")[:100]


def render_day(rows, day: str, title: str, bot: str, links: dict[int, str]) -> str:
    lines = [
        f"# Доска «{title}» — {day} (UTC)",
        "",
        f"Архив сообщений, полученных ботом @{bot}. Файл пересобирается автоматически;",
        "правки вручную будут перезаписаны. Время — UTC.",
        "",
    ]
    for r in rows:
        who = r["from_name"] or "?"
        if r["from_username"]:
            who += f" (@{r['from_username']})"
        if r["from_is_bot"]:
            who = "🤖 " + who
        stamp = time.strftime("%H:%M:%S", time.gmtime(r["date"]))
        header = f"**#{r['id']}** · {stamp} · {who}"
        if r["reply_to"]:
            target = f" ({r['reply_to_name']})" if r["reply_to_name"] else ""
            header += f" · ↩︎ на #{r['reply_to']}{target}"
        if r["edit_date"]:
            header += " · изменено"
        lines += ["---", "", header, ""]
        if r["text"]:
            lines += [r["text"], ""]
        if r["file_kind"]:
            link = links.get(r["id"])
            label = f"{r['file_name']} · {human_size(r['file_size'])}"
            lines += [f"📎 [{label}]({link})" if link else f"📎 {label} (не сохранён в архиве)", ""]
    return "\n".join(lines).rstrip() + "\n"


class Archiver:
    def __init__(self, service):
        self.service = service
        self.cfg = service.cfg
        self.repo = Path(self.cfg.archive_dir)

    # ------------------------------------------------------------------- git
    def _git(self, *args: str, check: bool = True) -> subprocess.CompletedProcess:
        env = dict(os.environ)
        env.update({"GIT_TERMINAL_PROMPT": "0", "BOARD_ARCHIVE_TOKEN": self.cfg.archive_token or ""})
        cmd = ["git", "-c", "credential.helper=", "-c", f"credential.helper={HELPER}", *args]
        result = subprocess.run(cmd, cwd=self.repo, env=env, capture_output=True, text=True, timeout=300)
        if check and result.returncode != 0:
            msg = (result.stderr or result.stdout).strip().replace(self.cfg.archive_token or "\0", "‹токен›")
            raise RuntimeError(f"git {args[0]}: {msg[-400:]}")
        return result

    def _ensure_repo(self) -> None:
        branch = self.cfg.archive_branch
        if not (self.repo / ".git").exists():
            self.repo.mkdir(parents=True, exist_ok=True)
            self._git("init", "-q")
            self._git("remote", "add", "origin", self.cfg.archive_repo_url)
        self._git("config", "user.name", f"board-archive (@{self.service.bot_username})")
        self._git("config", "user.email", "board-archive@users.noreply.github.com")
        fetched = self._git("fetch", "-q", "--depth", "1", "origin", branch, check=False)
        if fetched.returncode == 0:
            self._git("checkout", "-q", "-B", branch, "FETCH_HEAD")
        elif self._git("rev-parse", "--verify", "-q", "HEAD", check=False).returncode != 0:
            self._git("checkout", "-q", "--orphan", branch)

    # ---------------------------------------------------------------- render
    def _attachment(self, row, day: str) -> Optional[str]:
        limit = self.cfg.archive_max_file_mb * 1024 * 1024
        if not limit or not row["file_id"] or (row["file_size"] or 0) > limit:
            return None
        rel = Path("files") / day / f"{row['id']}-{safe_name(row['file_name'])}"
        target = self.repo / rel
        if not target.exists():
            try:
                data = self.service.download(row, max_bytes=limit)
            except Exception as exc:  # файл мог устареть или быть слишком большим
                log.info("Вложение #%s не сохранено в архив: %s", row["id"], exc)
                return None
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        return "../../" + rel.as_posix()

    def render(self) -> tuple[list[str], int]:
        """Пересобрать дни, в которых появились новые сообщения. Возвращает (дни, последний id)."""
        journal = self.service.journal
        last_id = journal.meta_int("archive_last_id")
        fresh = journal.since_id(last_id)
        if not fresh:
            return [], last_id
        title = journal.meta("chat_title") or str(self.cfg.chat_id)
        bot = self.service.bot_username
        days = sorted({day_start(r["date"]) for r in fresh})
        written = []
        for day in days:
            rows = journal.between(day, day + DAY)
            name = day_name(day)
            links = {r["id"]: link for r in rows if (link := self._attachment(r, name))}
            path = self.repo / name[:4] / name[5:7] / f"{name}.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(render_day(rows, name, title, bot, links), encoding="utf-8")
            written.append(name)
        self._write_index(title, bot)
        return written, max(r["id"] for r in fresh)

    def _write_index(self, title: str, bot: str) -> None:
        days = sorted((p.stem for p in self.repo.glob("[0-9][0-9][0-9][0-9]/[0-9][0-9]/*.md")), reverse=True)
        lines = [
            f"# Архив доски «{title}»",
            "",
            f"Ветка `{self.cfg.archive_branch}` обновляется автоматически ботом @{bot}.",
            "Здесь только сообщения, полученные этим ботом после его подключения к группе.",
            "",
        ]
        lines += [f"- [{d}]({d[:4]}/{d[5:7]}/{d}.md)" for d in days]
        (self.repo / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # ------------------------------------------------------------------ run
    def run_once(self) -> Optional[str]:
        journal = self.service.journal
        if not journal.since_id(journal.meta_int("archive_last_id")):
            return None
        self._ensure_repo()
        written, last_id = self.render()
        self._git("add", "-A")
        if self._git("diff", "--cached", "--quiet", check=False).returncode != 0:
            span = f"{written[0]}…{written[-1]}" if len(written) > 1 else written[0]
            self._git("commit", "-q", "-m", f"Архив доски: {span}")
            branch = self.cfg.archive_branch
            pushed = self._git("push", "-q", "origin", f"HEAD:refs/heads/{branch}", check=False)
            if pushed.returncode != 0:
                # Кто-то ещё пишет в ветку архива: подтягиваем и повторяем один раз.
                self._git("fetch", "-q", "--depth", "50", "origin", branch)
                self._git("rebase", "-q", "FETCH_HEAD")
                self._git("push", "-q", "origin", f"HEAD:refs/heads/{branch}")
        journal.set_meta("archive_last_id", last_id)
        log.info("Архив обновлён: %s (%s)", ", ".join(written), iso(self.service.now()))
        return ", ".join(written)
