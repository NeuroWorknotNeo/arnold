"""gpp_check.py -- independent check of G'' (natural parameter) when j = m+1 (then G = u_j|Sigma exactly, no shift):
   G'' = D^2u_j(T,T) - j*G + k*<grad u_j, n>,   n = grad f/|grad f|, T = w x n, k = -T^T D^2 f T/|grad f|
(at a critical point of G; derivation: omega''=-omega+k n for unit speed curves on S^2, <grad u,omega>=j u).  [Experiment]"""
import json, sympy as sp, mpmath as mp
import comps
from comps import U, x, y, z
from kfib import homog_parts
mp.mp.dps = 40
def run(ex, comp_idx, crit_idx_filter):
    r = json.load(open('out/%s.json' % ex)); m = r['m']
    comp = comps.COMPS[ex][comp_idx]; cres = r['components'][comp_idx]
    j = cres['j']; assert j == m + 1
    uj = homog_parts(U[ex])[j]; f = comp[4]
    Hu = sp.lambdify((x, y, z), sp.hessian(uj, (x, y, z)), 'mpmath')
    gu = sp.lambdify((x, y, z), [sp.diff(uj, v) for v in (x, y, z)], 'mpmath')
    gf = sp.lambdify((x, y, z), [sp.diff(f, v) for v in (x, y, z)], 'mpmath')
    Hf = sp.lambdify((x, y, z), sp.hessian(f, (x, y, z)), 'mpmath')
    uf = sp.lambdify((x, y, z), uj, 'mpmath')
    for c in cres['crit']:
        if c['kind'] != 'min': continue
        w = mp.matrix([mp.mpf(a) for a in c['omega']]); w = w/mp.norm(w)
        gF = mp.matrix(gf(*w)); n = gF/mp.norm(gF)
        T = mp.matrix([w[1]*n[2]-w[2]*n[1], w[2]*n[0]-w[0]*n[2], w[0]*n[1]-w[1]*n[0]])
        k = -(T.T*mp.matrix(Hf(*w))*T)[0]/mp.norm(gF)
        G0 = uf(*w); gU = mp.matrix(gu(*w))
        d2 = (T.T*mp.matrix(Hu(*w))*T)[0] - j*G0 + k*(gU.T*n)[0]
        print(ex, cres['name'], 'omega', c['omega'], 'G(formula)=%s  G(engine)=%s | G\'\'(formula)=%s  G\'\'(engine)=%s | tangential grad=%s' % (
            mp.nstr(G0, 12), c['G'][:14], mp.nstr(d2, 12), c['d2G'][:14], mp.nstr((gU.T*T)[0], 3)))
for ex, ci in [('K3', 0), ('A5', 0), ('A5', 1), ('Z1', 0), ('S1', 0), ('S1', 1), ('F1', 0)]:
    if ex == 'F1':
        continue
    run(ex, ci, None)
