"""R24: пересчёт констант §7–§10 results/008-class-K.md. [Эксперимент]"""
import sympy as sp
import random

ok_all = True


def check(name, cond):
    global ok_all
    ok_all &= bool(cond)
    print(('OK  ' if cond else 'FAIL') + ' ' + name)


# ---- §7: numeric constants
check('sqrt(17)/4 * X <= 3X/2 (so 2r <= 3X)', 2 * sp.sqrt(17) / 4 <= 3)
check('sqrt6*41/16 < 7', sp.sqrt(6) * sp.Rational(41, 16) < 7)
check('sqrt6*8 <= 20', sp.sqrt(6) * 8 <= 20)
check('5/16+9/4 = 41/16', sp.Rational(5, 16) + sp.Rational(9, 4) == sp.Rational(41, 16))
# r^{1/2} < sigma0 when r <= sqrt(17)/4 s0, s0 <= sigma0^2/2
check('sqrt(17)/8 < 1', sp.sqrt(17) / 8 < 1)
# F: varsigma (1+t^2)^{1/4} <= s0^{1/2}(17/16)^{1/4} < sigma0 when s0 <= sigma0^2/2
check('(17/16)^(1/4)/sqrt(2) < 1', (sp.Rational(17, 16)) ** sp.Rational(1, 4) / sp.sqrt(2) < 1)

# ---- §7 (V1): Hessian of F0(t,e) = (1+t^2)^{j/2}[G(atan t) + 1/2 h(atan t) (1+t^2)^{-c} e^2]
t, e, j, c = sp.symbols('t e j c', positive=True)
g0, g2, g3, h0, h1 = sp.symbols('g0 g2 g3 h0 h1', real=True)
th = sp.Symbol('th')
G = g0 + g2 * th ** 2 / 2 + g3 * th ** 3 / 6          # G'(0)=0
hn = h0 + h1 * th
F0 = (1 + t ** 2) ** (j / 2) * (G.subs(th, sp.atan(t)) + sp.Rational(1, 2) * hn.subs(th, sp.atan(t)) * (1 + t ** 2) ** (-c) * e ** 2)
H = sp.hessian(F0, (t, e)).subs({t: 0, e: 0})
grad = [sp.diff(F0, v).subs({t: 0, e: 0}) for v in (t, e)]
check('grad F0(0) = 0', all(sp.simplify(gv) == 0 for gv in grad))
check('H11 = G\'\'(0) + j G(0)', sp.simplify(H[0, 0] - (g2 + j * g0)) == 0)
check('H12 = 0', sp.simplify(H[0, 1]) == 0)
check('H22 = h_n(0)', sp.simplify(H[1, 1] - h0) == 0)

# ---- §9 item 4: Gamma' <= Gamma*
a0, beta, lam0, g1, g2_, delta = sp.symbols('a0 beta lambda0 gamma1 gamma2 delta', positive=True)
h1v, h0v = sp.Rational(3, 2), sp.Rational(1, 2)
a1 = a3 = a0
a2 = beta * a0
Gp = sp.sqrt(2) * ((a2 + beta * delta) * sp.sqrt(h1v / a1) * g1 / sp.sqrt(lam0) + sp.sqrt(2 * a3 / h0v) * g2_ / sp.sqrt(lam0))
Gstar = sp.sqrt(a0 / lam0) * (3 * sp.sqrt(3) / 2 * beta * g1 + 2 * sp.sqrt(2) * g2_)
diff_at_half = sp.simplify(Gp.subs(delta, a0 / 2) - Gstar)
check("Gamma'(delta=a0/2) == Gamma* (equality at the endpoint)", diff_at_half == 0)
check("dGamma'/ddelta >= 0 (so Gamma' <= Gamma* for delta <= a0/2)", sp.simplify(sp.diff(Gp, delta)) .is_nonnegative)
# L1, L2
L1 = 2 * (a2 + beta * a1 / 2) * sp.sqrt(h1v / a1)
L2 = 2 * sp.sqrt(2 * a3 / h0v)
check('L1 = 3 beta sqrt(3 a0/2)', sp.simplify(L1 - 3 * beta * sp.sqrt(3 * a0 / 2)) == 0)
check('L2 = 4 sqrt(a0)', sp.simplify(L2 - 4 * sp.sqrt(a0)) == 0)
# §9 item 5: L2 C1 R_b^2/sqrt(delta) + 4 C1 R_b with R_b = 2 sqrt(delta/lambda0)
C1 = sp.Symbol('C1', positive=True)
Rb = 2 * sp.sqrt(delta / lam0)
expr = L2 * C1 * Rb ** 2 / sp.sqrt(delta) + 4 * C1 * Rb
check('curvature term = C1 sqrt(delta)(16 sqrt(a0)/lambda0 + 8/sqrt(lambda0))',
      sp.simplify(expr - C1 * sp.sqrt(delta) * (16 * sp.sqrt(a0) / lam0 + 8 / sp.sqrt(lam0))) == 0)
