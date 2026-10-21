#!/bin/bash
# проекционные ширины: дописывает wid2 в out/ID.json (после run_all.sh)
cd "$(dirname "$0")"
ids="K2 K3 K1 A1 A2 A3 A4 A5 A7 C1 C2 D1 D2 F1 M1 M2 P1 P3 P4 Z1 S1 T1"
echo $ids | tr ' ' '\n' | xargs -P 7 -I{} sh -c '~/venv/bin/python -u widths.py {} > logs/w_{}.log 2>&1'
echo WDONE > logs/WDONE
