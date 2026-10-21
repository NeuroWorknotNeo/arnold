"""
val_analyze.py -- обработка out/ID.json: показатель глубины beta, направление дна, поперечные показатели, число оврагов,
классификация (i)/(ii)/(iii).  Вывод: summary.json, summary.md.   [Эксперимент]
"""
import json, os, sys, math
import numpy as np
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')
ORDER = ['K1', 'K2', 'K3', 'A1', 'A2', 'A3', 'A4', 'A5', 'A7', 'C1', 'C2', 'D1', 'D2', 'F1', 'M1', 'M2', 'P1', 'P3', 'P4', 'Z1', 'S1', 'T1']


def fl(s):
    return float(mp.mpf(s))


def slope(xs, ys):
    xs, ys = np.array(xs), np.array(ys)
    A = np.vstack([xs, np.ones_like(xs)]).T
    return np.linalg.lstsq(A, ys, rcond=None)[0][0]


def lslopes(lr, ly):
    return [(ly[i + 1] - ly[i]) / (lr[i + 1] - lr[i]) for i in range(len(lr) - 1)]


def symmetries(Ustr):
    """знаковые перестановки координат S (3x3), с U(S q) = U(q) (точно, sympy)"""
    import itertools
    import sympy as sp
    x, y, z = sp.symbols('x y z')
    U = sp.expand(sp.sympify(Ustr, locals={'x': x, 'y': y, 'z': z}))
    out = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            S = np.zeros((3, 3))
            for i in range(3):
                S[i, perm[i]] = sg[i]
            q = S @ np.array([x, y, z], dtype=object)
            if sp.expand(U.subs({x: q[0], y: q[1], z: q[2]}, simultaneous=True) - U) == 0:
                out.append(S)
    return out


def load(eid):
    p = os.path.join(OUT, eid + '.json')
    if not os.path.exists(p):
        return None
    return json.load(open(p))


