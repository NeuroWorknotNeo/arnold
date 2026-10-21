# R38: bottom of U_II on spheres |q|=r (minimum of U on the sphere). eta=1/2.
import mpmath as mp, numpy as np
mp.mp.dps = 40
eta = mp.mpf(1)/2
def U(x, y, z): return x**2*y**2 + 2*x*y*z**3 + eta*z**6 + x**6 + y**6
def f(th1, th2, r):
    c = 1/mp.sqrt(1+th1**2+th2**2)
    return U(r*c*th1, r*c*th2, r*c)
# coarse global search on the sphere (numpy, double) to locate global minima
def Unp(x, y, z, et=0.5): return x**2*y**2 + 2*x*y*z**3 + et*z**6 + x**6 + y**6
for r in [1e-1, 1e-2, 1e-3]:
    th = np.linspace(0, np.pi, 1201); ph = np.linspace(0, 2*np.pi, 2401)
    T, P = np.meshgrid(th, ph, indexing='ij')
    X, Yv, Z = r*np.sin(T)*np.cos(P), r*np.sin(T)*np.sin(P), r*np.cos(T)
    V = Unp(X, Yv, Z)
    i = np.unravel_index(np.argmin(V), V.shape)
    print(f"r={r:g}: grid min U/r^6={V[i]/r**6:.6f} at (x,y,z)/r=({X[i]/r:.4f},{Yv[i]/r:.4f},{Z[i]/r:.4f}); angle to +-e_z={min(T[i],np.pi-T[i]):.4f}, sqrt(2r)={np.sqrt(2*r):.4f}")
# local refinement near the vertex of the hyperbola
for r in [mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4'), mp.mpf('1e-6'), mp.mpf('1e-8')]:
    g1 = lambda a, b: mp.diff(lambda s: f(s, b, r), a)
    g2 = lambda a, b: mp.diff(lambda s: f(a, s, r), b)
    sol = mp.findroot([g1, g2], (mp.sqrt(r), -mp.sqrt(r)))
    a, b = sol[0], sol[1]
    th = mp.sqrt(a**2+b**2)
    print(f"r={mp.nstr(r,3)}: |theta|/sqrt(2r)={mp.nstr(th/mp.sqrt(2*r),10)}, th1*th2/(-r)={mp.nstr(a*b/(-r),10)}, U/r^6={mp.nstr(f(a,b,r)/r**6,10)}, -(1-eta)={-(1-eta)}")
