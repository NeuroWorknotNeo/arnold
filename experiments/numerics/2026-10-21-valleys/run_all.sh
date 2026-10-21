#!/bin/bash
# параллельный запуск (7 процессов); лог каждого примера в logs/ID.log
cd "$(dirname "$0")"
mkdir -p logs out
ids="K2 K3 K1 A1 A2 A3 A4 A5 A7 C1 C2 D1 D2 F1 M1 M2 P1 P3 P4 Z1 S1 T1"
echo $ids | tr ' ' '\n' | xargs -P 7 -I{} sh -c '~/venv/bin/python -u run_valleys.py {} > logs/{}.log 2>&1'
echo ALLDONE > logs/ALLDONE
