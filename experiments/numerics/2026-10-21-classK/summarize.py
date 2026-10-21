"""summarize.py -- assemble out/*.json (+ out/T1_crit.json, out/D1_next.json) into the classification table.
Reads the valleys summary (numerics/2026-10-21-valleys/summary.json) only for the final comparison column."""
import json, os, math
import sympy as sp, mpmath as mp
import comps
from comps import x, y, z, U, ALL, HARD, CALIB, COMPS
from kfib import homog_parts
mp.mp.dps = 30
HERE = os.path.dirname(os.path.abspath(__file__))
V = json.load(open(os.path.join(HERE, '..', '2026-10-21-valleys', 'summary.json')))

def kappa_bound(j, G0, Gpp, hn):
    lam0 = min(Gpp, hn)/4; a0 = -G0
    return j*lam0/(a0*(15*math.sqrt(3)/8*j + 2*math.sqrt(2))**2)

SIGMA = {
 'K1': 'две точки ±e_z (u_4=x⁴+y⁴)', 'K2': 'две окружности Σ±: конус Q=0 (круг.)', 'K3': 'две окружности Σ± (Q=0)',
 'A1': 'две окружности Σ± (Q=0)', 'A2': 'две окружности Σ± (Q=0)', 'A3': 'две окружности Σ± (Q=0)', 'A4': 'две окружности Σ± (Q=0)',
 'A5': 'две окружности Σ± (Q=0)', 'A7': 'две окружности Σ± (Q=0; u_6=Q²|q|²)', 'C1': 'два овала Σ± (эллипт. конус x²+2y²=z²)',
 'C2': 'две окружности Σ± (x²+y²=2z²)', 'D1': 'две окружности Σ± (Q=0; деформация только в u_5,u_6)',
 'D2': 'две окружности Σ± (Q=0)', 'F1': 'большой круг z=0', 'M1': 'большой круг z=0 (u_4=z⁴)', 'M2': 'большой круг z=0 (u_4=z⁴)',
 'P1': 'две точки ±e_z (u_4=x⁴+y⁴)', 'P3': '8 точек (±1,±1,±1)/√3', 'P4': '6 точек ±e_x, ±e_y, ±e_z',
 'Z1': 'большой круг z=0 ∪ полюса ±e_z', 'S1': 'два больших круга x=±y, пересекаются в ±e_z (особая)',
 'T1': 'одна гладкая замкнутая кривая (кубический конус C=0)',
}
res = {}
for ex in ALL:
    d = dict(id=ex)
    if ex == 'T1':
        cr = json.load(open(os.path.join(HERE, 'out', 'T1_crit.json')))
        m = 6
        # critical points: min (neg), max; each is one projective point = antipodal pair on S^2
        mins = [c for c in cr if float(c['d2G']) > 0]
        d.update(m=6, j=8, Gformula='u_8|Σ = (y⁸/8 − z⁸ + y z⁷)|Σ (u_7=0 ⇒ g_7=0, b_1=0)', MB='да (H=2|∇C|²>0, ∇C≠0 на Σ)',
                 crit=cr, gmin=min(float(c['G']) for c in cr))
        best = min(mins, key=lambda c: float(c['G']))
        d['best'] = dict(G=float(best['G']), d2=float(best['d2G']), k1=float(best['G2_plus_jG']), omega=best['omega'])
        d['k1_ok'] = float(best['G2_plus_jG']) > 0
        d['k2_ok'] = True
        h_n = None
        res[ex] = d
        continue
    r = json.load(open(os.path.join(HERE, 'out', ex + '.json')))
    d['m'] = r['m']
    d['comps'] = r['components']
    curves = [c for c in r['components'] if 'crit' in c or c.get('G_const')]
    points = [c for c in r['components'] if 'g_j' in c]
    nonmb = [c for c in r['components'] if c.get('kind') == 'nonMB']
    # candidates
    negmins = []
    for c in curves:
        for q in c.get('crit', []):
            if q['kind'] == 'min' and float(q['G']) < 0:
                negmins.append((c['name'], c['j'], q))
    d['K2_cands'] = [(n, j, q) for n, j, q in negmins]
    d['K1_cands'] = [(n, j, q) for n, j, q in negmins if float(q['G2_plus_jG']) > 0]
    d['K0_cands'] = [(c['name'], c['j'], c['g_j_float']) for c in points if c.get('g_j_sign', 0) < 0]
    d['const_neg'] = [(c['name'], c['j'], c['G_value']) for c in curves if c.get('G_const') and sp.sympify(c['G_value']) < 0]
    d['G_nonneg_zero'] = [(c['name'], c['j']) for c in curves if 'crit' in c and min(float(q['G']) for q in c['crit']) >= -1e-30 and
                          any(abs(float(q['G'])) < 1e-30 for q in c['crit'])]
    d['nonMB'] = [c['name'] for c in nonmb]
    res[ex] = d

