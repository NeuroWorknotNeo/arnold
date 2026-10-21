# [Эксперимент] Примеры записки notes/prover/2026-10-21-morse-bott.md: эффективный потенциал
# G = g_j на окружностях Sigma_+ (z>0) и Sigma_- (z<0) конуса Q0 = x^2+y^2-z^2 = 0 и тип случая
# (a)/(b)/(c)/(d) предложения M0. Ряды y*(s), R(s) = sum s^i g_{m+i} — функция fiber_series из
# experiments/prover/gt3-hardcore/reduced.py (точная арифметика sympy).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'gt3-hardcore'))
import sympy as sp
from reduced import fiber_series, x, y, z, s

ph = sp.symbols('phi', real=True)
Q0 = x**2 + y**2 - z**2
omP = [sp.cos(ph)/sp.sqrt(2), sp.sin(ph)/sp.sqrt(2), 1/sp.sqrt(2)]
nP = [-sp.cos(ph)/sp.sqrt(2), -sp.sin(ph)/sp.sqrt(2), 1/sp.sqrt(2)]
omM = [-t for t in omP]            # Sigma_- = -Sigma_+, натуральный параметр тот же
EXAMPLES = {
    'C1':  (Q0**2 - z**6 + x*z**6, 4),
    'C2':  ((Q0 + z**3)**2 - z**7 + x*y*z**6, 4),
    'D1':  (Q0**2 + y**2*z**4 + x*z**6 + x*y*z**5, 4),
    'D2s': (Q0**2 + 4*y**4*z**2 + x*z**6, 4),
    'D2':  (Q0**2 + 4*y**4*z**2 + x*z**6 + x*y*z**5, 4),
    'B':   (Q0**2 - z**6 + 4*y**4*z**2 + x*y*z**5, 4),
    'D3':  ((Q0 + z**3)**2 + y**2*z**6 + x*z**8, 4),
}

def gk(U, m, om, order):
    ys, R = fiber_series(U, m, om, [nP], order)
    return ys, {m + i: sp.simplify(sp.expand_trig(R.coeff(s, i))) for i in range(1, order + 1)}

if __name__ == '__main__':
    names = sys.argv[1:] or list(EXAMPLES)
    for name in names:
        U, m = EXAMPLES[name]
        print('=' * 72); print(name, ': U =', U)
        for lab, om in (('Sigma_+', omP), ('Sigma_-', omM)):
            ys, g = gk(U, m, om, 5)
            j = min((k for k in g if g[k] != 0), default=None)
            print(' ', lab, ': y*(s) =', sp.simplify(ys[0]).series(s, 0, 4) if j else '')
            for k in sorted(g):
                print('    g_%d =' % k, g[k])
            if j is None:
                print('    j > m+5'); continue
            G = g[j]
            Gn = sp.lambdify(ph, G, 'math')
            import math
            vals = [Gn(2*math.pi*i/4000) for i in range(4000)]
            print('    j = %d, G = g_j: min = %.6g, max = %.6g, %s' % (j, min(vals), max(vals),
                  'константа' if sp.simplify(sp.diff(G, ph)) == 0 else 'не константа'))
