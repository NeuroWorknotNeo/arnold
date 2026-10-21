"""R22: explicit families violating the radial Chetaev condition <grad U, q> < 0 on {U < 0}
arbitrarily close to 0, for U7 and U8 of section 9.7 (gt3-hardcore).

U7: q = (x, tau, -tau), x^2 = tau^2 + tau^3 - tau^(7/2)/2  =>  P1 = x^2 - z^2 + z^3 = -tau^(7/2)/2,
    B = y^2 - z^2 = 0, U = -3/4 tau^7, <grad U, q> = tau^(13/2) - 6 tau^7 > 0 for tau < 1/36.
U8: on the upper nappe at phi = 5pi/6, z = zeta > 0, R chosen by bisection with
    P = Q0 + z^3 = sqrt(-u7)/2 (IVT, see the review), => U = -3/4|u7| < 0 and
    <grad U, q> = zeta^3 sqrt|u7| - 6|u7| > 0.
Symbolic identity + numeric illustration.  [Experiment] (the U7 family is checked exactly)
"""
import sympy as sp
import mpmath as mp

x, y, z, tau = sp.symbols('x y z tau', positive=True)
X, Y, Z = sp.symbols('X Y Z', real=True)
U7 = (X**2 - Z**2 + Z**3)**2 + (Y**2 - Z**2)**2 + Z**7
rad7 = sp.expand(sum(v * sp.diff(U7, v) for v in (X, Y, Z)))
P1 = X**2 - Z**2 + Z**3
print('U7: <grad U,q> - (4U + 2 z^3 P1 + 3 z^7) =', sp.expand(rad7 - (4 * U7 + 2 * Z**3 * P1 + 3 * Z**7)))
sub = {X: sp.sqrt(tau**2 + tau**3 - tau**sp.Rational(7, 2) / 2), Y: tau, Z: -tau}
print('U7 on family:', sp.simplify(U7.subs(sub)))
print('<grad U7, q> on family:', sp.simplify(rad7.subs(sub)))

Q0 = X**2 + Y**2 - Z**2
P = Q0 + Z**3
u7 = X * Z**6 + X * Y * Z**5 + Z**7 / 2
U8 = P**2 + u7
rad8 = sp.expand(sum(v * sp.diff(U8, v) for v in (X, Y, Z)))
print('U8: <grad U,q> - (4U + 2 z^3 P + 3 u7) =', sp.expand(rad8 - (4 * U8 + 2 * Z**3 * P + 3 * u7)))
mp.mp.dps = 60
fU = sp.lambdify((X, Y, Z), U8, 'mpmath')
fr = sp.lambdify((X, Y, Z), rad8, 'mpmath')
fP = sp.lambdify((X, Y, Z), P, 'mpmath')
fu7 = sp.lambdify((X, Y, Z), u7, 'mpmath')
c, s_ = mp.cos(5 * mp.pi / 6), mp.sin(5 * mp.pi / 6)
for zeta in [mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4'), mp.mpf('1e-5')]:
    g = lambda R: fP(R * c, R * s_, zeta) - mp.sqrt(-fu7(R * c, R * s_, zeta)) / 2
    lo, hi = zeta * mp.sqrt(1 - zeta), zeta
    assert g(lo) < 0 < g(hi)
    R = mp.findroot(g, (lo, hi), solver='bisect')
    q = (R * c, R * s_, zeta)
    print(f'U8 zeta={mp.nstr(zeta, 2)}: u7={mp.nstr(fu7(*q), 4)}, U={mp.nstr(fU(*q), 4)}, '
          f'<grad U,q>={mp.nstr(fr(*q), 4)}, ratio <gradU,q>/|U| = {mp.nstr(fr(*q) / abs(fU(*q)), 4)}')
