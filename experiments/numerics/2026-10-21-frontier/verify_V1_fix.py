"""verify_V1_fix.py -- к V1 после расчёта добавлен хвост y^12 (иначе ось y состоит из критических точек). Проверка: дно исправленного V1 при
r = 1e-2, 1e-4, 1e-8, 1e-12 отличается от посчитанного (без y^12) не более чем на указанную величину.  [Эксперимент]"""
import json, os
from flib import *
e = cat()['V1']
P = Pot(e['U'])
d = json.load(open(os.path.join(HERE, 'out', 'V1.json')))['radii'] + json.load(open(os.path.join(HERE, 'out', 'V1.ext.json')))['radii']
lines = []
for lr in (-2, -4, -8, -12):
    rec = [t for t in d if abs(t['logr'] - lr) < 1e-9][0]
    r = mp.mpf(10) ** lr
    w0 = [mp.mpf(c) for c in rec['minima'][0]['w']]
    m0 = mp.mpf(rec['minima'][0]['m'])
    w, U, gt, Ht, ee, ok = newton_min(P, w0, r, maxit=400)
    lines.append(f"r=1e{lr}: ok={ok}  |m_new/m_old - 1| = {mp.nstr(abs(U / m0 - 1), 3)}   |w_new - w_old| = {mp.nstr(nrm([w[i] - w0[i] for i in range(3)]), 3)}")
    print(lines[-1], flush=True)
open(os.path.join(HERE, 'verify_V1_fix.txt'), 'w').write('\n'.join(lines) + '\n')
