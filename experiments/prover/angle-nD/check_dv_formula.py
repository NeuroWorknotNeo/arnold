# [Эксперимент] Проверка формулы предложения 4 (поле v = |x| exp_{x^}(tau)) для n = 3
# в сферических координатах и сведения к матрице Паламодова при n = 2.
import sympy as sp

r, th, ph = sp.symbols('r theta phi', positive=True)
A = sp.Function('A')(r, th, ph)   # tau = A e_theta + B e_phi
B = sp.Function('B')(r, th, ph)

er  = sp.Matrix([sp.sin(th)*sp.cos(ph), sp.sin(th)*sp.sin(ph), sp.cos(th)])
eth = sp.Matrix([sp.cos(th)*sp.cos(ph), sp.cos(th)*sp.sin(ph), -sp.sin(th)])
eph = sp.Matrix([-sp.sin(ph), sp.cos(ph), 0])

tau = A*eth + B*eph
t = sp.sqrt(A**2 + B**2)
sinc = sp.sin(t)/t
w = sp.cos(t)*er + sinc*tau
v = r*w

# Dv xi = d_r v * xi_r + (1/r) d_th v * xi_th + (1/(r sin th)) d_ph v * xi_ph
cols = [sp.diff(v, r), sp.diff(v, th)/r, sp.diff(v, ph)/(r*sp.sin(th))]
frame = [er, eth, eph]
Dv = sp.zeros(3,3)
for i in range(3):
    for j in range(3):
        Dv[i,j] = (frame[i].T*cols[j])[0]

# Формула из предложения 4: Q(xi) = <xi, Dv xi>
xr, x1, x2 = sp.symbols('xi_r xi_1 xi_2', real=True)
xi = sp.Matrix([xr, x1, x2])
Q_direct = (xi.T*Dv*xi)[0]

# ковариантная производная sigma = A e_th + B e_ph на единичной S^2 (орт. репер)
N = sp.Matrix([[sp.diff(A,th), sp.diff(A,ph)/sp.sin(th) - sp.cos(th)/sp.sin(th)*B],
               [sp.diff(B,th), sp.diff(B,ph)/sp.sin(th) + sp.cos(th)/sp.sin(th)*A]])
tauv = sp.Matrix([A, B])          # в репере (e_th, e_ph)
taur = r*sp.Matrix([sp.diff(A,r), sp.diff(B,r)])  # tau_rho = r d_r tau
xt = sp.Matrix([x1, x2])
that = tauv/t
sincp = sp.diff(sp.sin(sp.Symbol('s'))/sp.Symbol('s'), sp.Symbol('s')).subs(sp.Symbol('s'), t)
dot = lambda a,b: (a.T*b)[0]
Nxt = N*xt
Q_formula = (xr**2*(sp.cos(t) - sp.sin(t)*dot(that, taur))
             + xr*sinc*dot(xt, taur)
             + xr*sincp*dot(that, taur)*dot(xt, tauv)
             + sp.cos(t)*dot(xt, xt)
             - xr*sp.sin(t)*dot(that, Nxt)
             + sinc*dot(xt, Nxt)
             + sincp*dot(that, Nxt)*dot(xt, tauv))

# численная проверка в случайных точках с конкретными функциями A, B
import random
random.seed(1)
Af = sp.Rational(3,10)*sp.sin(r)*sp.cos(2*th)*sp.exp(sp.sin(ph)) + sp.Rational(1,10)*r**2*th
Bf = sp.Rational(1,5)*sp.cos(3*ph)*th*r + sp.Rational(1,20)*sp.sin(th*ph) + sp.Rational(1,100)
diffexpr = (Q_direct - Q_formula).subs({A: Af, B: Bf}).doit()
maxerr = 0
for k in range(20):
    vals = {r: sp.Rational(random.randint(10,99),100), th: sp.Rational(random.randint(30,280),100), ph: sp.Rational(random.randint(0,600),100),
            xr: sp.Rational(random.randint(-99,99),100), x1: sp.Rational(random.randint(-99,99),100), x2: sp.Rational(random.randint(-99,99),100)}
    e = abs(sp.N(diffexpr.subs(vals), 30))
    maxerr = max(maxerr, e)
print("n=3: max |Q_direct - Q_formula| over 20 random points:", maxerr)

# n = 2: v = r(cos(a+D), sin(a+D)); матрица в репере (e_r, e_a) против [P77, с. 52]
a = sp.symbols('alpha', real=True)
D = sp.Function('Delta')(r, a)
v2 = r*sp.Matrix([sp.cos(a+D), sp.sin(a+D)])
e_r = sp.Matrix([sp.cos(a), sp.sin(a)]); e_a = sp.Matrix([-sp.sin(a), sp.cos(a)])
c2 = [sp.diff(v2, r), sp.diff(v2, a)/r]
M2 = sp.Matrix(2,2, lambda i,j: sp.simplify(([e_r,e_a][i].T*c2[j])[0]))
P77 = sp.Matrix([[sp.cos(D) - r*sp.diff(D,r)*sp.sin(D), -(1+sp.diff(D,a))*sp.sin(D)],
                 [sp.sin(D) + r*sp.diff(D,r)*sp.cos(D), (1+sp.diff(D,a))*sp.cos(D)]])
print("n=2: Dv - (матрица обзора/P77) =", sp.simplify(M2 - P77))
