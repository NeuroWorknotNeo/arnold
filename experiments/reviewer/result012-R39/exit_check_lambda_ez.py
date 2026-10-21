"""R39: [Experiment] variant of exit_check_lambda.py with Y = e_z (xi = Cb, i.e. Y = d_z Phi). Expect negative minimum.
example Lambda of results/012 with the free field Y = q/z (xi = (C-I)b, gamma = 0, L = I).

Direct differentiation in R^3 x R^3 (no use of Lemma 1 [007] or identities (I1)-(I4)):
  W = U + a0 z^8 (a0 = 1), rho = z, Y = (x/z, y/z, 1), h = |Y|^2, p = <v,Y>,
  V = |v|^2/2 - p^2/(2h) + W,  Xi = grad_q(V - delta rho^8).v - grad_v V . grad U.
Points: q = Phi(z,b) with P(s,b) = F + 1 <= delta, |b| < r1; v with E = 0, p < 0, V = delta rho^8
(K_perp = delta z^8 - W >= 0 distributed over directions of Y^perp).
Printed: min over samples of (rho/lambda) Xi / (delta rho^8), lambda = -p/h.  Theory (Lemma 2 [007]
+ proof of Theorem 2U): >= mu/2 = 2 for small z; the main term tends to mu*... >= mu = 4 at K_perp = 0.
Run: ~/venv/bin/python exit_check_lambda.py
"""
import sympy as sp
import mpmath as mp

mp.mp.dps = 30
x, y, z, vx, vy, vz, dl = sp.symbols('x y z vx vy vz delta', real=True)
k0 = sp.Rational(199, 100)
U = x**4 - k0 * x**2 * y * z + y**2 * z**2 + y**4 - z**8 + x * z**7
q = sp.Matrix([x, y, z]); v = sp.Matrix([vx, vy, vz])
Y = sp.Matrix([0, 0, 1])  # variant: Y = e_z (weights-of-ravine field xi = Cb)
h = (Y.T * Y)[0]
p = (v.T * Y)[0]
W = U + z**8
V = (v.T * v)[0] / 2 - p**2 / (2 * h) + W
G = V - dl * z**8
gradU = sp.Matrix([sp.diff(U, t) for t in (x, y, z)])
Xi = sum(sp.diff(G, qi) * vi for qi, vi in zip(q, v)) - sum(sp.diff(G, vi) * gi for vi, gi in zip(v, gradU))
fXi = sp.lambdify((x, y, z, vx, vy, vz, dl), Xi, 'mpmath')
fU = sp.lambdify((x, y, z), U, 'mpmath')


def P(zz, bb1, bb2):  # P = F + a0, F = z^{-8} U(z^2 b1, z^3 b2, z)
    return fU(zz**2 * bb1, zz**3 * bb2, zz) / zz**8 + 1


for delta in (mp.mpf('0.05'), mp.mpf('0.01')):
    for zz in (mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')):
        worst = mp.inf
        n = 0
        rb1 = mp.mpf('1.15') * (delta * 40000 / 399)**0.25  # Q <= delta forces (399/40000) b1^4 <= delta
        rb2 = mp.mpf('1.15') * (delta**0.5 + k0 * rb1**2 / 2)
        for i in range(-60, 61):
            for j in range(-60, 61):
                bb1 = rb1 * i / 60
                bb2 = rb2 * j / 60
                PP = P(zz, bb1, bb2)
                if PP > delta:
                    continue
                X, Yy = zz**2 * bb1, zz**3 * bb2
                Wv = fU(X, Yy, zz) + zz**8
                Kp = delta * zz**8 - Wv
                Yv = mp.matrix([0, 0, 1])
                hh = (Yv.T * Yv)[0]
                # orthonormal basis of Y^perp
                e = mp.matrix([1, 0, 0])
                yn = Yv / mp.sqrt(hh)
                w1 = e - (e.T * yn)[0] * yn; w1 = w1 / mp.norm(w1)
                w2 = mp.matrix([yn[1] * w1[2] - yn[2] * w1[1], yn[2] * w1[0] - yn[0] * w1[2], yn[0] * w1[1] - yn[1] * w1[0]])
                Uq = fU(X, Yy, zz)
                for k in range(12):
                    ang = 2 * mp.pi * k / 12
                    vperp = mp.sqrt(2 * Kp) * (mp.cos(ang) * w1 + mp.sin(ang) * w2)
                    pp = -mp.sqrt(hh * (-2 * Uq - 2 * Kp))
                    vv = pp / hh * Yv + vperp
                    lam = -pp / hh
                    val = (zz / lam) * fXi(X, Yy, zz, vv[0], vv[1], vv[2], delta) / (delta * zz**8)
                    worst = min(worst, val)
                    n += 1
        print(f'delta={mp.nstr(delta,3)} z={mp.nstr(zz,3)}: samples={n}, min (rho/lambda) Xi/(delta rho^8) = {mp.nstr(worst, 6)}')
