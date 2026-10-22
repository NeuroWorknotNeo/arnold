"""[Эксперимент] Строгий выход (A5) теоремы A [007] для двойной складки O2D с полосовым треугольным полем.

U = U_O2D + sigma x^32 y,  U_O2D = s^32 (-1 + A(th^, e) B(th^, e)),  s^2 = x^2 + y^2,  th^ = xy/s^2 = sin th cos th,
e = z/s^2 (fold §6.3: U_O2D — многочлен; здесь вычисляем по этой формуле); sigma = -1 ломает квазиоднородность
(луч th = 0 перестаёт быть инвариантным). Карта MT: трубчатая калибровка у экватора, веса (1, c = 2),
Psi(s, th, e) = (s cos th, s sin th, s^2 e),  rho = s,  A(rho) = rho^32 (a0 = 1, beta = 32).
Поле MT: xi^(kappa) = kappa (th, Lam d_e P(th, e)),  P = A B (th^(th), e) — коническая компонента kappa*th зависит
только от th (условие (T)), Lam = 1.5 Lam_0(delta) из band_T.py (PO2D).
Y = Psi_s - (xi_th/s) Psi_th - (xi_e/s) Psi_e.
Xi = d/dt (V - delta rho^beta) вычисляется по определению (без тождества (1.3)): d/dt(|v|^2/2+U) = 0,
pdot = -<grad U, Y> + <v, D_v Y>, hdot = 2 <Y, D_v Y>, rhodot = <grad rho, v>.
Точки множества (A5): (th, e) из выборки K = {P <= 2 delta} (band_T.Profile) с W/rho^beta <= delta,
K_perp = delta rho^beta - W, v = -lam Y + v_perp, |v_perp|^2 = 2 K_perp, направления v_perp — по сетке в Y^perp.
Печатается min N, N := (rho/lam) Xi / (delta rho^beta), по точкам; нужно N > 0. Ожидание: N >= ~ kappa*mu*(1-1/8)
при kappa <~ delta (условие (5.4) MT), и провал при большом kappa (перекрёстные члены ~ kappa^2/delta).
Контроль: поле с нарушенным (T): xi_th = kappa (th + e^2/2) (коническая компонента зависит от узкой e).
"""
import sys
import numpy as np
import sympy as sp
import mpmath as mp
sys.path.insert(0, '.')
from band_T import Profile, PROFILES  # noqa: E402

mp.mp.dps = 50
x, y, z = sp.symbols('x y z', real=True)
beta, sigma = 32, -1
s2 = x**2 + y**2
s = sp.sqrt(s2)
TH, E = x * y / s2, z / s2
Ap = (TH - E**2)**2 + E**8
Bp = (TH - E**2 - E**3)**2 + E**8
U = s2**16 * (-1 + Ap * Bp) + sigma * x**32 * y
th = sp.atan2(y, x)
Ts, es = sp.symbols('T e', real=True)
PAB = ((Ts - es**2)**2 + es**8) * ((Ts - es**2 - es**3)**2 + es**8)
dPe_expr = sp.diff(PAB, es).subs({Ts: TH, es: E}, simultaneous=True)
q = sp.Matrix([x, y, z])
gU = sp.Matrix([sp.diff(U, w) for w in q])
grho = sp.Matrix([x / s, y / s, 0])


def build(kappa, Lam, nonT=False):
    xi_th = kappa * (th + (E**2 / 2 if nonT else 0))
    xi_e = kappa * Lam * dPe_expr
    Y = sp.Matrix([x / s + xi_th * y / s, y / s - xi_th * x / s, 2 * s * E - s * xi_e])
    J = Y.jacobian(q)
    return sp.lambdify((x, y, z), [U, list(gU), list(Y), J.tolist(), list(grho)], 'mpmath')


