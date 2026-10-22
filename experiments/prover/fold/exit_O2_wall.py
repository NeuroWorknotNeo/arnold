# [Эксперимент] Вторая редакция (по R48, З10): строгий выход (A5) теоремы A [results/007] для конструкции
# предложения O2 (notes/prover/2026-10-21-fold.md, §5) У СТЕНКИ: точки множества выхода с малым K_perp > 0.
#   U = z^4 - 2 z^2 y rho^2 - x^2 rho^4 + x^7 + y^7,  rho = s = sqrt(x^2+y^2),  A(rho) = rho^6 (a0 = 1, beta = 6),
#   Pi(s,th,eps) = (s cos th, s sin th, s^{3/2} eps),  Y = Pi_s - (X^th/s) Pi_th - (X^eps/s) Pi_eps,
#   X = mu' X_0,  X_0^th = chi(th) tan(th)/2,  X_0^eps = (eps^2 - (1-chi) sin th)/(4 eps)  (= eps/4 при chi = 1).
# Точки: W = delta rho^6 (1 - kappa), то есть f^2 + s g = delta (1 - kappa), K_perp = kappa delta rho^6,
#   E = 0, p < 0, V = delta rho^6;  v_perp = sqrt(2K)(cos phi e1 + sin phi e2), e1, e2 -- ортонормированный базис Y^perp.
# Xi = d/dt (V - delta rho^6) вдоль (q', v') = (v, -grad U): разностная производная 4-го порядка (mpmath).
# При фиксированных (q, K) величина Xi -- тригонометрический многочлен степени 2 по phi (формула (1.2) [007]:
#   Xi квадратична по v_perp при фиксированном p), поэтому минимум по phi берётся точно: 8 значений -> 5 коэффициентов
#   Фурье -> минимум на сетке 2000 углов. Печатается R := min (rho/lambda) Xi / (delta rho^6) (нужно R > 0).
# Режимы:  ~/venv/bin/python exit_O2_wall.py table      -- таблица R при разных delta, mu'
#          ~/venv/bin/python exit_O2_wall.py threshold  -- порог mu'_crit(delta) (бисекция по mu'), mu'_crit/delta
#          ~/venv/bin/python exit_O2_wall.py theory     -- R при mu' = 12 delta / C_M^2 (значение из доказательства)
import sys
import sympy as sp
import mpmath as mp
import numpy as np

mp.mp.dps = 40
X_, Y_, Z_ = sp.symbols('x y z', real=True)
r2 = X_**2 + Y_**2
Usym = Z_**4 - 2*Z_**2*Y_*r2 - X_**2*r2**2 + X_**7 + Y_**7
Uf = sp.lambdify((X_, Y_, Z_), Usym, 'mpmath')
gUf = [sp.lambdify((X_, Y_, Z_), sp.diff(Usym, v), 'mpmath') for v in (X_, Y_, Z_)]
CM = 45*mp.sqrt(3)/4 + 4
C15 = mp.mpf(3)/2


def step(t):
    if t <= 0:
        return mp.mpf(0)
    if t >= 1:
        return mp.mpf(1)
    a, b = mp.exp(-1/t), mp.exp(-1/(1-t))
    return a/(a+b)


def chi(th):
    d = min(abs(th), abs(th - mp.pi))
    return 1 - step((d - mp.pi/8)/(mp.pi/8))


def X0(th, e):
    c = chi(th)
    Xt = c*mp.tan(th)/2 if c != 0 else mp.mpf(0)
    Xe = e/4 if c == 1 else (e**2 - (1-c)*mp.sin(th))/(4*e)
    return Xt, Xe


def coords(q):
    s = mp.sqrt(q[0]**2 + q[1]**2)
    th = mp.atan2(q[1], q[0])
    if th < -mp.pi/4:
        th += 2*mp.pi
    return s, th, q[2]/s**C15


def Yv(q, mup):
    s, th, e = coords(q)
    Xt, Xe = X0(th, e)
    Xt, Xe = mup*Xt, mup*Xe
    return [mp.cos(th) + Xt*mp.sin(th), mp.sin(th) - Xt*mp.cos(th), mp.sqrt(s)*(C15*e - Xe)]


def dot(a, b):
    return sum(a[i]*b[i] for i in range(3))


def Vfun(q, v, mup):
    Y = Yv(q, mup)
    p = dot(v, Y)
    s = mp.sqrt(q[0]**2 + q[1]**2)
    return dot(v, v)/2 - p**2/(2*dot(Y, Y)) + Uf(*q) + s**6


