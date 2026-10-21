# R31: arithmetic of Theorem 2'' (steps 4-5) and Theorem N (pp. 2, 5, 7)
import sympy as sp
a0, lam0, beta, delta, C1, mu, kap, kg, r0 = sp.symbols('a0 lambda0 beta delta C1 mu kappa kbar r0', positive=True)
h0, h1 = sp.Rational(1, 2), sp.Rational(3, 2)
a1 = a3 = a0; a2 = beta*a0
L1 = 2*(a2 + beta*a1/2)*sp.sqrt(h1/a1); L2 = 2*sp.sqrt(2*a3/h0)
print('L1 - 3 beta sqrt(3a0/2) =', sp.simplify(L1 - 3*beta*sp.sqrt(3*a0/2)), '; L2 - 4 sqrt(a0) =', sp.simplify(L2 - 4*sp.sqrt(a0)))
# Gamma' with delta = a0/2 (worst case) vs Gamma_*
g1, g2 = sp.symbols('gamma1 gamma2', positive=True)
Gp = sp.sqrt(2)*((a2 + beta*a0/2)*sp.sqrt(h1/a1)*g1/sp.sqrt(lam0) + sp.sqrt(2*a3/h0)*g2/sp.sqrt(lam0))
Gs = sp.sqrt(a0/lam0)*(3*sp.sqrt(3)/2*beta*g1 + 2*sp.sqrt(2)*g2)
print("Gamma'(delta=a0/2) - Gamma_* =", sp.simplify(Gp - Gs))
# delta-only terms: theta2 = C1 R'^2, theta3 = C1 R', R'^2 = 2 delta/lam0
Rp2 = 2*delta/lam0
expr = L2*C1*Rp2/sp.sqrt(delta) + 4*C1*sp.sqrt(Rp2)
print('delta-only terms - C1 sqrt(delta)(8 sqrt(a0)/lam0 + 4 sqrt2/sqrt(lam0)) =',
      sp.simplify(expr - C1*sp.sqrt(delta)*(8*sp.sqrt(a0)/lam0 + 4*sp.sqrt(2)/sp.sqrt(lam0))))
print('bracket lower bound =', sp.Rational(1, 2)*mu*sp.Rational(3, 4) - mu/16 - mu/8 - mu/16)
# Theorem N p.2: h bound
print('h upper bound =', 1 + sp.Rational(1, 4)*sp.Rational(1, 16)*sp.Rational(25, 16) + sp.Rational(1, 16), '< 3/2')
# Theorem N p.5: theta-coefficient
coef = sp.Rational(5, 3)*kap*kg + sp.Rational(5, 4)*kap**2*sp.Rational(1, 4) + 2*kap*kg
print('theta coefficient =', sp.simplify(coef), ';  C1 - coef =', sp.simplify(sp.Rational(5, 4)*kap**2*(1 + kg) + 4*kap*kg - coef))
# Theorem N p.7: Euler identity
th, e, c = sp.symbols('theta e c', real=True)
rp = sp.symbols('rp', positive=True, integer=True)
G = sp.Function('G'); p = sp.Function('p')
Q = G(th) - G(0) + e**(2*rp)*p(th, e)
lhs = kap*th*sp.diff(Q, th) + c*e*sp.diff(Q, e) - kap*Q
rhs = kap*(th*sp.diff(G(th), th) - (G(th) - G(0))) + e**(2*rp)*((2*rp*c - kap)*p(th, e) + c*e*sp.diff(p(th, e), e) + kap*th*sp.diff(p(th, e), th))
print('Euler identity diff =', sp.simplify(sp.expand(lhs - rhs)))
# (4.0): Gamma_* with gamma1 = 5/4 kappa, gamma2 = kappa(1-kappa)
Gs_N = sp.sqrt(a0/lam0)*(3*sp.sqrt(3)/2*beta*sp.Rational(5, 4)*kap + 2*sp.sqrt(2)*kap*(1 - kap))
bound = kap*sp.sqrt(a0/lam0)*(sp.Rational(15, 8)*sp.sqrt(3)*beta + 2*sp.sqrt(2))
print('bound - Gamma_* =', sp.simplify(bound - Gs_N), '(= 2 sqrt2 kappa^2 sqrt(a0/lam0) >= 0)')
