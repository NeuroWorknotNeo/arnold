"""
zoolib.py -- exact checks for the "zoo" of hard test potentials U(x,y,z) (problem 1971-4 (A), n=3).

Everything here is exact (sympy over Q, Singular over Q), unless a function says otherwise.  Floating
point is used only (a) to *find* a rational certificate (LP for weights, convex hull for Newton facets)
and the certificate is then re-verified exactly, (b) in the optional numerical sanity module.

Notation: U = sum_k u_k (homogeneous parts), m = lowest degree, Q0 = x^2+y^2-z^2.
"""
import itertools, math
import sympy as sp
import numpy as np
import sing

x, y, z = sp.symbols('x y z')
X = (x, y, z)
R2 = x**2 + y**2 + z**2          # positive definite: nonzero at every real q != 0
Q0 = x**2 + y**2 - z**2


def P(s):
    return sp.expand(sp.sympify(s, locals={'x': x, 'y': y, 'z': z}))


def parts(U):
    Pl = sp.Poly(sp.expand(U), *X)
    d = {}
    for mon, c in Pl.terms():
        k = sum(mon)
        d[k] = d.get(k, 0) + c * x**mon[0] * y**mon[1] * z**mon[2]
    return {k: sp.expand(v) for k, v in sorted(d.items()) if sp.expand(v) != 0}


def divides(f, h):
    """exact: does the polynomial f divide h (a single polynomial is its own Groebner basis)?"""
    return sp.div(sp.Poly(h, *X), sp.Poly(f, *X))[1].is_zero


def grad(f):
    return [sp.diff(f, v) for v in X]


def hess(f):
    return sp.Matrix(3, 3, lambda i, j: sp.diff(f, X[i], X[j]))


def subs3(f, a, b, c):
    return sp.expand(f.subs({x: a, y: b, z: c}, simultaneous=True))


def is_psd(M):
    """exact: symmetric matrix is PSD iff all principal minors >= 0"""
    n = M.shape[0]
    for k in range(1, n + 1):
        for idx in itertools.combinations(range(n), k):
            if M.extract(list(idx), list(idx)).det() < 0:
                return False
    return True


# ------------------------------------------------------------------ rays / witnesses
def prim_vectors(R):
    seen = set()
    for v in itertools.product(range(-R, R + 1), repeat=3):
        if v == (0, 0, 0) or math.gcd(math.gcd(abs(v[0]), abs(v[1])), abs(v[2])) != 1:
            continue
        yield v


def _terms(U):
    """integer-scaled terms [(monomial, int)], den : U = sum / den (den > 0)"""
    Pl = sp.Poly(sp.expand(U), *X)
    den = int(sp.ilcm(1, 1, *[sp.Rational(c).q for c in Pl.coeffs()]))
    return [(m, int(c * den)) for m, c in Pl.terms()], den


def ray_series(U, w, terms=None):
    """U(t*w) as polynomial in t: returns (k, c) = lowest nonzero degree and coefficient (exact integers)"""
    tr, den = terms or _terms(U)
    acc = {}
    for m, c in tr:
        v = c * (w[0] ** m[0]) * (w[1] ** m[1]) * (w[2] ** m[2])
        k = m[0] + m[1] + m[2]
        acc[k] = acc.get(k, 0) + v
    ks = sorted(k for k, v in acc.items() if v != 0)
    if not ks:
        return None, 0
    return ks[0], sp.Rational(acc[ks[0]], den)


def find_ray_witness(U, R=7, restrict=None):
    """exact search for rational direction w with U(t w) < 0 for small t>0.  restrict: predicate on w.
    Prefers the shallowest witness (smallest order k of the lowest nonzero term), first found among small vectors."""
    best = None
    terms = _terms(U)
    for w in prim_vectors(R):
        if restrict and not restrict(w):
            continue
        k, c = ray_series(U, w, terms)
        if k is None:
            continue
        if c < 0:
            cand = (w, k, c)
        elif k % 2 == 1:
            cand = (tuple(-a for a in w), k, -c)
        else:
            continue
        if best is None or cand[1] < best[1]:
            best = cand
    return best


