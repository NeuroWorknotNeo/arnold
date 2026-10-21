"""R36: (A5) для примера SV2 с полем следствия SV (alpha=1): сетка по (b1,t) и граница P=delta.
U = (z^4 y - z^4 x^2 - z^2 x^3)^2 + x^8 + y^8 - z^16 + x z^15, c=(2,4), beta=16, a0=1,
Y = (x/z, 2y/z - x^3/z^3, 1).  [Эксперимент] mpmath 40 знаков.
Запуск: ~/venv/bin/python exit_A5_SV2_fast.py DELTA RHO
"""
import sys
import sympy as sp
import mpmath as mp
from exit_A5 import build, x, y, z
from exit_A5_more import eval_point
from exit_A5_boundary import bisect

mp.mp.dps = 40
delta, rho = mp.mpf(sys.argv[1]), mp.mpf(sys.argv[2])
U = (z**4 * y - z**4 * x**2 - z**2 * x**3)**2 + x**8 + y**8 - z**16 + x * z**15
Y = sp.Matrix([x / z, 2 * y / z - x**3 / z**3, 1])
beta, a0 = 16, 1
fXi, fU, fY = build(U, Y, beta, a0, delta)


def pt(b1, t):
    return rho**2 * b1, rho**4 * (b1**2 + b1**3 + t)


best, arg, cnt = mp.inf, None, 0
B1, T, n = float(delta**(mp.mpf(1) / 8)) * 1.05, float(mp.sqrt(delta)) * 1.05, 41
for i in range(n):
    b1 = -B1 + 2 * B1 * mp.mpf(i) / (n - 1)
    for j in range(n):
        t = -T + 2 * T * mp.mpf(j) / (n - 1)
        X, Yc = pt(b1, t)
        val = eval_point(fXi, fU, fY, X, Yc, rho, rho, beta, a0, delta, 8)
        if val is not None:
            cnt += 1
            if val < best:
                best, arg = val, (float(b1), float(t))
print(f"SV2, SV field: grid, delta={delta}, rho={float(rho):.0e}: min = {mp.nstr(best, 6)} at (b1,t)={arg}; "
      f"points {cnt}", flush=True)


def P(b1, t):
    X, Yc = pt(b1, t)
    return (fU(X, Yc, rho) + a0 * rho**beta) / rho**beta


best, arg = mp.inf, None
for i in range(120):
    phi = 2 * mp.pi * i / 120
    ray = (lambda ph: (lambda r: (r * mp.cos(ph), r**4 * mp.sin(ph))))(phi)
    r = bisect(lambda r: P(*ray(r)) - delta, mp.mpf('1e-6'), mp.mpf(2))
    X, Yc = pt(*ray(r))
    val = eval_point(fXi, fU, fY, X, Yc, rho, rho, beta, a0, delta + mp.mpf(10)**-30, 16)
    if val is not None and val < best:
        best, arg = val, tuple(float(u) for u in ray(r))
print(f"SV2, SV field: boundary P=delta, delta={delta}, rho={float(rho):.0e}: min = {mp.nstr(best, 6)} "
      f"at (b1,t)={arg}", flush=True)
