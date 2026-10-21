"""R36: кольцо с глубиной, меняющейся вдоль кольца в порядке x^beta (вне следствия S).
U = (x^2+y^2-z^6)^2 - z^16 + x z^13, луч +e_z, c=(3,3), N=1, beta=16.  [Эксперимент: sympy]"""
import sympy as sp
x, y, z, s, b1, b2, th = sp.symbols('x y z s b1 b2 theta', real=True)
U = (x**2 + y**2 - z**6)**2 - z**16 + x * z**13
F = sp.expand(U.subs({x: z**3 * b1, y: z**3 * b2}, simultaneous=True) / z**16).subs(z, s)
print("F =", F, "; F - (-1 + s^-4(|b|^2-1)^2 + b1) =", sp.simplify(F - (-1 + s**-4 * (b1**2 + b2**2 - 1)**2 + b1)))
EF0 = sp.simplify(-s * sp.diff(F, s))   # xi = 0, N = 1
print("xi=0: E F = -s dF/ds =", sp.factor(EF0))
a0 = 2  # максимум глубины на кольце (theta = pi)
P = F + a0
ring = {b1: sp.cos(th), b2: sp.sin(th)}
print("on ring: P =", sp.simplify(P.subs(ring)), "; E F =", sp.simplify(EF0.subs(ring)),
      "-> (U4) E F >= mu P - eps fails where eps/mu < 1+cos(theta) <= delta")
