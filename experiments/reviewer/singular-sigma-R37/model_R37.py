"""R37: независимая проверка модели U_eps (§3 записки singular-sigma) [Эксперимент].

1. Градиент и разбор случаев (a).
2. Полярная форма (3.1) в гномонической карте.
3. Тождество (S2) для модели и цепочка оценок п. 1, 3 доказательства теоремы 3.2.
4. Оценка (c) на случайных точках.
5. Картезианское тождество 6W - zW_z - 4W.
"""
import random
import sympy as sp

x, y, z, eps, r, t1, t2, kap = sp.symbols('x y z epsilon r theta1 theta2 kappa', real=True)
U = x**2*y**2 + eps*z**2*(x**4 + y**4) - z**6 + x**6 + y**6
g = [sp.diff(U, v) for v in (x, y, z)]
print('grad:', [sp.factor(gi) for gi in g])

# (a): случай x!=0, y!=0: сумма уравнений
A = sp.expand(g[0]/(2*x)); B = sp.expand(g[1]/(2*y))
print('(a) A+B - [(x^2+y^2)(1+2 eps z^2)+3(x^4+y^4)] =',
      sp.simplify(A + B - ((x**2 + y**2)*(1 + 2*eps*z**2) + 3*(x**4 + y**4))))

# 2. полярная форма
t = t1**2 + t2**2
c = 1/sp.sqrt(1 + t)
sub = {x: r*c*t1, y: r*c*t2, z: r*c}
E = eps*(t1**4 + t2**4) + t1**6 + t2**6
Wcal = sp.simplify(U.subs(sub)/r**6 + 1)
S = c**4*t1**2*t2**2/r**2
Lam = 1 - c**6 + c**6*E
print('(3.1) residual:', sp.simplify(Wcal - S - Lam))

# 3. (S2)
lhs = -r*sp.diff(Wcal, r) + kap*(t1*sp.diff(Wcal, t1) + t2*sp.diff(Wcal, t2)) - kap*Wcal
claimed = (2 + 4*kap*c**2 - kap)*S + kap*(t1*sp.diff(Lam, t1) + t2*sp.diff(Lam, t2) - Lam)
print('(S2) identity residual:', sp.simplify(lhs - claimed))
tt = sp.symbols('t', nonnegative=True)
th_grad_Lam_minus_Lam = sp.simplify(t1*sp.diff(Lam, t1) + t2*sp.diff(Lam, t2) - Lam)
c6 = c**6
claimed2 = 6*t*(1 + t)**-4 - (1 - c6) + c6*((3 - 6*t*c**2)*E + 2*(t1**6 + t2**6))
print('theta.grad Lam - Lam formula residual:', sp.simplify(th_grad_Lam_minus_Lam - claimed2))

# численная проверка нижних оценок на сетке, включая большие |eps|
import math
worst1 = 1e9; worst2 = 1e9
for e in [-200, -50, -10, -2, -1, -0.1, 0, 0.1, 1, 2, 10, 50, 200]:
    t0 = 1/(9 + abs(e))
    th0 = min(0.5, math.sqrt(t0))
    for i in range(1, 60):
        rho = th0*i/60
        for k in range(0, 73):
            a = 2*math.pi*k/72
            a1, a2 = rho*math.cos(a), rho*math.sin(a)
            T = a1*a1 + a2*a2
            cc6 = (1 + T)**-3
            EE = e*(a1**4 + a2**4) + a1**6 + a2**6
            L = 1 - cc6 + cc6*EE
            G = 6*T*(1 + T)**-4 - (1 - cc6) + cc6*((3 - 6*T/(1 + T))*EE + 2*(a1**6 + a2**6))
            worst1 = min(worst1, (L - 2*T)/T)
            worst2 = min(worst2, G/T)
print('min (Lam-2t)/t =', worst1, '  min (theta.grad Lam - Lam)/t =', worst2)

# 4. (c): U + r^6 >= x^2y^2 + r^4(x^2+y^2) при |eps|<=1
random.seed(1)
bad = 0
fU = sp.lambdify((x, y, z, eps), U)
for _ in range(200000):
    X, Yv, Z = [random.uniform(-1, 1) for _ in range(3)]
    e = random.uniform(-1, 1)
    R2 = X*X + Yv*Yv + Z*Z
    val = fU(X, Yv, Z, e) + R2**3 - (X*X*Yv*Yv + R2**2*(X*X + Yv*Yv))
    if val < -1e-12:
        bad += 1
print('(c) violations:', bad)

# 5. картезианское тождество
W = U + z**6
print('6W - zW_z - 4W =', sp.factor(sp.expand(6*W - z*sp.diff(W, z) - 4*W)))
