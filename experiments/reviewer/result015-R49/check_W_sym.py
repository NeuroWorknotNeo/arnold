"""R49: независимая символьная проверка леммы W (results/015-master.md), [Эксперимент].

P(s,u) -- общая 3-струя в точке (s0, u0), u0 = s0^A b0 (символьные коэффициенты),
xi(s,b) -- общая 2-струя в точке (s0, b0); веса a_i символьные (m = 2) или случайные
рациональные (m = 3). Theta(s,b) = P(s, s^A b).

Определения (без формул леммы W):
  * поле Y в координатах (s,b) есть (1, -xi/s); его образ при (s,b) -> (s,Theta) имеет
    th-компоненту d_sTheta - D_bTheta xi/s; по определению угловой скорости (Y = d_s + (v/s) d_th)
    V(s,b) := v(s,Theta(s,b)) = s d_sTheta - D_bTheta xi;
  * D_th v = D_b V (D_b Theta)^{-1}  (цепное правило при фиксированном s);
  * d_s v|_th = d_s V - D_th v d_s Theta;
  * psi = v + (D_th v) v + s d_s v|_th  (определение из раздела «Поле с угловой скоростью»).
Проверяются (W0), (W1), (W2), (W3) и совпадение psi с v + s d/ds v вдоль потока.
"""
import itertools
import random
import sympy as sp


def multi_indices(nvar, order):
    for tot in range(order + 1):
        for k in itertools.product(range(tot + 1), repeat=nvar):
            if sum(k) == tot:
                yield k


