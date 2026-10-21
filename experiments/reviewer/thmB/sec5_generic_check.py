"""[Эксперимент] Независимая проверка оценок §5 results/002-theorem-B.md (reviewer, 21.10.2026).

Вопрос: верно ли, что для ЛЮБОЙ гладкой Gamma вида (2.2)
    Gamma(theta,a,eps) = omega(theta) + eps*sum_i a_i e_i(theta) + eps^2*Gamma2(theta,a,eps)
(omega -- кривая на S^{n-1}, e_i -- ортонормированная рамка нормали (omega, omega')^perp)
и любых гладких c1(theta,a,eps), Y(theta,a,eps) поле
    A = V/(m+1) + r (c1 V + Y),  V = r d/dr,  Phi(r,theta,a) = r Gamma(theta,a,r^{1/2})
удовлетворяет DA^x = (I + P_N/2)/(m+1) + O(r^{1/2})?
Это проверяет дифференциально-геометрическую часть §5 отдельно от потенциала:
Gamma2, c1, Y -- случайные многочлены (не из U).
Параметры: n=4, s=1, c=2 (двумерный слой, рамка зависит от theta), m=4; seed=12345;
mpmath 60 знаков; якобианы -- численное дифференцирование mpmath (mp.diff) по координатам
(eps, theta, a1, a2), r = eps^2.
Запуск: ~/venv/bin/python sec5_generic_check.py
Это не доказательство.
"""
import random
import mpmath as mp

random.seed(12345)
mp.mp.dps = 60
m, n = 4, 4


def unit(v):
    return v/mp.norm(v)


def omega(t):
    w = mp.matrix([mp.cos(t), mp.sin(t), mp.cos(2*t)/2, mp.sin(3*t)/3 + 1])
    return unit(w)


def frame(t):
    om = omega(t)
    d = mp.matrix([mp.diff(lambda s: omega(s)[i], t) for i in range(n)])
    t1 = unit(d - (om.T*d)[0]*om)
    out = []
    for v in (mp.matrix([0, 0, 1, 0]), mp.matrix([0, 1, 0, 0])):
        for b in [om, t1] + out:
            v = v - (b.T*v)[0]*b
        out.append(unit(v))
    return out


C = [[mp.mpf(random.randint(-9, 9))/7 for _ in range(10)] for _ in range(8)]


def rp(k, t, b1, b2, e):
    c = C[k]
    mons = [1, b1, b2, e, t, b1*e, b2*t, e*e, b1*b2, t*e]
    return sum(ci*mi for ci, mi in zip(c, mons))


def Gamma(e, t, b1, b2):
    om = omega(t)
    e1, e2 = frame(t)
    G2 = mp.matrix([rp(i, t, b1, b2, e) for i in range(4)])
    return om + e*(b1*e1 + b2*e2) + e*e*G2


def Phi(y):
    e, t, b1, b2 = y
    return e*e*Gamma(e, t, b1, b2)


def jac(F, y):
    cols = []
    for j in range(4):
        def Fj(s, j=j):
            yy = list(y)
            yy[j] = s
            return F(yy)
        cols.append(mp.matrix([mp.diff(lambda s: Fj(s)[i], y[j]) for i in range(n)]))
    J = mp.matrix(n, 4)
    for j in range(4):
        for i in range(n):
            J[i, j] = cols[j][i]
    return J


def Ahat(y):
    e, t, b1, b2 = y
    r = e*e
    c1 = rp(4, t, b1, b2, e)
    Y = [rp(5, t, b1, b2, e), rp(6, t, b1, b2, e), rp(7, t, b1, b2, e)]
    # (r/(m+1) + r^2 c1) d/dr = (r/(m+1) + r^2 c1)/(2 eps) d/deps
    return mp.matrix([(r/(m + 1) + r*r*c1)/(2*e), r*Y[0], r*Y[1], r*Y[2]])


def Ax(y):
    return jac(Phi, y)*Ahat(y)


pts = [(mp.mpf('0.3'), mp.mpf('0.7'), mp.mpf('-1.1')), (mp.mpf('2.0'), mp.mpf('-1.5'), mp.mpf('0.4')),
       (mp.mpf('-1.2'), mp.mpf('2.5'), mp.mpf('2.5'))]
for (t0, b1, b2) in pts:
    print('point theta=%s a=(%s,%s)' % (t0, b1, b2), flush=True)
    for k in range(2, 7):
        e0 = mp.mpf(10)**(-k)
        y = [e0, t0, b1, b2]
        Jn = jac(Phi, y)
        DA = jac(Ax, y)*mp.inverse(Jn)
        e1, e2 = frame(t0)
        P = e1*e1.T + e2*e2.T
        T = (mp.eye(n) + P/2)/(m + 1)
        err = mp.mnorm(DA - T, 1)
        S = (DA + DA.T)/2
        lmin = min(mp.eigsy(S)[0])
        ratio = mp.norm(Ax(y))/mp.norm(Phi(y))
        print('   eps=1e-%d  |DA-(I+P/2)/(m+1)|/eps=%s  lmin(symDA)=%s  |A|/|x|=%s'
              % (k, mp.nstr(err/e0, 8), mp.nstr(lmin, 10), mp.nstr(ratio, 10)), flush=True)
