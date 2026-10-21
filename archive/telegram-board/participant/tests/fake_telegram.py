"""Поддельный Telegram Bot API для тестов: HTTP-сервер в отдельном потоке."""

from __future__ import annotations

import json
import re
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

TOKEN = "123456789:AAFakeTokenForTestsOnly_abcdefghijklm"
BOT_ID = 123456789
BOT_USERNAME = "arnold_test_bot"
CHAT_ID = -1001234567890
OWNER_ID = 42


class FakeTelegram:
    def __init__(self, host: str = "127.0.0.1", port: int = 0):
        self.updates: list[dict] = []
        self.next_update_id = 1000
        self.next_message_id = 500
        self.sent: list[dict] = []
        self.files: dict[str, bytes] = {}
        self.fail_next: list[tuple[str, int, str]] = []  # (метод, код, описание)
        self.lock = threading.Lock()
        self.cond = threading.Condition(self.lock)
        self.server = ThreadingHTTPServer((host, port), self._handler())
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)

    @property
    def base(self) -> str:
        return f"http://127.0.0.1:{self.server.server_address[1]}"

    def start(self) -> "FakeTelegram":
        self.thread.start()
        return self

    def close(self) -> None:
        self.server.shutdown()
        self.server.server_close()

    # --------------------------------------------------------------- helpers
    def push_message(self, text: str = "", user_id: int = 7, username: str = "alice", is_bot: bool = False,
                     chat_id: int = CHAT_ID, chat_type: str = "supergroup", entities=None, reply_to=None,
                     document=None, edited: bool = False, message_id=None) -> dict:
        with self.cond:
            mid = message_id or self.next_message_id
            if message_id is None:
                self.next_message_id += 1
            msg: dict[str, Any] = {
                "message_id": mid,
                "date": int(time.time()),
                "chat": {"id": chat_id, "type": chat_type, "title": "Тестовая доска"},
                "from": {"id": user_id, "is_bot": is_bot, "first_name": username.title(), "username": username},
            }
            if document:
                msg["document"] = document
                msg["caption"] = text
            else:
                msg["text"] = text
            if entities:
                msg["entities" if not document else "caption_entities"] = entities
            if reply_to:
                msg["reply_to_message"] = reply_to
            if edited:
                msg["edit_date"] = int(time.time())
            self.updates.append({"update_id": self.next_update_id, ("edited_message" if edited else "message"): msg})
            self.next_update_id += 1
            self.cond.notify_all()
            return msg

    def _new_message(self, chat_id: int, text: str = "", **extra) -> dict:
        mid = self.next_message_id
        self.next_message_id += 1
        msg = {
            "message_id": mid,
            "date": int(time.time()),
            "chat": {"id": chat_id, "type": "supergroup" if chat_id < 0 else "private", "title": "Тестовая доска"},
            "from": {"id": BOT_ID, "is_bot": True, "first_name": "Arnold", "username": BOT_USERNAME},
        }
        if text:
            msg["text"] = text
        msg.update(extra)
        return msg

    # --------------------------------------------------------------- server
    def _handler(self):
        fake = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def _json(self, payload, status=200):
                body = json.dumps(payload).encode()
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def do_GET(self):
                m = re.match(r"^/file/bot([^/]+)/(.+)$", self.path)
                if m and m.group(1) == TOKEN and m.group(2) in fake.files:
                    data = fake.files[m.group(2)]
                    self.send_response(200)
                    self.send_header("Content-Length", str(len(data)))
                    self.end_headers()
                    self.wfile.write(data)
                    return
                self._json({"ok": False, "error_code": 404, "description": "Not Found"}, 404)

            def do_POST(self):
                if self.path.startswith("/_control/"):
                    length = int(self.headers.get("Content-Length") or 0)
                    body = json.loads(self.rfile.read(length) or b"{}")
                    self._json(fake.control(self.path[len("/_control/"):], body))
                    return
                m = re.match(r"^/bot([^/]+)/(\w+)$", self.path)
                if not m or m.group(1) != TOKEN:
                    self._json({"ok": False, "error_code": 401, "description": "Unauthorized"}, 401)
                    return
                method = m.group(2)
                length = int(self.headers.get("Content-Length") or 0)
                raw = self.rfile.read(length)
                ctype = self.headers.get("Content-Type", "")
                if ctype.startswith("multipart/form-data"):
                    params = fake._parse_multipart(raw, ctype)
                else:
                    params = json.loads(raw or b"{}")
                with fake.lock:
                    for i, (meth, code, desc) in enumerate(fake.fail_next):
                        if meth == method:
                            fake.fail_next.pop(i)
                            payload = {"ok": False, "error_code": code, "description": desc}
                            if code == 429:
                                payload["parameters"] = {"retry_after": 1}
                            self._json(payload, code)
                            return
                result = fake.handle(method, params)
                if isinstance(result, tuple):
                    self._json({"ok": False, "error_code": result[0], "description": result[1]}, result[0])
                else:
                    self._json({"ok": True, "result": result})

        return Handler

    @staticmethod
    def _parse_multipart(raw: bytes, ctype: str) -> dict:
        boundary = ctype.split("boundary=", 1)[1].encode()
        params: dict[str, Any] = {}
        for part in raw.split(b"--" + boundary):
            if b"\r\n\r\n" not in part:
                continue
            head, body = part.split(b"\r\n\r\n", 1)
            body = body[:-2] if body.endswith(b"\r\n") else body
            name = re.search(rb'name="([^"]+)"', head).group(1).decode()
            filename = re.search(rb'filename="([^"]*)"', head)
            if filename:
                params[name] = {"filename": filename.group(1).decode(), "data": body}
            else:
                params[name] = body.decode()
        return params

    def control(self, op: str, body: dict):
        """Управление поддельным сервером из e2e-теста в Docker."""
        if op == "push":
            return self.push_message(**body)
        if op == "sent":
            with self.lock:
                return [{"method": s["method"], "text": s["params"].get("text"),
                         "chat_id": s["params"].get("chat_id"),
                         "reply_to": (s["params"].get("reply_parameters") or {}).get("message_id")
                         if isinstance(s["params"].get("reply_parameters"), dict) else None,
                         "message_id": s["message"]["message_id"]} for s in self.sent]
        return {"error": f"unknown op {op}"}

    def handle(self, method: str, params: dict):
        if method == "getMe":
            return {"id": BOT_ID, "is_bot": True, "first_name": "Arnold", "username": BOT_USERNAME}
        if method == "getChat":
            if int(params["chat_id"]) == CHAT_ID:
                return {"id": CHAT_ID, "type": "supergroup", "title": "Тестовая доска"}
            return (400, "Bad Request: chat not found")
        if method == "getUpdates":
            offset = int(params.get("offset") or 0)
            timeout = float(params.get("timeout") or 0)
            deadline = time.time() + min(timeout, 2)
            with self.cond:
                while True:
                    pending = [u for u in self.updates if u["update_id"] >= offset]
                    if offset:
                        self.updates = [u for u in self.updates if u["update_id"] >= offset]
                    if pending or time.time() >= deadline:
                        return pending
                    self.cond.wait(timeout=max(0.01, deadline - time.time()))
        if method == "sendMessage":
            with self.lock:
                extra = {}
                reply = params.get("reply_parameters")
                if reply:
                    extra["reply_to_message"] = {"message_id": reply["message_id"], "from": {"id": 7}}
                msg = self._new_message(int(params["chat_id"]), params["text"], **extra)
                self.sent.append({"method": method, "params": params, "message": msg})
                return msg
        if method == "sendDocument":
            with self.lock:
                doc = params["document"]
                extra = {"document": {"file_id": f"f{self.next_message_id}", "file_name": doc["filename"],
                                      "file_size": len(doc["data"])}}
                if params.get("caption"):
                    extra["caption"] = params["caption"]
                msg = self._new_message(int(params["chat_id"]), **extra)
                self.sent.append({"method": method, "params": {**params, "document": doc}, "message": msg})
                return msg
        if method == "getFile":
            fid = params["file_id"]
            if fid in self.files:
                return {"file_id": fid, "file_path": fid, "file_size": len(self.files[fid])}
            return (400, "Bad Request: invalid file_id")
        return (404, f"Not Found: method {method}")
