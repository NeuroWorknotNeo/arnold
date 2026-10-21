"""R34: sensitivity test for check_identities.py -- perturbed identities must FAIL.
[Experiment: sympy.]"""
import runpy, sys, io
src = open('check_identities.py').read()
tests = {
 'drop -L x^{c-1} s/N d_s xi in (I4)': ("            - L * xcm1 * (S / N) * xis)", "            )"),
 'drop -L\' x^c xi in (I4)': ("            - L.diff(x) * xc * xiB - L * xcm1", "            - L * xcm1"),
 'wrong sign of xi in (I1)': ("+ xi_vec(s_of_x, Bv) / x)", "- xi_vec(s_of_x, Bv) / x)"),
 'A without x^{ci-cj} in (I3)': ("x**(cs[i] - cs[j]) * ((cs[i]", "((cs[i]"),
}
for name, (a, b) in tests.items():
    assert a in src, name
    s2 = src.replace(a, b)
    buf = io.StringIO(); old = sys.stdout; sys.stdout = buf
    try:
        exec(compile(s2, 'perturbed', 'exec'), {'__name__': '__main__'})
    finally:
        sys.stdout = old
    out = buf.getvalue()
    print(name, '->', 'FAILED as expected' if 'SOME IDENTITY FAILED' in out else 'NOT DETECTED')
