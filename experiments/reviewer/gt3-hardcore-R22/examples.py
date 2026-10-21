"""R22: independent recomputation for sections 9.6-9.7 of notes/prover/2026-10-21-gt3-hardcore.md.

For each example: the series of the critical point of the normal-slice function
  F(t, y) = U(t (w + sum_a y_a f_a)) / t^m
(w = unnormalised point of Sigma, f_a = unnormalised orthogonal basis of the normal space;
the slice {t(w + sum y_a f_a)} is the same affine plane as in lemma K1, only rescaled), solved
order by order from d_y F = 0 in exact arithmetic; then R = F(t, y*(t)) and
g_{m+i} = [t^i]R / |w|^{m+i}  (since s = |w| t).  Hence j, G = g_j, the minimum of G,
G'' in the natural parameter, G'' + jG, kappa from (8.5), and a numerical check of the
normal form (6.3).  Own code, not the author's examples.py.  [Experiment]
Run: ~/venv/bin/python -u examples.py
"""
import sympy as sp
import numpy as np
import mpmath as mp

x, y, z, t = sp.symbols('x y z t', real=True)
C, S = sp.symbols('C S', real=True)       # cos(phi), sin(phi) on the circles


def trunc(expr, N):
    p = sp.Poly(sp.expand(expr), t)
    return sum(cf * t**mon[0] for mon, cf in zip(p.monoms(), p.coeffs()) if mon[0] <= N)


def red(expr):
    """reduce modulo C^2 + S^2 = 1 (S^2 -> 1 - C^2)"""
    e = sp.expand(expr)
    return sp.expand(sp.Poly(e, S).as_expr().subs(S**2, 1 - C**2)) if e.has(S) else e


def red_full(expr):
    e = sp.expand(expr)
    for _ in range(10):
        e2 = sp.expand(e.subs(S**2, 1 - C**2))
        if e2 == e:
            break
        e = e2
    return e


def reduced_series(U, m, w, fs, N, trig=False):
    p = len(fs)
    yv = sp.symbols(f'y0:{p}')
    pt = sp.Matrix(w) + sum((yv[a] * sp.Matrix(fs[a]) for a in range(p)), sp.zeros(3, 1))
    F = sp.expand(U.subs({x: t * pt[0], y: t * pt[1], z: t * pt[2]}, simultaneous=True) / t**m)
    if trig:
        F = red_full(F)
    grad = [sp.expand(sp.diff(F, yv[a])) for a in range(p)]
    Hmat = sp.Matrix(p, p, lambda a, b: sp.diff(grad[a], yv[b]).subs({t: 0, **{v: 0 for v in yv}}))
    if trig:
        Hmat = Hmat.applyfunc(red_full)
    Hinv = Hmat.inv()
    yser = [sp.Integer(0)] * p
    for i in range(1, N + 1):
        res = []
        for a in range(p):
            ga = trunc(grad[a].subs({yv[b]: yser[b] for b in range(p)}, simultaneous=True), i)
            res.append(sp.expand(ga).coeff(t, i))
        if trig:
            res = [red_full(r_) for r_ in res]
        Yi = -(Hinv * sp.Matrix(res))
        yser = [sp.expand(yser[a] + sp.simplify(Yi[a]) * t**i) for a in range(p)]
    R = trunc(F.subs({yv[b]: yser[b] for b in range(p)}, simultaneous=True), N + 1)
    if trig:
        R = red_full(R)
    nw = sp.sqrt(sum(c_**2 for c_ in w))
    if trig:
        nw = sp.sqrt(red_full(sum(c_**2 for c_ in w)))
    g = {m + i: sp.simplify(sp.expand(R).coeff(t, i) / nw**(m + i)) for i in range(0, N + 2)}
    # normalised y*: y_norm_a(s) = y_a(t) |f_a| / |w|,  s = |w| t
    return yser, g, Hmat, nw


