"""R42: проверка формул (1.1), (1.2) теоремы S для нелинейной карты omega и нелинейного xi (n=3).
[Эксперимент] sympy: Y задаётся в координатах (r, theta); D_Y Y и D_w Y вычисляются через
матрицу Якоби D Pi, независимо от вывода в тексте.
"""
import sympy as sp
import random

r, t1, t2, kap = sp.symbols('r t1 t2 kappa', real=True)
th = sp.Matrix([t1, t2])
v = sp.Matrix([t1 + t2**2/3, t2 + t1*t2/2, 1 + t1**2/5])
om = v/sp.sqrt(v.dot(v))
xi = sp.Matrix([t1 + t1*t2, 2*t2 - t1**2])
Pi = r*om
J = Pi.jacobian([r, t1, t2])          # D Pi
Domega = om.jacobian([t1, t2])
y_th = om - kap*Domega*xi             # (1.1)
# поле в координатах: Ycoord = (1, -kappa xi / r); образ в R^3:
Ycart = J*sp.Matrix([1, -kap*xi[0]/r, -kap*xi[1]/r])
print('(1.1):', [sp.simplify(e_) for e_ in (Ycart - y_th)] == [0, 0, 0])

# Производная поля Z(q) = y(theta(q)) по направлению w = J * c: D_w Z = d/ds y(theta + s c_theta) = Dy * c_theta
Dy = y_th.jacobian([t1, t2])
# D_Y Y: c = (1, -kappa xi/r)
DYY = Dy*sp.Matrix([-kap*xi[0]/r, -kap*xi[1]/r])
D2om = lambda a, b: sp.Matrix([sum(sp.diff(om[i], th[k], th[l])*a[k]*b[l] for k in range(2) for l in range(2)) for i in range(3)])
Dxi = xi.jacobian([t1, t2])
form_rDYY = -kap*(Domega*xi - kap*D2om(xi, xi) - kap*Domega*(Dxi*xi))
# произвольный w: w = a*omega + Domega*(r*alpha)
a, al1, al2 = sp.symbols('a al1 al2', real=True)
alpha = sp.Matrix([al1, al2])
w = a*om + Domega*(r*alpha)
tau = Domega*(r*alpha)
DwY = Dy*alpha
form_rwDwY = tau.dot(tau) - kap*w.dot(D2om(xi, r*alpha)) - kap*tau.dot(Domega*(Dxi*(r*alpha)))
random.seed(3)
mx1 = mx2 = 0
for _ in range(15):
    vals = {r: random.uniform(0.01, 1), t1: random.uniform(-.5, .5), t2: random.uniform(-.5, .5),
            kap: random.uniform(0, .5), a: random.uniform(-1, 1), al1: random.uniform(-1, 1), al2: random.uniform(-1, 1)}
    d1 = (r*DYY - form_rDYY).subs(vals).evalf(40)
    d2 = (r*w.dot(DwY) - form_rwDwY).subs(vals).evalf(40)
    mx1 = max(mx1, max(abs(q_) for q_ in d1)); mx2 = max(mx2, abs(d2))
print('(1.2) rD_YY residual max:', mx1, '; r<w,D_wY> residual max:', mx2)
# <omega, Domega v> = 0
print('<omega, Domega> = 0:', [sp.simplify(om.dot(Domega[:, k])) for k in range(2)])
