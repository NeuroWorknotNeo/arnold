import json
import os
import stat
import sys
import time
from pathlib import Path

import pytest

from board.config import AgentConfig
from board.runner import Runner, RunnerState, parse_stream, reset_time
from tests.fake_telegram import BOT_USERNAME, OWNER_ID

ROOT = Path(__file__).resolve().parents[1]
FAKE = Path(__file__).with_name("fake_claude.py")


@pytest.fixture
def harness(tmp_path, client):
    fake_dir = tmp_path / "fake"
    fake_dir.mkdir()
    exe = tmp_path / "claude"
    exe.write_text(f"#!/bin/sh\nexec {sys.executable} {FAKE} \"$@\"\n")
    exe.chmod(exe.stat().st_mode | stat.S_IEXEC)
    work = tmp_path / "work"
    work.mkdir()

    def make(scenario, **overrides):
        (fake_dir / "scenario.json").write_text(json.dumps(scenario))
        params = dict(participant_id="test-claude", socket_path=client.socket_path, workdir=str(work),
                      claude_bin=str(exe), min_pause=120, turn_timeout=20, state_dir=str(tmp_path / "state"))
        params.update(overrides)
        cfg = AgentConfig(**params)
        env = dict(os.environ, FAKE_CLAUDE_DIR=str(fake_dir), PYTHONPATH=str(ROOT), BOARD_SOCKET=client.socket_path)
        return Runner(cfg, client, env=env)

    def calls():
        path = fake_dir / "calls.jsonl"
        return [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []

    return make, calls


def prompt_of(call):
    argv = call["argv"]
    return argv[argv.index("--") + 1]


def test_first_turn_then_resume_on_mention(harness, service, fake_tg):
    make, calls = harness
    runner = make([{"kind": "ok", "session": "sess-A"}])
    assert runner.step() == 1
    first = calls()[0]
    assert "--resume" not in first["argv"] and "первый ход" in prompt_of(first)
    assert "--dangerously-skip-permissions" in first["argv"] and "--append-system-prompt" in first["argv"]
    brief = first["argv"][first["argv"].index("--append-system-prompt") + 1]
    assert f"@{BOT_USERNAME}" in brief and str(OWNER_ID) in brief
    assert runner.state.session_id == "sess-A" and runner.state.turns == 1
    assert RunnerState.load(runner.cfg.state_path).session_id == "sess-A"

    # Пауза между ходами: без обращений новый ход не начинается.
    assert runner.step() <= 30 and len(calls()) == 1
    fake_tg.push_message(f"@{BOT_USERNAME} есть вопрос", username="bob")
    service.poll_once()
    assert runner.step() == 1
    second = calls()[1]
    assert second["argv"][second["argv"].index("--resume") + 1] == "sess-A"
    assert "Непрочитанных обращений к тебе: 1" in prompt_of(second)
    assert runner.state.turns == 2


def test_agent_requested_sleep(harness, service):
    make, calls = harness
    runner = make([{"kind": "ok", "command": f"{sys.executable} -m board.cli sleep 600 'жду расчёт'"},
                   {"kind": "ok"}], min_pause=0)
    runner.step()
    assert service.op_control({})["sleep_until"] > time.time() + 500
    assert runner.step() <= 30 and len(calls()) == 1  # спит, ход не начат
    service.journal.set_meta("sleep_until", int(time.time()) - 1)
    runner.step()
    assert len(calls()) == 2
    assert "жду расчёт" in prompt_of(calls()[1]) and "закончилось" in prompt_of(calls()[1])
    assert service.op_control({})["sleep_until"] is None


def test_rate_limit_waits_even_for_mentions(harness, service, fake_tg):
    make, calls = harness
    runner = make([{"kind": "ok"}, {"kind": "rate_limit"}], min_pause=0)
    runner.step()
    runner.step()
    assert runner.state.hard_until >= time.time() + 170
    assert "лимит" in runner.state.last_error
    fake_tg.push_message(f"@{BOT_USERNAME} срочно", username="bob")
    service.poll_once()
    runner.step()
    assert len(calls()) == 2


def test_broken_session_recovers_with_new_session(harness):
    make, calls = harness
    runner = make([{"kind": "ok", "session": "sess-old"}, {"kind": "broken"}, {"kind": "ok", "session": "sess-new"}],
                  min_pause=0)
    runner.step()
    runner.step()
    assert runner.state.session_id is None and runner.state.pending_recovery
    runner.state.soft_until = 0
    runner.step()
    third = calls()[2]
    assert "--resume" not in third["argv"] and "новая сессия" in prompt_of(third)
    assert runner.state.session_id == "sess-new" and runner.state.pending_recovery is None


def test_timeout_kills_hanging_turn(harness):
    make, calls = harness
    runner = make([{"kind": "hang", "sleep": 60}], turn_timeout=2)
    started = time.monotonic()
    runner.step()
    assert time.monotonic() - started < 40
    assert runner.state.last_subtype == "timeout" and "TURN_TIMEOUT" in runner.state.last_error


def test_pause_blocks_turns(harness, service):
    make, calls = harness
    runner = make([{"kind": "ok"}])
    service.journal.set_meta("paused", 1)
    assert runner.step() == 30 and calls() == []


def test_auth_error_alerts_owner_once(harness, fake_tg):
    make, calls = harness
    runner = make([{"kind": "auth"}])
    runner.step()
    assert runner.state.last_error == "Claude Code не авторизован"
    dms = [s for s in fake_tg.sent if s["params"]["chat_id"] == OWNER_ID]
    assert len(dms) == 1 and "CLAUDE_CODE_OAUTH_TOKEN" in dms[0]["params"]["text"]
    runner.state.hard_until = 0
    runner.step()
    assert len([s for s in fake_tg.sent if s["params"]["chat_id"] == OWNER_ID]) == 1


def test_daily_cap(harness):
    make, calls = harness
    runner = make([{"kind": "ok"}], min_pause=0, max_turns_per_day=1)
    runner.step()
    assert runner.step() == 300 and len(calls()) == 1


def test_parse_stream_and_reset_time():
    lines = [
        '{"type":"system","subtype":"init","session_id":"s1","model":"m"}',
        "не json",
        '{"type":"rate_limit_event","rate_limit_info":{"status":"allowed_warning","resetsAt":1760000000000}}',
        '{"type":"result","subtype":"success","is_error":false,"result":"ok","session_id":"s1","num_turns":2}',
    ]
    res = parse_stream(lines)
    assert res.session_id == "s1" and not res.is_error and res.num_turns == 2 and res.model == "m"
    assert reset_time(res.rate_limit) == 1760000000
    assert reset_time({"resetsAt": "2026-09-27T10:00:00Z"}) is not None
