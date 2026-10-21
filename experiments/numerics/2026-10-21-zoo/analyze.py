"""analyze.py -- full exact analysis of one catalogue entry"""
import time, json
import sympy as sp
import zoolib as zl
import criteria as cr
from zoolib import x, y, z, X, P, parts


def analyze(e, quick=False):
    t0 = time.time()
    U = P(e['U'])
    pr = parts(U)
    res = dict(id=e['id'], name=e.get('name', ''), U=str(U), forms={k: str(v) for k, v in pr.items()})
    m = min(pr)
    res['m'] = m
    res['basic'] = dict(U0=U.subs({x: 0, y: 0, z: 0}) == 0, grad0=all(g.subs({x: 0, y: 0, z: 0}) == 0 for g in zl.grad(U)))
    # ---------------- isolation
    res['isolation'] = zl.isolation(U)
    # ---------------- not a minimum: explicit witness
    w = e.get('witness')
    if w and w[0] == 'curve':
        k, c = zl.curve_witness(U, w[1])
        res['witness'] = dict(kind='curve', curve=[str(a) for a in w[1]], order=int(k), coeff=str(c), negative=bool(c < 0))
    elif w and w[0] == 'arc':           # arc on a surface F=0: x(tau) from series, y=a tau, z=tau
        F, a_, b_, N = P(w[1]), sp.Rational(w[2]), sp.Rational(w[3]), w[4]
        xs = zl.arc_on_surface(F, a_, b_, N)
        tau = sp.Symbol('tau')
        k, c = zl.curve_witness(U, (xs, a_ * tau, tau))
        res['witness'] = dict(kind='arc', curve=[str(xs), str(a_ * tau), 'tau'], order=int(k), coeff=str(c), negative=bool(c < 0))
    elif w and w[0] == 'ray':
        k, c = zl.ray_series(U, tuple(w[1]))
        res['witness'] = dict(kind='ray', w=list(w[1]), order=int(k), coeff=str(c), negative=bool(c < 0))
    else:
        ww = zl.find_ray_witness(U, R=e.get('R', 7))
        if ww:
            res['witness'] = dict(kind='ray', w=list(ww[0]), order=int(ww[1]), coeff=str(ww[2]), negative=bool(ww[2] < 0))
        else:
            res['witness'] = None
    # ---------------- hard core
    core = e.get('core')
    ci, comps = (None, [])
    if core:
        ci, comps = cr.hard_core_data(U, core)
    res['core'] = ci
    # ---------------- criteria
    C = {}
    C['Lyapunov'] = cr.lyapunov(pr)
    C['KP82'] = cr.kozlov_palamodov(pr, ci)
    C['Koz86'] = cr.kozlov86(pr)
    C['FGT08*'] = cr.fgt_corank(pr)
    C['Pa20-T3'] = cr.pa20_T3(pr, ci)
    C['QH-linear'] = cr.quasi_homog_linear(U, pr)
    t6, t6data = cr.pa20_T6(U)
    C['Pa20-T6'] = t6
    C['Bu25-P1.2'] = cr.burgos_prop12(pr, ci)
    hints = []
    if res['witness'] and res['witness']['kind'] == 'ray':
        hints = [tuple(res['witness']['w'])]
    C['Bu25-C1.4'] = cr.burgos_cor14(U, pr, ci, comps, hints)
    thB, flags = cr.theorem_B(ci)
    C['ThmB'] = thB
    C['N13*'] = cr.n13_star(U, pr, ci, comps, hints)
    # N13 proper: identical to Example 13 up to orthogonal change (declared and verified exactly)
    eq = e.get('equiv_ex13')
    if eq is not None:
        Rm = sp.Matrix(eq)
        assert sp.simplify(Rm * Rm.T - sp.eye(3)) == sp.zeros(3, 3)
        q = Rm * sp.Matrix(X)
        U13 = (x**2 + y**2 - z**2)**2 + z**5 * x + z**4 * x * y + sp.Rational(1, 2) * z**6
        lam = e.get('equiv_scale', 1)
        ok = sp.expand(U - lam * U13.subs({x: q[0], y: q[1], z: q[2]}, simultaneous=True)) == 0
        C['N13'] = cr.r(cr.Y if ok else cr.N, 'U = c * U_13(R q) with R orthogonal (exact identity): Theorem 1 of 003 [Доказано, R8]' if ok else 'declared equivalence is false')
    else:
        U13 = (x**2 + y**2 - z**2)**2 + z**5 * x + z**4 * x * y + sp.Rational(1, 2) * z**6
        C['N13'] = cr.r(cr.Y if sp.expand(U - U13) == 0 else cr.N,
                        'U is exactly the polynomial of Example 13' if sp.expand(U - U13) == 0 else 'U is not (a rotation/scaling of) the Example-13 polynomial')
    # reduction to n <= 2: ALL invariant planes / lines of the dynamics (includes every isometric symmetry reduction)
    inv = cr.invariant_subspace_search(U)
    res['invariant_subspaces'] = inv
    yes = [v for v in inv if v['verdict'] == 'yes']
    maybe = [v for v in inv if v['verdict'] == 'maybe']
    if yes:
        v = yes[0]
        desc = (f"invariant plane with normal {v['normal']}, U|plane is not a local minimum (exact witness {v['note']}) -> n=2 theorem"
                if v['kind'] == 'plane' else f"invariant line {v['direction']}: {v['note']} (n=1)")
        C['SYM'] = cr.r(cr.Y, desc)
    elif maybe:
        C['SYM'] = cr.r(cr.M, '; '.join(f"{v['kind']} {v.get('normal', v.get('direction', ''))}: {v['note']}" for v in maybe))
    else:
        C['SYM'] = cr.r(cr.N, 'exact search of ALL invariant planes and lines: ' +
                        '; '.join(f"{v['kind']} {v.get('normal', v.get('direction', ''))}: {v['verdict']}" for v in inv if v['verdict'] != 'info') +
                        ' (U restricted is a local minimum / positive on each)')
    res['n_invariant_found'] = len(inv)
    res['invariant_search_done'] = True
    res['gutter'] = None
    if core and len(comps) == 1 and comps[0]['kind'] == 'curve' and sp.Poly(comps[0]['f'], *X).total_degree() == 2:
        try:
            res['gutter'] = cr.gutter_info(U, comps[0]['f'], hints)
        except Exception as ex:
            res['gutter'] = dict(error=repr(ex)[:200])
    res['T6data'] = t6data
    res['criteria'] = C
    # ---------------- coverage summary
    rig = ['Lyapunov', 'KP82', 'Koz86', 'Pa20-T3', 'QH-linear', 'Bu25-C1.4', 'SYM']      # published or elementary
    ours = ['ThmB', 'N13']
    soft = ['N13*', 'Pa20-T6', 'FGT08*']      # sketch / unverified source hypotheses
    st = lambda k: C[k]['status']
    res['covered_known'] = [k for k in rig if st(k) == 'yes']
    res['covered_ours'] = [k for k in ours if st(k) == 'yes']
    res['covered_soft'] = [k for k in soft if st(k) in ('yes', 'maybe')]
    res['not_covered'] = not (res['covered_known'] or res['covered_ours'] or res['covered_soft'])
    res['not_covered_by_proved'] = not (res['covered_known'] or res['covered_ours'])
    res['seconds'] = round(time.time() - t0, 1)
    return res
