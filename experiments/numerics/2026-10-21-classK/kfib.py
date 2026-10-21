"""kfib.py -- exact (sympy, rational arithmetic) reduction in the normal fibre (Lemma K1 of the gt3-hardcore note).

For a point (ray) p in R^3 with u_m(p)=0, grad u_m(p)=0 and normal directions nu_1..nu_r (spanning a complement
of span(p, T_p Sigma), i.e. N_omega) we compute the formal series
    phi(s,Y) = sum_{k>=m} s^{k-m} u_k(p + sum_a Y_a nu_a),
    y*(s)    = the critical point in Y  (series, y*(0)=0),
    R(s)     = phi(s, y*(s)) = sum_{i>=1} s^i g^p_{m+i}.
Scaling: p = lam*omega with |omega|=1  =>  g_k(omega) = g^p_k / lam^k  (see README, section 'Method').
R (value at critical point) does not depend on the scale/basis of nu, only on the line p+N.
"""
import sympy as sp

x, y, z = sp.symbols('x y z')
X = (x, y, z)


def homog_parts(U):
    Pl = sp.Poly(sp.expand(U), *X)
    d = {}
    for mon, c in Pl.terms():
        k = sum(mon)
        d[k] = d.get(k, 0) + c * x**mon[0] * y**mon[1] * z**mon[2]
    return {k: sp.expand(v) for k, v in sorted(d.items()) if sp.expand(v) != 0}


# ---- truncated power series in s: python lists of sympy expressions, length K+1
def smul(a, b, K, simp):
    out = [0]*(K+1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b):
            if i+j > K:
                break
            if bj == 0:
                continue
            out[i+j] += ai*bj
    return [simp(c) for c in out]


def sadd(a, b):
    return [u+v for u, v in zip(a, b)]


def fibre(U, m, p, nus, K, simp=sp.cancel):
    """returns dict with 'g' = {k: g^p_k}, 'ystar' = list of series (one per nu), 'H' matrix.
    K = number of orders above m that are computed (g_{m+1..m+K})."""
    r = len(nus)
    Y = sp.symbols('Y0:%d' % r) if r > 0 else ()
    parts = homog_parts(U)
    w = [p[i] + sum(Y[a]*nus[a][i] for a in range(r)) for i in range(3)]
    # phi as dict: monomial exponent tuple in Y -> series list (length K+1)
    phi = {}
    for k, uk in parts.items():
        i = k - m
        if i < 0 or i > K:
            continue
        e = sp.expand(uk.subs({x: w[0], y: w[1], z: w[2]}, simultaneous=True))
        if r == 0:
            terms = {(): e}
        else:
            P = sp.Poly(e, *Y)
            terms = {mon: c for mon, c in P.terms()}
        for mon, c in terms.items():
            ser = phi.setdefault(mon, [0]*(K+1))
            ser[i] = simp(ser[i] + c)
    zero = tuple([0]*r)
    # H = Hessian in Y at s=0, Y=0 : coefficients of s^0
    H = sp.zeros(r, r)
    for a in range(r):
        for b in range(r):
            mon = [0]*r
            mon[a] += 1
            mon[b] += 1
            c = phi.get(tuple(mon), [0]*(K+1))[0]
            H[a, b] = simp(c*(2 if a == b else 1))
    # check zero-order: phi(0,0)=u_m(p) = 0, grad = 0
    assert simp(phi.get(zero, [0]*(K+1))[0]) == 0, 'u_m(p) != 0'
    for a in range(r):
        mon = [0]*r
        mon[a] = 1
        assert simp(phi.get(tuple(mon), [0]*(K+1))[0]) == 0, 'grad u_m(p) != 0'
    if r == 0:
        R = phi.get(zero, [0]*(K+1))
        return dict(g={m+i: R[i] for i in range(1, K+1)}, ystar=[], H=H)
    Hinv = H.inv() if r > 1 else sp.Matrix([[1/H[0, 0]]])
    Hinv = Hinv.applyfunc(simp)
    # Newton iteration for y*(s)
    ys = [[0]*(K+1) for _ in range(r)]
    one = [1] + [0]*K

    def powers(ser, maxd):
        out = [one]
        for _ in range(maxd):
            out.append(smul(out[-1], ser, K, simp))
        return out
    maxdeg = max(sum(mon) for mon in phi)
    for _ in range(K+1):
        pw = [powers(ys[a], maxdeg) for a in range(r)]
        grad = [[0]*(K+1) for _ in range(r)]
        for mon, ser in phi.items():
            # value of monomial at y(s)
            val = one
            for a in range(r):
                if mon[a]:
                    val = smul(val, pw[a][mon[a]], K, simp)
            base = smul(ser, val, K, simp)  # coefficient * monomial; derivative needs mon[a] * mon/Y_a
            for a in range(r):
                if mon[a]:
                    mon2 = list(mon)
                    mon2[a] -= 1
                    val2 = one
                    for b in range(r):
                        if mon2[b]:
                            val2 = smul(val2, pw[b][mon2[b]], K, simp)
                    t = smul(ser, val2, K, simp)
                    grad[a] = sadd(grad[a], [mon[a]*c for c in t])
        new = []
        for a in range(r):
            upd = [0]*(K+1)
            for b in range(r):
                upd = sadd(upd, [Hinv[a, b]*c for c in grad[b]])
            new.append([simp(ys[a][i] - upd[i]) for i in range(K+1)])
        ys = new
    # check: gradient vanishes to order K
    pw = [powers(ys[a], maxdeg) for a in range(r)]
    # R
    R = [0]*(K+1)
    for mon, ser in phi.items():
        val = one
        for a in range(r):
            if mon[a]:
                val = smul(val, pw[a][mon[a]], K, simp)
        R = sadd(R, smul(ser, val, K, simp))
    R = [simp(c) for c in R]
    return dict(g={m+i: R[i] for i in range(1, K+1)}, ystar=ys, H=H, R0=R[0])
