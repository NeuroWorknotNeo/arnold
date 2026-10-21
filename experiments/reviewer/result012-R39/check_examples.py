"""R39: exact checks of the examples of results/012-free-field.md.

[Experiment: sympy, exact rational arithmetic unless stated.]
Longitudinal coordinate z (ray +e_z), transverse (x, y).  s = z^{1/N}.
Run:  ~/venv/bin/python check_examples.py
"""
import sympy as sp

x, y, z, b1, b2 = sp.symbols('x y z b1 b2', real=True)
s = sp.symbols('s', positive=True)  # s = z^{1/N} > 0
zp = sp.symbols('zp', positive=True)


def chart_F(U, c, N, beta, L=None, gamma=(0, 0)):
    """F(s,b) = z^{-beta} U(Phi(z,b)), z = s^N, transverse = gamma + L z^c b."""
    zz = s**N
    v = sp.Matrix([zz**sp.Rational(c[0]) * b1, zz**sp.Rational(c[1]) * b2])
    if L is not None:
        v = L.subs(z, zz) * v
    X = gamma[0] + v[0]
    Yv = gamma[1] + v[1]
    F = U.subs({x: X, y: Yv, z: zz}, simultaneous=True) / zz**beta
    return sp.expand(sp.simplify(sp.expand(F)))


def euler(Q, lam):
    return sp.expand(lam[0] * b1 * sp.diff(Q, b1) + lam[1] * b2 * sp.diff(Q, b2))


R = sp.Rational
ok = True


def check(name, cond):
    global ok
    print(f'{name:60s}', bool(cond))
    ok = ok and bool(cond)


# ---------------- K1
U = x**4 + y**4 - z**6
F = chart_F(U, (R(3, 2), R(3, 2)), 2, 6)
check('K1: F = -1 + b1^4 + b2^4', sp.expand(F - (-1 + b1**4 + b2**4)) == 0)
Q = b1**4 + b2**4
check('K1: <Cb,grad Q> = 6Q', sp.expand(euler(Q, (R(3, 2), R(3, 2))) - 6 * Q) == 0)

# ---------------- P1
U = x**4 + y**4 - z**6 + x**3 * z**2 + 2 * y**3 * z**2 + x * z**6 + 3 * y * z**6
F = chart_F(U, (R(3, 2), R(3, 2)), 2, 6)
check('P1: F formula', sp.expand(F - (-1 + b1**4 + b2**4 + s * (b1**3 + 2 * b2**3) + s**3 * (b1 + 3 * b2))) == 0)
check('P1: even in z', sp.expand(U.subs(z, -z) - U) == 0)
xi_, eta_ = sp.symbols('xi eta', real=True)
Uscaled = sp.expand(U.subs({x: z**2 * xi_, y: z**2 * eta_}, simultaneous=True))
check('P1: U(z^2 xi, z^2 eta, z) = -z^6 + z^8(a+b)',
      sp.expand(Uscaled - (-z**6 + z**8 * (xi_**4 + xi_**3 + xi_ + eta_**4 + 2 * eta_**3 + 3 * eta_))) == 0)
ap = sp.diff(xi_**4 + xi_**3 + xi_, xi_)
print('   a\'(xi) factor:', sp.factor(ap), ' real roots:', sp.real_roots(sp.Poly(ap, xi_)))
bp = sp.diff(eta_**4 + 2 * eta_**3 + 3 * eta_, eta_)
rr = sp.real_roots(sp.Poly(bp, eta_))
print('   b\'(eta) real roots:', [sp.N(r, 10) for r in rr])
etas = sp.N(rr[0], 30)
bval = etas**4 + 2 * etas**3 + 3 * etas
print('   a(-1) + b(eta*) =', sp.N(-1 + bval, 10), '(text: -7.589968)')

