#!/usr/bin/env python3
"""
sieve.py -- prototype "sieve" for Arnold's problem 1971-4 in R^3.

Input : a polynomial U(x,y,z) with U(0)=0, grad U(0)=0.
Output: a verdict with a reason:
  UNSTABLE / TOTALLY_UNSTABLE  -- covered by a known (or proved in our notes) criterion,
  MIN                          -- numerically looks like a (strict) minimum: not part of problem 1971-4,
  NONISOLATED                  -- critical point at 0 looks non-isolated: outside problem 1971-4,
  SUSPICIOUS                   -- not covered by any implemented criterion (with the reason).

The criteria are tried in order of cost.  Labels in brackets say what each one rests on:
  [Lyapunov]  linear instability;
  [KP82]      Kozlov--Palamodov 1982: first nonzero form takes negative values;
  [Pa20-T3]   Palamodov 2020, Thm 3: first form has no critical points except 0 (total instability);
  [Pa20-T5]   Palamodov 2020, Thm 5: corank-1 Hessian (reduction to the kernel);
  [Ko86]      Kozlov 1986 (Thm 4 in Pa20): u2>=0, u_m has no minimum on ker u2;
  [Pa20-T6]   Palamodov 2020, Thm 6: quasi-homogeneous facet without critical points + small tail;
  [Bu25]      Burgos 2025, Cor. 1.4: second form < 0 on the zero set of the first one;
  [N13]       note "Example 13", Prop. 1: circular gutter with regular effective potential (proved);
  [N13*]      the same virial argument for a general Morse-Bott gutter / point-horn (proof sketched only);
  [SYM]       an isometric symmetry with an invariant line/plane where U has no minimum (n=1 or n=2 theorem).
Everything numerical is heuristic (sampling + local optimisation); a rigorous version would replace
it by exact algebra (Groebner bases, Sturm sequences) or interval arithmetic.
"""
import itertools, math
import numpy as np
import sympy as sp

x, y, z = sp.symbols('x y z', real=True)
X = (x, y, z)
TOL = 1e-9          # relative tolerance for "zero" on the unit sphere

# ----------------------------------------------------------------------------- utilities
def homog_parts(expr):
    P = sp.Poly(sp.expand(expr), *X)
    parts = {}
    for mon, c in P.terms():
        k = sum(mon)
        parts[k] = parts.get(k, 0) + c * x**mon[0] * y**mon[1] * z**mon[2]
    return {k: sp.expand(v) for k, v in sorted(parts.items()) if sp.expand(v) != 0}

def lam(expr):
    f = sp.lambdify(X, expr, 'numpy')
    def g(P):
        P = np.asarray(P, float)
        r = f(P[..., 0], P[..., 1], P[..., 2])
        return np.broadcast_to(np.asarray(r, float), P.shape[:-1]).copy()
    return g

def lam_grad(expr):
    fs = [lam(sp.diff(expr, v)) for v in X]
    return lambda P: np.stack([f(P) for f in fs], axis=-1)

def lam_hess(expr):
    fs = [[lam(sp.diff(expr, a, b)) for b in X] for a in X]
    return lambda P: np.stack([np.stack([fs[i][j](P) for j in range(3)], -1) for i in range(3)], -2)

def fib_sphere(n):
    i = np.arange(n) + 0.5
    ph = np.arccos(1 - 2 * i / n); th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(ph), np.sin(th) * np.sin(ph), np.cos(ph)], -1)

SPH = fib_sphere(20000)

def tangential(G, U):
    return G - np.sum(G * U, -1, keepdims=True) * U

def sphere_minimize(f, g, starts, iters=300):
    """normalized projected gradient descent with adaptive steps on S^2"""
    U = np.array(starts, float); val = f(U); step = np.full(len(U), 0.05)
    for _ in range(iters):
        G = tangential(g(U), U); nG = np.linalg.norm(G, axis=-1)
        cand = U - step[:, None] * G / np.maximum(nG, 1e-300)[:, None]
        cand /= np.linalg.norm(cand, axis=-1, keepdims=True)
        cv = f(cand); better = cv < val
        U[better] = cand[better]; val[better] = cv[better]
        step = np.where(better, step * 1.3, step * 0.5)
        if np.all(step < 1e-13): break
    return U, val

