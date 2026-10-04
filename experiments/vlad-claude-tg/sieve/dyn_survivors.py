import sympy as sp, time
from sieve import x, y, z
from dyncheck import escape_test
S = [
 ("S1 (касающийся нуль, без симметрий)", "(x**2+y**2-z**2)**2 + y**2*z**4 + x*y*z**5/10 - z**8"),
 ("S2 (пример 14: жёлоб надо искать)", "(x**2+y**2-z**2 - z*(x**2+x*y))**2 - z**8"),
 ("S3 (из семейства C: тройной нуль)", "x**4 + x**3*y**2*z**2 - x**2*y**3*z + 2*x**2*y**2 - 2*x**2*z**2 + y**4 - y**3*z**3 - 2*y**2*z**2 + z**4"),
]
for name, s in S:
    U = sp.sympify(s, locals={'x': x, 'y': y, 'z': z})
    t0 = time.time()
    res = escape_test(U, 0.05, R=0.3, tmax_factor=200.0)
    print(name, '| N, escaped, median escape time (in units r0/sqrt|h|), energy drift =', res, ' (%.0fs)' % (time.time()-t0), flush=True)
