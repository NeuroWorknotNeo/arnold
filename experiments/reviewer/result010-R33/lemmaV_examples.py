# R33 [Experiment]: Lemma V of results/010 on explicit examples.
# For each f(s,tau) and a chosen real branch T_i(t) of d_tau f = 0 (s = t^N1), compute
#   v(t)=f(t^N1,T(t)) ~ -a t^G1, nu_k = ord_t a_k(t), A'_*, K_*, Q_V; then check numerically:
#   (1) the global minimiser of f(s,.) on the window is T(s^{1/N1}) (or a tied branch);
#   (2) t^{-G1} f(t^N1, T(t)+t^{A'} b) -> -a + Q_V(b);  (3) Q_V >= 0, lowest degree even, coeff > 0.
import sympy as sp, numpy as np
from fractions import Fraction
t, tp, b = sp.symbols('t tau_p b', real=True)
s, tau = sp.symbols('s tau', real=True)

def analyse(name, f, N1, T, tau0=0.5, order=14):
    ft = sp.expand(f.subs({s: t**N1, tau: T + tp}))
    ser = sp.series(ft, t, 0, order).removeO()
    P = sp.Poly(sp.expand(ser), tp)
    coeffs = {mon[0]: c for mon, c in zip(P.monoms(), P.coeffs())}
    v = sp.expand(coeffs.get(0, 0))
    G1 = min(sp.Poly(v, t).monoms())[0] if v != 0 else None
    a = -sp.Poly(v, t).coeff_monomial(t**G1)
    nu = {}
    for kk, ck in coeffs.items():
        if kk >= 1:
            ck = sp.expand(ck)
            if ck != 0:
                nu[kk] = min(sp.Poly(ck, t).monoms())[0]
    assert 1 not in nu or sp.simplify(coeffs[1]) == 0, 'linear term nonzero'
    nu.pop(1, None)
    # A'_*: min_k (nu_k + k A) = G1
    cands = [Fraction(int(G1 - nk), int(kk)) for kk, nk in nu.items() if G1 - nk > 0]
    Ast = None
    for A in sorted(set(cands)):
        if min(Fraction(int(nk)) + kk * A for kk, nk in nu.items()) == G1:
            Ast = A; break
    Ks = sorted(kk for kk, nk in nu.items() if Fraction(int(nk)) + kk * Ast == G1)
    QV = sum(sp.Poly(sp.expand(coeffs[kk]), t).coeff_monomial(t**nu[kk]) * b**kk for kk in Ks)
    print(f'=== {name}: N1={N1}, Gamma1={G1}, a={a}, nu={dict(sorted(nu.items()))}, A*={Ast}, K*={Ks}')
    print('    Q_V(b) =', sp.factor(QV))
    # (3)
    bb = np.linspace(-5, 5, 20001); QVf = sp.lambdify(b, QV, 'numpy')
    print('    min Q_V on [-5,5] =', float(np.min(QVf(bb))), ' lowest deg', Ks[0], 'coef', sp.Poly(QV, b).coeff_monomial(b**Ks[0]))
    # (1) window minimiser
    ff = sp.lambdify((s, tau), f, 'numpy'); Tf = sp.lambdify(t, T, 'numpy')
    grid = np.linspace(-tau0, tau0, 400001)
    worst = 0.0
    for sv in [1e-2, 3e-3, 1e-3, 3e-4, 1e-4]:
        vals = ff(sv, grid); i = int(np.argmin(vals))
        tv = Tf(sv**(1.0 / N1))
        worst = max(worst, abs(vals[i] - ff(sv, tv)) / abs(ff(sv, tv)))
        print(f'    s={sv:.0e}: argmin={grid[i]: .6f}, T(s^(1/N1))={tv: .6f}, f_min={vals[i]:.6e}, f(T)={ff(sv, tv):.6e}')
    # (2) scaled profile
    Phi = sp.lambdify((t, b), sp.expand(ft.subs(tp, t**Ast * b)) / t**G1, 'numpy') if Ast.denominator == 1 else None
    if Phi is not None:
        for tv in [1e-1, 1e-2, 1e-3]:
            errs = [abs(Phi(tv, bv) - (-float(a) + QVf(bv))) for bv in [-1.0, -0.3, 0.2, 0.7, 1.5]]
            print(f'    t={tv:.0e}: max|Phi_hat - (-a+Q_V)| = {max(errs):.3e}')

# (a) symmetric tie, k0=2
analyse('(a) (tau^2-s)^2 - s^3', (tau**2 - s)**2 - s**3, 2, t)
# (c) tie between branches inside the scaled window: Q_V has a second zero
analyse('(c) tau^4 - s tau^2 + s^3', tau**4 - s * tau**2 + s**3, 2, t / sp.sqrt(2))
# (e) degenerate angular minimum k0 = 4
analyse('(e) tau^4 + s^4 tau^2 - s^2', tau**4 + s**4 * tau**2 - s**2, 1, sp.Integer(0))
# (f) Puiseux with N1=3: d_tau f = 4 tau^3 - s
analyse('(f) tau^4 - s tau', tau**4 - s * tau, 3, t / sp.root(4, 3), tau0=0.5)
# (g) degenerate k0=4 with K* = {4} after nontrivial bottom: f = (tau - s)^4 + s^5 (tau-s)^2 - s^3
analyse('(g) (tau-s)^4 + s^5 (tau-s)^2 - s^3', (tau - s)**4 + s**5 * (tau - s)**2 - s**3, 1, t)
