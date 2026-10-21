"""R39: [Experiment] direct check of the (L3) quantity theta_3 for the free field Y of Theorem 2U.

Chart of example SH: longitudinal z, transverse u = L(z) z^c b, L = [[1,0],[z,1]], gamma = 0, c = (2,4).
Field Y = e_z + Zt, Zt = L' z^c b + L z^{c-1}(C b - xi(b))  (gamma = 0).
theta_3(z) := - min over |b| <= r1 and unit w perp Y of  z <w, D_w Y>.
Theory (Section 5.2, step 5 of results/012): theta_3 -> 0 as z -> 0 if xi satisfies (T), (Theta).
Fields:
  good : xi = (b1, 2 b2 + b1^3)      ((T): d xi1/d b2 = 0; (Theta): 2-1 >= 0, 4-2 >= 0)
  diag : xi = C b                    (Y = d_z Phi)
  bad  : xi = (b1 + b2, 2 b2)        (violates (T): d xi1 / d b2 = 1, c1 < c2)
D Y is computed exactly in chart coordinates (z,b) and transported by the inverse chart Jacobian
(mpmath, 40 digits).  Run: ~/venv/bin/python theta3_check.py
"""
import sympy as sp
import mpmath as mp

mp.mp.dps = 40
z, b1, b2 = sp.symbols('z b1 b2', real=True)
c = (2, 4)
C = sp.diag(*c)
L = sp.Matrix([[1, 0], [z, 1]])
Zc = sp.diag(z**c[0], z**c[1])
Zc1 = sp.diag(z**(c[0] - 1), z**(c[1] - 1))
b = sp.Matrix([b1, b2])
u = L * Zc * b
q = sp.Matrix([u[0], u[1], z])          # point in R^3 (x, y, z)
Jq = q.jacobian([b1, b2, z])             # dq / d(b1,b2,z)

fields = {
    'good': sp.Matrix([b1, 2 * b2 + b1**3]),
    'diag': C * b,
    'bad': sp.Matrix([b1 + b2, 2 * b2]),
}

r1 = 0.5
grid = [(r1 * mp.cos(2 * mp.pi * k / 24) * rr, r1 * mp.sin(2 * mp.pi * k / 24) * rr)
        for k in range(24) for rr in (mp.mpf('0.3'), mp.mpf('0.7'), mp.mpf(1))] + [(0, 0)]

for name, xi in fields.items():
    Zt = L.diff(z) * Zc * b + L * Zc1 * (C * b - xi)
    Y = sp.Matrix([Zt[0], Zt[1], 1])
    JY = Y.jacobian([b1, b2, z])
    fJq = sp.lambdify((z, b1, b2), Jq, 'mpmath')
    fJY = sp.lambdify((z, b1, b2), JY, 'mpmath')
    fY = sp.lambdify((z, b1, b2), Y, 'mpmath')
    print(f'field {name}:')
    for zz in ('1e-2', '1e-3', '1e-4', '1e-5', '1e-6'):
        zz = mp.mpf(zz)
        worst = mp.inf
        for (bb1, bb2) in grid:
            A = mp.matrix(fJq(zz, bb1, bb2))
            DY = mp.matrix(fJY(zz, bb1, bb2)) * mp.inverse(A)   # DY in (x,y,z) coordinates
            Yv = mp.matrix(fY(zz, bb1, bb2))
            # orthonormal basis of Y^perp
            e1 = mp.matrix([1, 0, 0]); e2 = mp.matrix([0, 1, 0])
            def proj(v, ws):
                for w in ws:
                    v = v - (v.T * w)[0] * w
                return v
            yn = Yv / mp.norm(Yv)
            w1 = proj(e1, [yn]); w1 = w1 / mp.norm(w1)
            w2 = proj(e2, [yn, w1]); w2 = w2 / mp.norm(w2)
            W = [w1, w2]
            S = mp.matrix(2, 2)
            for i in range(2):
                for j in range(2):
                    S[i, j] = zz * ((W[i].T * DY * W[j])[0] + (W[j].T * DY * W[i])[0]) / 2
            ev = mp.eigsy(S)[0]
            worst = min(worst, min(ev[0], ev[1]))
        print(f'   z={mp.nstr(zz,3):>7}  min z<w,D_wY>/|w|^2 = {mp.nstr(worst, 8)}')
