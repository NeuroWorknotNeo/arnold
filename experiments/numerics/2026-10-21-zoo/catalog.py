"""
catalog.py -- the zoo: polynomials U(x,y,z), U(0)=0, grad U(0)=0, with explicit data used by the exact checks.

Entry fields
  id, name, U            : label, short name, polynomial (string; sympy syntax, x y z)
  why                    : what makes the example hard / which feature it tests
  core = dict(sos=[(c, p),...], sigma=[...])
                         : u_m = sum c p^2 (explicit SOS certificate of u_m >= 0), and the declared real zero set
                           Sigma of u_m on the sphere: {'kind':'curve','f':form} (cone over a curve f=0),
                           {'kind':'points','pts':[directions]} (rays through the listed points, +-)
  witness (optional)     : ('curve', (x(tau),y(tau),z(tau))) or ('arc', F, a, b, N) -- explicit curve with U < 0;
                           otherwise a rational ray with U(t w) < 0 is searched automatically
  equiv_ex13 (optional)  : orthogonal matrix R with U = c * U_13(R q)
"""
import sympy as sp

Q = '(x**2+y**2-z**2)'
U13 = f'{Q}**2+z**5*x+z**4*x*y+z**6/2'


def circle_core(f=Q):
    return dict(sos=[(1, f)], sigma=[dict(kind='curve', f=f)])


def rot(a, b, c, d, e, f):
    """product of three rational plane rotations: (a/b) about z, (c/d) about x, (e/f) about y; c,s from Pythagorean triples"""
    def R(k, cs, sn):
        if k == 'z':
            return sp.Matrix([[cs, -sn, 0], [sn, cs, 0], [0, 0, 1]])
        if k == 'x':
            return sp.Matrix([[1, 0, 0], [0, cs, -sn], [0, sn, cs]])
        return sp.Matrix([[cs, 0, sn], [0, 1, 0], [-sn, 0, cs]])
    return R('y', sp.Rational(e), sp.Rational(f)) * R('x', sp.Rational(c), sp.Rational(d)) * R('z', sp.Rational(a), sp.Rational(b))


Rrot = rot('3/5', '4/5', '5/13', '12/13', '8/17', '15/17')
_q = Rrot * sp.Matrix(sp.symbols('x y z'))
_xr, _yr, _zr = [sp.expand(e) for e in _q]
_w = Rrot.T * sp.Matrix([-4, 3, 5])
_den = sp.ilcm(1, 1, *[sp.Rational(v).q for v in _w])
_w13 = tuple(int(v * _den) for v in _w)


def rotated(expr_str):
    x, y, z = sp.symbols('x y z')
    f = sp.sympify(expr_str, locals={'x': x, 'y': y, 'z': z})
    return sp.expand(f.subs({x: _xr, y: _yr, z: _zr}, simultaneous=True))


CATALOG = []


def add(**kw):
    CATALOG.append(kw)


# ============================================================ calibration
add(id='K1', name='x^4+y^4-z^6', U='x**4+y**4-z**6',
    why='calibration: quasi-homogeneous (weights 3,3,2), u_4 = x^4+y^4 >= 0 vanishes on the z-axis',
    core=dict(sos=[(1, 'x**2'), (1, 'y**2')], sigma=[dict(kind='points', pts=[(0, 0, 1)])]))
add(id='K2', name='Example 13', U=U13,
    why='calibration: circular gutter, effective potential with simple zeros; covered only by our Example-13 criterion',
    core=circle_core())

add(id='K3', name='Theorem B example Q^2 + x z^4',
    U=f'{Q}**2+x*z**4',
    why='calibration: example of results/002 (has the reflection y -> -y, hence also covered by the n=2 reduction)',
    core=circle_core())

# ============================================================ circular 45-degree cone, u_4 = Q^2
add(id='A1', name='Q^2 + effective potential, double zero from below',
    U=f'{Q}**2+z**4*(x-z)*(z+y/2)+z**7',
    why='W_6 on the gutter: G = (cos f - 1)(1+sin f/2) <= 0 with a DOUBLE zero at f=0; W_7 = z^7 (G7 = 1 > 0) keeps 0 isolated',
    core=circle_core())
add(id='A2', name='Q^2 + effective potential, double zero from above',
    U=f'{Q}**2+z**4*(z-x)*(x+y/3-z/2)-z**7',
    why='G = (1-cos f)(cos f + sin f/3 - 1/2): G >= 0 near the DOUBLE zero f=0, negative elsewhere; G7 = -1 < 0',
    core=circle_core())
add(id='A3', name='Q^2 + effective potential, triple zero',
    U=f'{Q}**2+y**3*z**2*(z+x/2)+z**7+y*z**6',
    why='G = sin^3 f (1+cos f/2): triple zeros (sign change with vanishing slope) at f = 0, pi; W_7 = z^7 resolves isolation; no symmetry',
    core=circle_core())
