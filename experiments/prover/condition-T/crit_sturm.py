"""[Эксперимент, точная арифметика] Число вещественных корней результанта Res_b1(d1 Qt, d2 Qt) по b2:
факторизация (python-flint) и подсчёт вещественных корней каждого множителя по Штурму (sympy count_roots)."""
import sympy as sp
import flint
b1, b2 = sp.symbols('b1 b2', real=True)
A = (b1 - b2**2)**2 + b2**8
B = (b1 - b2**2 - b2**3)**2 + b2**8
for name, Qt in (('Qt1', sp.expand((b1 - b2**2)**2 + b2**8 + b1**12)), ('Qt2', sp.expand(A * B + b1**24))):
    ctx = flint.fmpz_mpoly_ctx.get(('b1', 'b2'), 'lex')
    F = [ctx.from_dict({k: int(v) for k, v in sp.Poly(sp.diff(Qt, w), b1, b2).as_dict().items()}) for w in (b1, b2)]
    R = F[0].resultant(F[1], 'b1')
    co = {mon[1]: int(c) for mon, c in zip(R.monoms(), R.coeffs())}
    Rz = flint.fmpz_poly([co.get(i, 0) for i in range(max(co) + 1)])
    c, facs = Rz.factor()
    out = []
    for p, e in facs:
        P = sp.Poly([int(a) for a in reversed(p.coeffs())], b2)
        out.append((P.degree(), e, P.count_roots()))
    print(f'{name}: factors (degree, multiplicity, #real roots): {out}')
