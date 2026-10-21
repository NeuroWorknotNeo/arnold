"""R25: symbolic checks for notes/prover/2026-10-21-euler-field.md (reviewer, independent).
[Эксперимент] sympy; exact identities.
"""
import sympy as sp

b1, b2, t, y, x, k, tau = sp.symbols('b1 b2 t y x k tau', real=True)
lam1, lam2 = sp.symbols('lambda1 lambda2', real=True)

print("=== Lemma 3.4 identity ===")
phi = sp.Function('phi')(b1)   # complex root phi_k
psi = sp.Function('psi')(b1)   # real part of phi_j
chi = b1*sp.diff(psi, b1) - psi
g = b2 - phi
xi_g = b1*sp.diff(g, b1) + (b2 + chi)*sp.diff(g, b2)
D = phi - psi
LD = b1*sp.diff(D, b1) - D
print("xi^(j)(b2-phi_k) - [(b2-phi_k) - L D_jk] =", sp.simplify(xi_g - (g - LD)))
e, eps, z = sp.symbols('e epsilon z')
lhs = (g - (e - 1 + e*eps)*D)/g
# D = (b2-psi) - (b2-phi) = z*g - g
lhs2 = (g - (e - 1 + e*eps)*(z*g - g))/g
print("ratio - [e-(e-1)z-e eps (z-1)] =", sp.simplify(lhs2 - (e - (e-1)*z - e*eps*(z-1))))

print("\n=== Step 6: sup_{rho>=1} (rho-1) rho^{-2N} ===")
r = sp.symbols('rho', positive=True)
for N in [1, 2, 3, 10]:
    f = (r-1)*r**(-2*N)
    crit = sp.solve(sp.diff(f, r), r)
    vals = [sp.nsimplify(f.subs(r, c)) for c in crit]
    print(N, crit, [float(v) for v in vals], "1/(2N-1) =", 1/(2*N-1))

print("\n=== Prop 5.4 ===")
G1 = b2**2 + k*b1**2*b2 + b1**4
G2 = b1**2 + k*b1*b2**2 + b2**4
Q = G1*G2
xiQ = lam1*b1*sp.diff(Q, b1) + lam2*b2*sp.diff(Q, b2)
ratio = sp.simplify((xiQ/Q).subs(b2, tau*b1**2))
lim = sp.limit(ratio, b1, 0)
gg = tau**2 + k*tau + 1
rho = tau*sp.diff(gg, tau)/gg
print("limit along b2=tau b1^2:", sp.simplify(lim))
print("limit - [6l1+(l2-2l1)rho] =", sp.simplify(lim - (6*lam1 + (lam2 - 2*lam1)*rho)))
num = sp.numer(sp.together(sp.diff(rho, tau)))
print("rho' numerator:", sp.factor(num))
crit = sp.solve(sp.Eq(k*tau**2 + 4*tau + k, 0), tau)
for c in crit:
    print("rho at crit:", sp.simplify(rho.subs(tau, c)))
for kv in [sp.Rational(199, 100), 8*sp.sqrt(3)/7]:
    vals = [sp.N(rho.subs({tau: c, k: kv}).subs(k, kv)) for c in crit]
    vals = [sp.N(rho.subs(tau, c).subs(k, kv)) for c in crit]
    print("k =", sp.N(kv), "rho at crits:", vals, " 1-2/sqrt(4-k^2) =", sp.N(1 - 2/sp.sqrt(4-kv**2)), " R =", sp.N(2/sp.sqrt(4-kv**2)-1))
print("8sqrt3/7 =", sp.N(8*sp.sqrt(3)/7))
# Newton polygon of Q
Qp = sp.Poly(sp.expand(Q.subs(k, sp.Rational(199,100))), b1, b2)
print("support of Q:", sorted(Qp.monoms()))

print("\n=== Prop 6.2 ===")
A = (x - y**2)**2 + y**8
B = (x - y**2 - y**3)**2 + y**8
Qc = sp.expand(A*B)
print("lowest form:", [m for m in sp.Poly(Qc, x, y).terms() if sum(m[0]) == 4])
f, xi2 = sp.symbols('f xi2', real=True)   # xi = (f, xi2) at the point
s1 = x - y**2; s2 = x - y**2 - y**3
def xiF(F):
    return f*sp.diff(F, x) + xi2*sp.diff(F, y)
xs1 = sp.symbols('xs1')  # xi s1 value
# express f via xs1: xi s1 = f - 2y xi2 -> f = xs1 + 2 y xi2
sub_f = {f: xs1 + 2*y*xi2}
for sgn in [1, -1]:
    P = {x: y**2 + sgn*y**4}
    lA = sp.simplify((xiF(A)/A).subs(P).subs(sub_f))
    print("P^%s: xi log A =" % ('+' if sgn > 0 else '-'), lA, "  claimed:", sp.simplify(lA - (sgn*xs1/y**4 + 4*xi2/y)))
P1 = {x: y**2}
lA1 = sp.simplify((xiF(A)/A).subs(P1).subs(sub_f))
lB1 = sp.simplify((xiF(B)/B).subs(P1).subs(sub_f))
print("P1: xi log A =", lA1)
print("P1: xi log B - claimed =", sp.simplify(lB1 - (xi2*(6 + 8*y**2)/(y*(1 + y**2)) - 2*xs1/(y**3*(1 + y**2)))))
# field (3/2x-1/2y^2, 1/2y)
X1 = sp.Rational(3,2)*x - y**2/2; X2 = y/2
print("xi s1 - 3/2 s1 =", sp.simplify(X1*sp.diff(s1,x)+X2*sp.diff(s1,y) - sp.Rational(3,2)*s1))
print("xi s2 - 3/2 s2 =", sp.simplify(X1*sp.diff(s2,x)+X2*sp.diff(s2,y) - sp.Rational(3,2)*s2))
print("xi Q - 6Q =", sp.factor(sp.expand(X1*sp.diff(Qc,x)+X2*sp.diff(Qc,y) - 6*Qc)))
print("(1+3y/2)/(1+y) - [1+y/2-y^2/2+y^3/(2(1+y))] =", sp.simplify((1+sp.Rational(3,2)*y)/(1+y) - (1 + y/2 - y**2/2 + y**3/(2*(1+y)))))

print("\n=== §5.2, §5.3 examples ===")
def xiQ_(X1, X2, Q):
    return sp.expand(X1*sp.diff(Q, b1) + X2*sp.diff(Q, b2))
Q1 = (b2**2 - b1**4)**2 + b1**10
print("(b2^2-b1^4)^2+b1^10, xi=(b1,2b2): xiQ-8Q =", sp.factor(xiQ_(b1, 2*b2, Q1) - 8*Q1))
Q2 = b2**2 + k*b1**2*b2 + b1**4
print("b2^2+k b1^2 b2+b1^4: xiQ-4Q =", sp.simplify(xiQ_(b1, 2*b2, Q2) - 4*Q2))
Q3 = (b2 - b1**2)**2 + b1**6
print("(b2-b1^2)^2+b1^6, xi=(b1,b2+b1^2): xiQ-2Q =", sp.factor(xiQ_(b1, b2 + b1**2, Q3) - 2*Q3))
Q4 = (b2 - b1**2 - b1**3)**2 + b1**8
print("(b2-b1^2-b1^3)^2+b1^8, xi=(b1,b2+b1^2+2b1^3): xiQ-2Q =", sp.factor(xiQ_(b1, b2 + b1**2 + 2*b1**3, Q4) - 2*Q4))
