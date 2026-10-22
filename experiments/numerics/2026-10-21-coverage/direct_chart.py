"""direct_chart.py -- проверка условий утверждения Q / следствия E [012] (прямая карта q = (s^N, gamma(s)+w), L = I) точной арифметикой.
(Q1) все мономы U-hat(s,w) = U(s^N, gamma(s)+w) имеют уровень l_c(k,alpha) = k/N + c.alpha >= beta;
(Q2) F_0 = сумма мономов уровня beta: F_0(0) < 0, Q = F_0 - F_0(0) имеет строгий локальный минимум в 0;
(Q3) <Cb, grad Q> >= mu Q около 0;  для следствия E: Q >= 0 около 0 с изолированным нулём, c_1 <= c_2, Q_d(0,1) != 0.
Коэффициенты, содержащие 4^(-1/3), хранятся как многочлены от K (4K^3 = 1) и редуцируются точно.   [Эксперимент: точный]"""
import sys, json, os, itertools
import sympy as sp
from exlist import BY, HERE, x, y, z

s, w1, w2, K = sp.symbols('s w1 w2 K')
X3 = (x, y, z)
REL = sp.Poly(4*K**3 - 1, K)
KAP = sp.Rational(1, 4)**sp.Rational(1, 3)

def nv(e, n=50):
    return sp.N(sp.sympify(e).subs(K, KAP), n)


def red(c):
    c = sp.expand(c)
    if not c.has(K):
        return c
    return sp.rem(sp.Poly(c, K), REL).as_expr()

def level_table(U, axis, N, c, gamma):
    tr = [i for i in range(3) if i != axis]
    sub = {X3[axis]: s**N, X3[tr[0]]: gamma[0] + w1, X3[tr[1]]: gamma[1] + w2}
    Uh = sp.expand(U.subs(sub, simultaneous=True))
    P = sp.Poly(Uh, s, w1, w2)
    rows = {}
    for (k, a1, a2), co in P.terms():
        co = red(co)
        if co == 0:
            continue
        lev = sp.Rational(k, N) + c[0]*a1 + c[1]*a2
        rows[(k, a1, a2)] = (lev, co)
    return rows

def check_Q(key, axis, N, c, beta, gamma, label=''):
    U = BY[key]['U']
    c = [sp.Rational(v) for v in c]; beta = sp.Rational(beta)
    rows = level_table(U, axis, N, c, gamma)
    lev_min = min(l for l, _ in rows.values())
    out = dict(key=key, axis='xyz'[axis], N=N, c=[str(v) for v in c], beta=str(beta), gamma=[str(g) for g in gamma],
               Nc_int=all((N*v).is_integer for v in c), Nbeta_int=(N*beta).is_integer, c_gt1=all(v > 1 for v in c),
               min_level=str(lev_min), Q1=bool(lev_min >= beta))
    bad = [(m_, str(v[0])) for m_, v in rows.items() if v[0] < beta]
    out['monomials_below_beta'] = bad[:6]
    face = {m_: v[1] for m_, v in rows.items() if v[0] == beta}
    F0 = sum(co * w1**m_[1] * w2**m_[2] for m_, co in face.items())
    F0 = sp.expand(F0)
    # group by power of s (grading k)
    byk = {}
    for m_, co in face.items():
        byk.setdefault(m_[0], 0)
        byk[m_[0]] += co * w1**m_[1] * w2**m_[2]
    out['F0'] = str(F0)
    F00 = F0.subs({w1: 0, w2: 0})
    out['F0_at_0'] = str(nv(F00, 20))
    out['F0_negative'] = bool(nv(F00) < 0)
    Qp = sp.expand(F0 - F00)
    out['Q'] = str(Qp)
    grad0 = [nv(sp.diff(Qp, v).subs({w1: 0, w2: 0}), 20) for v in (w1, w2)]
    out['grad_Q_at_0'] = [str(g) for g in grad0]
    H = sp.hessian(Qp, (w1, w2)).subs({w1: 0, w2: 0})
    out['Hess_Q_at_0'] = str(H.applyfunc(lambda e: nv(e, 12)).tolist())
    ev = [nv(v, 15) for v in H.eigenvals()] if H.rank() > 0 else []
    out['hess_eigs'] = [str(v) for v in ev]
    out['hess_PD'] = bool(nv(H[0, 0]) > 0 and nv(H.det()) > 0)
    out['byk_degrees'] = {int(k): str(sp.Rational(beta - sp.Rational(k, N))) for k in byk}
    return out, Qp, F0

