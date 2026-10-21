# [Эксперимент] Редуцированная функция U_red и эффективный потенциал G = g_j
# (определение 1.2 записки notes/prover/2026-10-21-gt3-hardcore.md).
# phi(s,y) = s^{-m} U(s(omega + sum y_i e_i)); y*(s) — критическая точка по y (ряд по s);
# R(s) = phi(s, y*(s)) = sum_{k>m} s^{k-m} g_k.
import sympy as sp

x, y, z = sp.symbols('x y z', real=True)
s = sp.symbols('s', real=True)

def fiber_series(U, m, omega, frame, order):
    """U — многочлен от x,y,z; omega — вектор (выражения); frame — список векторов
    ортонормированного базиса N_omega. Возвращает (ys, R): ряды y*(s) и R(s) до s^order."""
    p = len(frame)
    Y = sp.symbols('Y0:%d' % p)
    pt = [s*(omega[i] + sum(Y[a]*frame[a][i] for a in range(p))) for i in range(3)]
    P = sp.expand(U.subs({x: pt[0], y: pt[1], z: pt[2]}, simultaneous=True))
    P = sp.expand(sp.simplify(P / s**m)) if False else sp.expand(P * s**(-m))
    # коэффициенты y* = sum_{i>=1} a_i s^i
    A = [[sp.Symbol('a%d_%d' % (a, i)) for i in range(1, order + 1)] for a in range(p)]
    ysub = {Y[a]: sum(A[a][i - 1]*s**i for i in range(1, order + 1)) for a in range(p)}
    grad = [sp.diff(P, Y[a]) for a in range(p)]
    sol = {}
    for i in range(1, order + 1):
        eqs = []
        for a in range(p):
            g = sp.expand(grad[a].subs(ysub).subs(sol))
            eqs.append(sp.expand(g).coeff(s, i))
        unk = [A[a][i - 1] for a in range(p)]
        si = sp.solve(eqs, unk, dict=True)
        assert len(si) == 1, (i, eqs)
        sol.update({k: sp.simplify(v) for k, v in si[0].items()})
    ys = [sp.expand(ysub[Y[a]].subs(sol)) for a in range(p)]
    R = sp.expand(P.subs({Y[a]: ys[a] for a in range(p)}))
    R = sum(sp.simplify(R.coeff(s, i))*s**i for i in range(0, order + 1))
    return ys, R

if __name__ == '__main__':
    # проверка на тривиальном примере: U = (x^2+y^2-z^2)^2 + x z^4 на верхней окружности
    ph = sp.symbols('phi', real=True)
    om = [sp.cos(ph)/sp.sqrt(2), sp.sin(ph)/sp.sqrt(2), 1/sp.sqrt(2)]
    nn = [-sp.cos(ph)/sp.sqrt(2), -sp.sin(ph)/sp.sqrt(2), 1/sp.sqrt(2)]
    U = (x**2 + y**2 - z**2)**2 + x*z**4
    ys, R = fiber_series(U, 4, om, [nn], 3)
    print('y* =', ys)
    print('R  =', R)
