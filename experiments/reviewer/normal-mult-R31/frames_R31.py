# R31: independent symbolic check of (4.2)-(4.6) and Lemma N5 formulas
# of notes/prover/2026-10-21-normal-multiplicity.md.
# Darboux frame on S^2 is modelled abstractly: omega, ell, n are symbols with
# derivative rules (1.1); vectors are coefficient triples in (omega, ell, n).
import sympy as sp

s, th, zeta, x, u, kap = sp.symbols('s theta zeta x u kappa', real=True)
kg = sp.Function('k')(th)            # geodesic curvature k_g(theta)
eta0 = sp.Function('eta0')(s, th)    # general C^2 floor function

# vector = (a_omega, a_ell, a_n) functions of (s,theta,zeta)
def dtheta_vec(v, var_dep_theta=True):
    """derivative w.r.t. theta of a vector field v=(a,b,c) given in frame
    (omega,ell,n)(theta): d/dth (a w + b l + c n) = a' w + a l + b' l + b(-w+kg n) + c' n + c(-kg l)"""
    a, b, c = v
    return (sp.diff(a, th) - b,
            sp.diff(b, th) + a - kg*c,
            sp.diff(c, th) + kg*b)

def dplain(v, var):
    return tuple(sp.diff(comp, var) for comp in v)

def dot(v, w):
    return sum(vi*wi for vi, wi in zip(v, w))

# Psi(s,theta,zeta) = s*omega + (eta0+zeta)*n
Psi = (s, sp.Integer(0), eta0 + zeta)
eta = eta0 + zeta
eps = kg*eta/s
nu = sp.diff(eta0, s) - kap*th*sp.diff(eta0, th)/s

Psi_s = dplain(Psi, s)
Psi_th = dtheta_vec(Psi)
Psi_z = dplain(Psi, zeta)
chk = []
chk.append(('Psi_s', [sp.simplify(a-b) for a, b in zip(Psi_s, (1, 0, sp.diff(eta0, s)))]))
chk.append(('Psi_th', [sp.simplify(a-b) for a, b in zip(Psi_th, (0, s*(1-eps), sp.diff(eta0, th)))]))
chk.append(('Psi_z', [sp.simplify(a-b) for a, b in zip(Psi_z, (0, 0, 1))]))

# Map Phi(x,u,zeta) = Psi(x, u x^{-kappa}, zeta).  Total x-derivative at fixed (u,zeta):
# d/dx F(s=x, theta=u x^-k) = F_s + F_theta * (-k theta / x)
def Dx(v):
    """total derivative along x at fixed (u,zeta) of a frame-vector field depending on (s,theta,zeta)"""
    vs = dplain(v, s)
    vt = dtheta_vec(v)
    return tuple(a + b*(-kap*th/s) for a, b in zip(vs, vt))
def Dx_scalar(f):
    return sp.diff(f, s) + sp.diff(f, th)*(-kap*th/s)

Y = Dx(Psi)
Y_claim = (1, -kap*th*(1-eps), nu)
chk.append(('Y (4.3)', [sp.simplify(a-b) for a, b in zip(Y, Y_claim)]))
h = dot(Y, Y)
chk.append(('h (4.3)', [sp.simplify(h - (1 + kap**2*th**2*(1-eps)**2 + nu**2))]))

# (4.4): x * d^2/dx^2 Phi
YY = Dx(Y)
xdeps = s*Dx_scalar(eps)
xdnu = s*Dx_scalar(nu)
claim44 = (-kap**2*th**2*(1-eps),
           -kap*th*((1-kap) + kap*eps - xdeps - nu*kg),
           kap**2*th**2*(1-eps)*kg + xdnu)
chk.append(('x Phi_xx (4.4)', [sp.simplify(s*a - b) for a, b in zip(YY, claim44)]))
chk.append(('x d_x eps', [sp.simplify(xdeps - (-kap*th*sp.diff(kg, th)*eta/s + kg*nu - eps))]))
chk.append(('d eta/dx = nu', [sp.simplify(Dx_scalar(eta) - nu)]))

# (4.5): Y as field in (s,theta,zeta)
Yf = Y_claim
dthY = dtheta_vec(Yf)
dsY = dplain(Yf, s)
dzY = dplain(Yf, zeta)
claim_dth = (kap*th*(1-eps),
             1 - kap*(1-eps) + kap*th*sp.diff(eps, th) - nu*kg,
             -kap*th*(1-eps)*kg + sp.diff(nu, th))
