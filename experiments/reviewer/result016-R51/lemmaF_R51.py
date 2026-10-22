# R51: проверка полей лемм F2, F3 на примерах (results/016-fold.md, §3.1) и тождества лемы 0(b).
# [Эксперимент]: символьные тождества + численный минимум X_p P / P на малой окрестности.
import sympy as sp
import numpy as np

th, ep, u = sp.symbols('theta varepsilon u', real=True)

print('--- (F2): вертикальная точка, F = theta - eps^3 + theta*eps, k=1, ptilde = 1 + theta + eps^2 + theta*eps')
F = th - ep**3 + th*ep        # dF/deps(0)=0, dF/dtheta(0)=1
pt = 1 + th + ep**2 + th*ep
P = F**2*pt
# {F=0}: theta = eps^3/(1+eps) =: g(eps)
g = u**3/(1+u)
print('F on graph theta=g(eps):', sp.simplify(F.subs(th, g.subs(u, ep))))
q = sp.simplify(g/sp.diff(g, u))
print('q = g/g\' =', q, ' series:', sp.series(q, u, 0, 4))
Xp_th = th
Xp_ep = q.subs(u, ep)
F1 = th - g.subs(u, ep)
print('X_p F1 - F1 =', sp.simplify(Xp_th*sp.diff(F1, th) + Xp_ep*sp.diff(F1, ep) - F1))
XP = sp.simplify(Xp_th*sp.diff(P, th) + Xp_ep*sp.diff(P, ep))
f = sp.lambdify((th, ep), sp.simplify(XP/P), 'numpy')
for r in [0.2, 0.1, 0.05]:
    T, E = np.meshgrid(np.linspace(-r, r, 401), np.linspace(-r, r, 401))
    with np.errstate(all='ignore'):
        vals = f(T, E)
    vals = vals[np.isfinite(vals)]
    print('  box r=%.2f: min X_pP/P = %.4f (claim >= k=1)' % (r, vals.min()))

print('--- (F3): P = (eps - theta)^2 (eps + theta^2)^4 * (1+theta-eps), k1=1,k2=2, m0=1')
phi1, phi2 = th, -th**2
pt = 1 + th - ep
P = (ep - phi1)**2*(ep - phi2)**4*pt
M = sp.simplify(th*(sp.diff(phi2, th) - sp.diff(phi1, th))/(phi2 - phi1))
print('M =', M)
Xth = th
Xep = th*sp.diff(phi1, th) + (ep - phi1)*M
for ph in (phi1, phi2):
    print('X(eps-phi) - M(eps-phi) =', sp.simplify(Xth*sp.diff(ep-ph, th) + Xep*sp.diff(ep-ph, ep) - M*(ep-ph)))
XP = sp.simplify(Xth*sp.diff(P, th) + Xep*sp.diff(P, ep))
f = sp.lambdify((th, ep), sp.simplify(XP/P), 'numpy')
for r in [0.2, 0.1, 0.05]:
    T, E = np.meshgrid(np.linspace(-r, r, 401), np.linspace(-r, r, 401))
    with np.errstate(all='ignore'):
        vals = f(T, E)
    vals = vals[np.isfinite(vals)]
    print('  box r=%.2f: min X_pP/P = %.4f (claim >= 3/2 near p)' % (r, vals.min()))

print('--- лемма 0(b): P = (eps - sin theta)^4 (1 + eps^2), Phi0 = P - a0; (CM) с r\'=2 на ветви eps_b = sin theta')
e = sp.Symbol('e')
P = (ep - sp.sin(th))**4*(1 + ep**2)
Pe = sp.expand(P.subs(ep, sp.sin(th) + e))
coeffs = sp.Poly(Pe, e).all_coeffs()[::-1]
print('coefficients e^0..e^3 vanish:', [sp.simplify(cc) for cc in coeffs[:4]], ' p(theta,0)=', sp.simplify(coeffs[4]))