def exit_min(f, delta, svals, pts, nth, rng):
    out = []
    for S in svals:
        S = mp.mpf(S)
        worst = (mp.inf, None)
        for thv, ev in pts:
            thm, em = mp.mpf(thv), mp.mpf(ev)
            X, Yc, Zc = S * mp.cos(thm), S * mp.sin(thm), S**2 * em
            Uv, gUv, Yv, J, gr = f(X, Yc, Zc)
            gUv = mp.matrix(gUv); Yv = mp.matrix(Yv); J = mp.matrix(J); gr = mp.matrix(gr)
            W = Uv + S**beta
            K = delta * S**beta - W
            if K < 0:
                continue
            h = (Yv.T * Yv)[0]
            lam2 = 2 * (-Uv - K) / h
            if lam2 <= 0:
                continue
            lam = mp.sqrt(lam2)
            e0 = mp.matrix([0, 0, 1])
            e1 = e0 - Yv * ((Yv.T * e0)[0] / h); e1 = e1 / mp.norm(e1)
            e2 = mp.matrix([Yv[1] * e1[2] - Yv[2] * e1[1], Yv[2] * e1[0] - Yv[0] * e1[2], Yv[0] * e1[1] - Yv[1] * e1[0]])
            e2 = e2 / mp.norm(e2)
            angs = [2 * mp.pi * kk / nth for kk in range(nth)] + [2 * mp.pi * rng.random()]
            for a in angs:
                vp = mp.sqrt(2 * K) * (mp.cos(a) * e1 + mp.sin(a) * e2)
                v = -lam * Yv + vp
                p = (v.T * Yv)[0]
                DvY = J * v
                pdot = -(gUv.T * Yv)[0] + (v.T * DvY)[0]
                hdot = 2 * (Yv.T * DvY)[0]
                rdot = (gr.T * v)[0]
                Xi = beta * S**(beta - 1) * rdot - (p / h) * pdot + p * p / (2 * h * h) * hdot - beta * delta * S**(beta - 1) * rdot
                val = (S / lam) * Xi / (delta * S**beta)
                if val < worst[0]:
                    worst = (val, (round(float(thv), 4), round(float(ev), 4), mp.nstr(K / (delta * S**beta), 3)))
        out.append((S, worst))
    return out


def main_bulk():
    delta = 1e-4
    Lam = 1.5 * 3.2817e2       # band_T.out, PO2D, delta = 1e-4
    rng = np.random.default_rng(2026)
    pr = Profile(*PROFILES['PO2D'])
    xs, es_ = pr.sample(delta, 201, 6, rng)
    ths = pr.th(xs)
    Pv = pr.eval(xs, es_)[0]
    idx = np.where(Pv <= 1.05 * delta)[0]
    idx = rng.choice(idx, size=min(250, len(idx)), replace=False)
    pts = [(ths[i], es_[i]) for i in idx]
    print(f'O2D: delta={delta}, Lam={Lam:.4g}, mu=1, {len(pts)} points (th,e) with P <= 1.05 delta, 9 directions of v_perp')
    for kappa in (1e-6, 1e-5, 1e-4, 1e-3):
        f = build(kappa, Lam)
        for S, (val, where) in exit_min(f, delta, ('1e-6', '1e-9', '1e-12'), pts, 8, rng):
            print(f'  band (T) field, kappa={kappa:.0e}, s={mp.nstr(S, 2)}: min N = {mp.nstr(val, 6)}  '
                  f'(min N/kappa = {mp.nstr(val / kappa, 5)}) at (th,e,K/(d rho^b))={where}', flush=True)
    for kappa in (1e-5,):
        f = build(kappa, Lam, nonT=True)
        for S, (val, where) in exit_min(f, delta, ('1e-6', '1e-9', '1e-12'), pts, 8, rng):
            print(f'  nonT control xi_th = kappa(th + e^2/2), kappa={kappa:.0e}, s={mp.nstr(S, 2)}: min N = {mp.nstr(val, 6)} '
                  f'at {where}', flush=True)