def any_negative_value(U, R=6):
    """exact: some integer point v with U(v) < 0 (U need not be small there)"""
    terms, den = _terms(U)
    for v in itertools.product(range(-R, R + 1), repeat=3):
        if v == (0, 0, 0):
            continue
        tot = 0
        for m, c in terms:
            tot += c * (v[0] ** m[0]) * (v[1] ** m[1]) * (v[2] ** m[2])
        if tot < 0:
            return v
    return None


def curve_witness(U, curve):
    """curve = (x(t),y(t),z(t)) polynomials in tau.  Returns (k, c): U(gamma(tau)) = c tau^k + ..."""
    tau = sp.Symbol('tau')
    g = [sp.sympify(e, locals={'tau': tau}) for e in curve]
    pw = sp.Poly(sp.expand(U.subs({x: g[0], y: g[1], z: g[2]}, simultaneous=True)), tau)
    terms = sorted([(k[0], c) for k, c in pw.terms() if c != 0])
    return terms[0]


def arc_on_surface(F, a, b, N):
    """Truncated power series x(tau) = b tau + c2 tau^2 + ... (rational) with F(x, a tau, tau) = O(tau^{N+2}),
    for F with F(b tau, a tau, tau) = O(tau^3) (lowest form vanishes at (b,a,1)) and F_x != 0 there.
    Returns the polynomial x(tau)."""
    tau = sp.Symbol('tau')
    xs = b * tau
    for k in range(2, N + 1):
        c = sp.Symbol('c')
        e = sp.expand(F.subs({x: xs + c * tau**k, y: a * tau, z: tau}, simultaneous=True))
        co = sp.Poly(e, tau).coeff_monomial(tau**(k + 1))
        sol = sp.solve(co, c)
        xs = xs + sol[0] * tau**k
    return xs


# ------------------------------------------------------------------ isolation (exact)
def pd_candidates():
    """positive definite diagonal quadrics a x^2 + b y^2 + c z^2, ordered by size"""
    c = [(a, b, cc) for a in range(1, 7) for b in range(1, 7) for cc in range(1, 7)]
    c.sort(key=lambda t: (t[0] + t[1] + t[2], t))
    return [a * x**2 + b * y**2 + cc * z**2 for a, b, cc in c]


def real_isolation_cert(J):
    """Exact sufficient certificate that 0 is an isolated REAL zero of the ideal J (polynomials vanishing at 0):
    K = J : p^infty with p positive definite; real zeros q != 0 satisfy p(q) > 0, hence lie in V(K);
    if K is not contained in the maximal ideal, 0 is not in V(K), so there are no real zeros q != 0 near 0.
    Returns (ok, p)."""
    for p in pd_candidates():
        unit, inm, K = sing.sat_check(J, p)
        if not inm:
            return True, p
    return False, None


def sat_unit(gens):
    """True iff, for some positive definite diagonal quadric p, <gens> : p^infty is the unit ideal; then the
    ideal has NO real zero q != 0 (such a zero would satisfy p(q) > 0 and lie in V(K) = empty).  Returns (bool, K)."""
    last = None
    for p in pd_candidates()[:12]:
        unit, inm, K = sing.sat_check(gens, p)
        if unit:
            return True, K
        last = K
    return False, last


def exact_common_zero(gens, R=8):
    """exact search for a nonzero integer point where all gens vanish (proves that the ideal has a real nonzero zero)"""
    gs = [sp.Poly(g, *X) for g in gens]
    for v in prim_vectors(R):
        if all(g.eval({x: v[0], y: v[1], z: v[2]}) == 0 for g in gs):
            return v
    return None


def isolation(U, with_comps=True):
    """Exact data on the critical point 0.
    mu      : local Milnor number (Singular, local ordering ds); None if infinite (then 0 is not isolated over C)
    cert    : 0 is an isolated real critical point, certified by saturation w.r.t. a positive definite quadric p
    comps   : minimal associated primes of J (Singular, GTZ; only with a time limit, informative)"""
    J = grad(U)
    mu = sing.local_milnor(U)
    cert, p = real_isolation_cert(J)
    comps = []
    if with_comps:
        try:
            comps = sing.min_ass(J, timeout=12)
        except Exception as e:
            comps = ['(primary decomposition skipped: %s)' % type(e).__name__]
    return dict(mu=None if mu < 0 else mu, cert=cert, p=str(p), comps=comps, complex_isolated=(mu >= 0))


