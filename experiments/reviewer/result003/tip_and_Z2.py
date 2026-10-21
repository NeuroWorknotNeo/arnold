"""R4: tip value of Phi and norm of Sym DZ_2 / kappa' (Cartesian). [Experiment]"""
import sympy as sp, numpy as np
from scipy.optimize import brentq
x, y, z = sp.symbols('x y z', real=True)
Q = x**2+y**2-z**2; U = Q**2+z**5*x+z**4*x*y+sp.Rational(1,2)*z**6
gU = sp.Matrix([sp.diff(U, v) for v in (x, y, z)])
rho = sp.sqrt(x**2+y**2); s = (rho+z)/sp.sqrt(2); d = (rho-z)/sp.sqrt(2)
n = (sp.Matrix([x/rho, y/rho, 0]) - sp.Matrix([0, 0, 1]))/sp.sqrt(2)
dphi = sp.Matrix([-y, x, 0]); q = sp.Matrix([x, y, z])
kap, kapp = sp.Rational(1,100), sp.Rational(1,50)
V = (q + d*n)/6 - kap*(gU.dot(n))/s**2*n - kapp*(gU.dot(dphi))/s**6*dphi
W2 = -(gU.dot(dphi))/s**6*dphi   # Z_2 / kappa'
fW = sp.lambdify((x, y, z), (gU.dot(V) - U/2)/s**6, 'mpmath')
JW = W2.jacobian([x, y, z]); fJW = sp.lambdify((x, y, z), JW, 'numpy')
G = lambda t: np.cos(t)*(1+np.sin(t))+0.5; Gp = lambda t: 1-np.sin(t)-2*np.sin(t)**2
import mpmath as mp; mp.mp.dps = 40
for t0 in (brentq(G, 1.6, 2.6), brentq(G, 2.7, 4.6)):
    for sv in (1e-2, 1e-3, 1e-4):
        r = sv/np.sqrt(2); X, Y, Z = mp.mpf(r)*mp.cos(t0), mp.mpf(r)*mp.sin(t0), mp.mpf(r)
        print(f'tip phi={t0:.4f} s={sv}: Phi={float(fW(X,Y,Z)):.6e}  predicted -k\'G\'^2/64={-0.02*Gp(t0)**2/64:.6e}')
A = 0.6313773675921359; C0 = np.sqrt(2*A)
PH, ET = np.meshgrid(np.linspace(0, 2*np.pi, 721)[:-1], np.linspace(-2*C0, 2*C0, 401)); PH = PH.ravel(); ET = ET.ravel()
for sv in (0.1, 0.01, 0.001):
    dv = sv*sv*ET; r = (sv+dv)/np.sqrt(2); Z = (sv-dv)/np.sqrt(2); X = r*np.cos(PH); Y = r*np.sin(PH)
    mx = 0
    for k in range(X.size):
        M = np.array(fJW(X[k], Y[k], Z[k]), dtype=float); mx = max(mx, np.abs(np.linalg.eigvalsh((M+M.T)/2)).max())
    print(f's={sv}: max ||Sym D(Z_2/kappa\')|| = {mx:.4f}  (text bound 0.91+O(s))')
