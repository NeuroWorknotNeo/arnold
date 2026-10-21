"""Независимая проверка results/003 (reviewer, 21.10.2026): тождества лемм 2, 3, 5 и теоремы 2.
[Эксперимент]. Запуск: ~/venv/bin/python symbolic.py (около минуты)."""
import sympy as sp
x, y, z = sp.symbols('x y z', real=True)
s, d, eta, ph = sp.symbols('s d eta phi', real=True)
c, sg = sp.cos(ph), sp.sin(ph)
Q = x**2+y**2-z**2
U6 = z**5*x+z**4*x*y+sp.Rational(1,2)*z**6
U = Q**2+U6
rho = (s+d)/sp.sqrt(2); Z = (s-d)/sp.sqrt(2)
sub = {x: rho*c, y: rho*sg, z: Z}
Us = sp.expand(sp.expand_trig(U.subs(sub)))
# claimed coefficients (as written in the text)
C, S = c, sg
claim = {
 0: sp.Rational(1,16)*(2*C*S+2*C+1),
 1: -sp.Rational(1,8)*(2*C*S+4*C+3),
 2: -sp.Rational(1,16)*(2*C*S-10*C-15),
 3: sp.Rational(1,4)*(2*C*S-5),
 4: -sp.Rational(1,16)*(2*C*S+10*C-15),
 5: -sp.Rational(1,8)*(2*C*S-4*C+3),
 6: sp.Rational(1,16)*(2*C*S-2*C+1),
}
Uclaim = 4*s**2*d**2 + sum(claim[j]*s**(6-j)*d**j for j in range(7))
print('Lemma2: U - claimed =', sp.simplify(sp.expand(Us-Uclaim)))
G = c*(1+sg)+sp.Rational(1,2)
print('a0 - G/8 =', sp.simplify(claim[0]-G/8))
print('a1 alt form:', sp.simplify(claim[1]-(-sp.sin(2*ph)/8-c/2-sp.Rational(3,8))))
a1p = sp.diff(claim[1], ph)
print("a1' - (-cos2phi/4+sin/2) =", sp.simplify(a1p-(-sp.cos(2*ph)/4+sg/2)))
Gp = sp.diff(G, ph); Gpp = sp.diff(G, ph, 2)
print("G' - (1-sin-2sin^2) =", sp.simplify(Gp-(1-sg-2*sg**2)), "; G'+(2s-1)(1+s) =", sp.simplify(sp.expand(Gp+(2*sg-1)*(1+sg))))
print("G'' + (cos+2sin2phi) =", sp.simplify(Gpp+(c+2*sp.sin(2*ph))))
import numpy as np
p = np.linspace(0, 2*np.pi, 400001)
print("max|a1'|=", np.max(np.abs(-np.cos(2*p)/4+np.sin(p)/2)), " max|G''|=", np.max(np.abs(np.cos(p)+2*np.sin(2*p))))
print("bound: 3/(4sqrt2)+3/8 =", 3/(4*np.sqrt(2))+3/8)
# sharper: max over phi of |a1'|/sqrt2 + |G''|/8 (same phi)
print("sharper max_phi(|a1'|/sqrt2+|G''|/8)=", np.max(np.abs(-np.cos(2*p)/4+np.sin(p)/2)/np.sqrt(2)+np.abs(np.cos(p)+2*np.sin(2*p))/8))
# Lemma 3 values
for v in (sp.pi/6, 5*sp.pi/6, 3*sp.pi/2):
    print('G(', v, ')=', sp.nsimplify(sp.simplify(G.subs(ph, v))))