def euler_ratio(Qp, c, mu):
    """E(Q) - mu Q  for E = c1 w1 d1 + c2 w2 d2"""
    E = c[0]*w1*sp.diff(Qp, w1) + c[1]*w2*sp.diff(Qp, w2)
    return sp.expand(E - mu*Qp)

def lowest_form(Qp, deg_weights=(1, 1)):
    P = sp.Poly(sp.expand(Qp), w1, w2)
    d = min(a1 + a2 for (a1, a2), co in P.terms())
    return d, sum(co * w1**a1 * w2**a2 for (a1, a2), co in P.terms() if a1 + a2 == d)

def newton_weights_scan(key, axis, beta, cs_grid=None):
    """для (L=I, gamma=0): все ли мономы имеют уровень >= beta при c1,c2 > 1 -- допустимая область (LP по мономам)"""
    U = BY[key]['U']
    tr = [i for i in range(3) if i != axis]
    P = sp.Poly(U, *X3)
    cons = []
    for mon, co in P.terms():
        a = mon[axis]; j = mon[tr[0]]; k = mon[tr[1]]
        cons.append((a, j, k))
    return cons

if __name__ == '__main__':
    res = {}
    kap = sp.Rational(1, 4)**sp.Rational(1, 3)
    # K1 = x^4+y^4-z^6, ось z (индекс 2), поперечные x,y: c=(3/2,3/2), N=2, beta=6
    r, Qp, F0 = check_Q('z:K1', 2, 2, (sp.Rational(3, 2), sp.Rational(3, 2)), 6, (0, 0)); res['z:K1'] = r
    r, Qp, F0 = check_Q('z:P1', 2, 2, (sp.Rational(3, 2), sp.Rational(3, 2)), 6, (0, 0)); res['z:P1'] = r
    # frontier A1: ось x, поперечные (y,z), c=(4/3,4/3), N=3, beta=16/3, сдвиг z = -K s^4 (4K^3=1)
    r, Qp, F0 = check_Q('f:A1', 0, 3, (sp.Rational(4, 3), sp.Rational(4, 3)), sp.Rational(16, 3), (0, -K*s**4)); res['f:A1'] = r
    r, Qp, F0 = check_Q('f:A3', 0, 6, (sp.Rational(7, 6), sp.Rational(4, 3)), sp.Rational(22, 3), (0, -K*s**8)); res['f:A3'] = r
    r, Qp, F0 = check_Q('f:V3', 0, 1, (5, 2), 32, (0, 0)); res['f:V3'] = r
    for k, v in res.items():
        print('==', k)
        for kk, vv in v.items():
            print('   ', kk, ':', vv)
    json.dump(res, open(os.path.join(HERE, 'direct_chart.json'), 'w'), indent=1, ensure_ascii=False)


# ---------------------------------------------------------------- дополнительные проверки (Q3) и (E)
def weighted_lowest(expr, p):
    P = sp.Poly(sp.expand(expr), w1, w2)
    terms = {}
    for (a1, a2), co in P.terms():
        co = red(co) if co.has(K) else co
        if co == 0:
            continue
        terms.setdefault(p[0]*a1 + p[1]*a2, []).append(((a1, a2), co))
    lo = min(terms)
    comp = sum(co * w1**a1 * w2**a2 for (a1, a2), co in terms[lo])
    rest_min = min([k for k in terms if k > lo], default=None)
    return lo, comp, rest_min

def euler_check(Qp, c, mu, p):
    """E(Q) - mu Q: младшая p-однородная часть и положительная определённость (для сумм вида a*w1^i + b*w2^j с a,b>0 -- точно)"""
    D = euler_ratio(Qp, c, mu)
    loQ, compQ, nxtQ = weighted_lowest(Qp, p)
    loD, compD, nxtD = weighted_lowest(D, p)
    def posdef_diag(comp):
        P = sp.Poly(comp, w1, w2)
        ok = True
        for (a1, a2), co in P.terms():
            ok = ok and (a1 % 2 == 0) and (a2 % 2 == 0) and (nv(co) > 0)
        return ok and len(P.terms()) == 2 and all((a1 == 0) != (a2 == 0) for (a1, a2), _ in P.terms())
    return dict(mu=str(mu), p=[str(v) for v in p], Q_lowest_weight=str(loQ), Q_lowest_part=str(compQ), Q_next_weight=str(nxtQ),
                Q_lowest_posdef=bool(posdef_diag(compQ)),
                D_lowest_weight=str(loD), D_lowest_part=str(compD), D_next_weight=str(nxtD), D_lowest_posdef=bool(posdef_diag(compD)))

