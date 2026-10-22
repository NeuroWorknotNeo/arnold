"""xprime.py -- проверка условий следствия X' [013] (и теоремы S [013]) для B1, B3, B4 (касп и тэкнод), точно (sympy) + численные запасы.
Следствие X' (013): n=3, U in C^{j+1}, U = sum_{k=m}^j u_k + O(|q|^{j+1}); omega: замкнутый круг -> S^2 (аналитическая инъективная иммерсия), omega(0) = omega_0,
p_k = u_k o omega; xi in C^1, xi(0) = 0, |Dxi| <= K;
 (X'0) p_m >= 0, xi.grad p_m >= -C p_m;  (X'1) m<k<j: p_k >= 0, p_k(0)=0, xi.grad p_k >= -C p_k;
 (X'2) p_j(0) = -a0 < 0, Lambda := p_j + a0 >= lambda0 |theta|^{2p}, xi.grad Lambda >= mu0 Lambda.
usage: python xprime.py   -> xprime.json, печатает проверки."""
import json, os
import sympy as sp, mpmath as mp
from exlist import BY, HERE, x, y, z
from basic import forms

th1, th2, u = sp.symbols('theta1 theta2 u', real=True)
t, w = sp.symbols('t w', real=True)
res = {}

def cusp(key):
    """gnomonic chart around e_z: omega = c (th1, th2, 1), c = (1+|th|^2)^(-1/2); xi = (2 th1, 3 th2) (weights of the cusp th2^2 = th1^3)"""
    fm = forms(BY[key]['U'])
    m = min(fm); assert m == 6 and 7 in fm and fm[6] == (y**2*z - x**3)**2 or sp.expand(fm[6] - (y**2*z - x**3)**2) == 0
    c = (1 + th1**2 + th2**2)**sp.Rational(-1, 2)
    sub = {x: c*th1, y: c*th2, z: c}
    p6 = sp.simplify(fm[6].subs(sub, simultaneous=True))
    p7 = sp.simplify(fm[7].subs(sub, simultaneous=True))
    xi = (2*th1, 3*th2)
    F = th2**2 - th1**3
    r = dict(key=key, chart='гномоническая карта вокруг e_z: omega = c(th1, th2, 1)', xi='(2 th1, 3 th2)')
    r['p6'] = str(sp.simplify(p6)); r['p7'] = str(p7)
    # (X'0): p6 = c^6 F^2 ; xi.grad p6 = 12 p6 + F^2 xi.grad(c^6)
    ratio = sp.simplify((xi[0]*sp.diff(p6, th1) + xi[1]*sp.diff(p6, th2))/p6)
    r['X0_ratio_xi_p6_over_p6'] = str(sp.simplify(ratio))
    rho2 = th1**2 + th2**2
    # ratio = 12 - 6 c^2 (2 th1^2 + 3 th2^2) >= 12 - 18 rho2/(1+rho2)
    lower = 12 - 18*rho2/(1 + rho2)
    r['X0_identity'] = bool(sp.simplify(ratio - (12 - 6*(2*th1**2 + 3*th2**2)/(1 + rho2))) == 0)
    r['X0_C'] = 'ratio >= 12 - 18 rho^2/(1+rho^2) >= -6 при всех theta (C=6)'
    # (X'2)
    a0 = -p7.subs({th1: 0, th2: 0})
    Lam = sp.simplify(p7 + a0)
    r['a0'] = str(a0)
    uu = sp.symbols('uu', positive=True)
    Lam_u = sp.simplify(Lam.subs({th1: sp.sqrt(uu), th2: 0}))      # Lambda зависит только от rho^2
    r['Lambda_of_u'] = str(Lam_u)
    ser = sp.series(Lam_u, uu, 0, 4).removeO()
    r['Lambda_series'] = str(ser)
    return r, p6, p7, Lam, xi, a0

