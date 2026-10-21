"""Проверки к results/007-gt3.md (обозначения результата, а не записки).

[Эксперимент]: символьная/численная проверка выкладок; не доказательство.
Запуск: ~/venv/bin/python check_result007.py
"""
import sympy as sp
import mpmath as mp
import random

ok = True
def report(name, cond):
    global ok
    ok = ok and bool(cond)
    print(f"[{'OK' if cond else 'FAIL'}] {name}")

# ---------- (5.2): beta*W - x*dW/dx при фиксированном u ----------
x, beta, N = sp.symbols('x beta N', positive=True)
c1, c2, u1, u2 = sp.symbols('c1 c2 u1 u2', positive=True)
Fs = sp.Function('F')
s = x**(1/N)
b1, b2 = u1*x**(-c1), u2*x**(-c2)
F0_0 = sp.Symbol('F00')
S_, B1, B2 = sp.symbols('S_ B1 B2')
# проверка на конкретной (достаточно общей) функции F(s, b1, b2)
a, bb, cc = sp.symbols('a bb cc')
Fexpr = sp.exp(a*S_) * (1 + B1**2*bb + B1*B2*cc) + sp.sin(S_*B2)
Fx = Fexpr.subs({S_: s, B1: b1, B2: b2})
Wx = x**beta*(Fx - F0_0)
lhs = beta*Wx - x*sp.diff(Wx, x)
rhs = x**beta*(c1*B1*sp.diff(Fexpr, B1) + c2*B2*sp.diff(Fexpr, B2) - S_/N*sp.diff(Fexpr, S_))
rhs = rhs.subs({S_: s, B1: b1, B2: b2})
report("(5.2) beta W - rho YW = x^beta[sum c_i b_i dF/db_i - (s/N) dF/ds]", sp.simplify(lhs - rhs) == 0)

# ---------- константы шага 5 теоремы 2 ----------
a0, C1, lam0, dl, mu = sp.symbols('a0 C1 lambda0 delta mu', positive=True)
a1 = a3 = a0; a2 = beta*a0; h0 = sp.Rational(1, 2); h1 = sp.Rational(3, 2)
L1 = 2*(a2 + beta*a1/2)*sp.sqrt(h1/a1)
L2 = 2*sp.sqrt(2*a3/h0)
report("L1 = 3 beta sqrt(3 a0/2)", sp.simplify(L1 - 3*beta*sp.sqrt(3*a0/2)) == 0)
report("L2 = 4 sqrt(a0)", sp.simplify(L2 - 4*sp.sqrt(a0)) == 0)
Rb = 2*sp.sqrt(dl/lam0)
expr = L2*C1*Rb**2/sp.sqrt(dl) + 4*C1*Rb
report("(V1): L2 C1 Rb^2/sqrt(delta)+4 C1 Rb = (16 sqrt(a0) C1/lambda0 + 8 C1/sqrt(lambda0)) sqrt(delta)",
       sp.simplify(expr - (16*sp.sqrt(a0)*C1/lam0 + 8*C1/sp.sqrt(lam0))*sp.sqrt(dl)) == 0)

# ---------- пример 13: репер, карта, производные ----------
X, xi, eta = sp.symbols('X xi eta', real=True)
th = sp.Symbol('theta', real=True)
phi0 = 5*sp.pi/6
phi = phi0 + sp.sqrt(2)*th
Nh = sp.Matrix([sp.cos(phi), sp.sin(phi), 1])/sp.sqrt(2)
nu = sp.Matrix([sp.cos(phi), sp.sin(phi), -1])/sp.sqrt(2)
tau = sp.Matrix([-sp.sin(phi), sp.cos(phi), 0])
report("dN/dtheta = tau", sp.simplify(Nh.diff(th) - tau) == sp.zeros(3, 1))
report("dnu/dtheta = tau", sp.simplify(nu.diff(th) - tau) == sp.zeros(3, 1))
report("dtau/dtheta = -(N+nu)", sp.simplify(tau.diff(th) + Nh + nu) == sp.zeros(3, 1))
G = sp.Matrix.hstack(Nh, nu, tau)
report("(N, nu, tau) ортонормирован", sp.simplify(G.T*G - sp.eye(3)) == sp.zeros(3, 3))

