"""
criteria.py -- which known instability criteria apply to a given polynomial U(x,y,z)?

Each criterion returns a dict {status: 'yes'|'no'|'maybe', why: str}.  'yes' / 'no' are exact statements about the
HYPOTHESES as we read them from problem/KNOWN_RESULTS.md and results/002, results/003; 'maybe' means our exact
tools were inconclusive (never used to claim coverage).  Hypotheses of the published theorems are quoted in the
docstrings; sources that were not opened (marked "не сверено" in KNOWN_RESULTS.md) stay unverified here too.
"""
import itertools
import sympy as sp
import zoolib as zl
import sing
from zoolib import x, y, z, X, R2, Q0, P, parts, grad, hess

Y, N, M = 'yes', 'no', 'maybe'


def r(status, why):
    return dict(status=status, why=why)


# ===================================================================== hard core (u_m >= 0 with zeros)
def comp_ideal_gens(c):
    """ideal (in Q[x,y,z]) of a declared component of the zero cone"""
    if c['kind'] == 'curve':
        return [P(c['f'])]
    w = c['pt']
    return [P(w[i] * X[j] - w[j] * X[i]) for i, j in ((0, 1), (0, 2), (1, 2))]


def declared_sigma(core):
    comps = []
    for c in core['sigma']:
        if c['kind'] == 'curve':
            comps.append(dict(kind='curve', f=P(c['f'])))
        else:
            for pt in c['pts']:
                comps.append(dict(kind='point', pt=tuple(sp.Rational(v) for v in pt)))
    return comps


