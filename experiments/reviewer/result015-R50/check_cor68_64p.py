# R50: проверки к следствиям 6.8, 6.4', 6.2 (results/015-master.md, §9). [Эксперимент]
import numpy as np
import sympy as sp

th, e, kap, c, r = sp.symbols('theta e kappa c r', real=True)
G = sp.Function('G')(th)
p = sp.Function('p')(th, e)
Q = G - G.subs(th, 0) + e**(2*r)*p
lhs = kap*th*sp.diff(Q, th) + c*e*sp.diff(Q, e) - kap*Q
rhs = kap*(th*sp.diff(G, th) - (G - G.subs(th, 0))) + e**(2*r)*((2*r*c - kap)*p + c*e*sp.diff(p, e)
                                                              + kap*th*sp.diff(p, th))
print('6.8, п. 1, тождество:', sp.simplify(sp.expand(lhs - rhs)))

# 6.8: (G_deg) для G - G(0) = a th^{2q}(1+O(th)): th G' - (G-G(0)) = (2q-1) a th^{2q}(1+O(th))
a, qq = sp.symbols('a q', positive=True)
for qv in [1, 2, 3]:
    Gx = -1 + a*th**(2*qv)*(1 + 3*th - th**2)
    print(f'q={qv}: th G\' - (G-G(0)) =', sp.factor(sp.expand(th*sp.diff(Gx, th) - (Gx + 1))))

# 6.8, п. 1: численно — неравенство kappa th Q_th + c e Q_e >= kappa Q на квадрате r3
rng = np.random.default_rng(5)
qv, rp, cv, lam0, p0 = 2, 2, 1.25, 1.0, 1.0
def Gf(t): return -1 + t**4 + 0.3*t**5
def Gp(t): return 4*t**3 + 1.5*t**4
def pf(t, ee): return p0 + 0.2*t + 0.3*ee + 0.1*t*ee
def pt(t, ee): return 0.2 + 0.1*ee
def pe(t, ee): return 0.3 + 0.1*t
r3 = 0.05
worst = np.inf
for _ in range(200000):
    t = rng.uniform(-r3, r3); ee = rng.uniform(-r3, r3); kv = rng.uniform(1e-4, 0.5)
    Qv = Gf(t) + 1 + ee**(2*rp)*pf(t, ee)
    Qt = Gp(t) + ee**(2*rp)*pt(t, ee)
    Qe = 2*rp*ee**(2*rp - 1)*pf(t, ee) + ee**(2*rp)*pe(t, ee)
    val = kv*t*Qt + cv*ee*Qe - kv*Qv
    worst = min(worst, val/(Qv + 1e-300))
print('6.8 пример (q=2, r\'=2, c=1.25): min (k th Q_th + c e Q_e - k Q)/Q на квадрате =', worst)

# 6.4': трубчатая калибровка, большой круг (k_g=0), y0=0, xi = (kappa theta, c2 e):
# I + D_theta v = diag(1-kappa, c - c2) (в координатах theta, y), то есть узкий блок N0 = c - c2.
s, thh, ee, kk, cc, c2 = sp.symbols('s theta e kappa c c2', positive=True)
yv = s**(cc - 1)*ee
# поток: s dtheta/ds = -kappa theta, s de/ds = -c2 e; v = s d/ds (theta, y)
v = sp.Matrix([-kk*thh, sp.diff(yv, s)*s + sp.diff(yv, ee)*(-c2*ee)])
# выразим v через (s, theta, y): e = y s^{1-c}
yy = sp.symbols('y', real=True)
v_th = sp.simplify(v.subs(ee, yy*s**(1 - cc)))
Dth = v_th.jacobian([thh, yy])
print("6.4': I + D_theta v =", sp.simplify(sp.eye(2) + Dth))

# 6.2: Gamma' = Gamma_* при h0 = 1/2, h1 = 3/2, gamma_i' = gamma_i/sqrt(lambda0)
a0, bt, g1, g2, l0 = sp.symbols('a0 beta gamma1 gamma2 lambda0', positive=True)
Gp_ = sp.sqrt(2*a0)*(sp.Rational(3, 2)*bt*sp.sqrt(sp.Rational(3, 2))*g1/sp.sqrt(l0) + sp.sqrt(2/sp.Rational(1, 2))*g2/sp.sqrt(l0))
Gs = sp.sqrt(a0/l0)*(3*sp.sqrt(3)/2*bt*g1 + 2*sp.sqrt(2)*g2)
print("6.2: Gamma' - Gamma_* =", sp.simplify(Gp_ - Gs))
# 6.2: L2 C1 Rb^2/sqrt(d) + 4 C1 Rb при Rb = 2 sqrt(d/l0), L2 = 4 sqrt(a0)
C1, d = sp.symbols('C1 delta', positive=True)
Rb = 2*sp.sqrt(d/l0)
print('6.2: остаток =', sp.simplify(4*sp.sqrt(a0)*C1*Rb**2/sp.sqrt(d) + 4*C1*Rb
                                     - C1*sp.sqrt(d)*(16*sp.sqrt(a0)/l0 + 8/sp.sqrt(l0))))
# 6.7: (3-e)(sqrt2-1)/2 + e <= 0.63 + e и 2 m < 6 - 2e при e in (0, 1/2]
for ev in np.linspace(1e-6, 0.5, 6):
    mv = (3 - ev)*(np.sqrt(2) - 1)/2 + ev
    print(f'6.7: e={ev:.3f}: m={mv:.4f}, m-0.63-e={mv-0.63-ev:.4f}, 6-2e-2m={6-2*ev-2*mv:.4f}')
