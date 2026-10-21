# R38: sampled check of the step-3 bounds of theorem II on D_sigma (V=0): |xi|<=3 z^1/2, |z d_z xi|<=4 z^1/2,
# |z D_Y Y| <= 19 z^1/2, x|y| in [3/4,5/4] z^3, and of the zone estimate in step 5.
import numpy as np, spectra_check as sc
rng = np.random.default_rng(5)
for e in [0.1, 0.5]:
  for delta in [1/32, 0.01]:
    mx = dict(xi=0, zdz=0, DYY=0, xy_lo=9, xy_hi=0, L2=9)
    for z in [1e-2, 1e-3, 1e-5]:
        for _ in range(40000):
            x = 10**rng.uniform(np.log10(0.7*z**2/(2*delta)**(1/6)), np.log10((2*delta)**(1/6)*z))
            H = rng.uniform(-1, 1)*np.sqrt(2*delta)*z**3
            y = (H - z**3)/x
            if H**2 + x**6 + y**6 > 2*delta*z**6 or -y >= z or x >= z: continue
            xi, DzXi, zdzxi = sc.field(x, y, z, e)
            mx['xi'] = max(mx['xi'], np.linalg.norm(xi)/z**0.5)
            mx['zdz'] = max(mx['zdz'], np.linalg.norm(zdzxi)/z**0.5)
            mx['DYY'] = max(mx['DYY'], np.linalg.norm(DzXi@xi + zdzxi)/z**0.5)
            r = x*(-y)/z**3; mx['xy_lo'] = min(mx['xy_lo'], r); mx['xy_hi'] = max(mx['xy_hi'], r)
            # Euler: (6W - zYW - 2e(H^2+x^6+y^6)) / z^9 lower bound vs claimed -5000 z^9 - 6e(2delta)^{2/3} z^7 (V=0)
            t = -y; lx = (3-e)*t/(x+t); ly = (3-e)*x/(x+t)
            r2 = x**2+y**2
            zz1 = -e*z**3*y/r2; zz2 = -e*z**3*x/r2
            E6 = 2*e*H**2 + 6*(1-lx)*x**6 + 6*(1-ly)*y**6 - 6*(x**5*zz1 + y**5*zz2)
            slack = E6 - 2*e*(H**2 + x**6 + y**6)
            claimed = -5000*z**9 - 6*e*(2*delta)**(2/3)*z**7
            mx['L2'] = min(mx['L2'], slack - claimed)
    print(f"e={e} delta={delta:.4f}: sup|xi|/z^.5={mx['xi']:.3f}(<=3) sup|z dz xi|/z^.5={mx['zdz']:.3f}(<=4) sup|zD_YY|/z^.5={mx['DYY']:.3f}(<=19) x|y|/z^3 in [{mx['xy_lo']:.3f},{mx['xy_hi']:.3f}] min(slack-claimed)={mx['L2']:.3e} (>=0)")
