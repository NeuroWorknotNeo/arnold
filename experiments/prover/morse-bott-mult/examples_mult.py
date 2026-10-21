# [Эксперимент] Примеры записки notes/prover/2026-10-21-morse-bott-mult.md, §10.
# Для каждого U с u_4 = z^4 (Sigma — экватор z = 0, нормальная кратность 2r = 4, a == 1):
#   * функция phi(s,theta,y) = U(s(omega + y n))/s^4, omega = (cos t, sin t, 0), n = e_z;
#   * носитель S, первое ребро gamma*, N, j, c, многочлен первого ребра Phi_0(theta, eps);
#   * масштабированная функция U~(sigma,theta,eps) и тождество U(s omega + s^c eps n) = s^j U~(s^(1/N),theta,eps);
#   * данные случая (W / C / D / уточнение / открытые случаи O1, O2) — точные выкладки sympy.
# Всё — проверка выкладок записки, а не доказательство.
import sympy as sp

x, y, z = sp.symbols('x y z', real=True)
s, t, yv, sig, eps, e = sp.symbols('s t yv sigma epsilon e', real=True)
sp_ = sp.Symbol('s', positive=True)
rho2 = x**2 + y**2


def phi_of(U, m=4):
    q = {x: s*sp.cos(t), y: s*sp.sin(t), z: s*yv}
    return sp.expand(sp.expand(U.subs(q, simultaneous=True))/s**m)


def support(phi):
    P = sp.Poly(phi, s, yv)
    out = {}
    for (i, l), cf in zip(P.monoms(), P.coeffs()):
        cf = sp.simplify(sp.trigsimp(cf))
        if cf != 0:
            out[(i, l)] = cf
    return out


def first_edge(supp, r=2):
    cands = [sp.Rational(i, 2*r - l) for (i, l) in supp if l < 2*r]
    g = min(cands)
    N = sp.fraction(g)[1]
    Phi0 = sum(cf*eps**l for (i, l), cf in supp.items() if i + g*l == 2*r*g)
    return g, N, sp.expand(Phi0)


def Utilde(supp, g, N, r=2):
    return sp.expand(sum(cf*sig**int(N*(i + g*l - 2*r*g))*eps**l for (i, l), cf in supp.items()))


def check_identity(U, g, N, Ut, r=2, m=4):
    # U(s omega + s^(1+g) eps n) == s^j U~(s^(1/N), t, eps) при s > 0
    j = m + 2*r*g
    lhs = U.subs({x: sp_*sp.cos(t), y: sp_*sp.sin(t), z: sp_**(1 + g)*eps}, simultaneous=True)
    rhs = sp_**j*Ut.subs(sig, sp_**(sp.Rational(1, N)))
    d = sp.simplify(sp.expand(sp.powsimp(sp.expand(lhs - rhs), force=True)))
    return d == 0


def header(name, U):
    print('=' * 100)
    print(name, ':  U =', U)
    phi = phi_of(U)
    supp = support(phi)
    print('  носитель S и коэффициенты phi_il(theta):')
    for k in sorted(supp):
        print('    ', k, ':', supp[k])
    g, N, Phi0 = first_edge(supp)
    j = 4 + 4*g
    print('  gamma* =', g, ', N =', N, ', j = m + 2r gamma* =', j, ', c = 1 + gamma* =', 1 + g)
    print('  Phi_0(theta, eps) =', sp.factor(Phi0))
    Ut = Utilde(supp, g, N)
    print('  U~(sigma,theta,eps) =', Ut)
    print('  тождество U(s omega + s^c eps n) = s^j U~(s^(1/N),theta,eps):', check_identity(U, g, N, Ut))
    return supp, g, N, Phi0, Ut


