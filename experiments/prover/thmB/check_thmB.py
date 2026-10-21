"""[Эксперимент] Символьная проверка выкладок results/002-theorem-B.md (prover, 21.10.2026).

Вопрос: верны ли выкладки, добавленные или переписанные в results/002:
  (1) разбор примера U=(x^2+y^2-z^2)^2+x z^4: критические точки над R и над C, (B1)-(B3),
      "не минимум";
  (2) на том же примере, в точной параметризации п. 2.6 (ортогональная трубка, сдвиг eta,
      метрика dtheta^2+da^2 на L_C; в тексте допускается любая аналитическая метрика): лемма 2 (U(Phi)=r^5(f+r h), h многочлен), лемма 5
      (A(U)=U как рациональная функция eps в трёх точках (theta,a)), п. 5.1 (Q(.,0)=[omega|d_theta omega|e]), п. 5.2 и итог п. 5
      (DA^x = (I+P_N/2)/(m+1) + O(eps): точные производные, значения в mpmath при eps=1e-2..1e-6);
  (3) лемма 2 (сокращение члена порядка eps) на примере с нетривиальным отображением Морса
      (m=6, U=(x^2+y^2-z^2)^2 (x^2+2y^2+3z^2) + x z^4 (x^2+y^2+z^2) + y^8), ряд по eps в трёх фиксированных точках omega;
  (4) n=2: U=y^2+x^3, поле A=(x/3,y/2).
Метод: sympy, точная арифметика; ряды по eps; в п. (2) для DA значения точных выражений
вычисляются в mpmath (60 знаков). Параметров и seed нет; точки выбраны вручную.
Запуск: ~/venv/bin/python check_thmB.py
Это не доказательство: проверены отдельные выкладки на конкретных примерах.
"""
import sympy as sp

x, y, z = sp.symbols('x y z')
th, a, eps, t = sp.symbols('theta a epsilon t')
S2 = sp.sqrt(2)

def ok(name, cond):
    print(('OK   ' if cond else 'FAIL ') + name)

# ---------------------------------------------------------------- (1) example
q = x**2 + y**2 - z**2
U = q**2 + x*z**4
G = [sp.diff(U, v) for v in (x, y, z)]
ok('grad U = (4xq+z^4, 4yq, -4z(q-xz^2))',
   all(sp.expand(G[i] - e) == 0 for i, e in enumerate([4*x*q + z**4, 4*y*q, -4*z*(q - x*z**2)])))
GB = sp.groebner(G, x, y, z, order='lex')
print('   Groebner basis (lex x>y>z):', GB.exprs)
# real critical points: case analysis is in the text; check its two algebraic identities
ok('q=x z^2 => first component 4xq+z^4 = z^2(4x^2+z^2)',
   sp.expand((4*x*(x*z**2) + z**4) - z**2*(4*x**2 + z**2)) == 0)
# complex critical lines z=0, x=+-i y
for sgn in (1, -1):
    sub = {x: sgn*sp.I*y, z: 0}
    ok('complex line x=%si y, z=0 is critical' % ('+' if sgn > 0 else '-'),
       all(sp.simplify(gi.subs(sub)) == 0 for gi in G))
# (B1)-(B3)
u4, u5 = q**2, x*z**4
for sgn in (1, -1):
    om = sp.Matrix([sp.cos(th), sp.sin(th), sgn])/S2
    nv = sp.Matrix([sp.cos(th), sp.sin(th), -sgn])/S2
    dom = om.diff(th)
    sub = {x: om[0], y: om[1], z: om[2]}
    Hs = sp.hessian(u4, (x, y, z)).subs(sub)
    ok('sgn=%d: u4=0 on Sigma, |omega|=1' % sgn, sp.simplify(u4.subs(sub)) == 0 and sp.simplify((om.T*om)[0]) == 1)
    ok('sgn=%d: n unit, n _|_ omega, n _|_ d_theta omega' % sgn,
       sp.simplify((nv.T*nv)[0] - 1) == 0 and sp.simplify((nv.T*om)[0]) == 0 and sp.simplify((nv.T*dom)[0]) == 0)
    ok('sgn=%d: D^2u4 omega = D^2u4 d_theta omega = 0, H(n,n)=8' % sgn,
       sp.simplify(Hs*om) == sp.zeros(3, 1) and sp.simplify(Hs*dom) == sp.zeros(3, 1)
       and sp.simplify((nv.T*Hs*nv)[0]) == 8)
    gth = sp.simplify(u5.subs(sub))
    ok('sgn=%d: g = cos(theta)/2^(5/2)' % sgn, sp.simplify(gth - sp.cos(th)/2**sp.Rational(5, 2)) == 0)
    ok('sgn=%d: g(+-pi/2)=0, g\'(+-pi/2)=-+2^(-5/2)' % sgn,
       all(sp.simplify(gth.subs(th, v)) == 0 and sp.simplify(sp.diff(gth, th).subs(th, v) + sp.sign(v)*2**sp.Rational(-5, 2)) == 0
           for v in (sp.pi/2, -sp.pi/2)))
    ok('sgn=%d: U(t omega) = t^5 g' % sgn, sp.simplify(U.subs({x: t*om[0], y: t*om[1], z: t*om[2]}) - t**5*gth) == 0)

