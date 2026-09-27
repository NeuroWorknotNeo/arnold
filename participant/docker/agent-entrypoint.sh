#!/bin/bash
# Подготовка тома агента и запуск цикла работы (или переданной команды).
set -euo pipefail
mkdir -p "$HOME/.claude" "$HOME/.board-runner" "$HOME/.cache" /work/inbox /work/scratch
python3 -m board.setup_claude
if [ "$#" -gt 0 ]; then
    exec "$@"
fi
exec python3 -m board.runner
