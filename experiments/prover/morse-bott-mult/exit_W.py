# [Эксперимент] Строгий выход (A5) теоремы A [results/007] для конструкции теоремы W записки
# notes/prover/2026-10-21-morse-bott-mult.md, теорема W (§2, доказательство — §5): поле
#     Y = Psi_s - (kappa theta / s) Psi_theta + lambda (zeta / s) Psi_zeta,   lambda = c - w kappa,
# область D = {Psi(s, theta, s^c e): s < sigma, P(theta, e) < 4 delta, W < delta s^beta}, A(rho) = a0 rho^beta.
# Xi = d/dt (V - delta rho^beta) считается прямым численным дифференцированием вдоль поля (q,v) -> (v, -grad U).
# Печатается минимум (rho/lambda_v) Xi / (delta rho^beta) по точкам множества выхода
# {q in closure D, E = 0, p < 0, V = delta rho^beta}; направление v_perp ⟂ Y перебирается по окружности.
# Сравниваются поле теоремы W (lambda = c - w kappa) и «наивное» поле теоремы Mb (lambda = 0, вес нормали c).
# Запуск: python exit_W.py W3 | W1 | W2
import sys
import random
import sympy as sp
import mpmath as mp

mp.mp.dps = 30
x, y, z = sp.symbols('x y z', real=True)
name = sys.argv[1] if len(sys.argv) > 1 else 'W3'
rho2 = x**2 + y**2
if name == 'W3':
    U = z**4 + z**2*y*rho2 - rho2**3 + y**2*rho2**2 + x*z**5 + y**7
    beta = mp.mpf(6); cw = mp.mpf(3)/2; a0 = mp.mpf(1); th0 = mp.mpf(0); wgt = mp.mpf(1)/2
    epsb = lambda ph: mp.mpf(0); epsbp = lambda ph: mp.mpf(0)
    P = lambda t, e: e**4 + mp.sin(t)*e**2 + mp.sin(t)**2
elif name == 'W1':
    U = (z - x**2)**4 + sp.Rational(3, 2)*x*rho2**2 - sp.Rational(1, 2)*x**3*rho2 + y*z**5
    beta = mp.mpf(5); cw = mp.mpf(5)/4; a0 = mp.mpf(1); th0 = mp.pi; wgt = mp.mpf(1)
    epsb = lambda ph: mp.mpf(0); epsbp = lambda ph: mp.mpf(0)
    G = lambda ph: mp.cos(ph)*(3 - mp.cos(ph)**2)/2
    P = lambda t, e: G(th0 + t) + 1 + e**4
else:  # W2
    f4 = 6*rho2**2 + 4*(x**2 - y**2)*rho2 - (x**4 - 6*x**2*y**2 + y**4)
    U = z**4 + z*f4 + x**6 + y*z**5
    beta = mp.mpf(16)/3; cw = mp.mpf(4)/3; th0 = mp.mpf(0); wgt = mp.mpf(1)
    ff = lambda ph: 9 - 8*mp.sin(ph)**4
    ffp = lambda ph: -32*mp.sin(ph)**3*mp.cos(ph)
    epsb = lambda ph: -mp.cbrt(ff(ph)/4)
    epsbp = lambda ph: -ffp(ph)/(12*mp.cbrt(ff(ph)/4)**2)
    Gb = lambda ph: epsb(ph)**4 + ff(ph)*epsb(ph)
    a0 = -Gb(th0)
    P = lambda t, e: (Gb(th0 + t) + a0) + e**2*((e + 2*epsb(th0 + t))**2 + 2*epsb(th0 + t)**2)

Uf = sp.lambdify((x, y, z), U, 'mpmath')
gU = [sp.lambdify((x, y, z), sp.diff(U, v), 'mpmath') for v in (x, y, z)]


def frame(t):
    ph = th0 + t
    return ([mp.cos(ph), mp.sin(ph), mp.mpf(0)], [-mp.sin(ph), mp.cos(ph), mp.mpf(0)], [mp.mpf(0), mp.mpf(0), mp.mpf(1)])


def eta0(s, t):
    return s**cw*epsb(th0 + t)


def point(s, t, e):
    w, l, n = frame(t)
    eta = eta0(s, t) + s**cw*e
    return [s*w[i] + eta*n[i] for i in range(3)]


def coords(q):
    s = mp.sqrt(q[0]**2 + q[1]**2)
    t = mp.atan2(q[1], q[0]) - th0
    while t > mp.pi:
        t -= 2*mp.pi
    while t < -mp.pi:
        t += 2*mp.pi
    return s, t


def Yfield(q, kap, lam):
    s, t = coords(q)
    w, l, n = frame(t)
    zeta = q[2] - eta0(s, t)
    e0s = cw*s**(cw - 1)*epsb(th0 + t)
    e0t = s**cw*epsbp(th0 + t)
    nut = e0s - kap*t*e0t/s + lam*zeta/s
    return [w[i] - kap*t*l[i] + nut*n[i] for i in range(3)], s     # k_g = 0 (экватор)


def Vminus(q, v, kap, lam, delta):
    Y, rho = Yfield(q, kap, lam)
    h = sum(c*c for c in Y)
    p = sum(v[i]*Y[i] for i in range(3))
    return sum(c*c for c in v)/2 - p**2/(2*h) + Uf(*q) + a0*rho**beta - delta*rho**beta


