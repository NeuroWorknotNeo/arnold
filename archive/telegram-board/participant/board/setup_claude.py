"""Подготовка окружения агента при старте контейнера (идемпотентно).

- добавляет PostToolUse-хук ``board-hook`` в пользовательские настройки Claude Code
  (~/.claude/settings.json), не трогая остальные настройки;
- настраивает git: имя автора коммитов и, если задан GH_TOKEN, помощник учётных данных,
  который берёт токен из переменной окружения (сам токен в файлы не пишется).
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

HOOK_COMMAND = "board-hook"
GIT_HELPER = '!f() { test "$1" = get || exit 0; echo username=x-access-token; echo "password=$GH_TOKEN"; }; f'


def ensure_hook(settings_path: Path) -> bool:
    """Возвращает True, если файл изменён."""
    try:
        settings = json.loads(settings_path.read_text(encoding="utf-8"))
        if not isinstance(settings, dict):
            settings = {}
    except (OSError, ValueError):
        settings = {}
    hooks = settings.setdefault("hooks", {})
    post = hooks.setdefault("PostToolUse", [])
    for group in post:
        for hook in (group or {}).get("hooks", []):
            if hook.get("command") == HOOK_COMMAND:
                return False
    post.append({"matcher": "*", "hooks": [{"type": "command", "command": HOOK_COMMAND, "timeout": 10}]})
    settings_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = settings_path.with_suffix(".tmp")
    tmp.write_text(json.dumps(settings, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(settings_path)
    return True


def git_config(*args: str) -> None:
    subprocess.run(["git", "config", "--global", *args], check=True, capture_output=True, text=True)


def main() -> int:
    home = Path.home()
    changed = ensure_hook(home / ".claude" / "settings.json")
    pid = os.environ.get("PARTICIPANT_ID") or "participant"
    git_config("user.name", os.environ.get("GIT_AUTHOR_NAME") or f"{pid} (agent)")
    git_config("user.email", os.environ.get("GIT_AUTHOR_EMAIL") or f"{pid}@users.noreply.github.com")
    git_config("pull.ff", "only")
    key = "credential.https://github.com.helper"
    subprocess.run(["git", "config", "--global", "--unset-all", key], capture_output=True, text=True)
    if os.environ.get("GH_TOKEN"):
        git_config("--add", key, "")  # пустое значение сбрасывает унаследованные помощники
        git_config("--add", key, GIT_HELPER)
    print(f"setup: хук {'добавлен' if changed else 'уже был'}, git настроен"
          + (" (с GH_TOKEN)" if os.environ.get("GH_TOKEN") else " (только чтение GitHub)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
