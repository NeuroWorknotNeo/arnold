# R38: non-applicability checks.
# (1) constant-weight fields rho=z, Y = e_z + (lx x, ly y, 0)/z: direct (A5) minimum on the wall (same sampler as exit_check)
# (2) theta_3 of the field (5.1) near the vertex for several e: shows 4*theta_3 >= 2e (lemma 2 [007] bracket <= 0)
# (3) radial kappa-field of theorem S centred at e_z: (S3) fails since W(r,0) = 1
# (4) theorem 2 [007]: profile F0 in straight weighted charts
import mpmath as mp, exit_check as ec, numpy as np, sympy as sp, sys
mp.mp.dps = 80
which = sys.argv[1] if len(sys.argv) > 1 else 'all'
if which in ('1', 'all'):
    for lx, ly in [(1.5, 1.5), (0.9, 0.9), (0.5, 2.5), (0.0, 0.0), (0.95, 1.95), (-0.5, -0.5)]:
        lxm, lym = mp.mpf(lx), mp.mpf(ly)
        def Yc(q, lxm=lxm, lym=lym):
            x, y, z = q
            return [lxm*x/z, lym*y/z, mp.mpf(1)]
        ec.Yf = Yc; ec.mode = 'C'
        for delta, sigma in [(0.01, 2e-4), (0.01, 2e-6)]:
            w, a4 = ec.sample(mp.mpf(delta), mp.mpf(sigma), 300, 11)
            print(f"const field lx={lx}, ly={ly}: delta={delta} sigma={sigma}: min rho Xi/(lambda delta rho^6) = {mp.nstr(w[0],6)} at x/z^1.5={w[1]}, y/z^1.5={w[2]}, tau={w[4]}")
        sys.stdout.flush()
if which in ('2', 'all'):
    rng = np.random.default_rng(3)
    import spectra_check as sc
    for e in [0.5, 1.0, 1.5, 2.0]:
        z = 1e-6; delta = 0.01
        worst = 1e9; wq = None
        for _ in range(30000):
            # concentrate near the vertex: x = z^1.5 * 10^U(-1,1)
            x = z**1.5*10**rng.uniform(-1.5, 1.5)
            H = rng.uniform(-1, 1)*np.sqrt(delta)*z**3
            y = (H - z**3)/x
            if H**2 + x**6 + y**6 > delta*z**6: continue
            xi, DzXi, zdzxi = sc.field(x, y, z, e)
            Y = np.array([xi[0], xi[1], 1.0])
            n1 = np.cross(Y, [1.0, 0, 0]); n1 /= np.linalg.norm(n1)
            n2 = np.cross(Y, n1); n2 /= np.linalg.norm(n2)
            B = np.stack([n1, n2], axis=1)
            J = np.zeros((3, 3)); J[:2, :2] = DzXi; J[:2, 2] = zdzxi
            Q = B.T @ J @ B; m = np.linalg.eigvalsh((Q+Q.T)/2).min()
            if m < worst: worst, wq = m, (x/z**1.5, y/z**1.5)
        th3 = max(-worst, (3-e)*(np.sqrt(2)-1)/2)
        print(f"e={e}: inf near vertex = {worst:.4f} at {wq}; theta3 >= {th3:.4f}; 4*theta3 = {4*th3:.4f} vs mu<=2e={2*e}")
if which in ('3', 'all'):
    eta = sp.Rational(1, 2); r, t1, t2 = sp.symbols('r t1 t2', positive=True)
    c = 1/sp.sqrt(1+t1**2+t2**2)
    x, y, z = r*c*t1, r*c*t2, r*c
    U = x**2*y**2 + 2*x*y*z**3 + eta*z**6 + x**6 + y**6
    calW = sp.simplify(U/r**6 + (1-eta))
    print("theorem S at e_z: calW(r,0) =", sp.simplify(calW.subs({t1: 0, t2: 0})), " (S3 requires -> 0)")
if which in ('4', 'all'):
    b1, b2, z = sp.symbols('b1 b2 z', real=True)
    eta = sp.Symbol('eta', positive=True)
    U = lambda x, y, z: x**2*y**2 + 2*x*y*z**3 + eta*z**6 + x**6 + y**6
    F_axis = sp.expand(U(z**sp.Rational(3, 2)*b1, z**sp.Rational(3, 2)*b2, z)/z**6)
    print("axis-centred chart, c=(3/2,3/2): F =", F_axis, "; F0(0) =", F_axis.subs({z: 0, b1: 0, b2: 0}))
    F_vert = sp.expand(U(z**sp.Rational(3, 2)*(1+b1), z**sp.Rational(3, 2)*(-1+b2), z)/z**6)
    F0v = sp.factor(F_vert.subs(z, 0)); print("vertex-centred chart, c=(3/2,3/2): F0 =", F0v, "; Q = F0 - F0(0) =", sp.factor(F0v - F0v.subs({b1: 0, b2: 0})))
    print("   Q vanishes on b2 = b1/(1+b1) (unbounded branch): ", sp.simplify((F0v - F0v.subs({b1: 0, b2: 0})).subs(b2, b1/(1+b1))))
