# [Эксперимент] R48: численная проверка тождества реализации O2D в случайных точках (mpmath, 60 знаков).
import random, sympy as sp, mpmath as mp
mp.mp.dps = 60
x, y, z, xh, e = sp.symbols('x y z xh e', real=True)
A = (xh - e**2)**2 + e**8
B = (xh - e**2 - e**3)**2 + e**8
AB = sp.Poly(sp.expand(A*B), xh, e)
Uo = sum(c*z**l*(x*y)**k*(x**2 + y**2)**(16 - l - k) for (k, l), c in AB.terms()) - (x**2 + y**2)**16
Uf = sp.lambdify((x, y, z), Uo, 'mpmath')
ABf = sp.lambdify((xh, e), A*B, 'mpmath')
random.seed(1)
worst = 0
for _ in range(10):
    s = mp.mpf(random.uniform(0.05, 1.5)); th = mp.mpf(random.uniform(0, 6.28)); ep = mp.mpf(random.uniform(-2, 2))
    lhs = Uf(s*mp.cos(th), s*mp.sin(th), s**2*ep)
    rhs = s**32*(ABf(mp.sin(th)*mp.cos(th), ep) - 1)
    worst = max(worst, abs(lhs - rhs)/max(abs(rhs), mp.mpf(10)**-40))
print('O2D: max rel. error of U(s cos, s sin, s^2 eps) - s^32(AB-1) over 10 random points:', mp.nstr(worst, 5))
