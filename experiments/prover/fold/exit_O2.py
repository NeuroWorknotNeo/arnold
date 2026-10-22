# [Эксперимент] Строгий выход (A5) теоремы A [results/007] для конструкции теоремы X / C_Gamma
# записки notes/prover/2026-10-21-fold.md на примере O2:
#   U = z^4 - 2 z^2 y rho^2 - x^2 rho^4 + x^7 + y^7,   rho^2 = x^2 + y^2,
# карта Pi(s,theta,eps) = (s cos theta, s sin theta, s^(3/2) eps), U o Pi = s^6 [(eps^2 - sin theta)^2 - 1 + s g(theta)],
# поле Y = Pi_s - (X^th/s) Pi_theta - (X^eps/s) Pi_eps с
#   X^th  = mu' * chi(theta) tan(theta) / 2,
#   X^eps = mu' * (eps^2 - (1 - chi(theta)) sin theta) / (4 eps),
# так что X f = (mu'/2) f для f = eps^2 - sin theta и X P = mu' P, P = f^2 (овал дна Gamma = {f = 0}).
# rho = s, A(rho) = rho^6, beta = 6. Область D = {Pi(s,theta,eps): s < sigma, f^2 < 4 delta, f^2 + s g < delta}.
# Xi = d/dt (V - delta rho^beta) считается прямым численным дифференцированием вдоль поля (q,v) -> (v, -grad U)
# в точках множества выхода {q in closure D, E = 0, p < 0, V = delta rho^beta}; v_perp ⟂ Y перебирается по окружности.
# Печатается минимум (rho/lambda) Xi / (delta rho^beta) (нужно > 0) и для сравнения mu' (выигрыш Эйлера).
# Запуск: ~/venv/bin/python exit_O2.py [deep | normal]   (normal — отрицательный контроль)
import sys
import random
import sympy as sp
import mpmath as mp

deep = len(sys.argv) > 1 and sys.argv[1] == 'deep'
mp.mp.dps = 60 if (deep or (len(sys.argv) > 1 and sys.argv[1] == 'normal')) else 40
x, y, z = sp.symbols('x y z', real=True)
rho2 = x**2 + y**2
U = z**4 - 2*z**2*y*rho2 - x**2*rho2**2 + x**7 + y**7
beta = mp.mpf(6); cw = mp.mpf(3)/2; a0 = mp.mpf(1)
Uf = sp.lambdify((x, y, z), U, 'mpmath')
gU = [sp.lambdify((x, y, z), sp.diff(U, v), 'mpmath') for v in (x, y, z)]


def psi(t):          # гладкая ступенька: 0 при t <= 0, 1 при t >= 1
    if t <= 0:
        return mp.mpf(0)
    if t >= 1:
        return mp.mpf(1)
    a, b = mp.exp(-1/t), mp.exp(-1/(1 - t))
    return a/(a + b)


def chi(th):         # 1 при dist(theta,{0,pi}) <= pi/8, 0 при dist >= pi/4
    d = min(abs(th), abs(th - mp.pi))
    return 1 - psi((d - mp.pi/8)/(mp.pi/8))


MODE = 'X'


def Xfield(th, e, mup):
    if MODE == 'normal':      # отрицательный контроль: нормальное поле X = (mu'/2) f grad f/|grad f|^2, X^th зависит от eps
        f = e**2 - mp.sin(th)
        g1, g2 = -mp.cos(th), 2*e
        n2 = g1**2 + g2**2
        return mup*f*g1/(2*n2), mup*f*g2/(2*n2)
    ch = chi(th)
    Xt = mup*ch*mp.tan(th)/2 if ch > 0 else mp.mpf(0)
    if ch == 1:
        Xe = mup*e/4
    else:
        Xe = mup*(e**2 - (1 - ch)*mp.sin(th))/(4*e)
    return Xt, Xe


def point(s, th, e):
    return [s*mp.cos(th), s*mp.sin(th), s**cw*e]


def coords(q):
    s = mp.sqrt(q[0]**2 + q[1]**2)
    th = mp.atan2(q[1], q[0])
    if th < -mp.pi/2:
        th += 2*mp.pi
    return s, th, q[2]/s**cw


def Yfield(q, mup):
    s, th, e = coords(q)
    Xt, Xe = Xfield(th, e, mup)
    w = [mp.cos(th), mp.sin(th), mp.mpf(0)]
    l = [-mp.sin(th), mp.cos(th), mp.mpf(0)]
    nu = s**(cw - 1)*(cw*e - Xe)
    return [w[i] - Xt*l[i] + (nu if i == 2 else 0) for i in range(3)], s


def Vminus(q, v, mup, delta):
    Y, rho = Yfield(q, mup)
    h = sum(cc*cc for cc in Y)
    p = sum(v[i]*Y[i] for i in range(3))
    return sum(cc*cc for cc in v)/2 - p**2/(2*h) + Uf(*q) + a0*rho**beta - delta*rho**beta


def gamma_pt(e0, branch):   # точка овала Gamma и единичная нормаль к нему в плоскости (theta, eps)
    th = mp.asin(e0**2) if branch == 0 else mp.pi - mp.asin(e0**2)
    g = [-mp.cos(th), 2*e0]
    ng = mp.sqrt(g[0]**2 + g[1]**2)
    return th, e0, [g[0]/ng, g[1]/ng]


