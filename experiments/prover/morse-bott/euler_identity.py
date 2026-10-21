# [Эксперимент] Проверка тождества (2.5) results/010: для W(Psi(s,theta,zeta)) = s^j (F(s^{1/2},theta,zeta s^{-c}) + a0)
# и поля Y = d_s + upsilon(s,theta) d_theta (в координатах (s,theta,zeta)):
#   beta W - rho Y W = s^j [ -s upsilon F_theta + c e F_e - (varsigma/2) F_varsigma ],  beta = j, rho = s.
import sympy as sp
s, th, ze, a0, j, c = sp.symbols('s theta zeta a0 j c', positive=True)
F = sp.Function('F'); ups = sp.Function('upsilon')(s, th)
vs, e = sp.sqrt(s), ze*s**(-c)
g = s**j*(F(vs, th, e) + a0)
lhs = j*g - s*(sp.diff(g, s) + ups*sp.diff(g, th))
X, T, E = sp.symbols('X T E')
Fv = lambda k: sp.diff(F(X, T, E), k).subs({X: vs, T: th, E: e})
rhs = s**j*(-s*ups*Fv(T) + c*e*Fv(E) - vs/2*Fv(X))
print('(2.5) верно:', sp.simplify(sp.expand(lhs - rhs).doit()) == 0)
