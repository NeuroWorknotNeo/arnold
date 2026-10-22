# [Эксперимент] Двухуровневая локализация в складке O2 (записка notes/prover/2026-10-21-fold.md, §7):
# A(rho) = rho^6 + rho^7 (глубина в складке -s^6 - s^7), уровень delta rho^7, rho = s,
# поле Y = Pi_s - (X^th/s) Pi_theta - (X^eps/s) Pi_eps с X = mu' (theta d_theta + (eps/2) d_eps) (сжатие к складке вдоль овала),
# область D = {s < sigma, W < delta s^7}, W = U + s^6 + s^7 = s^6 f^2 + s^7 G(theta), окрестность складки theta = 0.
# Xi = d/dt (V - delta rho^7) — численно; печатается min (rho/lambda) Xi/(delta rho^7) (нужно > 0).
# Ожидание (§7): отрицательно и растёт по модулю как s^(-1/2).
import random
import sympy as sp
import mpmath as mp

mp.mp.dps = 50
x, y, z = sp.symbols('x y z', real=True)
rho2 = x**2 + y**2
# складка theta = 0 у O2 эквивалентна складке theta = pi после замены x -> -x; берём U с отражённым x^7,
# чтобы минимум следующего порядка был в theta = 0: U' = (z^2 - y rho^2)^2 - rho^6 - x^7 + y^7
U = (z**2 - y*rho2)**2 - rho2**3 - x**7 + y**7
Uf = sp.lambdify((x, y, z), U, 'mpmath')
gU = [sp.lambdify((x, y, z), sp.diff(U, v), 'mpmath') for v in (x, y, z)]
cw = mp.mpf(3)/2


def point(s, th, e):
    return [s*mp.cos(th), s*mp.sin(th), s**cw*e]


def coords(q):
    s = mp.sqrt(q[0]**2 + q[1]**2)
    return s, mp.atan2(q[1], q[0]), q[2]/s**cw


def Yfield(q, mup):
    s, th, e = coords(q)
    Xt, Xe = mup*th, mup*e/2
    nu = s**(cw - 1)*(cw*e - Xe)
    return [mp.cos(th) + Xt*mp.sin(th), mp.sin(th) - Xt*mp.cos(th), nu], s


def Wf(q):
    s = mp.sqrt(q[0]**2 + q[1]**2)
    return Uf(*q) + s**6 + s**7


def Vminus(q, v, mup, delta):
    Y, rho = Yfield(q, mup)
    h = sum(c*c for c in Y)
    p = sum(v[i]*Y[i] for i in range(3))
    return sum(c*c for c in v)/2 - p**2/(2*h) + Wf(q) - delta*rho**7


def scan(mup, delta, sigma, npts, nang=16, seed=2):
    rnd = random.Random(seed)
    worst = None
    cnt = 0
    while cnt < npts:
        s = mp.mpf(sigma)*(mp.mpf(rnd.random()) + mp.mpf('0.1'))
        e = (2*rnd.random() - 1)*mp.mpf(delta)**mp.mpf('0.25')*mp.mpf('0.9')
        th = mp.asin(e**2) + (2*rnd.random() - 1)*mp.sqrt(delta*s)
        q = point(s, th, e)
        W = Wf(q)
        if W >= delta*s**7:
            continue
        K = delta*s**7 - W
        Y, rho = Yfield(q, mup)
        h = sum(c*c for c in Y)
        Yn = mp.sqrt(h)
        a = [mp.mpf(0), mp.mpf(0), mp.mpf(1)]
        u1 = [a[i] - sum(a[k]*Y[k] for k in range(3))/h*Y[i] for i in range(3)]
        nn = mp.sqrt(sum(c*c for c in u1)); u1 = [c/nn for c in u1]
        u2 = [Y[1]*u1[2] - Y[2]*u1[1], Y[2]*u1[0] - Y[0]*u1[2], Y[0]*u1[1] - Y[1]*u1[0]]
        nn = mp.sqrt(sum(c*c for c in u2)); u2 = [c/nn for c in u2]
        vpar = mp.sqrt(-2*Uf(*q) - 2*K)
        gq = [gg(*q) for gg in gU]
        for kk in range(nang):
            al = 2*mp.pi*kk/nang
            vp = [mp.sqrt(2*K)*(mp.cos(al)*u1[i] + mp.sin(al)*u2[i]) for i in range(3)]
            v = [-vpar*Y[i]/Yn + vp[i] for i in range(3)]
            fl = lambda tt: Vminus([q[i] + tt*v[i] for i in range(3)], [v[i] - tt*gq[i] for i in range(3)], mup, delta)
            Xi = mp.diff(fl, 0)
            val = rho/(vpar/Yn)*Xi/(delta*rho**7)
            if abs(Vminus(q, v, mup, delta))/(delta*rho**7) > mp.mpf('1e-15'):
                raise RuntimeError('не на множестве выхода')
            if worst is None or val < worst[0]:
                worst = (val, s, th, e, K/(delta*rho**7))
        cnt += 1
    return worst


print('O2 у складки, двухуровневая схема: A = rho^6 + rho^7, уровень delta rho^7, X = mu\'(theta, eps/2)')
for delta in [0.01]:
    for sigma in [1e-4, 1e-6, 1e-8]:
        for mup in [0.05, 0.2]:
            wv = scan(mp.mpf(mup), mp.mpf(delta), sigma, 40)
            print('delta=%-5g sigma=%-6g mu\'=%-5g: min (rho/lam)Xi/(delta rho^7) = %-11s [s=%s, theta=%s, eps=%s, K/(d rho^7)=%s]'
                  % (delta, sigma, mup, mp.nstr(wv[0], 5), mp.nstr(wv[1], 3), mp.nstr(wv[2], 3), mp.nstr(wv[3], 3), mp.nstr(wv[4], 3)))
