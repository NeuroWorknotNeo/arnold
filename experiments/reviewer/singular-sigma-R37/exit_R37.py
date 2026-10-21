"""R37: независимая проверка (A5) для модели с возмущением, поле теоремы S [Эксперимент].

U = x^2y^2 + eps z^2(x^4+y^4) - z^6 + x^6 + y^6 + V,  V = x z^6 + 2 y^2 z^5 (порядок 7).
rho = |q|, Y = omega - kappa*Domega*theta (гномоническая карта, xi = theta), A = r^6.
Точки стенки: W <= delta r^6 в кресте, K_perp = delta r^6 - W, v_perp — случайное
направление в Y^perp, E = 0, p < 0. Xi = d/dt (V - delta rho^6) вдоль (v, -grad U)
считается прямым дифференцированием (mpmath.diff), без тождества (1.3).
Выводится min (rho/lambda) Xi / (delta rho^6). Это проверка в конечном числе точек.
"""
import random
import mpmath as mp

mp.mp.dps = 40


def make(eps, pert):
    def U(q):
        x, y, z = q
        u = x**2*y**2 + eps*z**2*(x**4 + y**4) - z**6 + x**6 + y**6
        if pert:
            u += x*z**6 + 2*y**2*z**5
        return u

    def gradU(q):
        x, y, z = q
        gx = 2*x*y**2 + 4*eps*z**2*x**3 + 6*x**5
        gy = 2*y*x**2 + 4*eps*z**2*y**3 + 6*y**5
        gz = 2*eps*z*(x**4 + y**4) - 6*z**5
        if pert:
            gx += z**6
            gy += 4*y*z**5
            gz += 6*x*z**5 + 10*y**2*z**4
        return mp.matrix([gx, gy, gz])
    return U, gradU


def omega(t1, t2):
    c = 1/mp.sqrt(1 + t1**2 + t2**2)
    return mp.matrix([c*t1, c*t2, c])


def Domega(t1, t2):
    c = 1/mp.sqrt(1 + t1**2 + t2**2)
    c3 = c**3
    # d omega / d t1, d t2
    d1 = mp.matrix([c - c3*t1**2, -c3*t1*t2, -c3*t1])
    d2 = mp.matrix([-c3*t1*t2, c - c3*t2**2, -c3*t2])
    return d1, d2


def Yfield(q, kap):
    t1, t2 = q[0]/q[2], q[1]/q[2]
    d1, d2 = Domega(t1, t2)
    return omega(t1, t2) - kap*(t1*d1 + t2*d2)


def Vfun(q, v, U, kap, delta):
    Y = Yfield(q, kap)
    h = mp.fdot(Y, Y)
    p = mp.fdot(v, Y)
    rho = mp.norm(q)
    W = U(q) + rho**6
    return 0.5*mp.fdot(v, v) - p**2/(2*h) + W - delta*rho**6


def test(eps, pert, kap, delta, r, n=400, seed=0):
    U, gradU = make(eps, pert)
    rnd = random.Random(seed)
    worst = mp.inf
    cnt = 0
    tries = 0
    while cnt < n and tries < 50*n:
        tries += 1
        a = rnd.uniform(-1.2, 1.2)*mp.sqrt(delta)
        scale = r*mp.sqrt(delta)/max(abs(a), (r**2*delta)**0.25)
        b = rnd.uniform(-1.5, 1.5)*scale
        t1, t2 = (a, b) if rnd.random() < 0.5 else (b, a)
        q = r*omega(t1, t2)
        W = U(q) + r**6
        if W > delta*r**6:
            continue
        tau = rnd.choice([0, 1e-3, 1e-2, 0.05, 0.2, 0.5, 1.0])
        # подвинем W ближе к стенке, если tau мало: используем точку как есть,
        # K_perp = delta r^6 - W (стенка V = delta r^6)
        Kp = delta*r**6 - W
        Y = Yfield(q, kap)
        h = mp.fdot(Y, Y)
        # базис Y^perp
        e1 = mp.matrix([1, 0, 0]) - (Y[0]/h)*Y
        e1 = e1/mp.norm(e1)
        e2 = mp.matrix([Y[1]*e1[2] - Y[2]*e1[1], Y[2]*e1[0] - Y[0]*e1[2], Y[0]*e1[1] - Y[1]*e1[0]])
        e2 = e2/mp.norm(e2)
        ang = rnd.uniform(0, 2*mp.pi)
        vperp = mp.sqrt(2*Kp)*(mp.cos(ang)*e1 + mp.sin(ang)*e2)
        p2h = -2*U(q) - 2*Kp  # p^2/h
        if p2h <= 0:
            print('p2h<=0 !', p2h)
            continue
        p = -mp.sqrt(p2h*h)
        v = (p/h)*Y + vperp
        lam = -p/h
        g = gradU(q)
        f = lambda s: Vfun(q + s*v, v - s*g, U, kap, delta)
        Xi = mp.diff(f, 0)
        val = (r/lam)*Xi/(delta*r**6)
        worst = min(worst, val)
        cnt += 1
        _ = tau
    return worst, cnt


if __name__ == '__main__':
    for eps in [mp.mpf('-0.5'), mp.mpf('0.1'), mp.mpf(-3)]:
        for pert in [False, True]:
            for kap in [mp.mpf('0.05'), mp.mpf('0.2')]:
                for r in [mp.mpf('1e-3'), mp.mpf('1e-5')]:
                    w, c = test(eps, pert, kap, mp.mpf('0.01'), r)
                    print('eps=%s pert=%s kappa=%s r=%s: min (rho/lam)Xi/(delta rho^6) = %s  (%d pts)'
                          % (mp.nstr(eps, 3), pert, mp.nstr(kap, 3), mp.nstr(r, 2), mp.nstr(w, 6), c))
