"""R39: symbolic check of identities (I1)-(I4) of results/012-free-field.md, Section 5.1.

[Experiment] Generic smooth functions gamma_i(x), L_ij(x) (full 2x2 matrix), xi_i(x,b), P(x,b),
symbolic weights c1, c2 and exponent beta. Computation in coordinates (x,b), y = gamma + L x^c b.
For a function f(x,b):  d_y f = grad_b f * J^{-1},  d_x|_y f = d_x|_b f - grad_b f * J^{-1} d_x|_b y,
J = d y / d b = L x^c.  Y.grad f = d_x|_y f + d_y f . Ztilde.
The term (s/N) d_s xi in (I4) equals x d_x|_b xi when xi is written as a function of (x,b);
this is checked separately (chain rule) at the end.
Run:  ~/venv/bin/python check_identities.py
"""
import sympy as sp

x, b1, b2 = sp.symbols('x b1 b2', positive=True)
c1, c2, beta, N = sp.symbols('c1 c2 beta N', positive=True)

g = sp.Matrix([sp.Function('g1')(x), sp.Function('g2')(x)])
L = sp.Matrix(2, 2, lambda i, j: sp.Function(f'L{i+1}{j+1}')(x))
xi = sp.Matrix([sp.Function('xi1')(x, b1, b2), sp.Function('xi2')(x, b1, b2)])
P = sp.Function('P')(x, b1, b2)
b = sp.Matrix([b1, b2])
cs = [c1, c2]
C = sp.diag(c1, c2)
Xc = sp.diag(x**c1, x**c2)
Xc1 = sp.diag(x**(c1 - 1), x**(c2 - 1))

y = g + L * Xc * b
Zt = g.diff(x) + L.diff(x) * Xc * b + L * Xc1 * (C * b - xi)
J = L * Xc
Jinv = J.inv()
dyx = y.diff(x)


def gradb(f):
    return sp.Matrix([[f.diff(b1), f.diff(b2)]])


def Yder(f):
    gb = gradb(f)
    dy = gb * Jinv
    dx = f.diff(x) - (gb * Jinv * dyx)[0]
    return sp.simplify(dx + (dy * Zt)[0])


def zero(e):
    e = sp.simplify(sp.powsimp(sp.expand(e), force=True))
    return e == 0


# (I1)
I1 = Jinv * (Zt - dyx) + xi / x
print('(I1) Y.grad b + xi/x == 0 :', all(zero(e) for e in I1))
# also check via Yder on b_i
print('(I1) via operator        :', all(zero(Yder(b[i]) + xi[i] / x) for i in range(2)))

# (I2)
W = x**beta * P
lhs = x * Yder(W)
rhs = x**beta * (beta * P + x * P.diff(x) - (xi[0] * P.diff(b1) + xi[1] * P.diff(b2)))
print('(I2)                     :', zero(lhs - rhs))

# (I3)
dZb = Zt.jacobian(b)
Mcal = x * dZb * Jinv
Dxi = xi.jacobian(b)
Acal = sp.Matrix(2, 2, lambda i, j: x**(cs[i] - cs[j]) * ((cs[i] if i == j else 0) - Dxi[i, j]))
M_formula = x * L.diff(x) * L.inv() + L * Acal * L.inv()
print('(I3)                     :', all(zero(e) for e in (Mcal - M_formula)))

# (I4)
xYZ = sp.Matrix([x * Yder(Zt[i]) for i in range(2)])
Lp, Lpp = L.diff(x), L.diff(x, 2)
I = sp.eye(2)
xi_x = xi.diff(x)  # x * xi_x plays the role of (s/N) d_s xi
formula = (x * g.diff(x, 2) + x * Lpp * Xc * b + Lp * C * Xc * b + Lp * Xc * (C * b - xi)
           + L * (C - I) * Xc1 * (C * b - xi) - Lp * Xc * xi
           - L * Xc1 * (C * xi - Dxi * xi) - L * Xc1 * (x * xi_x))
print('(I4)                     :', all(zero(e) for e in (xYZ - formula)))

# chain rule: x d/dx [f(x^{1/N}, b)] = (s/N) f_s(s, b), s = x^{1/N}
s = sp.symbols('s', positive=True)
f = sp.Function('f')
expr = x * sp.diff(f(x**(1 / N), b1), x)
target = (s / N * sp.diff(f(s, b1), s)).subs(s, x**(1 / N))
print('chain rule x d_x = (s/N) d_s :', sp.simplify(expr.doit() - target.doit()) == 0)

# Sensitivity control: a deliberately wrong (I1) (sign of xi) must fail
print('control (wrong sign) fails :', not all(zero(e) for e in (Jinv * (Zt - dyx) - xi / x)))

# More sensitivity controls: drop a term of (I4); perturb (I3)
bad4 = formula + L * Xc1 * (x * xi_x)
print('control (I4 without s d_s xi term) fails :', not all(zero(e) for e in (xYZ - bad4)))
Abad = sp.Matrix(2, 2, lambda i, j: x**(cs[j] - cs[i]) * ((cs[i] if i == j else 0) - Dxi[i, j]))
print('control (I3 with x^{c_j-c_i}) fails      :',
      not all(zero(e) for e in (Mcal - (x * L.diff(x) * L.inv() + L * Abad * L.inv()))))
