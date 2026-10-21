"""R34: independent check of examples K1, P1 (Sec. 3.2 of
notes/prover/2026-10-21-point-degenerate.md) and of the Euler identity for K1/P1.
[Experiment: sympy exact + mpmath for the cubic root.]"""
import sympy as sp
import mpmath as mp

x, y, z = sp.symbols('x y z', real=True)
s = sp.Symbol('s', positive=True)
b1, b2 = sp.symbols('b1 b2', real=True)

U_K1 = x**4 + y**4 - z**6
U_P1 = x**4 + y**4 - z**6 + x**3 * z**2 + 2 * y**3 * z**2 + x * z**6 + 3 * y * z**6

for name, U in (('K1', U_K1), ('P1', U_P1)):
    zz = s**2   # N = 2, z = s^2, weights 3/2: x = z^{3/2} b1 = s^3 b1
    F = sp.expand(U.subs({x: s**3 * b1, y: s**3 * b2, z: zz}) / zz**6)
    print(name, 'F(s,b) =', F)
    # (Q1): all powers of s nonnegative integers
    P = sp.Poly(F, s, b1, b2)
    print('   min power of s:', min(m[0] for m in P.monoms()))
    F0 = F.subs(s, 0)
    Q = F0 - F0.subs({b1: 0, b2: 0})
    euler = sp.simplify(sp.Rational(3, 2) * (b1 * Q.diff(b1) + b2 * Q.diff(b2)) - 6 * Q)
    print('   F0 =', F0, ';  <Cb,grad Q> - 6Q =', euler)
    # critical points of U (is 0 isolated?) -- Groebner basis
    G = sp.groebner([U.diff(v) for v in (x, y, z)], x, y, z, order='lex')
    print('   Groebner basis of grad U:', list(G)[:4], '...' if len(G) > 4 else '')

# P1: parity in z
print('P1: U(x,y,-z) - U(x,y,z) =', sp.expand(U_P1.subs(z, -z) - U_P1))

# P1 exact bottom: U(z^2 xi, z^2 eta, z) = -z^6 + z^8 (a(xi)+b(eta))
xi, eta = sp.symbols('xi eta', real=True)
bot = sp.expand(U_P1.subs({x: z**2 * xi, y: z**2 * eta}))
print('P1 bottom substitution:', sp.factor(bot + z**6))
a = xi**4 + xi**3 + xi
bb = eta**4 + 2 * eta**3 + 3 * eta
print("a' factor:", sp.factor(a.diff(xi)), ' a(-1)=', a.subs(xi, -1))
rts = sp.Poly(bb.diff(eta), eta).nroots(n=30)
print("b' roots:", rts)
er = [r for r in rts if abs(sp.im(r)) < 1e-20][0]
print('eta* =', er, ' b(eta*) =', bb.subs(eta, er), ' m coefficient z^8:', -1 + bb.subs(eta, er))
