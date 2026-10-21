# R33 (reviewer): symbolic check of (5.1)-(5.3) and (8.2)-(8.3) of results/010-morse-bott.md.
# Vectors are coefficient triples in the Darboux frame (omega, ell, n) at angle theta;
# d/dtheta of A*omega+B*ell+C*n = (A_t - B) omega + (B_t + A - k C) ell + (C_t + k B) n  (formula (0.1)).
import sympy as sp

s, th, ze, kap, x, u, th0 = sp.symbols('s theta zeta kappa x u theta0', real=True)
k = sp.Function('k')
eta = sp.Function('eta')

def dth(V, t, kk):
    A, B, C = V
    return (sp.diff(A, t) - B, sp.diff(B, t) + A - kk * C, sp.diff(C, t) + kk * B)

def dplain(V, var):
    return tuple(sp.diff(c, var) for c in V)

def add(*Vs):
    return tuple(sp.simplify(sum(V[i] for V in Vs)) for i in range(3))

def mul(a, V):
    return tuple(a * c for c in V)

def dot(V, W):
    return sum(V[i] * W[i] for i in range(3))

kg = k(th)
es = eta(s, th)
# Psi = s*omega + (eta*+zeta) n
Psi = (s, sp.Integer(0), es + ze)
Ps = dplain(Psi, s)                    # theta fixed: frame does not move
Pt = dth(Psi, th, kg)
Pz = dplain(Psi, ze)
eps = kg * (es + ze) / s
print('(2.1) Psi_s:', [sp.simplify(a - b) for a, b in zip(Ps, (1, 0, sp.diff(es, s)))])
print('(2.1) Psi_th:', [sp.simplify(a - b) for a, b in zip(Pt, (0, s * (1 - eps), sp.diff(es, th)))])
print('(2.1) Psi_ze:', Pz)

# Y_kappa = Psi_s - kappa*theta/s * Psi_theta, as field in (s,theta,zeta)
Y = add(Ps, mul(-kap * th / s, Pt))
nu = sp.diff(es, s) - kap * th * sp.diff(es, th) / s
print('(5.1) Y:', [sp.simplify(a - b) for a, b in zip(Y, (1, -kap * th * (1 - eps), nu))])
h = dot(Y, Y)
print('(5.1) h:', sp.simplify(h - (1 + kap**2 * th**2 * (1 - eps)**2 + nu**2)))

def D(V, coeffs):
    # derivative of field V(s,theta,zeta) along a^s d_s + a^th d_th + a^ze d_ze
    a_s, a_t, a_z = coeffs
    return add(mul(a_s, dplain(V, s)), mul(a_t, dth(V, th, kg)), mul(a_z, dplain(V, ze)))

DYY = D(Y, (1, -kap * th / s, 0))
sDYY = tuple(sp.simplify(s * c) for c in DYY)
eps_s = sp.diff(eps, s); eps_t = sp.diff(eps, th)
nu_s = sp.diff(nu, s); nu_t = sp.diff(nu, th)
rhs52 = (-kap**2 * th**2 * (1 - eps),
         kap * th * (s * eps_s - 1 + kap * (1 - eps) - kap * th * eps_t + nu * kg),
         s * nu_s + kap**2 * th**2 * (1 - eps) * kg - kap * th * nu_t)
print('(5.2):', [sp.simplify(sp.expand(a - b)) for a, b in zip(sDYY, rhs52)])

# (5.3)
wo, wl, wn = sp.symbols('w_o w_l w_n', real=True)
es_s = sp.diff(es, s); es_t = sp.diff(es, th)
a_s = wo
a_t = wl / (s * (1 - eps))
a_z = wn - wo * es_s - wl * es_t / (s * (1 - eps))
# check decomposition w = a_s Psi_s + a_t Psi_t + a_z Psi_z
wrec = add(mul(a_s, Ps), mul(a_t, Pt), mul(a_z, Pz))
print('decomp w:', [sp.simplify(a - b) for a, b in zip(wrec, (wo, wl, wn))])
DwY = D(Y, (a_s, a_t, a_z))
lhs53 = sp.simplify(s * dot((wo, wl, wn), DwY))
rhs53 = ((1 / (1 - eps) - kap) * wl**2 + kap * th * s * eps_s * wo * wl + s * nu_s * wo * wn + kap * th * wo * wl
         + (kap * th * eps_t - nu * kg) * wl**2 / (1 - eps) + nu_t * wl * wn / (1 - eps)
         - kap * th * kg * wl * (wo * es_s + wl * es_t / (s * (1 - eps))))