def hard_core_data(U, core):
    """Exact analysis of u_m: SOS certificate, completeness of the declared zero set Sigma, B1, B2, B3."""
    pr = parts(U)
    m = min(pr); um = pr[m]
    out = dict(m=m, um=str(um))
    # --- u_m >= 0 : explicit SOS
    sos = [(sp.Rational(c), P(p)) for c, p in core['sos']]
    out['sos_ok'] = sp.expand(um - sum(c * p**2 for c, p in sos)) == 0 and all(c > 0 for c, _ in sos)
    # --- completeness of Sigma: radical(<p_j>) == intersection of declared component ideals
    comps = declared_sigma(core)
    out['ncomp'] = len(comps)
    pj = [p for _, p in sos]
    gens_p = ','.join(sing.to_sing(p) for p in pj)
    ideals = ['ideal(' + ','.join(sing.to_sing(g) for g in comp_ideal_gens(c)) + ')' for c in comps]
    script = sing.HEAD + 'ring r=0,(x,y,z),dp;\nideal P0=' + gens_p + ';\nideal RP=radical(P0);\nideal I=' + ideals[0] + ';\n'
    for k, idl in enumerate(ideals[1:]):
        script += f'ideal I{k}=' + idl[len('ideal('):-1] + f';\nI=intersect(I,I{k});\n'
    script += 'ideal sRP=std(RP); ideal sI=std(I);\n'
    script += 'print("EQ=" + string(size(reduce(I,sRP))==0 && size(reduce(RP,sI))==0));\n'
    script += 'print("RPSUB=" + string(size(reduce(I,sRP))==0));\n'   # V(P) subset V(I)? i.e. I subset rad(P) -> V(P) subset V(I)
    res = sing.run(script)
    out['sigma_complete_C'] = 'EQ=1' in res
    # --- smoothness/disjointness/dimensions (B1)
    dims = {c['kind'] for c in comps}
    curves = [c for c in comps if c['kind'] == 'curve']
    pts = [c for c in comps if c['kind'] == 'point']
    b1_notes = []
    b1 = True
    if len(dims) > 1:
        b1 = False; b1_notes.append('components of different dimension (curve and points)')
    for c in curves:
        f = c['f']
        unit, K = zl.sat_unit([f] + grad(f))
        c['smooth'] = unit
        if not unit:
            b1 = False; b1_notes.append(f'curve {{{f}=0}} not certified smooth (singular real points may exist)')
    for a, b in itertools.combinations(curves, 2):
        unit, K = zl.sat_unit([a['f'], b['f']])
        if not unit:
            b1 = False; b1_notes.append(f'components {{{a["f"]}=0}} and {{{b["f"]}=0}} may intersect')
    for c in curves:
        for p in pts:
            if sp.simplify(c['f'].subs({x: p['pt'][0], y: p['pt'][1], z: p['pt'][2]})) == 0:
                b1 = False; b1_notes.append('a point lies on a curve component')
    out['B1'] = b1; out['B1_notes'] = b1_notes
    out['s'] = (1 if curves else 0) if len(dims) == 1 else None
    # --- B2 (Morse-Bott): kernel of Hess u_m(omega) = T_omega Z
    H = hess(um)
    b2 = True; b2_notes = []
    for c in curves:
        unit, K = zl.sat_unit([c['f']] + list(H))
        if not unit:
            # does the Hessian vanish identically on the curve?
            if all(zl.divides(c['f'], h) for h in H if h != 0):
                b2 = False; b2_notes.append(f'Hess u_m == 0 on {{{c["f"]}=0}} (multiplicity >= 4: degenerate)')
            else:
                b2 = None; b2_notes.append(f'Hess u_m rank on {{{c["f"]}=0}} inconclusive')
        else:
            b2_notes.append(f'Hess u_m != 0 on {{{c["f"]}=0}} (rank 1 = n-1-s): Morse-Bott')
    for p in pts:
        Hp = H.subs({x: p['pt'][0], y: p['pt'][1], z: p['pt'][2]})
        rk = Hp.rank()
        if rk != 2:
            b2 = False; b2_notes.append(f'zero direction {tuple(p["pt"])}: rank Hess = {rk} < 2 (degenerate transverse part)')
    out['B2'] = b2; out['B2_notes'] = b2_notes
    # --- next forms
    higher = [k for k in pr if k > m]
    out['l2'] = higher[0] if higher else None
    out['u_next'] = str(pr[m + 1]) if (m + 1) in pr else '0'
    # --- B3: g = u_{m+1}|_Sigma has 0 as a regular value
    if (m + 1) not in pr:
        out['B3'] = False; out['B3_notes'] = ['u_{m+1} == 0']
    else:
        h = pr[m + 1]
        b3 = True; b3_notes = []
        for c in curves:
            f = c['f']
            if zl.divides(f, h):
                b3 = False; b3_notes.append(f'u_{m+1} == 0 on {{{f}=0}}'); continue
            Dm = sp.Matrix([grad(h), grad(f), list(X)]).det()
            unit, K = zl.sat_unit([f, h, sp.expand(Dm)])
            if unit:
                b3_notes.append(f'0 regular value of u_{m+1} on {{{f}=0}} (ideal (f,h,det[grad h,grad f,q]) has no real nonzero zero)')
            else:
                pz = zl.exact_common_zero([f, h, sp.expand(Dm)])
                if pz:
                    b3 = False
                    b3_notes.append(f'g = u_{m+1}|{{{f}=0}} has a MULTIPLE zero at w={pz}: f=h=0 and dh|T = 0 there (exact)')
                else:
                    b3 = None; b3_notes.append(f'regularity on {{{f}=0}} inconclusive: K={K[:80]}')
        for p in pts:
            v = h.subs({x: p['pt'][0], y: p['pt'][1], z: p['pt'][2]})
            if v == 0:
                b3 = False; b3_notes.append(f'u_{m+1}(zero direction {tuple(p["pt"])}) = 0')
        out['B3'] = b3; out['B3_notes'] = b3_notes
    return out, comps


# ===================================================================== individual criteria
def lyapunov(pr):
    if 2 in pr and min(pr) == 2:
        H = hess(pr[2]) / 2
        if not zl.is_psd(H):
            return r(Y, 'u_2 indefinite or negative')
    return r(N, 'u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)')


def kozlov_palamodov(pr, core_info):
    m = min(pr)
    if m == 2:
        return r(N, 'm = 2: covered by the Lyapunov / Koz86 columns')
    if m % 2 == 1:
        return r(Y, f'lowest form u_{m} has odd degree, hence takes negative values')
    if core_info and core_info['sos_ok']:
        return r(N, f'u_{m} >= 0 (explicit SOS), so the lowest form has no negative values')
    w = zl.find_ray_witness(pr[m], R=7)
    if w:
        return r(Y, f'u_{m}(w)<0 at w={w[0]}')
    return r(M, 'no rational negative direction found and no SOS certificate')


