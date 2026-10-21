# [Эксперимент] Перепроверка по замечанию З12 рецензента R40 (notes/reviewer/2026-10-21-morse-bott-mult-A.md):
# строгий выход (A5) для примера W3 в точках СТЕНКИ {W = delta s^beta} при v_perp = 0 (K_perp = 0),
# плотная выборка по лучам (256 лучей) в плоскости (theta, e), глубокий режим s = 1e-12.
# В этих точках T1 = T2 = T3 = 0, и (rho/lambda) Xi/(delta rho^beta) равно отношению Эйлера профиля
# с весами (kappa, c_2) (см. §5 записки notes/prover/2026-10-21-morse-bott-mult.md).
# Функции карты, поля и V берутся из exit_W.py (пример W3).
import sys
sys.argv = ['exit_W.py', 'W3']
import mpmath as mp
import exit_W as X

mp.mp.dps = 40


def wall_point(s, alpha, delta):
    """Точка стенки W = delta s^beta на луче (theta, e) = lmb (cos alpha * 0.25, sin alpha) от b = 0."""
    dt, de = mp.cos(alpha)*mp.mpf('0.25'), mp.sin(alpha)
    Wm = lambda lmb: X.Uf(*X.point(s, lmb*dt, lmb*de)) + X.a0*s**X.beta - delta*s**X.beta
    lo, hi = mp.mpf(0), mp.mpf('0.01')
    while Wm(hi) < 0:
        hi *= mp.mpf('1.1')
    for _ in range(120):
        mid = (lo + hi)/2
        if Wm(mid) < 0:
            lo = mid
        else:
            hi = mid
    return lo*dt, lo*de


def value(s, t, e, kap, lam, delta):
    q = X.point(s, t, e)
    Y, rho = X.Yfield(q, kap, lam)
    h = sum(c*c for c in Y)
    Yn = mp.sqrt(h)
    K = delta*s**X.beta - (X.Uf(*q) + X.a0*s**X.beta)
    vpar = mp.sqrt(-2*X.Uf(*q) - 2*max(K, 0))
    v = [-vpar*Y[i]/Yn for i in range(3)]
    gq = [g(*q) for g in X.gU]
    fl = lambda tt: X.Vminus([q[i] + tt*v[i] for i in range(3)], [v[i] - tt*gq[i] for i in range(3)], kap, lam, delta)
    Xi = mp.diff(fl, 0)
    return rho/(vpar/Yn)*Xi/(delta*rho**X.beta)


s = mp.mpf('1e-12')
for delta in (mp.mpf('0.01'), mp.mpf('0.002')):
    for kap in (mp.mpf('0.05'), mp.mpf('0.1'), mp.mpf('0.2')):
        for name, lam in (('W:  lambda = c - kappa/2', X.cw - kap/2), ('Mb: lambda = 0', mp.mpf(0))):
            best = None
            for k in range(256):
                al = 2*mp.pi*k/256
                t, e = wall_point(s, al, delta)
                val = value(s, t, e, kap, lam, delta)
                if best is None or val < best[0]:
                    best = (val, t, e)
            print('delta=%-6s kappa=%-5s %-26s min по стенке (256 лучей) = %-12s [theta=%s, e=%s]' % (
                mp.nstr(delta, 3), mp.nstr(kap, 3), name, mp.nstr(best[0], 6), mp.nstr(best[1], 4), mp.nstr(best[2], 4)))
