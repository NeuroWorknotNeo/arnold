# R50: проверка констант (5.2)-(5.4) доказательства теоремы MT (results/015-master.md, §7, п. 6)
# и формулы (MT3a). [Эксперимент]: символьно (sympy) и случайной выборкой параметров.
import random
import sympy as sp
import numpy as np

# --- 1. Символьно: Gamma теоремы H при h0=Lambda^-2, h1=4Lambda^2, gamma1=Lambda^3 C_P K0 kappa,
#        gamma2=C_psi kappa равно C_Gamma*kappa, формула (5.3).
L, CP, K0, kap, a0, beta, Cpsi = sp.symbols('Lambda C_P K_0 kappa a_0 beta C_psi', positive=True)
h0 = L**-2; h1 = 4*L**2
g1 = L**3*CP*K0*kap; g2 = Cpsi*kap
Gamma = sp.sqrt(2*a0)*(sp.Rational(3, 2)*beta*sp.sqrt(h1)*g1 + sp.sqrt(2/h0)*g2)
CGamma = sp.sqrt(2*a0)*(3*beta*L**4*CP*K0 + sp.sqrt(2)*L*Cpsi)
print('(5.3) Gamma - C_Gamma*kappa =', sp.simplify(Gamma - CGamma*kap))

# условие 4 sqrt(delta) gamma1 <= 1/2 sqrt(a0/h1)  <=>  kappa <= sqrt(a0)/(16 L^4 C_P K0 sqrt(delta))
dl = sp.symbols('delta', positive=True)
lhs = 4*sp.sqrt(dl)*g1; rhs = sp.Rational(1, 2)*sp.sqrt(a0/h1)
kap_star = sp.sqrt(a0)/(16*L**4*CP*K0*sp.sqrt(dl))
print('4 sqrt(d) g1 at kappa=kappa* minus rhs =', sp.simplify(lhs.subs(kap, kap_star) - rhs))

# --- 2. Случайная выборка: m3 <= m0 + C3 kappa (5.2) и три условия (M) при kappa = kappa* (5.4)
random.seed(1)
bad = 0
worst = {'m3': -1e9, 'cond1': 1e9, 'cond2': -1e9, 'cond3': -1e9}
for trial in range(200000):
    Lam = 1 + 3*random.random()
    Cp = 1 + 3*random.random()
    k0 = random.choice([0.0, 10**random.uniform(-3, 1)])
    k1 = 0.0 if k0 == 0 else 10**random.uniform(-2, 1)
    ks = 0.0 if k0 == 0 else 10**random.uniform(-2, 1)
    d2 = random.choice([0.0, 10**random.uniform(-2, 1)])
    Cv = 10**random.uniform(-1, 2)
    Bt = 10**random.uniform(np.log10(2), 1)
    mu1 = random.choice([0.0, Bt*random.random()*0.99])
    mu0 = random.choice([0.0, 10**random.uniform(-2, 1)]) if mu1 > 0 else 10**random.uniform(-2, 1)
    m0 = (Bt - mu1)/2*random.random()*0.99
    A0 = 10**random.uniform(-2, 1)
    dlt = A0/2*random.random()
    if dlt <= 0:
        continue
    CG = Cp**4*Lam**4
    Cps = Lam*Cp*(k0 + ks + k1*k0) + 2*d2*Cp**2*k0**2
    C3 = k1*CG*(1 + 3*Lam**4*Cp*k0) + 3*m0*Lam**4*Cp*k0 + 2*Lam**6*Cv*Cp*k0 + Lam*d2*Cp*k0
    CGam = np.sqrt(2*A0)*(3*Bt*Lam**4*Cp*k0 + np.sqrt(2)*Lam*Cps)
    b0 = Bt - mu1 - 2*m0
    inf = float('inf')
    def fr(a, b):
        return inf if b == 0 else a/b
    ks_list = [1, fr(1, 2*Cp*k0), fr(1, Lam**4*Cp*k0), fr(b0, 2*(mu0 + 2*C3)),
               fr(np.sqrt(A0), 16*Lam**4*Cp*k0*np.sqrt(dlt)),
               max(fr(mu0*b0*dlt, 2*CGam**2), fr(np.sqrt(mu1*b0*dlt/2), CGam))]
    kst = min(ks_list)
    for kappa in [kst, kst*random.random()]:
        gT = Lam*Cp*k0*kappa; gv = d2*Cp*k0*kappa
        m = m0 + kappa*k1*CG
        m3 = m*(1 + Lam**3*gT)**2 + 2*Lam**5*Cv*gT + Lam*gv
        mu = mu1 + kappa*mu0
        G1 = Lam**2*gT; G2 = Cps*kappa
        Gam = np.sqrt(2*A0)*(1.5*Bt*np.sqrt(4*Lam**2)*G1 + np.sqrt(2*Lam**2)*G2)
        e1 = m3 - (m0 + C3*kappa)                      # должно быть <= 0
        c1 = Bt - mu - 2*m3                            # должно быть > 0
        c2 = Gam**2/(4*c1*dlt) - mu/4 if c1 > 0 else inf   # <= 0
        c3 = 4*np.sqrt(dlt)*G1 - 0.5*np.sqrt(A0/(4*Lam**2))  # <= 0
        worst['m3'] = max(worst['m3'], e1/(1 + abs(m3)))
        worst['cond1'] = min(worst['cond1'], c1/Bt)
        worst['cond2'] = max(worst['cond2'], c2/(mu + 1e-300))
        worst['cond3'] = max(worst['cond3'], c3/np.sqrt(A0))
        if e1 > 1e-12*(1 + abs(m3)) or c1 <= 0 or c2 > 1e-12*mu or c3 > 1e-12 or mu >= Bt or mu <= 0:
            bad += 1
print('random trials: violations =', bad)
print('worst normalized margins:', worst)

# --- 3. (MT3a): e(s) = ||G~ - I|| ||G~^{-1}|| (||N0|| + m0) даёт t^T G~ N0 t >= -(m0+e) t^T G~ t,
#        если t^T N0 t >= -m0 |t|^2.
rng = np.random.default_rng(2)
viol = 0
for trial in range(20000):
    k = rng.integers(2, 6)
    # блочно-диагональная N0 с sym >= -m0
    m0 = rng.uniform(0, 2)
    M = rng.normal(size=(k, k))
    S = (M + M.T)/2
    lam_min = np.linalg.eigvalsh(S).min()
    N0 = M - (lam_min + m0)*np.eye(k)*rng.uniform(0.0, 1.0)  # sym N0 >= ? проверим явно
    if np.linalg.eigvalsh((N0 + N0.T)/2).min() < -m0:
        N0 = N0 + (-m0 - np.linalg.eigvalsh((N0 + N0.T)/2).min())*np.eye(k)
    E = rng.normal(size=(k, k))*rng.uniform(0, 0.3)
    Gt = np.eye(k) + (E + E.T)/2
    if np.linalg.eigvalsh(Gt).min() <= 0.05:
        continue
    e = np.linalg.norm(Gt - np.eye(k), 2)*np.linalg.norm(np.linalg.inv(Gt), 2)*(np.linalg.norm(N0, 2) + m0)
    # min над t формы t^T (G N0 + (m0+e) G) t
    Form = Gt @ N0 + (m0 + e)*Gt
    if np.linalg.eigvalsh((Form + Form.T)/2).min() < -1e-10:
        viol += 1
print('(MT3a) random matrices: violations =', viol)