def analyze(eid, tail=7):
    d = load(eid)
    if d is None or not d['radii']:
        return None
    R = d['radii']
    lr = [x['logr'] for x in R]     # log10 r (не ln)
    res = dict(id=eid, nradii=len(R), logr=lr)
    # глубина
    lm = [math.log10(abs(fl(x['minima'][0]['m']))) if x['nmin'] else None for x in R]
    res['log10_abs_m'] = lm
    sl = lslopes(lr, lm)
    res['local_beta'] = sl
    res['beta_fit'] = slope(lr[-tail:], lm[-tail:])
    beta = round(res['beta_fit'] * 6) / 6
    res['beta_round'] = beta
    res['a_coef'] = [fl(x['minima'][0]['m']) / 10 ** (beta * x['logr']) for x in R]
    # направление дна: w глубочайшего минимума
    W = [np.array([fl(c) for c in x['minima'][0]['w']]) for x in R]
    res['omega_last'] = W[-1].tolist()
    # ветвь: на каждом радиусе берём минимум (ratio >= 0.5), ближайший к omega(1e-6)
    dist = []
    for x in R:
        best = None
        for it in x['minima']:
            if fl(it['ratio']) < 0.5:
                continue
            w_ = np.array([fl(c) for c in it['w']])
            dd = float(np.linalg.norm(w_ - W[-1]))
            if best is None or dd < best:
                best = dd
        dist.append(best)
    res['omega_dist_to_last'] = dist
    sel = [(x_, dd) for x_, dd in zip(lr, dist) if dd is not None and dd > 1e-13 and -5.6 <= x_ <= -2]
    res['omega_exp'] = slope([t[0] for t in sel], [math.log10(t[1]) for t in sel]) if len(sel) >= 3 else None
    ac = res['a_coef']
    sel = [(x_, abs(v - ac[-1])) for x_, v in zip(lr, ac) if abs(v - ac[-1]) > 1e-13 * abs(ac[-1]) and -5.6 <= x_ <= -2]
    res['a_corr_exp'] = slope([t[0] for t in sel], [math.log10(t[1]) for t in sel]) if len(sel) >= 3 else None
    # число оврагов на последнем радиусе: ветви с ratio >= 0.5 ; различные модуло w -> -w учитываются отдельно
    last = R[-1]
    ratios = [fl(it['ratio']) for it in last['minima']]
    res['nmin_last'] = last['nmin']
    res['ratios_last'] = ratios
    # антиподальные пары
    wl = [np.array([fl(c) for c in it['w']]) for it in last['minima']]
    groups = []
    for k, w in enumerate(wl):
        placed = False
        for g in groups:
            same_val = abs(ratios[k] - ratios[g[0]]) < 1e-9 * max(1.0, abs(ratios[g[0]]))
            if same_val and (np.linalg.norm(w + wl[g[0]]) < 1e-6 or np.linalg.norm(w - wl[g[0]]) < 1e-6):
                g.append(k)
                placed = True
                break
        if not placed:
            groups.append([k])
    syms = symmetries(d['U'])
    res['nsym'] = len(syms)
    # орбиты минимумов относительно найденных симметрий (знаковые перестановки), при совпадении значения
    orb = []
    for k, w in enumerate(wl):
        placed = False
        for g in orb:
            same_val = abs(ratios[k] - ratios[g[0]]) < 1e-7 * max(1.0, abs(ratios[g[0]]))
            if same_val and any(np.linalg.norm(S @ w - wl[g[0]]) < 1e-6 for S in syms):
                g.append(k)
                placed = True
                break
        if not placed:
            orb.append([k])
    res['orbits_last'] = [dict(idx=g, ratio=ratios[g[0]], w=wl[g[0]].tolist(), size=len(g)) for g in orb]
    res['groups_last'] = [dict(idx=g, ratio=ratios[g[0]], w=wl[g[0]].tolist(), pair=len(g)) for g in groups]
    # собственные значения и ширины глубочайшего минимума
    eig = []
    for x in R:
        it = x['minima'][0]
        es = it['eigs']
        lam = sorted([fl(e['lam']) for e in es])
        # сопоставление ширин с собственными значениями
        pairs = []
        for e in es:
            pairs.append((fl(e['lam']), e))
        def avg2(lst):
            v2 = [float(t) if not isinstance(t, float) else t for t in lst if t is not None]
            return (sum(v2) / len(v2)) if len(v2) == 2 else None
        if 'scan' in it and all('wids' in sc for sc in it['scan']):
            # вырожденный гессиан: мягкое направление = макс профильная ширина, жёсткое = мин прямая ширина
            prof = [avg2(sc['wid']) for sc in it['scan']]
            stra = [avg2(sc['wids']) for sc in it['scan']]
            lam0 = pairs[0][0]
            if all(t is not None for t in prof) and all(t is not None for t in stra):
                pairs = [(lam0, max(prof), 0.5), (lam0, min(stra), 0.5)]
            else:
                pairs = [(lam0, None, 0.5), (lam0, None, 0.5)]
        else:
            pairs.sort(key=lambda t: t[0])
            # мягкое (меньшее lam): профильная ширина wid2 (следует за изогнутым дном); жёсткое: прямая ширина wid
            f0 = pairs[0][1].get('wid2_f', 0.5) if pairs[0][1].get('wid2') else 0.5
            pairs = [(pairs[0][0], avg2(pairs[0][1].get('wid2') or pairs[0][1]['wid']), f0),
                     (pairs[1][0], avg2(pairs[1][1]['wid']), 0.5)]
        eig.append(pairs)
    res['eig'] = [[(p[0], p[1], p[2]) for p in ps] for ps in eig]
    mabs = [abs(fl(x['minima'][0]['m'])) for x in R]
    out_i = []
    for i in range(2):
        lam = [ps[i][0] for ps in eig]
        wid = [ps[i][1] for ps in eig]
        ok_w = all(w is not None and w > 0 for w in wid)
        llam = [math.log10(abs(v)) if v != 0 else None for v in lam]
        rr = [10 ** x_ for x_ in lr]
        info = dict(lam=lam, wid=wid)
        # квадратичная оценка ширины (угол) sqrt(|m|/(lam r^2)): > 1 означает дно, плоское вдоль всей сферы
        info['wquad_ang'] = [math.sqrt(mabs[k] / (lam[k] * rr[k] ** 2)) if lam[k] > 0 else None for k in range(len(R))]
        if all(v is not None for v in llam):
            info['gamma_local'] = lslopes(lr, llam)
            info['gamma_fit'] = slope(lr[-tail:], llam[-tail:])
        if ok_w:
            lw = [math.log10(w) for w in wid]
            info['cw_local'] = lslopes(lr, lw)
            info['cw_fit'] = slope(lr[-tail:], lw[-tail:])
            fs = [ps[i][2] for ps in eig]
            kap = [lam[k] * wid[k] ** 2 / (2 * fs[k] * mabs[k]) for k in range(len(R))]
            info['f_level'] = fs
            info['kappa'] = kap
            info['kappa_slope'] = slope(lr[-tail:], [math.log10(abs(v)) for v in kap[-tail:]]) if all(v != 0 for v in kap[-tail:]) else None
        out_i.append(info)
    res['dirs'] = out_i
    return res


