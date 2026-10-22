"""v3_build.py -- точная реализация профиля Q (results/009 §6.2) с весами c=(5,2): U(x,y1,y2) = x^32 (-1 + Q(y1/x^5, y2/x^2)).
Строит многочлен, печатает (степень, число мономов, младшая форма u_m), проверяет тождество масштабирования и пытается
сертифицировать изолированность 0 (Singular, локальное число Милнора).  [Эксперимент: точно]"""
import sympy as sp, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '2026-10-21-zoo'))
import sing
b1, b2, x, y, z = sp.symbols('b1 b2 x y z')   # y1 = y, y2 = z
A = (b1 - b2**2)**2 + b2**8
B = (b1 - b2**2 - b2**3)**2 + b2**8
Q = sp.expand(A * B)
c1, c2, beta = 5, 2, 32
U = -x**beta
for (i, j), co in sp.Poly(Q, b1, b2).terms():
    U += co * x**(beta - c1 * i - c2 * j) * y**i * z**j
U = sp.expand(U)
print('U =', U)
t = sp.Symbol('t')
chk = sp.expand(U.subs({x: t, y: t**c1 * b1, z: t**c2 * b2}, simultaneous=True) - t**beta * (-1 + Q))
print('тождество масштабирования U(t, t^5 b1, t^2 b2) = t^32 (-1+Q):', chk == 0)
P = sp.Poly(U, x, y, z)
degs = {}
for mon, co in P.terms():
    degs.setdefault(sum(mon), []).append((mon, co))
m = min(degs)
print('степень U:', max(degs), ' число мономов:', len(P.terms()), ' младшая степень m =', m)
print('u_m =', sum(co * x**mon[0] * y**mon[1] * z**mon[2] for mon, co in degs[m]))
if '--milnor' in sys.argv:
    print('число Милнора:', sing.local_milnor(U))