ell = sp.sqrt(X**2 + xi**2)
theta = sp.atan(xi/X)
sub = {th: theta}
Phi = (ell*Nh + eta*nu).subs(sub)
cth, sth = X/ell, xi/ell        # cos theta, sin theta
eps = eta/ell
Nt, nut, taut = Nh.subs(sub), nu.subs(sub), tau.subs(sub)
formulas = {
    'd_X Phi': (Phi.diff(X), cth*Nt - (1+eps)*sth*taut),
    'd_xi Phi': (Phi.diff(xi), sth*Nt + (1+eps)*cth*taut),
    'd_eta Phi': (Phi.diff(eta), nut),
    'd_X^2 Phi': (Phi.diff(X, 2), -eta*sth**2/ell**2*Nt - (1+eps)*sth**2/ell*nut + 2*eta*sth*cth/ell**2*taut),
    'd_xi d_X Phi': (Phi.diff(X).diff(xi), eta*sth*cth/ell**2*Nt + (1+eps)*sth*cth/ell*nut + eta*(sth**2-cth**2)/ell**2*taut),
    'd_eta d_X Phi': (Phi.diff(X).diff(eta), -sth/ell*taut),
}
mp.mp.dps = 40
random.seed(7)
pts = []
for _ in range(15):
    # точки области N: 0<X<s0, |b|<r0 при r0=1/4, s0=2/3
    Xv = random.uniform(0.01, 0.6)
    while True:
        t1, t2 = random.uniform(-0.25, 0.25), random.uniform(-0.25, 0.25)
        if t1*t1 + t2*t2 < 0.0625:
            break
    pts.append((mp.mpf(Xv), mp.mpf(t1*Xv), mp.mpf(t2*Xv**2)))
for name, (A_, B_) in formulas.items():
    f = sp.lambdify((X, xi, eta), A_ - B_, 'mpmath')
    err = max(max(abs(v) for v in f(*p)) for p in pts)
    report(f"{name}: формула §6.1 (макс. расхождение {mp.nstr(err, 3)})", err < mp.mpf(10)**-30)

J = Phi.jacobian([X, xi, eta])
Bm = J.T*J
k = 2*eps + eps**2
w = sp.Matrix([sth, -cth, 0])
fB = sp.lambdify((X, xi, eta), Bm - sp.eye(3) - k*w*w.T, 'mpmath')
err = max(max(abs(v) for v in fB(*p)) for p in pts)
report(f"B - I = k varpi varpi^T (макс. расхождение {mp.nstr(err, 3)})", err < mp.mpf(10)**-30)

# обратное отображение
x_, y_, z_ = Phi
R = sp.sqrt(x_**2 + y_**2)
inv_ell, inv_eta = (R + z_)/sp.sqrt(2), (R - z_)/sp.sqrt(2)
fI = sp.lambdify((X, xi, eta), sp.Matrix([inv_ell - ell, inv_eta - eta, sp.atan2(y_, x_) - (phi0 + sp.sqrt(2)*theta)]), 'mpmath')
err = max(max(abs(v) for v in fI(*p)) for p in pts)
report(f"обратное отображение: l=(R+z)/sqrt2, eta=(R-z)/sqrt2, arg=phi (макс. {mp.nstr(err, 3)})", err < mp.mpf(10)**-30)
fn = sp.lambdify((X, xi, eta), (Phi.T*Phi)[0] - ell**2 - eta**2, 'mpmath')
report("|Phi|^2 = l^2 + eta^2", max(abs(fn(*p)) for p in pts) < mp.mpf(10)**-30)

# U∘Phi = X^6 F(X,b)
xx, yy, zz = sp.symbols('x y z', real=True)
Q0 = xx**2 + yy**2 - zz**2
U = Q0**2 + zz**5*xx + zz**4*xx*yy + sp.Rational(1, 2)*zz**6
UPhi = U.subs({xx: x_, yy: y_, zz: z_})
B1s, B2s, Xs = sp.symbols('b1 b2 X_')
S = sp.sqrt(1 + B1s**2)
Lam = (S + Xs*B2s)/(S - Xs*B2s)
ph = phi0 + sp.sqrt(2)*sp.atan(B1s)
GamL = Lam*sp.cos(ph) + Lam**2*sp.cos(ph)*sp.sin(ph) + sp.Rational(1, 2)
Fex = 4*(1 + B1s**2)*B2s**2 + (S - Xs*B2s)**6/8*GamL
fU = sp.lambdify((X, xi, eta), UPhi, 'mpmath')
fF = sp.lambdify((Xs, B1s, B2s), Fex, 'mpmath')
err = max(abs(fU(*p) - p[0]**6*fF(p[0], p[1]/p[0], p[2]/p[0]**2))/p[0]**6 for p in pts)
report(f"U∘Phi = X^6 F(X, xi/X, eta/X^2) (макс. отн. расхождение {mp.nstr(err, 3)})", err < mp.mpf(10)**-30)

