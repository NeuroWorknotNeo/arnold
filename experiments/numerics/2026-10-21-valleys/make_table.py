"""
make_table.py -- итоговая таблица table.md из summary.json (val_analyze.py) и traj/*.json (traj_run.py).  [Эксперимент]
"""
import json, os, math, glob
import numpy as np
import val_analyze as V

HERE = os.path.dirname(os.path.abspath(__file__))
IDS = V.ORDER


COMMENTS = {
    'K1': 'калибровка; дно — ось z точно (U=−z⁶), квартичная чаша ξ⁴+η⁴',
    'K2': 'калибровка (пример 13); H_plane=0.0502 совпало с §6.3 заметки prover',
    'K3': 'калибровка (теорема B); H_plane<0',
    'A1': 'двойной нуль G при φ=0 не при чём: овраг в невыр. минимуме G<0; два антиподальных оврага (β чётно)',
    'A2': 'то же; овраг в отрицательном минимуме G',
    'A3': 'тройной нуль G не при чём; ρ>0, но запас мал (0.12)',
    'A4': 'G≥0 с двойным нулём; овраг сидит в нуле G, глубина r⁷ из z⁷; c дробные ⇒ N=2',
    'A5': 'β=5; овраг в отриц. минимуме G; ρ<0',
    'A7': 'm=6, β=8; ρ<0 (−0.19)',
    'C1': 'эллиптический конус; ρ=+0.63',
    'C2': 'круговой конус с другим раствором; ρ<0',
    'D1': 'плоское дно: на деформированном конусе U≈−z⁸ вдоль всей кривой; λ_мягк ∼ r^(β−1); нужен следующий порядок',
    'D2': 'как K2 (ρ тот же: деформация O(r²) не меняет ведущий порядок)',
    'F1': 'плоский желоб (большой круг); ρ=+0.98',
    'M1': 'овраг на оси −y; поперечно ζ=z−x² квартично (c=5/4), вдоль x квадратично (c=1); два оврага (x,y-оси) равной глубины',
    'M2': 'β=16/3 дробное; дно вдоль кривой (τ³,0,−τ⁴/2); ω(r)→(1,0,0) медленно (∼r^0.4); 4 оврага',
    'P1': 'квазиоднородная чаша ξ⁴+η⁴ (c=3/2,3/2) + хвост x³z²; поправки ∼ r^(1/2)',
    'P3': 'овраг в направлении (−1,1,1)/√3, где u₅=−2≠0; невыр. чаша c=(3/2,3/2)',
    'P4': 'овраги по осям x,y (u₅=−1); ось z (u₅=0) не даёт оврага',
    'Z1': 'овраг на экваторе (ранг 1), 3 оврага; ρ=0.04 — малый запас',
    'S1': 'овраг на гладкой части одной из двух окружностей; ρ=+0.11',
    'T1': 'кубический желоб; β=8; ρ=+0.11',
}


def f3(x, n=2):
    return '—' if x is None else f'{x:.{n}f}'


def rat(x):
    # приблизительно рациональная запись показателя
    if x is None:
        return '—'
    for den in (1, 2, 3, 4, 6):
        if abs(x * den - round(x * den)) < 0.04 * den ** 0.5 / 2 + 0.02:
            n = round(x * den)
            from math import gcd
            g = gcd(abs(n), den)
            n //= g
            d = den // g
            return f'{n}' if d == 1 else f'{n}/{d}'
    return f'{x:.2f}'


def trend(vals):
    """последние значения: стабилизировались ли (отн. разброс последних 4)"""
    v = [t for t in vals[-4:] if t is not None]
    if len(v) < 3:
        return None
    return (max(v) - min(v)) / abs(np.mean(v)) if np.mean(v) != 0 else None


