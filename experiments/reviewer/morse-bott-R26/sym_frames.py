"""R26: symbolic check of the chart formulas in notes/prover/2026-10-21-morse-bott.md, sec. 2.3, 6.2, 6.3.

Independent re-derivation. Vectors are stored as coefficient triples in the moving
Darboux frame (omega, T, n) of a curve on S^2 with natural parameter theta:
    omega' = T,  T' = -omega + k n,  n' = -k T.
Generic functions: k(theta), E(s,theta) = eta^*(s,theta). Coordinates (s, theta, zeta).

Checks:
 (2.5)  Psi_s, Psi_theta, Psi_zeta
 (6.3)  Y_kappa = Psi_s - (kappa theta/s) Psi_theta,  h = |Y|^2
 (6.5)  s D_Y Y
 (6.7)  s <w, D_w Y>  (generic w, 7 terms)
 w perp Y  =>  w_omega = kappa theta (1-eps) w_T - psi w_n
 (6.4)  beta W - rho Y W  for generic F(sigma, theta, e)
 (6.2)  Euler inequality identity
 Lemma M, item 6: completing the square
 Theorem Mb, step 7: constant C_Gamma
"""
import sympy as sp

s, th, z, ka = sp.symbols('s theta zeta kappa', real=True)
k = sp.Function('k')(th)
E = sp.Function('E')(s, th)          # eta^*
eta = E + z


def d_th(v):
    a, b, c = v
    return (sp.diff(a, th) - b, sp.diff(b, th) + a - k * c, sp.diff(c, th) + k * b)


def d_s(v):
    return tuple(sp.diff(x, s) for x in v)


def d_z(v):
    return tuple(sp.diff(x, z) for x in v)


def add(*vs):
    return tuple(sp.Add(*[v[i] for v in vs]) for i in range(3))


def mul(c, v):
    return tuple(c * x for x in v)


def dot(u, v):
    return sum(u[i] * v[i] for i in range(3))


def simp(x):
    return sp.simplify(sp.expand(x))


Psi = (s, 0, eta)
Ps, Pt, Pz = d_s(Psi), d_th(Psi), d_z(Psi)
eps = k * eta / s
print('(2.5) Psi_s     :', [simp(Ps[i] - (1, 0, sp.diff(E, s))[i]) for i in range(3)])
print('(2.5) Psi_theta :', [simp(Pt[i] - (0, s * (1 - eps), sp.diff(E, th))[i]) for i in range(3)])
print('(2.5) Psi_zeta  :', [simp(Pz[i] - (0, 0, 1)[i]) for i in range(3)])

Y = add(Ps, mul(-ka * th / s, Pt))
psi = sp.diff(E, s) - ka * th * sp.diff(E, th) / s
Y63 = (1, -ka * th * (1 - eps), psi)
print('(6.3) Y         :', [simp(Y[i] - Y63[i]) for i in range(3)])
h = dot(Y, Y)
print('(L1)  h         :', simp(h - (1 + ka**2 * th**2 * (1 - eps)**2 + psi**2)))

# (6.5): s D_Y Y; Y in coordinates is d_s - (ka th/s) d_th (zeta fixed)
DYY = add(d_s(Y), mul(-ka * th / s, d_th(Y)))
eps_s, eps_t = sp.diff(eps, s), sp.diff(eps, th)
psi_s, psi_t = sp.diff(psi, s), sp.diff(psi, th)
f65 = (-ka**2 * th**2 * (1 - eps),
       ka * th * (s * eps_s - 1 + ka * (1 - eps) - ka * th * eps_t + psi * k),
       s * psi_s + ka**2 * th**2 * (1 - eps) * k - ka * th * psi_t)
print('(6.5) s D_Y Y   :', [simp(s * DYY[i] - f65[i]) for i in range(3)])

# (6.7): generic w
wo, wT, wn = sp.symbols('w_omega w_T w_n', real=True)
w = (wo, wT, wn)
aS, aT, aZ = sp.symbols('a_s a_t a_z')
sol = sp.solve([sp.expand(add(mul(aS, Ps), mul(aT, Pt), mul(aZ, Pz))[i] - w[i]) for i in range(3)],
               [aS, aT, aZ], dict=True)[0]
