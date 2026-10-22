"""[Эксперимент] Динамика модели U2 (model_U.py): c = (2,3), beta = 48, F = -a0 + Qt(b) + sigma*s*b1, s = x,
Qt = A*B + b1^24 (профиль предложения 6.2 [009]).

Масштабированные переменные (точные для U = x^beta F(x, b)): l = log x, b, X = xdot/x^{beta/2}, V_i = udot_i/x^{beta/2},
время tau: dt = x^{1-beta/2} dtau:
  dl/dtau = X,  db_i/dtau = x^{1-c_i} V_i - c_i b_i X,
  dX/dtau = -(beta F + s dF/ds - sum c_i b_i d_iF) - beta/2 X^2,  dV_i/dtau = -x^{1-c_i} d_iF - beta/2 X V_i.
Энергия: E/x^beta = (X^2+|V|^2)/2 + F (сохраняется; E = 0).
Функция Важевского поля Y = e_x + Z, Z_i = x^{c_i-1}(c_i b_i - xi_i(b)):
  calV := V/x^beta = (X^2+|V|^2)/2 - (X + Z.V)^2/(2h) + F + a0,  h = 1 + |Z|^2,
  нормированная производная  N := (rho/lam) Xi/(delta rho^beta) = [beta X (calV - delta) + d calV/dtau] / (delta (-(X+Z.V)/h)).

Часть A (sigma = 0): вдоль отрезков траекторий сравниваются поле с (T) (xi = Cb, поле d_x Phi) и поле nonT
(xi = (3/2 b1 - b2^2/2, b2/2), предложение 6.2(b) [009]): размах N_nonT растёт как 1/x, у поля с (T) — ограничен;
сами функции calV_nonT и calV_T почти совпадают (разность ~ x^{c1-1}).
Часть B (sigma = -1): «стрельба назад» по теореме A [007]: из точки дна b0(s_k) при x_k с v = -kappa*Y (v_perp = 0)
интегрируем назад до x = 0.1; печатаем конец и max calV/delta по пути. Режим доасимптотический (s*b1 не мало
по сравнению с delta) — это иллюстрация, не проверка теоремы.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

beta, a0, c1, c2 = 48.0, 1.0, 2.0, 3.0


def QG(b1, b2):
    s1 = b1 - b2**2
    s2 = b1 - b2**2 - b2**3
    A = s1**2 + b2**8
    B = s2**2 + b2**8
    dA1, dB1 = 2 * s1, 2 * s2
    dA2 = -4 * b2 * s1 + 8 * b2**7
    dB2 = 2 * s2 * (-2 * b2 - 3 * b2**2) + 8 * b2**7
    return A * B + b1**24, dA1 * B + A * dB1 + 24 * b1**23, dA2 * B + A * dB2


def make_rhs(sigma):
    def rhs(t, w):
        l, b1, b2, X, V1, V2 = w
        x = np.exp(l)
        Q, Q1, Q2 = QG(b1, b2)
        F = -a0 + Q + sigma * x * b1
        F1, F2 = Q1 + sigma * x, Q2
        sFs = sigma * x * b1
        return [X,
                x**(1 - c1) * V1 - c1 * b1 * X,
                x**(1 - c2) * V2 - c2 * b2 * X,
                -(beta * F + sFs - c1 * b1 * F1 - c2 * b2 * F2) - beta / 2 * X * X,
                -x**(1 - c1) * F1 - beta / 2 * X * V1,
                -x**(1 - c2) * F2 - beta / 2 * X * V2]
    return rhs


def calV(w, xi, sigma):
    l, b1, b2, X, V1, V2 = w
    x = np.exp(l)
    xi1, xi2 = xi(b1, b2)
    Z1 = x**(c1 - 1) * (c1 * b1 - xi1)
    Z2 = x**(c2 - 1) * (c2 * b2 - xi2)
    h = 1 + Z1 * Z1 + Z2 * Z2
    pp = X + Z1 * V1 + Z2 * V2
    F = -a0 + QG(b1, b2)[0] + sigma * x * b1
    return 0.5 * (X * X + V1 * V1 + V2 * V2) - pp * pp / (2 * h) + F + a0, pp / h


XI_T = lambda b1, b2: (c1 * b1, c2 * b2)                       # noqa: E731
XI_N = lambda b1, b2: (1.5 * b1 - 0.5 * b2 * b2, 0.5 * b2)      # noqa: E731


def initial(x0, b, Vt, sigma, xi):
    """E = 0, X < 0; поперечные скорости Vt."""
    F = -a0 + QG(*b)[0] + sigma * x0 * b[0]
    X2 = -2 * F - Vt[0]**2 - Vt[1]**2
    return [np.log(x0), b[0], b[1], -np.sqrt(X2), Vt[0], Vt[1]]


def partA():
    print('Часть A: sigma = 0, delta_ref = 1e-3; отрезок tau in [0, 0.05]')
    rng = np.random.default_rng(3)
    rhs = make_rhs(0.0)
    for x0 in (0.03, 0.01, 0.003, 0.001):
        res = []
        for trial in range(3):
            b = rng.normal(size=2) * np.array([0.05, 0.15])
            Vt = rng.normal(size=2) * 0.02
            w0 = initial(x0, b, Vt, 0.0, XI_T)
            sol = solve_ivp(rhs, (0, 0.05), w0, method='DOP853', rtol=1e-11, atol=1e-13, dense_output=True,
                            max_step=0.05 * x0**2)
            ts = np.linspace(0, 0.05, 200001)
            W = sol.sol(ts)
            out = {}
            for name, xi in (('T', XI_T), ('nonT', XI_N)):
                cV, ph = calV(W, xi, 0.0)
                d = np.gradient(cV, ts)
                dref = 1e-3
                N = (beta * W[3] * (cV - dref) + d) / (dref * (-ph))
                out[name] = (cV, N)
            diffV = np.max(np.abs(out['T'][0] - out['nonT'][0]))
            res.append((np.max(np.abs(out['T'][1])), np.max(np.abs(out['nonT'][1])), diffV,
                        np.ptp(out['nonT'][0]), np.mean(out['T'][0])))
        r = np.array(res)
        print(f'  x0={x0:6.3f}: max|N_T|={r[:, 0].max():9.3g}  max|N_nonT|={r[:, 1].max():11.4g}  '
              f'x0*max|N_nonT|={x0 * r[:, 1].max():8.3g}  max|calV_T-calV_nonT|={r[:, 2].max():.2e} '
              f'(calV_T~{r[:, 4].mean():.2e})')


def bottom(s):
    best = None
    for st in ([0.0, 0.0], [s**(1 / 6), s**(1 / 12)], [s**(1 / 6), -s**(1 / 12)], [0.2, 0.4], [0.2, -0.4]):
        r = minimize(lambda b: QG(*b)[0] - s * b[0], st, method='Nelder-Mead',
                     options={'xatol': 1e-13, 'fatol': 1e-20, 'maxiter': 20000})
        if best is None or r.fun < best.fun:
            best = r
    return best.x, best.fun


def partB():
    print('Часть B: sigma = -1, стрельба назад до x = 0.1 (поле Y = d_x Phi, xi = Cb)')
    rhs = make_rhs(-1.0)

    def hit(t, w):
        return w[0] - np.log(0.1)
    hit.terminal = True
    for xk in (0.03, 0.01, 0.005, 0.003):
        b0, fmin = bottom(xk)
        w0 = initial(xk, b0, (0.0, 0.0), -1.0, XI_T)
        # v_perp = 0 для поля Y: X и V пропорциональны Y = (1, Z1, Z2)
        Z1 = xk**(c1 - 1) * (c1 * b0[0] - c1 * b0[0]); Z2 = 0.0   # для xi = Cb: Z = 0
        sol = solve_ivp(rhs, (0, -50), w0, method='DOP853', rtol=1e-11, atol=1e-13, events=hit,
                        dense_output=True, max_step=0.05 * xk**2)
        ts = np.linspace(sol.t[-1], 0, 20001)
        W = sol.sol(ts)
        cV, ph = calV(W, XI_T, -1.0)
        we = sol.y[:, -1]
        print(f'  x_k={xk:6.3f}: bottom b0=({b0[0]:.4f},{b0[1]:.4f}), F_min+a0={fmin:.3e}; reached x=0.1 at tau={sol.t[-1]:.3f};'
              f' end b=({we[1]:.5f},{we[2]:.5f}), X={we[3]:.5f}, V=({we[4]:.2e},{we[5]:.2e}); '
              f'max calV over path = {cV.max():.3e}')


if __name__ == '__main__':
    partA()
    partB()
