"""[Эксперимент] Динамика модели U2 (model_U.py): c = (2,3), beta = 48, F = -a0 + Qt(b) + sigma*s*b1, s = x,
Qt = A*B + b1^24 (профиль предложения 6.2 [009]); b1 = y/x^2 — широкая, b2 = z/x^3 — узкая.

Масштабированные переменные (точные для U = x^beta F(x, b)): l = log x, b, X = xdot/x^{beta/2},
V_i = udot_i/x^{beta/2}, время tau: dt = x^{1-beta/2} dtau:
  dl/dtau = X,  db_i/dtau = x^{1-c_i} V_i - c_i b_i X,
  dX/dtau = -(beta F + s dF/ds - sum c_i b_i d_iF) - beta/2 X^2,  dV_i/dtau = -x^{1-c_i} d_iF - beta/2 X V_i.
Энергия E/x^beta = (X^2+|V|^2)/2 + F (= 0). Функция Важевского поля Y = e_x + Z, Z_i = x^{c_i-1}(c_i b_i - xi_i(b)):
  calV := V/x^beta = (X^2+|V|^2)/2 - (X + Z.V)^2/(2h) + F + a0,  h = 1 + |Z|^2,
  N := (rho/lam) Xi/(delta rho^beta) = [beta X (calV - delta) + d calV/dtau] / (delta (-(X+Z.V)/h)).

Часть A (sigma = 0): вдоль отрезков истинных траекторий сравниваются три поля: T0: xi = Cb (Y = e_x),
TB: полосовое (T)-поле xi = t(b1, Lam d2Qt) (band_T.py, delta = 1e-4, t — масштаб (Theta)), nonT: xi = (3/2 b1 - b2^2/2, b2/2)
(предложение 6.2(b) [009], нарушает (T)). Печатаются max|N| (поточечно) и среднее N по отрезку, а также
max|calV_T0 - calV_nonT|: функции почти совпадают, а производные nonT имеют быстро осциллирующую часть ~ 1/x.
Часть B (sigma = -1): «стрельба назад» (шаг 3 теоремы A [007]): из точки дна b0(x_k) с v = -kappa Y (Y = e_x, V = 0)
интегрируем назад до x = sigma2; печатаем конечное состояние (сходимость при x_k -> 0) и вдоль траектории от
наименьшего x_k — b, дно b0(x), calV (относительная энергия), узкую и широкую кинетические энергии V_i^2/2 и
размах колебаний b2 и b1 в окнах по l.
"""
import sys
import time
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


LAM_B, T_B = 1.5 * 3.3180e2, 1.0 / 162.0      # band_T.out (Q62 = Qt2 numerically), delta = 1e-4; t = 1/M1
XI_T0 = lambda b1, b2: (c1 * b1, c2 * b2)                                    # noqa: E731
XI_TB = lambda b1, b2: (T_B * b1, T_B * LAM_B * QG(b1, b2)[2])               # noqa: E731
XI_N = lambda b1, b2: (1.5 * b1 - 0.5 * b2 * b2, 0.5 * b2)                    # noqa: E731


def initial(x0, b, Vt, sigma):
    F = -a0 + QG(*b)[0] + sigma * x0 * b[0]
    X2 = -2 * F - Vt[0]**2 - Vt[1]**2
    return [np.log(x0), b[0], b[1], -np.sqrt(X2), Vt[0], Vt[1]]


def partA():
    print('Part A: sigma = 0, delta_ref = 1e-4; segments tau in [0, T], T = 0.02; 3 random starts per x0')
    rng = np.random.default_rng(3)
    rhs = make_rhs(0.0)
    dref = 1e-4
    for x0 in (0.03, 0.01, 0.003, 0.001):
        res = []
        for trial in range(3):
            b = rng.normal(size=2) * np.array([0.02, 0.08])
            Vt = rng.normal(size=2) * 0.005
            w0 = initial(x0, b, Vt, 0.0)
            T = 0.02
            sol = solve_ivp(rhs, (0, T), w0, method='DOP853', rtol=1e-11, atol=1e-13, dense_output=True)
            ts = np.linspace(0, T, 400001)
            W = sol.sol(ts)
            row = []
            Vs = {}
            for name, xi in (('T0', XI_T0), ('TB', XI_TB), ('nonT', XI_N)):
                cV, ph = calV(W, xi, 0.0)
                d = np.gradient(cV, ts)
                N = (beta * W[3] * (cV - dref) + d) / (dref * (-ph))
                row += [np.max(np.abs(N)), np.mean(N)]
                Vs[name] = cV
            row += [np.max(np.abs(Vs['T0'] - Vs['nonT'])), np.mean(Vs['T0'])]
            res.append(row)
        r = np.array(res)
        print(f'  x0={x0:6.3f}: max|N_T0|={r[:, 0].max():9.3g} (mean {r[:, 1].mean():9.3g}); '
              f'max|N_TB|={r[:, 2].max():9.3g} (mean {r[:, 3].mean():9.3g}); '
              f'max|N_nonT|={r[:, 4].max():10.4g} (mean {r[:, 5].mean():9.3g}); x0*max|N_nonT|={x0 * r[:, 4].max():8.3g}; '
              f'max|calV_T0-calV_nonT|={r[:, 6].max():.2e} (calV~{r[:, 7].mean():.2e})', flush=True)


