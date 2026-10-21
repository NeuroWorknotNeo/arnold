# [Эксперимент] Пример с касанием ветвей Sigma: U = y^2 (y z - x^2)^2 - z^8 + x^8 + y^8 (m = 6, j = 8).
# Sigma около e_z: {y = 0} и {y z = x^2} — касаются в e_z (в гномонической карте t2 = 0 и t2 = t1^2).
# Проверки: изолированность 0 (исключение), условия следствия X' с полем xi_w = (t1, 2 t2).
import sympy as sp, numpy as np
x, y, z = sp.symbols('x y z', real=True)
U = y**2*(y*z - x**2)**2 - z**8 + x**8 + y**8
g = [sp.expand(sp.diff(U, v)) for v in (x, y, z)]
G = sp.groebner(g, x, y, z, order='lex')
last = G.exprs[-1]
print('последний элемент базиса (по z):', sp.factor(last))
for f, mult in sp.factor_list(last)[1]:
    pf = sp.Poly(f, z)
    if pf.degree() > 0:
        rr = np.roots([float(cf) for cf in pf.all_coeffs()])
        print('  множитель степени', pf.degree(), ': min |корня| =', min(abs(rr)))
print('при z = 0: grad =', [sp.factor(gg.subs(z, 0)) for gg in g])
t1, t2, r = sp.symbols('t1 t2 r', real=True)
c = 1/sp.sqrt(1 + t1**2 + t2**2)
Upol = sp.simplify(U.subs({x: r*c*t1, y: r*c*t2, z: r*c}, simultaneous=True))
p6 = c**6*t2**2*(t2 - t1**2)**2; p8 = c**8*(-1 + t1**8 + t2**8)
print('полярная форма U = r^6 p6 + r^8 p8:', sp.simplify(Upol - r**6*p6 - r**8*p8) == 0)
xi = (t1, 2*t2)
print('xi.grad p6 / p6 =', sp.simplify((xi[0]*sp.diff(p6, t1) + xi[1]*sp.diff(p6, t2))/p6))
L = p8 + 1
eL = xi[0]*sp.diff(L, t1) + xi[1]*sp.diff(L, t2)
tt, a = sp.symbols('tt a', real=True)
print('Lambda ~', sp.series(L.subs({t1: tt*sp.cos(a), t2: tt*sp.sin(a)}), tt, 0, 4).removeO().simplify())
print('xi.grad Lambda ~', sp.series(eL.subs({t1: tt*sp.cos(a), t2: tt*sp.sin(a)}), tt, 0, 4).removeO().simplify())
