"""cusp_G.py -- B1, B2, B4 (m = 6, u_6 = (y^2 z - x^3)^2, j = m+1 = 7): эффективный потенциал G = g_7 = u_7|_Sigma (лемма K1 [008]: g_{m+1} = u_{m+1}|_Sigma),
его критические точки на гладких дугах кубического конуса y^2 z = x^3 (параметр t: p = +-(t^2, t^3, 1); t = inf: p = +-(tau, 1, tau^3)).
Точно: числитель G' (многочлен), вещественные корни (sympy).  [Эксперимент: точный + mpmath]"""
import sys, json, os
import sympy as sp, mpmath as mp
from exlist import BY, HERE, x, y, z
from basic import forms
t, tau = sp.symbols('t tau', real=True)
mp.mp.dps = 40

def analyse(key):
    U = BY[key]['U']
    fm = forms(U)
    u7 = fm[7]
    out = dict(key=key, u7=str(u7), branches=[])
    for sgn in (1, -1):
        p = [sgn*t**2, sgn*t**3, sgn]
        N = sp.expand(u7.subs({x: p[0], y: p[1], z: p[2]}, simultaneous=True))
        Dn = 1 + t**4 + t**6
        # G = N / Dn^(7/2);  G' ~ (N' Dn - 7/2 N Dn')/Dn^(9/2)
        num = sp.expand(sp.diff(N, t)*Dn - sp.Rational(7, 2)*N*sp.diff(Dn, t))
        crit = []
        P = sp.Poly(num, t)
        fac = sp.factor_list(P.as_expr())[1]
        roots = []
        for f_, mult in fac:
            fp = sp.Poly(f_, t)
            if fp.degree() > 0:
                for r in sp.real_roots(fp):
                    roots.append((sp.N(r, 40), mult))
        Gf = sp.lambdify(t, N/Dn**sp.Rational(7, 2), 'mpmath')
        def G_of(tv):
            return Gf(mp.mpf(str(tv)))
        # second derivative wrt arclength: |omega_t|^2 = (|p_t|^2|p|^2 - (p.p_t)^2)/|p|^4
        pt = [sp.diff(c, t) for c in p]
        pp = sum(c**2 for c in p)
        sp2 = sp.cancel((sum(c**2 for c in pt)*pp - sum(a*b for a, b in zip(p, pt))**2)/pp**2)
        Gexpr = N/Dn**sp.Rational(7, 2)
        Gtt = sp.lambdify(t, sp.diff(Gexpr, t, 2), 'mpmath')
        sp2f = sp.lambdify(t, sp2, 'mpmath')
        for r, mult in roots:
            rv = mp.mpf(str(r))
            G0 = G_of(r)
            if sp2f(rv) == 0:
                crit.append(dict(t=mp.nstr(rv, 15), G=mp.nstr(G0, 15), kind='ОСОБАЯ ТОЧКА Sigma (острие каспа): дуговой параметр не определён', mult=int(mult)))
                continue
            d2 = Gtt(rv)/sp2f(rv)
            crit.append(dict(t=mp.nstr(rv, 15), G=mp.nstr(G0, 15), d2G=mp.nstr(d2, 12), G2_plus_7G=mp.nstr(d2 + 7*G0, 12), mult=int(mult),
                             kind='min' if (mult == 1 and d2 > 0) else ('max' if mult == 1 else 'degenerate/inflection')))
        # t = infinity: chart tau, p = sgn*(tau, 1, tau^3)
        pi_ = [sgn*tau, sgn, sgn*tau**3]
        N2 = sp.expand(u7.subs({x: pi_[0], y: pi_[1], z: pi_[2]}, simultaneous=True))
        D2 = 1 + tau**2 + tau**6
        G2 = N2/D2**sp.Rational(7, 2)
        G2t = sp.diff(G2, tau)
        g0 = sp.N(G2.subs(tau, 0), 20); g1 = sp.N(G2t.subs(tau, 0), 20); g2 = sp.N(sp.diff(G2, tau, 2).subs(tau, 0), 20)
        ptau = [sp.diff(c, tau) for c in pi_]; ppt = sum(c**2 for c in pi_)
        sp2tau = sp.cancel((sum(c**2 for c in ptau)*ppt - sum(a*b for a, b in zip(pi_, ptau))**2)/ppt**2).subs(tau, 0)
        crit.append(dict(t='inf (tau=0)', G=str(g0), G_prime_tau=str(g1), d2G=str(sp.N(g2/sp2tau, 12)), G2_plus_7G=str(sp.N(g2/sp2tau + 7*g0, 12))))
        out['branches'].append(dict(sign=sgn, G_poly_N=str(N), crit=crit))
    return out

if __name__ == '__main__':
    res = {}
    for k in ('f:B1', 'f:B2', 'f:B4'):
        r = analyse(k); res[k] = r
        print('==', k, 'u7 =', r['u7'])
        for b in r['branches']:
            print('  branch sign', b['sign'], 'N(t) =', b['G_poly_N'][:100])
            for c in b['crit']:
                print('     ', c)
    json.dump(res, open(os.path.join(HERE, 'cusp_G.json'), 'w'), indent=1, ensure_ascii=False)
