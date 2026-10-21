"""Клиент API транспорта (HTTP поверх Unix-сокета) для CLI, хука и цикла агента."""

from __future__ import annotations

import http.client
import json
import os
import socket
from typing import Any, Optional

from .config import DEFAULT_SOCKET


class BoardUnavailable(Exception):
    """Транспорт не отвечает (контейнер остановлен или ещё запускается)."""


class BoardApiError(Exception):
    def __init__(self, status: int, code: str, message: str, extra: Optional[dict] = None):
        super().__init__(message)
        self.status = status
        self.code = code
        self.message = message
        self.extra = extra or {}


class _UnixConnection(http.client.HTTPConnection):
    def __init__(self, path: str, timeout: float):
        super().__init__("board", timeout=timeout)
        self._path = path

    def connect(self) -> None:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.settimeout(self.timeout)
        sock.connect(self._path)
        self.sock = sock


class BoardClient:
    def __init__(self, socket_path: Optional[str] = None, timeout: float = 120):
        self.socket_path = socket_path or os.environ.get("BOARD_SOCKET") or DEFAULT_SOCKET
        self.timeout = timeout

    def call(self, op: str, payload: Optional[dict] = None) -> dict[str, Any]:
        body = json.dumps(payload or {}, ensure_ascii=False).encode("utf-8")
        conn = _UnixConnection(self.socket_path, self.timeout)
        try:
            conn.request("POST", "/" + op.lstrip("/"), body=body,
                         headers={"Content-Type": "application/json", "Content-Length": str(len(body))})
            resp = conn.getresponse()
            raw = resp.read()
            status = resp.status
        except (OSError, http.client.HTTPException) as exc:
            raise BoardUnavailable(f"транспорт доски недоступен ({exc.__class__.__name__}: {exc})") from None
        finally:
            conn.close()
        try:
            data = json.loads(raw.decode("utf-8"))
        except (ValueError, UnicodeDecodeError):
            raise BoardApiError(status, "bad_response", "транспорт вернул не JSON") from None
        if status != 200:
            err = data.get("error") if isinstance(data, dict) else None
            err = err if isinstance(err, dict) else {}
            extra = {k: v for k, v in err.items() if k not in {"code", "message"}}
            raise BoardApiError(status, str(err.get("code") or status), str(err.get("message") or "ошибка"), extra)
        return data
