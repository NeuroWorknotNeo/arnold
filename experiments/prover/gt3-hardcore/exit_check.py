# [Эксперимент] Строгий выход (A5) для поворачивающейся полярной карты (теорема 4 записки
# notes/prover/2026-10-21-gt3-hardcore.md) на примере теоремы B: U = (x^2+y^2-z^2)^2 + x z^4,
# луч omega* = omega(phi=pi) на верхней окружности, j = 5, G'' + 5G < 0 (декартова карта не годится).
# Xi = d/dt (V - delta rho^j) вычисляется прямым численным дифференцированием вдоль поля
# (q,v) -> (v, -grad U), без формулы (3.3). Печатается min (rho/lambda) Xi / (delta rho^j)
# по случайным точкам границы {V = delta rho^j, E = 0, pi < 0} над трубкой.
import sys
import random
import sympy as sp
import mpmath as mp
from reduced import fiber_series, x, y, z, s

mp.mp.dps = 30
ph = sp.symbols('phi', real=True)
om = [sp.cos(ph)/sp.sqrt(2), sp.sin(ph)/sp.sqrt(2), 1/sp.sqrt(2)]
nv = [-sp.cos(ph)/sp.sqrt(2), -sp.sin(ph)/sp.sqrt(2), 1/sp.sqrt(2)]
Q0 = x**2 + y**2 - z**2
EX = sys.argv[1] if len(sys.argv) > 1 else 'thmB'
if EX == 'thmB':
    U = Q0**2 + x*z**4; m = 4; j = 5; phi0 = mp.pi
elif EX == 'curved':
    U = (Q0 + z**3)**2 + x*z**6 + x*y*z**5 + z**7/2; m = 4; j = 7; phi0 = 5*mp.pi/6
elif EX == 'shift':
    U = Q0**2 + 2*Q0*z**2*x - z**6/10; m = 4; j = 6; phi0 = mp.mpf(0)
ys, R = fiber_series(U, m, om, [nv], 4)
G = sp.simplify(R.coeff(s, j - m))
c = mp.mpf(j - m + 2)/2
Gf = sp.lambdify(ph, G, 'mpmath')
a0 = -Gf(phi0)
etas_expr = sp.expand(s*ys[0])                         # eta*(s, phi)
eta_f = sp.lambdify((s, ph), etas_expr, 'mpmath')
eta_s = sp.lambdify((s, ph), sp.diff(etas_expr, s), 'mpmath')
eta_p = sp.lambdify((s, ph), sp.diff(etas_expr, ph), 'mpmath')   # d/dphi; d/dtheta = sqrt2 d/dphi
Uf = sp.lambdify((x, y, z), U, 'mpmath')
gU = [sp.lambdify((x, y, z), sp.diff(U, v), 'mpmath') for v in (x, y, z)]
hn = mp.mpf(8)
S2 = mp.sqrt(2)

def frame(phv):
    w = [mp.cos(phv)/S2, mp.sin(phv)/S2, 1/S2]
    T = [-mp.sin(phv), mp.cos(phv), mp.mpf(0)]
    n = [-mp.cos(phv)/S2, -mp.sin(phv)/S2, 1/S2]
    return w, T, n

def chart_inv(q):
    Rr = mp.sqrt(q[0]**2 + q[1]**2)
    sv = (Rr + q[2])/S2
    eta = (q[2] - Rr)/S2
    phv = mp.atan2(q[1], q[0])
    if phv < 0 and phi0 > 1:
        phv += 2*mp.pi
    return sv, phv, eta

def Yfield(q, kap):
    sv, phv, eta = chart_inv(q)
    th = (phv - phi0)/S2
    w, T, n = frame(phv)
    eps = eta/sv                                      # k = 1
    p = eta_s(sv, phv) - kap*th*S2*eta_p(sv, phv)/sv
    return [w[i] - kap*th*(1 - eps)*T[i] + p*n[i] for i in range(3)], sv

