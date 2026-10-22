"""Проверка леммы G прямым дифференцированием по q (без цепного правила через DPi).

[Эксперимент] рецензента R45.
(C) плоская калибровка, n = 3: q = (x, y1, y2), s = x, theta = y/x, Upsilon = e + E theta.
    Поле Y(q) = e + E(theta + v(s,theta)) выписано как функция q; D_w Y = (D_q Y) w.
    Сравниваем x<w, D_w Y> с (G3) и с формулой <w_y, M w_y> + w_x <w_y, x d_x Z>, M = x d_y Z.
(P) полярная калибровка, n = 3: Upsilon = omega(phi, th) (сферические углы), q -> (r, phi, th)
    явными формулами (atan2, acos). Сравниваем (G1)-(G3) численно в случайных точках.
v -- многочлены степени 2 со случайными коэффициентами (для (C) -- символьными).
"""
import itertools
import numpy as np
import sympy as sp

# ---------- (C) символьно ----------
x = sp.Symbol('x', positive=True)
y1, y2 = sp.symbols('y1 y2', real=True)
s, t1, t2 = sp.symbols('s t1 t2', real=True)


def generic_poly(vars_, deg, name):
    monos = [sp.Mul(*c) for d in range(deg + 1)
             for c in itertools.combinations_with_replacement(vars_, d)]
    coefs = sp.symbols(f'{name}0:{len(monos)}')
    return sum(c * mo for c, mo in zip(coefs, monos))


v_st = sp.Matrix([generic_poly((s, t1, t2), 2, f'a{i}_') for i in range(2)])
E = sp.Matrix([[0, 0], [1, 0], [0, 1]])
e = sp.Matrix([1, 0, 0])
th_q = sp.Matrix([y1 / x, y2 / x])
sub = {s: x, t1: y1 / x, t2: y2 / x}
v_q = v_st.subs(sub)
Zq = E * (th_q + v_q)
Yq = e + Zq
q = sp.Matrix([x, y1, y2])
DYq = Yq.jacobian(q)
al, ta1, ta2 = sp.symbols('alpha tau1 tau2')
tau = sp.Matrix([ta1, ta2])
Ups = e + E * th_q
w = al * Ups + E * tau
lhs = sp.simplify(x * (w.T * DYq * w)[0])
# (G3) в калибровке (C): G = I, k = theta, D^2Ups = 0
Dv = v_st.jacobian((t1, t2)).subs(sub)
dsv = sp.diff(v_st, s).subs(sub)
I2 = sp.eye(2)
k = th_q
rhs_G3 = (tau.T * (I2 + Dv) * tau)[0] + al * (k.T * (I2 + Dv) * tau)[0] + al * (w.T * E * (x * dsv))[0]
print('(C) (G3):', sp.simplify(lhs - rhs_G3) == 0)
wx = w[0]
wy = sp.Matrix([w[1], w[2]])
Zy = sp.Matrix([Zq[1], Zq[2]])
M = x * Zy.jacobian((y1, y2))
rhs_2U = (wy.T * M * wy)[0] + wx * (wy.T * (x * sp.diff(Zy, x)))[0]
print('(C) formula 2U:', sp.simplify(lhs - rhs_2U) == 0)
# (G2) в (C): x nabla_Y Y = E psi, psi = v + Dv v + s dsv
nabYY = DYq * Yq
psi = v_q + Dv * v_q + x * dsv
print('(C) (G2):', sp.simplify(x * nabYY - E * psi) == sp.zeros(3, 1))

