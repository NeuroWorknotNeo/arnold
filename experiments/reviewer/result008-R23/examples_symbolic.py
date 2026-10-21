"""R23: символьная проверка примеров 1-3 из results/008-class-K.md (§12).

[Эксперимент] Точная арифметика sympy. Проверяет:
 - пример 1: Sigma, градиенты, H в базисе e1,e2, частные производные и полиномы по случаям;
 - пример 2: разложение на u_k, полиномы по случаям, семейство Четаева, E U;
 - пример 3: u_k, G_+-, критические точки и значения, G'', G''+7G, kappa из (U3),
   комплексные критические прямые, тождество E U = 4U + 2 z^3 P + 3 u_7;
 - формула g_{m+2} = u_{m+2} - 1/2 b1^T H^{-1} b1 на случайном примере (точно).
"""
import sympy as sp
import random

x, y, z, s, t, tau = sp.symbols('x y z s t tau', real=True)
q = sp.Matrix([x, y, z])


def homog_parts(U, vars_, maxdeg):
    lam = sp.Symbol('lam')
    Ul = sp.expand(U.subs({v: lam * v for v in vars_}, simultaneous=True))
    return {k: sp.expand(Ul.coeff(lam, k)) for k in range(maxdeg + 1)}


def euler(U):
    return sp.expand(x * sp.diff(U, x) + y * sp.diff(U, y) + z * sp.diff(U, z))


ok = True


def check(name, cond):
    global ok
    print(('OK  ' if cond else 'FAIL') + '  ' + name)
    ok = ok and bool(cond)


# ---------------- Пример 1 ----------------
A = x**2 - z**2
B = y**2 - z**2
U1 = A**2 + B**2 + z**5
w = sp.Matrix([1, 1, -1]) / sp.sqrt(3)
e1 = sp.Matrix([1, -1, 0]) / sp.sqrt(2)
e2 = sp.Matrix([1, 1, 2]) / sp.sqrt(6)
check('ex1: e1,e2 ortho to w*', sp.simplify(e1.dot(w)) == 0 and sp.simplify(e2.dot(w)) == 0 and sp.simplify(e1.dot(e2)) == 0)
u4 = A**2 + B**2
D2 = sp.hessian(u4, (x, y, z)).subs({x: w[0], y: w[1], z: w[2]})
E = sp.Matrix.hstack(e1, e2)
H = sp.simplify(E.T * D2 * E)
check('ex1: H = diag(8/3, 8)', H == sp.diag(sp.Rational(8, 3), 8))
gradU = [sp.diff(U1, v) for v in (x, y, z)]
check('ex1: dU/dx = 4xA', sp.expand(gradU[0] - 4 * x * A) == 0)
check('ex1: dU/dy = 4yB', sp.expand(gradU[1] - 4 * y * B) == 0)
check('ex1: dU/dz = -4zA-4zB+5z^4', sp.expand(gradU[2] - (-4 * z * A - 4 * z * B + 5 * z**4)) == 0)
# случаи: A=B=0 ; A=0,y=0 ; x=0,B=0 ; x=y=0
dz = gradU[2]
c2 = sp.factor(dz.subs({x**2: z**2}).subs(y, 0))
c2 = sp.factor(sp.expand((-4 * z * 0 - 4 * z * (0 - z**2) + 5 * z**4)))
check('ex1: case A=0,y=0 -> z^3(4+5z)', sp.expand(c2 - z**3 * (4 + 5 * z)) == 0)
c4 = sp.expand(dz.subs({x: 0, y: 0}))
check('ex1: case x=y=0 -> z^3(8+5z)', sp.expand(c4 - z**3 * (8 + 5 * z)) == 0)
check('ex1: U(t w*) = -3^{-5/2} t^5', sp.simplify(U1.subs({x: t * w[0], y: t * w[1], z: t * w[2]}) + 3**sp.Rational(-5, 2) * t**5) == 0)
check('ex1: E U = 4U + z^5', sp.expand(euler(U1) - 4 * U1 - z**5) == 0)

