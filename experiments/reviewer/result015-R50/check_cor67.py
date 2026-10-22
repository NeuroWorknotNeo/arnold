# R50: численная проверка данных следствия 6.7 (теорема II [013] через теорему H),
# results/015-master.md, §9, 6.7. [Эксперимент]: U = U_II (V = 0), поле (3) [013],
# случайные точки русла {theta in K, W <= delta}, z мало.
import numpy as np
import sympy as sp

x, y, z, e = sp.symbols('x y z e', real=True)
ay = -y                                  # |y| в квадранте y < 0
g = x*ay/(x + ay)
zxi = sp.Matrix([(3 - e)*g, -(3 - e)*g]) - e*z**3*sp.Matrix([y, x])/(x**2 + y**2)
xi = zxi/z
Y = sp.Matrix([xi[0], xi[1], 1])
q = sp.Matrix([x, y, z])
DY = Y.jacobian(q)                       # D_w Y = DY w
DYY = DY*Y
Dxy_zxi = zxi.jacobian([x, y])
eta = sp.Rational(1, 2)
H = x*y + z**3
U = H**2 + x**6 + y**6 - (1 - eta)*z**6
W = U + (1 - eta)*z**6
gradW = sp.Matrix([W]).jacobian(q).T
zYW = z*(gradW.T*Y)[0]
# s d_s v|_theta: v(z,theta) = xi(z theta, z) - theta; z d/dz при фиксированном theta
th1, th2 = sp.symbols('th1 th2', real=True)
v_th = sp.Matrix([xi[0], xi[1]]).subs({x: z*th1, y: z*th2}, simultaneous=True) - sp.Matrix([th1, th2])
zdzv = (z*sp.diff(v_th, z)).subs({th1: x/z, th2: y/z}, simultaneous=True)

f = sp.lambdify((x, y, z, e), [xi, DY, DYY, Dxy_zxi, W, zYW, zdzv], 'numpy')

rng = np.random.default_rng(3)
results = {}
for ev in [0.5, 0.25, 0.05]:
    m = (3 - ev)*(np.sqrt(2) - 1)/2 + ev
    for delta in [1/32, 1/100]:
        worst = dict(xi=0, v=0, v_claim=0, psi=0, symmin=np.inf, direct=np.inf, H6=np.inf, zdzv=0, theta=0)
        cnt = 0
        while cnt < 4000:
            zz = 10**rng.uniform(-6, -2)
            Hh = rng.uniform(-1, 1)*np.sqrt(delta)*zz**3
            uu = np.exp(rng.uniform(-np.log(1e4), np.log(1e4)))
            xy_abs = zz**3 - Hh
            ya = np.sqrt(xy_abs/uu); xx = uu*ya; yy = -ya
            if not (0 < xx < zz and -zz < yy < 0):
                continue
            Wv = (Hh**2 + xx**6 + yy**6)
            if Wv > delta*zz**6:
                continue
            cnt += 1
            xiv, DYv, DYYv, Dxyv, Wn, zYWv, zdzvv = f(xx, yy, zz, ev)
            xiv = np.array(xiv, float).ravel(); DYv = np.array(DYv, float); DYYv = np.array(DYYv, float).ravel()
            Dxyv = np.array(Dxyv, float); zdzvv = np.array(zdzvv, float).ravel()
            th = np.array([xx/zz, yy/zz])
            vv = xiv - th
            worst['xi'] = max(worst['xi'], np.linalg.norm(xiv)/np.sqrt(zz))
            worst['v'] = max(worst['v'], np.linalg.norm(vv))
            worst['theta'] = max(worst['theta'], np.linalg.norm(th))
            worst['v_claim'] = max(worst['v_claim'], np.linalg.norm(vv) - (3*np.sqrt(zz) + (2*delta)**(1/6)))
            psi = zz*DYYv[:2]               # горизонтальная часть z D_Y Y (вертикальная = 0)
            worst['psi'] = max(worst['psi'], 2*np.linalg.norm(psi)/np.sqrt(zz))
            S = (Dxyv + Dxyv.T)/2
            worst['symmin'] = min(worst['symmin'], np.linalg.eigvalsh(S).min() + m)   # >= 0 ожидается
            # прямой минимум z <w, D_w Y> по единичным w ⊥ Y
            Yv = np.array([xiv[0], xiv[1], 1.0])
            Q, _ = np.linalg.qr(np.column_stack([Yv, rng.normal(size=3), rng.normal(size=3)]))
            Bp = Q[:, 1:3]                  # ортонормированный базис Y^perp
            M = zz*Bp.T @ DYv @ Bp
            worst['direct'] = min(worst['direct'], np.linalg.eigvalsh((M + M.T)/2).min() + m)
            # (H6): (6W - zYW - mu W)/z^6 >= -chi(z), mu = 2e; печатаем min of (...)/z (ожидается O(1))
            val = (6*Wn - zYWv - 2*ev*Wn)/zz**6
            worst['H6'] = min(worst['H6'], val/zz)
            worst['zdzv'] = max(worst['zdzv'], np.linalg.norm(zdzvv))
        results[(ev, delta)] = worst
        print(f'e={ev}, delta={delta:.4f}: max|xi|/sqrt z={worst["xi"]:.3f} (<=3?), max|v|={worst["v"]:.3f} (<1?), '
              f'max|theta|={worst["theta"]:.3f}, max(|v|-(3sqrt z+(2d)^(1/6)))={worst["v_claim"]:.2e}, '
              f'max 2|psi|/sqrt z={worst["psi"]:.2f} (<=38?), min(eig sym Dxy(z xi))+m={worst["symmin"]:.3e} (>=0?), '
              f'min(z<w,D_wY>)+m={worst["direct"]:.3e}, min (6W-zYW-2eW)/z^7={worst["H6"]:.2f}, '
              f'max|z d_z v|_theta|={worst["zdzv"]:.2f}')
