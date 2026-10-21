"""R35: symbolic check of (7.2)-(7.6), x d_x eps, s d_s eps and Lemma N5 formulas
of results/011-normal-multiplicity.md.  [Experiment]

Vectors are coefficient triples in the Darboux frame (omega, ell, n), which depends on theta
only, with  omega' = ell,  ell' = -omega + kg n,  n' = -kg ell.
eta0(s, theta) and kg(theta) are arbitrary functions.
"""
import sympy as sp

s, th, ze, x, u, ka = sp.symbols('s theta zeta x u kappa', positive=True)
kg = sp.Function('k')(th)
eta0 = sp.Function('eta0')(s, th)


def d(V, var):
    """derivative of a frame vector V=(a,b,c) w.r.t. var in {s, th, ze}"""
    a, b, c = V
    da, db, dc = [sp.diff(t, var) for t in V]
    if var == th:
        # a omega' + b ell' + c n' = a ell + b(-omega + kg n) - c kg ell
        return (da - b, db + a - c * kg, dc + b * kg)
    return (da, db, dc)


def add(*Vs):
    return tuple(sp.simplify(sum(V[i] for V in Vs)) for i in range(3))


def mul(k, V):
    return tuple(k * t for t in V)


def dot(V, W):
    return sum(V[i] * W[i] for i in range(3))


def zero(expr):
    return sp.simplify(sp.expand(expr)) == 0


eta = eta0 + ze
Psi = (s, 0, eta)
Ps, Pt, Pz = d(Psi, s), d(Psi, th), d(Psi, ze)
eps = kg * eta / s
nu = sp.diff(eta0, s) - ka * th * sp.diff(eta0, th) / s

ok = []
# (7.2)
ok.append(('7.2 Psi_s', all(zero(a - b) for a, b in zip(Ps, (1, 0, sp.diff(eta0, s))))))
ok.append(('7.2 Psi_th', all(zero(a - b) for a, b in zip(Pt, (0, s * (1 - eps), sp.diff(eta0, th))))))
ok.append(('7.2 Psi_ze', all(zero(a - b) for a, b in zip(Pz, (0, 0, 1)))))

# (7.3): Y = Psi_s - (kappa theta / x) Psi_theta  (x = s)
Y = add(Ps, mul(-ka * th / s, Pt))
Yf = (1, -ka * th * (1 - eps), nu)
ok.append(('7.3 Y', all(zero(a - b) for a, b in zip(Y, Yf))))
h = dot(Yf, Yf)
ok.append(('7.3 h', zero(h - (1 + ka**2 * th**2 * (1 - eps)**2 + nu**2))))

# total x-derivative at constant (u, zeta): d/dx = d_s - (kappa theta/x) d_theta
def ddx(V):
    return add(d(V, s), mul(-ka * th / s, d(V, th)))

def ddx_scalar(f):
    return sp.diff(f, s) - ka * th / s * sp.diff(f, th)

xdxeps = s * ddx_scalar(eps)
ok.append(('x d_x eps', zero(xdxeps - (-ka * th * sp.diff(kg, th) * eta / s + kg * nu - eps))))
xdxnu = s * ddx_scalar(nu)
sdsnu = s * sp.diff(nu, s)
dthnu = sp.diff(nu, th)
ok.append(('x d_x nu = s d_s nu - k th d_th nu', zero(xdxnu - (sdsnu - ka * th * dthnu))))

# (7.4)
xY2 = mul(s, ddx(Yf))
rhs74 = add(mul(-ka * th * ((1 - ka) + ka * eps - xdxeps - nu * kg), (0, 1, 0)),
            mul(ka**2 * th**2 * (1 - eps), (-1, 0, kg)),
            (0, 0, xdxnu))
ok.append(('7.4', all(zero(a - b) for a, b in zip(xY2, rhs74))))

