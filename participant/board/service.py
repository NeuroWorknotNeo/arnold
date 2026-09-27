"""Логика транспорта: разбор обновлений Telegram, команды владельца и операции для агента.

Операции вызываются через Unix-сокет (см. ``transport.py``) и отдают JSON. Модель здесь не
запускается: транспорт только журналирует доску и публикует то, что решил отправить агент.
"""

from __future__ import annotations

import base64
import hashlib
import json
import logging
import re
import threading
import time
from pathlib import Path
from typing import Any, Callable, Optional

from .config import TransportConfig
from .journal import Journal, iso, public_message
from .secrets_scan import find_secret, find_secret_bytes
from .telegram_api import TelegramAPI, TelegramError

log = logging.getLogger("board.transport")

TEXT_LIMIT = 4000          # Telegram режет сообщения на 4096 символах; оставляем запас
MAX_POST_CHARS = 16000     # один вызов post — не больше четырёх сообщений
MAX_FILE_BYTES = 20 * 1024 * 1024
MAX_CAPTION = 1024
OWNER_COMMANDS = {"pause", "resume", "status", "start", "help"}
ALLOWED_UPDATES = ["message", "edited_message", "my_chat_member"]
FILENAME_RE = re.compile(r"^[^/\\\x00-\x1f]{1,120}$")


class ApiError(Exception):
    def __init__(self, status: int, code: str, message: str, **extra: Any):
        super().__init__(message)
        self.status = status
        self.code = code
        self.message = message
        self.extra = extra

    def payload(self) -> dict[str, Any]:
        return {"error": {"code": self.code, "message": self.message, **self.extra}}


def utf16_slice(text: str, offset: int, length: int) -> str:
    """Срез по смещениям в единицах UTF-16 (так Telegram задаёт entities)."""
    raw = text.encode("utf-16-le")
    return raw[2 * offset: 2 * (offset + length)].decode("utf-16-le", errors="ignore")


def split_text(text: str, limit: int = TEXT_LIMIT) -> list[str]:
    """Режет текст на части не длиннее limit, по возможности по абзацам и строкам."""
    text = text.strip()
    chunks: list[str] = []
    while len(text) > limit:
        cut = text.rfind("\n\n", 0, limit)
        if cut < limit // 3:
            cut = text.rfind("\n", 0, limit)
        if cut < limit // 3:
            cut = text.rfind(" ", 0, limit)
        if cut < limit // 3:
            cut = limit
        chunks.append(text[:cut].rstrip())
        text = text[cut:].lstrip()
    if text:
        chunks.append(text)
    return chunks


def sender_name(user: Optional[dict], sender_chat: Optional[dict] = None) -> tuple[Optional[int], str, Optional[str], bool]:
    if sender_chat:
        return sender_chat.get("id"), sender_chat.get("title") or "анонимно", sender_chat.get("username"), False
    if not user:
        return None, "неизвестно", None, False
    name = " ".join(p for p in (user.get("first_name"), user.get("last_name")) if p) or user.get("username") or str(user.get("id"))
    return user.get("id"), name, user.get("username"), bool(user.get("is_bot"))


def file_of(msg: dict) -> tuple[Optional[str], Optional[str], Optional[str], Optional[int]]:
    """(вид, file_id, имя, размер) вложения сообщения."""
    if msg.get("document"):
        d = msg["document"]
        return "document", d.get("file_id"), d.get("file_name") or "document", d.get("file_size")
    if msg.get("photo"):
        p = max(msg["photo"], key=lambda s: (s.get("file_size") or 0, s.get("width", 0) * s.get("height", 0)))
        return "photo", p.get("file_id"), f"photo-{msg.get('message_id')}.jpg", p.get("file_size")
    for kind in ("video", "audio", "voice", "animation", "video_note"):
        if msg.get(kind):
            f = msg[kind]
            return kind, f.get("file_id"), f.get("file_name") or f"{kind}-{msg.get('message_id')}", f.get("file_size")
    return None, None, None, None


