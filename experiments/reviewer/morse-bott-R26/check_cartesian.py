"""R26: Cartesian check of (6.5), (6.7) and of the scaled normal form (2.8) on the model of model.py.

D_w Y and D_Y Y are computed by numerical differentiation of the Cartesian field Y(q)
(model.Yfield), independently of the moving-frame algebra; the right-hand sides use the
formulas of the note with eps = k eta/s (k = 1), psi = eta*_s - kappa theta eta*_theta/s and
their partial derivatives (computed by numerical differentiation of eta^* in (s, theta)).
"""
import mpmath as mp
from model import build, frame, eta_star_data, Psi, Yfield, dot, chart_inv

mp.mp.dps = 60


def etas_fun(M):
    return lambda s, th: eta_star_data(M, s, th * mp.sqrt(2))[0]


def check(M, s, theta, e, kappa, wcoef):
    c = mp.mpf(3) / 2
    zeta = s**c * e
    q = Psi(M, s, theta, zeta)
    Y, _ = Yfield(M, q, kappa)
    om, T, n, _, _ = frame(theta * mp.sqrt(2))
    w = wcoef[0] * om + wcoef[1] * T + wcoef[2] * n
    hh = mp.mpf(10)**-25 * s
    DwY = (Yfield(M, q + hh * w, kappa)[0] - Yfield(M, q - hh * w, kappa)[0]) / (2 * hh)
    DYY = (Yfield(M, q + hh * Y, kappa)[0] - Yfield(M, q - hh * Y, kappa)[0]) / (2 * hh)
    lhs67 = s * dot(w, DwY)
    # quantities of the note
    E = etas_fun(M)
    k = 1
    eta = E(s, theta) + zeta
    Es = mp.diff(lambda x: E(x, theta), s)
    Et = mp.diff(lambda t: E(s, t), theta)
    eps_f = lambda x, t: k * (E(x, t) + zeta) / x
    psi_f = lambda x, t: mp.diff(lambda y: E(y, t), x) - kappa * t * mp.diff(lambda u: E(x, u), t) / x
    eps = eps_f(s, theta)
    eps_s = mp.diff(lambda x: eps_f(x, theta), s)
    eps_t = mp.diff(lambda t: eps_f(s, t), theta)
    psi = psi_f(s, theta)
    psi_s = mp.diff(lambda x: psi_f(x, theta), s)
    psi_t = mp.diff(lambda t: psi_f(s, t), theta)
    wo, wT, wn = wcoef
    kt = kappa * theta
    terms = [(1 / (1 - eps) - kappa) * wT**2,
             kt * s * eps_s * wo * wT,
             s * psi_s * wo * wn,
             kt * wo * wT,
             (kt * eps_t - psi * k) * wT**2 / (1 - eps),
             psi_t * wT * wn / (1 - eps),
             -kt * k * wT * (wo * Es + wT * Et / (s * (1 - eps)))]
    rhs67 = sum(terms)
    f65 = [-kt**2 * (1 - eps),
           kt * (s * eps_s - 1 + kappa * (1 - eps) - kt * eps_t + psi * k),
           s * psi_s + kt**2 * (1 - eps) * k - kt * psi_t]
    sDYY = [s * dot(DYY, om), s * dot(DYY, T), s * dot(DYY, n)]
    # (6.3)
    Y63 = [1, -kt * (1 - eps), psi]
    Ycomp = [dot(Y, om), dot(Y, T), dot(Y, n)]
    return (mp.nstr(lhs67 - rhs67, 5), mp.nstr(abs(lhs67), 5),
            [mp.nstr(sDYY[i] - f65[i], 5) for i in range(3)],
            [mp.nstr(Ycomp[i] - Y63[i], 5) for i in range(3)])


for p in (2, 3):
    M = build(p)
    print(f'--- p = {p}')
    for (s, th, e, ka, w) in [(mp.mpf('1e-2'), mp.mpf('0.3'), mp.mpf('0.4'), mp.mpf('0.37'), (0.3, -0.8, 0.5)),
                              (mp.mpf('3e-3'), mp.mpf('-0.2'), mp.mpf('-0.7'), mp.mpf('0.5'), (-0.6, 0.2, 0.9)),
                              (mp.mpf('1e-4'), mp.mpf('0.1'), mp.mpf('0.2'), mp.mpf('0.05'), (0.1, 1.0, -0.3))]:
        r = check(M, s, th, e, ka, [mp.mpf(x) for x in w])
        print(f's={mp.nstr(s,3)} th={mp.nstr(th,3)} e={mp.nstr(e,3)} ka={mp.nstr(ka,3)}: '
              f'(6.7) diff={r[0]} (|lhs|={r[1]}); (6.5) diff={r[2]}; (6.3) diff={r[3]}')
    # (2.8): U(Psi(s,theta,s^c e))/s^5 -> G(theta) + 4 e^2
    for th, e in [(mp.mpf('0.3'), mp.mpf('0.5')), (mp.mpf('-0.1'), mp.mpf('0.9'))]:
        G = mp.mpf(2)**-2.5 * ((1 - mp.cos(mp.sqrt(2) * th))**p - M['b'])
        out = []
        for s in [mp.mpf('1e-4'), mp.mpf('1e-8'), mp.mpf('1e-12')]:
            q = Psi(M, s, th, s**mp.mpf(1.5) * e)
            out.append(mp.nstr(M['U'](*q) / s**5 - (G + 4 * e**2), 5))
        print(f'(2.8) th={mp.nstr(th,3)} e={mp.nstr(e,3)}: F - F0 at s=1e-4,1e-8,1e-12:', out)
