"""Рецензент R21: проверка условия выхода (A5) прямым дифференцированием на модельном примере
с «поворачивающейся полярной картой» (перекрёстные члены, линейные по |b|).

[Эксперимент] Пример: q in R^2, полярные (r, phi), U = r^beta f(phi), f(phi) = -a0 + g(1-cos phi).
Карта Phi(x,u) = x(cos th, sin th), th = u x^{-kappa}; b = th (вес kappa), N = 1.
Поле Y(q) = omega(phi) - kappa*phi*T(phi), rho = |q|, h = 1 + kappa^2 phi^2, A(r) = a0 r^beta.
Здесь (Phi2') выполнено с gamma1 = kappa, gamma2 = kappa(1-kappa), C1 = kappa^3 r0 (берём kappa^2),
varpi = 0; (Phi3) с theta3 = 0 (x<w,D_wY> = <T,w>^2 (1-kappa+kappa^2 phi^2) >= 0).
Q = g(1-cos b) >= (g/4) b^2 при b^2<=6: lambda0 = g/4; Эйлер kappa*b*Q' >= kappa*Q: mu = kappa.

Xi = d/dt (V - delta rho^beta) считается прямым дифференцированием (без формулы (1.3)) на
множестве (A5): x = 1 (по однородности), Q(phi) <= delta, V = delta, E = 0, p < 0.
Сравнивается с нижней оценкой (7.1) леммы 2'.
Запуск: ~/venv/bin/python polar2d_exit.py
"""
import numpy as np
import sympy as sp

q1, q2, v1, v2 = sp.symbols('q1 q2 v1 v2', real=True)
beta, a0, g, kap, dl = sp.symbols('beta a0 g kappa delta', positive=True)
r = sp.sqrt(q1**2 + q2**2)
phi = sp.atan2(q2, q1)
om = sp.Matrix([q1 / r, q2 / r])
T = sp.Matrix([-q2 / r, q1 / r])
Y = om - kap * phi * T
h = (Y.T * Y)[0]
U = r**beta * (-a0 + g * (1 - sp.cos(phi)))
v = sp.Matrix([v1, v2])
p = (v.T * Y)[0]
V = (v.T * v)[0] / 2 - p**2 / (2 * h) + U + a0 * r**beta
Fn = V - dl * r**beta
gradU = sp.Matrix([sp.diff(U, q1), sp.diff(U, q2)])
Xi = (sp.diff(Fn, q1) * v1 + sp.diff(Fn, q2) * v2
      - sp.diff(Fn, v1) * gradU[0] - sp.diff(Fn, v2) * gradU[1])
Xi_f = sp.lambdify((q1, q2, v1, v2, beta, a0, g, kap, dl), Xi, 'numpy')


def min_exit(betav, a0v, gv, kv, dv, npts=801):
    """min по множеству (A5) (x=1) от (rho/lambda)Xi/delta и нижняя оценка (7.1)/delta."""
    lam0 = gv / 4
    # граница множества Q(phi) <= delta
    phimax = np.arccos(1 - dv / gv)
    best = np.inf
    for ph in np.linspace(-phimax, phimax, npts):
        Qv = gv * (1 - np.cos(ph))
        K = dv - Qv
        if K < 0:
            K = 0.0
        om_ = np.array([np.cos(ph), np.sin(ph)]); T_ = np.array([-np.sin(ph), np.cos(ph)])
        Yv = om_ - kv * ph * T_
        hv = Yv @ Yv
        lam = np.sqrt(2 * (a0v - dv) / hv)
        nY = np.array([-Yv[1], Yv[0]]) / np.sqrt(hv)
        for sgn in (+1, -1):
            vv = -lam * Yv + sgn * np.sqrt(2 * K) * nY
            # контроль: E = 0, V = delta
            E = 0.5 * vv @ vv + (-a0v + gv * (1 - np.cos(ph)))
            assert abs(E) < 1e-10, E
            x = Xi_f(om_[0], om_[1], vv[0], vv[1], betav, a0v, gv, kv, dv)
            best = min(best, x / lam / dv)        # rho = 1
    # нижняя оценка (7.1): eps0 = eps1 = 0, theta1 = 0, theta2 = C1 Rb^2, theta3 = 0
    Rb = 2 * np.sqrt(dv / lam0)
    C1 = kv**2
    c2 = 4 * np.sqrt(a0v)
    bound = kv / 2 - c2 * C1 * Rb**2 / np.sqrt(dv)
    Gstar = np.sqrt(a0v / lam0) * (1.5 * np.sqrt(3) * betav * kv + 2 * np.sqrt(2) * kv * (1 - kv))
    return best, bound, Gstar**2 <= betav * kv


if __name__ == "__main__":
    print("beta a0  g   kappa   delta    min(rho/lam)Xi/delta  оценка(7.1)/delta  (7.2)?")
    for (b_, a_, g_) in [(6, 1.0, 1.0), (6, 1.0, 0.2), (4, 1.0, 0.05), (10, 1.0, 1.0)]:
        lam0 = g_ / 4
        kmax = b_ * lam0 / (a_ * (1.5 * np.sqrt(3) * b_ + 2 * np.sqrt(2))**2)
        for k_ in [kmax, 0.05, 0.2, 0.5, 1.0, 2.0]:
            for d_ in [1e-3, 1e-5]:
                m, bd, ok72 = min_exit(b_, a_, g_, k_, d_)
                flag = "" if (not ok72 or m >= bd - 1e-12) else "  <-- НАРУШЕНИЕ (7.1)"
                print(f"{b_:4d} {a_:3.1f} {g_:4.2f} {k_:8.5f} {d_:8.0e}   {m:14.6e}      {bd:14.6e}   {ok72}{flag}")
