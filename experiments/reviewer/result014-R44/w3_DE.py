"""R44: пример W3, (DE) в точке (0,0) минимального дна: тождество и численные оценки на сетке."""
import sympy as sp, numpy as np
t, e = sp.symbols('tau e', real=True)
P = (e**2 + sp.sin(t)/2)**2 + sp.Rational(3, 4)*sp.sin(t)**2
lhs = t*sp.diff(P, t) + sp.Rational(1, 2)*e*sp.diff(P, e) - 2*P
print('identity:', sp.simplify(lhs - (t*sp.cos(t) - sp.sin(t))*(e**2 + 2*sp.sin(t))) == 0)
Pf = sp.lambdify((t, e), P, 'numpy'); Rf = sp.lambdify((t, e), lhs, 'numpy')
T, E = np.meshgrid(np.linspace(-0.2, 0.2, 2001), np.linspace(-0.2, 0.2, 2001))
Pv = Pf(T, E); Rv = Rf(T, E)
mask = (T**2 + E**4) > 0
print('min P/(tau^2+e^4) on [-0.2,0.2]^2:', (Pv[mask]/(T[mask]**2 + E[mask]**4)).min())
print('max |R|/P on [-0.2,0.2]^2:', (np.abs(Rv[mask])/Pv[mask]).max())
