"""[Эксперимент] Построение функции Delta из статьи Паламодова (ФАН 11:4, 1977, с. 48-50)
на одной окружности |x| = r и проверка неравенства III леммы 7:
        lambda_H(r) <= Delta'_alpha <= lambda_B(r) = eta1.

Для каждой дуги окружности внутри U^- (угол поднят на интервал (a, b), a < b):
  phi   -- направленный угол от -x к u'(x);
  delta -- как на с. 48;
  alpha_i -- точки, где delta != 0 и delta'_alpha пересекает lambda_B или lambda_H
             (решения уравнений (11) внутри U^-);
  Delta_i -- касательные куски (с. 49);
  Delta -- max / min по Delta_i, i >= 0 (с. 50).
Константы: c r^d := K * sup(|phi| - pi/2) по дуге (лемма 3), gamma1, eta1 -- фиксированы.
Сообщаем, где Delta'_alpha выходит из [lambda_H, lambda_B], и минимум
mu = min eig sym(v') по формуле с. 53 при r Delta'_r := 0 (только угловая часть;
если уже она отрицательна, условие (3) нарушено).
"Исправленная" Delta_fix: к семейству alpha_i добавлены концы дуги a, b
(касательные с наклоном lambda_H или lambda_B в нужную сторону).
Численная иллюстрация, не доказательство.
"""
import sys
import numpy as np
from scipy.optimize import brentq

EXAMPLES = {
    # name: (u, grad u)
    "u1=-x2(x1-x2^2)": (lambda x1, x2: -x2 * (x1 - x2**2),
                        lambda x1, x2: (-x2, -x1 + 3 * x2**2)),
    "u2=x1^5-(x2-x1^2)^2": (lambda x1, x2: x1**5 - (x2 - x1**2) ** 2,
                            lambda x1, x2: (5 * x1**4 + 4 * x1 * (x2 - x1**2), -2 * (x2 - x1**2))),
}


def make(name):
    u, g = EXAMPLES[name]

    def phi(alpha, r):
        x1, x2 = r * np.cos(alpha), r * np.sin(alpha)
        g1, g2 = g(x1, x2)
        d = np.arctan2(g2, g1) - np.arctan2(-x2, -x1)
        return (d + np.pi) % (2 * np.pi) - np.pi

    def uu(alpha, r):
        return u(r * np.cos(alpha), r * np.sin(alpha))
    return uu, phi


def arcs(uu, r, n=20000000):
    th = np.linspace(0, 2 * np.pi, n, endpoint=False)
    s = uu(th, r) < 0
    if s.all():
        return [(0.0, 2 * np.pi, True)]
    res = []
    # rotate so that index 0 is outside U^-
    k0 = np.where(~s)[0][0]
    idx = (np.arange(n) + k0) % n
    ss = s[idx]
    tt = th[idx] + np.where(idx < k0, 2 * np.pi, 0.0)
    i = 0
    while i < n:
        if ss[i]:
            j = i
            while j + 1 < n and ss[j + 1]:
                j += 1
            f = lambda t: uu(t, r)
            a = brentq(f, tt[i - 1], tt[i])
            b = brentq(f, tt[j], tt[j + 1] if j + 1 < n else tt[0] + 2 * np.pi)
            res.append((a, b, False))
            i = j + 1
        else:
            i += 1
    return res


def delta_of(p):
    return np.where(p >= np.pi / 2, p - np.pi / 2, np.where(p <= -np.pi / 2, p + np.pi / 2, 0.0))


def tangent_piece(al, ai, di, lam):
    """Delta_i: the line di + lam (alpha - ai) on the segment between ai and ai - di/lam."""
    end = ai - di / lam
    lo, hi = min(ai, end), max(ai, end)
    on = (al >= lo) & (al <= hi)
    return np.where(on, di + lam * (al - ai), 0.0)


def combine(de, pieces):
    allp = [de] + pieces
    M = np.max(allp, axis=0)
    m = np.min(allp, axis=0)
    return np.where(M > 0, M, np.where(m < 0, m, 0.0))


