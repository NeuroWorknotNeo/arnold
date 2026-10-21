# R38: nonzero real critical points of U_II predicted by Prop. 5.1(a): z^3=(1-eta)/(3 eta^2), y=-x, x^2=eta z^3
import sympy as sp
X, Y, Z = sp.symbols('x y z', real=True)
for eta in [sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(9, 10)]:
    U = X**2*Y**2 + 2*X*Y*Z**3 + eta*Z**6 + X**6 + Y**6
    z0 = sp.cbrt((1-eta)/(3*eta**2)); x0 = sp.sqrt(eta*z0**3)
    g = [sp.simplify(sp.diff(U, v).subs({X: x0, Y: -x0, Z: z0})) for v in (X, Y, Z)]
    print(f"eta={eta}: grad at (x0,-x0,z0) = {g}; radius |z0| = {sp.N(z0, 8)}, |q| = {sp.N(sp.sqrt(2*x0**2+z0**2), 8)}")
