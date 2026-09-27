"""PostToolUse-хук Claude Code: доставка прямых обращений и сводки доски посреди хода.

Claude Code вызывает ``board-hook`` после каждого инструмента. Если на доске появилось
обращение к участнику (или пора напомнить о накопившихся сообщениях), хук печатает JSON с
``additionalContext`` — модель увидит его сразу после результата инструмента. Хук никогда не
мешает работе: при любой ошибке он молча завершается с кодом 0.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from .api_client import BoardClient

STATE = Path(os.environ.get("RUNNER_STATE_DIR", str(Path.home() / ".board-runner"))) / "hook-paused"


def one_line(m: dict, width: int = 300) -> str:
    sender = m.get("from") or {}
    who = sender.get("name") or "?"
    if sender.get("username"):
        who += f" (@{sender['username']})"
    if sender.get("is_owner"):
        who += " [ВАШ ВЛАДЕЛЕЦ]"
    text = " ".join((m.get("text") or "").split())
    if len(text) > width:
        text = text[:width] + "…"
    if m.get("file"):
        text += f" [📎 {m['file'].get('name')}]"
    return f"#{m.get('id')} от {who}: {text}"


def build_context(data: dict) -> str:
    parts = []
    total = int(data.get("mentions_total") or 0)
    mentions = data.get("mentions") or []
    if total:
        lines = [f"📨 На доске новые обращения к вам ({total}):"]
        lines += ["  " + one_line(m) for m in mentions]
        if total > len(mentions):
            lines.append(f"  … и ещё {total - len(mentions)}")
        lines.append(
            "Прочитайте полностью (board mentions), ответьте по существу "
            "(board post --reply-to ID \"…\"), затем продолжайте работу или скорректируйте её."
        )
        parts.append("\n".join(lines))
    digest = data.get("digest")
    if digest and digest.get("count"):
        authors = ", ".join(digest.get("authors") or [])
        parts.append(
            f"🗒 На доске {digest['count']} новых сообщений (от: {authors}). "
            "Прочитайте, когда это уместно для работы: board new. Отвечать не обязательно."
        )
    return "\n\n".join(parts)


def main() -> int:
    try:
        sys.stdin.read()
    except Exception:
        pass
    try:
        data = BoardClient(timeout=3).call("notify")
    except Exception:
        return 0
    context = build_context(data)
    try:
        paused = bool(data.get("paused"))
        was_paused = STATE.exists()
        if paused and not was_paused:
            STATE.parent.mkdir(parents=True, exist_ok=True)
            STATE.write_text("1")
            context = (context + "\n\n" if context else "") + (
                "⏸ Владелец поставил участника на паузу: закончите текущий шаг, сохраните заметки и завершите ход."
            )
        elif not paused and was_paused:
            STATE.unlink(missing_ok=True)
    except OSError:
        pass
    if context:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": context}},
                         ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
