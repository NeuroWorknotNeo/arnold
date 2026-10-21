"""[Эксперимент] Проверка предложения 3 (склейка карт) results/004-lemmaR.md (prover, 21.10.2026).

Вопрос: при склейке полей двух карт одного режима разбиением единицы по угловой координате
  A = V + phi_1 W_1 + phi_2 W_2
сохраняются ли A(U) = dU + (1 - chi(F)) U_+, sym DA >= (1 - O(r^kappa)) I и |A| = O(r), а
добавочный член sum_a W_a (x) grad phi_a = (W_1 - W_2) (x) grad phi_1 имеет порядок r^e?
Пример: n = 2, U = x^3 - 3 x y^2 + (x^2 + y^2)^2 + x y^3 = r^3 cos 3th + r^4 (1 + cos th sin^3 th)
  (H != 0 на перекрытии карт, так что U_+ = r^4 H там не мал).
  Карта 1: Phi_1(r, v) = r (cos v, sin v), |v| < 2.2.
  Карта 2: Phi_2(r, v) = r (cos g(v), sin g(v)), g(v) = pi + v + 0.4 sin v, |v| < 2.2 --
           другая евклидова метрика по углу, поэтому W_2 != W_1 на перекрытии.
  Данные леммы R: s = 1, k = 0, N = 1, d = 3, e = 1, F_a = cos 3g_a, H_a = h(g_a),
  J = {r, 0}, D_J = 9 F^2 + F'^2 >= 9 min(1, g'^2) > 0, c_0 = 0.5; kappa = min(1/N, e) = 1.
  Условие (C1): обе карты -- полярные, r общий, Phi_1(t, v) = Phi_2(t, v') при g(v') = v.
  Разбиение единицы: psi_1(th) = 1 при |th| <= 1.2, 0 при |th| >= 2.0 (C^infty), psi_2 = 1 - psi_1.
Метод: поле строго по шагу 3 в каждой карте; DA -- центральные разности в mpmath (60 знаков,
  шаг h = 1e-25 r); 160 углов (равномерно + сгущение в зонах перекрытия), r = 1e-2 ... 1e-8.
Запуск: ~/venv/bin/python check_gluing.py
Это не доказательство: один пример с n = 2.
"""
import mpmath as mp

mp.mp.dps = 60
c0 = mp.mpf('0.5')
d, e = 3, 1


def hstep(u):
    # C^infty step: 0 for u <= 0, 1 for u >= 1
    if u <= 0:
        return mp.mpf(0)
    if u >= 1:
        return mp.mpf(1)
    a, b = mp.e**(-1 / u), mp.e**(-1 / (1 - u))
    return a / (a + b)


def chi(Fv):
    return 1 - hstep((abs(Fv) - c0 / 2) / (c0 / 2))


def psi1(th):
    return 1 - hstep((abs(th) - mp.mpf('1.2')) / mp.mpf('0.8'))


def h(t):
    return 1 + mp.cos(t) * mp.sin(t)**3


def dh(t):
    return -mp.sin(t)**4 + 3 * mp.cos(t)**2 * mp.sin(t)**2


def U(x):
    X, Y = x
    return X**3 - 3 * X * Y**2 + (X**2 + Y**2)**2 + X * Y**3


def gradU(x):
    X, Y = x
    return (3 * X**2 - 3 * Y**2 + 4 * X * (X**2 + Y**2) + Y**3,
            -6 * X * Y + 4 * Y * (X**2 + Y**2) + 3 * X * Y**2)


charts = {
    1: (lambda v: v, lambda v: mp.mpf(1)),
    2: (lambda v: mp.pi + v + mp.mpf('0.4') * mp.sin(v), lambda v: 1 + mp.mpf('0.4') * mp.cos(v)),
}


def chart_coord(a, x):
    th = mp.atan2(x[1], x[0])
    if a == 1:
        return th
    t = mp.atan2(-x[1], -x[0])        # th - pi, normalized to (-pi, pi]
    return mp.findroot(lambda v: v + mp.mpf('0.4') * mp.sin(v) - t, t / mp.mpf('1.2'))