# ---------- (P) численно, явная обратная карта ----------
X = sp.symbols('X1 X2 X3', real=True)
r = sp.sqrt(X[0]**2 + X[1]**2 + X[2]**2)
ph = sp.atan2(X[1], X[0])
thh = sp.acos(X[2] / r)
P, T = sp.symbols('P T', real=True)
omega = sp.Matrix([sp.sin(T) * sp.cos(P), sp.sin(T) * sp.sin(P), sp.cos(T)])
Domega = omega.jacobian((P, T))
rng = np.random.default_rng(7)
coef = rng.normal(size=(2, 10))
monos = [sp.Integer(1), s, P, T, s * s, s * P, s * T, P * P, P * T, T * T]
v_sym = sp.Matrix([sum(float(coef[i, j]) * monos[j] for j in range(10)) for i in range(2)])
y_field = omega + Domega * v_sym                     # функция (s,P,T)
Yfun = y_field.subs({s: r, P: ph, T: thh})           # функция q
Xv = sp.Matrix(X)
DY = Yfun.jacobian(Xv)
grad_rho = sp.Matrix([r]).jacobian(Xv).T
f_Y = sp.lambdify(X, Yfun, 'numpy')
f_DY = sp.lambdify(X, DY, 'numpy')
f_gr = sp.lambdify(X, grad_rho, 'numpy')
Dv_s = v_sym.jacobian((P, T))
dsv_s = sp.diff(v_sym, s)
D2om = [[sp.diff(omega, a, b) for b in (P, T)] for a in (P, T)]
f_jet = sp.lambdify((s, P, T), [omega, Domega, v_sym, Dv_s, dsv_s,
                                D2om[0][0], D2om[0][1], D2om[1][1]], 'numpy')
maxerr = {'G0': 0, 'G1': 0, 'G2': 0, 'G3': 0}
for trial in range(200):
    sv = rng.uniform(0.2, 2.0)
    Pv = rng.uniform(-2.5, 2.5)
    Tv = rng.uniform(0.3, 2.8)
    om, Dom, vv, Dvv, dsvv, d00, d01, d11 = [np.array(a, dtype=float) for a in f_jet(sv, Pv, Tv)]
    om = om.ravel(); vv = vv.ravel(); dsvv = dsvv.ravel()
    d00 = d00.ravel(); d01 = d01.ravel(); d11 = d11.ravel()

    def D2(a, b):
        return a[0] * b[0] * d00 + (a[0] * b[1] + a[1] * b[0]) * d01 + a[1] * b[1] * d11
    qv = sv * om
    Yv = np.array(f_Y(*qv), dtype=float).ravel()
    DYv = np.array(f_DY(*qv), dtype=float)
    gr = np.array(f_gr(*qv), dtype=float).ravel()
    B = np.column_stack([om, Dom])
    nu = np.linalg.inv(B).T[:, 0]
    maxerr['G0'] = max(maxerr['G0'], np.linalg.norm(gr - nu))
    h = Yv @ Yv
    YT = Yv - nu / (nu @ nu)
    # (G1): |nu - Y/h| <= |nu|^2 |Y_T| и равенство с |nu|^4|Y_T|^2/(1+|nu|^2|Y_T|^2)
    lhs1 = np.linalg.norm(gr - Yv / h)**2
    rhs1 = (nu @ nu)**2 * (YT @ YT) / (1 + (nu @ nu) * (YT @ YT))
    maxerr['G1'] = max(maxerr['G1'], abs(lhs1 - rhs1))
    psi = vv + Dvv @ vv + sv * dsvv
    maxerr['G2'] = max(maxerr['G2'], np.linalg.norm(sv * DYv @ Yv - (Dom @ psi + D2(vv, vv))))
    a_ = rng.normal(); t_ = rng.normal(size=2)
    wv = a_ * om + Dom @ t_
    G = Dom.T @ Dom
    kk = Dom.T @ om
    I2n = np.eye(2)
    rhs3 = t_ @ G @ (I2n + Dvv) @ t_ + a_ * kk @ (I2n + Dvv) @ t_ + a_ * wv @ Dom @ (sv * dsvv) + wv @ D2(vv, t_)
    maxerr['G3'] = max(maxerr['G3'], abs(sv * wv @ DYv @ wv - rhs3))
print('(P) max errors over 200 random points:', maxerr)
