#!/bin/bash
# R26: batch of (A5) scans; outputs scan_out/*.txt, summary in scan_A5.out
cd "$(dirname "$0")"
PY=~/venv/bin/python
mkdir -p scan_out
run() { $PY scan_A5.py "$@" > "scan_out/p$1_d$2_k$3_s$4.txt" 2>&1; }
run 2 1e-4 proof 1e-14 15 &
run 2 1e-4 0.5 1e-14 15 &
run 2 1e-4 0.05 1e-14 15 &
run 2 1e-6 proof 1e-16 15 &
run 2 1e-6 0.5 1e-16 15 &
run 2 1e-6 0.01 1e-16 15 &
wait
run 3 1e-5 proof 1e-16 15 &
run 3 1e-5 0.5 1e-16 15 &
run 3 1e-5 0.005 1e-16 15 &
run 3 1e-7 proof 1e-18 15 &
run 3 1e-7 0.5 1e-18 15 &
run 1 1e-4 0.5 1e-14 15 &
wait
run 2 1e-4 proof 1e-6 15 &
run 3 1e-5 proof 1e-6 15 &
run 1 1e-6 0.5 1e-16 15 &
wait
for f in scan_out/*.txt; do cat "$f"; echo; done > scan_A5.out
