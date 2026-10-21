"""R26: leading-order (s -> 0) formula for r = (rho/lambda) Xi/(delta rho^beta) on the model of model.py,
used (i) to cross-check the finite-difference scan scan_A5.py, (ii) to find the critical kappa
above which (A5) fails, as a function of delta, for p = 1, 2, 3.

At s -> 0 (eps, psi, eta^*-terms -> 0), for (theta, e) with Lambda + 4e^2 = delta - k (K = k rho^beta),
v_perp = rho^{beta/2}(w_o, t, u) in the frame (omega, T, n), w_o = kappa theta t, (1 + kappa^2 theta^2) t^2 + u^2 = 2k:
  main  = beta k + kappa theta Lambda' + c h_n e^2          (h_n = 8 constant, c = 3/2)
  T1    = j kappa theta sqrt((a0 - delta) h / 2) t          (h = 1 + kappa^2 theta^2)
  T2    = -sqrt(2 (a0 - delta)/h) * < (w_o, t, u), sD_YY >,  sD_YY = (-k^2th^2, -kappa(1-kappa) theta, kappa^2 theta^2)
  T3    = (1 - kappa) t^2 + kappa theta w_o t
(formulas (1.3) [007], (6.4), (6.5), (6.7) with eps = psi = 0, k_g = 1).
"""
import numpy as np

j, c, hn = 5, 1.5, 8.0
a = 2**-2.5


def Lam(th, p):
    return a * (1 - np.cos(np.sqrt(2) * th))**p


def dLam(th, p):
    x = np.sqrt(2) * th
    return a * p * (1 - np.cos(x))**(p - 1) * np.sqrt(2) * np.sin(x)


def rmin(p, delta, kappa, a0=a, nth=401, nk=400, nal=721):
    best = np.inf
    arg = None
    thmax = (delta / a)**(1 / (2 * p)) * 1.3
    ths = np.linspace(-thmax, thmax, nth)
    al = np.linspace(0, 2 * np.pi, nal)
    for th in ths:
        L = Lam(th, p)
        if L > delta:
            continue
        ks = np.concatenate([[0.0], np.geomspace(1e-12 * delta, delta - L, nk)])
        for k in ks:
            e2 = (delta - k - L) / 4.0
            if e2 < 0:
                continue
            h = 1 + kappa**2 * th**2
            t = np.sqrt(2 * k / h) * np.cos(al)
            u = np.sqrt(2 * k) * np.sin(al)
            wo = kappa * th * t
            main = j * k + kappa * th * dLam(th, p) + c * hn * e2
            T1 = j * kappa * th * np.sqrt((a0 - delta) * h / 2) * t
            sD = (-kappa**2 * th**2, -kappa * (1 - kappa) * th, kappa**2 * th**2)
            T2 = -np.sqrt(2 * (a0 - delta) / h) * (wo * sD[0] + t * sD[1] + u * sD[2])
            T3 = (1 - kappa) * t**2 + kappa * th * wo * t
            r = (main + T1 + T2 + T3) / delta
            i = np.argmin(r)
            if r[i] < best:
                best = r[i]
                arg = (th, k / delta, al[i])
    return best, arg


def kappa_proof(p, delta, a0=a):
    CG = 15 / 8 * np.sqrt(3) * j + 4
    Rt2 = (8 * delta / a)**(1 / p)
    return min(0.5, j * delta / (2 * CG**2 * a0 * Rt2))


if __name__ == '__main__':
    print('Comparison configs (as in scan_A5.out):')
    for (p, d, k) in [(2, 1e-4, 'proof'), (2, 1e-4, 0.5), (2, 1e-4, 0.05), (2, 1e-6, 'proof'), (2, 1e-6, 0.5),
                      (2, 1e-6, 0.01), (3, 1e-5, 'proof'), (3, 1e-5, 0.5), (3, 1e-5, 0.005), (3, 1e-7, 'proof'),
                      (3, 1e-7, 0.5), (1, 1e-4, 0.5), (1, 1e-6, 0.5)]:
        kap = kappa_proof(p, d) if k == 'proof' else k
        r, arg = rmin(p, d, kap, nth=201, nk=200)
        print(f'p={p} delta={d:.0e} kappa={kap:.4g}: min r = {r:.6g}, r/kappa = {r/kap:.4g}, at theta={arg[0]:.4g}, '
              f'K/(delta rho^b)={arg[1]:.3g}')
    print()
    print('Critical kappa (largest kappa in a geometric grid with min r > 0) vs delta:')
    for p in (1, 2, 3):
        for d in (1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8):
            if (8 * d / a)**(1 / (2 * p)) > 1.0:
                continue
            kgrid = np.geomspace(1e-5, 0.5, 60)
            kc = 0.0
            for kap in kgrid:
                r, _ = rmin(p, d, kap, nth=121, nk=120, nal=361)
                if r > 0:
                    kc = kap
                else:
                    break
            print(f'p={p} delta={d:.0e}: kappa_crit ~ {kc:.3g} (proof kappa {kappa_proof(p, d):.3g}); '
                  f'kappa_crit/delta^(1-1/p) = {kc / d**(1 - 1 / p):.3g}')