def verdict_from(d):
    recs = d['recs']
    ent = [np.array(r['q'] + [-c for c in r['v']]) for r in recs if r['status'] == 0]
    dist = [float(np.linalg.norm(ent[k + 1] - ent[k])) for k in range(len(ent) - 1)]
    rat = [dist[k + 1] / dist[k] for k in range(len(dist) - 1) if dist[k] > 0]
    gm = float(np.exp(np.mean(np.log(np.maximum(rat[-3:], 1e-300))))) if len(rat) >= 3 else float('nan')
    conv = bool((gm < 0.85) or dist[-1] < 1e-12)
    sigma, beta, a0 = d['sigma'], d['beta'], d['a0']
    floor = 10 * sigma * (1e-16) ** (1.0 / beta)    # ниже ~этого r округление (double) входных данных искажает E=0
    last = None
    if d['fwd']:
        rows_ok = [rw for rw in d['fwd']['rows'] if abs(rw['E']) < 1e-2]   # (E-E0)/(a r^b) мала
        if rows_ok:
            rw = rows_ok[-1]
            last = dict(r=rw['r'], dev=rw['r'] / rw['pred'] - 1, U=rw['U'])
    return dict(conv=conv, gm=gm, d_last=dist[-1], last=last, dist=dist, ratios=rat, floor=floor)