print('=' * 70)
print('9.6: U = (x^2-z^2)^2 + (y^2-z^2)^2 + z^5, omega* = (1,1,-1)/sqrt3')
w0 = [1, 1, -1]
f1, f2 = [1, -1, 0], [1, 1, 2]
U96 = (x**2 - z**2)**2 + (y**2 - z**2)**2 + z**5
ys, g, Hm, nw = reduced_series(U96, 4, w0, [f1, f2], 3)
# H in the orthonormal basis: Hm is d^2F/dy^2 in unnormalised (t=1,|w|=sqrt3) coords:
# F = U(t(...))/t^4, normalised y_a' = y_a |f_a| / |w| and phi = F/|w|^4 => H'_{ab} = Hm_ab |w|^2/(|f_a||f_b| |w|^4)
nf = [sp.sqrt(2), sp.sqrt(6)]
Hn = sp.Matrix(2, 2, lambda a, b: sp.simplify(Hm[a, b] / (nf[a] * nf[b] * nw**2)))
print('H (orthonormal e1,e2) =', Hn, '  claim diag(8/3, 8)')
print('g_k =', {kk: sp.nsimplify(v) for kk, v in g.items()})
print('g_5 = -3^(-5/2)?', sp.simplify(g[5] + 3**sp.Rational(-5, 2)) == 0)

print('=' * 70)
print('9.7 (s=0): U7 = (x^2-z^2+z^3)^2 + (y^2-z^2)^2 + z^7')
U7 = (x**2 - z**2 + z**3)**2 + (y**2 - z**2)**2 + z**7
for sx in (1, -1):
    for sy in (1, -1):
        for sz in (1, -1):
            wv = [sx, sy, sz]
            fa = [sx, -sy, 0]
            fb = list(sp.Matrix(wv).cross(sp.Matrix(fa)))
            ys, g, Hm, nw = reduced_series(U7, 4, wv, [fa, fb], 4)
            line = f'  omega=({sx},{sy},{sz})/sqrt3: g5..g8 = ' + str([sp.nsimplify(sp.radsimp(g[kk])) for kk in (5, 6, 7, 8)])
            if (sx, sy, sz) == (1, 1, -1):
                # normalised y*(s) first order: y_a t |f_a|/|w| with t = s/|w| -> coefficient * |f_a| / |w|^2
                y1 = [sp.simplify(ys[a].coeff(t, 1) * sp.sqrt(sum(c_**2 for c_ in f)) / nw**2) for a, f in enumerate([fa, fb])]
                line += f'\n      y*(s) first-order coefficients (orthonormal frame) = {y1}  (claim sqrt2/12={sp.sqrt(2)/12}, sqrt6/36={sp.sqrt(6)/36})'
                line += f'\n      g_7 = -sqrt3/81 ? {sp.simplify(g[7] + sp.sqrt(3) / 81) == 0}'
            print(line)

print('=' * 70)
print('9.7 (s=1): U8 = (Q0+z^3)^2 + x z^6 + x y z^5 + z^7/2,  omega = (C,S,+-1)/sqrt2, n = omega x T')
Q0 = x**2 + y**2 - z**2
U8 = (Q0 + z**3)**2 + x * z**6 + x * y * z**5 + sp.Rational(1, 2) * z**7
ph = sp.symbols('varphi', real=True)
Gs_ = {}
for sgn in (1, -1):
    wv = [C, S, sgn]
    Tv = sp.Matrix([-S, C, 0])
    nv = list(red_full(c_) for c_ in sp.Matrix(wv).cross(Tv))     # = sqrt2 * n
    ys, g, Hm, nw = reduced_series(U8, 4, wv, [nv], 4, trig=True)
    print(f' circle z = {sgn}/sqrt2: n*sqrt2 = {nv}, |w| = {nw}')
    hn = sp.simplify(Hm[0, 0] / (2 * nw**2) / 1) * 2   # phi'' in normalised y: Hm*|n|^2... see below
    # normalised: y' = y |nv| / |w| = y, phi = F/|w|^4; d^2 phi/dy'^2 = Hm / |w|^4 * |w|^2/|nv|^2 = Hm/4
    print('   h_n =', sp.simplify(Hm[0, 0] / 4))
    for kk in sorted(g):
        gk = sp.simplify(g[kk].subs({C: sp.cos(ph), S: sp.sin(ph)}))
        print(f'   g_{kk} =', sp.simplify(sp.trigsimp(gk)))
        if kk == 7:
            Gs_[sgn] = gk
