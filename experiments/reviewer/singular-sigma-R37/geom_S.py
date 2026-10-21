"""R37: независимая проверка формул (2.1), (2.2) теоремы S [Эксперимент].

Карта: omega(theta) = Phi(theta)/|Phi(theta)| для нелинейного Phi (n=3),
поле xi(theta) нелинейно, xi(0)=0. Y(q) = y(theta(q)), theta(q) находится
методом Ньютона из q/|q|. Производные D_Y Y, D_w Y считаются конечными
разностями (mpmath, 50 знаков) и сравниваются с (2.2).
"""
import mpmath as mp

mp.mp.dps = 50
kap = mp.mpf('0.37')


def Phi(t):
    t1, t2 = t
    return mp.matrix([t1 + t2**2 / 3 + mp.sin(t1 * t2) / 5,
                      t2 + t1 * t2 / 5 - t1**3 / 7,
                      1 + t1 / 7 - t2**2 / 11])


def omega(t):
    v = Phi(t)
    return v / mp.norm(v)


def xi(t):
    t1, t2 = t
    return mp.matrix([t1 + t2**2 - t1 * t2 / 3, 2 * t2 + mp.sin(t1) * t2 + t1**2])


def jac(f, t, h=mp.mpf('1e-20')):
    # центральные разности по theta
    cols = []
    for i in range(2):
        e = [mp.mpf(0), mp.mpf(0)]
        e[i] = h
        tp = [t[0] + e[0], t[1] + e[1]]
        tm = [t[0] - e[0], t[1] - e[1]]
        cols.append((f(tp) - f(tm)) / (2 * h))
    m = mp.matrix(len(cols[0]), 2)
    for i in range(2):
        for k in range(len(cols[0])):
            m[k, i] = cols[i][k]
    return m


def Domega(t):
    return jac(omega, t)


def y(t):
    return omega(t) - kap * Domega(t) * xi(t)


def theta_of(q):
    u = q / mp.norm(q)
    t = [mp.mpf(0), mp.mpf(0)]
    for _ in range(60):
        r = omega(t) - u
        J = Domega(t)
        # решаем J dt = -r в смысле наименьших квадратов
        JT = J.T
        dt = mp.lu_solve(JT * J, -(JT * r))
        t = [t[0] + dt[0], t[1] + dt[1]]
    return t


def Yq(q):
    return y(theta_of(q))


def D2omega(t, a, b, h=mp.mpf('1e-15')):
    # D^2 omega (a,b)
    def g(s):
        return Domega(s) * b
    tp = [t[0] + h * a[0], t[1] + h * a[1]]
    tm = [t[0] - h * a[0], t[1] - h * a[1]]
    return (g(tp) - g(tm)) / (2 * h)


def check(t, r, wvec):
    q = r * omega(t)
    Y = Yq(q)
    # (2.1)
    res21 = mp.norm(Y - (omega(t) - kap * Domega(t) * xi(t)))
    # Y rho = 1
    yrho = mp.fdot(omega(t), Y)
    # D_Y Y конечной разностью по q
    h = mp.mpf('1e-18')
    DYY = (Yq(q + h * Y) - Yq(q - h * Y)) / (2 * h)
    Dw = Domega(t)
    x = xi(t)
    Dxi = jac(xi, t)
    pred = -kap * (Dw * x - kap * D2omega(t, x, x) - kap * Dw * (Dxi * x))
    res_YY = mp.norm(r * DYY - pred)
    # r <w, D_w Y>
    DwY = (Yq(q + h * wvec) - Yq(q - h * wvec)) / (2 * h)
    lhs = r * mp.fdot(wvec, DwY)
    # разложение w = a omega + tau, tau = Domega (r alpha)
    om = omega(t)
    a = mp.fdot(wvec, om)
    tau = wvec - a * om
    ra = mp.lu_solve(Dw.T * Dw, Dw.T * tau)  # r*alpha
    rhs = (mp.fdot(tau, tau) - kap * mp.fdot(wvec, D2omega(t, x, ra))
           - kap * mp.fdot(tau, Dw * (Dxi * ra)))
    return res21, yrho - 1, res_YY, lhs - rhs


if __name__ == '__main__':
    pts = [([mp.mpf('0.1'), mp.mpf('-0.07')], mp.mpf('0.3'), mp.matrix([0.3, -1.1, 0.7])),
           ([mp.mpf('-0.2'), mp.mpf('0.15')], mp.mpf('0.05'), mp.matrix([1.0, 0.2, -0.4])),
           ([mp.mpf('0.03'), mp.mpf('0.21')], mp.mpf('1.7'), mp.matrix([-0.5, 0.9, 0.1]))]
    for t, r, w in pts:
        out = check(t, r, w)
        print('theta=', [mp.nstr(s, 4) for s in t], 'r=', mp.nstr(r, 3),
              'res(2.1)=', mp.nstr(out[0], 3), 'Yrho-1=', mp.nstr(out[1], 3),
              'res rD_YY=', mp.nstr(out[2], 3), 'res r<w,D_wY>=', mp.nstr(out[3], 3))
