"""Журнал доски в SQLite: сообщения группы, курсоры чтения, исходящие с ключами идемпотентности.

Журнал содержит только то, что бот реально получил после подключения к группе:
Bot API не отдаёт историю, отправленную раньше.
"""

from __future__ import annotations

import json
import sqlite3
import threading
import time
from pathlib import Path
from typing import Any, Iterable, Optional

SCHEMA = """
CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS messages (
  id INTEGER PRIMARY KEY,
  date INTEGER NOT NULL,
  edit_date INTEGER,
  from_id INTEGER,
  from_name TEXT NOT NULL DEFAULT '',
  from_username TEXT,
  from_is_bot INTEGER NOT NULL DEFAULT 0,
  is_own INTEGER NOT NULL DEFAULT 0,
  is_owner INTEGER NOT NULL DEFAULT 0,
  addressed INTEGER NOT NULL DEFAULT 0,
  is_command INTEGER NOT NULL DEFAULT 0,
  reply_to INTEGER,
  reply_to_name TEXT,
  thread_id INTEGER,
  text TEXT NOT NULL DEFAULT '',
  file_kind TEXT,
  file_id TEXT,
  file_name TEXT,
  file_size INTEGER,
  seen INTEGER NOT NULL DEFAULT 0,
  notified INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS idx_messages_attention ON messages(addressed, seen, notified);
CREATE INDEX IF NOT EXISTS idx_messages_date ON messages(date);
CREATE TABLE IF NOT EXISTS outbox (
  key TEXT PRIMARY KEY,
  kind TEXT NOT NULL,
  created INTEGER NOT NULL,
  status TEXT NOT NULL,
  message_ids TEXT,
  error TEXT
);
"""

COLUMNS = (
    "id", "date", "edit_date", "from_id", "from_name", "from_username", "from_is_bot", "is_own",
    "is_owner", "addressed", "is_command", "reply_to", "reply_to_name", "thread_id", "text",
    "file_kind", "file_id", "file_name", "file_size",
)


def iso(ts: Optional[int]) -> Optional[str]:
    if ts is None:
        return None
    return time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime(ts))


def public_message(row: sqlite3.Row) -> dict[str, Any]:
    """Сообщение в виде, который отдаётся агенту (без file_id и служебных флагов)."""
    file_info = None
    if row["file_kind"]:
        file_info = {"kind": row["file_kind"], "name": row["file_name"], "size": row["file_size"]}
    return {
        "id": row["id"],
        "date": iso(row["date"]),
        "edited": row["edit_date"] is not None,
        "from": {
            "name": row["from_name"],
            "username": row["from_username"],
            "is_bot": bool(row["from_is_bot"]),
            "is_owner": bool(row["is_owner"]),
            "is_self": bool(row["is_own"]),
        },
        "addressed": bool(row["addressed"]),
        "reply_to": row["reply_to"],
        "reply_to_name": row["reply_to_name"],
        "text": row["text"],
        "file": file_info,
    }