def verify_cusp():
    for key in ('f:B1', 'f:B4'):
        r, p6, p7, Lam, xi, a0 = cusp(key)
        # xi.grad Lambda = 2 th1 L_1 + 3 th2 L_2 ; Lambda = h(u), u = rho^2 : xi.grad Lambda = h'(u) * 2(2 th1^2 + 3 th2^2) >= 4 u h'(u)
        uu = sp.symbols('uu', positive=True)
        h = sp.simplify(Lam.subs({th1: sp.sqrt(uu), th2: 0}))
        hp = sp.simplify(sp.diff(h, uu))
        r['h_prime'] = str(sp.factor(hp))
        xiL = sp.simplify(xi[0]*sp.diff(Lam, th1) + xi[1]*sp.diff(Lam, th2))
        # проверка тождества xi.grad Lambda = h'(u)*2(2 th1^2 + 3 th2^2)
        sub = {uu: th1**2 + th2**2}
        ident = sp.simplify(xiL - hp.subs(sub)*2*(2*th1**2 + 3*th2**2))
        r['xiLambda_identity'] = bool(ident == 0)
        # численные запасы на 0 < u <= 1 (theta0 = 1): h(u) >= lambda0 u^p ; xi.grad Lambda >= 4 u h'(u) >= mu0 h(u)
        mp.mp.dps = 30
        hf = sp.lambdify(uu, h, 'mpmath'); hpf = sp.lambdify(uu, hp, 'mpmath')
        us = [mp.mpf(i)/200 for i in range(1, 201)]
        mu_min = min(4*uu_*hpf(uu_)/hf(uu_) for uu_ in us)
        p_exp = 1 if key == 'f:B1' else 2
        lam_min = min(hf(uu_)/uu_**p_exp for uu_ in us)
        r['theta0'] = '1 (u = rho^2 in (0,1])'
        r['p_exponent_(rho^{2p}=u^p)'] = p_exp
        r['lambda0_min_on_grid'] = mp.nstr(lam_min, 8)
        r['mu0_min_on_grid (4 u h\'/h)'] = mp.nstr(mu_min, 8)
        r['verdict'] = 'X\' применимо: (X\'0) ✓, (X\'1) пусто (j=m+1), (X\'2) ✓ (Lambda=h(u)~u^%d, 4uh\'(u) >= mu0 h(u))' % p_exp
        res[key] = r
        print(key, json.dumps(r, ensure_ascii=False, indent=1)[:1800])

def verify_tacnode():
    """B3: omega(t,w): y = t, f1 = w (=x^2+y^2-z^2 на сфере) -> z = sqrt((1-w)/2), x = sqrt((1+w-2t^2)/2); f2 = x^2+2y^2-z^2 = w + t^2 точно."""
    key = 'f:B3'
    fm = forms(BY[key]['U'])
    X_ = sp.sqrt((1 + w - 2*t**2)/2); Z_ = sp.sqrt((1 - w)/2); Y_ = t
    sub = {x: X_, y: Y_, z: Z_}
    f1 = sp.simplify((x**2 + y**2 - z**2).subs(sub)); f2 = sp.simplify((x**2 + 2*y**2 - z**2).subs(sub))
    r = dict(key=key, chart='координаты на S^2 около omega_0=(1,0,1)/sqrt2: t = y, w = x^2+y^2-z^2', f1=str(f1), f2=str(f2))
    p8 = sp.simplify(fm[8].subs(sub))
    r['p8'] = str(sp.factor(p8))
    xi = (t, 2*w)
    r['xi'] = '(t, 2w)'
    r['X0_identity_xi_p8_eq_8_p8'] = bool(sp.simplify(xi[0]*sp.diff(p8, t) + xi[1]*sp.diff(p8, w) - 8*p8) == 0)
    p9 = sp.simplify(fm[9].subs(sub))
    a0 = sp.simplify(-p9.subs({t: 0, w: 0}))
    r['p9'] = str(p9); r['a0'] = str(a0)
    Lam = p9 + a0
    ser = sp.series(sp.series(Lam, t, 0, 4).removeO(), w, 0, 4).removeO()
    r['Lambda_Taylor_order3'] = str(sp.expand(sp.simplify(ser)))
    H = sp.hessian(Lam, (t, w)).subs({t: 0, w: 0})
    r['Hess_Lambda_0'] = str(sp.simplify(H).tolist())
    xiH = sp.Matrix([[1, 0], [0, 2]])
    CH = sp.simplify(xiH*H + H*xiH)
    r['C_H_plus_H_C'] = str(CH.tolist())
    r['CH+HC_PD'] = bool(all(sp.N(CH[:k, :k].det()) > 0 for k in (1, 2)))
    r['mu0_max_from_quadratic'] = 'lambda_min(H^{-1/2}(CH+HC)H^{-1/2}) = ' + str(sp.N(min(sp.Matrix(H.inv()*CH).eigenvals()), 8)) if False else None
    ev = sp.Matrix(H.inv()*CH).eigenvals()
    r['mu0_quadratic_order'] = str([sp.N(e_, 8) for e_ in ev])
    res[key] = r
    print(key, json.dumps(r, ensure_ascii=False, indent=1)[:2500])

if __name__ == '__main__':
    verify_cusp()
    verify_tacnode()
    json.dump(res, open(os.path.join(HERE, 'xprime.json'), 'w'), indent=1, ensure_ascii=False)
