"""[Эксперимент] Примеры к записке notes/prover/2026-10-21-point-degenerate.md (точная арифметика sympy).

Для каждого примера: ведущая форма u_m, поперечный профиль p, карта, функция F(s,b) = x^{-beta} U(карта),
разложение F по уровням L = k/N + c.alpha, профиль Q, условие Эйлера.
Продольная координата везде z (луч omega = +e_z), поперечные (x, y).
"""
import itertools
import sympy as sp

x, y, z, b1, b2, t = sp.symbols('x y z b1 b2 t', real=True)
s = sp.symbols('s', positive=True)
zp = sp.symbols('zp', positive=True)


def lowest_form(U):
    P = sp.Poly(sp.expand(U), x, y, z)
    m = min(sum(mon) for mon in P.monoms())
    um = sum(cf * x**a * y**b_ * z**c_ for (a, b_, c_), cf in zip(P.monoms(), P.coeffs()) if a + b_ + c_ == m)
    return m, sp.expand(um)


def chart_F(U, beta, c, N, gam=(0, 0), L=None):
    """F(s,b) = z^{-beta} U(gam + L(z) z^c b, z), s = z^{1/N}; возвращает выражение от (s,b1,b2)."""
    zz = s**N
    v = sp.Matrix([zz**c[0] * b1, zz**c[1] * b2])
    if L is not None:
        v = L.subs(z, zz) * v
    X = gam[0] + v[0]
    Yv = gam[1] + v[1]
    F = sp.expand(sp.powsimp(sp.expand(U.subs({x: X, y: Yv, z: zz}, simultaneous=True) / zz**beta), force=True))
    return F


def split_levels(F):
    """Разложение F по степеням s: {показатель s: коэффициент(b)}."""
    F = sp.expand(F)
    d = {}
    for term in sp.Add.make_args(F):
        e = term.as_powers_dict().get(s, 0) if term.has(s) else 0
        d[e] = sp.expand(d.get(e, 0) + term / s**e)
    return dict(sorted(d.items(), key=lambda kv: kv[0]))


def euler(Q, w):
    return sp.expand(w[0] * b1 * sp.diff(Q, b1) + w[1] * b2 * sp.diff(Q, b2))


def report(name, U, beta, c, N, gam=(0, 0), L=None):
    print('=' * 100)
    print(name, ':  U =', U)
    m, um = lowest_form(U)
    print(f'  m = {m}, u_m = {um};  p(y1,y2) = u_m(y1,y2,1) = {sp.expand(um.subs({x: b1, y: b2, z: 1}))}')
    F = chart_F(U, beta, c, N, gam, L)
    lev = split_levels(F)
    print(f'  chart: beta={beta}, c={c}, N={N}, gamma={gam}, L={L}')
    for e, coef in lev.items():
        print(f'    s^{e}:  {coef}')
    return F, lev


out = []

# ---------------------------------------------------------------- K1, P1
for name, U in [('K1', x**4 + y**4 - z**6),
                ('P1', x**4 + y**4 - z**6 + x**3 * z**2 + 2 * y**3 * z**2 + x * z**6 + 3 * y * z**6)]:
    F, lev = report(name, U, 6, (sp.Rational(3, 2), sp.Rational(3, 2)), 2)
    Q = lev[0] - lev[0].subs({b1: 0, b2: 0})
    print('  F0(0) =', lev[0].subs({b1: 0, b2: 0}), ';  Q =', Q)
    EQ = euler(Q, (sp.Rational(3, 2), sp.Rational(3, 2)))
    print('  sum c_i b_i dQ/db_i - 6 Q =', sp.simplify(EQ - 6 * Q))
    assert all(e >= 0 for e in lev), 'negative s-power'

# P1: точное дно (разделение переменных)
print('-' * 100)
xi_, eta_ = sp.symbols('xi eta', real=True)
a_ = xi_**4 + xi_**3 + xi_
b_ = eta_**4 + 2 * eta_**3 + 3 * eta_
print("P1 bottom: a'(xi) =", sp.factor(sp.diff(a_, xi_)), ';  real roots:', sp.real_roots(sp.Poly(sp.diff(a_, xi_), xi_)))
rb = sp.real_roots(sp.Poly(sp.diff(b_, eta_), eta_))
print("           b'(eta) =", sp.diff(b_, eta_), ';  real roots:', rb, '=', [sp.N(r, 15) for r in rb])
print('           a(-1) =', a_.subs(xi_, -1), ';  b(eta*) =', sp.N(b_.subs(eta_, rb[0]), 15))
Up1 = x**4 + y**4 - z**6 + x**3 * z**2 + 2 * y**3 * z**2 + x * z**6 + 3 * y * z**6
print('  check U(z^2 xi, z^2 eta, z) = -z^6 + z^8 (a(xi)+b(eta)):',
      sp.expand(Up1.subs({x: zp**2 * xi_, y: zp**2 * eta_, z: zp}) - (-zp**6 + zp**8 * (a_ + b_))))

