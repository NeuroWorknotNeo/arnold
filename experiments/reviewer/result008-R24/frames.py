"""R24: независимая символьная проверка формул §6, §7, §10 results/008-class-K.md.

Векторы записываются коэффициентами в подвижном репере Дарбу (omega, ell, n) в точке theta.
Производная репера (6.1): omega' = ell, ell' = -omega + kg*n, n' = -kg*ell, kg = kg(theta) произвольна.
eta*(s,theta) — произвольная функция. Все тождества проверяются как sympy.simplify(разность) == 0.
[Эксперимент] (символьная выкладка; доказательством не является).
"""
import sympy as sp

s, th, zeta, x, u, r, kap = sp.symbols('s theta zeta x u r kappa', real=True)
wO, wL, wN = sp.symbols('w_omega w_ell w_n', real=True)
kg = sp.Function('k')            # геодезическая кривизна k_g(theta)
es = sp.Function('etastar')      # eta*(s, theta)

ok_all = True


def check(name, expr):
    global ok_all
    if isinstance(expr, sp.MatrixBase):
        e = expr.applyfunc(lambda t: sp.simplify(sp.expand(t)))
        ok = all(t == 0 for t in e)
    else:
        e = sp.simplify(sp.expand(expr))
        ok = (e == 0)
    ok_all &= ok
    print(f"{'OK ' if ok else 'FAIL'} {name}" + ('' if ok else f'   residual = {e}'))


def frame_part(v, T):
    """d/dtheta репера, применённая к коэффициентам v=(a,b,c), T = kg(theta)."""
    a, b, c = v
    return (-b, a - c * T, b * T)


def D(v, var, theta_expr, dtheta_dvar):
    """Полная производная вектора v (коэфф. в репере в точке theta_expr) по var.
    dtheta_dvar = производная theta по var."""
    T = kg(theta_expr)
    fp = frame_part(v, T)
    return tuple(sp.diff(v[i], var) + dtheta_dvar * fp[i] for i in range(3))


def dot(a, b):
    return sum(a[i] * b[i] for i in range(3))


# ---------- §6: Darboux frame sanity: n = omega x ell, n' = -kg ell (in abstract frame ok by construction)
# ---------- Lemma K3: Pi = s omega + eta n
eta = sp.Symbol('eta', real=True)
Pi = (s, 0, eta)
Pi_s = D(Pi, s, th, 0)
Pi_th = D(Pi, th, th, 1)
Pi_eta = D(Pi, eta, th, 0)
check('(6.2) Pi_s = omega', sp.Matrix(Pi_s) - sp.Matrix([1, 0, 0]))
check('(6.2) Pi_theta = (s - kg eta) ell', sp.Matrix(Pi_th) - sp.Matrix([0, s - kg(th) * eta, 0]))
check('(6.2) Pi_eta = n', sp.Matrix(Pi_eta) - sp.Matrix([0, 0, 1]))

# ---------- (6.4): Psi(s,theta,zeta) = s omega + (eta* + zeta) n
E = es(s, th)
Psi = (s, 0, E + zeta)
Psi_s = D(Psi, s, th, 0)
Psi_th = D(Psi, th, th, 1)
Psi_z = D(Psi, zeta, th, 0)
eps = kg(th) * (E + zeta) / s
check('(6.4) Psi_s', sp.Matrix(Psi_s) - sp.Matrix([1, 0, sp.diff(E, s)]))
check('(6.4) Psi_theta', sp.Matrix(Psi_th) - sp.Matrix([0, s * (1 - eps), sp.diff(E, th)]))
check('(6.4) Psi_zeta', sp.Matrix(Psi_z) - sp.Matrix([0, 0, 1]))
# (6.5): s d_s eps = kg eta*_s - eps ; d_theta eps
check('(6.5) s d_s eps', s * sp.diff(eps, s) - (kg(th) * sp.diff(E, s) - eps))
check('(6.5) d_theta eps', sp.diff(eps, th) - (sp.diff(kg(th), th) * (E + zeta) + kg(th) * sp.diff(E, th)) / s)