add(id='A4', name='Q^2 + effective potential >= 0 with double zero, thin horn only from W_7',
    U=f'{Q}**2+z**4*(z-x)*(z+y/2)-z**7',
    why='G = (1-cos f)(1+sin f/2) >= 0 with a double zero at f=0: negative values only in a horn of angular width ~ r^(1/2) around the ray (1,0,1), where U = -t^7',
    core=circle_core())
add(id='A5', name='Q^2 + odd W_5 with a double zero on the gutter',
    U=f'{Q}**2+z**3*(x-z)*(z+y/2)+z**6',
    why='W_5|gutter = (cos f - 1)(1+ sin f/2) z^5: not a regular value (touching zero), so B3 fails; next form W_6 = z^6',
    core=circle_core())
add(id='A6', name='Example 13 rotated by a rational rotation',
    U=str(rotated(U13)),
    why='the same system in rotated orthonormal coordinates: tests that detection does not rely on the axis being z',
    core=dict(sos=[(1, str(rotated(Q)))], sigma=[dict(kind='curve', f=str(rotated(Q)))]),
    equiv_ex13=Rrot.tolist(),
    witness=('ray', _w13))
add(id='A7', name='m=6: Q^2 (x^2+y^2+z^2) + W_8',
    U=f'{Q}**2*(x**2+y**2+z**2)+z**7*x+z**6*x*y+z**8/2',
    why='u_6 = Q^2 |q|^2: gutter = circle, u_7 = 0, W_8 = Example-13 type potential; the Example-13 criterion is stated for u_4 = Q^2 only',
    core=dict(sos=[(1, f'{Q}*x'), (1, f'{Q}*y'), (1, f'{Q}*z')], sigma=[dict(kind='curve', f=Q)]))

# ============================================================ other cones
add(id='C1', name='elliptic cone, simple zeros of the effective potential',
    U='(x**2+2*y**2-z**2)**2+z**5*x+z**4*x*y+z**6/2',
    why='gutter = ellipse; not circular, so the Example-13 construction is not stated for it',
    core=circle_core('x**2+2*y**2-z**2'))
add(id='C2', name='circular cone with aperture != 90 degrees',
    U='(x**2+y**2-2*z**2)**2+z**5*x+z**4*x*y+z**6/2',
    why='cone x^2+y^2=2z^2: circular but not the 45-degree cone of Example 13',
    core=circle_core('x**2+y**2-2*z**2'))
add(id='C3', name='elliptic cone, odd W_5 (Theorem B territory)',
    U='(x**2+2*y**2-z**2)**2+(x+3*y)*z**4+z**6',
    why='gutter ellipse, u_5 regular on it: Theorem B applies, no symmetry',
    core=circle_core('x**2+2*y**2-z**2'))

# ============================================================ deformed gutters
add(id='D1', name='gutter to be searched: (Q - z m)^2 - z^8',
    U=f'({Q}-z*(x*(x+2*y)+3*x*z))**2-z**8',
    why='m = x(x+2y)+3xz (m must involve z and be non-axial, otherwise principal axes of m give invariant planes). U_5 = -2 Q z m, U_6 = z^2 m^2 vanish/are >= 0 on the cone; negativity lives on the DEFORMED cone Q = z m (U = -z^8 there)',
    core=circle_core(),
    witness=('arc', f'{Q}-z*(x*(x+2*y)+3*x*z)', '3/5', '4/5', 4))
add(id='D2', name='Example 13 on a deformed cone',
    U=f'({Q}-z*(x*(x+2*y)+3*x*z))**2+z**5*x+z**4*x*y+z**6/2',
    why='Q replaced by Q - z m: the gutter is a curved surface, effective potential as in Example 13',
    core=circle_core(),
    witness=('arc', f'{Q}-z*(x*(x+2*y)+3*x*z)', '3/5', '-4/5', 4))

# ============================================================ flat gutter (great circle)
add(id='F1', name='flat gutter z=0 with a linear term in z (effective potential by completing the square)',
    U='z**2*(x**2+y**2+z**2)+z*(x**4+2*x*y**3)+y**6+x**5*y',
    why='u_4 = z^2 |q|^2: gutter = equator; u_5 = z f_4 vanishes on it; G = W_6 - f_4^2/4 is not a polynomial restriction',
    core=dict(sos=[(1, 'z*x'), (1, 'z*y'), (1, 'z**2')], sigma=[dict(kind='curve', f='z')]))

# ============================================================ multiplicity >= 4
add(id='M1', name='(z - x^2)^4 + x^5 + y^5',
    U='(z-x**2)**4+x**5+y**5+x*y**6+y*x**6',
    why='gutter z=0 of multiplicity 4, quasi-homogeneous only after the non-linear change z -> z - x^2; negativity along a PARABOLA',
    core=dict(sos=[(1, 'z**2')], sigma=[dict(kind='curve', f='z')]))
add(id='M2', name='z^4 + z (x^4+y^4) + x^6 : quasi-homogeneous principal part, tail in the gap',
    U='z**4+z*(x**4+x**3*y+y**4)+x**6+x*z**5+2*y*z**5',
    witness=('curve', ('tau**3', '0', '-tau**4/2')),
    why='principal part (weights 3,3,4) has no critical points, but the tail x^6 has weighted degree 18 < d + a_min = 19',
    core=dict(sos=[(1, 'z**2')], sigma=[dict(kind='curve', f='z')]))

