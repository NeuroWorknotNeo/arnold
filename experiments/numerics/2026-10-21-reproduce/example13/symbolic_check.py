# Symbolic checks for Example 13: U = (x^2+y^2-z^2)^2 + z^5 x + z^4 x y + z^6/2
import sympy as sp
s, d, ph, eta = sp.symbols('s d phi eta', real=True)
x, y, z = sp.symbols('x y z', real=True)
U_xyz = (x**2+y**2-z**2)**2 + z**5*x + z**4*x*y + sp.Rational(1,2)*z**6
# cone-adapted coordinates: rho=(s+d)/sqrt2, z=(s-d)/sqrt2
r2 = sp.sqrt(2)
rho = (s+d)/r2; Z = (s-d)/r2
sub = {x: rho*sp.cos(ph), y: rho*sp.sin(ph), z: Z}
U = sp.expand(sp.simplify(U_xyz.subs(sub)))
Q2 = sp.expand(((x**2+y**2-z**2)**2).subs(sub))
print("Q^2 in (s,d):", sp.simplify(Q2))
U6 = sp.expand(U - 4*s**2*d**2)
poly = sp.Poly(U6, s, d)
print("U - 4 s^2 d^2 is homogeneous of degree 6 in (s,d):", all(sum(m)==6 for m in poly.monoms()))
a = {}
for j in range(7):
    a[j] = sp.simplify(sp.trigsimp(poly.coeff_monomial(s**(6-j)*d**j)))
G = sp.cos(ph) + sp.sin(2*ph)/2 + sp.Rational(1,2)
print("a0 - G/8 =", sp.simplify(sp.expand_trig(a[0] - G/8)))
print("a1 =", sp.simplify(a[1]), " ;  (sin2phi - 1 - 4G)/8 - a1 =", sp.simplify(sp.expand_trig((sp.sin(2*ph)-1-4*G)/8 - a[1])))
# weighted Euler field E = s d/ds + 2 d d/dd
EU = sp.expand(s*sp.diff(U,s) + 2*d*sp.diff(U,d))
g = sp.expand(EU/6 - U)
print("E(U)/6 - U == (1/6) sum j a_j s^(6-j) d^j :", sp.simplify(g - sum(sp.Rational(j,6)*a[j]*s**(6-j)*d**j for j in range(7)))==0)
# scaled potential Utilde(s,phi,eta) = U(s,phi,s^2 eta)/s^6
Ut = sp.expand(sp.simplify(U.subs(d, s**2*eta)/s**6))
Ut0 = sp.simplify(Ut.subs(s,0))
print("Utilde at s=0:", sp.simplify(sp.expand_trig(Ut0 - (4*eta**2 + G/8))) == 0)
# max power of s in Utilde, check polynomial in s, eta
print("Utilde is polynomial in s,eta:", sp.Poly(Ut, s, eta).is_polynomial if hasattr(sp.Poly(Ut,s,eta),'is_polynomial') else True)
# common zeros of G and G': resultant in t = tan(phi/2)
t = sp.symbols('t', real=True)
c = (1-t**2)/(1+t**2); sn = 2*t/(1+t**2)
Gt = sp.together(c + sn*c + sp.Rational(1,2))   # sin2phi/2 = sin*cos
Gpt = sp.together(-sn + (c**2 - sn**2))         # G' = -sin + cos2phi
num1 = sp.numer(Gt); num2 = sp.numer(Gpt)
res = sp.resultant(sp.expand(num1), sp.expand(num2), t)
print("resultant of numerators of G and G' (in t=tan(phi/2)):", sp.factor(res))
# also check phi = pi (t = infinity): G(pi) = -1/2 != 0
print("G(pi) =", G.subs(ph, sp.pi))
# zeros of G on the circle (numerical) and G' there
import numpy as np
f = sp.lambdify(ph, G, 'numpy'); fp = sp.lambdify(ph, sp.diff(G,ph), 'numpy')
P = np.linspace(0, 2*np.pi, 2000001); Gv = f(P)
idx = np.where(np.sign(Gv[:-1]) != np.sign(Gv[1:]))[0]
for i in idx:
    print("  zero of G near phi=%.6f, G'=%.6f" % (P[i], fp(P[i])))
print("min G = %.6f at phi=%.6f (5pi/6=%.6f)" % (Gv.min(), P[Gv.argmin()], 5*np.pi/6))
