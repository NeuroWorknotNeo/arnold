# [Эксперимент] Примеры §7 записки notes/prover/2026-10-21-gt3-hardcore.md.
# Для каждого примера: эффективный потенциал G = g_j (через ряд y*(s)), точка минимума,
# G'' (по натуральному параметру Sigma), знак G''+jG (условие декартовой карты, теорема 3),
# допустимое kappa теоремы 4, h_n, и численная проверка нормальной формы
#   U(Psi(s,theta,s^c e)) / s^j  ->  F_0(theta,e) = G(theta) + h_n(theta) e^2 / 2.
import sympy as sp
import mpmath as mp
from reduced import fiber_series, x, y, z, s

mp.mp.dps = 50
ph = sp.symbols('phi', real=True)
Q0 = x**2 + y**2 - z**2
# верхняя окружность конуса Q0=0: omega(phi), натуральный параметр theta = phi/sqrt2,
# T = d omega/d theta, n = omega x T, геодезическая кривизна k = 1
om = [sp.cos(ph)/sp.sqrt(2), sp.sin(ph)/sp.sqrt(2), 1/sp.sqrt(2)]
Tv = [-sp.sin(ph), sp.cos(ph), sp.Integer(0)]
nv = [-sp.cos(ph)/sp.sqrt(2), -sp.sin(ph)/sp.sqrt(2), 1/sp.sqrt(2)]

def kappa_bound(j, G0, Gpp, hn):
    lam0 = min(Gpp, hn)/4
    a0 = -G0
    return j*lam0/(a0*(15*sp.sqrt(3)/8*j + 2*sp.sqrt(2))**2)

