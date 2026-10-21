"""R43: независимая символьная проверка формул (3.1)-(3.7) results/014 (теорема W).

Векторы записываются коэффициентами в подвижном репере (omega, ell, n) кривой на сфере,
производная по theta берётся по уравнениям Дарбу (0.1):
  omega' = ell,  ell' = -omega + k n,  n' = -k ell.
eta0(s,theta) -- произвольная функция, k(theta) -- произвольная функция.
Поле Y = Psi_s - (kappa*theta/s) Psi_theta + (lam*zeta/s) Psi_zeta.
[Эксперимент]
"""
import sympy as sp

s = sp.symbols('s', positive=True)
th, z = sp.symbols('theta zeta', real=True)
kap, lam, a0 = sp.symbols('kappa lambda a0', real=True)
c, beta, N = sp.symbols('c beta N', positive=True)
k = sp.Function('k')(th)
eta0 = sp.Function('eta0')(s, th)


def dth(V):
    a, b, cc = V
    return (sp.diff(a, th) - b, sp.diff(b, th) + a - k * cc, sp.diff(cc, th) + k * b)


def ds(V):
    return tuple(sp.diff(x, s) for x in V)


def dz(V):
    return tuple(sp.diff(x, z) for x in V)


def add(*Vs):
    return tuple(sp.simplify(sum(V[i] for V in Vs)) for i in range(3))


def mul(f, V):
    return tuple(f * x for x in V)


def dot(V, W):
    return sum(V[i] * W[i] for i in range(3))


eta = eta0 + z
Psi = (s, sp.Integer(0), eta)            # s*omega + eta*n
Ps, Pt, Pz = ds(Psi), dth(Psi), dz(Psi)

eps = k * eta / s
nu = sp.diff(eta0, s) - kap * th * sp.diff(eta0, th) / s
nut = nu + lam * z / s

checks = {}
# (3.1)
checks['3.1 Psi_s'] = [sp.simplify(Ps[i] - (1, 0, sp.diff(eta0, s))[i]) for i in range(3)]
checks['3.1 Psi_th'] = [sp.simplify(Pt[i] - (0, s * (1 - eps), sp.diff(eta0, th))[i]) for i in range(3)]
checks['3.1 Psi_z'] = [sp.simplify(Pz[i] - (0, 0, 1)[i]) for i in range(3)]

Y = add(Ps, mul(-kap * th / s, Pt), mul(lam * z / s, Pz))
# (3.2)
Y_claim = (1, -kap * th * (1 - eps), nut)
checks['3.2 Y'] = [sp.simplify(Y[i] - Y_claim[i]) for i in range(3)]
h_claim = 1 + kap**2 * th**2 * (1 - eps)**2 + nut**2
checks['3.2 h'] = [sp.simplify(dot(Y, Y) - h_claim)]

# (3.3)
Yt, Ys, Yz = dth(Y), ds(Y), dz(Y)
eps_t = sp.diff(eps, th)
nut_t = sp.diff(nut, th)
Yt_claim = (kap * th * (1 - eps),
            1 - kap * (1 - eps) + kap * th * eps_t - nut * k - (lam * z / s) * k,
            -kap * th * (1 - eps) * k + nut_t)
# NB: в (3.3) стоит nu~ k_g, nu~ включает lam*zeta/s; проверяем с nut
Yt_claim = (kap * th * (1 - eps),
            1 - kap * (1 - eps) + kap * th * eps_t - nut * k,
            -kap * th * (1 - eps) * k + nut_t)
checks['3.3 dY/dth'] = [sp.simplify(Yt[i] - Yt_claim[i]) for i in range(3)]
Ys_claim = (0, kap * th * sp.diff(eps, s), sp.diff(nut, s))
checks['3.3 dY/ds'] = [sp.simplify(Ys[i] - Ys_claim[i]) for i in range(3)]
Yz_claim = (0, kap * th * k / s, lam / s)
checks['3.3 dY/dz'] = [sp.simplify(Yz[i] - Yz_claim[i]) for i in range(3)]

# (3.4): s D_Y Y = s*Ys - kap*th*Yt + lam*z*Yz
sDYY = add(mul(s, Ys), mul(-kap * th, Yt), mul(lam * z, Yz))
sds_eps = s * sp.diff(eps, s)
sds_nut = s * sp.diff(nut, s)
DYY_claim = (-kap**2 * th**2 * (1 - eps),
             kap * th * (sds_eps - 1 + kap * (1 - eps) - kap * th * eps_t + nut * k + lam * k * z / s),
             sds_nut + kap**2 * th**2 * (1 - eps) * k - kap * th * nut_t + lam**2 * z / s)
