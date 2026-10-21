"""
curves.py -- поиск дна оврага вдоль кривой Sigma = {f = 0} на сфере: профиль m(s) = min_theta U(r w(s, theta)),
где w(s, theta) = cos(theta) p(s) + sin(theta) n(s), p(s) in Sigma, n(s) -- единичная нормаль к Sigma в касательной
плоскости сферы. Овраг узкий и изогнутый (ширина ~ r), поэтому обычный Ньютон на сфере идёт по дну крошечными
шагами; профильный метод этого избегает. [Эксперимент]
"""
import numpy as np
import sympy as sp
import mpmath as mp
from vlib import *


class Form:
    def __init__(self, fstr):
        self.f = sym(fstr)
        g = [sp.diff(self.f, v) for v in XYZ]
        self._f = sp.lambdify(XYZ, [self.f] + g, modules='mpmath', cse=True)
        self._fn = sp.lambdify(XYZ, [self.f] + g, modules='numpy')

    def fg(self, w):
        v = self._f(w[0], w[1], w[2])
        return v[0], [v[1], v[2], v[3]]

    def fgn(self, w):
        v = self._fn(w[0], w[1], w[2])
        return float(v[0]), np.array([float(v[1]), float(v[2]), float(v[3])])


def proj_mp(F, w, iters=60):
    """проекция (Гаусс-Ньютон) точки w в окрестности Sigma на {f=0} ∩ S^2"""
    w = unit(w)
    for _ in range(iters):
        f, g = F.fg(w)
        gp = [g[i] - dot(g, w) * w[i] for i in range(3)]
        n2 = dot(gp, gp)
        if n2 == 0:
            break
        d = [f * c / n2 for c in gp]
        w = unit([w[i] - d[i] for i in range(3)])
        if nrm(d) < mp.mpf(10) ** (-(DPS - 8)):
            break
    return w


def frame_curve(F, p):
    """касательная tau к Sigma и нормаль n (в касательной плоскости сферы) в точке p"""
    f, g = F.fg(p)
    gp = [g[i] - dot(g, p) * p[i] for i in range(3)]
    n = unit(gp)
    tau = unit(cross(p, n))
    return tau, n


def trace_double(F, start, ds=0.02, maxn=2000):
    """замкнутая кривая Sigma в double: список точек с шагом ds"""
    def proj(w):
        w = w / np.linalg.norm(w)
        for _ in range(30):
            f, g = F.fgn(w)
            gp = g - (g @ w) * w
            n2 = gp @ gp
            if n2 == 0:
                break
            d = f * gp / n2
            w = w - d
            w /= np.linalg.norm(w)
            if np.linalg.norm(d) < 1e-14:
                break
        return w
    p0 = proj(np.array(start, float))
    pts = [p0]
    p = p0
    prev_tau = None
    for k in range(maxn):
        f, g = F.fgn(p)
        gp = g - (g @ p) * p
        n = gp / np.linalg.norm(gp)
        tau = np.cross(p, n)
        if prev_tau is not None and tau @ prev_tau < 0:
            tau = -tau
        prev_tau = tau
        p = proj(p + ds * tau)
        if k > 5 and np.linalg.norm(p - p0) < 0.75 * ds:
            break
        pts.append(p)
    return np.array(pts)


def components(fstr, ds=0.02, rng=None):
    """все связные компоненты кривой {f=0} на S^2 как замкнутые ломаные"""
    F = Form(fstr)
    S = sphere_zero_samples(fstr, 800, 800)
    comps = []
    covered = np.zeros((0, 3))
    for s in S:
        if len(covered) and np.min(np.linalg.norm(covered - s, axis=1)) < 3 * ds:
            continue
        pts = trace_double(F, s, ds)
        comps.append(pts)
        covered = np.vstack([covered, pts])
    return F, comps


def mpf3(a):
    return [mp.mpf(float(c)) for c in a]


# ---------------------------------------------------------------- 1D минимизация по theta
def phi_d(P, p, n, r, th):
    """U, dU/dth, d2U/dth2 на геодезической w(th) = cos p + sin n"""
    c, s_ = mp.cos(th), mp.sin(th)
    w = [c * p[i] + s_ * n[i] for i in range(3)]
    t = [-s_ * p[i] + c * n[i] for i in range(3)]
    q = [r * c_ for c_ in w]
    U, g, H = P.full(q)
    d1 = r * dot(g, t)
    Ht = [sum(H[a][b] * t[b] for b in range(3)) for a in range(3)]
    d2 = r * r * dot(t, Ht) - r * dot(g, w)
    return U, d1, d2, w