# ---------------------------------------------------------------- classification
def classify(ex):
    d = res[ex]
    if ex == 'T1':
        return 'K¹', 'K1', '—'
    if d['nonMB']:
        return 'вне K', '—', '§10.2 п.4 (не Морс–Ботт: D²u_m ≡ 0 на нормалях, порядок 4)'
    if ex == 'S1':
        return 'вне K формально (особое Σ)', 'K1 локально', '§10.2 п.5 формально; на гладкой дуге выполнены условия K1 (§1 п.3: локальность)'
    tags = []
    th = []
    if d['K0_cands']:
        tags.append('K⁰'); th.append('K0')
    if d['K1_cands']:
        tags.append('K¹'); th.append('K1')
    elif d['K2_cands']:
        tags.append('K¹'); th.append('K2 (только)')
    if tags:
        return ' и '.join(tags) if len(tags) > 1 else tags[0], ' + '.join(th), '—'
    if d['const_neg']:
        return 'вне K', '—', '§10.2 п.1 (G ≡ const < 0 на замкнутой компоненте)'
    if d['G_nonneg_zero']:
        return 'вне K', '—', '§10.2 п.3 (каскад: G ≥ 0 с нулём, отрицательные значения в следующих порядках)'
    return '?', '?', '?'

for ex in ALL:
    c, th, why = classify(ex)
    res[ex]['class'] = c; res[ex]['theorem'] = th; res[ex]['outside'] = why

json.dump(res, open(os.path.join(HERE, 'summary.json'), 'w'), indent=1, default=str)

# ---------------------------------------------------------------- valleys comparison and table
def vcmp(ex):
    v = V[ex]
    beta_v = v['beta_round']; a_v = abs(v['a_coef'][-1]); om_v = v['omega_last']; rho_v = v.get('rho')
    return beta_v, a_v, om_v, rho_v

def best_neg(ex):
    """predicted deepest valley from the K-analysis: smallest j with a negative value, then smallest G"""
    d = res[ex]
    cands = []
    if ex == 'T1':
        b = d['best']; cands.append((8, b['G'], b['omega'], b['k1'], 'curve'))
    else:
        for n, j, q in d.get('K2_cands', []):
            cands.append((j, float(q['G']), q['omega'], float(q['G2_plus_jG']), 'curve'))
        for n, j, g in d.get('K0_cands', []):
            comp = [c for c in d['comps'] if c['name'] == n][0]
            cands.append((j, g, n, None, 'point'))
        for n, j, g in d.get('const_neg', []):
            cands.append((j, float(sp.sympify(g)), None, None, 'const'))
    return sorted(cands, key=lambda c: (c[0], c[1]))

import numpy as np
rows = []
for ex in ALL:
    d = res[ex]; v = V[ex]
    beta_v, a_v, om_v, rho_v = vcmp(ex)
    pred = best_neg(ex)
    line = dict(id=ex, cls=d['class'], thm=d['theorem'], outside=d['outside'], beta_v=beta_v, a_v=a_v, om_v=om_v, rho_v=rho_v)
    if pred:
        j, G, om, k1, kind = pred[0]
        line['beta_p'] = j; line['a_p'] = -G
        if kind == 'curve':
            line['rho_p'] = k1/(-j*G)
            omv = np.array(om_v)
            # distance to the predicted minimiser (either orientation of the pair is a distinct point: compare directly)
            alls = [np.array([float(a) for a in q['omega']]) for n, jj, q in d['K2_cands'] if jj == j and abs(float(q['G']) - G) < 1e-9] if ex != 'T1' else [np.array([float(a) for a in d['best']['omega']]), -np.array([float(a) for a in d['best']['omega']])]
            line['om_dist'] = min(np.linalg.norm(omv - a) for a in alls)
        elif kind == 'point':
            comp = [c for c in d['comps'] if c['name'] == om][0]
            line['om_p'] = om
    rows.append(line)
json.dump(rows, open(os.path.join(HERE, 'valleys_compare.json'), 'w'), indent=1, default=str)
for r in rows:
    print({k: (round(v, 5) if isinstance(v, float) else v) for k, v in r.items() if k not in ('om_v',)})
