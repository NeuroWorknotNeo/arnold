"""R39: [Experiment] zero-dimensionality of the gradient ideal (Groebner basis, sympy, grevlex, QQ).
If the ideal (dU/dx, dU/dy, dU/dz) is zero-dimensional over C, the critical set is finite, so 0 is an
isolated critical point.  Run: ~/venv/bin/python isolated_check_R39.py NAME
"""
import sys, time
import sympy as sp
x, y, z = sp.symbols('x y z')
R = sp.Rational
k0 = R(199, 100)
EX = {
    'Lambda': x**4 - k0*x**2*y*z + y**2*z**2 + y**4 - z**8 + x*z**7,
    'SH': z**4*(y - x**2 - x*z)**2 + x**6 + y**6 - z**12 + x*z**11,
    'X': x**6 + y**6 + y**4*z**2 + x**2*y**2*z**2 - z**12 + x*z**11,
}
name = sys.argv[1]
U = EX[name]
t0 = time.time()
G = sp.groebner([sp.diff(U, v) for v in (x, y, z)], x, y, z, order='grevlex', domain='QQ')
print(name, 'zero-dimensional:', G.is_zero_dimensional, f'({time.time()-t0:.1f}s, {len(G.exprs)} polys)')
