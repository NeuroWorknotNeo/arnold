"""[Эксперимент] R20: замечания 2 и 3 §3.3 записки gt3-hardcore.

1. Пример теоремы B: U=(x^2+y^2-z^2)^2+x z^4; g_5=sqrt2 cos(phi)/8, g_6=-9cos^2(phi)/512.
2. Случайные u_{m+1}, u_{m+2} (d=0 и d=1): g_{m+1}=u_{m+1}(omega),
   g_{m+2}=u_{m+2}(omega)-1/2 b^T H^{-1} b.
3. Чётность g_k(-omega)=(-1)^k g_k(omega).
Точная рациональная арифметика (cos phi=3/5, sin phi=4/5 и т. п.).
"""
import random
import sympy as sp
from reduced import reduced_series

x, y, z = X = sp.symbols('x y z')
Q0 = x**2 + y**2 - z**2


def omega_cone(c, sn, sign=1):
    r2 = sp.sqrt(2)
    return [sign * c / r2, sign * sn / r2, sign * 1 / r2], [[-c / r2, -sn / r2, 1 / r2]]


def coeffs(R, s, kmax):
    return [sp.nsimplify(sp.simplify(R.coeff(s, i))) for i in range(kmax + 1)]


print('--- 1. пример теоремы B ---')
U = Q0**2 + x * z**4
for (c, sn) in [(sp.Rational(3, 5), sp.Rational(4, 5)), (sp.Integer(1), sp.Integer(0)),
                (sp.Rational(-5, 13), sp.Rational(12, 13))]:
    om, fr = omega_cone(c, sn)
    R, ys, s, H0 = reduced_series(U, X, om, fr, 4, 3)
    cf = coeffs(R, s, 3)
    print('cos phi =', c, ' H =', H0, ' g5 =', cf[1], ' ожид.', sp.sqrt(2) * c / 8,
          ' g6 =', cf[2], ' ожид.', -9 * c**2 / 512)
    assert sp.simplify(cf[1] - sp.sqrt(2) * c / 8) == 0
    assert sp.simplify(cf[2] + 9 * c**2 / 512) == 0


def rand_form(deg, rng):
    mons = [x**i * y**j * z**(deg - i - j) for i in range(deg + 1) for j in range(deg + 1 - i)]
    return sum(sp.Integer(rng.randint(-3, 3)) * mm for mm in mons)


def formula_check(U_m, U_m1, U_m2, om, fr, m, label):
    U = U_m + U_m1 + U_m2
    R, ys, s, H0 = reduced_series(U, X, om, fr, m, 2)
    cf = coeffs(R, s, 2)
    sub = dict(zip(X, om))
    g1 = U_m1.subs(sub)
    grad1 = [sp.diff(U_m1, v).subs(sub) for v in X]
    b = sp.Matrix([sum(grad1[i] * e[i] for i in range(3)) for e in fr])
    Hm = sp.Matrix(len(fr), len(fr), lambda a, bb: sum(
        sp.diff(U_m, X[i], X[j]).subs(sub) * fr[a][i] * fr[bb][j] for i in range(3) for j in range(3)))
    g2 = U_m2.subs(sub) - sp.Rational(1, 2) * (b.T * Hm.inv() * b)[0]
    ok1 = sp.simplify(cf[1] - g1) == 0
    ok2 = sp.simplify(cf[2] - g2) == 0
    print(label, 'g_{m+1}:', ok1, ' g_{m+2}:', ok2)
    assert ok1 and ok2
    return R, s


print('--- 2. случайные проверки формулы g_{m+2} ---')
rng = random.Random(20)
# d=0, n=3, omega=(1,0,0), u_4=(x^2+y^2+z^2)(y^2+2z^2+yz): H=diag-ish >0 на omega^perp
u4p = (x**2 + y**2 + z**2) * (y**2 + 2 * z**2 + y * z)
for t in range(4):
    formula_check(u4p, rand_form(5, rng), rand_form(6, rng), [1, 0, 0], [[0, 1, 0], [0, 0, 1]], 4,
                  'd=0, тест %d' % t)
# d=1: u_4=Q0^2 * (1 + ...)?  берём u_4 = Q0^2, точки конуса
for t in range(3):
    om, fr = omega_cone(sp.Rational(3, 5), sp.Rational(4, 5))
    formula_check(Q0**2, rand_form(5, rng), rand_form(6, rng), om, fr, 4, 'd=1, тест %d' % t)

print('--- 3. чётность g_k(-omega)=(-1)^k g_k(omega) ---')
U = Q0**2 + rand_form(5, rng) + rand_form(6, rng) + rand_form(7, rng)
om, fr = omega_cone(sp.Rational(3, 5), sp.Rational(4, 5))
omm, frm = omega_cone(sp.Rational(3, 5), sp.Rational(4, 5), sign=-1)
R1, ys1, s, _ = reduced_series(U, X, om, fr, 4, 3)
R2, ys2, s, _ = reduced_series(U, X, omm, frm, 4, 3)
for i in range(1, 4):
    k = 4 + i
    a, bq = sp.simplify(R1.coeff(s, i)), sp.simplify(R2.coeff(s, i))
    print('k=%d' % k, 'g_k(om)=', a, ' g_k(-om)=', bq, ' ok:', sp.simplify(bq - (-1)**k * a) == 0)
    assert sp.simplify(bq - (-1)**k * a) == 0
print('все проверки прошли')
