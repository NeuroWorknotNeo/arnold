# [Эксперимент] Символьные проверки для модели особой точки Sigma (записка
# notes/prover/2026-10-21-singular-sigma.md, §3):
#   U = x^2 y^2 + eps z^2 (x^4 + y^4) - z^6 + x^6 + y^6.
# 1) изолированность 0 (разбор случаев; проверка разложением градиента);
# 2) полярная форма в гномонической карте omega(theta) = (t1, t2, 1)/sqrt(1+|t|^2):
#    U(r omega) = r^4 c^4 t1^2 t2^2 + r^6 c^6 (-1 + E),  c = (1+|t|^2)^(-1/2);
# 3) тождество Эйлера для поля Y = d_r - (kappa/r) theta.d_theta:
#    -r d_r W~ + kappa theta.grad W~ = (2 + 4 kappa c^2) r^-2 c^4 t1^2 t2^2 + kappa theta.grad Lambda,
#    W~ = U/r^6 + 1 = r^-2 c^4 t1^2 t2^2 + Lambda,  Lambda = 1 - c^6 + c^6 E;
# 4) ряды Lambda = 3|t|^2 + ..., theta.grad Lambda = 6|t|^2 + ...; оценки (S1), (S2) на сетке;
# 5) Картезианский вариант (rho = z, Y = e_z): 6W - z dW/dz >= 4W при eps >= 0.
import sympy as sp

x, y, z, eps, r, k = sp.symbols('x y z epsilon r kappa', real=True)
t1, t2 = sp.symbols('t1 t2', real=True)
U = x**2*y**2 + eps*z**2*(x**4 + y**4) - z**6 + x**6 + y**6
grad = [sp.factor(sp.diff(U, v)) for v in (x, y, z)]
print('grad U =', grad)
# разбор случаев (вручную в записке); проверка: подставляем ветви
# x != 0, y != 0: y^2 = -2 eps z^2 x^2 - 3 x^4 и x^2 = -2 eps z^2 y^2 - 3 y^4 => сумма:
S = sp.expand((x**2 + y**2)*(1 + 2*eps*z**2) + 3*(x**4 + y**4))
print('сумма уравнений (должна быть x^2+y^2 + 2eps z^2(x^2+y^2) + 3(x^4+y^4)):', S)
# x = 0, y != 0: 2 eps z^2 y^2 + 3 y^4 = 0, eps y^4 - 3 z^4 = 0
y2 = sp.Symbol('Y2')
sol = sp.solve([2*eps*z**2*y2 + 3*y2**2, eps*y2**2 - 3*z**4], [y2, eps], dict=True)
print('x=0, y!=0: решения (Y2 = y^2, eps):', sol)

# 2) полярная форма
c = 1/sp.sqrt(1 + t1**2 + t2**2)
om = [t1*c, t2*c, c]
Upol = sp.simplify(U.subs({x: r*om[0], y: r*om[1], z: r*om[2]}, simultaneous=True))
E = eps*(t1**4 + t2**4) + t1**6 + t2**6
claim = r**4*c**4*t1**2*t2**2 + r**6*c**6*(-1 + E)
print('полярная форма верна:', sp.simplify(Upol - claim) == 0)

# 3) тождество Эйлера
Wt = sp.expand(claim/r**6 + 1)
Lam = 1 - c**6 + c**6*E
lhs = -r*sp.diff(Wt, r) + k*(t1*sp.diff(Wt, t1) + t2*sp.diff(Wt, t2))
rhs = (2 + 4*k*c**2)*r**-2*c**4*t1**2*t2**2 + k*(t1*sp.diff(Lam, t1) + t2*sp.diff(Lam, t2))
print('тождество Эйлера (S2) для модели:', sp.simplify(lhs - rhs) == 0)
print('theta.grad(c^4 t1^2 t2^2) = 4 c^6 t1^2 t2^2:',
      sp.simplify(t1*sp.diff(c**4*t1**2*t2**2, t1) + t2*sp.diff(c**4*t1**2*t2**2, t2) - 4*c**6*t1**2*t2**2) == 0)

# 4) ряды и оценки
tt = sp.Symbol('tt', positive=True)   # масштаб: theta = tt*(cos a, sin a)
a = sp.Symbol('a', real=True)
sub = {t1: tt*sp.cos(a), t2: tt*sp.sin(a)}
Ls = sp.series(sp.simplify(Lam.subs(sub)), tt, 0, 6).removeO()
print('Lambda =', sp.simplify(sp.expand(Ls)))
eL = t1*sp.diff(Lam, t1) + t2*sp.diff(Lam, t2)
eLs = sp.series(sp.simplify(eL.subs(sub)), tt, 0, 6).removeO()
print('theta.grad Lambda =', sp.simplify(sp.expand(eLs)))

# численная проверка оценок (S1): Lambda >= 2|t|^2 и (S2): theta.grad Lambda >= Lambda
# при |t|^2 <= 1/(9+|eps|), eps in {-2,-1,-0.1,0,0.1,1,2}
import mpmath as mp
mp.mp.dps = 30
Lf = sp.lambdify((t1, t2, eps), Lam, 'mpmath')
eLf = sp.lambdify((t1, t2, eps), eL, 'mpmath')
for ev in [-2, -1, -0.1, 0, 0.1, 1, 2]:
    worst1 = mp.inf; worst2 = mp.inf
    T0 = 1/mp.sqrt(9 + abs(ev))
    for i in range(1, 61):
        for j in range(0, 64):
            tv = T0*i/60; av = 2*mp.pi*j/64
            u1, u2 = tv*mp.cos(av), tv*mp.sin(av)
            L = Lf(u1, u2, ev); eLv = eLf(u1, u2, ev)
            worst1 = min(worst1, (L - 2*tv**2)/tv**2)
            worst2 = min(worst2, (eLv - L)/tv**2)
    print('eps=%5s: min (Lambda-2|t|^2)/|t|^2 = %s, min (theta.gradLambda - Lambda)/|t|^2 = %s' % (
        ev, mp.nstr(worst1, 6), mp.nstr(worst2, 6)))

# 5) картезианский вариант: 6W - z dW/dz при rho = z, Y = e_z
W = sp.expand(U + z**6)
print('6W - z W_z =', sp.factor(sp.expand(6*W - z*sp.diff(W, z))))
print('6W - z W_z - 4W =', sp.expand(6*W - z*sp.diff(W, z) - 4*W))
