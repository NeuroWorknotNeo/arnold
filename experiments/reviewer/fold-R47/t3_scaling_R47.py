"""R47: член ~ s^{1-c} в s<w,D_wY> при X^theta, зависящей от epsilon (пример O2, c=3/2, k_g=0).
Прямо в R^3: Pi=(s cos th, s sin th, s^{3/2} e), Y = DPi (1,-X^th/s,-X^e/s),
q(s) := min{ s<w,D_wY> : w ⊥ Y, |w|=1 } (мин. собств. значение симметр. части на Y^⊥).
Поле 1 (нормальное, X^th зависит от e): X = (mu/2) f grad f/|grad f|^2, f = e^2 - sin th.
Поле 2 (треугольное, середина дуги, chi=0): X^th = 0, X^e = (mu/4)(e^2 - sin th)/e.
"""
import sympy as sp, mpmath as mp
mp.mp.dps = 40
s, th, e = sp.symbols('s theta epsilon', positive=True)
mu = sp.Rational(1, 10)
f = e**2 - sp.sin(th)
gf = sp.Matrix([sp.diff(f, th), sp.diff(f, e)])
fields = {
  'normal': (mu/2*f*gf[0]/(gf.dot(gf)), mu/2*f*gf[1]/(gf.dot(gf))),
  'triangular(chi=0)': (sp.Integer(0), mu/4*(e**2 - sp.sin(th))/e),
}
Pi = sp.Matrix([s*sp.cos(th), s*sp.sin(th), s**sp.Rational(3, 2)*e])
J = Pi.jacobian([s, th, e])
for name, (Xt, Xe) in fields.items():
    Y = J*sp.Matrix([1, -Xt/s, -Xe/s])
    JY = Y.jacobian([s, th, e])
    fJ = sp.lambdify((s, th, e), J, 'mpmath'); fJY = sp.lambdify((s, th, e), JY, 'mpmath'); fY = sp.lambdify((s, th, e), Y, 'mpmath')
    dXt = sp.lambdify((th, e), sp.diff(Xt, e), 'mpmath')
    th0 = mp.mpf(1.0); e0 = mp.sqrt(mp.sin(th0))  # point on Gamma
    print('==', name, ' d_e X^theta at point =', mp.nstr(dXt(th0, e0), 8))
    for k in range(2, 19, 2):
        sv = mp.mpf(10)**(-k)
        Jv = mp.matrix(fJ(sv, th0, e0)); JYv = mp.matrix(fJY(sv, th0, e0)); Yv = mp.matrix(fY(sv, th0, e0))
        DY = JYv*mp.inverse(Jv)            # Cartesian derivative of Y
        Ssym = (DY + DY.T)/2*sv
        # orthonormal basis of Y^perp
        u = Yv/mp.norm(Yv)
        a = mp.matrix([1, 0, 0]) if abs(u[0]) < 0.9 else mp.matrix([0, 1, 0])
        b1 = a - (a.T*u)[0]*u; b1 = b1/mp.norm(b1)
        b2 = mp.matrix([u[1]*b1[2]-u[2]*b1[1], u[2]*b1[0]-u[0]*b1[2], u[0]*b1[1]-u[1]*b1[0]])
        B = mp.matrix(3, 2)
        for i in range(3):
            B[i, 0] = b1[i]; B[i, 1] = b2[i]
        M = B.T*Ssym*B
        ev = mp.eigsy(M)[0]
        qmin = min(ev[0], ev[1])
        print('  s=1e-%02d  min q = %s   q*s^{1/2} = %s' % (k, mp.nstr(qmin, 10), mp.nstr(qmin*mp.sqrt(sv), 10)))
