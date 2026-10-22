# [Эксперимент] Рецензент R48: символьные проверки к notes/prover/2026-10-21-fold.md, §§4-6.
# Запуск: ~/venv/bin/python symbolic_checks.py
import sympy as sp

th, e, s, u, tau = sp.symbols('theta epsilon s u tau', real=True)
x, y, z = sp.symbols('x y z', real=True)
ok = lambda name, expr: print(('OK  ' if sp.simplify(expr) == 0 else 'FAIL'), name)

# 1. (2.1) для O2
rho2 = x**2 + y**2
U = z**4 - 2*z**2*y*rho2 - x**2*rho2**2 + x**7 + y**7
sub = {x: s*sp.cos(th), y: s*sp.sin(th), z: s**sp.Rational(3, 2)*e}
g = sp.cos(th)**7 + sp.sin(th)**7
ok('(2.1) U(Pi)=s^6[(e^2-sin)^2-1+s g]', sp.expand(U.subs(sub) - s**6*((e**2 - sp.sin(th))**2 - 1 + s*g)))

# 2. X_0 f = f/2 (обе формулы X_0^eps), chi -- произвольная функция
chi = sp.Function('chi')(th)
f = e**2 - sp.sin(th)
X0t = chi*sp.tan(th)/2
X0e_O2 = (e**2 - (1 - chi)*sp.sin(th))/(4*e)
ok('X0 f = f/2 на O2', X0t*sp.diff(f, th) + X0e_O2*sp.diff(f, e) - f/2)
ok('X0 f = f/2 на O1 (chi=1, X^eps=e/4)', (sp.tan(th)/2)*sp.diff(f, th) + (e/4)*sp.diff(f, e) - f/2)

# 3. (F2): общая g с g(0)=g'(0)=0 -- в виде ряда g = a2 u^2 + a3 u^3 + ...; X_p F1 = F1 тождественно
G = sp.Function('G')
F1 = tau - G(e)
q = G(e)/sp.diff(G(e), e)
ok('(F2) X_p F1 = F1 (tau d_tau + q d_e)', tau*sp.diff(F1, tau) + q*sp.diff(F1, e) - F1)
# аналитичность q = g/g' при g = a u^m0 (1+...): проверка ряда
a2, a3, a4 = sp.symbols('a2 a3 a4')
for m0 in (2, 3, 4):
    gg = a2*u**m0 + a3*u**(m0+1) + a4*u**(m0+2)
    qq = sp.series(gg/sp.diff(gg, u), u, 0, 3).removeO()
    print('    (F2) m0=%d: g/g\' = %s' % (m0, sp.simplify(qq)))
# фактическая складка O2 в (0,0): Gamma = {theta = arcsin(eps^2)}
gO2 = sp.asin(u**2)
print('    (F2) O2: q(u)=g/g\' =', sp.series(gO2/sp.diff(gO2, u), u, 0, 8))

# 4. (F3): X_p(eps-phi_i) = M (eps - phi_i)
p1 = sp.Function('phi1')(tau)
p2 = sp.Function('phi2')(tau)
M = tau*(sp.diff(p2, tau) - sp.diff(p1, tau))/(p2 - p1)
Xe3 = tau*sp.diff(p1, tau) + (e - p1)*M
for nm, ph in (('phi1', p1), ('phi2', p2)):
    expr = tau*sp.diff(e - ph, tau) + Xe3*sp.diff(e - ph, e) - M*(e - ph)
    ok('(F3) X_p(eps-%s) = M(eps-%s)' % (nm, nm), sp.together(expr))

# 5. касп (F4)
P = (e**2 - tau**3)**2
ok('(F4) касп: (tau d_tau + 3/2 e d_e)P = 6P', tau*sp.diff(P, tau) + sp.Rational(3, 2)*e*sp.diff(P, e) - 6*P)

# 6. одиночная складка (6.2): (2tau d_tau + e d_e)((tau-e^2)^2+e^{2q})
qq = sp.symbols('q', positive=True, integer=True)
P = (tau - e**2)**2 + e**(2*qq)
expr = sp.expand(2*tau*sp.diff(P, tau) + e*sp.diff(P, e) - 4*(tau - e**2)**2 - 2*qq*e**(2*qq))
ok('(6.2) одиночная складка: XP = 4(tau-e^2)^2 + 2q e^{2q}', sp.simplify(expr))

# 7. скачок кратности: P = F^2(F^2+tau^2), XP = 4P
Fv = sp.symbols('F', real=True)
P = Fv**2*(Fv**2 + tau**2)
ok('(6.2) скачок кратности: (tau d_tau + F d_F)P = 4P', tau*sp.diff(P, tau) + Fv*sp.diff(P, Fv) - 4*P)

# 8. O2D: реализация U(s cos, s sin, s^2 eps) = s^32 (AB - 1), младшая форма z^16
xh = sp.symbols('xh', real=True)   # \hat theta
A = (xh - e**2)**2 + e**8
B = (xh - e**2 - e**3)**2 + e**8
AB = sp.Poly(sp.expand(A*B), xh, e)
Uo = 0
maxkl = 0
for (k, l), c in AB.terms():
    maxkl = max(maxkl, k + l)
    Uo += c*z**l*(x*y)**k*(x**2 + y**2)**(16 - l - k)
Uo -= (x**2 + y**2)**16
print('    O2D: max(k+l) =', maxkl)
subd = {x: s*sp.cos(th), y: s*sp.sin(th), z: s**2*e}
lhs = sp.expand(Uo.subs(subd))
rhs = sp.expand(s**32*((A*B).subs(xh, sp.sin(th)*sp.cos(th)) - 1))
diff = sp.simplify(sp.expand_trig(lhs - rhs))
print(('OK  ' if diff == 0 else 'CHECK'), 'O2D: U(s cos, s sin, s^2 eps) = s^32(AB-1)', '' if diff == 0 else diff)
Upoly = sp.Poly(sp.expand(Uo), x, y, z)
mindeg = min(sum(mon) for mon in Upoly.monoms())
low = sum(c*x**a*y**b*z**cc for (a, b, cc), c in Upoly.terms() if a + b + cc == mindeg)
print('    O2D: младшая степень', mindeg, ' младшая форма:', low)

# 9. 6.2(b) для O2D: нетреугольное поле xi = (3/2 x - 1/2 y^2, 1/2 y) даёт xi(AB) >= 6AB
X1 = sp.Rational(3, 2)*xh - e**2/2
X2 = e/2
expr = sp.expand(X1*sp.diff(A*B, xh) + X2*sp.diff(A*B, e) - 6*A*B)
print('    O2D: xi(AB) - 6AB =', sp.factor(expr), '(>=0)')
