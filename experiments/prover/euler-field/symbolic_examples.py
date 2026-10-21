"""[Эксперимент] Символьная проверка явных полей Эйлера для примеров из
notes/prover/2026-10-21-euler-field.md (лемма E).

Для каждого примера печатается xi.grad Q - mu*Q в виде, из которого видна
неотрицательность (сумма неотрицательных мономов или явный квадрат).
Запуск: ~/venv/bin/python symbolic_examples.py
"""
import sympy as sp

b1, b2, k, tau = sp.symbols('b1 b2 k tau', real=True)


def lie(xi, Q):
    return sp.expand(xi[0]*sp.diff(Q, b1) + xi[1]*sp.diff(Q, b2))


print("=== Пример 1: Q=(b2-b1^2)^2+b1^6, xi=(b1, b2+b1^2) [формула теоремы, chi=b1*psi'-psi=b1^2]")
Q = (b2 - b1**2)**2 + b1**6
xi = (b1, b2 + b1**2)
d = sp.factor(lie(xi, Q) - 2*Q)
print("  xi Q - 2Q =", d)

print("=== Пример 2: Q=(b2-b1^2-b1^3)^2+b1^8, xi=(b1, b2+b1^2+2b1^3)")
Q = (b2 - b1**2 - b1**3)**2 + b1**8
xi = (b1, b2 + b1**2 + 2*b1**3)
print("  xi Q - 2Q =", sp.factor(lie(xi, Q) - 2*Q))

print("=== Пример 3: Q=(b2^2-b1^4)^2+b1^10, простое поле xi=(b1, 2 b2) (веса (1,2))")
Q = (b2**2 - b1**4)**2 + b1**10
xi = (b1, 2*b2)
print("  xi Q - 8Q =", sp.factor(lie(xi, Q) - 8*Q))

print("=== Пример 4: Q=b2^2+k b1^2 b2+b1^4, xi=(b1, 2 b2)")
Q = b2**2 + k*b1**2*b2 + b1**4
xi = (b1, 2*b2)
print("  xi Q - 4Q =", sp.simplify(lie(xi, Q) - 4*Q))

print("=== Пример 5: Q=G1*G2, G1=b2^2+k b1^2 b2+b1^4, G2=b1^2+k b1 b2^2+b2^4")
print("  Одно диагональное поле lam1 b1 d1 + lam2 b2 d2 невозможно при R=min(-m,M)>=6,")
print("  где [m,M] — множество значений rho(tau)=tau g'(tau)/g(tau), g=tau^2+k tau+1.")
g = tau**2 + k*tau + 1
rho = sp.simplify(tau*sp.diff(g, tau)/g)
# критические точки rho
num = sp.numer(sp.together(sp.diff(rho, tau)))
print("  rho =", rho, ";  числитель rho' =", sp.factor(num))
for kv in [sp.Rational(19, 10), sp.Rational(197, 100), sp.Rational(199, 100)]:
    crit = sp.solve(num.subs(k, kv), tau)
    vals = [sp.nsimplify(rho.subs({k: kv, tau: c})) for c in crit]
    vals_f = [float(v) for v in vals] + [2.0]  # предел на бесконечности = 2
    m, M = min(vals_f), max(vals_f)
    print(f"  k={kv}: крит. точки {[sp.N(c, 6) for c in crit]}, m={m:.4f}, M={M:.4f}, R=min(-m,M)={min(-m, M):.4f}",
          "-> одно поле НЕВОЗМОЖНО" if min(-m, M) >= 6 else "-> критерий не срабатывает")
# проверка асимптотики xi log Q вдоль b2 = tau b1^2
lam1, lam2 = sp.symbols('lam1 lam2', real=True)
G1 = b2**2 + k*b1**2*b2 + b1**4
G2 = b1**2 + k*b1*b2**2 + b2**4
Q = G1*G2
xi = (lam1*b1, lam2*b2)
r = sp.simplify((lie(xi, Q)/Q).subs(b2, tau*b1**2))
lim = sp.simplify(sp.limit(r, b1, 0))
target = sp.simplify(6*lam1 + (lam2 - 2*lam1)*rho)
print("  lim_{b1->0} xi log Q (b2=tau b1^2) - [6 lam1 + (lam2-2lam1) rho(tau)] =", sp.simplify(lim - target))

print("=== Контрпример к анизотропному варианту: Q=A*B,")
print("    A=(x-y^2)^2+y^8, B=(x-y^2-y^3)^2+y^8 (x=b1 широкое, y=b2 узкое)")
x, y = b1, b2
A = (x - y**2)**2 + y**8
B = (x - y**2 - y**3)**2 + y**8
Q = A*B
xi = (sp.Rational(3, 2)*x - y**2/2, y/2)   # поле с d xi_2/dx = 0 (обратная анизотропия)
s1 = x - y**2
s2 = x - y**2 - y**3
print("  xi s1 - 3/2 s1 =", sp.expand(lie(xi, s1) - sp.Rational(3, 2)*s1))
print("  xi s2 - 3/2 s2 =", sp.expand(lie(xi, s2) - sp.Rational(3, 2)*s2))
print("  xi A - 3A =", sp.factor(lie(xi, A) - 3*A), ";  xi B - 3B =", sp.factor(lie(xi, B) - 3*B))
print("  => xi Q >= 6 Q, Dxi ограничена, но d xi_1/dy = -y != 0")
print("  младшая форма Q:", sp.Poly(sp.expand(Q), x, y).terms()[-1] if False else
      sp.expand(sum(t for t in sp.Add.make_args(sp.expand(Q)) if sp.Poly(t, x, y).total_degree() == 4)))

print("=== Тождества из доказательства предложения 6.2 (контрпример)")
X1, X2, sg = sp.symbols('xi1 xi2 sigma', real=True)
yp = sp.symbols('y', positive=True)
A_ = (b1 - b2**2)**2 + b2**8
B_ = (b1 - b2**2 - b2**3)**2 + b2**8
xs1 = X1 - 2*b2*X2                      # xi s1
xs2 = X1 - (2*b2 + 3*b2**2)*X2          # xi s2
logA = (X1*sp.diff(A_, b1) + X2*sp.diff(A_, b2))/A_
logB = (X1*sp.diff(B_, b1) + X2*sp.diff(B_, b2))/B_
# точки P^{+-} = (y^2 + sigma y^4, y), sigma = +-1
sub = {b1: yp**2 + sg*yp**4, b2: yp}
e1 = sp.simplify((logA - (sg*xs1/yp**4 + 4*X2/yp)).subs(sub).subs(sg**2, 1))
print("  xi log A в P^± минус (±xi s1/y^4 + 4 xi2/y):", sp.simplify(e1.subs(sg, 1)), sp.simplify(e1.subs(sg, -1)))
# точка P1 = (y^2, y)
sub1 = {b1: yp**2, b2: yp}
e2 = sp.simplify((logA - 8*X2/yp).subs(sub1))
e3 = sp.simplify((logB - (X2*(6 + 8*yp**2)/(yp*(1 + yp**2)) - 2*xs1/(yp**3*(1 + yp**2)))).subs(sub1))
print("  xi log A в P1 - 8 xi2/y =", e2, ";  xi log B в P1 - [...] =", e3)
print("  (1+3y/2)/(1+y) - (1+y/2-y^2/2) = ", sp.factor(sp.together((1 + sp.Rational(3, 2)*yp)/(1 + yp) - (1 + yp/2 - yp**2/2))))
