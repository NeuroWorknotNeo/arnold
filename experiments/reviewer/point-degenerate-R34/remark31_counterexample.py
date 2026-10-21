"""R34: counterexample to Remark 3.1 in the generality of Statement Q (Q only locally >= 0).
U = -z^8 + z^4 (x^2+y^2) - z^2 x^3, c=(2,2), N=1, beta=8.  [Experiment: sympy exact.]"""
import sympy as sp
x, y, z, b1, b2, mu = sp.symbols('x y z b1 b2 mu', real=True)
s = sp.Symbol('s', positive=True)
U = -z**8 + z**4*(x**2 + y**2) - z**2*x**3
F = sp.expand(U.subs({x: s**2*b1, y: s**2*b2, z: s})/s**8)
print('F =', F)
Q = F + 1
E = sp.expand(2*(b1*Q.diff(b1) + b2*Q.diff(b2)) - mu*Q)
print('<Cb,gradQ> - mu Q =', sp.collect(E, [b1, b2]))
print('graded parts: s^4-level', b1**2 + b2**2, '; s^2-level', -b1**3, '(not >= 0)')
