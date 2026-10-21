"""comps.py -- the 22 examples (19 hard + K1-K3 calibrations) with exact data of the zero set Sigma of u_m.
U is taken from the zoo catalog (experiments/numerics/2026-10-21-zoo/catalog.py), not retyped.
For each example: list of components of Sigma:
   ('curve', name, p(t), nu(t), f)   rational parametrisation of the ray-curve (u or t parameter), f = defining form
   ('point', name, p)                rational direction p (unnormalised), +-p are different components
   ('nonMB', ...)  components where Morse-Bott fails (declared by hand, verified in analyze.py)
"""
import sys, os
import sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '2026-10-21-zoo'))
import catalog as C
x, y, z = sp.symbols('x y z')
t = sp.symbols('t', real=True)

U = {e['id']: sp.expand(sp.sympify(e['U'], locals={'x': x, 'y': y, 'z': z})) for e in C.CATALOG}
CORE = {e['id']: e['core'] for e in C.CATALOG}
HARD = ['A1', 'A2', 'A3', 'A4', 'A5', 'A7', 'C1', 'C2', 'D1', 'D2', 'F1', 'M1', 'M2', 'P1', 'P3', 'P4', 'Z1', 'S1', 'T1']
CALIB = ['K1', 'K2', 'K3']
ALL = CALIB + HARD

Q = x**2 + y**2 - z**2
fE = x**2 + 2*y**2 - z**2
f2 = x**2 + y**2 - 2*z**2


def grad(f, p):
    return [sp.expand(sp.diff(f, v).subs({x: p[0], y: p[1], z: p[2]}, simultaneous=True)) for v in (x, y, z)]


def mk(name, p, f):
    """curve component: ray-curve p(t) on the cone f=0; normal line direction nu = grad f(p) (in N_omega)"""
    p = [sp.expand(c) for c in p]
    nu = grad(f, p)
    assert sp.expand(f.subs({x: p[0], y: p[1], z: p[2]}, simultaneous=True)) == 0
    assert sp.expand(sum(a*b for a, b in zip(p, nu))) == 0                      # nu . p = 0
    assert sp.expand(sum(sp.diff(a, t)*b for a, b in zip(p, nu))) == 0          # nu . p'(t) = 0 (nu is normal to the curve)
    return ('curve', name, p, nu, f)


def circle(f, kind):
    """conic cones through rational parametrisations, upper (z>0) / lower (z<0) half-circle of the cone"""
    if kind == 'Q':
        p = [1 - t**2, 2*t, 1 + t**2]
    elif kind == 'E':       # x^2+2y^2=z^2
        p = [1 - 2*t**2, 2*t, 1 + 2*t**2]
    elif kind == 'C2':      # x^2+y^2=2z^2
        p = [1 + 2*t - t**2, 1 - 2*t - t**2, 1 + t**2]
    else:
        raise ValueError
    return [mk('Sigma+ (z>0)', p, f), mk('Sigma- (z<0)', [p[0], p[1], -p[2]], f)]


def equator():
    return [mk('equator z=0', [1 - t**2, 2*t, 0], z)]


def S1_comps():
    return [mk('circle x=y', [2 - t**2, 2 - t**2, 4*t], x - y), mk('circle x=-y', [2 - t**2, -(2 - t**2), 4*t], x + y)]


def pts(*ps, both=True):
    out = []
    for p in ps:
        out.append(('point', str(tuple(p)), list(p)))
        if both:
            out.append(('point', str(tuple(-sp.Integer(1)*sp.Integer(c) for c in p)), [-c for c in p]))
    return out


# the 8 points (+-1,+-1,+-1)/sqrt3 :
P8 = [(a, b, c) for a in (1, -1) for b in (1, -1) for c in (1, -1)]
COMPS = {
    'K1': [('nonMB', 'poles +-e_z (u_4 = x^4+y^4)', None)],
    'K2': circle(Q, 'Q'), 'K3': circle(Q, 'Q'),
    'A1': circle(Q, 'Q'), 'A2': circle(Q, 'Q'), 'A3': circle(Q, 'Q'), 'A4': circle(Q, 'Q'), 'A5': circle(Q, 'Q'),
    'A7': circle(Q, 'Q'), 'C1': circle(fE, 'E'), 'C2': circle(f2, 'C2'),
    'D1': circle(Q, 'Q'), 'D2': circle(Q, 'Q'),
    'F1': equator(),
    'M1': [('nonMB', 'equator z=0 (u_4 = z^4)', None)], 'M2': [('nonMB', 'equator z=0 (u_4 = z^4)', None)],
    'P1': [('nonMB', 'poles +-e_z (u_4 = x^4+y^4)', None)],
    'P3': [('point', str(q), list(q)) for q in P8],
    'P4': [('point', n_, p_) for n_, p_ in [('+e_x', [1, 0, 0]), ('-e_x', [-1, 0, 0]), ('+e_y', [0, 1, 0]), ('-e_y', [0, -1, 0]), ('+e_z', [0, 0, 1]), ('-e_z', [0, 0, -1])]],
    'Z1': equator() + [('point', '+e_z', [0, 0, 1]), ('point', '-e_z', [0, 0, -1])],
    'S1': S1_comps(),
    'T1': [('numcurve', 'cubic cone C=0', None)],
}
