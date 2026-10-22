"""[Эксперимент: символьные тождества, sympy] к записке notes/prover/2026-10-22-condition-T.md.

(1) Замена поля в функции Важевского: для Y' = Y + Theta (любые векторы в R^3), v = -lam Y + v_perp, v_perp ⊥ Y,
    V_Y = |v|^2/2 - <v,Y>^2/(2|Y|^2) + W:
        V_{Y'} - V_Y = [lam^2 h |Theta|^2 + 2 lam h <v_perp,Theta> - (<v_perp,Theta> - lam <Y,Theta>)^2] / (2 h'),
    h = |Y|^2, h' = |Y'|^2. Первый порядок по Theta: lam <v_perp, Theta> — поправка «C = lam <v_perp,Theta>».
(2) Плоская карта, Y = e_x + Z, Z_i = x^{c_i-1}(c_i b_i - xi_i(b)), b_i = u_i/x^{c_i} (поле (0.1) теоремы 2U [012]):
    x * <w, D_w Y> для w = (0, w1, w2) равно sum_{ij} x^{c_i-c_j} (c_i delta_ij - d_j xi_i) w_i w_j; коэффициент при w1 w2
    содержит x^{c_1-c_2} (-d_2 xi_1) -> infinity при c_1 < c_2, если (T) нарушено.
(3) Пример O1 [014]: Phi_0 = -1 + G1 G2 (th^, e), th^ = sin th cos th, реализуется многочленом
    U = sum_l z^l h_l(x, y), deg h_l = 4(6-l): U(s cos th, s sin th, s^4 e) = s^24 Phi_0(th, e).
(4) Профиль Qt2 модели U2: весовое поле Эйлера Cb = (2 b1, 3 b2) не удовлетворяет (Q3) [012]: min (Cb.grad Qt2)/Qt2 < 0.
"""
import numpy as np
import sympy as sp

# (1)
lam = sp.Symbol('lam', positive=True)
Y = sp.Matrix(sp.symbols('Y1:4', real=True))
T = sp.Matrix(sp.symbols('T1:4', real=True))
a = sp.Matrix(sp.symbols('a1:4', real=True))
vperp = a - Y * (a.dot(Y) / Y.dot(Y))           # общий вектор, ортогональный Y
v = -lam * Y + vperp


def VY(Yv):
    return v.dot(v) / 2 - v.dot(Yv)**2 / (2 * Yv.dot(Yv))


h, hp = Y.dot(Y), (Y + T).dot(Y + T)
rhs = (lam**2 * h * T.dot(T) + 2 * lam * h * vperp.dot(T) - (vperp.dot(T) - lam * Y.dot(T))**2) / (2 * hp)
print('(1) V_{Y+Theta} - V_Y - formula =', sp.simplify(sp.together(VY(Y + T) - VY(Y) - rhs)))
eps = sp.Symbol('eps')
lin = sp.diff((VY(Y + eps * T) - VY(Y)), eps).subs(eps, 0)
print('    first order in Theta minus lam<v_perp,Theta> =', sp.simplify(lin - lam * vperp.dot(T)))

# (2)
x = sp.Symbol('x', positive=True)
u1, u2, w1, w2 = sp.symbols('u1 u2 w1 w2', real=True)
c1, c2 = sp.symbols('c1 c2', positive=True)
xi1, xi2 = sp.Function('xi1'), sp.Function('xi2')
B1, B2 = u1 / x**c1, u2 / x**c2
Z1 = x**(c1 - 1) * (c1 * B1 - xi1(B1, B2))
Z2 = x**(c2 - 1) * (c2 * B2 - xi2(B1, B2))
DwY = [sp.diff(Zi, u1) * w1 + sp.diff(Zi, u2) * w2 for Zi in (Z1, Z2)]
form = sp.expand(x * (w1 * DwY[0] + w2 * DwY[1]))
b1s, b2s = sp.symbols('b1 b2', real=True)
form = form.subs({u1: b1s * x**c1, u2: b2s * x**c2})
d1x1 = sp.Derivative(xi1(b1s, b2s), b1s); d2x1 = sp.Derivative(xi1(b1s, b2s), b2s)
d1x2 = sp.Derivative(xi2(b1s, b2s), b1s); d2x2 = sp.Derivative(xi2(b1s, b2s), b2s)
expected = ((c1 - d1x1) * w1**2 + (c2 - d2x2) * w2**2
            + x**(c1 - c2) * (-d2x1) * w1 * w2 + x**(c2 - c1) * (-d1x2) * w1 * w2)
