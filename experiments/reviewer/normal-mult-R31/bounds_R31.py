# R31 [Experiment]: random stress test of the termwise bounds in Theorem N, pp. 3-5:
#  |<omega,w>| <= (5/4 kappa|theta| + |nu|)|w|,
#  |<x Phi_xx, w>| <= gamma2|theta| + C1 theta^2 + (1+kbar)*varpi1   (|w|=1),
#  |E_r| <= (C1|theta| + 6(1+kbar) varpi1)|w|^2   for w perp Y,
# with all "small quantities" drawn independently subject only to the constraints of the
# choice of s_0: |eps|,|nu|<=1/4, |eta0_s|+4/3|eta0_th|/x<=1, |theta|<r0<=1/4, kappa<=1/2.
import numpy as np
rng = np.random.default_rng(31)
worst = [0, 0, 0, 0]
for it in range(400000):
    kap = rng.uniform(0, 0.5); kb = rng.uniform(0, 3); kgv = kb*rng.uniform(-1, 1)
    th = rng.uniform(-0.25, 0.25)
    sc = 10**rng.uniform(-6, 0)   # scale of small quantities
    eps = np.clip(rng.uniform(-1, 1)*sc, -0.25, 0.25)
    nu = np.clip(rng.uniform(-1, 1)*sc, -0.25, 0.25)
    dte, sde, dtn, sdn, xde, xdn = rng.uniform(-1, 1, 6)*sc
    e0s = rng.uniform(-1, 1); e0t = rng.uniform(-1, 1)*(1 - abs(e0s))*0.75   # eta0_th/x
    varpi1 = abs(eps)+abs(nu)+abs(dte)+abs(sde)+abs(dtn)+abs(sdn)+abs(xde)+abs(xdn)
    C1 = 1.25*kap**2*(1+kb) + 4*kap*kb
    # random w perp Y: Y=(1,-kap th(1-eps),nu)
    Y = np.array([1, -kap*th*(1-eps), nu])
    w = rng.normal(size=3); w -= Y*(w@Y)/(Y@Y); w /= np.linalg.norm(w)
    wo, wl, wn = w
    # (Phi2'') first
    r1 = abs(wo) / (1.25*kap*abs(th) + abs(nu) + 1e-300)
    # (Phi2'') second, |w|=1 (any w)
    v = rng.normal(size=3); v /= np.linalg.norm(v)
    P44 = np.array([-kap**2*th**2*(1-eps), -kap*th*((1-kap)+kap*eps-xde-nu*kgv), kap**2*th**2*(1-eps)*kgv + xdn])
    r2 = abs(P44@v) / (kap*(1-kap)*abs(th) + C1*th**2 + (1+kb)*varpi1 + 1e-300)
    # (Phi3'')
    az = wn - wo*e0s - wl*e0t/(1-eps)        # eta0_th/(s(1-eps)) with s=x
    Er = (wl/(1-eps))*((kap*th*dte - nu*kgv)*wl + (-kap*th*(1-eps)*kgv + dtn)*wn) \
         + kap*th*wl*wo + wo*(kap*th*sde*wl + sdn*wn) + az*kap*th*kgv*wl
    r3 = abs(Er) / (C1*abs(th) + 6*(1+kb)*varpi1 + 1e-300)
    main = wl**2*(1/(1-eps) - kap)
    worst = [max(worst[0], r1), max(worst[1], r2), max(worst[2], r3), min(worst[3], main)]
print('max ratio first (Phi2\'\') :', worst[0])
print('max ratio second (Phi2\'\'):', worst[1])
print('max ratio |E_r| bound     :', worst[2])
print('min main term (should be >=0):', worst[3])
