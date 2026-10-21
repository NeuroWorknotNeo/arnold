#!/usr/bin/env bash
# Главный агент: интерактивная сессия Claude Code с Remote Control.
# Запускается службой arnold-agent внутри tmux от имени claudeagent и перезапускает Claude Code,
# если тот завершился. После первого удачного запуска продолжает тот же разговор (--continue).
#
# Вручную (от claudeagent, внутри tmux): bash ~/arnold/ops/arnold-agent.sh
set -u

REPO="${ARNOLD_REPO:-$HOME/arnold}"
NAME="${ARNOLD_SESSION_NAME:-Арнольд — главный}"
MODEL="${ARNOLD_MODEL:-claude-opus-5-5}"
EFFORT="${ARNOLD_EFFORT:-max}"
STATE_DIR="$HOME/.arnold-agent"

export PATH="$HOME/.local/bin:$PATH"
# Вход — через claude.ai (/login). API-ключ списывал бы деньги с API, токен setup-token не
# поддерживает Remote Control, а CLAUDE_CODE_EFFORT_LEVEL перебил бы effort подагентов.
unset ANTHROPIC_API_KEY CLAUDE_CODE_OAUTH_TOKEN CLAUDE_CODE_EFFORT_LEVEL ANTHROPIC_MODEL

START_PROMPT='Ты запущен как главный агент исследования задачи Арнольда 1971-4 (A). Прочитай CLAUDE.md, orchestrator/PLAN.md и orchestrator/LOG.md, заведи пульс (раздел «Работа без владельца: пульс» в CLAUDE.md) и начинай работу по плану. Владельцу коротко напиши, с чего начал.'
RESUME_PROMPT='[перезапуск] Claude Code был перезапущен: сбой, обновление или перезагрузка сервера. Фоновые подагенты и команды, если они шли, остановлены. Сверься с orchestrator/PLAN.md и концом orchestrator/LOG.md. Если в плане стоит пауза, ничего не делай. Иначе проверь пульс (CronList: ровно одна задача; нет — заведи), перезапусти прерванное и продолжай работу.'

cd "$REPO" || { echo "Нет папки $REPO" >&2; exit 1; }
mkdir -p "$STATE_DIR"
command -v claude >/dev/null || { echo "Не найден claude в PATH ($PATH)" >&2; exit 1; }

FLAGS=(--remote-control "$NAME" --model "$MODEL" --effort "$EFFORT" --permission-mode bypassPermissions)
fast_fails=0
while true; do
  started=$(date +%s)
  if [ -f "$STATE_DIR/has-session" ] && [ "$fast_fails" -lt 2 ]; then
    mode="continue"
    claude --continue "${FLAGS[@]}" -- "$RESUME_PROMPT"
  else
    mode="new"
    claude "${FLAGS[@]}" -- "$START_PROMPT"
  fi
  code=$?
  ran=$(( $(date +%s) - started ))
  if [ "$ran" -ge 120 ]; then
    # Работал по-настоящему: дальше продолжаем этот разговор.
    touch "$STATE_DIR/has-session"
    fast_fails=0
  else
    # Быстрый выход. Два раза подряд при --continue — значит, продолжать нечего: начнём заново.
    fast_fails=$((fast_fails + 1))
  fi
  echo "$(date '+%F %T') claude ($mode) завершился: код $code, работал $ran с. Перезапуск через 30 с." \
    | tee -a "$STATE_DIR/restarts.log"
  sleep 30
done
