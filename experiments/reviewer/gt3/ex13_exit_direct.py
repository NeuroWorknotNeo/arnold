# [Experiment] Independent check of strict exit (A5) for example 13: compute Xi = d/dt(V - delta*rho^6)
# directly by differentiating V(q,v) in Cartesian coordinates (not via identity (3.3)).
import sympy as sp, numpy as np
x, y, z, v1, v2, v3 = sp.symbols('x y z v1 v2 v3', real=True)
phi0 = 5*sp.pi/6
R = sp.sqrt(x**2+y**2)
s = (R+z)/sp.sqrt(2); eta = (R-z)/sp.sqrt(2)
th = sp.atan2(-x*sp.sin(phi0)+y*sp.cos(phi0), x*sp.cos(phi0)+y*sp.sin(phi0))/sp.sqrt(2)
X = s*sp.cos(th)
phi = phi0 + sp.sqrt(2)*th
Nh = sp.Matrix([sp.cos(phi), sp.sin(phi), 1])/sp.sqrt(2)
tau = sp.Matrix([-sp.sin(phi), sp.cos(phi), 0])
Yf = sp.cos(th)*Nh - (1+eta/s)*sp.sin(th)*tau     # = d_X Phi at Phi^{-1}(q)
Q0 = x**2+y**2-z**2
U = Q0**2 + z**5*x + z**4*x*y + z**6/2
a0 = -(sp.Rational(1,16) - 3*sp.sqrt(3)/32)
q = [x,y,z]; v = sp.Matrix([v1,v2,v3])
dl = sp.Symbol('dl')
h = Yf.dot(Yf); pi_ = v.dot(Yf)
V = v.dot(v)/2 - pi_**2/(2*h) + U + a0*X**6
Fun = V - dl*X**6
gU = [sp.diff(U, qi) for qi in q]
Xi = sum(sp.diff(Fun, q[i])*v[i] for i in range(3)) + sum(sp.diff(Fun, [v1,v2,v3][i])*(-gU[i]) for i in range(3))
fXi = sp.lambdify((x,y,z,v1,v2,v3,dl), Xi, 'numpy')
fY = sp.lambdify((x,y,z), Yf, 'numpy'); fU = sp.lambdify((x,y,z), U, 'numpy')
fV = sp.lambdify((x,y,z,v1,v2,v3), V, 'numpy')
# chart Phi
def Phi(Xc, Yc, ec):
    sc = np.hypot(Xc, Yc); thc = np.arctan2(Yc, Xc); ph = float(phi0) + np.sqrt(2)*thc
    N = np.array([np.cos(ph), np.sin(ph), 1])/np.sqrt(2); n_ = np.array([np.cos(ph), np.sin(ph), -1])/np.sqrt(2)
    return sc*N + ec*n_
rng = np.random.default_rng(7)
a0f = float(a0)
for delta, sigma in [(0.02, 0.2), (0.005, 0.05), (0.001, 0.02), (0.0002, 0.01)]:
    worst = np.inf; cnt = 0
    while cnt < 3000:
        Xc = rng.uniform(0.05*sigma, sigma)
        b = rng.normal(size=2); b *= rng.uniform(0, 1)**0.5 / np.linalg.norm(b)
        # scale b to roughly the sublevel ellipse Q<=delta: Q ~ H11 t^2/2 + 4 e^2
        tv = b[0]*np.sqrt(2*delta/0.0502); ev = b[1]*np.sqrt(delta/4)
        qv = Phi(Xc, tv*Xc, ev*Xc**2)
        W = fU(*qv) + a0f*Xc**6
        if not (-delta*Xc**6 <= W <= delta*Xc**6): continue
        Yv = np.array(fY(*qv), dtype=float).ravel(); hv = Yv@Yv
        Kp = delta*Xc**6 - W
        # random direction perpendicular to Y
        w = rng.normal(size=3); w -= (w@Yv)/hv*Yv; w /= np.linalg.norm(w)
        vperp = np.sqrt(2*Kp)*w
        piv = -np.sqrt(2*hv*(a0f - delta)*Xc**6)
        vv = piv/hv*Yv + vperp
        E = 0.5*vv@vv + fU(*qv)
        Vv = fV(*qv, *vv)
        assert abs(E) < 1e-9*Xc**6 + 1e-14 and abs(Vv - delta*Xc**6) < 1e-6*Xc**6, (E, Vv, delta*Xc**6)
        lam = -piv/hv
        val = Xc/lam*fXi(*qv, *vv, delta)/(delta*Xc**6)
        worst = min(worst, val); cnt += 1
    print(f'delta={delta}, sigma={sigma}: min (rho/lam) Xi/(delta rho^6) over {cnt} boundary points = {worst:.4f}')
