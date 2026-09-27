"""Процесс транспорта: единственный читатель обновлений бота, API для агента на Unix-сокете, архив.

Запуск: ``python -m board.transport``. Токен бота есть только в этом процессе/контейнере.
"""

from __future__ import annotations

import http.server
import json
import logging
import os
import signal
import socketserver
import sys
import threading
import time
from pathlib import Path
from typing import Optional

from .config import ConfigError, TransportConfig
from .journal import Journal
from .service import BoardService
from .telegram_api import TelegramAPI, TelegramError

log = logging.getLogger("board.transport")
MAX_REQUEST_BYTES = 32 * 1024 * 1024


class _Handler(http.server.BaseHTTPRequestHandler):
    server_version = "board"
    service: BoardService  # задаётся в make_server

    def address_string(self) -> str:  # у Unix-сокета нет адреса клиента
        return "unix"

    def log_message(self, fmt: str, *args) -> None:
        log.debug("api: " + fmt, *args)

    def _reply(self, status: int, payload: dict) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self) -> None:  # noqa: N802 (имя из http.server)
        try:
            length = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            length = -1
        if length < 0 or length > MAX_REQUEST_BYTES:
            self._reply(413, {"error": {"code": "too_large", "message": "слишком большой запрос"}})
            return
        raw = self.rfile.read(length) if length else b"{}"
        try:
            payload = json.loads(raw.decode("utf-8") or "{}")
        except (ValueError, UnicodeDecodeError):
            self._reply(400, {"error": {"code": "bad_json", "message": "тело запроса не JSON"}})
            return
        try:
            status, result = self.service.dispatch(self.path, payload)
        except Exception:
            log.exception("Ошибка операции %s", self.path)
            status, result = 500, {"error": {"code": "internal", "message": "внутренняя ошибка транспорта"}}
        self._reply(status, result)

    do_GET = do_POST


class _Server(socketserver.ThreadingMixIn, socketserver.UnixStreamServer):
    daemon_threads = True


def make_server(socket_path: str, service: BoardService) -> _Server:
    path = Path(socket_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() or path.is_symlink():
        path.unlink()
    handler = type("Handler", (_Handler,), {"service": service})
    server = _Server(str(path), handler)
    # Сокет лежит в томе, общем только для двух контейнеров этого участника.
    os.chmod(path, 0o666)
    return server


def poll_forever(service: BoardService, stop: threading.Event) -> None:
    backoff = 1.0
    conflict_logged = False
    while not stop.is_set():
        try:
            service.poll_once()
            backoff = 1.0
            conflict_logged = False
        except TelegramError as exc:
            if exc.code == 401:
                log.error("Telegram отверг токен бота (401). Проверьте TELEGRAM_BOT_TOKEN; транспорт остановлен.")
                service.fatal_code = 3
                stop.set()
                return
            if exc.code == 409:
                if not conflict_logged:
                    log.error(
                        "Обновления этого бота уже читает другой процесс или настроен webhook (409). "
                        "Токен должен использовать только этот участник. Жду и повторяю."
                    )
                    conflict_logged = True
                stop.wait(30)
                continue
            delay = float(exc.retry_after) if exc.retry_after else backoff
            log.warning("Ошибка getUpdates: %s; повтор через %.0f с", exc, delay)
            stop.wait(delay)
            backoff = min(backoff * 2, 60.0)
        except Exception:
            log.exception("Непредвиденная ошибка опроса; повтор через %.0f с", backoff)
            stop.wait(backoff)
            backoff = min(backoff * 2, 60.0)


def archive_forever(service: BoardService, stop: threading.Event) -> None:
    from .archive import Archiver

    archiver = Archiver(service)
    stop.wait(60)  # дать опросу набрать первые сообщения
    while not stop.is_set():
        try:
            archiver.run_once()
        except Exception as exc:
            log.warning("Архив не обновлён: %s", exc)
        stop.wait(service.cfg.archive_interval)


def main(argv: Optional[list[str]] = None) -> int:
    logging.basicConfig(
        level=os.environ.get("LOG_LEVEL", "INFO"),
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    try:
        cfg = TransportConfig.from_env()
    except ConfigError as exc:
        log.error("Ошибка конфигурации: %s", exc)
        return 2
    journal = Journal(cfg.journal_path)
    service = BoardService(cfg, journal, TelegramAPI(cfg.token, cfg.api_base))
    stop = threading.Event()

    def _stop(signum, frame):  # noqa: ARG001
        stop.set()

    signal.signal(signal.SIGTERM, _stop)
    signal.signal(signal.SIGINT, _stop)

    while not stop.is_set():
        try:
            service.init_identity()
            break
        except TelegramError as exc:
            if exc.code == 401:
                log.error("Telegram отверг токен бота (401). Проверьте TELEGRAM_BOT_TOKEN.")
                return 3
            log.warning("getMe не удался (%s); повтор через 15 с", exc)
            stop.wait(15)
    if stop.is_set():
        return 0

    server = make_server(cfg.socket_path, service)
    threads = [
        threading.Thread(target=server.serve_forever, name="api", daemon=True),
        threading.Thread(target=poll_forever, args=(service, stop), name="poll", daemon=True),
    ]
    if cfg.archive_enabled:
        threads.append(threading.Thread(target=archive_forever, args=(service, stop), name="archive", daemon=True))
    for t in threads:
        t.start()
    log.info("Транспорт запущен: сокет %s, архив %s", cfg.socket_path, "включён" if cfg.archive_enabled else "выключен")
    try:
        while not stop.is_set():
            stop.wait(5)
            # Пульс для healthcheck — только пока опрос Telegram действительно проходит.
            if time.time() - journal.meta_int("last_poll_ok") < 180:
                Path(cfg.data_dir, "heartbeat").write_text(str(int(time.time())))
    finally:
        server.shutdown()
        server.server_close()
        journal.close()
        log.info("Транспорт остановлен")
    return getattr(service, "fatal_code", 0)


if __name__ == "__main__":
    sys.exit(main())
