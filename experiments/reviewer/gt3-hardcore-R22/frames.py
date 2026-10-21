"""R22: independent symbolic check of the frame formulas of
notes/prover/2026-10-21-gt3-hardcore.md, sections 6 (lemma K3, (6.4), theorem K1)
and 8 ((8.2)-(8.4), step 5 of theorem K2, Euler inequality, (8.5)).

Method (independent of the author's frame_check.py): vectors are coefficient columns in the
moving Darboux frame (omega, T, n) of a unit-speed curve on S^2 with ARBITRARY geodesic
curvature k(theta) (sympy Function) and ARBITRARY eta*(s, theta) (sympy Function).
The theta-derivative of the frame is d/dtheta [omega, T, n] = [T, -omega + k n, -k T].
A coordinate vector field V acting on a vector a*omega + b*T + c*n gives
   V(coeffs) + V(theta) * M * coeffs,   M = [[0,-1,0],[1,0,-k],[0,k,0]].
Run: ~/venv/bin/python frames.py   (prints True for every identity)  [Experiment]
"""
import sympy as sp

th, r, zeta, x, s, kap = sp.symbols('theta r zeta x s kappa', real=True)
k = sp.Function('k')(th)
E = sp.Function('E')          # eta*(s, theta)


def M():
    return sp.Matrix([[0, -1, 0], [1, 0, -k], [0, k, 0]])


def vder(vec, op, op_theta):
    """derivative of a frame vector along a coordinate field op; op_theta = op(theta)"""
    return sp.Matrix([op(c) for c in vec]) + op_theta * M() * vec


def dot(a, b):
    return sp.expand((a.T * b)[0, 0])


def check(name, expr):
    ok = sp.simplify(sp.expand(expr)) == 0
    if not ok:
        ok = sp.simplify(sp.trigsimp(sp.expand(expr))) == 0
    print(f'{name:55s} {ok}')
    return ok


allok = True

# ---------------- (6.2) lemma K3, P(s,theta,eta) = s omega + eta n ----------------------
eta_ = sp.symbols('eta', real=True)
P = sp.Matrix([s, 0, eta_])
Ps = vder(P, lambda f: sp.diff(f, s), 0)
Pt = vder(P, lambda f: sp.diff(f, th), 1)
Pe = vder(P, lambda f: sp.diff(f, eta_), 0)
allok &= check('(6.2) P_s = omega', (Ps - sp.Matrix([1, 0, 0])).norm())
allok &= check('(6.2) P_theta = (s - k eta) T', (Pt - sp.Matrix([0, s - k * eta_, 0])).norm())
allok &= check('(6.2) P_eta = n', (Pe - sp.Matrix([0, 0, 1])).norm())
allok &= check('(6.2) |P|^2 = s^2 + eta^2', dot(P, P) - s**2 - eta_**2)
# Darboux frame (6.1) on a concrete curve: upper circle z = 1/sqrt2, theta = phi/sqrt2, k = 1
ph = sp.sqrt(2) * th
om = sp.Matrix([sp.cos(ph), sp.sin(ph), 1]) / sp.sqrt(2)
T = sp.diff(om, th)
nn = om.cross(T)
allok &= check('(6.1) circle: |T| = 1', sp.simplify(T.dot(T)) - 1)
allok &= check("(6.1) circle: T' = -omega + 1*n", (sp.diff(T, th) + om - nn).norm())
allok &= check("(6.1) circle: n' = -1*T", (sp.diff(nn, th) + T).norm())
allok &= check('(9) circle: n = (-cos,-sin,1)/sqrt2', (nn - sp.Matrix([-sp.cos(ph), -sp.sin(ph), 1]) / sp.sqrt(2)).norm())

# ---------------- (6.4) chart Psi(s,theta,zeta) = s omega + (eta*+zeta) n --------------
Es = E(s, th)
eta = Es + zeta
eps = k * eta / s
Psi = sp.Matrix([s, 0, eta])
Psi_s = vder(Psi, lambda f: sp.diff(f, s), 0)
Psi_t = vder(Psi, lambda f: sp.diff(f, th), 1)
Psi_z = vder(Psi, lambda f: sp.diff(f, zeta), 0)
allok &= check('(6.4) Psi_s', (Psi_s - sp.Matrix([1, 0, sp.diff(Es, s)])).norm())
allok &= check('(6.4) Psi_theta', (Psi_t - sp.Matrix([0, s * (1 - eps), sp.diff(Es, th)])).norm())
allok &= check('(6.4) Psi_zeta', (Psi_z - sp.Matrix([0, 0, 1])).norm())
allok &= check('(6.5) s d_s eps = k eta*_s - eps', s * sp.diff(eps, s) - (k * sp.diff(Es, s) - eps))
allok &= check('(6.5) d_theta eps = (k eta + k eta*_theta)/s',
               sp.diff(eps, th) - (sp.diff(k, th) * eta + k * sp.diff(Es, th)) / s)

