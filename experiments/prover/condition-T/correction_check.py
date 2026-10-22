"""[Эксперимент] Поправка главного агента = замена поля на поле с (T).

Модель (не обязательно аналитическая): U = x^beta (-1 + Q(b)), b = (y/x^c1, z/x^c2), Q = A*B (предложение 6.2 [009]),
c = (3, 4) (здесь 2c1 - 1 - c2 = 1 > 0), beta = 64.
Поле nonT: xi = (3/2 b1 - b2^2/2, b2/2), нарушает (T). Поправка (в форме записки §6):
    C = lam * <v_perp, Theta>,  Theta = x^{c1-1} G(b) e_y,  G(b) = xi_1(b) - xi_1(b1, 0) = -b2^2/2,
так что Y + Theta — поле с xi' = (3/2 b1, b2/2) (условие (T) выполнено).
В точках (q, v) с E = 0, p < 0, V_{Y'} = delta rho^beta сравниваются нормированные производные
    N_V  = (rho/lam) Xi_V /(delta rho^beta)           (поле nonT без поправки),
    N_C  = (rho/lam) d/dt(V_Y + C - delta rho^beta)/(delta rho^beta),
    N_Y' = (rho/lam) Xi_{V_{Y'}}/(delta rho^beta)      (поле с (T)),
Ожидание: N_V ~ -1/x -> -inf, а N_C - N_Y' = O(x^{2c1-1-c2}) = O(x) -> 0.
"""
import numpy as np
import sympy as sp
import mpmath as mp

mp.mp.dps = 50
x, y, z, v1, v2, v3 = sp.symbols('x y z v1 v2 v3', real=True)
B1, B2 = sp.symbols('B1 B2', real=True)
c1, c2, beta, a0 = 3, 4, 64, 1
A_ = (B1 - B2**2)**2 + B2**8
Bq = (B1 - B2**2 - B2**3)**2 + B2**8
bsub = {B1: y / x**c1, B2: z / x**c2}
U = x**beta * (-a0 + (A_ * Bq).subs(bsub, simultaneous=True))
q = sp.Matrix([x, y, z]); v = sp.Matrix([v1, v2, v3])
gU = sp.Matrix([sp.diff(U, w) for w in q])


def field(xi1, xi2):
    Z1 = x**(c1 - 1) * (c1 * B1 - xi1)
    Z2 = x**(c2 - 1) * (c2 * B2 - xi2)
    return sp.Matrix([1, Z1, Z2]).subs(bsub, simultaneous=True)


def Vfun(Y):
    p = (v.T * Y)[0]; h = (Y.T * Y)[0]
    return (v.T * v)[0] / 2 - p**2 / (2 * h) + U + a0 * x**beta, p, h


def ddt(expr):
    """Производная вдоль потока qdot = v, vdot = -grad U."""
    return sum(sp.diff(expr, q[i]) * v[i] for i in range(3)) - sum(sp.diff(expr, v[i]) * gU[i] for i in range(3))


Y = field(sp.Rational(3, 2) * B1 - B2**2 / 2, B2 / 2)
Yp = field(sp.Rational(3, 2) * B1, B2 / 2)
VY, pY, hY = Vfun(Y)
VYp, pYp, hYp = Vfun(Yp)
lam = -pY / hY
vperp = v - (pY / hY) * Y
Theta = sp.Matrix([0, x**(c1 - 1) * (-(z / x**c2)**2 / 2), 0])
C = lam * (vperp.T * Theta)[0]
delta = sp.Rational(1, 10**4)
XiV = ddt(VY - delta * x**beta)
XiC = ddt(VY + C - delta * x**beta)
XiYp = ddt(VYp - delta * x**beta)
f = sp.lambdify((x, y, z, v1, v2, v3), [U, list(Yp), XiV, XiC, XiYp, lam, -pYp / hYp], 'mpmath')

rng = np.random.default_rng(5)
print('delta = 1e-4; points: b random in {Q <= delta}, |b|<=0.6, v = -lam\' Y\' + v_perp\' (V_{Y\'} = delta rho^beta)')
for X in ('1e-2', '1e-3', '1e-4', '1e-5', '1e-6'):
    X = mp.mpf(X)
    stats = []
    tries = 0
    while len(stats) < 150 and tries < 20000:
        tries += 1
        b = rng.uniform(-0.6, 0.6, 2)
        Qv = ((b[0] - b[1]**2)**2 + b[1]**8) * ((b[0] - b[1]**2 - b[1]**3)**2 + b[1]**8)
        if Qv > 1e-4:
            continue
        yy, zz = X**c1 * mp.mpf(b[0]), X**c2 * mp.mpf(b[1])
        Uv, Ypv, *_ = f(X, yy, zz, 0, 0, 0)
        Ypv = mp.matrix(Ypv)
        W = Uv + a0 * X**beta
        K = delta * X**beta - W
        h = (Ypv.T * Ypv)[0]
        lam2 = 2 * (-Uv - K) / h
        e = mp.matrix([0, 1, 0]); e1 = e - Ypv * ((Ypv.T * e)[0] / h); e1 /= mp.norm(e1)
        e2 = mp.matrix([Ypv[1] * e1[2] - Ypv[2] * e1[1], Ypv[2] * e1[0] - Ypv[0] * e1[2], Ypv[0] * e1[1] - Ypv[1] * e1[0]])
        e2 /= mp.norm(e2)
        th = rng.uniform(0, 2 * np.pi)
        vv = -mp.sqrt(lam2) * Ypv + mp.sqrt(2 * K) * (mp.cos(th) * e1 + mp.sin(th) * e2)
        _, _, xV, xC, xYp, lamY, lamYp = f(X, yy, zz, vv[0], vv[1], vv[2])
        nrm = delta * X**beta
        stats.append((X / lamY * xV / nrm, X / lamY * xC / nrm, X / lamYp * xYp / nrm))
    s = np.array([[float(a) for a in r] for r in stats])
    print(f'  x={mp.nstr(X, 2):6s} n={len(s)}: min N_V = {s[:, 0].min():12.4g}   min N_C = {s[:, 1].min():9.4g}   '
          f"min N_Y' = {s[:, 2].min():9.4g}   max|N_C - N_Y'| = {np.abs(s[:, 1] - s[:, 2]).max():.3e}")