def kozlov86(pr):
    """Koz86 / Neg95 Thm 4.1: u_2 >= 0, u_k (first nonzero form of degree >=3) restricted to ker u_2 has no minimum"""
    m = min(pr)
    if m != 2:
        return r(N, 'u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)')
    A = hess(pr[2]) / 2
    if not zl.is_psd(A):
        return r(N, 'u_2 not >= 0')
    ker = A.nullspace()
    higher = [k for k in pr if k >= 3]
    if not higher:
        return r(N, 'no higher forms')
    k = higher[0]
    a, b = sp.symbols('a b')
    if len(ker) == 3:
        return r(N, 'u_2 = 0')
    if len(ker) == 0:
        return r(N, 'u_2 > 0 (strict minimum)')
    if len(ker) == 1:
        q = ker[0] * a
    else:
        q = ker[0] * a + ker[1] * b
    uk = sp.expand(pr[k].subs({x: q[0], y: q[1], z: q[2]}, simultaneous=True))
    if uk == 0:
        return r(N, f'u_{k}|ker u_2 == 0 for the first form u_{k} (literal hypothesis V_2 + V_m + ...)')
    if len(ker) == 1:
        if k % 2 == 1 or uk.subs(a, 1) < 0:
            return r(Y, f'ker u_2 is a line, u_{k}|ker = {uk}: no minimum')
        return r(N, f'u_{k}|ker = {uk} >= 0')
    # 2-dim kernel: rational search for a negative value
    for v in itertools.product(range(-6, 7), repeat=2):
        if v == (0, 0):
            continue
        val = uk.subs({a: v[0], b: v[1]})
        if val < 0:
            return r(Y, f'dim ker u_2 = 2, u_{k}|ker({v}) = {val} < 0')
    return r(M, f'dim ker u_2 = 2; u_{k}|ker has no negative value among small rational points')


def fgt_corank(pr):
    """conditional: Hessian >= 0 with kernel of dim <= 2 (Freire-Garcia-Tal 2008 as quoted in AG17; hypotheses
    NOT verified at the source; Pa20 Thm 5 for corank 1 likewise unverified)"""
    if min(pr) != 2:
        return r(N, 'u_2 = 0 (Hessian is zero, kernel of dimension 3)')
    A = hess(pr[2]) / 2
    if not zl.is_psd(A):
        return r(N, 'Hessian not >= 0')
    k = 3 - A.rank()
    if k == 0:
        return r(N, 'Hessian positive definite')
    return r(M, f'Hessian >= 0 with kernel of dimension {k} <= 2: covered by FGT08/Pa20-T5 IF their hypotheses are as '
                f'recorded in KNOWN_RESULTS (not verified at the source)')


def pa20_T3(pr, core_info):
    m = min(pr)
    if core_info and core_info['sos_ok'] and core_info['ncomp'] > 0:
        return r(N, f'u_{m} >= 0 vanishes at nonzero points, which are critical points of u_{m} (grad u_{m} = 0 at a minimum)')
    st_, how = zl.no_real_critical_points(pr[m])
    ok = st_ == 'none'
    if ok:
        if m % 2 == 1 or zl.find_ray_witness(pr[m], R=6):
            return r(Y, f'grad u_{m} != 0 off 0 ({how}), u_{m} takes negative values')
        return r(N, 'grad u_m != 0 but u_m has no negative values')
    return r(M, 'inconclusive')


def quasi_homog_linear(U, pr):
    wd = zl.weights_for(U)
    if wd is None:
        return r(N, 'U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)')
    neg = zl.find_ray_witness(U, R=7)
    a, d = wd
    # for qh polynomial negative values anywhere give negative values near 0 by scaling; search general points
    found = zl.any_negative_value(U, 6)
    if found is None:
        return r(M, f'U quasi-homogeneous with weights {a}, degree {d}, but no negative value found')
    return r(Y, f'U quasi-homogeneous with weights {a}, degree {d}; U{found} < 0 (Euler field V = (1/d) sum a_i x_i d_i)')


