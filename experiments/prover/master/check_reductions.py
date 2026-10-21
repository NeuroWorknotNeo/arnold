"""
[Эксперимент] Проверка, что поля известных теорем -- частные случаи конструкции мастер-теоремы:
поле Y определяется весами a = c - 1, образующей P(s,u) карты th = P(s, s^A b) и полем xi
(Y.grad s = 1, Y.grad b = -xi/s), и тогда Y o Pi = Om + DOm v, v = s P_s + P_u (A u - s^A xi) (лемма W, (W0)).

1. Трубчатая калибровка Om(theta,t) = omega(theta) + t n(theta) (репер Дарбу, k_g -- произвольная функция),
   P(s,u) = (u1, Y*(s,u1) + u2), a = (0, c-1), xi = (kappa*theta, c2*e), c2 = c - lambda:
   Y o Pi  ==  Psi_s - (kappa theta/s) Psi_theta + lambda (zeta/s) Psi_zeta,
   Psi(s,theta,zeta) = s omega + (s Y* + zeta) n   (поле теорем Mb [010], K2 [008], N [011]; при lambda != 0 --
   поле теоремы W записки P16).
2. Та же калибровка, P(s,u) = (th0 + tau(s) + u1, Y*(s, th0 + tau(s) + u1) + u2), a = (alpha, c'-1), xi = (I+A) b:
   Y o Pi == d/dx Phi(x,u,zeta) при постоянных (u,zeta), Phi = Psi(x, th0 + tau(x) + u/x, zeta)  (теорема Md [010]).
3. Гномоническая калибровка Om(th) = (1, th) в R^3, P(s,u) = gamma(s)/s + L(s) u, a = c - 1, xi произвольно:
   th + v == Ztilde := gamma' + L' x^c b + L x^{c-1}(C b - xi)  (поле (0.1) теоремы 2U [012]).
"""
import sympy as sp

s, kap, lam, c, al, cp, th0 = sp.symbols('s kappa lambda c alpha cprime theta0', positive=True)
th, e, b1 = sp.symbols('theta e b1', real=True)
kg = sp.Function('kg')
Ys = sp.Function('Ystar')

# --- векторы в репере (omega, l, n) вдоль кривой; производная по theta
def dth(vec, var):
    cw, cl, cn = vec
    return sp.Matrix([sp.diff(cw, var) - cl,
                      sp.diff(cl, var) + cw - kg(var) * cn,
                      sp.diff(cn, var) + kg(var) * cl])

# ===== 1.
tt = sp.symbols('t', real=True)
Om = sp.Matrix([1, 0, tt])                 # omega + t n
Om_th = dth(Om, th); Om_t = sp.diff(Om, tt)
u1 = th; u2 = s**(c - 1) * e
P2 = Ys(s, u1) + u2
# v по (W0): v = s P_s + P_u ubar
ubar = sp.Matrix([-kap * th, (c - 1) * u2 - s**(c - 1) * (c - lam) * e])
Pu = sp.Matrix([[1, 0], [sp.diff(Ys(s, th), th), 1]])
sPs = sp.Matrix([0, s * sp.diff(Ys(s, th), s)])
v = sPs + Pu * ubar
y = (Om + Om_th * v[0] + Om_t * v[1]).subs(tt, P2)
# цель
zeta = s**c * e
Psi = sp.Matrix([s, 0, s * Ys(s, th) + zeta])
zsym = sp.symbols('zeta')
Psi_z = Psi.subs(zeta, zsym)  # zeta как независимая переменная
Psi_z = sp.Matrix([s, 0, s * Ys(s, th) + zsym])
Psi_s = sp.diff(Psi_z, s)
Psi_th = dth(Psi_z, th)
Psi_zeta = sp.diff(Psi_z, zsym)
target = (Psi_s - kap * th / s * Psi_th + lam * zsym / s * Psi_zeta).subs(zsym, zeta)
print('1 (трубка, xi=(kappa theta, c2 e)):', sp.simplify(sp.expand(y - target)).T)

