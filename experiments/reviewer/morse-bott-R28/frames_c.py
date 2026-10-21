"""R28: символьная проверка выкладок §2.3 и §4 (теорема Mc) записки
notes/prover/2026-10-21-morse-bott.md.  [Эксперимент]

Векторы записываются коэффициентами в подвижном репере (omega, T, n) кривой на S^2:
  omega' = T,  T' = -omega + k n,  n' = -k T   (производная по theta),
k(theta), eta*(s,theta) -- произвольные функции.

Проверяется:
 1. (2.5): Psi_s, Psi_theta, Psi_zeta для Psi = s*omega + (eta* + zeta) n;
 2. (N3): P_theta = (s - k eta) T;
 3. формула шага 8 теоремы Mc (= (6.7) при kappa = 0):
    s<w, D_w Y> = (1 - eta*_s k) w_T^2/(1-eps) + s eta*_ss w_om w_n + eta*_sth w_T w_n/(1-eps),
    Y = Psi_s, eps = k eta / s;
 4. nabla_Y Y = eta*_ss n;
 5. тождество Эйлера (4.1): beta W - rho Y W = s^j [c e dF/de - sigma/2 dF/dsigma].
"""
import sympy as sp

s, th, zeta = sp.symbols('s theta zeta', real=True)
k = sp.Function('k')(th)
es = sp.Function('etastar')(s, th)
eta = es + zeta
eps = k * eta / s


def d_theta(v):
    """Производная по theta вектора v = (a, b, c) = a*omega + b*T + c*n."""
    a, b, c = v
    # d(a omega) = a' omega + a T ; d(b T) = b' T + b(-omega + k n) ; d(c n) = c' n - c k T
    return (sp.diff(a, th) - b,
            sp.diff(b, th) + a - c * k,
            sp.diff(c, th) + b * k)


def d_s(v):
    return tuple(sp.diff(x, s) for x in v)


def d_zeta(v):
    return tuple(sp.diff(x, zeta) for x in v)


def dot(u, v):
    return sp.expand(sum(a * b for a, b in zip(u, v)))


def simp(v):
    return tuple(sp.simplify(x) for x in v)


Psi = (s, sp.Integer(0), eta)
Ps, Pt, Pz = d_s(Psi), d_theta(Psi), d_zeta(Psi)

ok1 = (sp.simplify(Ps[0] - 1) == 0 and Ps[1] == 0 and sp.simplify(Ps[2] - sp.diff(es, s)) == 0)
ok2 = (Pt[0] == 0 and sp.simplify(Pt[1] - s * (1 - eps)) == 0
       and sp.simplify(Pt[2] - sp.diff(es, th)) == 0)
ok3 = (Pz == (0, 0, 1))
print('(2.5) Psi_s  = omega + eta*_s n :', ok1)
print('(2.5) Psi_th = s(1-eps)T + eta*_th n :', ok2)
print('(2.5) Psi_z  = n :', ok3)

# (N3): P(s,theta,eta) = s omega + eta n с независимой eta
et = sp.Symbol('eta_ind', real=True)
P = (s, sp.Integer(0), et)
PT = d_theta(P)
print('(N3) P_theta = (s - k eta) T :', PT[0] == 0 and sp.simplify(PT[1] - (s - k * et)) == 0 and PT[2] == 0)

# Y = Psi_s как функция координат (s, theta, zeta); производные Y по координатам
Y = Ps
Y_s, Y_t, Y_z = d_s(Y), d_theta(Y), d_zeta(Y)
print('nabla_Y Y = d_s Psi_s = eta*_ss n :', simp(Y_s) == (0, 0, sp.diff(es, s, 2)))

# произвольный w = (w_om, w_T, w_n); разложение по базису Psi_s, Psi_theta, Psi_zeta
wo, wT, wn = sp.symbols('w_om w_T w_n', real=True)
a_s, a_t, a_z = sp.symbols('a_s a_t a_z')
sol = sp.solve([a_s * Ps[i] + a_t * Pt[i] + a_z * Pz[i] - w for i, w in enumerate((wo, wT, wn))],
               [a_s, a_t, a_z], dict=True)[0]
DwY = tuple(sol[a_s] * Y_s[i] + sol[a_t] * Y_t[i] + sol[a_z] * Y_z[i] for i in range(3))
lhs = s * dot((wo, wT, wn), DwY)
ess = sp.diff(es, s)
rhs = ((1 - ess * k) * wT**2 / (1 - eps) + s * sp.diff(es, s, 2) * wo * wn
       + sp.diff(es, s, th) * wT * wn / (1 - eps))
print('Mc шаг 8: s<w,D_wY> = формула :', sp.simplify(lhs - rhs) == 0)

# Тождество Эйлера (4.1)
j, c, a0 = sp.symbols('j c a_0', positive=True)
F = sp.Function('F')
sig = sp.sqrt(s)
e = zeta * s**(-c)
g = s**j * (F(sig, th, e) + a0)          # W(Psi(s,theta,zeta))
lhs = j * g - s * sp.diff(g, s)          # beta W - rho Y W,  Y = d/ds при фикс. (theta, zeta)
S, E = sp.symbols('S E')
Fse = F(S, th, E)
rhs = s**j * (c * E * sp.diff(Fse, E) - S / 2 * sp.diff(Fse, S))
rhs = rhs.subs({S: sig, E: e})
print('(4.1) beta W - rho YW = s^j[c e F_e - sigma/2 F_sigma] :', sp.simplify(sp.expand(lhs - rhs.doit())) == 0)

# (2.8): показатели
m = sp.Symbol('m', positive=True)
cc = (j - m + 2) / 2
print('(2.8) m-2+2c = j :', sp.simplify(m - 2 + 2 * cc - j) == 0,
      '; s^(c-1) = (s^(1/2))^(j-m) :', sp.simplify((cc - 1) - (j - m) / 2) == 0)
# запас Эйлера: c e d/de (h e^2/2) = 2c * (h e^2/2)
h = sp.Symbol('h', positive=True)
ee = sp.Symbol('e', real=True)
Qn = h * ee**2 / 2
print('c e Q_e = 2c Q :', sp.simplify(c * ee * sp.diff(Qn, ee) - 2 * c * Qn) == 0,
      '; mu = 2c <= beta = j  <=>  m >= 2 :', sp.simplify(2 * cc - (j - m + 2)) == 0)
