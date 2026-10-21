"""[Эксперимент] Строгий выход (A5) для кольца U_R = (x^2+y^2-z^3)^2 - z^8 + x z^8 (без симметрии в рассуждении):
rho = z, Y = (c x/z, c y/z, 1), c = 3/2 (поле однородной гомотетии; xi = 0 в теореме 2U), A = rho^8.
Точки: b = (1+u)(cos phi, sin phi), x = z^{3/2} b1, y = z^{3/2} b2, u в полосе, где W <= delta rho^8.
Формулы для Xi — как в exit_check.py (прямое дифференцирование вдоль поля)."""
import numpy as np
import sympy as sp
from exit_check import make

x, y, z = sp.symbols('x y z', real=True)
UR = (x**2 + y**2 - z**3)**2 - z**8 + x * z**8
c = 1.5
Y = sp.Matrix([c * x / z, c * y / z, 1])
f = make(UR, Y)
beta, a0 = 8, 1.0
for delta in (0.05, 0.01):
    for rho in (0.01, 0.002, 0.0005):
        worst, cnt, wp = np.inf, 0, None
        umax = 2 * np.sqrt(delta) * rho  # (|b|^2-1)^2 ~ 4u^2 <= delta rho^2
        for phi in np.linspace(0, 2 * np.pi, 73)[:-1]:
            for u in np.linspace(-umax, umax, 41):
                b1, b2 = (1 + u) * np.cos(phi), (1 + u) * np.sin(phi)
                X, Yc = rho**c * b1, rho**c * b2
                Uv, gU, Yv, JY = f(X, Yc, rho)
                gU = np.array(gU, float).ravel(); Yv = np.array(Yv, float).ravel(); JY = np.array(JY, float)
                W = Uv + a0 * rho**beta
                K = delta * rho**beta - W
                if K < 0:
                    continue
                h = Yv @ Yv
                lam = np.sqrt(2 * (-Uv - K) / h)
                e1 = np.cross(Yv, [0.0, 0.0, 1.0]); e1 /= np.linalg.norm(e1)
                e2 = np.cross(Yv, e1); e2 /= np.linalg.norm(e2)
                for th in np.linspace(0, 2 * np.pi, 12, endpoint=False):
                    v = -lam * Yv + np.sqrt(2 * K) * (np.cos(th) * e1 + np.sin(th) * e2)
                    p = v @ Yv; DvY = JY @ v
                    pdot = -(gU @ Yv) + v @ DvY; hdot = 2 * (Yv @ DvY)
                    Xi = -(p / h) * pdot + p * p / (2 * h * h) * hdot + (a0 * beta - beta * delta) * rho**(beta - 1) * v[2]
                    val = (rho / lam) * Xi / (delta * rho**beta)
                    cnt += 1
                    if val < worst:
                        worst, wp = val, (phi, u / rho, K / (delta * rho**beta), th)
        print(f'ring: delta={delta}, rho={rho}: points={cnt}, min (rho/lam)Xi/(delta rho^8) = {worst:.4f} '
              f'at (phi, u/rho, K/(d rho^8), theta) = {tuple(round(float(t), 3) for t in wp)}')
