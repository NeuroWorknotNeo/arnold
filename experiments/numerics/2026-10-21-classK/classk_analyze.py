"""analyze.py -- exact (sympy) analysis of the curve/point components of Sigma for the zoo examples.
Usage: python analyze.py ID [ID...]   (writes out/ID.json and prints a log)
[Experiment] symbolic, exact where stated; the numbers (critical points of G) are real algebraic numbers
evaluated to 40 digits (mpmath) from exact polynomial root isolation (sympy real_roots)."""
import sys, json, os, itertools, time
import sympy as sp
import mpmath as mp
from kfib import fibre, homog_parts
import comps
from comps import x, y, z, t, U, COMPS, CORE

mp.mp.dps = 50
HERE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
KMAX = 4          # g_{m+1..m+4}


def lowest(Uexpr):
    pr = homog_parts(Uexpr)
    m = min(pr)
    return m, pr[m], pr


def sos_check(ex, um):
    core = CORE[ex]
    tot = sum(c*comps.sp.sympify(str(pp), locals={'x': x, 'y': y, 'z': z})**2 for c, pp in core['sos'])
    return sp.expand(tot - um) == 0


def real_roots_exact(poly_expr, var):
    """real roots of a rational-function numerator: list of (mp value, multiplicity)"""
    P = sp.Poly(sp.numer(sp.together(poly_expr)), var)
    if P.is_zero:
        return None
    out = []
    for fac, mult in sp.sqf_list(P)[1]:
        if fac.degree() <= 0:
            continue
        for r in sp.real_roots(fac):
            out.append((mp.mpf(str(sp.N(r, 60))), mult))
    return out


def analyse_curve(ex, comp, m, um):
    _, name, p, nu, f = comp
    t_ = t
    res = dict(name=name)
    K = KMAX
    t0 = time.time()
    out = fibre(U[ex], m, p, [nu], K)
    H = sp.cancel(out['H'][0, 0])
    res['H'] = str(sp.factor(H))
    # Morse-Bott: H>0 for all real t (H is D^2 u_m(p)(nu,nu))
    Hn = sp.Poly(sp.numer(sp.together(H)), t_)
    Hd = sp.Poly(sp.denom(sp.together(H)), t_)
    rr = [r for r in sp.real_roots(Hn)] if Hn.degree() > 0 else []
    rrd = [r for r in sp.real_roots(Hd)] if Hd.degree() > 0 else []
    res['H_real_roots'] = [str(sp.N(r, 15)) for r in rr]
    res['H_pos_at_0'] = bool((H.subs(t_, 0) if True else 0) > 0) if H.subs(t_, 0) != sp.zoo else None
    res['MB_on_component'] = (len(rr) == 0 and bool(H.subs(t_, sp.Rational(1, 3)) > 0))
    lam2 = sp.factor(sum(c**2 for c in p))
    lam = sp.sqrt(lam2)
    lam = sp.simplify(lam)
    res['lam'] = str(lam)
    g = {k: sp.cancel(v) for k, v in out['g'].items()}
    gs = {k: sp.factor(v/lam**k) for k, v in g.items()}           # unit-sphere normalisation
    res['g_unit'] = {k: str(v) for k, v in gs.items()}
    nz = [k for k in sorted(gs) if sp.simplify(gs[k]) != 0]
    if not nz:
        res['j'] = None
        res['note'] = 'g_{m+1..m+%d} all zero' % K
        return res
    j = nz[0]
    res['j'] = j
    G = sp.simplify(gs[j])
    res['G'] = str(sp.factor(G))
    # natural parameter speed^2 = |omega_t|^2 = (|p_t|^2 |p|^2 - (p.p_t)^2)/|p|^4
    pt = [sp.diff(c, t_) for c in p]
    sp2 = sp.cancel((sum(c**2 for c in pt)*lam2 - sum(a*b for a, b in zip(p, pt))**2)/lam2**2)
    Gt = sp.cancel(sp.diff(G, t_))
    res['G_const'] = (Gt == 0)
    if Gt == 0:
        res['G_value'] = str(G)
        return res
    crit = []
    # chart 1: all finite t
    roots1 = real_roots_exact(Gt, t_)
    # chart 2: tau = 1/t, only tau=0 (t=inf)
    tau = sp.symbols('tau', real=True)
    G2 = sp.cancel(sp.together(G.subs(t_, 1/tau)))
    G2t = sp.cancel(sp.diff(G2, tau))
    n2 = sp.numer(sp.together(G2t))
    inf_mult = 0
    P2 = sp.Poly(n2, tau)
    while not P2.is_zero and P2.eval(0) == 0:
        P2 = sp.Poly(sp.cancel(P2.as_expr()/tau), tau)
        inf_mult += 1
    G2tt = sp.cancel(sp.diff(G2, tau, 2))
    Gn = sp.lambdify(t_, G, 'mpmath')
    Gtt = sp.lambdify(t_, sp.diff(G, t_, 2), 'mpmath')
    Gttt = sp.lambdify(t_, sp.diff(G, t_, 3), 'mpmath')
    sp2f = sp.lambdify(t_, sp2, 'mpmath')
    pf = [sp.lambdify(t_, c, 'mpmath') for c in p]
    lamf = sp.lambdify(t_, lam, 'mpmath')
    def omega_at(tv):
        v = [c(tv) for c in pf]
        l = lamf(tv)
        return [c/l for c in v]
    for (r, mult) in roots1:
        G0 = Gn(r)
        sp2v = sp2f(r)
        d2 = Gtt(r)/sp2v
        # higher derivative for degenerate extremum: order of vanishing mult+1 of G-G0
        if mult == 1:
            kind = 'min' if d2 > 0 else 'max'
        elif mult % 2 == 0:
            kind = 'inflection (G\'..G^(%d)=0)' % mult
        else:
            # odd multiplicity >=3 : degenerate extremum, sign by the first nonvanishing derivative G^(mult+1)
            Gh = sp.lambdify(t_, sp.diff(G, t_, mult + 1), 'mpmath')(r)
            kind = 'DEGENERATE min (order %d)' % (mult + 1) if Gh > 0 else 'DEGENERATE max (order %d)' % (mult + 1)
        crit.append(dict(t=mp.nstr(r, 30), omega=[mp.nstr(c, 15) for c in omega_at(r)], G=mp.nstr(G0, 25),
                         d2G=mp.nstr(d2, 25) if mult == 1 else '0 (mult %d)' % mult,
                         G2_plus_jG=mp.nstr(d2 + j*G0, 25) if mult == 1 else None, mult=mult,
                         kind=kind, chart='t'))
    if inf_mult:
        # at t=inf  (tau=0): direction p/|p| limit; speed in tau-chart
        lim = [sp.limit(c/lam, t_, sp.oo) for c in p]
        # G2 at tau=0
        G0 = sp.limit(G, t_, sp.oo)
        # second derivative in the unit-speed parameter at tau=0
        pt2 = [sp.diff(c.subs(t_, 1/tau), tau) for c in p]
        pp = [c.subs(t_, 1/tau) for c in p]
        l2 = sp.factor(sum(c**2 for c in pp))
        sp2inf = sp.cancel((sum(c**2 for c in pt2)*l2 - sum(a*b for a, b in zip(pp, pt2))**2)/l2**2)
        s2 = sp.limit(sp2inf, tau, 0)
        d2 = sp.limit(G2tt, tau, 0)/s2 if inf_mult == 1 else 0
        d2 = sp.simplify(d2)
        if inf_mult == 1:
            inf_kind = 'min' if d2 > 0 else 'max'
        elif inf_mult % 2 == 0:
            inf_kind = 'inflection (G\'..G^(%d)=0)' % inf_mult
        else:
            Gh = sp.limit(sp.diff(G2, tau, inf_mult + 1), tau, 0)
            inf_kind = 'DEGENERATE min (order %d)' % (inf_mult + 1) if Gh > 0 else 'DEGENERATE max (order %d)' % (inf_mult + 1)
        crit.append(dict(t='inf', omega=[str(sp.N(c, 15)) for c in lim], G=str(sp.N(G0, 25)),
                         d2G=str(sp.N(d2, 25)) if inf_mult == 1 else '0 (mult %d)' % (inf_mult),
                         G2_plus_jG=str(sp.N(d2 + j*G0, 25)) if inf_mult == 1 else None, mult=inf_mult,
                         kind=inf_kind, chart='tau'))
    res['crit'] = crit
    res['Gmin'] = min(float(c['G']) for c in crit)
    res['time'] = time.time() - t0
    return res


