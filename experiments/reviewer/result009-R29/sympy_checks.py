"""R29: символьные проверки к results/009-euler-field.md. [Эксперимент]"""
import sympy as sp

ok = lambda name, cond: print(("OK  " if cond else "FAIL"), name)

# --- Лемма 3.4: xi^(j)(b2-phi_k) = (b2-phi_k) - L D_jk
b1, b2 = sp.symbols('b1 b2', positive=True)
phik = sp.Function('phik')(b1); psij = sp.Function('psij')(b1)
chi = b1*sp.diff(psij, b1) - psij
lhs = b2 + chi - b1*sp.diff(phik, b1)       # xi^(j) = (b1, b2+chi)
D = phik - psij
LD = b1*sp.diff(D, b1) - D
ok("3.4: xi(b2-phi_k) = (b2-phi_k) - LD", sp.simplify(lhs - ((b2 - phik) - LD)) == 0)
e, eps, z = sp.symbols('e epsilon z')
ok("3.4: 1-(e-1+e eps)(z-1) = e-(e-1)z-e eps(z-1)",
   sp.expand(1 - (e - 1 + e*eps)*(z - 1) - (e - (e - 1)*z - e*eps*(z - 1))) == 0)

# --- Лемма 3.3: eps_D = tau (tau g)'/(k0 (1+tau g))
tau, m, k0, d0 = sp.symbols('tau m k0 d0', positive=True)
g = sp.Function('g')(tau)
Dt = d0*tau**k0*(1 + tau*g)
eD = (tau/m*sp.diff(Dt, tau))/((k0/m)*Dt) - 1
ok("3.3: eps_D formula", sp.simplify(eD - tau*sp.diff(tau*g, tau)/(k0*(1 + tau*g))) == 0)

# --- (2.2): chi = sum_{k>m}(k/m-1)a_k tau^k ; chi' = sum (k/m)(k/m-1) a_k tau^{k-m}
mm = 3
a = sp.symbols('a3:12')
psi = sum(a[i]*tau**(i + 3) for i in range(9))      # порядок >= m=3
B1 = tau**mm
dpsi_db1 = sp.diff(psi, tau)/sp.diff(B1, tau)
chi_t = sp.expand(B1*dpsi_db1 - psi)
ok("(2.2): член k=m уходит из chi", sp.Poly(chi_t, tau).coeff_monomial(tau**3) == 0)
chip = sp.expand(sp.diff(chi_t, tau)/sp.diff(B1, tau))
target = sum(sp.Rational(i + 3, mm)*(sp.Rational(i + 3, mm) - 1)*a[i]*tau**i for i in range(9))
ok("(2.2): chi' формула", sp.simplify(chip - target) == 0)

# --- Лемма 3.5: sup_{rho>=1}(rho-1)rho^{-2N} <= 1/(2N-1), rho^{-2N}(rho+1) <= 2
rho = sp.symbols('rho', positive=True)
good = True
for N in range(1, 30):
    r0 = sp.Rational(2*N, 2*N - 1)
    val = (r0 - 1)*r0**(-2*N)
    good &= bool(val <= sp.Rational(1, 2*N - 1))
ok("3.5: sup (rho-1)rho^-2N <= 1/(2N-1), N=1..29", good)

# --- Лемма 3.6(d): grad w_j
p = sp.symbols('p1:4', positive=True)
Nn = sp.symbols('N', positive=True)
S = sum(pk**(-Nn) for pk in p)
w = [pk**(-Nn)/S for pk in p]
t = sp.symbols('t')
pf = [sp.Function('P%d' % i)(t) for i in range(3)]
Sf = sum(pk**(-Nn) for pk in pf)
wf0 = pf[0]**(-Nn)/Sf
lhs = sp.diff(wf0, t)
rhs = Nn*wf0*(-sp.diff(pf[0], t)/pf[0] + sum((pf[k]**(-Nn)/Sf)*sp.diff(pf[k], t)/pf[k] for k in range(3)))
ok("3.6(d): формула grad w_j", sp.simplify(lhs - rhs) == 0)

