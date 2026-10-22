"""[Эксперимент] Теорема T (полосовое (T)-поле) для профиля Q = A*B предложения 6.2 [009].

b_1 — широкая координата (вес c_1), b_2 — узкая (c_2 > c_1). Поле с условием (T):
    xi = (kappa*b1, Lam * d_2 Q(b)),   kappa = 1.
Требуется (полосовое неравенство Эйлера, (U4) теоремы 2U [012] при eps_E = mu*delta/8):
    xi . grad Q >= mu (Q - eps_b*delta)  на K = {|b| <= r1, Q <= 2 delta},  eps_b = 1/8.
Константы — как в доказательстве теоремы T: m = min b1 d1Q по полярным точкам K c Q >= eps'*delta
(eps' = 1/16), mu = kappa*m/(4 delta); Lam — минимальное значение, при котором неравенство верно на
плотной выборке K (по каждому b2 множество {Q <= 2 delta} находится корнями многочлена по b1).
Затем неравенство проверяется на независимой более плотной выборке с Lam_used = 1.2*Lam_needed.
Для сравнения: неравномерность по delta (рост Lam) согласуется с предложением 6.2(a) [009]: равномерного
(T)-поля с xi Q >= mu Q нет.
"""
import numpy as np

r1 = 0.5
EPS_B, EPS1, KAPPA = 1 / 8, 1 / 16, 1.0


def Q_and_grad(b1, b2):
    s1 = b1 - b2**2
    s2 = b1 - b2**2 - b2**3
    A = s1**2 + b2**8
    B = s2**2 + b2**8
    dA1, dB1 = 2 * s1, 2 * s2
    dA2 = 2 * s1 * (-2 * b2) + 8 * b2**7
    dB2 = 2 * s2 * (-2 * b2 - 3 * b2**2) + 8 * b2**7
    return A * B, dA1 * B + A * dB1, dA2 * B + A * dB2


def poly_b1(b2):
    """Коэффициенты Q(., b2) как многочлена 4-й степени по b1 (старший первый)."""
    p1 = np.array([1.0, -2 * b2**2, b2**4 + b2**8])           # A
    c = b2**2 + b2**3
    p2 = np.array([1.0, -2 * c, c * c + b2**8])               # B
    return np.polymul(p1, p2)


def sample_K(delta, nb2, nb1, rng=None):
    b2s = np.concatenate([np.linspace(-r1, r1, nb2),
                          np.sign(np.linspace(-1, 1, 400)) * np.logspace(-6, np.log10(r1), 400)])
    out1, out2 = [], []
    for b2 in b2s:
        p = poly_b1(b2).copy()
        p[-1] -= 2 * delta
        rts = np.roots(p)
        rts = np.sort(rts[np.abs(rts.imag) < 1e-12].real)
        lim = np.sqrt(max(r1 * r1 - b2 * b2, 0.0))
        pts = np.concatenate([[-lim], rts[(rts > -lim) & (rts < lim)], [lim]])
        for a, b in zip(pts[:-1], pts[1:]):
            mid = 0.5 * (a + b)
            if Q_and_grad(mid, b2)[0] > 2 * delta:
                continue
            if rng is None:
                t = np.linspace(0, 1, nb1)
                t = 0.5 - 0.5 * np.cos(np.pi * t)          # сгущение к концам
            else:
                t = rng.random(nb1)
            xs = a + (b - a) * t
            out1.append(xs)
            out2.append(np.full_like(xs, b2))
    return np.concatenate(out1), np.concatenate(out2)


def polar_points(delta, nb1=20001):
    pts = []
    for a in np.concatenate([np.linspace(-r1, r1, nb1), np.logspace(-8, np.log10(r1), 2000)]):
        # d2 Q(a, .) — многочлен по b2; строим через выборку коэффициентов (степень <= 15)
        ys = np.linspace(-1, 1, 40)
        vals = np.array([Q_and_grad(a, y)[2] for y in ys])
        coef = np.polyfit(ys, vals, 15)
        for y in np.roots(coef):
            if abs(y.imag) > 1e-9:
                continue
            y = y.real
            # уточнение Ньютоном по b2
            for _ in range(30):
                h = 1e-7 * max(1.0, abs(y))
                g = Q_and_grad(a, y)[2]
                dg = (Q_and_grad(a, y + h)[2] - Q_and_grad(a, y - h)[2]) / (2 * h)
                if dg == 0:
                    break
                y -= g / dg
            if a * a + y * y <= r1 * r1:
                Q, d1, d2 = Q_and_grad(a, y)
                if abs(d2) < 1e-12 * (1 + abs(d1)) and Q <= 2 * delta:
                    pts.append((a, y, Q, a * d1))
    return np.array(pts)


def run(delta):
    P = polar_points(delta)
    band = P[P[:, 2] >= EPS1 * delta]
    m = band[:, 3].min()
    mu = KAPPA * m / (4 * delta)
    print(f'delta={delta:.0e}: polar pts in K: {len(P)}, in band: {len(band)}; '
          f'min b1 d1Q (polar, all) = {P[:, 3].min():.3e}; m = {m:.3e}; mu = {mu:.3e}')
    b1, b2 = sample_K(delta, 6001, 60)
    Q, d1, d2 = Q_and_grad(b1, b2)
    rhs = mu * (Q - EPS_B * delta)
    deficit = rhs - KAPPA * b1 * d1
    bad = deficit > 0
    need = np.max(deficit[bad] / d2[bad]**2) if bad.any() else 0.0
    Lam = 1.2 * need
    rng = np.random.default_rng(1)
    c1, c2 = sample_K(delta, 15001, 200, rng)
    Q, d1, d2 = Q_and_grad(c1, c2)
    lhs = KAPPA * c1 * d1 + Lam * d2**2
    marg = lhs - mu * (Q - EPS_B * delta)
    i = np.argmin(marg / (mu * delta))
    print(f'   Lam_needed = {need:.3e}; check with Lam = {Lam:.3e} on {len(c1)} pts: '
          f'min (xi.gradQ - mu(Q-delta/8))/(mu delta) = {marg[i] / (mu * delta):.4f} at b=({c1[i]:.4f},{c2[i]:.4f}), '
          f'Q/delta={Q[i] / delta:.3f}')
    return need, mu


if __name__ == '__main__':
    for d in (1e-6, 1e-7, 1e-8, 1e-9):
        run(d)
