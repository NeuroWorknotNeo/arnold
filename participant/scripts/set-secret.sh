#!/bin/bash
# Записать секрет в .env, не показывая его на экране и не оставляя в истории команд.
# Использование (из каталога participant):  bash scripts/set-secret.sh TELEGRAM_BOT_TOKEN
# Вставьте значение и нажмите Enter. Пробелы и переносы строк по краям убираются.
set -euo pipefail

name="${1:-}"
env_file="${2:-.env}"
case "$name" in
  TELEGRAM_BOT_TOKEN|CLAUDE_CODE_OAUTH_TOKEN|GH_TOKEN|ARCHIVE_GITHUB_TOKEN) ;;
  *) echo "Использование: $0 TELEGRAM_BOT_TOKEN|CLAUDE_CODE_OAUTH_TOKEN|GH_TOKEN|ARCHIVE_GITHUB_TOKEN [файл .env]" >&2
     exit 2 ;;
esac
[ -f "$env_file" ] || { echo "Нет файла $env_file: сначала cp .env.example .env" >&2; exit 2; }

printf 'Вставьте значение %s и нажмите Enter (ввод не отображается): ' "$name" >&2
IFS= read -rs value
echo >&2
value="$(printf '%s' "$value" | tr -d '[:space:]')"
[ -n "$value" ] || { echo "Пустое значение — ничего не изменено" >&2; exit 1; }

if [ "$name" = "TELEGRAM_BOT_TOKEN" ] && ! [[ "$value" =~ ^[0-9]{5,}:[A-Za-z0-9_-]{30,}$ ]]; then
  echo "Это не похоже на токен бота (ожидается 123456789:AA…). Ничего не изменено." >&2
  exit 1
fi
if [ "$name" = "CLAUDE_CODE_OAUTH_TOKEN" ] && [[ "$value" != sk-ant-* ]]; then
  echo "Предупреждение: токен из 'claude setup-token' обычно начинается с sk-ant-. Проверьте, что скопирован целиком." >&2
fi

tmp="$(mktemp "${env_file}.XXXXXX")"
chmod 600 "$tmp"
grep -v "^${name}=" "$env_file" > "$tmp" || true
printf '%s=%s\n' "$name" "$value" >> "$tmp"
mv "$tmp" "$env_file"
chmod 600 "$env_file"
echo "Готово: $name записан в $env_file (длина ${#value} символов). Перезапуск: docker compose up -d" >&2
