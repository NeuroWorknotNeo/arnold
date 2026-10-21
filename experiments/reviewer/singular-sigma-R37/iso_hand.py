"""R37: тождества для ручного доказательства изолированности каспа и касания."""
import sympy as sp
x, y, z = sp.symbols('x y z', real=True)
Uc = (y**2*z - x**3)**2 - z**8 + x**8 + y**8
Ut = y**2*(y*z - x**2)**2 - z**8 + x**8 + y**8
d = lambda U, v: sp.diff(U, v)
print('cusp: (y/2)U_y - z U_z =', sp.factor(sp.expand(y/2*d(Uc, y) - z*d(Uc, z))))
print('cusp: U_x(x,0,0) =', sp.factor(d(Uc, x).subs({y: 0, z: 0})))
print('tan:  (y/2)U_y - (z/2)U_z - [y^2 (yz-x^2)^2 + 4y^8 + 4z^8] =',
      sp.expand(y/2*d(Ut, y) - z/2*d(Ut, z) - (y**2*(y*z - x**2)**2 + 4*y**8 + 4*z**8)))
print('tan:  U_x(x,0,0) =', sp.factor(d(Ut, x).subs({y: 0, z: 0})))
