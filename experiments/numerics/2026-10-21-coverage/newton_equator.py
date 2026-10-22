"""newton_equator.py -- M1, M2 (zoo): постоянная нормальная кратность 2r = 4 вдоль экватора, первое ребро многоугольника Ньютона [011], условия (R) / (UR) [014],
следствие N' [011].  Точно (sympy); числа G, G'' -- mpmath.   [Эксперимент: точный символьный]"""
import json, os
import sympy as sp, mpmath as mp
from exlist import BY, HERE, x, y, z
from basic import forms
ph, s, yy, eps, tt = sp.symbols('phi s y epsilon tt', real=True)
sig = sp.Symbol('sigma', positive=True)
mp.mp.dps = 40

def support(key):
    fm = forms(BY[key]['U']); m = min(fm)
    phi_expr = 0
    for k, uk in fm.items():
        phi_expr += s**(k - m)*uk.subs({x: sp.cos(ph), y: sp.sin(ph), z: yy}, simultaneous=True)
    phi_expr = sp.expand(phi_expr)
    P = sp.Poly(phi_expr, s, yy)
    supp = {}
    for (i, l), co in P.terms():
        co = sp.simplify(co)
        if co != 0:
            supp[(i, l)] = co
    return m, supp

def first_edge(supp, two_r):
    from fractions import Fraction
    c = [Fraction(i, two_r - l) for (i, l) in supp if l < two_r]
    return min(c) if c else None

def M1():
    key = 'z:M1'
    m, supp = support(key)
    out = dict(key=key, m=int(m), support=sorted(supp.keys()))
    g = first_edge(supp, 4)
    out['gamma_star'] = str(g); N = g.denominator
    j = m + 4*sp.Rational(g.numerator, g.denominator)
    out['N'] = N; out['j'] = str(j); out['c'] = str(1 + sp.Rational(g.numerator, g.denominator))
    # edge polynomial Phi0: points (i,l) with i + gamma l = 4 gamma
    gam = sp.Rational(g.numerator, g.denominator)
    Phi0 = sum(co*eps**l for (i, l), co in supp.items() if sp.Rational(i) + gam*l == 4*gam)
    out['Phi0'] = str(sp.simplify(Phi0))
    # точная форма U-tilde(sigma, phi, eps) = U(s w + s^c eps n)/s^j, s = sigma^N, c = 5/4
    Uf = BY[key]['U']
    sN = sig**N
    X_ = sN*sp.cos(ph); Y_ = sN*sp.sin(ph); Z_ = sN**(1 + gam)*eps
    Ut = sp.simplify(sp.expand(Uf.subs({x: X_, y: Y_, z: Z_}, simultaneous=True)/sN**j))
    claim = (eps - sig**3*sp.cos(ph)**2)**4 + sp.cos(ph)**5 + sp.sin(ph)**5 + sig**8*(sp.cos(ph)*sp.sin(ph)**6 + sp.sin(ph)*sp.cos(ph)**6)
    out['Utilde_identity_(eps-sigma^3 cos^2)^4+G+sigma^8(...)'] = bool(sp.simplify(sp.expand(Ut - claim)) == 0)
    G = sp.cos(ph)**5 + sp.sin(ph)**5
    out['G'] = 'cos^5+sin^5'
    # критические точки G: phi = pi: G=-1, G''=5 ; phi = 3pi/2
    for name, pv in (('pi', sp.pi), ('3pi/2', 3*sp.pi/2)):
        out['G_at_' + name] = [str(sp.simplify(G.subs(ph, pv))), str(sp.simplify(sp.diff(G, ph).subs(ph, pv))), str(sp.simplify(sp.diff(G, ph, 2).subs(ph, pv)))]
    out['N_prime'] = 'ветвь eps_0 = 0: Phi0 = eps^4 + G, d^k Phi0 = 0 (k=1,2,3), d^4 Phi0 = 24 > 0 => постоянная кратность 2r\'-1 = 3, r\' = 2 (E); G(pi) = -1 < 0, G\'(pi) = 0 < G\'\'(pi) = 5'
    out['UR'] = 'ветвь eps*_k(sigma,theta) = sigma^3 cos^2(theta) аналитична; U-tilde(sigma,theta,eps*+e) = G-hat(sigma,theta) + e^4 * 1, M = 1 > 0; глобальный минимум U-tilde(sigma,theta,.) на [-E,E] единствен = eps* => (UR1),(UR2) на всей окружности'
    out['R_fails'] = 'd^2 Phi0 (eps=0) = 0 при каждом theta: условие (R) нарушено (минимум вырожден) => M\'_R неприменимо, применимо M\' через (UR)'
    return out

