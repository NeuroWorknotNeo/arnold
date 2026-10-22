"""[Эксперимент, точная арифметика: python-flint] Вещественные критические точки профиля Qt2 = A*B + b1^24 модели U2.

R(b2) := Res_{b1}(d1 Qt2, d2 Qt2) in Z[b2]. Старший коэффициент d1 Qt2 по b1 — константа 24 (член 24 b1^23), поэтому
R(b2*) = 0 тогда и только тогда, когда d1 Qt2(., b2*) и d2 Qt2(., b2*) имеют общий комплексный корень по b1.
Значит, у каждой вещественной критической точки (b1*, b2*) координата b2* — вещественный корень R.
Вещественные корни R изолируются строго: разложение на неприводимые множители (fmpz_poly.factor) и
fmpz_poly.complex_roots() для каждого множителя (FLINT arb_fmpz_poly_complex_roots: строгая изоляция; вещественные корни выдаются с мнимой частью, точно равной нулю).
"""
import sympy as sp
import flint

b1, b2 = sp.symbols('b1 b2', real=True)
A = (b1 - b2**2)**2 + b2**8
B = (b1 - b2**2 - b2**3)**2 + b2**8
Qt = sp.expand(A * B + b1**24)
ctx = flint.fmpz_mpoly_ctx.get(('b1', 'b2'), 'lex')
F = [ctx.from_dict({kk: int(v) for kk, v in sp.Poly(sp.diff(Qt, w), b1, b2).as_dict().items()}) for w in (b1, b2)]
print('leading term of d1 Qt in b1:', sp.LT(sp.Poly(sp.diff(Qt, b1), b1)))
R = F[0].resultant(F[1], 'b1')
co = {mon[1]: int(c) for mon, c in zip(R.monoms(), R.coeffs())}
Rz = flint.fmpz_poly([co.get(i, 0) for i in range(max(co) + 1)])
print('deg R =', Rz.degree(), '; R not identically zero:', not Rz.is_zero())
c, facs = Rz.factor()
total_real = []
for p, e in facs:
    # arb_fmpz_poly_complex_roots: вещественные корни выдаются с мнимой частью, равной нулю точно (строгая изоляция)
    cr = p.complex_roots()
    rr = [r for r in cr if r[0].imag.is_exact() and r[0].imag == 0]
    assert len(cr) == p.degree()
    total_real += [(r, p.degree(), e) for r in rr]
    print(f'  factor of degree {p.degree():4d}, multiplicity {e:3d}: {len(rr)} real roots {[str(r[0]) for r in rr][:5]}')
print('all real roots of R:', [(str(r[0]), d, e) for r, d, e in total_real])
# на b2 = 0: d2 Qt(b1, 0) == 0 тождественно, d1 Qt(b1, 0) = 4 b1^3 + 24 b1^23
print('d2 Qt(b1, 0) =', sp.expand(sp.diff(Qt, b2).subs(b2, 0)), '; d1 Qt(b1, 0) =', sp.factor(sp.diff(Qt, b1).subs(b2, 0)))