def bottom(s, sigma):
    best = None
    for st in ([0.0, 0.0], [0.3, 0.55], [0.3, -0.55], [0.2, 0.45], [0.2, -0.45], [0.1, 0.3], [0.1, -0.3]):
        r = minimize(lambda b: QG(*b)[0] + sigma * s * b[0], st, method='Nelder-Mead',
                     options={'xatol': 1e-14, 'fatol': 1e-22, 'maxiter': 40000})
        if best is None or r.fun < best.fun:
            best = r
    return best.x, best.fun


def partB(sigma2=0.05, xks=(0.03, 0.02, 0.01, 0.006, 0.004, 0.003)):
    sigma = -1.0
    print(f'Part B: sigma = {sigma}, backward shooting from the bottom with V = 0 up to x = {sigma2}')
    rhs = make_rhs(sigma)

    def hit(t, w):
        return w[0] - np.log(sigma2)
    hit.terminal = True
    ends = []
    sols = {}
    for xk in xks:
        t0 = time.time()
        b0, fmin = bottom(xk, sigma)
        w0 = initial(xk, b0, (0.0, 0.0), sigma)
        sol = solve_ivp(rhs, (0, -100), w0, method='DOP853', rtol=1e-11, atol=1e-14, events=hit, dense_output=True)
        we = sol.y[:, -1]
        cV, _ = calV(we, XI_T0, sigma)
        ends.append(we)
        sols[xk] = sol
        print(f'  x_k={xk:6.4f}: bottom b0=({b0[0]:.5f},{b0[1]:.5f}), W_min/x^b={fmin:.3e}; reached x={sigma2} at '
              f'tau={sol.t[-1]:.4f} (nfev={sol.nfev}, {time.time() - t0:.0f}s); end b=({we[1]:.7f},{we[2]:.7f}), '
              f'X={we[3]:.7f}, V=({we[4]:.3e},{we[5]:.3e}), calV={cV:.4e}', flush=True)
    E = np.array(ends)
    for i in range(1, len(E)):
        print(f'   |end(x_k={xks[i]}) - end(x_k={xks[i - 1]})| = {np.max(np.abs(E[i, 1:] - E[i - 1, 1:])):.3e}')
    # профиль вдоль траектории от наименьшего x_k
    sol = sols[xks[-1]]
    print(f'  along the trajectory from x_k={xks[-1]} (forward direction: x decreasing):')
    ls = np.linspace(np.log(sigma2), np.log(xks[-1]), 9)
    tgrid = np.linspace(sol.t[-1], 0, 400001)
    Wd = sol.sol(tgrid)
    print('   pointwise: excess of the relative energy over the bottom, calV - W_min(x) >= 0, and distance to the bottom')
    for lt in np.linspace(np.log(sigma2), np.log(xks[-1]) + 0.05, 10):
        j = np.argmin(np.abs(Wd[0] - lt))
        xx = np.exp(Wd[0, j])
        b0, fmin = bottom(xx, sigma)
        cV, _ = calV(Wd[:, j], XI_T0, sigma)
        print(f'     x={xx:.5f}: b=({Wd[1, j]:.5f},{Wd[2, j]:.5f}), b0(x)=({b0[0]:.5f},{b0[1]:.5f}), |b-b0|={np.hypot(*(Wd[1:3, j] - b0)):.4f}, '
              f'calV-W_min={cV - fmin:.3e}, |W_min|={-fmin:.3e}, V=({Wd[4, j]:.2e},{Wd[5, j]:.2e})', flush=True)
    for a, bnd in zip(ls[:-1], ls[1:]):
        m = (Wd[0] <= a) & (Wd[0] >= bnd)
        seg = Wd[:, m]
        xm = np.exp(0.5 * (a + bnd))
        b0, fmin = bottom(xm, sigma)
        cV, _ = calV(seg, XI_T0, sigma)
        print(f'   x in [{np.exp(bnd):.4f},{np.exp(a):.4f}]: b1 in [{seg[1].min():.5f},{seg[1].max():.5f}], '
              f'b2 in [{seg[2].min():.5f},{seg[2].max():.5f}]; bottom at x={xm:.4f}: ({b0[0]:.5f},{b0[1]:.5f}); '
              f'calV in [{cV.min():.3e},{cV.max():.3e}] (W_min={fmin:.3e}); max V1^2/2={0.5 * (seg[4]**2).max():.2e}, '
              f'max V2^2/2={0.5 * (seg[5]**2).max():.2e}', flush=True)


