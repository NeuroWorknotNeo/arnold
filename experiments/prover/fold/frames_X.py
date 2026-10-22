# [Эксперимент] Символьная проверка формул (3.2)-(3.7) §3.2 записки notes/prover/2026-10-21-fold.md (теорема X):
# карта Pi(s,theta,eps) = s*omega(theta) + s^c*eps*n(theta), поле
#     Y = Pi_s - (X^th(theta)/s) Pi_theta - (X^eps(theta,eps)/s) Pi_eps,
# k_g(theta), X^th(theta), X^eps(theta,eps) — общие многочлены, c — символ.
# Вектор хранится тройкой коэффициентов в репере Дарбу (omega, l, n):
#   omega' = l,  l' = -omega + k n,  n' = -k l   (производные по theta).
# Производная по переменной v при theta = theta(v):
#   D_v(A,B,C) = (A_v - B th_v, B_v + (A - C k) th_v, C_v + B k th_v).
import random
import sympy as sp

S, TH, E = sp.symbols('S TH E', real=True)
c = sp.symbols('c', positive=True)
kc = sp.symbols('k0:4')
xt = sp.symbols('xt0:4')
xe = sp.symbols('xe0:3_0:3')
w1, w2, w3 = sp.symbols('w1 w2 w3', real=True)


def kf(t):
    return sum(kc[i]*t**i for i in range(4))


def Xt(t):
    return sum(xt[i]*t**i for i in range(4))


def Xe(t, e):
    return sum(xe[3*i + j]*t**i*e**j for i in range(3) for j in range(3))


def D(vec, var, th):
    A, B, C = vec
    thv = sp.diff(th, var)
    k = kf(th)
    return (sp.diff(A, var) - B*thv, sp.diff(B, var) + (A - C*k)*thv, sp.diff(C, var) + B*k*thv)


def zero(e):
    e = sp.expand(sp.powsimp(sp.expand(e), force=True))
    if e == 0 or sp.simplify(e) == 0:
        return True
    rnd = random.Random(7)
    for _ in range(6):
        sub = {v: sp.Rational(rnd.randint(-9, 9), rnd.randint(1, 9)) for v in e.free_symbols}
        sub[S] = sp.Rational(rnd.randint(1, 9), rnd.randint(10, 19))
        sub[c] = sp.Rational(rnd.randint(11, 29), 10)
        val = sp.N(e.subs(sub), 60)
        if abs(val) > sp.Float('1e-45'):
            return False
    print('      (тождество подтверждено численно в 6 точках, 60 знаков)')
    return True


def vzero(v):
    return all(zero(t) for t in v)


def dot(a, b):
    return sum(p*q for p, q in zip(a, b))


ok_all = True


def report(name, flag):
    global ok_all
    ok_all = ok_all and flag
    print(('OK   ' if flag else 'FAIL ') + name)


k = kf(TH)
Pi = (S, sp.Integer(0), S**c*E)
PiS, PiT, PiE = D(Pi, S, TH), D(Pi, TH, TH), D(Pi, E, TH)
eps = S**(c - 1)*E*k
report('(3.2) Pi_s = omega + c s^(c-1) eps n', vzero([PiS[0] - 1, PiS[1], PiS[2] - c*S**(c - 1)*E]))
report('(3.2) Pi_theta = s(1-epsilon) l', vzero([PiT[0], PiT[1] - S*(1 - eps), PiT[2]]))
report('(3.2) Pi_eps = s^c n', vzero([PiE[0], PiE[1], PiE[2] - S**c]))

a, b = Xt(TH), Xe(TH, E)
Y = tuple(PiS[i] - a/S*PiT[i] - b/S*PiE[i] for i in range(3))
nu = S**(c - 1)*(c*E - b)
report('(3.3) Y = omega - X^th (1-epsilon) l + nu n', vzero([Y[0] - 1, Y[1] + a*(1 - eps), Y[2] - nu]))


def DY(coef):   # производная Y по направлению coef = (a^s, a^th, a^eps) в координатах
    d = [D(Y, v, TH) for v in (S, TH, E)]
    return tuple(sum(coef[j]*d[j][i] for j in range(3)) for i in range(3))


