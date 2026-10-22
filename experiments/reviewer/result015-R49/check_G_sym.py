"""R49: независимая символьная проверка леммы G (results/015-master.md), [Эксперимент].

Идея: тождества (G0)-(G3) поточечные и зависят только от 2-струи Upsilon в точке theta
и 1-струи v в точке (s, theta). Поэтому берём ОБЩИЕ струи с символьными коэффициентами
(Upsilon = U0 + U1 th + 1/2 U2(th,th), v = v0 + V1 th + vs (s'-s)), сдвигая точку в th = 0.
Производные поля Y в объемлющем пространстве считаем честно: D_q Y = D_{(s,th)} y * (D Pi)^{-1},
grad rho = первая строка (D Pi)^{-1} (так как rho o Pi = s). Обратную матрицу считаем через
присоединённую и определитель; тождества проверяем как полиномиальные (после умножения на
степень det) при n = 2, 3, а при n = 4, 5 -- подстановкой случайных рациональных чисел
(точная арифметика, лемма Шварца-Зиппеля).
"""
import random
import sys
import sympy as sp


def build(n, numeric=None):
    m = n - 1
    s = sp.Symbol('s', positive=True)
    th = sp.symbols('t0:%d' % m)
    sp_ = sp.Symbol('sp')  # переменная s'
    # символы струй
    U0 = sp.Matrix(n, 1, lambda i, _: sp.Symbol('U0_%d' % i))
    U1 = sp.Matrix(n, m, lambda i, j: sp.Symbol('U1_%d_%d' % (i, j)))
    U2 = [[[sp.Symbol('U2_%d_%d_%d' % (i, min(j, k), max(j, k))) for k in range(m)]
           for j in range(m)] for i in range(n)]
    v0 = sp.Matrix(m, 1, lambda i, _: sp.Symbol('v0_%d' % i))
    V1 = sp.Matrix(m, m, lambda i, j: sp.Symbol('V1_%d_%d' % (i, j)))
    vs = sp.Matrix(m, 1, lambda i, _: sp.Symbol('vs_%d' % i))
    al = sp.Symbol('alpha')
    tau = sp.Matrix(m, 1, lambda i, _: sp.Symbol('tau_%d' % i))
    syms = list(U0) + list(U1) + sorted({x for a in U2 for b in a for x in b}, key=str) \
        + list(v0) + list(V1) + list(vs) + [al] + list(tau) + [s]
    subs = {}
    if numeric is not None:
        rnd = numeric
        for x in syms:
            subs[x] = sp.Rational(rnd.randint(-9, 9), rnd.randint(1, 5))
        subs[s] = sp.Rational(rnd.randint(1, 9), rnd.randint(1, 5))

    def S(e):
        return e.subs(subs) if subs else e

    thv = sp.Matrix(m, 1, list(th))
    Ups = sp.Matrix(n, 1, lambda i, _: U0[i] + sum(U1[i, j] * th[j] for j in range(m))
                    + sp.Rational(1, 2) * sum(U2[i][j][k] * th[j] * th[k]
                                              for j in range(m) for k in range(m)))
    DUps = Ups.jacobian(thv)
    v = v0 + V1 * thv + vs * (sp_ - s)
    y = Ups + DUps * v
    Pi = sp_ * Ups
    coords = sp.Matrix([sp_] + list(th))
    pt = {sp_: s, **{t: 0 for t in th}}
    Dy = y.jacobian(coords).subs(pt)
    DPi = Pi.jacobian(coords).subs(pt)
    Dy, DPi = S(Dy), S(DPi)
    Y = S(y.subs(pt))
    B = S(sp.Matrix.hstack(U0, U1))
    det = DPi.det()
    adj = DPi.adjugate()          # DPi^{-1} = adj/det
    DqY_num = Dy * adj            # D_q Y = DqY_num / det
    grad_rho_num = adj[0, :].T    # grad rho = grad_rho_num / det
    w = B * S(sp.Matrix([al] + list(tau)))
    alS, tauS = S(al), S(tau)
    G = S(U1.T * U1)
    k = S(U1.T * U0)
    v0S, V1S, vsS, U1S = S(v0), S(V1), S(vs), S(U1)
    U2S = [[[S(U2[i][j][kk]) for kk in range(m)] for j in range(m)] for i in range(n)]

    def D2(a, b):
        return sp.Matrix(n, 1, lambda i, _: sum(U2S[i][j][kk] * a[j] * b[kk]
                                                 for j in range(m) for kk in range(m)))
    sS = S(s)
    return dict(n=n, m=m, s=sS, det=det, DqY_num=DqY_num, grad_num=grad_rho_num, Y=Y, B=B,
                w=w, al=alS, tau=tauS, G=G, k=k, v0=v0S, V1=V1S, vs=vsS, U1=U1S, D2=D2)


