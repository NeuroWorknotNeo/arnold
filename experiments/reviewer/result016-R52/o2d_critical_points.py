# R52 [символьно]: все критические точки Q(t,eps) = A*B на плоскости (t,eps), t = sin(theta)cos(theta),
# через результант по t; классификация гессианом; плюс граница t = +-1/2 (cos 2theta = 0).
import sympy as sp
t, e = sp.symbols('t e', real=True)
A = (t - e**2)**2 + e**8
B = (t - e**2 - e**3)**2 + e**8
Q = sp.expand(A*B)
Qt = sp.expand(sp.diff(Q, t)); Qe = sp.expand(sp.diff(Q, e))
R = sp.resultant(Qt, Qe, t)
fl = sp.factor_list(R)
print('resultant factors:', [(f, m) for f, m in fl[1]])
H = sp.hessian(Q, (t, e))
pts = []
for f, m in fl[1]:
    for r in sp.Poly(f, e).all_roots():
        if not r.is_real: continue
        g = sp.gcd(sp.Poly(Qt.subs(e, r), t), sp.Poly(Qe.subs(e, r), t))
        for tr in sp.Poly(g, t).all_roots() if sp.Poly(g, t).degree() > 0 else []:
            if tr.is_real: pts.append((sp.nsimplify(tr), r))
print('real critical points:')
for tr, r in pts:
    Hm = H.subs({t: tr, e: r})
    print('  t =', sp.N(tr, 15), ' e =', sp.N(r, 15), ' Q =', sp.N(Q.subs({t: tr, e: r}), 15),
          ' det H =', sp.N(Hm.det(), 10), ' tr H =', sp.N(Hm.trace(), 10), ' |t|<=1/2:', bool(abs(sp.N(tr)) <= 0.5))
print('boundary t = +-1/2:')
for tb in (sp.Rational(1, 2), -sp.Rational(1, 2)):
    q1 = sp.Poly(sp.diff(Q.subs(t, tb), e), e)
    for r in q1.nroots(n=30, maxsteps=400):
        if abs(sp.im(r)) > 1e-25: continue
        r = sp.re(r)
        sec = sp.diff(Q.subs(t, tb), e, 2).subs(e, r)
        qt = Qt.subs({t: tb, e: r})
        print(f'  t={tb} e={float(r):+.8f} Q={float(Q.subs({t: tb, e: r})):.6e} Q_ee={float(sec):+.4e} Q_t={float(qt):+.4e}',
              ' -> local min on cylinder' if (sec > 0 and ((qt < 0) if tb > 0 else (qt > 0))) else '')
