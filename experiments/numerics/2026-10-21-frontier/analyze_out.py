"""
analyze_out.py -- сводка по out/ID.json: m(r), локальный показатель глубины, смещение дна от особого направления (показатель),
гессиан, ширины (показатели c_i), сходимость масштабированного профиля, конкурирующие ветви.  [Эксперимент]
usage: python analyze_out.py ID [ID ...]   -> summary/ID.md, summary/ID.json (+печать)
"""
import sys, os, json, math
import numpy as np
import mpmath as mp
mp.mp.dps = 40


def lg(s):
    return float(mp.log10(abs(mp.mpf(s))))
HERE = os.path.dirname(os.path.abspath(__file__))
import fcat

SUM = os.path.join(HERE, 'summary')
os.makedirs(SUM, exist_ok=True)


def fl(s):
    return float(s)


def slope(xs, ys):
    A = np.vstack([xs, np.ones(len(xs))]).T
    return float(np.linalg.lstsq(A, np.array(ys), rcond=None)[0][0])


def analyze(eid):
    e = {x['id']: x for x in fcat.CAT}[eid]
    d = json.load(open(os.path.join(HERE, 'out', eid + '.json')))['radii']
    res = dict(id=eid, rows=[])
    lr = [rec['logr'] for rec in d]
    best = [rec['minima'][0] for rec in d]
    lm = [lg(b['m']) for b in best]
    W = [np.array([fl(c) for c in b['w']]) for b in best]
    seeds = [np.array(s, float) / np.linalg.norm(s) for s in e['seeds']]
    lines = [f"## {eid}: {e['name']}", '', f"`U = {e['U']}`", '',
             '| log10 r | log10 \\|m\\| | β лок. | n мин. | ω | расст. до особого напр. (δ) | δ-показатель | λ1/λ2 (физ.) | ширины угл. (±, e1; ±, e2) |',
             '|---|---|---|---|---|---|---|---|---|']
    prev_delta = None
    for k, rec in enumerate(d):
        b = best[k]
        w = W[k]
        # особое направление: ближайшее
        sd = min(seeds, key=lambda s: np.linalg.norm(w - s))
        delta = float(np.linalg.norm(w - sd))
        bl = ''
        if k >= 4:
            bl = f"{slope(lr[k-4:k+1], lm[k-4:k+1]) * -1:.4f}"
        dp = ''
        if k >= 4 and delta > 0:
            ds_ = [float(np.linalg.norm(W[j] - min(seeds, key=lambda s: np.linalg.norm(W[j] - s)))) for j in range(k - 4, k + 1)]
            if min(ds_) > 0:
                dp = f"{slope(lr[k-4:k+1], [math.log10(x) for x in ds_]):.3f}"
        lam = b.get('lam_phys')
        lamtxt = f"{fl(lam[0]):.3e} / {fl(lam[1]):.3e}" if lam else ''
        wt = ''
        if 'widths_angle' in b:
            wa = b['widths_angle']
            wt = '; '.join(', '.join('-' if v is None else f"{fl(v):.3e}" for v in row) for row in wa)
        lines.append(f"| {rec['logr']:.2f} | {lm[k]:.5f} | {bl} | {rec['nmin']} | ({w[0]:.8f}, {w[1]:.3e}, {w[2]:.8f}) | {delta:.3e} | {dp} | {lamtxt} | {wt} |")
        res['rows'].append(dict(logr=rec['logr'], logm=lm[k], beta_loc=bl, delta=delta, dp=dp, lam=lam))
    # ширины: показатели
    pts = [(rec['logr'], b) for rec, b in zip(d, best) if 'widths_angle' in b]
    if len(pts) >= 3:
        lines += ['', '**Показатели ширин** (физические ширины w ~ r^c; c = 1 + наклон угловой ширины по log r; последние 4 точки с шириной):']
        for ax in (0, 1):
            ys, xs = [], []
            for (lrr, b) in pts[-4:]:
                vals = [fl(v) for v in b['widths_angle'][ax] if v is not None]
                if vals:
                    xs.append(lrr)
                    ys.append(math.log10(sum(vals) / len(vals)))
            if len(xs) >= 3:
                c = 1 + slope(xs, ys)
                lines.append(f"- направление e{ax+1}: c = {c:.3f}")
                res[f'c{ax+1}'] = c
        # сходимость профиля
        pr = [(rec['logr'], b['profile5']) for rec, b in zip(d, best) if 'profile5' in b]
        if len(pr) >= 2:
            (l1, p1), (l2, p2) = pr[-2], pr[-1]
            P1 = np.array([[fl(v) for v in row] for row in p1])
            P2 = np.array([[fl(v) for v in row] for row in p2])
            lines += ['', f"**Масштабированный профиль** F(s1,s2) = U/|m| на сетке s_i ∈ {{-2,-1,0,1,2}} (s_i — в единицах угловых ширин по e_i), радиус 10^{l2:g}:", '```']
            for row in P2:
                lines.append('  '.join(f"{v:9.3f}" for v in row))
            lines.append('```')
            lines.append(f"max |F(10^{l2:g}) − F(10^{l1:g})| = {np.max(np.abs(P2 - P1)):.3g}")
            res['profile_change'] = float(np.max(np.abs(P2 - P1)))
    # конкурирующие ветви на последних радиусах
    lines += ['', '**Минимумы на последних радиусах (ratio = U/U_глоб.):**']
    for rec in d[-3:]:
        lines.append(f"- r=10^{rec['logr']:g}: " + ', '.join(f"{fl(it['ratio']):.4f}" for it in rec['minima'][:8]))
    open(os.path.join(SUM, eid + '.md'), 'w').write('\n'.join(lines))
    json.dump(res, open(os.path.join(SUM, eid + '.json'), 'w'), indent=1)
    return '\n'.join(lines)


if __name__ == '__main__':
    for a in sys.argv[1:]:
        print(analyze(a))