def ratio(s, th, e, phi, mup, delta):
    q = [s*mp.cos(th), s*mp.sin(th), s**C15*e]
    U = Uf(*q)
    K = delta*s**6 - (U + s**6)
    if K < 0:
        K = mp.mpf(0)
    Y = Yv(q, mup)
    h = dot(Y, Y)
    a = [0, 0, 1]
    e1 = [a[i] - dot(a, Y)/h*Y[i] for i in range(3)]
    n1 = mp.sqrt(dot(e1, e1)); e1 = [c/n1 for c in e1]
    e2 = [Y[1]*e1[2]-Y[2]*e1[1], Y[2]*e1[0]-Y[0]*e1[2], Y[0]*e1[1]-Y[1]*e1[0]]
    n2 = mp.sqrt(dot(e2, e2)); e2 = [c/n2 for c in e2]
    vp = [mp.sqrt(2*K)*(mp.cos(phi)*e1[i] + mp.sin(phi)*e2[i]) for i in range(3)]
    pp = -mp.sqrt(h*(-2*U - 2*K))
    v = [pp/h*Y[i] + vp[i] for i in range(3)]
    g = [gf(*q) for gf in gUf]
    chk = abs(Vfun(q, v, mup) - delta*s**6)/(delta*s**6)
    if chk > mp.mpf(10)**-20:
        raise RuntimeError('точка не на множестве выхода: %s' % chk)
    lam = -pp/h
    hh = mp.mpf(10)**-8*s/mp.sqrt(dot(v, v))

    def Phi(t):
        qt = [q[i] + t*v[i] for i in range(3)]
        vt = [v[i] - t*g[i] for i in range(3)]
        st = mp.sqrt(qt[0]**2 + qt[1]**2)
        return Vfun(qt, vt, mup) - delta*st**6
    Xi = (-Phi(2*hh) + 8*Phi(hh) - 8*Phi(-hh) + Phi(-2*hh))/(12*hh)
    return s/lam*Xi/(delta*s**6)


def min_phi(s, th, e, mup, delta):
    """Точный минимум по phi: Xi -- тригонометрический многочлен степени 2."""
    vals = [ratio(s, th, e, 2*mp.pi*k/8, mup, delta) for k in range(8)]
    c0 = sum(vals)/8
    cs = [(sum(vals[k]*mp.cos(2*mp.pi*j*k/8) for k in range(8))/4,
           sum(vals[k]*mp.sin(2*mp.pi*j*k/8) for k in range(8))/4) for j in (1, 2)]
    # контроль: гармоники 3, 4 должны быть ~0
    c3 = abs(sum(vals[k]*mp.cos(2*mp.pi*3*k/8) for k in range(8))/4) + abs(sum(vals[k]*(-1)**k for k in range(8))/8)
    a1, b1, a2, b2 = (float(cs[0][0]), float(cs[0][1]), float(cs[1][0]), float(cs[1][1]))
    ph = np.linspace(0, 2*np.pi, 3600, endpoint=False)
    vals_f = a1*np.cos(ph) + b1*np.sin(ph) + a2*np.cos(2*ph) + b2*np.sin(2*ph)
    i0 = int(np.argmin(vals_f))
    lo, hi = ph[i0] - 2*np.pi/3600, ph[i0] + 2*np.pi/3600
    fun = lambda t: a1*np.cos(t) + b1*np.sin(t) + a2*np.cos(2*t) + b2*np.sin(2*t)
    for _ in range(60):   # золотое сечение
        m1, m2 = lo + 0.382*(hi - lo), lo + 0.618*(hi - lo)
        if fun(m1) < fun(m2):
            hi = m2
        else:
            lo = m1
    best = c0 + mp.mpf(min(fun(lo), vals_f[i0]))
    return best, c3


def points(s, th, kap, delta):
    """Точки (th, eps) с f^2 + s g = delta (1 - kap), обе ветви f, оба знака eps."""
    gth = mp.cos(th)**7 + mp.sin(th)**7
    f2 = delta*(1 - kap) - s*gth
    out = []
    if f2 < 0 or f2 > 4*delta:
        return out
    for sf in (1, -1):
        e2 = mp.sin(th) + sf*mp.sqrt(f2)
        if e2 <= 0:
            continue
        for se in (1,):
            ep = se*mp.sqrt(e2)
            if abs(ep) < mp.mpf('1e-30') and chi(th) < 1:
                continue
            out.append(ep)
    return out