def form_min(expr, nstart=80):
    f, g = lam(expr), lam_grad(expr)
    v = f(SPH); idx = np.argsort(v)[:nstart]
    U, val = sphere_minimize(f, g, SPH[idx])
    i = np.argmin(val)
    return float(val[i]), U[i], float(np.max(np.abs(v)))

def tangent_basis(u):
    a = np.array([1.0, 0, 0]) if abs(u[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = a - (a @ u) * u; e1 /= np.linalg.norm(e1); e2 = np.cross(u, e1)
    return e1, e2

def signed_permutations():
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            S = np.zeros((3, 3), int)
            for i in range(3): S[i, perm[i]] = signs[i]
            if not np.array_equal(S, np.eye(3, dtype=int)):
                yield S

# ----------------------------------------------------------------------------- numerical sanity tests
def negative_points(Uexpr, radii=(0.1, 0.03, 0.01)):
    """search for q with U(q)<0 on small spheres (returns list of points)"""
    f, g = lam(Uexpr), lam_grad(Uexpr); found = []
    for r in radii:
        F = lambda W: f(r * W); Gf = lambda W: r * g(r * W)
        v = F(SPH); idx = np.argsort(v)[:40]
        W, val = sphere_minimize(F, Gf, SPH[idx], iters=200)
        if val.min() < 0: found.append(r * W[np.argmin(val)])
    return found

def isolated_check(Uexpr, radii=(0.1, 0.05, 0.02)):
    """heuristic: min |grad U| / max |grad U| on small spheres.  For an isolated critical point the
    ratio decays only polynomially in r (Lojasiewicz); for a critical curve it is ~ rounding noise
    at every radius.  Returns the largest of the ratios over the radii."""
    g, H = lam_grad(Uexpr), lam_hess(Uexpr); ratios = []
    for r in radii:
        F = lambda W: np.sum(g(r * W) ** 2, -1)
        Gf = lambda W: 2 * r * np.einsum('...ij,...j->...i', H(r * W), g(r * W))
        v = F(SPH); idx = np.argsort(v)[:40]
        W, val = sphere_minimize(F, Gf, SPH[idx], iters=300)
        ratios.append(math.sqrt(max(val.min(), 0)) / math.sqrt(v.max()))
    return max(ratios)

# ----------------------------------------------------------------------------- reduction to the Hessian kernel
def reduced_potential(Uexpr, K, C, A, D):
    """splitting lemma by fixed-point iteration on power series (floats).
    K: kernel basis (3 x kdim), C: complement basis (3 x cdim), A: Hessian block on C.
    returns (t symbols, reduced potential truncated at degree D)"""
    kdim, cdim = K.shape[1], C.shape[1]
    ts = sp.symbols('t1:%d' % (kdim + 1)); ys = sp.symbols('y1:%d' % (cdim + 1))
    q = sp.Matrix(K) * sp.Matrix(ts) + sp.Matrix(C) * sp.Matrix(ys)
    Uq = sp.expand(Uexpr.subs({x: q[0], y: q[1], z: q[2]}, simultaneous=True))
    dU = [sp.diff(Uq, yy) for yy in ys]
    Ainv = np.linalg.inv(A)
    def trunc(e, deg):
        P = sp.Poly(sp.expand(e), *ts)
        return sum((c * sp.prod([t ** k for t, k in zip(ts, mon)]) for mon, c in P.terms()
                    if sum(mon) <= deg and abs(float(c)) > 1e-12), sp.Integer(0))
    Y = [sp.Integer(0)] * cdim
    for _ in range(D):
        vals = [trunc(d.subs(dict(zip(ys, Y))), D) for d in dU]
        Y = [trunc(Y[i] - sum(Ainv[i, j] * vals[j] for j in range(cdim)), D) for i in range(cdim)]
    u = trunc(Uq.subs(dict(zip(ys, Y))), D)
    return ts, u

# ----------------------------------------------------------------------------- Palamodov Thm 6 (Newton facets)
def newton_facets(Uexpr):
    from scipy.spatial import ConvexHull
    P = sp.Poly(sp.expand(Uexpr), *X); mons = np.array([m for m, c in P.terms()], float)
    coeffs = {m: c for m, c in P.terms()}
    pts = [mons] + [mons + 50 * np.eye(3)[i] for i in range(3)]
    hull = ConvexHull(np.vstack(pts))
    out = []
    for eq in np.unique(np.round(hull.equations, 9), axis=0):
        nrm, off = eq[:3], eq[3]
        if np.all(nrm < -1e-9):
            a = -nrm / np.min(-nrm)
            fr = [sp.Rational(v).limit_denominator(50) for v in a]
            den = sp.ilcm(*[f.q for f in fr]); a = np.array([int(f * den) for f in fr])
            dvals = mons @ a; d = dvals.min()
            face = [tuple(int(v) for v in m) for m in mons[np.isclose(dvals, d)]]
            tail = [tuple(int(v) for v in m) for m in mons[~np.isclose(dvals, d)]]
            out.append((a, int(round(d)), face, tail, coeffs))
    return out

def check_palamodov_T6(Uexpr):
    for a, d, face, tail, coeffs in newton_facets(Uexpr):
        u = sum(coeffs[m] * x**m[0] * y**m[1] * z**m[2] for m in face)
        if any(np.dot(a, b) < d + a.max() for b in tail):
            continue
        gnorm = lam(sp.sqrt(sum(sp.diff(u, v) ** 2 for v in X)))
        if np.min(gnorm(SPH)) < 1e-6 * np.max(gnorm(SPH)):
            continue
        umin, _, usc = form_min(u)
        if umin < -TOL * usc:
            return True, 'weights %s, face degree %d' % (tuple(int(v) for v in a), d)
    return False, ''

# ----------------------------------------------------------------------------- gutters and point-horns
def project_to_curve(f, g, u, sc):
    for _ in range(40):
        G = g(u[None])[0]; Gs = G - (G @ u) * u; n2 = Gs @ Gs
        if n2 < 1e-30: break
        u = u - f(u[None])[0] * Gs / n2; u /= np.linalg.norm(u)
        if abs(f(u[None])[0]) < 1e-14 * sc: break
    return u

def trace_zero_curves(fexpr, h=0.01):
    f, g = lam(fexpr), lam_grad(fexpr)
    vals = f(SPH); sc = np.max(np.abs(vals))
    seeds = SPH[np.abs(vals) < 0.03 * sc]; used = np.zeros(len(seeds), bool); comps = []
    for i in range(len(seeds)):
        if used[i]: continue
        u0 = project_to_curve(f, g, seeds[i].copy(), sc); pts = [u0]; u = u0.copy(); tprev = None
        for step in range(int(8 * np.pi / h)):
            G = g(u[None])[0]; Gs = G - (G @ u) * u
            t = np.cross(u, Gs); nt = np.linalg.norm(t)
            if nt < 1e-12: break
            t /= nt
            if tprev is not None and t @ tprev < 0: t = -t
            tprev = t
            u = project_to_curve(f, g, (u + h * t) / np.linalg.norm(u + h * t), sc); pts.append(u)
            if step > 20 and np.linalg.norm(u - u0) < 0.6 * h: break
        pts = np.array(pts)
        dmin = np.min(np.linalg.norm(seeds[:, None, :] - pts[None, ::3, :], axis=-1), axis=1)
        used |= dmin < 4 * h
        comps.append(pts)
    return comps

def regular_value_check(G, pts):
    """G: values along a closed curve (points pts).  Returns (ok, has_negative, kind).
    ok=False if G vanishes identically, has a touching zero (local extremum at level ~0, even order)
    or a sign change with vanishing slope (odd order >= 3)."""
    n = len(G); Gmax = np.max(np.abs(G))
    if Gmax < 1e-7: return False, False, 'vanishes identically'
    ds = np.linalg.norm(np.roll(pts, -1, axis=0) - pts, axis=-1); ds[ds == 0] = 1e-12
    slope = (np.roll(G, -1) - G) / ds; Smax = np.max(np.abs(slope))
    for i in range(n):
        gm, g0, gp = G[i - 1], G[i], G[(i + 1) % n]
        if (g0 - gm) * (gp - g0) <= 0:                      # discrete extremum
            a = (gp - 2 * g0 + gm) / 2; b = (gp - gm) / 2
            ext = g0 - b * b / (4 * a) if abs(a) > 1e-300 else g0
            if abs(ext) < 1e-6 * Gmax:
                return False, bool(np.any(G < 0)), 'touching (even-order) zero'
        if g0 * gp < 0 and abs(slope[i]) < 1e-3 * Smax:   # sign change with tiny slope
            return False, True, 'sign change at a multiple (odd-order) zero'
    return True, bool(np.any(G < 0)), ''

def hard_core(parts, k, D):
    """U_k >= 0 with zeros on S^2.  Returns (horns_covered, degenerate_reasons, notes, zero_points)."""
    Uk = parts[k]; fk, gk, Hk = lam(Uk), lam_grad(Uk), lam_hess(Uk)
    sc_k = np.max(np.abs(fk(SPH)))
    higher = [j for j in parts if j > k]
    F = {j: lam(parts[j]) for j in higher}; Gr = {j: lam_grad(parts[j]) for j in higher}
    covered, degenerate, notes, zero_pts = [], [], [], []
    const, facs = sp.factor_list(Uk, *X)
    curves = []
    for fac, e in facs:
        if sp.Poly(fac, *X).total_degree() == 0: continue
        vals = lam(fac)(SPH)
        if vals.min() < -1e-9 * np.abs(vals).max() and vals.max() > 1e-9 * np.abs(vals).max():
            curves.append((fac, e))
    # ---- gutters
    for fac, e in curves:
        comps = trace_zero_curves(fac)
        cof = sp.cancel(Uk / fac ** e); fcof = lam(cof); gf = lam_grad(fac)
        for pts in comps:
            zero_pts.extend(list(pts[::5]))
            if e != 2:
                degenerate.append('gutter {%s=0} of multiplicity %d (non-Morse-Bott)' % (fac, e)); continue
            Gs = tangential(gf(pts), pts); ng = np.linalg.norm(Gs, axis=-1)
            if ng.min() < 1e-6 * ng.max():
                degenerate.append('singular gutter {%s=0}' % fac); continue
            if fcof(pts).min() <= 1e-9 * sc_k:
                degenerate.append('gutter {%s=0}: cofactor vanishes on it' % fac); continue
            nrm = Gs / ng[:, None]
            lamb = np.einsum('ni,nij,nj->n', nrm, Hk(pts), nrm)
            G = {j: F[j](pts) for j in higher}
            c = {j: np.sum(nrm * Gr[j](pts), -1) for j in higher}
            sc = {j: np.max(np.abs(lam(parts[j])(SPH))) for j in higher}
            m = next((j for j in higher if np.max(np.abs(G[j])) > 1e-8 * sc[j]), None)
            lin = [j for j in higher if (m is None or j < m) and np.max(np.abs(c[j])) > 1e-8 * sc[j]]
            cand = ([m] if m is not None else []) + [2 * j - k for j in lin]
            if not cand:
                degenerate.append('gutter {%s=0}: effective potential vanishes up to degree %d' % (fac, D)); continue
            mstar = min(cand)
            Geff = (G[m] if m == mstar else 0) - sum(c[j] ** 2 / (2 * lamb) for j in lin if 2 * j - k == mstar)
            Geff = np.asarray(Geff, float) * np.ones(len(pts))
            ok, neg, kind = regular_value_check(Geff, pts)
            circ = sp.expand(fac - (x**2 + y**2 - z**2)) == 0 or sp.expand(fac + (x**2 + y**2 - z**2)) == 0
            literal = (circ and k == 4 and sp.Poly(cof, *X).total_degree() == 0 and not lin and m == mstar
                       and all(j >= m for j in higher))
            tag = '[N13]' if literal else '[N13*]'
            if not ok:
                degenerate.append('gutter {%s=0}: effective potential (degree %d): %s' % (fac, mstar, kind))
            elif neg:
                covered.append('%s gutter {%s=0}: effective potential of degree %d has simple zeros and is '
                               'negative somewhere' % (tag, fac, mstar))
            else:
                notes.append('gutter {%s=0}: effective potential > 0 (no horn)' % fac)
    # ---- isolated zeros of U_k (points)
    v = fk(SPH); idx = np.argsort(v)[:400]
    W, val = sphere_minimize(fk, gk, SPH[idx], iters=400)
    cand = W[val < 1e-10 * sc_k]
    pts = []
    for w in cand:
        if zero_pts and np.min(np.linalg.norm(np.array(zero_pts) - w, axis=-1)) < 0.05: continue
        if all(np.linalg.norm(w - p) > 1e-3 for p in pts): pts.append(w)
    for e_ in pts:
        zero_pts.append(e_)
        e1, e2 = tangent_basis(e_); Hm = Hk(e_[None])[0]
        He = np.array([[e1 @ Hm @ e1, e1 @ Hm @ e2], [e2 @ Hm @ e1, e2 @ Hm @ e2]])
        ev = np.linalg.eigvalsh(He)
        if ev.min() < 1e-3 * sc_k:
            degenerate.append('zero direction %s of U_%d with degenerate transverse Hessian' % (np.round(e_, 3), k))
            continue
        Uj = {j: float(F[j](e_[None])[0]) for j in higher}
        gj = {j: np.array([e1 @ Gr[j](e_[None])[0], e2 @ Gr[j](e_[None])[0]]) for j in higher}
        m = next((j for j in higher if abs(Uj[j]) > 1e-9), None)
        lin = [j for j in higher if (m is None or j < m) and np.linalg.norm(gj[j]) > 1e-9]
        cand_m = ([m] if m is not None else []) + [2 * j - k for j in lin]
        if not cand_m:
            degenerate.append('zero direction %s: nothing up to degree %d' % (np.round(e_, 3), D)); continue
        mstar = min(cand_m); Hinv = np.linalg.inv(He)
        cstar = (Uj[m] if m == mstar else 0.0) - sum(0.5 * gj[j] @ Hinv @ gj[j] for j in lin if 2 * j - k == mstar)
        if cstar < -1e-9:
            covered.append('[N13*] point-horn along %s (effective degree %d, coefficient %.3g)'
                           % (np.round(e_, 3), mstar, cstar))
        elif abs(cstar) <= 1e-9:
            degenerate.append('point-horn along %s: effective coefficient vanishes' % np.round(e_, 3))
    return covered, degenerate, notes, zero_pts

def symmetry_reduction(Uexpr):
    for S in signed_permutations():
        Sq = sp.Matrix(S) * sp.Matrix(X)
        if sp.expand(Uexpr.subs({x: Sq[0], y: Sq[1], z: Sq[2]}, simultaneous=True) - Uexpr) != 0:
            continue
        ns = sp.Matrix(S - np.eye(3, dtype=int)).nullspace()
        if len(ns) == 1:
            t = sp.Symbol('t'); v = ns[0]
            ut = sp.Poly(sp.expand(Uexpr.subs({x: t * v[0], y: t * v[1], z: t * v[2]}, simultaneous=True)), t)
            terms = sorted(ut.terms(), key=lambda mc: mc[0][0])
            if terms and (terms[0][0][0] % 2 == 1 or terms[0][1] < 0):
                return True, 'invariant line %s, U restricted to it has no minimum (n=1)' % list(v)
        elif len(ns) == 2:
            a, b = sp.symbols('a b'); v1, v2 = ns
            q = a * v1 + b * v2
            u2 = sp.expand(Uexpr.subs({x: q[0], y: q[1], z: q[2]}, simultaneous=True))
            fu = sp.lambdify((a, b), u2, 'numpy')
            th = np.linspace(0, 2 * np.pi, 20001)
            for r in (0.1, 0.03, 0.01, 0.003):
                if np.min(fu(r * np.cos(th), r * np.sin(th))) < 0:
                    return True, 'invariant plane spanned by %s, %s; U on it is not a minimum (n=2 theorem)' % (
                        list(v1), list(v2))
    return False, ''

# ----------------------------------------------------------------------------- main classifier
def classify(Uexpr, do_symmetry=True):
    Uexpr = sp.expand(sp.sympify(Uexpr, locals={'x': x, 'y': y, 'z': z}))
    parts = homog_parts(Uexpr)
    if 0 in parts or 1 in parts:
        raise ValueError('need U(0)=0 and grad U(0)=0')
    D = max(parts)
    # ---------------- Hessian level
    U2 = parts.get(2, sp.Integer(0))
    H = np.array([[float(sp.diff(U2, a, b)) for b in X] for a in X])
    w, Vv = np.linalg.eigh(H); hs = max(1.0, np.abs(w).max())
    if w.min() < -1e-12 * hs:
        return 'UNSTABLE', '[Lyapunov] Hessian has a negative eigenvalue'
    rank = int(np.sum(w > 1e-12 * hs))
    if rank == 3:
        return 'MIN', 'Hessian positive definite'
    if rank == 2:
        K, C = Vv[:, w <= 1e-12 * hs], Vv[:, w > 1e-12 * hs]
        A = C.T @ H @ C
        ts, u = reduced_potential(Uexpr, K, C, A, D)
        P = sp.Poly(u, *ts); terms = sorted(P.terms(), key=lambda mc: mc[0][0])
        if not terms:
            return 'NONISOLATED', 'reduced 1D potential vanishes up to degree %d (corank 1)' % D
        (deg,), c0 = terms[0]
        if deg % 2 == 1 or float(c0) < 0:
            return 'TOTALLY_UNSTABLE', '[Pa20-T5] corank-1 Hessian, reduced potential ~ %.3g t^%d' % (c0, deg)
        return 'MIN', 'corank-1 Hessian, reduced potential ~ +t^%d' % deg
    if rank == 1:
        K = Vv[:, w <= 1e-12 * hs]; C = Vv[:, w > 1e-12 * hs]
        a, b = sp.symbols('a b')
        q = sp.Matrix(K) * sp.Matrix([a, b])
        for m in sorted(j for j in parts if j >= 3):
            um = sp.expand(parts[m].subs({x: q[0], y: q[1], z: q[2]}, simultaneous=True))
            fu = sp.lambdify((a, b), um, 'numpy'); th = np.linspace(0, 2 * np.pi, 20001)
            vals = fu(np.cos(th), np.sin(th)) * np.ones_like(th)
            if np.max(np.abs(vals)) > 1e-10:
                if vals.min() < -1e-10 * np.max(np.abs(vals)):
                    return 'UNSTABLE', '[Ko86] corank-2 Hessian, U_%d restricted to the kernel takes negative values' % m
                break
        A = C.T @ H @ C
        ts, u = reduced_potential(Uexpr, K, C, A, D)
        up = {}
        for mon, cc in sp.Poly(u, *ts).terms():
            up[sum(mon)] = up.get(sum(mon), 0) + cc * ts[0] ** mon[0] * ts[1] ** mon[1]
        up = {kk: vv for kk, vv in up.items() if abs(float(sp.Poly(vv, *ts).max_norm())) > 1e-10}
        if up:
            kl = min(up); lead = up[kl]
            fl = sp.lambdify(ts, lead, 'numpy'); th = np.linspace(0, 2 * np.pi, 20001)
            vals = fl(np.cos(th), np.sin(th)) * np.ones_like(th)
            gl = sp.lambdify(ts, sp.sqrt(sp.diff(lead, ts[0]) ** 2 + sp.diff(lead, ts[1]) ** 2), 'numpy')
            gv = gl(np.cos(th), np.sin(th)) * np.ones_like(th)
            if vals.min() < 0 and gv.min() > 1e-6 * gv.max():
                return 'TOTALLY_UNSTABLE', '[Pa20-T5] corank-2 Hessian, reduced leading form has no critical points'
        if do_symmetry:
            ok, why = symmetry_reduction(Uexpr)
            if ok: return 'UNSTABLE', '[SYM] ' + why
        return 'SUSPICIOUS', 'corank-2 Hessian with degenerate reduced 2D potential (expected to reduce to n=2, not proved)'
    # ---------------- Hessian = 0: first nonzero form
    k = min(parts)
    if k % 2 == 1:
        return 'UNSTABLE', '[KP82] first nonzero form U_%d has odd degree' % k
    fmin, _, fsc = form_min(parts[k])
    if fmin < -TOL * fsc:
        gnorm = lam(sp.sqrt(sum(sp.diff(parts[k], v) ** 2 for v in X)))
        gv = gnorm(SPH)
        if gv.min() > 1e-6 * gv.max():
            return 'TOTALLY_UNSTABLE', '[Pa20-T3] U_%d takes negative values and has no critical points except 0' % k
        return 'UNSTABLE', '[KP82] first nonzero form U_%d takes negative values' % k
    ok, why = check_palamodov_T6(Uexpr)
    if ok:
        return 'TOTALLY_UNSTABLE', '[Pa20-T6] ' + why
    if fmin > TOL * fsc:
        return 'MIN', 'first nonzero form U_%d is positive definite' % k
    # ---------------- hard core
    covered, degenerate, notes, zero_pts = hard_core(parts, k, D)
    higher = [j for j in parts if j > k]
    if higher and zero_pts:
        l2 = higher[0]; vals = lam(parts[l2])(np.array(zero_pts))
        if np.max(vals) < -1e-9 * np.max(np.abs(lam(parts[l2])(SPH))):
            return 'TOTALLY_UNSTABLE', '[Bu25] U_%d < 0 on the whole zero set of U_%d' % (l2, k)
    covered = list(dict.fromkeys(covered)); degenerate = list(dict.fromkeys(degenerate))
    if covered and not degenerate:
        return 'TOTALLY_UNSTABLE', '; '.join(covered)
    if covered:
        return 'UNSTABLE', '; '.join(covered) + '  (other horns degenerate: ' + '; '.join(degenerate) + ')'
    if do_symmetry:
        ok, why = symmetry_reduction(Uexpr)
        if ok: return 'UNSTABLE', '[SYM] ' + why
    if isolated_check(Uexpr) < 1e-13:
        return 'NONISOLATED', 'critical point at 0 looks non-isolated'
    neg = negative_points(Uexpr)
    if degenerate and neg:
        return 'SUSPICIOUS', '; '.join(degenerate)
    if degenerate:
        return 'UNDECIDED', 'degenerate, but no negative values found (maybe a minimum): ' + '; '.join(degenerate)
    if neg:
        return 'SUSPICIOUS', 'negative values found, but no horn explained at this level'
    return 'MIN', 'no negative horns found (probably a non-strict or strict minimum)'

if __name__ == '__main__':
    import sys
    for s in sys.argv[1:]:
        print(s, '=>', *classify(s))
