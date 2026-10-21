"""
[Эксперимент] Символьная проверка формул леммы W записки notes/prover/2026-10-21-master.md.

Взвешенная треугольная карта: th = Theta(s,b) := P(s, u), u = s^A b, A = diag(a1,a2), a_i >= 0 -- символы.
P = (P1,P2)(s,u1,u2), xi = (X1,X2) -- ПРОИЗВОЛЬНЫЕ функции (sympy Function). Все функции записаны в
переменных (s,u); b = s^{-A} u. Производные:
  s d/ds при постоянном b:  (s Ds_b) f = s f_s + sum_k a_k u_k f_{u_k};
  d/db_j:                   Db_j f   = s^{a_j} f_{u_j}.
Поле в координатах (s,b): Y.grad s = 1, Y.grad b = -xi/s. Его угловая скорость v := s d(th)/ds вдоль потока.

Проверяются:
 (W0) v = s P_s + P_u ubar,  ubar := A u - s^A xi ;
 (W1) P_u^{-1} (I + D_th v) P_u = N,
      N := I + A + P_u^{-1}[ d_s P_u - D^2_u P(s^A xi, .) ] - s^A D_b xi s^{-A},   d_s P_u := (s Ds_b) P_u ;
 (W2) psi := v + s (dv/ds)_поток = s P_s + s(s P_s)_s + 2 (s P_{u s}) ubar + D^2_u P(ubar,ubar)
             + P_u[ (I+A) ubar - s^A ( A xi + (s Ds_b) xi - D_b xi . xi ) ].
"""
import sympy as sp

s = sp.symbols('s', positive=True)
u1, u2 = sp.symbols('u1 u2', real=True)
a1, a2 = sp.symbols('a1 a2', nonnegative=True)
u = [u1, u2]
avec = [a1, a2]
P = sp.Matrix([sp.Function('P%d' % i)(s, u1, u2) for i in range(1, 3)])
X = sp.Matrix([sp.Function('X%d' % i)(s, u1, u2) for i in range(1, 3)])
A = sp.diag(a1, a2)
SA = sp.diag(s**a1, s**a2)
SAi = sp.diag(s**(-a1), s**(-a2))
I2 = sp.eye(2)

def sDs_b(f):
    out = s * sp.diff(f, s)
    for k in range(2):
        out = out + avec[k] * u[k] * sp.diff(f, u[k])
    return out

def Db(f, j):
    return s**avec[j] * sp.diff(f, u[j])

def jac_b(F):
    return sp.Matrix(2, 2, lambda i, j: Db(F[i], j))

Pu = P.jacobian(u)
uvec = sp.Matrix(u)
ubar = A * uvec - SA * X

def D2P(z1, z2):
    return sp.Matrix([sum(sp.diff(P[i], u[k], u[j]) * z1[k] * z2[j]
                          for k in range(2) for j in range(2)) for i in range(2)])

def D2P_mat(z):
    return sp.Matrix(2, 2, lambda i, j: sum(sp.diff(P[i], u[k], u[j]) * z[k] for k in range(2)))

# (W0)
v = sDs_b(P) - jac_b(P) * X
v_f = s * sp.diff(P, s) + Pu * ubar
print('(W0):', sp.simplify(sp.expand(v - v_f)).T)

# (W1)
J = jac_b(P)
Dthv = jac_b(v) * J.inv()
dsPu = Pu.applyfunc(sDs_b)
S = sp.Matrix(2, 2, lambda i, j: s**avec[i] * Db(X[i], j) * s**(-avec[j]))
N_f = I2 + A + Pu.inv() * (dsPu - D2P_mat(SA * X)) - S
res1 = (Pu.inv() * (I2 + Dthv) * Pu - N_f).applyfunc(lambda e: sp.simplify(sp.powsimp(sp.expand(e), force=True)))
print('(W1):', res1)

# (W2)
psi = v + (v.applyfunc(sDs_b) - jac_b(v) * X)
DbX_X = jac_b(X) * X
psi_f = s * sp.diff(P, s) + s * sp.diff(s * sp.diff(P, s), s) + 2 * (s * sp.diff(Pu, s)) * ubar \
        + D2P(ubar, ubar) + Pu * ((I2 + A) * ubar - SA * (A * X + X.applyfunc(sDs_b) - DbX_X))
res2 = (psi - psi_f).applyfunc(lambda e: sp.simplify(sp.powsimp(sp.expand(e), force=True)))
print('(W2):', res2.T)