def main():
    rows = []
    out = []
    summ = {}
    for eid in IDS:
        r = V.analyze(eid)
        if r is None:
            continue
        cls, flags = V.classify(r)
        r['class'] = cls
        r['flags'] = flags
        summ[eid] = r
        tj = {}
        for f in sorted(glob.glob(os.path.join(HERE, 'traj', eid + '*.json'))):
            d = json.load(open(f))
            tj[d.get('orbit', 0)] = d
        d = r['dirs']
        soft, stiff = d[0], d[1]
        orb = [o for o in r['orbits_last'] if o['ratio'] >= 0.5]
        norb = len(orb)
        w = np.array(r['omega_last'])
        kap_s = soft.get('kappa', [None])[-1]
        kap_t = stiff.get('kappa', [None])[-1]
        t0 = tj.get(0)
        if t0:
            v = verdict_from(t0)
            tr = f"сходится (отнош. ≈{v['gm']:.2f}, d_посл={v['d_last']:.0e})" if v['conv'] else \
                f"НЕ сошлось (отнош. ≈{v['gm']:.2f}, d_посл={v['d_last']:.0e})"
            lw = v['last']
            tr += (f"; пр. прогон до r={lw['r']:.1e}: r/r_pred−1={lw['dev']:+.1%}, U/(a r^β)={lw['U']:.3f}" if lw else "; пр. прогон: нет данных")
            others = []
            for k, dd in sorted(tj.items()):
                if k != 0:
                    vv = verdict_from(dd)
                    others.append(f"ветвь {k}: {'сх.' if vv['conv'] else 'НЕ сх.'} ({vv['gm']:.2f})")
            if others:
                tr += "; " + ", ".join(others)
        else:
            tr = 'нет данных'
        rows.append(dict(id=eid, beta=r['beta_round'], beta_fit=r['beta_fit'], a=abs(r['a_coef'][-1]),
                         omega=w, omega_exp=r['omega_exp'], a_exp=r['a_corr_exp'],
                         soft=soft, stiff=stiff, cls=cls, flags=flags, norb=norb,
                         orb_ratios=[round(o['ratio'], 3) for o in r['orbits_last']], tr=tr, traj=tj,
                         nsym=r['nsym']))
    json.dump(summ, open(os.path.join(HERE, 'summary.json'), 'w'), indent=1)
    L = []
    L.append("| № | β | a=\\|m\\|/r^β | ω∞ (r=1e-6) | ω−ω∞ ~ r^p | мягк.: γ, c (κ) | жёстк.: γ, c (κ) | λ_мягк, λ_жёстк (r=1e-6) | w_мягк, w_жёстк (r=1e-6) | оврагов (орбит) ratio≥½ | класс | асимпт. траектория |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for x in rows:
        s, t = x['soft'], x['stiff']
        sk = s.get('kappa', [None])[-1]
        tk = t.get('kappa', [None])[-1]
        L.append(f"| {x['id']} | {rat(x['beta_fit'])} | {x['a']:.5g} | ({x['omega'][0]:+.4f}, {x['omega'][1]:+.4f}, {x['omega'][2]:+.4f}) | "
                 f"{f3(x['omega_exp'], 1)} | γ={f3(s.get('gamma_fit'), 2)}, c={f3(s.get('cw_fit'), 2)} (κ={f3(sk, 3)}, наклон {f3(s.get('kappa_slope'), 2)}) | "
                 f"γ={f3(t.get('gamma_fit'), 2)}, c={f3(t.get('cw_fit'), 2)} (κ={f3(tk, 3)}, наклон {f3(t.get('kappa_slope'), 2)}) | "
                 f"{s['lam'][-1]:.3e}, {t['lam'][-1]:.3e} | "
                 f"{'—' if s['wid'][-1] is None else format(s['wid'][-1], '.3e')}, {'—' if t['wid'][-1] is None else format(t['wid'][-1], '.3e')} | "
                 f"{x['norb']} {x['orb_ratios']} | {x['cls']} | {x['tr']} |")
    open(os.path.join(HERE, 'table.md'), 'w').write("\n".join(L))
    # короткая таблица для README
    S = ["| № | β | ω∞ (направление дна) | c мягк. / жёстк. | κ мягк. / жёстк. | ρ = H_plane/(βa) | класс | асимптотическая траектория | комментарий |",
         "|---|---|---|---|---|---|---|---|---|"]
    for x in rows:
        s_, t_ = x['soft'], x['stiff']
        def cc(inf):
            return rat(inf.get('cw_fit')) if inf.get('cw_fit') is not None else '—'
        def kk(inf):
            k = inf.get('kappa', [None])[-1]
            return '—' if k is None else (f'{k:.2f}' if inf.get('kappa_slope') is not None and abs(inf['kappa_slope']) < 0.15 else f"→0 (∝r^{inf['kappa_slope']:.1f})")
        rho = summ[x['id']].get('rho')
        c_soft_is_1 = (s_.get('cw_fit') is not None and abs(s_['cw_fit'] - 1) < 0.1) or (s_.get('cw_fit') is None and s_.get('gamma_fit') is not None and abs(s_['gamma_fit'] - (x['beta'] - 2)) < 0.5)
        rs = (f'{rho:+.3f}' if (rho is not None and c_soft_is_1) else ('—' if rho is None else (f'{rho:+.2f} (λ→0, дно плоское)' if s_.get('cw_fit') is None and s_.get('kappa_slope') is None and s_['lam'][-1] < 1e-3 * x['a'] * 10 ** (-6 * (x['beta'] - 2)) * x['beta'] else 'c>1: n/a')))
        t0 = x['traj'].get(0)
        if t0:
            v = verdict_from(t0)
            lw = v['last']
            tr_short = (f"сх. (×{v['gm']:.2f}/шаг, d={v['d_last']:.0e}); пр. прогон до r={lw['r']:.0e}: {lw['dev']:+.1%}" if lw else f"сх. (×{v['gm']:.2f})") if v['conv'] else f"НЕ сх. (×{v['gm']:.2f})"
            oth = [f"ветвь {k}: {'сх.' if verdict_from(dd)['conv'] else 'НЕ сх.'}" for k, dd in sorted(x['traj'].items()) if k != 0]
            if oth:
                tr_short += "; " + ", ".join(oth)
        else:
            tr_short = '—'
        S.append(f"| {x['id']} | {rat(x['beta_fit'])} | ({x['omega'][0]:+.3f}, {x['omega'][1]:+.3f}, {x['omega'][2]:+.3f}) | {cc(s_)} / {cc(t_)} | {kk(s_)} / {kk(t_)} | {rs} | {x['cls']} | {tr_short} | {COMMENTS.get(x['id'], '')} |")
    open(os.path.join(HERE, 'table_short.md'), 'w').write("\n".join(S))
    print("\n".join(S))


if __name__ == '__main__':
    main()
