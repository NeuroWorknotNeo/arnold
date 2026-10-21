"""[Эксперимент] Символьная проверка тождества для производной поперечной энергии (лемма 1 в
notes/prover/2026-10-21-gt3.md).

Система  q' = v,  v' = -grad U(q)  в R^3 (евклидова метрика).
Даны: функция rho(q), векторное поле Z(q); положим Y = Z/<grad rho, Z>, так что Y rho = 1.
pi = <v, Y>, h = |Y|^2, v_perp = v - (pi/h) Y,  W = U + A(rho),
V = |v|^2/2 - pi^2/(2h) + W.
Утверждение:
  dV/dt = (pi/h) * (Y W) + A'(rho) <grad rho, v_perp> - (pi/h)^2 <v_perp, (DY) Y>
          - (pi/h) <v_perp, (DY) v_perp>,
где (DY) w = производная поля Y по направлению w.
Проверяем как тождество рациональных функций для случайных полиномиальных U, rho, Z, A.
"""
import random
import sympy as sp

random.seed(1)
q = sp.symbols('q1:4')
v = sp.symbols('v1:4')
r = sp.Symbol('r')


def rand_poly(deg, nterms=6):
    mons = [m for m in sp.itermonomials(q, deg) if sp.Poly(m, *q).total_degree() >= 1]
    expr = 0
    for _ in range(nterms):
        expr += random.randint(-3, 3) * random.choice(mons)
    return sp.expand(expr)


ok = True
for trial in range(3):
    U = rand_poly(4)
    rho = q[0] + rand_poly(2, 3) / 5
    Z = sp.Matrix([1 + rand_poly(2, 3) / 7, rand_poly(2, 3) / 7, rand_poly(2, 3) / 7])
    Aexpr = 2 * r**3 + r**4  # произвольная гладкая A
    A = sp.Lambda(r, Aexpr)
    Ap = sp.Lambda(r, sp.diff(Aexpr, r))

    grad = lambda f: sp.Matrix([sp.diff(f, qi) for qi in q])
    qv = sp.Matrix(q)
    vv = sp.Matrix(v)
    grho = grad(rho)
    Y = Z / (grho.dot(Z))
    h = Y.dot(Y)
    pi = vv.dot(Y)
    W = U + A(rho)
    V = vv.dot(vv) / 2 - pi**2 / (2 * h) + W

    gU = grad(U)
    # производная вдоль потока
    Vdot = sum(sp.diff(V, q[i]) * v[i] for i in range(3)) + sum(sp.diff(V, v[i]) * (-gU[i]) for i in range(3))

    DY = Y.jacobian(qv)  # (DY) w = DY * w
    vperp = vv - (pi / h) * Y
    YW = grad(W).dot(Y)
    rhs = (pi / h) * YW + Ap(rho) * grho.dot(vperp) - (pi / h)**2 * vperp.dot(DY * Y) - (pi / h) * vperp.dot(DY * vperp)

    # численная проверка в случайных рациональных точках (точная арифметика)
    for _ in range(5):
        pt = {s: sp.Rational(random.randint(-9, 9), random.randint(5, 13)) for s in list(q) + list(v)}
        d = sp.nsimplify(sp.simplify((Vdot - rhs).subs(pt)))
        if d != 0:
            ok = False
            print('MISMATCH', trial, d)
    print('trial', trial, 'checked')
print('identity holds at all test points (exact rational arithmetic):', ok)
