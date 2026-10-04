import sympy as sp, time
from sieve import x, y, z
from dyncheck_fine import escape_test
s = "x**4 + x**3*y**2*z**2 - x**2*y**3*z + 2*x**2*y**2 - 2*x**2*z**2 + y**4 - y**3*z**3 - 2*y**2*z**2 + z**4"
U = sp.sympify(s, locals={'x': x, 'y': y, 'z': z}); t0 = time.time()
print('S3 fine:', escape_test(U, 0.05, R=0.3, tmax_factor=400.0), '(%.0fs)' % (time.time()-t0), flush=True)
