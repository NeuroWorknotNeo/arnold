"""R36: независимая символьная проверка выкладок §5 записки
notes/prover/2026-10-21-point-degenerate.md (теорема C', следствия R, X, SV, S, E, примеры).
[Эксперимент] sympy, точная арифметика. Запуск: ~/venv/bin/python check_symbolic.py
"""
import sympy as sp

x, y, z, s, b1, b2, t = sp.symbols('x y z s b1 b2 t', real=True)
alpha, e, N = sp.symbols('alpha e N', positive=True)
ok = True


def check(name, expr):
    global ok
    v = sp.simplify(sp.expand(expr))
    flag = (v == 0)
    ok = ok and flag
    print(f"[{'OK' if flag else 'FAIL'}] {name}: {v if not flag else 0}")


def grad(f):
    return sp.Matrix([sp.diff(f, b1), sp.diff(f, b2)])


def lie(xi, f):
    return sp.expand(xi[0] * sp.diff(f, b1) + xi[1] * sp.diff(f, b2))


# --- C': оператор E = xi.grad_b - (s/N) d_s на s^{-e} R(b)
R = sp.Function('R')(b1, b2)
xi1 = sp.Function('xi1')(b1, b2)
xi2 = sp.Function('xi2')(b1, b2)
expr = s**(-e) * R
Eexpr = xi1 * sp.diff(expr, b1) + xi2 * sp.diff(expr, b2) - s / N * sp.diff(expr, s)
check("C': E(s^-e R) = s^-e (xi.gradR + e/N R)",
      Eexpr - s**(-e) * (xi1 * sp.diff(R, b1) + xi2 * sp.diff(R, b2) + e / N * R))

# --- Пример Lambda: U = x^4 - k x^2 y z + y^2 z^2 + y^4 - z^8 + x z^7, луч +e_z, c=(2,3), N=1, beta=8
k = sp.Rational(199, 100)
U = x**4 - k * x**2 * y * z + y**2 * z**2 + y**4 - z**8 + x * z**7
F = sp.expand(U.subs({x: z**2 * b1, y: z**3 * b2}, simultaneous=True) / z**8).subs(z, s)
Q = b1**4 - k * b1**2 * b2 + b2**2
check("Lambda: F = -1 + Q + s b1 + s^4 b2^4", F - (-1 + Q + s * b1 + s**4 * b2**4))
u4 = x**4 - k * x**2 * y * z + y**2 * z**2 + y**4
check("Lambda: u4 = (yz-k/2 x^2)^2 + (1-k^2/4) x^4 + y^4",
      u4 - ((y * z - k / 2 * x**2)**2 + (1 - k**2 / 4) * x**4 + y**4))
check("Lambda: <(C-I)b, gradQ> = 4Q", lie((b1, 2 * b2), Q) - 4 * Q)
CQ = lie((2 * b1, 3 * b2), Q)
check("Lambda: <Cb,gradQ> = 8b1^4 - 7k b1^2 b2 + 6 b2^2", CQ - (8 * b1**4 - 7 * k * b1**2 * b2 + 6 * b2**2))
print("   discriminant 49k^2-192 =", 49 * k**2 - 192)
pt = {b1: 1, b2: sp.Rational(116, 100)}
print("   at (1,1.16): Q =", Q.subs(pt), " <Cb,gradQ> =", CQ.subs(pt))
print("   1 - k^2/4 =", 1 - k**2 / 4)

# --- Пример X: c=(2,5/2), N=2, beta=12, s=z^{1/2}
UX = x**6 + y**6 + y**4 * z**2 + x**2 * y**2 * z**2 - z**12 + x * z**11
FX = sp.expand(UX.subs({x: s**4 * b1, y: s**5 * b2, z: s**2}, simultaneous=True) / s**24)
check("X: F", FX - (-1 + b1**6 + b2**4 + s**(-2) * b1**2 * b2**2 + s**2 * b1 + s**6 * b2**6))
QX = b1**6 + b2**4
check("X: <Cb,gradQ> - 10Q = 2 b1^6", lie((2 * b1, sp.Rational(5, 2) * b2), QX) - 10 * QX - 2 * b1**6)
cross = b1**2 * b2**2
check("X: <Cb,grad cross> + (e/N) cross = 10 cross  (e=2,N=2)",
      lie((2 * b1, sp.Rational(5, 2) * b2), cross) + 1 * cross - 10 * cross)
