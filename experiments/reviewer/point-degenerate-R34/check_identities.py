"""R34: independent symbolic check of identities (I1)-(I4) of Theorem 2U
(notes/prover/2026-10-21-point-degenerate.md, Sec. 4.2) and of the theta_1, theta_3
decompositions used in Sec. 4.3, step 5.

Setting: n-1 = 2 transversal coordinates, generic functions:
  gamma(x) = (g1(x), g2(x)),  L(x) = [[l11,l12],[l21,l22]](x)  (generic 2x2),
  xi(s,b) = (xi1(s,b1,b2), xi2(s,b1,b2)), s = x**(1/N),
  weights c1, c2 > 0 symbolic, N symbolic positive.
Map: y = gamma(x) + L(x) x^c b,  b(x,y) = x^{-c} L^{-1} (y - gamma).
Field: Y = (1, Zt), Zt = gamma' + L' x^c b + L x^{c-1} (C b - xi).
[Experiment: sympy, exact symbolic simplification.]
"""
import sympy as sp

x, N = sp.symbols('x N', positive=True)
c1, c2, beta = sp.symbols('c1 c2 beta', positive=True)
y1, y2 = sp.symbols('y1 y2', real=True)
B1, B2 = sp.symbols('B1 B2', real=True)   # placeholders for b when b is independent
S = sp.Symbol('S', positive=True)

g1, g2 = sp.Function('g1')(x), sp.Function('g2')(x)
l11, l12, l21, l22 = [sp.Function(n)(x) for n in ('l11', 'l12', 'l21', 'l22')]
gam = sp.Matrix([g1, g2])
L = sp.Matrix([[l11, l12], [l21, l22]])
Linv = L.inv()
C = sp.diag(c1, c2)
xc = sp.diag(x**c1, x**c2)
xcm1 = sp.diag(x**(c1 - 1), x**(c2 - 1))
xmc = sp.diag(x**(-c1), x**(-c2))
s_of_x = x**(1/N)

xi1f, xi2f = sp.Function('xi1'), sp.Function('xi2')


def xi_vec(sv, bv):
    return sp.Matrix([xi1f(sv, bv[0], bv[1]), xi2f(sv, bv[0], bv[1])])


# b as a function of (x,y)
yv = sp.Matrix([y1, y2])
b_xy = xmc * Linv * (yv - gam)

# Zt as a function of (x,y): substitute b = b(x,y)
def Zt_of(bv):
    return gam.diff(x) + L.diff(x) * xc * bv + L * xcm1 * (C * bv - xi_vec(s_of_x, bv))

Zt_xy = Zt_of(b_xy)

# Y . grad applied to a function f(x,y)
def Ygrad(f):
    return f.diff(x) + Zt_xy[0] * f.diff(y1) + Zt_xy[1] * f.diff(y2)

# substitution y = gamma + L x^c B  (B independent symbols)
Bv = sp.Matrix([B1, B2])
y_of_B = gam + L * xc * Bv
subsY = {y1: y_of_B[0], y2: y_of_B[1]}

def at_B(expr):
    return sp.simplify(expr.subs(subsY))

ok = True

# ---- (I1): Y.grad b = -xi/x
I1 = sp.Matrix([Ygrad(b_xy[i]) for i in range(2)])
res = (I1.applyfunc(at_B) + xi_vec(s_of_x, Bv) / x).applyfunc(sp.simplify)
print('(I1) residual:', res.T)
ok &= res == sp.zeros(2, 1)

# ---- (I2): rho * Y.grad (x^beta P(s,b)) = x^beta [beta P + s/N dP/ds - xi.grad_b P]
Pf = sp.Function('P')
W_xy = x**beta * Pf(s_of_x, b_xy[0], b_xy[1])
lhs = at_B(x * Ygrad(W_xy))
Ps = Pf(S, B1, B2)
rhs = x**beta * (beta * Ps + S / N * Ps.diff(S)
                 - xi_vec(S, Bv)[0] * Ps.diff(B1) - xi_vec(S, Bv)[1] * Ps.diff(B2))
rhs = rhs.subs(S, s_of_x)
res2 = sp.simplify(sp.expand(lhs - rhs).doit())
print('(I2) residual:', res2)
ok &= res2 == 0

