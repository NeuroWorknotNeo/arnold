"""b2_check.py -- независимая проверка мелкого оврага B2 на нижнем листе конуса: локальный минимум U на сферах |q| = r около ω* = -(t²,t³,1)/|.|, t = ±0.8678…
Отношение U/r^7 в минимуме должно стремиться к G(ω*) = -0.0667250094 (из cusp_G.py).   [Эксперимент: mpmath 50 знаков, прямая минимизация, не использует ряды kfib]"""
import mpmath as mp, sympy as sp
from exlist import BY, x, y, z
mp.mp.dps = 50
f = sp.lambdify((x, y, z), BY['f:B2']['U'], 'mpmath')
t0 = mp.mpf('0.867820882130354')
for st in (1, -1):
    t = st * t0
    p = [-t**2, -t**3, -mp.mpf(1)]
    nrm = mp.sqrt(sum(c**2 for c in p)); om = [c / nrm for c in p]
    e1 = [om[1], -om[0], 0]; n1 = mp.sqrt(sum(c**2 for c in e1)); e1 = [c / n1 for c in e1]
    e2 = [om[1] * e1[2] - om[2] * e1[1], om[2] * e1[0] - om[0] * e1[2], om[0] * e1[1] - om[1] * e1[0]]
    for r in (mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')):
        def F(a, b):
            v = [om[i] + a * e1[i] + b * e2[i] for i in range(3)]
            n = mp.sqrt(sum(c**2 for c in v))
            return f(*[r * c / n for c in v]) / r**7
        best = None
        for i in range(-10, 11):
            for j in range(-10, 11):
                a, b = mp.mpf(i) / 50 * mp.mpf('0.05'), mp.mpf(j) / 200 * mp.mpf('0.05')
                val = F(a, b)
                if best is None or val < best[0]:
                    best = (val, a, b)
        a, b = best[1], best[2]
        g = lambda a_, b_: [mp.diff(F, (a_, b_), (1, 0)), mp.diff(F, (a_, b_), (0, 1))]
        try:
            a, b = mp.findroot(lambda a_, b_: g(a_, b_), (a, b), tol=1e-30, maxsteps=50)
        except Exception:
            pass
        print('t=%s r=%s  min U/r^7 = %s   (a=%s, b=%s)   [ожидается G(ω*) = -0.0667250094 при r -> 0]' % (mp.nstr(t, 6), mp.nstr(r, 3), mp.nstr(F(a, b), 9), mp.nstr(a, 4), mp.nstr(b, 4)))
