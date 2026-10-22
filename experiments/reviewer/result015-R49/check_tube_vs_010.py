"""R49: частный случай (T) леммы G против формул (5.1)-(5.3) из results/010-morse-bott.md.
[Эксперимент, символьно для произвольных функций k_g(theta), eta*(s,theta).]

Векторы — коэффициенты в репере Дарбу (omega, ell, n) точки theta; omega'=ell, ell'=-omega+k_g n,
n'=-k_g ell. Трубчатая калибровка Upsilon(theta,y)=omega+y n. Поле Y_kappa = Psi_s - (kappa theta/s) Psi_theta
([010], Psi(s,theta,zeta)=s omega+(eta*+zeta) n) имеет в координатах (s,theta,y), y=(eta*+zeta)/s,
угловую скорость v=(-kappa theta, nu - y), nu = eta*_s - kappa theta eta*_theta/s.
"""
import sympy as sp

s, th, y, kap, zeta = sp.symbols('s theta y kappa zeta')
kg = sp.Function('k')(th)
eta = sp.Function('eta')(s, th)
al, t1, t2 = sp.symbols('alpha tau1 tau2')


def dth(vec):
    """d/dtheta вектора с коэффициентами (a,b,c) в репере (omega,ell,n), коэффициенты зависят от theta."""
    a, b, c = vec
    # a' omega + a ell + b' ell + b(-omega + kg n) + c' n + c(-kg ell)
    return sp.Matrix([sp.diff(a, th) - b, a + sp.diff(b, th) - kg * c, sp.diff(c, th) + kg * b])


Ups = sp.Matrix([1, 0, y])
Ups_th = dth(Ups)
Ups_y = sp.diff(Ups, y)
Ups_thth = dth(Ups_th)
Ups_thy = sp.diff(Ups_th, y)
Ups_yy = sp.diff(Ups_y, y)
DU = sp.Matrix.hstack(Ups_th, Ups_y)


def D2(a, b):
    return Ups_thth * a[0] * b[0] + Ups_thy * (a[0] * b[1] + a[1] * b[0]) + Ups_yy * a[1] * b[1]


nu = sp.diff(eta, s) - kap * th * sp.diff(eta, th) / s
v = sp.Matrix([-kap * th, nu - y])
Dv = v.jacobian(sp.Matrix([th, y]))
dsv = sp.diff(v, s)
psi = v + Dv * v + s * dsv
eps = kg * y
# (5.1): Y = omega - kappa theta (1-eps) ell + nu n
Y = Ups + DU * v
print('(5.1) Y:', sp.simplify(Y - sp.Matrix([1, -kap * th * (1 - eps), nu])) == sp.zeros(3, 1))
# (5.2) via (G2)
G2 = DU * psi + D2(v, v)
# epsilon as function of [010] coordinates (s,theta,zeta): eps = kg (eta+zeta)/s ; then substitute zeta = s y - eta
eps_z = kg * (eta + zeta) / s
sub = {zeta: s * y - eta}
s_eps_s = sp.simplify((s * sp.diff(eps_z, s)).subs(sub))
eps_th = sp.simplify(sp.diff(eps_z, th).subs(sub))
nu_s, nu_th = sp.diff(nu, s), sp.diff(nu, th)
rhs52 = sp.Matrix([-kap ** 2 * th ** 2 * (1 - eps),
                   kap * th * (s_eps_s - 1 + kap * (1 - eps) - kap * th * eps_th + nu * kg),
                   s * nu_s + kap ** 2 * th ** 2 * (1 - eps) * kg - kap * th * nu_th])
print('(5.2) from (G2):', all(sp.simplify(sp.expand(x)) == 0 for x in (G2 - rhs52)))
# (5.3) via (G3): w = alpha Ups + DU tau ; frame is orthonormal
tau = sp.Matrix([t1, t2])
w = al * Ups + DU * tau
Gm = DU.T * DU
k = DU.T * Ups
I2 = sp.eye(2)
G3 = (tau.T * Gm * (I2 + Dv) * tau)[0] + al * (k.T * (I2 + Dv) * tau)[0] \
    + al * (w.T * DU * (s * dsv))[0] + (w.T * D2(v, tau))[0]
wo, wl, wn = w
eta_s, eta_th = sp.diff(eta, s), sp.diff(eta, th)
rhs53 = ((1 / (1 - eps) - kap) * wl ** 2 + kap * th * s_eps_s * wo * wl + s * nu_s * wo * wn + kap * th * wo * wl
         + (kap * th * eps_th - nu * kg) * wl ** 2 / (1 - eps) + nu_th * wl * wn / (1 - eps)
         - kap * th * kg * wl * (wo * eta_s + wl * eta_th / (s * (1 - eps))))
print('(5.3) from (G3):', sp.simplify(sp.expand(G3 - rhs53)) == 0)
