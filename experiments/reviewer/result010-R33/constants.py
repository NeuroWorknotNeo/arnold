# R33: arithmetic of Lemma M and of the constant choice in Theorem Mb (results/010, §4, §5.2 pp. 5-7).
import sympy as sp
a0, j, kap, Rt, dl, a, p = sp.symbols('a0 j kappa R_theta delta a p', positive=True)
# Gamma with a1=a3=a0, a2=j a0, beta=j, h0=1, h1=3/2, gamma1=5/4 kappa R, gamma2<=2 kappa R, a2+beta*delta<=3/2 j a0
G_bound = sp.sqrt(2) * (sp.Rational(3, 2) * j * a0 * sp.sqrt(sp.Rational(3, 2) / a0) * sp.Rational(5, 4) * kap * Rt
                        + sp.sqrt(2 * a0) * 2 * kap * Rt)
CG = sp.Rational(15, 8) * sp.sqrt(3) * j + 4
print('Gamma bound == C_Gamma sqrt(a0) kappa R:', sp.simplify(G_bound - CG * sp.sqrt(a0) * kap * Rt))
# kappa formulas: j*delta/(2 C^2 a0 R^2) with R^2=(8 delta/a)^(1/p)
k1 = j * dl / (2 * CG**2 * a0 * (8 * dl / a)**(1 / p))
k2 = j / (2 * CG**2 * a0) * (a / 8)**(1 / p) * dl**(1 - 1 / p)
print('kappa(0.4) equivalence:', sp.simplify(sp.powsimp(sp.expand_power_base(k1 / k2, force=True), force=True)))
# Gamma^2/(4 b' delta) with b'>=j/2 and kappa <= j delta/(2 C^2 a0 R^2)
expr = (CG * sp.sqrt(a0) * kap * Rt)**2 / (4 * (j / 2) * dl)
print('Gamma^2/(4b delta) at kappa=kmax equals kappa/4:', sp.simplify(expr.subs(kap, j * dl / (2 * CG**2 * a0 * Rt**2)) / (j * dl / (2 * CG**2 * a0 * Rt**2)) ))
# Lemma M: completing the square
K, rb, bp, Gm = sp.symbols('K rho_b bprime Gamma', positive=True)
print('square identity:', sp.simplify(bp * K - Gm * sp.sqrt(K) * rb + Gm**2 / (4 * bp) * rb**2
                                      - (sp.sqrt(bp * K) - Gm * rb / (2 * sp.sqrt(bp)))**2))
# Lemma M step 3: (a2+beta delta) sqrt(h1/a1) * 2 theta1 sqrt(delta) <= L1 theta1 sqrt(delta) when delta<=a1/2
a1, a2, h1, beta = sp.symbols('a1 a2 h1 beta', positive=True)
L1 = 2 * (a2 + beta * a1 / 2) * sp.sqrt(h1 / a1)
print('L1 - 2(a2+beta delta)sqrt(h1/a1) at delta=a1/2:', sp.simplify(L1 - 2 * (a2 + beta * a1 / 2) * sp.sqrt(h1 / a1)))
# Gamma definition: sqrt2[(a2+beta delta)sqrt(h1/a1) g1 + sqrt(2a3/h0) g2]: coefficient check against T1,T2 bounds
g1, g2, a3, h0 = sp.symbols('gamma1 gamma2 a3 h0', positive=True)
T1c = (a2 + beta * dl) * sp.sqrt(h1 / a1) * sp.sqrt(2) * g1
T2c = sp.sqrt(2 * a3 / h0) * sp.sqrt(2) * g2
print('Gamma = T1c+T2c:', sp.simplify(sp.sqrt(2) * ((a2 + beta * dl) * sp.sqrt(h1 / a1) * g1 + sp.sqrt(2 * a3 / h0) * g2) - (T1c + T2c)))
# h <= 3/2: 1 + kappa^2 theta^2 (1-eps)^2 + nu^2 with kappa<=1/2,|theta|<1,|eps|,|nu|<=1/4
print('h max:', 1 + sp.Rational(1, 4) * (sp.Rational(5, 4))**2 + sp.Rational(1, 16), float(1 + sp.Rational(1, 4) * (sp.Rational(5, 4))**2 + sp.Rational(1, 16)))
# Lemma M p.1 condition in Mb step 7: 1/4 S + 5 sqrt(delta) kappa R <= 1/2 S, S=sqrt(2a0/3), with 5 R sqrt(delta)<=S/4, kappa<=1/2
print('p.1 margin: 1/4+1/8 =', sp.Rational(1, 4) + sp.Rational(1, 8), '<= 1/2')
# C_Gamma vs (U3) of [008]: 15sqrt3/8 j + 2 sqrt2 vs + 4
print('C_Gamma(j=3..8):', [float(CG.subs(j, jj)) for jj in range(3, 9)])
