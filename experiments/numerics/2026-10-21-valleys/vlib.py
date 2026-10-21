"""
vlib.py -- "дно оврага" для потенциалов полигона n = 3 (mpmath, высокая точность).  [Эксперимент]

m(r) = min_{|q|=r} U(q).  Локальные минимумы на сфере S_r ищутся методом Ньютона на сфере (mpmath, dps=DPS)
из множества стартов: (a) точки множества Sigma (нулевое множество младшей формы) + поперечные сдвиги
порядка r, r^1.5, r^2, r^3; (b) предыдущие минимумы (продолжение по r); (c) грубая сетка на сфере (double).
"""
import sys, os, math, itertools
import numpy as np
import sympy as sp
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
ZOO = os.path.join(HERE, '..', '2026-10-21-zoo')
sys.path.insert(0, ZOO)

DPS = 60
mp.mp.dps = DPS

x, y, z = sp.symbols('x y z')
XYZ = (x, y, z)


def load_catalog():
    import catalog
    return {e['id']: e for e in catalog.CATALOG}


def sym(U):
    return sp.expand(sp.sympify(U, locals={'x': x, 'y': y, 'z': z}))


class Pot:
    """потенциал: U, grad, Hess в mpmath и numpy"""

    def __init__(self, Ustr):
        self.U = sym(Ustr)
        g = [sp.diff(self.U, v) for v in XYZ]
        H = [[sp.diff(gi, v) for v in XYZ] for gi in g]
        exprs = [self.U] + g + [H[i][j] for i in range(3) for j in range(i, 3)]
        self._f = sp.lambdify(XYZ, exprs, modules='mpmath', cse=True)
        self._fn = sp.lambdify(XYZ, [self.U], modules='numpy')
        self._Un = sp.lambdify(XYZ, self.U, modules='numpy')
        self.deg_low = min(sum(m) for m, _ in sp.Poly(self.U, *XYZ).terms())

    def full(self, q):
        v = self._f(q[0], q[1], q[2])
        U = v[0]
        g = [v[1], v[2], v[3]]
        h = v[4:]
        H = [[h[0], h[1], h[2]], [h[1], h[3], h[4]], [h[2], h[4], h[5]]]
        return U, g, H

    def val(self, q):
        return self._f(q[0], q[1], q[2])[0]

    def un(self, X, Y, Z):
        return self._Un(X, Y, Z)


# ---------------------------------------------------------------- векторы (списки mpf)
def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def nrm(a):
    return mp.sqrt(dot(a, a))


def unit(a):
    n = nrm(a)
    return [c / n for c in a]


def tangent_frame(w):
    """ортонормированный базис касательной плоскости к единичной сфере в точке w"""
    ax = min(range(3), key=lambda i: abs(w[i]))
    a = [mp.mpf(0)] * 3
    a[ax] = mp.mpf(1)
    e1 = unit(cross(w, a))
    e2 = cross(w, e1)
    return e1, e2


def mpv(a):
    return [mp.mpf(c) for c in a]


# ---------------------------------------------------------------- локальная минимизация на S_r
def riem(P, w, r):
    """значение g=U(r w), градиент и риманов гессиан на единичной сфере в касательном базисе (e1,e2)"""
    q = [r * c for c in w]
    U, g, H = P.full(q)
    gw = [r * c for c in g]
    sn = dot(w, gw)
    e1, e2 = tangent_frame(w)
    e = (e1, e2)
    gt = [dot(e[i], gw) for i in range(2)]
    Ht = [[0, 0], [0, 0]]
    Hw = [[r * r * H[a][b] for b in range(3)] for a in range(3)]
    for i in range(2):
        for j in range(2):
            s = mp.mpf(0)
            for a in range(3):
                for b in range(3):
                    s += e[i][a] * Hw[a][b] * e[j][b]
            Ht[i][j] = s - (sn if i == j else 0)
    return U, gt, Ht, e


def eig2(Ht):
    a, b, d = Ht[0][0], Ht[0][1], Ht[1][1]
    tr = (a + d) / 2
    df = mp.sqrt(((a - d) / 2) ** 2 + b * b)
    return tr - df, tr + df


