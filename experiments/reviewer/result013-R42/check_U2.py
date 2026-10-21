"""R42: теорема II, предложение 5.1, замечание 3 results/013. [Эксперимент] sympy + numpy.
Квадрант x>0, y<0; пишем y = -Y, Y>0.
"""
import sympy as sp
import numpy as np

x, Y, z, eta, e = sp.symbols('x Y z eta e', positive=True)
y = -Y
H = x*y + z**3
U2 = x**2*y**2 + 2*x*y*z**3 + eta*z**6 + x**6 + y**6
print('U_II = H^2-(1-eta)z^6+x^6+y^6:', sp.expand(U2 - (H**2-(1-eta)*z**6+x**6+y**6)) == 0)

# поле (3)
g = x*Y/(x+Y)
zxi0 = sp.Matrix([(3-e)*g, -(3-e)*g])
zzeta = -e*z**3*sp.Matrix([y, x])/(x**2+y**2)
zxi = zxi0 + zzeta
xi = zxi/z
lam_x = (3-e)*Y/(x+Y); lam_y = (3-e)*x/(x+Y)
print('lambda_x x = (3-e)g, lambda_y y = -(3-e)g:',
      sp.simplify(lam_x*x-(3-e)*g) == 0, sp.simplify(lam_y*y+(3-e)*g) == 0)

# Производная вдоль Y = (xi1, xi2, 1) от функции f(x, y, z); y = -Y, d/dy = -d/dY
def Yder(f):
    return xi[0]*sp.diff(f, x) - xi[1]*sp.diff(f, Y) + sp.diff(f, z)

print('(8.1) zY(H) = (3-e)H:', sp.simplify(z*Yder(H) - (3-e)*H) == 0)
print('family H = c z^{3-e} preserved: Y(H/z^{3-e}) =', sp.simplify(Yder(H/z**(3-e))))

# (8.2) при V=0
a0 = 1-eta
W = U2 + a0*z**6
lhs = 6*W - z*Yder(W)
rhs = 2*e*H**2 + 6*(1-lam_x)*x**6 + 6*(1-lam_y)*y**6 - 6*(x**5*zzeta[0] + y**5*zzeta[1])
print('(8.2) (V=0):', sp.simplify(lhs - rhs) == 0)
# член с V: Y V = xi.grad_xy V + V_z — линейно, проверим на произвольной V
Vf = sp.Function('V')(x, Y, z)
lhsV = 6*(W+Vf) - z*Yder(W+Vf)
rhsV = rhs + 6*Vf - z*(xi[0]*sp.diff(Vf, x) - xi[1]*sp.diff(Vf, Y) + sp.diff(Vf, z))
print('(8.2) with V:', sp.simplify(lhsV - rhsV) == 0)

# x^5 z zeta_1 и y^5 z zeta_2
print('x^5 z zeta1 =', sp.simplify(x**5*zzeta[0]), '; y^5 z zeta2 =', sp.simplify(y**5*zzeta[1]))

# f(u)
u = sp.symbols('u', positive=True)
expr6 = 6*(1-lam_x)*x**6 + 6*(1-lam_y)*y**6
fu = ((u-2+e)*u**6 + 1 - (2-e)*u)/(1+u)
print('6(1-lx)x^6+6(1-ly)y^6 = 6Y^6 f(u):', sp.simplify(expr6.subs(x, u*Y) - 6*Y**6*fu) == 0)
# численная проверка f(u) >= 0.398(u^6+1) при u>=4, e in (0,1/2]
fl = sp.lambdify((u, e), fu - sp.Rational(398, 1000)*(u**6+1), 'numpy')
uu = np.concatenate([np.linspace(4, 10, 2000), np.logspace(1, 4, 2000)])
mn = min(np.min(fl(uu, ev)/(uu**6+1)) for ev in np.linspace(1e-6, 0.5, 51))
print('min over u>=4 of (f-0.398(u^6+1))/(u^6+1) =', mn)
# симметрия x <-> Y
sw = expr6.subs({x: sp.Symbol('T')}).subs({Y: x}).subs({sp.Symbol('T'): Y})
print('symmetry x<->|y|:', sp.simplify(sw - expr6) == 0)

# D_xy(z xi0): производные g
a_ = sp.diff(g, x); b_ = sp.diff(g, Y)  # d g/dy = -dg/dY
print('dg/dx = Y^2/(x+Y)^2:', sp.simplify(a_ - Y**2/(x+Y)**2) == 0,
      '; dg/dy = -x^2/(x+Y)^2:', sp.simplify(-b_ + x**2/(x+Y)**2) == 0)