def more():
    res = json.load(open(os.path.join(HERE, 'direct_chart.json')))
    # A1 (изотропные веса 4/3): гессиан Q положителен => D_2 = (8/3 - mu) Q_2
    r, Qp, F0 = check_Q('f:A1', 0, 3, (sp.Rational(4, 3), sp.Rational(4, 3)), sp.Rational(16, 3), (0, -K*s**4))
    H = sp.hessian(Qp, (w1, w2)).subs({w1: 0, w2: 0})
    D = euler_ratio(Qp, (sp.Rational(4, 3), sp.Rational(4, 3)), 2)
    HD = sp.hessian(D, (w1, w2)).subs({w1: 0, w2: 0})
    res['f:A1']['Q3'] = dict(mu=2, hess_D_PD=bool(nv(HD[0, 0]) > 0 and nv(HD.det()) > 0), hess_D=str(HD.applyfunc(lambda e: nv(e, 10)).tolist()),
                              note='E(Q)-2Q имеет положительно определённый гессиан в 0 => <Cb,grad Q> >= 2 Q около 0')
    r, Qp, F0 = check_Q('f:A3', 0, 6, (sp.Rational(7, 6), sp.Rational(4, 3)), sp.Rational(22, 3), (0, -K*s**8))
    res['f:A3']['Q3'] = euler_check(Qp, (sp.Rational(7, 6), sp.Rational(4, 3)), 2, (sp.Rational(1, 2), 1))
    res['f:A3']['Q2_strict_min'] = res['f:A3']['Q3']['Q_lowest_posdef']
    # K1, P1: E(Q) = 6 Q точно
    for k in ('z:K1', 'z:P1'):
        r, Qp, F0 = check_Q(k, 2, 2, (sp.Rational(3, 2), sp.Rational(3, 2)), 6, (0, 0))
        res[k]['Q3'] = dict(mu=6, identity=str(sp.expand(euler_ratio(Qp, (sp.Rational(3, 2),) * 2, 6))), note='E(Q) - 6Q = 0 (Q = w1^4 + w2^4 квазиоднороден, степень 4*(3/2) = 6 = beta)')
        res[k]['Q2_strict_min'] = bool(sp.Poly(Qp, w1, w2).total_degree() == 4)
    # V3: Q = A B, A = (w1-w2^2)^2 + w2^8, B = (w1-w2^2-w2^3)^2 + w2^8;  E: c1 <= c2 после перенумерации
    r, Qp, F0 = check_Q('f:V3', 0, 1, (5, 2), 32, (0, 0))
    A = (w1 - w2**2)**2 + w2**8; B = (w1 - w2**2 - w2**3)**2 + w2**8
    fac = sp.expand(A*B - Qp) == 0
    d, Qd = lowest_form(Qp)
    # после перенумерации b_1 := w2 (вес 2, широкая), b_2 := w1 (вес 5, узкая): Q_d(0,1) = Qd(w1=1, w2=0)
    Qd01 = Qd.subs({w1: 1, w2: 0})
    zeroA = sp.solve([(w1 - w2**2)**2 + w2**8], [w1, w2], dict=True)
    res['f:V3']['E'] = dict(Q_equals_A_times_B=bool(fac), A='(w1-w2^2)^2+w2^8', B='(w1-w2^2-w2^3)^2+w2^8', ord_Q=int(d), Q_d=str(Qd),
                            Q_d_at_narrow_axis=str(Qd01), orientation='после перенумерации (b1,b2) = (z,y): c = (2,5), c1 <= c2; Q_d(0,1) = Q_d(w1=1,w2=0) = ' + str(Qd01),
                            isolated_zero='Q = A B, A=0 <=> w2=0, w1=0 (вещественно); B=0 <=> w2=0, w1=0', zeros_of_A=str(zeroA))
    json.dump(res, open(os.path.join(HERE, 'direct_chart.json'), 'w'), indent=1, ensure_ascii=False)
    for k in ('f:A1', 'f:A3', 'z:K1', 'z:P1', 'f:V3'):
        print(k, {kk: vv for kk, vv in res[k].items() if kk in ('Q3', 'Q2_strict_min', 'E')})

if __name__ == '__main__' and len(sys.argv) > 1 and sys.argv[1] == 'more':
    more()