def M2():
    key = 'z:M2'
    m, supp = support(key)
    out = dict(key=key, m=int(m), support=sorted(supp.keys()))
    g = first_edge(supp, 4)
    out['gamma_star'] = str(g); N = g.denominator
    gam = sp.Rational(g.numerator, g.denominator)
    j = m + 4*gam
    out['N'] = N; out['j'] = str(j); out['c'] = str(1 + gam)
    Phi0 = sum(co*eps**l for (i, l), co in supp.items() if sp.Rational(i) + gam*l == 4*gam)
    out['Phi0'] = str(sp.simplify(Phi0))
    f = sp.cos(ph)**4 + sp.cos(ph)**3*sp.sin(ph) + sp.sin(ph)**4
    out['Phi0_equals_eps4_plus_f_eps'] = bool(sp.simplify(Phi0 - (eps**4 + f*eps)) == 0)
    # f > 0: f = cos^4 (1 + t + t^4), t = tan phi;  1 + t + t^4 > 0 при всех t (минимум в t0 = -(1/4)^(1/3))
    t0 = -sp.Rational(1, 4)**sp.Rational(1, 3)
    fmin_num = sp.N(1 + t0 + t0**4, 30)
    out['min_(1+t+t^4)'] = str(fmin_num)
    # (R): d^2 Phi0 в точке глобального минимума eps_0 = -(f/4)^(1/3): 12 eps_0^2 > 0 (f>0)
    out['R'] = 'eps_0 = -(f/4)^{1/3} != 0 (f > 0), d^2 Phi0 = 12 eps_0^2 > 0  => условие (R) выполнено при каждом phi (глобальный минимум eps^4 + f eps единствен и невырожден)'
    # G(phi) = -3 * 4^(-4/3) f^(4/3) ; критические точки f
    tsym = sp.symbols('tsym', real=True)
    fnum = (1 + tsym + tsym**4)/(1 + tsym**2)**2
    dnum = sp.numer(sp.together(sp.diff(fnum, tsym)))
    roots = sp.real_roots(sp.Poly(sp.expand(dnum), tsym))
    Gphi = lambda p_: -3*mp.mpf(4)**(-mp.mpf(4)/3)*(mp.cos(p_)**4 + mp.cos(p_)**3*mp.sin(p_) + mp.sin(p_)**4)**(mp.mpf(4)/3)
    cr = []
    for rt in roots:
        rv = mp.mpf(str(sp.N(rt, 40)))
        p_ = mp.atan(rv)
        G0 = Gphi(p_)
        G2 = mp.diff(Gphi, p_, 2)
        G1 = mp.diff(Gphi, p_, 1)
        cr.append(dict(t=mp.nstr(rv, 12), phi=mp.nstr(p_, 12), G=mp.nstr(G0, 12), G1=mp.nstr(G1, 6), G2=mp.nstr(G2, 12), kind='min' if G2 > 0 else 'max'))
    out['critical_points_of_G_(chart tan phi)'] = cr
    out['f_at_phi=pi/2'] = '1 (t=inf): G(pi/2) = -3*4^(-4/3)'
    G90 = Gphi(mp.pi/2)
    out['phi=pi/2'] = dict(G=mp.nstr(G90, 12), G2=mp.nstr(mp.diff(Gphi, mp.pi/2, 2), 12))
    return out

if __name__ == '__main__':
    res = {}
    for fn_ in (M1, M2):
        r = fn_()
        res[r['key']] = r
        print(json.dumps(r, indent=1, ensure_ascii=False, default=str)[:3500])
    json.dump(res, open(os.path.join(HERE, 'newton_equator.json'), 'w'), indent=1, ensure_ascii=False, default=str)
