#!/bin/bash
# стрельба назад: основные ветви (orbit 0) и дополнительные ветви с ratio >= 1/2 (orbit k); 5 процессов
cd "$(dirname "$0")"
mkdir -p logs traj
jobs="K2:0 K3:0 K1:0 A1:0 A2:0 A3:0 A4:0 A5:0 A7:0 C1:0 C2:0 D2:0 F1:0 M2:0 P1:0 P3:0 Z1:0 S1:0 A1:1 A2:1 A3:1 D2:1 M2:1 M2:2 M2:3 Z1:1 Z1:2 S1:1"
echo $jobs | tr ' ' '\n' | xargs -P 5 -I{} sh -c 'id=$(echo {} | cut -d: -f1); o=$(echo {} | cut -d: -f2); ~/venv/bin/python -u traj_run.py $id --orbit $o > logs/traj2_${id}_o$o.log 2>&1'
echo T2DONE > logs/T2DONE
