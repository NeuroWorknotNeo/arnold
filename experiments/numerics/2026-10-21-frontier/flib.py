"""
flib.py -- общая библиотека: дно оврага (минимумы U на сферах S_r, mpmath), продолжение по r, профильные ширины,
масштабированный профиль.  Повторно использует vlib (valleys) без изменений.  [Эксперимент]
"""
import sys, os, math
HERE = os.path.dirname(os.path.abspath(__file__))
VAL = os.path.join(HERE, '..', '2026-10-21-valleys')
sys.path.insert(0, VAL)
import numpy as np
import mpmath as mp
import sympy as sp
from vlib import (Pot, DPS, XYZ, dot, cross, nrm, unit, tangent_frame, mpv, riem, eig2, newton_min, geod,
                  sphere_zero_samples, thin_points, grid_minima, sym)
import fcat

mp.mp.dps = DPS
SEED = 20261021


def cat():
    return {e['id']: e for e in fcat.CAT}


def sigma_form(eid):
    """строка однородной формы, нули которой образуют Sigma (для старта), или None"""
    return {
        'A1': 'z', 'A2': 'z', 'A3': 'z', 'E1': 'z',
        'B1': 'y**2*z-x**3', 'B2': 'y**2*z-x**3', 'B4': 'y**2*z-x**3',
        'B3': '(x**2+y**2-z**2)*(x**2+2*y**2-z**2)', 'B3b': '(x**2+y**2-z**2)*(x**2+2*y**2-z**2)',
        'D1': '(x**2+y**2-z**2)*(x**2/2+y**2-z**2)', 'D2': '(x**2+y**2-z**2)*(x**2/2+y**2-z**2)', 'D3': '(x**2+y**2-z**2)*(x**2/2+y**2-z**2)', 'D4': '(x**2+y**2-z**2)*(x**2/2+y**2-z**2)',
        'V1': None, 'V2': None, 'V3': None, 'V4': None,
    }[eid]


