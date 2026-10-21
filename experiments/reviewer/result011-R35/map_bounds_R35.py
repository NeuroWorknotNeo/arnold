"""R35: end-to-end numeric test of (Phi1'), (Phi2''), (Phi3'') for the map (7.1) of results/011
on a CURVED arc (circle of latitude, k_g != 0) with a nontrivial approximate bottom
eta0 = s*y0(s^{1/N}, theta).  Everything is computed directly in R^3 from Phi(x,u,zeta)
(Jacobian, second derivatives), NOT from the frame formulas (7.2)-(7.6).
The smallness function varpi is taken POINTWISE (a lower bound of the sup in the text),
which makes the test stricter.  [Experiment]"""
import sympy as sp
import numpy as np

x, u, zt = sp.symbols('x u zeta', positive=True)
ka = sp.Rational(1, 8)
z0 = sp.Rational(3, 5)                 # latitude circle z = 3/5, radius 4/5
R = sp.sqrt(1 - z0**2)
N = 3
th = u * x**(-ka)
om = sp.Matrix([R * sp.cos(th / R), R * sp.sin(th / R), z0])
ell = sp.diff(om, u) / sp.diff(th, u)
nn = om.cross(ell)
kg_expr = sp.simplify((sp.diff(ell, u) / sp.diff(th, u)).dot(nn))  # ell' . n
print('k_g =', kg_expr)
A, B, Cc = sp.Rational(7, 10), sp.Rational(-13, 10), sp.Rational(9, 10)
TH = sp.Symbol('TH')
S = sp.Symbol('S', positive=True)
y0 = lambda sig, t: sig * (A + B * t + Cc * t**2) + sig**2 * sp.sin(t)
eta0 = S * y0(S**sp.Rational(1, N), TH)          # eta0(s, theta)
eta0_x = eta0.subs({S: x, TH: th})
Phi = x * om + (eta0_x + zt) * nn
X = [x, u, zt]
J = Phi.jacobian(X)
Yv = J[:, 0]
Phixx = sp.diff(Yv, x)
dY = [sp.diff(Yv, v) for v in X]   # columns d_j d_x Phi
fJ = sp.lambdify((x, u, zt), J, 'numpy')
fPxx = sp.lambdify((x, u, zt), Phixx, 'numpy')
fdY = sp.lambdify((x, u, zt), sp.Matrix.hstack(*dY), 'numpy')

# small quantities from their DEFINITIONS (eps = kg*eta/s, nu = eta0_s - k th eta0_th/s, ...)
kg = kg_expr
eta = eta0 + sp.Symbol('Z')
Z = sp.Symbol('Z')
eps = kg * eta / S
nu = sp.diff(eta0, S) - ka * TH * sp.diff(eta0, TH) / S
q8 = [eps, nu, sp.diff(eps, TH), S * sp.diff(eps, S), sp.diff(nu, TH), S * sp.diff(nu, S),
      S * sp.diff(eps, S) - ka * TH * sp.diff(eps, TH),   # x d_x eps at const (u,zeta)
      S * sp.diff(nu, S) - ka * TH * sp.diff(nu, TH)]
fq8 = sp.lambdify((S, TH, Z), q8, 'numpy')
fe0s = sp.lambdify((S, TH), [sp.diff(eta0, S), sp.diff(eta0, TH) / S], 'numpy')
kbar = abs(float(kg))
C1 = 1.25 * float(ka)**2 * (1 + kbar) + 4 * float(ka) * kbar
g1 = 1.25 * float(ka); g2 = float(ka) * (1 - float(ka))

rng = np.random.default_rng(1)
r0 = 0.25
worst = {'h': (9, -9), 'a': -9, 'b': -9, 'c': -9}
cnt = 0
for trial in range(4000):
    xv = 10**rng.uniform(-9, -2)
    thv = rng.uniform(-r0, r0) * 0.99
    ev = rng.uniform(-1, 1) * np.sqrt(max(r0**2 - thv**2, 0)) * 0.99
    uv = thv * xv**float(ka)
    zv = ev * xv**(float(1 + sp.Rational(1, 3)))   # c = 4/3
    Jv = np.array(fJ(xv, uv, zv), dtype=float)
    Y = Jv[:, 0]
    h = Y @ Y
    gradrho = np.linalg.inv(Jv)[0, :]
    Pxx = np.array(fPxx(xv, uv, zv), dtype=float).ravel()
    dYm = np.array(fdY(xv, uv, zv), dtype=float)
    q = np.abs(np.array(fq8(xv, thv, zv), dtype=float))
    es, et = fe0s(xv, thv)
    if abs(q[0]) > .25 or abs(q[1]) > .25 or abs(es) + 4 / 3 * abs(et) > 1:
        continue
    cnt += 1
    varpi = 10 * (1 + kbar) * q.sum()
    # orthonormal basis of Y^perp
    Yn = Y / np.sqrt(h)
    tmp = np.array([1., 0, 0]) if abs(Yn[0]) < .9 else np.array([0, 1., 0])
    e1 = tmp - (tmp @ Yn) * Yn; e1 /= np.linalg.norm(e1)
    e2 = np.cross(Yn, e1)
    P = np.vstack([e1, e2])
    # (a) |<grad rho - Y/h, w>| <= (g1|th| + varpi)|w|
    lhs_a = np.linalg.norm(P @ (gradrho - Y / h))
    worst['a'] = max(worst['a'], lhs_a - (g1 * abs(thv) + varpi))
    # (b) x|<Phi_xx, w>| <= (g2|th| + C1 th^2 + varpi)|w|
    lhs_b = xv * np.linalg.norm(P @ Pxx)
    worst['b'] = max(worst['b'], lhs_b - (g2 * abs(thv) + C1 * thv**2 + varpi))
    # (c) x<w, D_w Y> >= -(C1|th| + varpi)|w|^2 for w perp Y ; D_w Y = dYm @ J^{-1} w
    Jinv = np.linalg.inv(Jv)
    Mq = xv * (dYm @ Jinv)          # w -> x D_w Y
    Q2 = P @ Mq @ P.T
    lam_min = np.linalg.eigvalsh((Q2 + Q2.T) / 2).min()
    worst['c'] = max(worst['c'], -(C1 * abs(thv) + varpi) - lam_min)
    worst['h'] = (min(worst['h'][0], h), max(worst['h'][1], h))
print('points tested:', cnt)
print('h range:', worst['h'], ' (need within [1/2, 3/2])')
print('max violation (a) [<=0 ok]:', worst['a'])
print('max violation (b) [<=0 ok]:', worst['b'])
print('max violation (c) [<=0 ok]:', worst['c'])
