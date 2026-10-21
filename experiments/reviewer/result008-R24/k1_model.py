"""R24: численная проверка условий (Phi1)-(Phi3) [007] для декартовой карты (7.1) теоремы K1. [Эксперимент]

Та же модель, что в k2_model.py: параллель широты alpha=3/5 (k_g = tan alpha), eta* = s^2 a1 + s^3 a2.
Проверяется: ||B - I|| -> 0, |B_xu| -> 0, X|(Phi_XX)^perp| - 7 kbar |b|^2 -> (<= 0 + o(1)),
-X<w, D_w Y> - 7 kbar |b| -> (<= 0 + o(1)) для единичных w perp Phi_X (C1 = 7 kbar, §7).
Производные — в декартовых координатах (Y(q) = d_X Phi o Phi^{-1} через явное обращение карты).
"""
import sympy as sp
import mpmath as mp
import random

mp.mp.dps = 60
random.seed(7)
alpha = sp.Rational(3, 5)
ca, sa = sp.cos(alpha), sp.sin(alpha)
kgv = sp.tan(alpha)
th, S = sp.symbols('theta s', real=True)
a1 = sp.Rational(7, 10) + sp.Rational(3, 10) * sp.sin(th)
a2 = -sp.Rational(1, 2) * sp.cos(th)
estar = S ** 2 * a1 + S ** 3 * a2
c_ = sp.Rational(5, 2)
phi = th / ca
om = sp.Matrix([ca * sp.cos(phi), ca * sp.sin(phi), sa])
ell = sp.Matrix([-sp.sin(phi), sp.cos(phi), 0])
nn = sp.Matrix([-sa * sp.cos(phi), -sa * sp.sin(phi), ca])

X, Yd, z = sp.symbols('X Y_d zeta', real=True)
r = sp.sqrt(X ** 2 + Yd ** 2)
thXY = sp.atan(Yd / X)
Phi = (S * om + (estar + z) * nn).subs(th, thXY).subs(S, r)
PX = Phi.diff(X)
PXX = PX.diff(X)
J = Phi.jacobian(sp.Matrix([X, Yd, z]))
B = J.T * J

q1, q2, q3 = sp.symbols('q1 q2 q3', real=True)
rxy = sp.sqrt(q1 ** 2 + q2 ** 2)
s_q = rxy * ca + q3 * sa
eta_q = -rxy * sa + q3 * ca
th_q = sp.atan2(q2, q1) * ca
X_q = s_q * sp.cos(th_q)
Y_q = s_q * sp.sin(th_q)
z_q = eta_q - estar.subs({S: s_q, th: th_q})
Yfield = PX.subs({X: X_q, Yd: Y_q, z: z_q})
JY = Yfield.jacobian(sp.Matrix([q1, q2, q3]))

fPhi = sp.lambdify((X, Yd, z), Phi, 'mpmath')
fPX = sp.lambdify((X, Yd, z), PX, 'mpmath')
fPXX = sp.lambdify((X, Yd, z), PXX, 'mpmath')
fB = sp.lambdify((X, Yd, z), B, 'mpmath')
fY = sp.lambdify((q1, q2, q3), Yfield, 'mpmath')
fJY = sp.lambdify((q1, q2, q3), JY, 'mpmath')
kbar = mp.mpf(sp.N(abs(kgv), 50))
C1 = 7 * kbar


def v3(M):
    return mp.matrix([M[i] for i in range(3)])


def dot(a, b):
    return sum(a[i] * b[i] for i in range(3))


def unit_perp(Yv):
    while True:
        w = mp.matrix([mp.mpf(random.gauss(0, 1)) for _ in range(3)])
        w = w - dot(w, Yv) / dot(Yv, Yv) * Yv
        nrm = mp.sqrt(dot(w, w))
        if nrm > 1e-6:
            return w / nrm


print('k_g =', mp.nstr(kbar, 6), ' C1 = 7 kbar =', mp.nstr(C1, 6))
for Xe in [mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4'), mp.mpf('1e-5')]:
    mBI = mBxu = R2 = R3 = mY = mp.mpf(-10)
    for _ in range(200):
        while True:
            t_, e_ = random.uniform(-0.25, 0.25), random.uniform(-0.25, 0.25)
            if t_ * t_ + e_ * e_ < 0.0625:
                break
        t_, e_ = mp.mpf(t_), mp.mpf(e_)
        Yv_ = t_ * Xe
        zz = e_ * Xe ** c_
        bn = mp.sqrt(t_ ** 2 + e_ ** 2)
        P = v3(fPhi(Xe, Yv_, zz))
        Px = v3(fPX(Xe, Yv_, zz))
        Pxx = v3(fPXX(Xe, Yv_, zz))
        Bm = fB(Xe, Yv_, zz)
        BI = Bm - mp.eye(3)
        mBI = max(mBI, mp.norm(BI, 2) if False else max(abs(BI[i, k]) for i in range(3) for k in range(3)) * 3)
        mBxu = max(mBxu, mp.sqrt(Bm[0, 1] ** 2 + Bm[0, 2] ** 2))
        Yv = v3(fY(*P))
        mY = max(mY, mp.sqrt(dot(Yv - Px, Yv - Px)))
        perp = Pxx - dot(Pxx, Px) / dot(Px, Px) * Px
        R2 = max(R2, Xe * mp.sqrt(dot(perp, perp)) - C1 * bn ** 2)
        JYm = fJY(*P)
        for _k in range(3):
            w = unit_perp(Px)
            R3 = max(R3, -(Xe * dot(w, JYm * w)) - C1 * bn)
    print(f'  X={mp.nstr(Xe, 2):>6}: |YoPhi-Phi_X|={mp.nstr(mY, 3):>9}  3max|B-I|={mp.nstr(mBI, 4):>10}  '
          f'|B_xu|={mp.nstr(mBxu, 4):>10}  res(Phi2)={mp.nstr(R2, 4):>11}  res(Phi3)={mp.nstr(R3, 4):>11}')
