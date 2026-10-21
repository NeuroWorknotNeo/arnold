# [Эксперимент] Строгий выход (A5) для примеров следствия X (записка singular-sigma, §4):
#   X1: U = x^2y^2 + z(x^4+y^4) - z^6 + x^6 + y^6            (m=4, j=6, промежуточный член q_5 >= 0), a0 = 1;
#   X2: U = x^2y^2 + x y z^4 - z^7 + x^8 + y^8              (m=4, j=7, перекрёстный член n_6, 2k > m+j), a0 = 1.
# Сферические срезы rho = |q|, поле теоремы S в гномонической карте: Y = omega - kappa Domega.theta.
# Схема точек стенки и численного Xi — как в exit_model.py.
import sys, random
import sympy as sp
import mpmath as mp
mp.mp.dps = 40
NAME = sys.argv[1] if len(sys.argv) > 1 else 'X1'
X, Yy, Z = sp.symbols('x y z', real=True)
EX = {'X1': (X**2*Yy**2 + Z*(X**4 + Yy**4) - Z**6 + X**6 + Yy**6, 6),
      'X2': (X**2*Yy**2 + X*Yy*Z**4 - Z**7 + X**8 + Yy**8, 7)}
Uexpr, beta = EX[NAME]; a0 = mp.mpf(1)
Uf = sp.lambdify((X, Yy, Z), Uexpr, 'mpmath')
gf = [sp.lambdify((X, Yy, Z), sp.diff(Uexpr, v), 'mpmath') for v in (X, Yy, Z)]
U = lambda q: Uf(*q)
gradU = lambda q: [g(*q) for g in gf]
KAPPA = mp.mpf(0)
def Yfield(q):
    th = [q[0]/q[2], q[1]/q[2]]; t2 = th[0]**2 + th[1]**2; c = 1/mp.sqrt(1 + t2)
    om = [c*th[0], c*th[1], c]
    Dth = [c*th[0] - c**3*t2*th[0], c*th[1] - c**3*t2*th[1], -c**3*t2]
    return [om[i] - KAPPA*Dth[i] for i in range(3)], mp.sqrt(q[0]**2 + q[1]**2 + q[2]**2)
def Vminus(q, v, delta):
    Y, rho = Yfield(q)
    h = sum(t*t for t in Y); p = sum(v[i]*Y[i] for i in range(3))
    return sum(t*t for t in v)/2 - p*p/(2*h) + U(q) + a0*rho**beta - delta*rho**beta
def point(rv, t, al):
    th = [t*mp.cos(al), t*mp.sin(al)]; c = 1/mp.sqrt(1 + th[0]**2 + th[1]**2)
    return [rv*c*th[0], rv*c*th[1], rv*c]
def wall_scan(delta, sigma, npts, seed=1, taus=(0, 1e-3, 1e-2, 0.05, 0.2, 0.5), nang=24):
    random.seed(seed); worst = None
    samples = []
    for _ in range(npts):
        rv = sigma*mp.mpf(random.random())**2 + sigma*mp.mpf('1e-4')
        al = 2*mp.pi*random.random()
        if random.random() < 0.3:
            al = mp.pi/2*random.randint(0, 3) + (0 if random.random() < 0.5 else mp.mpf(random.uniform(-1e-3, 1e-3)))  # половина — точно по оси
        samples.append((rv, al))
    for fr in ('0.9', '0.3', '0.05', '0.002'):        # плюс лучи точно по ветвям (осям)
        for kq in range(4):
            samples.append((sigma*mp.mpf(fr), mp.pi/2*kq))
    for (rv, al) in samples:
        for tau in taus:
            lev = (1 - mp.mpf(tau))*delta
            Wm = lambda t: U(point(rv, t, al)) + (a0 - lev)*rv**beta
            lo, hi = mp.mpf(0), mp.mpf('1e-5')
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
            gq = gradU(q); lam_ = mp.sqrt(-2*U(q) - 2*K)
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
    print('пример', NAME, ': U =', Uexpr, ', beta =', beta)
    for kp in (sys.argv[2].split(',') if len(sys.argv) > 2 else ['0', '0.2']):
        KAPPA = mp.mpf(kp)
        for (delta, sigma) in [(0.02, 0.01), (0.005, 0.0005)]:
            wv = wall_scan(mp.mpf(delta), mp.mpf(sigma), 25)
            print('kappa=%-5s delta=%-6g sigma=%-6g: min (rho/lambda)Xi/(delta rho^beta) = %s  [r=%s, |theta|=%s, alpha=%s, tau=%s]' % (
                kp, delta, sigma, mp.nstr(wv[0], 5), mp.nstr(wv[1], 3), mp.nstr(wv[2], 3), mp.nstr(wv[3], 3), wv[4]))
