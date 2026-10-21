# [Эксперимент] Символьные проверки к замечаниям results/006-angle-lemma.md.
# Это свидетельство, а не доказательство. Запуск: ~/venv/bin/python check_remarks.py
import sympy as sp

x, y, z, t, u, e = sp.symbols('x y z t u e', real=True)

def grad(U, V):
    return [sp.diff(U, v) for v in V]

def radial(U, V):
    return sp.expand(sum(v*d for v, d in zip(V, grad(U, V))))

print("1. Однородный U степени m: <x,grad U> = m U (Эйлер)")
for U, m in [(x**3 - 3*x*y**2, 3), (x**2*y - y**2*z + z**3, 3), (x**4 - y**2*z**2 + x*y*z**2, 4)]:
    print("   ", U, ":", sp.simplify(radial(U, [x, y, z]) - m*U) == 0)

print("2. <x,grad U> - m U = sum_k (k-m) u_k для U = u_2 + u_3 + u_5")
u2, u3, u5 = x**2 - y**2 + z**2, x*y*z, x**5 + y**4*z
U = u2 + u3 + u5
print("   ", sp.expand(radial(U, [x, y, z]) - 2*U - (u3 + 3*u5)) == 0)

print("3. Квазиоднородный пример U=(y-x^2)(y-2x^2): на y=x^2")
U = (y - x**2)*(y - 2*x**2)
gU = grad(U, [x, y])
print("    grad U =", [sp.factor(c.subs(y, x**2)) for c in gU])
print("    <x,grad U> =", sp.factor((x*gU[0] + y*gU[1]).subs(y, x**2)))
print("    U(x, x^2(1+e)):", sp.factor(U.subs(y, x**2*(1 + e))), "(<0 при 0<e<1)")

print("4. Дробный показатель: U=(y^2-x^3)^2-x^10, точка p=(x, x^{3/2}(1-x^2/4)), x=u^2")
U = (y**2 - x**3)**2 - x**10
gx, gy = grad(U, [x, y])
X, Y = u**2, u**3*(1 - u**4/4)
Up = sp.expand(U.subs({x: X, y: Y}))
print("    U(p) =", sp.series(Up, u, 0, 23).removeO().as_ordered_terms()[-1], "+ ... (главный член)")
num = sp.expand((x*gx + y*gy).subs({x: X, y: Y}))
GX, GY = sp.expand(gx.subs({x: X, y: Y})), sp.expand(gy.subs({x: X, y: Y}))
# g = num / (|p| |grad U|); главные члены
print("    <p,grad U> ~", sp.series(num, u, 0, 18).removeO().as_ordered_terms()[-1])
print("    grad_x ~", sp.series(GX, u, 0, 16).removeO().as_ordered_terms()[-1],
      "; grad_y ~", sp.series(GY, u, 0, 16).removeO().as_ordered_terms()[-1])
g = num / (sp.sqrt(X**2 + Y**2) * sp.sqrt(GX**2 + GY**2))
gs = sp.series(sp.simplify(g / u), u, 0, 3)
print("    g(p)/sqrt(x) =", gs, "  (x = u^2, т.е. g ~ (1/2) x^{1/2})")

print("5. Радиальный C^oo пример f(r)=exp(-1/r^2) sin(1/r): g = sign f'(r)")
r = sp.symbols('r', positive=True)
f = sp.exp(-1/r**2)*sp.sin(1/r)
fp = sp.diff(f, r)
k = 3
ra, rb = 1/((2*k + 2)*sp.pi), 1/((2*k + 1)*sp.pi)   # отрицательный слой
import mpmath as mp
mp.mp.dps = 30
F = sp.lambdify(r, f, 'mpmath'); FP = sp.lambdify(r, fp, 'mpmath')
grid = [ra + (rb - ra)*sp.Rational(j, 400) for j in range(1, 400)]
vals = [(float(F(sp.N(q, 30))), float(FP(sp.N(q, 30)))) for q in grid]
print("    слой k=3: max f =", max(v[0] for v in vals), "(<0);",
      "есть точки с f'>0:", any(v[1] > 0 for v in vals), "; с f'<0:", any(v[1] < 0 for v in vals))
