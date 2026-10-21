# Independent check of example 13 chart (section 6 of notes/prover/2026-10-21-gt3.md)
import sympy as sp, numpy as np, random, math
X, Yv, eta = sp.symbols('X Y eta', real=True)
th = sp.atan(Yv/X); s = sp.sqrt(X**2+Yv**2)
phi0 = 5*sp.pi/6; phi = phi0 + sp.sqrt(2)*th
Nh = sp.Matrix([sp.cos(phi), sp.sin(phi), 1])/sp.sqrt(2)
nu = sp.Matrix([sp.cos(phi), sp.sin(phi), -1])/sp.sqrt(2)
tau = sp.Matrix([-sp.sin(phi), sp.cos(phi), 0])
Phi = s*Nh + eta*nu
x, y, z = Phi
Q0 = x**2+y**2-z**2
U = Q0**2 + z**5*x + z**4*x*y + z**6/2
# 1) U∘Phi vs X^6 F(X,t,e)
t, e = sp.symbols('t e', real=True)
S = sp.sqrt(1+t**2)
lam = (S+X*e)/(S-X*e)
ph = phi0 + sp.sqrt(2)*sp.atan(t)
G = lambda L, p: L*sp.cos(p) + L**2*sp.cos(p)*sp.sin(p) + sp.Rational(1,2)
F = 4*(1+t**2)*e**2 + (S-X*e)**6/8*G(lam, ph)
UF = X**6*F.subs({t: Yv/X, e: eta/X**2})
f_U = sp.lambdify((X,Yv,eta), U, 'mpmath'); f_UF = sp.lambdify((X,Yv,eta), UF, 'mpmath')
import mpmath as mp
mp.mp.dps = 40
md = 0
for _ in range(30):
    Xv = mp.mpf(random.uniform(0.01,0.5)); tv = random.uniform(-0.25,0.25); ev = random.uniform(-0.25,0.25)
    a = f_U(Xv, tv*Xv, ev*Xv**2); b = f_UF(Xv, tv*Xv, ev*Xv**2)
    md = max(md, abs(a-b)/abs(a))
print('1) max rel diff U∘Phi vs X^6 F:', md)
# 2) F0, grad, Hessian
F0 = F.subs(X, 0)
g = [sp.simplify(sp.diff(F0, v).subs({t:0, e:0})) for v in (t, e)]
H = sp.Matrix(2,2, lambda i,j: sp.nsimplify(sp.simplify(sp.diff(F0, (t,e)[i], (t,e)[j]).subs({t:0,e:0}))))
print('2) F0(0)=', sp.nsimplify(sp.simplify(F0.subs({t:0,e:0}))), float(F0.subs({t:0,e:0})), ' grad=', g, ' H=', H, [float(hh) for hh in H])
print('   expected H11=(6-3*sqrt3)/16 =', float((6-3*sp.sqrt(3))/16))
# 3) derivative formulas
c, sn = sp.cos(th), sp.sin(th); ep = eta/s
dX = c*Nh - (1+ep)*sn*tau; dY = sn*Nh + (1+ep)*c*tau; deta = nu
dXX = -eta*sn**2/s**2*Nh - (1+ep)*sn**2/s*nu + 2*eta*sn*c/s**2*tau
dYX = eta*sn*c/s**2*Nh + (1+ep)*sn*c/s*nu + eta*(sn**2-c**2)/s**2*tau
detaX = -sn/s*tau
cands = [(sp.diff(Phi,X), dX), (sp.diff(Phi,Yv), dY), (sp.diff(Phi,eta), deta), (sp.diff(Phi,X,2), dXX), (sp.diff(Phi,X,Yv), dYX), (sp.diff(Phi,X,eta), detaX)]
fs = [sp.lambdify((X,Yv,eta), a-b, 'mpmath') for a,b in cands]
mx = 0
for _ in range(20):
    Xv = mp.mpf(random.uniform(0.01,0.5)); tv = random.uniform(-0.25,0.25); ev = random.uniform(-0.25,0.25)
    for f in fs:
        mx = max(mx, max(abs(w) for w in f(Xv, tv*Xv, ev*Xv**2)))
print('3) max abs diff derivative formulas:', mx)
# 4) (Phi1)-(Phi3) numerically, r0=1/4, s0 = 2/3
J = Phi.jacobian([X,Yv,eta])
fJ = sp.lambdify((X,Yv,eta), J, 'numpy')
fdXX = sp.lambdify((X,Yv,eta), sp.diff(Phi,X,2), 'numpy')
fdXY = sp.lambdify((X,Yv,eta), sp.diff(Phi,X,Yv), 'numpy')
fdXe = sp.lambdify((X,Yv,eta), sp.diff(Phi,X,eta), 'numpy')
r0 = 0.25; s0 = 2/3
worst = {'BI':0, 'Bxu/(r0X)':0, 'Phi2':-1e9, 'Phi3':-1e9, 'Phi3ratioC':0}
rng = np.random.default_rng(1)
for _ in range(20000):
    Xv = rng.uniform(1e-4, s0)
    while True:
        b = rng.uniform(-r0, r0, 2)
        if np.linalg.norm(b) < r0: break
    tv, ev = b; Yq, eq = tv*Xv, ev*Xv**2
    Jm = np.array(fJ(Xv,Yq,eq), dtype=float); B = Jm.T@Jm
    worst['BI'] = max(worst['BI'], np.linalg.norm(B-np.eye(3),2))
    worst['Bxu/(r0X)'] = max(worst['Bxu/(r0X)'], np.linalg.norm(B[0,1:])/(r0*Xv))
    a = np.array(fdXX(Xv,Yq,eq),dtype=float).ravel(); Yx = Jm[:,0]
    aperp = a - (a@Yx)/(Yx@Yx)*Yx
    nb = np.linalg.norm(b)
    worst['Phi2'] = max(worst['Phi2'], Xv*np.linalg.norm(aperp) - (5*nb**2 + 5*r0*Xv))
    # (Phi3): w ⊥ Yx, w = J zeta, D_wY = zeta0*dXX + zeta1*dXY + zeta2*dXe
    M = np.column_stack([a, np.array(fdXY(Xv,Yq,eq),dtype=float).ravel(), np.array(fdXe(Xv,Yq,eq),dtype=float).ravel()])
    # basis of Yx-perp
    P = np.linalg.svd(Yx.reshape(1,3))[2][1:]
    for _k in range(5):
        w = rng.normal(size=2) @ P
        zeta = np.linalg.solve(Jm, w)
        val = Xv * w @ (M @ zeta) / (w@w)
        worst['Phi3'] = max(worst['Phi3'], -val - (5*nb + 5*r0*Xv))
        worst['Phi3ratioC'] = max(worst['Phi3ratioC'], -val/(nb + r0*Xv))
    # also minimum over w exactly: symmetric part of quadratic form on perp-plane
print('4)', worst)
