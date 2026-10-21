# R40 (reviewer): independent symbolic check of formulas (2.4), (5.1)-(5.7) of
# notes/prover/2026-10-21-morse-bott-mult.md  [Experiment, not a proof].
#
# Part A: frame calculus with GENERIC k_g(theta) and GENERIC eta_0(s,theta)
#         (sympy Functions), vectors stored as components in the Darboux frame
#         (omega, ell, n) with  omega' = ell, ell' = -omega + k_g n, n' = -k_g ell.
# Part B: concrete curve in R^3 (loxodrome on S^2, natural parameter, NON-constant k_g),
#         concrete eta_0 = s*y0(s^(1/3),theta); Y is built in R^3 from Psi by direct
#         differentiation (no frame rules), D_w Y via the Jacobian chain rule;
#         compared numerically (mpmath, 40 digits) with the frame formulas (5.2)-(5.6).
import sympy as sp
import mpmath as mp
import random

s, th, ze, kap, lam, beta, c, a0 = sp.symbols('s theta zeta kappa lambda beta c a0', real=True)
N = sp.Symbol('N', positive=True)
wo, wl, wn = sp.symbols('w_o w_l w_n', real=True)
kg = sp.Function('k')(th)
eta0 = sp.Function('eta0')(s, th)

def dth(V):
    a, b, cc = V
    return (sp.diff(a, th) - b, sp.diff(b, th) + a - kg*cc, sp.diff(cc, th) + kg*b)

def dcomp(V, x):
    return tuple(sp.diff(v, x) for v in V)

def add(*Vs):
    return tuple(sp.simplify(sum(v[i] for v in Vs)) for i in range(3))

def mul(f, V):
    return tuple(f*v for v in V)

def dot(U, V):
    return sum(U[i]*V[i] for i in range(3))

ok_all = True
def check(name, expr):
    global ok_all
    r = sp.simplify(sp.expand(expr))
    ok = (r == 0)
    ok_all &= ok
    print(f"{name:55s} {'OK' if ok else 'FAIL: ' + str(r)}")

# Psi = s*omega + (eta0+zeta) n
Psi = (s, sp.Integer(0), eta0 + ze)
Ps = dcomp(Psi, s)
Pt = dth(Psi)
Pz = dcomp(Psi, ze)
eta = eta0 + ze
eps = kg*eta/s
e0s, e0t = sp.diff(eta0, s), sp.diff(eta0, th)
check("(5.1) Psi_s", dot((1,0,0),Ps)-1 + (Ps[1])**2 + (Ps[2]-e0s)**2)
check("(5.1) Psi_theta", Pt[0]**2 + (Pt[1]-s*(1-eps))**2 + (Pt[2]-e0t)**2)
check("(5.1) Psi_zeta", Pz[0]**2 + Pz[1]**2 + (Pz[2]-1)**2)

# field (2.4)
Ys, Yt, Yz = sp.Integer(1), -kap*th/s, lam*ze/s
Y = add(mul(Ys, Ps), mul(Yt, Pt), mul(Yz, Pz))
nu = e0s - kap*th*e0t/s
nut = nu + lam*ze/s
check("(5.2) Y omega-comp", Y[0]-1)
check("(5.2) Y ell-comp", Y[1]+kap*th*(1-eps))
check("(5.2) Y n-comp", Y[2]-nut)
h = dot(Y, Y)
check("(5.2) h", h-(1+kap**2*th**2*(1-eps)**2+nut**2))

# derivatives (5.3)
dYt = dth(Y); dYs = dcomp(Y, s); dYz = dcomp(Y, ze)
eps_t = sp.diff(eps, th); eps_s = sp.diff(eps, s)
nut_t = sp.diff(nut, th); nut_s = sp.diff(nut, s)
f53t = (kap*th*(1-eps), 1-kap*(1-eps)+kap*th*eps_t-nut*kg - (lam*ze/s)*kg,
        -kap*th*(1-eps)*kg+nut_t)
# NB: in (5.3) the ell-coefficient is written with nu~ (tilde): -nu~ k_g
f53t_tilde = (kap*th*(1-eps), 1-kap*(1-eps)+kap*th*eps_t-nut*kg + 0, -kap*th*(1-eps)*kg+nut_t)
for i, nm in enumerate("o l n".split()):
    check(f"(5.3) d_theta Y [{nm}] (with nu~)", dYt[i]-f53t_tilde[i])
f53s = (0, kap*th*eps_s, nut_s)
f53z = (0, kap*th*kg/s, lam/s)
for i, nm in enumerate("o l n".split()):
    check(f"(5.3) d_s Y [{nm}]", dYs[i]-f53s[i])
    check(f"(5.3) d_zeta Y [{nm}]", dYz[i]-f53z[i])

