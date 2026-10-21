#!/usr/bin/env python3
"""selftest.py -- the criteria code on textbook cases (each expectation is mathematically obvious)."""
import analyze
from zoolib import P

def crit(U, core=None, **kw):
    e = dict(id='t', U=U, **kw)
    if core:
        e['core'] = core
    return analyze.analyze(e)

# 1. Lyapunov: indefinite Hessian
r = crit('-x**2+y**2+z**2+x*y*z')
assert r['criteria']['Lyapunov']['status'] == 'yes', r['criteria']['Lyapunov']
# 2. odd lowest form (Kozlov-Palamodov / Chetaev)
r = crit('x**3+y**4+z**4')
assert r['criteria']['KP82']['status'] == 'yes'
# 3. x^4+y^4-z^4: grad of the lowest form vanishes only at 0 and the form is negative somewhere (Palamodov Thm 3), quasi-homogeneous
r = crit('x**4+y**4-z**4+x**3*y**2+z**5')
assert r['criteria']['Pa20-T3']['status'] == 'yes' and r['criteria']['KP82']['status'] == 'yes'
# 4. quasi-homogeneous in linear coordinates with weights (3,3,2)
r = crit('x**4+y**4-z**6')
assert r['criteria']['QH-linear']['status'] == 'yes' and 'weights (3, 3, 2)' in r['criteria']['QH-linear']['why']
# 5. Kozlov 1986: u_2 >= 0 with 2-dim kernel and u_3 negative on the kernel
r = crit('z**2+x**3+y**4')
assert r['criteria']['Koz86']['status'] == 'yes', r['criteria']['Koz86']
# 6. Theorem B on a Morse-Bott example with regular u_5|Sigma (results/002 example, non-symmetric version)
core = dict(sos=[(1, 'x**2+y**2-z**2')], sigma=[dict(kind='curve', f='x**2+y**2-z**2')])
r = crit('(x**2+y**2-z**2)**2+(x+3*y)*z**4', core)
assert r['criteria']['ThmB']['status'] == 'yes'
# 7. Theorem B must FAIL for u_4 = z^4 (not Morse-Bott) and for a double zero of the restriction
r = crit('z**4+x**5+y**5', dict(sos=[(1, 'z**2')], sigma=[dict(kind='curve', f='z')]))
assert r['criteria']['ThmB']['status'] == 'no'
# 8. Burgos Cor. 1.4 positive case: Q^2 - z^6
r = crit('(x**2+y**2-z**2)**2-z**6', core)
assert r['criteria']['Bu25-C1.4']['status'] == 'yes'
# 9. invariant plane: Q^2 + x z^5 is symmetric in y (known from the notes) -> reduces to n=2
r = crit('(x**2+y**2-z**2)**2+x*z**5', core)
assert r['criteria']['SYM']['status'] == 'yes'
# 10. a strict minimum must NOT be reported as covered by anything (x^4+y^4+z^4+...)
r = crit('x**4+y**4+z**4+x**5')
assert not r['covered_known'] and not r['covered_ours']
# 11. the isolation certificate must FAIL for non-isolated critical points (critical cone / critical axis) and hold for x^4+y^4+z^4
import zoolib as zl
for U, expect in (('(x**2+y**2-z**2)**2', False), ('x**2*y**2+z**4+y**4', False), ('x**4+y**4+z**4', True),
                  ('x**2*y**2*z**2+x**6+y**6+z**6', True)):
    ok, _ = zl.real_isolation_cert(zl.grad(P(U)))
    assert ok == expect, (U, ok)
print('selftest OK')
