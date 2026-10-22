"""verify_V3_fix.py -- у V3 хвост y^8 (степень 8 < m = 16, ломал изолированность ω) заменён на y^16. Проверка: дно нового многочлена при r = 1e-2, 1e-4, 1e-6 отличается от посчитанного (с y^8) не более чем на указанную величину.  [Эксперимент]"""
import json, os
from flib import *
e = cat()['V3']
P = Pot(e['U'])
d = json.load(open(os.path.join(HERE, 'out', 'V3.json')))['radii']
lines = []
for lr in (-2, -4, -6):
    rec = [t for t in d if abs(t['logr'] - lr) < 1e-9][0]
    r = mp.mpf(10) ** lr
    w0 = [mp.mpf(c) for c in rec['minima'][0]['w']]
    m0 = mp.mpf(rec['minima'][0]['m'])
    w, U, gt, Ht, ee, ok = newton_min(P, w0, r, maxit=400)
    lines.append(f"r=1e{lr}: ok={ok}  |m_new/m_old - 1| = {mp.nstr(abs(U / m0 - 1), 3)}   |w_new - w_old| = {mp.nstr(nrm([w[i] - w0[i] for i in range(3)]), 3)}")
    print(lines[-1], flush=True)
open(os.path.join(HERE, 'verify_V3_fix.txt'), 'w').write('\n'.join(lines) + '\n')
