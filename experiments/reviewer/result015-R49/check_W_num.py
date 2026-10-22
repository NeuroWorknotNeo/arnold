"""R49: независимая численная проверка леммы W (results/015-master.md), [Эксперимент].

Конкретные нелинейные P(s,u), xi(s,b), веса a. Функцию v(s,th) строим честно: по th
находим b из th = Theta(s,b) (метод Ньютона, mpmath, 60 знаков), затем
v = s d_sTheta|_b - D_bTheta xi (угловая скорость образа поля (1,-xi/s)). Производные
D_th v, d_s v|_th берём численным дифференцированием функции v(s,th) (то есть через
обращение карты, без цепного правила), psi = v + (D_th v) v + s d_s v|_th.
Сравниваем с (W0), (W1), (W2), где производные P, xi -- численные (mpmath.diff).
Отдельно проверяется (5.1): структура блоков матрицы N при условии (T).
"""
import mpmath as mp

mp.mp.dps = 60


def make(a, kappa):
    a1, a2 = a

    def P(s, u1, u2):
        return [u1 + mp.mpf('0.3') * s ** mp.mpf('1.3') + mp.mpf('0.2') * u1 ** 2 + mp.mpf('0.1') * s * u2
                + mp.mpf('0.05') * mp.sin(u2),
                u2 + mp.mpf('0.5') * s * u1 + mp.mpf('0.3') * u1 * u2 + mp.mpf('0.2') * s ** 2
                + mp.mpf('0.1') * mp.cos(u1) * s ** mp.mpf('0.7')]

    def xi(s, b1, b2):
        # i=1 коническое (a1=0) при a=(0,..): xi_1 = kappa*xi^c(s,b1); i=2 узкое: зависит от b1, b2
        return [kappa * (mp.sin(b1) + mp.mpf('0.2') * s * b1),
                2 * b2 + mp.mpf('0.3') * b1 * b2 + mp.mpf('0.2') * s * b1 + mp.mpf('0.1') * s ** mp.mpf('0.5')]
    return P, xi


def Theta(P, a, s, b):
    return P(s, s ** a[0] * b[0], s ** a[1] * b[1])


def num_jac(f, x, h=mp.mpf('1e-15')):
    """Якобиан f: R^k -> R^m по центральным разностям 4-го порядка (mp.diff медленнее)."""
    fx = f(*x)
    m = len(fx)
    k = len(x)
    Jm = mp.matrix(m, k)
    for j in range(k):
        def g(t, j=j):
            xx = list(x)
            xx[j] = t
            return f(*xx)
        c = [mp.mpf(1) / 12, mp.mpf(-2) / 3, 0, mp.mpf(2) / 3, mp.mpf(-1) / 12]
        vals = [g(x[j] + (i - 2) * h) for i in range(5)]
        for i in range(m):
            Jm[i, j] = sum(c[t] * vals[t][i] for t in range(5)) / h
    return Jm


def V_of_sb(P, xi, a, s, b):
    Th = lambda ss, b1, b2: Theta(P, a, ss, [b1, b2])
    Jall = num_jac(Th, [s, b[0], b[1]])
    dsTh = mp.matrix([Jall[0, 0], Jall[1, 0]])
    Jb = mp.matrix([[Jall[0, 1], Jall[0, 2]], [Jall[1, 1], Jall[1, 2]]])
    x = xi(s, b[0], b[1])
    return s * dsTh - Jb * mp.matrix(x)


def invert(P, a, s, th, guess):
    b = mp.matrix(guess)
    for _ in range(60):
        F = mp.matrix(Theta(P, a, s, [b[0], b[1]])) - mp.matrix(th)
        if mp.norm(F) < mp.mpf('1e-50'):
            break
        Jb = num_jac(lambda b1, b2: Theta(P, a, s, [b1, b2]), [b[0], b[1]], h=mp.mpf('1e-20'))
        b = b - mp.lu_solve(Jb, F)
    return [b[0], b[1]]


