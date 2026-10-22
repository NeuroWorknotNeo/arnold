"""[Эксперимент] Лемма P: на полярной кривой Pi = {d_2 Q = 0} около нуля b_1 * d_1 Q > 0.

Профили (b_1 — широкая координата, b_2 — узкая):
  Q1 = (b1 - b2^2)^2 + b2^8                        (один подовраг, касается узкой оси)
  Q2 = A*B, A = (b1-b2^2)^2 + b2^8, B = (b1-b2^2-b2^3)^2 + b2^8   (предложение 6.2 [009])
  Q3 = Q2 + b1^24  (изолирующая добавка для полиномиального U, см. model_U.py)
Для каждого b_1 = +-10^{-k} и равномерной сетки по b_1 ищем все вещественные корни b_2 многочлена
d_2 Q(b_1, .) (mpmath.polyroots, 60 знаков) с |b| < r и печатаем min b_1 d_1 Q / Q (должно быть > 0),
а также число полярных точек над b_1.
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 60
b1, b2 = sp.symbols('b1 b2', real=True)
A = (b1 - b2**2)**2 + b2**8
B = (b1 - b2**2 - b2**3)**2 + b2**8
PROFILES = {
    'Q1': (b1 - b2**2)**2 + b2**8,
    'Q2': sp.expand(A * B),
    'Q3': sp.expand(A * B + b1**24),
}


def analyse(name, Q, r=0.5):
    d1 = sp.diff(Q, b1)
    d2 = sp.Poly(sp.diff(Q, b2), b2)
    coeffs = [sp.lambdify(b1, c, 'mpmath') for c in d2.all_coeffs()]
    fQ = sp.lambdify((b1, b2), Q, 'mpmath')
    f1 = sp.lambdify((b1, b2), d1, 'mpmath')
    pts = []
    grid = [mp.mpf(s) * mp.mpf(10)**(-k) for k in range(1, 13) for s in (1, -1)]
    grid += [mp.mpf(j) / 200 * r for j in range(-199, 200) if j != 0]
    worst = None
    for a in grid:
        cs = [c(a) for c in coeffs]
        while cs and cs[0] == 0:
            cs = cs[1:]
        roots = mp.polyroots(cs, maxsteps=400, extraprec=400)
        npol = 0
        for z in roots:
            if abs(mp.im(z)) > mp.mpf(10)**(-40) * (1 + abs(z)):
                continue
            y = mp.re(z)
            if a * a + y * y >= r * r:
                continue
            q = fQ(a, y)
            phi = a * f1(a, y)
            npol += 1
            ratio = phi / q
            if worst is None or ratio < worst[0]:
                worst = (ratio, a, y, q)
        pts.append((a, npol))
    print(f'{name}: min over polar points (|b|<{r}) of b1*d1Q/Q = {mp.nstr(worst[0], 6)} '
          f'at b=({mp.nstr(worst[1], 4)}, {mp.nstr(worst[2], 4)}), Q={mp.nstr(worst[3], 4)}')
    small = [(mp.nstr(a, 2), n) for a, n in pts[:24]]
    print('   number of real polar points over b1=+-10^-k, k=1..12:', small)
    return worst


if __name__ == '__main__':
    for name, Q in PROFILES.items():
        analyse(name, Q)
