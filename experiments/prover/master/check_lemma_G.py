"""
[Эксперимент] Символьная проверка формул леммы G записки notes/prover/2026-10-21-master.md.

Однородная карта Pi(s,th) = s*Om(th), th = (p1,p2) in R^2, n = 3; Om -- ПРОИЗВОЛЬНЫЕ функции
(sympy Function), поле Y(Pi(s,th)) = y(s,th) := Om + DOm v, v = (v1,v2)(s,th) -- произвольные функции.
Производная D_w Y в точке q = Pi(s,th) по направлению w = DPi(s,th)(a, tau/s) = a*Om + DOm tau
равна d/de y(s + e a, th + e tau/s) при e = 0, то есть a*d_s y + D_th y (tau/s).

Проверяются тождества:
 (G2) s*D_Y Y = DOm psi + D^2Om(v,v),  psi = v + D_th v . v + s d_s v ;
 (G3) s<w, D_w Y> = tau^T G (I + D_th v) tau + a t^T (I + D_th v) tau + a <w, DOm s d_s v> + <w, D^2Om(v,tau)>,
      w = a Om + DOm tau, t = DOm^T Om, G = DOm^T DOm ;
 (G0) nu := B^{-T} e1 удовлетворяет <nu, DPi(s,th)(1,0)> = 1, <nu, DPi(s,th)(0,e_j)> = 0
      (то есть nu = grad rho, rho = s o Pi^{-1});
 (G1) <nu, y> = 1 (Y rho = 1).
Также (численно, случайные точки) -- бесчартовое тождество
 |grad rho - Y/h|^2 = |nu|^4 |Y_T|^2 / (1 + |nu|^2 |Y_T|^2),  Y_T := Y - <Y,nu> nu/|nu|^2 .
"""
import sympy as sp
import random

s, p1, p2, a, t1, t2 = sp.symbols('s p1 p2 a tau1 tau2', real=True)
th = [p1, p2]
Om = sp.Matrix([sp.Function('O%d' % i)(p1, p2) for i in range(3)])
v = sp.Matrix([sp.Function('v%d' % j)(s, p1, p2) for j in range(2)])
DOm = Om.jacobian(th)                       # 3x2
y = Om + DOm * v                            # Y o Pi

def Dth(F, z):
    """производная по th по направлению z (z -- 2-вектор)"""
    return sum((sp.diff(F, th[j]) * z[j] for j in range(2)), sp.zeros(F.shape[0], 1))

def D2Om(z1, z2):
    return sp.Matrix([sum(sp.diff(Om[i], th[j], th[k]) * z1[j] * z2[k]
                          for j in range(2) for k in range(2)) for i in range(3)])

# (G2)
DYY = sp.diff(y, s) + Dth(y, v / s)
Dthv = v.jacobian(th)
psi = v + Dthv * v + s * sp.diff(v, s)
res_G2 = sp.simplify(sp.expand(s * DYY - (DOm * psi + D2Om(v, v))))
print('(G2) s D_Y Y - [DOm psi + D2Om(v,v)] =', res_G2.T)

# (G3)
tau = sp.Matrix([t1, t2])
w = a * Om + DOm * tau
DwY = a * sp.diff(y, s) + Dth(y, tau / s)
G = DOm.T * DOm
t = DOm.T * Om
I2 = sp.eye(2)
rhs = (tau.T * G * (I2 + Dthv) * tau)[0] + a * (t.T * (I2 + Dthv) * tau)[0] \
      + a * (w.T * DOm * (s * sp.diff(v, s)))[0] + (w.T * D2Om(v, tau))[0]
res_G3 = sp.simplify(sp.expand(s * (w.T * DwY)[0] - rhs))
print('(G3) s<w,D_wY> - formula =', res_G3)

# (G0), (G1)
B = Om.row_join(DOm)                        # 3x3
nu = B.T.inv() * sp.Matrix([1, 0, 0])
DPi_s = Om
DPi_j = [s * DOm[:, j] for j in range(2)]
r0 = sp.simplify((nu.T * DPi_s)[0] - 1)
r1 = [sp.simplify((nu.T * DPi_j[j])[0]) for j in range(2)]
r2 = sp.simplify((nu.T * y)[0] - 1)
print('(G0) <nu,Om>-1 =', r0, '; <nu, s dOm/dth_j> =', r1)
print('(G1) <nu,y>-1 =', r2)

# бесчартовое тождество, численно
random.seed(1)
mx = 0
for trial in range(200):
    nu_n = sp.Matrix([random.uniform(-2, 2) for _ in range(3)])
    YT = sp.Matrix([random.uniform(-2, 2) for _ in range(3)])
    YT = YT - (YT.dot(nu_n) / nu_n.dot(nu_n)) * nu_n          # Y_T перпендикулярен nu
    Yv = nu_n / nu_n.dot(nu_n) + YT                             # <nu,Y> = 1
    h = Yv.dot(Yv)
    lhs = (nu_n - Yv / h).dot(nu_n - Yv / h)
    n2 = nu_n.dot(nu_n); y2 = YT.dot(YT)
    rhs_n = n2**2 * y2 / (1 + n2 * y2)
    mx = max(mx, abs(float(lhs - rhs_n)))
print('бесчартовое тождество: max |lhs - rhs| по 200 случайным точкам =', mx)