def Vfun(q, v, kap, delta):
    Y, rho = Yfield(q, kap)
    h = sum(t*t for t in Y)
    pi_ = sum(v[i]*Y[i] for i in range(3))
    return (sum(t*t for t in v)/2 - pi_**2/(2*h) + Uf(*q) + a0*rho**j) - delta*rho**j

def point(xv, th, e, kap):
    phv = phi0 + S2*th
    w, T, n = frame(phv)
    eta = eta_f(xv, phv) + xv**c*e
    return [xv*w[i] + eta*n[i] for i in range(3)]

def sample(kap, delta, sigma, N, seed=0):
    random.seed(seed)
    lam0 = min(2*mp.mpf(float(sp.diff(G, ph, 2).subs(ph, float(phi0)))), hn)/4
    Rb = 2*mp.sqrt(delta/lam0)
    worst = None; npts = 0
    while npts < N:
        xv = sigma*mp.mpf(random.random())**2 + mp.mpf('1e-6')
        if npts % 2 == 0:
            # точка на стенке трубки: W = delta rho^j, K = 0 (самый опасный случай)
            al = 2*mp.pi*random.random()
            dth, de = mp.cos(al), mp.sin(al)*mp.sqrt(lam0*4/hn)
            def Wm(t):
                qq = point(xv, t*dth, t*de, kap)
                return Uf(*qq) + a0*xv**j - delta*xv**j     # rho = s = x на карте
            lo, hi = mp.mpf(0), 2*Rb
            if Wm(hi) < 0:
                continue
            for _ in range(80):
                mid = (lo + hi)/2
                if Wm(mid) < 0: lo = mid
                else: hi = mid
            th, e = lo*dth, lo*de
        else:
            th = (2*random.random() - 1)*Rb; e = (2*random.random() - 1)*Rb
        q = point(xv, th, e, kap)
        Y, rho = Yfield(q, kap)
        W = Uf(*q) + a0*rho**j
        if W > delta*rho**j:
            continue
        K = max(delta*rho**j - W, mp.mpf(0))  # поперечная кинетическая энергия на границе
        # случайный единичный вектор, ортогональный Y
        r = [mp.mpf(random.gauss(0, 1)) for _ in range(3)]
        h = sum(t*t for t in Y)
        r = [r[i] - sum(r[k]*Y[k] for k in range(3))/h*Y[i] for i in range(3)]
        nr = mp.sqrt(sum(t*t for t in r)); r = [t/nr for t in r]
        vp = [mp.sqrt(2*K)*t for t in r]
        lam_ = mp.sqrt(-2*Uf(*q) - 2*K)     # |v_parallel|
        Yn = mp.sqrt(h)
        v = [-lam_*Y[i]/Yn + vp[i] for i in range(3)]
        gq = [g(*q) for g in gU]
        f = lambda t: Vfun([q[i] + t*v[i] for i in range(3)], [v[i] - t*gq[i] for i in range(3)], kap, delta)
        Xi = mp.diff(f, 0)
        lam = lam_/Yn                        # lambda = -pi/h
        val = rho/lam*Xi/(delta*rho**j)
        npts += 1
        if worst is None or val < worst[0]:
            worst = (val, xv, th, e, K/(delta*rho**j))
    return worst

if __name__ == '__main__':
    print('пример', EX, ': j =', j, ', a0 = -G(phi*) =', mp.nstr(a0, 8))
    for kap in [0.0, 0.007, 0.05, 0.2, 0.5]:
        for (delta, sigma) in [(0.01, 0.05), (0.002, 0.02)]:
            wv = sample(mp.mpf(kap), mp.mpf(delta), mp.mpf(sigma), 600, seed=1)
            print('kappa=%-6g delta=%-6g sigma=%-5g: min (rho/lambda)Xi/(delta rho^j) = %s'
                  '  [x=%s, theta=%s, e=%s, K/(delta rho^j)=%s]' % (kap, delta, sigma,
                  mp.nstr(wv[0], 5), mp.nstr(wv[1], 3), mp.nstr(wv[2], 3), mp.nstr(wv[3], 3), mp.nstr(wv[4], 3)))

