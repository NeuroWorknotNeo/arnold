# [Эксперимент] Строгий выход (A5) теоремы A [results/007] для модели особой точки Sigma
#   U = x^2 y^2 + eps z^2 (x^4+y^4) - z^6 + x^6 + y^6  (+ необязательное возмущение степени 7).
# Xi = d/dt (V - delta rho^beta) вдоль поля (q, v) -> (v, -grad U) считается прямым численным
# дифференцированием (mpmath.diff), без тождества (1.3) [007]. Точки стенки: W = (1 - tau) delta rho^beta,
# K_perp = tau delta rho^beta, E = 0, p < 0; лучи из оси в плоскости угла theta; 24 направления v_perp.
# Печатается min (rho/lambda) Xi / (delta rho^beta) (> 0 означает строгий выход в проверенных точках).
# Режимы:
#   S    — сферические срезы rho = |q|, поле Y = omega - kappa Domega.theta (теорема S), гномоническая карта;
#   C    — картезианские срезы rho = z, Y = e_z (лемма 2 [007]); только eps >= 0;
#   SP   — как S, но U + x z^6 + 2 y^2 z^5 (возмущение степени 7, ломает симметрию; дно не прямое).
#   CP   — как C с тем же возмущением.
import sys, random
import mpmath as mp
mp.mp.dps = 40
MODE = sys.argv[1] if len(sys.argv) > 1 else 'S'
EPS = mp.mpf(sys.argv[2]) if len(sys.argv) > 2 else mp.mpf('0.1')
PERT = MODE in ('SP', 'CP')
beta = 6; a0 = mp.mpf(1)

def U(q):
    X, Yy, Z = q
    val = X**2*Yy**2 + EPS*Z**2*(X**4 + Yy**4) - Z**6 + X**6 + Yy**6
    if PERT: val += X*Z**6 + 2*Yy**2*Z**5
    return val
def gradU(q):
    X, Yy, Z = q
    g = [2*X*Yy**2 + 4*EPS*Z**2*X**3 + 6*X**5,
         2*Yy*X**2 + 4*EPS*Z**2*Yy**3 + 6*Yy**5,
         2*EPS*Z*(X**4 + Yy**4) - 6*Z**5]
    if PERT:
        g[0] += Z**6; g[1] += 4*Yy*Z**5; g[2] += 6*X*Z**5 + 10*Yy**2*Z**4
    return g

KAPPA = mp.mpf(0)
def Yfield(q):
    """Возвращает (Y, rho)."""
    if MODE in ('C', 'CP'):
        return [mp.mpf(0), mp.mpf(0), mp.mpf(1)], q[2]
    th = [q[0]/q[2], q[1]/q[2]]
    t2 = th[0]**2 + th[1]**2
    c = 1/mp.sqrt(1 + t2)
    om = [c*th[0], c*th[1], c]
    # Domega.theta для omega = c (theta, 1): d_i omega = c e_i - c^3 theta_i (theta, 1)
    Dth = [c*th[0] - c**3*t2*th[0], c*th[1] - c**3*t2*th[1], -c**3*t2]
    Y = [om[i] - KAPPA*Dth[i] for i in range(3)]
    return Y, mp.sqrt(q[0]**2 + q[1]**2 + q[2]**2)

def Vminus(q, v, delta):
    Y, rho = Yfield(q)
    h = sum(t*t for t in Y); p = sum(v[i]*Y[i] for i in range(3))
    return sum(t*t for t in v)/2 - p*p/(2*h) + U(q) + a0*rho**beta - delta*rho**beta

def point(rv, t, al):
    """S: q = r omega(theta), theta = t (cos al, sin al); C: q = (z t cos al, z t sin al, z), z = rv."""
    th = [t*mp.cos(al), t*mp.sin(al)]
    if MODE in ('C', 'CP'):
        return [rv*th[0], rv*th[1], rv]
    c = 1/mp.sqrt(1 + th[0]**2 + th[1]**2)
    return [rv*c*th[0], rv*c*th[1], rv*c]

