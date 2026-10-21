"""R37: примеры X1, X2, касп, касание (§4.3 записки singular-sigma) [Эксперимент].

1. Градиенты каспа и касания (для ручного доказательства изолированности в отзыве).
2. Гномонические p_k и тождества таблицы §4.3.
3. Разложения (X0)-(X2) для модели, X1, X2: p_j = -a0 + L1 + L2 + theta1*theta2*n_j.
"""
import sympy as sp

x, y, z, r, t1, t2 = sp.symbols('x y z r theta1 theta2', real=True)
t = t1**2 + t2**2
c = 1/sp.sqrt(1 + t)
sub = {x: r*c*t1, y: r*c*t2, z: r*c}

Ucusp = (y**2*z - x**3)**2 - z**8 + x**8 + y**8
Utan = y**2*(y*z - x**2)**2 - z**8 + x**8 + y**8
UX1 = x**2*y**2 + z*(x**4 + y**4) - z**6 + x**6 + y**6
UX2 = x**2*y**2 + x*y*z**4 - z**7 + x**8 + y**8

for name, U in [('cusp', Ucusp), ('tangency', Utan)]:
    print(name, 'grad =', [sp.factor(sp.diff(U, v)) for v in (x, y, z)])

# ручной довод для каспа: F=y^2 z-x^3; Uz=2y^2F-8z^7, Uy=4yzF+8y^7
F = y**2*z - x**3
print('cusp Uz - (2y^2F-8z^7) =', sp.expand(sp.diff(Ucusp, z) - (2*y**2*F - 8*z**7)))
print('cusp Uy - (4yzF+8y^7) =', sp.expand(sp.diff(Ucusp, y) - (4*y*z*F + 8*y**7)))
print('cusp Ux - (-6x^2F+8x^7) =', sp.expand(sp.diff(Ucusp, x) - (-6*x**2*F + 8*x**7)))
# касание: G=yz-x^2; Uz=2y^3G-8z^7, Uy=2yG(G+yz)+8y^7, Ux=-4xy^2G+8x^7
G = y*z - x**2
print('tan Uz - (2y^3G-8z^7) =', sp.expand(sp.diff(Utan, z) - (2*y**3*G - 8*z**7)))
print('tan Uy - (2yG(G+yz)+8y^7) =', sp.expand(sp.diff(Utan, y) - (2*y*G*(G + y*z) + 8*y**7)))
print('tan Ux - (-4xy^2G+8x^7) =', sp.expand(sp.diff(Utan, x) - (-4*x*y**2*G + 8*x**7)))


def pk(U, k):
    """k-я однородная часть U в гномонической карте, делённая на r^k."""
    P = sp.Poly(sp.expand(U), x, y, z)
    uk = sp.Integer(0) + sum(coef*x**a*y**b*z**cc for (a, b, cc), coef in P.terms() if a + b + cc == k)
    return sp.simplify(sp.expand(uk.subs(sub))/r**k)


def eul(f, w):
    return w[0]*t1*sp.diff(f, t1) + w[1]*t2*sp.diff(f, t2)


# касп
p6 = pk(Ucusp, 6); p8 = pk(Ucusp, 8)
print('cusp p6 - c^6(t2^2-t1^3)^2 =', sp.simplify(p6 - c**6*(t2**2 - t1**3)**2))
print('cusp xi_w.grad p6 / p6 - 6(2-t2^2)/(1+|t|^2) =',
      sp.simplify(eul(p6, (2, 3))/p6 - 6*(2 - t2**2)/(1 + t)))
Lam = p8 + 1
ser = sp.series(sp.expand(eul(Lam, (2, 3)) - Lam).subs({t1: sp.Symbol('s')*sp.Symbol('a'), t2: sp.Symbol('s')*sp.Symbol('b')}), sp.Symbol('s'), 0, 4)
print('cusp xi.grad Lam - Lam ~', sp.simplify(ser.removeO()))
print('cusp Lam ~', sp.series(Lam.subs({t1: sp.Symbol('s')*sp.Symbol('a'), t2: sp.Symbol('s')*sp.Symbol('b')}), sp.Symbol('s'), 0, 4))

# касание
p6 = pk(Utan, 6); p8 = pk(Utan, 8)
print('tan p6 - c^6 t2^2 (t2-t1^2)^2 =', sp.simplify(p6 - c**6*t2**2*(t2 - t1**2)**2))
print('tan xi_w.grad p6 / p6 - 2(t1^2-2t2^2+4)/(1+|t|^2) =',
      sp.simplify(eul(p6, (1, 2))/p6 - 2*(t1**2 - 2*t2**2 + 4)/(1 + t)))
Lam = p8 + 1
ser = sp.series(sp.expand(eul(Lam, (1, 2)) - Lam).subs({t1: sp.Symbol('s')*sp.Symbol('a'), t2: sp.Symbol('s')*sp.Symbol('b')}), sp.Symbol('s'), 0, 4)
print('tan xi.grad Lam - Lam ~', sp.simplify(ser.removeO()))
print('u7 cusp, tan:', pk(Ucusp, 7), pk(Utan, 7))

# X1, X2
q5 = pk(UX1, 5)
print('X1 p4 =', pk(UX1, 4), ' p5 - c^5(t1^4+t2^4) =', sp.simplify(q5 - c**5*(t1**4 + t2**4)))
print('X1 theta.grad q5 / q5 - (4 - 5c^2|t|^2) =', sp.simplify(eul(q5, (1, 1))/q5 - (4 - 5*c**2*t)))
p6 = pk(UX1, 6)
n6 = sp.simplify((p6 - p6.subs(t2, 0) - p6.subs(t1, 0) + p6.subs({t1: 0, t2: 0}))/(t1*t2))
print('X1 n6 =', n6)
print('X2 p6 =', pk(UX2, 6), ' p5 =', pk(UX2, 5), ' p7 =', pk(UX2, 7))
p7 = pk(UX2, 7)
print('X2 Lam1 =', sp.simplify(p7.subs(t2, 0) + 1))