# ===== 2.
tau = sp.Function('tau')
x = s
u = sp.symbols('u', real=True); zz = sp.symbols('zz', real=True)
thhat = th0 + tau(x) + u / x
# Phi(x,u,zeta) в репере: s omega(thhat) + (x Y*(x,thhat) + zeta) n(thhat); производная по x при пост. (u,zeta):
#  d/dx (vec(thhat)) = d_x vec + dth(vec) * d thhat/dx
def Phi_vec(xx, thv, zv):
    return sp.Matrix([xx, 0, xx * Ys(xx, thv) + zv])
T = sp.symbols('T', real=True)
base = Phi_vec(x, T, zz)
dPhi_dx = sp.diff(base, s) + dth(base, T) * sp.diff(thhat, x)
dPhi_dx = dPhi_dx.subs(T, thhat)
# мастер-конструкция: b1 = u x^{-(1+alpha)}, e = zeta x^{-c'}, u-координаты u1 = x^alpha b1, u2 = x^{c'-1} e
U1 = x**al * b1; U2 = x**(cp - 1) * e
Pm = sp.Matrix([th0 + tau(s) + U1, Ys(s, th0 + tau(s) + U1) + U2])
# P как функция (s,u1,u2)
w1, w2 = sp.symbols('w1 w2', real=True)
Pf = sp.Matrix([th0 + tau(s) + w1, Ys(s, th0 + tau(s) + w1) + w2])
Pu2 = Pf.jacobian([w1, w2]).subs({w1: U1, w2: U2})
sPs2 = (s * sp.diff(Pf, s)).subs({w1: U1, w2: U2})
A = sp.diag(al, cp - 1)
xi = (sp.eye(2) + A) * sp.Matrix([b1, e])
ubar2 = A * sp.Matrix([U1, U2]) - sp.diag(s**al, s**(cp - 1)) * xi
v2 = sPs2 + Pu2 * ubar2
thv, tv = Pm[0], Pm[1]
Om2 = sp.Matrix([1, 0, tt])
Om2_th = dth(Om2, T)
y2 = (Om2 + Om2_th * v2[0] + sp.Matrix([0, 0, 1]) * v2[1]).subs({tt: tv}).subs(T, thv)
subsd = {u: x**(1 + al) * b1, zz: x**cp * e}
res2 = sp.simplify(sp.expand((y2 - dPhi_dx.subs(subsd)).doit()))
# остаток вида Subs(d/dxi Y*(xi, .), xi, s) - Subs(d/ds Y*(s,T), T, .) -- одна и та же величина
# в двух записях sympy; для однозначности подставим конкретный многочлен общего вида:
Ycoef = sp.symbols('y0:12')
Ypoly = lambda S_, T_: sum(Ycoef[3*i + j] * S_**(i + 1) * T_**j for i in range(4) for j in range(3))
res2b = sp.simplify(sp.expand((y2 - dPhi_dx.subs(subsd)).replace(Ys, Ypoly).doit()))
print('2 (трубка, теорема Md, xi=(I+A)b), Y* -- функция:', res2.T)
print('2 (тот же остаток при Y* = общий многочлен степени (4,2) с символьными коэффициентами):', res2b.T)

# ===== 3.
g1, g2 = sp.Function('g1')(s), sp.Function('g2')(s)
L = sp.Matrix(2, 2, lambda i, j: sp.Function('L%d%d' % (i + 1, j + 1))(s))
c1, c2_ = sp.symbols('c1 c2', positive=True)
C = sp.diag(c1, c2_)
A3 = C - sp.eye(2)
bb = sp.Matrix(sp.symbols('bb1 bb2', real=True))
XI = sp.Matrix([sp.Function('xi1')(s, bb[0], bb[1]), sp.Function('xi2')(s, bb[0], bb[1])])
gam = sp.Matrix([g1, g2])
SA3 = sp.diag(s**(c1 - 1), s**(c2_ - 1))
uu = SA3 * bb
Theta = gam / s + L * uu
# v = s Ps + Pu ubar, P(s,u) = gam/s + L u
sPs3 = s * (sp.diff(gam / s, s) + sp.diff(L, s) * uu)
v3 = sPs3 + L * (A3 * uu - SA3 * XI)
Ztil = sp.diff(gam, s) + sp.diff(L, s) * sp.diag(s**c1, s**c2_) * bb + L * SA3 * (C * bb - XI)
print('3 (гномоническая, теорема 2U):', sp.simplify(sp.expand(Theta + v3 - Ztil)).T)