# ---------------------------------------------------------------- X (крест)
UX = x**6 + y**6 + y**4 * z**2 + x**2 * y**2 * z**2 - z**12 + x * z**11
F, lev = report('X (cross)', UX, 12, (2, sp.Rational(5, 2)), 2)
print('  low level s^-2 coefficient (must be a sum of positive even monomials):', lev.get(-2))
Q = lev[0] + 1
print('  Q =', Q, ';  E_c Q - 10 Q =', euler(Q, (2, sp.Rational(5, 2))) - 10 * Q)
R2 = lev[-2]
print('  E_c R2 + (e/N) R2 with e=2,N=2:', sp.factor(euler(R2, (2, sp.Rational(5, 2))) + R2), ' = 10*R2 ?',
      sp.simplify(euler(R2, (2, sp.Rational(5, 2))) + R2 - 10 * R2) == 0)
# изолированность критической точки U_X: dU/dy = 2y(3y^4+2y^2z^2+x^2z^2)
print('  dU_X/dy =', sp.factor(sp.diff(UX, y)))
print('  on y=0: dU/dx =', sp.diff(UX, x).subs(y, 0), ';  dU/dz =', sp.factor(sp.diff(UX, z).subs(y, 0)))

# ---------------------------------------------------------------- Lambda
k = sp.Rational(199, 100)
UL = x**4 - k * x**2 * y * z + y**2 * z**2 + y**4 - z**8 + x * z**7
F, lev = report('Lambda', UL, 8, (2, 3), 1)
Q = lev[0] + 1
print('  Q =', Q)
EcQ = euler(Q, (2, 3))
print('  E_c Q =', EcQ, ';  discriminant in tau=b2/b1^2 of E_cQ/b1^4:',
      sp.discriminant(sp.expand(EcQ.subs(b2, t * b1**2) / b1**4), t))
print('  Lambda Q (lambda=(1,2)) - 4Q =', sp.expand(euler(Q, (1, 2)) - 4 * Q))
print('  example point b=(1, 1.16): Q =', Q.subs({b1: 1, b2: sp.Rational(116, 100)}),
      ', E_cQ =', EcQ.subs({b1: 1, b2: sp.Rational(116, 100)}))
print('  u_4 as SOS: (yz - k x^2/2)^2 + (1-k^2/4) x^4 + y^4:',
      sp.expand((y * z - k * x**2 / 2)**2 + (1 - k**2 / 4) * x**4 + y**4 - lowest_form(UL)[1]))

# ---------------------------------------------------------------- SV и SH (подовраги)
USV = z**4 * (y - x**2)**2 + x**6 + y**6 - z**12 + x * z**11
F, lev = report('SV (sub-valley y=x^2)', USV, 12, (2, 4), 1)
Q = lev[0] + 1
print('  Q =', sp.factor(Q), ';  E_cQ - 8Q =', sp.factor(euler(Q, (2, 4)) - 8 * Q))

USH = z**4 * (y - x**2 - x * z)**2 + x**6 + y**6 - z**12 + x * z**11
print('-' * 100)
F0, lev0 = report('SH, straight chart (no shear)', USH, 12, (2, 4), 1)
Lsh = sp.Matrix([[1, 0], [z, 1]])
F, lev = report('SH, shear chart L(z)=[[1,0],[z,1]]', USH, 12, (2, 4), 1, L=Lsh)
Q = lev[0] + 1
print('  Q =', sp.factor(Q))

# ---------------------------------------------------------------- R (кольцо), плоскость y=0
UR = (x**2 + y**2 - z**3)**2 - z**8 + x * z**8
print('=' * 100)
print('R (ring): U =', UR, '; lowest form:', lowest_form(UR))
print('  U(x,-y,z) - U(x,y,z) =', sp.expand(UR.subs(y, -y) - UR))
U2 = UR.subs(y, 0)
F2 = sp.expand(sp.powsimp(sp.expand(U2.subs({x: -s**3 + s**5 * b1, z: s**2}) / s**16), force=True))
print('  2D chart x = -z^{3/2} + z^{5/2} b, s = z^{1/2}:  F =', sp.collect(F2, s))
print('  dU/dy =', sp.factor(sp.diff(UR, y)))

# ---------------------------------------------------------------- E (два подоврага, для теоремы E)
UE = x**12 + y**12 + z**4 * (x**2 - y * z**2)**2 * (x**3 - y * z**4)**2 - z**24 + x * z**23
F, lev = report('E (two sub-valleys)', UE, 24, (2, 2), 1)
Q = lev[0] + 1
print('  Q =', sp.factor(Q))
QE = (b2 - b1**2)**2 * (b2 - b1**3)**2 + b1**12 + b2**12
print('  Q - [(b2-b1^2)^2 (b2-b1^3)^2 + b1^12 + b2^12] =', sp.expand(Q - QE))
