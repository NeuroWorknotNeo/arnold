# R51: численная проверка вывода теоремы X ((A5) на множестве выхода) в R^3 на параллели с k_g != 0
# (results/016-fold.md, теорема X). [Эксперимент], не доказательство.
# Параллель с полярным углом alpha: omega=(sin a cos u, sin a sin u, cos a), u=theta/sin a, n = omega x ell.
# Обратная карта явная: s = r_xy sin a + z cos a, eta = -r_xy cos a + z sin a, eps = eta/s^c.
# U(Pi(s,th,ep)) = s^beta (-a0 + P(th,ep)) точно, P = (th-th0)^2 + 2 ep^2.
# Поле X = kappa((th-th0) d_th + ep d_ep): XP = 2 kappa P, mu = 2 kappa; Gamma_theta = kappa*R.
# Печатается min (rho/lambda) Xi / (delta rho^beta) по точкам множества (A5) (V = delta rho^beta, E=0, p<0),
# параметризованным (th, ep) с P <= delta и углом phi направления v_perp в Y^perp.
import mpmath as mp

mp.mp.dps = 50
beta, c, a0 = mp.mpf(6), mp.mpf(3)/2, mp.mpf(1)
alpha = mp.mpf(1)
sa, ca = mp.sin(alpha), mp.cos(alpha)
th0 = mp.mpf('0.3')


def frame(t):
    u = t/sa
    o = mp.matrix([sa*mp.cos(u), sa*mp.sin(u), ca])
    l = mp.matrix([-mp.sin(u), mp.cos(u), 0])
    n = mp.matrix([-ca*mp.cos(u), -ca*mp.sin(u), sa])
    return o, l, n


def Pi(s, t, e):
    o, l, n = frame(t)
    return s*o + s**c*e*n


def Pinv(q):
    x, y, z = q
    rxy = mp.sqrt(x**2 + y**2)
    u = mp.atan2(y, x)
    s = rxy*sa + z*ca
    eta = -rxy*ca + z*sa
    return s, u*sa, eta/s**c


P = lambda t, e: (t-th0)**2 + 2*e**2


def U(q):
    s, t, e = Pinv(q)
    return s**beta*(-a0 + P(t, e))


def make(kappa):
    Xth = lambda t, e: kappa*(t-th0)
    Xep = lambda t, e: kappa*e

    def Yvec(q):
        s, t, e = Pinv(q)
        o, l, n = frame(t)
        eps_ = s**(c-1)*e*(ca/sa)  # k_g = cot(alpha) для этой ориентации; проверяется ниже численно
        # Pi_s, Pi_th, Pi_ep численно (центральные разности), чтобы не полагаться на (X.2)
        h = mp.mpf(10)**(-20)
        Ps = (Pi(s+h*s, t, e) - Pi(s-h*s, t, e))/(2*h*s)
        Pt = (Pi(s, t+h, e) - Pi(s, t-h, e))/(2*h)
        Pe = (Pi(s, t, e+h) - Pi(s, t, e-h))/(2*h)
        return Ps - Xth(t, e)/s*Pt - Xep(t, e)/s*Pe
    return Yvec


def Gfun(q, v, Yvec, delta):
    Y = Yvec(q)
    h = (Y.T*Y)[0]
    p = (v.T*Y)[0]
    s = Pinv(q)[0]
    return (v.T*v)[0]/2 - p**2/(2*h) + U(q) + a0*s**beta - delta*s**beta


def gradU(q, s):
    g = mp.matrix(3, 1)
    for i in range(3):
        e = mp.matrix(3, 1); e[i] = 1
        g[i] = mp.diff(lambda tau: U(q + tau*e), 0, h=s*mp.mpf(10)**(-12))
    return g


def scan(kappa, delta, s, nr=5, nphi=8):
    Yvec = make(kappa)
    R = mp.sqrt(delta)  # P <= delta  =>  |th-th0| <= sqrt(delta)
    best = None
    for i in range(-nr, nr+1):
        for j in range(-nr, nr+1):
            t = th0 + R*mp.mpf(i)/nr
            e = R/mp.sqrt(2)*mp.mpf(j)/nr
            if P(t, e) > delta:
                continue
            q = Pi(s, t, e)
            Y = Yvec(q); h = (Y.T*Y)[0]
            W = s**beta*P(t, e)
            K = delta*s**beta - W
            # ортонормированный базис Y^perp
            o, l, n = frame(t)
            e1 = l - ((l.T*Y)[0]/h)*Y; e1 = e1/mp.sqrt((e1.T*e1)[0])
            e2 = n - ((n.T*Y)[0]/h)*Y - ((n.T*e1)[0])*e1; e2 = e2/mp.sqrt((e2.T*e2)[0])
            A = a0*s**beta
            p = -mp.sqrt(2*h*(A - delta*s**beta))
            lam = -p/h
            gU = gradU(q, s)
            for k in range(nphi if K > 0 else 1):
                phi = 2*mp.pi*k/nphi
                vperp = mp.sqrt(2*K)*(mp.cos(phi)*e1 + mp.sin(phi)*e2)
                v = p/h*Y + vperp
                f = lambda tau: Gfun(q + tau*v, v - tau*gU, Yvec, delta)
                Xi = mp.diff(f, 0, h=s*mp.mpf(10)**(-12)/mp.sqrt((v.T*v)[0]))
                val = (s/lam)*Xi/(delta*s**beta)
                if best is None or val < best[0]:
                    best = (val, t, e, phi, K/s**beta)
    return best


if __name__ == '__main__':
    # проверка знака k_g: ell' = -omega + k_g n  =>  k_g = <ell', n>
    t = mp.mpf('0.2'); hh = mp.mpf(10)**(-20)
    lp = (frame(t+hh)[1] - frame(t-hh)[1])/(2*hh)
    print('k_g =', mp.nstr((lp.T*frame(t)[2])[0], 10), ' cot(alpha) =', mp.nstr(ca/sa, 10))
    delta = mp.mpf('0.01')
    CM = 15*mp.sqrt(3)/8*beta + 4
    R = mp.sqrt(4*delta)  # Omega = {P<4 delta}: |th-th0| < 2 sqrt(delta)
    # (X4): (kappa R)^2 <= 2 kappa beta delta / (2 CM^2 a0)  =>  kappa <= beta delta/(CM^2 R^2)
    kmax = beta*delta/(CM**2*R**2)
    print('kappa_max from (X4) =', mp.nstr(kmax, 6), '  mu = 2 kappa')
    for kappa in [kmax, 10*kmax, 100*kmax]:
        for s in ['1e-6', '1e-10']:
            b = scan(kappa, delta, mp.mpf(s))
            print('kappa=%s s=%s: min (rho/lam)Xi/(delta rho^b) = %s at th-th0=%s ep=%s phi=%s K/s^b=%s ; mu/2=%s'
                  % (mp.nstr(kappa, 4), s, mp.nstr(b[0], 6), mp.nstr(b[1]-th0, 3), mp.nstr(b[2], 3),
                     mp.nstr(b[3], 3), mp.nstr(b[4], 3), mp.nstr(kappa, 4)))
