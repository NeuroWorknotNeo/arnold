# [Эксперимент] Функция дна F_fl(s,theta) = min_{|y|<=y1} U(s(omega + y n)) для примеров записки
# notes/prover/2026-10-21-morse-bott-mult.md, §10, и сравнение с предсказанием теорем W, C, D:
#   W: min_theta F_fl / s^j -> min G_min = -a0;           C: F_fl / s^j -> -a0 равномерно по theta;
#   D: min_theta F_fl / s^beta_d -> -a, точка минимума theta(s) -> theta_*.
# Минимум по слою: все вещественные корни d_y phi (mp.polyroots) на [-y1, y1] и концы отрезка.
import mpmath as mp
import sympy as sp

mp.mp.dps = 50
x, y, z = sp.symbols('x y z', real=True)
s_, t_, yv = sp.symbols('s t yv', real=True)
rho2 = x**2 + y**2
f4 = 6*rho2**2 + 4*(x**2 - y**2)*rho2 - (x**4 - 6*x**2*y**2 + y**4)
G2 = -3*(sp.Rational(9, 4))**sp.Rational(4, 3)      # G(0) для W2: -3 4^(-4/3) 9^(4/3)
# имя: (U, тип, показатель, предсказанное значение, theta_* или None)
EX = {
    'W1': ((z - x**2)**4 + sp.Rational(3, 2)*x*rho2**2 - sp.Rational(1, 2)*x**3*rho2 + y*z**5, 'W', 5, -1, sp.pi),
    'W2': (z**4 + z*f4 + x**6 + y*z**5, 'W', sp.Rational(16, 3), G2, 0),
    'W3': (z**4 + z**2*y*rho2 - rho2**3 + y**2*rho2**2 + x*z**5 + y**7, 'W', 6, -1, 0),
    'W4': ((z**2 - rho2**2)**2 + z*x**8, 'W', 10, -1, 0),       # после уточнения: beta = 8 + 2 = 10
    'C1': ((z + x*y)**4 - rho2**3 + x**7 + z**3*y**4, 'C', 6, -1, None),
    'C2': (z**4 + z*rho2**2 + x**6*z + y**7, 'C', sp.Rational(16, 3), -3*2**sp.Rational(1, 3)/8, None),
    'D1': ((z - x*y - x**3)**4 + y**2*rho2**2 + x**7, 'D', 7, -1, sp.pi),
    'D2': ((z**2 - rho2**2)**2 + y**2*rho2**3 + x**9 + z**3*x**6, 'D', 9, -1, sp.pi),
    'D3': ((z**2 - rho2**2)**2 + z**2*y**2*rho2**2 + x**11, 'D', 11, -1, sp.pi),
}
Y1 = mp.mpf('0.5')


def fiber_poly(U):
    q = {x: s_*sp.cos(t_), y: s_*sp.sin(t_), z: s_*yv}
    phi = sp.expand(U.subs(q, simultaneous=True))      # = U(s(omega + yv n)), многочлен по yv
    P = sp.Poly(phi, yv)
    coeffs = [sp.lambdify((s_, t_), c, 'mpmath') for c in P.all_coeffs()]
    return coeffs


def Ffl(coeffs, s, t):
    cs = [c(s, t) for c in coeffs]
    while abs(cs[0]) < mp.mpf(10)**(-40)*max(abs(c) for c in cs):   # старший коэффициент может обнулиться
        cs = cs[1:]
    deg = len(cs) - 1
    val = lambda yy: mp.polyval(cs, yy)
    dcs = [cs[i]*(deg - i) for i in range(deg)]
    while abs(dcs[0]) < mp.mpf(10)**(-40)*max(abs(c) for c in dcs):
        dcs = dcs[1:]
    best = min(val(-Y1), val(Y1))
    arg = -Y1 if val(-Y1) < val(Y1) else Y1
    try:
        roots = mp.polyroots(dcs, maxsteps=200, extraprec=200)
    except mp.libmp.libhyper.NoConvergence:
        roots = mp.polyroots(dcs, maxsteps=2000, extraprec=800)
    for r in roots:
        if abs(mp.im(r)) < mp.mpf(10)**(-30) and abs(mp.re(r)) <= Y1:
            v = val(mp.re(r))
            if v < best:
                best, arg = v, mp.re(r)
    return best, arg


for name, (U, kind, expo, pred, thstar) in EX.items():
    coeffs = fiber_poly(U)
    print('=' * 90)
    print(name, '(случай %s): предсказание %s -> %s' % (kind, 'min_theta F_fl/s^%s' % expo if kind != 'C' else 'F_fl/s^%s' % expo,
                                                         mp.nstr(mp.mpf(sp.N(pred, 40)), 12)))
    for s in [mp.mpf(10)**(-k) for k in (2, 3, 4, 6)]:
        if kind == 'C':
            vals = [Ffl(coeffs, s, 2*mp.pi*k/64)[0]/s**mp.mpf(sp.N(expo, 40)) for k in range(64)]
            print('   s=%-8s  min_theta = %-16s max_theta = %-16s' % (mp.nstr(s, 3), mp.nstr(min(vals), 12), mp.nstr(max(vals), 12)))
        else:
            th0 = mp.mpf(sp.N(thstar, 40))
            # грубая сетка по всей окружности + уточнение около лучшей точки
            grid = [2*mp.pi*k/256 for k in range(256)]
            vals = [(Ffl(coeffs, s, t)[0], t) for t in grid]
            vbest, tbest = min(vals)
            f = lambda t: Ffl(coeffs, s, t)[0]
            a, b = tbest - 2*mp.pi/256, tbest + 2*mp.pi/256
            for _ in range(60):          # золотое сечение
                m1, m2 = a + (b - a)*mp.mpf('0.382'), a + (b - a)*mp.mpf('0.618')
                if f(m1) < f(m2):
                    b = m2
                else:
                    a = m1
            tb = (a + b)/2
            vb, yb = Ffl(coeffs, s, tb)
            dth = tb - th0
            dth = (dth + mp.pi) % (2*mp.pi) - mp.pi
            print('   s=%-8s  min F_fl/s^%s = %-16s в theta - theta_* = %-12s  (y/s^... : y = %s)' % (
                mp.nstr(s, 3), expo, mp.nstr(vb/s**mp.mpf(sp.N(expo, 40)), 12), mp.nstr(dth, 4), mp.nstr(yb, 6)))
