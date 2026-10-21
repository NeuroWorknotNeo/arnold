"""R42: примеры X1, X2, касп, касание (results/013, §7). [Эксперимент] sympy."""
import sympy as sp

x, y, z, t1, t2, r = sp.symbols('x y z theta1 theta2 r', real=True)
c = (1+t1**2+t2**2)**sp.Rational(-1, 2)
sub = {x: c*t1, y: c*t2, z: c}
grad_th = lambda f, w: w[0]*sp.diff(f, t1) + w[1]*sp.diff(f, t2)
tt = t1**2+t2**2

def homog(U, k):
    P = sp.Poly(sp.expand(U), x, y, z)
    return sum(coef*x**m[0]*y**m[1]*z**m[2] for m, coef in P.terms() if sum(m) == k)

ex = {
    'X1': x**2*y**2 + z*(x**4+y**4) - z**6 + x**6 + y**6,
    'X2': x**2*y**2 + x*y*z**4 - z**7 + x**8 + y**8,
    'cusp': (y**2*z-x**3)**2 - z**8 + x**8 + y**8,
    'tang': y**2*(y*z-x**2)**2 - z**8 + x**8 + y**8,
}
# X1
U = ex['X1']
p5 = homog(U, 5).subs(sub)
print('X1 p5 = c^5(t1^4+t2^4):', sp.simplify(p5 - c**5*(t1**4+t2**4)) == 0)
print('X1 theta.grad q5 = q5(4-5c^2|t|^2):', sp.simplify(grad_th(p5, (t1, t2)) - p5*(4-5*c**2*tt)) == 0)
p6 = homog(U, 6).subs(sub)
print('X1 p6 = c^6(-1+t1^6+t2^6):', sp.simplify(p6 - c**6*(-1+t1**6+t2**6)) == 0)
# X2
U = ex['X2']
print('X2 p5 =', homog(U, 5), '; p6 - c^6 t1 t2 =', sp.simplify(homog(U, 6).subs(sub) - c**6*t1*t2),
      '; p7 + c^7 =', sp.simplify(homog(U, 7).subs(sub) + c**7))
# cusp
U = ex['cusp']
p6 = homog(U, 6).subs(sub)
F = t2**2 - t1**3
print('cusp p6 = c^6 F^2:', sp.simplify(p6 - c**6*F**2) == 0, '; homog7 =', homog(U, 7))
xw = (2*t1, 3*t2)
print('cusp xi_w.grad F = 6F:', sp.expand(grad_th(F, xw) - 6*F) == 0)
print('cusp xi_w.grad c^6 = -3c^8(4t1^2+6t2^2):', sp.simplify(grad_th(c**6, xw) + 3*c**8*(4*t1**2+6*t2**2)) == 0)
print('cusp xi_w.grad p6 = p6*6(2-t2^2)/(1+t^2):', sp.simplify(grad_th(p6, xw) - p6*6*(2-t2**2)/(1+tt)) == 0)
p8 = homog(U, 8).subs(sub)
Lam = p8 + 1
print('cusp p8 = c^8(-1+t1^8+t2^8):', sp.simplify(p8 - c**8*(-1+t1**8+t2**8)) == 0)
s_ = sp.symbols('s')
ser = lambda f: sp.series(f.subs({t1: s_*t1, t2: s_*t2}), s_, 0, 4).removeO().subs(s_, 1)
print('cusp Lambda ~', sp.expand(ser(Lam)), '; xi_w.grad L - L ~', sp.expand(ser(grad_th(Lam, xw) - Lam)))
# tangency
U = ex['tang']
p6 = homog(U, 6).subs(sub)
xw = (t1, 2*t2)
print('tang p6 = c^6 t2^2 (t2-t1^2)^2:', sp.simplify(p6 - c**6*t2**2*(t2-t1**2)**2) == 0, '; homog7 =', homog(U, 7))
print('tang xi_w.grad p6 = p6*2(t1^2-2t2^2+4)/(1+t^2):',
      sp.simplify(grad_th(p6, xw) - p6*2*(t1**2-2*t2**2+4)/(1+tt)) == 0)
Lam = homog(U, 8).subs(sub) + 1
print('tang Lambda ~', sp.expand(ser(Lam)), '; xi_w.grad L - L ~', sp.expand(ser(grad_th(Lam, xw) - Lam)))

# Изолированность
U = ex['cusp']; Ux, Uy, Uz = [sp.diff(U, v) for v in (x, y, z)]
print('cusp identity y/2 U_y - z U_z = 4(y^8+2z^8):', sp.expand(y/2*Uy - z*Uz - 4*(y**8+2*z**8)) == 0)
print('cusp U_x(x,0,0) =', sp.factor(Ux.subs({y: 0, z: 0})))
U = ex['tang']; Ux, Uy, Uz = [sp.diff(U, v) for v in (x, y, z)]
print('tang identity y/2 U_y - z/2 U_z = y^2(yz-x^2)^2+4y^8+4z^8:',
      sp.expand(y/2*Uy - z/2*Uz - (y**2*(y*z-x**2)**2+4*y**8+4*z**8)) == 0)
print('tang U_x(x,0,0) =', sp.factor(Ux.subs({y: 0, z: 0})))
U = ex['X2']; Ux, Uy, Uz = [sp.diff(U, v) for v in (x, y, z)]
print('X2 U_z =', sp.factor(Uz), '; x U_x on xy=7z^3/4:',
      sp.simplify(sp.expand(x*Ux).subs(y, sp.Rational(7, 4)*z**3/x) - (z**6*(sp.Rational(49, 8)+sp.Rational(7, 4)*z)+8*x**8)))
U = ex['X1']; Ux, Uy, Uz = [sp.diff(U, v) for v in (x, y, z)]
print('X1 U_x =', sp.factor(Ux), '; U_z =', Uz)
# Замечание 1: ось инвариантна
for k, U in ex.items():
    print('axis invariant', k, [sp.diff(U, v).subs({x: 0, y: 0}) for v in (x, y)])