def wall_scan(kap, delta, sigma, Npts, seed=2, taus=(0, 1e-3, 1e-2, 0.05, 0.2, 0.5), nang=24):
    """Точки стенки W = delta rho^j (K=0), затем сдвиг вглубь: W = (1-tau) delta rho^j, K = tau delta rho^j;
    направление v_perp перебирается по окружности в плоскости, ортогональной Y."""
    random.seed(seed)
    lam0 = min(2*mp.mpf(float(sp.diff(G, ph, 2).subs(ph, float(phi0)))), hn)/4
    Rb = 2*mp.sqrt(delta/lam0)
    worst = None
    for _ in range(Npts):
        xv = sigma*mp.mpf(random.random())**2 + mp.mpf('1e-6')
        al = 2*mp.pi*random.random()
        dth, de = mp.cos(al), mp.sin(al)*mp.sqrt(lam0*4/hn)
        for tau in taus:
            lev = (1 - mp.mpf(tau))*delta
            def Wm(t):
                qq = point(xv, t*dth, t*de, kap)
                return Uf(*qq) + a0*xv**j - lev*xv**j
            lo, hi = mp.mpf(0), 2*Rb
            if Wm(hi) < 0 or Wm(lo) > 0:
                continue
            for _ in range(70):
                mid = (lo + hi)/2
                if Wm(mid) < 0: lo = mid
                else: hi = mid
            q = point(xv, lo*dth, lo*de, kap)
            Y, rho = Yfield(q, kap)
            W = Uf(*q) + a0*rho**j
            K = max(delta*rho**j - W, mp.mpf(0))
            h = sum(t*t for t in Y); Yn = mp.sqrt(h)
            # ортонормированный базис Y^perp
            a = [mp.mpf(1), mp.mpf(0), mp.mpf(0)] if abs(Y[0]) < 0.9*Yn else [mp.mpf(0), mp.mpf(1), mp.mpf(0)]
            u1 = [a[i] - sum(a[k]*Y[k] for k in range(3))/h*Y[i] for i in range(3)]
            nu = mp.sqrt(sum(t*t for t in u1)); u1 = [t/nu for t in u1]
            u2 = [Y[1]*u1[2] - Y[2]*u1[1], Y[2]*u1[0] - Y[0]*u1[2], Y[0]*u1[1] - Y[1]*u1[0]]
            nu = mp.sqrt(sum(t*t for t in u2)); u2 = [t/nu for t in u2]
            gq = [g(*q) for g in gU]
            lam_ = mp.sqrt(-2*Uf(*q) - 2*K)
            for k in range(nang if K > 0 else 1):
                be = 2*mp.pi*k/nang
                vp = [mp.sqrt(2*K)*(mp.cos(be)*u1[i] + mp.sin(be)*u2[i]) for i in range(3)]
                v = [-lam_*Y[i]/Yn + vp[i] for i in range(3)]
                f = lambda t: Vfun([q[i] + t*v[i] for i in range(3)], [v[i] - t*gq[i] for i in range(3)], kap, delta)
                val = rho/(lam_/Yn)*mp.diff(f, 0)/(delta*rho**j)
                if worst is None or val < worst[0]:
                    worst = (val, xv, lo*dth, lo*de, tau, be)
    return worst

if __name__ == '__main__':
    print('--- перебор стенки, K = tau*delta*rho^j, все направления v_perp ---')
    for kap in [0.0, 0.007, 0.05, 0.2, 0.5]:
        for (delta, sigma) in [(0.01, 0.05), (0.002, 0.005)]:
            wv = wall_scan(mp.mpf(kap), mp.mpf(delta), mp.mpf(sigma), 40)
            print('kappa=%-6g delta=%-6g sigma=%-6g: min = %s  [x=%s, theta=%s, e=%s, tau=%s]' % (
                kap, delta, sigma, mp.nstr(wv[0], 5), mp.nstr(wv[1], 3), mp.nstr(wv[2], 3),
                mp.nstr(wv[3], 3), wv[4]))