def analyse_point(ex, comp, m, um):
    _, name, p = comp
    res = dict(name=name)
    p = [sp.Integer(c) for c in p]
    # basis of p^perp (rational)
    M = sp.Matrix([p])
    ns = M.nullspace()
    nus = [list(v) for v in ns]
    out = fibre(U[ex], m, p, nus, KMAX)
    H = out['H']
    res['H'] = str(H.tolist())
    # positive definiteness of H on N (exact: leading minors)
    minors = [H[:k, :k].det() for k in range(1, H.shape[0]+1)]
    res['H_minors'] = [str(c) for c in minors]
    res['MB'] = all(c > 0 for c in minors)
    lam = sp.sqrt(sum(c**2 for c in p))
    gs = {k: sp.nsimplify(sp.cancel(v)/lam**k) for k, v in out['g'].items()}
    res['g_unit'] = {k: str(sp.simplify(v)) for k, v in gs.items()}
    nz = [k for k in sorted(gs) if sp.simplify(gs[k]) != 0]
    res['j'] = nz[0] if nz else None
    if nz:
        v = sp.simplify(gs[nz[0]])
        res['g_j'] = str(v)
        res['g_j_float'] = float(v)
        res['g_j_sign'] = int(sp.sign(v))
    return res


def analyse(ex):
    m, um, parts = lowest(U[ex])
    res = dict(id=ex, m=m, parts_degrees=sorted(parts))
    res['u_m'] = str(sp.factor(um))
    res['sos_certificate_ok'] = sos_check(ex, um)
    comps_out = []
    for comp in COMPS[ex]:
        if comp[0] == 'curve':
            comps_out.append(analyse_curve(ex, comp, m, um))
        elif comp[0] == 'point':
            comps_out.append(analyse_point(ex, comp, m, um))
        else:
            comps_out.append(dict(name=comp[1], kind=comp[0]))
    res['components'] = comps_out
    return res


if __name__ == '__main__':
    for ex in sys.argv[1:]:
        t0 = time.time()
        r = analyse(ex)
        json.dump(r, open(os.path.join(HERE, 'out', ex + '.json'), 'w'), indent=1, default=str)
        print('===', ex, 'm=', r['m'], 'time %.1fs' % (time.time()-t0))
        for c in r['components']:
            print(json.dumps(c, indent=1, default=str)[:3000])