# ------------------------------------------------------------------------------------------
# W1: случай (b), p = 2, вырожденный нормальный профиль e^4 (r' = 2), (C) выполнено, (UR) нарушено
U_W1 = (z - x**2)**4 + sp.Rational(3, 2)*x*rho2**2 - sp.Rational(1, 2)*x**3*rho2 + y*z**5
supp, g, N, Phi0, Ut = header('W1', U_W1)
G = sp.simplify(Phi0.subs(eps, 0))
print('  ветвь eps_b = 0 кратности 3 (Phi_0 = eps^4 + G): G(theta) =', sp.factor(G))
tau = sp.symbols('tau', real=True)
ser = sp.series(G.subs(t, sp.pi + tau), tau, 0, 7).removeO()
print('  G(pi + tau) =', sp.nsimplify(sp.expand(ser)), '  => минимум -1 порядка 2p = 4, a = 3/8')
cc = sp.symbols('cc', real=True)
gc = sp.expand(cc*(3 - cc**2)/2)
print('  G = g(cos theta), g(c) = c(3-c^2)/2, g\'(c) =', sp.factor(sp.diff(gc, cc)), '>= 0 на [-1,1] => min G = g(-1) =', gc.subs(cc, -1))
# точная критическая ветвь в слое не RCM: член sigma^9 sin(t) eps^5
crit = sp.diff(Ut, eps)
print('  d_eps U~ =', sp.factor(crit), ' — при sigma>0 корень около sigma^3 cos^2 простой (кратность 1), при sigma = 0 — тройной')

# ------------------------------------------------------------------------------------------
# W2: случай (b), p = 2, невырожденный профиль после сдвига (r' = 1), условие (R)
f4 = 6*rho2**2 + 4*(x**2 - y**2)*rho2 - (x**4 - 6*x**2*y**2 + y**4)
U_W2 = z**4 + z*f4 + x**6 + y*z**5
supp, g, N, Phi0, Ut = header('W2', U_W2)
fth = sp.simplify(supp[(1, 1)])
print('  f(theta) = phi_11 =', fth, ' = 6 + 4 cos 2t - cos 4t:', sp.simplify(fth - (6 + 4*sp.cos(2*t) - sp.cos(4*t))) == 0)
print('  f(tau) около 0:', sp.expand(sp.series(fth.subs(t, tau), tau, 0, 6).removeO()), ' => вырожденный максимум 9 - 8 tau^4')
uu = sp.symbols('u', real=True)
print('  min f: f = -2u^2 + 4u + 7, u = cos 2t in [-1,1]:', sp.simplify(fth.subs(t, sp.acos(uu)/2)), '; f(u=-1) =',
      (-2*uu**2 + 4*uu + 7).subs(uu, -1), ' > 0')
e0 = -(fth/4)**sp.Rational(1, 3)
Gb = sp.simplify(Phi0.subs(eps, e0))
print('  eps_0 = -(f/4)^(1/3) — единственная критическая точка Phi_0 = eps^4 + f eps, Phi_0\'\' = 12 eps_0^2 > 0;')
print('  G = Phi_0(eps_0) = -3 4^(-4/3) f^(4/3); G(tau) =',
      sp.nsimplify(sp.expand(sp.series((-3*4**sp.Rational(-4, 3)*(9 - 8*tau**4)**sp.Rational(4, 3)), tau, 0, 6).removeO())),
      ' => min порядка 4')

# ------------------------------------------------------------------------------------------
# W3 (= S1): расщепление ветви в минимуме, профиль не разделяется, условие (DE) с w = 1/2
kk = sp.Integer(1)
U_W3 = z**4 + z**2*y*rho2 - rho2**3 + kk*y**2*rho2**2 + x*z**5 + y**7
supp, g, N, Phi0, Ut = header('W3', U_W3)
print('  Phi_0 + 1 = (eps^2 + sin t/2)^2 + (k - 1/4) sin^2 t:',
      sp.simplify(Phi0 + 1 - ((eps**2 + sp.sin(t)/2)**2 + (kk - sp.Rational(1, 4))*sp.sin(t)**2)) == 0)
