"""R36: (A5) на границе P = delta (там K_perp = 0 и запас минимален) для Lambda, X, R.
Точки границы находятся решением P(s,b) = delta вдоль лучей (mpmath.findroot, бисекция).
[Эксперимент] mpmath, 40 знаков. Запуск: ~/venv/bin/python exit_A5_boundary.py
"""
import sympy as sp
import mpmath as mp
from exit_A5 import build, x, y, z
from exit_A5_more import eval_point

mp.mp.dps = 40
k = sp.Rational(199, 100)


def bisect(f, lo, hi):
    flo, fhi = f(lo), f(hi)
    assert flo < 0 < fhi, (flo, fhi)
    for _ in range(150):
        mid = (lo + hi) / 2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def run(name, U, Y, beta, a0, c, deltas, rhos, ray, tmax, nray=180, ndir=24):
    for delta in deltas:
        fXi, fU, fY = build(U, Y, beta, a0, delta)
        for rho in rhos:
            P = lambda b1, b2: (fU(rho**c[0] * b1, rho**c[1] * b2, rho) + a0 * rho**beta) / rho**beta
            best, arg = mp.inf, None
            for i in range(nray):
                phi = 2 * mp.pi * i / nray
                f = lambda t: P(*ray(t, phi)) - delta
                t = bisect(f, mp.mpf('1e-6'), tmax)
                b1, b2 = ray(t, phi)
                X, Yc = rho**c[0] * b1, rho**c[1] * b2
                val = eval_point(fXi, fU, fY, X, Yc, rho, rho, beta, a0, delta + mp.mpf(10)**-30, ndir)
                if val is not None and val < best:
                    best, arg = val, (float(b1), float(b2))
            print(f"{name}: boundary P=delta, delta={delta}, rho={float(rho):.0e}: min = {mp.nstr(best, 6)} at b={arg}",
                  flush=True)


if __name__ == '__main__':
    # Lambda: лучи в весах (1,2): b = (t cos phi, t^2 sin phi)
    U = x**4 - k * x**2 * y * z + y**2 * z**2 + y**4 - z**8 + x * z**7
    run('Lambda, Y=q/z', U, sp.Matrix([x / z, y / z, 1]), 8, 1, (2, 3), [mp.mpf('0.05'), mp.mpf('0.01')],
        [mp.mpf('1e-3'), mp.mpf('1e-5')], lambda t, p: (t * mp.cos(p), t**2 * mp.sin(p)), mp.mpf(3))
    # X: прямые лучи
    U = x**6 + y**6 + y**4 * z**2 + x**2 * y**2 * z**2 - z**12 + x * z**11
    run('X, Y=e_z', U, sp.Matrix([0, 0, 1]), 12, 1, (2, sp.Rational(5, 2)), [mp.mpf('0.05'), mp.mpf('0.01')],
        [mp.mpf('1e-3'), mp.mpf('1e-6')], lambda t, p: (t * mp.cos(p), t * mp.sin(p)), mp.mpf(1))
    # R: снаружи и изнутри кольца, b = (1 + u)^{1/2} (cos phi, sin phi), u = +-t s^2
    U = (x**2 + y**2 - z**3)**2 - z**8 + x * z**8
    Yh = sp.Matrix([sp.Rational(3, 2) * x / z, sp.Rational(3, 2) * y / z, 1])
    for sgn in (1, -1):
        for rho in (mp.mpf('1e-4'), mp.mpf('1e-6'), mp.mpf('1e-8')):
            s = mp.sqrt(rho)
            ray = (lambda s_, sg: (lambda t, p: (mp.sqrt(1 + sg * t * s_**2) * mp.cos(p),
                                                 mp.sqrt(1 + sg * t * s_**2) * mp.sin(p))))(s, sgn)
            run(f'R ring ({"outer" if sgn > 0 else "inner"}), Y=e_z+(3/2)(x,y)/z', U, Yh, 8, 1,
                (sp.Rational(3, 2), sp.Rational(3, 2)), [mp.mpf('0.05'), mp.mpf('0.01')], [rho], ray, mp.mpf(2),
                nray=72, ndir=16)
