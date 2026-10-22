"""R47: независимая проверка §2 записки fold (пример O2)."""
import sympy as sp
x, y, z, s, th, e, t, Y = sp.symbols('x y z s theta epsilon t Y', real=True)
rho2 = x**2 + y**2
U = z**4 - 2*z**2*y*rho2 - x**2*rho2**2 + x**7 + y**7
print('1. global form:', sp.expand(U - ((z**2 - y*rho2)**2 - rho2**3 + x**7 + y**7)) == 0)
# first edge data from phi(s,theta,y) = sum s^{k-m} u_k(omega + y n), m = 4
om = (sp.cos(th), sp.sin(th), 0)
hom = sp.Poly(sp.expand(U), x, y, z)
phi = 0
for (i, j, k), co in hom.terms():
    deg = i + j + k
    phi += co*s**(deg-4)*om[0]**i*om[1]**j*Y**k
phi = sp.expand(phi)
P2 = sp.Poly(phi, s, Y)
S = {}
for (i, l), co in P2.terms():
    S[(i, l)] = S.get((i, l), 0) + co
print('support S (i,l):', sorted(S))
r = 2
gam = min(sp.Rational(i, 2*r - l) for (i, l) in S if l < 2*r)
print('gamma_* =', gam, ' c =', 1+gam, ' j =', 4 + 2*r*gam)
Phi0 = sum(co*e**l for (i, l), co in S.items() if i + gam*l == 2*r*gam)
print('Phi0 - ((e^2 - sin th)^2 - 1) =', sp.simplify(Phi0 - ((e**2 - sp.sin(th))**2 - 1)))
# (2.1)
sub = {x: s*sp.cos(th), y: s*sp.sin(th), z: s**sp.Rational(3, 2)*e}
lhs = sp.expand(U.subs(sub), trig=False)
g = sp.cos(th)**7 + sp.sin(th)**7
s_pos = sp.Symbol('s', positive=True)
print('(2.1):', sp.simplify((lhs - s**6*((e**2 - sp.sin(th))**2 - 1 + s*g)).subs(s, s_pos)) == 0)
# 3. bottom
f = e**2 - sp.sin(th)
grad = (sp.diff(f, th), sp.diff(f, e))
crit = sp.solve([grad[0], grad[1]], [th, e], dict=True)
print('zeros of grad f:', crit, ' f there:', [f.subs(cc) for cc in crit])
# 4. g(pi - t)
print('g(pi-t) series:', sp.series(g.subs(th, sp.pi - t), t, 0, 8))
# numeric: min over theta of G_min + s g for several s
import numpy as np
TH = np.linspace(0, 2*np.pi, 2000001)
Gmin = np.where(np.sin(TH) >= 0, -1.0, -np.cos(TH)**2)
gv = np.cos(TH)**7 + np.sin(TH)**7
for sv in [0.9, 0.5, 0.1, 1e-3]:
    vals = Gmin + sv*gv
    k = np.argmin(vals)
    print('s=%g: min=%.12f (-1-s=%.12f) at theta=%.6f (pi=%.6f)' % (sv, vals[k], -1-sv, TH[k], np.pi))
# Gmin check by brute force in e
EE = np.linspace(-2, 2, 40001)
for thv in [-2.0, -0.5, 0.3, 1.0, 2.5, 4.0]:
    m = np.min((EE**2 - np.sin(thv))**2 - 1)
    pred = -1.0 if np.sin(thv) >= 0 else -np.cos(thv)**2
    print('Gmin(%.2f): brute %.8f pred %.8f' % (thv, m, pred))
# 5. W2
sub2 = {x: -s*sp.cos(t), y: s*sp.sin(t)}
W2 = (U + rho2**3 + (x**2+y**2)**sp.Rational(7, 2)).subs(sub2)
W2 = sp.simplify(sp.expand(sp.expand_trig(W2)).subs(s, s_pos))
Gt = 1 - sp.cos(t)**7 + sp.sin(t)**7
print('(2.2):', sp.simplify(W2 - ((z**2 - s_pos**3*sp.sin(t))**2 + s_pos**7*Gt)) == 0)
print('Gtilde series:', sp.series(Gt, t, 0, 8))
# 6. blow-up profile
d = sp.Symbol('delta', positive=True)
T, E = sp.symbols('T E', real=True)
expr = ((d**sp.Rational(1, 4)*E)**2 - sp.sin(sp.sqrt(d)*T))**2/d
print('blow-up limit:', sp.limit(expr, d, 0))
# 7. two-level profile
v = sp.Symbol('v', real=True)
expr7 = v**2 + Gt.subs(t, sp.asin(e**2))
print('two-level profile series in e:', sp.series(expr7, e, 0, 10))
# 8. surface: y(x^2+y^2) = z^2 near (-1,0,0)
Fs = y*(x**2 + y**2) - z**2
print('dF/dy at (-1,0,0):', sp.diff(Fs, y).subs({x: -1, y: 0, z: 0}))