# (7.5)
dthY, dsY, dzY = d(Yf, th), d(Yf, s), d(Yf, ze)
dtheps = sp.diff(eps, th)
dseps = sp.diff(eps, s)
r_th = (ka * th * (1 - eps), 1 - ka * (1 - eps) + ka * th * dtheps - nu * kg, -ka * th * (1 - eps) * kg + dthnu)
ok.append(('7.5 d_th Y', all(zero(a - b) for a, b in zip(dthY, r_th))))
ok.append(('7.5 d_s Y', all(zero(a - b) for a, b in zip(dsY, (0, ka * th * dseps, sp.diff(nu, s))))))
ok.append(('7.5 d_ze Y', all(zero(a - b) for a, b in zip(dzY, (0, ka * th * kg / s, 0)))))
ok.append(('s d_s eps', zero(s * dseps - (kg * sp.diff(eta0, s) - eps))))

# (7.6)
wo, wl, wn = sp.symbols('w_o w_l w_n')
w = (wo, wl, wn)
a_s = wo
a_t = wl / (s * (1 - eps))
a_z = wn - wo * sp.diff(eta0, s) - wl * sp.diff(eta0, th) / (s * (1 - eps))
recon = add(mul(a_s, Ps), mul(a_t, Pt), mul(a_z, Pz))
ok.append(('7.6 decomposition of w', all(zero(a - b) for a, b in zip(recon, w))))
DwY = add(mul(a_s, dsY), mul(a_t, dthY), mul(a_z, dzY))
lhs = s * dot(w, DwY)
Er = (wl / (1 - eps) * ((ka * th * dtheps - nu * kg) * wl + (-ka * th * (1 - eps) * kg + dthnu) * wn)
      + ka * th * wl * wo + wo * (ka * th * s * dseps * wl + s * sp.diff(nu, s) * wn)
      + a_z * ka * th * kg * wl)
ok.append(('7.6', zero(lhs - (wl**2 * (1 / (1 - eps) - ka) + Er))))
# w perp Y
ok.append(('w perp Y => w_o', zero(sp.solve(dot(w, Yf), wo)[0] - (ka * th * (1 - eps) * wl - nu * wn))))

# Lemma N5 formulas: eta0 = s y0(s^{1/N}, theta)
N = sp.Symbol('N', positive=True, integer=True)
sig = sp.Symbol('sigma', positive=True)
y0 = sp.Function('y0')
e0 = s * y0(s**(1 / N), th)
sub = {s: sig**N}
def chk(name, expr, target):
    val = sp.simplify((expr - target).subs(s, sig**N).doit())
    ok.append((name, sp.simplify(val) == 0))
Ys = lambda: sp.Derivative(y0(sig, th), sig)
y = y0(sig, th)
ys = sp.diff(y, sig)
yss = sp.diff(y, sig, 2)
yst = sp.diff(y, sig, th)
yt = sp.diff(y, th)
ytt = sp.diff(y, th, 2)
chk('N5 eta0_s', sp.diff(e0, s), y + sig / N * ys)
chk('N5 s eta0_ss', s * sp.diff(e0, s, 2), sig / N * ((1 + 1 / N) * ys + sig / N * yss))
chk('N5 eta0_sth', sp.diff(e0, s, th), yt + sig / N * yst)
chk('N5 eta0_thth/s', sp.diff(e0, th, 2) / s, ytt)
chk('N5 eta0_th/s', sp.diff(e0, th) / s, yt)
# s d_s nu, d_th nu formulas of N5
nu5 = sp.diff(eta0, s) - ka * th * sp.diff(eta0, th) / s
ok.append(('N5 d_th nu', zero(sp.diff(nu5, th) - (sp.diff(eta0, s, th) - ka * sp.diff(eta0, th) / s - ka * th * sp.diff(eta0, th, 2) / s))))
ok.append(('N5 s d_s nu', zero(s * sp.diff(nu5, s) - (s * sp.diff(eta0, s, 2) - ka * th * (sp.diff(eta0, s, th) - sp.diff(eta0, th) / s)))))
ok.append(('N5 d_th eps', zero(dtheps - (sp.diff(kg, th) * eta + kg * sp.diff(eta0, th)) / s)))

for name, v in ok:
    print(f'{name:40s} {v}')
print('ALL OK' if all(v for _, v in ok) else 'FAILURES')