P = sp.expand((Phi0 + 1).subs(t, tau).subs(eps, e))
print('  профиль P(tau, e) = Phi_0(tau, e) + 1 =', P)
# (DE): tau P_tau + (1/2) e P_e - 2P = (tau cos tau - sin tau)(e^2 + 2 k sin tau)
EU = sp.simplify(tau*sp.diff(P, tau) + sp.Rational(1, 2)*e*sp.diff(P, e) - 2*P)
print('  tau P_tau + e P_e/2 - 2P =', sp.factor(sp.simplify(EU)),
      ' (проверка формулы:', sp.simplify(EU - (tau*sp.cos(tau) - sp.sin(tau))*(e**2 + 2*kk*sp.sin(tau))) == 0, ')')
# (CM) нарушено в tau = 0: при sin t < 0 у Phi_0(t, .) три критические точки
print('  d_eps Phi_0 =', sp.factor(sp.diff(Phi0, eps)), ' — при t = 0 тройной корень eps = 0, при sin t < 0 три простых')

# ------------------------------------------------------------------------------------------
# W4: G == 0 на первом ребре (две невырожденные ветви eps = +-1), уточнение => случай (a)
U_W4 = (z**2 - rho2**2)**2 + z*x**8
supp, g, N, Phi0, Ut = header('W4', U_W4)
print('  ветви eps = +-1, Phi_0\'\' = 8; G_+- == 0. Точные ветви: решаем d_eps U~ = 0 рядом с +-1')
for sgn in (1, -1):
    es = sp.symbols('es')
    # eps* = sgn + a1 sigma^2 + ...: подстановка в ряд
    a1, a2 = sp.symbols('a1 a2')
    trial = sgn + a1*sig**2 + a2*sig**4
    eq = sp.expand(sp.diff(Ut, eps).subs(eps, trial))
    sol = sp.solve([eq.coeff(sig, 2), eq.coeff(sig, 4)], [a1, a2], dict=True)[0]
    Gh = sp.expand(sp.series(Ut.subs(eps, trial.subs(sol)), sig, 0, 5).removeO())
    print('   ветвь', sgn, ': eps* =', trial.subs(sol), ' Ghat =', sp.simplify(Gh), ' => kappa\' = 2, G\' =', sp.simplify(Gh.coeff(sig, 2)))

# ------------------------------------------------------------------------------------------
# C1: G == -1 на всей окружности, вырожденный профиль e^4, (C) выполнено, (UR) нарушено
U_C1 = (z + x*y)**4 - rho2**3 + x**7 + z**3*y**4
supp, g, N, Phi0, Ut = header('C1', U_C1)
print('  ветвь eps_g = 0 кратности 3 по всей окружности, G == -1, профиль e^4')

# C2: G == const < 0, невырожденный профиль после сдвига, (R)
U_C2 = z**4 + z*rho2**2 + x**6*z + y**7
supp, g, N, Phi0, Ut = header('C2', U_C2)
print('  eps_0 = -4^(-1/3), Phi_0\'\' = 12 eps_0^2 > 0, G =', sp.nsimplify(Phi0.subs(eps, -4**sp.Rational(-1, 3))))

# ------------------------------------------------------------------------------------------
# D1: каскад, вырожденный жёсткий профиль (RCM, r' = 2), (UR)
U_D1 = (z - x*y - x**3)**4 + y**2*rho2**2 + x**7
supp, g, N, Phi0, Ut = header('D1', U_D1)
estar = sig*sp.cos(t)*sp.sin(t) + sig**3*sp.cos(t)**3
print('  U~ - (eps - eps*)^4 =', sp.simplify(Ut - (eps - estar)**4), '  => точная ветвь кратности 3 при всех sigma, M == 1')
Gh = sp.sin(t)**2 + sig**2*sp.cos(t)**7
print('  Ghat(sigma,theta) = U~(sigma,theta,eps*) = sin^2 t + sigma^2 cos^7 t:',
      sp.simplify(sp.expand(sp.expand_trig(Ut.subs(eps, estar) - Gh)).subs(sp.cos(t)**2, 1 - sp.sin(t)**2)) == 0)
