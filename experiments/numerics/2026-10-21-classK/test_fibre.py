import sympy as sp
from kfib import *
t = sp.symbols('t', real=True)
Q = x**2+y**2-z**2
for name, U, m, K in [('K3', Q**2+x*z**4, 4, 2), ('K2', Q**2+z**5*x+z**4*x*y+z**6/2, 4, 3)]:
    p = [1-t**2, 2*t, 1+t**2]; nu = [[1-t**2, 2*t, -(1+t**2)]]
    out = fibre(U, m, p, nu, K)
    lam = sp.sqrt(2)*(1+t**2)
    for k, g in out['g'].items():
        Gu = sp.simplify(g/lam**k)
        # compare with known: K3 g5 = sqrt2 cos(phi)/8, g6=-9cos^2/512 ; cos(phi) = (1-t^2)/(1+t^2)
        c = (1-t**2)/(1+t**2)
        print(name, k, sp.factor(Gu))
        if name == 'K3' and k == 5: print('  diff', sp.simplify(Gu - sp.sqrt(2)*c/8))
        if name == 'K3' and k == 6: print('  diff', sp.simplify(Gu + 9*c**2/512))
        if name == 'K2' and k == 6: print('  diff', sp.simplify(Gu - (sp.Rational(1, 16) + c/8 + (2*t/(1+t**2))*c/8)))
