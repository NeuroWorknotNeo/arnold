"""R28: проверка тождества Эйлера (4.1) на явной функции F (защита от артефактов Subs). [Эксперимент]"""
import sympy as sp

s, th, zeta = sp.symbols('s theta zeta', positive=True)
j, c, a0 = sp.Integer(7), sp.Rational(5, 2), sp.Rational(1, 3)
sig = sp.sqrt(s)
e = zeta * s**(-c)
Sg, E = sp.symbols('S E')
Fexpr = Sg**3 * sp.cos(th) + E**2 * Sg + E**4 * (1 + Sg**2 * sp.sin(th)) - 2
g = s**j * (Fexpr.subs({Sg: sig, E: e}) + a0)
lhs = j * g - s * sp.diff(g, s)
rhs = s**j * (c * E * sp.diff(Fexpr, E) - Sg / 2 * sp.diff(Fexpr, Sg)).subs({Sg: sig, E: e})
print('(4.1) на явной F:', sp.simplify(lhs - rhs) == 0)