f = sp.simplify(Gh.subs(t, sp.pi + tau))
print('  f(sigma,tau) = Ghat(sigma, pi + tau) =', f)
print('  d_tau f =', sp.factor(sp.diff(f, tau)), ' => полярная кривая tau = 0 (около 0), f(sigma,0) =', f.subs(tau, 0))
bb = sp.symbols('b', real=True)
prof = sp.simplify(sp.series(f.subs(tau, sig*bb)/sig**2, sig, 0, 1).removeO())
print('  sigma^-2 f(sigma, sigma b) -> ', prof, '  (Q_V = b^2, a = 1, Gamma_1 = 2, A\' = 1)')

# D2: каскад, (R): две невырожденные ветви eps = +-1, G_min = sin^2
U_D2 = (z**2 - rho2**2)**2 + y**2*rho2**3 + x**9 + z**3*x**6
supp, g, N, Phi0, Ut = header('D2', U_D2)
for sgn in (1, -1):
    a1, a2, a3 = sp.symbols('a1 a2 a3')
    trial = sgn + a1*sig + a2*sig**2 + a3*sig**3
    eq = sp.expand(sp.diff(Ut, eps).subs(eps, trial))
    sol = sp.solve([eq.coeff(sig, k) for k in (1, 2, 3)], [a1, a2, a3], dict=True)[0]
    Gh = sp.expand(sp.series(Ut.subs(eps, trial.subs(sol)), sig, 0, 5).removeO())
    print('   ветвь', sgn, ': Ghat = ', sp.simplify(Gh), ' + O(sigma^5)')
    fD = sp.simplify(Gh.subs(t, sp.pi + tau))
    prof = sp.simplify(sp.series(fD.subs(tau, sp.sqrt(sig)*bb).subs(sig, sp_), sp_, 0, 2).removeO()/sp_)
    print('     sigma^-1 Ghat(sigma, pi + sigma^(1/2) b) -> ', sp.simplify(sp.limit(prof, sp_, 0)), '  (Q_V = b^2, a = 1)')

# D3: G == 0 на первом ребре, уточнение kappa' = 2, затем каскад
U_D3 = (z**2 - rho2**2)**2 + z**2*y**2*rho2**2 + x**11
supp, g, N, Phi0, Ut = header('D3', U_D3)
for sgn in (1, -1):
    es2 = 1 - sig**2*sp.sin(t)**2/2
    print('   ветвь', sgn, ': eps*^2 = 1 - sigma^2 sin^2/2 — точная критическая точка:',
          sp.simplify(sp.diff(Ut, eps).subs(eps, sgn*sp.sqrt(es2))) == 0)
    Gh = sp.simplify(sp.expand(Ut.subs(eps, sgn*sp.sqrt(es2))))
    print('     Ghat =', sp.expand(Gh), ' => kappa\' = 2, G\' = sin^2 t >= 0, нули 0, pi')

# ------------------------------------------------------------------------------------------
# O2: складка (открытый случай): Phi_0 = (eps^2 - sin t)^2 - 1, G_min == -1 на дуге [0, pi]
U_O2 = z**4 - 2*z**2*y*rho2 - x**2*rho2**2 + x**7 + y**7
supp, g, N, Phi0, Ut = header('O2', U_O2)
print('  Phi_0 - ((eps^2 - sin t)^2 - 1) =', sp.simplify(Phi0 - ((eps**2 - sp.sin(t))**2 - 1)))
print('  профиль в складке t = 0: P(tau, e) = (e^2 - sin tau)^2 — нуль не изолирован (парабола), (CM) нарушено')