# ---------------- Пример 2 ----------------
P1 = x**2 - z**2 + z**3
P2 = y**2 - z**2
U2 = sp.expand(P1**2 + P2**2 + z**7)
hp = homog_parts(U2, (x, y, z), 8)
check('ex2: u4 = A^2+B^2', sp.expand(hp[4] - (A**2 + B**2)) == 0)
check('ex2: u5 = 2 A z^3', sp.expand(hp[5] - 2 * A * z**3) == 0)
check('ex2: u6 = z^6', sp.expand(hp[6] - z**6) == 0)
check('ex2: u7 = z^7', sp.expand(hp[7] - z**7) == 0)
g = [sp.diff(U2, v) for v in (x, y, z)]
check('ex2: dU/dx = 4xP1', sp.expand(g[0] - 4 * x * P1) == 0)
check('ex2: dU/dy = 4yP2', sp.expand(g[1] - 4 * y * P2) == 0)
dz2 = sp.expand(2 * P1 * sp.diff(P1, z) + 2 * P2 * sp.diff(P2, z) + 7 * z**6)
check('ex2: dU/dz formula', sp.expand(g[2] - dz2) == 0)
# case P1=0,y=0: P2=-z^2
case2 = sp.expand(2 * 0 * 1 + 2 * (-z**2) * (-2 * z) + 7 * z**6)
check('ex2: case P1=0,y=0 -> z^3(7z^3+4)', sp.expand(case2 - z**3 * (7 * z**3 + 4)) == 0)
# case x=0,P2=0: P1 = -z^2+z^3
case3 = sp.expand(2 * (-z**2 + z**3) * (-2 * z + 3 * z**2) + 7 * z**6)
check('ex2: case x=0,P2=0 -> z^3(7z^3+6z^2-10z+4)', sp.expand(case3 - z**3 * (7 * z**3 + 6 * z**2 - 10 * z + 4)) == 0)
case4 = sp.expand(g[2].subs({x: 0, y: 0}))
check('ex2: case x=y=0 -> z^3(7z^3+6z^2-10z+8)', sp.expand(case4 - z**3 * (7 * z**3 + 6 * z**2 - 10 * z + 8)) == 0)
for poly in [7 * z**3 + 4, 7 * z**3 + 6 * z**2 - 10 * z + 4, 7 * z**3 + 6 * z**2 - 10 * z + 8]:
    r = [complex(rr) for rr in sp.Poly(poly, z).nroots()]
    print('    roots', poly, [round(abs(rr), 4) for rr in r])
check('ex2: E U = 4U + 2 z^3 P1 + 3 z^7', sp.expand(euler(U2) - 4 * U2 - 2 * z**3 * P1 - 3 * z**7) == 0)
# семейство Четаева
T = sp.Symbol('T', positive=True)  # T = tau^{1/2}
qx = sp.sqrt(T**4 + T**6 - T**7 / 2)
sub = {x: qx, y: T**2, z: -T**2}
check('ex2 family: P1 = -tau^{7/2}/2', sp.simplify(P1.subs(sub) + T**7 / 2) == 0)
check('ex2 family: P2 = 0', sp.simplify(P2.subs(sub)) == 0)
check('ex2 family: U = -3/4 tau^7', sp.simplify(U2.subs(sub) + sp.Rational(3, 4) * T**14) == 0)
check('ex2 family: E U = tau^{13/2} - 6 tau^7', sp.simplify(euler(U2).subs(sub) - (T**13 - 6 * T**14)) == 0)
# y* first order for ex2: -H^{-1} b1
u5 = hp[5]
grad5 = sp.Matrix([sp.diff(u5, v) for v in (x, y, z)]).subs({x: w[0], y: w[1], z: w[2]})
b1 = E.T * grad5
ystar1 = sp.simplify(-H.inv() * b1)
check('ex2: y*_1 = (sqrt2/12, sqrt6/36)', sp.simplify(ystar1 - sp.Matrix([sp.sqrt(2) / 12, sp.sqrt(6) / 36])) == sp.zeros(2, 1))
# u_5 restricted to Sigma = 0 (g5 = u5|Sigma since A=0) and g6 = u6 - 1/2 b1^T H^-1 b1
g6 = sp.simplify(hp[6].subs({x: w[0], y: w[1], z: w[2]}) - sp.Rational(1, 2) * (b1.T * H.inv() * b1)[0])
check('ex2: g6(w*) = u6 - 1/2 b^T H^-1 b = 0', g6 == 0)

