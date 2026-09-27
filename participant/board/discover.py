"""Узнать ID группы до первого запуска транспорта.

Добавьте бота в группу, напишите там любое сообщение и выполните
``docker compose run --rm transport python -m board.discover``.
Команда читает ожидающие обновления, НЕ подтверждая их, и печатает чаты,
из которых они пришли. Запускайте, пока транспорт этого бота остановлен:
два читателя обновлений одного токена конфликтуют (ошибка 409).
"""

from __future__ import annotations

import os
import sys

from .config import TOKEN_RE
from .telegram_api import TelegramAPI, TelegramError


def main() -> int:
    token = (os.environ.get("TELEGRAM_BOT_TOKEN") or "").strip()
    if not TOKEN_RE.match(token):
        print("TELEGRAM_BOT_TOKEN не задан или не похож на токен бота", file=sys.stderr)
        return 2
    api = TelegramAPI(token, os.environ.get("TELEGRAM_API_BASE") or "https://api.telegram.org")
    try:
        me = api.get_me()
        updates = api.call("getUpdates", {"timeout": 0, "allowed_updates": ["message", "my_chat_member"]})
    except TelegramError as exc:
        if exc.code == 409:
            print("Обновления этого бота уже читает другой процесс (транспорт запущен?). Остановите его и повторите.",
                  file=sys.stderr)
        else:
            print(f"Ошибка Telegram: {exc}", file=sys.stderr)
        return 1
    print(f"Бот: @{me.get('username')} (id {me.get('id')})")
    chats: dict[int, dict] = {}
    for update in updates or []:
        for key in ("message", "my_chat_member"):
            chat = (update.get(key) or {}).get("chat")
            if chat:
                chats[chat["id"]] = chat
    if not chats:
        print("Обновлений нет. Добавьте бота в группу, отправьте там сообщение и повторите команду.")
        return 0
    for chat_id, chat in chats.items():
        title = chat.get("title") or chat.get("username") or chat.get("first_name") or ""
        print(f"{chat_id}\t{chat.get('type')}\t{title}")
    print("ID группы — отрицательное число у строки с типом supergroup/group.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
