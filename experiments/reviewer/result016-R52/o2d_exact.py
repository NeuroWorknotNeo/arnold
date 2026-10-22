# R52: точные проверки примера O2D (sympy, рациональная арифметика).
# 1) построение U_O2D по (O.2) и тождество U(s cos, s sin, s^2 eps) = s^32 (AB - 1);
# 2) младшая форма, квазиоднородность весов (1,1,2) степени 32;
# 3) изолированность критической точки 0 над R:
#    U квазиоднородна => вне оси z критические точки <=> критические точки Phi0 на уровне Phi0 = 0;
#    на оси z: U = z^16.
import sympy as sp
x, y, z, s, th, e, t, lam = sp.symbols('x y z s theta epsilon t lambda', real=True)
TH = sp.Symbol('T')  # hat theta
A = (TH - e**2)**2 + e**8
B = (TH - e**2 - e**3)**2 + e**8
AB = sp.Poly(sp.expand(A*B), TH, e)
U = 0
for (k, l), a in AB.terms():
    assert k + l <= 16, (k, l)
    U += a * z**l * (x*y)**k * (x**2 + y**2)**(16 - l - k)
U -= (x**2 + y**2)**16
U = sp.expand(U)
print('U_O2D: number of terms', len(sp.Poly(U, x, y, z).terms()), ', total degree', sp.Poly(U, x, y, z).total_degree())
# 1) identity
sub = U.subs({x: s*sp.cos(th), y: s*sp.sin(th), z: s**2*e})
rhs = s**32*(sp.expand(A*B).subs(TH, sp.sin(th)*sp.cos(th)) - 1)
print('identity U(s cos, s sin, s^2 e) - s^32 Phi0 == 0 :', sp.simplify(sp.expand(sp.expand_trig(sub - rhs)).rewrite(sp.exp)) == 0)
# 2) weighted homogeneity and lowest form
wh = sp.expand(U.subs({x: lam*x, y: lam*y, z: lam**2*z}) - lam**32*U)
print('weighted homogeneous (1,1,2), degree 32:', wh == 0)
P = sp.Poly(U, x, y, z)
mindeg = min(sum(m) for m in P.monoms())
low = sum(c*x**m[0]*y**m[1]*z**m[2] for m, c in P.terms() if sum(m) == mindeg)
print('lowest degree', mindeg, ' lowest form:', low)
# 3) isolation
Q = sp.expand(A*B).subs(TH, t)
Qt, Qe = sp.diff(Q, t), sp.diff(Q, e)
R = sp.factor(sp.resultant(Qt, Qe, t))
print('Res_t(Q_t, Q_e) =', R)
print('Q_t(t,0) =', sp.factor(Qt.subs(e, 0)), '; Q_e(t,0) =', sp.factor(Qe.subs(e, 0)))
for tb in (sp.Rational(1, 2), -sp.Rational(1, 2)):
    q = sp.expand(Q.subs(t, tb))
    r = sp.resultant(q - 1, sp.diff(q, e), e)
    print(f't={tb}: Res_e(Q-1, Q_e) = {sp.nsimplify(r)} (nonzero => no critical point of Phi0 at level 0 on cos2theta=0)')
# z-axis
print('U(0,0,z) =', sp.factor(U.subs({x: 0, y: 0})))
