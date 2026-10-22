#!/bin/bash
# Сертификация изолированности D3, D4, V3 (двойное насыщение K=(J:p1^inf):p2^inf, Singular).  Память сервера ~7 ГБ, поэтому ПОСЛЕДОВАТЕЛЬНО:
#  фаза 1: над F_32003 (быстрый индикатор, iso_sat2_p.py), фаза 2: над Q (сертификат, iso_sat2.py из папки frontier; дописывает iso_sat2.txt).
# Первая попытка (3 процесса параллельно, ulimit -v 2.3 ГБ) упала: Singular: "no more memory".  Здесь ulimit -v 3.4 ГБ и по одному процессу.
# Запуск:  setsid nohup bash queue_sat2.sh > logs/queue_sat2.log 2>&1 < /dev/null &      PID записывается в logs/queue_sat2.pid
FR=/home/claudeagent/arnold/experiments/numerics/2026-10-21-frontier
HERE=$(cd "$(dirname "$0")" && pwd)
echo $$ > "$HERE/logs/queue_sat2.pid"
ulimit -v 3400000
for ID in D3 D4 V3; do
  echo "$(date) phase1 (F_p) $ID"
  ( cd "$HERE"; timeout 3000 ~/venv/bin/python -u iso_sat2_p.py $ID > "$HERE/logs/satp_$ID.log" 2>&1; echo "$(date) satp $ID exit=$?" )
done
for ID in D3 D4 V3; do
  echo "$(date) phase2 (Q) $ID"
  ( cd "$FR"; ~/venv/bin/python -u iso_sat2.py $ID > "$HERE/logs/sat2_$ID.log" 2>&1; echo "$(date) sat2 $ID exit=$?" )
done
echo "$(date) queue done"
