"""[Эксперимент] Независимая проверка леммы R и предложения 3 из results/004-lemmaR.md
(reviewer, 21.10.2026).

Вопрос: даёт ли построение поля из 004 (шаг 3) в карте с n = 3, s = 1, k = 1, нелинейной G и
ненулевой H оценки леммы R:  ||DA - L|| = O(r^kappa),  lambda_min(sym DA) -> 1,
A(U) = dU + (1-chi(F))U_+;  и что ломается, если взять J не внутри J_max (контроль).
Склейка (предложение 3): две карты одного глобального отображения, связанные заменой
(theta, y) = (theta' + 0.3 sin theta',  g(theta') y' + h(theta')) -- угловой репараметризацией
и сдвигом/растяжением нормальной координаты, зависящими от угла. (C1) выполнено, (C2): psi(theta).

Метод: Phi, U o Phi и их первые производные -- символьно (sympy -> mpmath), поле Z(p) = DPhi(p) A^(p)
в координатах p = (r, theta, y); DA = D_p Z * DPhi^{-1}, D_p Z -- центральные разности в mpmath
(80 знаков, шаг 1e-25 относительно eps по eps, 1e-25 по theta, y).  r = eps^N.

Запуск: ~/venv/bin/python check_chart_n3.py
Это не доказательство: один пример.
"""
import sympy as sp
import mpmath as mp

mp.mp.dps = 80
eps, th, y = sp.symbols('eps th y', real=True)
c0 = mp.mpf('0.5')


def hstep(u):
    if u <= 0:
        return mp.mpf(0)
    if u >= 1:
        return mp.mpf(1)
    a, b = mp.e**(-1 / u), mp.e**(-1 / (1 - u))
    return a / (a + b)


def chi(Fv):
    return 1 - hstep((abs(Fv) - c0 / 2) / (c0 / 2))


def make_chart(Nv, w1, ev, d):
    a = int(Nv * (w1 - 1))
    Ne = int(Nv * ev)
    assert a == Nv * (w1 - 1) and Ne == Nv * ev
    mu = eps**a * y
    G = sp.Matrix([
        sp.cos(th) + sp.Rational(3, 10) * eps * sp.sin(th) + sp.Rational(2, 5) * mu**2
        + sp.Rational(1, 10) * eps * mu + sp.Rational(1, 5) * eps**2,
        sp.sin(th) + sp.Rational(1, 5) * eps - sp.Rational(1, 10) * mu**2
        + sp.Rational(3, 10) * eps * mu * sp.cos(th),
        mu + sp.Rational(1, 2) * eps * sp.cos(2 * th) + sp.Rational(1, 5) * mu**2 * sp.sin(th)
        + sp.Rational(7, 10) * eps**2 + sp.Rational(3, 10) * mu**3,
    ])
    r = eps**Nv
    Phi = r * G
    J = Phi.jacobian([eps, th, y])
    F = y**2 - sp.cos(th) - sp.Rational(1, 2)
    H = 2 * sp.cos(th + y) + eps * y**2 + sp.Rational(13, 10)
    Uc = r**d * (F + eps**Ne * H)
    grad = [sp.diff(Uc, v) for v in (eps, th, y)]
    f = lambda ex: sp.lambdify((eps, th, y), ex, 'mpmath')
    return dict(N=Nv, w1=mp.mpf(w1), e=ev, d=d, Phi=f(Phi), J=f(J), F=f(F), U=f(Uc),
                grad=[f(gg) for gg in grad])


def coords_data(C, p):
    """DPhi in (r,th,y), r d_r U, d_th U, d_y U, U, F at p = (eps, th, y)."""
    e_, t_, y_ = p
    N = C['N']
    Jm = mp.matrix(C['J'](e_, t_, y_))
    for i in range(3):
        Jm[i, 0] = Jm[i, 0] / (N * e_**(N - 1))
    Ue, Ut, Uy = [g(e_, t_, y_) for g in C['grad']]
    return Jm, e_ / N * Ue, Ut, Uy, C['U'](e_, t_, y_), C['F'](e_, t_, y_)


def What(C, rdrU, Ut, Uy, U, Fv, r, Jset, metric=None):
    """Components of W^ in (r, th, y) for J subset of {'r','0','1'}; metric = None (chart is
    Euclidean in its own coordinates)."""
    d = C['d']
    Uplus = rdrU - d * U
    ch = chi(Fv)
    if ch == 0:
        return [mp.mpf(0)] * 3, Uplus
    den = (rdrU**2 if 'r' in Jset else 0) + (Ut**2 if '0' in Jset else 0) + (Uy**2 if '1' in Jset else 0)
    k = -ch * Uplus / den
    return [k * rdrU * r if 'r' in Jset else 0, k * Ut if '0' in Jset else 0,
            k * Uy if '1' in Jset else 0], Uplus


def Z_single(C, Jset):
    def Z(p):
        e_ = p[0]
        r = e_**C['N']
        DP, rdrU, Ut, Uy, U, Fv = coords_data(C, p)
        W, _ = What(C, rdrU, Ut, Uy, U, Fv, r, Jset)
        Ah = mp.matrix([r + W[0], W[1], W[2]])
        return DP * Ah
    return Z


