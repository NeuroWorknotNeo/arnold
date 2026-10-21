# R33 [Experiment]: sampled check of the Euler inequality (5.4) and of the (V0)-Euler inequality of §8 p.7.
import numpy as np
rng = np.random.default_rng(1)
# (5.4): kappa*theta*Lambda' + kappa/2*theta*h' e^2 + c h e^2 >= kappa*(Lambda + h e^2/2)
# with theta*Lambda' >= Lambda, |theta h'| <= h, c >= 3/2, kappa in (0,1/2]
worst = np.inf
for _ in range(200000):
    kap = rng.uniform(1e-6, 0.5); c = rng.uniform(1.5, 6); h = rng.uniform(0.1, 5); th_hp = rng.uniform(-h, h)
    Lam = rng.uniform(0, 1); thLp = Lam + rng.uniform(0, 1); e2 = rng.uniform(0, 1)
    lhs = kap * thLp + kap / 2 * th_hp * e2 + c * h * e2
    worst = min(worst, lhs - kap * (Lam + h * e2 / 2))
print('(5.4) min(lhs - kappa Q) over samples:', worst)
# §8 p.7: (1+alpha) b1 QV' + c' h e^2 >= QV + h e^2/2 given b1 QV' >= (k0/2) QV >= QV >= 0, c'>1
worst = np.inf
for _ in range(200000):
    al = rng.uniform(1e-6, 3); cp = rng.uniform(1 + 1e-9, 5); h = rng.uniform(0.1, 5); e2 = rng.uniform(0, 1)
    QV = rng.uniform(0, 1); k0 = 2 * rng.integers(1, 5); bQ = (k0 / 2) * QV + rng.uniform(0, 1)
    worst = min(worst, (1 + al) * bQ + cp * h * e2 - (QV + h * e2 / 2))
print('(V0) Euler min margin over samples:', worst)
# odd degree d=2q-1 of the Weierstrass polynomial => at least one real branch (I_R nonempty) — trivial check
print('d = 2q-1 odd for q=1..6:', [2 * q - 1 for q in range(1, 7)])