Gn = lambda t: np.cos(t)*(1+np.sin(t))+0.5
from scipy.optimize import brentq
pm = brentq(Gn, 1.6, 2.6); pp = brentq(Gn, 2.7, 4.6)
Gpn = lambda t: 1-np.sin(t)-2*np.sin(t)**2
print('zeros', pm, pp, "G' there", Gpn(pm), Gpn(pp), ' margin kappa\'/64 G\'^2 =', [Gpn(t)**2/64/50 for t in (pm, pp)])
# Euler-field identity
E = s*sp.diff(Uclaim, s)+2*d*sp.diff(Uclaim, d)
g = sp.Rational(1,6)*sum(j*claim[j]*s**(6-j)*d**j for j in range(1,7))
print('(1/6)E(U)-U-g =', sp.simplify(sp.expand(E/6-Uclaim-g)))
# rescaling
Ut = sp.expand(Uclaim.subs(d, s**2*eta)/s**6)
print('Ut polynomial in (s,eta):', sp.Poly(Ut, s, eta) is not None)
print('Ut(0) - (4eta^2+G/8)=', sp.simplify(Ut.subs(s,0)-4*eta**2-G/8))
# Theorem 2 identities
Ux, Uy, Uz = [sp.expand(sp.diff(U, v)) for v in (x, y, z)]
print('Ux:', sp.expand(Ux-(4*x*Q+z**5+z**4*y)), ' Uy:', sp.expand(Uy-(4*y*Q+z**4*x)), ' Uz:', sp.expand(Uz-(-4*z*Q+z**3*(5*z*x+4*x*y+3*z**2))))
print('(A):', sp.expand(y*Ux-x*Uy-z**4*(y**2+y*z-x**2)))
# p1,p2 identities with tau, c, sigma symbols
cc, ss, tau = sp.symbols('c sigma tau', real=True)
p1 = cc**2-ss**2-ss; p2 = ss*(5*cc+4*cc*ss+3)+cc
A_t = tau*(cc**2-ss**2)-ss; C_t = ss*(5*tau*cc+4*tau**2*cc*ss+3)+cc
print('p1 - A_t - (c^2-s^2)(1-tau) =', sp.expand(p1-A_t-(cc**2-ss**2)*(1-tau)))
print('p2 - C_t + s[5c(tau-1)+4cs(tau^2-1)] =', sp.expand(p2-C_t+ss*(5*cc*(tau-1)+4*cc*ss*(tau**2-1))))
# direct check that (A)/(rho z) and (C)/(rho z^2) give A_t, C_t
R = sp.symbols('R', positive=True); zz = sp.symbols('zz', positive=True)
Aexpr = ((x**2-y**2-y*z).subs({x: R*cc, y: R*ss, z: zz}))
print('(A)/(rho z) - A_t =', sp.simplify(sp.expand(Aexpr/(R*zz)).subs(R, tau*zz)-A_t))
Cexpr = ((y*(5*z*x+4*x*y+3*z**2)+z**2*x).subs({x: R*cc, y: R*ss, z: zz}))
print('(C)/(rho z^2) - C_t =', sp.simplify(sp.expand(Cexpr/(R*zz**2)).subs(R, tau*zz)-C_t))
print('Groebner {p1,p2,c^2+s^2-1}:', sp.groebner([p1, p2, cc**2+ss**2-1], cc, ss, order='lex').exprs)
P1 = 1-np.sin(p)-2*np.sin(p)**2; P2 = np.sin(p)*(5*np.cos(p)+4*np.cos(p)*np.sin(p)+3)+np.cos(p)
c0 = np.min(np.abs(P1)+np.abs(P2)); print('c0 ~', c0, ' radius sqrt(c0/33) ~', np.sqrt(c0/33))
print('max|sigma^2 c| =', np.max(np.abs(np.sin(p)**2*np.cos(p))))
# A
rng = np.random.default_rng(0); v = rng.normal(size=(2_000_000,3)); v /= np.linalg.norm(v,axis=1)[:,None]
X,Y,Zc = v.T; print('A ~', np.max(np.abs(Zc**5*X+Zc**4*X*Y+0.5*Zc**6)))
# point q_a
a = sp.symbols('a', real=True)
print('U(q_a) - a^6(1/2-3sqrt3/4) =', sp.simplify(sp.expand(U.subs({x: -sp.sqrt(3)/2*a, y: a/2, z: a})-a**6*(sp.Rational(1,2)-3*sp.sqrt(3)/4))))
# complex lines
for sgn in (1,-1):
    print('complex line', sgn, [sp.expand(e.subs({z:0, x:sgn*sp.I*y})) for e in (Ux,Uy,Uz)])
