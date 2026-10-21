# [Эксперимент] Строгий выход (A5) для примера U_II (записка singular-sigma, §5):
#   U = x^2 y^2 + 2 x y z^3 + eta z^6 + x^6 + y^6,  eta = 1/2,  rho = z,  beta = 6,  A = (1-eta) z^6,
#   W = (xy + z^3)^2 + x^6 + y^6.  Квадрант x > 0, y < 0.
# Режимы поля:
#   F  — свободное поле записки: Y = (xi1, xi2, 1),
#        z xi = (3-e) g (1,-1) - e z^3 (y, x)/(x^2+y^2),  g = x|y|/(x+|y|),  e = eps_h (аргумент 2);
#   E  — Y = e_z (картезианское поле без поправки): ожидается отсутствие строгого выхода;
#   FP — поле F для возмущённого U + 0.3 x z^6 + 0.5 x^2 y z^4 (степень 7).
# Xi = d/dt (V - delta rho^6) вдоль (v, -grad U) — численное дифференцирование. Точки стенки:
# от точки гиперболы x y = -z^3 (параметр s: x = z^1.5 e^(s/2)) по направлению угла phi до уровня
# W = (1-tau) delta z^6; K_perp = tau delta z^6; 24 направления v_perp. Печатается min (rho/lambda) Xi/(delta rho^6).
import sys, random
import mpmath as mp
mp.mp.dps = 50
MODE = sys.argv[1] if len(sys.argv) > 1 else 'F'
EH = mp.mpf(sys.argv[2]) if len(sys.argv) > 2 else mp.mpf('0.1')
ETA = mp.mpf('0.5'); a0 = 1 - ETA; beta = 6
PERT = MODE == 'FP'

def U(q):
    X, Yy, Z = q
    val = X**2*Yy**2 + 2*X*Yy*Z**3 + ETA*Z**6 + X**6 + Yy**6
    if PERT: val += mp.mpf('0.3')*X*Z**6 + mp.mpf('0.5')*X**2*Yy*Z**4
    return val
def gradU(q):
    X, Yy, Z = q
    g = [2*X*Yy**2 + 2*Yy*Z**3 + 6*X**5, 2*X**2*Yy + 2*X*Z**3 + 6*Yy**5, 6*X*Yy*Z**2 + 6*ETA*Z**5]
    if PERT:
        g[0] += mp.mpf('0.3')*Z**6 + X*Yy*Z**4
        g[1] += mp.mpf('0.5')*X**2*Z**4
        g[2] += mp.mpf('1.8')*X*Z**5 + 2*X**2*Yy*Z**3
    return g
def Yfield(q):
    X, Yy, Z = q
    if MODE == 'E':
        return [mp.mpf(0), mp.mpf(0), mp.mpf(1)], Z
    ay = -Yy
    gg = X*ay/(X + ay)
    r2 = X**2 + Yy**2
    xi1 = ((3 - EH)*gg - EH*Z**3*Yy/r2)/Z
    xi2 = (-(3 - EH)*gg - EH*Z**3*X/r2)/Z
    return [xi1, xi2, mp.mpf(1)], Z
def Vminus(q, v, delta):
    Y, rho = Yfield(q)
    h = sum(t*t for t in Y); p = sum(v[i]*Y[i] for i in range(3))
    return sum(t*t for t in v)/2 - p*p/(2*h) + U(q) + a0*rho**beta - delta*rho**beta

def wall_scan(delta, sigma, npts, seed=2, taus=(0, 1e-3, 1e-2, 0.05, 0.2, 0.5), nang=24):
    random.seed(seed); worst = None; cnt = 0
    for _ in range(npts):
        zv = sigma*mp.mpf(random.random())**2 + sigma*mp.mpf('1e-3')
        smax = mp.log(delta/zv**3)/3
        sv = mp.mpf(random.uniform(-1.15, 1.15))*smax
        P0 = [zv**mp.mpf(1.5)*mp.exp(sv/2), -zv**mp.mpf(1.5)*mp.exp(-sv/2)]
        ph = 2*mp.pi*random.random()
        d = [mp.cos(ph), mp.sin(ph)]
        for tau in taus:
            lev = (1 - mp.mpf(tau))*delta
            Wm = lambda t: U([P0[0] + t*d[0], P0[1] + t*d[1], zv]) + (a0 - lev)*zv**beta
            lo = mp.mpf(0)
            if Wm(lo) >= 0: continue
            hi = zv**4*mp.mpf('1e-6')
            while Wm(hi) < 0 and hi < zv: hi *= 2
            if Wm(hi) < 0: continue
            for _ in range(100):
                mid = (lo + hi)/2
                if Wm(mid) < 0: lo = mid
                else: hi = mid
            q = [P0[0] + lo*d[0], P0[1] + lo*d[1], zv]
            if not (q[0] > 0 and q[1] < 0): continue
            cnt += 1
            Y, rho = Yfield(q)
            W = U(q) + a0*rho**beta
            K = max(delta*rho**beta - W, mp.mpf(0))
            h = sum(t*t for t in Y); Yn = mp.sqrt(h)
            e1 = [mp.mpf(1), 0, 0]
            u1 = [e1[i] - sum(e1[j]*Y[j] for j in range(3))/h*Y[i] for i in range(3)]
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
                    worst = (val, zv, sv/smax, ph, tau, be)
    return worst, cnt

if __name__ == '__main__':
    print('режим', MODE, ', eps_h =', EH, ', eta =', ETA)
    PAIRS = [(0.05, 0.02), (0.02, 0.002), (0.01, 0.0002)]
    if len(sys.argv) > 3:
        PAIRS = [tuple(float(u) for u in pr.split(':')) for pr in sys.argv[3].split(',')]
    for (delta, sigma) in PAIRS:
        wv, cnt = wall_scan(mp.mpf(delta), mp.mpf(sigma), 30)
        print('delta=%-5g sigma=%-7g (%d точек стенки): min (rho/lambda)Xi/(delta rho^6) = %s  [z=%s, s/smax=%s, phi=%s, tau=%s]' % (
            delta, sigma, cnt, mp.nstr(wv[0], 5), mp.nstr(wv[1], 3), mp.nstr(wv[2], 3), mp.nstr(wv[3], 3), wv[4]))
