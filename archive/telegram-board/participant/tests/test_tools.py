import io
import json

from board import discover, owner_tools
from tests.fake_telegram import CHAT_ID, OWNER_ID, TOKEN


def test_discover_lists_chats_without_confirming_updates(monkeypatch, fake_tg, capsys):
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", TOKEN)
    monkeypatch.setenv("TELEGRAM_API_BASE", fake_tg.base)
    fake_tg.push_message("привет")
    fake_tg.push_message("/start", user_id=OWNER_ID, chat_id=OWNER_ID, chat_type="private")
    assert discover.main() == 0
    out = capsys.readouterr().out
    assert str(CHAT_ID) in out and "supergroup" in out
    assert len(fake_tg.updates) == 2  # обновления не подтверждены и достанутся транспорту


def test_owner_tools_attachment_and_upload(monkeypatch, service, fake_tg, capsysbinary):
    cfg = service.cfg
    for key, value in {
        "TELEGRAM_BOT_TOKEN": TOKEN, "BOARD_CHAT_ID": str(CHAT_ID), "OWNER_USER_IDS": str(OWNER_ID),
        "TELEGRAM_API_BASE": fake_tg.base, "BOARD_DATA_DIR": cfg.data_dir,
    }.items():
        monkeypatch.setenv(key, value)
    fake_tg.files["job1"] = b"job-archive-bytes"
    msg = fake_tg.push_message("#compute заявка", document={"file_id": "job1", "file_name": "job.tar.gz", "file_size": 17})
    service.poll_once()
    assert owner_tools.main(["attachment", str(msg["message_id"])]) == 0
    captured = capsysbinary.readouterr()
    assert captured.out == b"job-archive-bytes" and b"name=job.tar.gz" in captured.err

    monkeypatch.setattr("sys.stdin", io.TextIOWrapper(io.BytesIO(b"result-bytes")))
    assert owner_tools.main(["upload", "--name", "result.tar.gz", "--reply-to", str(msg["message_id"]),
                             "--caption", "#compute результат"]) == 0
    sent = fake_tg.sent[-1]["params"]
    assert sent["document"]["data"] == b"result-bytes"
    assert json.loads(sent["reply_parameters"])["message_id"] == msg["message_id"]  # в multipart — JSON-строка
    assert owner_tools.main(["attachment", "999999"]) == 1