# ============================================================ point horns
add(id='P1', name='x^4+y^4-z^6 + tail x^3z^2+2y^3z^2 (in the gap of Palamodov Thm 6)',
    U='x**4+y**4-z**6+x**3*z**2+2*y**3*z**2+x*z**6+3*y*z**6',
    why='quasi-homogeneous principal part (3,3,2), d=12; tail x^3 z^2 of weighted degree 13 < d + a_min = 14',
    core=dict(sos=[(1, 'x**2'), (1, 'y**2')], sigma=[dict(kind='points', pts=[(0, 0, 1)])]))
add(id='P2', name='four zero directions, nondegenerate: Theorem B territory',
    U='(x**2-z**2)**2+(y**2-z**2)**2+x*y*z**3+2*x*z**4',
    why='u_4 vanishes at 8 points of the sphere with nondegenerate transverse Hessian; u_5 != 0 at all of them',
    core=dict(sos=[(1, 'x**2-z**2'), (1, 'y**2-z**2')], sigma=[dict(kind='points', pts=[(1, 1, 1), (1, -1, 1), (-1, 1, 1), (-1, -1, 1)])]))
add(id='P3', name='four zero directions, u_5 vanishes at two of them',
    U='(x**2-z**2)**2+(y**2-z**2)**2+(x-z)*z**4-z**6',
    why='B3 fails at two zero directions (1,+-1,1)',
    core=dict(sos=[(1, 'x**2-z**2'), (1, 'y**2-z**2')], sigma=[dict(kind='points', pts=[(1, 1, 1), (1, -1, 1), (-1, 1, 1), (-1, -1, 1)])]))
add(id='P4', name='three axes, u_5 = x^5+y^5 vanishes on the third axis',
    U='x**2*y**2+y**2*z**2+z**2*x**2+x**5+y**5+z*x**4+z**6+x*z**5+2*y*z**5+x*y**4+y*x**4',
    why='B3 fails at the z-axis directions (u_5(e_z) = 0), but U < 0 along the other two axes',
    core=dict(sos=[(1, 'x*y'), (1, 'y*z'), (1, 'z*x')], sigma=[dict(kind='points', pts=[(1, 0, 0), (0, 1, 0), (0, 0, 1)])]))

add(id='Z1', name='mixed zero set: equator + poles',
    U='z**2*(x**2+y**2)+x**5+y**5+z**5+z*x**4+x*z**4+2*y*z**4+x*y**4+y*x**4',
    why='u_4 = z^2 (x^2+y^2): Sigma = great circle z=0 (Hessian rank 1) UNION two poles (rank 2): components of different dimension, outside the statement of Theorem B',
    core=dict(sos=[(1, 'z*x'), (1, 'z*y')], sigma=[dict(kind='curve', f='z'), dict(kind='points', pts=[(0, 0, 1)])]))

# ============================================================ singular gutter, cubic gutter
add(id='S1', name='singular gutter: two crossing great circles',
    U='(x**2-y**2)**2+x**5+2*y**5+z*(x**4+y**4)+z**6',
    why='u_4 = (x^2-y^2)^2: Sigma = two great circles meeting at the poles: not a submanifold; x^5+2y^5 and z(x^4+y^4) keep 0 isolated and break all reductions',
    core=dict(sos=[(1, 'x**2-y**2')], sigma=[dict(kind='curve', f='x-y'), dict(kind='curve', f='x+y')]))
add(id='T1', name='cubic gutter, m=6',
    U='(y**2*z-x**3-x*z**2)**2+y**8/8-z**8+y*z**7',
    why='u_6 = C^2, C = y^2 z - x^3 - x z^2 a smooth real cubic: gutter is an elliptic curve (not a conic); u_7 = 0, W_8 = y^8/8 - z^8',
    core=dict(sos=[(1, 'y**2*z-x**3-x*z**2')], sigma=[dict(kind='curve', f='y**2*z-x**3-x*z**2')]))

# ============================================================ Hessian >= 0 (m = 2): reduce to the kernel
add(id='H1', name='corank 1, curved valley',
    U='(y-x**2)**2+(z-x**3)**2-x**7',
    why='u_2 = y^2+z^2, kernel = x-axis; the valley is the twisted cubic (x, x^2, x^3)',
    witness=('curve', ('tau', 'tau**2', 'tau**3')),
    core=dict(sos=[(1, 'y'), (1, 'z')], sigma=[dict(kind='points', pts=[(1, 0, 0)])]))
add(id='H2', name='corank 2, cuspidal valley',
    U='(z-x**2)**2+(x**2-y**3)**2-y**7',
    why='u_2 = z^2, kernel = the plane z=0; reduced 2D potential (x^2-y^3)^2 - y^7 (cusp)',
    witness=('curve', ('tau**3', 'tau**2', 'tau**6')),
    core=dict(sos=[(1, 'z')], sigma=[dict(kind='curve', f='z')]))
