"""[Эксперимент] R27: лемма V записки notes/prover/2026-10-21-morse-bott.md на каскадных
примерах (своих, не из §9 записки).

Для каждого примера f(s,tau) (многочлен) и выбранной ветви T(t) (s = t^{N1}):
 1) символьно: d_tau f(t^N1, T(t)) == 0 (если ветвь задана точно);
 2) численно (mpmath, 60 знаков): глобальный минимум f(s,.) на [-tau0, tau0] по всем
    вещественным корням d_tau f(s,.) и по концам -- совпадает ли с T(s^{1/N1}) (до ничьей);
 3) многоугольник Ньютона по шагам 5-6 леммы: nu_k, Gamma1, A'_*, K_*, Q_V;
 4) Q_V >= 0, младшая степень чётна, c_{k0} > 0;
 5) sup_{|b|<=B} | t^{-Gamma1} f(t^N1, tau_v + t^{A'} b) - (-a + Q_V(b)) | -> 0 при t -> 0,
    где tau_v -- численный глобальный минимум (а не формула);
 6) взвешенное неравенство Эйлера (1+alpha) b Q_V'(b) >= Q_V(b) при |b| <= r2.
"""
import sympy as sp
import mpmath as mp

mp.mp.dps = 60
s, tau, t, b = sp.symbols('s tau t b', real=True)


def global_min(fexpr, sval, tau0):
    """Глобальный минимум f(sval, .) на [-tau0, tau0]: перебор вещественных корней f_tau и концов."""
    fs = sp.Poly(sp.expand(fexpr.subs(s, sp.Rational(1)) * 0 + fexpr), tau, s)
    ftau = sp.diff(fexpr, tau)
    coeffs = sp.Poly(ftau, tau).all_coeffs()
    cnum = [mp.mpf(sp.N(cc.subs(s, sp.Float(str(sval), 70)), 70)) if cc.free_symbols else mp.mpf(sp.N(cc, 70))
            for cc in coeffs]
    roots = mp.polyroots(cnum, maxsteps=400, extraprec=400)
    F = sp.lambdify((s, tau), fexpr, 'mpmath')
    cands = [mp.mpf(-tau0), mp.mpf(tau0)]
    for r in roots:
        if abs(mp.im(r)) < mp.mpf(10)**(-40) and abs(mp.re(r)) < tau0:
            cands.append(mp.re(r))
    vals = sorted((F(sval, c), c) for c in cands)
    return vals[0][1], vals[0][0], vals


def newton(fexpr, N1, Texpr, kmax):
    """Шаги 5-6: nu_k, старшие коэффициенты a_k, Gamma1, a, A', K_*, Q_V."""
    ft = sp.expand(fexpr.subs(s, t**N1))
    taup = sp.symbols('taup')
    ftil = sp.expand(ft.subs(tau, Texpr + taup))
    v = sp.series(ftil.subs(taup, 0), t, 0, 40).removeO()
    v = sp.Poly(sp.expand(v), t)
    terms = sorted(v.terms(), key=lambda m: m[0][0])
    G1, lead = terms[0][0][0], terms[0][1]
    a1 = sp.simplify(sp.diff(ftil, taup).subs(taup, 0))
    nus, cs = {}, {}
    for kk in range(2, kmax + 1):
        ak = sp.expand(sp.diff(ftil, taup, kk).subs(taup, 0) / sp.factorial(kk))
        if ak == 0:
            continue
        pk = sp.Poly(sp.series(ak, t, 0, 40).removeO(), t)
        tk = sorted(pk.terms(), key=lambda m: m[0][0])[0]
        nus[kk], cs[kk] = tk[0][0], sp.nsimplify(tk[1])
    # E(A') = min(nu_k + k A') = G1
    cand = sorted({sp.Rational(G1 - nu, kk) for kk, nu in nus.items() if G1 - nu > 0})
    Astar = None
    for A in cand:
        if min(nu + kk*A for kk, nu in nus.items()) == G1:
            Astar = A
            break
    Ks = [kk for kk, nu in nus.items() if nu + kk*Astar == G1]
    QV = sum(cs[kk]*b**kk for kk in Ks)
    return dict(a1=a1, Gamma1=G1, a=-lead, nus=nus, cs=cs, Astar=Astar, Ks=Ks, QV=sp.expand(QV))


EXAMPLES = [
    # имя, f, N1, T(t) (точная ветвь), tau0, комментарий
    ('E1 ничья симметричная', tau**4 - s*tau**2 + s**3, 2, t/sp.sqrt(2), 0.5,
     'две глобальные ветви +-t/sqrt2 с равной глубиной; вторая в окне при b=-sqrt2'),
    ('E2 узкий невырожденный', (tau**3 - s)**2 - s**3, 3, t, 0.5,
     'дно tau=s^{1/3}, ширина s^{5/6}'),
    ('E3 двойная яма внутри', tau**2*(tau - s**3)**2 - s**4, 1, sp.Integer(0), 0.5,
     'ничья tau=0 и tau=s^3 на расстоянии << ширины s; Q_V вырожден'),
    ('E4 глубина от свободного члена', tau**4 + s*tau**3 - s**3, 1, -sp.Rational(3, 4)*t, 0.5,
     'ещё крит. точка tau=0 со значением -s^3; Q_V=b^4'),
    ('E5 комплексные ветви', tau**4 - 4*s*tau, 3, t, 0.5,
     'f_tau = 4(tau^3 - s): одна вещественная ветвь'),
]


