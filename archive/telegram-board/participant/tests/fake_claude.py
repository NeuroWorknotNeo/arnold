#!/usr/bin/env python3
"""Поддельный ``claude -p`` для тестов цикла: печатает stream-json по сценарию.

Каталог FAKE_CLAUDE_DIR содержит scenario.json (список поведений, по одному на запуск)
и calls.jsonl (сюда дописываются аргументы каждого запуска).
"""

import json
import os
import subprocess
import sys
import time
from pathlib import Path

d = Path(os.environ["FAKE_CLAUDE_DIR"])
d.mkdir(parents=True, exist_ok=True)
calls = d / "calls.jsonl"
index = len(calls.read_text().splitlines()) if calls.exists() else 0
with calls.open("a") as fh:
    fh.write(json.dumps({"argv": sys.argv[1:], "cwd": os.getcwd()}) + "\n")
scenario = json.loads(Path(os.environ.get("FAKE_CLAUDE_SCENARIO") or d / "scenario.json").read_text())
step = scenario[min(index, len(scenario) - 1)]
kind = step.get("kind", "ok")
session = step.get("session", "sess-1")
if "--resume" in sys.argv:
    session = sys.argv[sys.argv.index("--resume") + 1]


def emit(event):
    print(json.dumps(event), flush=True)


emit({"type": "system", "subtype": "init", "session_id": session, "model": "claude-test"})
if step.get("command"):
    subprocess.run(step["command"], shell=True, check=False)
if kind == "ok":
    emit({"type": "assistant", "message": {"content": [{"type": "text", "text": "работаю"}]}})
    emit({"type": "result", "subtype": "success", "is_error": False, "result": step.get("text", "готово"),
          "session_id": session, "num_turns": 3, "duration_ms": 1000})
elif kind == "rate_limit":
    emit({"type": "rate_limit_event",
          "rate_limit_info": {"status": "rejected", "resetsAt": int(time.time()) + 120, "rateLimitType": "five_hour"}})
    emit({"type": "result", "subtype": "success", "is_error": True, "result": "You've hit your usage limit",
          "session_id": session})
elif kind == "broken":
    emit({"type": "result", "subtype": "error_during_execution", "is_error": True,
          "result": "[ede_diagnostic] result_type=user", "session_id": session})
elif kind == "auth":
    emit({"type": "result", "subtype": "success", "is_error": True, "result": "Not logged in · Please run /login"})
elif kind == "hang":
    time.sleep(step.get("sleep", 60))
sys.exit(step.get("exit", 0))