# ---- (I3): M = x d_y Zt = x L' L^{-1} + L A L^{-1},  A_ij = x^{c_i-c_j}(c_i delta_ij - d_bj xi_i)
M = sp.Matrix(2, 2, lambda i, j: x * Zt_xy[i].diff([y1, y2][j]))
M_B = M.applyfunc(at_B)
cs = [c1, c2]
Dxi = sp.Matrix(2, 2, lambda i, j: xi_vec(S, Bv)[i].diff([B1, B2][j])).subs(S, s_of_x)
A = sp.Matrix(2, 2, lambda i, j: x**(cs[i] - cs[j]) * ((cs[i] if i == j else 0) - Dxi[i, j]))
M_claim = x * L.diff(x) * Linv + L * A * Linv
res3 = (M_B - M_claim).applyfunc(lambda e: sp.simplify(sp.expand(e.doit())))
print('(I3) residual:', res3)
ok &= res3 == sp.zeros(2, 2)

# ---- (I4): x Y.grad Zt
I4 = sp.Matrix([x * Ygrad(Zt_xy[i]) for i in range(2)]).applyfunc(at_B)
xiB = xi_vec(S, Bv)
xis = xiB.diff(S)
I4_claim = (x * gam.diff(x, 2) + x * L.diff(x, 2) * xc * Bv + L.diff(x) * C * xc * Bv
            + L.diff(x) * xc * (C * Bv - xiB) + L * (C - sp.eye(2)) * xcm1 * (C * Bv - xiB)
            - L.diff(x) * xc * xiB - L * xcm1 * (C * xiB - Dxi.subs(s_of_x, S) * xiB)
            - L * xcm1 * (S / N) * xis)
I4_claim = I4_claim.subs(S, s_of_x)
res4 = (I4 - I4_claim).applyfunc(lambda e: sp.simplify(sp.expand(e.doit())))
print('(I4) residual:', res4.T)
ok &= res4 == sp.zeros(2, 1)

# ---- theta_1: |grad rho - Y/h|^2 = |Zt|^2/h with h = 1+|Zt|^2  (Zt arbitrary vector)
z1, z2 = sp.symbols('z1 z2', real=True)
h = 1 + z1**2 + z2**2
d = sp.Matrix([1 - 1 / h, -z1 / h, -z2 / h])
res5 = sp.simplify(d.dot(d) - (z1**2 + z2**2) / h)
print('theta_1 identity residual:', res5)
ok &= res5 == 0

# ---- theta_3 decomposition: for w = (w_x, w_y) with w_x = -<Zt, w_y>,
#      x <w, D_w Y> = w_x <w_y, x Y.grad Zt> + <w_y, M w_y> - w_x <w_y, M Zt>
wy1, wy2 = sp.symbols('wy1 wy2', real=True)
wy = sp.Matrix([wy1, wy2])
wx = -(Zt_xy.T * wy)[0]
DwZ = sp.Matrix([wx * Zt_xy[i].diff(x) + wy1 * Zt_xy[i].diff(y1) + wy2 * Zt_xy[i].diff(y2)
                 for i in range(2)])
lhs6 = x * (wy.T * DwZ)[0]          # first component of D_w Y is 0
YgZ = sp.Matrix([Ygrad(Zt_xy[i]) for i in range(2)])
rhs6 = wx * (wy.T * (x * YgZ))[0] + (wy.T * M * wy)[0] - wx * (wy.T * M * Zt_xy)[0]
res6 = sp.simplify(sp.expand(lhs6 - rhs6))
print('theta_3 decomposition residual:', res6)
ok &= res6 == 0

# ---- Lemma 2 constants (3.1) [007] with h0=1, h1=3/2, a1=a3=a0, a2=beta*a0
a0 = sp.Symbol('a0', positive=True)
h0, h1 = 1, sp.Rational(3, 2)
L1 = 2 * (beta * a0 + beta * a0 / 2) * sp.sqrt(h1 / a0)
L2 = 2 * sp.sqrt(2 * a0 / h0)
print('L1 - 3 beta sqrt(3a0/2):', sp.simplify(L1 - 3 * beta * sp.sqrt(3 * a0 / 2)))
print('L2 - 2 sqrt(2a0):', sp.simplify(L2 - 2 * sp.sqrt(2 * a0)))

# ---- special cases of the field: xi = C b (L=I) gives Y=(1,gamma'); xi=(C-I)b, gamma=0 gives q/x
print('ALL IDENTITIES OK' if ok else 'SOME IDENTITY FAILED')
