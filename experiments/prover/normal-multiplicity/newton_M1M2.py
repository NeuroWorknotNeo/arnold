# [Эксперимент] Точные (sympy) выкладки §5 записки notes/prover/2026-10-21-normal-multiplicity.md
# для примеров полигона M1, M2 (experiments/numerics/2026-10-21-zoo/catalog.py):
#   нормальная кратность 2r, многоугольник Ньютона функции phi(s,theta,y) = U(s(omega+y n))/s^m,
#   наклон первого ребра gamma*, j = m + 2r gamma*, c = 1 + gamma*, весовая начальная форма Phi_0,
#   перемасштабированная функция U~(sigma,theta,eps), ветвь eps_0(theta), G, профиль p(theta,e),
#   критические точки G и знак G'', тождество U(s omega + s^c (eps_0+e) n) = s^j F~(s^(1/N),theta,e),
#   константы теоремы N (a_0, lambda_0, допустимое kappa).
# Sigma_0 у обоих примеров — большой круг z = 0: omega = (cos th, sin th, 0), n = (0,0,1), k_g = 0.
import sympy as sp

x, y, z = sp.symbols('x y z', real=True)
s, eta, Y, eps, e, sig = sp.symbols('s eta y epsilon e sigma', real=True)
th = sp.symbols('theta', real=True)
C, Sn = sp.symbols('C S', real=True)            # C = cos th, S = sin th (C^2 + S^2 = 1)

EX = {
    'M1': ((z - x**2)**4 + x**5 + y**5 + x*y**6 + y*x**6, 4),
    'M2': (z**4 + z*(x**4 + x**3*y + y**4) + x**6 + x*z**5 + 2*y*z**5, 4),
}

def trig(expr):
    return sp.expand(expr.subs({C: sp.cos(th), Sn: sp.sin(th)}))

def analyze(name):
    U, m = EX[name]
    print('=' * 100)
    print(name, ': U =', U, ', m =', m)
    # U(s omega + eta n) и phi(s,theta,y) = U(s(omega + y n))/s^m
    Ucone = sp.expand(U.subs({x: s*C, y: s*Sn, z: eta}, simultaneous=True))
    phi = sp.expand(sp.expand(Ucone.subs(eta, s*Y)) / s**m)
    P = sp.Poly(phi, s, Y)
    supp = {}
    for (i, l), coef in P.terms():
        cf = sp.simplify(trig(coef))
        if cf != 0:
            supp[(i, l)] = coef
    # нормальная кратность: u_m(omega + y n) = phi(0,theta,y)
    l0 = [l for (i, l) in supp if i == 0]
    two_r = min(l0)
    a_coef = supp[(0, two_r)]
    print('  phi(0,theta,y) = u_m(omega+y n) =', sp.factor(sum(supp[(0, l)]*Y**l for l in l0)),
          ' => 2r =', two_r, ', a(theta,0) =', a_coef)
    print('  носитель phi (i = степень s, l = степень y):', sorted(supp))
    cand = [(sp.Rational(i, two_r - l), (i, l)) for (i, l) in supp if l < two_r]
    gam = min(c_[0] for c_ in cand)
    edge = sorted([pt for g, pt in cand if g == gam] + [(0, two_r)])
    bprime = two_r*gam
    j = m + bprime
    cw = 1 + gam
    Nn = sp.fraction(gam)[1]; pp = sp.fraction(gam)[0]
    print('  наклон первого ребра gamma* =', gam, ', точки ребра:', edge)
    # проверка: все точки носителя выше прямой i + gamma* l = 2r gamma*
    assert all(i + gam*l >= bprime for (i, l) in supp)
    print('  beta\' = 2r gamma* =', bprime, ', j = m + beta\' =', j, ', c = 1 + gamma* =', cw,
          ', N =', Nn, ', p =', pp)
    Phi0 = sp.expand(sum(supp[pt]*eps**pt[1] for pt in edge))
    print('  весовая начальная форма Phi_0(theta,eps) =', Phi0)
    # перемасштабирование: U~(sigma,theta,eps) = sigma^(-N beta') phi(sigma^N, theta, sigma^p eps)
    Ut = sp.expand(sp.expand(phi.subs({s: sig**Nn, Y: sig**pp*eps}, simultaneous=True)) / sig**(Nn*bprime))
    assert sp.Poly(Ut, sig).degree() >= 0 and all(mon[0] >= 0 for mon in sp.Poly(Ut, sig).monoms())
    print('  U~(sigma,theta,eps) =', Ut)
    print('  U~(0,theta,eps) - Phi_0 =', sp.simplify(trig(Ut.subs(sig, 0) - Phi0)))
    # тождество U(s omega + s^c eps n) = s^j U~(s^(1/N), theta, eps), проверяем через s = sigma^N
    lhs = sp.expand(U.subs({x: sig**Nn*C, y: sig**Nn*Sn, z: sig**(Nn*cw)*eps}, simultaneous=True))
    rhs = sp.expand(sig**(Nn*j)*Ut)
    print('  тождество U(s omega + s^c eps n) = s^j U~ :', sp.simplify(lhs - rhs) == 0)
    return dict(U=U, m=m, two_r=two_r, gam=gam, j=j, c=cw, N=Nn, p=pp, Phi0=Phi0, Ut=Ut)

