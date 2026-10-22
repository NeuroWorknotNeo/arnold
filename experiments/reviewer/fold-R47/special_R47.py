"""R47: частные случаи §3.1 (теоремы W, C) и тождество Xf = (mu/2) f для поля из §0.1."""
import sympy as sp
s, th, e, c, kap, lam, zeta = sp.symbols('s theta epsilon c kappa lambda zeta', positive=True)
# W with eta0 = 0: Psi(s,th,zeta) = Pi(s,th,zeta s^-c). Field Y = d_s - kap th/s d_th + lam zeta/s d_zeta (in Psi coords)
# transform to (s,th,e), e = zeta s^{-c}: Y(e) = d_s e + (-kap th/s) d_th e + (lam zeta/s) d_zeta e
e_of = zeta*s**(-c)
Ye = sp.diff(e_of, s) + lam*zeta/s*sp.diff(e_of, zeta)
print('W: X^e coefficient (Y = ... - X^e/s d_e):', sp.simplify(-s*Ye.subs(zeta, e*s**c)), ' expected (c-lam)*e')
# C with eta0 = s^c eps_g(th): e = eps_g + zeta s^-c, Y = Psi_s (d_s at fixed th, zeta)
eg = sp.Function('eps_g')(th)
e_of2 = eg + zeta*s**(-c)
Ye2 = sp.diff(e_of2, s)
print('C: X^e =', sp.simplify(-s*Ye2.subs(zeta, (e-eg)*s**c)), ' expected c*(e-eps_g)')
# §0.1 field
mu, chi = sp.symbols('mu chi', real=True)
f = e**2 - sp.sin(th)
Xt = mu/2*chi*sp.tan(th)
Xe = mu/4*(e**2 - (1-chi)*sp.sin(th))/e
print('§0.1: Xf - (mu/2) f =', sp.simplify(Xt*sp.diff(f, th) + Xe*sp.diff(f, e) - mu/2*f), '(chi treated as constant; d_th chi does not enter Xf)')
