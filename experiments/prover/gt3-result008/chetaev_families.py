# [Эксперимент] Явные семейства точек, где нарушено радиальное условие Четаева (result 008, пример 3).
# U7 = (x^2-z^2+z^3)^2 + (y^2-z^2)^2 + z^7: q = (sqrt(t^2+t^3-t^(7/2)/2), t, -t)  (семейство R22).
# U8 = (Q0+z^3)^2 + u7, u7 = x z^6 + x y z^5 + z^7/2:
#   верхняя компонента: phi = 5pi/6, z = zeta > 0, P = +1/2 sqrt(-u7);
#   нижняя компонента:  phi = pi,    z = -zeta < 0, P = -1/2 sqrt(-u7).
import sympy as sp
import mpmath as mp
mp.mp.dps = 60
x, y, z, t = sp.symbols('x y z t', positive=False, real=True)
U7 = (x**2 - z**2 + z**3)**2 + (y**2 - z**2)**2 + z**7
R7 = sum(sp.diff(U7, v)*v for v in (x, y, z))
sub = {x: sp.sqrt(t**2 + t**3 - t**sp.Rational(7, 2)/2), y: t, z: -t}
tp = sp.symbols('tau', positive=True)
U7s = sp.simplify(U7.subs(sub).subs(t, tp))
R7s = sp.simplify(sp.expand(R7.subs(sub).subs(t, tp)))
print('U7 на семействе =', sp.factor(U7s))
print('<grad U7, q> на семействе =', sp.factor(R7s))

Q0 = x**2 + y**2 - z**2
u7 = x*z**6 + x*y*z**5 + z**7/2
U8 = (Q0 + z**3)**2 + u7
R8 = sum(sp.diff(U8, v)*v for v in (x, y, z))
print('тождество <grad U8,q> - (4U8 + 2 z^3 P + 3 u7) =',
      sp.expand(R8 - (4*U8 + 2*z**3*(Q0 + z**3) + 3*u7)))
Uf = sp.lambdify((x, y, z), U8, 'mpmath'); Rf = sp.lambdify((x, y, z), R8, 'mpmath')
u7f = sp.lambdify((x, y, z), u7, 'mpmath')
for (phi, sgn) in [(5*mp.pi/6, 1), (mp.pi, -1)]:
    for zeta in [mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4'), mp.mpf('1e-5')]:
        zz = sgn*zeta
        def Pminus(Rr):
            xx, yy = Rr*mp.cos(phi), Rr*mp.sin(phi)
            P = Rr**2 - zz**2 + zz**3
            return P - sgn*mp.sqrt(-u7f(xx, yy, zz))/2
        a = zeta*mp.sqrt(1 - zeta) if sgn > 0 else zeta
        b = zeta if sgn > 0 else mp.sqrt(zeta**2 + zeta**3)
        Rr = mp.findroot(Pminus, (a, b), solver='bisect')
        xx, yy = Rr*mp.cos(phi), Rr*mp.sin(phi)
        print('phi=%s zeta=%s: u7=%s, U=%s, <gradU,q>=%s, <gradU,q>/|U|=%s' % (
            mp.nstr(phi, 4), mp.nstr(zeta, 2), mp.nstr(u7f(xx, yy, zz), 4), mp.nstr(Uf(xx, yy, zz), 4),
            mp.nstr(Rf(xx, yy, zz), 4), mp.nstr(Rf(xx, yy, zz)/abs(Uf(xx, yy, zz)), 5)))
# комплексные критические прямые U8: z = 0, x = i y
X, Y, Z = sp.symbols('X Y Z')
g = [sp.diff(U8, v).subs({x: X, y: Y, z: Z}) for v in (x, y, z)]
print('grad U8 на {z=0, x=iy}:', [sp.simplify(e.subs({Z: 0, X: sp.I*Y})) for e in g])