class Journal:
    def __init__(self, path: Path | str):
        self.path = Path(path)
        if str(path) != ":memory:":
            self.path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()
        self._db = sqlite3.connect(str(path), check_same_thread=False, isolation_level=None)
        self._db.row_factory = sqlite3.Row
        with self._lock:
            if str(path) != ":memory:":
                self._db.execute("PRAGMA journal_mode=WAL")
            self._db.execute("PRAGMA synchronous=NORMAL")
            self._db.executescript(SCHEMA)

    def close(self) -> None:
        with self._lock:
            self._db.close()

    # ------------------------------------------------------------------ meta
    def meta(self, key: str, default: Optional[str] = None) -> Optional[str]:
        with self._lock:
            row = self._db.execute("SELECT value FROM meta WHERE key=?", (key,)).fetchone()
        return row["value"] if row else default

    def meta_int(self, key: str, default: int = 0) -> int:
        value = self.meta(key)
        try:
            return int(value) if value is not None else default
        except ValueError:
            return default

    def set_meta(self, key: str, value: Any) -> None:
        with self._lock:
            self._db.execute(
                "INSERT INTO meta(key, value) VALUES(?, ?) ON CONFLICT(key) DO UPDATE SET value=excluded.value",
                (key, str(value)),
            )

    def del_meta(self, key: str) -> None:
        with self._lock:
            self._db.execute("DELETE FROM meta WHERE key=?", (key,))

    # -------------------------------------------------------------- messages
    def store(self, row: dict[str, Any]) -> None:
        """Сохранить новое сообщение; повтор того же id обновляет содержимое, но не флаги чтения."""
        values = [row.get(col) for col in COLUMNS]
        updates = ", ".join(f"{col}=excluded.{col}" for col in COLUMNS if col != "id")
        with self._lock:
            self._db.execute(
                f"INSERT INTO messages({', '.join(COLUMNS)}) VALUES({', '.join('?' * len(COLUMNS))}) "
                f"ON CONFLICT(id) DO UPDATE SET {updates}",
                values,
            )

    def store_edit(self, message_id: int, text: str, edit_date: int) -> bool:
        with self._lock:
            cur = self._db.execute(
                "UPDATE messages SET text=?, edit_date=? WHERE id=?", (text, edit_date, message_id)
            )
        return cur.rowcount > 0

    def get(self, message_id: int) -> Optional[sqlite3.Row]:
        with self._lock:
            return self._db.execute("SELECT * FROM messages WHERE id=?", (message_id,)).fetchone()

    def latest_id(self) -> int:
        with self._lock:
            row = self._db.execute("SELECT MAX(id) AS m FROM messages").fetchone()
        return int(row["m"] or 0)

    def count(self) -> int:
        with self._lock:
            return int(self._db.execute("SELECT COUNT(*) AS c FROM messages").fetchone()["c"])

    def unread_counts(self) -> tuple[int, int]:
        cursor = self.meta_int("read_cursor")
        with self._lock:
            unread = self._db.execute(
                "SELECT COUNT(*) AS c FROM messages WHERE id>? AND is_own=0 AND is_command=0", (cursor,)
            ).fetchone()["c"]
            mentions = self._db.execute(
                "SELECT COUNT(*) AS c FROM messages WHERE addressed=1 AND seen=0 AND is_own=0"
            ).fetchone()["c"]
        return int(unread), int(mentions)

    def _mark_seen(self, ids: Iterable[int]) -> None:
        ids = list(ids)
        if ids:
            with self._lock:
                self._db.executemany("UPDATE messages SET seen=1, notified=1 WHERE id=?", [(i,) for i in ids])

    def read_new(self, limit: int) -> tuple[list[sqlite3.Row], int]:
        """Новые сообщения после курсора чтения агента; курсор сдвигается на прочитанное."""
        with self._lock:
            cursor = self.meta_int("read_cursor")
            rows = self._db.execute(
                "SELECT * FROM messages WHERE id>? AND is_own=0 AND is_command=0 ORDER BY id LIMIT ?",
                (cursor, limit),
            ).fetchall()
            if rows:
                self.set_meta("read_cursor", rows[-1]["id"])
                self._mark_seen(r["id"] for r in rows if r["addressed"])
            remaining = self._db.execute(
                "SELECT COUNT(*) AS c FROM messages WHERE id>? AND is_own=0 AND is_command=0",
                (rows[-1]["id"] if rows else cursor,),
            ).fetchone()["c"]
        return rows, int(remaining)

    def history(self, before: Optional[int], limit: int) -> list[sqlite3.Row]:
        with self._lock:
            if before:
                rows = self._db.execute(
                    "SELECT * FROM messages WHERE id<? AND is_command=0 ORDER BY id DESC LIMIT ?", (before, limit)
                ).fetchall()
            else:
                rows = self._db.execute(
                    "SELECT * FROM messages WHERE is_command=0 ORDER BY id DESC LIMIT ?", (limit,)
                ).fetchall()
        return list(reversed(rows))

    def search(self, query: str, limit: int, scan: int = 20000) -> list[sqlite3.Row]:
        needle = query.casefold()
        with self._lock:
            rows = self._db.execute(
                "SELECT * FROM messages WHERE is_command=0 ORDER BY id DESC LIMIT ?", (scan,)
            ).fetchall()
        found = [
            r for r in rows
            if needle in (r["text"] or "").casefold()
            or needle in (r["file_name"] or "").casefold()
            or needle in (r["from_name"] or "").casefold()
            or needle in (r["from_username"] or "").casefold()
        ]
        return list(reversed(found[:limit]))

    def mentions(self, limit: int, include_seen: bool = False) -> list[sqlite3.Row]:
        with self._lock:
            if include_seen:
                rows = self._db.execute(
                    "SELECT * FROM messages WHERE addressed=1 AND is_own=0 ORDER BY id DESC LIMIT ?", (limit,)
                ).fetchall()
                rows = list(reversed(rows))
            else:
                rows = self._db.execute(
                    "SELECT * FROM messages WHERE addressed=1 AND seen=0 AND is_own=0 ORDER BY id LIMIT ?", (limit,)
                ).fetchall()
            self._mark_seen(r["id"] for r in rows)
        return rows

    def take_notifications(self, limit: int) -> tuple[list[sqlite3.Row], int]:
        """Непоказанные обращения для хука: помечаются показанными (но не прочитанными)."""
        with self._lock:
            rows = self._db.execute(
                "SELECT * FROM messages WHERE addressed=1 AND seen=0 AND notified=0 AND is_own=0 ORDER BY id",
            ).fetchall()
            if rows:
                self._db.executemany("UPDATE messages SET notified=1 WHERE id=?", [(r["id"],) for r in rows])
        return rows[:limit], len(rows)

    def take_digest(self, now: int, interval: int) -> Optional[dict[str, Any]]:
        """Сводка обычных сообщений не чаще раза в ``interval`` секунд (для хука)."""
        with self._lock:
            last_at = self.meta_int("digest_at")
            if last_at and now - last_at < interval:
                return None
            start = max(self.meta_int("read_cursor"), self.meta_int("digest_cursor"))
            rows = self._db.execute(
                "SELECT id, from_name, from_username FROM messages "
                "WHERE id>? AND is_own=0 AND is_command=0 AND addressed=0 ORDER BY id",
                (start,),
            ).fetchall()
            if not rows:
                return None
            self.set_meta("digest_at", now)
            self.set_meta("digest_cursor", rows[-1]["id"])
        authors: list[str] = []
        for r in rows:
            name = f"@{r['from_username']}" if r["from_username"] else r["from_name"]
            if name and name not in authors:
                authors.append(name)
        return {"count": len(rows), "authors": authors[:8]}

    def since_id(self, last_id: int) -> list[sqlite3.Row]:
        with self._lock:
            return self._db.execute(
                "SELECT * FROM messages WHERE id>? AND is_command=0 ORDER BY id", (last_id,)
            ).fetchall()

    def between(self, ts_from: int, ts_to: int) -> list[sqlite3.Row]:
        with self._lock:
            return self._db.execute(
                "SELECT * FROM messages WHERE date>=? AND date<? AND is_command=0 ORDER BY id", (ts_from, ts_to)
            ).fetchall()

    # ---------------------------------------------------------------- outbox
    def outbox_get(self, key: str) -> Optional[sqlite3.Row]:
        with self._lock:
            return self._db.execute("SELECT * FROM outbox WHERE key=?", (key,)).fetchone()

    def outbox_begin(self, key: str, kind: str, now: int) -> None:
        with self._lock:
            self._db.execute(
                "INSERT INTO outbox(key, kind, created, status) VALUES(?, ?, ?, 'pending') "
                "ON CONFLICT(key) DO UPDATE SET status='pending', created=excluded.created, error=NULL",
                (key, kind, now),
            )

    def outbox_finish(self, key: str, status: str, message_ids: Optional[list[int]] = None,
                      error: Optional[str] = None) -> None:
        with self._lock:
            self._db.execute(
                "UPDATE outbox SET status=?, message_ids=?, error=? WHERE key=?",
                (status, json.dumps(message_ids or []), error, key),
            )

    def posts_since(self, ts: int) -> int:
        with self._lock:
            row = self._db.execute(
                "SELECT COUNT(*) AS c FROM outbox WHERE created>=? AND status IN ('sent', 'pending')", (ts,)
            ).fetchone()
        return int(row["c"])

    def oldest_post_since(self, ts: int) -> Optional[int]:
        with self._lock:
            row = self._db.execute(
                "SELECT MIN(created) AS m FROM outbox WHERE created>=? AND status IN ('sent', 'pending')", (ts,)
            ).fetchone()
        return int(row["m"]) if row and row["m"] is not None else None
