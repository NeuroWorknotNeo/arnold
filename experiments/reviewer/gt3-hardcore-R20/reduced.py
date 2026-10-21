"""[Эксперимент] Рецензент R20: независимый расчёт редуцированной функции R(s) леммы K1.

Для полиномиального U, точки omega (u_m(omega)=0, grad u_m(omega)=0) и ортонормированной
рамки e_a нормального пространства N считаем
    phi(s, y) = s^{-m} U(s(omega + sum y_a e_a)),
решаем d_y phi = 0 рядом y*(s) = sum_{i>=1} Y_i s^i (итерации Ньютона по степеням s)
и выдаём ряд R(s) = phi(s, y*(s)) до заданного порядка.
Это не зависит от выкладок записки (формулы g_{m+1}, g_{m+2} проверяются отдельно).
"""
import sympy as sp


def reduced_series(U, X, omega, frame, m, order, params=()):
    s = sp.Symbol('s')
    p = len(frame)
    ys = sp.symbols('y0:%d' % p)
    pt = [s * (omega[i] + sum(ys[a] * frame[a][i] for a in range(p))) for i in range(len(X))]
    phi = sp.expand(sp.expand(U.subs(dict(zip(X, pt)), simultaneous=True)) / s**m)
    phi = sp.simplify(phi) if params else phi
    grad = [sp.diff(phi, ya) for ya in ys]
    H0 = sp.Matrix(p, p, lambda a, b: sp.diff(phi, ys[a], ys[b]).subs({s: 0, **{y: 0 for y in ys}}))
    H0inv = H0.inv()
    ystar = [sp.Integer(0)] * p
    for _ in range(order + 1):
        sub = dict(zip(ys, ystar))
        res = [sp.series(sp.expand(g.subs(sub)), s, 0, order + 1).removeO() for g in grad]
        corr = H0inv * sp.Matrix(res)
        ystar = [sp.expand(ystar[a] - corr[a]) for a in range(p)]
        ystar = [sp.series(v, s, 0, order + 1).removeO() for v in ystar]
    sub = dict(zip(ys, ystar))
    R = sp.series(sp.expand(phi.subs(sub)), s, 0, order + 1).removeO()
    return sp.expand(R), ystar, s, H0
