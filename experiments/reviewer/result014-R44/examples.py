"""R44: пересчёт столбцов gamma_*, j, c, Phi_0 таблицы примеров (замечание 3 results/014),
пример O2 (замечание 4) и замечание 2. Сигма -- экватор, omega=(cos,sin,0), n=(0,0,1), u_4=z^4, r=2."""
import sympy as sp
x, y, z, s, Y, th, eps = sp.symbols('x y z s Y theta epsilon', real=True)
rho2 = x**2 + y**2
C, S = sp.cos(th), sp.sin(th)

def edge(U, m=4, r=2):
    phi = sp.expand(U.subs({x: s*C, y: s*S, z: s*Y})/s**m)
    P = sp.Poly(phi, s, Y)
    sup = {}
    for (i, l), co in P.terms():
        co = sp.simplify(co)
        if co != 0:
            sup[(i, l)] = sp.simplify(sup.get((i, l), 0) + co)
    cand = [sp.Rational(i, 2*r - l) for (i, l) in sup if l < 2*r]
    g = min(cand)
    Phi0 = sum(co*eps**l for (i, l), co in sup.items() if i + g*l == 2*r*g)
    return g, m + 2*r*g, 1 + g, sp.simplify(sp.expand(sp.expand_trig(Phi0)))

ex = {
 'W1': (z - x**2)**4 + sp.Rational(3, 2)*x*rho2**2 - sp.Rational(1, 2)*x**3*rho2 + y*z**5,
 'W2': z**4 + z*(9*rho2**2 - 8*y**4) + x**6 + y*z**5,
 'W3': z**4 + z**2*y*rho2 - rho2**3 + y**2*rho2**2 + x*z**5 + y**7,
 'W4': (z**2 - rho2**2)**2 + z*x**8,
 'C1': (z + x*y)**4 - rho2**3 + x**7 + z**3*y**4,
 'C2': z**4 + z*rho2**2 + x**6*z + y**7,
 'D1': (z - x*y - x**3)**4 + y**2*rho2**2 + x**7,
 'D2': (z**2 - rho2**2)**2 + y**2*rho2**3 + x**9 + z**3*x**6,
 'D3': (z**2 - rho2**2)**2 + z**2*y**2*rho2**2 + x**11,
 'O2': z**4 - 2*z**2*y*rho2 - x**2*rho2**2 + x**7 + y**7,
}
claimed = {
 'W1': eps**4 + sp.Rational(1, 2)*C*(3 - C**2),
 'W2': eps**4 + (9 - 8*S**4)*eps,
 'W3': (eps**2 + S/2)**2 + sp.Rational(3, 4)*S**2 - 1,
 'W4': (eps**2 - 1)**2,
 'C1': eps**4 - 1,
 'C2': eps**4 + eps,
 'D1': eps**4 + S**2,
 'D2': (eps**2 - 1)**2 + S**2,
 'D3': (eps**2 - 1)**2,
 'O2': (eps**2 - S)**2 - 1,
}
for k, U in ex.items():
    g, j, c, Phi0 = edge(U)
    d = sp.simplify(sp.expand(sp.expand_trig(Phi0 - claimed[k])))
    print(k, 'gamma*=', g, 'j=', j, 'c=', c, 'Phi0 matches:', d == 0, '' if d == 0 else Phi0)

# W4, D3: full Utilde (N=1, gamma*=1): Utilde(sigma,theta,eps) = phi(s, th, s*eps)/s^4 with sigma=s
for k in ['W4', 'D3', 'D1']:
    U = ex[k]
    g, j, c, Phi0 = edge(U)
    Nn = sp.fraction(g)[1]
    sig = sp.Symbol('sigma', positive=True)
    Ut = sp.expand(U.subs({x: s*C, y: s*S, z: s**(1+g)*eps})/s**j)
    Ut = sp.expand(Ut.subs(s, sig**Nn))
    print(k, 'Utilde =', sp.simplify(Ut))

# W4 branch near eps=-1: expand Ghat in sigma
sig = sp.Symbol('sigma', positive=True)
for k, e0 in [('W4', -1), ('D3', 1), ('D3', -1)]:
    U = ex[k]
    Ut = sp.expand(U.subs({x: s*C, y: s*S, z: s**2*eps})/s**8).subs(s, sig)
    # critical point branch eps = e0 + a1 sig + a2 sig^2 + ...
    a = sp.symbols('a1:6')
    br = e0 + sum(a[i]*sig**(i+1) for i in range(5))
    dU = sp.series(sp.diff(Ut, eps).subs(eps, br), sig, 0, 6).removeO()
    sol = {}
    for i in range(1, 6):
        ci = sp.expand(dU).coeff(sig, i)
        ci = ci.subs(sol)
        ai = sp.solve(ci, a[i-1])
        sol[a[i-1]] = sp.simplify(ai[0]) if ai else 0
    Gh = sp.series(Ut.subs(eps, br.subs(sol)), sig, 0, 5).removeO()
    print(k, 'branch', e0, ' Ghat =', sp.simplify(sp.expand(Gh)))

# O2: floor function in units s^6: min_eps Utilde
U = ex['O2']
Ut = sp.simplify(sp.expand(U.subs({x: s*C, y: s*S, z: s**sp.Rational(3, 2)*eps})/s**6))
print('O2 Utilde =', Ut)
# (CM) at fold (0,0): d^3 Phi0 = 24 eps -> eps_b = 0, then d^2 Phi0(theta,0)
Phi0 = (eps**2 - S)**2 - 1
print('O2 d2Phi0(theta,0) =', sp.simplify(sp.diff(Phi0, eps, 2).subs(eps, 0)), ' (CM) needs == 0')
import numpy as np
for sv in [1e-2, 1e-3]:
    ths = np.linspace(0, 2*np.pi, 200001)
    Gm = np.where(np.sin(ths) >= 0, -1.0, np.sin(ths)**2 - 1)
    fl = Gm + sv*(np.cos(ths)**7 + np.sin(ths)**7)
    i = np.argmin(fl)
    print('O2 floor s=%g: min=%.10f at theta=%.6f (pi=%.6f), -1-s=%.10f' % (sv, fl[i], ths[i], np.pi, -1 - sv))

# Remark 2
k_, c_, th_, E = sp.symbols('kappa c theta E', real=True)
P0 = E**2 + th_*E + th_**2       # E = e^2
form = sp.expand(k_*th_*sp.diff(P0, th_) + c_*2*E*sp.diff(P0, E))   # e d/de = 2E d/dE
print('Remark 2 form:', form, '| claimed:', sp.expand(4*c_*E**2 + (k_ + 2*c_)*th_*E + 2*k_*th_**2 - form) == 0)
print('roots of (k+2c)^2-32ck in k/c:', sp.solve((k_ + 2)**2 - 32*k_, k_), float(14 - sp.sqrt(192)))
print('c2=k/2:', sp.simplify(k_*(th_*sp.diff(P0, th_) + sp.Rational(1, 2)*2*E*sp.diff(P0, E)) - 2*k_*P0) == 0)