# ---------- §7: K1 map, independent variables (r, theta, zeta); d_X = c d_r - (s/r) d_theta, d_Y = s d_r + (c/r) d_theta
C, S = sp.cos(th), sp.sin(th)


def dX(f):
    return C * sp.diff(f, r) - S / r * sp.diff(f, th)


def dY(f):
    return S * sp.diff(f, r) + C / r * sp.diff(f, th)


def DX(v):
    T = kg(th)
    fp = frame_part(v, T)
    return tuple(dX(v[i]) + (-S / r) * fp[i] for i in range(3))


def DY(v):
    T = kg(th)
    fp = frame_part(v, T)
    return tuple(dY(v[i]) + (C / r) * fp[i] for i in range(3))


def DZ(v):
    return tuple(sp.diff(v[i], zeta) for i in range(3))


Er = es(r, th)
Phi = (r, 0, Er + zeta)
epsr = kg(th) * (Er + zeta) / r
Es_r = sp.diff(es(s, th), s).subs(s, r)    # eta*_s at (r,theta)
Eth_r = sp.diff(es(s, th), th).subs(s, r)  # eta*_theta at (r,theta)
nuX = C * Es_r - S * Eth_r / r
nuY = S * Es_r + C * Eth_r / r
PX, PY, PZ = DX(Phi), DY(Phi), DZ(Phi)
check('(7.1) Phi_X', sp.Matrix(PX) - sp.Matrix([C, -S * (1 - epsr), nuX]))
check('(7.1) Phi_Yd', sp.Matrix(PY) - sp.Matrix([S, C * (1 - epsr), nuY]))
check('(7.1) Phi_zeta', sp.Matrix(PZ) - sp.Matrix([0, 0, 1]))
check('(7.1) B_XYd', dot(PX, PY) - (S * C * (1 - (1 - epsr) ** 2) + nuX * nuY))
check('(7.1) B_Xzeta', dot(PX, PZ) - nuX)
PXX = DX(PX)
PXY = DY(PX)
PXZ = DZ(PX)
claimXX = sp.Matrix([S ** 2 * epsr / r,
                     -S * C * epsr / r + S * dX(epsr) + nuX * kg(th) * S / r,
                     S ** 2 * (1 - epsr) * kg(th) / r + dX(nuX)])
claimXY = sp.Matrix([-S * C * epsr / r,
                     C ** 2 * epsr / r + S * dY(epsr) - nuX * kg(th) * C / r,
                     -S * C * (1 - epsr) * kg(th) / r + dY(nuX)])
claimXZ = sp.Matrix([0, S * kg(th) / r, 0])
check('(7.1) Phi_XX', sp.Matrix(PXX) - claimXX)
check('(7.1) Phi_XYd', sp.Matrix(PXY) - claimXY)
check('(7.1) Phi_Xzeta', sp.Matrix(PXZ) - claimXZ)
# B_XX, B_YY entries (for (Phi1) bound)
check('B_XX - 1', dot(PX, PX) - 1 - (S ** 2 * ((1 - epsr) ** 2 - 1) + nuX ** 2))
check('B_YY - 1', dot(PY, PY) - 1 - (C ** 2 * ((1 - epsr) ** 2 - 1) + nuY ** 2))

# ---------- §10: K2 map. Independent variables (x, theta, zeta) with theta = u x^{-kappa}:
# d_x|_{u,zeta} = d_x|_theta - (kappa theta/x) d_theta
def Dx(v):
    T = kg(th)
    fp = frame_part(v, T)
    return tuple(sp.diff(v[i], x) - kap * th / x * sp.diff(v[i], th) + (-kap * th / x) * fp[i] for i in range(3))


def dx_scalar(f):
    return sp.diff(f, x) - kap * th / x * sp.diff(f, th)