# (5.4)  s D_Y Y
DYY = add(mul(Ys, dYs), mul(Yt, dYt), mul(Yz, dYz))
f54 = (-kap**2*th**2*(1-eps),
       kap*th*(s*eps_s-1+kap*(1-eps)-kap*th*eps_t+nut*kg+lam*kg*ze/s),
       s*nut_s+kap**2*th**2*(1-eps)*kg-kap*th*nut_t+lam**2*ze/s)
for i, nm in enumerate("o l n".split()):
    check(f"(5.4) s D_Y Y [{nm}]", s*DYY[i]-f54[i])
# negative control: drop lambda-terms from (5.4)
f54bad = (f54[0], kap*th*(s*eps_s-1+kap*(1-eps)-kap*th*eps_t+nut*kg),
          s*nut_s+kap**2*th**2*(1-eps)*kg-kap*th*nut_t)
r = sp.simplify(sp.expand(s*DYY[1]-f54bad[1])) != 0 and sp.simplify(sp.expand(s*DYY[2]-f54bad[2])) != 0
print(f"{'(5.4) negative control (lambda terms removed) fails':55s} {'OK' if r else 'UNEXPECTED'}")

# decomposition of w
as_ = wo
at_ = wl/(s*(1-eps))
az_ = wn - wo*e0s - wl*e0t/(s*(1-eps))
wrec = add(mul(as_, Ps), mul(at_, Pt), mul(az_, Pz))
check("decomp w: omega", wrec[0]-wo); check("decomp w: ell", wrec[1]-wl); check("decomp w: n", wrec[2]-wn)
DwY = add(mul(as_, dYs), mul(at_, dYt), mul(az_, dYz))
lhs55 = s*dot((wo, wl, wn), DwY)
rhs55 = ((1/(1-eps)-kap)*wl**2 + kap*th*wo*wl
         + ((kap*th*eps_t-nut*kg)*wl**2 + nut_t*wl*wn)/(1-eps)
         + wo*(kap*th*s*eps_s*wl + s*nut_s*wn)
         - kap*th*kg*wl*(wo*e0s + wl*e0t/(s*(1-eps)))
         + lam*az_*wn)
check("(5.5) s<w, D_w Y>", lhs55-rhs55)
rhs55bad = rhs55 - lam*az_*wn
print(f"{'(5.5) negative control (lambda a^zeta w_n removed) fails':55s} "
      f"{'OK' if sp.simplify(sp.expand(lhs55-rhs55bad))!=0 else 'UNEXPECTED'}")
# (5.6)
check("(5.6) <w,Y> with w_o substituted", dot((kap*th*(1-eps)*wl-nut*wn, wl, wn), Y))

# auxiliary identities
check("aux s eps_s = k eta0_s - eps", s*eps_s-(kg*e0s-eps))
check("aux eps_theta", eps_t-(sp.diff(kg, th)*eta+kg*e0t)/s)
check("aux nu~_theta", nut_t-(sp.diff(eta0, s, th)-kap*e0t/s-kap*th*sp.diff(eta0, th, 2)/s))
check("aux s nu~_s", s*nut_s-(s*sp.diff(eta0, s, 2)-kap*th*(sp.diff(eta0, s, th)-e0t/s)-lam*ze/s))

# (5.7): Euler identity with generic F~
sig, e = sp.symbols('sigma e', positive=True)
F = sp.Function('F')
g = s**beta*(F(s**(1/N), th, ze*s**(-c)) + a0)
Yg = sp.diff(g, s) + Yt*sp.diff(g, th) + Yz*sp.diff(g, ze)
lhs57 = beta*g - s*Yg    # beta*W - rho*Y W  with W o Psi = g, rho = s
c2 = c - lam
# derivatives of F at the point (sigma, theta, e)
X = (s**(1/N), th, ze*s**(-c))
Fs = sp.Subs(sp.Derivative(F(sig, th, e), sig), (sig, th, e), X).doit()
Ft = sp.Subs(sp.Derivative(F(sig, th, e), th), (sig, th, e), X).doit()
Fe = sp.Subs(sp.Derivative(F(sig, th, e), e), (sig, th, e), X).doit()
rhs57 = s**beta*(kap*th*Ft + c2*(ze*s**(-c))*Fe - (s**(1/N)/N)*Fs)
d = sp.simplify(sp.expand(lhs57 - rhs57))
print(f"{'(5.7) beta W - rho Y W':55s} {'OK' if d == 0 else 'check numerically: ' + str(d)[:200]}")
if d != 0:
    # numeric check with a concrete F
    Fc = lambda a, b, cc: sp.sin(a)*sp.exp(b*cc)+a**2*cc**3+b**2
    gg = s**beta*(Fc(s**(1/N), th, ze*s**(-c)) + a0)
    l = beta*gg - s*(sp.diff(gg, s)+Yt*sp.diff(gg, th)+Yz*sp.diff(gg, ze))
    A, B, C = sp.symbols('A B C')
    FF = Fc(A, B, C)
    rr = s**beta*(kap*th*sp.diff(FF, B)+c2*C*sp.diff(FF, C)-(A/N)*sp.diff(FF, A)).subs({A: s**(1/N), B: th, C: ze*s**(-c)})
    vals = {s: sp.Rational(3, 10), th: sp.Rational(1, 7), ze: sp.Rational(1, 50), kap: sp.Rational(1, 9),
            lam: sp.Rational(2, 3), beta: sp.Rational(13, 2), c: sp.Rational(5, 4), a0: 2, N: 3}
    print("   numeric (5.7) diff:", sp.N((l-rr).subs(vals), 30))

