# R52 [Эксперимент]: профиль примера (O1) из [014] (Phi0 = -1 + G1 G2, hat theta = sin cos) на луче theta = pi/4
# (hat theta = 1/2), т.е. на плоскости x = y, если реализация симметрична по x<->y (как у O2D).
import sympy as sp
e, k = sp.symbols('e k', real=True)
T = sp.Rational(1, 2)
G1 = e**2 + k*T**2*e + T**4; G2 = T**2 + k*T*e**2 + e**4
q = sp.expand(G1*G2)
for kv in [sp.Rational(19796, 10000), sp.Rational(19, 10), sp.Rational(199, 100)]:  # 8*sqrt(3)/7 ~ 1.97949
    qq = sp.Poly(q.subs(k, kv), e)
    d = qq.diff(e)
    mins = []
    for r in d.real_roots():
        rv = sp.N(r, 30); sec = d.diff(e).eval(rv)
        if sec > 0: mins.append((sp.N(rv, 8), sp.N(qq.eval(rv) - 1, 8), sp.N(sec, 6)))
    print('k =', sp.N(kv, 6), ' local minima of Phi0(pi/4, e): (e*, Phi0, Phi0\'\') =', mins)
