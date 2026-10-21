# [Эксперимент: символьная проверка] Тождества для изолированности каспа и касания (по замечанию 1 отзыва R37):
#   касп:    U = (y^2 z - x^3)^2 - z^8 + x^8 + y^8,   (y/2) U_y - z U_z     = 4 (y^8 + 2 z^8);
#   касание: U = y^2 (y z - x^2)^2 - z^8 + x^8 + y^8, (y/2) U_y - (z/2) U_z = y^2 (y z - x^2)^2 + 4 y^8 + 4 z^8.
# Отсюда в любой вещественной критической точке y = z = 0, и U_x(x,0,0) = 2x^5(3 + 4x^2) (касп), 8x^7 (касание).
import sympy as sp
x, y, z = sp.symbols('x y z', real=True)
Uc = (y**2*z - x**3)**2 - z**8 + x**8 + y**8
Ut = y**2*(y*z - x**2)**2 - z**8 + x**8 + y**8
print('касп:', sp.expand(y/2*sp.diff(Uc, y) - z*sp.diff(Uc, z) - 4*(y**8 + 2*z**8)) == 0,
      '; U_x(x,0,0) =', sp.factor(sp.diff(Uc, x).subs({y: 0, z: 0})))
print('касание:', sp.expand(y/2*sp.diff(Ut, y) - z/2*sp.diff(Ut, z) - (y**2*(y*z - x**2)**2 + 4*y**8 + 4*z**8)) == 0,
      '; U_x(x,0,0) =', sp.factor(sp.diff(Ut, x).subs({y: 0, z: 0})))
