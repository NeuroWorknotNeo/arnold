# R31: independent check of examples M1, M2 (§5 of notes/prover/2026-10-21-normal-multiplicity.md)
import sympy as sp
from fractions import Fraction as Fr
X, Yv, Z = sp.symbols('x y z', real=True)
s, yy, ph, eps, sig, e = sp.symbols('s y phi varepsilon sigma e', real=True)
c, sn = sp.cos(ph), sp.sin(ph)

def analyse(name, U, m, gam, N):
    print('='*20, name)
    P = sp.Poly(sp.expand(U), X, Yv, Z)
    low = min(sum(mon) for mon in P.monoms())
    um = sum(coef*X**a*Yv**b*Z**cc for (a, b, cc), coef in zip(P.monoms(), P.coeffs()) if a+b+cc == low)
    print('lowest degree m =', low, ' u_m =', um)
    assert low == m
    # cone parametrisation q = s(omega + y n), omega=(cos,sin,0), n=e_z
    phi_fun = sp.expand(sp.expand(U.subs({X: s*c, Yv: s*sn, Z: s*yy}))/s**m)
    Pp = sp.Poly(phi_fun, s, yy)
    supp = {}
    for (i, l), co in zip(Pp.monoms(), Pp.coeffs()):
        co = sp.simplify(co)
        if co != 0:
            supp[(i, l)] = co
    print('support S =', sorted(supp))
    # u_m(omega+y n)
    print('u_m(omega+yn) =', sp.simplify(um.subs({X: c, Yv: sn, Z: yy})))
    # gamma_*: 2r = 4
    r2 = 4
    gs = min(Fr(i, r2-l) for (i, l) in supp if l < r2)
    print('gamma_* =', gs, ' (claimed', gam, ')')
    assert gs == gam
    beta_p = min(Fr(i) + gs*l for (i, l) in supp)
    j = m + beta_p
    print("beta' =", beta_p, ' j =', j, ' c =', 1+gs, ' N =', N)
    Phi0 = sum(co*eps**l for (i, l), co in supp.items() if Fr(i)+gs*l == beta_p)
    print('Phi_0 =', sp.simplify(Phi0))
    # tilde U and identity (2.1): U(s omega + s^{1+g} eps n) = s^{m+beta'} tildeU(s^{1/N},...)
    tU = sum(co*sig**int(N*i + N*gs*l - N*beta_p)*eps**l for (i, l), co in supp.items())
    lhs = U.subs({X: sig**N*c, Yv: sig**N*sn, Z: sig**(N*(1+gs))*eps})
    rhs = sig**int(N*(m+beta_p))*tU
    print('tilde U =', sp.simplify(tU))
    print('(2.1) identity diff =', sp.simplify(sp.expand(lhs - rhs)))
    return supp, Phi0, tU, j

# ---------------- M1
U1 = (Z - X**2)**4 + X**5 + Yv**5 + X*Yv**6 + Yv*X**6
supp, Phi0, tU, j = analyse('M1', U1, 4, Fr(1, 4), 4)
G = c**5 + sn**5
print('Phi0 - eps^4 - G =', sp.simplify(Phi0 - eps**4 - G))
print('claimed tildeU diff =', sp.simplify(sp.expand(tU - ((eps - sig**3*c**2)**4 + G + sig**8*(c*sn**6 + sn*c**6)))))
G1 = sp.diff(G, ph); G2 = sp.diff(G, ph, 2)
print("G' - 5 sin cos (sin^3-cos^3) =", sp.simplify(G1 - 5*sn*c*(sn**3 - c**3)))
for p in [0, sp.pi/2, sp.pi, 3*sp.pi/2, sp.pi/4, 5*sp.pi/4]:
    print(f'  phi={p}: G={sp.nsimplify(sp.simplify(G.subs(ph,p)))}, G\'={sp.simplify(G1.subs(ph,p))}, G\'\'={sp.nsimplify(sp.simplify(G2.subs(ph,p)))}, G\'\'+5G={sp.simplify((G2+5*G).subs(ph,p))}')
# all critical points on [0,2pi): G'=0 <=> sin=0 or cos=0 or tan=1
sols = sp.solveset(G1, ph, sp.Interval.Ropen(0, 2*sp.pi))
print('critical points of G on [0,2pi):', sols)
# constants (4.0)
def kappa_bound(beta, a0, lam0):
    return beta*lam0/(a0*(sp.Rational(15, 8)*sp.sqrt(3)*beta + 2*sp.sqrt(2))**2)
print('M1 kappa bound =', sp.N(kappa_bound(5, 1, sp.Rational(5, 4))))

