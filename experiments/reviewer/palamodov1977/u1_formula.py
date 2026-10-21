"""[Эксперимент/сверка] Для u1 = -x2(x1 - x2^2): формула phi(alpha, r) = -alpha - atan(3 r sin(alpha) - cot(alpha))
(mod 2pi, около alpha = pi/2) и её производная по alpha; сверка с прямым вычислением угла."""
import sympy as sp
import numpy as np
a, r = sp.symbols('alpha r', positive=True)
F = -a - sp.atan(3*r*sp.sin(a) - sp.cot(a))
dF = sp.simplify(sp.diff(F, a))
print("dphi/dalpha =", dF)
# value at alpha = pi/2 - tau, expansion in r with tau = k r
k = sp.symbols('k', positive=True)
ser = sp.series(dF.subs(a, sp.pi/2 - k*r), r, 0, 2).removeO()
print("dphi/dalpha at alpha = pi/2 - k r:", sp.simplify(ser))
serF = sp.series(F.subs(a, sp.pi/2 - k*r), r, 0, 2).removeO()
print("phi at alpha = pi/2 - k r:", sp.simplify(serF))
f = sp.lambdify((a, r), F, 'numpy')
def phi_direct(al, rr):
    x1, x2 = rr*np.cos(al), rr*np.sin(al)
    g1, g2 = -x2, -x1 + 3*x2**2
    d = np.arctan2(g2, g1) - np.arctan2(-x2, -x1)
    return (d + np.pi) % (2*np.pi) - np.pi
for rr in (1e-2, 1e-3):
    al = np.pi/2 - np.linspace(0.9, 3, 7)*rr
    print(rr, np.max(np.abs(((f(al, rr) - phi_direct(al, rr)) + np.pi) % (2*np.pi) - np.pi)))