# ---------------- Theorem K1: X = r cos theta, Y = r sin theta --------------------------
C, S = sp.cos(th), sp.sin(th)
Er = E(r, th)
etaK = Er + zeta
epsK = k * etaK / r


def DX(f):
    return C * sp.diff(f, r) - S / r * sp.diff(f, th)


def DY(f):
    return S * sp.diff(f, r) + C / r * sp.diff(f, th)


def Dz(f):
    return sp.diff(f, zeta)


DXth, DYth = -S / r, C / r
Phi = sp.Matrix([r, 0, etaK])
PhX = vder(Phi, DX, DXth)
PhY = vder(Phi, DY, DYth)
Phz = vder(Phi, Dz, 0)
pX = C * sp.diff(Er, r) - S * sp.diff(Er, th) / r
pY = S * sp.diff(Er, r) + C * sp.diff(Er, th) / r
allok &= check('K1 Phi_X', (PhX - sp.Matrix([C, -S * (1 - epsK), pX])).norm())
allok &= check('K1 Phi_Y', (PhY - sp.Matrix([S, C * (1 - epsK), pY])).norm())
allok &= check('K1 Phi_zeta', (Phz - sp.Matrix([0, 0, 1])).norm())
allok &= check('K1 B_XY', dot(PhX, PhY) - (S * C * (1 - (1 - epsK)**2) + pX * pY))
allok &= check('K1 B_Xzeta', dot(PhX, Phz) - pX)
allok &= check('K1 B_XX - 1', dot(PhX, PhX) - 1 - (S**2 * ((1 - epsK)**2 - 1) + pX**2))
allok &= check('K1 B_YY - 1', dot(PhY, PhY) - 1 - (C**2 * ((1 - epsK)**2 - 1) + pY**2))
allok &= check('K1 B_Yzeta', dot(PhY, Phz) - pY)
PhXX = vder(PhX, DX, DXth)
PhXY = vder(PhX, DY, DYth)
PhXz = vder(PhX, Dz, 0)
PhYX = vder(PhY, DX, DXth)
allok &= check('K1 Phi_XY = Phi_YX (consistency)', (PhXY - PhYX).norm())
PhXX_claim = sp.Matrix([S**2 * epsK / r,
                        -S * C * epsK / r + S * DX(epsK) + pX * k * S / r,
                        S**2 * (1 - epsK) * k / r + DX(pX)])
PhXY_claim = sp.Matrix([-S * C * epsK / r,
                        C**2 * epsK / r + S * DY(epsK) - pX * k * C / r,
                        -S * C * (1 - epsK) * k / r + DY(pX)])
allok &= check('K1 Phi_XX', (PhXX - PhXX_claim).norm())
allok &= check('K1 Phi_XY', (PhXY - PhXY_claim).norm())
allok &= check('K1 Phi_Xzeta', (PhXz - sp.Matrix([0, S * k / r, 0])).norm())

# (V1) of K1: F0(t,e) = (1+t^2)^{j/2} [G(atan t) + 1/2 h(atan t) (1+t^2)^{-c} e^2]
t, e, j, c = sp.symbols('t e j c', real=True)
G = sp.Function('G')
h = sp.Function('h')
F0 = (1 + t**2)**(j / 2) * (G(sp.atan(t)) + sp.Rational(1, 2) * h(sp.atan(t)) * (1 + t**2)**(-c) * e**2)
H = sp.hessian(F0, (t, e)).subs({t: 0, e: 0}).doit()
grad = [sp.diff(F0, v).subs({t: 0, e: 0}).doit() for v in (t, e)]
G1 = sp.Subs(sp.Derivative(G(t), t), t, 0).doit()
print('K1 grad F0(0) =', [sp.simplify(g) for g in grad])
print('K1 Hess F0(0) =', sp.simplify(H))
G0, G2 = sp.symbols('G0 G2')
Hs = sp.simplify(H.subs(sp.Subs(sp.Derivative(G(t), t), t, 0), 0))
print('   with G\'(0)=0:', Hs)

# ---------------- Theorem K2: Phi(x,u,zeta) = Psi(x, u x^-kappa, zeta) ----------------
Ex = E(x, th)
etaX = Ex + zeta
epsX = k * etaX / x


def Dx(f):            # d/dx at constant (u, zeta): theta = u x^-kappa, d_x theta = -kappa theta/x
    return sp.diff(f, x) - kap * th / x * sp.diff(f, th)


Dxth = -kap * th / x
PhiK2 = sp.Matrix([x, 0, etaX])
Y = vder(PhiK2, Dx, Dxth)
p = sp.diff(Ex, x) - kap * th * sp.diff(Ex, th) / x
allok &= check('(8.2) Y', (Y - sp.Matrix([1, -kap * th * (1 - epsX), p])).norm())
allok &= check('(8.2) h = |Y|^2', dot(Y, Y) - (1 + kap**2 * th**2 * (1 - epsX)**2 + p**2))
xYx = x * vder(Y, Dx, Dxth)
xDeps = x * Dx(epsX)
xDp = x * Dx(p)
claim83 = (-kap * th * ((1 - kap) + kap * epsX - xDeps - p * k) * sp.Matrix([0, 1, 0])
           + kap**2 * th**2 * (1 - epsX) * sp.Matrix([-1, 0, k]) + xDp * sp.Matrix([0, 0, 1]))
