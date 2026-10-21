"""R26: full-model finite-difference check of the (A5) threshold found at leading order.

For p = 2, 3: take kappa = 0.8 kappa_crit and 1.25 kappa_crit (kappa_crit from leading_order_edge.out),
the worst point (theta*, k*) of the leading-order formula (edge e = 0), place the point exactly on the
edge in the full model (theta solving F(s^1/2, theta, 0) + a0 = delta - k*), and compute
min over the direction of v_perp of r = (rho/lambda) Xi/(delta rho^beta) by finite differences (model.Xi).
Also kappa = kappa(6.6) at the same point.
"""
import mpmath as mp
from model import build
import scan_A5 as S
from leading_order_edge import rmin as rmin_lo

mp.mp.dps = 90


def edge_theta(M, s, target, sign):
    lo, hi = mp.mpf(0), mp.mpf('0.9')
    for _ in range(90):
        mid = (lo + hi) / 2
        if S.Fn(M, s, sign * mid, mp.mpf(0))[0] < target:
            lo = mid
        else:
            hi = mid
    return sign * (lo + hi) / 2


for p, delta, kc in [(2, 1e-6, 0.005442), (3, 1e-7, 0.0002346)]:
    M = build(p)
    s = mp.mpf('1e-18')
    kp = float(S.kappa_proof(M, p, mp.mpf(delta)))
    for kap in (0.8 * kc, 1.25 * kc, kp):
        r_lo, (th_lo, kfrac, lf) = rmin_lo(p, delta, kap, nk=200, nl=40)
        k = mp.mpf(kfrac) * mp.mpf(delta)
        sign = 1 if th_lo >= 0 else -1
        th = edge_theta(M, s, mp.mpf(delta) - k, sign)
        samples, Kn = S.r_values(M, s, th, mp.mpf(0), mp.mpf(kap), mp.mpf(delta))
        rfd, res, _ = S.trig_min(samples)
        print(f'p={p} delta={delta:.0e} kappa={kap:.4g} ({kap/kc:.3g} kappa_crit): leading-order min r = {r_lo:.4g} '
              f'at theta={th_lo:.4g}, K/(delta rho^b)={kfrac:.3g}; full model (s=1e-18, same K, e=0, theta={mp.nstr(th,5)}): '
              f'min_alpha r = {rfd:.4g} (fit residual {res:.1e})')
