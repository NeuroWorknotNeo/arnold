"""R32: символьная проверка формул §1-§2 и §6 results/010-morse-bott.md.  [Эксперимент]

Абстрактное исчисление в репере Дарбу (omega, ell, n) кривой на S^2:
    omega' = ell,  ell' = -omega + kg*n,  n' = -kg*ell     ((0.1))
Вектор v = a*omega + b*ell + c*n хранится как (a, b, c); d/dtheta действует по (0.1),
d/ds, d/dzeta -- покомпонентно. kg(theta), eta*(s,theta) -- произвольные функции.

Проверяется:
 1. (N3): Pi_s, Pi_theta, Pi_eta.
 2. (2.1): Psi_s, Psi_theta, Psi_zeta.
 3. §2: s*eps_s = kg*eta*_s - eps, eps_theta = (kg' eta + kg eta*_theta)/s.
 4. (2.5): тождество Эйлера для произвольных F, upsilon.
 5. §6 п.6: d_theta(Y o Psi), nabla_Y Y, формула s<w, D_w Y> для Y = Psi_s.
 6. §6 п.6: |nabla rho - Y/h| = sup_{w perp Y,|w|=1} |w_omega| = |eta*_s|/sqrt(1+eta*_s^2) <= |eta*_s|.
 7. (0.1) на конкретной несимметричной кривой сферы (численно-символьно).
"""
import sympy as sp

s, th, ze, eta_, e, a0, c, j = sp.symbols('s theta zeta eta e a_0 c j', real=True)
kg = sp.Function('k_g')(th)
es = sp.Function('etastar')(s, th)


def Dth(v):
    a, b, cc = v
    return (sp.diff(a, th) - b, sp.diff(b, th) + a - kg * cc, sp.diff(cc, th) + kg * b)


def Dvar(v, x):
    return tuple(sp.diff(t, x) for t in v)


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def lin(*pairs):
    out = [0, 0, 0]
    for coef, v in pairs:
        for i in range(3):
            out[i] += coef * v[i]
    return tuple(out)


ok = True


def check(name, expr):
    global ok
    if isinstance(expr, (sp.MatrixBase, tuple, list)):
        good = all(sp.simplify(t) == 0 for t in expr)
    else:
        good = sp.simplify(expr) == 0
    ok &= bool(good)
    print(f'{name}: {good}')


# 1. Pi(s,theta,eta) = s*omega + eta*n
Pi = (s, 0, eta_)
check('Pi_s = omega', sp.Matrix(Dvar(Pi, s)) - sp.Matrix([1, 0, 0]))
check('Pi_theta = (s - kg eta) ell', sp.Matrix(Dth(Pi)) - sp.Matrix([0, s - kg * eta_, 0]))
check('Pi_eta = n', sp.Matrix(Dvar(Pi, eta_)) - sp.Matrix([0, 0, 1]))

# 2. Psi(s,theta,zeta) = s*omega + (eta*+zeta) n
eta = es + ze
eps = kg * eta / s
Psi = (s, 0, eta)
Ps, Pt, Pz = Dvar(Psi, s), Dth(Psi), Dvar(Psi, ze)
check('(2.1) Psi_s', sp.Matrix(Ps) - sp.Matrix([1, 0, sp.diff(es, s)]))
check('(2.1) Psi_theta', sp.Matrix(Pt) - sp.Matrix([0, s * (1 - eps), sp.diff(es, th)]))
check('(2.1) Psi_zeta', sp.Matrix(Pz) - sp.Matrix([0, 0, 1]))

# 3. small quantities
check('s eps_s = kg eta*_s - eps', s * sp.diff(eps, s) - (kg * sp.diff(es, s) - eps))
check('eps_theta', sp.diff(eps, th) - (sp.diff(kg, th) * eta + kg * sp.diff(es, th)) / s)

