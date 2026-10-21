"""Настройки из переменных окружения.

Транспорт и агент живут в разных контейнерах и читают разные наборы переменных:
токен Telegram-бота видит только транспорт, токен Claude — только агент.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Mapping, Optional

TOKEN_RE = re.compile(r"^\d{5,}:[A-Za-z0-9_-]{30,}$")
PARTICIPANT_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{1,30}[a-z0-9]$")
DEFAULT_SOCKET = "/run/board/board.sock"


class ConfigError(ValueError):
    """Ошибка конфигурации: сообщение можно показывать владельцу (секретов в нём нет)."""


def _get(env: Mapping[str, str], name: str) -> Optional[str]:
    value = env.get(name)
    if value is None:
        return None
    value = value.strip()
    # systemd/compose иногда передают значения в кавычках — снимаем одну пару.
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1].strip()
    return value or None


def _int(env: Mapping[str, str], name: str, default: int, lo: int, hi: int) -> int:
    raw = _get(env, name)
    if raw is None:
        return default
    try:
        value = int(raw)
    except ValueError:
        raise ConfigError(f"{name} должно быть целым числом, получено {raw!r}") from None
    if not lo <= value <= hi:
        raise ConfigError(f"{name} должно быть в диапазоне [{lo}, {hi}], получено {value}")
    return value


def _bool(env: Mapping[str, str], name: str, default: bool) -> bool:
    raw = _get(env, name)
    if raw is None:
        return default
    lowered = raw.lower()
    if lowered in {"1", "true", "yes", "on", "да"}:
        return True
    if lowered in {"0", "false", "no", "off", "нет"}:
        return False
    raise ConfigError(f"{name} должно быть true или false, получено {raw!r}")


def parse_owner_ids(raw: Optional[str]) -> frozenset[int]:
    if not raw:
        return frozenset()
    ids = set()
    for part in re.split(r"[,\s]+", raw):
        if not part:
            continue
        if not part.isdigit():
            raise ConfigError(f"OWNER_USER_IDS: {part!r} не похоже на числовой Telegram ID")
        ids.add(int(part))
    return frozenset(ids)


@dataclass(frozen=True)
class TransportConfig:
    token: str = field(repr=False)
    chat_id: int
    owner_ids: frozenset[int]
    socket_path: str = DEFAULT_SOCKET
    data_dir: str = "/data"
    api_base: str = "https://api.telegram.org"
    poll_timeout: int = 50
    max_posts_per_hour: int = 12
    digest_interval: int = 600
    archive_enabled: bool = False
    archive_repo_url: Optional[str] = None
    archive_token: Optional[str] = field(default=None, repr=False)
    archive_branch: str = "archive"
    archive_interval: int = 3600
    archive_max_file_mb: int = 5

    @property
    def journal_path(self) -> Path:
        return Path(self.data_dir) / "journal.sqlite3"

    @property
    def files_dir(self) -> Path:
        return Path(self.data_dir) / "files"

    @property
    def archive_dir(self) -> Path:
        return Path(self.data_dir) / "archive-repo"

    @classmethod
    def from_env(cls, env: Optional[Mapping[str, str]] = None) -> "TransportConfig":
        env = os.environ if env is None else env
        token = _get(env, "TELEGRAM_BOT_TOKEN")
        if not token:
            raise ConfigError("не задан TELEGRAM_BOT_TOKEN (токен бота от @BotFather)")
        if not TOKEN_RE.match(token):
            raise ConfigError(
                "TELEGRAM_BOT_TOKEN не похож на токен бота (ожидается вид 123456789:AA…); "
                "проверьте, что он скопирован целиком, без пробелов и переносов"
            )
        raw_chat = _get(env, "BOARD_CHAT_ID")
        if not raw_chat:
            raise ConfigError("не задан BOARD_CHAT_ID (числовой ID группы, начинается с -100)")
        try:
            chat_id = int(raw_chat)
        except ValueError:
            raise ConfigError(f"BOARD_CHAT_ID должно быть числом, получено {raw_chat!r}") from None
        if chat_id >= 0:
            raise ConfigError("BOARD_CHAT_ID группы отрицательный (обычно -100…); проверьте значение")
        owner_ids = parse_owner_ids(_get(env, "OWNER_USER_IDS"))
        if not owner_ids:
            raise ConfigError("не задан OWNER_USER_IDS (ваш числовой Telegram ID; узнать — @userinfobot)")
        archive_enabled = _bool(env, "ARCHIVE_ENABLED", False)
        archive_repo_url = _get(env, "ARCHIVE_REPO_URL")
        archive_token = _get(env, "ARCHIVE_GITHUB_TOKEN")
        if archive_enabled:
            if not archive_repo_url or not archive_repo_url.startswith("https://"):
                raise ConfigError("для архива нужен ARCHIVE_REPO_URL вида https://github.com/владелец/репозиторий.git")
            if not archive_token:
                raise ConfigError("для архива нужен ARCHIVE_GITHUB_TOKEN (fine-grained, Contents: read and write)")
        branch = _get(env, "ARCHIVE_BRANCH") or "archive"
        if not re.match(r"^[A-Za-z0-9._/-]{1,60}$", branch) or branch in {"main", "master"}:
            raise ConfigError("ARCHIVE_BRANCH: нужна отдельная ветка (не main/master), например archive")
        return cls(
            token=token,
            chat_id=chat_id,
            owner_ids=owner_ids,
            socket_path=_get(env, "BOARD_SOCKET") or DEFAULT_SOCKET,
            data_dir=_get(env, "BOARD_DATA_DIR") or "/data",
            api_base=(_get(env, "TELEGRAM_API_BASE") or "https://api.telegram.org").rstrip("/"),
            poll_timeout=_int(env, "TELEGRAM_POLL_TIMEOUT", 50, 0, 60),
            max_posts_per_hour=_int(env, "MAX_POSTS_PER_HOUR", 12, 1, 200),
            digest_interval=_int(env, "DIGEST_INTERVAL_SECONDS", 600, 60, 86400),
            archive_enabled=archive_enabled,
            archive_repo_url=archive_repo_url,
            archive_token=archive_token,
            archive_branch=branch,
            archive_interval=_int(env, "ARCHIVE_INTERVAL_SECONDS", 3600, 300, 86400),
            archive_max_file_mb=_int(env, "ARCHIVE_MAX_FILE_MB", 5, 0, 20),
        )


@dataclass(frozen=True)
class AgentConfig:
    participant_id: str
    socket_path: str = DEFAULT_SOCKET
    workdir: str = "/work/repo"
    repo_url: Optional[str] = None
    claude_bin: str = "claude"
    model: Optional[str] = None
    effort: Optional[str] = None
    turn_timeout: int = 5400
    min_pause: int = 120
    max_pause: int = 3600
    error_backoff_max: int = 1800
    max_turns_per_day: int = 0
    state_dir: str = "/home/agent/.board-runner"
    extra_args: tuple[str, ...] = ()

    @property
    def state_path(self) -> Path:
        return Path(self.state_dir) / "state.json"

    @property
    def turns_log_path(self) -> Path:
        return Path(self.state_dir) / "turns.jsonl"

    @classmethod
    def from_env(cls, env: Optional[Mapping[str, str]] = None) -> "AgentConfig":
        env = os.environ if env is None else env
        participant_id = _get(env, "PARTICIPANT_ID")
        if not participant_id:
            raise ConfigError("не задан PARTICIPANT_ID (короткое имя участника латиницей, например vlad-claude)")
        if not PARTICIPANT_ID_RE.match(participant_id):
            raise ConfigError(
                "PARTICIPANT_ID: только строчные латинские буквы, цифры и дефис, 3–32 символа, "
                f"получено {participant_id!r}"
            )
        effort = _get(env, "CLAUDE_EFFORT")
        if effort and effort not in {"low", "medium", "high", "xhigh", "max"}:
            raise ConfigError(f"CLAUDE_EFFORT: допустимо low, medium, high, xhigh, max; получено {effort!r}")
        extra = _get(env, "CLAUDE_EXTRA_ARGS")
        extra_args = tuple(extra.split()) if extra else ()
        if "--bare" in extra_args:
            raise ConfigError("CLAUDE_EXTRA_ARGS: --bare не работает с подпиской (не читает CLAUDE_CODE_OAUTH_TOKEN)")
        min_pause = _int(env, "MIN_PAUSE_SECONDS", 120, 0, 86400)
        max_pause = _int(env, "MAX_PAUSE_SECONDS", 3600, 60, 86400)
        if max_pause < min_pause:
            raise ConfigError("MAX_PAUSE_SECONDS не может быть меньше MIN_PAUSE_SECONDS")
        return cls(
            participant_id=participant_id,
            socket_path=_get(env, "BOARD_SOCKET") or DEFAULT_SOCKET,
            workdir=_get(env, "WORKDIR") or "/work/repo",
            repo_url=_get(env, "PROBLEM_REPO_URL"),
            claude_bin=_get(env, "CLAUDE_BIN") or "claude",
            model=_get(env, "CLAUDE_MODEL"),
            effort=effort,
            turn_timeout=_int(env, "TURN_TIMEOUT_SECONDS", 5400, 60, 86400),
            min_pause=min_pause,
            max_pause=max_pause,
            error_backoff_max=_int(env, "ERROR_BACKOFF_MAX_SECONDS", 1800, 60, 86400),
            max_turns_per_day=_int(env, "MAX_TURNS_PER_DAY", 0, 0, 10000),
            state_dir=_get(env, "RUNNER_STATE_DIR") or str(Path.home() / ".board-runner"),
            extra_args=extra_args,
        )
