"""R44: (1) тождество (5.1) теоремы D; (2) уточнённые данные теоремы Z, п. 4 (проверка (0.6));
(3) неравенства (W2) в W', п. 1 и в Z, п. 4 (случай W) -- случайная проверка на модельных профилях."""
import sympy as sp, random, math

t, b1, b2, beta, c = sp.symbols('t b1 b2 beta c', positive=True)
th = sp.Symbol('theta', real=True)
Phi_hat = sp.Function('Phihat')
H = [sp.Function('H%d' % l) for l in range(1, 8)]
M = sp.Function('M')
ok = True
for (Nn, NV, AV, GV, rp) in [(3, 2, 1, 4, 2), (4, 3, 2, 6, 3), (1, 2, 3, 2, 1), (2, 2, 1, 12, 3)]:
    assert GV % (2*rp) == 0
    B = sp.Rational(GV, 2*rp)
    x = t**(Nn*NV)
    gam = sp.Rational(GV, Nn*NV)
    cp = c + gam/(2*rp)
    e = sp.simplify((x**cp*b2)*x**(-c))          # zeta = x^{c'} b2, e = zeta x^{-c}
    assert sp.simplify(e - t**B*b2) == 0
    lhs = x**beta*(t**GV*Phi_hat(t, b1) + sum(H[l-1](t, b1)*e**l for l in range(1, 2*rp))
                   + e**(2*rp)*M(t, b1, e))
    rhs = x**(beta+gam)*(Phi_hat(t, b1) + sum(t**(l*B-GV)*H[l-1](t, b1)*b2**l for l in range(1, 2*rp))
                         + b2**(2*rp)*M(t, b1, t**B*b2))
    r = sp.simplify(sp.powsimp(sp.expand(lhs - rhs), force=True))
    ok = ok and (r == 0)
print('(1) identity (5.1):', ok)

# (2) refinement step of theorem Z
s = sp.Symbol('s', positive=True)
j, ep = sp.symbols('j eprime', real=True)
epsg = sp.Function('epsg'); Gp = sp.Function('Gp'); Mg = sp.Function('Mg')
ok = True
for (Nn, gnum, rg, kp) in [(2, 1, 2, 3), (1, 1, 1, 2), (3, 2, 3, 1), (4, 3, 2, 5)]:
    gs = sp.Rational(gnum, Nn)            # gamma_* with N*gamma_* = gnum integer
    cc = 1 + gs
    sig = s**sp.Rational(1, Nn)
    vs = sig**sp.Rational(1, 2*rg)          # varsigma
    Np = 2*rg*Nn
    cp = cc + sp.Rational(kp, Np)
    betap = j + sp.Rational(kp, Nn)
    y0p = lambda v, T: v**(2*rg*Nn*gs)*epsg(v**(2*rg), T)
    # normal displacement in the refined chart
    disp = s*y0p(s**sp.Rational(1, Np), th) + s**cp*ep
    # it must equal s^c (eps_g^* + varsigma^{kappa'} e')
    eps_arg = sp.simplify(disp/s**cc)
    target = epsg(sig, th) + vs**kp*ep
    ok = ok and sp.simplify(sp.powsimp(eps_arg - target, force=True)) == 0
    # U = s^j Utilde(sigma, th, eps_arg),  Utilde(sigma,th,eps_g+e) = sigma^k' Gp + e^{2rg} Mg(sigma,th,e)
    e_ = vs**kp*ep
    U = s**j*(sig**kp*Gp(sig, th) + e_**(2*rg)*Mg(sig, th, e_))
    Ftp = Gp(vs**(2*rg), th) + ep**(2*rg)*Mg(vs**(2*rg), th, vs**kp*ep)
    r = sp.simplify(sp.powsimp(sp.expand(U - s**betap*Ftp.subs({}) ), force=True))
    ok = ok and r == 0
print('(2) refined data (0.6) in theorem Z, p.4:', ok)

# (3) W2 in W', p.1: kappa tau dLambda + c e dP >= kappa P on small square, random model profiles
random.seed(1)
worst = 1e9
for trial in range(300):
    p = random.choice([1, 2, 3]); rp = random.choice([1, 2, 3]); a = random.uniform(0.1, 3)
    cw = random.uniform(1.0001, 3); kap = random.uniform(1e-4, 0.5)
    a1, a2, a3 = [random.uniform(-1, 1) for _ in range(3)]
    p0 = random.uniform(0.2, 2); q1, q2 = random.uniform(-1, 1), random.uniform(-1, 1)
    Lam = lambda T: a*T**(2*p)*(1 + a1*T + a2*T**2)
    dLam = lambda T: a*(2*p*T**(2*p-1)*(1 + a1*T + a2*T**2) + T**(2*p)*(a1 + 2*a2*T))
    pp = lambda T, E: p0 + q1*T + q2*E
    # window where tau Lam' >= Lam, |e dp| <= p/4, |tau dp| <= p
    r = 0.05
    for _ in range(200):
        T = random.uniform(-r, r); E = random.uniform(-r, r)
        if T*dLam(T) < Lam(T) or abs(E*q2) > pp(T, E)/4 or abs(T*q1) > pp(T, E): continue
        P = Lam(T) + E**(2*rp)*pp(T, E)
        lhs = kap*T*(dLam(T) + E**(2*rp)*q1) + cw*E*(2*rp*E**(2*rp-1)*pp(T, E) + E**(2*rp)*q2)
        if P > 0: worst = min(worst, lhs/(kap*P))
print('(3) min over samples of [kappa tau P_tau + c e P_e]/(kappa P) (must be >=1):', worst)