def W(a, x):
    """Field W_a of chart a (step 3), Euclidean representation."""
    g, gp = charts[a]
    r = mp.sqrt(x[0]**2 + x[1]**2)
    v = chart_coord(a, x)
    G = g(v)
    F, Fp = mp.cos(3 * G), -3 * mp.sin(3 * G) * gp(v)
    Hh, Hp = h(G), dh(G) * gp(v)
    Uc = r**3 * F + r**4 * Hh
    rdrU = 3 * r**3 * F + 4 * r**4 * Hh
    dvU = r**3 * Fp + r**4 * Hp
    Uplus = r**4 * Hh                 # r d_r U - d U
    den = rdrU**2 + dvU**2
    k = -chi(F) * Uplus / den
    Wr, Wv = k * rdrU * r, k * dvU   # coefficients of d_r and d_v
    er = (mp.cos(G), mp.sin(G))
    ev = (-mp.sin(G) * r * gp(v), mp.cos(G) * r * gp(v))
    return (Wr * er[0] + Wv * ev[0], Wr * er[1] + Wv * ev[1]), F, Uplus, Uc


def A(x):
    th = mp.atan2(x[1], x[0])
    p1 = psi1(th)
    out = [x[0], x[1]]
    for a, p in ((1, p1), (2, 1 - p1)):
        if p != 0:
            w = W(a, x)[0]
            out[0] += p * w[0]
            out[1] += p * w[1]
    return out


def jac(f, x, hh):
    J = mp.matrix(2, 2)
    for j in range(2):
        xp, xm = list(x), list(x)
        xp[j] += hh
        xm[j] -= hh
        fp, fm = f(xp), f(xm)
        for i in range(2):
            J[i, j] = (fp[i] - fm[i]) / (2 * hh)
    return J


angles = [mp.mpf(i) * 2 * mp.pi / 100 - mp.pi + mp.mpf('0.0123') for i in range(100)]
angles += [s * (mp.mpf('1.2') + mp.mpf('0.8') * i / 30) for i in range(1, 30) for s in (1, -1)]

for rv in ['1e-2', '1e-4', '1e-6', '1e-8']:
    r = mp.mpf(rv)
    lmin, devmax, ratio_min, idmax, glue_max, diffW_max, Amax = mp.inf, 0, mp.inf, 0, 0, 0, 0
    for th in angles:
        x = [r * mp.cos(th), r * mp.sin(th)]
        hh = r * mp.mpf('1e-25')
        DA = jac(A, x, hh)
        S = (DA + DA.T) / 2
        ev = mp.eigsy(S)[0]
        lmin = min(lmin, min(ev[0], ev[1]))
        devmax = max(devmax, mp.mnorm(DA - mp.eye(2), 1) / r)
        Ax = A(x)
        Amax = max(Amax, mp.sqrt(Ax[0]**2 + Ax[1]**2) / r)
        gu = gradU(x)
        AU = Ax[0] * gu[0] + Ax[1] * gu[1]
        Uv = U(x)
        # identity A(U) = dU + (1 - chi(F)) U_+ (F, U_+ do not depend on the chart)
        a0 = 1 if psi1(th) > 0 else 2
        _, F, Uplus, Uc = W(a0, x)
        idmax = max(idmax, abs(AU - d * Uv - (1 - chi(F)) * Uplus) / r**3)
        if Uv < 0:
            ratio_min = min(ratio_min, AU / Uv)
        p1 = psi1(th)
        if 0 < p1 < 1:   # overlap: gluing term (W_1 - W_2) (x) grad psi_1
            W1, W2 = W(1, x)[0], W(2, x)[0]
            dW = (W1[0] - W2[0], W1[1] - W2[1])
            diffW_max = max(diffW_max, mp.sqrt(dW[0]**2 + dW[1]**2) / r**2)
            gp1 = jac(lambda z: [psi1(mp.atan2(z[1], z[0])), 0], x, hh)
            grad = (gp1[0, 0], gp1[0, 1])
            glue = mp.sqrt((dW[0]**2 + dW[1]**2) * (grad[0]**2 + grad[1]**2))
            glue_max = max(glue_max, glue / r)
    print(f"r={rv}: min lambda_min(sym DA)={mp.nstr(lmin, 10)}; max|DA-I|/r={mp.nstr(devmax, 6)}; "
          f"max|A|/r={mp.nstr(Amax, 8)}; min_(U<0) A(U)/U={mp.nstr(ratio_min, 8)} (need >= d/2=1.5); "
          f"max|A(U)-dU-(1-chi)U_+|/r^3={mp.nstr(idmax, 3)}; "
          f"overlap: max|W_1-W_2|/r^2={mp.nstr(diffW_max, 6)}, max|(W_1-W_2)(x)grad psi_1|/r={mp.nstr(glue_max, 6)}")