def DA_of(Zfun, C, p):
    e_, t_, y_ = p
    N = C['N']
    DP = coords_data(C, p)[0]
    cols = []
    for j, hh in enumerate([e_ * mp.mpf('1e-25'), mp.mpf('1e-25'), mp.mpf('1e-25')]):
        pp, pm = list(p), list(p)
        pp[j] += hh
        pm[j] -= hh
        col = (Zfun(pp) - Zfun(pm)) / (2 * hh)
        if j == 0:
            col = col / (N * e_**(N - 1))
        cols.append(col)
    DZ = mp.matrix(3, 3)
    for j in range(3):
        for i in range(3):
            DZ[i, j] = cols[j][i]
    return DZ * mp.inverse(DP)


def report(C, Zfun, Jset_for_identity, label, kappa, pts, rs):
    L = mp.diag([1, 1, C['w1']])
    print(label)
    for rv in rs:
        r = mp.mpf(rv)
        e_ = r**(mp.mpf(1) / C['N'])
        dev, lmin, idmax, ratio = 0, mp.inf, 0, mp.inf
        for (t_, y_) in pts:
            p = [e_, t_, y_]
            DA = DA_of(Zfun, C, p)
            S = (DA + DA.T) / 2
            ev = mp.eigsy(S)[0]
            lmin = min(lmin, min(ev[i] for i in range(3)))
            dev = max(dev, mp.norm(DA - L, 2))   # Frobenius >= operator norm
            # identity A(U) = dU + (1-chi)U_+ via chain rule: <Z, grad_x U> = D_pU * DPhi^{-1} * Z
            DP, rdrU, Ut, Uy, U, Fv = coords_data(C, p)
            gp = mp.matrix([[rdrU / r, Ut, Uy]])   # d_r U, d_th U, d_y U
            gx = gp * mp.inverse(DP)
            Zp = Zfun(p)
            AU = (gx * Zp)[0, 0]
            Uplus = rdrU - C['d'] * U
            idmax = max(idmax, abs(AU - C['d'] * U - (1 - chi(Fv)) * Uplus) / r**C['d'])
            if U < 0:
                ratio = min(ratio, AU / U)
        print(f"  r={rv}: max||DA-L||={mp.nstr(dev, 6)}  /r^kappa={mp.nstr(dev / r**kappa, 6)}  "
              f"min eig sym DA={mp.nstr(lmin, 8)}  max|A(U)-dU-(1-chi)U+|/r^d={mp.nstr(idmax, 3)}  "
              f"min_(U<0) A(U)/U={mp.nstr(ratio, 6)}")


def sample_points(C):
    pts = []
    for t_ in ['-0.4', '0', '0.5', '1.0', '1.4']:
        for i in range(21):
            pts.append((mp.mpf(t_), mp.mpf(-2) + mp.mpf(4) * i / 20))
    # points in the transition zone of chi: |F| in (c0/2, c0)
    extra = []
    for t_ in ['-0.3', '0.2', '0.7', '1.2']:
        tv = mp.mpf(t_)
        for Fv in ['0.3', '0.4', '0.45', '-0.3', '-0.4', '-0.45']:
            yy2 = mp.mpf(Fv) + mp.cos(tv) + mp.mpf('0.5')
            if yy2 > 0:
                extra += [(tv, mp.sqrt(yy2)), (tv, -mp.sqrt(yy2))]
    return pts + extra


if __name__ == '__main__':
    rs = ['1e-4', '1e-8', '1e-12', '1e-16', '1e-20', '1e-24']
    # E1: N=4, w1=3/2, e=3/4, d=2: J_max = {r,0,1}, kappa = min(1/4, e+1-w1=1/4, e) = 1/4
    C1 = make_chart(4, sp.Rational(3, 2), sp.Rational(3, 4), 2)
    pts = sample_points(C1)
    report(C1, Z_single(C1, {'r', '0', '1'}), None, 'E1: N=4, w1=3/2, e=3/4, J=J_max={r,0,1}, kappa=1/4',
           mp.mpf(1) / 4, pts, rs)
    # E2: e=1/4: J_max={1}; J={1}, kappa = min(1/4, 1/4) = 1/4
    C2 = make_chart(4, sp.Rational(3, 2), sp.Rational(1, 4), 2)
    report(C2, Z_single(C2, {'1'}), None, 'E2: N=4, w1=3/2, e=1/4, J=J_max={1}, kappa=1/4',
           mp.mpf(1) / 4, pts, rs)
    # E3 (control): e=1/4 but J={r,0,1} not in J_max: expect blow-up ~ r^{e+1-w1} = r^{-1/4}
    report(C2, Z_single(C2, {'r', '0', '1'}), None,
           'E3 (control, J not in J_max): N=4, w1=3/2, e=1/4, J={r,0,1}; expect ||DA-L|| ~ r^{-1/4}',
           mp.mpf(1) / 4, pts, rs)