def scan(kap, lam, delta, sigma, npts, Th, E, nang=16, seed=5):
    rnd = random.Random(seed)
    worst = None
    cnt = 0
    tries = 0
    while cnt < npts and tries < 200*npts:
        tries += 1
        s = mp.mpf(sigma)*(mp.mpf(rnd.random())**2 + mp.mpf('1e-3'))
        t = (2*rnd.random() - 1)*Th
        e = (2*rnd.random() - 1)*E
        if P(t, e) >= 4*delta:
            continue
        q = point(s, t, e)
        W = Uf(*q) + a0*s**beta
        if rnd.random() < 0.5:        # сдвиг на стенку W = delta s^beta вдоль луча от b = 0
            def Wm(lmb):
                return Uf(*point(s, lmb*t, lmb*e)) + a0*s**beta - delta*s**beta
            if Wm(1) < 0 and P(2*t, 2*e) < 4*delta and Wm(2) > 0:
                lo, hi = mp.mpf(1), mp.mpf(2)
                for _ in range(80):
                    mid = (lo + hi)/2
                    if Wm(mid) < 0:
                        lo = mid
                    else:
                        hi = mid
                t, e = lo*t, lo*e
                q = point(s, t, e)
                W = Uf(*q) + a0*s**beta
        if W > delta*s**beta:
            continue
        K = delta*s**beta - W
        Y, rho = Yfield(q, kap, lam)
        h = sum(c*c for c in Y)
        Yn = mp.sqrt(h)
        a = [mp.mpf(1), mp.mpf(0), mp.mpf(0)] if abs(Y[0]) < mp.mpf('0.9')*Yn else [mp.mpf(0), mp.mpf(1), mp.mpf(0)]
        u1 = [a[i] - sum(a[k]*Y[k] for k in range(3))/h*Y[i] for i in range(3)]
        nn = mp.sqrt(sum(c*c for c in u1))
        u1 = [c/nn for c in u1]
        u2 = [Y[1]*u1[2] - Y[2]*u1[1], Y[2]*u1[0] - Y[0]*u1[2], Y[0]*u1[1] - Y[1]*u1[0]]
        nn = mp.sqrt(sum(c*c for c in u2))
        u2 = [c/nn for c in u2]
        vpar = mp.sqrt(-2*Uf(*q) - 2*K)
        gq = [gg(*q) for gg in gU]
        for k in range(nang if K > 0 else 1):
            al = 2*mp.pi*k/nang
            vp = [mp.sqrt(2*K)*(mp.cos(al)*u1[i] + mp.sin(al)*u2[i]) for i in range(3)]
            v = [-vpar*Y[i]/Yn + vp[i] for i in range(3)]
            fl = lambda tt: Vminus([q[i] + tt*v[i] for i in range(3)], [v[i] - tt*gq[i] for i in range(3)], kap, lam, delta)
            Xi = mp.diff(fl, 0)
            lamv = vpar/Yn
            val = rho/lamv*Xi/(delta*rho**beta)
            chk = abs(Vminus(q, v, kap, lam, delta))/(delta*rho**beta)
            if chk > mp.mpf('1e-12'):
                raise RuntimeError('точка не на множестве выхода: %s' % chk)
            if worst is None or val < worst[0]:
                worst = (val, s, t, e, K/(delta*rho**beta))
        cnt += 1
    return worst, cnt


if __name__ == '__main__':
    print('пример', name, ': beta =', mp.nstr(beta, 6), ', c =', mp.nstr(cw, 6), ', theta0 =', mp.nstr(th0, 8),
          ', a0 =', mp.nstr(a0, 10), ', w =', mp.nstr(wgt, 4))
    print('контроль: в каждой точке |V - delta rho^beta|/(delta rho^beta) < 1e-12 (иначе остановка)')
    deep = len(sys.argv) > 2 and sys.argv[2] == 'deep'
    if deep:
        # глубокий режим: поправки s^(c-1) (член lambda zeta/s, наклон дна) должны стать << kappa sqrt(delta)
        mp.mp.dps = 60
    if name == 'W3':
        cases = [(0.01, 1e-4), (0.002, 1e-5)] if not deep else [(0.01, 1e-12), (0.002, 1e-16)]
        kaps = [0.05, 0.1, 0.2]
    elif name == 'W1':
        cases = [(0.01, 1e-3), (0.002, 1e-4)] if not deep else [(0.01, 1e-16), (0.01, 1e-24), (0.002, 1e-24)]
        kaps = [0.02, 0.05, 0.1, 0.2]
    else:
        cases = [(0.01, 1e-6), (0.002, 1e-8)] if not deep else [(0.01, 1e-20), (0.01, 1e-30), (0.002, 1e-30)]
        kaps = [0.02, 0.05, 0.1, 0.2]
    for (delta, sigma) in cases:
        # прямоугольник, содержащий Omega_delta: ищем грубо
        Th = mp.mpf('0.01'); E = mp.mpf('0.01')
        while any(P(Th*u, E*v) < 4*delta for u in (-1, 1) for v in (-1, 0, 1)) or \
                any(P(Th*u, E*v) < 4*delta for u in (-1, 0, 1) for v in (-1, 1)):
            Th *= mp.mpf('1.2'); E *= mp.mpf('1.2')
        for kap in kaps:
            for lamname, lam in (('W: lambda = c - w kappa', cw - wgt*mp.mpf(kap)), ('Mb: lambda = 0', mp.mpf(0))):
                (wv, cnt) = scan(mp.mpf(kap), lam, mp.mpf(delta), sigma, 150, Th, E)
                print('delta=%-6g sigma=%-6g kappa=%-5g %-24s (%d точек): min (rho/lam)Xi/(delta rho^beta) = %-11s'
                      ' [s=%s, theta=%s, e=%s, K/(delta rho^beta)=%s]' % (delta, sigma, kap, lamname, cnt,
                      mp.nstr(wv[0], 5), mp.nstr(wv[1], 3), mp.nstr(wv[2], 3), mp.nstr(wv[3], 3), mp.nstr(wv[4], 3)))
