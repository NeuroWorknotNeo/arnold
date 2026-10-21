"""R35: independent recomputation of examples M1, M2 of results/011 (§10) and of the
constants (0.4).  [Experiment]  Exact sympy where possible, mpmath for numerics."""
import sympy as sp
import mpmath as mp

x, y, z = sp.symbols('x y z', real=True)
s, eta, Y, ph, sig, eps, e = sp.symbols('s eta y phi sigma epsilon e', real=True)

M1 = (z - x**2)**4 + x**5 + y**5 + x*y**6 + y*x**6
M2 = z**4 + z*(x**4 + x**3*y + y**4) + x**6 + x*z**5 + 2*y*z**5

c, si = sp.cos(ph), sp.sin(ph)


def analyse(U, name, m=4, r=2):
    print('=' * 70, '\n', name)
    # u_m
    P = sp.Poly(sp.expand(U), x, y, z)
    um = sum(cf * x**a * y**b * z**cc for (a, b, cc), cf in P.terms() if a + b + cc == m)
    print('u_m =', um, ' lowest degree =', min(a + b + cc for (a, b, cc), _ in P.terms()))
    # (M): u_m(omega + y n) with omega=(cos,sin,0), n=e_z
    print('u_m(omega+y n) =', sp.simplify(um.subs({x: c, y: si, z: Y}, simultaneous=True)))
    # phi(s,theta,y) = U(s(omega+y n))/s^m
    phi = sp.expand(sp.simplify(U.subs({x: s*c, y: s*si, z: s*Y}, simultaneous=True) / s**m))
    Pphi = sp.Poly(phi, s, Y)
    supp = {}
    for (i, l), cf in Pphi.terms():
        cf = sp.simplify(sp.trigsimp(cf))
        if cf != 0:
            supp[(i, l)] = cf
    print('support S =', sorted(supp))
    cand = [sp.Rational(i, 2*r - l) for (i, l) in supp if l < 2*r]
    gs = min(cand)
    N = sp.fraction(gs)[1]
    beta1 = 2*r*gs
    j = m + beta1
    cw = 1 + gs
    print('gamma_* =', gs, ' N =', N, " beta' =", beta1, ' j =', j, ' c =', cw)
    # check beta'(gamma_*) = min(i + gs l)
    print("min(i+gamma l) over S =", min(i + gs*l for (i, l) in supp))
    Phi0 = sum(cf * eps**l for (i, l), cf in supp.items() if i + gs*l == beta1)
    print('Phi0 =', sp.simplify(Phi0))
    Ut = sum(cf * sig**(N*i + N*gs*l - N*beta1) * eps**l for (i, l), cf in supp.items())
    print('Utilde =', sp.factor(sp.simplify(Ut)))
    # check (0.3): U(s omega + s^{1+g} eps n) = s^{m+beta'} Utilde(s^{1/N})
    lhs = U.subs({x: s*c, y: s*si, z: s**(1+gs)*eps}, simultaneous=True)
    rhs = s**(m+beta1) * Ut.subs(sig, s**sp.Rational(1, N))
    print('(0.3) residual =', sp.simplify(sp.expand(lhs - rhs)))
    return dict(phi=phi, supp=supp, gs=gs, N=N, j=j, c=cw, Phi0=sp.simplify(Phi0), Ut=Ut)


R1 = analyse(M1, 'M1')
# U(s omega + eta n) formula
lhs = M1.subs({x: s*c, y: s*si, z: eta}, simultaneous=True)
G1 = c**5 + si**5
g7 = c*si**6 + si*c**6
print('M1 formula residual:', sp.simplify(sp.expand(lhs - ((eta - s**2*c**2)**4 + s**5*G1 + s**7*g7))))
print('Utilde - claimed:', sp.simplify(sp.expand(R1['Ut'] - ((eps - sig**3*c**2)**4 + G1 + sig**8*g7))))
G1p = sp.diff(G1, ph)
print("G' - claimed:", sp.simplify(G1p - 5*si*c*(si**3 - c**3)))
for p0 in [0, sp.pi/2, sp.pi, 3*sp.pi/2, sp.pi/4, 5*sp.pi/4]:
    print(f'  phi={p0}: G={sp.nsimplify(sp.simplify(G1.subs(ph,p0)))}, G\'={sp.simplify(G1p.subs(ph,p0))}, '
          f'G\'\'={sp.nsimplify(sp.simplify(sp.diff(G1,ph,2).subs(ph,p0)))}')
# all critical points of G on [0,2pi): solve numerically
fG = sp.lambdify(ph, G1p, 'mpmath')
roots = set()
for k in range(400):
    try:
        rt = mp.findroot(fG, 2*mp.pi*k/400)
        rt = float(rt % (2*mp.pi))
        roots.add(round(rt, 8))
    except Exception:
        pass
print('M1 critical points of G (numeric):', sorted(roots))


def kappa_bound(beta, a0, lam0):
    return beta*lam0 / (a0*(15*mp.sqrt(3)/8*beta + 2*mp.sqrt(2))**2)