def newton_min(P, w0, r, maxit=200, tol=None):
    """минимум U на S_r из старта w0 (единичный вектор, mpf). Возвращает (w, U, gt, Ht, e, ok)."""
    tol = tol or mp.mpf(10) ** (-(DPS // 2))
    w = unit(w0)
    U, gt, Ht, e = riem(P, w, r)
    conv = False
    for it in range(maxit):
        gn = mp.sqrt(gt[0] ** 2 + gt[1] ** 2)
        l1, l2 = eig2(Ht)
        # шаг ньютоновский с LM-сдвигом (модифицированный)
        scale = max(abs(l1), abs(l2), mp.mpf(10) ** (-400))
        lam = mp.mpf(0) if l1 > 0 else (-l1 + mp.mpf('1e-3') * scale)
        A = [[Ht[0][0] + lam, Ht[0][1]], [Ht[1][0], Ht[1][1] + lam]]
        det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
        s = [-(A[1][1] * gt[0] - A[0][1] * gt[1]) / det, -(-A[1][0] * gt[0] + A[0][0] * gt[1]) / det]
        sn_ = mp.sqrt(s[0] ** 2 + s[1] ** 2)
        if sn_ < tol:
            conv = True
            break
        # ограничение шага (угол) - доверительная область
        if sn_ > mp.mpf('0.3'):
            s = [c * mp.mpf('0.3') / sn_ for c in s]
            sn_ = mp.mpf('0.3')
        # поиск по лучу
        t = mp.mpf(1)
        ok = False
        for _ in range(60):
            wn = unit([w[i] + t * (s[0] * e[0][i] + s[1] * e[1][i]) for i in range(3)])
            Un = P.val([r * c for c in wn])
            if Un <= U:
                ok = True
                break
            t /= 2
        if not ok:
            break
        w = wn
        U, gt, Ht, e = riem(P, w, r)
    gn = mp.sqrt(gt[0] ** 2 + gt[1] ** 2)
    l1, l2 = eig2(Ht)
    return w, U, gt, Ht, e, (l1 > 0 and conv)


def geod(w, e, s):
    return [mp.cos(s) * w[i] + mp.sin(s) * e[i] for i in range(3)]


def half_width(P, w, e, r, m, Hgii, sign):
    """угол s>0 вдоль геодезической (w, sign*e) до пересечения U = m/2 (m<0). Возвращает mpf или None (если >1.2)."""
    target = m / 2
    s_est = mp.sqrt(abs(m) / abs(Hgii)) if Hgii > 0 else mp.mpf('1e-6')
    ee = [sign * c for c in e]
    s_lo = mp.mpf(0)
    s = s_est / 8
    f = lambda ss: P.val([r * c for c in geod(w, ee, ss)]) - target
    # на старте f<0 (U=m<target)
    tries = 0
    while f(s) < 0:
        s_lo = s
        s *= mp.mpf('1.25')
        tries += 1
        if s > 1.2 or tries > 400:
            return None
    s_hi = s
    for _ in range(45):
        mid = (s_lo + s_hi) / 2
        if f(mid) < 0:
            s_lo = mid
        else:
            s_hi = mid
    return (s_lo + s_hi) / 2


# ---------------------------------------------------------------- Sigma: образцы на сфере
def sphere_zero_samples(fstr, n_theta=1500, n_phi=1500):
    """точки на S^2 (double), где однородная форма f меняет знак: поиск по сетке + линейная интерполяция
    + доводка Ньютоном по градиенту. Возвращает массив (N,3)."""
    f = sym(fstr)
    F = sp.lambdify(XYZ, f, 'numpy')
    gF = sp.lambdify(XYZ, [sp.diff(f, v) for v in XYZ], 'numpy')
    th = np.linspace(1e-4, np.pi - 1e-4, n_theta)
    ph = np.linspace(0, 2 * np.pi, n_phi, endpoint=False)
    TH, PH = np.meshgrid(th, ph, indexing='ij')
    X = np.sin(TH) * np.cos(PH)
    Y = np.sin(TH) * np.sin(PH)
    Zc = np.cos(TH)
    V = F(X, Y, Zc) + 0 * X
    pts = []
    sgn = np.sign(V)
    # смена знака по theta
    ch = (sgn[:-1, :] * sgn[1:, :] <= 0)
    ii, jj = np.nonzero(ch)
    for a, b in zip(ii, jj):
        pts.append((X[a, b], Y[a, b], Zc[a, b]))
    ch = (sgn[:, :-1] * sgn[:, 1:] <= 0)
    ii, jj = np.nonzero(ch)
    for a, b in zip(ii, jj):
        pts.append((X[a, b], Y[a, b], Zc[a, b]))
    pts = np.array(pts)
    # доводка
    for _ in range(8):
        v = F(pts[:, 0], pts[:, 1], pts[:, 2])
        g = np.array(gF(pts[:, 0], pts[:, 1], pts[:, 2]), dtype=float)
        if g.ndim == 1:
            g = g[:, None]
        g = g.T
        gp = g - (g * pts).sum(1)[:, None] * pts
        n2 = (gp ** 2).sum(1) + 1e-300
        pts = pts - (v / n2)[:, None] * gp
        pts /= np.linalg.norm(pts, axis=1)[:, None]
    v = np.abs(F(pts[:, 0], pts[:, 1], pts[:, 2]))
    pts = pts[v < 1e-8]
    return pts


def thin_points(pts, n, rng):
    """равномерно проредить множество точек на сфере: жадно (farthest point)"""
    if len(pts) <= n:
        return pts
    idx = [int(rng.integers(len(pts)))]
    d = np.linalg.norm(pts - pts[idx[0]], axis=1)
    for _ in range(n - 1):
        k = int(np.argmax(d))
        idx.append(k)
        d = np.minimum(d, np.linalg.norm(pts - pts[k], axis=1))
    return pts[idx]


def grid_minima(P, r, nth=1200, nph=2400, ntop=60):
    """грубый глобальный поиск на сфере в double: локальные минимумы сетки (с 8 соседями)"""
    th = np.linspace(0, np.pi, nth)
    ph = np.linspace(0, 2 * np.pi, nph, endpoint=False)
    TH, PH = np.meshgrid(th, ph, indexing='ij')
    Xc = r * np.sin(TH) * np.cos(PH)
    Yc = r * np.sin(TH) * np.sin(PH)
    Zc = r * np.cos(TH)
    V = P.un(Xc, Yc, Zc) + 0 * Xc
    Vp = np.pad(V, ((1, 1), (0, 0)), mode='edge')
    isMin = np.ones_like(V, dtype=bool)
    for da in (-1, 0, 1):
        for db in (-1, 0, 1):
            if da == 0 and db == 0:
                continue
            sh = np.roll(Vp[1 + da:1 + da + nth, :], -db, axis=1) if True else None
            isMin &= V <= sh
    ii, jj = np.nonzero(isMin)
    order = np.argsort(V[ii, jj])[:ntop]
    out = []
    for k in order:
        a, b = ii[k], jj[k]
        out.append((float(np.sin(th[a]) * np.cos(ph[b])), float(np.sin(th[a]) * np.sin(ph[b])), float(np.cos(th[a]))))
    return out


def tube_seeds(P, pts_sigma, r, rng, offsets=(0, 1, -1), powers=(1, 1.5, 2, 3), nrand=0):
    """старты: точки Sigma, сдвинутые по касательной к сфере в случайных/нормальных направлениях"""
    seeds = []
    for p in pts_sigma:
        seeds.append(tuple(p))
        for pw in powers:
            for sgn in (1, -1):
                # два ортогональных направления в касательной плоскости
                a = np.array([1.0, 0, 0]) if abs(p[0]) < 0.9 else np.array([0, 1.0, 0])
                e1 = np.cross(p, a); e1 /= np.linalg.norm(e1)
                e2 = np.cross(p, e1)
                for e in (e1, e2):
                    q = p + sgn * (r ** pw) * e
                    q /= np.linalg.norm(q)
                    seeds.append(tuple(q))
    return seeds


def collect_minima(P, r, seeds, known=None, dedupe_tol=mp.mpf('1e-12')):
    """запустить Ньютон из стартов; вернуть список локальных минимумов (w,U,Ht,e) без повторов"""
    res = []
    allseeds = list(seeds) + (list(known) if known else [])
    for s in allseeds:
        try:
            w, U, gt, Ht, e, ok = newton_min(P, mpv(s), r)
        except (ZeroDivisionError, ValueError):
            continue
        if not ok:
            continue
        gn = mp.sqrt(gt[0] ** 2 + gt[1] ** 2)
        if gn > mp.mpf(10) ** (-(DPS // 2)) * max(abs(U), mp.mpf(10) ** (-300)):
            pass  # не сошлось до конца; всё равно оставляем, если Гессиан положителен
        dup = False
        for (w2, U2, *_r) in res:
            if nrm([w[i] - w2[i] for i in range(3)]) < dedupe_tol:
                dup = True
                break
        if not dup:
            res.append((w, U, Ht, e))
    res.sort(key=lambda t: t[1])
    return res
