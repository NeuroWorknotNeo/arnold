"""[Эксперимент] Продолжение exit_check.py: (1) поле nonT при меньших x (там, где возмущение sigma*s*b1
уже мало по сравнению с delta) — рост провала ~ 1/x = x^{c1-c2}; (2) поле теоремы T в «худших» точках:
полярные точки полосы (d2 Qt = 0, delta/2 <= Qt <= delta), где xi.grad Q = alpha*kappa*b1*d1Q мало, и точки
рядом с ними; v_perp = 0 и по 8 направлениям."""
import sys
import numpy as np
import sympy as sp
import mpmath as mp
sys.path.insert(0, '.')
from band_field import sample_K, polar_points, Q_and_grad  # noqa: E402
from exit_check import build, exit_min, B1, B2, Qt  # noqa: E402

mp.mp.dps = 60
delta = mp.mpf('1e-6')
rng = np.random.default_rng(11)
b1s, b2s = sample_K(1e-6, 301, 6, rng)
keep = [(a, b) for a, b in zip(b1s, b2s) if a * a + b * b <= 0.25]
idx = rng.choice(len(keep), size=300, replace=False)
bs = [keep[i] for i in idx]
fN = build(sp.Rational(3, 2) * B1 - B2**2 / 2, B2 / 2)
print('(1) nonT field, delta = 1e-6, 300 random points of K x 9 directions')
for X in ('1e-8', '1e-10', '1e-12'):
    exit_min(fN, delta, [X], bs, 8, f'nonT field, x={X}', rng)

P = polar_points(1e-6, nb1=4001)
band = P[(P[:, 2] >= 0.5e-6) & (P[:, 2] <= 1e-6)]
sel = band[rng.choice(len(band), size=min(120, len(band)), replace=False)]
pts = [(a, b) for a, b, _, _ in sel]
# точки рядом с полярными: сдвиг по b2 на малую величину
pts += [(a, b + s * 1e-4) for a, b in pts[:60] for s in (-1, 1)]
print(f'(2) band field at {len(pts)} polar / near-polar points of the band')
Lam, kappa, alpha = 2.861e5, 1.0, 2.006e-06
fB = build(alpha * kappa * B1, alpha * Lam * sp.diff(Qt, B2))
for X in ('1e-12', '1e-16', '1e-20'):
    exit_min(fB, delta, [X], pts, 8, f'band field, x={X}', rng)
