# R33: re-run of the Md part of frames.py with eta*(s,theta), k(theta) generic polynomials
# (avoids sympy Subs-artifacts with undefined functions). Same formulas (8.2)-(8.3).
import sympy as sp
x, u, ze, th0, s, th = sp.symbols('x u zeta theta0 s theta', real=True)
cs = sp.symbols('c0:16'); ks = sp.symbols('k0:4'); ts = sp.symbols('t1:4')
etaP = sum(cs[4*i+j] * s**(i) * th**j for i in range(4) for j in range(4))
kP = sum(ks[j] * th**j for j in range(4))
tauP = sum(ts[j-1] * x**sp.Rational(j, 3) for j in range(1, 4))   # tau_v(x)=T(x^{1/N}), N=3 here
thh = th0 + tauP + u / x
E = lambda expr: expr.subs({s: x, th: thh}, simultaneous=True)
kgh = E(kP)
def dvar(V, var):
    A, B, C = V
    tv = sp.diff(thh, var)
    return (sp.diff(A, var) - tv * B, sp.diff(B, var) + tv * (A - kgh * C), sp.diff(C, var) + tv * kgh * B)
def dth(V):
    A, B, C = V
    return (sp.diff(A, th) - B, sp.diff(B, th) + A - kP * C, sp.diff(C, th) + kP * B)
add = lambda *Vs: tuple(sum(V[i] for V in Vs) for i in range(3))
mul = lambda a, V: tuple(a * c for c in V)
Phi = (x, 0, E(etaP) + ze)
Px = dvar(Phi, x); Pu = dvar(Phi, u); Pz = tuple(sp.diff(c, ze) for c in Phi)
kt = x * sp.diff(thh, x)
eps = kP * (etaP + ze) / s
es_s, es_t = sp.diff(etaP, s), sp.diff(etaP, th)
chk = lambda a, b: [sp.simplify(sp.expand(p - q)) for p, q in zip(a, b)]
print('(8.2) Phi_x', chk(Px, (1, kt * (1 - E(eps)), E(es_s) + kt * E(es_t) / x)))
print('(8.2) Phi_u', chk(Pu, (0, 1 - E(eps), E(es_t) / x)))
print('(8.2) Phi_z', Pz)
Psi = (s, 0, etaP + ze)
Ps = tuple(sp.diff(c, s) for c in Psi); Pt = dth(Psi)
Pst = dth(Ps); Ptt = dth(Pt)
Etup = lambda V: tuple(E(c) for c in V)
rhs_xx = add((0, 0, x * E(sp.diff(etaP, s, 2))), mul(2 * kt, Etup(Pst)), mul(kt**2 / x, Etup(Ptt)), mul(x * sp.diff(thh, x, 2), Etup(Pt)))
print('(8.3) x Phi_xx', chk(mul(x, dvar(Px, x)), rhs_xx))
rhs_xu = add((0, E(eps) - kgh * E(es_s), E(sp.diff(etaP, s, th)) - E(es_t) / x), mul(kt / x, Etup(Ptt)))
print('(8.3) x d_u Phi_x', chk(mul(x, dvar(Px, u)), rhs_xu))
print('(8.3) x d_z Phi_x', chk(mul(x, tuple(sp.diff(c, ze) for c in Px)), (0, -kt * kgh, 0)))
