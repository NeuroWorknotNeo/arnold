"""R35: algebra of the constants in Theorem 2'' (§6) and Theorem N (§8) of results/011,
plus numeric checks of (V'') for M1, M2.  [Experiment]"""
import sympy as sp
import mpmath as mp

a0, lam, beta, mu, C1, d, ka, kb = sp.symbols('a0 lambda0 beta mu C1 delta kappa kbar', positive=True)
h0, h1 = sp.Rational(1, 2), sp.Rational(3, 2)
a1 = a3 = a0
a2 = beta * a0
L1 = 2 * (a2 + beta * a1 / 2) * sp.sqrt(h1 / a1)
L2 = 2 * sp.sqrt(2 * a3 / h0)
print('L1 - 3 beta sqrt(3a0/2):', sp.simplify(L1 - 3 * beta * sp.sqrt(3 * a0 / 2)))
print('L2 - 4 sqrt(a0):', sp.simplify(L2 - 4 * sp.sqrt(a0)))
theta2_d = 2 * C1 * d / lam
theta3_d = C1 * sp.sqrt(2 * d / lam)
expr = L2 * theta2_d / sp.sqrt(d) + 4 * theta3_d
print('delta-terms - C1 sqrt(d)(8sqrt(a0)/lam + 4sqrt2/sqrt(lam)):',
      sp.simplify(expr - C1 * sp.sqrt(d) * (8 * sp.sqrt(a0) / lam + 4 * sp.sqrt(2) / sp.sqrt(lam))))
# Gamma' <= Gamma_*
g1, g2 = sp.symbols('gamma1 gamma2', positive=True)
Gp = sp.sqrt(2) * ((a2 + beta * d) * sp.sqrt(h1 / a1) * g1 / sp.sqrt(lam) + sp.sqrt(2 * a3 / h0) * g2 / sp.sqrt(lam))
Gs = sp.sqrt(a0 / lam) * (sp.Rational(3, 2) * sp.sqrt(3) * beta * g1 + 2 * sp.sqrt(2) * g2)
print("Gamma'(delta=a0/2) - Gamma_*:", sp.simplify(Gp.subs(d, a0 / 2) - Gs), "(Gamma' increasing in delta)")
# bracket
print('bracket:', sp.Rational(1, 2) * mu * sp.Rational(3, 4) - mu / 16 - mu / 8 - mu / 16)
# Gamma_* for theorem N and (0.4)
GsN = Gs.subs({g1: sp.Rational(5, 4) * ka, g2: ka * (1 - ka)})
bound = ka * sp.sqrt(a0 / lam) * (sp.Rational(15, 8) * sp.sqrt(3) * beta + 2 * sp.sqrt(2))
print('bound - Gamma_*  (should be kappa^2*...>=0):', sp.factor(sp.simplify(bound - GsN)))
kmax = beta * lam / (a0 * (sp.Rational(15, 8) * sp.sqrt(3) * beta + 2 * sp.sqrt(2))**2)
print('bound^2 at kappa=kmax  - beta*kmax:', sp.simplify((bound**2 - beta * ka).subs(ka, kmax)))
# h bound
print('h max:', 1 + sp.Rational(1, 4) * sp.Rational(1, 16) * sp.Rational(25, 16) + sp.Rational(1, 16), '< 3/2')
# (Phi3''): (11/3) k kb + 5/16 k^2 <= C1 = 5/4 k^2 (1+kb) + 4 k kb
C1N = sp.Rational(5, 4) * ka**2 * (1 + kb) + 4 * ka * kb
print('C1 - (11/3 k kb + 5/16 k^2):', sp.expand(C1N - (sp.Rational(11, 3) * ka * kb + sp.Rational(5, 16) * ka**2)))
# |w_omega| <= |w|: 5/4*1/2*1/4 + 1/4
print('5/4*k*r0 + 1/4 at k=1/2,r0=1/4:', sp.Rational(5, 4) * sp.Rational(1, 2) * sp.Rational(1, 4) + sp.Rational(1, 4))
# 2 - 2/sqrt(1+t^2) <= t^2
t = sp.symbols('t', real=True)
uu = sp.symbols('u', positive=True)
print('u^3-3u+2 factor:', sp.factor(uu**3 - 3 * uu + 2))
# x(t) asymptotics: d/dt x^{1-b/2} = (1-b/2) x^{-b/2} xdot
x = sp.Function('x')(sp.Symbol('t'))
print('d/dt x^(1-b/2):', sp.simplify(sp.diff(x**(1 - beta / 2), sp.Symbol('t'))))

# ---- numeric (V'') for M1 and M2 near omega* ----
mp.mp.dps = 20
def check(name, G, p, c, rp, r1, kap):
    G0 = G(0); G2 = mp.diff(G, 0, 2); lam0 = G2 / 4; p0 = p(0, 0)
    worstQ = mp.inf; worstE = mp.inf
    n = 60
    for i in range(-n, n + 1):
        for k in range(-n, n + 1):
            th = r1 * i / n; e = r1 * k / n
            if th * th + e * e >= r1 * r1:
                continue
            Q = G(th) - G0 + e**(2 * rp) * p(th, e)
            lb = lam0 * th**2 + p0 / 2 * abs(e)**(2 * rp)
            dQt = mp.diff(lambda tt: G(tt) - G0 + e**(2 * rp) * p(tt, e), th)
            dQe = mp.diff(lambda ee: ee**(2 * rp) * p(th, ee), e)
            E = kap * th * dQt + c * e * dQe - kap * Q
            worstQ = min(worstQ, Q - lb)
            worstE = min(worstE, E)
    print(f'{name}: r1={r1} min(Q - lower bound)={mp.nstr(worstQ,5)}  min(Euler - kappa Q)={mp.nstr(worstE,5)}')

# M1 at phi*=pi
G1 = lambda th: mp.cos(mp.pi + th)**5 + mp.sin(mp.pi + th)**5
check('M1 phi=pi', G1, lambda th, e: 1, mp.mpf(5) / 4, 2, mp.mpf(0.2), 0.0171)
G1b = lambda th: mp.cos(3 * mp.pi / 2 + th)**5 + mp.sin(3 * mp.pi / 2 + th)**5
check('M1 phi=3pi/2', G1b, lambda th, e: 1, mp.mpf(5) / 4, 2, mp.mpf(0.2), 0.0171)
# M2 at phi* and pi/2
f = lambda p_: mp.cos(p_)**4 + mp.cos(p_)**3 * mp.sin(p_) + mp.sin(p_)**4
t2 = mp.findroot(lambda q: 4 * q**3 - 3 * q**2 - 4 * q + 1, 0.2236)
for nm, ph0, kap in [('M2 phi*', mp.atan(t2), 0.0177), ('M2 pi/2', mp.pi / 2, 0.0175)]:
    e0 = lambda th, ph0=ph0: -(f(ph0 + th) / 4)**(mp.mpf(1) / 3)
    G = lambda th, ph0=ph0: -3 * mp.mpf(4)**(-mp.mpf(4) / 3) * f(ph0 + th)**(mp.mpf(4) / 3)
    p = lambda th, e, e0=e0: (e + 2 * e0(th))**2 + 2 * e0(th)**2
    check(nm, G, p, mp.mpf(4) / 3, 1, mp.mpf(0.1), kap)
