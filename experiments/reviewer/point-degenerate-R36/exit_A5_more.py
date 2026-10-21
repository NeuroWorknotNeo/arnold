"""R36: (A5) для кольца R (полярная параметризация трубки) и для собственного примера SV2,
где нужно именно поле следствия SV (не диагональное; поле Cb и диагональные поля не работают).

SV2: U = (z^4 y - z^4 x^2 - z^2 x^3)^2 + x^8 + y^8 - z^16 + x z^15, луч +e_z, c=(2,4), N=1, beta=16:
     F = -1 + (b2 - b1^2 - b1^3)^2 + b1^8 + s b1 + s^16 b2^8 (проверяется ниже символьно).
     Поле следствия SV с alpha=1, phi=b1^2+b1^3: xi = (b1, 2 b2 + b1^3),
     Y = e_z + x^{c-1}(Cb - xi) = (x/z, 2y/z - x^3/z^3, 1).
[Эксперимент] mpmath, 40 знаков. Запуск: ~/venv/bin/python exit_A5_more.py [R|SV2]
"""
import sys
import sympy as sp
import mpmath as mp
from exit_A5 import build, x, y, z

mp.mp.dps = 40


def frame(Yv):
    hv = sum(t * t for t in Yv)
    yn = [t / mp.sqrt(hv) for t in Yv]
    a = [1, 0, 0] if abs(yn[0]) < 0.9 else [0, 1, 0]
    d = sum(a[k] * yn[k] for k in range(3))
    e1 = [a[k] - d * yn[k] for k in range(3)]
    ne = mp.sqrt(sum(t * t for t in e1)); e1 = [t / ne for t in e1]
    e2 = [yn[1] * e1[2] - yn[2] * e1[1], yn[2] * e1[0] - yn[0] * e1[2], yn[0] * e1[1] - yn[1] * e1[0]]
    return hv, e1, e2


def eval_point(fXi, fU, fY, X, Yc, Z, rho, beta, a0, delta, ndir):
    Uv = fU(X, Yc, Z)
    W = Uv + a0 * rho**beta
    if W > delta * rho**beta:
        return None
    Yv = [mp.mpf(t) for t in fY(X, Yc, Z)]
    hv, e1, e2 = frame(Yv)
    Kp = delta * rho**beta - W
    lam = mp.sqrt(2 * (a0 - delta) * rho**beta / hv)
    best = mp.inf
    for kdir in range(ndir):
        th = 2 * mp.pi * kdir / ndir
        ee = [mp.cos(th) * e1[k] + mp.sin(th) * e2[k] for k in range(3)]
        vv = [-lam * Yv[k] + mp.sqrt(2 * Kp) * ee[k] for k in range(3)]
        E = sum(t * t for t in vv) / 2 + Uv
        assert abs(E) < mp.mpf(10)**(-25) * rho**beta
        val = (rho / lam) * fXi(X, Yc, Z, *vv) / (delta * rho**beta)
        best = min(best, val)
    return best


def run_R():
    U = (x**2 + y**2 - z**3)**2 - z**8 + x * z**8
    Yh = sp.Matrix([sp.Rational(3, 2) * x / z, sp.Rational(3, 2) * y / z, 1])
    beta, a0 = 8, 1
    for delta in (mp.mpf('0.05'), mp.mpf('0.01')):
        fXi, fU, fY = build(U, Yh, beta, a0, delta)
        for rho in (mp.mpf('1e-2'), mp.mpf('1e-4'), mp.mpf('1e-6'), mp.mpf('1e-8')):
            s = mp.sqrt(rho)
            # трубка: | |b|^2 - 1 | <= sqrt(delta + s^3) s^2 (с запасом)
            umax = mp.sqrt(delta + s**3) * s**2 * mp.mpf('1.2')
            best, arg, cnt = mp.inf, None, 0
            for i in range(72):
                th = 2 * mp.pi * i / 72
                for j in range(41):
                    u = -umax + 2 * umax * j / 40
                    r = mp.sqrt(1 + u)
                    b1, b2 = r * mp.cos(th), r * mp.sin(th)
                    X, Yc = rho**mp.mpf(1.5) * b1, rho**mp.mpf(1.5) * b2
                    val = eval_point(fXi, fU, fY, X, Yc, rho, rho, beta, a0, delta, 8)
                    if val is None:
                        continue
                    cnt += 1
                    if val < best:
                        best, arg = val, (float(th), float(u / s**2))
            print(f"R ring, Y=e_z+(3/2)(x,y)/z: delta={delta}, rho={float(rho):.0e}: min = {mp.nstr(best, 6)} "
                  f"at (theta, (|b|^2-1)/s^2)={arg}; points: {cnt}", flush=True)