print('M1 kappa bound:', kappa_bound(5, 1, mp.mpf(5)/4))

R2 = analyse(M2, 'M2')
f = c**4 + c**3*si + si**4
lhs = M2.subs({x: s*c, y: s*si, z: eta}, simultaneous=True)
print('M2 formula residual:', sp.simplify(sp.expand(lhs - (eta**4 + s**4*f*eta + s**6*c**6 + s*eta**5*(c + 2*si)))))
print('Utilde - claimed:', sp.simplify(sp.expand(R2['Ut'] - (eps**4 + f*eps + sig**2*c**6 + sig**7*eps**5*(c + 2*si)))))
print('f identity:', sp.simplify(sp.expand_trig(f - (sp.Rational(3, 4) + sp.cos(4*ph)/4 + sp.sin(2*ph)/4 + sp.sin(4*ph)/8))))
fn = sp.lambdify(ph, f, 'mpmath')
fmin = min(fn(2*mp.pi*k/20000) for k in range(20000))
print('min f (grid) =', fmin, ' >= 1/8:', fmin >= 0.125)
# eps0, G, profile
e0 = sp.Symbol('e0', real=True)
Phi0 = eps**4 + sp.Symbol('F')*eps
F = sp.Symbol('F', positive=True)
e0expr = -(F/4)**sp.Rational(1, 3)
print('dPhi0 at eps0:', sp.simplify(4*e0expr**3 + F))
Gexpr = sp.simplify(e0expr**4 + F*e0expr)
print('G - (-3*4^{-4/3} F^{4/3}):', sp.simplify(Gexpr + 3*sp.Integer(4)**sp.Rational(-4, 3)*F**sp.Rational(4, 3)))
print('profile identity:', sp.simplify(sp.expand((e0 + e)**4 + F*(e0 + e) - e0**4 - F*e0 - e**2*((e + 2*e0)**2 + 2*e0**2)).subs(F, -4*e0**3)))
# f' and cubic
fp = sp.diff(f, ph)
t = sp.Symbol('t')
print("f' - cos^4*cubic(tan):", sp.simplify(sp.expand_trig(fp - c**4*(4*sp.tan(ph)**3 - 3*sp.tan(ph)**2 - 4*sp.tan(ph) + 1))))
print("f'' - claimed:", sp.simplify(sp.expand_trig(sp.diff(f, ph, 2) - (-4*sp.cos(4*ph) - sp.sin(2*ph) - 2*sp.sin(4*ph)))))
cub = 4*t**3 - 3*t**2 - 4*t + 1
print('cubic(0.22), cubic(0.23):', cub.subs(t, sp.Rational(22, 100)), cub.subs(t, sp.Rational(23, 100)))
print('cubic real roots:', [sp.N(rr, 10) for rr in sp.real_roots(sp.Poly(cub, t))])
print('intervals:', sp.Poly(cub, t).intervals(eps=sp.Rational(1, 10**8)))
mp.mp.dps = 30
t2 = mp.findroot(lambda tt: 4*tt**3 - 3*tt**2 - 4*tt + 1, 0.2236)
phs = mp.atan(t2)
print('t2 =', t2, ' phi* =', phs)
print('4 atan(0.22), 4 atan(0.23):', 4*mp.atan(0.22), 4*mp.atan(0.23), ' cos(0.905)=', mp.cos(0.905))
Gf = lambda p: -3*mp.mpf(4)**(-mp.mpf(4)/3)*fn(p)**(mp.mpf(4)/3)
for name, p in [('phi*', phs), ('pi/2', mp.pi/2), ('phi*+pi', phs + mp.pi), ('3pi/2', 3*mp.pi/2)]:
    G0 = Gf(p); G1d = mp.diff(Gf, p); G2 = mp.diff(Gf, p, 2)
    e0v = -(fn(p)/4)**(mp.mpf(1)/3)
    print(f'  {name}: G={mp.nstr(G0,10)} G\'={mp.nstr(G1d,5)} G\'\'={mp.nstr(G2,10)} eps0={mp.nstr(e0v,8)} '
          f'G\'\'+jG={mp.nstr(G2 + mp.mpf(16)/3*G0,6)} kappa<={mp.nstr(kappa_bound(mp.mpf(16)/3, -G0, G2/4),6)} '
          f'f\'\'={mp.nstr(mp.diff(fn,p,2),8)}')
for tt in [-0.8263205, 1.3526517]:
    rt = mp.findroot(lambda q: 4*q**3 - 3*q**2 - 4*q + 1, tt)
    p = mp.atan(rt)
    print(f'  atan(t)={mp.nstr(p,8)} t={mp.nstr(rt,10)}: G\'\'={mp.nstr(mp.diff(Gf,p,2),8)} (max if <0)')
print('pi/2 exact: G\'\'+jG =', sp.simplify(sp.Integer(4)**sp.Rational(2, 3) - 16*sp.Integer(4)**sp.Rational(-4, 3)))
print('M2 |e| bound check: p0 = 6 eps0^2 -> |e| <= sqrt(4delta/(6 eps0^2)) = sqrt(2delta/3)/|eps0|')
