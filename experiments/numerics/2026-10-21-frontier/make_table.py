"""
make_table.py -- сводная таблица по всем примерам: глубина (beta, a), направление дна, показатель смещения дна, ширины, число ветвей
равной глубины, стрельба назад.  Читает out/*.json, traj/*.json, iso_*.json, summary/*.json.  Пишет table.md, table.json.  [Эксперимент]
"""
import os, json, math, glob
import numpy as np
import mpmath as mp
mp.mp.dps = 40


def lg(s):
    return float(mp.log10(abs(mp.mpf(s))))
HERE = os.path.dirname(os.path.abspath(__file__))
import fcat

cat = {e['id']: e for e in fcat.CAT}
iso = {}
for f in sorted(glob.glob(os.path.join(HERE, 'iso_*.json'))):
    for r in json.load(open(f)):
        iso[r['id']] = r        # последний файл перекрывает (порядок имён)


def slope(xs, ys):
    return float(np.polyfit(xs, ys, 1)[0])


def data(eid):
    p = os.path.join(HERE, 'out', eid + '.json')
    if not os.path.exists(p):
        return None
    d = json.load(open(p))['radii']
    pe = os.path.join(HERE, 'out', eid + '.ext.json')
    if os.path.exists(pe):
        d = d + json.load(open(pe))['radii']
    return d


def row(eid):
    e = cat[eid]
    d = data(eid)
    if not d:
        return None
    lr = [r['logr'] for r in d]
    best = [r['minima'][0] for r in d]
    lm = [lg(b['m']) for b in best]
    k = 5
    beta = slope(lr[-k:], lm[-k:])
    a = 10 ** (lm[-1] - beta * lr[-1])
    w = np.array([float(c) for c in best[-1]['w']])
    seeds = [np.array(s, float) / np.linalg.norm(s) for s in e['seeds']]
    def dist(W):
        return min(float(np.linalg.norm(W - s)) for s in seeds)
    ds = [dist(np.array([float(c) for c in b['w']])) for b in best]
    dexp = slope(lr[-k:], [math.log10(x) for x in ds[-k:]]) if min(ds[-k:]) > 0 else None
    last = d[-1]['minima']
    neq = sum(1 for it in last if float(it['ratio']) >= 0.99)
    near = sorted(float(it['ratio']) for it in last if float(it['ratio']) < 0.99)
    comp = near[-1] if near else None
    # ширины
    c = {}
    pts = [(r['logr'], b) for r, b in zip(d, best) if 'widths_angle' in b]
    for ax in (0, 1):
        xs, ys = [], []
        for (l, b) in pts[-4:]:
            vals = [float(v) for v in b['widths_angle'][ax] if v is not None]
            if vals:
                xs.append(l)
                ys.append(math.log10(sum(vals) / len(vals)))
        if len(xs) >= 3:
            c[ax] = 1 + slope(xs, ys)
    hs = None
    try:
        hs = []
        for i in (0, 1):
            ys = [lg(b['lam_phys'][i]) for b in best[-5:]]
            hs.append(slope(lr[-5:], ys))        # показатель γ_i: λ_i ~ r^γ_i  (физический гессиан = (гессиан по сфере)/r^2)
    except Exception:
        hs = None
    tr = None
    pt = os.path.join(HERE, 'traj', eid + '.json')
    if os.path.exists(pt):
        tr = json.load(open(pt))['verdict']
    return dict(id=eid, group=e['group'], rmin=lr[-1], beta=beta, a=a, w=w.tolist(), dexp=dexp, d_last=ds[-1], neq=neq, comp=comp,
                c=c, hs=hs, traj=tr)


if __name__ == '__main__':
    rows = []
    for e in fcat.CAT:
        r = row(e['id'])
        if r:
            rows.append(r)
    L = ['| № | гр. | r_min | β (fit) | a | ω(r_min) | смещение дна δ ~ r^p | ветвей равной глубины / лучший конкурент | c (e1, e2) | показатели γ_i гессиана (λ_i ~ r^γ_i) | стрельба назад (p_fit; сходится) |',
         '|---|---|---|---|---|---|---|---|---|---|---|']
    for r in rows:
        c = r['c']
        ct = ', '.join(f"{c[i]:.3f}" if i in c else '—' for i in (0, 1))
        hs = '; '.join(f"{v:.2f}" for v in r['hs']) if r['hs'] else '—'
        tr = r['traj']
        trt = '—'
        if tr:
            if tr.get('p_fit') is not None:
                trt = f"p={tr['p_fit']:.2f}; {'да' if tr.get('entries_converge') else 'НЕТ/медленно'}"
            else:
                dd = tr.get('entry_dists') or []
                trt = ('мало точек (' + ', '.join(f'{x:.1e}' for x in dd) + '): ' + ('убывают быстро' if len(dd) >= 2 and all(dd[k + 1] < 0.1 * dd[k] for k in range(len(dd) - 1)) else '?')) if dd else '—'
        dx = f"{r['dexp']:.3f}" if r['dexp'] is not None else '(δ=0)'
        comp = f"{r['neq']} / {r['comp']:.4f}" if r['comp'] is not None else f"{r['neq']} / —"
        L.append(f"| {r['id']} | {r['group']} | 1e{r['rmin']:g} | {r['beta']:.4f} | {r['a']:.5g} | ({r['w'][0]:.6f}, {r['w'][1]:.3e}, {r['w'][2]:.6f}) | {dx} | {comp} | {ct} | {hs} | {trt} |")
    open(os.path.join(HERE, 'table.md'), 'w').write('\n'.join(L) + '\n')
    json.dump(rows, open(os.path.join(HERE, 'table.json'), 'w'), indent=1)
    print('\n'.join(L))