allok &= check('(8.3) x d_x^2 Phi', (xYx - claim83).norm())
allok &= check('(8.3) x d_x eps = -kap th k\' eta/x + k p - eps',
               xDeps - (-kap * th * sp.diff(k, th) * etaX / x + k * p - epsX))

# (8.4): Y as a field in Psi-coordinates (s, theta, zeta)
epsS = eps
pS = sp.diff(Es, s) - kap * th * sp.diff(Es, th) / s
Yf = sp.Matrix([1, -kap * th * (1 - epsS), pS])
dtY = vder(Yf, lambda f: sp.diff(f, th), 1)
dsY = vder(Yf, lambda f: sp.diff(f, s), 0)
dzY = vder(Yf, lambda f: sp.diff(f, zeta), 0)
claim_dtY = sp.Matrix([kap * th * (1 - epsS),
                       1 - kap * (1 - epsS) + kap * th * sp.diff(epsS, th) - pS * k,
                       -kap * th * (1 - epsS) * k + sp.diff(pS, th)])
allok &= check('(8.4) d_theta Y', (dtY - claim_dtY).norm())
allok &= check('(8.4) d_s Y', (dsY - sp.Matrix([0, kap * th * sp.diff(epsS, s), sp.diff(pS, s)])).norm())
allok &= check('(8.4) d_zeta Y', (dzY - sp.Matrix([0, kap * th * k / s, 0])).norm())
# consistency of (8.3) and (8.4): nabla_Y Y = d_s Y - (kappa theta/s) d_theta Y must equal d_x^2 Phi
nablaYY = dsY - kap * th / s * dtY
allok &= check('(8.3)=(8.4) consistency nabla_Y Y', (s * nablaYY - xYx.subs(x, s)).norm())

# step 5 of K2: x <w, D_w Y> = wT^2 (1/(1-eps) - kappa) + calE
wo, wT, wn = sp.symbols('w_omega w_T w_n', real=True)
w = sp.Matrix([wo, wT, wn])
as_ = wo
at_ = wT / (s * (1 - epsS))
az_ = wn - wo * sp.diff(Es, s) - wT * sp.diff(Es, th) / (s * (1 - epsS))
allok &= check('K2 step5 decomposition of w', (as_ * Psi_s + at_ * Psi_t + az_ * Psi_z - w).norm())
DwY = as_ * dsY + at_ * dtY + az_ * dzY
lhs = s * dot(w, DwY)
calE = (wT / (1 - epsS) * ((kap * th * sp.diff(epsS, th) - pS * k) * wT + kap * th * (1 - epsS) * wo
                           + (-kap * th * (1 - epsS) * k + sp.diff(pS, th)) * wn)
        + wo * (kap * th * s * sp.diff(epsS, s) * wT + s * sp.diff(pS, s) * wn)
        + az_ * kap * th * k * wT)
allok &= check('K2 step5 x<w,D_wY> = wT^2(1/(1-eps)-kappa) + E', lhs - (wT**2 * (1 / (1 - epsS) - kap) + calE))

# Euler inequality (step 7 of K2)
Q = G(th) - G(0) + sp.Rational(1, 2) * h(th) * e**2
cc = sp.symbols('c', positive=True)
lhsE = kap * th * sp.diff(Q, th) + cc * e * sp.diff(Q, e) - kap * Q
rhsE = (kap * (th * sp.diff(G(th), th) - (G(th) - G(0)))
        + e**2 * ((cc - kap / 2) * h(th) + kap / 2 * th * sp.diff(h(th), th)))
allok &= check('K2 step7 Euler identity', lhsE - rhsE)

# Gamma_* and (8.5)
a0, lam0, jj = sp.symbols('a0 lambda0 j', positive=True)
g1 = sp.Rational(5, 4) * kap
g2 = kap * (1 - kap)
Gam = sp.sqrt(a0 / lam0) * (sp.Rational(3, 2) * sp.sqrt(3) * jj * g1 + 2 * sp.sqrt(2) * g2)
Gbound = kap * sp.sqrt(a0 / lam0) * (sp.Rational(15, 8) * sp.sqrt(3) * jj + 2 * sp.sqrt(2))
allok &= check('K2 Gamma_* <= bound: bound - Gamma = 2sqrt2 kappa^2 sqrt(a0/l0)',
               sp.simplify(Gbound - Gam - 2 * sp.sqrt(2) * kap**2 * sp.sqrt(a0 / lam0)))
kmax = jj * lam0 / (a0 * (sp.Rational(15, 8) * sp.sqrt(3) * jj + 2 * sp.sqrt(2))**2)
allok &= check('K2 (8.5): Gbound^2 = j*kappa at kappa = kmax', sp.simplify((Gbound**2 - jj * kap).subs(kap, kmax)))
print('ALL OK:', allok)