def min_theta(P, p, n, r, th0, maxit=60):
    """локальный минимум по theta из старта th0: (th, U, w) или None"""
    th = mp.mpf(th0)
    U, d1, d2, w = phi_d(P, p, n, r, th)
    tolth = mp.mpf(10) ** (-(DPS // 2 + 5))
    for it in range(maxit):
        if d2 <= 0:
            # шаг градиентный малой длины
            step = -d1 / (abs(d2) + mp.mpf(10) ** (-300)) if d2 != 0 else mp.mpf(0)
            lim = max(abs(th), r) * 0.5
            if abs(step) > lim:
                step = lim * (1 if step > 0 else -1)
        else:
            step = -d1 / d2
            lim = max(abs(th), r) * 4
            if abs(step) > lim:
                step = lim * (1 if step > 0 else -1)
        if abs(step) < tolth:
            break
        t = mp.mpf(1)
        ok = False
        for _ in range(50):
            U2, d12, d22, w2 = phi_d(P, p, n, r, th + t * step)
            if U2 <= U:
                ok = True
                break
            t /= 2
        if not ok:
            break
        th = th + t * step
        U, d1, d2, w = U2, d12, d22, w2
    if d2 <= 0:
        return None
    return th, U, w


def best_theta(P, p, n, r, cont=None):
    starts = [mp.mpf(0)]
    for pw in (0.5, 1, 1.5, 2, 3):
        for sg in (1, -1):
            starts.append(sg * r ** mp.mpf(pw))
    if cont is not None:
        starts.append(cont)
    best = None
    for s0 in starts:
        res = min_theta(P, p, n, r, s0)
        if res is None:
            continue
        if best is None or res[1] < best[1]:
            best = res
    return best


def point_at(F, pk, tauk, s):
    """p(s) = project(p_k + s tau_k) на Sigma, и её нормаль"""
    p = proj_mp(F, [pk[i] + s * tauk[i] for i in range(3)])
    tau, n = frame_curve(F, p)
    return p, tau, n


def profile(P, F, comp, r):
    """профиль вдоль компоненты (замкнутая ломаная comp). Возвращает список записей"""
    recs = []
    cont = None
    for pk in comp:
        p = proj_mp(F, mpf3(pk))
        tau, n = frame_curve(F, p)
        best = best_theta(P, p, n, r, cont)
        if best is None:
            recs.append(None)
            continue
        cont = best[0]
        recs.append(dict(p=p, tau=tau, n=n, th=best[0], U=best[1]))
    return recs


def golden(fun, a, b, tol):
    gr = (mp.sqrt(5) - 1) / 2
    c = b - gr * (b - a)
    d = a + gr * (b - a)
    fc, fd = fun(c), fun(d)
    while abs(b - a) > tol:
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - gr * (b - a)
            fc = fun(c)
        else:
            a, c, fc = c, d, fd
            d = a + gr * (b - a)
            fd = fun(d)
    return (a + b) / 2


def refine_profile_min(P, F, rec, r, ds):
    """уточнить локальный минимум профиля вблизи записи rec: золотое сечение по s в [-1.3 ds, 1.3 ds]"""
    pk, tauk = rec['p'], rec['tau']
    state = {'th': rec['th']}

    def fun(s):
        p, tau, n = point_at(F, pk, tauk, s)
        res = min_theta(P, p, n, r, state['th'])
        if res is None:
            return mp.mpf('1e300')
        state['th'] = res[0]
        return res[1]
    tol = mp.mpf(10) ** (-(DPS // 2 + 3))
    s = golden(fun, -mp.mpf(1.3) * ds, mp.mpf(1.3) * ds, tol)
    p, tau, n = point_at(F, pk, tauk, s)
    res = min_theta(P, p, n, r, state['th'])
    return res  # (th, U, w)


def curve_minima(P, F, comp, r, ds):
    """все локальные минимумы профиля (U<0) на компоненте comp: список (w, U)"""
    recs = profile(P, F, comp, r)
    N = len(recs)
    out = []
    for k in range(N):
        a = recs[k]
        if a is None:
            continue
        l = recs[(k - 1) % N]
        rr = recs[(k + 1) % N]
        if (l is not None and l['U'] < a['U']) or (rr is not None and rr['U'] < a['U']):
            continue
        res = refine_profile_min(P, F, a, r, ds)
        if res is None:
            continue
        th, U, w = res
        if U < 0:
            out.append((w, U))
    return out, recs
