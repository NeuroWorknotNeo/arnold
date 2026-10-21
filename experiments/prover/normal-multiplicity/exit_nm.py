# [Эксперимент] Строгий выход (A5) теоремы A [results/007] для поворачивающейся полярной карты
# теоремы N записки notes/prover/2026-10-21-normal-multiplicity.md на примерах M1 (вырожденный,
# квартичный нормальный профиль e^4) и M2 (невырожденный профиль после сдвига на eps_0(theta)).
# Xi = d/dt (V - delta rho^beta) считается прямым численным дифференцированием вдоль поля
# (q, v) -> (v, -grad U), без формулы (1.3) [007]. Печатается минимум (rho/lambda) Xi / (delta rho^beta)
# по точкам множества выхода {q in closure D, E = 0, p < 0, V = delta rho^beta}:
#   b = (theta, e) в Omega_delta = {Q < 2 delta}, W <= delta rho^beta, K_perp = delta rho^beta - W,
#   направление v_perp ⟂ Y перебирается по окружности.
# Запуск: python exit_nm.py M1   |   python exit_nm.py M2
import sys
import random
import sympy as sp
import mpmath as mp

mp.mp.dps = 30
x, y, z = sp.symbols('x y z', real=True)
name = sys.argv[1] if len(sys.argv) > 1 else 'M1'
if name == 'M1':
    U = (z - x**2)**4 + x**5 + y**5 + x*y**6 + y*x**6
    beta = mp.mpf(5); cw = mp.mpf(5)/4
    th_star = -mp.pi/2
    Gfun = lambda t: mp.sin(t)**5 + mp.cos(t)**5            # t — полярный угол
    e0fun = lambda t: mp.mpf(0)                               # eps_0 = 0
    e0p = lambda t: mp.mpf(0)
    Pfun = lambda t, e: e**4                                  # профиль: Phi_0(t, eps_0 + e) - G(t)
    p0 = mp.mpf(1)
else:
    U = z**4 + z*(x**4 + x**3*y + y**4) + x**6 + x*z**5 + 2*y*z**5
    beta = mp.mpf(16)/3; cw = mp.mpf(4)/3
    ffun = lambda t: mp.cos(t)**4 + mp.cos(t)**3*mp.sin(t) + mp.sin(t)**4
    th_star = mp.atan(mp.findroot(lambda t: 4*t**3 - 3*t**2 - 4*t + 1, mp.mpf('0.2237')))
    e0fun = lambda t: -mp.cbrt(ffun(t)/4)
    fpfun = lambda t: -4*mp.cos(t)**3*mp.sin(t) - 3*mp.cos(t)**2*mp.sin(t)**2 + mp.cos(t)**4 + 4*mp.sin(t)**3*mp.cos(t)
    e0p = lambda t: -fpfun(t)/(12*mp.cbrt(ffun(t)/4)**2)       # d eps_0 / d theta
    Gfun = lambda t: e0fun(t)**4 + ffun(t)*e0fun(t)
    Pfun = lambda t, e: e**2*((e + 2*e0fun(t))**2 + 2*e0fun(t)**2)
    p0 = 6*e0fun(th_star)**2

Uf = sp.lambdify((x, y, z), U, 'mpmath')
gU = [sp.lambdify((x, y, z), sp.diff(U, v), 'mpmath') for v in (x, y, z)]
a0 = -Gfun(th_star)
Gpp = mp.diff(Gfun, th_star, 2)
lam0 = Gpp/4

def eta0(s, t):                                    # дно: eta_0 = s^c eps_0(theta)
    return s**cw*e0fun(th_star + t)

def frame(t):                                      # omega, l, n для полярного угла th_star + t
    ph = th_star + t
    return ([mp.cos(ph), mp.sin(ph), mp.mpf(0)], [-mp.sin(ph), mp.cos(ph), mp.mpf(0)], [mp.mpf(0), mp.mpf(0), mp.mpf(1)])

def point(xv, t, e):
    w, l, n = frame(t)
    eta = eta0(xv, t) + xv**cw*e
    return [xv*w[i] + eta*n[i] for i in range(3)]

def Yfield(q, kap):
    s = mp.sqrt(q[0]**2 + q[1]**2)
    t = mp.atan2(q[1], q[0]) - th_star
    while t > mp.pi: t -= 2*mp.pi
    while t < -mp.pi: t += 2*mp.pi
    w, l, n = frame(t)
    # nu = eta_0,s - kappa theta eta_0,theta / s,  eta_0 = s^c eps_0(theta* + theta)
    nu = cw*s**(cw - 1)*e0fun(th_star + t) - kap*t*s**cw*e0p(th_star + t)/s
    return [w[i] - kap*t*l[i] + nu*n[i] for i in range(3)], s     # k_g = 0 (большой круг)

def Vminus(q, v, kap, delta):
    Y, rho = Yfield(q, kap)
    h = sum(c*c for c in Y)
    p = sum(v[i]*Y[i] for i in range(3))
    return sum(c*c for c in v)/2 - p**2/(2*h) + Uf(*q) + a0*rho**beta - delta*rho**beta

def Q(t, e):
    return Gfun(th_star + t) - Gfun(th_star) + Pfun(th_star + t, e)