def run(m, a_vals=None, rnd=None):
    s = sp.Symbol('s', positive=True)
    s0 = sp.Symbol('s0', positive=True)
    b = sp.symbols('b0:%d' % m)
    b0 = sp.symbols('bb0:%d' % m)
    u = sp.symbols('u0:%d' % m)
    if a_vals is None:
        a = sp.symbols('a0:%d' % m, nonnegative=True)
    else:
        a = a_vals
    u0 = [s0 ** a[i] * b0[i] for i in range(m)]
    # 3-струя P_i
    coeff = {}
    P = []
    for i in range(m):
        e = 0
        for k in multi_indices(m + 1, 3):
            c = sp.Symbol('p%d_' % i + '_'.join(map(str, k)))
            coeff[c] = None
            mon = (s - s0) ** k[0]
            for j in range(m):
                mon *= (u[j] - u0[j]) ** k[j + 1]
            e += c * mon
        P.append(e)
    # 2-струя xi_i
    XI = []
    for i in range(m):
        e = 0
        for k in multi_indices(m + 1, 2):
            c = sp.Symbol('x%d_' % i + '_'.join(map(str, k)))
            coeff[c] = None
            mon = (s - s0) ** k[0]
            for j in range(m):
                mon *= (b[j] - b0[j]) ** k[j + 1]
            e += c * mon
        XI.append(e)
    subsnum = {}
    if rnd is not None:
        for c in coeff:
            subsnum[c] = sp.Rational(rnd.randint(-7, 7), rnd.randint(1, 4))
        for x in b0:
            subsnum[x] = sp.Rational(rnd.randint(-5, 5), rnd.randint(1, 3))
        subsnum[s0] = sp.Rational(rnd.randint(1, 7), rnd.randint(2, 5))
    if subsnum:   # подставляем числа сразу: иначе выражения слишком велики
        P = [sp.expand(e.subs(subsnum)) for e in P]
        XI = [sp.expand(e.subs(subsnum)) for e in XI]
    Pm = sp.Matrix(P)
    XIm = sp.Matrix(XI)
    bv = sp.Matrix(b)
    uv = sp.Matrix(u)
    sub_u = {u[j]: s ** a[j] * b[j] for j in range(m)}
    Theta = Pm.subs(sub_u)
    J = Theta.jacobian(bv)
    V = s * Theta.diff(s) - J * XIm               # V = v o Theta
    DbV = V.jacobian(bv)
    pt = {s: s0, **{b[j]: b0[j] for j in range(m)}}

    def at(e):
        e = e.subs(pt)
        if subsnum:
            e = e.subs(subsnum)
        return e
    Jp, Vp, DbVp = at(J), at(V), at(DbV)
    Dthv = DbVp * Jp.adjugate() / Jp.det()
    sdsTheta = at(s * Theta.diff(s))
    sdsV = at(s * V.diff(s))
    sdsv_th = sdsV - Dthv * sdsTheta
    psi_def = Vp + Dthv * Vp + sdsv_th
    psi_flow = Vp + sdsV - DbVp * at(XIm)        # v + s d/ds V(s, b(s)), s db/ds = -xi
    # величины формул леммы W: производные P в точке (s, s^A b)
    A = sp.diag(*a)
    sA = sp.diag(*[s ** a[j] for j in range(m)])
    sAi = sp.diag(*[s ** (-a[j]) for j in range(m)])
    Pu = Pm.jacobian(uv)
    sdsP = s * Pm.diff(s)
    sds_sdsP = s * sdsP.diff(s)
    sdsPu = s * Pu.diff(s)

    def D2u(vec):   # матрица D^2_u P(vec, .): (i,k) -> sum_j d2P_i/du_j du_k vec_j
        return sp.Matrix(m, m, lambda i, k: sum(Pm[i].diff(u[j]).diff(u[k]) * vec[j] for j in range(m)))

    def D2u_bil(x, y):
        return sp.Matrix(m, 1, lambda i, _: sum(Pm[i].diff(u[j]).diff(u[k]) * x[j] * y[k]
                                                 for j in range(m) for k in range(m)))
    bb = bv

    def at2(e):
        return at(e.subs(sub_u))
    # все блоки -- в точке; обратные матрицы берём уже от чисел (через adjugate/det)
    Pu_p = at2(Pu)
    Pu_inv = Pu_p.adjugate() / Pu_p.det()
    sA_p, sAi_p, A_p = at2(sA), at2(sAi), A
    X_p = at2(XIm)
    Dxi_p = at2(XIm.jacobian(bv))
    sdsxi_p = at2(s * XIm.diff(s))
    b_p = at2(bb)
    sdsP_p, sds_sdsP_p, sdsPu_p = at2(sdsP), at2(sds_sdsP), at2(sdsPu)
    H = [[[at2(Pm[i].diff(u[j]).diff(u[k])) for k in range(m)] for j in range(m)] for i in range(m)]

    def D2u(vec):
        return sp.Matrix(m, m, lambda i, k: sum(H[i][j][k] * vec[j] for j in range(m)))

    def D2u_bil(x, y):
        return sp.Matrix(m, 1, lambda i, _: sum(H[i][j][k] * x[j] * y[k] for j in range(m) for k in range(m)))
    ubar = sA_p * (A_p * b_p - X_p)
    v_W0p = sdsP_p + Pu_p * ubar
    ds_Pu = sdsPu_p + D2u(sA_p * A_p * b_p)
    Nmat = sp.eye(m) + A_p + Pu_inv * (ds_Pu - D2u(sA_p * X_p)) - sA_p * Dxi_p * sAi_p
    W1p = Pu_p * Nmat * Pu_inv
    W2p = (sdsP_p + sds_sdsP_p + 2 * sdsPu_p * ubar + D2u_bil(ubar, ubar)
           + Pu_p * ((sp.eye(m) + A_p) * ubar - sA_p * (A_p * X_p + sdsxi_p - Dxi_p * X_p)))
    W3p = sdsP_p + Pu_p * sA_p * A_p * b_p       # s d_s Theta|_b по (W3)
    NEG_W2 = W2p - sdsPu_p * ubar                   # без множителя 2
    NEG_W1 = Pu_p * (Nmat + sA_p * Dxi_p * sAi_p - Dxi_p) * Pu_inv   # без сопряжения s^A

    asyms = [x for x in a if isinstance(x, sp.Symbol)]

    def zero1(x):
        x = sp.expand(sp.powsimp(sp.expand(x, power_exp=True), force=True))
        if x == 0:
            return True
        status = 'exact'
        for trial in range(3 if asyms else 1):
            rr = random.Random(trial)
            vals = {aa: sp.Rational(rr.randint(0, 8), 2) for aa in asyms}
            xv = x.subs(vals)
            num = sp.N(xv, 80)
            if abs(num) > sp.Float('1e-50'):
                return False
            # точное упрождение (корни в знаменателях): radsimp + simplify
            if sp.simplify(sp.radsimp(sp.together(xv))) != 0:
                status = 'zero to 80 digits'
        if asyms:
            return 'zero at sampled weights (%s)' % status
        return True if status == 'exact' else status

    def zero(M):
        r = [zero1(x) for x in M]
        if all(z is True for z in r):
            return True
        if any(z is False for z in r):
            return False
        return sorted({z for z in r if z is not True}, key=str)
    res = {
        'W0': zero(Vp - v_W0p),
        'W1': zero(sp.eye(m) + Dthv - W1p),
        'W2': zero(psi_def - W2p),
        'psi_def==psi_flow': zero(psi_def - psi_flow),
        'W3': zero(sdsTheta - W3p),
        # отрицательный контроль: (W2) без множителя 2 при (s d_s P_u) ubar
        'NEG_W2_factor': zero(psi_def - NEG_W2),
        # отрицательный контроль: (W1) без сопряжения s^A (.) s^{-A}
        'NEG_W1_noconj': zero(sp.eye(m) + Dthv - NEG_W1),
    }
    return res


if __name__ == '__main__':
    rnd = random.Random(7)
    print('m=2, symbolic weights, random-rational coefficients (3 trials):')
    for t in range(3):
        print(' ', run(2, rnd=rnd))
    print('m=2, weights (0, 3/2) and (1/2, 2) -- with negative control:')
    for av in ((0, sp.Rational(3, 2)), (sp.Rational(1, 2), 2)):
        print(' ', av, run(2, a_vals=av, rnd=rnd))
    print('m=3, random rational weights (2 trials):')
    for t in range(2):
        av = tuple(sp.Rational(rnd.randint(0, 6), 2) for _ in range(3))
        print(' ', av, run(3, a_vals=av, rnd=rnd))
