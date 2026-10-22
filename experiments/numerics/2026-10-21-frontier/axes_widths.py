"""
axes_widths.py -- ширины профиля {U < m/2} вдоль КООРДИНАТНЫХ направлений y и z (проекции на касательную плоскость сферы в точке дна),
а не вдоль собственных направлений гессиана: нужна для ориентации (какая из поперечных координат шире) в классе (в).  [Эксперимент]
usage: python axes_widths.py ID logr1,logr2,...   ->  out/ID.axes.json
"""
import sys, os, json
from flib import *


def load(eid):
    d = json.load(open(os.path.join(HERE, 'out', eid + '.json')))['radii']
    pe = os.path.join(HERE, 'out', eid + '.ext.json')
    if os.path.exists(pe):
        d += json.load(open(pe))['radii']
    return d


def gs(v, basis):
    for b in basis:
        c = dot(v, b)
        v = [v[i] - c * b[i] for i in range(3)]
    return unit(v)


def main(eid, lrs):
    e = cat()[eid]
    P = Pot(e['U'])
    d = load(eid)
    out = []
    for lr in lrs:
        rec = min(d, key=lambda t: abs(t['logr'] - lr))
        if abs(rec['logr'] - lr) > 1e-9:
            print('нет радиуса', lr)
            continue
        r = mp.mpf(10) ** mp.mpf(rec['logr'])
        w = [mp.mpf(c) for c in rec['minima'][0]['w']]
        w, U, gt, Ht, ee, ok = newton_min(P, w, r, maxit=400)
        w = unit(w)
        ey = gs([mp.mpf(0), mp.mpf(1), mp.mpf(0)], [w])
        ez = gs([mp.mpf(0), mp.mpf(0), mp.mpf(1)], [w, ey])
        res = dict(logr=lr)
        for name, (va, vb) in (('y', (ey, ez)), ('z', (ez, ey))):
            ws = []
            for sg in (1, -1):
                try:
                    ws.append(profile_width(P, r, w, va, vb, U, sign=sg))
                except Exception:
                    ws.append(None)
            res['w_' + name] = [None if v is None else mp.nstr(v, 10) for v in ws]
        out.append(res)
        print(eid, lr, res, flush=True)
    json.dump(out, open(os.path.join(HERE, 'out', eid + '.axes.json'), 'w'), indent=1)


if __name__ == '__main__':
    main(sys.argv[1], [float(t) for t in sys.argv[2].split(',')])