print("Part A all OK:", ok_all)

# ---------------- Part B: concrete loxodrome in R^3 ----------------
mp.mp.dps = 40
bb = sp.Rational(1, 3)          # loxodrome angle parameter (sin(beta_l) = 1/3)
sb = bb; cb = sp.sqrt(1-sb**2)
phi = th*sb
lon = (cb/sb)*sp.atanh(sp.sin(phi))
om = sp.Matrix([sp.cos(phi)*sp.cos(lon), sp.cos(phi)*sp.sin(lon), sp.sin(phi)])
ell = om.diff(th)
nn = om.cross(ell)
kgx = sp.simplify(ell.diff(th).dot(nn))
y0 = lambda sg, t: sg**2*(sp.Rational(1, 2)+t) + sg**3*t**2 - sg**4/5
Nn = 3
eta0x = s*y0(s**sp.Rational(1, Nn), th)
Psix = s*om + (eta0x+ze)*nn
PSs, PSt, PSz = Psix.diff(s), Psix.diff(th), Psix.diff(ze)
Yx = PSs - (kap*th/s)*PSt + (lam*ze/s)*PSz
J = Yx.jacobian([s, th, ze])
DPsi = Psix.jacobian([s, th, ze])
fl = lambda ex: sp.lambdify((s, th, ze, kap, lam), ex, 'mpmath')
Yf, Jf, DPf = fl(Yx), fl(J), fl(DPsi)
omf, ellf, nnf, kgf = fl(om), fl(ell), fl(nn), fl(kgx)
# frame formulas, with generic objects replaced by the concrete ones
subsd = {kg: kgx, eta0: eta0x}
def concrete(ex):
    return fl(ex.subs(subsd).doit())
f52 = [concrete(sp.Integer(1)), concrete(-kap*th*(1-eps)), concrete(nut)]
f54c = [concrete(x) for x in f54]
lhs55f = concrete(rhs55)   # function of (s,th,ze,kap,lam) but needs w; build separately
rhs55c = sp.lambdify((s, th, ze, kap, lam, wo, wl, wn), rhs55.subs(subsd).doit(), 'mpmath')
random.seed(40)
maxerr = mp.mpf(0)
for trial in range(6):
    S = mp.mpf(random.uniform(0.01, 0.2)); T = mp.mpf(random.uniform(-0.8, 0.8))
    Z = mp.mpf(random.uniform(-1, 1))*S**mp.mpf(1.4)
    K = mp.mpf(random.uniform(0.05, 0.5)); L = mp.mpf(random.uniform(0, 1.5))
    O, Lv, Nv = omf(S, T, Z, K, L), ellf(S, T, Z, K, L), nnf(S, T, Z, K, L)
    O, Lv, Nv = [mp.matrix(x) for x in (O, Lv, Nv)]
    Yv = mp.matrix(Yf(S, T, Z, K, L))
    # (5.2) components
    comps = [mp.fdot(Yv, O), mp.fdot(Yv, Lv), mp.fdot(Yv, Nv)]
    for i in range(3):
        maxerr = max(maxerr, abs(comps[i]-f52[i](S, T, Z, K, L)))
    # D_Y Y in R^3: J * DPsi^{-1} * Y
    Jm = mp.matrix(Jf(S, T, Z, K, L)); Dm = mp.matrix(DPf(S, T, Z, K, L))
    Dinv = mp.inverse(Dm)
    DYYv = Jm*(Dinv*Yv)
    c54 = [S*mp.fdot(DYYv, O), S*mp.fdot(DYYv, Lv), S*mp.fdot(DYYv, Nv)]
    for i in range(3):
        maxerr = max(maxerr, abs(c54[i]-f54c[i](S, T, Z, K, L)))
    # random w
    W = [mp.mpf(random.uniform(-1, 1)) for _ in range(3)]
    wv = W[0]*O + W[1]*Lv + W[2]*Nv
    DwY = Jm*(Dinv*wv)
    l55 = S*mp.fdot(wv, DwY)
    maxerr = max(maxerr, abs(l55 - rhs55c(S, T, Z, K, L, *W)))
print("Part B (loxodrome, R^3 Jacobian vs frame formulas (5.2),(5.4),(5.5)): max |diff| =", mp.nstr(maxerr, 5))
print("k_g of the loxodrome (non-constant):", sp.simplify(kgx))
