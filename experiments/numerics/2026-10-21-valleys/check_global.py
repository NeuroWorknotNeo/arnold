"""
check_global.py -- контроль глобальности найденного минимума: сравнение m(r) (mpmath, out/ID.json) с минимумом по плотной сетке
2400 x 4800 (double) на сферах r = 0.1, 0.03, 0.01.  Сетка может только пропустить тонкие рога (она даёт верхнюю оценку min U);
если сетка нашла значение НИЖЕ нашего m(r) -- это ошибка поиска.   [Эксперимент]
"""
import json, os, sys
import numpy as np
from vlib import *

ids = sys.argv[1:] or ['K1','K2','K3','A1','A2','A3','A4','A5','A7','C1','C2','D1','D2','F1','M1','M2','P1','P3','P4','Z1','S1','T1']
cat = load_catalog()
lines = []
for eid in ids:
    P = Pot(cat[eid]['U'])
    d = json.load(open(os.path.join(HERE, 'out', eid + '.json')))
    th = np.linspace(0, np.pi, 2400)
    ph = np.linspace(0, 2 * np.pi, 4800, endpoint=False)
    TH, PH = np.meshgrid(th, ph, indexing='ij')
    sx, sy, sz = np.sin(TH) * np.cos(PH), np.sin(TH) * np.sin(PH), np.cos(TH)
    for lr in (-1, -1.5, -2):
        r = 10 ** lr
        V = P.un(r * sx, r * sy, r * sz) + 0 * sx
        gmin = float(V.min())
        rec = [x for x in d['radii'] if abs(x['logr'] - lr) < 1e-9][0]
        mine = float(mp.mpf(rec['minima'][0]['m']))
        ok = 'OK' if mine <= gmin * (1 - 1e-12) or mine <= gmin + abs(gmin) * 1e-9 else 'CHECK!!'
        lines.append(f"{eid} r=1e{lr}: grid min = {gmin:.6e}, ours = {mine:.6e}, ratio ours/grid = {mine / gmin:.6f}  {ok}")
        print(lines[-1], flush=True)
open(os.path.join(HERE, 'check_global.txt'), 'w').write("\n".join(lines))
