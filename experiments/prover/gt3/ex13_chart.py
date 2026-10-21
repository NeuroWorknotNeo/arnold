"""[Эксперимент] Пример 13 в координатах «развёртки конуса» (раздел 5 заметки
notes/prover/2026-10-21-gt3.md). Символьные выкладки sympy.

U = (x^2+y^2-z^2)^2 + z^5 x + z^4 x y + z^6/2.
Карта Phi(X,Y,eta) = s*N(theta) + eta*nu(theta),  s = sqrt(X^2+Y^2), theta = atan(Y/X),
  phi = phi0 + sqrt2*theta, phi0 = 5pi/6,
  N = (cos phi, sin phi, 1)/sqrt2,  nu = (cos phi, sin phi, -1)/sqrt2,  tau = (-sin phi, cos phi, 0).
Проверяем:
 (1) U(Phi) = 4 s^2 eta^2 + z^6 G_lambda(phi), z = (s-eta)/sqrt2, lambda = (s+eta)/(s-eta)
     (тождество по (s, eta, phi)), откуда U(Phi) = X^6 F(t,e,X), t = Y/X, e = eta/X^2;
 (2) F0 = F(.,.,0): grad F0(0)=0, F0(0)=G(phi0)/8<0, Hess F0(0)=diag((6-3sqrt3)/16, 8);
 (3) формулы для d_X Phi, d^2_X Phi, d_Y d_X Phi, d_eta d_X Phi и матрицы Грама B
     (сравнение символьного дифференцирования с выписанными в заметке формулами);
 (4) первый порядок дна b*(X).
"""
import random
import sympy as sp

X, Y, eta = sp.symbols('X Y eta', positive=True)
s_, h_, ph = sp.symbols('s eta_ phi', real=True)
t, e = sp.symbols('t e', real=True)
phi0 = 5 * sp.pi / 6
r2 = sp.sqrt(2)

# (1) тождество по (s, eta, phi)
R = (s_ + h_) / r2
z = (s_ - h_) / r2
xx, yy = R * sp.cos(ph), R * sp.sin(ph)
U = (xx**2 + yy**2 - z**2)**2 + z**5 * xx + z**4 * xx * yy + z**6 / 2
lam = R / z
Glam = lam * sp.cos(ph) + lam**2 * sp.cos(ph) * sp.sin(ph) + sp.Rational(1, 2)
d1 = sp.simplify(sp.expand(U - (4 * s_**2 * h_**2 + z**6 * Glam)))
print('(1) U(Phi) - [4 s^2 eta^2 + z^6 G_lambda(phi)] =', d1)

# F(t,e,X)
S = sp.sqrt(1 + t**2)
lamF = (S + X * e) / (S - X * e)
phit = phi0 + r2 * sp.atan(t)
GF = lamF * sp.cos(phit) + lamF**2 * sp.cos(phit) * sp.sin(phit) + sp.Rational(1, 2)
F = 4 * (1 + t**2) * e**2 + (S - X * e)**6 / 8 * GF
# подстановка s = X S, eta = X^2 e: проверка в случайных точках с 40 знаками
random.seed(0)
md = 0
for _ in range(10):
    Xv = sp.Rational(random.randint(1, 40), 100)
    tv = sp.Rational(random.randint(-30, 30), 100)
    ev = sp.Rational(random.randint(-30, 30), 100)
    sv = Xv * sp.sqrt(1 + tv**2)
    lhs = (4 * s_**2 * h_**2 + z**6 * Glam).subs({s_: sv, h_: ev * Xv**2, ph: phi0 + r2 * sp.atan(tv)})
    rhs = Xv**6 * F.subs({t: tv, e: ev, X: Xv})
    md = max(md, abs(sp.N(lhs - rhs, 40)))
print('    max |X^6 F - (4s^2eta^2+z^6 G)| at 10 random points:', sp.N(md, 3))

# (2)
F0 = F.subs(X, 0)
g0 = [sp.simplify(sp.diff(F0, w).subs({t: 0, e: 0})) for w in (t, e)]
H = sp.Matrix(2, 2, lambda i, j: sp.nsimplify(sp.simplify(sp.diff(F0, [t, e][i], [t, e][j]).subs({t: 0, e: 0}))))
F00 = sp.nsimplify(sp.simplify(F0.subs({t: 0, e: 0})))
print('(2) F0(0) =', F00, '≈', sp.N(F00), ';  grad F0(0) =', g0)
print('    Hess F0(0) =', list(H), '≈', [sp.N(v) for v in H])
print('    (6-3*sqrt3)/16 =', sp.N((6 - 3 * sp.sqrt(3)) / 16))

# (4) первый порядок дна
gX = sp.Matrix([sp.nsimplify(sp.simplify(sp.diff(sp.diff(F, w), X).subs({t: 0, e: 0, X: 0}))) for w in (t, e)])
b1 = sp.simplify(-H.inv() * gX)
print('(4) d_X grad_b F(0) =', list(gX), ';  b*(X) = X*', list(b1), '+ O(X^2) ≈ X*', [sp.N(v) for v in b1])

# (3) геометрия карты
th = sp.atan(Y / X)
s = sp.sqrt(X**2 + Y**2)
phi = phi0 + r2 * th
N = sp.Matrix([sp.cos(phi), sp.sin(phi), 1]) / r2
nu = sp.Matrix([sp.cos(phi), sp.sin(phi), -1]) / r2
tau = sp.Matrix([-sp.sin(phi), sp.cos(phi), 0])
Phi = s * N + eta * nu
dX = sp.diff(Phi, X)
dXX = sp.diff(Phi, X, 2)
dXY = sp.diff(dX, Y)
dXe = sp.diff(dX, eta)
c, sn = sp.cos(th), sp.sin(th)
f_dX = c * N - (1 + eta / s) * sn * tau
f_dXX = -(eta * sn**2 / s**2) * N - (1 + eta / s) * (sn**2 / s) * nu + (2 * eta * sn * c / s**2) * tau
f_dXY = (eta * sn * c / s**2) * N + (1 + eta / s) * (sn * c / s) * nu + (eta * (sn**2 - c**2) / s**2) * tau
f_dXe = -(sn / s) * tau
J = Phi.jacobian(sp.Matrix([X, Y, eta]))
B = J.T * J
k = 2 * eta / s + eta**2 / s**2
f_B = sp.Matrix([[1 + k * sn**2, -k * sn * c, 0], [-k * sn * c, 1 + k * c**2, 0], [0, 0, 1]])
md = 0
for _ in range(10):
    pt = {X: sp.Rational(random.randint(5, 40), 100), Y: sp.Rational(random.randint(-20, 20), 1000),
          eta: sp.Rational(random.randint(1, 20), 10000)}
    for a, b in [(dX, f_dX), (dXX, f_dXX), (dXY, f_dXY), (dXe, f_dXe), (B, f_B)]:
        md = max(md, max(abs(sp.N(v, 40)) for v in (a - b).subs(pt)))
print('(3) max deviation of the hand formulas (d_X Phi, d2_X Phi, d_Y d_X Phi, d_eta d_X Phi, B):',
      sp.N(md, 3))