def scan(kap, delta, sigma, npts, nang=16, seed=3):
    rnd = random.Random(seed)
    Th = mp.sqrt(2*delta/lam0)*mp.mpf('1.3')
    E = (4*delta/p0)**(1/(2*float(1 if name == 'M2' else 2)))*mp.mpf('1.3')
    worst = None; cnt = 0; tries = 0
    while cnt < npts and tries < 50*npts:
        tries += 1
        xv = mp.mpf(sigma)*(mp.mpf(rnd.random())**2 + mp.mpf('1e-4'))
        t = (2*rnd.random() - 1)*Th; e = (2*rnd.random() - 1)*E
        if Q(t, e) >= 2*delta:
            continue
        # с вероятностью 1/2 сдвигаем точку на стенку W = delta x^beta (луч от b = 0)
        q = point(xv, t, e)
        W = Uf(*q) + a0*xv**beta
        if rnd.random() < 0.5:
            def Wm(lmb):
                qq = point(xv, lmb*t, lmb*e)
                return Uf(*qq) + a0*xv**beta - delta*xv**beta
            if Wm(1) < 0 and Q(2*t, 2*e) < 2*delta and Wm(2) > 0:
                lo, hi = mp.mpf(1), mp.mpf(2)
                for _ in range(60):
                    mid = (lo + hi)/2
                    if Wm(mid) < 0: lo = mid
                    else: hi = mid
                t, e = lo*t, lo*e
                q = point(xv, t, e); W = Uf(*q) + a0*xv**beta
        if W > delta*xv**beta:
            continue
        K = delta*xv**beta - W
        Y, rho = Yfield(q, kap)
        h = sum(c*c for c in Y); Yn = mp.sqrt(h)
        a = [mp.mpf(1), mp.mpf(0), mp.mpf(0)] if abs(Y[0]) < mp.mpf('0.9')*Yn else [mp.mpf(0), mp.mpf(1), mp.mpf(0)]
        u1 = [a[i] - sum(a[k]*Y[k] for k in range(3))/h*Y[i] for i in range(3)]
        nn = mp.sqrt(sum(c*c for c in u1)); u1 = [c/nn for c in u1]
        u2 = [Y[1]*u1[2] - Y[2]*u1[1], Y[2]*u1[0] - Y[0]*u1[2], Y[0]*u1[1] - Y[1]*u1[0]]
        nn = mp.sqrt(sum(c*c for c in u2)); u2 = [c/nn for c in u2]
        vpar = mp.sqrt(-2*Uf(*q) - 2*K)
        gq = [g(*q) for g in gU]
        for k in range(nang if K > 0 else 1):
            al = 2*mp.pi*k/nang
            vp = [mp.sqrt(2*K)*(mp.cos(al)*u1[i] + mp.sin(al)*u2[i]) for i in range(3)]
            v = [-vpar*Y[i]/Yn + vp[i] for i in range(3)]
            fl = lambda tt: Vminus([q[i] + tt*v[i] for i in range(3)], [v[i] - tt*gq[i] for i in range(3)], kap, delta)
            Xi = mp.diff(fl, 0)
            lam = vpar/Yn
            val = rho/lam*Xi/(delta*rho**beta)
            chk = abs(Vminus(q, v, kap, delta))/(delta*rho**beta)
            if chk > mp.mpf('1e-15'):
                raise RuntimeError('точка не на множестве выхода: %s' % chk)
            if worst is None or val < worst[0]:
                worst = (val, xv, t, e, K/(delta*rho**beta))
        cnt += 1
    return worst, cnt

if __name__ == '__main__':
    print('пример', name, ': beta =', mp.nstr(beta, 6), ', c =', mp.nstr(cw, 6), ', theta* =', mp.nstr(th_star, 12),
          ', a0 = -G =', mp.nstr(a0, 10), ', G\'\' =', mp.nstr(Gpp, 10), ', lambda0 = G\'\'/4 =', mp.nstr(lam0, 8))
    print('контроль: в каждой точке |V - delta rho^beta|/(delta rho^beta) < 1e-15 (иначе остановка)')
    grid = [(0.05, 0.05), (0.01, 0.01), (0.002, 0.001)]
    kaps = [0.0, 0.017, 0.05, 0.2, 0.5]
    if len(sys.argv) > 2 and sys.argv[2] == 'deep':
        # очень малые x: поправки Пюизё ~ x^(1/N) (у M2 N = 3) должны стать << kappa sqrt(delta)
        mp.mp.dps = 50
        grid = [(0.01, 1e-4), (0.01, 1e-6), (0.01, 1e-8), (0.01, 1e-10), (0.01, 1e-12), (0.01, 1e-18), (0.01, 1e-24), (0.002, 1e-30)]
        kaps = [0.0, 0.0178, 0.05, 0.2]
    for kap in kaps:
        for (delta, sigma) in grid:
            (wv, cnt) = scan(mp.mpf(kap), mp.mpf(delta), sigma, 120)
            print('kappa=%-6g delta=%-6g sigma=%-6g (%d точек): min (rho/lambda)Xi/(delta rho^beta) = %-10s'
                  ' [x=%s, theta=%s, e=%s, K/(delta rho^beta)=%s]' % (kap, delta, sigma, cnt, mp.nstr(wv[0], 5),
                  mp.nstr(wv[1], 3), mp.nstr(wv[2], 3), mp.nstr(wv[3], 3), mp.nstr(wv[4], 3)))