# --- Предложение 5.3
x1, x2, lam, gam = sp.symbols('b1 b2 lambda gamma', real=True)
kk = 3
phi = sp.Function('phi')(x1)
tt = x2 - phi
Q = tt**2 + gam*x1**(2*kk)
xi = (x1, lam*tt + x1*sp.diff(phi, x1))
xiQ = xi[0]*sp.diff(Q, x1) + xi[1]*sp.diff(Q, x2)
ok("5.3: xiQ = 2 lam t^2 + 2k gam b1^2k", sp.simplify(xiQ - (2*lam*tt**2 + 2*kk*gam*x1**(2*kk))) == 0)
J = sp.Matrix([[sp.diff(xi[0], x1), sp.diff(xi[0], x2)], [sp.diff(xi[1], x1), sp.diff(xi[1], x2)]])
ok("5.3: D xi", sp.simplify(J - sp.Matrix([[1, 0], [(1 - lam)*sp.diff(phi, x1) + x1*sp.diff(phi, x1, 2), lam]])) == sp.zeros(2))

# --- Предложение 5.4
k = sp.symbols('k', positive=True)
B1s, B2s = sp.symbols('b1 b2', real=True)
G1 = B2s**2 + k*B1s**2*B2s + B1s**4
G2 = B1s**2 + k*B1s*B2s**2 + B2s**4
ok("5.4: дискриминант G1 по b2 = (k^2-4) b1^4", sp.simplify(sp.discriminant(G1, B2s) - (k**2 - 4)*B1s**4) == 0)
Qp = sp.Poly(sp.expand(G1*G2), B1s, B2s)
supp = sorted(Qp.monoms())
print("     носитель Q (k общий):", supp)
# рёберные многочлены
e1 = sum(c*B1s**i*B2s**j for (i, j), c in zip(Qp.monoms(), Qp.coeffs()) if i + 2*j == 6)
e2 = sum(c*B1s**i*B2s**j for (i, j), c in zip(Qp.monoms(), Qp.coeffs()) if 2*i + j == 6)
ok("5.4: ребро (1,2): b1^2 G1", sp.expand(e1 - B1s**2*G1) == 0)
ok("5.4: ребро (2,1): b2^2 G2", sp.expand(e2 - B2s**2*G2) == 0)
ok("5.4: все мономы выше рёбер", all(i + 2*j >= 6 and 2*i + j >= 6 for (i, j) in Qp.monoms()))
# предел xi log Q вдоль b2 = tau b1^2
l1, l2, ta, s = sp.symbols('lambda1 lambda2 tau s', real=True)
xiQ = l1*B1s*sp.diff(G1*G2, B1s) + l2*B2s*sp.diff(G1*G2, B2s)
ratio = sp.simplify((xiQ/(G1*G2)).subs(B2s, ta*B1s**2))
lim = sp.limit(ratio, B1s, 0)
gg = ta**2 + k*ta + 1
rho_t = ta*sp.diff(gg, ta)/gg
ok("5.4: предел = 6l1+(l2-2l1)rho(tau)", sp.simplify(lim - (6*l1 + (l2 - 2*l1)*rho_t)) == 0)
num = sp.factor(sp.numer(sp.together(sp.diff(rho_t, ta))))
print("     числитель rho':", num)
crit = sp.solve(sp.Eq(k*ta**2 + 4*ta + k, 0), ta)
cv = [sp.simplify(rho_t.subs(ta, c)) for c in crit]
print("     критические значения:", cv)
kval = sp.Rational(19, 10)
vals = sorted([float(c.subs(k, kval)) for c in cv])
print("     при k=1.9:", vals, " ожидается", 1 - 2/float(sp.sqrt(4 - kval**2)), 1 + 2/float(sp.sqrt(4 - kval**2)))
kstar = 8*sp.sqrt(3)/7
ok("5.4: R(8sqrt3/7) = 6", sp.simplify(2/sp.sqrt(4 - kstar**2) - 1 - 6) == 0)
# симметрия Q при b1<->b2
ok("5.4: Q симметрична", sp.expand((G1*G2).subs({B1s: B2s, B2s: B1s}, simultaneous=True) - G1*G2) == 0)

