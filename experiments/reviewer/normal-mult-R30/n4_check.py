"""R30. [Эксперимент] Лемма N4 (невырожденная ветвь: точное дно и уточнение).

A. M2: eps*(sigma,theta) — ряд по sigma (sympy), hat G(0,theta) = Phi0(theta,eps0) = G,
   и численная проверка (2.1)+(b): U(s w + eta* n) = s^beta hat G(s^{1/N},theta).
B. Синтетика с k=1: phi = (y^2 - s)^2 + th s^2 y + g(th) s^3, gamma=1/2, N=2, beta'=2,
   U~ = (e^2-1)^2 + sigma th e + sigma^2 g; ветвь eps0=+1 (невырожденная, d^2Phi0 = 8).
   Проверка формулы (c): phi(s, (eta*+s^{c'} e)/s) = s^{beta''-m}[hat G^{(k)}(tau^2) + e^2 M(tau^2, tau^k e)],
   c' = c + k/(2N), beta'' = beta + k/N, tau = s^{1/(2N)}; и значение скобки при tau=0.
"""
import sympy as sp
import mpmath as mp

mp.mp.dps = 50
sig, th, e, eps = sp.symbols('sigma theta e epsilon', real=True)

# ---------- A. M2 ----------
f = sp.cos(th)**4 + sp.cos(th)**3*sp.sin(th) + sp.sin(th)**4
Ut = eps**4 + f*eps + sig**2*sp.cos(th)**6 + sig**7*eps**5*(sp.cos(th) + 2*sp.sin(th))
F = sp.symbols('F', positive=True)
e0 = -(F/4)**sp.Rational(1, 3)
# ряд eps* = e0 + a2 sigma^2 + ... (U~ зависит от sigma через sigma^2 и sigma^7)
K = 9
a = sp.symbols('a1:%d' % (K + 1))
UtF = eps**4 + F*eps + sig**2*sp.Symbol('C6') + sig**7*eps**5*sp.Symbol('L')
es = e0 + sum(a[k]*sig**(k + 1) for k in range(K))
dU = sp.expand(sp.series(sp.diff(UtF, eps).subs(eps, es), sig, 0, K + 1).removeO())
sol = {}
for k in range(1, K + 1):
    co = sp.expand(dU.coeff(sig, k).subs(sol))
    sk = sp.solve(co, a[k - 1])
    sol[a[k - 1]] = sp.simplify(sk[0])
print('A. M2: eps* = e0 + ', sp.simplify(sum(sol[a[k]]*sig**(k + 1) for k in range(4))), '+ ...')
Ghat = sp.series(UtF.subs(eps, es.subs(sol)), sig, 0, 4).removeO()
Ghat = sp.simplify(sp.expand(Ghat))
print('   hat G (до sigma^3):', Ghat)
G0 = sp.simplify(Ghat.subs(sig, 0) - (-3*sp.Rational(1, 4)**sp.Rational(4, 3)*F**sp.Rational(4, 3)))
print('   hat G(0) - (-3*4^{-4/3} F^{4/3}) =', G0)

# численно: theta = phi*, s малые; eta* из корня d/d eta U, сравнить с s^beta hat G
def U_M2(s, phi, eta):
    c, sn = mp.cos(phi), mp.sin(phi)
    x, y_, z = s*c, s*sn, eta
    return z**4 + z*(x**4 + x**3*y_ + y_**4) + x**6 + x*z**5 + 2*y_*z**5

