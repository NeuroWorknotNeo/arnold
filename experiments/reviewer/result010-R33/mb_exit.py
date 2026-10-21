# R33 [Experiment]: strict exit (A5) for the field Y_kappa of Theorem Mb on the model
#   U = z^2 + rho^j G(theta),  G = -1 + b sin^{2p}(theta),  rho = sqrt(x^2+y^2)
# (Sigma_0 = great circle z=0, k_g=0, eta*=0, m=2, c=j/2, a0=1, h_n=2, F = G + e^2 exactly, chi=0).
# Xi = d/dt (V - delta rho^j) along the flow, computed by direct differentiation (independent of (1.3)).
# Exit set (A5): Q(theta,e)=Lambda+e^2 <= delta (= closure of D here), E=0, p<0, V=delta rho^j;
# parametrised by qh=Q/delta in [0,1], psi (split of Q between Lambda and e^2), phi (direction of v_perp).
import sys
import numpy as np, sympy as sp
from scipy.optimize import brentq, minimize

def build(j, p, bcoef):
    X, Yv, Z, vx, vy, vz, kap, dl = sp.symbols('x y z vx vy vz kappa delta', real=True)
    r2 = X**2 + Yv**2
    U = Z**2 - r2**sp.Rational(j, 2) + bcoef * r2**sp.Rational(j - 2 * p, 2) * Yv**(2 * p)
    s = sp.sqrt(r2); th = sp.atan2(Yv, X)
    om = sp.Matrix([X / s, Yv / s, 0]); el = sp.Matrix([-Yv / s, X / s, 0])
    Yf = om - kap * th * el
    v = sp.Matrix([vx, vy, vz]); q = sp.Matrix([X, Yv, Z])
    pp = v.dot(Yf); h = 1 + kap**2 * th**2
    V = v.dot(v) / 2 - pp**2 / (2 * h) + U + s**j
    gU = sp.Matrix([sp.diff(U, w) for w in q])
    Xi = sum(sp.diff(V, q[i]) * v[i] for i in range(3)) - sum(sp.diff(V, v[i]) * gU[i] for i in range(3)) \
         - j * dl * s**(j - 1) * sum(sp.diff(s, q[i]) * v[i] for i in range(3))
    return sp.lambdify((X, Yv, Z, vx, vy, vz, kap, dl), Xi, 'numpy')

def xi_hat(f, j, p, bcoef, kap, dl, qh, psi, sg, phi, s=0.4):
    c = j / 2
    Lam = qh * dl * np.cos(psi)**2
    e = np.sqrt(qh * dl) * np.sin(psi)
    th = sg * np.arcsin(np.minimum(1.0, (Lam / bcoef)**(1.0 / (2 * p))))
    K = s**j * dl * (1 - qh)
    ct, st = np.cos(th), np.sin(th)
    Y = np.stack([ct + kap * th * st, st - kap * th * ct, 0 * th])
    h = 1 + kap**2 * th**2
    lam = np.sqrt(2 * s**j * (1 - dl) / h)
    mh = np.stack([kap * th * ct - st, kap * th * st + ct, 0 * th]) / np.sqrt(h)
    n = np.stack([0 * th, 0 * th, 1 + 0 * th])
    vp = np.sqrt(2 * K) * (np.cos(phi) * n + np.sin(phi) * mh)
    v = -lam * Y + vp
    qx = np.stack([s * ct, s * st, s**c * e])
    Xi = f(qx[0], qx[1], qx[2], v[0], v[1], v[2], kap, dl)
    return s / lam * Xi / (dl * s**j)

QH = np.concatenate([np.linspace(0, 0.9, 10), 1 - np.geomspace(1e-1, 1e-6, 16), [1.0]])
def grid_min(f, j, p, bcoef, kap, dl, npsi=181, nphi=72):
    qh, psi, sg, phi = np.meshgrid(QH, np.linspace(0, 2 * np.pi, npsi), [1.0, -1.0],
                                   np.linspace(0, 2 * np.pi, nphi, endpoint=False), indexing='ij')
    val = xi_hat(f, j, p, bcoef, kap, dl, qh, psi, sg, phi)
    i = np.unravel_index(np.nanargmin(val), val.shape)
    return float(val[i]), (qh[i], psi[i], sg[i], phi[i]), int(np.isnan(val).sum())

def refined_min(f, j, p, bcoef, kap, dl):
    m, (q0, ps0, sg0, ph0), nn = grid_min(f, j, p, bcoef, kap, dl)
    fun = lambda z: float(xi_hat(f, j, p, bcoef, kap, dl, min(1.0, max(0.0, z[0])), z[1], sg0, z[2]))
    r = minimize(fun, [q0, ps0, ph0], method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-14, maxiter=4000))
    return min(m, r.fun), nn

def kappa04(j, p, a, a0, dl):
    CG = 15 * np.sqrt(3) / 8 * j + 4
    return min(0.5, j / (2 * CG**2 * a0) * (a / 8)**(1 / p) * dl**(1 - 1 / p))

if __name__ == '__main__':
    for (j, p) in [(4, 1), (6, 2), (8, 3), (10, 4)]:
        bcoef = 1.0
        f = build(j, p, bcoef)
        print(f'--- j={j}, p={p}, b=a={bcoef}')
        k0 = kappa04(j, p, bcoef, 1.0, 1e-2)
        print('  scale check:', xi_hat(f, j, p, bcoef, k0, 1e-2, 0.7, 0.3, 1.0, 1.0, s=0.4),
              xi_hat(f, j, p, bcoef, k0, 1e-2, 0.7, 0.3, 1.0, 1.0, s=0.05))
        for dl in [1e-2, 1e-3, 1e-4, 1e-5]:
            k = kappa04(j, p, bcoef, 1.0, dl)
            m, nn = refined_min(f, j, p, bcoef, k, dl)
            gm = lambda kk: grid_min(f, j, p, bcoef, kk, dl, npsi=121, nphi=48)[0]
            ks = np.geomspace(1e-6, 0.5, 30)
            vals = np.array([gm(kk) for kk in ks])
            kc = None
            for i in range(len(ks) - 1):
                if vals[i] > 0 and vals[i + 1] <= 0:
                    kc = brentq(gm, ks[i], ks[i + 1], xtol=1e-4 * ks[i]); break
            nbad = int(np.sum(vals[ks <= (kc if kc else 1)] <= 0)) if kc else int(np.sum(vals <= 0))
            print(f'  delta={dl:.0e}: kappa(0.4)={k:.3e}  min xi_hat={m:.4e}  kappa/2={k/2:.3e}  '
                  f'min>=kappa/2: {m >= k/2}  min/kappa={m/k:.3f}  NaN={nn}  '
                  f'kappa_crit={"none<=0.5" if kc is None else f"{kc:.3e}"}'
                  + ('' if kc is None else f'  kc/delta^(1-1/p)={kc/dl**(1-1/p):.3f}  kc/kappa04={kc/k:.0f}')
                  + f'  #neg below kc={nbad}')
            sys.stdout.flush()
