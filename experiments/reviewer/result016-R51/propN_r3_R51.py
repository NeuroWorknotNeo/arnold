# R51: прямая проверка предложения N в R^3 (results/016-fold.md, §2, предложение N; доказательство §2.3).
# Экватор (k_g=0) и параллель (k_g != 0); U(Pi(s,th,ep)) = s^beta * (-a0 + P(th,ep)) точно;
# поле X = X^th(th,ep) d_th + X^ep d_ep; Y = Pi_*(d_s - X^th/s d_th - X^ep/s d_ep).
# Точка q = Pi(s,p0), скорость v из п. 3 доказательства. Xi = d/dt (V - delta rho^beta) вдоль
# потока (v, -grad U) считается численным дифференцированием (mpmath) в R^3, без формул (X.4),(X.5).
# [Эксперимент]. Печатается (rho/lambda) Xi / s^beta и его отношение к s^{1-c}.
import mpmath as mp

mp.mp.dps = 60

beta, c, a0, delta = mp.mpf(6), mp.mpf(3)/2, mp.mpf(1), mp.mpf('0.1')


def make_curve(alpha):
    """Параллель с полярным углом alpha (alpha=pi/2 — экватор), натуральный параметр."""
    sa, ca = mp.sin(alpha), mp.cos(alpha)

    def omega(t):
        u = t/sa
        return mp.matrix([sa*mp.cos(u), sa*mp.sin(u), ca])

    def ell(t):
        u = t/sa
        return mp.matrix([-mp.sin(u), mp.cos(u), 0])

    def nvec(t):
        o, l = omega(t), ell(t)
        return mp.matrix([o[1]*l[2]-o[2]*l[1], o[2]*l[0]-o[0]*l[2], o[0]*l[1]-o[1]*l[0]])
    return omega, ell, nvec, sa


def setup(alpha, Xth, Xep, P):
    omega, ell, nvec, sa = make_curve(alpha)

    def Pi(s, t, e):
        return s*omega(t) + s**c*e*nvec(t)

    def Pinv(q):
        # q = s*omega + eta*n с eta = s^c e; решаем численно, начиная с грубого приближения
        x, y, z = q
        u0 = mp.atan2(y, x)
        t0 = u0*sa
        s0 = mp.sqrt(x**2+y**2+z**2)
        def fun(s, t, e):
            r = Pi(s, t, e) - q
            return [r[0], r[1], r[2]]
        sol = mp.findroot(fun, (s0, t0, mp.mpf(0)))
        return sol[0], sol[1], sol[2]

    def U(q):
        s, t, e = Pinv(q)
        return s**beta*(-a0 + P(t, e))

    def Yvec(q):
        s, t, e = Pinv(q)
        h = mp.mpf(10)**(-25)
        Ps = (Pi(s+h, t, e) - Pi(s-h, t, e))/(2*h)
        Pt = (Pi(s, t+h, e) - Pi(s, t-h, e))/(2*h)
        Pe = (Pi(s, t, e+h) - Pi(s, t, e-h))/(2*h)
        return Ps - Xth(t, e)/s*Pt - Xep(t, e)/s*Pe

    return Pi, Pinv, U, Yvec, omega, ell, nvec


def G(q, v, U, Yvec, Pinv):
    Y = Yvec(q)
    h = (Y.T*Y)[0]
    p = (v.T*Y)[0]
    s = Pinv(q)[0]
    W = U(q) + a0*s**beta
    return (v.T*v)[0]/2 - p**2/(2*h) + W - delta*s**beta


def gradU(q, U, scale):
    g = mp.matrix(3, 1)
    for i in range(3):
        e = mp.matrix(3, 1); e[i] = 1
        g[i] = mp.diff(lambda tau: U(q + tau*e), 0, h=scale*mp.mpf(10)**(-15))
    return g


def run(alpha, Xth, Xep, dXth_de, P, p0, slist, label):
    Pi, Pinv, U, Yvec, omega, ell, nvec = setup(alpha, Xth, Xep, P)
    t0, e0 = p0
    print(label, ' P(p0)=', mp.nstr(P(t0, e0), 6), ' d_eps X^th(p0)=', mp.nstr(dXth_de(t0, e0), 6))
    for s in slist:
        s = mp.mpf(s)
        q = Pi(s, t0, e0)
        Y = Yvec(q); h = (Y.T*Y)[0]
        W = s**beta*P(t0, e0)        # W = U + a0 rho^beta
        K = delta*s**beta - W
        sg = mp.sign(dXth_de(t0, e0))
        eps_ = 0  # k_g e s^{c-1}: учтём точно через Y
        # w = w_om omega + ell/sqrt2 + sg n/sqrt2, w ⟂ Y
        l, n, o = ell(t0), nvec(t0), omega(t0)
        base = l/mp.sqrt(2) + sg*n/mp.sqrt(2)
        w_om = -(base.T*Y)[0]/(o.T*Y)[0]
        w = w_om*o + base
        wn = mp.sqrt((w.T*w)[0])
        vperp = mp.sqrt(2*K)*w/wn
        A = a0*s**beta
        p = -mp.sqrt(2*h*(A - delta*s**beta))
        v = p/h*Y + vperp
        E = (v.T*v)[0]/2 + U(q)
        lam = -p/h
        gU = gradU(q, U, s)
        # Xi = d/dt G(q(t), v(t)) at t=0
        f = lambda tau: G(q + tau*v, v - tau*gU, U, Yvec, Pinv)
        Xi = mp.diff(f, 0, h=mp.mpf(10)**(-15)*s/ mp.sqrt((v.T*v)[0]))
        R = (s/lam)*Xi/s**beta
        print('  s=%s  E/s^beta=%s  V-delta s^b=%s  (rho/lam)Xi/s^beta=%s  ratio to s^{1-c}=%s'
              % (mp.nstr(s, 3), mp.nstr(E/s**beta, 3), mp.nstr((G(q, v, U, Yvec, Pinv))/s**beta, 3),
                 mp.nstr(R, 8), mp.nstr(R/s**(1-c), 8)))


if __name__ == '__main__':
    mu = mp.mpf('0.05'); x0 = mp.mpf('0.3')
    P = lambda t, e: e**2 + t**2
    Xth = lambda t, e: mu*t + x0*e
    Xep = lambda t, e: mu*e
    dXth = lambda t, e: x0
    slist = ['1e-4', '1e-6', '1e-8', '1e-10']
    run(mp.pi/2, Xth, Xep, dXth, P, (mp.mpf('0.1'), mp.mpf('0.1')), slist, 'equator, nontriangular x0=0.3')
    run(mp.mpf(1), Xth, Xep, dXth, P, (mp.mpf('0.1'), mp.mpf('0.1')), slist, 'parallel alpha=1 (k_g!=0), x0=0.3')
    # контроль: треугольное поле (x0=0) — величина должна оставаться ограниченной (не расти как s^{-1/2})
    Xth0 = lambda t, e: mu*t
    run(mp.mpf(1), Xth0, Xep, lambda t, e: 0*t, P, (mp.mpf('0.1'), mp.mpf('0.1')), slist, 'parallel alpha=1, triangular x0=0')