# ------------------------------------------------------------------ M1
d1 = analyze('M1')
Phi0 = trig(d1['Phi0'])
G1 = trig(d1['Phi0'].subs(eps, 0))
print('  M1: eps_0 = 0, Phi_0(theta, e) - G =', sp.simplify(Phi0.subs(eps, e) - G1), ' => r\' = 2, p = 1')
G1p = sp.diff(G1, th); G1pp = sp.diff(G1, th, 2)
print('  G(theta) =', G1, ';  G\'(theta) = ', sp.factor(sp.expand_trig(G1p)))
for t0, nm in [(-sp.pi/2, 'omega* = (0,-1,0)'), (sp.pi, 'omega* = (-1,0,0)')]:
    print('    в %s: G = %s, G\' = %s, G\'\' = %s, G\'\'+jG = %s' % (nm, sp.simplify(G1.subs(th, t0)),
          sp.simplify(G1p.subs(th, t0)), sp.simplify(G1pp.subs(th, t0)),
          sp.simplify(G1pp.subs(th, t0) + d1['j']*G1.subs(th, t0))))
# все критические точки G на окружности: G' = 5 sin cos (sin^3 - cos^3) = 0
print('    критические точки G: sin*cos*(sin^3-cos^3) = 0 => theta in {0, pi/2, pi, 3pi/2, pi/4, 5pi/4}')
for t0 in [0, sp.pi/2, sp.pi, 3*sp.pi/2, sp.pi/4, 5*sp.pi/4]:
    print('      theta = %-8s G = %-14s G\'\' = %s' % (t0, sp.nsimplify(sp.simplify(G1.subs(th, t0))),
          sp.simplify(G1pp.subs(th, t0))))
# F~ для M1 в центрированном параметре (omega* = (0,-1,0)): theta -> theta - pi/2
Ft1 = sp.expand(trig(d1['Ut']).subs(th, th - sp.pi/2))
print('  F~(sigma,theta,e) (theta от omega*=(0,-1,0)) =', sp.simplify(Ft1.subs(eps, e)))

# ------------------------------------------------------------------ M2
d2 = analyze('M2')
f = trig(d2['Phi0'].coeff(eps, 1))
print('  M2: f(theta) = коэффициент при eps в Phi_0 =', f)
print('      f = 3/4 + cos(4th)/4 + sin(2th)/4 + sin(4th)/8 :',
      sp.simplify(f - (sp.Rational(3, 4) + sp.cos(4*th)/4 + sp.sin(2*th)/4 + sp.sin(4*th)/8)) == 0,
      ' => f >= 1/8 > 0')
fv = sp.symbols('f', positive=True)
e0 = -(fv/4)**sp.Rational(1, 3)
Phi0f = eps**4 + fv*eps
print('      d/deps Phi_0 (eps_0) =', sp.simplify(sp.diff(Phi0f, eps).subs(eps, e0)))
Gf = sp.simplify(Phi0f.subs(eps, e0))
print('      G = Phi_0(eps_0) =', Gf, ' = -3*4^(-4/3) f^(4/3):', sp.simplify(Gf + 3*4**sp.Rational(-4, 3)*fv**sp.Rational(4, 3)) == 0)
prof = sp.expand(Phi0f.subs(eps, e0 + e) - Gf)
pM2 = sp.simplify(sp.expand(prof/e**2))
print('      Phi_0(eps_0+e) - G = e^2 * (', pM2, ')  [= e^2 ((e+2 eps_0)^2 + 2 eps_0^2)]:',
      sp.simplify(pM2 - ((e + 2*e0)**2 + 2*e0**2)) == 0)
