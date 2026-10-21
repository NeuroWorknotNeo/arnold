"""Thin wrapper around the Singular binary (passagemath-singular wheel).  All computations over Q."""
import os, re, subprocess, tempfile, sys
import sympy as sp

SINGULAR = os.environ.get('SINGULAR', os.path.expanduser(
    '~/venv/lib/python3.14/site-packages/sage_wheels/bin/Singular'))

def to_sing(expr):
    """sympy polynomial -> Singular string (rational coefficients allowed)"""
    e = sp.expand(expr)
    if e == 0:
        return '0'
    xs = sorted(e.free_symbols, key=str) or [sp.Symbol('x')]
    den = sp.ilcm(1, 1, *[sp.Rational(c).q for c in sp.Poly(e, *xs).coeffs()])
    s = sp.sstr(sp.expand(e * den))      # scaling by a positive integer changes nothing we compute
    return s.replace('**', '^')

def run(script, timeout=600):
    """run a Singular script, return stdout without the 'redefining' noise"""
    script = re.sub(r'(ring \w+=[^;]*;)', r'\1 short=0;', script)      # 'short' is a ring property: print x^32, not x32
    with tempfile.NamedTemporaryFile('w', suffix='.sing', delete=False) as f:
        f.write(script + '\nquit;\n'); name = f.name
    try:
        p = subprocess.run([SINGULAR, '-q', name], capture_output=True, text=True, timeout=timeout)
    finally:
        os.unlink(name)
    out = '\n'.join(l for l in p.stdout.splitlines() if 'redefining' not in l)
    if p.returncode != 0 or 'error' in p.stderr.lower() or '? ' in out:
        raise RuntimeError('Singular failed:\n' + out + '\n' + p.stderr)
    return out

HEAD = 'LIB "sing.lib"; LIB "elim.lib"; LIB "primdec.lib"; short=0;\n'

def local_milnor(U, vars_=('x', 'y', 'z')):
    """dimension of the local Jacobian algebra at 0 (Milnor number); -1 if infinite.  Local ordering ds."""
    v = ','.join(vars_)
    out = run(HEAD + f'ring r=0,({v}),ds; poly U={to_sing(U)}; ideal J=jacob(U); vdim(std(J));')
    return int(out.split()[-1])

def sat_check(gens, pos_poly, vars_=('x', 'y', 'z')):
    """K = <gens> : pos_poly^infty.  Returns (K_is_unit, K_subset_of_m, K_generators_str).
    0 not in V(K)  <=>  K not contained in m = <vars>."""
    v = ','.join(vars_)
    g = ','.join(to_sing(e) for e in gens)
    out = run(HEAD + f'''ring r=0,({v}),dp; ideal J={g}; ideal K=sat(J,ideal({to_sing(pos_poly)}));
    ideal SK=std(K); ideal mm=maxideal(1);
    print("UNIT=" + string(reduce(1,SK)==0));
    print("INM=" + string(size(reduce(SK,std(mm)))==0));
    print("K=" + string(SK));''')
    unit = 'UNIT=1' in out
    inm = 'INM=1' in out
    k = re.search(r'K=(.*)', out, re.S).group(1).strip()
    return unit, inm, k

def min_ass(gens, vars_=('x', 'y', 'z'), timeout=60):
    v = ','.join(vars_); g = ','.join(to_sing(e) for e in gens)
    out = run(HEAD + f'''ring r=0,({v}),dp; ideal J={g}; list L=minAssGTZ(J); int i;
    for(i=1;i<=size(L);i++){{ print("COMP " + string(i) + " dim=" + string(dim(std(L[i]))) + " : " + string(L[i])); }}''', timeout=timeout)
    return [l for l in out.splitlines() if l.startswith('COMP')]

if __name__ == '__main__':
    x, y, z = sp.symbols('x y z')
    U = (x**2+y**2-z**2)**2 + z**5*x + z**4*x*y + sp.Rational(1, 2)*z**6
    J = [sp.diff(U, v) for v in (x, y, z)]
    print(local_milnor(U))
    print(sat_check(J, x**2+y**2+z**2))
    print(min_ass(J))
