"""R42: независимая проверка выкладок results/013 (модель, теорема 3.2, предложение 3.3, примеры).
[Эксперимент] sympy. Запуск: ~/venv/bin/python check_model.py
"""
import sympy as sp

x, y, z, eps, r, t1, t2, eta = sp.symbols('x y z epsilon r theta1 theta2 eta', real=True)
ok = lambda e: sp.simplify(sp.expand(e)) == 0

# --- Модель
U = x**2*y**2 + eps*z**2*(x**4+y**4) - z**6 + x**6 + y**6
g = [sp.diff(U, v) for v in (x, y, z)]
print('3.1(a) grad:',
      ok(g[0]-2*x*(y**2+2*eps*z**2*x**2+3*x**4)),
      ok(g[1]-2*y*(x**2+2*eps*z**2*y**2+3*y**4)),
      ok(g[2]-2*z*(eps*(x**4+y**4)-3*z**4)))

# 3.1(c): U + r^6 = x^2y^2 + B
rr2 = x**2+y**2+z**2
s = x**2+y**2
B = eps*z**2*(x**4+y**4)+x**6+y**6+s*(rr2**2+rr2*z**2+z**4)
print('3.1(c) U+r^6 = x^2y^2+B:', ok(U+rr2**3-x**2*y**2-B))

# 3.1(d): гномоническая карта
c = (1+t1**2+t2**2)**sp.Rational(-1, 2)
sub = {x: r*c*t1, y: r*c*t2, z: r*c}
E = eps*(t1**4+t2**4)+t1**6+t2**6
lhs = U.subs(sub)
rhs = r**4*c**4*t1**2*t2**2 + r**6*c**6*(-1+E)
print('3.1(d) (1):', sp.simplify(lhs-rhs) == 0)
Lam = 1-c**6+c**6*E
Wc = r**-2*c**4*t1**2*t2**2 + Lam
print('3.1(d) (2):', sp.simplify(r**-6*lhs+1-Wc) == 0)
tt = sp.symbols('t', nonnegative=True)
print('Lambda series:', sp.series(Lam.subs({t1: tt, t2: 0}), tt, 0, 5))

# 3.1(e)
ph = sp.symbols('varphi', real=True)
G = (U.subs({x: sp.sin(ph), y: 0, z: sp.cos(ph)}))
print('3.1(e) G(0), G\'\'(0):', sp.simplify(G.subs(ph, 0)), sp.simplify(sp.diff(G, ph, 2).subs(ph, 0)))

# Теорема 3.2 (S2): тождества
th_grad = lambda f: t1*sp.diff(f, t1)+t2*sp.diff(f, t2)
tsym = t1**2+t2**2
print('S2: theta.grad(c^4 t1^2 t2^2) = 4c^6 t1^2t2^2:',
      sp.simplify(th_grad(c**4*t1**2*t2**2)-4*c**6*t1**2*t2**2) == 0)
kap = sp.symbols('kappa', positive=True)
S2lhs = -r*sp.diff(Wc, r) + kap*th_grad(Wc) - kap*Wc
S2rhs = (2+4*kap*c**2-kap)*c**4*t1**2*t2**2/r**2 + kap*(th_grad(Lam)-Lam)
print('S2 decomposition:', sp.simplify(S2lhs-S2rhs) == 0)
print('theta.grad c^6 = -6 t c^8:', sp.simplify(th_grad(c**6)+6*tsym*c**8) == 0)
print('theta.grad E = 4E+2(t1^6+t2^6):', sp.simplify(th_grad(E)-4*E-2*(t1**6+t2**6)) == 0)
expr = 6*tsym*(1+tsym)**-4 - (1-c**6) + c**6*((3-6*tsym*c**2)*E + 2*(t1**6+t2**6))
print('theta.grad Lam - Lam formula:', sp.simplify(th_grad(Lam)-Lam-expr) == 0)

# численно: Lambda >= 2t и theta.grad Lam - Lam >= 0 при t <= 1/(9+|eps|), с запасом по сетке
import numpy as np
fL = sp.lambdify((t1, t2, eps), Lam, 'numpy')
fD = sp.lambdify((t1, t2, eps), th_grad(Lam)-Lam, 'numpy')
worst1, worst2 = np.inf, np.inf
for ev in [-1000, -100, -30, -10, -3, -1, -0.3, 0, 0.3, 1, 3, 10, 30, 100, 1000]:
    t0 = 1/(9+abs(ev))
    rad = np.sqrt(t0)*np.linspace(1e-4, 1, 400)
    ang = np.linspace(0, 2*np.pi, 401)
    R_, A_ = np.meshgrid(rad, ang)
    T1, T2 = R_*np.cos(A_), R_*np.sin(A_)
    tv = T1**2+T2**2
    worst1 = min(worst1, np.min(fL(T1, T2, ev)/tv - 2))
    worst2 = min(worst2, np.min(fD(T1, T2, ev)/tv))
print('min(Lambda/t - 2) =', worst1, ';  min((th.grad L - L)/t) =', worst2)

# Предложение 3.3: 6W - z W_z - 4W = 2(x^6+x^2y^2+y^6)
W = U + z**6
print('3.3 (L2) identity:', ok(6*W - z*sp.diff(W, z) - 4*W - 2*(x**6+x**2*y**2+y**6)))
a, b = sp.symbols('a b', nonnegative=True)
print('(a+b)^3 <= 4(a^3+b^3): 4(a^3+b^3)-(a+b)^3 =', sp.factor(4*(a**3+b**3)-(a+b)**3))

# Замечание 1: решение на оси
z0, tt2 = sp.symbols('z0 t', positive=True)
zt = z0*(1+2*sp.sqrt(2)*z0**2*tt2)**sp.Rational(-1, 2)
print('axis solution: zdot + sqrt(2) z^3 =', sp.simplify(sp.diff(zt, tt2)+sp.sqrt(2)*zt**3))
# Замечание 2: eps=-10
print('eps=-10 point:', sp.simplify(U.subs({eps: -10, x: r/sp.sqrt(2), y: 0, z: r/sp.sqrt(2)})/r**6))
