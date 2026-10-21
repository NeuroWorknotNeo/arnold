# R38: direct numerical check of (A5) and (A4) for U_II (+ optional degree-7 perturbation) with the field (5.1),
# rho = z, beta = 6, A = a0 z^6. Xi computed as d/dt of (V - delta rho^6) along the vector field (v, -grad U)
# by mpmath.diff (not via identity (1.3)). Sampling: q random in closure(D), K_perp = delta z^6 - W, v_perp direction random.
import sys, mpmath as mp, random
mp.mp.dps = 120
eta = mp.mpf(1)/2; a0 = 1 - eta
mode = sys.argv[1] if len(sys.argv) > 1 else 'F'      # F: field (5.1); E: Y = e_z; P: field (5.1) + perturbation
e = mp.mpf(sys.argv[2]) if len(sys.argv) > 2 else mp.mpf('0.1')
def Vpert(x, y, z):
    return (mp.mpf('0.7')*z**7 - mp.mpf('0.4')*x*z**6 + mp.mpf('0.6')*x*y*z**5) if mode == 'P' else 0
def U(q):
    x, y, z = q
    return x**2*y**2 + 2*x*y*z**3 + eta*z**6 + x**6 + y**6 + Vpert(x, y, z)
def gradU(q):
    x, y, z = q
    gx = 2*x*y**2 + 2*y*z**3 + 6*x**5
    gy = 2*x**2*y + 2*x*z**3 + 6*y**5
    gz = 6*x*y*z**2 + 6*eta*z**5
    if mode == 'P':
        gx += -mp.mpf('0.4')*z**6 + mp.mpf('0.6')*y*z**5
        gy += mp.mpf('0.6')*x*z**5
        gz += mp.mpf('4.9')*z**6 - mp.mpf('2.4')*x*z**5 + 3*x*y*z**4
    return [gx, gy, gz]
def Yf(q):
    x, y, z = q
    if mode == 'E': return [mp.mpf(0), mp.mpf(0), mp.mpf(1)]
    t = -y; g = x*t/(x+t)
    r2 = x**2 + y**2
    return [((3-e)*g - e*z**3*y/r2)/z, (-(3-e)*g - e*z**3*x/r2)/z, mp.mpf(1)]
def dot(a, b): return sum(ai*bi for ai, bi in zip(a, b))
def Vfun(q, v, delta):
    Y = Yf(q); h = dot(Y, Y); p = dot(v, Y)
    return dot(v, v)/2 - p**2/(2*h) + U(q) + a0*q[2]**6 - delta*q[2]**6
def sample(delta, sigma, n, seed):
    rnd = random.Random(seed)
    worst = None; worstA4 = None; cnt = 0
    while cnt < n:
        z = sigma*mp.mpf(10)**(-rnd.uniform(0, 1))
        # x log-uniform between ~z^{3/2}/50 and (2 delta)^{1/6} z; H uniform; boundary points with prob 1/3
        lo = mp.log10(mp.mpf(0.7)*z**2/(2*delta)**(mp.mpf(1)/6)); hi = mp.log10((2*delta)**(mp.mpf(1)/6)*z)
        x = mp.mpf(10)**(lo + (hi-lo)*rnd.random())
        H = (2*rnd.random()-1)*mp.sqrt(delta)*z**3
        y = (H - z**3)/x
        q = [x, y, z]
        Wq = U(q) + a0*z**6
        if not (y < 0 and x < z and -y < z and Wq <= delta*z**6): continue
        tau = rnd.choice([0, 0, 1e-3, 1e-2, 0.05, 0.2, 0.5, 0.9, 1.0])
        # move to a point with W = (1-tau) delta z^6 along H (bisection on H); if impossible keep the point
        if tau > 0:
            Kp = delta*z**6 - Wq
        else:
            # bring q to the boundary W = delta z^6 by scaling H outward
            sgn = 1 if H >= 0 else -1
            f = lambda Hs: U([x, (Hs - z**3)/x, z]) + a0*z**6 - delta*z**6
            Hb = sgn*mp.sqrt(2*delta)*z**3
            if f(Hb) < 0: continue
            try:
                Hs = mp.findroot(f, (H, Hb), solver='anderson')
            except Exception:
                continue
            y = (Hs - z**3)/x; q = [x, y, z]
            if not (y < 0 and -y < z): continue
            Wq = U(q) + a0*z**6; Kp = mp.mpf(0)
        if Kp < 0: Kp = mp.mpf(0)
        Y = Yf(q); h = dot(Y, Y)
        # orthonormal basis of Y-perp
        n1 = [Y[1], -Y[0], mp.mpf(0)] if (abs(Y[0]) + abs(Y[1])) > 0 else [mp.mpf(1), 0, 0]
        nn = mp.sqrt(dot(n1, n1)); n1 = [c/nn for c in n1]
        n2 = [Y[1]*n1[2]-Y[2]*n1[1], Y[2]*n1[0]-Y[0]*n1[2], Y[0]*n1[1]-Y[1]*n1[0]]
        nn = mp.sqrt(dot(n2, n2)); n2 = [c/nn for c in n2]
        phi = 2*mp.pi*rnd.random()
        vp = [mp.sqrt(2*Kp)*(mp.cos(phi)*n1[i] + mp.sin(phi)*n2[i]) for i in range(3)]
        lam = mp.sqrt(2*(a0 - delta)*z**6/h)   # E=0, V=delta z^6
        v = [-lam*Y[i] + vp[i] for i in range(3)]
        E = dot(v, v)/2 + U(q)
        assert abs(E) < mp.mpf(10)**(-40)*z**6 + mp.mpf(10)**(-50), E
        g = gradU(q)
        F = lambda s: Vfun([q[i] + s*v[i] for i in range(3)], [v[i] - s*g[i] for i in range(3)], delta)
        Xi = mp.diff(F, 0)
        val = z/lam*Xi/(delta*z**6)
        a4 = v[2]/z**3   # rho-dot / rho^{beta/2}
        if worst is None or val < worst[0]:
            worst = (val, mp.nstr(x/z**mp.mpf(1.5), 5), mp.nstr(y/z**mp.mpf(1.5), 5), mp.nstr(z, 3), tau)
        if worstA4 is None or a4 > worstA4: worstA4 = a4
        cnt += 1
    return worst, worstA4
if __name__ == '__main__':
    print(f"mode={mode} e={e} eta={eta}")
    for delta, sigma in [(0.05, 0.02), (0.02, 2e-3), (0.01, 2e-4), (0.01, 2e-5), (0.01, 2e-6), (0.005, 2e-7), (0.01, 1e-9)]:
        w, a4 = sample(mp.mpf(delta), mp.mpf(sigma), 300, 7)
        print(f"delta={delta} sigma={sigma}: min rho Xi/(lambda delta rho^6) = {mp.nstr(w[0], 6)} at x/z^1.5={w[1]}, y/z^1.5={w[2]}, z={w[3]}, tau={w[4]};  max zdot/z^3 = {mp.nstr(a4, 5)}")
        sys.stdout.flush()
