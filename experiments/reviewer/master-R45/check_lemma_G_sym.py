"""Независимая символьная проверка леммы G (записка notes/prover/2026-10-21-master.md, §4.2).

[Эксперимент] рецензента R45. Идея: берём Upsilon(theta) -- многочлен степени 3 от theta
с произвольными символьными коэффициентами, v(s,theta) -- многочлен степени 2 от (s,theta)
с произвольными символьными коэффициентами; точка (s,theta) тоже символьная.
Поле Y строим как функцию точки q = s*Upsilon(theta): Y(q) = y(s,theta),
y = Upsilon + DUpsilon v. Производные Y по q считаем через цепное правило sympy:
D_q Y = D_{(s,theta)} y * (DPi)^{-1}. Сравниваем с формулами (G0)-(G3).

Так как формулы (G0)-(G3) -- поточечные тождества между 2-струёй Upsilon и 1-струёй v,
а символьные многочлены имеют произвольную 2-струю в произвольной точке, совпадение
тождеств для них означает совпадение для любых C^2-функций (это рассуждение, а не
только эксперимент; но скрипт помечен как [Эксперимент]).

Запуск: ~/venv/bin/python check_lemma_G_sym.py [n]   (по умолчанию n = 3)
"""
import sys
import itertools
import sympy as sp

n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
m = n - 1

s = sp.Symbol('s', positive=True)
th = sp.symbols(f't1:{m+1}')
al = sp.Symbol('alpha')
tau = sp.Matrix(sp.symbols(f'tau1:{m+1}'))


def generic_poly(vars_, deg, name):
    monos = [sp.Mul(*c) for d in range(deg + 1)
             for c in itertools.combinations_with_replacement(vars_, d)]
    coefs = sp.symbols(f'{name}0:{len(monos)}')
    return sum(c * mo for c, mo in zip(coefs, monos))


Ups = sp.Matrix([generic_poly(th, 3, f'u{i}_') for i in range(n)])
v = sp.Matrix([generic_poly((s,) + tuple(th), 2, f'v{i}_') for i in range(m)])

DUps = Ups.jacobian(th)                       # n x m
# вторая производная D^2Ups(a,b) = sum_ij a_i b_j d_i d_j Ups
def D2Ups(a, b):
    return sp.Matrix([sum(a[i] * b[j] * sp.diff(Ups[k], th[i], th[j])
                          for i in range(m) for j in range(m)) for k in range(n)])

Dv = v.jacobian(th)                           # m x m
dsv = sp.diff(v, s)                           # m x 1
I = sp.eye(m)

y = Ups + DUps * v                            # поле в точке Pi(s,theta)
Pi = s * Ups
J = Pi.jacobian((s,) + tuple(th))             # DPi, n x n
Dy = y.jacobian((s,) + tuple(th))             # n x n

B = Ups.row_join(DUps)                        # [Ups | DUps]
e1 = sp.Matrix([1] + [0] * m)

ok = {}

# B * diag(1, s I) = DPi
ok['DPi = B diag(1,sI)'] = sp.expand(J - B * sp.diag(1, *([s] * m))) == sp.zeros(n, n)

# (G0): grad rho = nu = B^{-T} e1. grad rho определяется из rho(Pi(s,th)) = s: J^T grad = e1.
# nu через присоединённую матрицу: nu = adj(B)^T e1 / det B.
detB = sp.expand(B.det())
adjB = B.adjugate()
nu_num = adjB.T * e1                          # nu = nu_num / detB
ok['(G0) J^T nu = e1'] = sp.expand(J.T * nu_num - detB * e1) == sp.zeros(n, 1)

# w = alpha Ups + DUps tau;  <nu, w> = alpha
w = al * Ups + DUps * tau
ok['(G0) <nu,w> = alpha'] = sp.expand((nu_num.T * w)[0] - al * detB) == 0
# <nu, Ups> = 1, DUps^T nu = 0
ok['<nu,Ups> = 1'] = sp.expand((nu_num.T * Ups)[0] - detB) == 0
ok['DUps^T nu = 0'] = sp.expand(DUps.T * nu_num) == sp.zeros(m, 1)
# <nu, Y> = 1  => Y_T = Y - nu/|nu|^2 = Ups_T + DUps v
ok['<nu,Y> = 1'] = sp.expand((nu_num.T * y)[0] - detB) == 0

# Прообраз w и Y при DPi: J (alpha, tau/s) = w, J (1, v/s) = Y  -- для цепного правила
xw = sp.Matrix([al] + list(tau / s))
xY = sp.Matrix([1] + list(v / s))
ok['J xw = w'] = sp.simplify(J * xw - w) == sp.zeros(n, 1)
ok['J xY = Y'] = sp.simplify(J * xY - y) == sp.zeros(n, 1)

# D_w Y = Dy * J^{-1} w = Dy * xw ;  nabla_Y Y = Dy * xY
DwY = Dy * xw
nabYY = Dy * xY

# (G2): s nabla_Y Y = DUps psi + D^2Ups(v,v),  psi = v + Dv v + s dsv
psi = v + Dv * v + s * dsv
lhs = sp.expand(s * nabYY)
rhs = sp.expand(DUps * psi + D2Ups(v, v))
ok['(G2)'] = sp.expand(lhs - rhs) == sp.zeros(n, 1)

# (G3) векторно: s D_w Y = DUps((I+Dv)tau + alpha s dsv) + D^2Ups(v,tau)
lhs_v = sp.expand(s * DwY)
rhs_v = sp.expand(DUps * ((I + Dv) * tau + al * s * dsv) + D2Ups(v, tau))
ok['(G3) vector'] = sp.expand(lhs_v - rhs_v) == sp.zeros(n, 1)

# (G3) скалярно
G = DUps.T * DUps
k = DUps.T * Ups
lhs_s = sp.expand((w.T * (s * DwY))[0])
rhs_s = sp.expand((tau.T * G * (I + Dv) * tau)[0] + al * (k.T * (I + Dv) * tau)[0]
                  + al * (w.T * DUps * (s * dsv))[0] + (w.T * D2Ups(v, tau))[0])
ok['(G3) scalar'] = sp.expand(lhs_s - rhs_s) == 0

# psi = v + s dv/ds вдоль Y:  d/dt v(s(t),th(t)) при ds/dt=1, dth/dt=v/s
dvdt = dsv + Dv * (v / s)
ok['psi = v + s dv/ds|_Y'] = sp.simplify(psi - (v + s * dvdt)) == sp.zeros(m, 1)

for key, val in ok.items():
    print(f'{key:28s} {val}')
print('ALL', all(ok.values()), 'n =', n)
