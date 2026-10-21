"""Служебные команды владельца, выполняются внутри контейнера transport.

Скачать вложение сообщения доски (байты — в stdout)::

    docker compose exec -T transport python3 -m board.owner_tools attachment 1234 > job.tar.gz

Отправить файл на доску от имени бота участника (байты — из stdin)::

    docker compose exec -T transport python3 -m board.owner_tools upload \
        --name result.tar.gz --reply-to 1234 --caption "результат" < result.tar.gz

Используются скриптом ``compute/run_job.py`` для расчётов на сервере владельца.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import sys

from .config import ConfigError, TransportConfig
from .journal import Journal
from .service import ApiError, BoardService
from .telegram_api import TelegramAPI, TelegramError


def build_service() -> BoardService:
    cfg = TransportConfig.from_env()
    service = BoardService(cfg, Journal(cfg.journal_path), TelegramAPI(cfg.token, cfg.api_base))
    service.bot_id = service.journal.meta_int("bot_id") or None
    service.bot_username = service.journal.meta("bot_username") or ""
    return service


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="board.owner_tools")
    sub = parser.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("attachment", help="вложение сообщения в stdout")
    a.add_argument("id", type=int)
    u = sub.add_parser("upload", help="отправить файл из stdin на доску")
    u.add_argument("--name", required=True)
    u.add_argument("--caption")
    u.add_argument("--reply-to", type=int)
    args = parser.parse_args(argv)
    try:
        service = build_service()
        if args.cmd == "attachment":
            row = service.journal.get(args.id)
            if row is None:
                print(f"сообщения #{args.id} нет в журнале этого участника", file=sys.stderr)
                return 1
            data = service.download(row)
            print(f"name={row['file_name']} size={len(data)} sha256={hashlib.sha256(data).hexdigest()}",
                  file=sys.stderr)
            sys.stdout.buffer.write(data)
            return 0
        data = sys.stdin.buffer.read()
        key = "owner-" + hashlib.sha256(data + (args.caption or "").encode() + args.name.encode()).hexdigest()[:40]
        result = service.op_send_file({
            "name": args.name, "data_b64": base64.b64encode(data).decode("ascii"),
            "caption": args.caption, "reply_to": args.reply_to, "key": key,
        })
        print(("уже было отправлено: " if result.get("replayed") else "отправлено: ")
              + ", ".join(f"#{i}" for i in result["message_ids"]), file=sys.stderr)
        return 0
    except ConfigError as exc:
        print(f"ошибка конфигурации: {exc}", file=sys.stderr)
    except ApiError as exc:
        print(f"ошибка {exc.code}: {exc.message}", file=sys.stderr)
    except TelegramError as exc:
        print(f"ошибка Telegram: {exc}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