# ---------------------------------------------------------------- (2) construction on the example
m = 4
c, s = sp.cos(th), sp.sin(th)
om = sp.Matrix([c, s, 1])/S2
nv = sp.Matrix([c, s, -1])/S2
# fibre: u4(r omega + nu n) = 4 r^2 nu^2  => Morse map nu' = nu (exactly)
r_ = sp.symbols('r', positive=True)
P = r_*om + t*nv
ok('u4(r omega + t n) = 4 r^2 t^2 (Morse map = id, H_z = 8 r^2)',
   sp.simplify(u4.subs({x: P[0], y: P[1], z: P[2]}) - 4*r_**2*t**2) == 0)
grad5 = sp.Matrix([sp.diff(u5, v) for v in (x, y, z)]).subs({x: om[0], y: om[1], z: om[2]})
L = sp.simplify((grad5.T*nv)[0])
eta = sp.simplify(L/8)
print('   L_omega(n) =', L, ';  eta =', eta)
Gam = om + (eps*a - eps**2*eta)*nv          # Gamma(theta,a,eps)
Phi = eps**2*Gam                             # Phi(eps,theta,a), r = eps^2
Uphi = sp.expand(U.subs({x: Phi[0], y: Phi[1], z: Phi[2]}, simultaneous=True))
g = sp.simplify(u5.subs({x: om[0], y: om[1], z: om[2]}))
f = 4*a**2 + g
hh = sp.simplify(sp.expand((Uphi/eps**(2*(m + 1)) - f)/eps**2))
ok('Lemma 2: U(Phi) = r^5 (f + r h) with h polynomial in eps (no eps^{-1} terms)',
   sp.simplify(Uphi - eps**10*(f + eps**2*hh)) == 0 and sp.Poly(sp.expand(hh), eps).degree() >= 0)
print('   h =', sp.factor(hh))
# field of sec. 4 in coordinates (eps, theta, a); metric dtheta^2 + da^2 on L_C
he = sp.diff(hh, eps); ht = sp.diff(hh, th); ha = sp.diff(hh, a)
ft = sp.diff(f, th); fa = sp.diff(f, a)
D = (m + 1)**2*f**2 + ft**2 + fa**2
p = (hh + eps*he/2)/(m + 1)
qq = ((m + 1)*f*((m + 2)*hh + eps*he/2) + ft*ht + fa*ha)/D
den = D*(1 + eps**2*qq)
c1 = -(m + 1)*f*p/den
Yt = -p*ft/den
Ya = -p*fa/den
# r d/dr = (eps/2) d/deps ; A = V/(m+1) + r c1 V + r Y
Ae = (eps/2)*(sp.Rational(1, m + 1) + eps**2*c1)
At = eps**2*Yt
Aa = eps**2*Ya
AU = Ae*sp.diff(Uphi, eps) + At*sp.diff(Uphi, th) + Aa*sp.diff(Uphi, a)
# exact check at points: theta with rational cos/sin, a rational; remaining variable eps symbolic
lem5 = True
for (cv, sv, av) in [(sp.Rational(-3, 5), sp.Rational(4, 5), sp.Rational(1, 10)),
                     (sp.Rational(5, 13), sp.Rational(-12, 13), sp.Rational(-2, 7)),
                     (sp.Rational(-8, 17), sp.Rational(-15, 17), sp.Rational(3, 4))]:
    sub = {th: sp.atan2(sv, cv), a: av}
    lem5 = lem5 and sp.cancel(sp.together((AU - Uphi).subs(sub))) == 0