# (3.4): s D_Y Y
sDYY = tuple(S*t for t in DY((1, -a/S, -b/S)))
at = sp.diff(a, TH)
nut, nue = sp.diff(nu, TH), sp.diff(nu, E)
epst = sp.diff(eps, TH)
pred = (-a**2*(1 - eps),
        (c - 1)*a*eps - a*(1 - at*(1 - eps) + a*epst - nu*k) - b*S**(c - 1)*a*k,
        (c - 1)*nu - a*(nut - a*(1 - eps)*k) - b*S**(c - 1)*(c - sp.diff(b, E)))
report('(3.4) s D_Y Y', vzero([sDYY[i] - pred[i] for i in range(3)]))

# (3.5): s <w, D_w Y> для w = w1 omega + w2 l + w3 n
As = w1
At = w2/(S*(1 - eps))
Ae = (w3 - w1*c*S**(c - 1)*E)/S**c
wv = tuple(As*PiS[i] + At*PiT[i] + Ae*PiE[i] for i in range(3))
report('разложение w по Pi_s, Pi_theta, Pi_eps', vzero([wv[0] - w1, wv[1] - w2, wv[2] - w3]))
lhs = S*dot((w1, w2, w3), DY((As, At, Ae)))
rhs = ((1/(1 - eps) - at)*w2**2 + a*w1*w2 + (c - sp.diff(b, E))*w3**2
       + ((a*epst - nu*k)*w2**2 + nut*w2*w3)/(1 - eps)
       + (c - 1)*w1*(a*eps*w2 + nu*w3)
       - c*S**(c - 1)*E*w1*(a*k*w2 + (c - sp.diff(b, E))*w3))
report('(3.5) s <w, D_w Y>', zero(sp.together(lhs - rhs)))
# отрицательный контроль: если X^th зависит от eps, появляется член порядка s^(1-c)
a2 = Xt(TH) + xt[0]*E
Y2 = tuple(PiS[i] - a2/S*PiT[i] - b/S*PiE[i] for i in range(3))
d2 = [D(Y2, v, TH) for v in (S, TH, E)]
lhs2 = S*dot((w1, w2, w3), tuple(sum((As, At, Ae)[j]*d2[j][i] for j in range(3)) for i in range(3)))
extra = sp.together(lhs2 - rhs.subs(a, a2))
expected = -xt[0]*(1 - eps)*S**(1 - c)*(w3 - c*S**(c - 1)*E*w1)*w2
report('контроль: при X^th = X^th(theta) + xt0*eps лишний член = -xt0 (1-eps) s^(1-c) (w_n - c s^(c-1) eps w_omega) w_l',
       zero(extra - expected))

# (3.6): w ⟂ Y <=> w_omega = X^th (1-eps) w_l - nu w_n
report('(3.6) <w,Y> = w_omega - X^th(1-eps) w_l + nu w_n', zero(dot((w1, w2, w3), Y) - (w1 - a*(1 - eps)*w2 + nu*w3)))

# (3.7): beta W - s Y W = s^beta [X Ftil - (sigma/N) d_sigma Ftil]
N, beta, a0 = sp.symbols('N beta a0', positive=True)
Ft = sp.Function('F')
sig = S**(1/N)
Wc = S**beta*(Ft(sig, TH, E) + a0)
YW = sp.diff(Wc, S) - a/S*sp.diff(Wc, TH) - b/S*sp.diff(Wc, E)
s1, t1, e1 = sp.symbols('s1 t1 e1')
F_ = Ft(s1, t1, e1)
rhs6 = S**beta*((a*sp.diff(F_, t1) + b*sp.diff(F_, e1) - s1/N*sp.diff(F_, s1)).subs({s1: sig, t1: TH, e1: E}))
diff6 = sp.simplify(beta*Wc - S*YW - rhs6)
report('(3.7) beta W - s Y W', diff6 == 0)
print('ИТОГ:', 'все проверки OK' if ok_all else 'есть FAIL')
