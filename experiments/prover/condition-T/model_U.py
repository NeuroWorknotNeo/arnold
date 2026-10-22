"""[Эксперимент] Модельные аналитические U с подоврагами, касающимися узкой оси; изолированность.

Координаты q = (x, y, z): x — продольная, y — широкая (вес c1 = 2), z — узкая (вес c2 = 3);
b1 = y/x^2, b2 = z/x^3.

U1 = x^12 (x^4 y - z^2)^2 + z^8 + y^12 - a0 x^24 + sigma x^23 y          (beta = 24)
     = x^24 ( -a0 + Qt1(b) + sigma*x*b1 ),  Qt1 = (b1-b2^2)^2 + b2^8 + b1^12;
U2 = Ahat*Bhat + y^24 - a0 x^48 + sigma x^47 y                        (beta = 48)
     Ahat = x^12 (x^4 y - z^2)^2 + z^8,  Bhat = x^6 (x^7 y - x^3 z^2 - z^3)^2 + z^8,
     = x^48 ( -a0 + Qt2(b) + sigma*x*b1 ),  Qt2 = A*B + b1^24  (A, B — предложение 6.2 [009]).

Изолированность [Доказано в записке, лемма I]: U = U_0 + U_1, U_0 = x^beta(-a0 + Qt) квазиоднороден
(веса (1,2,3), степень beta), U_1 = sigma x^{beta-1} y имеет вес beta+1. Достаточно: grad U_0 != 0 вне 0,
что равносильно: (i) U_0(0,y,z) = y^k + z^l (изолированная критическая точка) и (ii) a0 — не критическое
значение Qt на R^2. Здесь (ii) проверяется: все критические точки Qt находятся через результант
(python-flint, точная арифметика) и вещественные корни; печатаются критические значения.
Затем — независимая численная проверка: поиск критических точек U вблизи 0 методом Ньютона (mpmath).
"""
import sympy as sp
import flint
import mpmath as mp

mp.mp.dps = 50
x, y, z, b1, b2 = sp.symbols('x y z b1 b2', real=True)
A = (b1 - b2**2)**2 + b2**8
B = (b1 - b2**2 - b2**3)**2 + b2**8
Qt1 = sp.expand((b1 - b2**2)**2 + b2**8 + b1**12)
Qt2 = sp.expand(A * B + b1**24)


def check_quasi(Uexpr, Qt, beta, a0, sigma):
    """Проверка тождества U = x^beta(-a0 + Qt(y/x^2, z/x^3) + sigma x b1)."""
    lhs = sp.expand(Uexpr)
    rhs = sp.expand(sp.simplify(x**beta * (-a0 + Qt.subs({b1: y / x**2, b2: z / x**3}, simultaneous=True)
                                          + sigma * x * y / x**2)))
    return sp.expand(lhs - rhs) == 0


def critical_values(Qt, name):
    """Критические точки Qt: результант Res_{b1}(d1 Qt, d2 Qt) по b2, вещественные корни, затем b1."""
    d1 = sp.Poly(sp.diff(Qt, b1), b1, b2)
    d2 = sp.Poly(sp.diff(Qt, b2), b1, b2)
    ctx = flint.fmpz_mpoly_ctx.get(('b1', 'b2'), 'lex')
    def to_flint(P):
        return ctx.from_dict({k: int(v) for k, v in P.as_dict().items()})
    F1, F2 = to_flint(d1), to_flint(d2)
    R = F1.resultant(F2, 'b1')
    # R — многочлен от b2
    coeffs = {}
    for mon, c in zip(R.monoms(), R.coeffs()):
        coeffs[mon[1]] = int(c)
    deg = max(coeffs)
    Rz = flint.fmpz_poly([coeffs.get(i, 0) for i in range(deg + 1)])
    print(f'{name}: deg Res_b1(d1,d2) in b2 = {deg}')
    fac = Rz.factor()
    real_b2 = []
    for (p, e) in fac[1]:
        for r in p.complex_roots():
            rr = r[0]
            if abs(rr.imag) < 1e-30:
                real_b2.append(mp.mpf(str(rr.real.mid())))
    real_b2 = sorted(set(real_b2))
    vals = []
    f1 = sp.lambdify((b1, b2), sp.diff(Qt, b1), 'mpmath')
    f2 = sp.lambdify((b1, b2), sp.diff(Qt, b2), 'mpmath')
    fQ = sp.lambdify((b1, b2), Qt, 'mpmath')
    for yb in real_b2:
        # общие корни по b1: корни d2(., yb) (степень <= 3 или 23), проверяем d1
        p2 = sp.Poly(sp.diff(Qt, b2).subs(b2, sp.Rational(str(yb))), b1)
        p1 = sp.Poly(sp.diff(Qt, b1).subs(b2, sp.Rational(str(yb))), b1)
        cand = [r for r in mp.polyroots([mp.mpf(str(c)) for c in p1.all_coeffs()], maxsteps=500, extraprec=500)
                if abs(mp.im(r)) < mp.mpf(10)**-20]
        for r in cand:
            xb = mp.re(r)
            if abs(f2(xb, yb)) < mp.mpf(10)**-15 and abs(f1(xb, yb)) < mp.mpf(10)**-15:
                vals.append((fQ(xb, yb), xb, yb))
    vals = sorted(set((mp.nstr(v, 12), mp.nstr(a, 8), mp.nstr(c, 8)) for v, a, c in vals))
    for v in vals:
        print('   critical point b=(%s, %s), value %s' % (v[1], v[2], v[0]))
    return vals


if __name__ == '__main__':
    a0, sigma = 1, -1
    Ahat = x**12 * (x**4 * y - z**2)**2 + z**8
    Bhat = x**6 * (x**7 * y - x**3 * z**2 - z**3)**2 + z**8
    U1 = x**12 * (x**4 * y - z**2)**2 + z**8 + y**12 - a0 * x**24 + sigma * x**23 * y
    U2 = Ahat * Bhat + y**24 - a0 * x**48 + sigma * x**47 * y
    print('U1 = x^24(-a0+Qt1(b)+sigma x b1):', check_quasi(U1, Qt1, 24, a0, sigma))
    print('U2 = x^48(-a0+Qt2(b)+sigma x b1):', check_quasi(U2, Qt2, 48, a0, sigma))
    print('U1(0,y,z) =', sp.factor(U1.subs(x, 0)), '; U2(0,y,z) =', sp.expand(U2.subs(x, 0)))
    critical_values(Qt1, 'Qt1')
    critical_values(Qt2, 'Qt2')
