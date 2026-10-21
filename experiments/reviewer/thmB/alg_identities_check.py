"""[Эксперимент] Проверка алгебраических тождеств results/002-theorem-B.md (reviewer, 21.10.2026).
(1) (M1): B^T M0 B = M для B = M0^{-1/2} S^{1/2} M0^{1/2}, S = M0^{-1/2} M M0^{-1/2} (случайные SPD, seed 7);
(2) лемма 2, шаг 3: eps^{-2} Q(eps v - eps^2 eta) = Q(v) - eps H(v,eta) + eps^2 Q(eta);
(3) §4: U_+ = V(U)/(m+1) - U = r^{m+2} p, R(F)=1, R(W)=r q, лемма 5 A(U)=U -- символьно,
    с f, h -- произвольными функциями (одномерное L для простоты: l -- одна координата, метрика G(l));
(4) 2.1(e): точки пересечения окружности gamma с вещественной осью.
Запуск: ~/venv/bin/python alg_identities_check.py. Это не доказательство.
"""
import numpy as np
import sympy as sp
from scipy.linalg import sqrtm

rng = np.random.default_rng(7)
for k in range(5):
    X = rng.normal(size=(5, 5)); M0 = X @ X.T + 5*np.eye(5)
    Y = rng.normal(size=(5, 5)); M = Y @ Y.T + 5*np.eye(5)
    M0h = np.real(sqrtm(M0)); M0mh = np.linalg.inv(M0h)
    S = M0mh @ M @ M0mh; Sh = np.real(sqrtm(S))
    B = M0mh @ Sh @ M0h
    print('(1) |B^T M0 B - M| =', np.abs(B.T @ M0 @ B - M).max())

e = sp.symbols('epsilon')
v1, v2, h1, h2 = sp.symbols('v1 v2 h1 h2')
H = sp.Matrix([[3, 1], [1, 2]])
v = sp.Matrix([v1, v2]); et = sp.Matrix([h1, h2])
Q = lambda w: (w.T*H*w)[0]/2
lhs = Q(e*v - e**2*et)/e**2
rhs = Q(v) - e*(v.T*H*et)[0] + e**2*Q(et)
print('(2)', sp.simplify(lhs - rhs) == 0)

r, l, m = sp.symbols('r l m', positive=True)
f = sp.Function('f')(l); G = sp.Function('G')(l)
h = sp.Function('h')
eps = sp.sqrt(r)
F = r**(m+1)*f
W = r**(m+2)*h(l, eps)
U = F + W
gradf = sp.diff(f, l)/G                 # градиент в метрике G dl^2
D = (m+1)**2*f**2 + G*gradf**2          # |grad f|^2 = G gradf^2
Rop = lambda phi: ((m+1)*f*r*sp.diff(phi, r) + gradf*sp.diff(phi, l))/(r**(m+1)*D)
Vop = lambda phi: r*sp.diff(phi, r)
print('(3) R(F)=1:', sp.simplify(Rop(F) - 1) == 0)
Uplus = Vop(U)/(m+1) - U
he = sp.Symbol('he')
hfun = h(l, eps)
p = (hfun + eps*sp.diff(hfun, r)*2*eps/2)/(m+1)   # h_eps = dh/dr * 2 eps
print('    U_+ = r^{m+2} p:', sp.simplify(Uplus - r**(m+2)*p) == 0)
q = ((m+1)*f*((m+2)*hfun + eps*sp.diff(hfun, r)*2*eps/2) + gradf*sp.diff(hfun, l))/D
print('    R(W) = r q:', sp.simplify(Rop(W) - r*q) == 0)
Aop = lambda phi: Vop(phi)/(m+1) - Uplus/(1 + Rop(W))*Rop(phi)
print('    A(U) = U:', sp.simplify(Aop(U) - U) == 0)
c1 = -(m+1)*f*p/(D*(1 + r*q)); Yl = -p*gradf/(D*(1 + r*q))
Aop2 = lambda phi: Vop(phi)/(m+1) + r*(c1*Vop(phi) + Yl*sp.diff(phi, l))
print('    A = V/(m+1) + r(c1 V + Y) gives A(U)=U:', sp.simplify(Aop2(U) - U) == 0)

l0, L0 = sp.symbols('lambda0 Lambda', positive=True)
cen = (l0 + L0)/2; rad = (L0 - l0)/2 + l0/4
print('(4) gamma meets R at', sp.simplify(cen - rad), 'and', sp.simplify(cen + rad))
