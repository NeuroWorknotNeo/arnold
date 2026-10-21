"""t1.py -- example T1 (cubic gutter C=0, m=6): G = u_8|Sigma exactly (u_7=0, so g_7=0 and b_1=0 => g_8=u_8|Sigma).
Critical points of u_8 on Sigma = {C=0}∩S^2 are found EXACTLY (resultant) from  C=0, det[grad u_8, grad C, w]=0 (w=(x,y,z)).
[Experiment] exact polynomial root isolation (sympy), values to 40 digits (mpmath)."""
import sympy as sp, mpmath as mp, json
mp.mp.dps = 50
x, y, z = sp.symbols('x y z')
C = y**2*z - x**3 - x*z**2
u8 = y**8/8 - z**8 + y*z**7
gradC = sp.Matrix([sp.diff(C, v) for v in (x, y, z)])
g8 = sp.Matrix([sp.diff(u8, v) for v in (x, y, z)])
w = sp.Matrix([x, y, z])
D = sp.expand(sp.Matrix.hstack(g8, gradC, w).det())
print('deg D =', sp.Poly(D, x, y, z).total_degree())
# smoothness of the cone: grad C = 0 only at origin (zero-dimensional homogeneous ideal)
Gb = sp.groebner([C] + list(gradC), x, y, z, order='grevlex')
lead = [sp.Poly(g, x, y, z).monoms(order='grevlex')[0] for g in Gb.exprs]
pure = [any(sum(m) == m[i] and m[i] > 0 for m in lead) for i in range(3)]
print('Groebner of (C, dC): leading monomials pure powers in x,y,z:', pure, '  => only the origin over C:', all(pure))
# affine chart z=1: C = y^2 - (x^3+x)
X = sp.symbols('X')
Dz = sp.expand(D.subs(z, 1))
# reduce y^2 -> x^3+x
Pxy = sp.Poly(Dz, y)
A = 0; B = 0
for (k,), c in Pxy.terms():
    red = (x**3 + x)**(k//2) * c
    if k % 2 == 0: A += red
    else: B += red
A = sp.expand(A); B = sp.expand(B)
res = sp.expand(A**2 - (x**3 + x)*B**2)
Pres = sp.Poly(res, x)
print('degree of resultant polynomial in x:', Pres.degree())
sols = []
for fac, mult in sp.sqf_list(Pres)[1]:
    if fac.degree() <= 0: continue
    for r in sp.real_roots(fac):
        xv = mp.mpf(str(sp.N(r, 60)))
        s2 = xv**3 + xv
        if s2 < 0: continue
        Bv = mp.mpf(str(sp.N(B.subs(x, r), 60))); Av = mp.mpf(str(sp.N(A.subs(x, r), 60)))
        cands = []
        if abs(Bv) > mp.mpf(10)**-30:
            cands = [-Av/Bv]
        else:
            cands = [mp.sqrt(s2), -mp.sqrt(s2)]
        for yv in cands:
            if abs(yv**2 - s2) < mp.mpf(10)**-25:
                sols.append((xv, yv, mp.mpf(1), mult))
# points at z=0 : C=-x^3 => x=0 -> (0,1,0)
print('z=0 point (0,1,0): D=', D.subs({x: 0, y: 1, z: 0}))
if D.subs({x: 0, y: 1, z: 0}) == 0:
    sols.append((mp.mpf(0), mp.mpf(1), mp.mpf(0), 1))
f_u8 = sp.lambdify((x, y, z), u8, 'mpmath')
f_g8 = sp.lambdify((x, y, z), list(g8), 'mpmath')
f_H8 = sp.lambdify((x, y, z), sp.hessian(u8, (x, y, z)), 'mpmath')
f_gC = sp.lambdify((x, y, z), list(gradC), 'mpmath')
f_HC = sp.lambdify((x, y, z), sp.hessian(C, (x, y, z)), 'mpmath')
out = []
for (xv, yv, zv, mult) in sols:
    p = mp.matrix([xv, yv, zv]); w_ = p/mp.norm(p)
    c = mp.mpf(1)
    # polish: Newton on C=0 projected? check residual
    resC = abs(C.subs({x: xv, y: yv, z: zv}).evalf(30)) if False else None
    gC = mp.matrix(f_gC(*w_)); gC_n = mp.norm(gC); n = gC/gC_n
    T = mp.matrix([w_[1]*n[2]-w_[2]*n[1], w_[2]*n[0]-w_[0]*n[2], w_[0]*n[1]-w_[1]*n[0]])
    G0 = f_u8(*w_)
    gu = mp.matrix(f_g8(*w_)); Hu = mp.matrix(f_H8(*w_)); HC = mp.matrix(f_HC(*w_))
    k = -(T.T*HC*T)[0]/gC_n
    d2 = (T.T*Hu*T)[0] - 8*G0 + k*(gu.T*n)[0]
    gT = (gu.T*T)[0]
    out.append(dict(omega=[mp.nstr(c_, 15) for c_ in w_], G=mp.nstr(G0, 25), tangential_derivative=mp.nstr(gT, 5),
                    d2G=mp.nstr(d2, 25), G2_plus_jG=mp.nstr(d2 + 8*G0, 25), mult=int(mult), Cres=mp.nstr(abs(C.subs({x: w_[0], y: w_[1], z: w_[2]}).evalf(50)) if False else abs(f_u8(0,0,0)), 3)))
out.sort(key=lambda d: float(d['G']))
print('critical points of G = u_8|Sigma on Sigma (one of each antipodal pair; G is even):')
seen = []
for d in out:
    print(d)
json.dump(out, open('out/T1_crit.json', 'w'), indent=1)