def check(a, kappa, s0, b0):
    P, xi = make(a, kappa)
    th0 = Theta(P, a, s0, b0)

    def v_sth(s, t1, t2):
        bb = invert(P, a, s, [t1, t2], b0)
        V = V_of_sb(P, xi, a, s, bb)
        return [V[0], V[1]]
    v0 = mp.matrix(v_sth(s0, th0[0], th0[1]))
    Jv = num_jac(v_sth, [s0, th0[0], th0[1]], h=mp.mpf('1e-12'))
    dsv = mp.matrix([Jv[0, 0], Jv[1, 0]])
    Dthv = mp.matrix([[Jv[0, 1], Jv[0, 2]], [Jv[1, 1], Jv[1, 2]]])
    psi_def = v0 + Dthv * v0 + s0 * dsv
    # формулы леммы W
    u0 = [s0 ** a[0] * b0[0], s0 ** a[1] * b0[1]]
    JP = num_jac(P, [s0, u0[0], u0[1]])
    sdsP = mp.matrix([s0 * JP[0, 0], s0 * JP[1, 0]])
    Pu = mp.matrix([[JP[0, 1], JP[0, 2]], [JP[1, 1], JP[1, 2]]])
    # s d_s (s d_s P) при постоянном u
    sdsP_f = lambda s, u1, u2: [s * x for x in [num_jac(P, [s, u1, u2])[i, 0] for i in range(2)]]
    J2 = num_jac(sdsP_f, [s0, u0[0], u0[1]], h=mp.mpf('1e-10'))
    sds_sdsP = mp.matrix([s0 * J2[0, 0], s0 * J2[1, 0]])
    sdsPu = mp.matrix([[J2[0, 1], J2[0, 2]], [J2[1, 1], J2[1, 2]]])   # D_u(s d_s P) = s d_s P_u
    # D^2_u P: Hessians
    Pu_f = lambda s, u1, u2: [num_jac(P, [s, u1, u2])[i, j] for i in range(2) for j in (1, 2)]
    H = num_jac(Pu_f, [s0, u0[0], u0[1]], h=mp.mpf('1e-10'))
    # H[(i,j), k] = d^2 P_i / du_j du_k  (строки i*2+(j-1))

    def D2(x, y):
        return mp.matrix([sum(H[2 * i + j, 1 + k] * x[j] * y[k] for j in range(2) for k in range(2))
                          for i in range(2)])

    def D2mat(x):
        M = mp.matrix(2, 2)
        for i in range(2):
            for k in range(2):
                M[i, k] = sum(H[2 * i + j, 1 + k] * x[j] for j in range(2))
        return M
    A = mp.diag([a[0], a[1]])
    sA = mp.diag([s0 ** a[0], s0 ** a[1]])
    sAi = mp.diag([s0 ** (-a[0]), s0 ** (-a[1])])
    bvec = mp.matrix(b0)
    X = mp.matrix(xi(s0, b0[0], b0[1]))
    Jxi = num_jac(xi, [s0, b0[0], b0[1]])
    sdsxi = mp.matrix([s0 * Jxi[0, 0], s0 * Jxi[1, 0]])
    Dbxi = mp.matrix([[Jxi[0, 1], Jxi[0, 2]], [Jxi[1, 1], Jxi[1, 2]]])
    ubar = sA * (A * bvec - X)
    vW0 = sdsP + Pu * ubar
    ds_Pu = sdsPu + D2mat(sA * A * bvec)
    I2 = mp.eye(2)
    N = I2 + A + mp.inverse(Pu) * (ds_Pu - D2mat(sA * X)) - sA * Dbxi * sAi
    W1 = Pu * N * mp.inverse(Pu)
    W2 = (sdsP + sds_sdsP + 2 * sdsPu * ubar + D2(ubar, ubar)
          + Pu * ((I2 + A) * ubar - sA * (A * X + sdsxi - Dbxi * X)))
    err0 = mp.norm(v0 - vW0)
    err1 = mp.mnorm(I2 + Dthv - W1, 1)
    err2 = mp.norm(psi_def - W2)
    # (5.1) при a=(0, a2>0): N = N0 - kappa(D xi^c (+) 0) + E,
    # N0 = 1 (+) (c2 - d_{b2} xi_2), E = Pu^{-1}[...] + элемент (2,1) = -s^{a2} d_{b1} xi_2
    E_pred = mp.inverse(Pu) * (ds_Pu - D2mat(sA * X))
    E_pred[1, 0] += -s0 ** (a[1] - a[0]) * Dbxi[1, 0]
    N0 = mp.diag([1, 1 + a[1] - Dbxi[1, 1]])
    cone = mp.matrix([[Dbxi[0, 0], 0], [0, 0]])
    err51 = mp.mnorm(N - (N0 - cone + E_pred), 1) if a[0] == 0 else None
    return err0, err1, err2, err51, mp.norm(v0), mp.mnorm(Dthv, 1), mp.norm(psi_def)


if __name__ == '__main__':
    for a, kappa, s0, b0 in [((0, mp.mpf('1.5')), mp.mpf('0.3'), mp.mpf('0.37'), [mp.mpf('0.4'), mp.mpf('-0.7')]),
                             ((0, mp.mpf('0.8')), mp.mpf('0.9'), mp.mpf('0.6'), [mp.mpf('-0.2'), mp.mpf('0.5')]),
                             ((mp.mpf('0.5'), 2), mp.mpf('0.5'), mp.mpf('0.25'), [mp.mpf('0.3'), mp.mpf('0.6')])]:
        e = check(a, kappa, s0, b0)
        print('a=%s kappa=%s s0=%s: |W0 err|=%s |W1 err|=%s |W2 err|=%s |(5.1) err|=%s ; sizes |v|=%s |Dv|=%s |psi|=%s'
              % (tuple(mp.nstr(x, 3) for x in a), mp.nstr(kappa, 3), mp.nstr(s0, 3),
                 *[mp.nstr(x, 3) if x is not None else '-' for x in e]))
