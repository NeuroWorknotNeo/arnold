# R52: пример O2D — симметрия x<->y, инвариантная плоскость x=y, профиль на ней;
# отсутствие локальных минимумов Phi0 вне F_min (точная часть + сертифицированные знаки на t=+-1/2).
import sympy as sp
x, y, z, u, e, t = sp.symbols('x y z u e t', real=True)
TH = sp.Symbol('T')
A = (TH - e**2)**2 + e**8; B = (TH - e**2 - e**3)**2 + e**8
AB = sp.Poly(sp.expand(A*B), TH, e)
U = sum(a*z**l*(x*y)**k*(x**2 + y**2)**(16 - l - k) for (k, l), a in AB.terms()) - (x**2 + y**2)**16
U = sp.expand(U)
print('U(x,y,z) == U(y,x,z):', sp.expand(U - U.subs({x: y, y: x}, simultaneous=True)) == 0)
print('U(x,y,z) == U(-y,-x,z):', sp.expand(U - U.subs({x: -y, y: -x}, simultaneous=True)) == 0)
Ux, Uy = sp.diff(U, x), sp.diff(U, y)
print('U_x == U_y on x = y:', sp.expand((Ux - Uy).subs(y, x)) == 0)
# restricted potential V(u,z) = U(u/sqrt2, u/sqrt2, z); V(u, u^2 eps) = u^32 Phi0(pi/4, eps)
V = sp.expand(U.subs({x: u/sp.sqrt(2), y: u/sp.sqrt(2)}))
Q12 = sp.expand(A*B).subs(TH, sp.Rational(1, 2))
print('V(u, u^2 e) == u^32 (Q(1/2,e) - 1):', sp.expand(V.subs(z, u**2*e) - u**32*(Q12 - 1)) == 0)
# real critical points of q(e) = Q(1/2, e): certified isolation
q = sp.Poly(Q12, e); dq = q.diff(e); d2q = dq.diff(e)
Qt12 = sp.Poly(sp.diff(sp.expand(A*B), TH).subs(TH, sp.Rational(1, 2)), e)
print('gcd(q\', Q_t(1/2,.)) =', sp.gcd(dq, Qt12), ' gcd(q\', q\'\') =', sp.gcd(dq, d2q))
for r in dq.real_roots():
    rv = sp.N(r, 40)
    print('  root of q\':', sp.N(r, 15), ' q =', sp.N(q.eval(rv), 15), " q''=", sp.N(d2q.eval(rv), 10), ' Q_t =', sp.N(Qt12.eval(rv), 10))
# same at T = -1/2
Qm = sp.Poly(sp.expand(A*B).subs(TH, -sp.Rational(1, 2)), e); dqm = Qm.diff(e)
Qtm = sp.Poly(sp.diff(sp.expand(A*B), TH).subs(TH, -sp.Rational(1, 2)), e)
print('T=-1/2: gcd(q\', Q_t) =', sp.gcd(dqm, Qtm))
for r in dqm.real_roots():
    rv = sp.N(r, 40)
    print('  root of q\':', sp.N(r, 15), ' q =', sp.N(Qm.eval(rv), 15), " q''=", sp.N(dqm.diff(e).eval(rv), 10), ' Q_t =', sp.N(Qtm.eval(rv), 10))
