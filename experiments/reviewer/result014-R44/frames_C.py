"""R44: проверка формул, на которые опирается теорема C (§4 results/014):
(a) s<w,D_wY> при Y=Psi_s (kappa=lambda=0) -- формула §4, п. 6;
(b) общая формула (3.5) при произвольных kappa, lambda (контроль);
(c) тождество Эйлера (3.7).
Векторы -- тройки коэффициентов в репере (omega, l, n), d/dtheta по (0.1)."""
import sympy as sp

s, th, ze, kap, lam, c, N, beta, a0 = sp.symbols('s theta zeta kappa lambda c N beta a0', real=True)
kg = sp.Function('k_g')(th)
eta0 = sp.Function('eta0')(s, th)

def dth(v):
    a, b, cc = v
    return (sp.diff(a, th) - b, sp.diff(b, th) + a - cc*kg, sp.diff(cc, th) + b*kg)

def dvar(v, var):
    if var == th:
        return dth(v)
    return tuple(sp.diff(x, var) for x in v)

eta = eta0 + ze
Psi = (s, 0, eta)
Ps = dvar(Psi, s); Pt = dvar(Psi, th); Pz = dvar(Psi, ze)
eps = kg*eta/s
assert sp.simplify(Pt[1] - s*(1-eps)) == 0

def dot(u, v):
    return sum(x*y for x, y in zip(u, v))

wo, wl, wn = sp.symbols('w_o w_l w_n', real=True)

def check(kv, lv):
    # Y = Psi_s - kappa*theta/s Psi_theta + lambda*zeta/s Psi_zeta (as vector field in (s,theta,zeta))
    Yc = (1, -kv*th/s, lv*ze/s)          # coordinate components
    Yv = tuple(Yc[0]*Ps[i] + Yc[1]*Pt[i] + Yc[2]*Pz[i] for i in range(3))
    # D_w Y where w = a^s Psi_s + a^th Psi_th + a^z Psi_z :  sum a^j d_j (Y o Psi)
    as_ = wo
    ath = wl/(s*(1-eps))
    az = wn - wo*sp.diff(eta0, s) - wl*sp.diff(eta0, th)/(s*(1-eps))
    w_rec = tuple(as_*Ps[i] + ath*Pt[i] + az*Pz[i] for i in range(3))
    assert all(sp.simplify(w_rec[i] - (wo, wl, wn)[i]) == 0 for i in range(3))
    DwY = tuple(as_*dvar(Yv, s)[i] + ath*dvar(Yv, th)[i] + az*dvar(Yv, ze)[i] for i in range(3))
    return sp.simplify(s*dot((wo, wl, wn), DwY)), az

# (a) kappa = lambda = 0
val, az = check(0, 0)
e0s = sp.diff(eta0, s); e0ss = sp.diff(eta0, s, 2); e0st = sp.diff(eta0, s, th)
formula_C = ((1 - e0s*kg)*wl**2 + e0st*wl*wn)/(1-eps) + s*e0ss*wo*wn
print('(a) theorem C, s<w,D_wY>:', sp.simplify(val - formula_C) == 0)

# (b) general (3.5)
val, az = check(kap, lam)
nu = sp.diff(eta0, s) - kap*th*sp.diff(eta0, th)/s
nut = nu + lam*ze/s
e0t = sp.diff(eta0, th)
f35 = (1/(1-eps) - kap)*wl**2 + kap*th*wo*wl \
    + ((kap*th*sp.diff(eps, th) - nut*kg)*wl**2 + sp.diff(nut, th)*wl*wn)/(1-eps) \
    + wo*(kap*th*s*sp.diff(eps, s)*wl + s*sp.diff(nut, s)*wn) \
    - kap*th*kg*wl*(wo*e0s + wl*e0t/(s*(1-eps))) + lam*az*wn
print('(b) general (3.5):', sp.simplify(sp.expand(val - f35)) == 0)

# (c) Euler identity (3.7):  beta W - rho Y W = s^beta [k th F_th + c2 e F_e - sigma/N F_sigma], c2 = c - lambda
F = sp.Function('F')
sig = sp.Symbol('sigma', positive=True)
e = sp.Symbol('e', real=True)
g = s**beta*(F(s**(1/N), th, ze*s**(-c)) + a0)
Yg = sp.diff(g, s) - kap*th/s*sp.diff(g, th) + lam*ze/s*sp.diff(g, ze)
lhs = beta*g - s*Yg
Fs = lambda var: sp.Derivative(F(sig, th, e), var)
rhs = s**beta*(kap*th*sp.diff(F(sig, th, e), th) + (c - lam)*e*sp.diff(F(sig, th, e), e) - sig/N*sp.diff(F(sig, th, e), sig))
rhs = rhs.subs({sig: s**(1/N), e: ze*s**(-c)}).doit()
print('(c) Euler (3.7):', sp.simplify(sp.expand(lhs - rhs)) == 0)

# negative controls
rhs_bad = s**beta*(kap*th*sp.diff(F(sig, th, e), th) + c*e*sp.diff(F(sig, th, e), e) - sig/N*sp.diff(F(sig, th, e), sig))
rhs_bad = rhs_bad.subs({sig: s**(1/N), e: ze*s**(-c)}).doit()
print('(c-) control with c2=c (must be False when lambda!=0):', sp.simplify(sp.expand(lhs - rhs_bad)) == 0)
val, az = check(0, 0)
bad = ((1 + e0s*kg)*wl**2 + e0st*wl*wn)/(1-eps) + s*e0ss*wo*wn
print('(a-) control with wrong sign (must be False):', sp.simplify(val - bad) == 0)