diff2 = sp.simplify(sp.powsimp(sp.expand(form.doit() - expected.doit()), force=True))
print('(2) x<w,D_wY> - [sum x^{c_i-c_j}(c_i delta_ij - d_j xi_i) w_i w_j] =', diff2)

# (3)
th, e, s, X, Yy, Zz = sp.symbols('th e s x y z', real=True)
k = sp.Rational(199, 100)
TH = sp.Symbol('T')
G1 = e**2 + k * TH**2 * e + TH**4
G2 = TH**2 + k * TH * e**2 + e**4
Phi = sp.expand(-1 + G1 * G2)
P = sp.Poly(Phi, e, TH)
U = 0
ok = True
for l in range(0, 7):
    coeff_l = sum(cf * TH**mon[1] for mon, cf in zip(P.monoms(), P.coeffs()) if mon[0] == l)
    D = 4 * (6 - l)
    Pl = sp.Poly(coeff_l, TH) if coeff_l != 0 else None
    hl = 0
    if Pl is not None:
        for (kk,), cf in zip(Pl.monoms(), Pl.coeffs()):
            if 2 * kk > D:
                ok = False
            hl += cf * (X * Yy)**kk * (X**2 + Yy**2)**sp.Rational(D - 2 * kk, 2)
    U += Zz**l * hl
print('(3) O1: all monomials th^k e^l of Phi_0 have 2k <= 4(6-l):', ok)
Us = sp.simplify(U.subs({X: s * sp.cos(th), Yy: s * sp.sin(th), Zz: s**4 * e}) / s**24
                 - Phi.subs(TH, sp.sin(th) * sp.cos(th)))
print('    U(s cos th, s sin th, s^4 e)/s^24 - Phi_0(th, e) =', sp.simplify(sp.expand_trig(Us)))
print('    U is a polynomial:', sp.Poly(sp.expand(U), X, Yy, Zz) is not None, '; lowest-degree form:',
      sp.factor(sum(t for t in sp.Add.make_args(sp.expand(U)) if sp.Poly(t, X, Yy, Zz).total_degree() == 6)))

# (4)
bb1, bb2 = np.meshgrid(np.linspace(-0.3, 0.3, 1201), np.linspace(-0.55, 0.55, 2201))
s1 = bb1 - bb2**2; s2_ = bb1 - bb2**2 - bb2**3
A = s1**2 + bb2**8; B = s2_**2 + bb2**8
Q = A * B + bb1**24
Q1 = 2 * s1 * B + A * 2 * s2_ + 24 * bb1**23
Q2 = (-4 * bb2 * s1 + 8 * bb2**7) * B + A * (2 * s2_ * (-2 * bb2 - 3 * bb2**2) + 8 * bb2**7)
r = np.where(Q > 0, (2 * bb1 * Q1 + 3 * bb2 * Q2) / np.where(Q > 0, Q, 1), np.inf)
i = np.unravel_index(np.argmin(r), r.shape)
print(f'(4) Qt2: min (Cb.grad Q)/Q on grid |b1|<=0.3, |b2|<=0.55 = {r[i]:.4g} at b=({bb1[i]:.4f},{bb2[i]:.4f}), Q={Q[i]:.3e}')
for rad in (0.3, 0.1, 0.03):
    m = (np.abs(bb1) <= rad**2) & (np.abs(bb2) <= rad)
    j = np.argmin(np.where(m, r, np.inf))
    print(f'    restricted to |b1|<={rad**2:.4f}, |b2|<={rad}: min = {r.flat[j]:.4g} at b=({bb1.flat[j]:.5f},{bb2.flat[j]:.4f})')
