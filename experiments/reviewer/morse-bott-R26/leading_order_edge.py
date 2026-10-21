"""R26: critical kappa for (A5) at leading order, with points parametrized near the edge e = 0.

Same formula as leading_order.py, but the points of the (A5) set are parametrized by
k = K/(rho^beta) in [0, delta] and lf in (0, 1]: Lambda(theta) = lf (delta - k), 4 e^2 = (1 - lf)(delta - k),
theta = +-Lambda^{-1}(...), so that the edge e = 0 (lf = 1), where the Euler margin is smallest, is hit exactly.
"""
import numpy as np
from scipy.optimize import brentq
from leading_order import Lam, dLam, kappa_proof, j, c, hn, a


def r_point(p, delta, kappa, th, k, e2, al, a0=a):
    h = 1 + kappa**2 * th**2
    t = np.sqrt(2 * k / h) * np.cos(al)
    u = np.sqrt(2 * k) * np.sin(al)
    wo = kappa * th * t
    main = j * k + kappa * th * dLam(th, p) + c * hn * e2
    T1 = j * kappa * th * np.sqrt((a0 - delta) * h / 2) * t
    T2 = -np.sqrt(2 * (a0 - delta) / h) * (wo * (-kappa**2 * th**2) + t * (-kappa * (1 - kappa) * th) + u * kappa**2 * th**2)
    T3 = (1 - kappa) * t**2 + kappa * th * wo * t
    return (main + T1 + T2 + T3) / delta


def rmin(p, delta, kappa, nk=300, nl=60, nal=361):
    al = np.linspace(0, 2 * np.pi, nal)
    best = np.inf
    arg = None
    ks = np.concatenate([[0.0], np.geomspace(1e-14, 1 - 1e-9, nk)]) * delta
    lfs = np.concatenate([[1.0], 1 - np.geomspace(1e-10, 1 - 1e-6, nl)])
    for k in ks:
        for lf in lfs:
            L = lf * (delta - k)
            th = brentq(lambda x: Lam(x, p) - L, 0, 1.0) if L > 0 else 0.0
            e2 = (1 - lf) * (delta - k) / 4
            for sg in (1, -1):
                r = r_point(p, delta, kappa, sg * th, k, e2, al)
                i = np.argmin(r)
                if r[i] < best:
                    best, arg = r[i], (sg * th, k / delta, lf)
    return best, arg


if __name__ == '__main__':
    for p in (1, 2, 3):
        for d in (1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-10):
            lo, hi = 1e-9, 0.5
            if rmin(p, d, hi, nk=120, nl=30)[0] > 0:
                print(f'p={p} delta={d:.0e}: (A5) holds at leading order for all kappa <= 0.5')
                continue
            for _ in range(40):
                mid = np.sqrt(lo * hi)
                if rmin(p, d, mid, nk=120, nl=30)[0] > 0:
                    lo = mid
                else:
                    hi = mid
            kp = kappa_proof(p, d)
            print(f'p={p} delta={d:.0e}: kappa_crit = {lo:.4g}; kappa_crit/delta^(1-1/p) = {lo / d**(1 - 1 / p):.4g}; '
                  f'proof kappa(6.6) = {kp:.3g} (ratio {lo / kp:.3g})')