ok('Lemma 5: A(U) = U as rational function of eps at 3 points (theta, a)', lem5)
# sec. 5.1: D Phi = Q diag(1, r, r eps) in (r,theta,a); check Q(theta,a,0)
Qr = Gam + eps*Gam.diff(eps)/2
Qt = Gam.diff(th)
Qa = Gam.diff(a)/eps
Q0 = sp.Matrix.hstack(Qr, Qt, sp.simplify(Qa)).subs(eps, 0)
ok('5.1: Q(theta,a,0) = [omega | d_theta omega | n]',
   sp.simplify(Q0 - sp.Matrix.hstack(om, om.diff(th), nv)) == sp.zeros(3, 3))
# sec. 5: DA^x by formula (*) in coordinates (eps,theta,a)
coords = (eps, th, a)
J = Phi.jacobian(coords)
Ahat = sp.Matrix([Ae, At, Aa])
DAh = Ahat.jacobian(coords)
D2 = sp.zeros(3, 3)
for j, cj in enumerate(coords):
    col = sp.zeros(3, 1)
    for i, ci in enumerate(coords):
        col += Ahat[i]*Phi.diff(ci).diff(cj)
    D2[:, j] = col
Vhat = sp.Matrix([eps/2, 0, 0])
DVh = Vhat.jacobian(coords)
D2V = sp.zeros(3, 3)
for j, cj in enumerate(coords):
    D2V[:, j] = Vhat[0]*Phi.diff(eps).diff(cj)
# exact symbolic derivatives (formula (*)), evaluated with mpmath (60 digits) at small eps:
# check that ||DA^x - (I+P_N/2)/5|| / eps and ||DV^x - I - P_N/2|| / eps stay bounded as eps -> 0
import mpmath as mp
mp.mp.dps = 60
args = (eps, th, a)
fJ = sp.lambdify(args, J, 'mpmath'); fDAh = sp.lambdify(args, DAh, 'mpmath'); fD2 = sp.lambdify(args, D2, 'mpmath')
fDVh = sp.lambdify(args, DVh, 'mpmath'); fD2V = sp.lambdify(args, D2V, 'mpmath')
fA = sp.lambdify(args, Ahat, 'mpmath'); fPhi = sp.lambdify(args, Phi, 'mpmath'); fPn = sp.lambdify(args, nv*nv.T, 'mpmath')
ff = sp.lambdify((th, a), f, 'mpmath')
pts = [(mp.atan2(4, -3), mp.mpf(1)/10), (mp.atan2(-4, -3), -mp.mpf(1)/7), (mp.atan2(12, 5), mp.mpf(1)/3),
       (mp.mpf(2), mp.mpf('0.25'))]
allok = True
for (t0, a0) in pts:
    print('   point theta=%s a=%s f=%s' % (mp.nstr(t0, 6), mp.nstr(a0, 4), mp.nstr(ff(t0, a0), 4)))
    for k in (2, 3, 4, 5, 6):
        e0 = mp.mpf(10)**(-k)
        Jn = mp.matrix(fJ(e0, t0, a0)); Ji = mp.inverse(Jn)
        DA = (mp.matrix(fD2(e0, t0, a0)) + Jn*mp.matrix(fDAh(e0, t0, a0)))*Ji
        DV = (mp.matrix(fD2V(e0, t0, a0)) + Jn*mp.matrix(fDVh(e0, t0, a0)))*Ji
        T = mp.eye(3) + mp.matrix(fPn(e0, t0, a0))/2
        eA = mp.mnorm(DA - T/5, 1); eV = mp.mnorm(DV - T, 1)
        S = (DA + DA.T)/2
        lmin = min(mp.eigsy(S)[0])
        Ax = Jn*mp.matrix(fA(e0, t0, a0)); X = mp.matrix(fPhi(e0, t0, a0))
        ratio = mp.norm(Ax)/mp.norm(X)
        print('      eps=1e-%d: |DA-(I+P/2)/5|/eps=%s  |DV-I-P/2|/eps=%s  lmin(symDA)=%s  |A|/|x|=%s'
              % (k, mp.nstr(eA/e0, 6), mp.nstr(eV/e0, 6), mp.nstr(lmin, 8), mp.nstr(ratio, 8)))
        allok = allok and eA/e0 < 100 and eV/e0 < 100 and lmin > 0
ok('5.2, 5: DV^x = I+P_N/2 + O(eps), DA^x = (I+P_N/2)/5 + O(eps), sym DA > 0 at sample points', allok)

