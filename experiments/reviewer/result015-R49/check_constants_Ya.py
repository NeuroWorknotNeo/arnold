"""R49: арифметика констант в доказательстве теоремы Я и теоремы H (results/015-master.md, §1, §5).
[Эксперимент: символьная арифметика; проверяет только выкладки с числами, не логику.]"""
import sympy as sp

mu, beta, a0, d, h0, h1, g1, g2, g1p, g2p = sp.symbols('mu beta a0 delta h0 h1 gamma1 gamma2 gamma1p gamma2p',
                                                         positive=True)
R = sp.Rational
# (2.1): L1 = 2(a2 + beta a1/2) sqrt(h1/a1), a1=a3=a0, a2=beta a0
L1 = 2 * (beta * a0 + beta * a0 / 2) * sp.sqrt(h1 / a0)
print('(2.1) L1 == 3 beta sqrt(a0 h1):', sp.simplify(L1 - 3 * beta * sp.sqrt(a0 * h1)) == 0)
# Gamma_M при a2+beta*delta = 3/2 beta a0 (верхняя граница) против Gamma теоремы Я
GM = sp.sqrt(2) * (R(3, 2) * beta * a0 * sp.sqrt(h1 / a0) * g1 + sp.sqrt(2 * a0 / h0) * g2)
G = sp.sqrt(2 * a0) * (R(3, 2) * beta * sp.sqrt(h1) * g1 + sp.sqrt(2 / h0) * g2)
print('Gamma_M(max) == Gamma:', sp.simplify(GM - G) == 0)
# monotonicity of Gamma_M in a2+beta*delta: coefficient of gamma1 positive -> Gamma_M <= Gamma
# вариант (M): скобка
eps1 = mu / 4 + mu / 32
br = mu - eps1 - R(5, 4) * mu / 4 - (mu / 8 + mu / 32)
print('(M) bracket =', sp.simplify(br))
# вариант (Q): скобка mu/2 (1-eps0) - eps1 - ... с eps0<=1/4, eps1<=mu/32, L-члены+4theta3 <= mu/8+mu/32
brQ = mu / 2 * R(3, 4) - mu / 32 - (mu / 8 + mu / 32)
print('(Q) bracket =', sp.simplify(brQ))
# (A4): 4 sqrt(delta) theta1^0 <= mu delta/(2 L1) <= (beta a0/2)/(2*3 beta sqrt(a0 h1))
val = (beta * a0 / 2) / (2 * 3 * beta * sp.sqrt(a0 * h1))
print('(A4) bound/sqrt(a0/h1) =', sp.simplify(val / sp.sqrt(a0 / h1)), '; total 1/12+1/4+1/2 =', R(1, 12) + R(1, 4) + R(1, 2))
# b' >= 4/5 (beta-mu-2theta3^0) when theta3(sigma) <= (beta-mu-2theta3^0)/10
X = sp.Symbol('X', positive=True)
print("b' lower bound:", sp.simplify(X - 2 * X / 10), '= 4/5 X')
# Lemma 2' Gamma' vs Gamma' of theorem Я
GQ = sp.sqrt(2) * (R(3, 2) * beta * a0 * sp.sqrt(h1 / a0) * g1p + sp.sqrt(2 * a0 / h0) * g2p)
GQY = sp.sqrt(2 * a0) * (R(3, 2) * beta * sp.sqrt(h1) * g1p + sp.sqrt(2 / h0) * g2p)
print("Gamma'_{2'}(max) == Gamma':", sp.simplify(GQ - GQY) == 0)
# Theorem H: expression for theta3(s) is nondecreasing in zeta and equals >= m3 at zeta=0
m, Lam, Cv, gT, gv, z = sp.symbols('m Lambda C_v gamma_T gamma_v zeta', nonnegative=True)
expr = (m + z) * (1 + Lam ** 3 * (z + gT)) ** 2 + 2 * Lam ** 5 * Cv * (z + gT) + Lam * (z + gv)
m3 = m * (1 + Lam ** 3 * gT) ** 2 + 2 * Lam ** 5 * Cv * gT + Lam * gv
print('H: expr(zeta=0) - m3 =', sp.simplify(expr.subs(z, 0) - m3))
dexpr = sp.expand(sp.diff(expr, z))
print('H: d expr/d zeta has only nonnegative coefficients:',
      all(c >= 0 for c in sp.Poly(dexpr, z, m, Lam, Cv, gT, gv).coeffs()))
