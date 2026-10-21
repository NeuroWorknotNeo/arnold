"""R43: проверка констант пп. 5, 8 §3.2 results/014 (теорема W).  [Эксперимент]"""
import sympy as sp

beta, a0, delta, kap, R, mu0 = sp.symbols('beta a0 delta kappa R mu0', positive=True)
a1 = a3 = a0
a2 = beta * a0
h0, h1 = 1, sp.Rational(3, 2)
# L1, L2 из (3.1) [007]
L1 = 2 * (a2 + beta * a1 / 2) * sp.sqrt(h1 / a1)
L2 = 2 * sp.sqrt(2 * a3 / h0)
print('L1 == 3 beta sqrt(3a0/2):', sp.simplify(L1 - 3 * beta * sp.sqrt(3 * a0 / 2)) == 0)
print('L2 == 2 sqrt(2 a0):', sp.simplify(L2 - 2 * sp.sqrt(2 * a0)) == 0)
# Gamma_M при delta = a0/2 (худший случай), gamma1 = 5/4 kap R, gamma2 = 3/2 kap R
g1 = sp.Rational(5, 4) * kap * R
g2 = sp.Rational(3, 2) * kap * R
Gam = sp.sqrt(2) * ((a2 + beta * a0 / 2) * sp.sqrt(h1 / a1) * g1 + sp.sqrt(2 * a3 / h0) * g2)
ratio = sp.simplify(Gam / (sp.sqrt(a0) * kap * R))
print('Gamma_M/(sqrt(a0) kap R) =', ratio, '; == 15sqrt3/8 beta + 3:', sp.simplify(ratio - (15 * sp.sqrt(3) / 8 * beta + 3)) == 0)
CM = 15 * sp.sqrt(3) / 8 * beta + 4
# Gamma^2/(4 b' delta) с b' = beta/2 и kappa = mu0 beta delta/(2 CM^2 a0 R^2)  ==  kappa mu0/4 ?
kapmax = mu0 * beta * delta / (2 * CM**2 * a0 * R**2)
expr = (CM**2 * a0 * kap**2 * R**2 / (4 * (beta / 2) * delta)).subs(kap, kapmax) - kapmax * mu0 / 4
print("Gamma^2/(4b'delta) - kappa mu0/4 при kappa = третьему члену (0.8):", sp.simplify(expr))
# h <= 1 + (1/8)^2 (41/40)^2 + (1/4)^2
print('h_max =', float(1 + sp.Rational(1, 64) * sp.Rational(41, 40)**2 + sp.Rational(1, 16)))
# первый член (3.5): 1/(1-eps) - kappa >= 40/41 - 1/2 >= 4/5 - 1/2
print('40/41 >= 4/5:', sp.Rational(40, 41) >= sp.Rational(4, 5), '; 1/(1-1/40) <= 4/3:', 1 / (1 - sp.Rational(1, 40)) <= sp.Rational(4, 3))
# k1, k2 из п. 1 леммы M
k1 = sp.Rational(1, 2) * sp.sqrt(a1 / h1)
print('k1 == 1/2 sqrt(2a0/3):', sp.simplify(k1 - sp.sqrt(2 * a0 / 3) / 2) == 0)
