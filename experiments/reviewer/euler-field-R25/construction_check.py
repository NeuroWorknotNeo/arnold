"""R25: independent implementation of the field of Theorem E (notes/prover/2026-10-21-euler-field.md)
and numerical check of  min xi.grad Q / Q  and  max |grad c|  on new examples.
[Эксперимент] mpmath, dps=120. Not a proof.

Q must be a polynomial monic in b2 (so the Weierstrass unit u == 1 near 0 and P == Q).
Roots phi_j(b1) of Q(b1, .) found by mpmath.polyroots; phi', phi'' by implicit differentiation.
c = sum_j w_j chi_j, chi_j = b1 psi_j' - psi_j, w_j = p_j^{-N}/sum p_k^{-N}, p_j = |b2 - phi_j|^2.
grad c computed analytically (formulas of step 7) and checked by central differences.
"""
import sys
import mpmath as mp
import sympy as sp

mp.mp.dps = 250
B1, B2 = sp.symbols('b1 b2')


def prepare(factors):
    """factors: list of sympy polynomials in (b1,b2), each monic in b2; Q = product."""
    facs = []
    d = 0
    for Fe in factors:
        Fp = sp.Poly(sp.expand(Fe), B2)
        assert Fp.LC() == 1, "factor must be monic in b2"
        d += Fp.degree()
        coeffs = [sp.lambdify(B1, c, 'mpmath') for c in Fp.all_coeffs()]
        F = sp.expand(Fe)
        der = {}
        for name, e in [('F', F), ('F1', sp.diff(F, B1)), ('F2', sp.diff(F, B2)),
                        ('F11', sp.diff(F, B1, 2)), ('F12', sp.diff(F, B1, B2)), ('F22', sp.diff(F, B2, 2))]:
            der[name] = sp.lambdify((B1, B2), e, 'mpmath')
        facs.append((coeffs, der))
    return d, facs, facs


def roots_data(b1, d, facs, _unused):
    out = []
    for coeffs, der in facs:
        cs = [mp.mpf(1)] + [c(b1) for c in coeffs[1:]]
        rts = mp.polyroots(cs, maxsteps=4000, extraprec=2000)
        for r in rts:
            F1 = der['F1'](b1, r); F2 = der['F2'](b1, r)
            p1 = -F1/F2
            F11 = der['F11'](b1, r); F12 = der['F12'](b1, r); F22 = der['F22'](b1, r)
            p2 = -(F11 + 2*F12*p1 + F22*p1**2)/F2
            out.append((r, p1, p2))
    assert len(out) == d
    return out


def field(b1, b2, N, rd):
    """return c, grad c (analytic) at (b1, b2)."""
    ps, chis, dchis, gps = [], [], [], []
    for (r, p1, p2) in rd:
        psi, eta = mp.re(r), mp.im(r)
        dpsi, deta = mp.re(p1), mp.im(p1)
        ddpsi = mp.re(p2)
        p = (b2 - psi)**2 + eta**2
        ps.append(p)
        chis.append(b1*dpsi - psi)
        dchis.append(b1*ddpsi)                    # chi' = b1 psi''
        gps.append((-2*(b2 - psi)*dpsi + 2*eta*deta, 2*(b2 - psi)))
    pmin = min(ps)
    q = [(pmin/p)**N for p in ps]
    S = sum(q)
    w = [qi/S for qi in q]
    c = sum(wi*ch for wi, ch in zip(w, chis))
    # grad w_j = N w_j (-grad p_j/p_j + sum_k w_k grad p_k/p_k)
    avg = [sum(w[k_]*gps[k_][a]/ps[k_] for k_ in range(len(ps))) for a in range(2)]
    gc = [mp.mpf(0), mp.mpf(0)]
    gc[0] = sum(wi*dc for wi, dc in zip(w, dchis))
    for j in range(len(ps)):
        for a in range(2):
            gwj = N*w[j]*(-gps[j][a]/ps[j] + avg[a])
            gc[a] += chis[j]*gwj
    return c, gc, w, ps


def xi_logQ(b1, b2, c, facs):
    s = mp.mpf(0)
    for _, der in facs:
        F = der['F'](b1, b2); F1 = der['F1'](b1, b2); F2 = der['F2'](b1, b2)
        s += (b1*F1 + (b2 + c)*F2)/F
    return s


def sample_b2(rd, b1):
    psis = sorted(set([mp.re(r) for (r, _, _) in rd]))
    etas = [abs(mp.im(r)) for (r, _, _) in rd]
    pts = []
    for (r, _, _) in rd:
        psi, eta = mp.re(r), abs(mp.im(r))
        for s in [mp.mpf(10)**(e/4) for e in range(-16, 17)]:
            pts += [psi + s*eta, psi - s*eta]
        pts.append(psi)
    for i in range(len(psis)):
        for j in range(i+1, len(psis)):
            a, b = psis[i], psis[j]
            for tt in [mp.mpf(k_)/20 for k_ in range(1, 20)]:
                pts.append(a + tt*(b - a))
    # Voronoi boundaries p_i = p_j (real b2): (b2-psi_i)^2+eta_i^2=(b2-psi_j)^2+eta_j^2
    R = [(mp.re(r), mp.im(r)**2) for (r, _, _) in rd]
    for i in range(len(R)):
        for j in range(i+1, len(R)):
            (pi, ei), (pj, ej) = R[i], R[j]
            if pi != pj:
                bnd = (pj**2 - pi**2 + ej - ei)/(2*(pj - pi))
                for dd in [0, 1e-3, -1e-3]:
                    pts.append(bnd + dd*abs(pj - pi))
    L = 3*max(abs(b1), max(abs(p) for p in psis))
    pts += [L*mp.mpf(k_)/40 for k_ in range(-40, 41)]
    pts += [s*abs(b1)**e for s in (1, -1) for e in (mp.mpf(1)/2, mp.mpf(1)/4)]
    return pts


