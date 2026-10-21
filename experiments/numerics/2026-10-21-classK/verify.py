"""verify.py -- independent brute-force check of the effective potential (no use of the series engine):
for each negative local minimum omega* of G found by analyze.py:  min over the normal line  eta |-> U(s*omega + eta*nu)
divided by s^j  must tend to G(omega*) as s->0 (error O(s)).  [Experiment], mpmath dps=60.
For point components the 2-dim normal plane p^perp is used."""
import sys, json, os
import sympy as sp, mpmath as mp
import comps
from comps import U, x, y, z, t, COMPS
mp.mp.dps = 60
HERE = os.path.dirname(os.path.abspath(__file__))

def num_funcs(ex):
    Ue = U[ex]
    f = sp.lambdify((x, y, z), Ue, 'mpmath')
    g = sp.lambdify((x, y, z), [sp.diff(Ue, v) for v in (x, y, z)], 'mpmath')
    H = sp.lambdify((x, y, z), sp.hessian(Ue, (x, y, z)), 'mpmath')
    return f, g, H

def newton_fibre(f, g, H, w, nus, s, steps=60):
    """minimise eta -> f(s*w + sum eta_a nus_a) by Newton (start at 0)"""
    r = len(nus)
    eta = mp.matrix([0]*r)
    for _ in range(steps):
        q = s*w
        for a in range(r):
            q = q + eta[a]*nus[a]
        gr = mp.matrix(g(*q)); Hh = mp.matrix(H(*q))
        ga = mp.matrix([(gr.T*nus[a])[0] for a in range(r)])
        Ha = mp.matrix(r, r)
        for a in range(r):
            for b in range(r):
                Ha[a, b] = (nus[a].T*Hh*nus[b])[0]
        d = mp.lu_solve(Ha, ga)
        eta = eta - d
        if mp.norm(d) < mp.mpf(10)**-(50)*s:
            break
    q = s*w
    for a in range(r):
        q = q + eta[a]*nus[a]
    return f(*q), eta

def omega_from(comp, crit):
    _, name, p, nu, f = comp
    if crit['t'] == 'inf':
        tau = sp.symbols('tau')
        w = [sp.limit(c/sp.sqrt(sp.factor(sum(cc**2 for cc in p))), t, sp.oo) for c in p]
        w = mp.matrix([mp.mpf(str(sp.N(c, 50))) for c in w])
    else:
        tv = sp.Float(crit['t'], 30)
        pv = [c.subs(t, tv) for c in p]
        n = sp.sqrt(sum(c**2 for c in pv))
        w = mp.matrix([mp.mpf(str(sp.N(c/n, 50))) for c in pv])
    return w

def run(ex):
    r = json.load(open(os.path.join(HERE, 'out', ex + '.json')))
    f, g, H = num_funcs(ex)
    outl = []
    for comp, cres in zip(COMPS[ex], r['components']):
        if comp[0] == 'curve':
            for crit in cres.get('crit', []):
                if crit['kind'] != 'min' or float(crit['G']) >= 0:
                    continue
                w = omega_from(comp, crit)
                nuv = sp.lambdify((x, y, z), [sp.diff(comp[4], v) for v in (x, y, z)], 'mpmath')(*w)
                nu = mp.matrix(nuv); nu = nu/mp.norm(nu)
                Gv = mp.mpf(crit['G']); j = cres['j']
                row = []
                for s in [mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4'), mp.mpf('1e-5')]:
                    val, eta = newton_fibre(f, g, H, w, [nu], s)
                    row.append(mp.nstr(val/s**j/Gv, 8))
                outl.append((cres['name'], crit['omega'], 'j=%d' % j, 'G=%s' % mp.nstr(Gv, 10), 'ratio min_eta U /(s^j G) at s=1e-2..1e-5:', row))
        elif comp[0] == 'point' and cres.get('g_j_sign', 0) < 0:
            p = mp.matrix([mp.mpf(c) for c in comp[2]]); w = p/mp.norm(p)
            ns = sp.Matrix([comp[2]]).nullspace()
            nus = [mp.matrix([mp.mpf(str(c)) for c in v]) for v in ns]
            Gv = mp.mpf(cres['g_j_float']); Gex = sp.sympify(cres['g_j']); Gv = mp.mpf(str(sp.N(Gex, 50))); j = cres['j']
            row = []
            for s in [mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4'), mp.mpf('1e-5')]:
                val, eta = newton_fibre(f, g, H, w, nus, s)
                row.append(mp.nstr(val/s**j/Gv, 8))
            outl.append((cres['name'], 'point', 'j=%d' % j, 'G=%s' % mp.nstr(Gv, 10), 'ratio at s=1e-2..1e-5:', row))
    return outl

if __name__ == '__main__':
    for ex in sys.argv[1:]:
        print('=====', ex)
        for line in run(ex):
            print(*line)