# --- Предложение 6.2(b)
x, y = sp.symbols('x y', real=True)
A = (x - y**2)**2 + y**8
Bq = (x - y**2 - y**3)**2 + y**8
Q62 = sp.expand(A*Bq)
xi62 = (sp.Rational(3, 2)*x - y**2/2, y/2)
L = lambda F: xi62[0]*sp.diff(F, x) + xi62[1]*sp.diff(F, y)
ok("6.2(b): xi s1 = 3/2 s1", sp.expand(L(x - y**2) - sp.Rational(3, 2)*(x - y**2)) == 0)
ok("6.2(b): xi s2 = 3/2 s2", sp.expand(L(x - y**2 - y**3) - sp.Rational(3, 2)*(x - y**2 - y**3)) == 0)
ok("6.2(b): xi Q - 6Q = y^8 (A+B)", sp.expand(L(Q62) - 6*Q62 - y**8*(A + Bq)) == 0)
# младшая форма Q
Pq = sp.Poly(Q62, x, y)
dmin = min(i + j for (i, j) in Pq.monoms())
Q4 = sum(c*x**i*y**j for (i, j), c in zip(Pq.monoms(), Pq.coeffs()) if i + j == dmin)
ok("6.2: d=4, Q_4 = x^4", dmin == 4 and sp.expand(Q4 - x**4) == 0)
# шаг 1: xi log A в P^pm, общий xi=(f,X2)
f, X2, a_ = sp.symbols('f X2 a', real=True)
ypos = sp.symbols('y', positive=True)
xis1 = sp.symbols('xis1', real=True)   # = f - 2y X2
for sgn in (1, -1):
    xx = ypos**2 + sgn*ypos**4
    s1 = xx - ypos**2
    Aval = (s1**2 + ypos**8)
    xiA = 2*s1*xis1 + 8*ypos**7*X2
    ok("6.2 шаг 1: A(P^%+d)=2y^8, xi log A" % sgn,
       sp.simplify(Aval - 2*ypos**8) == 0 and sp.simplify(xiA/Aval - (sgn*xis1/ypos**4 + 4*X2/ypos)) == 0)
# шаг 2: в P1
s2 = -ypos**3
Bv = s2**2 + ypos**8
xis2 = xis1 - 3*ypos**2*X2
xiB = 2*s2*xis2 + 8*ypos**7*X2
ok("6.2 шаг 2: xi log B в P1",
   sp.simplify(xiB/Bv - (X2*(6 + 8*ypos**2)/(ypos*(1 + ypos**2)) - 2*xis1/(ypos**3*(1 + ypos**2)))) == 0)
ok("6.2 шаг 2: множитель 8+(6+8y^2)/(1+y^2) в [14,16]",
   all(14 <= 8 + (6 + 8*v**2)/(1 + v**2) <= 16 for v in [0, 0.01, 0.1, 0.5, 1.0, 3.0]))
# шаг 3
ok("6.2 шаг 3: тождество y^3/(2(1+y))",
   sp.simplify((1 + sp.Rational(3, 2)*ypos)/(1 + ypos) - (1 + ypos/2 - ypos**2/2) - ypos**3/(2*(1 + ypos))) == 0)
ok("6.2 шаг 3: 73(2+3y)<=150 при y<=4/219", sp.simplify(73*(2 + 3*sp.Rational(4, 219)) - 150) == 0)
# шаг 1: проверим числовые константы 25K: 12*2K + 32y*2Ky <= 25K при y<=1/8
ok("6.2 шаг 1: 24+64y^2 <= 25 при y<=1/8", 24 + 64*sp.Rational(1, 64) <= 25)
ok("6.2: K(1+2y+3y^2) <= 2K при y<=1/8", 1 + 2*sp.Rational(1, 8) + 3*sp.Rational(1, 64) <= 2)

# --- Следствие 6.1(c): Q~_d(0,1) = G2^{-d} Q_d(0,1) на примере
u1, u2 = sp.symbols('u1 u2')
Qex = (B2s**2 - B1s**3)**2 + B1s**8 + B1s**2*B2s**2   # Q_4 = b2^4 + b1^2 b2^2
F = 2*B1s + B1s**2
Gm = 3*B2s + B1s + B1s*B2s + B2s**2
# Q~ = Q o Phi^{-1}: вычислим младшую форму через Q = Q~ o Phi
Qt = sp.Function('Qt')
# проще: Q~_d o DPhi(0) = Q_d  =>  Q~_d(v) = Q_d(DPhi(0)^{-1} v)
DPhi = sp.Matrix([[2, 0], [1, 3]])
Qd = B2s**4 + B1s**2*B2s**2
v = DPhi.inv()*sp.Matrix([0, 1])
ok("6.1(c): Q~_d(0,1) = 3^{-4} Q_d(0,1)", sp.simplify(Qd.subs({B1s: v[0], B2s: v[1]}, simultaneous=True) - sp.Rational(1, 81)) == 0)