claim_ds = (0, kap*th*sp.diff(eps, s), sp.diff(nu, s))
claim_dz = (0, kap*th*kg/s, 0)
chk.append(('d_theta Y (4.5)', [sp.simplify(a-b) for a, b in zip(dthY, claim_dth)]))
chk.append(('d_s Y (4.5)', [sp.simplify(a-b) for a, b in zip(dsY, claim_ds)]))
chk.append(('d_zeta Y (4.5)', [sp.simplify(a-b) for a, b in zip(dzY, claim_dz)]))
chk.append(('s d_s eps', [sp.simplify(s*sp.diff(eps, s) - (kg*sp.diff(eta0, s) - eps))]))

# decomposition of w and (4.6)
wo, wl, wn = sp.symbols('w_o w_l w_n', real=True)
w = (wo, wl, wn)
a_s = wo
a_t = wl/(s*(1-eps))
a_z = wn - wo*sp.diff(eta0, s) - wl*sp.diff(eta0, th)/(s*(1-eps))
recon = tuple(a_s*p + a_t*q + a_z*r for p, q, r in zip(Psi_s, Psi_th, Psi_z))
chk.append(('w decomposition', [sp.simplify(a-b) for a, b in zip(recon, w)]))
DwY = tuple(a_s*p + a_t*q + a_z*r for p, q, r in zip(dsY, dthY, dzY))
lhs = s*dot(w, DwY)
Er = (wl/(1-eps))*((kap*th*sp.diff(eps, th) - nu*kg)*wl + (-kap*th*(1-eps)*kg + sp.diff(nu, th))*wn) \
     + kap*th*wl*wo + wo*(kap*th*s*sp.diff(eps, s)*wl + s*sp.diff(nu, s)*wn) + a_z*kap*th*kg*wl
rhs = wl**2*(1/(1-eps) - kap) + Er
chk.append(('(4.6)', [sp.simplify(lhs - rhs)]))
# w perp Y
chk.append(('w perp Y => w_omega', [sp.simplify(dot(Y_claim, (kap*th*(1-eps)*wl - nu*wn, wl, wn)))]))

# Lemma N5: eta0 = s*y0(s^{1/N},theta)
N = sp.symbols('N', positive=True)
sig = sp.symbols('sigma', positive=True)
y0 = sp.Function('y0')
e0 = s*y0(s**(1/N), th)
sub = {s: sig**N}
def at(expr):
    return sp.simplify(expr.subs(s, sig**N))
ys = sp.Derivative(y0(sig, th), sig)
cl = {
 'eta0_s': (sp.diff(e0, s), y0(sig, th) + sig/N*sp.diff(y0(sig, th), sig)),
 'eta0_th/s': (sp.diff(e0, th)/s, sp.diff(y0(sig, th), th)),
 's eta0_ss': (s*sp.diff(e0, s, 2), sig/N*((1+1/N)*sp.diff(y0(sig, th), sig) + sig/N*sp.diff(y0(sig, th), sig, 2))),
 'eta0_sth': (sp.diff(e0, s, th), sp.diff(y0(sig, th), th) + sig/N*sp.diff(y0(sig, th), sig, th)),
 'eta0_thth/s': (sp.diff(e0, th, 2)/s, sp.diff(y0(sig, th), th, 2)),
}
for k, (a, b) in cl.items():
    d = sp.simplify(sp.expand(a.subs(s, sig**N).doit()) - b)
    # sympy writes derivatives of y0 at s**(1/N); after substitution s=sig^N they should match
    chk.append(('N5 ' + k, [sp.simplify(d)]))
# s d_s nu, d_theta nu, d_theta eps
chk.append(('N5 d_th nu', [sp.simplify(sp.diff(nu, th) - (sp.diff(eta0, s, th) - kap*sp.diff(eta0, th)/s - kap*th*sp.diff(eta0, th, 2)/s))]))
chk.append(('N5 s d_s nu', [sp.simplify(s*sp.diff(nu, s) - (s*sp.diff(eta0, s, 2) - kap*th*(sp.diff(eta0, th, s) - sp.diff(eta0, th)/s)))]))
chk.append(('N5 d_th eps', [sp.simplify(sp.diff(eps, th) - (sp.diff(kg, th)*eta + kg*sp.diff(eta0, th))/s)]))
chk.append(('N5 x d_x nu', [sp.simplify(xdnu - (s*sp.diff(nu, s) - kap*th*sp.diff(nu, th)))]))

ok = True
for name, lst in chk:
    good = all(sp.simplify(z) == 0 for z in lst)
    ok &= good
    print(f'{name:28s}', 'OK' if good else f'FAIL {lst}')
print('ALL OK' if ok else 'SOME FAIL')