# D_xy (y,x)/(x^2+y^2)
xs, ys = sp.symbols('xs ys', real=True)
F = sp.Matrix([ys, xs])/(xs**2+ys**2)
J = F.jacobian([xs, ys])
print('Jacobian (y,x)/(x^2+y^2):', sp.simplify(J*(xs**2+ys**2)**2))
print('J^T J = I/(x^2+y^2)^2:', sp.simplify(J.T*J - sp.eye(2)/(xs**2+ys**2)**2) == sp.zeros(2))

# z d_z xi = 2 zeta - xi0
zxi_full = zxi
zdz_xi = z*sp.diff(zxi_full/z, z)
print('z d_z xi = 2zeta - xi0:', sp.simplify(zdz_xi - (2*zzeta/z - zxi0/z)) == sp.zeros(2, 1))

# Предложение 5.1
X, Yv, Z = sp.symbols('X Yv Z', real=True)
U2r = X**2*Yv**2 + 2*X*Yv*Z**3 + eta*Z**6 + X**6 + Yv**6
print('dU/dz = 6z^2(xy+eta z^3):', sp.expand(sp.diff(U2r, Z) - 6*Z**2*(X*Yv+eta*Z**3)) == 0)
ex = sp.expand(X/2*sp.diff(U2r, X)).subs(Yv, -eta*Z**3/X)
print('(x/2)U_x on xy=-eta z^3 = 3x^6-eta(1-eta)z^6:', sp.simplify(ex - (3*X**6 - eta*(1-eta)*Z**6)) == 0)
zz = sp.symbols('zz', positive=True)
print('U_II(z^{3/2},-z^{3/2},z) =', sp.expand(U2r.subs({X: zz**sp.Rational(3, 2), Yv: -zz**sp.Rational(3, 2), Z: zz})))
# критические точки вне нуля: решение
sol = sp.solve([sp.diff(U2r.subs(eta, sp.Rational(1, 2)), v) for v in (X, Yv, Z)], [X, Yv, Z], dict=True)
real = [s_ for s_ in sol if all(sp.im(sp.N(v_)) == 0 for v_ in s_.values())]
print('eta=1/2 real critical points:', [(sp.N(s_[X], 6), sp.N(s_[Yv], 6), sp.N(s_[Z], 6)) for s_ in real])
print('predicted |z| =', sp.N(((1-sp.Rational(1, 2))/(3*sp.Rational(1, 4)))**sp.Rational(1, 3)))

# Замечание 3: прямые карты
b1, b2, zp = sp.symbols('b1 b2 zp', positive=True)
F_axis = sp.expand(U2r.subs({X: zp**sp.Rational(3, 2)*b1, Yv: zp**sp.Rational(3, 2)*b2, Z: zp})/zp**6)
print('axis chart U/z^6 - [(b1b2+1)^2-(1-eta)+z^3(b1^6+b2^6)] =',
      sp.simplify(F_axis - ((b1*b2+1)**2-(1-eta)+zp**3*(b1**6+b2**6))))
F_vert = sp.expand(U2r.subs({X: zp**sp.Rational(3, 2)*(1+b1), Yv: zp**sp.Rational(3, 2)*(-1+b2), Z: zp})/zp**6)
F0v = F_vert.subs(zp, 0)
print('vertex chart F0 + (1-eta) - (b1b2-b1+b2)^2 =', sp.simplify(F0v + (1-eta) - (b1*b2-b1+b2)**2))
# общий центр gamma = z^{3/2} (g1, g2)
g1, g2 = sp.symbols('g1 g2', real=True)
B1, B2 = sp.symbols('B1 B2', real=True)
Fg = sp.expand(U2r.subs({X: zp**sp.Rational(3, 2)*(g1+B1), Yv: zp**sp.Rational(3, 2)*(g2+B2), Z: zp})/zp**6).subs(zp, 0)
print('general center F0(b) =', sp.factor(Fg + 1 - eta), ' - (1-eta)')
print('grad F0(0) =', [sp.factor(sp.diff(Fg, v).subs({B1: 0, B2: 0})) for v in (B1, B2)])

# e_z: (rho/lambda)Xi = 6 delta z^6 - z dW/dz, W = H^2 + x^6 + y^6
Wz = (X*Yv+Z**3)**2 + X**6 + Yv**6
print('z dW/dz = 6 z^3 H:', sp.expand(Z*sp.diff(Wz, Z) - 6*Z**3*(X*Yv+Z**3)) == 0)
for d in (0.05, 0.02, 0.01):
    print('  6-6/sqrt(delta) at', d, ':', 6-6/np.sqrt(d))
# постоянные веса
lx, ly = sp.symbols('lx ly', real=True)
zYH = lx*X*Yv + ly*X*Yv + 3*Z**3
Hh = X*Yv + Z**3
print('6H^2 - 2H zYH = 2(3-L)H(H-z^3):',
      sp.expand(6*Hh**2 - 2*Hh*zYH - 2*(3-lx-ly)*Hh*(Hh-Z**3)) == 0)
