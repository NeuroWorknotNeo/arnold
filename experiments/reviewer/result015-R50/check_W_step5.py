# R50: независимая символьная проверка формул, на которые опирается доказательство теоремы MT
# (results/015-master.md, §7): (W0)-(W3), формула для s d_s(v o Theta)|_b из п. 5, компоненты
# квадратной скобки (W2) из п. 4. [Эксперимент]: sympy, n-1 = 2 (одно коническое направление
# с весом 1, одно узкое с весом 1+a), P и xi - случайные многочлены общего вида.
import random
import sympy as sp

random.seed(7)
s, b1, b2, kap = sp.symbols('s b1 b2 kappa', positive=True)
u1, u2 = sp.symbols('u1 u2')


def rpoly(vars_, deg):
    terms = 0
    mons = [sp.Integer(1)]
    for v in vars_:
        mons = [m*v**k for m in mons for k in range(deg + 1)]
    for m in mons:
        if sp.Poly(m, *vars_).total_degree() <= deg:
            terms += sp.Rational(random.randint(-5, 5), random.randint(1, 4))*m
    return terms


def pts(M, n=4):
    # значения невязки в n случайных точках (s - точная 6-я степень рационального, чтобы s^a было рационально)
    out = []
    for _ in range(n):
        t = sp.Rational(random.randint(1, 9), random.randint(10, 19))
        sub_ = {s: t**6, b1: sp.Rational(random.randint(-9, 9), 7), b2: sp.Rational(random.randint(-9, 9), 5),
                kap: sp.Rational(random.randint(1, 9), 11)}
        val = sp.Matrix(M).subs(sub_)
        out.append(max(abs(sp.nsimplify(sp.simplify(x))) for x in val))
    return sp.Matrix(out)


def run(a):
    A = sp.diag(0, a)
    sA = sp.diag(1, s**a)
    P = sp.Matrix([u1 + rpoly([s, u1, u2], 2), u2 + rpoly([s, u1, u2], 2)])
    xic = rpoly([s, b1], 2)            # коническая компонента xi^c(s,b1), не зависит от b2
    xin = rpoly([s, b1, b2], 2)        # узкая компонента
    xi = sp.Matrix([kap*xic, xin])
    b = sp.Matrix([b1, b2])
    ub = sA*b                          # u = s^A b
    sub = {u1: ub[0], u2: ub[1]}
    Theta = P.subs(sub)
    Pu = P.jacobian([u1, u2])
    # (W0) по определению: поток s db/ds = -xi, v = s dTheta/ds вдоль потока
    v_def = s*sp.diff(Theta, s) - Theta.jacobian([b1, b2])*xi
    ubar = sA*(A*b - xi)
    v_W0 = (s*sp.diff(P, s)).subs(sub) + Pu.subs(sub)*ubar
    r0 = pts(v_def - v_W0)
    # п. 5: s d_s (v o Theta)|_b
    lhs5 = s*sp.diff(v_def, s)
    sPu = (s*sp.diff(Pu, s))
    # D^2_u P(z, .) как матрица: (D^2 P(z,.))_{ij} = sum_k d^2P_i/du_k du_j z_k
    def D2(z):
        M = sp.zeros(2, 2)
        for i in range(2):
            for j in range(2):
                M[i, j] = sum(sp.diff(P[i], [u1, u2][k], [u1, u2][j])*z[k] for k in range(2))
        return M
    dsPu = sPu.subs(sub) + D2(sA*A*b).subs(sub)
    sdsxi = s*sp.diff(xi, s)
    rhs5 = (s*sp.diff(s*sp.diff(P, s), s)).subs(sub) + sPu.subs(sub)*sA*A*b + dsPu*ubar \
        + Pu.subs(sub)*(A*ubar - sA*sdsxi)
    r5 = pts(lhs5 - rhs5)
    # (W3): s d_s v|_theta = s d_s(v o Theta)|_b - D_theta v (s d_s P + P_u s^A A b)
    J = Theta.jacobian([b1, b2])
    Dthv = v_def.jacobian([b1, b2])*J.inv()
    # s d_s v|_theta вычислим через замену: d/ds|_theta = d/ds|_b - D_b(.) J^{-1} d_s Theta|_b
    sdv_theta = lhs5 - v_def.jacobian([b1, b2])*J.inv()*(s*sp.diff(Theta, s))
    rhsW3 = lhs5 - Dthv*((s*sp.diff(P, s)).subs(sub) + Pu.subs(sub)*sA*A*b)
    r3 = pts(sdv_theta - rhsW3)
    # (W1): I + D_theta v = P_u N P_u^{-1}
    N = sp.eye(2) + A + Pu.subs(sub).inv()*(dsPu - D2(sA*xi).subs(sub)) - sA*xi.jacobian([b1, b2])*sA.inv()
    r1 = pts(sp.eye(2) + Dthv - Pu.subs(sub)*N*Pu.subs(sub).inv())
    # (W2): psi = v + s dv/ds вдоль потока
    psi_def = v_def + lhs5 - v_def.jacobian([b1, b2])*xi
    br = (sp.eye(2) + A)*ubar - sA*(A*xi + sdsxi - xi.jacobian([b1, b2])*xi)
    psi_W2 = (s*sp.diff(P, s)).subs(sub) + (s*sp.diff(s*sp.diff(P, s), s)).subs(sub) \
        + 2*sPu.subs(sub)*ubar + sp.Matrix([sum(sp.diff(P[i], [u1, u2][k], [u1, u2][j])*ubar[k]*ubar[j]
                                                 for k in range(2) for j in range(2)) for i in range(2)]).subs(sub) \
        + Pu.subs(sub)*br
    r2 = pts(psi_def - psi_W2)
    # п. 4: компоненты скобки
    br_n = s**a*((1 + a)*(a*b2 - xin) - a*xin - s*sp.diff(xin, s) + (xi.jacobian([b1, b2])*xi)[1])
    br_c = -kap*xic - kap*s*sp.diff(xic, s) + kap**2*sp.diff(xic, b1)*xic
    rb = pts(sp.Matrix([br_c, br_n]) - br)
    return r0, r5, r3, r1, r2, rb


for a in [sp.Rational(1, 2), sp.Rational(3, 2), sp.Rational(1, 3)]:
    res = run(a)
    print('a =', a, ': (W0)', list(res[0]), ' step5', list(res[1]), ' (W3)', list(res[2]),
          ' (W1)', list(res[3]), ' (W2)', list(res[4]), ' bracket', list(res[5]))
