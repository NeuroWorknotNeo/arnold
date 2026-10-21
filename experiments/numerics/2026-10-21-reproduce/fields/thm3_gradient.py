"""[Эксперимент] Проверка градиентного поля φ = |x|^2/2 − K|x|^{3−m} U (max-gluing.md,
пример к теореме 3) на U = x^3 − 3xy^2 + x^4 + 2y^4 + x^2 y^2 (m = 3):
печатает min λ_min(D²φ) и max <∇φ,∇U>/U по случайным точкам {U<0} в шарах радиуса r."""
import numpy as np
import sympy as sp

x, y = sp.symbols('x y', real=True)
U = x**3 - 3*x*y**2 + x**4 + 2*y**4 + x**2*y**2
m, K = 3, 5
phi = (x**2 + y**2)/2 - K*(x**2 + y**2)**sp.Rational(3 - m, 2)*U
g = [sp.diff(phi, v) for v in (x, y)]
H = sp.hessian(phi, (x, y))
ratio = (g[0]*sp.diff(U, x) + g[1]*sp.diff(U, y))/U
fU, fH, fR = (sp.lambdify((x, y), e, 'numpy') for e in (U, H, ratio))
rng = np.random.default_rng(1)
for r in (0.1, 0.03, 0.01, 0.001):
    P = rng.normal(size=(20000, 2)); P *= (r*rng.random(20000)**0.5/np.linalg.norm(P, axis=1))[:, None]
    P = P[fU(*P.T) < 0]
    lam = min(np.linalg.eigvalsh(np.array(fH(*p), float))[0] for p in P)
    print(f"r={r}: min λ(D²φ)={lam:.4f}, min <∇φ,∇U>/U={np.min(fR(*P.T)):.4f} (нужно >0)")