# ---------------------------------------------------------------- (3) Lemma 2 with nontrivial Morse map (m=6)
# Lemma 2 is an identity in eps at each fixed omega, so omega is fixed (rational cos, sin), a symbolic.
w = x**2 + 2*y**2 + 3*z**2
u6 = q**2*w
u7 = x*z**4*(x**2 + y**2 + z**2)
tp = sp.symbols('tp')
N = 4
bs = sp.symbols('b2:%d' % (N + 1))
tser = tp + sum(bs[k - 2]*tp**k for k in range(2, N + 1))
for (cv, sv) in [(sp.Rational(-3, 5), sp.Rational(4, 5)), (sp.Rational(5, 13), sp.Rational(-12, 13)),
                 (sp.Integer(0), sp.Integer(1))]:
    omp = sp.Matrix([cv, sv, 1])/S2
    nvp = sp.Matrix([cv, sv, -1])/S2
    om_s = {x: omp[0], y: omp[1], z: omp[2]}
    Pt = omp + t*nvp
    Pts = {x: Pt[0], y: Pt[1], z: Pt[2]}
    hf = sp.expand(u6.subs(Pts, simultaneous=True))
    ok_fib = sp.expand(hf - 4*t**2*w.subs(Pts, simultaneous=True)) == 0
    H6 = sp.nsimplify(sp.expand(sp.diff(hf, t, 2).subs(t, 0)))
    Mt = sp.expand(4*w.subs(Pts, simultaneous=True))           # M(t) = hf / t^2
    # Morse map t' = t sqrt(M(t)/M(0)); invert as a series t = t' + b2 t'^2 + ...
    fwd = sp.series(tser*sp.sqrt(Mt.subs(t, tser)/Mt.subs(t, 0)), tp, 0, N + 1).removeO()
    sol = sp.solve([sp.expand(fwd).coeff(tp, k) for k in range(2, N + 1)], bs, dict=True)[0]
    tinv = sp.expand(tser.subs(sol))
    grad7 = sp.Matrix([sp.diff(u7, v) for v in (x, y, z)]).subs(om_s)
    L7 = sp.nsimplify(sp.expand((grad7.T*nvp)[0]))
    eta7 = L7/H6
    mu = eps*a - eps**2*eta7
    Gam7 = omp + tinv.subs(tp, mu)*nvp
    Gs = {x: Gam7[0], y: Gam7[1], z: Gam7[2]}
    g7 = sp.expand(u7.subs(om_s))
    f7 = H6/2*a**2 + g7
    expr = sp.expand(u6.subs(Gs, simultaneous=True))/eps**2 + sp.expand(u7.subs(Gs, simultaneous=True))
    ser = sp.expand(sp.series(sp.expand(expr), eps, 0, 2).removeO())
    c0 = sp.simplify(ser.coeff(eps, 0) - f7)
    c1_ = sp.simplify(ser.coeff(eps, 1))
    morse_err = sp.simplify(sp.series(sp.expand(u6.subs(Gs, simultaneous=True)) - H6/2*mu**2, eps, 0, 5).removeO())
    print('   cos=%s sin=%s: H=%s, g=%s, eta=%s, b2=%s' % (cv, sv, H6, sp.nsimplify(g7), sp.nsimplify(eta7), sp.nsimplify(sol[bs[0]])))
    ok('m=6 (cos=%s, sin=%s): fibre u6 = 4t^2 w; Morse map nontrivial (b2!=0)' % (cv, sv),
       ok_fib and sp.simplify(sol[bs[0]]) != 0)
    ok('   u6(Gamma) = Q(eps a - eps^2 eta) + O(eps^5)', morse_err == 0)
    ok('   eps^{-2}u6(Gamma)+u7(Gamma) = f + 0*eps + O(eps^2) (Lemma 2 cancellation)', c0 == 0 and c1_ == 0)

# ---------------------------------------------------------------- (4) n = 2
U2 = y**2 + x**3
A2 = sp.Matrix([x/3, y/2])
ok('n=2: A(U)=U for U=y^2+x^3, A=(x/3,y/2)', sp.expand((A2.T*sp.Matrix([sp.diff(U2, x), sp.diff(U2, y)]))[0] - U2) == 0)
ok('n=2: DA = diag(1/3,1/2) = (I + P_N/2)/(m+1) with m=2, N = y-axis',
   A2.jacobian((x, y)) == sp.diag(sp.Rational(1, 3), sp.Rational(1, 2)))