print('(5.3):', sp.simplify(sp.expand(lhs53 - rhs53)))
# identities used in (2.2)
print('s eps_s = k eta*_s - eps:', sp.simplify(s * eps_s - (kg * es_s - eps)))
print('eps_th:', sp.simplify(eps_t - (sp.diff(kg, th) * (es + ze) + kg * es_t) / s))
print('s nu_s:', sp.simplify(s * nu_s - (s * sp.diff(es, s, 2) - kap * th * (sp.diff(es, s, th) - es_t / s))))
print('nu_th:', sp.simplify(nu_t - (sp.diff(es, s, th) - kap * es_t / s - kap * th * sp.diff(es, th, 2) / s)))

# ---------------- Md: Phi(x,u,zeta) = Psi(x, th0+tau(x)+u/x, zeta)
tau = sp.Function('tau')
thh = th0 + tau(x) + u / x
sub = {s: x, th: thh}
def at(V):
    return tuple(c.subs(sub) for c in V) if isinstance(V, tuple) else V.subs(sub)
kgh = k(thh)
def dx_(V):  # total derivative in x at fixed u,zeta of field given in frame at thh
    A, B, C = V
    tx = sp.diff(thh, x)
    return (sp.diff(A, x) - tx * B, sp.diff(B, x) + tx * (A - kgh * C), sp.diff(C, x) + tx * kgh * B)
def du_(V):
    A, B, C = V
    tu = sp.diff(thh, u)
    return (sp.diff(A, u) - tu * B, sp.diff(B, u) + tu * (A - kgh * C), sp.diff(C, u) + tu * kgh * B)
def dz_(V):
    return dplain(V, ze)

Phi = (x, sp.Integer(0), eta(x, thh) + ze)
Px, Pu, Pzz = dx_(Phi), du_(Phi), dz_(Phi)
kt = x * sp.diff(thh, x)  # tilde kappa
epsh = at(eps)
esh_s = at(es_s); esh_t = at(es_t)
print('(8.2) Phi_x:', [sp.simplify(a - b) for a, b in zip(Px, (1, kt * (1 - epsh), esh_s + kt * esh_t / x))])
print('(8.2) Phi_u:', [sp.simplify(a - b) for a, b in zip(Pu, (0, 1 - epsh, esh_t / x))])
print('(8.2) Phi_ze:', Pzz)
Pst = dth(Ps, th, kg)          # Psi_{s theta}
Ptt = dth(Pt, th, kg)          # Psi_{theta theta}
print('Psi_sth formula:', [sp.simplify(a - b) for a, b in zip(Pst, (0, 1 - kg * es_s, sp.diff(es, s, th)))])
etaf = es + ze
Ptt_rhs = add((0, -(sp.diff(kg, th) * etaf + 2 * kg * es_t), sp.diff(es, th, 2)),
              mul(s - kg * etaf, (-1, 0, kg)))
print('Psi_thth formula:', [sp.simplify(a - b) for a, b in zip(Ptt, Ptt_rhs)])
Pxx = dx_(Px)
thxx = sp.diff(thh, x, 2)
rhs_xx = add((0, 0, x * at(sp.diff(es, s, 2))), mul(2 * kt, at(Pst)), mul(kt**2 / x, at(Ptt)), mul(x * thxx, at(Pt)))
print('(8.3) x Phi_xx:', [sp.simplify(sp.expand(x * a - b)) for a, b in zip(Pxx, rhs_xx)])
Pxu = du_(Px)
rhs_xu = add((0, epsh - kgh * esh_s, at(sp.diff(es, s, th)) - esh_t / x), mul(kt / x, at(Ptt)))
print('(8.3) x d_u Phi_x:', [sp.simplify(sp.expand(x * a - b)) for a, b in zip(Pxu, rhs_xu)])
Pxz = dz_(Px)
print('(8.3) x d_ze Phi_x:', [sp.simplify(x * a - b) for a, b in zip(Pxz, (0, -kt * kgh, 0))])
print('x^2 thh_xx - (x^2 tau_xx + 2u/x):', sp.simplify(x**2 * thxx - (x**2 * sp.diff(tau(x), x, 2) + 2 * u / x)))
