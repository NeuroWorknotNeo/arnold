# [Эксперимент] Проверка геометрических формул теоремы S (записка singular-sigma, §2, шаг 4)
# для произвольной аналитической карты сферы omega(theta) = F(theta)/|F(theta)|:
#   Pi(r,theta) = r omega(theta),  поле Y = d_r - (kappa/r) xi(theta).d_theta  (в координатах (r,theta)),
#   xi — произвольное C^1-поле с xi(0) = 0 (здесь нелинейное: xi = (2 t1 + t2^2, 3 t2 + t1 t2)).
# Проверяется:
#  (a) Y o Pi = omega - kappa Domega.xi;
#  (b) <omega, Domega v> = 0;
#  (c) r D_Y Y = -kappa [Domega.xi - kappa D^2omega(xi,xi) - kappa Domega(Dxi.xi)];
#  (d) D_w Y = Domega.alpha - kappa [D^2omega(xi,alpha) + Domega(Dxi.alpha)] для w = DPi(a, alpha);
#  (e) для w перп. Y: r<w, D_w Y> = |tau|^2 - kappa <w, D^2omega(xi, r alpha)> - kappa <tau, Domega(Dxi r alpha)>,
#      tau = r Domega.alpha.
# D_Y Y и D_w Y считаются как производные Y o Pi вдоль кривых в координатах (определение), формулы — как в записке.
import sympy as sp
import mpmath as mp
import random

mp.mp.dps = 40
r, s, k = sp.symbols('r s kappa', real=True)
th1, th2, a, al1, al2 = sp.symbols('th1 th2 a al1 al2', real=True)
A1, A2, A3, A4, A5 = [sp.Rational(n, 7) for n in (3, -2, 5, 1, -4)]
F = sp.Matrix([th1 + A1*th2**2 + A2*th1*th2, th2 + A3*th1**2 + A4*th1**3, 1 + A5*th1 + A1*th2**2])
om = F/sp.sqrt((F.T*F)[0])
th = sp.Matrix([th1, th2])
Dom = om.jacobian(th)
XI = sp.Matrix([2*th1 + th2**2, 3*th2 + th1*th2])
DXI = XI.jacobian(th)
def D2om(u, v):
    res = sp.zeros(3, 1)
    for i in range(2):
        for j in range(2):
            res += sp.diff(om, th[i], th[j])*u[i]*v[j]
    return res
Ypi = lambda rr, t1v, t2v: (om.subs({th1: t1v, th2: t2v}, simultaneous=True)
                            - k*(Dom*XI).subs({th1: t1v, th2: t2v}, simultaneous=True))
# (a): DPi.(1, -kappa theta/r) = omega + r Domega (-kappa theta/r)
Pi = r*om
DPi = Pi.jacobian(sp.Matrix([r, th1, th2]))
Ya = DPi*sp.Matrix([1, -k*XI[0]/r, -k*XI[1]/r])
# (c): вдоль интегральной кривой
curve = Ypi(r + s, th1 - s*k*XI[0]/r, th2 - s*k*XI[1]/r)
DYY = sp.diff(curve, s).subs(s, 0)
claim_c = -k*(Dom*XI - k*D2om(XI, XI) - k*Dom*(DXI*XI))/r
# (d)
al = sp.Matrix([al1, al2])
curve_w = Ypi(r + s*a, th1 + s*al1, th2 + s*al2)
DwY = sp.diff(curve_w, s).subs(s, 0)
claim_d = Dom*al - k*(D2om(XI, al) + Dom*(DXI*al))
f_a = sp.lambdify((r, th1, th2, k), Ya - Ypi(r, th1, th2), 'mpmath')
f_b = sp.lambdify((th1, th2, al1, al2), (om.T*Dom*al)[0], 'mpmath')
f_c = sp.lambdify((r, th1, th2, k), DYY - claim_c, 'mpmath')
f_d = sp.lambdify((r, th1, th2, k, a, al1, al2), DwY - claim_d, 'mpmath')
omf = sp.lambdify((th1, th2), om, 'mpmath')
Domf = sp.lambdify((th1, th2), Dom, 'mpmath')
D2f = sp.lambdify((th1, th2, al1, al2), D2om(XI, al), 'mpmath')
DXIf = sp.lambdify((th1, th2), DXI, 'mpmath')
XIf = sp.lambdify((th1, th2), XI, 'mpmath')
DwYf = sp.lambdify((r, th1, th2, k, a, al1, al2), DwY, 'mpmath')
random.seed(3)
mx = [0]*5
for _ in range(20):
    rv = mp.mpf(random.uniform(0.01, 1)); t = [mp.mpf(random.uniform(-0.3, 0.3)) for _ in range(2)]
    kv = mp.mpf(random.uniform(0, 0.5)); av = mp.mpf(random.uniform(-1, 1))
    alv = [mp.mpf(random.uniform(-1, 1)) for _ in range(2)]
    mx[0] = max(mx[0], max(abs(v) for v in f_a(rv, t[0], t[1], kv)))
    mx[1] = max(mx[1], abs(f_b(t[0], t[1], alv[0], alv[1])))
    mx[2] = max(mx[2], max(abs(v) for v in f_c(rv, t[0], t[1], kv)))
    mx[3] = max(mx[3], max(abs(v) for v in f_d(rv, t[0], t[1], kv, av, alv[0], alv[1])))
    # (e): выберем w перп. Y: w = a omega + r Domega alpha с a из условия <w, Y> = 0
    O = mp.matrix(omf(*t)); Dm = mp.matrix(Domf(*t))
    Yv = O - kv*(Dm*mp.matrix(XIf(*t)))
    tau = rv*(Dm*mp.matrix(alv))
    aw = -sum(tau[i]*Yv[i] for i in range(3))/sum(O[i]*Yv[i] for i in range(3))
    w = aw*O + tau
    lhs = rv*sum(w[i]*DwYf(rv, t[0], t[1], kv, aw, alv[0], alv[1])[i] for i in range(3))
    D2 = mp.matrix(D2f(t[0], t[1], rv*alv[0], rv*alv[1]))
    Dx = mp.matrix(DXIf(*t)); v2 = Dm*(Dx*mp.matrix([rv*alv[0], rv*alv[1]]))
    rhs = sum(tau[i]**2 for i in range(3)) - kv*sum(w[i]*D2[i] for i in range(3)) - kv*sum(tau[i]*v2[i] for i in range(3))
    mx[4] = max(mx[4], abs(lhs - rhs))
print('max невязки: (a) %s, (b) %s, (c) %s, (d) %s, (e) %s' % tuple(mp.nstr(v, 3) for v in mx))
