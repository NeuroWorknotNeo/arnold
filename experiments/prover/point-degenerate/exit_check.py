"""[Эксперимент] Строгий выход (A5) теоремы A (results/007) прямым дифференцированием в R^3.

Для U, поля Y (Y_z = 1, rho = z), A(r) = a0 r^beta и delta вычисляется
    Xi = d/dt (V - delta rho^beta) вдоль поля (v, -grad U),
    V = |v|^2/2 - p^2/(2h) + U + A(rho),  p = <v,Y>,  h = |Y|^2,
по формулам  d/dt(|v|^2/2 + U) = 0,  pdot = -<grad U, Y> + <v, D_v Y>,  hdot = 2<Y, D_v Y>
(без тождества (1.3) из 007). Точки множества из (A5): q = (z^{c1} b1, z^{c2} b2, z) с P(s,b) <= delta,
|b| <= r1, K_perp = delta rho^beta - W >= 0, v = -lam Y + v_perp, v_perp ⊥ Y, |v_perp|^2 = 2 K_perp,
lam из E = 0. Печатается минимум (rho/lam) Xi / (delta rho^beta).

Примеры: Lambda (поле e_z = поле теоремы 2 с весами c, и радиальное поле q/z = поле xi = (C-I)b),
X (крест, поле e_z = xi = Cb).
"""
import numpy as np
import sympy as sp

x, y, z = sp.symbols('x y z', real=True)
q = sp.Matrix([x, y, z])


def make(U, Y):
    gU = sp.Matrix([sp.diff(U, v) for v in q])
    JY = Y.jacobian(q)
    f = sp.lambdify((x, y, z), [U, gU, Y, JY], 'numpy')
    return f


def xi_min(U, Y, beta, a0, c, delta, rhos, r1, nb=61, nth=12, label=''):
    f = make(U, Y)
    worst = np.inf
    worst_pt = None
    count = 0
    for rho in rhos:
        for b1 in np.linspace(-r1, r1, nb):
            for b2 in np.linspace(-r1, r1, nb):
                if b1 * b1 + b2 * b2 > r1 * r1:
                    continue
                X, Yc, Zc = rho**c[0] * b1, rho**c[1] * b2, rho
                Uv, gU, Yv, JY = f(X, Yc, Zc)
                gU = np.array(gU, dtype=float).ravel()
                Yv = np.array(Yv, dtype=float).ravel()
                JY = np.array(JY, dtype=float)
                W = Uv + a0 * rho**beta
                K = delta * rho**beta - W
                if K < 0:
                    continue
                h = Yv @ Yv
                lam2 = 2 * (-Uv - K) / h
                if lam2 <= 0:
                    continue
                lam = np.sqrt(lam2)
                # базис Y^perp
                e1 = np.cross(Yv, [1.0, 0.0, 0.0]); e1 /= np.linalg.norm(e1)
                e2 = np.cross(Yv, e1); e2 /= np.linalg.norm(e2)
                for th in np.linspace(0, 2 * np.pi, nth, endpoint=False):
                    vperp = np.sqrt(2 * K) * (np.cos(th) * e1 + np.sin(th) * e2)
                    v = -lam * Yv + vperp
                    p = v @ Yv
                    DvY = JY @ v
                    pdot = -(gU @ Yv) + v @ DvY
                    hdot = 2 * (Yv @ DvY)
                    rhodot = v[2]  # rho = z
                    Ap = a0 * beta * rho**(beta - 1)
                    Xi = -(p / h) * pdot + p * p / (2 * h * h) * hdot + (Ap - beta * delta * rho**(beta - 1)) * rhodot
                    val = (rho / lam) * Xi / (delta * rho**beta)
                    count += 1
                    if val < worst:
                        worst = val
                        worst_pt = (rho, b1, b2, K / (delta * rho**beta), th)
    print(f'{label}: points={count}, min (rho/lam) Xi/(delta rho^beta) = {worst:.4f} at (rho,b1,b2,K/(d rho^b),theta)='
          f'{tuple(round(float(v), 4) for v in worst_pt)}')
    return worst


if __name__ == '__main__':
    k = sp.Rational(199, 100)
    UL = x**4 - k * x**2 * y * z + y**2 * z**2 + y**4 - z**8 + x * z**7
    for delta in (0.05, 0.01):
        b1m = (delta / (1 - 1.99**2 / 4))**0.25
        r1 = 1.3 * np.hypot(b1m, 0.995 * b1m**2)
        rhos = [delta / 10, delta / 100]
        xi_min(UL, sp.Matrix([0, 0, 1]), 8, 1.0, (2, 3), delta, rhos, r1, nb=121,
               label=f'Lambda, Y=e_z   (xi=Cb),     delta={delta}, rho={rhos}, r1={r1:.2f}')
        xi_min(UL, sp.Matrix([x / z, y / z, 1]), 8, 1.0, (2, 3), delta, rhos, r1, nb=121,
               label=f'Lambda, Y=q/z   (xi=(C-I)b), delta={delta}, rho={rhos}, r1={r1:.2f}')
    UX = x**6 + y**6 + y**4 * z**2 + x**2 * y**2 * z**2 - z**12 + x * z**11
    for delta in (0.05, 0.01):
        r1 = 1.3 * np.hypot(delta**(1 / 6), delta**0.25)
        rhos = [delta / 10, delta / 100]
        xi_min(UX, sp.Matrix([0, 0, 1]), 12, 1.0, (2, 2.5), delta, rhos, r1, nb=121,
               label=f'X (cross), Y=e_z (xi=Cb),    delta={delta}, rho={rhos}, r1={r1:.2f}')