def classify(res):
    """автоматическая оценка (по численным данным): подкласс (i-a)/(i-b)/(ii-a)/(ii-b) + пометка (iii) + флаги.
    (i)  оба поперечных направления: kappa -> const > 0 (невырожденный минимум со степенными масштабами);
         (i-a): мягкое направление с c = 1 имеет H_plane > 0 (rho > 0) либо c > 1;  (i-b): c = 1 и rho <= 0.
    (ii) kappa -> 0 как степень (вырожденное чашеобразное дно, ii-a) либо ширина не найдена и квадратичная оценка
         ширины > 1 рад (плоское дно вдоль всей кривой, ii-b).
    (iii) >= 2 орбит с ratio >= 0.99 (равная глубина на ведущем порядке)."""
    flags = []
    d = res['dirs']
    beta = res['beta_round']
    a = abs(res['a_coef'][-1])
    degenerate = False
    flat = False
    for i, inf in enumerate(d):
        ks = inf.get('kappa_slope')
        if ks is None:
            wq = inf.get('wquad_ang', [None])[-1]
            flags.append(f'dir{i}: ширина не найдена (квадр. оценка ширины {wq:.3g} рад)' if wq else f'dir{i}: ширина не найдена')
            degenerate = True
            if wq is not None and wq > 1:
                flat = True
        elif abs(ks) > 0.15:
            flags.append(f'dir{i}: kappa ~ r^{ks:.2f}')
            degenerate = True
    # rho: H_plane мягкого направления (если c_soft ~ 1)
    soft = d[0]
    cs = soft.get('cw_fit')
    gs = soft.get('gamma_fit')
    rho = None
    if soft['lam']:
        lam = soft['lam'][-1]
        rr = 10 ** res['logr'][-1]
        h = lam / rr ** (beta - 2) - beta * a
        rho = h / (beta * a)
        res['H_plane_soft'] = h
        res['rho'] = rho
    if degenerate:
        cls = 'ii-b' if flat else 'ii-a'
    else:
        if gs is not None and gs < beta - 2 - 0.5:
            cls = 'i-a'           # c_soft > 1: поправка сферы несущественна
        else:
            cls = 'i-a' if (rho is not None and rho > 0) else 'i-b'
    n_equal = len([g for g in res['orbits_last'] if g['ratio'] >= 0.99])
    if n_equal >= 2:
        cls += ' +iii'
    return cls, flags


def fmt(v, n=3):
    return 'None' if v is None else f'{v:.{n}f}'


def main():
    ids = sys.argv[1:] or ORDER
    summ = {}
    lines = []
    for eid in ids:
        r = analyze(eid)
        if r is None:
            continue
        cls, flags = classify(r)
        r['class'] = cls
        r['flags'] = flags
        summ[eid] = r
        d = r['dirs']
        lines.append(f"## {eid}: beta_fit={r['beta_fit']:.3f} (округлено {r['beta_round']}), a={r['a_coef'][-1]:.5g}, "
                     f"nmin(r=1e-6)={r['nmin_last']}, ratios={[round(x, 3) for x in r['ratios_last']]}")
        lines.append(f"  omega(1e-6)={np.round(r['omega_last'], 6).tolist()}, |omega(r)-omega(1e-6)| по r: "
                     f"{['%.1e' % v for v in r['omega_dist_to_last']]}; omega_exp={fmt(r['omega_exp'], 2)}, a_corr_exp={fmt(r['a_corr_exp'], 2)}")
        for i, inf in enumerate(d):
            lines.append(f"  dir{i}: lam={['%.3e' % v for v in inf['lam']]}")
            lines.append(f"        gamma_fit={fmt(inf.get('gamma_fit'))} cw_fit={fmt(inf.get('cw_fit'))} kappa_slope={fmt(inf.get('kappa_slope'))}")
            lines.append(f"        kappa={['%.3g' % v for v in inf.get('kappa', [])]}")
        lines.append(f"  class={cls}, flags={flags}")
    open(os.path.join(HERE, 'summary.md'), 'w').write("\n".join(lines))
    json.dump(summ, open(os.path.join(HERE, 'summary.json'), 'w'), indent=1)
    print("\n".join(lines))


if __name__ == '__main__':
    main()