def pa20_T6(U):
    res = zl.t6_check(U)
    best = None
    notes = []
    for f in res:
        base = f['nocrit'] and f['negative']
        tag = f"weights {f['weights']}, d={f['d']}, face has {f['nface']} monomials, tail wdeg_min={f['tail_min']}"
        if base and f['strong']:
            return r(Y, tag + ' (principal part no real crit. points, negative values, tail >= d + a_max)'), res
        if base and f['weak']:
            best = r(M, tag + ': tail only >= d + a_min (covered only under the weaker reading of O(|x||x|_w))')
        elif base:
            notes.append(tag + ': principal part is fine but the tail is TOO LARGE (' + f"{f['tail_min']} < d + a_min={f['d'] + min(f['weights'])}" + ')')
        else:
            notes.append(tag + f": principal part {('has real critical points (exact)' if f['crit_status'] == 'exist' else 'no certificate of absence of real critical points') if not f['nocrit'] else 'has no negative values'}")
    if best:
        return best, res
    return r(N, '; '.join(notes) if notes else 'no compact facet'), res


def burgos_prop12(pr, core_info):
    m = min(pr)
    if core_info and core_info['sos_ok'] and core_info['ncomp'] > 0:
        return r(N, f'f = u_{m}|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value')
    return r(M, 'not evaluated (no hard-core data)')


def burgos_cor14(U, pr, core_info, comps, extra_pts=()):
    """Burgos 2025 Cor 1.4 (as in KNOWN_RESULTS): U not homogeneous, second nonzero form u_{l2} < 0 at all critical
    points of f = u_m|S with f <= 0.  For u_m >= 0 these are exactly the zeros of u_m on the sphere."""
    m = min(pr)
    if not core_info or not core_info['sos_ok']:
        return r(M, 'no hard-core data')
    l2 = core_info['l2']
    if l2 is None:
        return r(N, 'U homogeneous')
    if l2 % 2 == 1:
        return r(N, f'l2 = {l2} odd and Sigma = -Sigma: u_{l2}(-w) = -u_{l2}(w), so u_{l2} < 0 on all of Sigma is impossible')
    h = pr[l2]
    for c in comps:
        if c['kind'] == 'point':
            if h.subs({x: c['pt'][0], y: c['pt'][1], z: c['pt'][2]}) >= 0:
                return r(N, f'u_{l2}(zero direction {tuple(c["pt"])}) >= 0')
        else:
            unit, K = zl.sat_unit([c['f'], h])
            if not unit:
                return r(N, f'u_{l2} has real zeros on {{{c["f"]}=0}} (or inconclusive): ideal saturation not the unit ideal')
            # constant sign: test one rational point of the cone via search
            pt = None
            for v in list(extra_pts) + list(zl.prim_vectors(6)):
                if c['f'].subs({x: v[0], y: v[1], z: v[2]}) == 0:
                    pt = v; break
            if pt is None:
                return r(M, 'no rational point on the component to determine the sign')
            if h.subs({x: pt[0], y: pt[1], z: pt[2]}) >= 0:
                return r(N, f'u_{l2} > 0 on {{{c["f"]}=0}}')
    return r(Y, f'u_{l2} < 0 on the whole zero set of u_{m} (l2 = {l2} even)')


def theorem_B(core_info):
    if not core_info:
        return r(M, 'no data'), {}
    m = core_info['m']
    flags = dict(B1=core_info['B1'], B2=core_info['B2'], B3=core_info['B3'])
    nx = []
    for k in ('B1', 'B2', 'B3'):
        v = core_info[k]
        if v is not True:
            nx.append(f'({k}) ' + ('fails' if v is False else 'inconclusive') + ': ' + '; '.join(core_info.get(k + '_notes', [])))
    if all(v is True for v in flags.values()) and core_info['sos_ok']:
        return r(Y, 'B1 (Sigma smooth submanifold), B2 (Morse-Bott), B3 (0 regular value of u_{m+1}|Sigma): ' +
                 ' | '.join(core_info['B2_notes'] + core_info['B3_notes'])), flags
    if any(v is False for v in flags.values()):
        return r(N, ' | '.join(nx)), flags
    return r(M, ' | '.join(nx)), flags


# ----------------------------------------------------------------------------- Example-13 type
def circular_cone_form(um):
    """if u_m = c * f^2 with f a quadratic form whose matrix has eigenvalues (a,a,-a): return f, else None"""
    c, facs = sp.factor_list(um, *X)
    if len(facs) != 1 or facs[0][1] != 2:
        return None
    f = facs[0][0]
    if sp.Poly(f, *X).total_degree() != 2 or sp.Poly(f, *X).is_homogeneous is False:
        return None
    A = sp.hessian(f, X) / 2
    ev = A.eigenvals()
    evs = []
    for k, mult in ev.items():
        evs += [k] * mult
    evs = sorted(evs, key=lambda t: float(t))
    if len(evs) != 3:
        return None
    a, b, cc = evs
    if sp.simplify(a - b) == 0 and sp.simplify(b + cc) == 0 and a != 0:
        return f   # eigenvalues (-s,-s,s)? check sign pattern below
    if sp.simplify(b - cc) == 0 and sp.simplify(a + b) == 0 and a != 0:
        return f
    return None


