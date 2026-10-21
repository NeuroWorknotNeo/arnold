"""R30, рецензия §1–§2 записки notes/prover/2026-10-21-normal-multiplicity.md.

[Эксперимент] Символьные проверки (sympy, точно):
  1. M1, M2: phi(s,theta,y), носитель S, gamma_*, beta', Phi_0, U~ и тождество (2.1)
     U(s w + s^{1+g} eps n) = s^{m+beta'} U~(s^{1/N}, theta, eps)  (с s = sigma^N).
  2. Утверждение о первом ребре на случайных носителях (перебор):
     beta'(gamma_*) = 2r gamma_*, грань = {(0,2r)} U {(gamma_*(2r-l), l)}.
  3. Связь с 008 при r=1: G_min первого ребра = g_{m+1} или g_{m+2}.
"""
import random
from fractions import Fraction as Fr
import sympy as sp

x, y, z = sp.symbols('x y z', real=True)
s, Y, ph, eps, sig = sp.symbols('s Y phi epsilon sigma', real=True)


def phi_of(U, m):
    """phi(s,phi,Y) = U(s(omega+Y n))/s^m для omega=(cos,sin,0), n=e_z."""
    expr = U.subs({x: s*sp.cos(ph), y: s*sp.sin(ph), z: s*Y}, simultaneous=True)
    return sp.expand(sp.simplify(sp.expand(expr) / s**m))


def support(phi):
    P = sp.Poly(phi, s, Y)
    S = {}
    for (i, l), co in zip(P.monoms(), P.coeffs()):
        co = sp.simplify(co)
        if co != 0:
            S[(i, l)] = co
    return S


def first_edge(S, r):
    cand = [Fr(i, 2*r - l) for (i, l) in S if l < 2*r]
    return min(cand) if cand else None


def check_example(name, U, m, r):
    print('=' * 70)
    print(name)
    phi = phi_of(U, m)
    S = support(phi)
    print('  support S =', sorted(S))
    # (M): коэффициенты (0,l) при l<2r нулевые, (0,2r) > 0
    assert all((0, l) not in S for l in range(2*r)), 'нарушено (M)'
    print('  phi_{0,2r} =', S[(0, 2*r)])
    g = first_edge(S, r)
    N = g.denominator
    vals = {k: k[0] + g*k[1] for k in S}
    bp = min(vals.values())
    face = sorted(k for k in S if vals[k] == bp)
    print(f'  gamma_* = {g}, N = {N}, beta\' = {bp}, 2r gamma_* = {2*r*g}, j = {m + 2*r*g}, c = {1+g}')
    assert bp == 2*r*g
    Phi0 = sum(S[k]*eps**k[1] for k in face)
    print('  face =', face, '  Phi_0 =', sp.simplify(Phi0))
    # U~
    Ut = 0
    for (i, l), co in S.items():
        k = N*i + N*g*l - N*bp
        assert k.denominator == 1 and k >= 0
        Ut += co * sig**int(k) * eps**l
    Ut = sp.expand(Ut)
    print('  U~ =', Ut)
    # тождество (2.1): s = sigma^N, gamma = g
    gam = sp.Rational(g.numerator, g.denominator)
    lhs = U.subs({x: sig**N*sp.cos(ph), y: sig**N*sp.sin(ph),
                  z: sig**(N + N*gam)*eps}, simultaneous=True)
    rhs = sig**(N*(m + sp.Rational(bp.numerator, bp.denominator))) * Ut
    diff = sp.simplify(sp.expand(lhs - rhs))
    print('  (2.1): lhs - rhs =', diff)
    assert diff == 0
    assert sp.simplify(Ut.subs(sig, 0) - Phi0) == 0
    return S, g, Phi0, Ut


# M1 и M2 (определения записки)
M1 = (z - x**2)**4 + x**5 + y**5 + x*y**6 + y*x**6
M2 = z**4 + z*(x**4 + x**3*y + y**4) + x**6 + x*z**5 + 2*y*z**5
S1, g1, P1, U1 = check_example('M1', M1, 4, 2)
S2, g2, P2, U2 = check_example('M2', M2, 4, 2)

# M1: ветвь eps_0 = 0, кратность 2r'-1 = 3 (E)
print('M1: d^k Phi0/deps^k at eps=0, k=1..4:',
      [sp.simplify(sp.diff(P1, eps, k).subs(eps, 0)) for k in range(1, 5)])
