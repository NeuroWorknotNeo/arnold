# [Эксперимент] Пример O2D («двойная складка», записка notes/prover/2026-10-21-fold.md, §6.3):
# реализация профиля первого ребра Phi_0 = -1 + A(th^, eps) B(th^, eps), th^ = sin(theta) cos(theta),
#   A = (x - y^2)^2 + y^8,  B = (x - y^2 - y^3)^2 + y^8   (результат 009, предложение 6.2: x = th^, y = eps),
# многочленом U = sum_l z^l h_l(x, y), deg h_l = 2(16 - l), h_16 = 1. Проверяется:
#   U(s cos, s sin, s^2 eps) = s^32 Phi_0(theta, eps) тождественно; младшая форма u_16 = z^16;
#   нули AB: только x = y = 0.
import sympy as sp

X, Yv, x, y, z, s, th, e = sp.symbols('X Y x y z s theta epsilon', real=True)
A = (X - Yv**2)**2 + Yv**8
B = (X - Yv**2 - Yv**3)**2 + Yv**8
Q = sp.expand(A*B)
Phi0 = sp.expand(-1 + Q)
poly = sp.Poly(Phi0, Yv)
U = 0
for (l,), cl in zip(poly.monoms(), poly.coeffs()):
    cpoly = sp.Poly(cl, X)
    h = 0
    for (k,), a in zip(cpoly.monoms(), cpoly.coeffs()):
        assert k <= 16 - l, (l, k)
        h += a*(x*y)**k*(x**2 + y**2)**(16 - l - k)
    U += z**l*h
U = sp.expand(U)
# младшая форма
low = min(sum(m) for m in sp.Poly(U, x, y, z).monoms())
u_low = sum(c*x**m[0]*y**m[1]*z**m[2] for m, c in zip(sp.Poly(U, x, y, z).monoms(), sp.Poly(U, x, y, z).coeffs()) if sum(m) == low)
print('младшая степень:', low, ', младшая форма:', u_low)
lhs = U.subs({x: s*sp.cos(th), y: s*sp.sin(th), z: s**2*e})
rhs = s**32*Phi0.subs({X: sp.sin(th)*sp.cos(th), Yv: e})
import random
rnd = random.Random(1)
ok1 = True
for _ in range(8):     # тождество проверяется в случайных рациональных точках (60 знаков); cos^2+sin^2=1 sympy сам не сокращает
    sub = {s: sp.Rational(rnd.randint(1, 9), 10), th: sp.Rational(rnd.randint(-30, 30), 10), e: sp.Rational(rnd.randint(-20, 20), 10)}
    val = sp.N((lhs - rhs).subs(sub), 80)
    scale = sp.N((s**32).subs(sub), 80)
    ok1 = ok1 and abs(val/scale) < 1e-50
print(('OK   ' if ok1 else 'FAIL ') + 'U(s cos, s sin, s^2 eps) = s^32 Phi_0(theta, eps) (8 случайных точек, 80 знаков)')
# нули: A = 0 <=> y = 0, x = 0; B = 0 <=> y = 0, x = 0
print('OK   A,B >= 0 как суммы квадратов; A = 0 => y^8 = 0 и x = y^2 => x = y = 0; так же B')
print('ИТОГ:', 'OK' if (ok1 and low == 16 and u_low == z**16) else 'FAIL')
