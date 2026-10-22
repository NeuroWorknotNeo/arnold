# R50: к следствию 6.4' — геометрия поля xi = (kappa theta, c2 e) в трубчатой калибровке при c2 > c.
# [Эксперимент]: малый круг на S^2 (k_g != 0), приближённое дно eta0 = s*y0, y0 = 0.3 s sin(theta).
# Поле в координатах (s, theta, zeta), zeta = s^c e:  Y = Psi_s - (kappa theta/s) Psi_theta + (c-c2)(zeta/s) Psi_zeta
# (формула (0.9) [014] с lambda_n = c - c2). Производные точные (sympy -> numpy).
# Считаем min по единичным w ⊥ Y величины s<w, D_w Y> и сравниваем с min(0, c - c2) (узкий блок N0 = c - c2).
import numpy as np
import sympy as sp

s, th, zt, kap, lam = sp.symbols('s theta zeta kappa lambda_n', real=True)
phi0 = sp.Rational(2, 5)
Rr = sp.cos(phi0)
ps = th/Rr
om = sp.Matrix([sp.cos(phi0)*sp.cos(ps), sp.cos(phi0)*sp.sin(ps), sp.sin(phi0)])
ell = sp.diff(om, th)
n = om.cross(ell)
eta0 = s*sp.Rational(3, 10)*s*sp.sin(th)
Psi = s*om + (eta0 + zt)*n
J = Psi.jacobian([s, th, zt])
Ycoord = sp.Matrix([1, -kap*th/s, lam*zt/s])
Y = J*Ycoord                                    # Y как функция координат
DYc = Y.jacobian([s, th, zt])                   # dY/d(coords)
fJ = sp.lambdify((s, th, zt, kap, lam), J, 'numpy')
fY = sp.lambdify((s, th, zt, kap, lam), Y, 'numpy')
fD = sp.lambdify((s, th, zt, kap, lam), DYc, 'numpy')

rng = np.random.default_rng(11)
for c, c2 in [(1.5, 1.5), (1.5, 1.0), (1.5, 2.0), (1.5, 2.5), (2.0, 3.2), (3.0, 4.4)]:
    worst = np.inf
    for _ in range(2000):
        sv = 10**rng.uniform(-6, -3); tv = rng.uniform(-0.05, 0.05); ev = rng.uniform(-0.1, 0.1); kv = 0.01
        zv = sv**c*ev
        Jn = np.array(fJ(sv, tv, zv, kv, c - c2), float)
        Yn = np.array(fY(sv, tv, zv, kv, c - c2), float).ravel()
        DY = np.array(fD(sv, tv, zv, kv, c - c2), float) @ np.linalg.inv(Jn)
        Q, _ = np.linalg.qr(np.column_stack([Yn, rng.normal(size=3), rng.normal(size=3)]))
        B = Q[:, 1:3]
        M = sv*B.T @ DY @ B
        worst = min(worst, np.linalg.eigvalsh((M + M.T)/2).min())
    print(f'c={c}, c2={c2}: min_w s<w,D_wY> = {worst:.4f},  min(0, c-c2) = {min(0, c-c2):.4f}')
