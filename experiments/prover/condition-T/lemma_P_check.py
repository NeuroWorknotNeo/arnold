"""[Эксперимент] Лемма P (полярная кривая): на Pi = {d_2 Q = 0} около нуля профиля b_1 d_1 Q >= e Q.

Профили (b_1 — широкая/коническая координата, b_2 — узкая):
  Q62   = A*B,  A = (b1-b2^2)^2 + b2^8,  B = (b1-b2^2-b2^3)^2 + b2^8      (предложение 6.2 [009])
  Qt2   = A*B + b1^24                                                   (модель U2, model_U.py)
  PO2D  = A*B (theta_hat, eps),  theta_hat = sin(th)cos(th),  b1 = th     (пример O2D, fold §6.3)
  PO1   = G1*G2 (theta_hat, eps), G1 = e^2+k th^2 e+th^4, G2 = th^2+k th e^2+e^4, k = 1.99 (пример O1 [014])
  PO2   = (eps^2 - sin th)^2 в складках th = 0 и th = pi (нуль не изолирован; локальная лемма P)
Для b_1 = +-10^{-k} (k = 1..14) и равномерной сетки по b_1 находим все вещественные корни многочлена
d_2 Q(b_1, .) по b_2 (mpmath.polyroots, 60 знаков) в шаре |b - p| < r и печатаем min и предел отношения
(b_1 - p_1) d_1 Q / Q на них. Нужно: min > 0; предел ожидается равным k_j/m_j (порядок Q вдоль ветви
в параметре Пюизё).
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 60
b1, b2, th, e = sp.symbols('b1 b2 th e', real=True)


def AB(x, y):
    return ((x - y**2)**2 + y**8) * ((x - y**2 - y**3)**2 + y**8)


k = sp.Rational(199, 100)
TH = sp.sin(th) * sp.cos(th)
PROFILES = {
    'Q62': (AB(b1, b2), (b1, b2), (0, 0), 0.5),
    'Qt2': (AB(b1, b2) + b1**24, (b1, b2), (0, 0), 0.5),
    'PO2D': (AB(TH, e), (th, e), (0, 0), 0.5),
    'PO1': ((e**2 + k * TH**2 * e + TH**4) * (TH**2 + k * TH * e**2 + e**4), (th, e), (0, 0), 0.5),
    'PO2@0': ((e**2 - sp.sin(th))**2, (th, e), (0, 0), 0.3),
    'PO2@pi': ((e**2 - sp.sin(th))**2, (th, e), (sp.pi, 0), 0.3),
}


def analyse(name, Q, var, p, r, zthr=False):
    u, w = var
    p1 = mp.mpf(sp.N(p[0], 70))
    d1 = sp.diff(Q, u)
    d2 = sp.Poly(sp.expand(sp.diff(Q, w)), w)      # многочлен по узкой переменной, коэффициенты — функции u
    coeffs = [sp.lambdify(u, c, 'mpmath') for c in d2.all_coeffs()]
    fQ = sp.lambdify((u, w), Q, 'mpmath')
    f1 = sp.lambdify((u, w), d1, 'mpmath')
    grid = [p1 + sg * mp.mpf(10)**(-kk) for kk in range(1, 15) for sg in (1, -1)]
    grid += [p1 + mp.mpf(j) / 400 * r for j in range(-399, 400) if j != 0]
    worst, near = None, {}
    npts = 0
    for a in grid:
        cs = [c(a) for c in coeffs]
        while cs and abs(cs[0]) < mp.mpf(10)**(-55):
            cs = cs[1:]
        if len(cs) <= 1:
            continue
        for z in mp.polyroots(cs, maxsteps=600, extraprec=600):
            if abs(mp.im(z)) > mp.mpf(10)**(-30) * (1 + abs(z)):
                continue
            y = mp.re(z)
            if (a - p1)**2 + y**2 >= r * r:
                continue
            q = fQ(a, y)
            if q == 0 or (zthr and q < mp.mpf(10)**(-50)):   # для PO2 исключаются точки самого нулевого множества
                continue
            ratio = (a - p1) * f1(a, y) / q
            npts += 1
            if worst is None or ratio < worst[0]:
                worst = (ratio, a - p1, y, q)
            dist = abs(a - p1)
            if dist <= mp.mpf(10)**(-10):
                key = (mp.sign(a - p1), mp.nstr(y / (abs(a - p1)**mp.mpf('0.5') + 1e-300), 3))
                near.setdefault(int(mp.sign(a - p1)), []).append(mp.nstr(ratio, 6))
    print(f'{name}: {npts} polar points with 0<|b-p|<{r}; min (b1-p1) d1Q/Q = {mp.nstr(worst[0], 6)} '
          f'at b-p=({mp.nstr(worst[1], 4)}, {mp.nstr(worst[2], 4)}), Q={mp.nstr(worst[3], 4)}')
    for sg, lst in sorted(near.items()):
        print(f'   ratios at b1-p1 = {"+" if sg > 0 else "-"}1e-10..1e-14: {sorted(set(lst))[:8]}')


if __name__ == '__main__':
    import sys
    names = sys.argv[1:] or list(PROFILES)
    for nm in names:
        Q, var, p, r = PROFILES[nm]
        analyse(nm, Q, var, p, r, zthr=nm.startswith('PO2@'))
