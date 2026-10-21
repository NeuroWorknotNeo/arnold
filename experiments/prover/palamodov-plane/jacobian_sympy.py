"""[Эксперимент, символьная сверка] Якобиан повёрнутого радиального поля v = R_Delta x
в репере (e_r, e_alpha) и формула наименьшего собственного числа sym Dv.

v(r, alpha) = r (cos(alpha + D), sin(alpha + D)),  D = D(alpha, r).
Проверяем:
 1) матрица Dv в репере (e_r, e_alpha);
 2) mu = cos D - 1/2 r D_r sin D + 1/2 D_a cos D - 1/2 sqrt((r D_r)^2 + D_a^2);
 3) нижняя оценка mu >= cos D - |r D_r| + min(D_a, 0) - 1/2 max(D_a,0) (1 - cos D)
    (численно на случайной выборке).
 4) <v, grad U> = -|x| |grad U| cos(phi - D), если grad U = |grad U| e^{i(alpha+pi+phi)}.
"""
import sympy as sp
import random
import math

r, a = sp.symbols('r alpha', positive=True)
D = sp.Function('D')(a, r)
v = sp.Matrix([r*sp.cos(a + D), r*sp.sin(a + D)])
x1, x2 = r*sp.cos(a), r*sp.sin(a)
# Jacobian d(v)/d(x) = d(v)/d(r,alpha) * (d(x)/d(r,alpha))^{-1}
J_polar = v.jacobian([r, a])
X = sp.Matrix([x1, x2])
J_x = sp.simplify(J_polar * X.jacobian([r, a]).inv())
# frame (e_r, e_alpha): Q = [e_r e_alpha]
Q = sp.Matrix([[sp.cos(a), -sp.sin(a)], [sp.sin(a), sp.cos(a)]])
M = sp.simplify(Q.T * J_x * Q)
Dr, Da = sp.symbols('D_r D_a')
M = sp.simplify(M.subs({sp.Derivative(D, r): Dr, sp.Derivative(D, a): Da}))
d = sp.Symbol('Delta')
M = sp.simplify(M.subs(D, d))
expected = sp.Matrix([[sp.cos(d) - r*Dr*sp.sin(d), -(1 + Da)*sp.sin(d)],
                      [sp.sin(d) + r*Dr*sp.cos(d), (1 + Da)*sp.cos(d)]])
diff = (M - expected)
diff = diff.applyfunc(lambda e: sp.simplify(sp.expand_trig(sp.expand(e))))
print("M - expected (after expand_trig):", diff)
random.seed(0)
mx = 0.0
for _ in range(200):
    sub = {d: random.uniform(-1, 1), r: random.uniform(0.1, 2), a: random.uniform(-3, 3),
           Dr: random.uniform(-3, 3), Da: random.uniform(-3, 3)}
    mx = max(mx, max(abs(float(e.subs(sub))) for e in (M - expected)))
print("max |M - expected| at 200 random points:", mx)
S = (M + M.T)/2
tr = sp.simplify(S.trace())
disc = sp.simplify((S[0, 0] - S[1, 1])**2 + 4*S[0, 1]**2)
print("trace(sym)/2 =", sp.simplify(tr/2))
print("(s11-s22)^2+4 s12^2 =", sp.simplify(sp.trigsimp(disc)))
mu = tr/2 - sp.sqrt(disc)/2
mu_formula = sp.cos(d) - r*Dr*sp.sin(d)/2 + Da*sp.cos(d)/2 - sp.sqrt((r*Dr)**2 + Da**2)/2
Se = (expected + expected.T)/2
tr_e = sp.simplify(Se.trace()/2)
disc_e = sp.simplify(sp.trigsimp(sp.expand((Se[0, 0] - Se[1, 1])**2 + 4*Se[0, 1]**2)))
print("for expected matrix: tr/2 =", tr_e, "; (s11-s22)^2+4s12^2 =", disc_e)
print("mu formula identical:", sp.simplify(tr_e - (sp.cos(d) - r*Dr*sp.sin(d)/2 + Da*sp.cos(d)/2)) == 0
      and sp.simplify(disc_e - ((r*Dr)**2 + Da**2)) == 0)
# numeric check of lower bound
random.seed(1)
f = sp.lambdify((d, r, Dr, Da), mu_formula)
worst = 1e9
for _ in range(200000):
    dd = random.uniform(-1.5, 1.5)
    rdr = random.uniform(-3, 3); da = random.uniform(-3, 5)
    lb = math.cos(dd) - abs(rdr) + min(da, 0) - 0.5*max(da, 0)*(1 - math.cos(dd))
    # f takes (Delta, r, D_r, D_a); with r = 1, r*D_r = rdr
    worst = min(worst, f(dd, 1.0, rdr, da) - lb)
print("min(mu - lower bound) over 2e5 random samples:", worst)
# (2): angle formula
phi = sp.Symbol('phi')
g = sp.Matrix([sp.cos(a + sp.pi + phi), sp.sin(a + sp.pi + phi)])
vv = sp.Matrix([sp.cos(a + d), sp.sin(a + d)])
print("<v/|v|, g/|g|> =", sp.simplify(sp.trigsimp((vv.T*g)[0])))