checks['3.4 sD_YY'] = [sp.simplify(sDYY[i] - DYY_claim[i]) for i in range(3)]

# (3.5)
wo, wl, wn = sp.symbols('w_o w_l w_n', real=True)
eta0s, eta0t = sp.diff(eta0, s), sp.diff(eta0, th)
as_ = wo
at_ = wl / (s * (1 - eps))
az_ = wn - wo * eta0s - wl * eta0t / (s * (1 - eps))
# проверка разложения w = a^s Psi_s + a^th Psi_th + a^z Psi_z
wrec = add(mul(as_, Ps), mul(at_, Pt), mul(az_, Pz))
checks['3.5 decomposition'] = [sp.simplify(wrec[i] - (wo, wl, wn)[i]) for i in range(3)]
DwY = add(mul(as_, Ys), mul(at_, Yt), mul(az_, Yz))
lhs35 = sp.simplify(s * dot((wo, wl, wn), DwY))
rhs35 = ((1 / (1 - eps) - kap) * wl**2 + kap * th * wo * wl
         + ((kap * th * eps_t - nut * k) * wl**2 + nut_t * wl * wn) / (1 - eps)
         + wo * (kap * th * sds_eps * wl + sds_nut * wn)
         - kap * th * k * wl * (wo * eta0s + wl * eta0t / (s * (1 - eps)))
         + lam * az_ * wn)
checks['3.5 s<w,D_wY>'] = [sp.simplify(lhs35 - rhs35)]

# (3.6)
checks['3.6 w perp Y'] = [sp.simplify(dot((kap * th * (1 - eps) * wl - nut * wn, wl, wn), Y))]

# Тождества после (3.7)
checks['s d_s eps'] = [sp.simplify(sds_eps - (k * eta0s - eps))]
checks['d_th eps'] = [sp.simplify(eps_t - (sp.diff(k, th) * eta + k * eta0t) / s)]
checks['d_th nut'] = [sp.simplify(nut_t - (sp.diff(eta0, s, th) - kap * eta0t / s - kap * th * sp.diff(eta0, th, 2) / s))]
checks['s d_s nut'] = [sp.simplify(sds_nut - (s * sp.diff(eta0, s, 2) - kap * th * (sp.diff(eta0, s, th) - eta0t / s) - lam * z / s))]

# (3.7): g = s^beta (F(s^(1/N), th, z s^(-c)) + a0), rho*Y g = s*(g_s - kap th/s g_th + lam z/s g_z)
F = sp.Function('F')
sig = s**(1 / N)
e = z * s**(-c)
g = s**beta * (F(sig, th, e) + a0)
rhoYg = s * sp.diff(g, s) - kap * th * sp.diff(g, th) + lam * z * sp.diff(g, z)
S1, T1, E1 = sp.symbols('S1 T1 E1')
Fs = sp.Derivative(F(S1, T1, E1), S1).subs({S1: sig, T1: th, E1: e})
Ft = sp.Derivative(F(S1, T1, E1), T1).subs({S1: sig, T1: th, E1: e})
Fe = sp.Derivative(F(S1, T1, E1), E1).subs({S1: sig, T1: th, E1: e})
c2 = c - lam
rhs37 = s**beta * (kap * th * Ft + c2 * e * Fe - sig / N * Fs)
expr37 = sp.simplify((beta * g - rhoYg - rhs37).doit())
checks['3.7 Euler'] = [sp.simplify(sp.powsimp(sp.expand(expr37), force=True))]

ok_all = True
for name, vals in checks.items():
    ok = all(v == 0 for v in vals)
    ok_all &= ok
    print(f'{name:22s}', 'True' if ok else vals)

# отрицательный контроль: если в (3.5) убрать lam*a^z*w_n, тождество должно нарушиться
neg = sp.simplify(lhs35 - (rhs35 - lam * az_ * wn))
print('neg. control (без lam a^z w_n) равен нулю?', neg == 0)
# отрицательный контроль для (3.7): c2 -> c
neg37 = sp.simplify(sp.powsimp(sp.expand((beta * g - rhoYg - s**beta * (kap * th * Ft + c * e * Fe - sig / N * Fs)).doit()), force=True))
print('neg. control (3.7) с c вместо c2 равен нулю?', neg37 == 0)
print('ALL', ok_all)
