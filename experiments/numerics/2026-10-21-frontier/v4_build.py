"""v4_build.py -- «подкладка» (padding): точная реализация профиля Q (results/009 §6.2) в ПЛОХОЙ ориентации c = (2,3) (b1 шире b2).
U = -x^66 + sum_alpha q_alpha x^{66 - 2 a1 - 3 a2} y^{a1} z^{a2} + y^34 + z^34.
Чистые степени y^34, z^34 имеют L_c = 68, 102 > 66 (хвост), но степень 34 = m (младшая степень граней: x^18 z^16 из b2^16) делает u_34 = x^18 z^16 + y^34 + z^34 >= 0
с изолированным нулём в e_x.  Печатает многочлен, проверяет тождество масштабирования и пишет строку для fcat.  [Эксперимент: точно]"""
import sympy as sp
b1, b2, x, y, z, t = sp.symbols('b1 b2 x y z t')
A = (b1 - b2**2)**2 + b2**8
B = (b1 - b2**2 - b2**3)**2 + b2**8
Q = sp.expand(A * B)
c1, c2, beta = 2, 3, 66
U = -x**beta
for (i, j), co in sp.Poly(Q, b1, b2).terms():
    U += co * x**(beta - c1 * i - c2 * j) * y**i * z**j
Uface = sp.expand(U)
U = sp.expand(U + y**34 + z**34)
chk = sp.expand(Uface.subs({x: t, y: t**c1 * b1, z: t**c2 * b2}, simultaneous=True) - t**beta * (-1 + Q))
print('тождество U_face(t, t^2 b1, t^3 b2) = t^66 (-1+Q):', chk == 0)
P = sp.Poly(U, x, y, z)
degs = {}
for mon, co in P.terms():
    degs.setdefault(sum(mon), []).append((mon, co))
m = min(degs)
print('степень', max(degs), 'мономов', len(P.terms()), 'm =', m)
print('u_m =', sum(co * x**mon[0] * y**mon[1] * z**mon[2] for mon, co in degs[m]))
s = str(U).replace('**', '**')
open('v4_poly.txt', 'w').write(s)
print(s)
