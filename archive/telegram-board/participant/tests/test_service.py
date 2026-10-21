import base64

import pytest

from board.service import ApiError, split_text, utf16_slice
from tests.fake_telegram import BOT_ID, BOT_USERNAME, CHAT_ID, OWNER_ID


def poll(service):
    service.poll_once()


def test_stores_group_messages_and_ignores_foreign_chats(service, fake_tg):
    fake_tg.push_message("обычное сообщение")
    fake_tg.push_message("чужой чат", chat_id=-100999)
    poll(service)
    rows = service.journal.history(None, 10)
    assert [r["text"] for r in rows] == ["обычное сообщение"]
    assert rows[0]["addressed"] == 0
    assert service.journal.meta_int("update_offset") > 0


def test_mention_detection_entities_reply_and_text(service, fake_tg):
    text = "🙂 привет @" + BOT_USERNAME + ", вопрос"
    offset = len("🙂 привет ".encode("utf-16-le")) // 2  # смайлик занимает две единицы UTF-16
    fake_tg.push_message(text, entities=[{"type": "mention", "offset": offset, "length": len(BOT_USERNAME) + 1}])
    fake_tg.push_message("ответ боту", reply_to={"message_id": 1, "from": {"id": BOT_ID, "is_bot": True}})
    fake_tg.push_message("эй @" + BOT_USERNAME.upper() + " без entities")
    fake_tg.push_message("упоминание @" + BOT_USERNAME + "_other не наше")
    poll(service)
    flags = [r["addressed"] for r in service.journal.history(None, 10)]
    assert flags == [1, 1, 1, 0]
    assert utf16_slice(text, offset, len(BOT_USERNAME) + 1) == "@" + BOT_USERNAME


def test_owner_commands(service, fake_tg):
    fake_tg.push_message(f"/pause@{BOT_USERNAME}", user_id=OWNER_ID, username="owner")
    poll(service)
    assert service.journal.meta_int("paused") == 1
    assert "Пауза" in fake_tg.sent[-1]["params"]["text"]
    # Команда без @имени в группе адресована всем ботам — не выполняем.
    fake_tg.push_message("/resume", user_id=OWNER_ID, username="owner")
    poll(service)
    assert service.journal.meta_int("paused") == 1
    # Чужой пользователь не может снять паузу.
    fake_tg.push_message(f"/resume@{BOT_USERNAME}", user_id=99, username="mallory")
    poll(service)
    assert service.journal.meta_int("paused") == 1
    # В личке владельцу хватает /resume.
    fake_tg.push_message("/resume", user_id=OWNER_ID, username="owner", chat_id=OWNER_ID, chat_type="private")
    poll(service)
    assert service.journal.meta_int("paused") == 0
    # Команды владельца не попадают агенту как сообщения доски.
    texts = [r["text"] for r in service.journal.history(None, 20)]
    assert f"/pause@{BOT_USERNAME}" not in texts
    assert f"/resume@{BOT_USERNAME}" in texts  # чужая «команда» — обычное сообщение


def test_private_messages_from_strangers_are_ignored(service, fake_tg):
    fake_tg.push_message("/status", user_id=99, chat_id=99, chat_type="private")
    poll(service)
    assert fake_tg.sent == []


def test_edit_updates_text(service, fake_tg):
    msg = fake_tg.push_message("первая версия")
    poll(service)
    fake_tg.push_message("вторая версия", message_id=msg["message_id"], edited=True)
    poll(service)
    row = service.journal.get(msg["message_id"])
    assert row["text"] == "вторая версия" and row["edit_date"]


def test_read_new_mentions_notify_and_digest(service, fake_tg):
    fake_tg.push_message("раз")
    fake_tg.push_message(f"@{BOT_USERNAME} вопрос")
    fake_tg.push_message("два", username="bob")
    poll(service)
    note = service.op_notify({})
    assert note["mentions_total"] == 1 and "вопрос" in note["mentions"][0]["text"]
    assert note["digest"]["count"] == 2
    again = service.op_notify({})
    assert again["mentions_total"] == 0 and again["digest"] is None  # не повторяем
    data = service.op_read_new({"limit": 2})
    assert [m["text"] for m in data["messages"]] == ["раз", f"@{BOT_USERNAME} вопрос"]
    assert data["remaining"] == 1
    assert service.op_mentions({})["messages"] == []  # обращение прочитано через read_new
    assert service.op_read_new({})["messages"][0]["text"] == "два"


