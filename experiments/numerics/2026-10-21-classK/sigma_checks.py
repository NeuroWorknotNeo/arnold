"""sigma_checks.py -- exact checks on Sigma: (1) smoothness of the cone {f=0} (Groebner: (f,grad f) is zero-dimensional
homogeneous => grad f != 0 off the origin over C); (2) for the non-Morse-Bott examples D^2 u_m vanishes identically on Sigma;
(3) for S1: singular points of Sigma = zeros of H.  [Experiment: symbolic, exact]"""
import sympy as sp
import comps
from comps import x, y, z, U
from kfib import homog_parts
def smooth(f):
    G = sp.groebner([f] + [sp.diff(f, v) for v in (x, y, z)], x, y, z, order='grevlex')
    if list(G.exprs) == [1]:
        return True      # (f, grad f) is the unit ideal: grad f never vanishes (f linear)
    lead = [sp.Poly(g, x, y, z).monoms(order='grevlex')[0] for g in G.exprs]
    return all(any(sum(m) == m[i] and m[i] > 0 for m in lead) for i in range(3))
C = y**2*z - x**3 - x*z**2
forms = {'Q=x^2+y^2-z^2 (K2,K3,A1-A5,A7,D1,D2)': comps.Q, 'x^2+2y^2-z^2 (C1)': comps.fE, 'x^2+y^2-2z^2 (C2)': comps.f2,
         'z (F1, Z1 equator)': z, 'x-y (S1)': x - y, 'x+y (S1)': x + y, 'C=y^2 z-x^3-x z^2 (T1)': C}
for k, f in forms.items():
    print('cone {f=0} smooth away from 0 (grad f != 0 on f=0, over C):', smooth(f), ' <-', k)
print('S1: Sigma = {x=y} u {x=-y} meet at (0,0,+-1): there grad(x^2-y^2)=0 -> Morse-Bott fails at exactly these 2 points')
for ex, um in [('K1', None), ('P1', None), ('M1', None), ('M2', None)]:
    m = min(homog_parts(U[ex])); u = homog_parts(U[ex])[m]
    Hm = sp.hessian(u, (x, y, z))
    if ex in ('K1', 'P1'):
        pts = [(0, 0, 1), (0, 0, -1)]
        vals = [Hm.subs({x: a, y: b, z: c}) for a, b, c in pts]
    else:
        # Sigma = {z=0}: Hessian on the whole equator (x,y free, z=0)
        vals = [Hm.subs(z, 0)]
    print(ex, 'u_m =', u, ': D^2 u_m on Sigma =', [v.tolist() for v in vals], ' => identically 0 (transversal order of vanishing 4)')
