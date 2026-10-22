"""[Эксперимент] Строгий выход (A5) теоремы A [007] прямым дифференцированием в R^3 для модели U2
(model_U.py: профиль Q = A*B предложения 6.2 [009] + b1^24, a0 = 1, sigma = -1, beta = 48, c = (2,3)).

Поле Y = e_x + Z, Z_i = x^{c_i-1}(c_i b_i - xi_i(b)) (поле (0.1) теоремы 2U [012], gamma = 0, L = I), rho = x,
A(r) = a0 r^beta. Xi = d/dt (V - delta rho^beta) вычисляется НЕ через тождество (1.3) [007], а по
определению: d/dt(|v|^2/2+U) = 0, pdot = -<grad U,Y> + <v,D_v Y>, hdot = 2<Y,D_v Y>.
Точки множества (A5): b из {P(s,b) <= delta, |b| <= r1} (P = Qt + sigma*s*b1), K = delta rho^beta - W >= 0,
v = -lam Y + v_perp, |v_perp|^2 = 2K, направление v_perp в Y^perp случайно/по сетке, lam из E = 0.
Печатается min (rho/lam) Xi / (delta rho^beta) (нужно > 0).

Поля:
  nonT : xi = (3/2 b1 - 1/2 b2^2, 1/2 b2) — предложение 6.2(b) [009]: xi Q >= 6Q, НО d xi_1/d b2 = -b2 != 0
         (нарушает (T)); ожидается провал выхода ~ x^{c1-c2} = 1/x;
  band : xi = alpha*(kappa b1, Lam d2 Qt) — поле теоремы T (условие (T) выполнено), kappa = 1,
         Lam = 2.861e5 (band_field.py, delta = 1e-6), alpha = масштаб для (Theta).
"""
import sys
import numpy as np
import sympy as sp
import mpmath as mp
sys.path.insert(0, '.')
from band_field import sample_K  # noqa: E402

mp.mp.dps = 60
x, y, z, B1, B2 = sp.symbols('x y z B1 B2', real=True)
beta, a0, sigma, c1, c2 = 48, 1, -1, 2, 3
A_ = (B1 - B2**2)**2 + B2**8
Bq = (B1 - B2**2 - B2**3)**2 + B2**8
Qt = sp.expand(A_ * Bq + B1**24)
Ahat = x**12 * (x**4 * y - z**2)**2 + z**8
Bhat = x**6 * (x**7 * y - x**3 * z**2 - z**3)**2 + z**8
U = Ahat * Bhat + y**24 - a0 * x**48 + sigma * x**47 * y
q = sp.Matrix([x, y, z])
bsub = {B1: y / x**c1, B2: z / x**c2}


def build(xi1, xi2):
    Z1 = x**(c1 - 1) * (c1 * B1 - xi1)
    Z2 = x**(c2 - 1) * (c2 * B2 - xi2)
    Y = sp.Matrix([1, Z1.subs(bsub, simultaneous=True), Z2.subs(bsub, simultaneous=True)])
    J = Y.jacobian(q)
    gU = sp.Matrix([sp.diff(U, w) for w in q])
    return sp.lambdify((x, y, z), [U, list(gU), list(Y), J.tolist()], 'mpmath')


def exit_min(f, delta, xs, bs, nth, label, rng):
    worst = (mp.inf, None)
    for X in xs:
        X = mp.mpf(X)
        for b1v, b2v in bs:
            yy, zz = X**c1 * mp.mpf(b1v), X**c2 * mp.mpf(b2v)
            Uv, gU, Yv, J = f(X, yy, zz)
            gU = mp.matrix(gU); Yv = mp.matrix(Yv); J = mp.matrix(J)
            W = Uv + a0 * X**beta
            K = delta * X**beta - W
            if K < 0:
                continue
            h = (Yv.T * Yv)[0]
            lam2 = 2 * (-Uv - K) / h
            if lam2 <= 0:
                continue
            lam = mp.sqrt(lam2)
            # ортонормированный базис Y^perp
            e = mp.matrix([0, 1, 0])
            e1 = e - Yv * ((Yv.T * e)[0] / h); e1 = e1 / mp.norm(e1)
            e2 = mp.matrix([Yv[1] * e1[2] - Yv[2] * e1[1], Yv[2] * e1[0] - Yv[0] * e1[2], Yv[0] * e1[1] - Yv[1] * e1[0]])
            e2 = e2 / mp.norm(e2)
            ths = [2 * mp.pi * k / nth for k in range(nth)] + [2 * mp.pi * rng.random()]
            for th in ths:
                vp = mp.sqrt(2 * K) * (mp.cos(th) * e1 + mp.sin(th) * e2)
                v = -lam * Yv + vp
                p = (v.T * Yv)[0]
                DvY = J * v
                pdot = -(gU.T * Yv)[0] + (v.T * DvY)[0]
                hdot = 2 * (Yv.T * DvY)[0]
                Ap = a0 * beta * X**(beta - 1)
                Xi = -(p / h) * pdot + p * p / (2 * h * h) * hdot + (Ap - beta * delta * X**(beta - 1)) * v[0]
                val = (X / lam) * Xi / (delta * X**beta)
                if val < worst[0]:
                    worst = (val, (mp.nstr(X, 3), round(b1v, 4), round(b2v, 4), mp.nstr(K / (delta * X**beta), 3)))
    print(f'  {label}: min (rho/lam)Xi/(delta rho^beta) = {mp.nstr(worst[0], 6)}  at (x,b1,b2,K/(d x^b))={worst[1]}',
          flush=True)
    return worst[0]


if __name__ == '__main__':
    delta = mp.mpf('1e-6')
    rng = np.random.default_rng(7)
    b1s, b2s = sample_K(1e-6, 301, 6, rng)
    keep = [(a, b) for a, b in zip(b1s, b2s) if a * a + b * b <= 0.25]
    idx = rng.choice(len(keep), size=min(400, len(keep)), replace=False)
    bs = [keep[i] for i in idx]
    print(f'delta = 1e-6, {len(bs)} sample points b in K, 9 directions of v_perp each')
    fN = build(sp.Rational(3, 2) * B1 - B2**2 / 2, B2 / 2)
    for X in ('1e-2', '1e-3', '1e-4', '1e-6'):
        exit_min(fN, delta, [X], bs, 8, f'nonT field, x={X}', rng)
    # поле теоремы T
    Lam, kappa = 2.861e5, 1.0
    d2Q = sp.diff(Qt, B2)
    # alpha: (Theta) — c1 - alpha*kappa >= 0, c2 - alpha*Lam*d2^2 Qt >= 0 на |b| <= 0.5
    g22 = sp.lambdify((B1, B2), sp.diff(Qt, B2, 2), 'numpy')
    th = np.linspace(0, 2 * np.pi, 2001); rr = np.linspace(0, 0.5, 501)
    R, T = np.meshgrid(rr, th)
    sup22 = np.max(g22(R * np.cos(T), R * np.sin(T)))
    alpha = min(1.0, c1 / kappa, c2 / (Lam * sup22))
    print(f'band field: kappa={kappa}, Lam={Lam:.4g}, sup d2^2 Qt (|b|<=.5) = {sup22:.4g}, alpha = {alpha:.4g}, '
          f'expected margin ~ alpha*mu*(7/8) = {alpha * 0.0631 * 7 / 8:.3g}')
    fB = build(alpha * kappa * B1, alpha * Lam * d2Q)
    for X in ('1e-4', '1e-8', '1e-12', '1e-16', '1e-20'):
        exit_min(fB, delta, [X], bs, 8, f'band field, x={X}', rng)
