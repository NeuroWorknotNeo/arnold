import json

import pytest

from board import cli, hook
from board.api_client import BoardApiError, BoardClient, BoardUnavailable
from tests.fake_telegram import BOT_USERNAME, OWNER_ID


@pytest.fixture
def board_env(monkeypatch, client, tmp_path):
    monkeypatch.setenv("BOARD_SOCKET", client.socket_path)
    monkeypatch.setenv("RUNNER_STATE_DIR", str(tmp_path / "state"))
    monkeypatch.setattr(hook, "STATE", tmp_path / "state" / "hook-paused")
    return client


def test_client_roundtrip_and_errors(board_env, tmp_path):
    status = board_env.call("status")
    assert status["bot_username"] == BOT_USERNAME
    with pytest.raises(BoardApiError) as exc:
        board_env.call("search", {"query": "a"})
    assert exc.value.code == "bad_request"
    with pytest.raises(BoardUnavailable):
        BoardClient(str(tmp_path / "missing.sock"), timeout=1).call("status")


def test_cli_post_new_show_fetch(board_env, service, fake_tg, capsys, tmp_path):
    assert cli.main(["post", "первая мысль", "--reply-to", "5"]) == 0
    assert "Опубликовано" in capsys.readouterr().out
    # Повтор той же команды не дублирует публикацию.
    assert cli.main(["post", "первая мысль", "--reply-to", "5"]) == 0
    assert "Уже было опубликовано" in capsys.readouterr().out
    assert len(fake_tg.sent) == 1

    fake_tg.files["doc9"] = b"data"
    msg = fake_tg.push_message(f"@{BOT_USERNAME} посмотри файл", user_id=OWNER_ID, username="owner",
                               document={"file_id": "doc9", "file_name": "lemma.md", "file_size": 4})
    service.poll_once()
    assert cli.main(["new"]) == 0
    out = capsys.readouterr().out
    assert "ВАШ ВЛАДЕЛЕЦ" in out and "обращение к вам" in out and f"board fetch {msg['message_id']}" in out
    assert cli.main(["fetch", str(msg["message_id"]), "--out", str(tmp_path / "inbox")]) == 0
    saved = tmp_path / "inbox" / f"{msg['message_id']}-lemma.md"
    assert saved.read_bytes() == b"data"
    capsys.readouterr()
    assert cli.main(["show", str(msg["message_id"])]) == 0
    assert "lemma.md" in capsys.readouterr().out

    note = tmp_path / "result.md"
    note.write_text("# Лемма\n")
    assert cli.main(["send", str(note), "--caption", "лемма"]) == 0
    assert fake_tg.sent[-1]["params"]["document"]["filename"] == "result.md"
    assert "Файл отправлен" in capsys.readouterr().out

    assert cli.main(["--json", "status"]) == 0
    assert json.loads(capsys.readouterr().out)["posts_last_hour"] == 2


def test_cli_reports_api_errors(board_env, capsys):
    assert cli.main(["post", "sk-ant-api03-" + "y" * 40]) == 1
    assert "secret_detected" in capsys.readouterr().err
    assert cli.main(["sleep", "600", "жду"]) == 0
    assert "не раньше" in capsys.readouterr().out


def test_cli_board_unavailable(monkeypatch, tmp_path, capsys):
    monkeypatch.setenv("BOARD_SOCKET", str(tmp_path / "none.sock"))
    assert cli.main(["status"]) == 3
    assert "недоступен" in capsys.readouterr().err


def test_hook_outputs_context_once(board_env, service, fake_tg, capsys, monkeypatch):
    monkeypatch.setattr("sys.stdin", __import__("io").StringIO("{}"))
    assert hook.main() == 0
    assert capsys.readouterr().out == ""  # нечего сообщать
    fake_tg.push_message(f"@{BOT_USERNAME} что думаешь о лемме 2?", username="bob")
    service.poll_once()
    monkeypatch.setattr("sys.stdin", __import__("io").StringIO("{}"))
    assert hook.main() == 0
    payload = json.loads(capsys.readouterr().out)
    ctx = payload["hookSpecificOutput"]["additionalContext"]
    assert payload["hookSpecificOutput"]["hookEventName"] == "PostToolUse"
    assert "лемме 2" in ctx and "board mentions" in ctx
    monkeypatch.setattr("sys.stdin", __import__("io").StringIO("{}"))
    assert hook.main() == 0
    assert capsys.readouterr().out == ""  # то же обращение повторно не показываем


def test_hook_pause_notice_once(board_env, service, capsys, monkeypatch):
    service.journal.set_meta("paused", 1)
    for expected in (True, False):
        monkeypatch.setattr("sys.stdin", __import__("io").StringIO("{}"))
        hook.main()
        out = capsys.readouterr().out
        assert ("паузу" in out) is expected


def test_hook_silent_when_board_down(monkeypatch, tmp_path, capsys):
    monkeypatch.setenv("BOARD_SOCKET", str(tmp_path / "none.sock"))
    monkeypatch.setattr("sys.stdin", __import__("io").StringIO("{}"))
    assert hook.main() == 0
    assert capsys.readouterr().out == ""
