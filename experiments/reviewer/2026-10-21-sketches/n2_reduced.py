# [Эксперимент/символьно] n2-sketch: «изолированность ⇒ U приведена» — проверка контрпримеров
import sympy as sp
x, y = sp.symbols('x y', real=True)
for U in [x*(x**2+y**2)**2, x*((y-x**2)**2 + x**6)**2]:
    Ux, Uy = sp.diff(U, x), sp.diff(U, y)
    print("U =", U)
    print("  factor:", sp.factor_list(sp.expand(U)))
    # real critical points: solve via resultant / Groebner
    G = sp.groebner([sp.expand(Ux), sp.expand(Uy)], y, x, order='lex')
    print("  Groebner last (in x):", sp.factor(G.exprs[-1]))
    sols = sp.solve([Ux, Uy], [x, y], dict=True)
    print("  solutions:", sols)
