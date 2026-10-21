"""[Эксперимент] Символьная проверка тождеств теоремы 2U (notes/prover/2026-10-21-point-degenerate.md, §4).

Карта Phi(x,b) = (x, gamma(x) + L(x) x^c b), поле Y = e_x + Zt,
  Zt = gamma' + L' x^c b + L x^{c-1} (c b - xi(s,b)),   s = x^{1/N}.
Проверяется:
  (I1)  Y . grad b_i = -xi_i / x;
  (I2)  x*Y.grad(x^beta P(s,b)) = x^beta [beta P + (s/N) P_s - xi . grad_b P];
  (I3)  M := x * d Zt / d y = x L' L^{-1} + L A L^{-1},  A_ij = x^{c_i-c_j} (c_i delta_ij - d_j xi_i);
  (I4)  x*Y.grad Zt = x gamma'' + x L'' x^c b + L' C x^c b + x L' x^{c-1}(c b - xi)
                      + L (C-I) x^{c-1}(c b - xi) - L' x^c xi - L x^{c-1}(C xi - D_b xi xi)
        + член от s-зависимости xi:  - L x^{c-1} (s/N) d_s xi.
Функции gamma, L, xi, P берутся конкретными (нелинейными, с дробными степенями), разность упрощается до 0
или вычисляется в случайных точках с 40 знаками.
"""
import random
import sympy as sp

x, y1, y2 = sp.symbols('x y1 y2', positive=True)
N = 2
c1, c2 = sp.Rational(3, 2), sp.Rational(7, 3)
c1f, c2f = c1, c2
beta = sp.Rational(13, 2)
s = x**sp.Rational(1, N)

g = sp.Matrix([x**sp.Rational(3, 2) / 3 - 2 * x**2, 5 * x**sp.Rational(5, 4)])
L = sp.Matrix([[1 + x / 3 + x**2, x**sp.Rational(1, 2) / 5], [-x / 7, 1 + x**sp.Rational(3, 2)]])
Cx = sp.diag(x**c1, x**c2)
C = sp.diag(c1, c2)
Y_minus_g = sp.Matrix([y1, y2]) - g
b = Cx.inv() * L.inv() * Y_minus_g
b = sp.Matrix([sp.simplify(e) for e in b])

B1, B2, S = sp.symbols('B1 B2 S')


def xi_fun(S_, B1_, B2_):
    return sp.Matrix([B1_ + B1_**2 / 3 - B1_ * B2_ / 5 + S_ * B1_,
                      2 * B2_ + B1_**3 - S_**2 * B2_ / 2 + S_ * B1_ * B2_])


def P_fun(S_, B1_, B2_):
    return B1_**4 - sp.Rational(3, 2) * B1_**2 * B2_ + B2_**2 + S_ * B1_**3 + S_**3 * B2_


xi_b = xi_fun(S, B1, B2)
Dxi_b = xi_b.jacobian([B1, B2])
subsb = {S: s, B1: b[0], B2: b[1]}
xi = xi_b.subs(subsb)
Dxi = Dxi_b.subs(subsb)
dsxi = sp.diff(xi_b, S).subs(subsb)

bvec = sp.Matrix([b[0], b[1]])
Zt = sp.diff(g, x) + sp.diff(L, x) * Cx * bvec + L * Cx * (C * bvec - xi) / x


def Ydot(f):
    return sp.diff(f, x) + Zt[0] * sp.diff(f, y1) + Zt[1] * sp.diff(f, y2)


random.seed(1)
pts = [(sp.Rational(random.randint(5, 60), 1000),
        None, None) for _ in range(6)]


def numcheck(expr, label):
    import mpmath as mp
    mp.mp.dps = 50
    f = sp.lambdify((x, y1, y2), expr, 'mpmath')
    gf = sp.lambdify(x, g, 'mpmath')
    Lf = sp.lambdify(x, L, 'mpmath')
    worst = mp.mpf(0)
    rnd = random.Random(7)
    for _ in range(8):
        xv = mp.mpf(rnd.randint(5, 60)) / 1000
        bb = mp.matrix([mp.mpf(rnd.randint(-90, 90)) / 100, mp.mpf(rnd.randint(-90, 90)) / 100])
        D = mp.matrix([[xv**mp.mpf(3)/2, 0], [0, xv**(mp.mpf(7)/3)]])
        yv = mp.matrix(gf(xv)) + mp.matrix(Lf(xv)) * D * bb
        val = f(xv, yv[0], yv[1])
        vals = list(val) if hasattr(val, 'rows') or isinstance(val, (list, tuple)) else [val]
        try:
            vals = [val[i, j] for i in range(val.rows) for j in range(val.cols)]
        except Exception:
            pass
        worst = max([worst] + [abs(v) for v in vals])
    print(f'{label}: max |difference| over 8 points = {mp.nstr(worst, 5)} (mp.dps=50)')
    return worst


# (I1)
I1 = sp.Matrix([Ydot(b[i]) + xi[i] / x for i in range(2)])
numcheck(I1, '(I1) Y.grad b_i + xi_i/x')

# (I2)
P = P_fun(s, b[0], b[1])
lhs = x * Ydot(x**beta * P)
Pb = P_fun(S, B1, B2)
rhs = x**beta * (beta * Pb + S / N * sp.diff(Pb, S) - (xi_b[0] * sp.diff(Pb, B1) + xi_b[1] * sp.diff(Pb, B2)))
rhs = rhs.subs(subsb)
numcheck(sp.Matrix([lhs - rhs]), '(I2) x Y.grad(x^beta P) - formula')

# (I3)
M = x * Zt.jacobian([y1, y2])
A = sp.Matrix(2, 2, lambda i, j: x**([c1, c2][i] - [c1, c2][j]) * ((C[i, j]) - Dxi[i, j]))
M_formula = x * sp.diff(L, x) * L.inv() + L * A * L.inv()
numcheck(M - M_formula, '(I3) M - (x L\'L^-1 + L A L^-1)')

# (I4)
Lp, Lpp = sp.diff(L, x), sp.diff(L, x, 2)
v = C * bvec - xi
I4f = (x * sp.diff(g, x, 2) + x * Lpp * Cx * bvec + Lp * C * Cx * bvec + x * Lp * Cx * v / x
       + L * (C - sp.eye(2)) * Cx * v / x - Lp * Cx * xi - L * Cx * (C * xi - Dxi * xi) / x
       - L * Cx * (s / N) * dsxi / x)
I4 = sp.Matrix([x * Ydot(Zt[i]) for i in range(2)]) - I4f
numcheck(I4, '(I4) x Y.grad Zt - formula')