def run(name, Qexpr, N, b1list, fdcheck=True):
    d, coeffs, der = prepare(Qexpr)
    print(f"--- {name}: d={d}, N={N}")
    worst = []
    for b1 in b1list:
        b1 = mp.mpf(b1)
        rd = roots_data(b1, d, coeffs, der)
        mn, mx, arg_mn, arg_mx = mp.inf, 0, None, None
        for b2 in sample_b2(rd, b1):
            c, gc, w, ps = field(b1, b2, N, rd)
            v = xi_logQ(b1, b2, c, der)
            g = mp.sqrt(gc[0]**2 + gc[1]**2)
            if v < mn:
                mn, arg_mn = v, b2
            if g > mx:
                mx, arg_mx = g, b2
        # finite-difference check of grad c at arg_mx
        fd = ''
        if fdcheck:
            h = abs(b1)*mp.mpf(10)**-30
            b2 = arg_mx
            cp = field(b1 + h, b2, N, roots_data(b1 + h, d, coeffs, der))[0]
            cm = field(b1 - h, b2, N, roots_data(b1 - h, d, coeffs, der))[0]
            c0, gc, _, _ = field(b1, b2, N, rd)
            hh = h
            cp2 = field(b1, b2 + hh, N, rd)[0]; cm2 = field(b1, b2 - hh, N, rd)[0]
            err = max(abs((cp - cm)/(2*h) - gc[0]), abs((cp2 - cm2)/(2*hh) - gc[1]))
            fd = f" fd-err={mp.nstr(err, 3)}"
        print(f"b1={mp.nstr(b1, 3):>9}  min xi.logQ={mp.nstr(mn, 6):>10} (b2={mp.nstr(arg_mn, 4)})"
              f"  max|grad c|={mp.nstr(mx, 6):>10} (b2={mp.nstr(arg_mx, 4)}){fd}")
        worst.append((mn, mx))
    print(f"    overall: min xi.logQ = {mp.nstr(min(a for a, _ in worst), 6)}, max|grad c| = {mp.nstr(max(b for _, b in worst), 6)}")
    return worst


if __name__ == '__main__':
    b1 = B1; b2 = B2
    sc = [10**(-e/2) for e in range(3, 13)]
    b1list = sc + [-s for s in sc]
    examples = {
        # three close pairs: real parts differ at order b1^3, imag parts b1^5
        'T1 three close pairs': [(b2 - b1**2 - i*b1**3)**2 + b1**10 for i in range(3)],
        # nested tree, different contact orders 1,2,3, imag parts of different orders
        'T2 nested tree': [(b2 - b1)**2 + b1**4, (b2 - b1 - b1**2)**2 + b1**6,
                           (b2 - b1 - b1**2 - b1**3)**2 + b1**8, (b2 - b1 - b1**2 + b1**3)**2 + b1**12],
        # fractional Puiseux exponents, different behaviour for b1<0 and b1>0
        'T3 Puiseux 5/2': [((b2 - b1**2)**2 - b1**5)**2 + b1**14],
        # four pairs, same real part up to b1^4, very thin (E large)
        'T4 four pairs': [(b2 - b1**2 - i*b1**4)**2 + b1**12 for i in range(-1, 3)],
        # one pair very thin (imag b1^10) far from another (E large)
        'T5 thin + fat': [(b2 - b1**2)**2 + b1**20, (b2 + b1)**2 + b1**2],
        # two Puiseux-type factors + a pair with half-integer imaginary order + a far pair
        'T6 two Puiseux': [((b2 - b1**2)**2 - b1**5)**2 + b1**14, (b2 - b1**2 - b1**3)**2 + b1**8,
                           ((b2 - b1**2 + b1**3)**2 + b1**7)**2 + b1**30, (b2 + b1)**2 + b1**2],
    }
    which = sys.argv[1:] or list(examples)
    for name in which:
        Q = examples[name]
        # N: a small value and the value required by the theorem, 2N-1 >= 4 d (E-1) (E computed by hand)
        Nth = {'T1 three close pairs': 49, 'T2 nested tree': 81, 'T3 Puiseux 5/2': 29,
               'T4 four pairs': 81, 'T5 thin + fat': 73, 'T6 two Puiseux': 85}[name]
        for N in [2, 8, Nth]:
            run(name, Q, N, b1list, fdcheck=True)