phis = mp.atan(mp.findroot(lambda t: 4*t**3 - 3*t**2 - 4*t + 1, 0.2237))
for s in [mp.mpf('1e-3'), mp.mpf('1e-6'), mp.mpf('1e-9')]:
    c, sn = mp.cos(phis), mp.sin(phis)
    fv = c**4 + c**3*sn + sn**4
    e0v = -(fv/4)**(mp.mpf(1)/3)
    eta = mp.findroot(lambda t: mp.diff(lambda u: U_M2(s, phis, u), t), s**(mp.mpf(4)/3)*e0v)
    val = U_M2(s, phis, eta) / s**(mp.mpf(16)/3)
    sigv = s**(mp.mpf(1)/3)
    # U~ на eps* (численный корень) == U/s^beta
    es_num = eta / s**(mp.mpf(4)/3)
    Utv = es_num**4 + fv*es_num + sigv**2*c**6 + sigv**7*es_num**5*(c + 2*sn)
    print(f'   s={mp.nstr(s,3)}: U(s w+eta* n)/s^(16/3) = {mp.nstr(val,15)},  U~(sigma,eps*) = {mp.nstr(Utv,15)},'
          f'  G = {mp.nstr(-3*mp.mpf(4)**(-mp.mpf(4)/3)*fv**(mp.mpf(4)/3),12)}')

# ---------- B. синтетика с k = 1 ----------
print('B. k=1: phi = (y^2-s)^2 + th s^2 y + g s^3')
gq = sp.Symbol('g')
UtB = (eps**2 - 1)**2 + sig*th*eps + sig**2*gq
KB = 6
b = sp.symbols('b1:%d' % (KB + 1))
esB = 1 + sum(b[k]*sig**(k + 1) for k in range(KB))
dUB = sp.expand(sp.diff(UtB, eps).subs(eps, esB))
solB = {}
for k in range(1, KB + 1):
    co = sp.expand(dUB.coeff(sig, k).subs(solB))
    solB[b[k - 1]] = sp.solve(co, b[k - 1])[0]
esB_s = sp.expand(esB.subs(solB))
GhB = sp.expand(sp.series(UtB.subs(eps, esB_s), sig, 0, 4).removeO())
print('   eps* =', sp.series(esB_s, sig, 0, 3), '  hat G =', GhB)
print('   k = 1, G_1 =', GhB.coeff(sig, 1), ';  1/2 d^2 Phi0(eps0=1) =', sp.diff((eps**2 - 1)**2, eps, 2).subs(eps, 1)/2)

# численная проверка формулы (c) с точным eps* (корень) и M (квадратура)
N, gam, k = 2, mp.mpf(1)/2, 1
c_ = 1 + gam
cp = c_ + mp.mpf(k)/(2*N)
bpp_minus_m = 2*2*gam + mp.mpf(k)/N   # beta'' - m = beta' + k/N
for (thv, gv) in [(mp.mpf('0.3'), mp.mpf('0.7')), (mp.mpf('-0.5'), mp.mpf('-1.1')), (mp.mpf(0), mp.mpf(2))]:
    for s in [mp.mpf('1e-2'), mp.mpf('1e-4'), mp.mpf('1e-8')]:
        sigv = s**(mp.mpf(1)/N)
        tau = s**(mp.mpf(1)/(2*N))
        Ut_num = lambda E: (E**2 - 1)**2 + sigv*thv*E + sigv**2*gv
        dUt = lambda E: 4*E*(E**2 - 1) + sigv*thv
        estar = mp.findroot(dUt, 1)
        Gh = Ut_num(estar)
        Ghk = Gh / sigv**k
        for ev in [mp.mpf('0.9'), mp.mpf('-0.4')]:
            phi_val = lambda yy: (yy**2 - s)**2 + thv*s**2*yy + gv*s**3
            eta_star = s**c_ * estar
            lhs = phi_val((eta_star + s**cp*ev)/s)
            e1 = tau**k*ev
            M = mp.quad(lambda t: (1 - t)*(12*(estar + t*e1)**2 - 4), [0, 1])
            rhs = s**bpp_minus_m * (Ghk + ev**2*M)
            rel = abs(lhs - rhs)/abs(rhs)
            br0 = thv + 4*ev**2
            print(f'   th={mp.nstr(thv,3):>5} s={mp.nstr(s,2):>6} e={mp.nstr(ev,2):>5}: |lhs-rhs|/|rhs| = {mp.nstr(rel,3):>9};'
                  f'  скобка = {mp.nstr(Ghk + ev**2*M, 10)}, при tau=0: G_1+4e^2 = {mp.nstr(br0, 10)}')
