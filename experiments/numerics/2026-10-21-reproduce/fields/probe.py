"""[Эксперимент] Для поля A = U ∇U/|∇U|^2 (A(U)=U, P=1) оценить λ_min(sym DA) на {U<0}
вблизи нуля (случайные точки в шарах радиуса r). Критерий (L') требует λ_min > -1/2."""
import sys
import numpy as np
import sympy as sp

def probe(Uexpr, vars_, radii=(1e-1, 1e-2, 1e-3), N=20000, seed=0):
    n = len(vars_)
    g = [sp.diff(Uexpr, v) for v in vars_]
    G2 = sum(gi**2 for gi in g)
    A = [Uexpr * gi / G2 for gi in g]
    DA = sp.Matrix(n, n, lambda i, j: sp.diff(A[i], vars_[j]))
    fU = sp.lambdify(vars_, Uexpr, 'numpy')
    fD = sp.lambdify(vars_, DA, 'numpy')
    rng = np.random.default_rng(seed)
    out = []
    for r in radii:
        X = rng.normal(size=(N, n))
        X *= (r * rng.random(N) ** (1 / n) / np.linalg.norm(X, axis=1))[:, None]
        worst = np.inf
        arg = None
        for x in X:
            if fU(*x) >= 0:
                continue
            M = np.array(fD(*x), dtype=float)
            lam = np.linalg.eigvalsh((M + M.T) / 2)[0]
            if lam < worst:
                worst, arg = lam, x
        out.append((r, worst, arg))
    return out

if __name__ == '__main__':
    x, y, z = sp.symbols('x y z', real=True)
    tests = {
        'x^2-y^2': (x**2 - y**2, [x, y]),
        'x^3-3xy^2': (x**3 - 3*x*y**2, [x, y]),
        'x(y-3x)': (x*(y - 3*x), [x, y]),
        'y^2-x^4 (quasi)': (y**2 - x**4, [x, y]),
        '(y-x^2)^2-x^5': ((y - x**2)**2 - x**5, [x, y]),
        'x^2+y^2-z^2': (x**2 + y**2 - z**2, [x, y, z]),
        'x^4+y^4-z^2*x^2+...': (x**4 + y**4 + z**4 - 3*x**2*z**2, [x, y, z]),
    }
    for name, (U, vs) in tests.items():
        res = probe(U, vs, N=4000)
        print(name, [(r, round(w, 4)) for r, w, _ in res])
        sys.stdout.flush()
