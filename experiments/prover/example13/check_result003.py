"""Проверка выкладок results/003-example13.md (prover, 21.10.2026).

Статус: [Эксперимент] (символьная проверка SymPy; не заменяет доказательство).
Запуск: ~/venv/bin/python check_result003.py
"""
import sympy as sp

x, y, z = sp.symbols('x y z', real=True)
s, d, eta, ph, tau = sp.symbols('s d eta phi tau', real=True)
c, sg = sp.cos(ph), sp.sin(ph)
r2 = sp.sqrt(2)

Q = x**2 + y**2 - z**2
U6 = z**5*x + z**4*x*y + sp.Rational(1, 2)*z**6
U = Q**2 + U6

def trig0(e):
    return sp.simplify(sp.expand_trig(sp.expand(e)))

# --- координаты (s, d, phi) на {rho>0} ---
rho = (s + d)/r2
Zs = (s - d)/r2
sub = {x: rho*c, y: rho*sg, z: Zs}
print('1. Q^2 - 4 s^2 d^2 =', trig0(Q.subs(sub)**2 - 4*s**2*d**2))

U6s = sp.expand(U6.subs(sub))
P = sp.Poly(U6s, s, d)
print('   U6 однороден степени 6 по (s,d):', all(sum(m) == 6 for m in P.monoms()))
a = [sp.simplify(P.coeff_monomial(s**(6 - j)*d**j)) for j in range(7)]
G = c*(1 + sg) + sp.Rational(1, 2)
cc_, ss_ = sp.symbols('c sigma')
for j in range(7):
    print('   a_%d =' % j, sp.factor(sp.expand(sp.expand_trig(a[j])).subs({sp.cos(ph): cc_, sp.sin(ph): ss_})))
print('2. a0 - G/8 =', trig0(a[0] - G/8))
a1claim = -sp.Rational(1, 8)*sp.sin(2*ph) - sp.Rational(1, 2)*c - sp.Rational(3, 8)
print('   a1 - claim =', trig0(a[1] - a1claim))
print('   a1\' - (-cos2phi/4 + sin phi/2) =',
      trig0(sp.diff(a[1], ph) - (-sp.cos(2*ph)/4 + sg/2)))

# --- тождество (1/6) E(U) - U = g ---
Us = 4*s**2*d**2 + sum(a[j]*s**(6 - j)*d**j for j in range(7))
EU = s*sp.diff(Us, s) + 2*d*sp.diff(Us, d)
g = sp.Rational(1, 6)*sum(j*a[j]*s**(6 - j)*d**j for j in range(1, 7))
print('3. (1/6)E(U) - U - g =', sp.simplify(sp.expand(EU/6 - Us - g)))

# --- перемасштабирование и Phi(0,...) ---
Ut = sp.expand(Us.subs(d, s**2*eta)/s**6)
Ut0 = Ut.subs(s, 0)
print('4. Ut(0) - (4 eta^2 + G/8) =', trig0(Ut0 - 4*eta**2 - G/8))
print('   d_eta U = s^4 Ut_eta :', sp.simplify(sp.diff(Us, d).subs(d, s**2*eta) - s**4*sp.diff(Ut, eta)) == 0)
kap, kapp, al = sp.symbols('kappa kappa_p alpha', positive=True)
ghat = sp.Rational(1, 6)*sum(j*a[j]*s**(j - 1)*eta**j for j in range(1, 7))
Phi = (1 - al)*Ut + s*ghat - kap*sp.diff(Ut, eta)**2 - kapp*sp.diff(Ut, ph)**2
Gp = sp.diff(G, ph)
print('   Phi(0) - [(1-a)Ut0 - 64 k eta^2 - k\'/64 G\'^2] =',
      trig0(Phi.subs(s, 0) - ((1 - al)*Ut0 - 64*kap*eta**2 - kapp/64*Gp**2)))
# <gradU,V> - alpha U = s^6 Phi  (в координатах (s,d,phi), V(U) = E(U)/6 - k(U_d)^2/s^2 - k'(U_phi)^2/s^6)
VU = EU/6 - kap*sp.diff(Us, d)**2/s**2 - kapp*sp.diff(Us, ph)**2/s**6
print('   V(U) - a U - s^6 Phi =',
      sp.simplify(sp.expand((VU - al*Us).subs(d, s**2*eta) - s**6*Phi)))

# --- лемма 3 ---
print('5. G\' + (2 sin-1)(1+sin) =', trig0(Gp + (2*sg - 1)*(1 + sg)))
Gpp = sp.diff(G, ph, 2)
print('   G\'\' + (cos + 2 sin 2phi) =', trig0(Gpp + (c + 2*sp.sin(2*ph))))
for p0 in (sp.pi/6, 5*sp.pi/6, 3*sp.pi/2):
    print('   G(%s) =' % p0, sp.nsimplify(sp.simplify(G.subs(ph, p0))))
zs = [sp.nsolve(G, ph, g0) for g0 in (1.8, 3.6)]
print('   нули G:', [sp.N(v, 6) for v in zs], ' G\' в них:', [sp.N(Gp.subs(ph, v), 5) for v in zs])

# --- лемма 6: константы ---
L = sp.Rational(3, 4)/r2 + sp.Rational(3, 8)
print('6. 3/(4 sqrt2) + 3/8 =', sp.N(L, 6), '<= 0.91:', bool(L <= sp.Rational(91, 100)))
print('   1/6 - 0.91/50 =', sp.N(sp.Rational(1, 6) - sp.Rational(91, 100)/50, 6),
      ' 1/3 - 8/100 =', sp.N(sp.Rational(1, 3) - sp.Rational(8, 100), 6), ' 1/12 =', sp.N(sp.Rational(1, 12), 6))

