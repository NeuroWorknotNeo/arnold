# R38: symbolic checks for section 5 of notes/prover/2026-10-21-singular-sigma.md
import sympy as sp
x, z, t, eta, e = sp.symbols('x z t eta e', positive=True)  # t = |y|, y = -t
y = -t
H = x*y + z**3
U = x**2*y**2 + 2*x*y*z**3 + eta*z**6 + x**6 + y**6
print("U = H^2-(1-eta)z^6+x^6+y^6:", sp.simplify(U - (H**2 - (1-eta)*z**6 + x**6 + y**6)) == 0)
# field (5.1) in the quadrant x>0,y<0
g = x*t/(x+t)
zxi0 = sp.Matrix([(3-e)*g, -(3-e)*g])
zzeta = -e*z**3*sp.Matrix([y, x])/(x**2+y**2)
zxi = zxi0 + zzeta
xi = zxi/z
lamx = (3-e)*t/(x+t); lamy = (3-e)*x/(x+t)
print("zxi0 = (lamx x, lamy y):", sp.simplify(zxi0[0]-lamx*x)==0, sp.simplify(zxi0[1]-lamy*y)==0, sp.simplify(lamx+lamy-(3-e))==0)
# derivative operator: Y = xi1 d_x + xi2 d_y + d_z, with y=-t so d_y = -d_t
def Yop(f):
    return xi[0]*sp.diff(f, x) + xi[1]*(-sp.diff(f, t)) + sp.diff(f, z)
print("(5.2) zY(H)=(3-e)H:", sp.simplify(z*Yop(H) - (3-e)*H) == 0)
# (5.3) with generic V: check the V-free part and the V-term separately
W0 = H**2 + x**6 + y**6
lhs = 6*W0 - z*Yop(W0)
rhs = 2*e*H**2 + 6*(1-lamx)*x**6 + 6*(1-lamy)*y**6 - 6*(x**5*zzeta[0] + y**5*zzeta[1])
print("(5.3) (V=0):", sp.simplify(lhs - rhs) == 0)
Vf = sp.Function('V')(x, t, z)
lhsV = 6*Vf - z*Yop(Vf)
rhsV = 6*Vf - z*(xi[0]*sp.diff(Vf, x) + xi[1]*(-sp.diff(Vf, t)) + sp.diff(Vf, z))
print("(5.3) V-term:", sp.simplify(lhsV - rhsV) == 0)
# f(u)
u = sp.symbols('u', positive=True)
part = 6*(1-lamx)*x**6 + 6*(1-lamy)*y**6
fu = ((u-2+e)*u**6 + 1 - (2-e)*u)/(1+u)
print("part = 6|y|^6 f(u):", sp.simplify(part.subs(x, u*t) - 6*t**6*fu) == 0)
# zeta terms
print("x^5 zzeta1 =", sp.simplify(x**5*zzeta[0]), "; y^5 zzeta2 =", sp.simplify(y**5*zzeta[1]))
# Jacobians
Dz0 = sp.Matrix([[sp.diff(zxi0[i], x), -sp.diff(zxi0[i], t)] for i in range(2)])
a = y**2/(x+t)**2; b = x**2/(x+t)**2
print("D(zxi0) = (3-e)[[a,-b],[-a,b]]:", sp.simplify(Dz0 - (3-e)*sp.Matrix([[a, -b], [-a, b]])) == sp.zeros(2))
Dzz = sp.Matrix([[sp.diff(zzeta[i], x), -sp.diff(zzeta[i], t)] for i in range(2)])
M = sp.Matrix([[-2*x*y, x**2-y**2], [y**2-x**2, -2*x*y]])/(x**2+y**2)**2
print("D(zzeta) = -e z^3 M:", sp.simplify(Dzz + e*z**3*M) == sp.zeros(2))
print("M^T M = I/(x^2+y^2)^2:", sp.simplify(M.T*M - sp.eye(2)/(x**2+y**2)**2) == sp.zeros(2))
# z d_z xi = 2 zeta - xi0
zdxi = z*sp.diff(xi, z)
print("z d_z xi = 2zeta - xi0:", sp.simplify(zdxi - (2*zzeta/z - zxi0/z)) == sp.zeros(2, 1))
# critical points: gradient components
X, Y_, Z = sp.symbols('X Y Z', real=True)
Up = X**2*Y_**2 + 2*X*Y_*Z**3 + eta*Z**6 + X**6 + Y_**6
gr = [sp.diff(Up, v) for v in (X, Y_, Z)]
print("dU/dz =", sp.factor(gr[2]))
print("(x/2) dU/dx with xy=-eta z^3:", sp.expand((X/2*gr[0]).subs(Y_, -eta*Z**3/X)))
