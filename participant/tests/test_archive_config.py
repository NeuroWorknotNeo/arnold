import json
import subprocess
from dataclasses import replace

import pytest

from board.archive import Archiver, render_day
from board.config import AgentConfig, ConfigError, TransportConfig
from board.setup_claude import HOOK_COMMAND, ensure_hook
from tests.fake_telegram import BOT_USERNAME, TOKEN


def git(*args, cwd=None):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, check=True).stdout


def test_archive_pushes_days_and_attachments(service, fake_tg, tmp_path):
    bare = tmp_path / "remote.git"
    git("init", "-q", "--bare", str(bare))
    service.cfg = replace(service.cfg, archive_enabled=True, archive_repo_url=str(bare), archive_token="t" * 20)
    archiver = Archiver(service)
    assert archiver.run_once() is None  # журнал пуст — нечего архивировать

    fake_tg.files["docA"] = b"proof"
    fake_tg.push_message("Идея: функция Четаева $V = (x, \\dot x)$", username="alice")
    fake_tg.push_message("вложение", username="bob", document={"file_id": "docA", "file_name": "proof.md", "file_size": 5})
    service.poll_once()
    service.op_post({"text": "ответ участника", "key": "post-key-arch1"})
    day = archiver.run_once()
    assert day
    readme = git("--git-dir", str(bare), "show", "archive:README.md")
    assert day in readme
    day_file = git("--git-dir", str(bare), "show", f"archive:{day[:4]}/{day[5:7]}/{day}.md")
    assert "функция Четаева" in day_file and "🤖" in day_file and "proof.md" in day_file
    files = git("--git-dir", str(bare), "ls-tree", "-r", "--name-only", "archive")
    assert any(f.endswith("-proof.md") for f in files.splitlines())
    assert "main" not in git("--git-dir", str(bare), "branch")
    # Повторный запуск без новых сообщений ничего не коммитит.
    before = git("--git-dir", str(bare), "rev-parse", "archive")
    assert archiver.run_once() is None
    assert git("--git-dir", str(bare), "rev-parse", "archive") == before


def test_render_day_marks_replies_and_missing_files():
    rows = [{
        "id": 7, "date": 0, "edit_date": None, "from_name": "Bob", "from_username": "bob", "from_is_bot": 1,
        "reply_to": 5, "reply_to_name": "@alice", "text": "текст", "file_kind": "document",
        "file_name": "big.zip", "file_size": 10 ** 8,
    }]
    text = render_day(rows, "1970-01-01", "Доска", BOT_USERNAME, {})
    assert "↩︎ на #5 (@alice)" in text and "не сохранён" in text and "🤖 Bob (@bob)" in text


def base_env(**extra):
    env = {"TELEGRAM_BOT_TOKEN": TOKEN, "BOARD_CHAT_ID": "-1001234567890", "OWNER_USER_IDS": "42, 43"}
    env.update(extra)
    return env


def test_transport_config_validation():
    cfg = TransportConfig.from_env(base_env())
    assert cfg.owner_ids == frozenset({42, 43}) and cfg.chat_id == -1001234567890
    assert TOKEN not in repr(cfg)
    for bad in ({"TELEGRAM_BOT_TOKEN": "123:abc"}, {"BOARD_CHAT_ID": "12345"}, {"OWNER_USER_IDS": ""},
                {"OWNER_USER_IDS": "@me"}, {"ARCHIVE_ENABLED": "true"}, {"ARCHIVE_BRANCH": "main"},
                {"MAX_POSTS_PER_HOUR": "0"}):
        with pytest.raises(ConfigError):
            TransportConfig.from_env(base_env(**bad))
    ok = TransportConfig.from_env(base_env(ARCHIVE_ENABLED="да", ARCHIVE_REPO_URL="https://github.com/a/b.git",
                                           ARCHIVE_GITHUB_TOKEN="x" * 30, BOARD_CHAT_ID='"-1001"'))
    assert ok.archive_enabled and ok.chat_id == -1001


def test_agent_config_validation():
    cfg = AgentConfig.from_env({"PARTICIPANT_ID": "vlad-claude", "CLAUDE_EFFORT": "high",
                                "CLAUDE_EXTRA_ARGS": "--max-turns 200"})
    assert cfg.effort == "high" and cfg.extra_args == ("--max-turns", "200")
    for bad in ({"PARTICIPANT_ID": "Vlad"}, {"PARTICIPANT_ID": "ok-id", "CLAUDE_EFFORT": "ultra"},
                {"PARTICIPANT_ID": "ok-id", "CLAUDE_EXTRA_ARGS": "--bare"},
                {"PARTICIPANT_ID": "ok-id", "MIN_PAUSE_SECONDS": "7200", "MAX_PAUSE_SECONDS": "60"}, {}):
        with pytest.raises(ConfigError):
            AgentConfig.from_env(bad)


def test_ensure_hook_is_idempotent_and_preserves_settings(tmp_path):
    path = tmp_path / ".claude" / "settings.json"
    path.parent.mkdir()
    path.write_text(json.dumps({"model": "opus", "hooks": {"Stop": [{"hooks": []}]}}))
    assert ensure_hook(path) is True
    assert ensure_hook(path) is False
    data = json.loads(path.read_text())
    assert data["model"] == "opus" and "Stop" in data["hooks"]
    commands = [h["command"] for g in data["hooks"]["PostToolUse"] for h in g["hooks"]]
    assert commands == [HOOK_COMMAND]