def tangent_basis_np(p):
    a = np.array([1.0, 0, 0]) if abs(p[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = np.cross(p, a)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(p, e1)
    return e1, e2


POW = (0.2, 0.25, 1 / 3, 0.5, 2 / 3, 0.75, 1.0, 1.25, 1.5, 2.0, 3.0)


def seeds_around(p, r, pows=POW):
    p = np.array(p, float)
    p /= np.linalg.norm(p)
    e1, e2 = tangent_basis_np(p)
    out = [tuple(p)]
    for pw in pows:
        for sg in (1, -1):
            for e in (e1, e2, (e1 + e2) / math.sqrt(2), (e1 - e2) / math.sqrt(2)):
                q = p + sg * (r ** pw) * e
                out.append(tuple(q / np.linalg.norm(q)))
    return out


def sigma_samples(eid, n=24):
    f = sigma_form(eid)
    if f is None:
        return np.zeros((0, 3))
    S = sphere_zero_samples(f, 500, 500)
    rng = np.random.default_rng(SEED)
    return thin_points(S, n, rng)


def is_new(mins, w, tol=mp.mpf('1e-14')):
    for t in mins:
        if nrm([w[i] - t[0][i] for i in range(3)]) < tol:
            return False
    return True


def find_all(P, r, seeds, maxit=400, tol_new=mp.mpf('1e-14')):
    """список локальных минимумов с U<0 на S_r: [(w, U, Ht, e)], по возрастанию U"""
    res = []
    for s in seeds:
        try:
            w, U, gt, Ht, e, ok = newton_min(P, mpv(s), r, maxit=maxit)
        except (ZeroDivisionError, ValueError):
            continue
        if ok and U < 0 and is_new(res, w, tol_new):
            res.append((w, U, Ht, e))
    res.sort(key=lambda t: t[1])
    return res


def eigdirs(Ht, e):
    a, b, d = Ht[0][0], Ht[0][1], Ht[1][1]
    psi = mp.atan2(2 * b, a - d) / 2
    c, s = mp.cos(psi), mp.sin(psi)
    v1 = [c * e[0][i] + s * e[1][i] for i in range(3)]
    v2 = [-s * e[0][i] + c * e[1][i] for i in range(3)]
    l1 = c * c * a + 2 * c * s * b + s * s * d
    l2 = s * s * a - 2 * c * s * b + c * c * d
    return [(l1, v1), (l2, v2)]


# --------------------------------------------------------------------- профильные ширины
def point_on(w0, e1, e2, a, b):
    return unit([w0[i] + a * e1[i] + b * e2[i] for i in range(3)])


def inner_min(P, r, w0, e1, e2, a, b0, step0):
    """минимум F(a, b) = U(r pt(a,b)) по b (1D), старт b0, начальный шаг step0.  Возвращает (b, U)."""
    f = lambda b: P.val([r * c for c in point_on(w0, e1, e2, a, b)])
    b = mp.mpf(b0)
    fb = f(b)
    h = mp.mpf(step0)
    # поиск по лучу: шаги в обе стороны с адаптацией (устойчивый 1D спуск без производных)
    for _ in range(400):
        improved = False
        for sg in (1, -1):
            f2 = f(b + sg * h)
            if f2 < fb:
                # растягиваем в том же направлении
                b, fb = b + sg * h, f2
                h *= mp.mpf('1.6')
                improved = True
                break
        if not improved:
            h /= mp.mpf(3)
            if h < mp.mpf(10) ** (-(DPS // 2 + 4)) * max(abs(b), mp.mpf('1e-30')):
                break
        if h < mp.mpf(10) ** (-50):
            break
    return b, fb


def profile_width(P, r, w0, e1, e2, m, theta=mp.mpf('0.5'), sign=1, a_start=None, amax=1.0):
    """угловая ширина профиля: наименьшее a>0 (в направлении sign*e1), при котором min_b U(r pt(a,b)) = m (1-theta).
    Профильный (по перпендикуляру e2) минимум следует за изогнутым дном."""
    target = m * (1 - theta)
    a = mp.mpf(a_start) if a_start else mp.mpf(os.environ.get('WIDTH_A0', '1e-14'))
    gfac = mp.mpf(os.environ.get('WIDTH_GROW', '1.35'))
    b = mp.mpf(0)
    prev_a, prev_b = mp.mpf(0), mp.mpf(0)
    lo = mp.mpf(0)
    hi = None
    n = 0
    while True:
        b_pred = b
        bn, Un = inner_min(P, r, w0, e1, e2, sign * a, b_pred, max(abs(b) * mp.mpf('0.05'), a * a, mp.mpf('1e-30')))
        if Un >= target:
            hi = a
            break
        lo, b = a, bn
        a *= gfac
        n += 1
        if a > amax or n > 600:
            return None
    for _ in range(40):
        mid = (lo + hi) / 2
        bn, Un = inner_min(P, r, w0, e1, e2, sign * mid, b, max(abs(b) * mp.mpf('0.05'), mid * mid, mp.mpf('1e-30')))
        if Un < target:
            lo, b = mid, bn
        else:
            hi = mid
    return (lo + hi) / 2


def scaled_profile(P, r, w0, e1, e2, m, A1, A2, ng=5, span=2):
    """F(s1,s2)=U(r pt(s1 A1, s2 A2))/|m| на сетке s_i in {-span..span} (ng точек): список списков"""
    vals = []
    for i in range(ng):
        s1 = -span + 2 * span * mp.mpf(i) / (ng - 1)
        row = []
        for j in range(ng):
            s2 = -span + 2 * span * mp.mpf(j) / (ng - 1)
            pt = point_on(w0, e1, e2, s1 * A1, s2 * A2)
            row.append(P.val([r * c for c in pt]) / abs(m))
        vals.append(row)
    return vals