# ---------------- Пример 3 ----------------
Q0 = x**2 + y**2 - z**2
P = Q0 + z**3
u7 = x * z**6 + x * y * z**5 + sp.Rational(1, 2) * z**7
U3 = sp.expand(P**2 + u7)
hp3 = homog_parts(U3, (x, y, z), 8)
check('ex3: u4 = Q0^2', sp.expand(hp3[4] - Q0**2) == 0)
check('ex3: u5 = 2 Q0 z^3', sp.expand(hp3[5] - 2 * Q0 * z**3) == 0)
check('ex3: u6 = z^6', sp.expand(hp3[6] - z**6) == 0)
check('ex3: u7', sp.expand(hp3[7] - u7) == 0)
ph = sp.Symbol('phi', real=True)
Gp = sp.simplify(u7.subs({x: sp.cos(ph) / sp.sqrt(2), y: sp.sin(ph) / sp.sqrt(2), z: 1 / sp.sqrt(2)}))
Gm = sp.simplify(u7.subs({x: sp.cos(ph) / sp.sqrt(2), y: sp.sin(ph) / sp.sqrt(2), z: -1 / sp.sqrt(2)}))
check('ex3: G+ formula', sp.simplify(sp.expand_trig(Gp - sp.sqrt(2) / 32 * (1 + 2 * sp.cos(ph) + sp.sin(2 * ph)))) == 0)
check('ex3: G- formula', sp.simplify(sp.expand_trig(Gm - sp.sqrt(2) / 32 * (2 * sp.cos(ph) - sp.sin(2 * ph) - 1))) == 0)
# g5 = u5|Sigma = 0, g6 = u6 - 1/2 b1^2/h_n with b1 = <grad u5, n>; на Sigma u5 = 2Q0 z^3, grad u5 = 2 z^3 grad Q0
# h_n = 8, <grad Q0, n> = +-2 -> b1 = +-4 z^3, b1^2/(2*8) = 16 z^6/16 = z^6 = u6 -> g6 = 0
for sgn in (1, -1):
    wv = sp.Matrix([sp.cos(ph) / sp.sqrt(2), sp.sin(ph) / sp.sqrt(2), sgn / sp.sqrt(2)])
    gq = sp.Matrix([sp.diff(Q0, v) for v in (x, y, z)]).subs({x: wv[0], y: wv[1], z: wv[2]})
    nvec = sp.simplify(gq / sp.sqrt(sp.simplify(gq.dot(gq))))
    D2 = sp.hessian(hp3[4], (x, y, z)).subs({x: wv[0], y: wv[1], z: wv[2]})
    hn = sp.simplify((nvec.T * D2 * nvec)[0])
    g5v = sp.Matrix([sp.diff(hp3[5], v) for v in (x, y, z)]).subs({x: wv[0], y: wv[1], z: wv[2]})
    bb = sp.simplify(g5v.dot(nvec))
    g6 = sp.simplify(hp3[6].subs({x: wv[0], y: wv[1], z: wv[2]}) - bb**2 / (2 * hn))
    check(f'ex3 sgn={sgn}: h_n = 8, |gradQ0|=2, g5=0, g6 = 0', hn == 8 and sp.simplify(gq.dot(gq)) == 4
          and sp.simplify(hp3[5].subs({x: wv[0], y: wv[1], z: wv[2]})) == 0 and g6 == 0)
dGp = sp.diff(sp.sqrt(2) / 32 * (1 + 2 * sp.cos(ph) + sp.sin(2 * ph)), ph)
dGm = sp.diff(sp.sqrt(2) / 32 * (2 * sp.cos(ph) - sp.sin(2 * ph) - 1), ph)
Gpf = sp.sqrt(2) / 32 * (1 + 2 * sp.cos(ph) + sp.sin(2 * ph))
Gmf = sp.sqrt(2) / 32 * (2 * sp.cos(ph) - sp.sin(2 * ph) - 1)
for pt in [sp.pi / 6, 5 * sp.pi / 6, 3 * sp.pi / 2]:
    print('    G+ crit', pt, sp.simplify(dGp.subs(ph, pt)), sp.nsimplify(sp.simplify(Gpf.subs(ph, pt))), float(Gpf.subs(ph, pt)))
for pt in [sp.pi / 2, 7 * sp.pi / 6, 11 * sp.pi / 6]:
    print('    G- crit', pt, sp.simplify(dGm.subs(ph, pt)), sp.simplify(Gmf.subs(ph, pt)), float(Gmf.subs(ph, pt)))
# все критические точки на [0,2pi): численно
import numpy as np
for nm, f in (('G+', Gpf), ('G-', Gmf)):
    fl = sp.lambdify(ph, sp.diff(f, ph), 'numpy')
    grid = np.linspace(0, 2 * np.pi, 200001)
    vals = fl(grid)
    sc = np.where(np.sign(vals[:-1]) * np.sign(vals[1:]) <= 0)[0]
    print('   ', nm, 'sign changes / zeros of derivative near', sorted(set(np.round(grid[sc], 3))))
    fv = sp.lambdify(ph, f, 'numpy')(grid)
    neg = fv < 0
    # число дуг отрицательности на окружности
    arcs = np.sum(neg[1:] & ~neg[:-1]) + (1 if (neg[0] and not neg[-1]) else 0)
    print('   ', nm, 'number of negative arcs =', arcs, ' min =', fv.min())
