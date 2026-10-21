"""R42: численная проверка оценок шагов 4, 6, 7 теоремы II (V=0) на точках D_sigma.
[Эксперимент]. Точки: x>0, y<0, H^2+x^6+y^6 <= 2 delta z^6 (как в п. 3), z in (0, sigma].
"""
import numpy as np
import sympy as sp

x, y, z, e = sp.symbols('x y z e', real=True)
Yabs = -y
g = x*Yabs/(x+Yabs)
zxi = sp.Matrix([(3-e)*g, -(3-e)*g]) - e*z**3*sp.Matrix([y, x])/(x**2+y**2)
xi = zxi/z
Yv = sp.Matrix([xi[0], xi[1], 1])
DY = Yv.jacobian([x, y, z])
H = x*y + z**3
W = H**2 + x**6 + y**6
YW = (sp.Matrix([W]).jacobian([x, y, z])*Yv)[0]
L2 = 6*W - z*YW - 2*e*W
fxi = sp.lambdify((x, y, z, e), xi, 'numpy')
fDY = sp.lambdify((x, y, z, e), DY, 'numpy')
fL2 = sp.lambdify((x, y, z, e), L2, 'numpy')

rng = np.random.default_rng(1)
for delta in (1/32, 0.01):
    for ev in (0.1, 0.5):
        worst_xi = worst_L2 = worst_th3 = worst_DYY = -np.inf
        n = 0
        while n < 20000:
            zz = 10**rng.uniform(-6, np.log10(1/18))
            # параметризация: H = h z^3, |h|<=sqrt(2delta); x|y| = (1-h) z^3; u = x/|y| произвольно
            h = rng.uniform(-1, 1)*np.sqrt(2*delta)
            P = (1-h)*zz**3
            lu = rng.uniform(-12, 12)
            u = np.exp(lu)
            Yab = np.sqrt(P/u); xx = u*Yab
            if h**2*zz**6 + xx**6 + Yab**6 > 2*delta*zz**6:
                continue
            yy = -Yab
            n += 1
            xv = np.array(fxi(xx, yy, zz, ev), dtype=float).ravel()
            worst_xi = max(worst_xi, np.linalg.norm(xv)/np.sqrt(zz) - 3)
            l2 = fL2(xx, yy, zz, ev)
            bound = -3250*zz**9 - 6*ev*(2*delta)**(2/3)*zz**7
            worst_L2 = max(worst_L2, (bound - l2)/zz**7)
            M = np.array(fDY(xx, yy, zz, ev), dtype=float)
            Yvec = np.array([xv[0], xv[1], 1.0])
            DYY = zz*M@Yvec
            worst_DYY = max(worst_DYY, np.linalg.norm(DYY)/np.sqrt(zz) - 19)
            # w ⊥ Y: базис ортогонального дополнения
            Q, _ = np.linalg.qr(np.column_stack([Yvec, np.eye(3)[:, :2]]))
            Bp = Q[:, 1:3]
            S = zz*Bp.T@((M+M.T)/2)@Bp
            mineig = np.min(np.linalg.eigvalsh(S))
            th3 = (3-ev)*(np.sqrt(2)-1)/2 + ev + 4*np.sqrt(zz)
            worst_th3 = max(worst_th3, -mineig - th3)
        print(f'delta={delta:.4f} e={ev}: max(|xi|/sqrt z - 3)={worst_xi:.3e}, '
              f'max((bound-L2)/z^7)={worst_L2:.3e}, max(|zD_YY|/sqrt z-19)={worst_DYY:.3e}, '
              f'max(-mineig - theta3bound)={worst_th3:.3e}')
# фактический theta_3 при u -> infinity: собственное значение симметричной части
for ev in (0.1, 0.5):
    print('limit eigenvalue (3-e)(1-sqrt2)/2 =', (3-ev)*(1-np.sqrt(2))/2)
