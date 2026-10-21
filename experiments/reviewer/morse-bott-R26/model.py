"""R26: concrete model for Theorem Mb (notes/prover/2026-10-21-morse-bott.md, sec. 6.2).

U = Q0^2 + u5,  Q0 = x^2 + y^2 - z^2  (m = 4),
  p = 2:  u5 = z^3 (z - x)^2 - b z^5
  p = 3:  u5 = z^2 (z - x)^3 - b z^5
Component Sigma_+ = {z = 1/sqrt2, x^2 + y^2 = 1/2}; omega(phi) = (cos phi, sin phi, 1)/sqrt2,
natural parameter theta = phi/sqrt2, T = (-sin phi, cos phi, 0), n = omega x T = (-cos phi, -sin phi, 1)/sqrt2,
geodesic curvature k = 1.  Q0(omega + y n) = -2y, so u4(omega + y n) = 4 y^2, h_n = 8.
j = 5 (g5 = u5|Sigma), c = 3/2, G(theta) = 2^{-5/2}((1 - cos(sqrt2 theta))^p - b),
a0 = b 2^{-5/2}, Lambda = a theta^{2p}(1 + O(theta^2)), a = 2^{-5/2}.

Everything here is computed in Cartesian coordinates with mpmath; the chart is inverted explicitly
(phi = atan2(q_y, q_x), s = <q, omega>, eta = <q, n>), and eta^* is found by Newton's method.
The field Y is built from Cartesian derivatives of omega(phi), n(phi), not from the Darboux formulas.
"""
import sympy as sp
import mpmath as mp

X, Yc, Z = sp.symbols('x y z', real=True)
S, PH, YY = sp.symbols('s phi yv', real=True)


def build(p, b=1):
    Q0 = X**2 + Yc**2 - Z**2
    if p == 2:
        u5 = Z**3 * (Z - X)**2 - b * Z**5
    elif p == 3:
        u5 = Z**2 * (Z - X)**3 - b * Z**5
    elif p == 1:
        # G = 2^{-5/2}((1 - cos phi) - b): order-2 minimum
        u5 = Z**4 * (Z - X) - b * Z**5
    else:
        raise ValueError
    U = sp.expand(Q0**2 + u5)
    gradU = [sp.diff(U, v) for v in (X, Yc, Z)]
    om = sp.Matrix([sp.cos(PH), sp.sin(PH), 1]) / sp.sqrt(2)
    nn = sp.Matrix([-sp.cos(PH), -sp.sin(PH), 1]) / sp.sqrt(2)
    pt = om + YY * nn
    u5r = u5.subs({X: pt[0], Yc: pt[1], Z: pt[2]}, simultaneous=True)
    Q0r = sp.simplify(Q0.subs({X: pt[0], Yc: pt[1], Z: pt[2]}, simultaneous=True))
    assert sp.simplify(Q0r + 2 * YY) == 0
    phi_fun = 4 * YY**2 + S * u5r            # = U(s(omega + y n))/s^4
    fy = sp.diff(phi_fun, YY)
    fyy = sp.diff(fy, YY)
    fys = sp.diff(fy, S)
    fyp = sp.diff(fy, PH)
    L = lambda e: sp.lambdify((S, PH, YY), e, modules='mpmath')
    d = dict(U=sp.lambdify((X, Yc, Z), U, modules='mpmath'),
             gradU=sp.lambdify((X, Yc, Z), gradU, modules='mpmath'),
             fy=L(fy), fyy=L(fyy), fys=L(fys), fyp=L(fyp), p=p, b=b)
    d['a0'] = mp.mpf(b) * mp.mpf(2)**mp.mpf(-2.5)
    d['a'] = mp.mpf(2)**mp.mpf(-2.5)
    return d


def frame(phi):
    c, s_ = mp.cos(phi), mp.sin(phi)
    r2 = mp.sqrt(2)
    om = mp.matrix([c / r2, s_ / r2, 1 / r2])
    T = mp.matrix([-s_, c, 0])
    n = mp.matrix([-c / r2, -s_ / r2, 1 / r2])
    # Cartesian derivatives w.r.t. natural parameter theta = phi/sqrt2 (d/dtheta = sqrt2 d/dphi)
    om_t = mp.matrix([-s_, c, 0])
    n_t = mp.matrix([s_, -c, 0])
    return om, T, n, om_t, n_t


def ystar(M, s, phi):
    y = mp.mpf(0)
    for _ in range(200):
        f = M['fy'](s, phi, y)
        dy = f / M['fyy'](s, phi, y)
        y -= dy
        if abs(dy) < mp.mpf(10)**(-mp.mp.dps + 5) * (abs(y) + mp.mpf(10)**(-mp.mp.dps)):
            break
    return y


def eta_star_data(M, s, phi):
    y = ystar(M, s, phi)
    fyy = M['fyy'](s, phi, y)
    ys = -M['fys'](s, phi, y) / fyy
    yphi = -M['fyp'](s, phi, y) / fyy
    es = y + s * ys                 # eta*_s
    et = s * mp.sqrt(2) * yphi      # eta*_theta
    return s * y, es, et


def chart_inv(q):
    phi = mp.atan2(q[1], q[0])
    om, T, n, _, _ = frame(phi)
    s = sum(q[i] * om[i] for i in range(3))
    eta = sum(q[i] * n[i] for i in range(3))
    return s, phi, eta


def Psi(M, s, theta, zeta):
    phi = theta * mp.sqrt(2)
    om, T, n, _, _ = frame(phi)
    es, _, _ = eta_star_data(M, s, phi)
    eta = es + zeta
    return s * om + eta * n


def Yfield(M, q, kappa):
    s, phi, eta = chart_inv(q)
    theta = phi / mp.sqrt(2)
    om, T, n, om_t, n_t = frame(phi)
    _, es, et = eta_star_data(M, s, phi)
    Ps = om + es * n
    Pt = s * om_t + et * n + eta * n_t
    return Ps - (kappa * theta / s) * Pt, s


def dot(u, v):
    return sum(u[i] * v[i] for i in range(3))


def Vfun(M, q, v, kappa, delta, j=5):
    Y, s = Yfield(M, q, kappa)
    h = dot(Y, Y)
    pp = dot(v, Y)
    U = M['U'](q[0], q[1], q[2])
    W = U + M['a0'] * s**j
    return dot(v, v) / 2 - pp**2 / (2 * h) + W - delta * s**j


def Xi(M, q, v, kappa, delta, hrel=mp.mpf('1e-12')):
    """d/dt (V - delta rho^beta) along the flow at t=0 (central differences + Richardson)."""
    g = M['gradU'](q[0], q[1], q[2])
    g = mp.matrix(g)
    tscale = chart_inv(q)[0] / mp.sqrt(dot(v, v))
    h = hrel * tscale
    f = lambda t: Vfun(M, q + t * v, v - t * g, kappa, delta)
    d1 = (f(h) - f(-h)) / (2 * h)
    d2 = (f(h / 2) - f(-h / 2)) / h
    return (4 * d2 - d1) / 3