# та же F без деления: многочленная запись через S -/+ X b2
Fpoly = 4*(1 + B1s**2)*B2s**2 + sp.Rational(1, 8)*((S - Xs*B2s)**5*(S + Xs*B2s)*sp.cos(ph)
        + (S - Xs*B2s)**4*(S + Xs*B2s)**2*sp.cos(ph)*sp.sin(ph) + sp.Rational(1, 2)*(S - Xs*B2s)**6)
report("многочленная запись F совпадает с записью через Lambda", sp.simplify(Fpoly - Fex) == 0)

# угол между q и лучом N(0): |q/|q| - N(0)| <= |b| (1 + X)
N0 = Nh.subs(th, 0)
fang = sp.lambdify((X, xi, eta), sp.sqrt(((Phi/sp.sqrt((Phi.T*Phi)[0]) - N0).T*(Phi/sp.sqrt((Phi.T*Phi)[0]) - N0))[0]), 'mpmath')
worst = max(fang(*p)/(mp.sqrt((p[1]/p[0])**2 + (p[2]/p[0]**2)**2)*(1 + p[0])) for p in pts)
report(f"|q/|q| - N(0)| <= |b|(1+X) на точках N (макс. отношение {mp.nstr(worst, 4)})", worst <= 1)

F0 = Fex.subs(Xs, 0)
grad = [sp.nsimplify(sp.simplify(sp.diff(F0, v).subs({B1s: 0, B2s: 0}))) for v in (B1s, B2s)]
H = sp.Matrix(2, 2, lambda i, j: sp.simplify(sp.diff(F0, [B1s, B2s][i], [B1s, B2s][j]).subs({B1s: 0, B2s: 0})))
report("F0(0) = 1/16 - 3 sqrt3/32", sp.simplify(F0.subs({B1s: 0, B2s: 0}) - (sp.Rational(1, 16) - 3*sp.sqrt(3)/32)) == 0)
report("grad F0(0) = 0", all(sp.simplify(g) == 0 for g in grad))
report("H = diag((6-3sqrt3)/16, 8)", sp.simplify(H - sp.diag((6 - 3*sp.sqrt(3))/16, 8)) == sp.zeros(2, 2))
report("d_b1 d_b2 [4(1+b1^2) b2^2] = 16 b1 b2", sp.simplify(sp.diff(4*(1+B1s**2)*B2s**2, B1s, B2s) - 16*B1s*B2s) == 0)
C = sp.diag(1, 2)
M = sp.simplify(C*H + H*C - H)
report("CH+HC-H = diag(H11, 24) > 0", M.is_diagonal() and M[1, 1] == 24 and sp.N(M[0, 0]) > 0)
# U(-q) = U(q)
report("U(-q) = U(q)", sp.expand(U.subs({xx: -xx, yy: -yy, zz: -zz}, simultaneous=True) - U) == 0)

# ---------- однородный случай: лучевое решение ----------
r, fval, bt = sp.symbols('r f beta', positive=True)
rdot = -sp.sqrt(2*fval)*r**(bt/2)          # f = |f(omega0)|
rddot = sp.diff(rdot, r)*rdot
report("луч: r'' = beta|f| r^(beta-1) при r' = -sqrt(2|f|) r^(beta/2)", sp.simplify(rddot - bt*fval*r**(bt - 1)) == 0)

# ---------- карта R16 для -|q|^2 при n=2 ----------
xs, us, kap = sp.symbols('x u kappa', positive=True)
bv = us/xs
Phi2 = sp.Matrix([xs - kap*us**2/xs, us])
Um = -(Phi2[0]**2 + Phi2[1]**2)
report("U∘Phi = x^2(-1+(2k-1)b^2-k^2 b^4) для -|q|^2",
       sp.simplify(Um - xs**2*(-1 + (2*kap - 1)*bv**2 - kap**2*bv**4)) == 0)
J2 = Phi2.jacobian([xs, us]); B2m = J2.T*J2
report("B_xu = -2 kappa b (1 + kappa b^2)", sp.simplify(B2m[0, 1] + 2*kap*bv*(1 + kap*bv**2)) == 0)

print("ВСЕ ПРОВЕРКИ ПРОШЛИ" if ok else "ЕСТЬ ОШИБКИ")
