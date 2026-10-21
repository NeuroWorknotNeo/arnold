# R38: (i) eigenvalue bound for sym part of D(z xi0); (ii) f(u) bounds; (iii) theta_3 actual infimum on D_sigma,
# showing it is ~ -(3-e)(sqrt2-1)/2 on the arms (so lemma 2 [007] with -4 theta_3 cannot work).
import numpy as np
for e in [0.1, 0.5]:
    s = np.linspace(0, 1, 200001)
    a, b = s**2, (1-s)**2
    lam = (3-e)/2*((a+b) - np.sqrt(2*(a**2+b**2)))
    print(f"e={e}: min eig sym D(z xi0) = {lam.min():.7f}, bound -(3-e)(sqrt2-1)/2 = {-(3-e)*(np.sqrt(2)-1)/2:.7f}, argmin s={s[lam.argmin()]}")
    nrm = (3-e)*np.sqrt(2)*np.sqrt(a**2+b**2)
    print(f"   max norm D(z xi0) = {nrm.max():.5f} <= 3sqrt2={3*np.sqrt(2):.5f}")
    u = np.concatenate([np.linspace(4, 50, 100001), np.logspace(np.log10(50), 8, 2001)])
    f = ((u-2+e)*u**6 + 1 - (2-e)*u)/(1+u)
    print(f"   min over u>=4 of f(u)/(u^6+1) = {(f/(u**6+1)).min():.5f} (claimed >= 0.398)")
# (iii) actual inf of z<w,D_wY>/|w|^2 over w perp Y, at points of D_sigma
def field(x, y, z, e):
    t = -y; g = x*t/(x+t)
    zxi = np.array([(3-e)*g, -(3-e)*g]) - e*z**3*np.array([y, x])/(x**2+y**2)
    a, b = t**2/(x+t)**2, x**2/(x+t)**2
    D0 = (3-e)*np.array([[a, -b], [-a, b]])
    r2 = x**2+y**2
    M = np.array([[-2*x*y, x**2-y**2], [y**2-x**2, -2*x*y]])/r2**2
    Dz = -e*z**3*M
    xi = zxi/z
    zeta = -e*z**2*np.array([y, x])/r2
    zdzxi = 2*zeta - (zxi/z - zeta)
    return xi, D0+Dz, zdzxi
rng = np.random.default_rng(1)
for e in [0.1, 0.5]:
  for delta in [0.01]:
    for z in [1e-2, 1e-4, 1e-6]:
        worst = 1e9; wq = None
        for _ in range(20000):
            x = z*10**rng.uniform(np.log10(z**0.5)-1.2, np.log10((2*delta)**(1/6)))
            H = rng.uniform(-1, 1)*np.sqrt(delta)*z**3
            y = (H - z**3)/x
            W = H**2 + x**6 + y**6
            if W > delta*z**6 or y >= 0 or x >= z or -y >= z: continue
            xi, DzXi, zdzxi = field(x, y, z, e)
            Y = np.array([xi[0], xi[1], 1.0])
            # basis of Y-perp
            n1 = np.cross(Y, [1.0, 0, 0]); n1 /= np.linalg.norm(n1)
            n2 = np.cross(Y, n1); n2 /= np.linalg.norm(n2)
            B = np.stack([n1, n2], axis=1)  # 3x2
            # bilinear form z<w,D_w Y> = what^T DzXi what + w_z what . zdzxi
            J = np.zeros((3, 3)); J[:2, :2] = DzXi; J[:2, 2] = zdzxi
            Q = B.T @ J @ B; Qs = (Q+Q.T)/2
            m = np.linalg.eigvalsh(Qs).min()
            if m < worst: worst, wq = m, (x/z, y/z, x/abs(y))
        print(f"e={e} delta={delta} z={z:g}: inf z<w,D_wY>/|w|^2 = {worst:.5f} at x/z,y/z,u = {wq}; -(3-e)(sqrt2-1)/2-2e/3={-(3-e)*(np.sqrt(2)-1)/2-2*e/3:.4f}")
