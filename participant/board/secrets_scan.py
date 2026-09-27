"""Грубая проверка исходящего текста и файлов на похожие на секреты строки.

Это страховка от случайной публикации, а не граница безопасности: преобразованный
секрет (закодированный, разбитый на части) такая проверка не поймает.
"""

from __future__ import annotations

import re
from typing import Iterable, Optional

PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("токен Telegram-бота", re.compile(r"\b\d{8,10}:[A-Za-z0-9_-]{35}\b")),
    ("ключ или токен Anthropic", re.compile(r"sk-ant-[A-Za-z0-9_-]{20,}")),
    ("токен GitHub", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{40,})")),
    ("закрытый ключ", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("ключ AWS", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("ключ OpenAI", re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{32,}")),
)


def find_secret(text: str, extra_exact: Iterable[str] = ()) -> Optional[str]:
    """Название найденного типа секрета или None."""
    for exact in extra_exact:
        if exact and exact in text:
            return "известный секрет этой установки"
    for name, pattern in PATTERNS:
        if pattern.search(text):
            return name
    return None


def find_secret_bytes(data: bytes, extra_exact: Iterable[str] = ()) -> Optional[str]:
    return find_secret(data.decode("utf-8", errors="ignore"), extra_exact)
