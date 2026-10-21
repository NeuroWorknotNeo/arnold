"""[Эксперимент] R20: контрпример к критерию минимума в предложении K4(c) (в формулировке записки).

U = x^2((y-x^2)^2+(z-x^2)^2),  n=3,  m=4,  u_4 = x^2(y^2+z^2).
Проверяем:
  * (K1): u_4>=0, Sigma = {x=0} cap S^2 (большая окружность) U {(+-1,0,0)} — гладкое компактное;
  * (K2): Морс-Ботт во всех точках Sigma;
  * R_omega == 0 в точечных компонентах (+-1,0,0), так что «старшего коэффициента» нет;
  * F_fl == 0 на кривой-компоненте;
  * U>=0, то есть 0 — (нестрогий) локальный минимум.
Значит, импликация «минимум => старшие коэффициенты R_omega в точечных компонентах положительны»
ложна без предположения R_omega != 0.
"""
import sympy as sp
from reduced import reduced_series

x, y, z = X = sp.symbols('x y z')
U = x**2 * ((y - x**2)**2 + (z - x**2)**2)
Ue = sp.expand(U)
P = sp.Poly(Ue, *X)
u4 = sum(c * sp.prod([v**k for v, k in zip(X, mon)]) for mon, c in P.terms() if sum(mon) == 4)
print('u_4 =', sp.factor(u4))
assert sp.expand(u4 - x**2 * (y**2 + z**2)) == 0

# Морс-Ботт в точке (1,0,0): гессиан на omega^perp
Hs = sp.hessian(u4, X).subs({x: 1, y: 0, z: 0})
print('D^2u_4(1,0,0) на (y,z):', Hs[1:, 1:])
# Морс-Ботт на окружности x=0: omega=(0,cos a, sin a), нормаль e_x
a = sp.Symbol('a')
hn = sp.diff(u4, x, 2).subs({x: 0, y: sp.cos(a), z: sp.sin(a)})
print('d^2u_4/dx^2 на окружности:', sp.simplify(hn))
# grad u_4 = 0 на Sigma
g = [sp.diff(u4, v) for v in X]
print('grad u_4 в (1,0,0):', [gi.subs({x: 1, y: 0, z: 0}) for gi in g],
      ' на окружности:', [sp.simplify(gi.subs({x: 0, y: sp.cos(a), z: sp.sin(a)})) for gi in g])

# R_omega в точечных компонентах
for sgn in (1, -1):
    R, ys, s, H0 = reduced_series(U, X, [sgn, 0, 0], [[0, 1, 0], [0, 0, 1]], 4, 6)
    print('omega=(%d,0,0): R(s) до s^6 =' % sgn, R, ' y* =', ys)
# функция дна на окружности: omega=(0,3/5,4/5), нормаль e_x
R, ys, s, H0 = reduced_series(U, X, [0, sp.Rational(3, 5), sp.Rational(4, 5)], [[1, 0, 0]], 4, 6)
print('кривая-компонента, omega=(0,3/5,4/5): R(s) до s^6 =', R, ' y* =', ys)
print('U = x^2*(сумма квадратов) >= 0: 0 — нестрогий локальный минимум U.')
