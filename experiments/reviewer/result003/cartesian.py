"""Independent Cartesian check (reviewer R4) of lemmas 5,6 of results/003. [Experiment]
V built directly in Cartesian coordinates; Jacobian by sympy differentiation; vectorized numpy."""
import sympy as sp, numpy as np
x, y, z = sp.symbols('x y z', real=True)
Q = x**2+y**2-z**2; U = Q**2+z**5*x+z**4*x*y+sp.Rational(1,2)*z**6
gU = sp.Matrix([sp.diff(U, v) for v in (x, y, z)])
rho = sp.sqrt(x**2+y**2); s = (rho+z)/sp.sqrt(2); d = (rho-z)/sp.sqrt(2)
n = (sp.Matrix([x/rho, y/rho, 0]) - sp.Matrix([0, 0, 1]))/sp.sqrt(2)
dphi = sp.Matrix([-y, x, 0])
kap, kapp = sp.Rational(1,100), sp.Rational(1,50)
q = sp.Matrix([x, y, z])
V = (q + d*n)/6 - kap*(gU.dot(n))/s**2*n - kapp*(gU.dot(dphi))/s**6*dphi
J = V.jacobian([x, y, z])
fJ = [[sp.lambdify((x, y, z), J[i, j], 'numpy') for j in range(3)] for i in range(3)]
fV = [sp.lambdify((x, y, z), V[i], 'numpy') for i in range(3)]
fU = sp.lambdify((x, y, z), U, 'numpy')
fgU = [sp.lambdify((x, y, z), gU[i], 'numpy') for i in range(3)]
A = 0.6313773675921359; C0 = np.sqrt(2*A)
PH, ET = np.meshgrid(np.linspace(0, 2*np.pi, 1441)[:-1], np.linspace(-2*C0, 2*C0, 801))
PH = PH.ravel(); ET = ET.ravel()
for sv in (0.17, 0.1, 0.03, 0.01, 0.003, 0.001):
    dv = sv*sv*ET; r = (sv+dv)/np.sqrt(2); Z = (sv-dv)/np.sqrt(2); X = r*np.cos(PH); Y = r*np.sin(PH)
    M = np.empty((X.size, 3, 3))
    for i in range(3):
        for j in range(3):
            M[:, i, j] = fJ[i][j](X, Y, Z) * np.ones_like(X)
    lam = np.linalg.eigvalsh((M+np.transpose(M, (0, 2, 1)))/2)[:, 0]
    u = fU(X, Y, Z)
    vv = np.stack([fV[i](X, Y, Z)*np.ones_like(X) for i in range(3)], 1)
    g = np.stack([fgU[i](X, Y, Z)*np.ones_like(X) for i in range(3)], 1)
    w = ((g*vv).sum(1) - 0.5*u)/sv**6
    neg = u < 0
    print(f's={sv}: lambda_min SymDV={lam.min():.5f}; max|V|/|q|={(np.linalg.norm(vv,axis=1)/np.sqrt(X*X+Y*Y+Z*Z)).max():.4f};'
          f' #U<0={neg.sum()}; max (<gradU,V>-U/2)/s^6 on U<0 = {w[neg].max():.3e}; on U/s^6<0.02: {w[u/sv**6<0.02].max():.3e}', flush=True)
