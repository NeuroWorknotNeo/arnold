# [Эксперимент] Пример U_II (случай II: гиперболическое разрешение креста), записка singular-sigma, §5:
#   U = x^2 y^2 + 2 x y z^3 + eta z^6 + x^6 + y^6 = H^2 - (1-eta) z^6 + x^6 + y^6,  H = x y + z^3,  0 < eta < 1.
#   (При eta = 0 ось z состоит из критических точек — изолированности нет; член eta z^6 её восстанавливает.)
# 1) изолированность 0 (разбор случаев + sympy);
# 2) поле в квадранте x > 0, y < 0 (rho = z, Y = (xi1, xi2, 1)):
#      z xi = (3 - e) g (1, -1) - e z^3 (y, x)/(x^2 + y^2),  g = x|y|/(x+|y|),  e = eps_h;
#    проверка: z Y(H) = (3 - e) H;  6W - z Y W  (W = U + (1-eta) z^6) — формула записки;
# 3) оценка снизу собственных значений sym(z D_xy xi^(0)) >= -(3-e)(sqrt2-1)/2.
import sympy as sp

x, z, e = sp.symbols('x z e', positive=True)
yy = sp.Symbol('yy', positive=True)            # yy = |y| = -y
y = -yy
H = x*y + z**3
eta = sp.Symbol('eta', positive=True)
U = x**2*y**2 + 2*x*y*z**3 + eta*z**6 + x**6 + y**6
print('U = H^2 - (1-eta) z^6 + x^6 + y^6:', sp.expand(U - (H**2 - (1 - eta)*z**6 + x**6 + y**6)) == 0)
X, Y, Z = sp.symbols('X Y Z', real=True)
Ug = X**2*Y**2 + 2*X*Y*Z**3 + eta*Z**6 + X**6 + Y**6
gr = [sp.factor(sp.diff(Ug, v)) for v in (X, Y, Z)]
print('grad U =', gr)
print('  eta = 0: ось z критическая:', [sp.simplify(g.subs({X: 0, Y: 0, eta: 0})) for g in gr])
# Разбор: dU/dz = 6 z^2 (x y + eta z^3). z = 0 => x(3x^4+y^2) = 0 => x = 0 => y = 0.
print('  при Z=0:', [sp.factor(g.subs(Z, 0)) for g in gr])
# z != 0: x y = -eta z^3; x*dU/dx/2 и y*dU/dy/2 после подстановки x y = -eta z^3:
P = sp.Symbol('P')
ex = sp.expand(X*gr[0]/2); ey = sp.expand(Y*gr[1]/2)
ex = sp.expand(ex.subs(X**2*Y**2, P**2).subs(X*Y, P)).subs(P, -eta*Z**3)
ey = sp.expand(ey.subs(X**2*Y**2, P**2).subs(X*Y, P)).subs(P, -eta*Z**3)
print('  z != 0: x U_x/2 =', sp.factor(ex), ';  y U_y/2 =', sp.factor(ey))
print('  => x^6 = y^6 = eta(1-eta) z^6/3, а из x y = -eta z^3: x^6 = eta^3 |z|^9 => |z|^3 = (1-eta)/(3 eta^2)')

g = x*yy/(x + yy)
zxi1 = (3 - e)*g - e*z**3*y/(x**2 + y**2)
zxi2 = -(3 - e)*g - e*z**3*x/(x**2 + y**2)
# d/dy = -d/dyy
def dy(f): return -sp.diff(f, yy)
zYH = sp.simplify(zxi1*sp.diff(H, x) + zxi2*dy(H) + z*sp.diff(H, z))
print('z Y(H) - (3-e) H =', sp.simplify(zYH - (3 - e)*H))
W = U + (1 - eta)*z**6          # A(rho) = a0 rho^6, a0 = 1 - eta
print('W = H^2 + x^6 + y^6:', sp.expand(W - H**2 - x**6 - y**6) == 0)
zYW = zxi1*sp.diff(W, x) + zxi2*dy(W) + z*sp.diff(W, z)
lam = (3 - e)*yy/(x + yy)                         # z xi1^(0) = lam x
zeta1 = -e*z**3*y/(x**2 + y**2); zeta2 = -e*z**3*x/(x**2 + y**2)
claim = 2*e*H**2 + 6*(1 - lam)*x**6 + 6*(lam - 2 + e)*y**6 - 6*(x**5*zeta1 + y**5*zeta2)
print('6W - zYW - [формула записки] =', sp.simplify(6*W - zYW - claim))
print('z xi1^(0) = lam x:', sp.simplify((3 - e)*g - lam*x) == 0,
      '; z xi2^(0) = (3-e-lam) y:', sp.simplify(-(3 - e)*g - (3 - e - lam)*y) == 0)
# 3) матрица z D_xy xi^(0) по (x, y): строки — компоненты
m11 = sp.diff((3 - e)*g, x); m12 = dy((3 - e)*g)
m21 = sp.diff(-(3 - e)*g, x); m22 = dy(-(3 - e)*g)
S_ = sp.Matrix([[m11, (m12 + m21)/2], [(m12 + m21)/2, m22]])
ev = [sp.simplify(v) for v in S_.eigenvals().keys()]
print('собств. значения sym(z D xi0):', ev)
import mpmath as mp, random
random.seed(5)
worst = mp.inf
for _ in range(20000):
    xv = mp.mpf(10)**random.uniform(-6, 0); yv = mp.mpf(10)**random.uniform(-6, 0)
    for v in ev:
        val = sp.lambdify((x, yy, e), v, 'mpmath')(xv, yv, mp.mpf('0.1'))
        worst = min(worst, val)
print('min собств. значения при e = 0.1 (20000 точек):', mp.nstr(worst, 8),
      '; граница -(3-e)(sqrt2-1)/2 =', mp.nstr(-(3 - mp.mpf('0.1'))*(mp.sqrt(2) - 1)/2, 8))
# функция f(u) = [(u-2+e)u^6 + 1 - (2-e)u]/(1+u) (x^6, y^6-часть, u = x/|y|): знак
u = sp.Symbol('u', positive=True)
f = ((u - 2 + e)*u**6 + 1 - (2 - e)*u)/(1 + u)
print('6(1-lam)x^6 + 6(lam-2+e)y^6 = 6 |y|^6 f(u):', sp.simplify(6*(1 - lam)*x**6 + 6*(lam - 2 + e)*y**6
      - 6*yy**6*f.subs(u, x/yy)) == 0)
for ev_ in ['0.1']:
    ff = sp.lambdify(u, f.subs(e, sp.Rational(1, 10)), 'mpmath')
    print('f(u) при e=1/10: u=1/4:', mp.nstr(ff(0.25), 6), ' u=1:', mp.nstr(ff(1), 6), ' u=4:', mp.nstr(ff(4), 6),
          ' min_{u>=4} f/(u^6+1) ~', mp.nstr(min(ff(4*1.1**k)/((4*1.1**k)**6 + 1) for k in range(80)), 6),
          ' min_{u<=1/4} f/(u^6+1) ~', mp.nstr(min(ff(0.25/1.1**k)/((0.25/1.1**k)**6 + 1) for k in range(80)), 6))