def circle_example(name, U, m, order, phis=None):
    print('=' * 70)
    print(name, ':  U =', U)
    ys, R = fiber_series(U, m, om, [nv], order)
    gs = {m + i: sp.simplify(R.coeff(s, i)) for i in range(1, order + 1)}
    for k in sorted(gs):
        print('  g_%d(phi) =' % k, gs[k])
    j = min(k for k in gs if gs[k] != 0)
    G = gs[j]
    c = sp.Rational(j - m + 2, 2)
    print('  j =', j, ', c = (j-m+2)/2 =', c)
    # минимумы G по phi
    dG = sp.diff(G, ph)
    cands = phis if phis is not None else [sp.nsimplify(r) for r in
             set(round(float(mp.findroot(sp.lambdify(ph, dG, 'mpmath'), t0)), 12)
                 for t0 in [0.1 + 0.5*i for i in range(13)]) ]
    # контроль: глобальный минимум G по сетке, затем уточнение корня G'
    Gn = sp.lambdify(ph, G, 'mpmath')
    grid = [2*mp.pi*i/2000 for i in range(2000)]
    pg = min(grid, key=lambda t: Gn(t))
    pr = mp.findroot(sp.lambdify(ph, dG, 'mpmath'), pg)
    print('  контроль: минимум G по сетке при phi ~', mp.nstr(pr, 12), ', G =', mp.nstr(Gn(pr), 12))
    best = None
    for p0 in cands:
        val = float(G.subs(ph, p0))
        if best is None or val < best[1]:
            best = (p0, val)
    p0 = best[0]
    G0 = sp.nsimplify(sp.simplify(G.subs(ph, p0)))
    Gpp = sp.simplify(2*sp.diff(G, ph, 2).subs(ph, p0))   # d^2/dtheta^2 = 2 d^2/dphi^2
    U4 = sp.expand(Q0**2) if m == 4 else None
    hn = sp.simplify(sum(sp.diff(U4, a, b)*nv[i]*nv[jj] for i, a in enumerate((x, y, z))
                         for jj, b in enumerate((x, y, z))).subs({x: om[0], y: om[1], z: om[2]}))
    print('  минимум G при phi* =', p0, ': G(phi*) =', G0, '=', float(G0))
    print("  G''(theta*) =", Gpp, '=', float(Gpp), ';  h_n =', hn)
    vh = sp.simplify(Gpp + j*G0)
    print("  G'' + jG =", vh, '=', float(vh),
          '->', 'декартова карта (теорема 3) годится' if vh > 0 else 'нужна теорема 4 (kappa-карта)')
    kb = kappa_bound(j, G0, Gpp, hn)
    print('  kappa теоремы 4: kappa <=', float(kb))
    # численная проверка нормальной формы, theta = (phi - phi*)/sqrt2
    etastar = sp.expand(s*ys[0])
    Uf = sp.lambdify((x, y, z), U, 'mpmath')
    Gf = sp.lambdify(ph, G, 'mpmath')
    es = sp.lambdify((s, ph), etastar, 'mpmath')
    for (th, e) in [(0, 0), (0.05, 0.3), (-0.08, -0.5)]:
        phv = mp.mpf(float(p0)) + mp.sqrt(2)*th
        F0 = Gf(phv) + mp.mpf(float(hn))/2*e**2
        errs = []
        for sv in [mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')]:
            eta = es(sv, phv) + sv**mp.mpf(float(c))*e
            omv = [mp.cos(phv)/mp.sqrt(2), mp.sin(phv)/mp.sqrt(2), 1/mp.sqrt(2)]
            nvv = [-mp.cos(phv)/mp.sqrt(2), -mp.sin(phv)/mp.sqrt(2), 1/mp.sqrt(2)]
            q = [sv*omv[i] + eta*nvv[i] for i in range(3)]
            errs.append(mp.nstr(Uf(*q)/sv**j - F0, 4))
        print('  (theta,e)=(%g,%g): U/s^j - F0 при s=1e-2,1e-3,1e-4:' % (th, e), errs)
    return dict(j=j, G=G, G0=G0, Gpp=Gpp, hn=hn, phi0=p0, ys=ys, c=c)

res = {}
res['ex13'] = circle_example('Пример 13', Q0**2 + z**5*x + z**4*x*y + z**6/2, 4, 3,
                             phis=[5*sp.pi/6])
res['thmB'] = circle_example('Пример теоремы B', Q0**2 + x*z**4, 4, 2, phis=[sp.pi])
res['W5'] = circle_example('Q0^2 + W5, W5 = x z^4 + y^2 z^3', Q0**2 + x*z**4 + y**2*z**3, 4, 2,
                           phis=[sp.pi, 0, sp.pi/3, -sp.pi/3])
res['W7'] = circle_example('Q0^2 + W7, W7 = x z^6 + x y^2 z^4', Q0**2 + x*z**6 + x*y**2*z**4, 4, 4,
                           phis=[sp.pi, sp.acos(-sp.sqrt(sp.Rational(2, 3)))])
res['shift'] = circle_example('Сдвиг: Q0^2 + 2 Q0 z^2 x - z^6/10', Q0**2 + 2*Q0*z**2*x - z**6/10, 4, 3,
                              phis=[0, sp.pi, sp.pi/2])

# тождество для примера со сдвигом: g_6 = -(cos^2 phi + 1/10)/8
d = res['shift']['G'] + (sp.cos(ph)**2 + sp.Rational(1, 10))/8
print('shift: max|g_6 + (cos^2+1/10)/8| на сетке =',
      max(abs(float(d.subs(ph, 0.1*i))) for i in range(63)))
U8 = (Q0 + z**3)**2 + x*z**6 + x*y*z**5 + z**7/2
res['curved'] = circle_example('Искривлённое дно: (Q0 + z^3)^2 + x z^6 + x y z^5 + z^7/2', U8, 4, 4,
                               phis=[5*sp.pi/6])

# Регулярность нулей G на обеих окружностях (следствие K4'): результант числителей G и G'
# после подстановки t = tan(phi/2); отдельно точка phi = pi (t = oo).
tt = sp.symbols('t', real=True)
def regular_zeros(G, name):
    Gt = sp.together(sp.expand_trig(G).subs({sp.cos(ph): (1 - tt**2)/(1 + tt**2),
                                             sp.sin(ph): 2*tt/(1 + tt**2)}))
    num = sp.numer(sp.together(Gt))
    dnum = sp.numer(sp.together(sp.diff(Gt, tt)))
    res_ = sp.resultant(sp.Poly(num, tt), sp.Poly(dnum, tt))
    print('  %s: результант(G, G\') = %s; G(pi) = %s, G\'(pi) = %s' % (name, sp.nsimplify(res_),
          sp.nsimplify(G.subs(ph, sp.pi)), sp.nsimplify(sp.diff(G, ph).subs(ph, sp.pi))))
om_m = [sp.cos(ph)/sp.sqrt(2), sp.sin(ph)/sp.sqrt(2), -1/sp.sqrt(2)]
nv_m = [sp.cos(ph)/sp.sqrt(2), sp.sin(ph)/sp.sqrt(2), 1/sp.sqrt(2)]
ys_m, R_m = fiber_series(U8, 4, om_m, [nv_m], 3)
print('Нижняя окружность для U_(8): g_5, g_6, g_7 =', [sp.simplify(R_m.coeff(s, i)) for i in (1, 2, 3)])
regular_zeros(res['curved']['G'], 'G_+ (U_(8))')
regular_zeros(sp.simplify(R_m.coeff(s, 3)), 'G_- (U_(8))')

# Радиальное условие Четаева R = <grad U, q> < 0 на {U<0}: доля точек {U<0} около дна, где R > 0.
import random
def chetaev(name, U, info, nsamp=3000):
    Uf = sp.lambdify((x, y, z), U, 'mpmath')
    gr = [sp.lambdify((x, y, z), sp.diff(U, v), 'mpmath') for v in (x, y, z)]
    es = sp.lambdify((s, ph), sp.expand(s*info['ys'][0]), 'mpmath')
    c = mp.mpf(float(info['c'])); p0 = mp.mpf(float(info['phi0']))
    random.seed(3)
    out = []
    for sv in [mp.mpf('1e-2'), mp.mpf('1e-3')]:
        tot = bad = 0
        for _ in range(nsamp):
            phv = p0 + (2*random.random() - 1)*0.6
            e = (2*random.random() - 1)*0.3
            eta = es(sv, phv) + sv**c*e
            q = [sv*mp.cos(phv)/mp.sqrt(2) - eta*mp.cos(phv)/mp.sqrt(2),
                 sv*mp.sin(phv)/mp.sqrt(2) - eta*mp.sin(phv)/mp.sqrt(2), (sv + eta)/mp.sqrt(2)]
            if Uf(*q) < 0:
                tot += 1
                if sum(gr[i](*q)*q[i] for i in range(3)) > 0:
                    bad += 1
        out.append('s=%s: U<0 в %d точках, из них R>0 в %d' % (mp.nstr(sv, 2), tot, bad))
    print('Четаев,', name, ':', '; '.join(out))

for key, U in [('ex13', Q0**2 + z**5*x + z**4*x*y + z**6/2), ('thmB', Q0**2 + x*z**4),
               ('W7', Q0**2 + x*z**6 + x*y**2*z**4), ('shift', Q0**2 + 2*Q0*z**2*x - z**6/10),
               ('curved', U8)]:
    chetaev(key, U, res[key])