Ex = es(x, th)
Phi2 = (x, 0, Ex + zeta)
Y = Dx(Phi2)
epsx = kg(th) * (Ex + zeta) / x
Es_x = sp.diff(es(s, th), s).subs(s, x)
Eth_x = sp.diff(es(s, th), th).subs(s, x)
nu = Es_x - kap * th * Eth_x / x
check('(10.2) Y', sp.Matrix(Y) - sp.Matrix([1, -kap * th * (1 - epsx), nu]))
check('(10.2) h', dot(Y, Y) - (1 + kap ** 2 * th ** 2 * (1 - epsx) ** 2 + nu ** 2))
xPxx = tuple(x * c for c in Dx(Y))
xdxeps_claim = -kap * th * sp.diff(kg(th), th) * (Ex + zeta) / x + kg(th) * nu - epsx
check('(10.3) x d_x eps', x * dx_scalar(epsx) - xdxeps_claim)
claim103 = sp.Matrix([-kap ** 2 * th ** 2 * (1 - epsx),
                      -kap * th * ((1 - kap) + kap * epsx - xdxeps_claim - nu * kg(th)),
                      kap ** 2 * th ** 2 * (1 - epsx) * kg(th) + x * dx_scalar(nu)])
check('(10.3) x d_x^2 Phi', sp.Matrix(xPxx) - claim103)

# (10.4): Y as field in Psi coordinates (s, theta, zeta)
epsS = kg(th) * (es(s, th) + zeta) / s
nuS = sp.diff(es(s, th), s) - kap * th * sp.diff(es(s, th), th) / s
YS = (sp.Integer(1), -kap * th * (1 - epsS), nuS)
dthY = D(YS, th, th, 1)
dsY = D(YS, s, th, 0)
dzY = D(YS, zeta, th, 0)
claim_dth = sp.Matrix([kap * th * (1 - epsS),
                       1 - kap * (1 - epsS) + kap * th * sp.diff(epsS, th) - nuS * kg(th),
                       -kap * th * (1 - epsS) * kg(th) + sp.diff(nuS, th)])
check('(10.4) d_theta Y', sp.Matrix(dthY) - claim_dth)
check('(10.4) d_s Y', sp.Matrix(dsY) - sp.Matrix([0, kap * th * sp.diff(epsS, s), sp.diff(nuS, s)]))
check('(10.4) d_zeta Y', sp.Matrix(dzY) - sp.Matrix([0, kap * th * kg(th) / s, 0]))
# consistency: Y in Psi-coords equals Psi_s + theta_x Psi_theta (theta_x = -kappa theta / s)
check('(10.2) vs Psi', sp.Matrix(YS) - (sp.Matrix(Psi_s) - kap * th / s * sp.Matrix(Psi_th)))

# §10.2 item 5: decomposition w = a^s Psi_s + a^th Psi_th + a^z Psi_z
aS = wO
aT = wL / (s * (1 - epsS))
aZ = wN - wO * sp.diff(es(s, th), s) - wL * sp.diff(es(s, th), th) / (s * (1 - epsS))
wrec = aS * sp.Matrix(Psi_s) + aT * sp.Matrix(Psi_th) + aZ * sp.Matrix(Psi_z)
check('item 5: w = DPsi a', wrec - sp.Matrix([wO, wL, wN]))
DwY = aS * sp.Matrix(dsY) + aT * sp.Matrix(dthY) + aZ * sp.Matrix(dzY)
lhs = s * (sp.Matrix([wO, wL, wN]).dot(DwY))
Er_claim = (wL / (1 - epsS)) * ((kap * th * sp.diff(epsS, th) - nuS * kg(th)) * wL
                                + (-kap * th * (1 - epsS) * kg(th) + sp.diff(nuS, th)) * wN) \
    + kap * th * wL * wO + wO * (kap * th * s * sp.diff(epsS, s) * wL + s * sp.diff(nuS, s) * wN) \
    + aZ * kap * th * kg(th) * wL
check('item 5: x<w,D_wY> = w_l^2(1/(1-eps)-kappa) + E_r', lhs - (wL ** 2 * (1 / (1 - epsS) - kap) + Er_claim))
# item 3: for w perp Y, <omega,w> = kappa theta (1-eps) <ell,w> - nu <n,w>
check('item 3: <Y,w>=0 <=> w_omega = ...', sp.Matrix(YS).dot(sp.Matrix([wO, wL, wN]))
      - (wO - kap * th * (1 - epsS) * wL + nuS * wN))

print('ALL OK' if ok_all else 'SOME FAILED')
