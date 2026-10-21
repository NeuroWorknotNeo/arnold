"""Минимальный клиент Telegram Bot API на стандартной библиотеке.

Токен входит в URL каждого запроса, поэтому ни URL, ни исходные исключения urllib
наружу не выходят: ошибки пересобираются без адреса, а строка токена затирается.
"""

from __future__ import annotations

import json
import secrets
import socket
import urllib.error
import urllib.request
from typing import Any, Optional

MAX_DOWNLOAD_BYTES = 20 * 1024 * 1024  # getFile отдаёт файлы не больше 20 МБ


class TelegramError(Exception):
    """Ошибка Bot API или сети. ``code`` — HTTP/Bot API код (0 для сетевой ошибки)."""

    def __init__(self, method: str, code: int, description: str, retry_after: Optional[int] = None):
        self.method = method
        self.code = code
        self.description = description
        self.retry_after = retry_after
        super().__init__(f"{method}: {code} {description}")

    @property
    def is_network(self) -> bool:
        return self.code == 0


class TelegramAPI:
    def __init__(self, token: str, base: str = "https://api.telegram.org"):
        self._token = token
        self._base = base.rstrip("/")

    def _clean(self, text: str) -> str:
        return text.replace(self._token, "‹токен›") if self._token else text

    def _request(self, method: str, data: bytes, content_type: str, timeout: float) -> Any:
        url = f"{self._base}/bot{self._token}/{method}"
        req = urllib.request.Request(url, data=data, headers={"Content-Type": content_type}, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = resp.read()
        except urllib.error.HTTPError as exc:
            raw = exc.read() if hasattr(exc, "read") else b""
            try:
                payload = json.loads(raw.decode("utf-8"))
            except (ValueError, UnicodeDecodeError):
                raise TelegramError(method, exc.code, self._clean(str(exc.reason))) from None
            return self._unwrap(method, payload, http_code=exc.code)
        except (urllib.error.URLError, socket.timeout, TimeoutError, ConnectionError, OSError) as exc:
            reason = getattr(exc, "reason", exc)
            raise TelegramError(method, 0, self._clean(f"сеть: {reason}")) from None
        try:
            payload = json.loads(raw.decode("utf-8"))
        except (ValueError, UnicodeDecodeError):
            raise TelegramError(method, 0, "ответ не JSON") from None
        return self._unwrap(method, payload)

    def _unwrap(self, method: str, payload: Any, http_code: int = 200) -> Any:
        if not isinstance(payload, dict):
            raise TelegramError(method, http_code, "неожиданный ответ")
        if payload.get("ok"):
            return payload.get("result")
        params = payload.get("parameters") or {}
        retry_after = params.get("retry_after") if isinstance(params, dict) else None
        code = int(payload.get("error_code") or http_code or 0)
        raise TelegramError(method, code, self._clean(str(payload.get("description") or "ошибка")), retry_after)

    def call(self, method: str, params: Optional[dict] = None, timeout: float = 30) -> Any:
        body = json.dumps(params or {}, ensure_ascii=False).encode("utf-8")
        return self._request(method, body, "application/json", timeout)

    def call_multipart(self, method: str, fields: dict, file_field: str, filename: str,
                       data: bytes, timeout: float = 120) -> Any:
        boundary = "----board" + secrets.token_hex(12)
        parts: list[bytes] = []
        for name, value in fields.items():
            if value is None:
                continue
            if not isinstance(value, str):
                value = json.dumps(value, ensure_ascii=False)
            parts.append(
                f"--{boundary}\r\nContent-Disposition: form-data; name=\"{name}\"\r\n\r\n".encode("utf-8")
                + value.encode("utf-8") + b"\r\n"
            )
        safe_name = filename.replace('"', "_").replace("\r", "_").replace("\n", "_")
        parts.append(
            f"--{boundary}\r\nContent-Disposition: form-data; name=\"{file_field}\"; "
            f"filename=\"{safe_name}\"\r\nContent-Type: application/octet-stream\r\n\r\n".encode("utf-8")
            + data + b"\r\n"
        )
        parts.append(f"--{boundary}--\r\n".encode("utf-8"))
        return self._request(method, b"".join(parts), f"multipart/form-data; boundary={boundary}", timeout)

    # ------------------------------------------------------------------ методы
    def get_me(self) -> dict:
        return self.call("getMe")

    def get_chat(self, chat_id: int) -> dict:
        return self.call("getChat", {"chat_id": chat_id})

    def get_updates(self, offset: int, timeout: int, allowed_updates: list[str]) -> list[dict]:
        params = {"offset": offset, "timeout": timeout, "allowed_updates": allowed_updates}
        return self.call("getUpdates", params, timeout=timeout + 15) or []

    def send_message(self, chat_id: int, text: str, reply_to: Optional[int] = None) -> dict:
        params: dict[str, Any] = {"chat_id": chat_id, "text": text, "link_preview_options": {"is_disabled": True}}
        if reply_to:
            params["reply_parameters"] = {"message_id": reply_to, "allow_sending_without_reply": True}
        return self.call("sendMessage", params)

    def send_document(self, chat_id: int, filename: str, data: bytes, caption: Optional[str] = None,
                      reply_to: Optional[int] = None) -> dict:
        fields: dict[str, Any] = {"chat_id": str(chat_id)}
        if caption:
            fields["caption"] = caption
        if reply_to:
            fields["reply_parameters"] = {"message_id": reply_to, "allow_sending_without_reply": True}
        return self.call_multipart("sendDocument", fields, "document", filename, data)

    def download_file(self, file_id: str, max_bytes: int = MAX_DOWNLOAD_BYTES) -> bytes:
        info = self.call("getFile", {"file_id": file_id})
        path = (info or {}).get("file_path")
        if not path:
            raise TelegramError("getFile", 400, "файл недоступен для скачивания (больше 20 МБ?)")
        size = (info or {}).get("file_size")
        if isinstance(size, int) and size > max_bytes:
            raise TelegramError("getFile", 400, f"файл {size} байт больше предела {max_bytes}")
        url = f"{self._base}/file/bot{self._token}/{path}"
        try:
            with urllib.request.urlopen(url, timeout=120) as resp:
                data = resp.read(max_bytes + 1)
        except (urllib.error.URLError, socket.timeout, TimeoutError, ConnectionError, OSError) as exc:
            reason = getattr(exc, "reason", exc)
            raise TelegramError("download", 0, self._clean(f"сеть: {reason}")) from None
        if len(data) > max_bytes:
            raise TelegramError("download", 400, "файл больше допустимого размера")
        return data