print('coeffs a^s, a^theta, a^zeta:', [simp(sol[aS] - wo), simp(sol[aT] - wT / (s * (1 - eps))),
                                       simp(sol[aZ] - (wn - wo * sp.diff(E, s) - wT * sp.diff(E, th) / (s * (1 - eps))))])
DwY = add(mul(sol[aS], d_s(Y)), mul(sol[aT], d_th(Y)), mul(sol[aZ], d_z(Y)))
lhs = s * dot(w, DwY)
Es, Et = sp.diff(E, s), sp.diff(E, th)
t1 = (1 / (1 - eps) - ka) * wT**2
t2 = ka * th * s * eps_s * wo * wT
t3 = s * psi_s * wo * wn
t4 = ka * th * wo * wT
t5 = (ka * th * eps_t - psi * k) * wT**2 / (1 - eps)
t6 = psi_t * wT * wn / (1 - eps)
t7 = -ka * th * k * wT * (wo * Es + wT * Et / (s * (1 - eps)))
print('(6.7) s<w,D_wY> - (1+...+7):', simp(sp.together(lhs - (t1 + t2 + t3 + t4 + t5 + t6 + t7))))

# w perp Y
wperp_o = ka * th * (1 - eps) * wT - psi * wn
print('w perp Y        :', simp(dot((wperp_o, wT, wn), Y)))

# kappa = 0 version used in theorem Mc (sanity)
lhs0 = lhs.subs(ka, 0)
rhs0 = (1 - Es * k) * wT**2 / (1 - eps) + s * sp.diff(Es, s) * wo * wn + sp.diff(Es, th) * wT * wn / (1 - eps)
print('(Mc, kappa=0)   :', simp(sp.together(lhs0 - rhs0)))

# (6.4): beta W - rho Y W for generic F(sigma, theta, e)
j, m, a0 = sp.symbols('j m a_0', positive=True)
c = (j - m + 2) / 2
sig, ee = sp.symbols('sigma e', positive=True)
F = sp.Function('F')
g = s**j * (F(sp.sqrt(s), th, z * s**(-c)) + a0)      # W o Psi in (s,theta,zeta)
YW = sp.diff(g, s) - ka * th / s * sp.diff(g, th)
lhs64 = j * g - s * YW
Fs = F(sig, th, ee)
rhs64 = s**j * (ka * th * sp.diff(Fs, th) + c * ee * sp.diff(Fs, ee) - sig / 2 * sp.diff(Fs, sig))
rhs64 = rhs64.subs({sig: sp.sqrt(s), ee: z * s**(-c)})
print('(6.4) Euler     :', simp(sp.expand(lhs64.doit() - rhs64.doit())))

# (6.2) identity
Lam = sp.Function('Lambda')(th)
hn = sp.Function('h_n')(th)
Q = Lam + hn * ee**2 / 2
expr = ka * th * sp.diff(Q, th) + c * ee * sp.diff(Q, ee) - ka * Q
target = ka * (th * sp.diff(Lam, th) - Lam) + ee**2 * ((c - ka / 2) * hn + ka / 2 * th * sp.diff(hn, th))
print('(6.2) identity  :', simp(expr - target))

# Lemma M step 6: b'K - Gamma sqrt(K) r + Gamma^2 r^2/(4b') = (...)^2
K, Gm, bp, r = sp.symbols('K Gamma bprime r', positive=True)
print('Lemma M square  :', simp(bp * K - Gm * sp.sqrt(K) * r + Gm**2 * r**2 / (4 * bp)
                               - (sp.sqrt(bp * K) - Gm * r / (2 * sp.sqrt(bp)))**2))

# Theorem Mb step 7: C_Gamma
a0p, kap, Rt, jj = sp.symbols('a0 kappa R_theta j', positive=True)
Gam = sp.sqrt(2) * (sp.Rational(3, 2) * jj * a0p * sp.sqrt(sp.Rational(3, 2) / a0p) * sp.Rational(5, 4) * kap * Rt
                    + sp.sqrt(2 * a0p) * 2 * kap * Rt)
CG = sp.Rational(15, 8) * sp.sqrt(3) * jj + 4
print('C_Gamma         :', simp(Gam - CG * sp.sqrt(a0p) * kap * Rt))