# ---------------- M2
U2 = Z**4 + Z*(X**4 + X**3*Yv + Yv**4) + X**6 + X*Z**5 + 2*Yv*Z**5
supp, Phi0, tU, j = analyse('M2', U2, 4, Fr(1, 3), 3)
f = c**4 + c**3*sn + sn**4
print('Phi0 - eps^4 - f eps =', sp.simplify(Phi0 - eps**4 - f*eps))
print('claimed tildeU diff =', sp.simplify(sp.expand(tU - (eps**4 + f*eps + sig**2*c**6 + sig**7*eps**5*(c + 2*sn)))))
print('f trig identity diff =', sp.simplify(sp.expand_trig(f - (sp.Rational(3, 4) + sp.cos(4*ph)/4 + sp.sin(2*ph)/4 + sp.sin(4*ph)/8))))
fpos = sp.symbols('fpos', positive=True)
e0 = -(fpos/4)**sp.Rational(1, 3)
Phi0f = eps**4 + fpos*eps
print('d Phi0 at eps0 =', sp.simplify(sp.diff(Phi0f, eps).subs(eps, e0)), ' d2 =', sp.simplify(sp.diff(Phi0f, eps, 2).subs(eps, e0) - 12*e0**2))
Gf = sp.simplify(Phi0f.subs(eps, e0))
print('G - (-3*4^(-4/3) f^(4/3)) =', sp.simplify(Gf + 3*4**sp.Rational(-4, 3)*fpos**sp.Rational(4, 3)), '; G - 3/4 f eps0 =', sp.simplify(Gf - sp.Rational(3, 4)*fpos*e0))
ee = sp.symbols('e0', real=True)
prof = sp.expand((ee + e)**4 + (-4*ee**3)*(ee + e) - (ee**4 + (-4*ee**3)*ee))   # f = -4 eps0^3
print('profile - e^2[(e+2e0)^2+2e0^2] =', sp.simplify(prof - e**2*((e + 2*ee)**2 + 2*ee**2)))
# G'(phi) and G''
Gphi = -3*4**sp.Rational(-4, 3)*f**sp.Rational(4, 3)
Gp = sp.diff(Gphi, ph)
print("G' + 4^(-1/3) f^(1/3) f' =", sp.simplify(Gp + 4**sp.Rational(-1, 3)*f**sp.Rational(1, 3)*sp.diff(f, ph)))
t = sp.symbols('t', real=True)
fp = sp.diff(f, ph)
print("f' - cos^4 (4t^3-3t^2-4t+1) =", sp.simplify((fp - c**4*(4*sp.tan(ph)**3 - 3*sp.tan(ph)**2 - 4*sp.tan(ph) + 1))))
fpp = sp.diff(f, ph, 2)
print("f'' - (-4cos4phi - sin2phi - 2 sin4phi) =", sp.simplify(sp.expand_trig(fpp - (-4*sp.cos(4*ph) - sp.sin(2*ph) - 2*sp.sin(4*ph)))))
cub = 4*t**3 - 3*t**2 - 4*t + 1
print('cubic at 0.22, 0.23:', cub.subs(t, sp.Rational(22, 100)), cub.subs(t, sp.Rational(23, 100)))
print('real root isolation:', sp.Poly(cub, t).intervals(eps=sp.Rational(1, 10**6)))
print('cubic discriminant:', sp.discriminant(cub, t))
# interval check at phi*: phi* in (atan .22, atan .23)
import mpmath as mp
mp.mp.dps = 40
lo, hi = mp.atan(mp.mpf('0.22')), mp.atan(mp.mpf('0.23'))
print('phi* in', lo, hi, ' 4phi* in', 4*lo, 4*hi, ' cos(4hi)=', mp.cos(4*hi), ' pi/2=', mp.pi/2)
# rigorous-ish: f'' <= -4 cos(4 hi) on the interval since sin2phi, sin4phi>0 and cos4phi decreasing
print('upper bound f\'\' < -4cos(4*hi) =', -4*mp.cos(4*hi))
t2 = [r for r in sp.Poly(cub, t).nroots(n=30) if 0 < r < 1][0]
phs = mp.atan(mp.mpf(str(t2)))
fN = sp.lambdify(ph, f, 'mpmath'); fppN = sp.lambdify(ph, fpp, 'mpmath')
GN = lambda p: -3*mp.mpf(4)**(-mp.mpf(4)/3)*fN(p)**(mp.mpf(4)/3)
G2N = lambda p: mp.diff(GN, p, 2)
print('phi* =', phs, ' f=', fN(phs), " f''=", fppN(phs), ' G=', GN(phs), " G''=", G2N(phs), ' eps0=', -(fN(phs)/4)**(mp.mpf(1)/3), " G''+jG=", G2N(phs) + mp.mpf(16)/3*GN(phs))
pp = mp.pi/2
print('phi=pi/2: f=', fN(pp), " f''=", fppN(pp), ' G=', GN(pp), " G''=", G2N(pp), " G''+jG=", G2N(pp) + mp.mpf(16)/3*GN(pp))
# exact G''(pi/2) + j G(pi/2)
exact = sp.simplify(sp.diff(Gphi, ph, 2).subs(ph, sp.pi/2) + sp.Rational(16, 3)*Gphi.subs(ph, sp.pi/2))
print("exact G''(pi/2)+jG(pi/2) =", exact, ' G''(pi/2)=', sp.simplify(sp.diff(Gphi, ph, 2).subs(ph, sp.pi/2)))
for r in sp.Poly(cub, t).nroots(n=20):
    p_ = mp.atan(mp.mpf(str(r)))
    print('  root t=', r, ' phi=', p_, " G''=", G2N(p_), ' f=', fN(p_))
# other critical points: phi=pi/2 (cos=0); f periodic with pi
print('f(phi+pi)-f(phi) =', sp.simplify(f.subs(ph, ph + sp.pi) - f))
# constants (4.0)
for nm, p_ in [('phi*', phs), ('pi/2', pp)]:
    a0 = -GN(p_); lam0 = G2N(p_)/4; b = mp.mpf(16)/3
    kb = b*lam0/(a0*(mp.mpf(15)/8*mp.sqrt(3)*b + 2*mp.sqrt(2))**2)
    print(f'  {nm}: a0={mp.nstr(a0,8)} lam0={mp.nstr(lam0,8)} kappa<= {mp.nstr(kb,6)}, eps0={mp.nstr(-(fN(p_)/4)**(mp.mpf(1)/3),8)}')
# min of f over circle (lower bound 1/8 claimed)
import numpy as np
phs_grid = np.linspace(0, 2*np.pi, 200001)
fv = np.cos(phs_grid)**4 + np.cos(phs_grid)**3*np.sin(phs_grid) + np.sin(phs_grid)**4
print('numerical min f =', fv.min())