# --- изолированность над R ---
Ux, Uy, Uz = [sp.expand(sp.diff(U, v)) for v in (x, y, z)]
print('7. y U_x - x U_y - z^4 (y^2 + y z - x^2) =', sp.expand(y*Ux - x*Uy - z**4*(y**2 + y*z - x**2)))
print('   U_z - [-4 z Q + z^3 (5 z x + 4 x y + 3 z^2)] =',
      sp.expand(Uz - (-4*z*Q + z**3*(5*z*x + 4*x*y + 3*z**2))))
print('   z=0: grad U - 4(x^2+y^2)(x,y,0) =',
      [sp.expand(e.subs(z, 0) - f) for e, f in zip((Ux, Uy, Uz), (4*(x**2 + y**2)*x, 4*(x**2 + y**2)*y, 0))])
# U_y = 0 при 4Q = z^2(5zx+4xy+3z^2):  z^2 [ y(5zx+4xy+3z^2) + z^2 x ]
expr = y*z**2*(5*z*x + 4*x*y + 3*z**2) + z**4*x
print('   4yQ + z^4 x  при 4Q=z^2(...)  =  z^2[y(5zx+4xy+3z^2)+z^2 x]:',
      sp.expand(expr - z**2*(y*(5*z*x + 4*x*y + 3*z**2) + z**2*x)) == 0)
# подстановка x = rho c, y = rho sg, rho = tau z
R = sp.symbols('R', positive=True)  # rho
cc, ss = sp.symbols('c sigma', real=True)
inner = (y*(5*z*x + 4*x*y + 3*z**2) + z**2*x).subs({x: R*cc, y: R*ss})
inner_t = sp.expand(inner.subs(R, tau*z)/(tau*z**3))
p2 = ss*(5*cc + 4*cc*ss + 3) + cc
print('   inner/(rho z^2) =', sp.factor(inner_t), ';  p2 - inner/(rho z^2) + sigma(5c(tau-1)+4c sigma(tau^2-1)) =',
      sp.expand(p2 - inner_t + ss*(5*cc*(tau - 1) + 4*cc*ss*(tau**2 - 1))))
eqA = (x**2 - y**2 - y*z).subs({x: R*cc, y: R*ss})
eqA_t = sp.expand(eqA.subs(R, tau*z)/(tau*z**2))
p1 = (cc**2 - ss**2) - ss  # = cos 2phi - sin phi = 1 - sin - 2 sin^2
print('   (x^2-y^2-yz)/(rho z) =', eqA_t, ';  p1 - that - (c^2-s^2)(1-tau) =',
      sp.expand(p1 - eqA_t - (cc**2 - ss**2)*(1 - tau)))
print('   p1 = G\' (на окружности):', trig0(((sp.cos(ph)**2 - sp.sin(ph)**2) - sp.sin(ph)) - Gp) == 0)
GB = sp.groebner([p1, p2, cc**2 + ss**2 - 1], cc, ss, order='lex')
print('8. базис Грёбнера {p1, p2, c^2+s^2-1} =', GB.exprs)
for sv in (sp.Rational(1, 2), -1):
    print('   sigma=%s: p2 =' % sv, sp.factor(p2.subs(ss, sv)), ' при c^2 =', 1 - sv**2)

# --- над C: прямые z=0, x=±i y ---
for sgn in (1, -1):
    print('9. z=0, x=%+d i y: grad U =' % sgn, [sp.expand(e.subs({z: 0, x: sgn*sp.I*y})) for e in (Ux, Uy, Uz)],
          ' U =', sp.expand(U.subs({z: 0, x: sgn*sp.I*y})))

# --- численные константы ---
import numpy as np
p = np.linspace(0, 2*np.pi, 2_000_001)
P1 = 1 - np.sin(p) - 2*np.sin(p)**2
P2 = np.sin(p)*(5*np.cos(p) + 4*np.cos(p)*np.sin(p) + 3) + np.cos(p)
print('10. min_{phi}(|p1|+|p2|) =', (np.abs(P1) + np.abs(P2)).min())
th = np.linspace(0, np.pi, 1501); fi = np.linspace(0, 2*np.pi, 3001)
TH, FI = np.meshgrid(th, fi)
X, Y, Zc = np.sin(TH)*np.cos(FI), np.sin(TH)*np.sin(FI), np.cos(TH)
print('    A = max_{|q|=1}|U6| ~', np.abs(Zc**5*X + Zc**4*X*Y + 0.5*Zc**6).max())
print('    max|a1\'| ~', np.abs(-np.cos(2*p)/4 + np.sin(p)/2).max(),
      ' max|G\'\'| ~', np.abs(np.cos(p) + 2*np.sin(2*p)).max())

a_ = sp.symbols('a', positive=True)
qa = {x: -sp.sqrt(3)/2*a_, y: a_/2, z: a_}
print('11. U(a(-sqrt3/2, 1/2, 1)) =', sp.factor(sp.simplify(U.subs(qa))), ' = a^6 (1/2 - 3 sqrt3/4):',
      sp.simplify(U.subs(qa) - a_**6*(sp.Rational(1, 2) - 3*sp.sqrt(3)/4)) == 0)