# ---------------- Lambda
k0 = R(199, 100)
U = x**4 - k0 * x**2 * y * z + y**2 * z**2 + y**4 - z**8 + x * z**7
u4 = x**4 - k0 * x**2 * y * z + y**2 * z**2 + y**4
check('Lambda: u4 SOS form', sp.expand(u4 - ((y * z - k0 / 2 * x**2)**2 + (1 - k0**2 / 4) * x**4 + y**4)) == 0)
check('Lambda: 1-k0^2/4 = 399/40000', 1 - k0**2 / 4 == R(399, 40000))
F = chart_F(U, (2, 3), 1, 8)
Q = b1**4 - k0 * b1**2 * b2 + b2**2
check('Lambda: F = -1 + Q + s b1 + s^4 b2^4', sp.expand(F - (-1 + Q + s * b1 + s**4 * b2**4)) == 0)
check('Lambda: <(C-I)b,grad Q> = 4Q', sp.expand(euler(Q, (1, 2)) - 4 * Q) == 0)
EC = euler(Q, (2, 3))
check('Lambda: <Cb,grad Q> = 8b1^4 - 7k0 b1^2 b2 + 6 b2^2', sp.expand(EC - (8 * b1**4 - 7 * k0 * b1**2 * b2 + 6 * b2**2)) == 0)
check('Lambda: discriminant 49k0^2-192 = 20449/10000', 49 * k0**2 - 192 == R(20449, 10000))
pt = {b1: 1, b2: R(116, 100)}
check('Lambda: Q(1,1.16) = 93/2500', Q.subs(pt) == R(93, 2500))
check('Lambda: <Cb,gradQ>(1,1.16) = -213/2500', EC.subs(pt) == R(-213, 2500))
# quasi-homogeneity (1,2) degree 4 of both
t = sp.symbols('t', positive=True)
check('Lambda: Q (1,2)-qh deg 4', sp.expand(Q.subs({b1: t * b1, b2: t**2 * b2}, simultaneous=True) - t**4 * Q) == 0)
check('Lambda: <Cb,gradQ> (1,2)-qh deg 4', sp.expand(EC.subs({b1: t * b1, b2: t**2 * b2}, simultaneous=True) - t**4 * EC) == 0)
p = sp.expand(u4.subs({x: b1, y: b2, z: 1}))
H = sp.hessian(p, (b1, b2)).subs({b1: 0, b2: 0})
print('   Lambda: D^2 p(0) =', H.tolist(), ' rank', H.rank())

# ---------------- SH
U = z**4 * (y - x**2 - x * z)**2 + x**6 + y**6 - z**12 + x * z**11
u6 = sum(term for term in sp.Add.make_args(sp.expand(U)) if sp.Poly(term, x, y, z).total_degree() == 6)
check('SH: u6 = x^6 + y^6 + y^2 z^4', sp.expand(u6 - (x**6 + y**6 + y**2 * z**4)) == 0)
mindeg = min(sp.Poly(term, x, y, z).total_degree() for term in sp.Add.make_args(sp.expand(U)))
check('SH: lowest degree = 6', mindeg == 6)
Fd = chart_F(U, (2, 4), 1, 12)
print('   SH direct chart F =', sp.collect(Fd, s))
Lm = sp.Matrix([[1, 0], [z, 1]])
FL = chart_F(U, (2, 4), 1, 12, L=Lm)
check('SH: shifted chart F', sp.expand(FL - (-1 + (b2 - b1**2)**2 + b1**6 + s * b1 + s**6 * (b1 + s * b2)**6)) == 0)
R1, R2 = (b2 - b1**2)**2, b1**6
check('SH: Cb.grad R1 = 8 R1', sp.expand(euler(R1, (2, 4)) - 8 * R1) == 0)
check('SH: Cb.grad R2 = 12 R2', sp.expand(euler(R2, (2, 4)) - 12 * R2) == 0)

# ---------------- R34 counterexample (remark 3)
U = -z**8 + z**4 * (x**2 + y**2) - z**2 * x**3
F = chart_F(U, (2, 2), 1, 8)
check('R34: F = -1 + b1^2 + b2^2 - b1^3', sp.expand(F - (-1 + b1**2 + b2**2 - b1**3)) == 0)

