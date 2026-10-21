"""R43: численная проверка (3.2), (3.4), (3.5) results/014 в R^3 на сферической кривой
с переменной геодезической кривизной k_g(theta) = 0.3 + 0.5 sin(theta) (репер получен
интегрированием уравнений Дарбу, mpmath taylor ODE), дно eta0 = s*y0(s^(1/3),theta),
y0(sigma,theta) = sigma^2 (0.7 cos theta + 0.2 sigma).  [Эксперимент]
Производные поля Y в R^3 берутся численно: Y∘Psi как функция (s,theta,zeta),
D_wY = sum_i a^i d_i(Y∘Psi), a = (DPsi)^{-1} w.
"""
import mpmath as mp

mp.mp.dps = 50


def fd(f, x, h):
    return (-f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)) / (12*h)


def fd2(f, x, h):
    return (-f(x + 2*h) + 16*f(x + h) - 30*f(x) + 16*f(x - h) - f(x - 2*h)) / (12*h*h)


kfun = lambda t: mp.mpf('0.3') + mp.mpf('0.5') * mp.sin(t)
# начальный репер
w0 = [mp.mpf(1), 0, 0]
l0 = [0, mp.mpf(1), 0]
n0 = [0, 0, mp.mpf(1)]  # n = omega x ell


def rhs(t, Y):
    o, l, n = Y[0:3], Y[3:6], Y[6:9]
    k = kfun(t)
    return [l[0], l[1], l[2],
            -o[0] + k * n[0], -o[1] + k * n[1], -o[2] + k * n[2],
            -k * l[0], -k * l[1], -k * l[2]]


sol = mp.odefun(rhs, 0, w0 + l0 + n0)


def frame(t):
    Y = sol(t)
    return Y[0:3], Y[3:6], Y[6:9]


Nn = 3
y0 = lambda sig, t: sig**2 * (mp.mpf('0.7') * mp.cos(t) + mp.mpf('0.2') * sig)
eta0 = lambda s, t: s * y0(s ** (mp.mpf(1) / Nn), t)

kap = mp.mpf('0.37')
lam = mp.mpf('0.61')


def Psi(s, t, z):
    o, l, n = frame(t)
    e = eta0(s, t) + z
    return [s * o[i] + e * n[i] for i in range(3)]


def Yfield(s, t, z):
    # Y = Psi_s - kap*t/s*Psi_t + lam*z/s*Psi_z  (численно)
    Ps = [fd(lambda x: Psi(x, t, z)[i], s, mp.mpf('1e-12')) for i in range(3)]
    Pt = [fd(lambda x: Psi(s, x, z)[i], t, mp.mpf('1e-12')) for i in range(3)]
    o, l, n = frame(t)
    return [Ps[i] - kap * t / s * Pt[i] + lam * z / s * n[i] for i in range(3)]


def jac(f, x):
    cols = []
    for j in range(3):
        def fj(u, j=j):
            xx = list(x)
            xx[j] = u
            return f(*xx)
        cols.append([fd(lambda u: fj(u)[i], x[j], mp.mpf('1e-7')) for i in range(3)])
    return mp.matrix([[cols[j][i] for j in range(3)] for i in range(3)])


s, t, z = mp.mpf('0.02'), mp.mpf('0.15'), mp.mpf('0.0004')
o, l, n = frame(t)
# Проверка ортонормированности репера
print('frame orth err', max(abs(mp.fdot(o, l)), abs(mp.fdot(o, n)), abs(mp.fdot(l, n)), abs(mp.fdot(o, o) - 1)))

k = kfun(t)
kp = fd(kfun, t, mp.mpf('1e-10'))
e0 = eta0(s, t)
e0s = fd(lambda x: eta0(x, t), s, mp.mpf('1e-10'))
e0t = fd(lambda x: eta0(s, x), t, mp.mpf('1e-10'))
e0ss = fd2(lambda x: eta0(x, t), s, mp.mpf('1e-8'))
e0st = fd(lambda y: fd(lambda x: eta0(x, y), s, mp.mpf('1e-10')), t, mp.mpf('1e-8'))
e0tt = fd2(lambda x: eta0(s, x), t, mp.mpf('1e-8'))
eta = e0 + z
eps = k * eta / s
nut = e0s - kap * t * e0t / s + lam * z / s
sde = k * e0s - eps
dte = (kp * eta + k * e0t) / s
dtn = e0st - kap * e0t / s - kap * t * e0tt / s
sdn = s * e0ss - kap * t * (e0st - e0t / s) - lam * z / s

Y = Yfield(s, t, z)
Yc = [o[i] - kap * t * (1 - eps) * l[i] + nut * n[i] for i in range(3)]
print('(3.2) Y err', max(abs(Y[i] - Yc[i]) for i in range(3)))
print('(3.2) h err', abs(mp.fdot(Y, Y) - (1 + kap**2 * t**2 * (1 - eps)**2 + nut**2)))

J_Y = jac(Yfield, (s, t, z))           # d(Y∘Psi)/d(s,t,z)
J_P = jac(Psi, (s, t, z))              # DPsi
# D_Y Y: коэффициенты Y в координатах (1, -kap t/s, lam z/s)
aY = mp.matrix([1, -kap * t / s, lam * z / s])
DYY = J_Y * aY
sDYY = [s * DYY[i] for i in range(3)]
comp = [mp.fdot(sDYY, o), mp.fdot(sDYY, l), mp.fdot(sDYY, n)]
cl = [-kap**2 * t**2 * (1 - eps),
      kap * t * (sde - 1 + kap * (1 - eps) - kap * t * dte + nut * k + lam * k * z / s),
      sdn + kap**2 * t**2 * (1 - eps) * k - kap * t * dtn + lam**2 * z / s]
print('(3.4) err', max(abs(comp[i] - cl[i]) for i in range(3)))

import random
random.seed(1)
maxerr = 0
for trial in range(5):
    wc = [mp.mpf(random.uniform(-1, 1)) for _ in range(3)]
    w = [wc[0] * o[i] + wc[1] * l[i] + wc[2] * n[i] for i in range(3)]
    a = mp.lu_solve(J_P, mp.matrix(w))
    DwY = J_Y * a
    lhs = s * mp.fdot([DwY[i] for i in range(3)], w)
    wo, wl, wn = wc
    az = wn - wo * e0s - wl * e0t / (s * (1 - eps))
    rhs = ((1 / (1 - eps) - kap) * wl**2 + kap * t * wo * wl
           + ((kap * t * dte - nut * k) * wl**2 + dtn * wl * wn) / (1 - eps)
           + wo * (kap * t * sde * wl + sdn * wn)
           - kap * t * k * wl * (wo * e0s + wl * e0t / (s * (1 - eps)))
           + lam * az * wn)
    maxerr = max(maxerr, abs(lhs - rhs))
print('(3.5) max err over 5 random w', maxerr)
