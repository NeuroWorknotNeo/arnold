"""
run_bottom.py -- дно оврага для примера ID: минимумы U на сферах S_r, r = 10^{-1}...10^{-6} (шаг 10^{-1/4}),
mpmath (60 знаков), продолжение по r + старты у особых точек + (для r >= 10^-3) сетка в double.
Для глубочайшего минимума: гессиан на сфере (собственные значения/направления), профильные ширины (f = 1/2),
масштабированный профиль.  [Эксперимент]   seed генератора: 20261021
usage: python run_bottom.py ID [--quick]   ->  out/ID.json
"""
import sys, os, json, time
from flib import *

OUT = os.path.join(HERE, 'out')
os.makedirs(OUT, exist_ok=True)


def f2s(v, n=30):
    return mp.nstr(v, n)


def run(eid, quick=False, ext=None):
    e = cat()[eid]
    P = Pot(e['U'])
    rng = np.random.default_rng(SEED)
    exps = [-1, -2, -3] if quick else [-1 - 0.25 * k for k in range(21)]
    known = []
    hist = []                     # история положений глубочайших минимумов (для экстраполяции по log r)
    out = dict(id=eid, U=e['U'], dps=DPS, radii=[])
    if ext:                       # продолжение до меньших радиусов: старт от последних минимумов основного прогона
        lo = float(ext)
        exps = [-6 - 0.25 * k for k in range(1, int((-lo - 6) / 0.25) + 1)]
        main = json.load(open(os.path.join(OUT, eid + '.json')))['radii']
        prev_recs = main[-3:]
        pe = os.path.join(OUT, eid + '.ext.json')
        if os.environ.get('EXT_RESUME') and os.path.exists(pe):
            old = [r_ for r_ in json.load(open(pe))['radii'] if r_['nmin'] > 0]
            out['radii'] = old
            prev_recs = (main + old)[-3:]
            exps = [t for t in exps if t < old[-1]['logr'] - 1e-9]
        for pr_ in prev_recs:
            hist.append((pr_['logr'], [[mp.mpf(c) for c in it['w']] for it in pr_['minima'][:3]]))
        known = [[float(c) for c in it['w']] for it in prev_recs[-1]['minima'][:5]]
    ssamp = sigma_samples(eid, 14) if not ext else np.zeros((0, 3))
    width_exps = ({-1, -2, -3, -4, -5, -6} if not quick else {-1, -2, -3}) if not ext else {-8, -10, -12, -14}
    for k_idx, ex in enumerate(exps):
        t0 = time.time()
        r = mp.mpf(10) ** mp.mpf(ex)
        rf = float(r)
        seeds = list(known)
        if len(hist) >= 2:             # экстраполяция положения дна по log r (линейная и квадратичная, в mpmath)
            nb = min(len(h[1]) for h in hist[-3:])
            for j in range(nb):
                pts = [(h[0], h[1][j]) for h in hist[-3:]]
                for order in (1, 2):
                    if order == 2 and len(pts) < 3:
                        continue
                    pp = pts[-(order + 1):]
                    wp = []
                    for c in range(3):
                        tot = mp.mpf(0)
                        for a_, (xa, wa) in enumerate(pp):
                            L = mp.mpf(1)
                            for b_, (xb, wb) in enumerate(pp):
                                if a_ != b_:
                                    L *= (mp.mpf(ex) - mp.mpf(xb)) / (mp.mpf(xa) - mp.mpf(xb))
                            tot += L * wa[c]
                        wp.append(tot)
                    seeds.append(tuple(wp))
        for s in e['seeds']:
            seeds += seeds_around(s, rf)
        full = (not ext) and (ex in (-1, -2, -3) or k_idx % 4 == 0)       # полный поиск на части радиусов
        if full:
            for p in ssamp:
                seeds += seeds_around(p, rf, pows=(0.5, 1.0, 2.0))
            if ex >= -3.05:
                seeds += grid_minima(P, rf, nth=700, nph=1400, ntop=25)
        mins = find_all(P, r, seeds, maxit=80)
        mglob = mins[0][1] if mins else None
        rec = dict(logr=ex, r=f2s(r, 6), nmin=len(mins), nseeds=len(seeds), minima=[])
        known = []
        if mins:
            hist.append((ex, [list(t[0]) for t in mins[:3]]))
        for k, (w, U, Ht, ee) in enumerate(mins[:12]):
            if k < 5:
                known.append([float(c) for c in w])
            item = dict(m=f2s(U, 25), w=[f2s(c, 25) for c in w], ratio=f2s(U / mglob, 8))
            ed = eigdirs(Ht, ee)
            item['lam_phys'] = [f2s(l / r ** 2, 12) for l, _ in ed]
            rec['minima'].append(item)
            wset = os.environ.get('WIDTH_EXPS')
            if wset:
                do_w = any(abs(ex - float(t)) < 1e-9 for t in wset.split(','))
            else:
                do_w = (int(round(ex)) == ex and int(ex) in width_exps) or (abs(ex * 2 - round(ex * 2)) < 1e-9 and ex <= -2 and not quick)
            if k == 0 and do_w:
                ws = []
                (l1, v1), (l2, v2) = ed
                for (va, vb) in ((v1, v2), (v2, v1)):
                    wl = []
                    for sg in (1, -1):
                        try:
                            wl.append(profile_width(P, r, w, va, vb, U, sign=sg))
                        except Exception as ex_:
                            wl.append(None)
                    ws.append(wl)
                item['widths_angle'] = [[None if v is None else f2s(v, 12) for v in wl] for wl in ws]
                item['widths_phys'] = [[None if v is None else f2s(v * r, 12) for v in wl] for wl in ws]
                try:
                    A1 = (ws[0][0] + ws[0][1]) / 2 if ws[0][0] and ws[0][1] else (ws[0][0] or ws[0][1])
                    A2 = (ws[1][0] + ws[1][1]) / 2 if ws[1][0] and ws[1][1] else (ws[1][0] or ws[1][1])
                    item['dirs'] = [[f2s(c, 15) for c in v1], [f2s(c, 15) for c in v2]]
                    if A1 and A2:
                        item['profile5'] = [[f2s(v, 8) for v in row] for row in scaled_profile(P, r, w, v1, v2, U, A1, A2)]
                except Exception as ex_:
                    item['profile_err'] = repr(ex_)[:100]
        out['radii'].append(rec)
        print(f"{eid} r=1e{ex:g}: nmin={len(mins)} m={mp.nstr(mglob, 8) if mglob is not None else None}  nseeds={len(seeds)} [{time.time()-t0:.1f}s]", flush=True)
        json.dump(out, open(os.path.join(OUT, eid + ('.quick' if quick else '') + ('.ext' if ext else '') + '.json'), 'w'), indent=1)
    return out


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    ext = None
    for i, a in enumerate(sys.argv):
        if a == '--ext':
            ext = sys.argv[i + 1]
            args = [t for t in args if t != ext]
    for a in args:
        run(a, '--quick' in sys.argv, ext)
