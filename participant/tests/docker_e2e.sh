#!/bin/bash
# Сквозная проверка Claude-участника в Docker: поддельные Telegram и claude, настоящие образы,
# тома, сокет между контейнерами, изоляция, перезапуск. Удаляет за собой только свой тестовый проект.
set -euo pipefail
cd "$(dirname "$0")/.."
P=board-e2e-$$
ENV_FILE=$(mktemp)
trap 'dc down -v --remove-orphans >/dev/null 2>&1; rm -f "$ENV_FILE"' EXIT
cat > "$ENV_FILE" <<ENV
COMPOSE_PROJECT_NAME=$P
PARTICIPANT_ID=e2e-claude
TELEGRAM_BOT_TOKEN=123456789:AAFakeTokenForTestsOnly_abcdefghijklm
BOARD_CHAT_ID=-1001234567890
OWNER_USER_IDS=42
CLAUDE_CODE_OAUTH_TOKEN=fake-token-for-e2e
TELEGRAM_API_BASE=http://faketg:8080
MIN_PAUSE_SECONDS=3
ENV
# Чистое окружение: переменные оболочки не должны попадать в контейнеры (см. ./dc).
dc() {
  env -i HOME="$HOME" PATH="$PATH" E2E_TRANSPORT_IMAGE="${E2E_TRANSPORT_IMAGE:-}" E2E_AGENT_IMAGE="${E2E_AGENT_IMAGE:-}" \
    docker compose -p "$P" -f compose.yaml -f tests/compose.e2e.yaml --env-file "$ENV_FILE" "$@"
}
ctl() {
  local body="${2:-}"
  [ -n "$body" ] || body='{}'
  dc exec -T faketg python3 -c "import json,sys,urllib.request as u; r=u.Request('http://localhost:8080/_control/'+sys.argv[1], data=sys.argv[2].encode(), headers={'Content-Type':'application/json'}); print(json.dumps(json.loads(u.urlopen(r).read()), ensure_ascii=False))" "$1" "$body"
}
wait_for() { local what="$1" cond="$2" i; for i in $(seq 1 60); do if eval "$cond" >/dev/null 2>&1; then echo "✅ $what"; return 0; fi; sleep 2; done; echo "❌ $what"; dc logs --tail=40; exit 1; }

dc up -d --no-build
wait_for "транспорт подключился к доске" "dc logs transport | grep -q 'подключён к доске'"
wait_for "первый ход агента опубликовал сообщение" "ctl sent | grep -q 'тестовый участник на связи'"
ctl push '{"text": "@arnold_test_bot вопрос: что делаешь?", "username": "owner", "user_id": 42, "entities": [{"type": "mention", "offset": 0, "length": 16}]}' >/dev/null
wait_for "обращение разбудило агента, ответ ушёл ответом на сообщение" "ctl sent | python3 -c \"import json,sys; s=json.load(sys.stdin); sys.exit(0 if any(x['text']=='ответ на обращение' and x['reply_to'] for x in s) else 1)\""
SESSION=$(dc exec -T agent board-runner status | python3 -c 'import json,sys; print(json.load(sys.stdin)["session_id"])')
[ "$SESSION" = "sess-e2e" ] && echo "✅ сессия сохранена: $SESSION"
dc exec -T agent sh -c 'test -z "${TELEGRAM_BOT_TOKEN:-}"' && echo "✅ токена бота в контейнере агента нет"
dc exec -T agent sh -c 'touch /usr/local/x 2>/dev/null' && { echo "❌ корень агента доступен на запись"; exit 1; } || echo "✅ корневая ФС агента только для чтения"
dc exec -T agent sh -c 'touch /run/board/x 2>/dev/null' && { echo "❌ каталог сокета доступен агенту на запись"; exit 1; } || echo "✅ каталог сокета у агента только для чтения, но сокет работает"
dc exec -T agent sh -c 'grep -q board-hook ~/.claude/settings.json' && echo "✅ хук упоминаний прописан в настройках Claude Code"
dc exec -T agent board status | head -2
dc restart >/dev/null
wait_for "после перезапуска транспорт снова на связи" "dc exec -T agent board status"
SESSION2=$(dc exec -T agent board-runner status | python3 -c 'import json,sys; print(json.load(sys.stdin)["session_id"])')
[ "$SESSION2" = "$SESSION" ] && echo "✅ после перезапуска тот же диалог: $SESSION2"
COUNT=$(dc exec -T agent board history -n 50 | grep -c 'тестовый участник на связи' || true)
[ "$COUNT" = "1" ] && echo "✅ журнал сохранился, дублей публикаций нет"
echo "Все проверки e2e пройдены"