Gp, Gm = Gs_[1], Gs_[-1]
print('G_+ == sqrt2/32 (1+2cos+sin2) :', sp.simplify(Gp - sp.sqrt(2) / 32 * (1 + 2 * sp.cos(ph) + sp.sin(2 * ph))) == 0)
print('G_- == sqrt2/32 (2cos-sin2-1) :', sp.simplify(Gm - sp.sqrt(2) / 32 * (2 * sp.cos(ph) - sp.sin(2 * ph) - 1)) == 0)
Gp = sp.sqrt(2) / 32 * (1 + 2 * sp.cos(ph) + sp.sin(2 * ph))
dG = sp.diff(Gp, ph)
# critical points: -2 sin + 2 cos 2phi = 0  <=>  2 sin^2 + sin - 1 = 0  <=> sin = 1/2 or -1
for phc in (sp.pi / 6, 5 * sp.pi / 6, 3 * sp.pi / 2):
    print(f'   G_+({phc}) = {sp.nsimplify(sp.simplify(Gp.subs(ph, phc)))} ~ {float(Gp.subs(ph, phc)):.6f};'
          f' dG = {sp.simplify(dG.subs(ph, phc))}')
fG = sp.lambdify(ph, Gp, 'numpy')
grid = np.linspace(0, 2 * np.pi, 400001)
print('   grid: min G_+ =', fG(grid).min(), 'at', grid[fG(grid).argmin()], ' 5pi/6 =', 5 * np.pi / 6)
phs = 5 * sp.pi / 6
G0 = sp.simplify(Gp.subs(ph, phs))
G2 = sp.simplify(2 * sp.diff(Gp, ph, 2).subs(ph, phs))
print('   G(phi*) =', G0, '; == sqrt2(2-3sqrt3)/64 :', sp.simplify(G0 - sp.sqrt(2) * (2 - 3 * sp.sqrt(3)) / 64) == 0, float(G0))
print("   G''(theta) =", G2, '; == 3sqrt6/16 :', sp.simplify(G2 - 3 * sp.sqrt(6) / 16) == 0, float(G2))
print("   G''+7G =", sp.simplify(G2 + 7 * G0), '=', float(G2 + 7 * G0),
      '; == 7sqrt2/32 - 9sqrt6/64 :', sp.simplify(G2 + 7 * G0 - (7 * sp.sqrt(2) / 32 - 9 * sp.sqrt(6) / 64)) == 0)
lam0 = sp.Rational(1, 4) * sp.Min(G2, 8)
kmax = 7 * lam0 / (-G0 * (sp.Rational(15, 8) * sp.sqrt(3) * 7 + 2 * sp.sqrt(2))**2)
print('   kappa_max by (8.5) =', float(kmax))

# normal form (6.3) at the upper circle: U(Psi(s,theta,s^c e))/s^7 - (G(theta) + 4 e^2) -> 0
print('normal form (6.3), U8, upper circle, c = 5/2:')
wv = [C, S, 1]
nv = [-C, -S, 1]
ys, g, Hm, nw = reduced_series(U8, 4, wv, [nv], 6, trig=True)
ystar_t = ys[0]     # y(t) in the unnormalised slice, point = t(w + y nv), s = sqrt2 t, eta = s*y (|nv|=|w|)
mp.mp.dps = 40
Uf = sp.lambdify((x, y, z), U8, 'mpmath')
yf = sp.lambdify((t, C, S), ystar_t, 'mpmath')
for thv, ev in [(0, 0), (0.05, 0.3), (-0.08, -0.5)]:
    phv = 5 * mp.pi / 6 + mp.sqrt(2) * thv
    out = []
    for sv in (mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')):
        tv = sv / mp.sqrt(2)
        eta = sv * yf(tv, mp.cos(phv), mp.sin(phv)) + sv**mp.mpf(2.5) * ev
        om = [mp.cos(phv) / mp.sqrt(2), mp.sin(phv) / mp.sqrt(2), 1 / mp.sqrt(2)]
        nn = [-mp.cos(phv) / mp.sqrt(2), -mp.sin(phv) / mp.sqrt(2), 1 / mp.sqrt(2)]
        q = [sv * om[i] + eta * nn[i] for i in range(3)]
        Gv = mp.sqrt(2) / 32 * (1 + 2 * mp.cos(phv) + mp.sin(2 * phv))
        out.append(mp.nstr(Uf(*q) / sv**7 - (Gv + 4 * ev**2), 4))
    print(f'   theta={thv}, e={ev}:', out)
