"""g1.py -- случай j = m+1: G = g_{m+1} = u_{m+1}|_Sigma (лемма K1 [008]); критические точки G на кривых-компонентах Sigma (рациональные параметризации),
G'' по натуральному параметру, G''+jG.  Для коник B3, B3b (Sigma = {f1 f2 = 0}) и D1-D4 (Sigma = C1 u C2), оба листа конуса.
[Эксперимент: точно (многочлен числителя G', вещественные корни sympy) + mpmath 40 цифр].  Особые точки Sigma (касания) помечены."""
import sys, os, json
import sympy as sp, mpmath as mp
from exlist import BY, HERE, x, y, z
from basic import forms
t, tau = sp.symbols('t tau', real=True)
mp.mp.dps = 40
CURVES = {
    'C1': ([1 - t**2, 2*t, 1 + t**2], x**2 + y**2 - z**2),
    'E_B': ([1 - 2*t**2, 2*t, 1 + 2*t**2], x**2 + 2*y**2 - z**2),
    'E_D': ([4*t, 1 - 2*t**2, 1 + 2*t**2], x**2 + 2*y**2 - 2*z**2),
    'CUSP': ([t**2, t**3, 1], x**3 - y**2*z),
}

def analyse(key, cname, sign):
    fm = forms(BY[key]['U']); m = min(fm); j = m + 1
    uj = fm[j]
    p0, f = CURVES[cname]
    p = [sp.expand(sign*c) for c in p0]
    N = sp.expand(uj.subs({x: p[0], y: p[1], z: p[2]}, simultaneous=True))
    lam2 = sp.expand(sum(c**2 for c in p))
    num = sp.numer(sp.together(sp.diff(N, t)*lam2 - sp.Rational(j, 2)*N*sp.diff(lam2, t)))
    roots = []
    for fct, mult in sp.factor_list(sp.expand(num))[1]:
        fp = sp.Poly(fct, t)
        if fp.degree() > 0:
            for r in sp.real_roots(fp):
                roots.append((mp.mpf(str(sp.N(r, 40))), mult))
    Gexpr = N/lam2**sp.Rational(j, 2)
    Gf = sp.lambdify(t, Gexpr, 'mpmath'); Gtt = sp.lambdify(t, sp.diff(Gexpr, t, 2), 'mpmath')
    pt = [sp.diff(c, t) for c in p]
    sp2 = sp.cancel((sum(c**2 for c in pt)*lam2 - sum(a*b for a, b in zip(p, pt))**2)/lam2**2)
    sp2f = sp.lambdify(t, sp2, 'mpmath')
    # H = D^2 u_m(n,n): через f: u_m = f_i^2 * g ... здесь просто отметим особые точки по равенству нулю другого множителя
    crit = []
    for r, mult in roots:
        rv = r
        G0 = Gf(rv)
        sp2v = sp2f(rv)
        if sp2v == 0:
            crit.append(dict(t=mp.nstr(rv, 14), G=mp.nstr(G0, 14), kind='особая точка параметризации'))
            continue
        d2 = Gtt(rv)/sp2v
        omega = [mp.nstr(sp.lambdify(t, c/sp.sqrt(lam2), 'mpmath')(rv), 10) for c in p]
        crit.append(dict(t=mp.nstr(rv, 14), omega=omega, G=mp.nstr(G0, 14), d2G=mp.nstr(d2, 10), G2_plus_jG=mp.nstr(d2 + j*G0, 10), mult=int(mult),
                         kind=('min' if d2 > 0 else 'max') if mult == 1 else 'degenerate'))
    # t = infinity
    pi_ = [c.subs(t, 1/tau) for c in p]
    den = sp.lcm([sp.denom(sp.together(c)) for c in pi_])
    pi_ = [sp.expand(sp.cancel(c*den)) for c in pi_]
    N2 = sp.expand(uj.subs({x: pi_[0], y: pi_[1], z: pi_[2]}, simultaneous=True))
    lam22 = sp.expand(sum(c**2 for c in pi_))
    G2 = N2/lam22**sp.Rational(j, 2)
    g_inf = sp.N(G2.subs(tau, 0), 20); g1 = sp.N(sp.diff(G2, tau).subs(tau, 0), 20)
    pt2 = [sp.diff(c, tau) for c in pi_]
    sp22 = sp.cancel((sum(c**2 for c in pt2)*lam22 - sum(a*b for a, b in zip(pi_, pt2))**2)/lam22**2).subs(tau, 0)
    d2inf = sp.N(sp.diff(G2, tau, 2).subs(tau, 0)/sp22, 12) if sp22 != 0 else None
    crit.append(dict(t='inf', omega_dir=[str(sp.N(c.subs(tau, 0)/sp.sqrt(lam22.subs(tau, 0)), 8)) for c in pi_], G=str(g_inf), G_prime_tau=str(g1), d2G=str(d2inf),
                     G2_plus_jG=str(sp.N(d2inf + j*g_inf, 10)) if d2inf is not None else None,
                     kind=('min' if (abs(g1) < 1e-12 and d2inf and d2inf > 0) else ('max' if abs(g1) < 1e-12 else 'not critical'))))
    return dict(key=key, comp=cname, sign=sign, m=int(m), j=int(j), G_N=str(N)[:300], crit=crit)

SPEC = {
    'f:B1': ['CUSP'], 'f:B2': ['CUSP'], 'f:B4': ['CUSP'],
    'f:B3': ['C1', 'E_B'], 'f:B3b': ['C1', 'E_B'],
    'f:D1': ['C1', 'E_D'], 'f:D2': ['C1', 'E_D'], 'f:D3': ['C1', 'E_D'], 'f:D4': ['C1', 'E_D'],
}
if __name__ == '__main__':
    res = {}
    keys = sys.argv[1:] or [k for k in SPEC if k not in ('f:B1', 'f:B2', 'f:B4')]
    for k in keys:
        for cn in SPEC[k]:
            for sg in (1, -1):
                r = analyse(k, cn, sg)
                res[f'{k}|{cn}|{sg}'] = r
                print('==', k, cn, sg, 'j=', r['j'])
                for c in r['crit']:
                    print('     ', {kk: vv for kk, vv in c.items() if kk != 'omega'}, c.get('omega', c.get('omega_dir')))
    fn = os.path.join(HERE, 'g1.json')
    old = json.load(open(fn)) if os.path.exists(fn) else {}
    old.update(res)
    json.dump(old, open(fn, 'w'), indent=1, default=str, ensure_ascii=False)
