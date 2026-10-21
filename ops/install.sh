#!/usr/bin/env bash
# Однократная настройка сервера для главного агента. Запускать от root:
#   bash /root/arnold/ops/install.sh
# Повторный запуск безопасен: уже сделанное пропускается.
# Переменные: AGENT_USER (по умолчанию claudeagent), SERVICE (arnold-agent).
set -euo pipefail

AGENT_USER="${AGENT_USER:-claudeagent}"
SERVICE="${SERVICE:-arnold-agent}"

say() { printf '\n== %s\n' "$*"; }
die() { printf 'ОШИБКА: %s\n' "$*" >&2; exit 1; }

[ "$(id -u)" = 0 ] || die "запустите от root: bash $0"
id "$AGENT_USER" >/dev/null 2>&1 || die "нет пользователя $AGENT_USER"
cd /  # команды от имени $AGENT_USER не должны стартовать в недоступной ему /root
AGENT_HOME="$(getent passwd "$AGENT_USER" | cut -d: -f6)"
REPO="$AGENT_HOME/arnold"
[ -d "$REPO/.git" ] || die "нет клона репозитория в $REPO"
[ -f "$REPO/ops/arnold-agent.sh" ] || die "в $REPO нет ops/arnold-agent.sh: выполните sudo -iu $AGENT_USER git -C $REPO pull"
sudo -u "$AGENT_USER" test -x "$AGENT_HOME/.local/bin/claude" \
  || die "у $AGENT_USER нет Claude Code: sudo -iu $AGENT_USER bash -c 'curl -fsSL https://claude.ai/install.sh | bash'"

say "Пакеты: tmux, python3-venv"
need=()
command -v tmux >/dev/null 2>&1 || need+=(tmux)
python3 -c 'import ensurepip' >/dev/null 2>&1 || need+=(python3-venv)
if [ "${#need[@]}" -gt 0 ]; then
  apt-get update -qq
  DEBIAN_FRONTEND=noninteractive apt-get install -y -qq "${need[@]}"
else
  echo "уже установлены"
fi

say "Python-окружение $AGENT_HOME/venv (sympy, mpmath, numpy, scipy)"
if [ ! -x "$AGENT_HOME/venv/bin/python" ]; then
  sudo -u "$AGENT_USER" -H python3 -m venv "$AGENT_HOME/venv"
fi
sudo -u "$AGENT_USER" -H "$AGENT_HOME/venv/bin/pip" install -q --upgrade pip sympy mpmath numpy scipy
echo "готово"

say "Claude Code у $AGENT_USER: хранить историю сессий год (по умолчанию 30 дней)"
sudo -u "$AGENT_USER" -H python3 - <<'PY'
import json, pathlib, sys
path = pathlib.Path.home() / ".claude" / "settings.json"
try:
    data = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
except ValueError as exc:
    sys.exit(f"ОШИБКА: {path} — не JSON ({exc}); исправьте файл и запустите скрипт снова")
data["cleanupPeriodDays"] = max(int(data.get("cleanupPeriodDays") or 0), 365)
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"{path}: cleanupPeriodDays = {data['cleanupPeriodDays']}")
PY

say "Вход Claude Code у $AGENT_USER"
auth="$(sudo -iu "$AGENT_USER" claude auth status 2>/dev/null || true)"
if printf '%s' "$auth" | grep -q '"authMethod": *"claude.ai"'; then
  echo "вход через claude.ai есть"
else
  echo "ВНИМАНИЕ: нет входа через claude.ai, без него Remote Control не работает."
  echo "Выполните: sudo -iu $AGENT_USER claude auth login"
fi

say "Git у $AGENT_USER"
if ! sudo -iu "$AGENT_USER" git config --global user.email >/dev/null; then
  sudo -iu "$AGENT_USER" git config --global user.name "Главный агент (Claude)"
  sudo -iu "$AGENT_USER" git config --global user.email "$AGENT_USER@$(hostname)"
  echo "задано имя автора коммитов: Главный агент (Claude)"
fi
if sudo -iu "$AGENT_USER" gh auth status >/dev/null 2>&1; then
  sudo -iu "$AGENT_USER" gh auth setup-git
  echo "git отправляет на GitHub через вход gh"
else
  echo "ВНИМАНИЕ: gh не авторизован, агент не сможет отправлять коммиты."
  echo "Выполните: sudo -iu $AGENT_USER gh auth login"
fi

say "Служба $SERVICE"
sed -e "s|/home/claudeagent|$AGENT_HOME|g" -e "s|^User=claudeagent|User=$AGENT_USER|" \
  "$REPO/ops/arnold-agent.service" > "/etc/systemd/system/$SERVICE.service"
systemctl daemon-reload
systemctl enable "$SERVICE" >/dev/null 2>&1
echo "служба установлена и включена в автозапуск"

cat <<EOF

Готово. Дальше:
  1) systemctl start $SERVICE
  2) sudo -iu $AGENT_USER tmux attach -t arnold
     Ответьте на вопросы Claude Code: доверять папке — да, включить Remote Control — да.
     Выйти, не останавливая агента: Ctrl+B, затем D.
     Уведомления на телефон уже включены, разрешите их приложению Claude на телефоне.
  3) В приложении Claude откройте сессию «Арнольд — главный».
Подробности и команды — $REPO/ops/README.md
EOF
