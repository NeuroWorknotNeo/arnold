"""R26: numerical check of the strict exit condition (A5) for Theorem Mb on the model of model.py.

For given (p, delta, kappa, s) sample points of the (A5) set of Theorem A [007]:
    q = Psi(s, theta, s^c e),  (theta, e) with F + a0 = delta - k  (k >= 0, i.e. W = (delta - k) rho^beta <= delta rho^beta),
    K_perp = k rho^beta,  v_perp = sqrt(2K)(cos al u1 + sin al u2),  u1, u2 an orthonormal basis of Y^perp,
    p = <v, Y> = -lambda h,  lambda^2 h/2 = A(rho) - delta rho^beta   (so E = 0 and V = delta rho^beta),
and compute r := (rho/lambda) Xi / (delta rho^beta), Xi = d/dt (V - delta rho^beta) along the flow,
by finite differences of V in Cartesian coordinates (model.Xi).  Xi is a trigonometric polynomial of
degree <= 2 in al (formula (1.2) [007] with p fixed), so 8 samples determine it exactly; the residual of
the fit is printed as a sanity check of the numerics.
Theorem Mb (with its choice kappa = kappa(delta) from (6.6) and sigma_* small) claims r >= kappa/2 > 0.

Usage: python scan_A5.py p delta kappa s [n_theta]
   kappa may be 'proof' (value (6.6)) or a number.
"""
import sys
import time
import mpmath as mp
from model import build, Psi, Yfield, dot, Xi, chart_inv

mp.mp.dps = 90
j, m = 5, 4
c = mp.mpf(j - m + 2) / 2


def kappa_proof(M, p, delta):
    CG = mp.mpf(15) / 8 * mp.sqrt(3) * j + 4
    Rt2 = (8 * delta / M['a'])**(mp.mpf(1) / p)
    return min(mp.mpf(1) / 2, j * delta / (2 * CG**2 * M['a0'] * Rt2))


def Fn(M, s, th, e):
    q = Psi(M, s, th, s**c * e)
    return (M['U'](*q) + M['a0'] * s**j) / s**j, q


def solve_e(M, s, th, target, sign):
    f0, _ = Fn(M, s, th, mp.mpf(0))
    if f0 > target:
        return None
    lo, hi = mp.mpf(0), mp.mpf('0.5')
    if Fn(M, s, th, sign * hi)[0] < target:
        return None
    for _ in range(80):
        mid = (lo + hi) / 2
        if Fn(M, s, th, sign * mid)[0] < target:
            lo = mid
        else:
            hi = mid
    return sign * (lo + hi) / 2


def r_values(M, s, th, e, kappa, delta, nal=8):
    val, q = Fn(M, s, th, e)
    rho = s
    W = (val) * rho**j
    K = delta * rho**j - W
    if K < 0:
        K = mp.mpf(0)
    Y, _ = Yfield(M, q, kappa)
    h = dot(Y, Y)
    lam = mp.sqrt(2 * (M['a0'] * rho**j - delta * rho**j) / h)
    # orthonormal basis of Y^perp
    e1 = mp.matrix([1, 0, 0]) if abs(Y[0]) < 0.9 * mp.sqrt(h) else mp.matrix([0, 1, 0])
    Yu = Y / mp.sqrt(h)
    u1 = e1 - dot(e1, Yu) * Yu
    u1 = u1 / mp.sqrt(dot(u1, u1))
    u2 = mp.matrix([Yu[1] * u1[2] - Yu[2] * u1[1], Yu[2] * u1[0] - Yu[0] * u1[2], Yu[0] * u1[1] - Yu[1] * u1[0]])
    out = []
    for i in range(nal):
        al = 2 * mp.pi * i / nal
        vp = mp.sqrt(2 * K) * (mp.cos(al) * u1 + mp.sin(al) * u2)
        v = -lam * Y + vp
        E = dot(v, v) / 2 + M['U'](*q)
        xi = Xi(M, q, v, kappa, delta)
        out.append((al, rho / lam * xi / (delta * rho**j), E / (rho**j)))
    return out, K / (delta * rho**j)