# 4. Euler identity (2.5)
F = sp.Function('F')
ups = sp.Function('upsilon')(s, th)
jj = sp.Symbol('j', positive=True)
cc = sp.Symbol('c', positive=True)
ss = sp.Symbol('s', positive=True)
g = ss**jj * (F(sp.sqrt(ss), th, ze * ss**(-cc)) + a0)
W = g
rhoYW = ss * sp.diff(g, ss) + ss * ups.subs(s, ss) * sp.diff(g, th)
lhs = jj * W - rhoYW
vs, vt, ve = sp.symbols('vs vt ve')
Fx = F(vs, vt, ve)
rhs = ss**jj * (-ss * ups.subs(s, ss) * sp.diff(Fx, vt) + cc * ve * sp.diff(Fx, ve)
                - vs / 2 * sp.diff(Fx, vs))
rhs = rhs.subs({vs: sp.sqrt(ss), vt: th, ve: ze * ss**(-cc)})
check('(2.5) Euler identity', sp.simplify(lhs - rhs.doit()))

# 5. §6 p.6: Y o Psi = Psi_s
Y = Ps
dthY = Dth(Y)
check('d_theta(Y o Psi) = (1-kg eta*_s) ell + eta*_{s theta} n',
      sp.Matrix(dthY) - sp.Matrix([0, 1 - kg * sp.diff(es, s), sp.diff(es, s, th)]))
check('nabla_Y Y = eta*_ss n', sp.Matrix(Dvar(Y, s)) - sp.Matrix([0, 0, sp.diff(es, s, 2)]))
check('Y o Psi independent of zeta', sp.Matrix(Dvar(Y, ze)))
wo, wl, wn = sp.symbols('w_omega w_ell w_n')
A_s, A_t, A_z = sp.symbols('A_s A_t A_z')
sol = sp.solve([sp.Eq(lin((A_s, Ps), (A_t, Pt), (A_z, Pz))[i], (wo, wl, wn)[i]) for i in range(3)],
               [A_s, A_t, A_z], dict=True)[0]
DwY = lin((sol[A_s], Dvar(Y, s)), (sol[A_t], dthY), (sol[A_z], Dvar(Y, ze)))
lhs6 = s * dot((wo, wl, wn), DwY)
rhs6 = ((1 - sp.diff(es, s) * kg) * wl**2 / (1 - eps) + s * sp.diff(es, s, 2) * wo * wn
        + sp.diff(es, s, th) * wl * wn / (1 - eps))
check('§6 p.6: s<w,D_wY>', lhs6 - rhs6)
check('a^theta = w_ell/(s(1-eps))', sol[A_t] - wl / (s * (1 - eps)))

# 6. |nabla rho - Y/h| for Y = omega + p n, nabla rho = omega
p = sp.Symbol('p', real=True)
h = 1 + p**2
d = sp.Matrix([1 - 1 / h, 0, -p / h])
check('|nabla rho - Y/h|^2 = p^2/(1+p^2)', (d.T * d)[0] - p**2 / (1 + p**2))

# 7. (0.1) on a concrete non-circular curve on S^2
t = sp.Symbol('t', real=True)
X = sp.Matrix([sp.cos(t), sp.sin(t), sp.Rational(3, 10) + sp.Rational(1, 5) * sp.sin(2 * t)])
om = X / sp.sqrt((X.T * X)[0])
v = sp.sqrt((om.diff(t).T * om.diff(t))[0])
ell = om.diff(t) / v
nn = om.cross(ell)
dl = ell.diff(t) / v
dn = nn.diff(t) / v
import random
random.seed(1)
bad = 0
for _ in range(5):
    tv = random.uniform(0, 6.28)
    sub = {t: sp.Float(tv, 40)}
    o, l, n_ = [M.subs(sub).evalf(40) for M in (om, ell, nn)]
    dlv, dnv = dl.subs(sub).evalf(40), dn.subs(sub).evalf(40)
    kgv = (dlv.T * n_)[0]
    r1 = dlv - (-o + kgv * n_)
    r2 = dnv - (-kgv * l)
    bad += int(max(float(abs(x)) for x in list(r1) + list(r2)) > 1e-20)
print('(0.1) on concrete curve (5 random points):', bad == 0)
ok &= bad == 0
print('ALL:', ok)
