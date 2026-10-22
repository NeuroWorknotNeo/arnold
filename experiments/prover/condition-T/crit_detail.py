"""[Эксперимент] Детальная проверка критических точек Qt1, Qt2 (см. model_U.py): для каждого вещественного
корня b2 результанта Res_b1(d1 Qt, d2 Qt) находим корни d2 Qt(., b2) по b1 (степень <= 3 для Qt2, <= 1 для
Qt1 — d2 Qt не содержит b1^24, b1^12) и печатаем |d1 Qt| в них (относительно масштаба)."""
import sympy as sp
import flint
import mpmath as mp
mp.mp.dps = 80
b1, b2 = sp.symbols('b1 b2', real=True)
A = (b1 - b2**2)**2 + b2**8
B = (b1 - b2**2 - b2**3)**2 + b2**8
for name, Qt in (('Qt1', sp.expand((b1 - b2**2)**2 + b2**8 + b1**12)), ('Qt2', sp.expand(A * B + b1**24))):
    d1 = sp.Poly(sp.diff(Qt, b1), b1, b2)
    d2 = sp.Poly(sp.diff(Qt, b2), b1, b2)
    ctx = flint.fmpz_mpoly_ctx.get(('b1', 'b2'), 'lex')
    F1 = ctx.from_dict({k: int(v) for k, v in d1.as_dict().items()})
    F2 = ctx.from_dict({k: int(v) for k, v in d2.as_dict().items()})
    R = F1.resultant(F2, 'b1')
    co = {}
    for mon, c in zip(R.monoms(), R.coeffs()):
        co[mon[1]] = int(c)
    Rz = flint.fmpz_poly([co.get(i, 0) for i in range(max(co) + 1)])
    reals = []
    for (p, e) in Rz.factor()[1]:
        for r, mult in p.complex_roots():
            if r.imag.contains(0) and abs(float(r.imag.mid())) < 1e-40:
                reals.append((mp.mpf(str(r.real.mid())), p.degree(), e))
    print(f'{name}: real roots of resultant (b2, deg of factor, mult):',
          [(mp.nstr(a, 10), d, e) for a, d, e in reals])
    f1 = sp.lambdify((b1, b2), sp.diff(Qt, b1), 'mpmath')
    fQ = sp.lambdify((b1, b2), Qt, 'mpmath')
    for yb, _, _ in reals:
        yr = sp.nsimplify(sp.Float(str(yb), 70), rational=True)
        p2 = sp.Poly(sp.diff(Qt, b2).subs(b2, yr), b1)
        cs = [mp.mpf(sp.Float(c, 70)) for c in p2.all_coeffs()]
        while cs and abs(cs[0]) < mp.mpf(10)**-70:
            cs = cs[1:]
        if len(cs) <= 1:
            print(f'   b2={mp.nstr(yb, 8)}: d2 Qt(., b2) == const = {cs}')
            continue
        for r in mp.polyroots(cs, maxsteps=500, extraprec=800):
            if abs(mp.im(r)) > mp.mpf(10)**-30:
                continue
            xb = mp.re(r)
            print(f'   b2={mp.nstr(yb, 8)}: d2=0 at b1={mp.nstr(xb, 8)}, d1Qt={mp.nstr(f1(xb, yb), 5)}, Qt={mp.nstr(fQ(xb, yb), 5)}')