if __name__ == '__main__':
    which = sys.argv[1:] or ['A', 'B']
    if 'A' in which:
        partA()
    if 'B' in which:
        partB()


def partC(xk=0.002, x_starts=(0.05, 0.01), dv_size=1e-13, x_stop=0.0025, dmax=1e-6):
    """Неустойчивость «свободных» поперечных колебаний: к опорной траектории (стрельба назад из x_k до x = 0.05)
    в точке x_p добавляется возмущение скорости dV (узкое или широкое) размера dv_size, и возмущённое решение
    интегрируется вперёд до x_stop или до выхода из линейного режима (|D| > dmax). Сравнение с опорным решением
    по одному tau. Относительная энергия возмущения e_i := dV_i^2/2 + |d_iiQ| db_i^2/2, огибающая по окнам l.
    Адиабатический прогноз (частота x^{1-c_i} sqrt(d_ii Q) >> beta|X|/2): e_i ~ x^{-(beta/2 + c_i)} = x^{-27} (узкое),
    x^{-26} (широкое); без усреднения (низкая частота) — до x^{-(beta+...)}."""
    sigma = -1.0
    rhs = make_rhs(sigma)

    def hit(t, w):
        return w[0] - np.log(0.05)
    hit.terminal = True
    b0, _ = bottom(xk, sigma)
    ref = solve_ivp(rhs, (0, -100), initial(xk, b0, (0.0, 0.0), sigma), method='DOP853', rtol=1e-12, atol=1e-15,
                    events=hit, dense_output=True)
    print(f'Part C: reference = backward shot from x_k={xk} to x=0.05 (nfev={ref.nfev}); perturbation size {dv_size}')
    for xp in x_starts:
        tp = ref.t[-1] + (np.log(0.05) - np.log(xp)) / 1.42           # приближённо; уточняем по l
        tt = np.linspace(ref.t[-1], 0, 200001)
        lr = ref.sol(tt)[0]
        tp = tt[np.argmin(np.abs(lr - np.log(xp)))]
        w0 = ref.sol(tp)
        for label, dv in (('narrow dV2', (0.0, dv_size)), ('wide dV1', (dv_size, 0.0))):
            w1 = w0.copy(); w1[4] += dv[0]; w1[5] += dv[1]

            def stop(t, w):
                return w[0] - np.log(x_stop)
            stop.terminal = True
            sol = solve_ivp(rhs, (tp, 0), w1, method='DOP853', rtol=1e-13, atol=1e-22, events=stop, dense_output=True)
            ts = np.linspace(tp, sol.t[-1], 400001)
            A_, R_ = sol.sol(ts), ref.sol(ts)
            D = A_ - R_
            lin = np.cumprod(np.max(np.abs(D), axis=0) < dmax).astype(bool)       # линейный режим до первого выхода
            hstep = 1e-6
            Q11 = (QG(R_[1] + hstep, R_[2])[1] - QG(R_[1] - hstep, R_[2])[1]) / (2 * hstep)
            Q22 = (QG(R_[1], R_[2] + hstep)[2] - QG(R_[1], R_[2] - hstep)[2]) / (2 * hstep)
            e1 = 0.5 * D[4]**2 + 0.5 * np.abs(Q11) * D[1]**2
            e2 = 0.5 * D[5]**2 + 0.5 * np.abs(Q22) * D[2]**2
            lmin = A_[0][lin].min()
            ls = np.linspace(np.log(xp), lmin, 9)
            rows = []
            for a, bnd in zip(ls[:-1], ls[1:]):
                m = lin & (A_[0] <= a) & (A_[0] >= bnd)
                if m.sum() < 10:
                    continue
                xm = np.exp(0.5 * (a + bnd))
                om1 = xm**(1 - c1) * np.sqrt(np.abs(Q11[m]).mean()); om2 = xm**(1 - c2) * np.sqrt(np.abs(Q22[m]).mean())
                rows.append((xm, e1[m].max(), e2[m].max(), om1, om2))
            R = np.array(rows)
            p1 = np.polyfit(np.log(R[:, 0]), np.log(R[:, 1]), 1)[0]
            p2 = np.polyfit(np.log(R[:, 0]), np.log(R[:, 2]), 1)[0]
            print(f'  start x_p={xp}, {label}: linear regime down to x={np.exp(lmin):.4f}; envelopes e1 (wide) ~ x^{p1:.1f}, '
                  f'e2 (narrow) ~ x^{p2:.1f}; scaled frequencies omega_1 in [{R[:, 3].min():.1f},{R[:, 3].max():.1f}], '
                  f'omega_2 in [{R[:, 4].min():.0f},{R[:, 4].max():.0f}] (compare beta|X|/2 ~ 34)', flush=True)
            for xm, a1, a2, o1, o2 in R:
                print(f'     x={xm:.5f}: e1={a1:.3e}, e2={a2:.3e}, omega1={o1:.2f}, omega2={o2:.1f}')


if __name__ == '__main__' and 'C' in sys.argv[1:]:
    partC()
