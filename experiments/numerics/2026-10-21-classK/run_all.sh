#!/bin/bash
# reproduce everything (about 3-4 minutes on one core; all parts deterministic, no random numbers, no seed)
cd "$(dirname "$0")"
PY=${PY:-$HOME/venv/bin/python}
mkdir -p out logs
$PY test_fibre.py                          # engine vs. known formulas of the note (K2, K3)
for e in K1 K2 K3 A1 A2 A3 A4 A5 A7 C1 C2 D1 D2 F1 M1 M2 P1 P3 P4 Z1 S1; do $PY classk_analyze.py $e > logs/$e.log 2>&1; done
$PY t1.py > logs/T1.log 2>&1               # T1: exact critical points of G=u_8|Sigma
$PY d1_next.py > logs/D1_next.log 2>&1     # D1: g_9, g_10
$PY sigma_checks.py > sigma_checks.txt     # smoothness of cones, D^2 u_m = 0 for non-Morse-Bott
$PY shift_flags.py > shift_flags.txt       # where the shift eta* matters
$PY verify.py K2 K3 A1 A2 A3 A5 A7 C1 C2 D2 F1 Z1 S1 P3 P4 > verify.txt   # brute force min over the normal line
$PY verify_extra.py > verify_extra.txt     # A4 cascade g_7, D1 constant G
$PY gpp_check.py > gpp_check.txt           # independent formula for G'' when j=m+1
$PY summarize.py > summarize.log
$PY make_table.py > /dev/null
$PY make_details.py