d2 = sp.simplify(sp.diff(Gpf, ph, 2).subs(ph, 5 * sp.pi / 6))
check('ex3: d2G+/dphi2 (5pi/6) = 3 sqrt6/32', sp.simplify(d2 - 3 * sp.sqrt(6) / 32) == 0)
Gstar = sp.simplify(Gpf.subs(ph, 5 * sp.pi / 6))
check('ex3: G+(5pi/6) = sqrt2(2-3sqrt3)/64', sp.simplify(Gstar - sp.sqrt(2) * (2 - 3 * sp.sqrt(3)) / 64) == 0)
Gpp = 2 * d2
check('ex3: G" (natural) = 3sqrt6/16', sp.simplify(Gpp - 3 * sp.sqrt(6) / 16) == 0)
val = sp.simplify(Gpp + 7 * Gstar)
check('ex3: G"+7G = (14sqrt2-9sqrt6)/64 < 0', sp.simplify(val - (14 * sp.sqrt(2) - 9 * sp.sqrt(6)) / 64) == 0 and float(val) < 0)
a0 = -Gstar
lam0 = sp.Rational(1, 4) * sp.Min(Gpp, 8)
kap = 7 * lam0 / (a0 * (sp.Rational(15, 8) * sp.sqrt(3) * 7 + 2 * sp.sqrt(2))**2)
print('    kappa bound (U3) =', float(kap))
check('ex3: E U = 4U + 2 z^3 P + 3 u7', sp.expand(euler(U3) - 4 * U3 - 2 * z**3 * P - 3 * u7) == 0)
# комплексные прямые z=0, x = +- i y
X, Y, Z = sp.symbols('X Y Z')
U3c = U3.subs({x: X, y: Y, z: Z})
for sg in (1, -1):
    grad = [sp.expand(sp.diff(U3c, v).subs({Z: 0, X: sg * sp.I * Y})) for v in (X, Y, Z)]
    check(f'ex3: grad U = 0 on z=0, x={sg}iy', all(gg == 0 for gg in grad))
check('ex3: U(t w*) = t^6/8 + O(t^7)', sp.series(U3.subs({x: t * sp.cos(5 * sp.pi / 6) / sp.sqrt(2), y: t * sp.sin(5 * sp.pi / 6) / sp.sqrt(2), z: t / sp.sqrt(2)}), t, 0, 7).removeO().equals(t**6 / 8))

# ---------------- формула g_{m+2} на случайном примере ----------------
random.seed(1)
# n=3, d=0, omega = e_z, u_4 = (x^2+y^2)*(a x^2 + b y^2 + ...)? проще: u_2 = x^2 + 2y^2 + xy (m=2), omega=(0,0,1)
m = 2
u2 = x**2 + x * y + 2 * y**2
u3 = sum(random.randint(-3, 3) * x**i * y**j * z**(3 - i - j) for i in range(4) for j in range(4 - i))
u4r = sum(random.randint(-3, 3) * x**i * y**j * z**(4 - i - j) for i in range(5) for j in range(5 - i))
y1, y2 = sp.symbols('y1 y2')
v = {x: y1, y: y2, z: 1}
phi = sp.expand(u2.subs(v) + s * u3.subs(v) + s**2 * u4r.subs(v))
# решаем d phi / dy = 0 рядом по s до порядка 2
c1, c2, d1, d2_ = sp.symbols('c1 c2 d1 d2')
ys = {y1: c1 * s + d1 * s**2, y2: c2 * s + d2_ * s**2}
eqs = [sp.expand(sp.diff(phi, yy).subs(ys)) for yy in (y1, y2)]
sol1 = sp.solve([e.coeff(s, 1) for e in eqs], [c1, c2], dict=True)[0]
eqs2 = [sp.expand(e.subs(sol1)).coeff(s, 2) for e in eqs]
sol2 = sp.solve(eqs2, [d1, d2_], dict=True)[0]
Rser = sp.expand(sp.series(phi.subs(ys).subs(sol1).subs(sol2), s, 0, 3).removeO())
Hm = sp.hessian(u2.subs(v), (y1, y2))
bvec = sp.Matrix([sp.diff(u3.subs(v), yy).subs({y1: 0, y2: 0}) for yy in (y1, y2)])
g4_formula = u4r.subs({x: 0, y: 0, z: 1}) - sp.Rational(1, 2) * (bvec.T * Hm.inv() * bvec)[0]
check('g_{m+1} = u_{m+1}(omega)', sp.simplify(Rser.coeff(s, 1) - u3.subs({x: 0, y: 0, z: 1})) == 0)
check('g_{m+2} = u_{m+2} - 1/2 b^T H^-1 b', sp.simplify(Rser.coeff(s, 2) - g4_formula) == 0)

print('ALL OK' if ok else 'SOME FAIL')