# ------------------------------------------------------------------ Newton facets, quasi-homogeneity
def exps(U):
    return [m for m, c in sp.Poly(sp.expand(U), *X).terms()]


def weights_for(U):
    """exact weights a>0 (rational), d with a.e = d for all exponents e of U; None if U is not quasi-homogeneous"""
    E = exps(U)
    A = sp.Matrix([list(e) + [-1] for e in E])
    ns = A.nullspace()
    if not ns:
        return None
    # find positive combination of nullspace vectors with a_i>0, d>0
    from scipy.optimize import linprog
    B = np.array([[float(v[i]) for v in ns] for i in range(4)])   # 4 x k
    k = B.shape[1]
    res = linprog(c=np.zeros(k), A_ub=-B[:3], b_ub=-np.ones(3), bounds=[(None, None)] * k)
    if not res.success:
        return None
    coef = [sp.nsimplify(float(c), rational=True, tolerance=1e-6) for c in res.x]
    vec = sum((c * v for c, v in zip(coef, ns)), sp.zeros(4, 1))
    a = [vec[i] for i in range(3)]
    if any(ai <= 0 for ai in a):
        return None
    den = sp.ilcm(1, 1, *[sp.Rational(ai).q for ai in a])
    a = [sp.Rational(ai) * den for ai in a]
    g = sp.igcd(0, 0, *[int(ai) for ai in a])
    a = [int(ai) // g for ai in a]
    d = sum(ai * ei for ai, ei in zip(a, E[0]))
    assert all(sum(ai * ei for ai, ei in zip(a, e)) == d for e in E)
    return tuple(a), d


def newton_facets(U):
    """compact facets of the Newton polyhedron: list of (a, d, face_monomials, tail_monomials)"""
    from scipy.spatial import ConvexHull
    E = np.array(exps(U), float)
    big = 100.0
    pts = np.vstack([E] + [E + big * np.eye(3)[i] for i in range(3)])
    hull = ConvexHull(pts)
    out, seen = [], set()
    for eq in hull.equations:
        nrm = eq[:3]
        if np.all(nrm < -1e-9):
            # exact normal from the points on the facet
            on = [tuple(int(v) for v in e) for e in E if abs(float(eq[:3] @ e + eq[3])) < 1e-7]
            M = sp.Matrix([list(p) + [-1] for p in on])
            ns = M.nullspace()
            if len(ns) != 1:
                continue
            v = ns[0]
            den = sp.ilcm(1, 1, *[sp.Rational(vi).q for vi in v]); v = [sp.Rational(vi) * den for vi in v]
            a = [int(abs(vi)) for vi in v[:3]]
            if not all(vi > 0 for vi in (v[0], v[1], v[2])) and not all(vi < 0 for vi in (v[0], v[1], v[2])):
                continue
            g = sp.igcd(0, 0, *a); a = tuple(ai // g for ai in a)
            d = sum(ai * ei for ai, ei in zip(a, on[0]))
            if (a, d) in seen:
                continue
            seen.add((a, d))
            allm = [tuple(int(v) for v in e) for e in E]
            face = [e for e in allm if sum(ai * ei for ai, ei in zip(a, e)) == d]
            tail = [e for e in allm if sum(ai * ei for ai, ei in zip(a, e)) > d]
            out.append((a, d, face, tail))
    return out


def poly_from_monomials(U, mons):
    Pl = sp.Poly(sp.expand(U), *X)
    return sum(Pl.coeff_monomial(m) * x**m[0] * y**m[1] * z**m[2] for m in mons)


def no_real_critical_points(f, weights=None):
    """f: (quasi-)homogeneous polynomial.  Exact certificate that grad f != 0 at all real q != 0.
    Method 1: saturation by a positive definite quadric (as for isolation).  Method 2 (needs weights a of f): critical
    points form a set invariant under the weighted scaling, so real nonzero critical points exist iff
    V(grad f) meets the weighted sphere {p_w = 1}, p_w = sum x_i^(2L/a_i) positive definite; if V(grad f, p_w - 1) is
    zero-dimensional its real points are computed exactly (Singular + sympy).  Returns (status, how) with status
    'none' (certified), 'exist' (a real critical point q != 0 found, exact) or 'unknown'."""
    import criteria as cr
    J = grad(f)
    ok, p = real_isolation_cert(J)
    if ok:
        return 'none', f'saturation by {p}'
    # Method 2: V(grad f) is invariant under the weighted scaling (f quasi-homogeneous), so a real critical point q != 0
    # can be scaled to have its LAST nonzero coordinate (in the order z, y, x) equal to +-1.
    found, unknown = [], False
    cases = []
    for s_ in (1, -1):
        cases.append(({z: s_}, [x, y]))
        cases.append(({z: 0, y: s_}, [x]))
        cases.append(({z: 0, y: 0, x: s_}, []))
    for sub, free in cases:
        eqs = [sp.expand(g.subs(sub)) for g in J]
        if not free:
            if all(e == 0 for e in eqs):
                found.append(tuple(sub.get(v, 0) for v in X))
            continue
        try:
            kind, sols, fam = cr.real_solutions(eqs, free)
        except Exception as e:
            unknown = True
            continue
        if kind == 'none':
            continue
        if kind == 'finite':
            for s in sols:
                pt = dict(sub); pt.update(dict(zip(free, s)))
                found.append(tuple(pt.get(v, 0) for v in X))
            continue
        unknown = True
    if found:
        return 'exist', f'real critical point(s) q != 0 (exact, after weighted scaling): {[tuple(sp.N(t, 6) for t in p) for p in found[:3]]}'
    if unknown:
        return 'unknown', 'chart equations not zero-dimensional or solver failed'
    return 'none', 'weighted-scaling charts z=+-1 / (z=0,y=+-1) / (z=y=0,x=+-1): no real solution of grad f = 0'


def t6_check(U):
    """Palamodov 2020, Thm 6 as recorded in KNOWN_RESULTS (NOT verified at the source): a compact facet with
    quasi-homogeneous part U_w, no real critical points of U_w off 0, U_w takes negative values, and a tail of
    weighted degree >= d + a_max (strong reading, safe) or >= d + a_min (weak reading)."""
    res = []
    for a, d, face, tail in newton_facets(U):
        Uw = poly_from_monomials(U, face)
        crit_status, how = no_real_critical_points(Uw, a)
        nocrit = crit_status == 'none'
        neg = any_negative_value(Uw, 8)
        dt = min([sum(ai * ei for ai, ei in zip(a, e)) for e in tail], default=None)
        strong = dt is None or dt >= d + max(a)
        weak = dt is None or dt >= d + min(a)
        res.append(dict(weights=a, d=d, nface=len(face), tail_min=dt, nocrit=nocrit, crit_status=crit_status, how=how,
                        negative=neg is not None, strong=bool(strong), weak=bool(weak),
                        Uw=str(Uw)))
    return res


# ------------------------------------------------------------------ rational points on a conic (cone)
def conic_rational_param(Qf, P0):
    """homogeneous rational parametrisation (X(t),Y(t),Z(t)) of the projective conic Qf=0 through the rational
    point P0 (lines through P0)."""
    t = sp.Symbol('t')
    Qm = sp.hessian(Qf, X) / 2
    P0 = sp.Matrix(P0)
    assert sp.expand(sum(Qf.subs({x: P0[0], y: P0[1], z: P0[2]}).expand() for _ in [0])) == 0
    # direction D(t) = D0 + t D1 with D0, D1 completing P0 to a basis
    cands = [sp.Matrix(v) for v in itertools.product([0, 1], repeat=3) if any(v)]
    D = None
    for D0 in cands:
        for D1 in cands:
            if sp.Matrix.hstack(P0, D0, D1).det() != 0:
                D = D0 + t * D1; break
        if D is not None:
            break
    qD = (D.T * Qm * D)[0]; b = (P0.T * Qm * D)[0]
    pt = qD * P0 - 2 * b * D
    return [sp.expand(c) for c in pt], t
