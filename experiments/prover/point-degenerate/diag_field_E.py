"""[Эксперимент] Пример E: профиль Q = (b2-b1^2)^2 (b2-b1^3)^2 + b1^12 + b2^12.
Проверяется, что никакое диагональное поле xi = (b1, r b2) (r > 0) не даёт xi.grad Q >= mu Q с mu > 0 около нуля:
для каждого r ищется точка b (|b| <= 0.2) с xi.grad Q < 0. Точки берутся на кривых b2 = b1^a (1 + eps).
Также печатается min (xi.grad Q)/Q для весов оврага c = (2,2) (то есть r = 1).
"""
import mpmath as mp

mp.mp.dps = 40


def Q(b1, b2):
    return (b2 - b1**2)**2 * (b2 - b1**3)**2 + b1**12 + b2**12


def dQ(b1, b2):
    A, B = (b2 - b1**2), (b2 - b1**3)
    d1 = 2 * A * (-2 * b1) * B**2 + A**2 * 2 * B * (-3 * b1**2) + 12 * b1**11
    d2 = 2 * A * B**2 + 2 * A**2 * B + 12 * b2**11
    return d1, d2


def worst_ratio(r):
    best = (mp.inf, None)
    for b1 in [mp.mpf(k) / 200 for k in range(1, 41)]:
        for a in [mp.mpf(2), mp.mpf(3), mp.mpf(5) / 2]:
            for eps in [mp.mpf(e) / 100 for e in range(-60, 61, 3)]:
                b2 = b1**a * (1 + eps)
                d1, d2 = dQ(b1, b2)
                val = (b1 * d1 + r * b2 * d2) / Q(b1, b2)
                if val < best[0]:
                    best = (val, (b1, a, eps))
    return best


for r in [0.5, 1, 1.5, 2, 2.5, 3, 4, 6]:
    v, pt = worst_ratio(mp.mpf(r))
    print(f'r = lambda2/lambda1 = {r}: min (xi.gradQ)/Q = {mp.nstr(v, 6)} at b1={mp.nstr(pt[0], 4)}, '
          f'b2 = b1^{mp.nstr(pt[1], 3)}(1+({mp.nstr(pt[2], 3)}))')
