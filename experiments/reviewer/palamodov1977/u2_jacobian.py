"""[Эксперимент] u2 = x1^5 - (x2 - x1^2)^2: полный якобиан поля v статьи (Delta = delta у
конца дуги a(r), куски Delta_i там не действуют) в точках alpha = a(r) + t*r.
Печатаем min собственное число симметрической части v' и <v, u'>."""
import numpy as np
from scipy.optimize import brentq

def g(x1, x2):
    return np.array([5 * x1**4 + 4 * x1 * (x2 - x1**2), -2 * (x2 - x1**2)])

def u(x1, x2):
    return x1**5 - (x2 - x1**2) ** 2

def phi_x(x):
    gg = g(*x)
    d = np.arctan2(gg[1], gg[0]) - np.arctan2(-x[1], -x[0])
    return (d + np.pi) % (2 * np.pi) - np.pi

def delta_x(x):
    p = phi_x(x)
    return p - np.pi / 2 if p >= np.pi / 2 else (p + np.pi / 2 if p <= -np.pi / 2 else 0.0)

def v(x):
    D = delta_x(x)
    c, s = np.cos(D), np.sin(D)
    return np.array([c * x[0] - s * x[1], s * x[0] + c * x[1]])

for r in (1e-2, 1e-3, 1e-4):
    # upper boundary of the cusp U^+ : x2 = x1^2 + x1^{5/2}; arc end a(r) solves u = 0 just above it
    f = lambda a: u(r * np.cos(a), r * np.sin(a))
    a = brentq(f, r * (1 + 0.5 * np.sqrt(r)), r * (1 + 3 * np.sqrt(r)) + 2 * r**1.5)
    assert f(a + 1e-3 * r) < 0
    for t in (0.001, 0.01, 0.1, 0.3, 0.6):
        al = a + t * r
        x = r * np.array([np.cos(al), np.sin(al)])
        h = 1e-7 * r
        J = np.column_stack([(v(x + h * e) - v(x - h * e)) / (2 * h) for e in np.eye(2)])
        mu = np.linalg.eigvalsh(0.5 * (J + J.T))[0]
        print(f"r={r:g}, alpha=a+{t}r: u={u(*x):+.2e}, delta={delta_x(x):+.3e},"
              f" min eig sym(v')={mu:+.4f}, <v,u'>={np.dot(v(x), g(*x)):+.2e}")