class BoardService:
    def __init__(self, cfg: TransportConfig, journal: Journal, api: TelegramAPI,
                 clock: Callable[[], float] = time.time, sleep: Callable[[float], None] = time.sleep):
        self.cfg = cfg
        self.journal = journal
        self.api = api
        self.clock = clock
        self.sleep = sleep
        self.bot_id: Optional[int] = None
        self.bot_username: str = ""
        self._send_lock = threading.Lock()
        self._foreign_chats: set[int] = set()
        self.routes: dict[str, Callable[[dict], dict]] = {
            "/status": self.op_status,
            "/read_new": self.op_read_new,
            "/history": self.op_history,
            "/search": self.op_search,
            "/mentions": self.op_mentions,
            "/message": self.op_message,
            "/post": self.op_post,
            "/send_file": self.op_send_file,
            "/fetch": self.op_fetch,
            "/notify": self.op_notify,
            "/control": self.op_control,
            "/sleep": self.op_sleep,
            "/wake": self.op_wake,
            "/heartbeat": self.op_heartbeat,
            "/notify_owner": self.op_notify_owner,
        }

    # ---------------------------------------------------------------- identity
    def now(self) -> int:
        return int(self.clock())

    def init_identity(self) -> dict:
        me = self.api.get_me()
        self.bot_id = int(me["id"])
        self.bot_username = me.get("username") or ""
        self.journal.set_meta("bot_id", self.bot_id)
        self.journal.set_meta("bot_username", self.bot_username)
        try:
            chat = self.api.get_chat(self.cfg.chat_id)
            title = chat.get("title") or ""
            self.journal.set_meta("chat_title", title)
            log.info("Бот @%s подключён к доске %s «%s»", self.bot_username, self.cfg.chat_id, title)
        except TelegramError as exc:
            log.warning(
                "Бот @%s не видит группу %s (%s). Добавьте бота в группу и проверьте BOARD_CHAT_ID.",
                self.bot_username, self.cfg.chat_id, exc.description,
            )
        return me

    # ----------------------------------------------------------------- updates
    def poll_once(self) -> int:
        offset = self.journal.meta_int("update_offset")
        updates = self.api.get_updates(offset, self.cfg.poll_timeout, ALLOWED_UPDATES)
        for update in updates:
            try:
                self.handle_update(update)
            except Exception:  # одно странное обновление не должно останавливать доску
                log.exception("Не удалось обработать обновление %s", update.get("update_id"))
            self.journal.set_meta("update_offset", int(update["update_id"]) + 1)
        self.journal.set_meta("last_poll_ok", self.now())
        return len(updates)

    def handle_update(self, update: dict) -> None:
        if "message" in update:
            self._on_message(update["message"], edited=False)
        elif "edited_message" in update:
            self._on_message(update["edited_message"], edited=True)
        elif "my_chat_member" in update:
            m = update["my_chat_member"]
            chat = m.get("chat") or {}
            status = (m.get("new_chat_member") or {}).get("status")
            log.info("Статус бота в чате %s «%s»: %s", chat.get("id"), chat.get("title"), status)

    def _on_message(self, msg: dict, edited: bool) -> None:
        chat = msg.get("chat") or {}
        chat_id = chat.get("id")
        if msg.get("migrate_to_chat_id") and chat_id == self.cfg.chat_id:
            log.error(
                "Группа стала супергруппой, её новый ID %s. Замените BOARD_CHAT_ID и перезапустите участника.",
                msg["migrate_to_chat_id"],
            )
            return
        if chat.get("type") == "private":
            self._on_private(msg)
            return
        if chat_id != self.cfg.chat_id:
            if chat_id not in self._foreign_chats:
                self._foreign_chats.add(chat_id)
                log.warning(
                    "Сообщение из чужого чата %s «%s» (%s) — игнорирую. Если это ваша доска, укажите BOARD_CHAT_ID=%s.",
                    chat_id, chat.get("title"), chat.get("type"), chat_id,
                )
            return
        text = msg.get("text") or msg.get("caption") or ""
        if edited:
            if not self.journal.store_edit(int(msg["message_id"]), text, int(msg.get("edit_date") or self.now())):
                self.journal.store(self._row(msg))
            return
        command = self._owner_command(msg)
        row = self._row(msg)
        if command:
            row["is_command"] = 1
            row["addressed"] = 0
            self.journal.store(row)
            self._run_owner_command(command, chat_id, int(msg["message_id"]))
            return
        self.journal.store(row)

    def _row(self, msg: dict) -> dict[str, Any]:
        from_id, name, username, is_bot = sender_name(msg.get("from"), msg.get("sender_chat"))
        own = self.bot_id is not None and from_id == self.bot_id
        reply = msg.get("reply_to_message") or {}
        reply_name = None
        if reply:
            _, reply_name, reply_username, _ = sender_name(reply.get("from"), reply.get("sender_chat"))
            if reply_username:
                reply_name = f"@{reply_username}"
        kind, file_id, file_name, file_size = file_of(msg)
        return {
            "id": int(msg["message_id"]),
            "date": int(msg.get("date") or self.now()),
            "edit_date": msg.get("edit_date"),
            "from_id": from_id,
            "from_name": name,
            "from_username": username,
            "from_is_bot": 1 if is_bot else 0,
            "is_own": 1 if own else 0,
            "is_owner": 1 if (from_id in self.cfg.owner_ids and not msg.get("sender_chat")) else 0,
            "addressed": 1 if (not own and self._is_addressed(msg)) else 0,
            "is_command": 0,
            "reply_to": reply.get("message_id") if reply else None,
            "reply_to_name": reply_name,
            "thread_id": msg.get("message_thread_id"),
            "text": msg.get("text") or msg.get("caption") or "",
            "file_kind": kind,
            "file_id": file_id,
            "file_name": file_name,
            "file_size": file_size,
        }

    def _is_addressed(self, msg: dict) -> bool:
        reply = msg.get("reply_to_message") or {}
        if reply and self.bot_id is not None and (reply.get("from") or {}).get("id") == self.bot_id:
            return True
        if not self.bot_username:
            return False
        text = msg.get("text") or msg.get("caption") or ""
        handle = "@" + self.bot_username.lower()
        for ent in msg.get("entities") or msg.get("caption_entities") or []:
            kind = ent.get("type")
            if kind == "text_mention" and (ent.get("user") or {}).get("id") == self.bot_id:
                return True
            if kind in {"mention", "bot_command"}:
                piece = utf16_slice(text, int(ent.get("offset", 0)), int(ent.get("length", 0))).lower()
                if piece == handle or (kind == "bot_command" and piece.endswith(handle)):
                    return True
        return re.search(re.escape(handle) + r"(?![A-Za-z0-9_])", text.lower()) is not None

    def _owner_command(self, msg: dict) -> Optional[str]:
        user = msg.get("from") or {}
        if user.get("id") not in self.cfg.owner_ids or msg.get("sender_chat"):
            return None
        text = (msg.get("text") or "").strip()
        m = re.match(r"^/([a-z_]+)(@[A-Za-z0-9_]+)?(?:\s|$)", text)
        if not m or m.group(1) not in OWNER_COMMANDS:
            return None
        target = m.group(2)
        if (msg.get("chat") or {}).get("type") != "private":
            # В группе команда без @имени адресована всем ботам — выполняем только явно нашу.
            if not target or target[1:].lower() != self.bot_username.lower():
                return None
        return m.group(1)

    def _on_private(self, msg: dict) -> None:
        chat_id = (msg.get("chat") or {}).get("id")
        user_id = (msg.get("from") or {}).get("id")
        if user_id not in self.cfg.owner_ids:
            return  # чужим личкам не отвечаем: бот не принимает задания в обход доски
        command = self._owner_command(msg)
        if command:
            self._run_owner_command(command, chat_id, None)
        else:
            self._safe_send(chat_id, "Я участник доски. В личке понимаю /pause, /resume, /status. "
                                     "Вопросы по задаче пишите в группе, упомянув меня.")

    def _run_owner_command(self, command: str, chat_id: int, reply_to: Optional[int]) -> None:
        if command == "pause":
            self.journal.set_meta("paused", 1)
            text = "⏸ Пауза: новые ходы не начинаются (текущий доработает). Продолжить — /resume."
        elif command == "resume":
            self.journal.set_meta("paused", 0)
            self.journal.del_meta("sleep_until")
            text = "▶️ Продолжаю работу."
        else:
            text = self.status_text()
        log.info("Команда владельца: /%s", command)
        self._safe_send(chat_id, text, reply_to)

    def status_text(self) -> str:
        unread, mentions = self.journal.unread_counts()
        paused = self.journal.meta_int("paused") == 1
        parts = [f"Участник @{self.bot_username}: {'⏸ на паузе' if paused else '▶️ работает'}"]
        sleep_until = self.journal.meta_int("sleep_until")
        if sleep_until and sleep_until > self.now():
            parts.append(f"ждёт до {iso(sleep_until)}: {self.journal.meta('sleep_reason') or ''}".strip())
        parts.append(f"журнал: {self.journal.count()} сообщ., непрочитано {unread}, обращений {mentions}")
        runner = self.journal.meta("runner_status")
        if runner:
            try:
                info = json.loads(runner)
                seen = int(info.get("at") or 0)
                age = self.now() - seen
                line = f"цикл: {info.get('state', '?')}, ходов {info.get('turns', 0)}"
                if info.get("last_error"):
                    line += f", последняя ошибка: {str(info['last_error'])[:120]}"
                if age > 900:
                    line += f" (данные {age // 60} мин назад — проверьте контейнер agent)"
                parts.append(line)
            except ValueError:
                pass
        else:
            parts.append("цикл агента ещё не выходил на связь")
        return "\n".join(parts)

    def _safe_send(self, chat_id: int, text: str, reply_to: Optional[int] = None) -> None:
        try:
            with self._send_lock:
                self.api.send_message(chat_id, text[:TEXT_LIMIT], reply_to)
        except TelegramError as exc:
            log.warning("Не удалось отправить служебный ответ: %s", exc)

    # ------------------------------------------------------------- operations
    def dispatch(self, path: str, payload: dict) -> tuple[int, dict]:
        handler = self.routes.get(path)
        if handler is None:
            return 404, {"error": {"code": "not_found", "message": f"нет операции {path}"}}
        try:
            return 200, handler(payload if isinstance(payload, dict) else {})
        except ApiError as exc:
            return exc.status, exc.payload()
        except TelegramError as exc:
            return 502, {"error": {"code": "telegram", "message": str(exc), "retry_after": exc.retry_after}}

    @staticmethod
    def _limit(payload: dict, default: int, hi: int) -> int:
        try:
            value = int(payload.get("limit", default))
        except (TypeError, ValueError):
            raise ApiError(400, "bad_request", "limit должно быть числом") from None
        return max(1, min(hi, value))

    def op_status(self, payload: dict) -> dict:
        unread, mentions = self.journal.unread_counts()
        return {
            "bot_username": self.bot_username,
            "chat_id": self.cfg.chat_id,
            "chat_title": self.journal.meta("chat_title"),
            "messages": self.journal.count(),
            "unread": unread,
            "unread_mentions": mentions,
            "paused": self.journal.meta_int("paused") == 1,
            "sleep_until": iso(self.journal.meta_int("sleep_until") or None),
            "last_poll_ok": iso(self.journal.meta_int("last_poll_ok") or None),
            "posts_last_hour": self.journal.posts_since(self.now() - 3600),
            "max_posts_per_hour": self.cfg.max_posts_per_hour,
            "owner_ids": sorted(self.cfg.owner_ids),
            "now": iso(self.now()),
        }

    def op_read_new(self, payload: dict) -> dict:
        rows, remaining = self.journal.read_new(self._limit(payload, 30, 100))
        return {"messages": [public_message(r) for r in rows], "remaining": remaining}

    def op_history(self, payload: dict) -> dict:
        before = payload.get("before")
        rows = self.journal.history(int(before) if before else None, self._limit(payload, 30, 200))
        return {"messages": [public_message(r) for r in rows]}

    def op_search(self, payload: dict) -> dict:
        query = str(payload.get("query") or "").strip()
        if len(query) < 2:
            raise ApiError(400, "bad_request", "строка поиска короче двух символов")
        rows = self.journal.search(query, self._limit(payload, 20, 100))
        return {"messages": [public_message(r) for r in rows]}

    def op_mentions(self, payload: dict) -> dict:
        rows = self.journal.mentions(self._limit(payload, 20, 100), bool(payload.get("include_seen")))
        return {"messages": [public_message(r) for r in rows]}

    def op_message(self, payload: dict) -> dict:
        row = self._require_message(payload)
        result = {"message": public_message(row)}
        if row["reply_to"]:
            parent = self.journal.get(int(row["reply_to"]))
            if parent is not None:
                result["reply_to_message"] = public_message(parent)
        return result

    def _require_message(self, payload: dict):
        try:
            message_id = int(payload.get("id"))
        except (TypeError, ValueError):
            raise ApiError(400, "bad_request", "нужен числовой id сообщения") from None
        row = self.journal.get(message_id)
        if row is None:
            raise ApiError(404, "not_found", f"сообщения #{message_id} нет в журнале")
        return row

    def _check_rate(self) -> None:
        now = self.now()
        used = self.journal.posts_since(now - 3600)
        if used >= self.cfg.max_posts_per_hour:
            oldest = self.journal.oldest_post_since(now - 3600) or now
            retry = max(60, oldest + 3600 - now)
            raise ApiError(429, "rate_limited",
                           f"лимит {self.cfg.max_posts_per_hour} публикаций в час исчерпан; "
                           f"следующая возможна через {retry // 60 + 1} мин",
                           retry_after=retry)

    def _idempotent(self, key: Any, kind: str) -> tuple[str, Optional[dict]]:
        if not isinstance(key, str) or not re.match(r"^[A-Za-z0-9_.:-]{8,120}$", key):
            raise ApiError(400, "bad_request", "нужен ключ идемпотентности key (8–120 символов)")
        prev = self.journal.outbox_get(key)
        if prev is not None:
            if prev["kind"] != kind:
                raise ApiError(409, "key_reused", "этот key уже использован для другой операции")
            if prev["status"] == "sent":
                return key, {"message_ids": json.loads(prev["message_ids"] or "[]"), "replayed": True}
            if prev["status"] == "pending":
                raise ApiError(409, "uncertain",
                               "предыдущая отправка с этим key не подтвердилась; проверьте доску (board history), "
                               "прежде чем отправлять снова с новым key")
        return key, None

    def _record_own(self, sent: dict) -> None:
        if not isinstance(sent, dict) or "message_id" not in sent:
            return
        row = self._row(sent)
        row["is_own"] = 1
        row["addressed"] = 0
        self.journal.store(row)

    def _telegram_retry(self, fn: Callable[[], dict]) -> dict:
        try:
            return fn()
        except TelegramError as exc:
            if exc.code == 429 and exc.retry_after and exc.retry_after <= 60:
                self.sleep(exc.retry_after + 1)
                return fn()
            raise

    def op_post(self, payload: dict) -> dict:
        text = payload.get("text")
        if not isinstance(text, str) or not text.strip():
            raise ApiError(400, "bad_request", "пустой текст")
        if len(text) > MAX_POST_CHARS:
            raise ApiError(400, "too_long", f"текст длиннее {MAX_POST_CHARS} символов: опубликуйте его файлом (board send)")
        secret = find_secret(text, [self.cfg.token])
        if secret:
            raise ApiError(400, "secret_detected", f"в тексте похоже есть секрет ({secret}); публикация отклонена")
        reply_to = payload.get("reply_to")
        reply_to = int(reply_to) if reply_to else None
        key, replay = self._idempotent(payload.get("key"), "post")
        if replay:
            return replay
        self._check_rate()
        chunks = split_text(text)
        self.journal.outbox_begin(key, "post", self.now())
        ids: list[int] = []
        try:
            with self._send_lock:
                for i, chunk in enumerate(chunks):
                    sent = self._telegram_retry(
                        lambda c=chunk, r=(reply_to if i == 0 else None): self.api.send_message(self.cfg.chat_id, c, r)
                    )
                    self._record_own(sent)
                    ids.append(int(sent["message_id"]))
        except TelegramError as exc:
            if ids or exc.is_network:
                # Часть ушла или ответ потерян: повтор может задублировать — оставляем pending.
                self.journal.outbox_finish(key, "pending", ids, str(exc))
                raise ApiError(502, "uncertain", f"отправка не подтверждена: {exc.description}", message_ids=ids) from None
            self.journal.outbox_finish(key, "failed", ids, str(exc))
            raise
        self.journal.outbox_finish(key, "sent", ids)
        return {"message_ids": ids, "replayed": False}

    def op_send_file(self, payload: dict) -> dict:
        name = payload.get("name")
        if not isinstance(name, str) or not FILENAME_RE.match(name) or name in {".", ".."}:
            raise ApiError(400, "bad_request", "недопустимое имя файла")
        try:
            data = base64.b64decode(payload.get("data_b64") or "", validate=True)
        except (ValueError, TypeError):
            raise ApiError(400, "bad_request", "data_b64 не в base64") from None
        if not data:
            raise ApiError(400, "bad_request", "пустой файл")
        if len(data) > MAX_FILE_BYTES:
            raise ApiError(400, "too_large", "файл больше 20 МБ")
        caption = payload.get("caption") or None
        if caption is not None and (not isinstance(caption, str) or len(caption) > MAX_CAPTION):
            raise ApiError(400, "bad_request", f"подпись длиннее {MAX_CAPTION} символов")
        secret = find_secret_bytes(data, [self.cfg.token]) or (find_secret(caption, [self.cfg.token]) if caption else None)
        if secret or re.search(r"(^|[._-])(env|credentials?|secrets?|id_rsa|id_ed25519)([._-]|$)", name.lower()):
            raise ApiError(400, "secret_detected", f"файл похож на секрет ({secret or 'имя файла'}); публикация отклонена")
        reply_to = payload.get("reply_to")
        reply_to = int(reply_to) if reply_to else None
        key, replay = self._idempotent(payload.get("key"), "file")
        if replay:
            return replay
        self._check_rate()
        self.journal.outbox_begin(key, "file", self.now())
        try:
            with self._send_lock:
                sent = self._telegram_retry(
                    lambda: self.api.send_document(self.cfg.chat_id, name, data, caption, reply_to)
                )
        except TelegramError as exc:
            status = "pending" if exc.is_network else "failed"
            self.journal.outbox_finish(key, status, [], str(exc))
            if exc.is_network:
                raise ApiError(502, "uncertain", f"отправка файла не подтверждена: {exc.description}") from None
            raise
        self._record_own(sent)
        self.journal.outbox_finish(key, "sent", [int(sent["message_id"])])
        return {"message_ids": [int(sent["message_id"])], "sha256": hashlib.sha256(data).hexdigest(),
                "replayed": False}

    def cached_file(self, row) -> Optional[Path]:
        if not row["file_id"]:
            return None
        safe = re.sub(r"[^A-Za-z0-9._-]+", "_", row["file_name"] or "file")[:100]
        return self.cfg.files_dir / f"{row['id']}-{safe}"

    def download(self, row, max_bytes: int = MAX_FILE_BYTES) -> bytes:
        path = self.cached_file(row)
        if path is None:
            raise ApiError(404, "no_file", f"у сообщения #{row['id']} нет вложения")
        if path.exists():
            return path.read_bytes()
        data = self.api.download_file(row["file_id"], max_bytes)
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(path.suffix + ".part")
        tmp.write_bytes(data)
        tmp.replace(path)
        return data

    def op_fetch(self, payload: dict) -> dict:
        row = self._require_message(payload)
        data = self.download(row)
        return {
            "name": row["file_name"],
            "size": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
            "data_b64": base64.b64encode(data).decode("ascii"),
        }

    def op_notify(self, payload: dict) -> dict:
        rows, total = self.journal.take_notifications(5)
        digest = self.journal.take_digest(self.now(), self.cfg.digest_interval)
        return {
            "mentions": [public_message(r) for r in rows],
            "mentions_total": total,
            "digest": digest,
            "paused": self.journal.meta_int("paused") == 1,
        }

    def op_control(self, payload: dict) -> dict:
        unread, mentions = self.journal.unread_counts()
        sleep_until = self.journal.meta_int("sleep_until")
        return {
            "paused": self.journal.meta_int("paused") == 1,
            "sleep_until": sleep_until or None,
            "sleep_reason": self.journal.meta("sleep_reason"),
            "unread": unread,
            "unread_mentions": mentions,
            "now": self.now(),
        }

    def op_sleep(self, payload: dict) -> dict:
        try:
            seconds = int(payload.get("seconds"))
        except (TypeError, ValueError):
            raise ApiError(400, "bad_request", "seconds должно быть числом") from None
        seconds = max(60, min(86400, seconds))
        reason = str(payload.get("reason") or "").strip()[:300]
        if not reason:
            raise ApiError(400, "bad_request", "укажите причину ожидания")
        until = self.now() + seconds
        self.journal.set_meta("sleep_until", until)
        self.journal.set_meta("sleep_reason", reason)
        return {"sleep_until": iso(until), "seconds": seconds}

    def op_wake(self, payload: dict) -> dict:
        self.journal.del_meta("sleep_until")
        self.journal.del_meta("sleep_reason")
        return {"ok": True}

    def op_heartbeat(self, payload: dict) -> dict:
        info = {k: payload.get(k) for k in ("state", "turns", "session", "last_error", "next_turn_at")}
        info["at"] = self.now()
        self.journal.set_meta("runner_status", json.dumps(info, ensure_ascii=False))
        return {"ok": True}

    def op_notify_owner(self, payload: dict) -> dict:
        text = str(payload.get("text") or "").strip()
        if not text:
            raise ApiError(400, "bad_request", "пустой текст")
        if find_secret(text, [self.cfg.token]):
            raise ApiError(400, "secret_detected", "текст похож на секрет")
        delivered = []
        for owner in sorted(self.cfg.owner_ids):
            try:
                with self._send_lock:
                    self.api.send_message(owner, f"[{self.bot_username}] {text}"[:TEXT_LIMIT])
                delivered.append(owner)
            except TelegramError as exc:
                log.warning("Не удалось написать владельцу %s в личку (%s). Владелец должен нажать /start у бота.",
                            owner, exc.description)
        return {"delivered": delivered}