def n13_star(U, pr, core_info, comps, extra_pts=()):
    """Example-13 criterion (results/003, Remark 3, Prop. 1, [Эскиз]): U = Q^2 + W (Q a circular 45-degree cone form
    up to an orthogonal change and a positive factor), W = W_m + ..., m >= 5; 0 is a regular value of W_m on the
    gutter {Q=0} and W_m takes negative values there."""
    m = min(pr)
    if m != 4 or not core_info or not core_info['sos_ok']:
        return r(N, 'u_4 is not of the form c Q^2')
    f = circular_cone_form(pr[4])
    if f is None:
        # distinguish the reason
        c, facs = sp.factor_list(pr[4], *X)
        if len(facs) == 1 and facs[0][1] == 2 and sp.Poly(facs[0][0], *X).total_degree() == 2:
            A = sp.hessian(facs[0][0], X) / 2
            return r(N, f'u_4 = c Q^2 but the cone Q=0 is not circular with aperture 90 degrees: eigenvalues of Q: {list(A.eigenvals().items())}')
        return r(N, 'u_4 is not c Q^2 with a quadratic form Q')
    W = sp.expand(U - pr[4])
    pw = parts(W)
    if not pw:
        return r(N, 'W = 0')
    mm = min(pw)
    if mm < 5:
        return r(N, 'W has degree < 5')
    h = pw[mm]
    if zl.divides(f, h):
        return r(N, f'W_{mm} vanishes identically on the gutter: effective potential is not W_{mm}; G == 0')
    Dm = sp.Matrix([grad(h), grad(f), list(X)]).det()
    unit, K = zl.sat_unit([f, h, sp.expand(Dm)])
    if not unit:
        pz = zl.exact_common_zero([f, h, sp.expand(Dm)])
        if pz:
            return r(N, f'W_{mm}|gutter has a multiple zero at w={pz} (exact): not a regular value')
        return r(M, f'W_{mm}|gutter regularity inconclusive')
    if mm % 2 == 1:
        return r(Y, f'circular 45-degree cone, W_{mm} (m={mm}, odd) has only simple zeros on the gutter and takes negative values [Эскиз, 003 Prop. 1]')
    # even: need a negative point on the cone
    for v in list(extra_pts) + list(zl.prim_vectors(8)):
        if sp.expand(f.subs({x: v[0], y: v[1], z: v[2]})) == 0 and h.subs({x: v[0], y: v[1], z: v[2]}) < 0:
            return r(Y, f'circular 45-degree cone, W_{mm} simple zeros, negative at the gutter point {v} [Эскиз, 003 Prop. 1]')
    return r(M, f'W_{mm} has only simple zeros on the gutter but no negative gutter point found (maybe positive: then minimum)')