# критические точки f: f' / cos^4 = 4t^3 - 3t^2 - 4t + 1, t = tan theta; плюс theta = pi/2
t = sp.symbols('t', real=True)
fp = sp.diff(f, th)
cub = sp.expand(sp.simplify(sp.expand_trig(fp).subs({sp.sin(th): t*sp.cos(th)}) / sp.cos(th)**4))
print('      f\'(theta)/cos^4 через t = tan theta:', sp.factor(cub))
roots = sp.Poly(4*t**3 - 3*t**2 - 4*t + 1, t).intervals(eps=sp.Rational(1, 10**6))
print('      изолирующие интервалы корней (точно):', [(sp.N(a, 8), sp.N(b, 8)) for (a, b), _ in roots])
print('      f\'(pi/2) =', sp.simplify(fp.subs(th, sp.pi/2)))
fpp = sp.diff(f, th, 2)
print('      f\'\' = -4 cos 4th - sin 2th - 2 sin 4th :', sp.simplify(fpp - (-4*sp.cos(4*th) - sp.sin(2*th) - 2*sp.sin(4*th))) == 0)
# строго: корень t* в (0.22, 0.23)
cubp = 4*t**3 - 3*t**2 - 4*t + 1
print('      cub(0.22) =', cubp.subs(t, sp.Rational(22, 100)), '> 0,  cub(0.23) =', cubp.subs(t, sp.Rational(23, 100)), '< 0')
tstar = sp.nsolve(cubp, t, 0.2236, prec=40)
thstar = sp.atan(tstar)
print('      t* =', sp.N(tstar, 20), ', theta* = atan t* =', sp.N(thstar, 20))
print('      на [atan 0.22, atan 0.23]: 4theta in [%s, %s] subset (0, pi/2), cos(4*0.2262) = %s > 0.6 => f\'\' < -2.4'
      % (sp.N(4*sp.atan(sp.Rational(22, 100)), 6), sp.N(4*sp.atan(sp.Rational(23, 100)), 6), sp.N(sp.cos(4*sp.atan(sp.Rational(23, 100))), 6)))
fs = f.subs(th, thstar); fpps = fpp.subs(th, thstar)
Gs = -3*4**sp.Rational(-4, 3)*fs**sp.Rational(4, 3)
Gpps = -4**sp.Rational(-1, 3)*fs**sp.Rational(1, 3)*fpps
print('      f(theta*) =', sp.N(fs, 15), ', f\'\'(theta*) =', sp.N(fpps, 15))
print('      G(theta*) =', sp.N(Gs, 15), ', G\'\'(theta*) =', sp.N(Gpps, 15), ', eps_0(theta*) =', sp.N(-(fs/4)**sp.Rational(1, 3), 15))
# прямая проверка G'' дифференцированием
Gth = -3*4**sp.Rational(-4, 3)*f**sp.Rational(4, 3)
print('      проверка G\'\' дифференцированием:', sp.N(sp.diff(Gth, th, 2).subs(th, thstar), 15),
      ', G\'(theta*) =', sp.N(sp.diff(Gth, th).subs(th, thstar), 5))
print('      G\'\'+jG в theta* =', sp.N(Gpps + d2['j']*Gs, 10), ' (декартова карта K1-типа: нужен знак +)')
print('      направление дна omega* = (cos, sin, 0) =', sp.N(sp.cos(thstar), 10), sp.N(sp.sin(thstar), 10))
# вторая долина theta = pi/2
print('      theta = pi/2: f = %s, f\'\' = %s, G = %s, G\'\' = %s' % (f.subs(th, sp.pi/2), fpp.subs(th, sp.pi/2),
      sp.N(-3*4**sp.Rational(-4, 3), 12), sp.N(-4**sp.Rational(-1, 3)*fpp.subs(th, sp.pi/2), 12)))
# тождество с ветвью eps_0(theta): U(s omega + s^c(eps_0 + e) n) = s^j F~(sigma,theta,e)
Ut2 = trig(d2['Ut'])
e0th = -(f/4)**sp.Rational(1, 3)
Ft2 = Ut2.subs(eps, e0th + e)
Ft2_0 = sp.simplify(Ft2.subs(sig, 0) - (Gth + e**2*((e + 2*e0th)**2 + 2*e0th**2)))
print('  M2: F~(0,theta,e) - [G(theta) + e^2 p(theta,e)] =', Ft2_0)

# ------------------------------------------------------------------ константы теоремы N
def kappa_bound(beta, a0, lam0):
    return beta*lam0/(a0*(sp.Rational(15, 8)*sp.sqrt(3)*beta + 2*sp.sqrt(2))**2)
print('=' * 100)
print('Константы (U2): kappa <= beta lambda_0 / (a_0 (15 sqrt3/8 beta + 2 sqrt2)^2), lambda_0 = G\'\'(0)/4')
print('  M1 (omega*=(0,-1,0)): beta=5, a0=1, lambda0=5/4: kappa <=', sp.N(kappa_bound(5, 1, sp.Rational(5, 4)), 6))
print('  M2 (theta*):           beta=16/3, a0=%s, lambda0=%s: kappa <= %s' % (sp.N(-Gs, 8), sp.N(Gpps/4, 8),
      sp.N(kappa_bound(sp.Rational(16, 3), -Gs, Gpps/4), 6)))
print('  M2 (theta=pi/2):       a0=%s, lambda0=%s: kappa <= %s' % (sp.N(3*4**sp.Rational(-4, 3), 8), sp.N(4**sp.Rational(2, 3)/4, 8),
      sp.N(kappa_bound(sp.Rational(16, 3), 3*4**sp.Rational(-4, 3), 4**sp.Rational(2, 3)/4), 6)))
