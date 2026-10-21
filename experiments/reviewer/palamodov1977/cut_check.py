"""[Эксперимент] u3 = x1^3 - x2^2 (U^+ -- касп вокруг луча alpha = 0, U^- -- остальное).
Угол alpha берётся в (-pi, pi], как в лемме 5 статьи; разрез alpha = pi лежит внутри дуги U^-.
Пары (alpha, beta) по разные стороны каспа: |beta - alpha| мало, а phi(beta) - phi(alpha) > pi.
Сравниваем с g(r) = min{|beta - alpha| : phi(beta) - phi(alpha) = pi} (нижняя граница P'_2)."""
import numpy as np

def phi(al, r):
    x1, x2 = r * np.cos(al), r * np.sin(al)
    g1, g2 = 3 * x1**2, -2 * x2
    d = np.arctan2(g2, g1) - np.arctan2(-x2, -x1)
    return (d + np.pi) % (2 * np.pi) - np.pi

for r in (1e-2, 1e-3):
    # cusp boundary: x2^2 = x1^3, angle ~ sqrt(r)
    ab = np.arctan(np.sqrt(r * np.cos(0)))  # rough
    from scipy.optimize import brentq
    f = lambda a: (r * np.cos(a))**3 - (r * np.sin(a))**2
    ab = brentq(f, 1e-9, 0.5)
    up = ab + np.concatenate([[1e-12], np.geomspace(1e-9, 0.5, 3000)])  # alpha > 0 side (in U^-)
    lo = -up                                           # symmetric side
    pu, pl = phi(up, r), phi(lo, r)
    # pairs alpha = lo[i] < beta = up[j]
    D = pu[None, :] - pl[:, None]
    W = up[None, :] - lo[:, None]
    over = D > np.pi
    print(f"r={r:g}: cusp half-width {ab:.4e}; pair at the cusp edges: |beta-alpha| = {2*ab:.4e},"
          f" phi(beta)-phi(alpha)-pi = {pu[0]-pl[0]-np.pi:+.3e}")
    eq = np.abs(D - np.pi) < 1e-3 * np.sqrt(r)
    if eq.any():
        print(f"   min |beta-alpha| over pairs with phi(beta)-phi(alpha) = pi (approx.): {W[eq].min():.4e}")
    print(f"   max |beta-alpha| among pairs with difference > pi: {W[over].max():.4e}")