def checks(d):
    n, m, s, det = d['n'], d['m'], d['s'], d['det']
    Y, B, w, al, tau = d['Y'], d['B'], d['w'], d['al'], d['tau']
    U1, v0, V1, vs, G, k, D2 = d['U1'], d['v0'], d['V1'], d['vs'], d['G'], d['k'], d['D2']
    I = sp.eye(m)
    res = {}
    # (G0): grad rho = nu = B^{-T} e1 ;  <nu, w> = alpha
    e1 = sp.Matrix([1] + [0] * (n - 1))
    # B^T nu = e1  <=>  B^T grad_num - det e1 = 0
    res['G0a'] = (B.T * d['grad_num'] - det * e1).expand()
    res['G0b'] = sp.expand((d['grad_num'].T * w)[0] - det * al)
    # (G1): с nu = grad rho, Y_T = Y - nu/|nu|^2 (так как <Y,nu> = 1)
    nu_num = d['grad_num']          # nu = nu_num/det
    nn = (nu_num.T * nu_num)[0]     # |nu|^2 det^2
    res['G1_Ynu'] = sp.expand((Y.T * nu_num)[0] - det)   # <Y,nu> = 1
    h = (Y.T * Y)[0]
    # Y_T = Y - nu/|nu|^2 = Y - nu_num*det/nn
    YT = Y - nu_num * det / nn
    YT2 = sp.together((YT.T * YT)[0])
    nu2 = nn / det**2
    lhs = sp.together(((nu_num / det - Y / h).T * (nu_num / det - Y / h))[0])
    rhs = sp.together(nu2**2 * YT2 / (1 + nu2 * YT2))
    res['G1_norm'] = sp.numer(sp.together(lhs - rhs)).expand()
    # (G1, вторая часть) при w ⟂ Y: берём проекцию w' = w - <Y,w>Y/h, её разложение
    # (alpha', tau') = B^{-1} w' и проверяем <grad rho - Y/h, w'> = alpha'
    wp = w - Y * (Y.T * w)[0] / h
    ab = B.adjugate() * wp / B.det()
    res['G1_w'] = sp.numer(sp.together(((nu_num / det - Y / h).T * wp)[0] - ab[0])).expand()
    # (G2): s nabla_Y Y = DUps psi + D2Ups(v,v),  psi = v + (D v) v + s d_s v
    psi = v0 + V1 * v0 + s * vs
    lhs2 = s * d['DqY_num'] * Y           # = det * s nabla_Y Y
    rhs2 = det * (U1 * psi + D2(v0, v0))
    res['G2'] = (lhs2 - rhs2).expand()
    # (G3)
    lhs3 = s * (w.T * d['DqY_num'] * w)[0]
    rhs3 = det * ((tau.T * G * (I + V1) * tau)[0] + al * (k.T * (I + V1) * tau)[0]
                  + al * (w.T * U1 * (s * vs))[0] + (w.T * D2(v0, tau))[0])
    res['G3'] = sp.expand(lhs3 - rhs3)
    # отрицательный контроль: без члена D2(v0,tau) тождество (G3) должно нарушаться
    res['NEG_G3_without_D2term'] = sp.expand(lhs3 - rhs3 + det * (w.T * D2(v0, tau))[0])
    res['NEG_G2_without_vs'] = (lhs2 - det * (U1 * (v0 + V1 * v0) + D2(v0, v0))).expand()
    out = {}
    for key, val in res.items():
        if isinstance(val, sp.MatrixBase):
            out[key] = all(sp.expand(x) == 0 for x in val)
        else:
            out[key] = sp.expand(val) == 0
    return out


if __name__ == '__main__':
    for n in (2, 3):
        d = build(n)
        print('n=%d symbolic:' % n, checks(d))
        sys.stdout.flush()
    rnd = random.Random(20261022)
    for n in (4, 5):
        allok = True
        for trial in range(6):
            r = checks(build(n, numeric=rnd))
            pos = {kk: vv for kk, vv in r.items() if not kk.startswith('NEG')}
            neg = {kk: vv for kk, vv in r.items() if kk.startswith('NEG')}
            allok = allok and all(pos.values()) and not any(neg.values())
            if not (all(pos.values()) and not any(neg.values())):
                print('FAIL n=%d trial %d' % (n, trial), r)
        print('n=%d random-rational (6 trials): all True =' % n, allok)
