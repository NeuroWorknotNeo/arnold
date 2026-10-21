"""Рецензент R21: символьная проверка констант §7 записки
notes/prover/2026-10-21-gt3-hardcore.md (лемма 2', теорема 2').

[Эксперимент] Проверяются только алгебраические тождества и неравенства между константами.
Запуск: ~/venv/bin/python check_constants.py
"""
import sympy as sp

a0, beta, delta, lam0, mu, C1, g1, g2, a1, a2, a3, h0, h1 = sp.symbols(
    'a0 beta delta lambda0 mu C1 gamma1 gamma2 a1 a2 a3 h0 h1', positive=True)

ok = True


def check(name, expr):
    global ok
    e = sp.simplify(expr)
    good = (e == 0)
    ok &= bool(good)
    print(f"{'OK ' if good else 'FAIL'} {name}: {e}")


# Константы леммы 2' (= L1, L2 в results/007)
c1 = 2 * (a2 + beta * a1 / 2) * sp.sqrt(h1 / a1)
c2 = 2 * sp.sqrt(2 * a3 / h0)
subs = {a1: a0, a3: a0, a2: beta * a0, h0: sp.Rational(1, 2), h1: sp.Rational(3, 2)}
check("c1 = 3 beta sqrt(3 a0/2)", c1.subs(subs) - 3 * beta * sp.sqrt(3 * a0 / 2))
check("c2 = 4 sqrt(a0)", c2.subs(subs) - 4 * sp.sqrt(a0))

# Gamma' из леммы 2' и Gamma_* из (7.2)
g1p, g2p = g1 / sp.sqrt(lam0), g2 / sp.sqrt(lam0)
Gp = sp.sqrt(2) * ((a2 + beta * delta) * sp.sqrt(h1 / a1) * g1p + sp.sqrt(2 * a3 / h0) * g2p)
Gstar = sp.sqrt(a0 / lam0) * (sp.Rational(3, 2) * sp.sqrt(3) * beta * g1 + 2 * sp.sqrt(2) * g2)
Gp_s = Gp.subs(subs)
check("Gamma'(delta=a0/2) = Gamma_*", Gp_s.subs(delta, a0 / 2) - Gstar)
# монотонность по delta: производная >= 0
dG = sp.diff(Gp_s, delta)
print("dGamma'/ddelta =", sp.simplify(dG), "(>=0 очевидно)")

# Член, зависящий только от delta (шаг 5 теоремы 2')
Rb = 2 * sp.sqrt(delta / lam0)
lhs = c2.subs(subs) * C1 * Rb**2 / sp.sqrt(delta) + 4 * C1 * Rb
rhs = C1 * sp.sqrt(delta) * (16 * sp.sqrt(a0) / lam0 + 8 / sp.sqrt(lam0))
check("c2 C1 Rb^2/sqrt(d) + 4 C1 Rb", lhs - rhs)

# Итоговая скобка
check("mu/2*3/4 - mu/8 - mu/16 - mu/16 = mu/8",
      mu / 2 * sp.Rational(3, 4) - mu / 8 - mu / 16 - mu / 16 - mu / 8)

# Квадратичная форма в п. 7 леммы 2': (beta-mu/2)K + (mu/2)P - Gamma sqrt(KP) >= 0
# <=> Gamma^2 <= 4 (beta-mu/2)(mu/2) = mu(2 beta - mu)
check("4(beta-mu/2)(mu/2) = mu(2beta-mu)", 4 * (beta - mu / 2) * (mu / 2) - mu * (2 * beta - mu))
print("mu(2beta-mu) - beta mu =", sp.factor(mu * (2 * beta - mu) - beta * mu), "(>=0 при mu<=beta)")

# п. 4 леммы 2': (a2+beta*delta) sqrt(h1/a1) * 2 <= c1 при delta <= a1/2
print("c1 - 2(a2+beta delta)sqrt(h1/a1) =",
      sp.simplify(c1 - 2 * (a2 + beta * delta) * sp.sqrt(h1 / a1)), "(>=0 при delta<=a1/2)")

# Теорема K2 использует (7.2) с gamma1=5/4 kappa, gamma2=kappa(1-kappa): проверка оценки (8.5)
# (вне объёма проверки; только как согласованность формулы (7.2))
kap, j = sp.symbols('kappa j', positive=True)
GK2 = Gstar.subs({g1: sp.Rational(5, 4) * kap, g2: kap * (1 - kap), beta: j})
bound = kap * sp.sqrt(a0 / lam0) * (sp.Rational(15, 8) * sp.sqrt(3) * j + 2 * sp.sqrt(2))
print("K2: bound - Gamma_* =", sp.simplify(bound - GK2), "(>=0)")

# Ослабленный вариант: Gamma'^2 < 4 beta mu даёт eps(K+P) с eps>0 (PSD-критерий)
eps, K, P, G = sp.symbols('epsilon K P Gamma', positive=True)
M = sp.Matrix([[beta - eps, -G / 2], [-G / 2, mu - eps]])
print("det для (beta-eps)K + (mu-eps)P - G sqrt(KP):", sp.expand(M.det()))

# Предел Gamma' при delta->0 с точной нижней оценкой lambda на множестве (A5):
# lambda^2 h/2 = (a0 - delta) rho^beta  =>  1/lambda <= sqrt(h1/(2(a0-delta))) rho^{-beta/2}
Gsharp = sp.sqrt(2) * (beta * a0 * sp.sqrt(h1 / (2 * a0)) * g1p + sp.sqrt(2 * a0 / h0) * g2p)
print("Gamma' (delta->0, точная оценка lambda) =",
      sp.simplify(Gsharp.subs({h0: sp.Rational(1, 2), h1: sp.Rational(3, 2)})))

print("ALL OK" if ok else "SOME FAILED")