def test_post_idempotent_chunked_and_rate_limited(service, fake_tg):
    long_text = ("абзац " * 500 + "\n\n") * 3
    first = service.op_post({"text": long_text, "key": "post-key-0001", "reply_to": 10})
    assert len(first["message_ids"]) >= 2
    assert fake_tg.sent[0]["params"]["reply_parameters"]["message_id"] == 10
    assert "reply_parameters" not in fake_tg.sent[1]["params"]
    replay = service.op_post({"text": long_text, "key": "post-key-0001"})
    assert replay["replayed"] and replay["message_ids"] == first["message_ids"]
    own = [r for r in service.journal.history(None, 50) if r["is_own"]]
    assert len(own) == len(first["message_ids"])
    for i in range(4):
        service.op_post({"text": f"сообщение {i}", "key": f"post-key-{i + 10:04d}"})
    with pytest.raises(ApiError) as exc:
        service.op_post({"text": "лишнее", "key": "post-key-9999"})
    assert exc.value.code == "rate_limited"


def test_post_rejects_secrets_and_bad_keys(service):
    with pytest.raises(ApiError) as exc:
        service.op_post({"text": "мой токен sk-ant-oat01-" + "x" * 40, "key": "post-key-0002"})
    assert exc.value.code == "secret_detected"
    with pytest.raises(ApiError) as exc:
        service.op_post({"text": "ок", "key": "short"})
    assert exc.value.code == "bad_request"


def test_uncertain_send_is_not_repeated(service, fake_tg, monkeypatch):
    from board.telegram_api import TelegramError

    def boom(*args, **kwargs):
        raise TelegramError("sendMessage", 0, "сеть: timeout")

    monkeypatch.setattr(service.api, "send_message", boom)
    with pytest.raises(ApiError) as exc:
        service.op_post({"text": "важное", "key": "post-key-0003"})
    assert exc.value.code == "uncertain"
    with pytest.raises(ApiError) as exc:
        service.op_post({"text": "важное", "key": "post-key-0003"})
    assert exc.value.code == "uncertain"


def test_definite_failure_can_be_retried(service, fake_tg):
    fake_tg.fail_next.append(("sendMessage", 400, "Bad Request: something"))
    status, payload = service.dispatch("/post", {"text": "текст", "key": "post-key-0004"})
    assert status == 502 and payload["error"]["code"] == "telegram"
    assert service.op_post({"text": "текст", "key": "post-key-0004"})["message_ids"]


def test_send_file_and_fetch(service, fake_tg):
    data = b"%PDF-1.4 test"
    res = service.op_send_file({"name": "note.pdf", "data_b64": base64.b64encode(data).decode(),
                                "caption": "черновик", "key": "file-key-0001"})
    assert res["message_ids"] and fake_tg.sent[-1]["params"]["document"]["data"] == data
    with pytest.raises(ApiError) as exc:
        service.op_send_file({"name": ".env", "data_b64": base64.b64encode(b"A=1").decode(), "key": "file-key-0002"})
    assert exc.value.code == "secret_detected"
    fake_tg.files["doc1"] = b"hello"
    msg = fake_tg.push_message("файл", document={"file_id": "doc1", "file_name": "a.txt", "file_size": 5})
    poll(service)
    got = service.op_fetch({"id": msg["message_id"]})
    assert base64.b64decode(got["data_b64"]) == b"hello" and got["name"] == "a.txt"
    fake_tg.files.clear()
    assert base64.b64decode(service.op_fetch({"id": msg["message_id"]})["data_b64"]) == b"hello"  # из кэша


def test_sleep_wake_heartbeat_and_status(service, fake_tg):
    res = service.op_sleep({"seconds": 5, "reason": "жду расчёт"})
    assert res["seconds"] == 60  # не меньше минуты
    assert service.op_control({})["sleep_until"]
    service.op_wake({})
    assert service.op_control({})["sleep_until"] is None
    service.op_heartbeat({"state": "working", "turns": 3})
    fake_tg.push_message(f"/status@{BOT_USERNAME}", user_id=OWNER_ID, username="owner")
    poll(service)
    assert "ходов 3" in fake_tg.sent[-1]["params"]["text"]


def test_split_text():
    parts = split_text("a" * 9000)
    assert len(parts) == 3 and all(len(p) <= 4000 for p in parts)
    assert split_text("короткий") == ["короткий"]


def test_dispatch_unknown_route(service):
    status, payload = service.dispatch("/nope", {})
    assert status == 404


def test_group_chat_id_constant():
    assert CHAT_ID < 0
