import numpy as np
rng = np.random.default_rng(1)
SQ2 = np.sqrt(2.0)
KAP, KAPP, ALPHA = 0.01, 0.02, 0.5

def U(q):
    x,y,z = q[...,0],q[...,1],q[...,2]
    Q = x*x+y*y-z*z
    return Q*Q + z**5*x + z**4*x*y + 0.5*z**6
def gradU(q):
    x,y,z = q[...,0],q[...,1],q[...,2]
    Q = x*x+y*y-z*z
    gx = 4*x*Q + z**5 + z**4*y
    gy = 4*y*Q + z**4*x
    gz = -4*z*Q + 5*z**4*x + 4*z**3*x*y + 3*z**5
    return np.stack([gx,gy,gz],axis=-1)
def V_upper(q):
    x,y,z = q[...,0],q[...,1],q[...,2]
    rho = np.sqrt(x*x+y*y); c = x/rho; sn = y/rho
    s = (rho+z)/SQ2; d = (rho-z)/SQ2
    n = np.stack([c/SQ2, sn/SQ2, -np.ones_like(c)/SQ2],axis=-1)   # unit normal to the cone
    rot = np.stack([-y, x, np.zeros_like(x)],axis=-1)              # coordinate field d/dphi
    g = gradU(q)
    dU_dd = np.sum(g*n,axis=-1); dU_dphi = np.sum(g*rot,axis=-1)
    E = q + d[...,None]*n                                          # = s e_s + 2 d n
    return E/6 - KAP*(dU_dd/s**2)[...,None]*n - KAPP*(dU_dphi/s**6)[...,None]*rot
def V(q):   # upper horn: z>0 ; lower horn via central symmetry V(q) = -V_upper(-q)
    q = np.atleast_2d(q); out = np.empty_like(q)
    up = q[:,2] > 0
    out[up] = V_upper(q[up]); out[~up] = -V_upper(-q[~up])
    return out
def jac(fun, q, h):
    J = np.empty((q.shape[0],3,3))
    for k in range(3):
        e = np.zeros(3); e[k] = h
        J[:,:,k] = (fun(q+e) - fun(q-e))/(2*h)
    return J

def sample_horn(r, N):
    # random points on the sphere of radius r with U<0 (rejection in a thin band near both cones)
    pts = []
    while sum(len(p) for p in pts) < N:
        M = 400000
        phi = rng.uniform(0, 2*np.pi, M)
        sgn = rng.choice([-1,1], M)
        s = r*np.ones(M); eta = rng.uniform(-0.25, 0.25, M); d = s**2*eta
        rho = (s+d)/SQ2; zz = (s-d)/SQ2*sgn
        q = np.stack([rho*np.cos(phi), rho*np.sin(phi), zz],axis=-1)
        q = q * (r/np.linalg.norm(q,axis=1))[:,None]
        u = U(q)
        pts.append(q[u<0])
    return np.concatenate(pts)[:N]

print("kappa=%g kappa'=%g alpha=%g" % (KAP,KAPP,ALPHA))
for r in [0.5, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005]:
    q = sample_horn(r, 20000)
    u = U(q); g = gradU(q); v = V(q)
    ratio = np.sum(g*v,axis=1)/u            # need >= alpha  (since U<0)
    J = jac(V, q, 1e-7*r)
    S = 0.5*(J + np.transpose(J,(0,2,1)))
    lmin = np.linalg.eigvalsh(S)[:,0]
    # also: max of |eta| = |d|/s^2 among sampled negative points (upper ones)
    up = q[:,2]>0; qq = q[up]; rho = np.hypot(qq[:,0],qq[:,1]); ss=(rho+qq[:,2])/SQ2; dd=(rho-qq[:,2])/SQ2
    print("r=%-6g  min <gradU,V>/U = %.4f   min eig Sym DV = %.4f   max|V|/r = %.3f   max|d|/s^2 = %.3f" %
          (r, ratio.min(), lmin.min(), np.linalg.norm(v,axis=1).max()/r, np.abs(dd/ss**2).max()))
