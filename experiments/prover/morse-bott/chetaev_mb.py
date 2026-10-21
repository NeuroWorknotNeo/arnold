# [Эксперимент] Радиальное условие Четаева <grad U, q> < 0 на {U < 0} около дна оврага
# для примеров записки notes/prover/2026-10-21-morse-bott.md. Точки q = s omega(phi) + eta n(phi),
# s = 10^-2, 10^-3, 10^-4, phi и eta случайны в окрестности дна (|eta - eta*| <= 3 s^c'), берутся только точки с U < 0.
# Печатается доля точек с <grad U, q> > 0 и max <grad U,q>/|U|.
import sys, random
import sympy as sp
import mpmath as mp
from examples_mb import EXAMPLES, gk, omP, x, y, z, s as S_
mp.mp.dps = 30
S2 = mp.sqrt(2)
ph = sp.Symbol('phi', real=True)
for name, cw, phr in [('C2', mp.mpf(5)/2, None), ('C1', mp.mpf(2), None), ('D1', mp.mpf(5)/2, (mp.pi - 0.3, mp.pi + 0.3)),
                      ('D2', mp.mpf(5)/2, (mp.pi - 0.6, mp.pi + 0.6)), ('B', mp.mpf(2), (-0.5, 0.5)), ('D3', mp.mpf(7)/2, (mp.pi - 0.3, mp.pi + 0.3))]:
    U, m = EXAMPLES[name]
    ys, g = gk(U, m, omP, 3)
    eta_f = sp.lambdify((S_, ph), sp.expand(S_*ys[0]), 'mpmath')
    Uf = sp.lambdify((x, y, z), U, 'mpmath')
    rad = sp.lambdify((x, y, z), sp.expand(x*sp.diff(U, x) + y*sp.diff(U, y) + z*sp.diff(U, z)), 'mpmath')
    random.seed(3)
    for sv in (mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')):
        npos = ntot = 0; mx = -mp.inf
        for _ in range(3000):
            phv = 2*mp.pi*random.random() if phr is None else phr[0] + (phr[1] - phr[0])*random.random()
            w = [mp.cos(phv)/S2, mp.sin(phv)/S2, 1/S2]; n = [-mp.cos(phv)/S2, -mp.sin(phv)/S2, 1/S2]
            eta = eta_f(sv, phv) + sv**cw*3*(2*random.random() - 1)
            q = [sv*w[i] + eta*n[i] for i in range(3)]
            u = Uf(*q)
            if u >= 0: continue
            ntot += 1; r = rad(*q)
            if r > 0: npos += 1
            mx = max(mx, r/abs(u))
        print('%-3s s=%-6s: точек U<0: %4d, из них <grad U,q> > 0: %4d, max <grad U,q>/|U| = %s'
              % (name, mp.nstr(sv, 2), ntot, npos, mp.nstr(mx, 4)))