def worst(mup, delta, s, ths, kaps):
    w = (mp.inf, None)
    c3max = 0
    for th in ths:
        for kap in kaps:
            for ep in points(s, th, kap, delta):
                r, c3 = min_phi(s, th, ep, mup, delta)
                c3max = max(c3max, c3)
                if r < w[0]:
                    w = (r, (th, ep, kap))
    return w, c3max


def refine(mup, delta, s, th0, kap0):
    """Локальное уточнение минимума по (th, kappa) вокруг найденной точки."""
    best = None
    for dth in [mp.mpf(k)/200 for k in range(-6, 7)]:
        for fk in [mp.mpf(2)**(mp.mpf(k)/2) for k in range(-4, 5)]:
            th = th0 + dth
            kap = kap0*fk
            if kap >= 1:
                continue
            for ep in points(s, th, kap, delta):
                r, _ = min_phi(s, th, ep, mup, delta)
                if best is None or r < best[0]:
                    best = (r, (th, ep, kap))
    return best


THS = ([mp.mpf(t)/100 for t in range(-24, 157, 4)] + [mp.mpf(t)/1000 for t in range(400, 601, 5)]
       + [mp.mpf(t)/100 for t in (-2, -1, 1, 2)])
THS = sorted(set(THS))
KAPS = [mp.mpf(10)**(mp.mpf(k)/4) for k in range(-24, -1)]   # 1e-6 ... 0.56


def R_of(mup, delta, s, coarse=None):
    if coarse is None:
        coarse, _ = worst(mup, delta, s, THS, KAPS)
    th0, ep0, kap0 = coarse[1]
    fine = refine(mup, delta, s, th0, kap0)
    return min(coarse, fine, key=lambda z: z[0])


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'table'
    s = mp.mpf('1e-12')
    if mode == 'theory':
        for delta in (mp.mpf('0.01'), mp.mpf('0.002')):
            mth = 12*delta/CM**2
            (r, where), c3 = worst(mth, delta, s, THS, [mp.mpf(0)] + KAPS)
            print('delta=%s mu\'_th=%s: R = %s, R/mu\' = %s, at (th, eps, kappa) = (%s, %s, %s); |гармоники 3,4| <= %s'
                  % (mp.nstr(delta, 3), mp.nstr(mth, 4), mp.nstr(r, 6), mp.nstr(r/mth, 6),
                     mp.nstr(where[0], 4), mp.nstr(where[1], 4), mp.nstr(where[2], 3), mp.nstr(c3, 2)), flush=True)
    elif mode == 'table':
        for delta in (mp.mpf('0.01'), mp.mpf('0.002')):
            for k in (1, 2, 4, 6, 8, 10):
                mup = k*delta
                (r, where), c3 = worst(mup, delta, s, THS, KAPS)
                r2_ = refine(mup, delta, s, where[0], where[2])
                if r2_[0] < r:
                    r, where = r2_
                print('delta=%s mu\'=%s*delta: R = %s at (th, eps, kappa) = (%s, %s, %s); |гармоники 3,4| <= %s'
                      % (mp.nstr(delta, 3), k, mp.nstr(r, 6), mp.nstr(where[0], 4), mp.nstr(where[1], 4),
                         mp.nstr(where[2], 3), mp.nstr(c3, 2)), flush=True)
    elif mode == 'threshold':
        for delta in (mp.mpf('0.01'), mp.mpf('0.002'), mp.mpf('0.0005')):
            lo, hi = 2*delta, 10*delta     # R(lo) > 0 > R(hi) проверяется
            Rlo = R_of(lo, delta, s)[0]
            Rhi = R_of(hi, delta, s)[0]
            print('delta=%s: R(2 delta) = %s, R(10 delta) = %s' % (mp.nstr(delta, 3), mp.nstr(Rlo, 5), mp.nstr(Rhi, 5)), flush=True)
            if not (Rlo > 0 > Rhi):
                continue
            for _ in range(7):
                mid = (lo + hi)/2
                Rm = R_of(mid, delta, s)[0]
                if Rm > 0:
                    lo = mid
                else:
                    hi = mid
            print('delta=%s: mu\'_crit in [%s, %s], mu\'_crit/delta in [%s, %s]'
                  % (mp.nstr(delta, 3), mp.nstr(lo, 5), mp.nstr(hi, 5), mp.nstr(lo/delta, 4), mp.nstr(hi/delta, 4)), flush=True)
