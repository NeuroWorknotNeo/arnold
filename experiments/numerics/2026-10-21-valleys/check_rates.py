"""
check_rates.py -- сопоставление измеренной скорости сходимости входов стрельбы d_k ~ r0^e с эвристическим предсказанием
e_pred = 1 + omega_exp + p_- (beta-2)/2, где p_- = Re(1 - sqrt(1 - 4h'))/2, h' = 2 beta rho/(beta-2)^2 (линеаризация вдоль
гомотетической траектории r(t) ~ t^{-2/(beta-2)}: d^2 y/dt^2 = -H_plane r^{beta-2} y  =>  уравнение Эйлера).
Только для примеров с мягким направлением c = 1.   [Эксперимент + эвристика]
"""
import json, math, os, glob
import numpy as np
import val_analyze as V
import make_table as MT

HERE = os.path.dirname(os.path.abspath(__file__))
rows = []
for eid in V.ORDER:
    r = V.analyze(eid)
    if r is None:
        continue
    V.classify(r)
    soft = r['dirs'][0]
    cw = soft.get('cw_fit')
    if cw is None or abs(cw - 1) > 0.1 or r.get('rho') is None:
        continue
    f = os.path.join(HERE, 'traj', eid + '.json')
    if not os.path.exists(f):
        continue
    d = json.load(open(f))
    v = MT.verdict_from(d)
    r0 = [x['r0'] for x in d['recs']]
    # измеренный показатель по последним трём шагам
    ex = []
    for k in range(len(v['dist']) - 3, len(v['dist']) - 1 + 1):
        if k >= 1 and v['dist'][k] > 0 and v['dist'][k - 1] > 0:
            ex.append(math.log(v['dist'][k] / v['dist'][k - 1]) / math.log(r0[k + 1] / r0[k]))
    e_meas = float(np.mean(ex[-3:])) if ex else None
    beta = r['beta_round']
    rho = r['rho']
    h = 2 * beta * rho / (beta - 2) ** 2
    disc = 1 - 4 * h
    pm = (1 - math.sqrt(disc)) / 2 if disc >= 0 else 0.5
    oe = r['omega_exp']
    e_pred = 1 + oe + pm * (beta - 2) / 2 if oe is not None else None
    rows.append((eid, beta, rho, h, pm, oe, e_meas, e_pred))
L = ["| № | β | ρ | h' | p_- | показатель сдвига дна ω−ω∞ ~ r^p | e измеренный | e предсказанный |", "|---|---|---|---|---|---|---|---|"]
for (eid, beta, rho, h, pm, oe, em, ep) in rows:
    L.append(f"| {eid} | {beta:.3g} | {rho:+.3f} | {h:+.3f} | {pm:+.3f} | {oe if oe is None else round(oe, 2)} | {em if em is None else round(em, 2)} | {ep if ep is None else round(ep, 2)} |")
open(os.path.join(HERE, 'rates.md'), 'w').write("\n".join(L))
print("\n".join(L))
