import sys
import threading
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from board.api_client import BoardClient  # noqa: E402
from board.config import TransportConfig  # noqa: E402
from board.journal import Journal  # noqa: E402
from board.service import BoardService  # noqa: E402
from board.telegram_api import TelegramAPI  # noqa: E402
from board.transport import make_server  # noqa: E402
from tests.fake_telegram import CHAT_ID, OWNER_ID, TOKEN, FakeTelegram  # noqa: E402


@pytest.fixture
def fake_tg():
    tg = FakeTelegram().start()
    yield tg
    tg.close()


@pytest.fixture
def cfg(tmp_path, fake_tg):
    return TransportConfig(
        token=TOKEN,
        chat_id=CHAT_ID,
        owner_ids=frozenset({OWNER_ID}),
        socket_path=str(tmp_path / "sock" / "board.sock"),
        data_dir=str(tmp_path / "data"),
        api_base=fake_tg.base,
        poll_timeout=0,
        max_posts_per_hour=5,
        digest_interval=600,
    )


@pytest.fixture
def service(cfg):
    journal = Journal(cfg.journal_path)
    svc = BoardService(cfg, journal, TelegramAPI(cfg.token, cfg.api_base), sleep=lambda s: None)
    svc.init_identity()
    yield svc
    journal.close()


@pytest.fixture
def server(service):
    srv = make_server(service.cfg.socket_path, service)
    thread = threading.Thread(target=srv.serve_forever, daemon=True)
    thread.start()
    yield srv
    srv.shutdown()
    srv.server_close()


@pytest.fixture
def client(server, service):
    return BoardClient(service.cfg.socket_path, timeout=10)
