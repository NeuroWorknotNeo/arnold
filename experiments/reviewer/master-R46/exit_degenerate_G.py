"""R46: [Эксперимент] строгий выход (A5) для поля теоремы MT в примере к следствию 6.8
(вырожденный минимум эффективного потенциала, q = 2, нормальная кратность 4).

Не доказательство. Запуск: ~/venv/bin/python exit_degenerate_G.py

U = z^4 + x^5 + (5/2) x^3 y^2   (n = 3).
Дуга: большой круг z = 0, omega = (cos th, sin th, 0), n = e_z, k_g = 0, y_0 = 0.
Около th = pi:  t := th - pi,  f(th) := u_5(omega) = -cos^3 t (1 + 1.5 sin^2 t) = -1 + (15/8) t^4 + O(t^6).
(NF): U(s omega + s^{5/4} e e_z) = s^5 (e^4 + f),  beta = 5, c = 5/4, a0 = 1, r' = 2, p = 1, G = f.
Поле MT при xi = (kappa t, c e):  Y = omega - kappa t ell  (не зависит от z).
Ляпунов: W = U + s^5, V = K_perp + W.  Точки (A5): calW(t,e) := e^4 + f + 1 <= delta, E = 0, p < 0,
V = delta s^5.  Вычисляем Xi = dV/dt - beta delta rho^{beta-1} drho/dt прямым дифференцированием
вдоль поля системы (не через лемму 1) и печатаем min (rho/lambda) Xi / (delta rho^beta).
По MT при kappa <~ delta / R_t^2 и малом s эта величина >= kappa/4 > 0.
"""
import sympy as sp
import mpmath as mp
import random

mp.mp.dps = 40
x, y, z, vx, vy, vz, kap = sp.symbols('x y z vx vy vz kappa', real=True)
q = sp.Matrix([x, y, z]); v = sp.Matrix([vx, vy, vz])
U = z**4 + x**5 + sp.Rational(5, 2)*x**3*y**2
s = sp.sqrt(x**2 + y**2)
t = sp.atan2(-y, -x)                      # t = th - pi, непрерывен около th = pi
om = sp.Matrix([x/s, y/s, 0]); ell = sp.Matrix([-y/s, x/s, 0])
Y = om - kap*t*ell
h = (Y.T*Y)[0, 0]
p = (v.T*Y)[0, 0]
beta = 5
V = sp.Rational(1, 2)*(v.T*v)[0, 0] - p**2/(2*h) + U + s**beta
gradU = sp.Matrix([sp.diff(U, c) for c in (x, y, z)])
Vdot = sum(sp.diff(V, c)*vc for c, vc in zip((x, y, z), (vx, vy, vz))) \
     - sum(sp.diff(V, vc)*gc for vc, gc in zip((vx, vy, vz), gradU))
rhodot = sum(sp.diff(s, c)*vc for c, vc in zip((x, y, z), (vx, vy, vz)))
dl = sp.symbols('delta', positive=True)
Xi = Vdot - beta*dl*s**(beta-1)*rhodot
fXi = sp.lambdify((x, y, z, vx, vy, vz, kap, dl), Xi, 'mpmath')
fY = sp.lambdify((x, y, z, kap), list(Y), 'mpmath')

def f_of_t(tt):
    return -mp.cos(tt)**3*(1 + mp.mpf(3)/2*mp.sin(tt)**2)

def calW(tt, e):
    return e**4 + f_of_t(tt) + 1

def sample_exit(delta, kappa, sval, rng):
    # (t,e) с calW <= delta (компонента у нуля), граница и внутренность
    while True:
        tt = mp.mpf(rng.uniform(-1, 1))*mp.mpf(1.2)*(delta)**mp.mpf(0.25)
        e = mp.mpf(rng.uniform(-1, 1))*mp.mpf(1.2)*(delta)**mp.mpf(0.25)
        if calW(tt, e) <= delta:
            break
    if rng.random() < 0.3:   # выдвинуть на границу calW = delta (K_perp = 0)
        lo, hi = mp.mpf(0), mp.mpf(3)
        for _ in range(80):
            mid = (lo+hi)/2
            if calW(tt*mid, e*mid) <= delta: lo = mid
            else: hi = mid
        tt, e = tt*lo, e*lo
    X = -sval*mp.cos(tt); Yc = -sval*mp.sin(tt); Z = sval**(mp.mpf(5)/4)*e
    Yv = mp.matrix(fY(X, Yc, Z, kappa))
    hh = sum(Yv[i]**2 for i in range(3))
    Wv = sval**5*calW(tt, e)
    Kp = delta*sval**5 - Wv
    if Kp < 0: Kp = mp.mpf(0)
    # базис Y^perp
    a1 = mp.matrix([0, 0, 1])
    a2 = mp.matrix([-Yv[1], Yv[0], 0]); n2 = mp.sqrt(sum(a2[i]**2 for i in range(3))); a2 = a2/n2
    phi = rng.uniform(0, 2*3.141592653589793)
    vp = (mp.cos(phi)*a1 + mp.sin(phi)*a2)*mp.sqrt(2*Kp)
    pp = -mp.sqrt(2*hh*(1-delta)*sval**5)
    vv = (pp/hh)*Yv + vp
    lam = -pp/hh
    xi_val = fXi(X, Yc, Z, vv[0], vv[1], vv[2], kappa, delta)
    return (sval/lam)*xi_val/(delta*sval**5), (tt, e, Kp/(delta*sval**5), phi)

rng = random.Random(46)
print('min (rho/lambda) Xi / (delta rho^beta) по выборке точек (A5)')
for delta in (mp.mpf('0.01'), mp.mpf('0.001')):
    Rt = (4*delta/(mp.mpf(15)/16))**mp.mpf(0.25)
    print('delta =', delta, ' R_t ~', mp.nstr(Rt, 3), ' delta/R_t^2 ~', mp.nstr(delta/Rt**2, 3))
    for kappa in ('0', '1e-4', '1e-3', '1e-2', '3e-2', '0.1', '0.3'):
        kappa = mp.mpf(kappa)
        for sval in (mp.mpf('1e-4'), mp.mpf('1e-8'), mp.mpf('1e-12')):
            vals = [sample_exit(delta, kappa, sval, rng) for _ in range(400)]
            mn = min(vals, key=lambda r: r[0])
            print('  kappa=%-6s s=%-6s  min=% .4e  (kappa/4=%.2e)  at t=%s e=%s K/dr^b=%s' % (
                mp.nstr(kappa, 2), mp.nstr(sval, 1), float(mn[0]), float(kappa/4),
                mp.nstr(mn[1][0], 3), mp.nstr(mn[1][1], 3), mp.nstr(mn[1][2], 3)))