check("X: dU/dy factorization", sp.diff(UX, y) - 2 * y * (3 * y**4 + 2 * y**2 * z**2 + x**2 * z**2))
check("X: dU/dx at y=0", sp.diff(UX, x).subs(y, 0) - (6 * x**5 + z**11))
check("X: dU/dz at y=0", sp.diff(UX, z).subs(y, 0) - z**10 * (11 * x - 12 * z))
# Утверждение: для gamma=0 нет весов c с phi(c)=beta=12 и изолированным нулём Q_c.
c1, c2 = sp.symbols('c1 c2', positive=True)
monos = [(0, 6, 0), (0, 0, 6), (2, 0, 4), (2, 2, 2), (11, 1, 0)]  # (степень z, степень x, степень y)
Ls = [kz + c1 * ax + c2 * ay for kz, ax, ay in monos]
print("   X levels L_c:", Ls)
# чистые степени: b1 -- x^6 (6c1) или x z^11 (11+c1); b2 -- y^6 (6c2) или y^4 z^2 (2+4c2)
for p1 in [(6 * c1, 'x^6'), (11 + c1, 'xz^11')]:
    for p2 in [(6 * c2, 'y^6'), (2 + 4 * c2, 'y^4z^2')]:
        sol = sp.solve([p1[0] - 12, p2[0] - 12], [c1, c2], dict=True)
        for so in sol:
            vals = [sp.nsimplify(L.subs(so)) for L in Ls]
            print(f"   pure {p1[1]},{p2[1]}: c={so[c1]},{so[c2]}; levels={vals}; min={min(vals)}")

# --- SV: общий phi, A, B
phi = sp.Function('phi')(b1)
A = sp.Function('A')(b1, b2)
tt = b2 - phi
xiSV = (alpha * b1, alpha * (b1 * sp.diff(phi, b1) + 2 * tt))
check("SV: xi.grad b1 = alpha b1", lie(xiSV, b1) - alpha * b1)
check("SV: xi.grad t = 2 alpha t", lie(xiSV, tt) - 2 * alpha * tt)
check("SV: xi.grad(A t^2) = (4 alpha A + xi.gradA) t^2",
      lie(xiSV, A * tt**2) - (4 * alpha * A + lie(xiSV, A)) * tt**2)
DxiSV = sp.Matrix([[sp.diff(xiSV[0], b1), sp.diff(xiSV[0], b2)], [sp.diff(xiSV[1], b1), sp.diff(xiSV[1], b2)]])
print("   SV: D xi =", sp.simplify(DxiSV))

# Пример SV
USV = z**4 * (y - x**2)**2 + x**6 + y**6 - z**12 + x * z**11
FSV = sp.expand(USV.subs({x: z**2 * b1, y: z**4 * b2}, simultaneous=True) / z**12).subs(z, s)
check("SV: F", FSV - (-1 + (b2 - b1**2)**2 + b1**6 + s * b1 + s**12 * b2**6))
QSV = (b2 - b1**2)**2 + b1**6
check("SV: <Cb,gradQ> - 8Q = 4 b1^6", lie((2 * b1, 4 * b2), QSV) - 8 * QSV - 4 * b1**6)
check("SV: u6", sp.expand(USV).as_poly(x, y, z).homogenize(sp.Symbol('h')) is not None and 0)
u6 = sum(term for term in sp.Add.make_args(sp.expand(USV)) if sp.Poly(term, x, y, z).total_degree() == 6)
check("SV: u6 = x^6+y^6+y^2 z^4", u6 - (x**6 + y**6 + y**2 * z**4))