def wall_scan(delta, sigma, npts, seed=1, taus=(0, 1e-3, 1e-2, 0.05, 0.2, 0.5), nang=24):
    random.seed(seed); worst = None
    samples = []
    for _ in range(npts):
        rv = sigma*mp.mpf(random.random())**2 + sigma*mp.mpf('1e-4')
        al = 2*mp.pi*random.random()
        if random.random() < 0.3:        # треть лучей — вдоль ветвей (оси), где крест широк
            al = mp.pi/2*random.randint(0, 3) + (0 if random.random() < 0.5 else mp.mpf(random.uniform(-1e-3, 1e-3)))  # половина — точно по оси
        samples.append((rv, al))
    for fr in ('0.9', '0.3', '0.05', '0.002'):        # плюс лучи точно по ветвям (осям)
        for kq in range(4):
            samples.append((sigma*mp.mpf(fr), mp.pi/2*kq))
    for (rv, al) in samples:
        for tau in taus:
            lev = (1 - mp.mpf(tau))*delta
            Wm = lambda t: U(point(rv, t, al)) + a0*Yfield(point(rv, t, al))[1]**beta - lev*Yfield(point(rv, t, al))[1]**beta
            lo, hi = mp.mpf(0), mp.mpf('1e-4')
            if Wm(lo) >= 0: continue
            while Wm(hi) < 0 and hi < 0.4: hi *= 2
            if Wm(hi) < 0: continue
            for _ in range(80):
                mid = (lo + hi)/2
                if Wm(mid) < 0: lo = mid
                else: hi = mid
            q = point(rv, lo, al)
            Y, rho = Yfield(q)
            W = U(q) + a0*rho**beta
            K = max(delta*rho**beta - W, mp.mpf(0))
            h = sum(t*t for t in Y); Yn = mp.sqrt(h)
            e = [mp.mpf(1), 0, 0] if abs(Y[0]) < mp.mpf('0.9')*Yn else [0, mp.mpf(1), 0]
            u1 = [e[i] - sum(e[j]*Y[j] for j in range(3))/h*Y[i] for i in range(3)]
            nu = mp.sqrt(sum(t*t for t in u1)); u1 = [t/nu for t in u1]
            u2 = [Y[1]*u1[2] - Y[2]*u1[1], Y[2]*u1[0] - Y[0]*u1[2], Y[0]*u1[1] - Y[1]*u1[0]]
            nu = mp.sqrt(sum(t*t for t in u2)); u2 = [t/nu for t in u2]
            gq = gradU(q)
            lam_ = mp.sqrt(-2*U(q) - 2*K)
            for kk in range(nang if K > 0 else 1):
                be = 2*mp.pi*kk/nang
                vp = [mp.sqrt(2*K)*(mp.cos(be)*u1[i] + mp.sin(be)*u2[i]) for i in range(3)]
                v = [-lam_*Y[i]/Yn + vp[i] for i in range(3)]
                Fh = lambda tt: Vminus([q[i] + tt*v[i] for i in range(3)], [v[i] - tt*gq[i] for i in range(3)], delta)
                val = rho/(lam_/Yn)*mp.diff(Fh, 0)/(delta*rho**beta)
                if worst is None or val < worst[0]:
                    worst = (val, rv, lo, al, tau, be)
    return worst

if __name__ == '__main__':
    print('режим', MODE, ', eps =', EPS, ', возмущение' if PERT else '')
    kappas = ['0'] if MODE in ('C', 'CP') else (sys.argv[3].split(',') if len(sys.argv) > 3 else ['0', '0.05', '0.2', '0.5'])
    for kp in kappas:
        KAPPA = mp.mpf(kp)
        for (delta, sigma) in [(0.02, 0.05), (0.005, 0.005)]:
            wv = wall_scan(mp.mpf(delta), mp.mpf(sigma), 25)
            print('kappa=%-5s delta=%-6g sigma=%-6g: min (rho/lambda)Xi/(delta rho^beta) = %s  [r=%s, |theta|=%s, alpha=%s, tau=%s]' % (
                kp, delta, sigma, mp.nstr(wv[0], 5), mp.nstr(wv[1], 3), mp.nstr(wv[2], 3), mp.nstr(wv[3], 3), wv[4]))
