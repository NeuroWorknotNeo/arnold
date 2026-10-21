# [Эксперимент] Пример с каспом Sigma: U = (y^2 z - x^3)^2 - z^8 + x^8 + y^8 (m = 6, j = 8).
# Sigma = {y^2 z = x^3} на S^2 — кубика с каспом в e_z. Проверки: изолированность 0 (базис Грёбнера /
# исключение), условия следствия X' с полем xi_w = (2 t1, 3 t2) в гномонической карте.
import sympy as sp
x, y, z = sp.symbols('x y z', real=True)
F = y**2*z - x**3
U = F**2 - z**8 + x**8 + y**8
g = [sp.expand(sp.diff(U, v)) for v in (x, y, z)]
G = sp.groebner(g, x, y, z, order='lex')
print('базис Грёбнера (lex x>y>z), последний элемент:', sp.factor(G.exprs[-1]))
# ищем вещественные решения около 0: решаем по z последнему
lastp = sp.Poly(G.exprs[-1], z)
print('степень по z:', lastp.degree())
import numpy as np
fac = sp.factor_list(G.exprs[-1])[1]
for f, mult in fac:
    pf = sp.Poly(f, z)
    if pf.degree() > 0:
        rr = np.roots([float(cf) for cf in pf.all_coeffs()])
        print('  множитель', f if pf.degree() < 3 else '(степень %d)' % pf.degree(), ': min |корня| =', min(abs(rr)))
print('=> около 0 любая критическая точка имеет z = 0; при z = 0: U_x = 6x^5 + 8x^7, U_y = 8y^7 => x = y = 0.')
print('   проверка: U_x(x,y,0) =', sp.expand(g[0].subs(z, 0)), '; U_y(x,y,0) =', sp.expand(g[1].subs(z, 0)))
# условия в гномонической карте
t1, t2 = sp.symbols('t1 t2', real=True)
c = 1/sp.sqrt(1 + t1**2 + t2**2)
r = sp.Symbol('r', positive=True)
Upol = sp.simplify(U.subs({x: r*c*t1, y: r*c*t2, z: r*c}, simultaneous=True))
p6 = c**6*(t2**2 - t1**3)**2; p8 = c**8*(-1 + t1**8 + t2**8)
print('полярная форма U = r^6 p6 + r^8 p8:', sp.simplify(Upol - r**6*p6 - r**8*p8) == 0)
xi = (2*t1, 3*t2)
L = p8 + 1
eL = sp.simplify(xi[0]*sp.diff(L, t1) + xi[1]*sp.diff(L, t2))
e6 = sp.simplify((xi[0]*sp.diff(p6, t1) + xi[1]*sp.diff(p6, t2))/((t2**2 - t1**3)**2*c**6))
print('xi.grad p6 / p6 =', sp.simplify(e6))
tt, a = sp.symbols('tt a', real=True)
print('Lambda ~', sp.series(L.subs({t1: tt*sp.cos(a), t2: tt*sp.sin(a)}), tt, 0, 4).removeO().simplify())
print('xi.grad Lambda ~', sp.series(eL.subs({t1: tt*sp.cos(a), t2: tt*sp.sin(a)}), tt, 0, 4).removeO().simplify())
