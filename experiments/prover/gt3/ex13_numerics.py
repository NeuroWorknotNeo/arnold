"""[Эксперимент] Численная проверка для примера 13 (раздел 4 и 6 заметки
notes/prover/2026-10-21-gt3.md).

U = (x^2+y^2-z^2)^2 + z^5 x + z^4 x y + z^6/2,  ẍ = -grad U.
Карта развёртки конуса: (X, Y, eta) -> q, rho(q) = X, поле Y = d_X Phi.
Поперечная энергия V = A(rho) - pi^2/(2h), pi = <v, Y>, h = |Y|^2.

Часть 1. Проверка формулы для Xi = d/dt (V - delta rho^6) (лемма 1 + (3.2)) против
         численной производной вдоль потока.
Часть 2. Знак Xi на выборке точек границы множества Omega для нескольких (delta, sigma).
Часть 3. «Стрельба назад» (схема доказательства теоремы A): из точек дна при X0 -> 0
         назад по времени до X = sigma2; сходимость точек входа; прямой прогон из предела.
Числа — двойная точность; это эксперимент, а не доказательство.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

phi0 = 5 * np.pi / 6
SQ2 = np.sqrt(2.0)
BETA = 6


def U(q):
    x, y, z = q
    return (x * x + y * y - z * z) ** 2 + z ** 5 * x + z ** 4 * x * y + 0.5 * z ** 6


def gradU(q):
    x, y, z = q
    Q = x * x + y * y - z * z
    return np.array([
        4 * x * Q + z ** 5 + z ** 4 * y,
        4 * y * Q + z ** 4 * x,
        -4 * z * Q + 5 * z ** 4 * x + 4 * z ** 3 * x * y + 3 * z ** 5,
    ])


def frame(theta):
    ph = phi0 + SQ2 * theta
    N = np.array([np.cos(ph), np.sin(ph), 1.0]) / SQ2
    nu = np.array([np.cos(ph), np.sin(ph), -1.0]) / SQ2
    tau = np.array([-np.sin(ph), np.cos(ph), 0.0])
    return N, nu, tau


def Phi(X, Yc, eta):
    s = np.hypot(X, Yc)
    th = np.arctan2(Yc, X)
    N, nu, tau = frame(th)
    return s * N + eta * nu


def coords(q):
    """Обратная карта: q -> (X, Yc, eta)."""
    x, y, z = q
    R = np.hypot(x, y)
    ph = np.arctan2(y, x)
    th = (np.mod(ph - phi0 + np.pi, 2 * np.pi) - np.pi) / SQ2
    s = (R + z) / SQ2
    eta = (R - z) / SQ2
    return s * np.cos(th), s * np.sin(th), eta


def Yfield(q):
    X, Yc, eta = coords(q)
    s = np.hypot(X, Yc)
    th = np.arctan2(Yc, X)
    N, nu, tau = frame(th)
    return np.cos(th) * N - (1 + eta / s) * np.sin(th) * tau


def F(Xs, t, e):
    """U(Phi(X, tX, eX^2)) / X^6, явная формула."""
    S = np.sqrt(1 + t * t)
    lam = (S + Xs * e) / (S - Xs * e)
    ph = phi0 + SQ2 * np.arctan(t)
    G = lam * np.cos(ph) + lam ** 2 * np.cos(ph) * np.sin(ph) + 0.5
    return 4 * (1 + t * t) * e * e + (S - Xs * e) ** 6 / 8 * G


_bstar_cache = {}


def bstar(Xs):
    key = round(Xs, 14)
    if key in _bstar_cache:
        return _bstar_cache[key]
    res = minimize(lambda b: F(Xs, b[0], b[1]), np.zeros(2), method='BFGS',
                   options={'gtol': 1e-14})
    _bstar_cache[key] = res.x
    return res.x


A0 = -(0.5 - 3 * np.sqrt(3) / 4) / 8  # a0 = -F0(0) = -G(phi0)/8


def A(Xs):
    """A(rho) = a0 rho^6 (выбор из доказательства теоремы 2)."""
    return A0 * Xs ** 6


def V(q, v):
    X = coords(q)[0]
    Yv = Yfield(q)
    h = Yv @ Yv
    pi = v @ Yv
    return A(X) - pi * pi / (2 * h)


def rhs(t, w):
    return np.concatenate([w[3:], -gradU(w[:3])])


# ---------------- Часть 1 и 2: знак Xi на границе ----------------

def num_deriv_Xi(q, v, delta, dt=1e-3):
    """d/dt (V - delta*rho^6) численно (центральная разность по двум интегрированиям)."""
    def G(w):
        qq, vv = w[:3], w[3:]
        return V(qq, vv) - delta * coords(qq)[0] ** BETA
    w0 = np.concatenate([q, v])
    sp_ = solve_ivp(rhs, [0, dt], w0, method='DOP853', rtol=1e-13, atol=1e-16)
    sm_ = solve_ivp(rhs, [0, -dt], w0, method='DOP853', rtol=1e-13, atol=1e-16)
    return (G(sp_.y[:, -1]) - G(sm_.y[:, -1])) / (2 * dt)


def boundary_point(X, xi, ang, delta, rng):
    """Точка (q,v) с rho = X, b = b*(X) + xi, V = delta X^6, pi<0, E = 0.
    Возвращает None, если W > delta X^6."""
    b = bstar(X) + xi
    t, e = b
    q = Phi(X, t * X, e * X * X)
    W = U(q) + A(X)
    K = delta * X ** BETA - W
    if K < 0:
        return None
    Yv = Yfield(q)
    h = Yv @ Yv
    # базис в Y^perp
    Yh = Yv / np.sqrt(h)
    a1 = np.cross(Yh, [0.0, 0.0, 1.0]); a1 /= np.linalg.norm(a1)
    a2 = np.cross(Yh, a1)
    vperp = np.sqrt(2 * K) * (np.cos(ang) * a1 + np.sin(ang) * a2)
    pi = -np.sqrt(2 * h * (A(X) - delta * X ** BETA))
    v = (pi / h) * Yv + vperp
    return q, v


def check_boundary(delta, sigma, nX=6, nxi=24, nang=8, seed=0):
    rng = np.random.default_rng(seed)
    worst = np.inf
    count = 0
    H = np.array([(6 - 3 * np.sqrt(3)) / 16, 8.0])
    for X in np.linspace(sigma / nX, sigma, nX):
        for k in range(nxi):
            # xi на эллипсе уровня ~ delta (и внутри)
            r = np.sqrt(rng.uniform(0, 1))
            al = rng.uniform(0, 2 * np.pi)
            xi = r * np.array([np.cos(al) * np.sqrt(2 * delta / H[0]), np.sin(al) * np.sqrt(2 * delta / H[1])])
            for j in range(nang):
                bp = boundary_point(X, xi, 2 * np.pi * j / nang, delta, rng)
                if bp is None:
                    continue
                q, v = bp
                Xi = num_deriv_Xi(q, v, delta, dt=1e-4 / X ** 2)
                # нормировка: (rho/lambda) Xi / (delta rho^6)
                lam = np.sqrt(2 * (A(X) - delta * X ** 6) / (Yfield(q) @ Yfield(q)))
                val = X / lam * Xi / (delta * X ** 6)
                worst = min(worst, val)
                count += 1
    return worst, count


def xi_formula(q, v, delta):
    """Xi по формуле (3.2) заметки: rho/lambda * Xi = [beta delta rho^b - rho YW] + T1 + T2 + T3."""
    Xc, Yc, et = coords(q)
    s = np.hypot(Xc, Yc); th = np.arctan2(Yc, Xc)
    N, nu, tau = frame(th)
    c, sn = np.cos(th), np.sin(th)
    Yv = c * N - (1 + et / s) * sn * tau
    h = Yv @ Yv
    pi = v @ Yv
    lam = -pi / h
    vperp = v - (pi / h) * Yv
    # grad rho численно
    eps = 1e-7
    grho = np.array([(coords(q + eps * ei)[0] - coords(q - eps * ei)[0]) / (2 * eps) for ei in np.eye(3)])
    # Y W = d/dX W(Phi(X,Y,eta)) при фиксированных (Y, eta)
    Wf = lambda Xv: U(Phi(Xv, Yc, et)) + A(Xv)
    dX = 1e-6 * Xc
    YW = (Wf(Xc + dX) - Wf(Xc - dX)) / (2 * dX)
    Ap = 6 * A0 * Xc ** 5
    dXX = -(et * sn ** 2 / s ** 2) * N - (1 + et / s) * (sn ** 2 / s) * nu + (2 * et * sn * c / s ** 2) * tau
    dXY = (et * sn * c / s ** 2) * N + (1 + et / s) * (sn * c / s) * nu + (et * (sn ** 2 - c ** 2) / s ** 2) * tau
    dXe = -(sn / s) * tau
    Jm = np.column_stack([Yv, sn * N + (1 + et / s) * c * tau, nu])
    zeta = np.linalg.solve(Jm, vperp)
    DYv = zeta[0] * dXX + zeta[1] * dXY + zeta[2] * dXe
    rho = Xc
    main = 6 * delta * rho ** 6 - rho * YW
    T1 = rho / lam * (Ap - 6 * delta * rho ** 5) * (grho @ vperp)
    T2 = -lam * rho * (vperp @ dXX)
    T3 = rho * (vperp @ DYv)
    return lam / rho * (main + T1 + T2 + T3), (main, T1, T2, T3)


def boundary_scan(delta, sigma, nX=5, nxi=16, nang=8):
    """xi на эллипсе {Q2(xi) = r^2 delta} для r in {0, 0.5, 0.8, 1, 1.05}; все углы v_perp."""
    worst = np.inf
    count = 0
    H = np.array([(6 - 3 * np.sqrt(3)) / 16, 8.0])
    for X in np.linspace(sigma / nX, sigma, nX):
        for r in [0.0, 0.5, 0.8, 0.9, 0.95, 0.98, 0.995, 1.0, 1.05]:
            for k in range(nxi if r > 0 else 1):
                al = 2 * np.pi * k / nxi
                xi = r * np.array([np.cos(al) * np.sqrt(2 * delta / H[0]), np.sin(al) * np.sqrt(2 * delta / H[1])])
                for j in range(nang):
                    bp = boundary_point(X, xi, 2 * np.pi * j / nang, delta, None)
                    if bp is None:
                        continue
                    q, v = bp
                    Xi = num_deriv_Xi(q, v, delta, dt=1e-4 / X ** 2)
                    lam = np.sqrt(2 * (A(X) - delta * X ** 6) / (Yfield(q) @ Yfield(q)))
                    worst = min(worst, X / lam * Xi / (delta * X ** 6))
                    count += 1
    return worst, count


def bottom_state(X0):
    b = bstar(X0)
    q = Phi(X0, b[0] * X0, b[1] * X0 ** 2)
    Yv = Yfield(q)
    speed = np.sqrt(-2 * U(q))
    v = -speed * Yv / np.linalg.norm(Yv)
    return np.concatenate([q, v])


def ev_sigma(sig):
    f = lambda t, w: coords(w[:3])[0] - sig
    f.terminal = True
    return f


def chart_state(w):
    Xc, Yc, et = coords(w[:3])
    return np.array([Xc, Yc / Xc, et / Xc ** 2])


if __name__ == '__main__':
    print('a0 = -G(phi0)/8 =', A0)
    for Xs in [0.2, 0.1, 0.05, 0.02]:
        b = bstar(Xs)
        print(f'X={Xs}: b*(X) = {b},  t*/X^2 = {b[0] / Xs ** 2:.5f}, e*/X = {b[1] / Xs:.5f}')

    print('\nЧасть 1: формула (3.2) против численной производной')
    for (X, xi, ang, dl) in [(0.1, np.array([0.3, 0.02]), 0.7, 0.02), (0.05, np.array([-0.5, 0.03]), 2.0, 0.02),
                             (0.2, np.array([0.1, -0.05]), 4.0, 0.04)]:
        q, v = boundary_point(X, xi, ang, dl, None) or (None, None)
        if q is None:
            print('  (point outside)'); continue
        xf, parts = xi_formula(q, v, dl)
        xn = num_deriv_Xi(q, v, dl, dt=1e-4 / X ** 2)
        print(f'  X={X}: Xi formula = {xf:.6e}, numeric = {xn:.6e}, rel.diff = {abs(xf - xn) / abs(xn):.1e};'
              f' parts/(delta rho^6) = {[f"{p / (dl * X ** 6):.3f}" for p in parts]}')
    print('Часть 2: min по выборке точек границы Omega величины (rho/lambda) Xi / (delta rho^6)')
    for delta, sigma in [(0.04, 0.3), (0.02, 0.2), (0.01, 0.1), (0.005, 0.05)]:
        w, c = boundary_scan(delta, sigma)
        print(f'  delta={delta:6.3f} sigma={sigma:5.2f}: min = {w:8.4f}  ({c} points)')

    print('\nЧасть 3: стрельба назад до X = 0.2 из точек дна при X0')
    sig2 = 0.2
    pts = []
    for X0 in [0.08, 0.04, 0.02, 0.01, 0.005]:
        w0 = bottom_state(X0)
        sol = solve_ivp(rhs, [0, -1e7], w0, method='DOP853', rtol=1e-11, atol=1e-15,
                        events=ev_sigma(sig2))
        wk = sol.y_events[0][0]
        Tk = -sol.t_events[0][0]
        cs = chart_state(wk)
        Vr = V(wk[:3], wk[3:]) / sig2 ** 6
        print(f'  X0={X0:6.3f}: T={Tk:10.1f}  entry (X,t,e)=({cs[0]:.4f},{cs[1]: .3e},{cs[2]: .3e})'
              f'  v={wk[3:]}  V/X^6={Vr:.2e}')
        pts.append(wk)
    pts = np.array(pts)
    print('  |q_k - q_last| :', [f'{np.linalg.norm(p - pts[-1]):.2e}' for p in pts[:-1]])

    print('\nПрямой прогон из предельной точки (X0=0.005): X(t), V/X^6, (t,e)')
    w = pts[-1]
    times = np.linspace(0, 2e5, 41)
    sol = solve_ivp(rhs, [0, times[-1]], w, method='DOP853', rtol=1e-12, atol=1e-16, t_eval=times)
    a0 = A0
    for i in range(0, sol.y.shape[1], 4):
        wi = sol.y[:, i]
        cs = chart_state(wi)
        Vr = V(wi[:3], wi[3:]) / cs[0] ** 6
        pred = (sig2 ** -2 + 2 * np.sqrt(2 * a0) * sol.t[i]) ** -0.5
        print(f'  t={sol.t[i]:9.0f}  X={cs[0]:.5f} (pred {pred:.5f})  V/X^6={Vr: .2e}  t={cs[1]: .2e} e={cs[2]: .2e}')