def level_points(delta, S, ks, neps, rng):
    """Точки (th, e) с W/rho^beta = delta (1 - k) точно (Ньютон по th в mpmath при фиксированном e), k из ks.
    W/rho^beta = P(th, e) + sigma s cos^32(th) sin(th)."""
    pr = Profile(*PROFILES['PO2D'])
    S = mp.mpf(S)
    out = []
    eps_grid = list(np.linspace(-0.42, 0.42, neps)) + list(rng.uniform(-0.42, 0.42, neps))
    for ev in eps_grid:
        c = np.array([float(cf(ev)) for cf in pr.cx])
        for k_ in ks:
            cc = c.copy(); cc[-1] -= delta * (1 - k_)
            rts = np.roots(cc)
            for xr in rts[np.abs(rts.imag) < 1e-10].real:
                if abs(xr) >= 0.49:
                    continue
                t = mp.mpf(0.5 * np.arcsin(2 * xr)); em = mp.mpf(ev)
                Wf = lambda tt: (lambda TH_: ((TH_ - em**2)**2 + em**8) * ((TH_ - em**2 - em**3)**2 + em**8))(mp.sin(tt) * mp.cos(tt)) \
                    + sigma * S * mp.cos(tt)**32 * mp.sin(tt) - delta * (1 - k_)
                try:
                    t = mp.findroot(Wf, t, tol=mp.mpf(10)**-45)
                except Exception:
                    continue
                if t * t + em * em < mp.mpf('0.45')**2:
                    out.append((t, em, k_))
    return out


def exit_level(f, delta, S, pts, nth, rng):
    """Как exit_min, но точки уже на уровне; печатает min N по каждому k."""
    S = mp.mpf(S)
    best = {}
    for thm, em, k_ in pts:
        X, Yc, Zc = S * mp.cos(thm), S * mp.sin(thm), S**2 * em
        Uv, gUv, Yv, J, gr = f(X, Yc, Zc)
        gUv = mp.matrix(gUv); Yv = mp.matrix(Yv); J = mp.matrix(J); gr = mp.matrix(gr)
        W = Uv + S**beta
        K = delta * S**beta - W
        if K < 0:
            K = mp.mpf(0)
        h = (Yv.T * Yv)[0]
        lam = mp.sqrt(2 * (-Uv - K) / h)
        e0 = mp.matrix([0, 0, 1])
        e1 = e0 - Yv * ((Yv.T * e0)[0] / h); e1 = e1 / mp.norm(e1)
        e2 = mp.matrix([Yv[1] * e1[2] - Yv[2] * e1[1], Yv[2] * e1[0] - Yv[0] * e1[2], Yv[0] * e1[1] - Yv[1] * e1[0]])
        e2 = e2 / mp.norm(e2)
        for a in [2 * mp.pi * kk / nth for kk in range(nth)] + [2 * mp.pi * rng.random()]:
            v = -lam * Yv + mp.sqrt(2 * K) * (mp.cos(a) * e1 + mp.sin(a) * e2)
            p = (v.T * Yv)[0]
            DvY = J * v
            pdot = -(gUv.T * Yv)[0] + (v.T * DvY)[0]
            hdot = 2 * (Yv.T * DvY)[0]
            rdot = (gr.T * v)[0]
            Xi = beta * (1 - delta) * S**(beta - 1) * rdot - (p / h) * pdot + p * p / (2 * h * h) * hdot
            val = (S / lam) * Xi / (delta * S**beta)
            if k_ not in best or val < best[k_][0]:
                best[k_] = (val, (mp.nstr(thm, 4), mp.nstr(em, 4)))
    return best


def main_level():
    delta = 1e-4
    Lam = 1.5 * 3.2817e2
    rng = np.random.default_rng(7)
    ks = (0.0, 1e-7, 1e-5, 1e-3)
    print(f'O2D level-set test: W = delta(1-k) rho^beta (K_perp = k delta rho^beta), delta={delta}, Lam={Lam:.4g}, mu=1')
    for S in ('1e-9', '1e-12'):
        pts = level_points(delta, S, ks, 40, rng)
        print(f' s={S}: {len(pts)} level points', flush=True)
        for kappa in (1e-5, 1e-4, 1e-3, 1e-2):
            best = exit_level(build(kappa, Lam), delta, S, pts, 8, rng)
            print('   band (T), kappa=%.0e: ' % kappa + '; '.join(
                f'k={k_:.0e}: min N/kappa={mp.nstr(v / kappa, 5)}' for k_, (v, w) in sorted(best.items())), flush=True)
        best = exit_level(build(1e-4, Lam, nonT=True), delta, S, pts, 8, rng)
        print('   nonT control, kappa=1e-4: ' + '; '.join(
            f'k={k_:.0e}: min N={mp.nstr(v, 5)}' for k_, (v, w) in sorted(best.items())), flush=True)


if __name__ == '__main__':
    if 'level' in sys.argv[1:]:
        main_level()
    else:
        main_bulk()