# Пример SH: прямая карта и карта со сдвигом
USH = z**4 * (y - x**2 - x * z)**2 + x**6 + y**6 - z**12 + x * z**11
u6h = sum(term for term in sp.Add.make_args(sp.expand(USH)) if sp.Poly(term, x, y, z).total_degree() == 6)
check("SH: u6 = x^6+y^6+y^2 z^4", u6h - (x**6 + y**6 + y**2 * z**4))
FSHd = sp.expand(USH.subs({x: z**2 * b1, y: z**4 * b2}, simultaneous=True) / z**12).subs(z, s)
lv = sp.collect(FSHd, s, evaluate=False)
print("   SH direct map levels:", {kk: sp.factor(vv) for kk, vv in lv.items()})
check("SH direct: s^-2 b1^2 + s^-1(2b1^3-2b1b2) + (b2-b1^2)^2 is (b2-b1^2-b1/s)^2",
      (s**-2 * b1**2 + s**-1 * (2 * b1**3 - 2 * b1 * b2) + (b2 - b1**2)**2) - (b2 - b1**2 - b1 / s)**2)
# L(z) = [[1,0],[z,1]]: (x,y) = L (z^2 b1, z^4 b2)
FSHs = sp.expand(USH.subs({x: z**2 * b1, y: z * z**2 * b1 + z**4 * b2}, simultaneous=True) / z**12).subs(z, s)
check("SH shifted: F", FSHs - (-1 + (b2 - b1**2)**2 + b1**6 + s * b1 + s**6 * (b1 + s * b2)**6))

# --- R (кольцо): h = (|w|^2 - z^3)^2, c=(3/2,3/2), d=6, beta=8, N=2
UR = (x**2 + y**2 - z**3)**2 - z**8 + x * z**8
lam = sp.symbols('lam', positive=True)
h = (x**2 + y**2 - z**3)**2
check("R: h quasihomogeneous deg 6", h.subs({x: lam**sp.Rational(3, 2) * x, y: lam**sp.Rational(3, 2) * y,
                                            z: lam * z}, simultaneous=True) - lam**6 * h)
FR = sp.expand(UR.subs({x: s**3 * b1, y: s**3 * b2, z: s**2}, simultaneous=True) / s**16)
check("R: F = -1 + s^-4 (|b|^2-1)^2 + s^3 b1", FR - (-1 + s**(-4) * (b1**2 + b2**2 - 1)**2 + s**3 * b1))
# плоскость y=0: x = -z^{3/2} + z^{5/2} b, s = z^{1/2}
bb = sp.symbols('b', real=True)
FRp = sp.expand(UR.subs({y: 0}).subs({x: -s**3 + s**5 * bb, z: s**2}, simultaneous=True) / s**16)
check("R plane: F = 4b^2-1-4s^2b^3+s^4b^4+s^5b-s^3", FRp - (4 * bb**2 - 1 - 4 * s**2 * bb**3 + s**4 * bb**4 + s**5 * bb - s**3))
# изолированность над R: ветвь y=0
gx = sp.diff(UR, x).subs(y, 0)
gz = sp.diff(UR, z).subs(y, 0)
print("   R, y=0: dU/dx =", sp.factor(gx), "; dU/dz =", sp.factor(gz))
res = sp.resultant(gx, gz, x)
print("   resultant_x =", sp.factor(res))
# критические точки над C: z=0, x^2+y^2=0
gR = [sp.diff(UR, v) for v in (x, y, z)]
print("   R grad on z=0, y=i x:", [sp.simplify(g.subs({z: 0, y: sp.I * x})) for g in gR])

# --- E: c=(2,2), N=1, beta=24
UE = x**12 + y**12 + z**4 * (x**2 - y * z**2)**2 * (x**3 - y * z**4)**2 - z**24 + x * z**23
FE = sp.expand(UE.subs({x: z**2 * b1, y: z**2 * b2}, simultaneous=True) / z**24).subs(z, s)
QE = (b2 - b1**2)**2 * (b2 - b1**3)**2 + b1**12 + b2**12
check("E: F = -1 + Q + s b1", FE - (-1 + QE + s * b1))
low = sp.Poly(sp.expand(QE), b1, b2)
dmin = min(sum(m) for m in low.monoms())
Qd = sum(c * b1**m[0] * b2**m[1] for m, c in zip(low.monoms(), low.coeffs()) if sum(m) == dmin)
print("   E: d =", dmin, " Q_d =", Qd)
u12 = sum(term for term in sp.Add.make_args(sp.expand(UE)) if sp.Poly(term, x, y, z).total_degree() == 12)
check("E: u12 = x^12+y^12", u12 - (x**12 + y**12))
mindeg = min(sp.Poly(term, x, y, z).total_degree() for term in sp.Add.make_args(sp.expand(UE)) if term not in (x**12, y**12))
print("   E: min degree of other monomials =", mindeg)
# (Q1) для E: все уровни L_c >= 24 при c=(2,2)
levels = set()
for term in sp.Add.make_args(sp.expand(UE)):
    pz = sp.Poly(term, x, y, z)
    (ax, ay, az), = pz.monoms()
    levels.add(az + 2 * ax + 2 * ay)