def run_SV2():
    U = (z**4 * y - z**4 * x**2 - z**2 * x**3)**2 + x**8 + y**8 - z**16 + x * z**15
    s, b1, b2 = sp.symbols('s b1 b2')
    F = sp.expand(U.subs({x: z**2 * b1, y: z**4 * b2}, simultaneous=True) / z**16).subs(z, s)
    print("SV2: F - expected =", sp.expand(F - (-1 + (b2 - b1**2 - b1**3)**2 + b1**8 + s * b1 + s**16 * b2**8)))
    Q = (b2 - b1**2 - b1**3)**2 + b1**8
    lie = lambda xi, f: sp.expand(xi[0] * sp.diff(f, b1) + xi[1] * sp.diff(f, b2))
    t = b2 - b1**2 - b1**3
    print("SV2: xi.gradQ - (4 t^2 + 8 b1^8) =", sp.expand(lie((b1, 2 * b2 + b1**3), Q) - (4 * t**2 + 8 * b1**8)))
    print("SV2: <Cb,gradQ> at t=b1^3/4:", sp.factor(lie((2 * b1, 4 * b2), Q).subs(b2, b1**2 + b1**3 + b1**3 / 4)))
    # диагональное поле (l1 b1, 2 l1 b2) при t = b1^3/4
    l1 = sp.symbols('l1', positive=True)
    print("SV2: diag (1,2) field at t=b1^3/4:", sp.factor(lie((l1 * b1, 2 * l1 * b2), Q).subs(b2, b1**2 + b1**3 + b1**3 / 4)))
    u8 = sum(term for term in sp.Add.make_args(sp.expand(U)) if sp.Poly(term, x, y, z).total_degree() == 8)
    lowdeg = min(sp.Poly(term, x, y, z).total_degree() for term in sp.Add.make_args(sp.expand(U)))
    print("SV2: lowest degree =", lowdeg, "; u8 =", u8)
    beta, a0 = 16, 1
    fields = {'SV field (x/z, 2y/z - x^3/z^3, 1)': sp.Matrix([x / z, 2 * y / z - x**3 / z**3, 1]),
              'Y=e_z (xi=Cb)': sp.Matrix([0, 0, 1]),
              'radial-(1,2) (x/z, 2y/z, 1)': sp.Matrix([x / z, 2 * y / z, 1])}
    for delta in (mp.mpf('0.05'), mp.mpf('0.01')):
        for name, Yf in fields.items():
            fXi, fU, fY = build(U, Yf, beta, a0, delta)
            for rho in (mp.mpf('1e-3'), mp.mpf('1e-5')):
                best, arg, cnt = mp.inf, None, 0
                # параметризация по (b1, t): b2 = b1^2 + b1^3 + t
                B1 = float(delta**(mp.mpf(1) / 8)) * 1.05
                T = float(mp.sqrt(delta)) * 1.05
                n = 81
                for i in range(n):
                    bb1 = -B1 + 2 * B1 * mp.mpf(i) / (n - 1)
                    for j in range(n):
                        tt = -T + 2 * T * mp.mpf(j) / (n - 1)
                        bb2 = bb1**2 + bb1**3 + tt
                        X, Yc = rho**2 * bb1, rho**4 * bb2
                        val = eval_point(fXi, fU, fY, X, Yc, rho, rho, beta, a0, delta, 12)
                        if val is None:
                            continue
                        cnt += 1
                        if val < best:
                            best, arg = val, (float(bb1), float(tt))
                print(f"SV2, {name}: delta={delta}, rho={float(rho):.0e}: min = {mp.nstr(best, 6)} at (b1,t)={arg}; "
                      f"points: {cnt}", flush=True)


if __name__ == '__main__':
    which = sys.argv[1:] or ['R', 'SV2']
    if 'R' in which:
        run_R()
    if 'SV2' in which:
        run_SV2()
