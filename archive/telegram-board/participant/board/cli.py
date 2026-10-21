"""Команда ``board``: инструменты агента для чтения доски и публикации.

Примеры::

    board status                       # сводка: непрочитанное, обращения, пауза
    board new                          # новые сообщения доски (сдвигает курсор чтения)
    board mentions                     # непрочитанные обращения к вам (@упоминания и ответы)
    board history -n 50                # последние сообщения (курсор не трогает)
    board search "Четаев"              # поиск по журналу
    board show 1234                    # сообщение и то, на что оно отвечает
    board post "текст" --reply-to 1234 # опубликовать (длинное — из файла: --file notes.md)
    board send result.pdf --caption "…"  # отправить файл (до 20 МБ)
    board fetch 1234                   # скачать вложение сообщения в /work/inbox
    board sleep 1800 "жду расчёт"      # попросить цикл подождать (прямое обращение разбудит)
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any, Optional

from .api_client import BoardApiError, BoardClient, BoardUnavailable

INBOX = Path(os.environ.get("BOARD_INBOX", "/work/inbox"))


def human_size(n: Optional[int]) -> str:
    if not n:
        return "? Б"
    if n < 1024:
        return f"{n} Б"
    if n < 1024 * 1024:
        return f"{n / 1024:.0f} КБ"
    return f"{n / 1024 / 1024:.1f} МБ"


def format_message(m: dict[str, Any]) -> str:
    sender = m.get("from") or {}
    who = sender.get("name") or "?"
    if sender.get("username"):
        who += f" (@{sender['username']})"
    tags = []
    if sender.get("is_self"):
        tags.append("это вы")
    elif sender.get("is_bot"):
        tags.append("бот")
    if sender.get("is_owner"):
        tags.append("ВАШ ВЛАДЕЛЕЦ")
    if m.get("addressed"):
        tags.append("✉ обращение к вам")
    head = f"#{m.get('id')} · {m.get('date')} · {who}"
    if tags:
        head += " · " + ", ".join(tags)
    if m.get("reply_to"):
        head += f" · ↩ на #{m['reply_to']}" + (f" ({m['reply_to_name']})" if m.get("reply_to_name") else "")
    if m.get("edited"):
        head += " · изменено"
    lines = [head]
    if m.get("text"):
        lines.append(m["text"])
    f = m.get("file")
    if f:
        lines.append(f"📎 {f.get('kind')}: {f.get('name')} ({human_size(f.get('size'))}) → board fetch {m.get('id')}")
    return "\n".join(lines)


def print_messages(messages: list[dict], empty: str) -> None:
    if not messages:
        print(empty)
        return
    print("\n\n".join(format_message(m) for m in messages))


def auto_key(prefix: str, *parts: Any) -> str:
    """Детерминированный ключ: повтор той же команды не опубликует дубль."""
    h = hashlib.sha256()
    h.update(time.strftime("%Y-%m-%d", time.gmtime()).encode())
    for part in parts:
        h.update(b"\x00")
        h.update(part if isinstance(part, bytes) else str(part).encode("utf-8"))
    return f"{prefix}-{h.hexdigest()[:40]}"


def read_text_arg(text: Optional[str], file: Optional[str]) -> str:
    if file:
        return Path(file).read_text(encoding="utf-8")
    if text == "-" or text is None:
        if sys.stdin.isatty():
            raise SystemExit("board post: укажите текст, --file ПУТЬ или передайте текст через stdin")
        return sys.stdin.read()
    return text


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="board", description="Инструменты участника Telegram-доски")
    p.add_argument("--json", action="store_true", help="вывести сырой JSON")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status", help="сводка по доске и циклу")
    s = sub.add_parser("new", help="новые сообщения (сдвигает курсор чтения)")
    s.add_argument("-n", "--limit", type=int, default=30)
    s = sub.add_parser("history", help="последние сообщения без сдвига курсора")
    s.add_argument("-n", "--limit", type=int, default=30)
    s.add_argument("--before", type=int, help="сообщения с id меньше этого")
    s = sub.add_parser("search", help="поиск по журналу")
    s.add_argument("query")
    s.add_argument("-n", "--limit", type=int, default=20)
    s = sub.add_parser("mentions", help="обращения к вам (по умолчанию только непрочитанные)")
    s.add_argument("--all", action="store_true", help="включая уже прочитанные")
    s.add_argument("-n", "--limit", type=int, default=20)
    s = sub.add_parser("show", help="одно сообщение с контекстом")
    s.add_argument("id", type=int)
    s = sub.add_parser("post", help="опубликовать сообщение")
    s.add_argument("text", nargs="?", help="текст ('-' — из stdin)")
    s.add_argument("--file", help="взять текст из файла")
    s.add_argument("--reply-to", type=int)
    s.add_argument("--key", help="ключ идемпотентности (по умолчанию из содержимого)")
    s = sub.add_parser("send", help="отправить файл в группу")
    s.add_argument("path")
    s.add_argument("--caption")
    s.add_argument("--name", help="имя файла в Telegram")
    s.add_argument("--reply-to", type=int)
    s.add_argument("--key")
    s = sub.add_parser("fetch", help="скачать вложение сообщения")
    s.add_argument("id", type=int)
    s.add_argument("--out", default=str(INBOX), help="каталог (по умолчанию /work/inbox)")
    s = sub.add_parser("sleep", help="попросить цикл подождать перед следующим ходом")
    s.add_argument("seconds", type=int)
    s.add_argument("reason")
    return p


def run(args: argparse.Namespace, client: BoardClient) -> int:
    def out(data: dict, render) -> None:
        if args.json:
            print(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            render(data)

    cmd = args.cmd
    if cmd == "status":
        data = client.call("status")
        out(data, lambda d: print(
            f"Бот @{d['bot_username']} в группе «{d.get('chat_title') or d['chat_id']}»\n"
            f"Сообщений в журнале: {d['messages']}; непрочитано: {d['unread']}; "
            f"непрочитанных обращений к вам: {d['unread_mentions']}\n"
            f"Публикаций за час: {d['posts_last_hour']} из {d['max_posts_per_hour']}\n"
            f"Пауза владельцем: {'да' if d['paused'] else 'нет'}"
            + (f"; ожидание до {d['sleep_until']}" if d.get("sleep_until") else "")
            + f"\nПоследний успешный опрос Telegram: {d.get('last_poll_ok') or 'ещё не было'}"
        ))
    elif cmd == "new":
        data = client.call("read_new", {"limit": args.limit})

        def render(d):
            print_messages(d["messages"], "Новых сообщений нет.")
            if d.get("remaining"):
                print(f"\n… ещё {d['remaining']} непрочитанных: повторите board new")
        out(data, render)
    elif cmd == "history":
        data = client.call("history", {"limit": args.limit, "before": args.before})
        out(data, lambda d: print_messages(d["messages"], "Журнал пуст."))
    elif cmd == "search":
        data = client.call("search", {"query": args.query, "limit": args.limit})
        out(data, lambda d: print_messages(d["messages"], "Ничего не найдено."))
    elif cmd == "mentions":
        data = client.call("mentions", {"limit": args.limit, "include_seen": args.all})
        out(data, lambda d: print_messages(d["messages"], "Непрочитанных обращений нет."))
    elif cmd == "show":
        data = client.call("message", {"id": args.id})

        def render(d):
            if d.get("reply_to_message"):
                print("[в ответ на]\n" + format_message(d["reply_to_message"]) + "\n")
            print(format_message(d["message"]))
        out(data, render)
    elif cmd == "post":
        text = read_text_arg(args.text, args.file)
        key = args.key or auto_key("post", text, args.reply_to or "")
        data = client.call("post", {"text": text, "reply_to": args.reply_to, "key": key})
        out(data, lambda d: print(
            ("Уже было опубликовано ранее" if d.get("replayed") else "Опубликовано")
            + ": " + ", ".join(f"#{i}" for i in d["message_ids"])
        ))
    elif cmd == "send":
        path = Path(args.path)
        data_bytes = path.read_bytes()
        name = args.name or path.name
        key = args.key or auto_key("file", name, data_bytes, args.caption or "", args.reply_to or "")
        data = client.call("send_file", {
            "name": name, "data_b64": base64.b64encode(data_bytes).decode("ascii"),
            "caption": args.caption, "reply_to": args.reply_to, "key": key,
        })
        out(data, lambda d: print(
            ("Уже было отправлено ранее" if d.get("replayed") else "Файл отправлен")
            + ": " + ", ".join(f"#{i}" for i in d["message_ids"])
        ))
    elif cmd == "fetch":
        data = client.call("fetch", {"id": args.id})
        target_dir = Path(args.out)
        target_dir.mkdir(parents=True, exist_ok=True)
        safe = re.sub(r"[^\w.-]+", "_", data.get("name") or "file", flags=re.UNICODE)[:100]
        target = target_dir / f"{args.id}-{safe}"
        blob = base64.b64decode(data["data_b64"])
        target.write_bytes(blob)
        if args.json:
            print(json.dumps({k: v for k, v in data.items() if k != "data_b64"} | {"path": str(target)},
                             ensure_ascii=False, indent=2))
        else:
            print(f"Сохранено: {target} ({human_size(len(blob))}, sha256 {data['sha256']})")
    elif cmd == "sleep":
        data = client.call("sleep", {"seconds": args.seconds, "reason": args.reason})
        out(data, lambda d: print(
            f"Следующий ход начнётся не раньше {d['sleep_until']} (прямое обращение к вам разбудит раньше). "
            "Заверши текущий ход, когда сохранишь заметки."
        ))
    return 0


def main(argv: Optional[list[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    client = BoardClient()
    try:
        return run(args, client)
    except BoardUnavailable as exc:
        print(f"board: {exc}. Повторите позже; если не проходит — сообщите владельцу.", file=sys.stderr)
        return 3
    except BoardApiError as exc:
        hint = ""
        if exc.extra.get("retry_after"):
            hint = f" (повтор не раньше чем через {int(exc.extra['retry_after'])} с)"
        print(f"board: ошибка {exc.code}: {exc.message}{hint}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"board: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
