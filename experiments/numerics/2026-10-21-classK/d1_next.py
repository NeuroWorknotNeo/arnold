"""d1_next.py -- D1: G = g_8 = -1/16 is constant on Sigma+ ; compute the next orders g_9, g_10 (K=6) exactly."""
import sympy as sp, mpmath as mp, json
from kfib import fibre
import comps
from comps import U, t, x, y, z
mp.mp.dps = 40
ex = 'D1'
res = {}
for comp in comps.COMPS[ex]:
    _, name, p, nu, f = comp
    out = fibre(U[ex], 4, p, [nu], 6)
    lam = sp.sqrt(sp.factor(sum(c**2 for c in p))); lam = sp.simplify(lam)
    for k in range(5, 11):
        gk = sp.factor(sp.cancel(out['g'][k])/lam**k)
        print(name, k, gk if len(str(gk)) < 600 else str(gk)[:600]+'...')
        res.setdefault(name, {})[k] = str(gk)
    # critical points of G_9, G_10 (the first non-constant ones)
    for k in (9, 10):
        G = sp.simplify(sp.cancel(out['g'][k])/lam**k)
        Gt = sp.cancel(sp.diff(G, t))
        if Gt == 0:
            print(name, 'g_%d constant =' % k, G); continue
        Pn = sp.Poly(sp.numer(sp.together(Gt)), t)
        vals = []
        for fac, mult in sp.sqf_list(Pn)[1]:
            if fac.degree() <= 0: continue
            for r in sp.real_roots(fac):
                vals.append((float(sp.N(r, 30)), float(sp.N(G.subs(t, r), 30)), mult))
        # value at t=inf
        vinf = sp.limit(G, t, sp.oo)
        vals.append(('inf', float(sp.N(vinf, 30)), 1))
        print(name, 'g_%d: critical values (t, G, mult):' % k, sorted(vals, key=lambda v: v[1]))
json.dump(res, open('out/D1_next.json', 'w'), indent=1)