def run(name, r, K=1.0, gamma1=0.5, eta1=2.0, n=400001):
    uu, phi = make(name)
    print(f"== {name},  r = {r:g},  K = {K}, gamma1 = {gamma1}, eta1 = {eta1}")
    for (a, b, full) in arcs(uu, r):
        eps = 1e-9 * (b - a)
        al = np.linspace(a + eps, b - eps, n)
        ph = phi(al, r)
        de = delta_of(ph)
        sup_ex = float(np.max(np.abs(ph) - np.pi / 2))
        crd = K * max(sup_ex, 0.0)
        if crd == 0:
            print(f"   arc ({a:.6f}, {b:.6f}): |phi| <= pi/2 everywhere -> v = x (simple case)")
            continue
        lamH, lamB = -2 * crd / gamma1, eta1
        dd = np.gradient(de, al)
        nz = (de != 0)
        nz2 = nz.copy()
        nz2[1:] &= nz[:-1]
        nz2[:-1] &= nz[1:]
        pieces = []
        sols = []
        for lam in (lamB, lamH):
            f = dd - lam
            ch = np.where(nz2[:-1] & nz2[1:] & (np.sign(f[:-1]) != np.sign(f[1:])))[0]
            for k in ch:
                ai = al[k]
                di = de[k]
                sols.append((ai, lam, di))
                pieces.append(tangent_piece(al, ai, di, lam))
        D = combine(de, pieces)
        dD = np.gradient(D, al)
        # ignore isolated kinks: look at points where both neighbours have the same slope-ish
        bad = (dD < lamH - 1e-9) | (dD > lamB + 1e-9)
        # angular part of mu (formula p.53 with r Delta'_r = 0)
        mu = np.cos(D) + 0.5 * dD * np.cos(D) - 0.5 * np.abs(dD)
        print(f"   arc ({a:.6f}, {b:.6f}) width {b - a:.4f}: sup(|phi|-pi/2) = {sup_ex:.3e},"
              f" lambda_H = {lamH:.3e}, lambda_B = {lamB}")
        print(f"     phi at ends: {ph[0]:+.6f}, {ph[-1]:+.6f};  delta at ends: {de[0]:+.3e}, {de[-1]:+.3e}")
        print(f"     solutions of (11) with delta != 0: {len(sols)}")
        if bad.any():
            ib = np.where(bad)[0]
            print(f"     Delta'_alpha outside [lambda_H, lambda_B] on {bad.sum()} of {n} grid points;"
                  f" alpha range of violations: [{al[ib[0]]:.6f}, {al[ib[-1]]:.6f}],"
                  f" Delta' there in [{dD[ib].min():.4f}, {dD[ib].max():.4f}]")
            print(f"     min of angular mu over the arc: {mu.min():+.4f}")
        else:
            print(f"     III holds on this circle; min angular mu = {mu.min():+.4f}")
        # corrected construction: add tangents from the arc ends
        extra = []
        for (ae, side) in ((a, "left"), (b, "right")):
            pe = phi(np.array([ae + (eps if side == "left" else -eps)]), r)[0]
            dE = float(delta_of(np.array([pe]))[0])
            if dE == 0:
                continue
            for lam in (lamB, lamH):
                end = ae - dE / lam
                # keep only tangents that point into the arc
                if (side == "left" and end > ae) or (side == "right" and end < ae):
                    extra.append(tangent_piece(al, ae, dE, lam))
        Dfix = combine(de, pieces + extra)
        dDf = np.gradient(Dfix, al)
        badf = (dDf < lamH - 1e-9) | (dDf > lamB + 1e-9)
        okI = np.all((Dfix >= ph - np.pi / 2 - 1e-12) & (Dfix <= ph + np.pi / 2 + 1e-12))
        muf = np.cos(Dfix) + 0.5 * dDf * np.cos(Dfix) - 0.5 * np.abs(dDf)
        print(f"     with end tangents: violations of III on {badf.sum()} points"
              f" (max |excess| {max(0, (lamH - dDf).max(), (dDf - lamB).max()):.2e}),"
              f" inequality I holds: {okI}, min angular mu = {muf.min():+.4f}")


if __name__ == "__main__":
    for name in EXAMPLES:
        for r in (1e-2, 1e-3, 1e-4):
            run(name, r)
    sys.stdout.flush()
