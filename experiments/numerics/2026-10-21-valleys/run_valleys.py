"""
run_valleys.py -- для каждого примера: m(r), точки минимума, гессиан на сфере, ширины, на радиусах r = 10^-1 ... 10^-6.
Использование:  python run_valleys.py ID [ID ...]  [--quick]     (результат: out/ID.json)
[Эксперимент]; seed генератора = 20261021.
"""
import sys, os, json, time
import numpy as np
from vlib import *
from curves import *

SEED = 20261021
OUT = os.path.join(HERE, 'out')
os.makedirs(OUT, exist_ok=True)

EXPS = [-1, -1.5, -2, -2.5, -3, -3.5, -4, -4.5, -5, -5.5, -6]
DS = 0.025


def eigdirs(Ht, e):
    a, b, d = Ht[0][0], Ht[0][1], Ht[1][1]
    psi = mp.atan2(2 * b, a - d) / 2
    c, s = mp.cos(psi), mp.sin(psi)
    v1 = [c * e[0][i] + s * e[1][i] for i in range(3)]
    v2 = [-s * e[0][i] + c * e[1][i] for i in range(3)]
    l1 = c * c * a + 2 * c * s * b + s * s * d
    l2 = s * s * a - 2 * c * s * b + c * c * d
    return [(l1, v1), (l2, v2)]


def f2s(v, n=30):
    return mp.nstr(v, n)


def is_new(mins, w, tol=mp.mpf('1e-12')):
    for t in mins:
        w2 = t[0]
        if nrm([w[i] - w2[i] for i in range(3)]) < tol:
            return False
    return True


def setup_sigma(e):
    comps, ptsS = [], []
    for sg in e['core']['sigma']:
        if sg['kind'] == 'points':
            for p in sg['pts']:
                p = np.array(p, float)
                p /= np.linalg.norm(p)
                ptsS += [p, -p]
        else:
            F, cs = components(sg['f'], DS)
            for c in cs:
                comps.append((F, c))
    return comps, ptsS


def minima_at(P, comps, ptsS, r, ex, rng, known):
    """все локальные минимумы U<0 на сфере S_r: [(w, U, Ht, e, src)], отсортированы по U"""
    cand = []
    for (F, c) in comps:
        ms, _ = curve_minima(P, F, c, r, DS)
        cand += [w for w, U in ms]
    seeds = []
    if len(ptsS):
        seeds += tube_seeds(P, ptsS, float(r), rng)
    if ex >= -3.1:
        seeds += grid_minima(P, float(r), ntop=60)
    mins = []
    for w in cand:   # полировка кривых минимумов 2D-Ньютоном на сфере
        w2, U2, gt, Ht, ee, ok = newton_min(P, w, r, maxit=30)
        if U2 < 0 and nrm([w2[i] - w[i] for i in range(3)]) < mp.mpf('1e-6'):
            w_, U_, Ht_, e_ = w2, U2, Ht, ee
        else:
            U_, gt, Ht_, e_ = riem(P, w, r)[0:4]
            w_ = w
        if U_ < 0 and is_new(mins, w_):
            mins.append((w_, U_, Ht_, e_, 'curve'))
    for s in seeds + list(known):
        try:
            w2, U2, gt, Ht, ee, ok = newton_min(P, mpv(s), r, maxit=300)
        except (ZeroDivisionError, ValueError):
            continue
        if ok and U2 < 0 and is_new(mins, w2):
            mins.append((w2, U2, Ht, ee, 'seed'))
    mins.sort(key=lambda t: t[1])
    return mins


def run_example(eid, quick=False):
    cat = load_catalog()
    e = cat[eid]
    P = Pot(e['U'])
    rng = np.random.default_rng(SEED)
    comps, ptsS = setup_sigma(e)
    exps = [-1, -2, -4] if quick else EXPS
    known = []
    out = dict(id=eid, U=e['U'], dps=DPS, ncomp=len(comps), npoints=len(ptsS), radii=[])
    for ex in exps:
        t0 = time.time()
        r = mp.mpf(10) ** mp.mpf(ex)
        mins = minima_at(P, comps, ptsS, r, ex, rng, known)
        rec = dict(r=f2s(r, 5), logr=ex, nmin=len(mins), minima=[])
        mglob = mins[0][1] if mins else None
        known = []
        for k, (w, U, Ht, ee, src) in enumerate(mins):
            known.append([float(c) for c in w])
            gt = riem(P, w, r)[1]
            gq = mp.sqrt(gt[0] ** 2 + gt[1] ** 2)
            item = dict(m=f2s(U), w=[f2s(c) for c in w], ratio=f2s(U / mglob, 8), src=src,
                        gradq=f2s(gq / abs(U), 5))
            if k < 8:
                ed = eigdirs(Ht, ee)
                eigs = []
                for (lam, v) in ed:
                    lphys = lam / r ** 2
                    wd = []
                    for sgn in (1, -1):
                        h = half_width(P, w, v, r, U, lam, sgn)
                        wd.append(None if h is None else f2s(h * r, 12))  # физическая ширина
                    eigs.append(dict(lam=f2s(lphys, 15), dir=[f2s(c, 12) for c in v], wid=wd))
                item['eigs'] = eigs
            rec['minima'].append(item)
        out['radii'].append(rec)
        print(f"{eid} r=1e{ex}: nmin={len(mins)} m={mp.nstr(mglob,8) if mglob is not None else None}  [{time.time()-t0:.1f}s]", flush=True)
        json.dump(out, open(os.path.join(OUT, eid + ('.quick' if quick else '') + '.json'), 'w'), indent=1)
    return out


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    quick = '--quick' in sys.argv
    for a in args:
        run_example(a, quick)