def scan(mup, delta, sigma, npts, nang=12, seed=3, fold_frac=0.6):
    rnd = random.Random(seed)
    worst = None
    cnt = 0
    while cnt < npts:
        s = mp.mpf(sigma)*(mp.mpf(rnd.random())**2 + mp.mpf('1e-3'))
        if rnd.random() < fold_frac:
            e0 = (2*rnd.random() - 1)*mp.mpf('0.4')
        else:
            e0 = (2*rnd.random() - 1)
        branch = rnd.randint(0, 1)
        th0, ee0, nrm = gamma_pt(e0, branch)
        # r: сдвиг по нормали; f ~ r |grad f|; ищем точку с f^2 < 4 delta
        rmax = mp.mpf(0)
        r = mp.mpf('1e-4')
        sg = 1 if rnd.random() < 0.5 else -1

        def pt(rr):
            return th0 + sg*rr*nrm[0], ee0 + sg*rr*nrm[1]

        def fval(rr):
            th, e = pt(rr)
            return e**2 - mp.sin(th)
        while fval(r)**2 < 4*delta and r < 1:
            rmax = r
            r *= mp.mpf('1.3')
        rr = rmax*mp.mpf(rnd.random())

        def Wm(rr):
            th, e = pt(rr)
            return Uf(*point(s, th, e)) + a0*s**beta - delta*s**beta
        if Wm(rr) > 0:
            continue
        if rnd.random() < 0.5 and Wm(rmax) > 0:   # на стенку W = delta s^beta
            lo, hi = rr, rmax
            for _ in range(90):
                mid = (lo + hi)/2
                if Wm(mid) < 0:
                    lo = mid
                else:
                    hi = mid
            rr = lo
        th, e = pt(rr)
        if chi(th) < 1 and abs(e) < mp.mpf('0.2'):
            continue
        q = point(s, th, e)
        W = Uf(*q) + a0*s**beta
        if W > delta*s**beta:
            continue
        K = delta*s**beta - W
        Y, rho = Yfield(q, mup)
        h = sum(cc*cc for cc in Y)
        Yn = mp.sqrt(h)
        a = [mp.mpf(0), mp.mpf(0), mp.mpf(1)]
        u1 = [a[i] - sum(a[k]*Y[k] for k in range(3))/h*Y[i] for i in range(3)]
        nn = mp.sqrt(sum(cc*cc for cc in u1))
        u1 = [cc/nn for cc in u1]
        u2 = [Y[1]*u1[2] - Y[2]*u1[1], Y[2]*u1[0] - Y[0]*u1[2], Y[0]*u1[1] - Y[1]*u1[0]]
        nn = mp.sqrt(sum(cc*cc for cc in u2))
        u2 = [cc/nn for cc in u2]
        vpar = mp.sqrt(-2*Uf(*q) - 2*K)
        gq = [gg(*q) for gg in gU]
        for kk in range(nang if K > 0 else 1):
            al = 2*mp.pi*kk/nang
            vp = [mp.sqrt(2*K)*(mp.cos(al)*u1[i] + mp.sin(al)*u2[i]) for i in range(3)]
            v = [-vpar*Y[i]/Yn + vp[i] for i in range(3)]
            fl = lambda tt: Vminus([q[i] + tt*v[i] for i in range(3)], [v[i] - tt*gq[i] for i in range(3)], mup, delta)
            Xi = mp.diff(fl, 0)
            lamv = vpar/Yn
            val = rho/lamv*Xi/(delta*rho**beta)
            chk = abs(Vminus(q, v, mup, delta))/(delta*rho**beta)
            if chk > mp.mpf('1e-12'):
                raise RuntimeError('точка не на множестве выхода: %s' % chk)
            if worst is None or val < worst[0]:
                worst = (val, s, th, e, K/(delta*rho**beta))
        cnt += 1
    return worst, cnt


if __name__ == '__main__' and len(sys.argv) > 1 and sys.argv[1] == 'normal':
    MODE = 'normal'
    print('ОТРИЦАТЕЛЬНЫЙ КОНТРОЛЬ: X = (mu/2) f grad f/|grad f|^2 (X f = (mu/2) f, но X^theta зависит от eps)')
    for (delta, sigma) in [(0.01, 1e-6), (0.01, 1e-10), (0.01, 1e-14)]:
        for mup in [0.02, 0.1]:
            (wv, cnt) = scan(mp.mpf(mup), mp.mpf(delta), sigma, 60)
            print('delta=%-6g sigma=%-6g mu\'=%-6g (%d точек): min (rho/lam)Xi/(delta rho^beta) = %-11s'
                  ' [s=%s, theta=%s, eps=%s, K/(delta rho^beta)=%s]' % (delta, sigma, mup, cnt,
                  mp.nstr(wv[0], 5), mp.nstr(wv[1], 3), mp.nstr(wv[2], 4), mp.nstr(wv[3], 4), mp.nstr(wv[4], 3)))
    sys.exit(0)

if __name__ == '__main__':
    print('O2: beta = 6, c = 3/2, a0 = 1; поле теоремы X с X P = mu\' P')
    print('контроль: в каждой точке |V - delta rho^beta|/(delta rho^beta) < 1e-12 (иначе остановка)')
    cases = [(0.01, 1e-8), (0.002, 1e-10)] if not deep else [(0.01, 1e-16), (0.002, 1e-20)]
    for (delta, sigma) in cases:
        for mup in [0.0, 0.002, 0.02, 0.1, 0.4]:
            (wv, cnt) = scan(mp.mpf(mup), mp.mpf(delta), sigma, 120)
            print('delta=%-6g sigma=%-6g mu\'=%-6g (%d точек): min (rho/lam)Xi/(delta rho^beta) = %-11s'
                  ' [s=%s, theta=%s, eps=%s, K/(delta rho^beta)=%s]' % (delta, sigma, mup, cnt,
                  mp.nstr(wv[0], 5), mp.nstr(wv[1], 3), mp.nstr(wv[2], 4), mp.nstr(wv[3], 4), mp.nstr(wv[4], 3)))
