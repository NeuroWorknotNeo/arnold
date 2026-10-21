"""R42: пример S1 (замечание 4 results/013). Интервальная арифметика mpmath.iv.
S1 = (x^2-y^2)^2 + x^5 + 2y^5 + z(x^4+y^4) + z^6; дуга x=y: omega=(sin f/sqrt2, sin f/sqrt2, cos f).
"""
import sympy as sp
from mpmath import iv, mp
iv.dps = 30
f = sp.symbols('f', real=True)
x, y, z = sp.symbols('x y z', real=True)
u4 = (x**2-y**2)**2
u5 = x**5 + 2*y**5 + z*(x**4+y**4)
om = {x: sp.sin(f)/sp.sqrt(2), y: sp.sin(f)/sp.sqrt(2), z: sp.cos(f)}
G = sp.simplify(u5.subs(om))
Gref = sp.Rational(1, 8)*sp.sin(f)**4*(3*sp.sqrt(2)*sp.sin(f) + 4*sp.cos(f))
print('G matches text:', sp.simplify(G - Gref) == 0)
# нормальный гессиан: n = (1,-1,0)/sqrt2
n = sp.Matrix([1, -1, 0])/sp.sqrt(2)
Hs = sp.hessian(u4, (x, y, z))
hn = sp.simplify((n.T*Hs*n)[0].subs(om))
print('h_n =', hn)
G1 = sp.diff(Gref, f); G2 = sp.diff(Gref, f, 2)
mods = {'sin': iv.sin, 'cos': iv.cos, 'sqrt': iv.sqrt, 'mpf': iv.mpf}
fG = sp.lambdify(f, Gref, modules=[mods])
fG1 = sp.lambdify(f, G1, modules=[mods])
fK = sp.lambdify(f, G2 + 5*Gref, modules=[mods])
fh = sp.lambdify(f, hn, modules=[mods])
a, b = iv.mpf('4.5464'), iv.mpf('4.5466')
print("G'(4.5464) =", fG1(a), "; G'(4.5466) =", fG1(b))
I = iv.mpf(['4.5464', '4.5466'])
print('G on I:', fG(I))
print("G''+5G on I:", fK(I))
print('h_n on I:', fh(I))
# Подробнее: разбиение I на 100 частей для более тесной оценки
lo, hi = [], []
N = 100
for k in range(N):
    J = iv.mpf([4.5464 + 0.0002*k/N, 4.5464 + 0.0002*(k+1)/N])
    v = fK(J); lo.append(v.a); hi.append(v.b)
print("G''+5G over subdivision: [", min(lo), ",", max(hi), "]")
# минимум G на окружности x=y (глобально) — грубо
import numpy as np
fGn = sp.lambdify(f, Gref, 'numpy')
ff = np.linspace(0, 2*np.pi, 200001)
k = np.argmin(fGn(ff)); print('argmin G on circle x=y ~', ff[k], 'G =', fGn(ff[k]))
# на окружности x=-y
om2 = {x: sp.sin(f)/sp.sqrt(2), y: -sp.sin(f)/sp.sqrt(2), z: sp.cos(f)}
G_m = sp.lambdify(f, sp.simplify(u5.subs(om2)), 'numpy')
k2 = np.argmin(G_m(ff)); print('argmin u5 on circle x=-y ~', ff[k2], 'value =', G_m(ff[k2]))
