# [Эксперимент] Вторая редакция записки notes/prover/2026-10-21-fold.md, замечание 3.4 (по R47, З6):
# символьная проверка формул для НЕтреугольного поля X = X^th(theta,eps) d_theta + X^eps(theta,eps) d_eps в карте
# Pi(s,theta,eps) = s omega(theta) + s^c eps n(theta), Y = Pi_s - (X^th/s) Pi_theta - (X^eps/s) Pi_eps:
#  (i)  s D_Y Y = (3.4)[X^th(theta,eps), X^th' := d_theta X^th] + X^eps d_eps X^th (1-epsilon) l;
#  (ii) s<w,D_w Y> = (3.5)[то же] - d_eps X^th (1-epsilon) s^(1-c) (w_n - c s^(c-1) eps w_omega) w_l;
#  (iii) при w_l = 1/sqrt2, w_n = sg/sqrt2, w_omega из (3.6) лишний член (ii) равен
#        -sg d_eps X^th (1-epsilon) s^(1-c)/2 + c eps d_eps X^th (1-epsilon) w_omega w_l.
# Общие многочлены k_g(theta), X^th(theta,eps), X^eps(theta,eps), символ c. Репер Дарбу, как в frames_X.py.
import random
import sympy as sp

S, TH, E = sp.symbols('S TH E', real=True)
c = sp.symbols('c', positive=True)
kc = sp.symbols('k0:3')
xt = sp.symbols('xt0:3_0:3')
xe = sp.symbols('xe0:3_0:3')
w1, w2, w3, sg = sp.symbols('w1 w2 w3 sg', real=True)


def kf(t):
    return sum(kc[i]*t**i for i in range(3))


def Xt(t, e):
    return sum(xt[3*i + j]*t**i*e**j for i in range(3) for j in range(3))


def Xe(t, e):
    return sum(xe[3*i + j]*t**i*e**j for i in range(3) for j in range(3))


def D(vec, var, th):
    A, B, C = vec
    thv = sp.diff(th, var)
    k = kf(th)
    return (sp.diff(A, var) - B*thv, sp.diff(B, var) + (A - C*k)*thv, sp.diff(C, var) + B*k*thv)


def zero(e):
    e = sp.expand(sp.powsimp(sp.expand(e), force=True))
    if e == 0:
        return True
    rnd = random.Random(11)
    for _ in range(8):
        sub = {v: sp.Rational(rnd.randint(-9, 9), rnd.randint(1, 9)) for v in e.free_symbols}
        sub[S] = sp.Rational(rnd.randint(1, 9), rnd.randint(10, 19))
        sub[c] = sp.Rational(rnd.randint(11, 29), 10)
        val = sp.N(e.subs(sub), 60)
        if abs(val) > sp.Float('1e-45'):
            return False
    print('      (тождество подтверждено численно в 8 случайных точках, 60 знаков)')
    return True


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
a, b = Xt(TH, E), Xe(TH, E)
Y = tuple(PiS[i] - a/S*PiT[i] - b/S*PiE[i] for i in range(3))
nu = S**(c - 1)*(c*E - b)
report('(3.3) Y = omega - X^th(1-epsilon) l + nu n  (X^th зависит от eps)',
       all(zero(t) for t in [Y[0] - 1, Y[1] + a*(1 - eps), Y[2] - nu]))


def DY(coef):
    d = [D(Y, v, TH) for v in (S, TH, E)]
    return tuple(sum(coef[j]*d[j][i] for j in range(3)) for i in range(3))


sDYY = tuple(S*t for t in DY((1, -a/S, -b/S)))
at = sp.diff(a, TH)
nut = sp.diff(nu, TH)
epst = sp.diff(eps, TH)
pred = (-a**2*(1 - eps),
        (c - 1)*a*eps - a*(1 - at*(1 - eps) + a*epst - nu*k) - b*S**(c - 1)*a*k,
        (c - 1)*nu - a*(nut - a*(1 - eps)*k) - b*S**(c - 1)*(c - sp.diff(b, E)))
extraY = (0, b*sp.diff(a, E)*(1 - eps), 0)
report('(i) s D_Y Y = (3.4) + X^eps d_eps X^th (1-epsilon) l',
       all(zero(sDYY[i] - pred[i] - extraY[i]) for i in range(3)))

As = w1
At = w2/(S*(1 - eps))
Ae = (w3 - w1*c*S**(c - 1)*E)/S**c
lhs = S*dot((w1, w2, w3), DY((As, At, Ae)))
rhs = ((1/(1 - eps) - at)*w2**2 + a*w1*w2 + (c - sp.diff(b, E))*w3**2
       + ((a*epst - nu*k)*w2**2 + nut*w2*w3)/(1 - eps)
       + (c - 1)*w1*(a*eps*w2 + nu*w3)
       - c*S**(c - 1)*E*w1*(a*k*w2 + (c - sp.diff(b, E))*w3))
bad = -sp.diff(a, E)*(1 - eps)*S**(1 - c)*(w3 - c*S**(c - 1)*E*w1)*w2
report('(ii) s<w,D_w Y> = (3.5) - d_eps X^th (1-epsilon) s^(1-c) (w_n - c s^(c-1) eps w_omega) w_l',
       zero(sp.together(lhs - rhs - bad)))

r2 = sp.sqrt(2)
wom = a*(1 - eps)*w2 - nu*w3
sub = {w2: 1/r2, w3: sg/r2}
bad_sub = bad.subs(w1, wom).subs(sub)
exp_sub = (-sg*sp.diff(a, E)*(1 - eps)*S**(1 - c)/2
           + c*E*sp.diff(a, E)*(1 - eps)*wom.subs(sub)/r2)
report('(iii) лишний член при w_l = 1/sqrt2, w_n = sg/sqrt2, w perp Y', zero(sp.expand(bad_sub - exp_sub).subs(sg**2, 1)))
report('(iii) w perp Y при этом выборе', zero(dot((wom, w2, w3), Y).subs(sub)))
print('ИТОГ:', 'все проверки OK' if ok_all else 'есть FAIL')