print("   E: levels L_c (c=(2,2)) =", sorted(levels))

# --- E (следствие): производная сглаженного поля
chi = sp.Function('chi')(b1, b2)
kap = sp.Function('kappa')(b1, b2)
xi0 = sp.Matrix([b1, b2 + kap])
xie = sp.Matrix([b1, b2 + (1 - chi) * kap])
J = lambda v: v.jacobian([b1, b2])
lhs = J(xie)
rhs = (1 - chi) * J(xi0) + chi * sp.eye(2) - sp.Matrix([[0, 0], [kap * sp.diff(chi, b1), kap * sp.diff(chi, b2)]])
check("E: D xi^eps formula", sp.simplify(lhs - rhs).norm())
# xi^eps = (1-chi) xi0 + chi b
check("E: xi^eps = (1-chi)xi0 + chi b", (xie - ((1 - chi) * xi0 + chi * sp.Matrix([b1, b2]))).norm())

# --- S: s d_s F_> для F_> = x^{-beta} r(x, x^c b), N=1 (конкретная "общая" r)
X_, B1, B2, beta, cc1, cc2 = sp.symbols('X B1 B2 beta cc1 cc2', positive=True)
Y1, Y2 = sp.symbols('Y1 Y2')
pp, qq, ww = sp.symbols('pp qq ww', positive=True)
rr = X_**pp * Y1**qq * Y2**ww + sp.sin(X_ * Y1) * Y2**2 + sp.exp(X_ * Y2) * Y1
sub = {Y1: X_**cc1 * B1, Y2: X_**cc2 * B2}
Fg = X_**(-beta) * rr.subs(sub)
lhs = X_ * sp.diff(Fg, X_)
rhs = (-beta * X_**(-beta) * rr + X_**(-beta) * (X_ * sp.diff(rr, X_) + cc1 * Y1 * sp.diff(rr, Y1)
                                                   + cc2 * Y2 * sp.diff(rr, Y2))).subs(sub)
check("S: x d_x F_> = -beta x^-beta r + x^-beta (x r_x + <Cy, grad_y r>)", sp.simplify(sp.expand(lhs - rhs)))

# --- K0: уровень c* = (beta-m+2)/2; моном |alpha|>=3 на уровне <= beta имел бы порядок < m
mm, bt, aa = sp.symbols('m beta a', positive=True)
cst = (bt - mm + 2) / 2
print("   K0: order bound for |alpha|=a at level beta:", sp.simplify(bt - (cst - 1) * aa), "; at a=3 minus m:",
      sp.factor(sp.simplify(bt - (cst - 1) * 3 - mm)))

# --- Пример SV-поля там, где Cb не работает: c=(2,3), Q=(b2-b1^2)^2+b1^6
Qs = (b2 - b1**2)**2 + b1**6
CQs = lie((2 * b1, 3 * b2), Qs)
val = CQs.subs({b2: b1**2 + b1**2 / 6})
print("   c=(2,3): <Cb,gradQ> at b2=b1^2(1+1/6):", sp.factor(val))
xiA = (b1, b1 * 2 * b1 + 2 * (b2 - b1**2))  # alpha=1, phi=b1^2
check("SV-field on Q=(b2-b1^2)^2+b1^6: xi.gradQ = 4 t^2 + 6 b1^6",
      lie(xiA, Qs) - (4 * (b2 - b1**2)**2 + 6 * b1**6))

print("ALL OK" if ok else "SOME FAILED")