def not_local_min_2var(f, a, b):
    """one-sided exact search: does f(a,b) take negative values arbitrarily close to 0?  Uses rational rays (lowest
    order terms) and the quasi-homogeneous parts along compact edges of the Newton polygon (integer arithmetic)."""
    import numpy as np
    from scipy.spatial import ConvexHull
    pf = sp.Poly(sp.expand(f), a, b)
    if pf.is_zero:
        return None
    den = int(sp.ilcm(1, 1, *[sp.Rational(cc).q for cc in pf.coeffs()]))
    tr = [(m, int(cc * den)) for m, cc in pf.terms()]
    for v in itertools.product(range(-8, 9), repeat=2):
        if v == (0, 0):
            continue
        acc = {}
        for m, cc in tr:
            acc[m[0] + m[1]] = acc.get(m[0] + m[1], 0) + cc * v[0] ** m[0] * v[1] ** m[1]
        ks = sorted(k for k, val in acc.items() if val != 0)
        if ks and (acc[ks[0]] < 0 or ks[0] % 2 == 1):
            return ('ray', v, ks[0], sp.Rational(acc[ks[0]], den))
    pts = [m for m, _ in tr]
    E = np.array(pts, float)
    big = 100.0
    try:
        hull = ConvexHull(np.vstack([E, E + [big, 0], E + [0, big]]))
    except Exception:
        return None
    seen = set()
    for eq in hull.equations:
        n1, n2 = eq[0], eq[1]
        if n1 < -1e-9 and n2 < -1e-9:
            wts = sp.Rational(-n1).limit_denominator(1000), sp.Rational(-n2).limit_denominator(1000)
            dd = sp.ilcm(wts[0].q, wts[1].q); wts = (int(wts[0] * dd), int(wts[1] * dd))
            gg = sp.igcd(0, 0, *wts); wts = (wts[0] // gg, wts[1] // gg)
            if wts in seen:
                continue
            seen.add(wts)
            dmin = min(wts[0] * m[0] + wts[1] * m[1] for m in pts)
            face = [(m, cc) for m, cc in tr if wts[0] * m[0] + wts[1] * m[1] == dmin]
            for v in itertools.product(range(-8, 9), repeat=2):
                if v[0] == 0 or v[1] == 0:
                    continue
                val = sum(cc * v[0] ** m[0] * v[1] ** m[1] for m, cc in face)
                if val < 0:
                    return ('edge', wts, dmin, v, sp.Rational(val, den))
    return None


def restricted_verdict(f, a, b):
    """Is 0 a local minimum of the 2-variable polynomial f?  ('yes', exact witness) if the one-sided exact search finds
    negative values arbitrarily close to 0; ('maybe', note) if only a floating-point scan sees negative values;
    ('no', note) if neither does (then 0 looks like a local minimum: the reduction does not help)."""
    import numpy as np
    w = not_local_min_2var(f, a, b)
    if w:
        return 'yes', str(w)
    fl = sp.lambdify((a, b), f, 'numpy')
    th = np.linspace(0, 2 * np.pi, 400001)
    for rr in (0.1, 0.03, 0.01, 0.003):
        v = fl(rr * np.cos(th), rr * np.sin(th)) * np.ones_like(th)
        if v.min() < -1e-9 * max(1e-300, np.abs(v).max()) * 0 - 1e-14 * rr**4:
            return 'maybe', f'floating-point scan finds f < 0 at radius {rr} but no exact witness (arcs along irrational directions?)'
    return 'no', 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'










# ----------------------------------------------------------------------------- all invariant planes and lines
def real_solutions(eqs, vars_):
    """real solutions of a polynomial system (exact): Singular + sympy.
    Returns (kind, sols, families): kind 'none' | 'finite' | 'mixed' | 'error'; sols = isolated real solutions
    (tuples of exact numbers); families = list of strings describing positive-dimensional components that are NOT
    hyperplanes in the unknowns (hyperplane families are reported as 'linear:<eq>')."""
    vs = ','.join(str(v) for v in vars_)
    revs = ','.join(str(v) for v in reversed(vars_))
    g = ','.join(sing.to_sing(e) for e in eqs if e != 0)
    if not g:
        return 'mixed', [], ['everything']
    out = sing.run(sing.HEAD + f'ring r=0,({vs}),dp; ideal J={g}; ideal s=std(J); print("DIM=" + string(dim(s))); '
                   f'print("VDIM=" + string(vdim(s)));')
    dimv = int(out.split('DIM=')[1].split()[0]); vd = int(out.split('VDIM=')[1].split()[0])
    loc = {str(v): v for v in vars_}
    if dimv <= 0 and vd == 0:
        return 'none', [], []
    if dimv <= 0:
        out = sing.run(sing.HEAD + f'ring r=0,({revs}),lp; ideal J={g}; ideal s=std(J); print("GB=" + string(s));')
        gb = out.split('GB=')[1].strip().split(',')
        eq = [sp.sympify(t.replace('^', '**'), locals=loc) for t in gb]
        try:
            sols = sp.solve_poly_system(eq, *reversed(vars_))
        except Exception:
            return 'error', [], []
        res = []
        for s in sols:
            v = [sp.nsimplify(sp.simplify(t)) for t in s[::-1]]
            if all(abs(sp.im(sp.N(t))) < 1e-12 for t in v):
                res.append(tuple(sp.re(t) if not t.is_real else t for t in v))
        return 'finite', res, []
    # positive-dimensional: decompose
    out = sing.run(sing.HEAD + f'ring r=0,({vs}),dp; ideal J={g}; list L=minAssGTZ(J); int i; '
                   'for(i=1;i<=size(L);i++){print("COMP dim=" + string(dim(std(L[i]))) + " : " + string(L[i]));}')
    sols, fam = [], []
    for ln in out.splitlines():
        if not ln.startswith('COMP'):
            continue
        d_ = int(ln.split('dim=')[1].split()[0]); gens = ln.split(':', 1)[1].strip().split(',')
        eqs2 = [sp.sympify(t.replace('^', '**'), locals=loc) for t in gens]
        if d_ == 0:
            try:
                ss = sp.solve_poly_system(eqs2, *vars_)
            except Exception:
                return 'error', [], []
            for s in ss:
                v = [sp.nsimplify(sp.simplify(t)) for t in s]
                if all(abs(sp.im(sp.N(t))) < 1e-12 for t in v):
                    sols.append(tuple(sp.re(t) if not t.is_real else t for t in v))
        elif len(eqs2) == 1 and sp.Poly(eqs2[0], *vars_).total_degree() == 1:
            fam.append('linear:' + str(eqs2[0]))
        else:
            fam.append('nonlinear:' + ','.join(gens))
    return 'mixed', sols, fam


def invariant_subspace_search(U):
    """EVERY plane {n.q = 0} and every line R d through 0 that is invariant for q'' = -grad U (n.grad U = 0 on the
    plane; grad U(td) parallel to d), found exactly (charts for n, d; solved with Singular + sympy).  For each
    rational one the restriction of U is tested (n=2: Palamodov/Taliaferro/Kozlov; n=1: trivial)."""
    a, b, c, t = sp.symbols('pa pb pc pt')
    out = []
    Ux, Uy, Uz = grad(U)
    X_, Y_ = sp.symbols('X Y')
    # ---- planes
    charts = [('n=(a,b,1)', (a, b, 1), (a, b), lambda: None)]
    # chart 1: z = -a x - b y
    def plane_chart(nv, unknowns, elim, free):
        F = sp.expand((nv[0] * Ux + nv[1] * Uy + nv[2] * Uz).subs(elim, simultaneous=True))
        co = sp.Poly(F, *free).coeffs() if F != 0 else []
        return co
    cases = [
        ('(a,b,1)', (a, b, sp.Integer(1)), (a, b), {z: -a * x - b * y}, (x, y)),
        ('(a,1,0)', (a, sp.Integer(1), sp.Integer(0)), (a,), {y: -a * x}, (x, z)),
    ]
    sols_planes = []
    for name, nv, unk, elim, free in cases:
        co = plane_chart(nv, unk, elim, free)
        kind, sols, fam = real_solutions(co, list(unk))
        for f_ in fam:
            if f_.startswith('linear:'):
                out.append(dict(kind='plane', chart=name, verdict='info', note=f'a 1-parameter family of invariant planes (pencil {f_}) -- not enumerated'))
            else:
                out.append(dict(kind='plane', chart=name, verdict='maybe', note=f'positive-dimensional family of invariant planes {f_}: not evaluated'))
        if kind == 'error':
            out.append(dict(kind='plane', chart=name, verdict='maybe', note='solver failed'))
        for s in sols:
            vals = dict(zip(unk, s))
            nvec = [sp.nsimplify(e.subs(vals)) if hasattr(e, 'subs') else e for e in nv]
            sols_planes.append(nvec)
    # coordinate plane x = 0 : n=(1,0,0)
    if sp.expand(Ux.subs({x: 0})) == 0:
        sols_planes.append([sp.Integer(1), sp.Integer(0), sp.Integer(0)])
    A_, B_ = sp.symbols('a b')
    for nvec in sols_planes:
        if not all(isinstance(e, sp.Rational) for e in nvec):
            out.append(dict(kind='plane', normal=str(nvec), verdict='maybe', note='invariant plane with irrational normal: restriction not evaluated'))
            continue
        den = sp.ilcm(1, 1, *[e.q for e in nvec]); nv = [int(e * den) for e in nvec]
        ns = sp.Matrix([nv]).nullspace()
        q = A_ * ns[0] + B_ * ns[1]
        f = sp.expand(U.subs({x: q[0], y: q[1], z: q[2]}, simultaneous=True))
        vd, note = restricted_verdict(f, A_, B_)
        out.append(dict(kind='plane', normal=nv, verdict=vd, note=note))
    # ---- lines: d=(1,b,c), (0,1,c), (0,0,1)
    cross = lambda dv: [sp.expand(e.subs({x: t * dv[0], y: t * dv[1], z: t * dv[2]}, simultaneous=True))
                        for e in (Uy * dv[2] - Uz * dv[1], Uz * dv[0] - Ux * dv[2], Ux * dv[1] - Uy * dv[0])]
    lcases = [((sp.Integer(1), b, c), (b, c)), ((sp.Integer(0), sp.Integer(1), c), (c,)), ((sp.Integer(0), sp.Integer(0), sp.Integer(1)), ())]
    for dv, unk in lcases:
        eqs = []
        for ex in cross(dv):
            if ex != 0:
                eqs += sp.Poly(ex, t).coeffs()
        fam = []
        if not unk:
            if not eqs:
                sols = [()]; kind = 'finite'
            else:
                kind, sols = 'none', []
        else:
            if not eqs:
                kind, sols, fam = 'mixed', [], ['everything']
            else:
                kind, sols, fam = real_solutions(eqs, list(unk))
        for f_ in fam:
            if f_ == 'everything' and dv[0] == 0 and dv[1] == 1:
                out.append(dict(kind='line', verdict='info', note='all lines of the plane {x=0} are invariant; that plane is tested by the plane search'))
            elif f_.startswith('linear:'):
                out.append(dict(kind='line', verdict='info', note=f'chart {dv}: family of invariant lines lying in a plane ({f_}); that plane is tested by the plane search'))
            else:
                out.append(dict(kind='line', verdict='maybe', note=f'chart {dv}: positive-dimensional family of invariant lines {f_}: not evaluated'))
        for s in sols:
            vals = dict(zip(unk, s))
            d = [sp.nsimplify(e.subs(vals)) if hasattr(e, 'subs') else e for e in dv]
            if not all(isinstance(e, sp.Rational) for e in d):
                out.append(dict(kind='line', direction=str(d), verdict='maybe', note='irrational invariant line: not evaluated'))
                continue
            den = sp.ilcm(1, 1, *[e.q for e in d]); dd = [int(e * den) for e in d]
            k, cc = zl.ray_series(U, tuple(dd))
            neg = k is not None and (cc < 0 or k % 2 == 1)
            out.append(dict(kind='line', direction=dd, verdict='yes' if neg else 'no',
                            note=f'U on the line = {cc} t^{k} + ...' if k else 'U = 0 on the line'))
    return out


# ----------------------------------------------------------------------------- naive effective potential on a conic gutter
def gutter_info(U, f, extra_pts=()):
    """For a single conic gutter {f=0}: restrict the first form u_l (l > m) that is not identically zero on the gutter to the
    gutter via a rational parametrisation; report the factorisation of the resulting univariate polynomial N(tau)
    with multiplicities and numbers of real roots, and the order of vanishing at tau = infinity.
    NOTE: this is the NAIVE restriction (no completion of squares); it is the effective potential only when the lower
    forms u_{m+1},... restricted/differentiated along the normal do not contribute (flagged in the text)."""
    pr = parts(U)
    m = min(pr)
    pt = None
    for v in list(extra_pts) + list(zl.prim_vectors(6)):
        if sp.expand(f.subs({x: v[0], y: v[1], z: v[2]})) == 0:
            pt = v; break
    if pt is None:
        return None
    par, t = zl.conic_rational_param(f, pt)
    out = dict(point=pt, param=[str(e) for e in par], terms=[])
    for l in sorted(k for k in pr if k > m):
        N = sp.expand(pr[l].subs({x: par[0], y: par[1], z: par[2]}, simultaneous=True))
        if N == 0:
            out['terms'].append(dict(degree=l, zero=True))
            continue
        # make the upper nappe the reference: sign of z-component for odd l is irrelevant to multiplicities
        c, fl = sp.factor_list(N, t)
        degN = sp.Poly(N, t).degree()
        lst = []
        for fac, mult in fl:
            nr = sp.Poly(fac, t).count_roots() if sp.Poly(fac, t).degree() > 0 else 0
            lst.append((str(fac), mult, nr))
        out['terms'].append(dict(degree=l, zero=False, const=str(c), factors=lst, deg_in_t=degN,
                                 inf_order=2 * l - degN))
        break
    return out