# M2: eps_0 = -(f/4)^{1/3}, профиль
f = sp.cos(ph)**4 + sp.cos(ph)**3*sp.sin(ph) + sp.sin(ph)**4
e0, e = sp.symbols('e0 e', real=True)
Fs = sp.symbols('F', positive=True)
prof = sp.expand((e0 + e)**4 + Fs*(e0 + e) - (e0**4 + Fs*e0))
prof = sp.expand(prof.subs(Fs, -4*e0**3))  # 4 e0^3 = -f
print('M2: Phi0(e0+e)-G, при 4e0^3=-f :', sp.factor(prof),
      ' == e^2((e+2e0)^2+2e0^2)?', sp.expand(prof - e**2*((e + 2*e0)**2 + 2*e0**2)) == 0)
print('M2: G = Phi0(e0) с 4e0^3=-f -> (3/4) f e0 :',
      sp.simplify((e0**4 + f*e0).subs(f, -4*e0**3) - sp.Rational(3, 4)*(-4*e0**3)*e0) == 0)

# 2. случайные носители: первое ребро
print('=' * 70)
print('Случайные носители: проверка утверждения о первом ребре')
random.seed(1)
bad = 0
for trial in range(20000):
    r = random.randint(1, 4)
    pts = {(0, 2*r)}
    for _ in range(random.randint(1, 8)):
        i = random.randint(1, 9)
        l = random.randint(0, 3*r)
        pts.add((i, l))
    # (0,l), l>2r допускаются
    for _ in range(random.randint(0, 2)):
        pts.add((0, random.randint(2*r + 1, 3*r + 2)))
    if not any(l < 2*r for (_, l) in pts):
        continue
    g = first_edge(pts, r)
    vals = {k: k[0] + g*k[1] for k in pts}
    bp = min(vals.values())
    face = {k for k in pts if vals[k] == bp}
    exp_face = {(0, 2*r)} | {(i, l) for (i, l) in pts if l < 2*r and Fr(i) == g*(2*r - l)}
    # опорная прямая к вершине (0,2r): все точки в полуплоскости i >= g(2r-l)
    ok = (bp == 2*r*g) and face == exp_face and all(Fr(i) >= g*(2*r - l) for (i, l) in pts)
    # g — максимальный такой наклон: при g' > g нарушается
    g2 = g + Fr(1, 1000)
    ok = ok and any(Fr(i) < g2*(2*r - l) for (i, l) in pts if l < 2*r)
    if not ok:
        bad += 1
        print('  НАРУШЕНИЕ', r, sorted(pts), g, bp, face)
print('  нарушений:', bad)

# 3. Связь с 008 при r=1
print('=' * 70)
print('Связь с 008, r=1')
h, b0, b1, b2, c0, c1, d0 = sp.symbols('h b0 b1 b2 c0 c1 d0', real=True)
# phi = h/2 y^2 + O(y^3) + s(b0 + b1 y + b2 y^2) + s^2(c0 + c1 y) + s^3 d0
a3 = sp.symbols('a3', real=True)
phi = h/2*Y**2 + a3*Y**3 + s*(b0 + b1*Y + b2*Y**2) + s**2*(c0 + c1*Y) + s**3*d0
# точное дно 008: y*(s) из dphi/dy = 0, R(s) = phi(s, y*)
ys = sp.symbols('ys')
cs = sp.symbols('k1:5')
ystar = sum(cs[k]*s**(k + 1) for k in range(4))
eq = sp.expand(sp.diff(phi, Y).subs(Y, ystar))
sol = {}
for k in range(1, 5):
    co = sp.expand(eq.coeff(s, k).subs(sol))
    sk = sp.solve(co, cs[k - 1])[0]
    sol[cs[k - 1]] = sp.simplify(sk)
R = sp.expand(phi.subs(Y, ystar.subs(sol)))
g_m1 = sp.simplify(R.coeff(s, 1))
g_m2 = sp.simplify(R.coeff(s, 2))
print('  g_{m+1} =', g_m1, '   g_{m+2} =', g_m2)
# Newton: при b0 != 0: gamma_*=1/2, Phi0 = h/2 e^2 + b0  -> G_min = b0
# при b0 = 0: gamma_* = 1, Phi0 = h/2 e^2 + b1 e + c0 -> G_min = c0 - b1^2/(2h)
Gmin = sp.simplify(c0 - b1**2/(2*h))
print('  b0=0: g_{m+2} - (c0 - b1^2/(2h)) =', sp.simplify(g_m2.subs(b0, 0) - Gmin))