def trig_min(samples):
    # fit a0 + a1 cos + b1 sin + a2 cos2 + b2 sin2 to 8 samples, minimize on a fine grid
    import numpy as np
    al = np.array([float(x[0]) for x in samples])
    y = np.array([float(x[1]) for x in samples])
    A = np.stack([np.ones_like(al), np.cos(al), np.sin(al), np.cos(2 * al), np.sin(2 * al)], 1)
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    res = np.max(np.abs(A @ coef - y))
    g = np.linspace(0, 2 * np.pi, 2001)
    Ag = np.stack([np.ones_like(g), np.cos(g), np.sin(g), np.cos(2 * g), np.sin(2 * g)], 1)
    yy = Ag @ coef
    return yy.min(), res, coef


def main():
    p = int(sys.argv[1])
    delta = mp.mpf(sys.argv[2])
    M = build(p)
    kap = kappa_proof(M, p, delta) if sys.argv[3] == 'proof' else mp.mpf(sys.argv[3])
    s = mp.mpf(sys.argv[4])
    nth = int(sys.argv[5]) if len(sys.argv) > 5 else 9
    Rt = (8 * delta / M['a'])**(mp.mpf(1) / (2 * p))
    Re = 4 * mp.sqrt(delta / 8)
    print(f'p={p} delta={mp.nstr(delta,3)} kappa={mp.nstr(kap,4)} (proof value {mp.nstr(kappa_proof(M,p,delta),4)}) '
          f's={mp.nstr(s,3)} R_theta={mp.nstr(Rt,4)} R_e={mp.nstr(Re,4)} a0={mp.nstr(M["a0"],4)}')
    t0 = time.time()
    worst = None
    rows = []
    fracs = [mp.mpf(x) for x in ('0', '1e-6', '1e-5', '1e-4', '3e-4', '1e-3', '3e-3', '1e-2', '3e-2', '0.1', '0.2', '0.5', '0.9')]
    thmax = (delta / M["a"])**(mp.mpf(1) / (2 * p)) * mp.mpf("1.15")
    ths = [thmax * (mp.mpf(i) / (nth - 1) * 2 - 1) for i in range(nth)]
    maxres = 0.0
    maxE = 0
    for th in ths:
        for fr in fracs:
            target = delta * (1 - fr)
            for sg in (1, -1):
                e = solve_e(M, s, th, target, sg)
                if e is None:
                    continue
                samples, Kn = r_values(M, s, th, e, kap, delta)
                rmin, res, coef = trig_min(samples)
                maxres = max(maxres, res)
                maxE = max(maxE, max(abs(x[2]) for x in samples))
                rows.append((float(th), float(e), float(Kn), rmin))
                if worst is None or rmin < worst[3]:
                    worst = (float(th), float(e), float(Kn), rmin)
                if fr == 0 and sg == -1:
                    pass
    rmins = [r[3] for r in rows]
    print(f'points: {len(rows)}, time {time.time()-t0:.0f}s, max fit residual {maxres:.2e}, max |E|/rho^j {mp.nstr(maxE,3)}')
    print(f'min r = {min(rmins):.6g}  at theta={worst[0]:.4g}, e={worst[1]:.4g}, K/(delta rho^b)={worst[2]:.3g}')
    print(f'kappa/2 = {float(kap)/2:.6g};  min r / kappa = {min(rmins)/float(kap):.4g};  '
          f'#(r<=0) = {sum(1 for r in rmins if r <= 0)}')
    # profile along theta at the most dangerous K-fraction
    byth = {}
    for r in rows:
        byth.setdefault(round(r[0], 6), []).append(r[3])
    print('min r over K,e for each theta:', ' '.join(f'{t:+.3f}:{min(v):.3g}' for t, v in sorted(byth.items())))


if __name__ == '__main__':
    main()
