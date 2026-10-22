# R52: проверки примера O2 (sympy, точно, кроме M1, M2 — сетка).
import sympy as sp, numpy as np
x, y, z, s, th, e = sp.symbols('x y z s theta epsilon', real=True)
rho2 = x**2 + y**2
U = z**4 - 2*z**2*y*rho2 - x**2*rho2**2 + x**7 + y**7
print('(a) U == (z^2-y rho^2)^2 - rho^6 + x^7 + y^7 :', sp.expand(U - ((z**2 - y*rho2)**2 - rho2**3 + x**7 + y**7)) == 0)
sub = sp.expand(U.subs({x: s*sp.cos(th), y: s*sp.sin(th), z: s**sp.Rational(3, 2)*e}))
rhs = s**6*((e**2 - sp.sin(th))**2 - 1 + s*(sp.cos(th)**7 + sp.sin(th)**7))
print('(O.1) identity:', sp.simplify(sub - sp.expand(rhs)) == 0)
# phi(s,theta,y) and first edge
yy = sp.Symbol('yy')
# homogeneous parts u_k and phi(s,theta,yy) = sum s^(k-4) u_k(omega + yy n)
P = sp.Poly(U, x, y, z)
parts = {}
for m, c in P.terms():
    parts.setdefault(sum(m), 0)
    parts[sum(m)] += c*x**m[0]*y**m[1]*z**m[2]
phi = sum(s**(k - 4)*parts[k].subs({x: sp.cos(th), y: sp.sin(th), z: yy}) for k in parts)
phi = sp.expand(phi)
supp = sorted({(i, l) for (i, l), c in sp.Poly(phi, s, yy).terms()})
print('support S (i,l):', supp)
g = min(sp.Rational(i, 4 - l) for i, l in supp if l < 4)
print('gamma* =', g, ' c =', 1 + g, ' j =', 4 + 4*g)
Phi0 = sum(sp.Poly(phi, s, yy).coeff_monomial(s**i*yy**l)*e**l for i, l in supp if i + g*l == 4*g)
print('Phi0 =', sp.factor(sp.simplify(Phi0 - ((e**2 - sp.sin(th))**2 - 1))) == 0 and '(e^2 - sin)^2 - 1' or Phi0)
# isolation of 0 over R by hand argument, checked symbolically:
Ux, Uy, Uz = [sp.diff(U, v) for v in (x, y, z)]
print('U_z =', sp.factor(Uz))
w = sp.Symbol('w')
# branch z^2 = y rho^2: U_x, U_y reduce to
Ux_b = sp.expand(Ux.subs(z**2, y*rho2)); Uy_b = sp.expand(Uy.subs(z**2, y*rho2))
print('on z^2 = y rho^2: U_x =', sp.factor(Ux_b), ' U_y =', sp.factor(Uy_b))
print('on z = 0: U_x =', sp.factor(Ux.subs(z, 0)), ' U_y =', sp.factor(Uy.subs(z, 0)))
# invariant x-axis
print('U_y(x,0,0) =', Uy.subs({y: 0, z: 0}), ' U_z(x,0,0) =', Uz.subs({y: 0, z: 0}), ' U(x,0,0) =', sp.factor(U.subs({y: 0, z: 0})))
# X0 f = f/2 with arbitrary chi
chi = sp.Function('chi')(th)
f = e**2 - sp.sin(th)
X0t = chi*sp.tan(th)/2; X0e = (e**2 - (1 - chi)*sp.sin(th))/(4*e)
print('X0 f - f/2 =', sp.simplify(X0t*sp.diff(f, th) + X0e*sp.diff(f, e) - f/2))
# M1, M2 on a grid (experiment)
def psi(u):
    u = np.asarray(u, float); out = np.zeros_like(u)
    m = (u > 0) & (u < 1); a = np.exp(-1/u[m]); b = np.exp(-1/(1 - u[m])); out[m] = a/(a + b); out[u >= 1] = 1
    return out
def chif(t):
    d = np.minimum(np.abs(t), np.abs(t - np.pi)); return 1 - psi((d - np.pi/8)/(np.pi/8))
T = np.linspace(-0.26, np.pi + 0.26, 6001); E = np.linspace(-1.2, 1.2, 4001)
TT, EE = np.meshgrid(T, E, indexing='ij'); F = EE**2 - np.sin(TT); mask = np.abs(F) <= 0.25
h = 1e-6
X0T = lambda t: 0.5*chif(t)*np.tan(t)
dX0T = (X0T(T + h) - X0T(T - h))/(2*h)
M1 = np.max(np.abs(dX0T)[np.any(mask, axis=1)])
C = chif(TT)
with np.errstate(divide='ignore', invalid='ignore'):
    dXe = np.where(np.abs(EE) > 1e-9, 0.25 + (1 - C)*np.sin(TT)/(4*EE**2), 0.25)
M2 = np.max(dXe[mask]); MX = np.max(np.abs(X0T(T))[np.any(mask, axis=1)])
print(f'[Эксперимент] M1 ~ {M1:.4f}, M2 ~ {M2:.4f}, max|X0^theta| ~ {MX:.4f}')
print('arcsin(1/4) =', float(sp.asin(sp.Rational(1, 4))), ' sin(pi/8) =', float(sp.sin(sp.pi/8)), ' sqrt(sin(pi/8)-1/4) =', float(sp.sqrt(sp.sin(sp.pi/8) - sp.Rational(1, 4))))
