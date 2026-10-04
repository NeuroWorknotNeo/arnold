# Batch integration of negative-energy trajectories of q'' = -grad U for Example 13.
import numpy as np, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from numeric_check import U, gradU, V, sample_horn, ALPHA
rng = np.random.default_rng(7)
R = 0.3
def run(r0, N):
    q = sample_horn(r0, N)
    u0 = U(q)
    dirn = rng.normal(size=(N,3)); dirn /= np.linalg.norm(dirn,axis=1)[:,None]
    p = dirn*np.sqrt(rng.uniform(0,0.9,N)*np.abs(u0)*2)[:,None]   # H in (U(q0), 0.1 U(q0))
    h = U(q) + 0.5*np.sum(p*p,1)
    t = np.zeros(N); alive = np.ones(N,bool); tesc = np.full(N,np.nan)
    F = np.sum(p*V(q),1); Fstart = F.copy(); rate_min = np.full(N,np.inf)
    Herr = np.zeros(N); last_t = t.copy(); last_F = F.copy(); step=0
    while alive.any():
        idx = np.where(alive)[0]
        qq, pp = q[idx], p[idx]
        dt = (0.004/np.linalg.norm(qq,axis=1))[:,None]     # ~1/100 of transverse period
        f = lambda Q: -gradU(Q)
        k1q,k1p = pp, f(qq); k2q,k2p = pp+dt/2*k1p, f(qq+dt/2*k1q)
        k3q,k3p = pp+dt/2*k2p, f(qq+dt/2*k2q); k4q,k4p = pp+dt*k3p, f(qq+dt*k3q)
        q[idx] = qq + dt/6*(k1q+2*k2q+2*k3q+k4q); p[idx] = pp + dt/6*(k1p+2*k2p+2*k3p+k4p)
        t[idx] += dt[:,0]; step += 1
        if step % 50 == 0:
            Fn = np.sum(p[idx]*V(q[idx]),1)
            rate_min[idx] = np.minimum(rate_min[idx], (Fn-last_F[idx])/(t[idx]-last_t[idx]))
            last_F[idx], last_t[idx] = Fn, t[idx]
            Herr[idx] = np.maximum(Herr[idx], np.abs(U(q[idx])+0.5*np.sum(p[idx]**2,1)-h[idx])/np.abs(h[idx]))
        out = idx[np.linalg.norm(q[idx],axis=1) >= R]
        tesc[out] = t[out]; alive[out] = False
        if step > 30_000_000: break
    return h, tesc, rate_min/(ALPHA*np.abs(h)), Herr
for r0 in [0.02, 0.01]:
    h, tesc, rr, Herr = run(r0, 100)
    print("r0=%-5g N=%d escaped=%d  t_esc in [%.3g, %.3g]   min (dF/dt)/(alpha|h|) = %.2f   max rel. energy drift %.1e"
          % (r0, len(h), np.isfinite(tesc).sum(), np.nanmin(tesc), np.nanmax(tesc), np.nanmin(rr), Herr.max()), flush=True)
