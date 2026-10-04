"""Heuristic dynamic test for a potential U: start trajectories with H<0 near 0 (inside the
negative region found by local minimisation on small spheres) and record whether they leave the
ball of radius R. Cannot prove stability; can only show escape or long trapping."""
import numpy as np, sympy as sp, sys
from sieve import lam, lam_grad, lam_hess, sphere_minimize, SPH, x, y, z

def negative_starts(U, r, n=60, rng=np.random.default_rng(0)):
    f, g = lam(U), lam_grad(U)
    F = lambda W: f(r*W); G = lambda W: r*g(r*W)
    v = F(SPH); idx = np.argsort(v)[:400]
    W, val = sphere_minimize(F, G, SPH[idx], iters=300)
    W = W[val < 0]
    if len(W) == 0: return np.zeros((0,3))
    # jitter inside the negative region
    out = []
    for w in W:
        for _ in range(3):
            q = r*w*(1 + 0.02*rng.normal()); 
            if f(q[None])[0] < 0: out.append(q)
    out = np.array(out)
    return out[rng.permutation(len(out))[:n]]

def escape_test(U, r0, R=0.3, tmax_factor=50.0, rng=np.random.default_rng(1)):
    f, g, H = lam(U), lam_grad(U), lam_hess(U)
    q = negative_starts(U, r0)
    if len(q) == 0: return None
    u0 = f(q)
    dirn = rng.normal(size=q.shape); dirn /= np.linalg.norm(dirn, axis=1)[:, None]
    p = dirn*np.sqrt(rng.uniform(0, 0.9, len(q))*np.abs(u0)*2)[:, None]
    h = f(q) + 0.5*np.sum(p*p, 1)
    t = np.zeros(len(q)); alive = np.ones(len(q), bool); tesc = np.full(len(q), np.nan)
    # time scale: |q| / speed ~ |q| / sqrt(|h|)
    T = tmax_factor * r0 / np.sqrt(np.abs(h))
    steps = 0
    while alive.any() and steps < 400000:
        idx = np.where(alive)[0]; qq, pp = q[idx], p[idx]
        lam_max = np.max(np.abs(np.linalg.eigvalsh(H(qq))), axis=1)
        dt = np.minimum(0.05/np.sqrt(lam_max + 1e-300), 0.02*np.linalg.norm(qq, axis=1)/np.sqrt(np.abs(h[idx])))[:, None]
        F_ = lambda Q: -g(Q)
        k1q, k1p = pp, F_(qq); k2q, k2p = pp+dt/2*k1p, F_(qq+dt/2*k1q)
        k3q, k3p = pp+dt/2*k2p, F_(qq+dt/2*k2q); k4q, k4p = pp+dt*k3p, F_(qq+dt*k3q)
        q[idx] = qq + dt/6*(k1q+2*k2q+2*k3q+k4q); p[idx] = pp + dt/6*(k1p+2*k2p+2*k3p+k4p)
        t[idx] += dt[:, 0]; steps += 1
        out = idx[np.linalg.norm(q[idx], axis=1) >= R]; tesc[out] = t[out]; alive[out] = False
        timeout = idx[t[idx] > T[idx]]; alive[timeout] = False
    drift = np.max(np.abs(f(q) + 0.5*np.sum(p*p, 1) - h)/np.abs(h))
    return len(q), int(np.isfinite(tesc).sum()), np.nanmedian(tesc*np.sqrt(np.abs(h))/r0), drift

if __name__ == '__main__':
    U = sp.sympify(sys.argv[1], locals={'x': x, 'y': y, 'z': z})
    for r0 in (0.05, 0.03):
        print(r0, escape_test(U, r0))
