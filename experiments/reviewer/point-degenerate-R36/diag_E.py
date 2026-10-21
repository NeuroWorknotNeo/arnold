"""R36: пример E — диагональных полей (l1 b1, l2 b2) с xi.Q >= mu Q нет (асимптотика у подоврагов).
[Эксперимент: sympy, ряды] — выкладка, подтверждающая довод рецензента."""
import sympy as sp
b1, tau, l1, l2 = sp.symbols('b1 tau l1 l2', real=True)
b2 = sp.symbols('b2', real=True)
Q = (b2 - b1**2)**2 * (b2 - b1**3)**2 + b1**12 + b2**12
xiQ = l1 * b1 * sp.diff(Q, b1) + l2 * b2 * sp.diff(Q, b2)
for name, curve in [('b2=b1^2+tau b1^4', b1**2 + tau * b1**4), ('b2=b1^3+tau b1^4', b1**3 + tau * b1**4)]:
    q = sp.series(Q.subs(b2, curve), b1, 0, 14).removeO()
    xq = sp.series(xiQ.subs(b2, curve), b1, 0, 14).removeO()
    lq = sp.Poly(q, b1); lx = sp.Poly(xq, b1)
    def lead(p):
        for (deg,), c in sorted(zip(p.monoms(), p.coeffs())):
            c = sp.factor(c)
            if c != 0:
                return deg, c
    print(name, ': Q ~', lead(lq), ';  xi.Q ~', lead(lx))