def run_example(name, f, N1, T, tau0, comment, branch_numeric=False):
    print('=' * 78)
    print(name, '|', comment)
    print('f =', f)
    ft = sp.expand(f.subs(s, t**N1))
    chk = sp.simplify(sp.diff(f, tau).subs(s, t**N1).subs(tau, T))
    print('  d_tau f(t^N1, T(t)) =', chk)
    nd = newton(f, N1, T, sp.Poly(f, tau).degree())
    print('  Gamma1 =', nd['Gamma1'], ' a =', nd['a'], ' nu_k =', nd['nus'], " A'* =", nd['Astar'],
          ' K* =', nd['Ks'])
    QV = nd['QV']
    print('  Q_V(b) =', QV, ' =', sp.factor(QV))
    alpha = nd['Astar'] / N1
    gamma = sp.Rational(nd['Gamma1'], N1)
    print('  alpha =', alpha, ' gamma =', gamma)
    # Q_V >= 0: минимум на R численно и аналитически через вещественные корни Q_V'
    QVf = sp.lambdify(b, QV, 'mpmath')
    minQ = min(QVf(mp.mpf(i)/1000) for i in range(-10000, 10001))  # сетка на [-10,10]
    k0 = min(nd['Ks'])
    print('  min Q_V на R =', minQ, ' k0 =', k0, ' c_k0 =', nd['cs'][k0])
    # глобальный минимум численно и сравнение с ветвью
    Tn = sp.lambdify(t, T, 'mpmath')
    QVn = sp.lambdify(b, QV, 'mpmath')
    F = sp.lambdify((s, tau), f, 'mpmath')
    a = mp.mpf(sp.N(nd['a'], 60))
    print('  t         |tau_v - T(t)|      f(s,tau_v)/(-a t^G1)   sup_{|b|<=1.2}|prof - (-a+Q_V)|')
    for e in [2, 3, 4, 6, 8]:
        tv = mp.mpf(10)**(-e)
        sv = tv**N1
        tmin, fmin, vals = global_min(f, sv, tau0)
        dev = abs(tmin - Tn(tv))
        # если ничья -- берём ближайший к T глобальный минимум
        ties = [c for (vv, c) in vals if abs(vv - fmin) <= abs(fmin)*mp.mpf(10)**(-45)]
        tsel = min(ties, key=lambda c: abs(c - Tn(tv)))
        sup = 0
        for i in range(-24, 25):
            bb = mp.mpf(i)/20
            prof = F(sv, tsel + tv**mp.mpf(nd['Astar'])*bb) / tv**nd['Gamma1']
            sup = max(sup, abs(prof - (-a + QVn(bb))))
        print(f'  1e-{e:<2d}  {mp.nstr(abs(tsel - Tn(tv)), 5):>14}   {mp.nstr(fmin/(-a*tv**nd["Gamma1"]), 12):>18}'
              f'   {mp.nstr(sup, 5):>12}   (ничьих: {len(ties)})')
    # Эйлер: (1+alpha) b Q_V' >= Q_V при малых |b|
    c1 = 1 + alpha
    eul = sp.expand(c1*b*sp.diff(QV, b) - QV)
    worst = min(float(eul.subs(b, sp.Rational(i, 1000))) for i in range(-300, 301))
    print('  min_{|b|<=0.3} [(1+alpha) b Q_V\' - Q_V] =', worst)
    return nd


if __name__ == '__main__':
    for ex in EXAMPLES:
        run_example(*ex)


def e6():
    """E6: почти-ничья с неравными глубинами, ветвь не в радикалах-виде; T -- ряд (до t^14)."""
    f = tau**4 - 2*s*tau**2 + s**2*tau
    sig = sp.symbols('sig')
    # tau = t*sig(t), 4 sig^3 - 4 sig + t = 0, sig(0) = -1 (простой корень)
    ser = sp.Integer(-1)
    for _ in range(6):   # итерации Ньютона в кольце рядов
        g = 4*ser**3 - 4*ser + t
        ser = sp.series(ser - g/(12*ser**2 - 4), t, 0, 15).removeO()
    T = sp.expand(t*ser)
    print('E6: T(t) =', sp.series(T, t, 0, 6))
    run_example('E6 почти-ничья, неравные глубины', f, 2, T, 0.5,
                'ветви ~ -t и ~ +t; глобальная -- отрицательная; вторая в окне при b ~ 2')


if __name__ == '__main__':
    e6()