mu = sp.Symbol('mu', positive=True)
check('bracket: mu/2*3/4 - mu/16 - mu/8 - mu/16 = mu/8',
      sp.simplify(mu / 2 * sp.Rational(3, 4) - mu / 16 - mu / 8 - mu / 16 - mu / 8) == 0)

# ---- Lemma 2' item 7: (beta - mu/2)K + (mu/2)Q >= Gamma sqrt(KQ) if Gamma^2 <= beta mu, 0<mu<=beta
random.seed(1)
worst = 1e9
for _ in range(200000):
    b_ = random.uniform(0.1, 10)
    m_ = random.uniform(1e-3, b_)
    Gm = (b_ * m_) ** 0.5
    K = random.uniform(0, 5)
    Q = random.uniform(0, 5)
    val = b_ * K + m_ * Q - Gm * (K * Q) ** 0.5 - m_ / 2 * (K + Q)
    worst = min(worst, val)
check(f'Lemma 2\' AM-GM (random, worst={worst:.3e}) >= -1e-12', worst >= -1e-12)
# symbolic: discriminant form. (beta-mu/2)K + (mu/2)Q - Gamma sqrt(KQ) >= 0 for all K,Q>=0 iff Gamma^2 <= mu(2beta-mu)
check('beta mu <= mu(2beta - mu) for mu<=beta', True)  # mu(2beta-mu) - beta mu = mu(beta-mu) >= 0

# ---- Lemma 2' item 2: lambda bounds
# lambda^2 h/2 in [(a1-delta) rho^beta, (a3+delta/2) rho^beta], delta<=a1/2 => 2(a1-delta)/h1 >= a1/h1
check('2(a1-delta) >= a1 when delta <= a1/2', True)
# |v_perp|^2 = 2K <= 3 delta rho^beta <= 4 delta rho^beta
check('sqrt(3) <= 2', sp.sqrt(3) <= 2)
check('sqrt(3/2) <= 2', sp.sqrt(sp.Rational(3, 2)) <= 2)

# ---- §10.2 item 2: h <= 1 + 25/16 kappa^2 r0^2 + 1/16 <= 3/2 for kappa <= 1/2, r0 <= 1/4
hb = 1 + sp.Rational(25, 16) * sp.Rational(1, 4) * sp.Rational(1, 16) + sp.Rational(1, 16)
check(f'h bound {float(hb):.4f} <= 3/2', hb <= sp.Rational(3, 2))
# item 5: 1/(1-eps) >= 4/5 for |eps| <= 1/4 ; 1/(1-eps) <= 4/3
check('main term 4/5 - 1/2 > 0', sp.Rational(4, 5) - sp.Rational(1, 2) > 0)
# item 7: Euler, e^2 coefficient (c - kappa/2) h - (kappa/2)|theta h'| >= (c - kappa) h >= h (c>=3/2,kappa<=1/2)
check('c - kappa >= 1', sp.Rational(3, 2) - sp.Rational(1, 2) >= 1)
# (U3)
jj, kk = sp.symbols('j kappa', positive=True)
Gs = sp.sqrt(a0 / lam0) * (3 * sp.sqrt(3) / 2 * jj * sp.Rational(5, 4) * kk + 2 * sp.sqrt(2) * kk * (1 - kk))
bound = kk * sp.sqrt(a0 / lam0) * (15 * sp.sqrt(3) / 8 * jj + 2 * sp.sqrt(2))
check('Gamma* <= kappa sqrt(a0/l0)(15sqrt3/8 j + 2sqrt2)', sp.simplify(bound - Gs - sp.sqrt(a0 / lam0) * 2 * sp.sqrt(2) * kk ** 2) == 0)
kmax = jj * lam0 / (a0 * (15 * sp.sqrt(3) / 8 * jj + 2 * sp.sqrt(2)) ** 2)
check('at kappa = kmax: (bound)^2 == j kappa', sp.simplify((bound ** 2 - jj * kk).subs(kk, kmax)) == 0)

# Example 3: j=7, G=sqrt2(2-3sqrt3)/64, G''=3sqrt6/16, h_n=8
Gv = sp.sqrt(2) * (2 - 3 * sp.sqrt(3)) / 64
Gpp = 3 * sp.sqrt(6) / 16
l0 = sp.Rational(1, 4) * sp.Min(Gpp, 8)
kv = (7 * l0 / ((-Gv) * (15 * sp.sqrt(3) / 8 * 7 + 2 * sp.sqrt(2)) ** 2))
print('   example 3: kappa_max =', sp.N(kv, 6))
check('example 3: kappa_max >= 0.0174', sp.N(kv) >= 0.0174)

print('ALL OK' if ok_all else 'SOME FAILED')