# ---------------- Remark 4 examples
# X
U = x**6 + y**6 + y**4 * z**2 + x**2 * y**2 * z**2 - z**12 + x * z**11
F = chart_F(U, (2, R(5, 2)), 2, 12)
check('X: F formula', sp.expand(F - (-1 + b1**6 + b2**4 + b1**2 * b2**2 / s**2 + s**2 * b1 + s**6 * b2**6)) == 0)
Qc = b1**6 + b2**4
check('X: lambda=c Euler: 12 b1^6 + 10 b2^4', sp.expand(euler(Qc, (2, R(5, 2))) - (12 * b1**6 + 10 * b2**4)) == 0)
# monomial b1^2 b2^2 s^{-2}: level 12 - 2/2 = 11 ; lambda.alpha + beta - level = 4 + 5 + 1 = 10
# SV2
U = (z**4 * y - z**4 * x**2 - z**2 * x**3)**2 + x**8 + y**8 - z**16 + x * z**15
F = chart_F(U, (2, 4), 1, 16)
tt = b2 - b1**2 - b1**3
check('SV2: F formula', sp.expand(F - (-1 + tt**2 + b1**8 + s * b1 + s**16 * b2**8)) == 0)
Q = tt**2 + b1**8
xiQ = sp.expand(b1 * sp.diff(Q, b1) + (2 * b2 + b1**3) * sp.diff(Q, b2))
check('SV2: xi.grad Q = 4 t^2 + 8 b1^8', sp.expand(xiQ - (4 * tt**2 + 8 * b1**8)) == 0)
phi = b1**2 + b1**3
check('SV2: field = (b1, b1 phi\' + 2(b2-phi))', sp.expand(b1 * sp.diff(phi, b1) + 2 * (b2 - phi) - (2 * b2 + b1**3)) == 0)
EC = euler(Q, (2, 4))
val = sp.factor(EC.subs(b2, b1**2 + b1**3 + b1**3 / 4))
check('SV2: <Cb,gradQ> at t=b1^3/4 = b1^6(32 b1^2-1)/2', sp.expand(val - b1**6 * (32 * b1**2 - 1) / 2) == 0)
# R (ring)
U = (x**2 + y**2 - z**3)**2 - z**8 + x * z**8
F = chart_F(U, (R(3, 2), R(3, 2)), 2, 8)
print('   R: F =', F)
# critical lines over C
xs, ys, zs = sp.symbols('xs ys zs')
Uc = U.subs({x: xs, y: ys, z: zs})
grad = [sp.diff(Uc, v) for v in (xs, ys, zs)]
check('R: grad U = 0 on {z=0, x=i y}', all(sp.expand(gc.subs({zs: 0, xs: sp.I * ys})) == 0 for gc in grad))
# E (two sub-ravines)
U = x**12 + y**12 + z**4 * (x**2 - y * z**2)**2 * (x**3 - y * z**4)**2 - z**24 + x * z**23
F = chart_F(U, (2, 2), 1, 24)
QE = (b2 - b1**2)**2 * (b2 - b1**3)**2 + b1**12 + b2**12
check('E: F = -1 + Q + s b1', sp.expand(F - (-1 + QE + s * b1)) == 0)
l1, l2, tau = sp.symbols('l1 l2 tau', real=True)
xiQE = sp.expand(l1 * b1 * sp.diff(QE, b1) + l2 * b2 * sp.diff(QE, b2))
for curve, lead in ((b1**2 + tau * b1**4, 10), (b1**3 + tau * b1**4, 11)):
    e = sp.expand(xiQE.subs(b2, curve))
    q = sp.expand(QE.subs(b2, curve))
    lowe = sp.Poly(e, b1).as_expr()
    # lowest-order term in b1
    terms = sp.Poly(e, b1).terms()
    mdeg = min(m[0][0] for m in terms)
    coeff = sp.factor(sp.Poly(e, b1).coeff_monomial(b1**mdeg))
    qterms = sp.Poly(q, b1).terms()
    qmdeg = min(m[0][0] for m in qterms)
    print(f'   E: on b2={curve}: lowest xiQ term b1^{mdeg} * ({coeff}),  Q ~ b1^{qmdeg}')

# ---------------- G1 example of R36
U = (x**2 + y**2 - z**6)**2 - z**16 + x * z**13
F = chart_F(U, (3, 3), 1, 16)
check('G1: F = -1 + s^-4 (|b|^2-1)^2 + b1', sp.expand(F - (-1 + (b1**2 + b2**2 - 1)**2 / s**4 + b1)) == 0)

print('ALL OK' if ok else 'SOME CHECK FAILED')
