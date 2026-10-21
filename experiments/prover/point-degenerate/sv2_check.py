"""[Эксперимент] Пример SV2 (предложен рецензентом R36): нужно именно поле следствия SV.
U = (z^4 y - z^4 x^2 - z^2 x^3)^2 + x^8 + y^8 - z^16 + x z^15, луч +e_z, c = (2,4), N = 1, beta = 16."""
import sympy as sp
x, y, z, b1, b2, tau = sp.symbols('x y z b1 b2 tau', real=True)
s = sp.symbols('s', positive=True)
U = (z**4*y - z**4*x**2 - z**2*x**3)**2 + x**8 + y**8 - z**16 + x*z**15
P = sp.Poly(sp.expand(U), x, y, z)
m = min(sum(e) for e in P.monoms())
print('m =', m, ' u_m =', sum(cf*x**a*y**b*z**c for (a, b, c), cf in zip(P.monoms(), P.coeffs()) if a+b+c == m))
F = sp.expand(U.subs({x: s**2*b1, y: s**4*b2, z: s}) / s**16)
print('F =', sp.collect(F, s))
Q = sp.expand(F.subs(s, 0) + 1)
t = b2 - b1**2 - b1**3
print('Q - [t^2 + b1^8] =', sp.expand(Q - (t**2 + b1**8)))
xi = (b1, 2*b2 + b1**3)
xiQ = sp.expand(xi[0]*sp.diff(Q, b1) + xi[1]*sp.diff(Q, b2))
print('xi.gradQ - (4 t^2 + 8 b1^8) =', sp.expand(xiQ - (4*t**2 + 8*b1**8)))
EcQ = sp.expand(2*b1*sp.diff(Q, b1) + 4*b2*sp.diff(Q, b2))
pt = {b2: b1**2 + b1**3 + b1**3/4}
print('E_c Q at t = b1^3/4:', sp.factor(EcQ.subs(pt)), ';  Q there:', sp.factor(Q.subs(pt)))
l1, l2 = sp.symbols('lambda1 lambda2', positive=True)
DQ = sp.expand(l1*b1*sp.diff(Q, b1) + l2*b2*sp.diff(Q, b2))
print('diag field, lambda2=2lambda1, at t=b1^3/4:', sp.factor(DQ.subs(l2, 2*l1).subs(pt)))
ptt = {b2: b1**2 + b1**3 + tau*b1**4}
lead = sp.series(sp.expand(DQ.subs(ptt)), b1, 0, 8).removeO()
print('diag field at t = tau b1^4, terms up to b1^7:', sp.factor(lead))
