# [Эксперимент] Строгий выход (A5) теоремы A [results/007] для областей теорем C, B, D записки
# notes/prover/2026-10-21-morse-bott.md. Xi = d/dt (V - delta rho^beta) вдоль поля (q,v) -> (v,-grad U)
# считается прямым численным дифференцированием (без тождества (1.3)). Точки стенки:
# W = U + a0 rho^beta = (1-tau) delta rho^beta на лучах из b = 0 в b-координатах карты, K_perp = tau delta rho^beta,
# все направления v_perp (24 угла в плоскости, ортогональной Y), E = 0, p < 0.
# Печатается min (rho/lambda) Xi / (delta rho^beta); положительность = строгий выход на проверенных точках.
#   C:  пример C2 = (Q0+z^3)^2 - z^7 + x y z^6, Sigma_+, j=7, G = -sqrt2/16 = const, Y = Psi_s, theta периодична;
#   B:  пример B  = Q0^2 - z^6 + 4y^4z^2 + x y z^5, Sigma_+, phi0 = 0, G = -1/8 + sin^4(phi)/2 (p = 2),
#       Y = Psi_s - (kappa theta/s) Psi_theta;
#   D:  пример D2s = Q0^2 + 4y^4z^2 + x z^6, Sigma_+, phi1 = pi, beta = 7, alpha = 1/4, c' = 5/2,
#       Y = Psi_s - ((theta-theta1)/s) Psi_theta (карта оврага, tau_v = 0);
#   D3: пример D3 = (Q0+z^3)^2 + y^2 z^6 + x z^8 (искривлённое дно, j = 8), beta = 9, alpha = 1/2, c' = 7/2, tau_c = 0;
#   D1: пример D1 = Q0^2 + y^2 z^4 + x z^6 + x y z^5, beta = 7, alpha = 1/2, tau_c(s) = -s/4 (приближение дна).
import sys, random, os
import sympy as sp
import mpmath as mp
from examples_mb import EXAMPLES, gk, omP, x, y, z, s as S_
mp.mp.dps = int(os.environ.get('DPS', '30'))   # для D3 при s ~ 1e-6 нужна DPS=60 (значения ~ 1e-58)
S2 = mp.sqrt(2)
MODE = sys.argv[1] if len(sys.argv) > 1 else 'C'
EXN = {'C': 'C2', 'B': 'B', 'D': 'D2s', 'D1': 'D1', 'D3': 'D3'}[MODE]
U, m = EXAMPLES[EXN]
ys, g = gk(U, m, omP, 4)
eta_expr = sp.expand(S_*ys[0])
ph = sp.Symbol('phi', real=True)
eta_f = sp.lambdify((S_, ph), eta_expr, 'mpmath')
eta_s = sp.lambdify((S_, ph), sp.diff(eta_expr, S_), 'mpmath')
eta_p = sp.lambdify((S_, ph), sp.diff(eta_expr, ph), 'mpmath')
Uf = sp.lambdify((x, y, z), U, 'mpmath')
gU = [sp.lambdify((x, y, z), sp.diff(U, v), 'mpmath') for v in (x, y, z)]
if MODE == 'C':
    beta = 7; a0 = S2/16; cw = mp.mpf(5)/2; phi_ref = mp.mpf(0)
elif MODE == 'B':
    beta = 6; a0 = mp.mpf(1)/8; cw = mp.mpf(2); phi_ref = mp.mpf(0)
elif MODE == 'D3':
    beta = 9; a0 = S2/32; cw = mp.mpf(7)/2; phi_ref = mp.pi; alpha = mp.mpf(1)/2
else:
    beta = 7; a0 = S2/16; cw = mp.mpf(5)/2; phi_ref = mp.pi
    alpha = mp.mpf(1)/4 if MODE == 'D' else mp.mpf(1)/2
def tau_c(sv):  return -sv/4 if MODE == 'D1' else mp.mpf(0)
def tau_c1(sv): return -mp.mpf(1)/4 if MODE == 'D1' else mp.mpf(0)

def frame(phv):
    return ([mp.cos(phv)/S2, mp.sin(phv)/S2, 1/S2], [-mp.sin(phv), mp.cos(phv), mp.mpf(0)],
            [-mp.cos(phv)/S2, -mp.sin(phv)/S2, 1/S2])
def chart_inv(q):
    R = mp.sqrt(q[0]**2 + q[1]**2)
    sv = (R + q[2])/S2; eta = (q[2] - R)/S2
    phv = mp.atan2(q[1], q[0])
    while phv - phi_ref > mp.pi: phv -= 2*mp.pi
    while phv - phi_ref < -mp.pi: phv += 2*mp.pi
    return sv, phv, eta
def Psi(sv, phv, zeta):
    w, T, n = frame(phv); eta = eta_f(sv, phv) + zeta
    return [sv*w[i] + eta*n[i] for i in range(3)]

KAPPA = mp.mpf(0)
def Yfield(q):
    sv, phv, eta = chart_inv(q)
    w, T, n = frame(phv)
    eps = eta/sv                                   # k = 1
    Ps = [w[i] + eta_s(sv, phv)*n[i] for i in range(3)]
    Pt = [sv*(1 - eps)*T[i] + S2*eta_p(sv, phv)*n[i] for i in range(3)]   # d/dtheta = sqrt2 d/dphi
    th = (phv - phi_ref)/S2
    if MODE == 'C':
        cf = 0
    elif MODE == 'B':
        cf = -KAPPA*th/sv
    else:
        cf = tau_c1(sv) - (th - tau_c(sv))/sv
    return [Ps[i] + cf*Pt[i] for i in range(3)], sv

def Vminus(q, v, delta):
    Y, rho = Yfield(q)
    h = sum(t*t for t in Y); p = sum(v[i]*Y[i] for i in range(3))
    return sum(t*t for t in v)/2 - p*p/(2*h) + Uf(*q) + a0*rho**beta - delta*rho**beta

def point(sv, b1, e):
    if MODE == 'C':   phv = b1                                  # b1 = phi (периодическая)
    elif MODE == 'B': phv = phi_ref + S2*b1                     # b1 = theta
    else:             phv = phi_ref + S2*(tau_c(sv) + sv**alpha*b1)
    return Psi(sv, phv, sv**cw*e)

def wall_scan(delta, sigma, npts, seed=1, taus=(0, 1e-3, 1e-2, 0.05, 0.2, 0.5), nang=24):
    random.seed(seed); worst = None
    for _ in range(npts):
        sv = sigma*mp.mpf(random.random())**2 + sigma*mp.mpf('1e-4')
        if MODE == 'C':
            phv = 2*mp.pi*random.random(); sg = 1 if random.random() < 0.5 else -1
            ray = lambda t: (phv, sg*t)
        else:
            al = 2*mp.pi*random.random()
            sc = (1, mp.mpf('0.3')) if MODE != 'D1' else (1, mp.mpf('0.3'))
            ray = lambda t: (t*mp.cos(al)*sc[0], t*mp.sin(al)*sc[1])
        for tau in taus:
            lev = (1 - mp.mpf(tau))*delta
            Wm = lambda t: Uf(*point(sv, *ray(t))) + a0*sv**beta - lev*sv**beta
            lo, hi = mp.mpf(0), mp.mpf('0.02')
            if Wm(lo) >= 0: continue
            while Wm(hi) < 0 and hi < 50: hi *= 2
            if Wm(hi) < 0: continue
            for _ in range(70):
                mid = (lo + hi)/2
                if Wm(mid) < 0: lo = mid
                else: hi = mid
            q = point(sv, *ray(lo))
            Y, rho = Yfield(q)
            W = Uf(*q) + a0*rho**beta
            K = max(delta*rho**beta - W, mp.mpf(0))
            h = sum(t*t for t in Y); Yn = mp.sqrt(h)
            a = [mp.mpf(1), 0, 0] if abs(Y[0]) < mp.mpf('0.9')*Yn else [0, mp.mpf(1), 0]
            u1 = [a[i] - sum(a[k]*Y[k] for k in range(3))/h*Y[i] for i in range(3)]
            nu = mp.sqrt(sum(t*t for t in u1)); u1 = [t/nu for t in u1]
            u2 = [Y[1]*u1[2] - Y[2]*u1[1], Y[2]*u1[0] - Y[0]*u1[2], Y[0]*u1[1] - Y[1]*u1[0]]
            nu = mp.sqrt(sum(t*t for t in u2)); u2 = [t/nu for t in u2]
            gq = [gg(*q) for gg in gU]
            lam_ = mp.sqrt(-2*Uf(*q) - 2*K)
            for k in range(nang if K > 0 else 1):
                be = 2*mp.pi*k/nang
                vp = [mp.sqrt(2*K)*(mp.cos(be)*u1[i] + mp.sin(be)*u2[i]) for i in range(3)]
                v = [-lam_*Y[i]/Yn + vp[i] for i in range(3)]
                F = lambda t: Vminus([q[i] + t*v[i] for i in range(3)], [v[i] - t*gq[i] for i in range(3)], delta)
                val = rho/(lam_/Yn)*mp.diff(F, 0)/(delta*rho**beta)
                if worst is None or val < worst[0]:
                    worst = (val, sv, ray(lo), tau, be)
    return worst

if __name__ == '__main__':
    print('режим', MODE, ', пример', EXN, ': U =', U, ', beta =', beta, ', a0 =', mp.nstr(a0, 8))
    kappas = [None] if MODE in ('C', 'D', 'D1', 'D3') else sys.argv[2].split(',') if len(sys.argv) > 2 else ['0', '0.003', '0.02', '0.1']
    for kp in kappas:
        if kp is not None: KAPPA = mp.mpf(kp)
        for (delta, sigma) in [(0.02, 0.01), (0.005, 0.001)]:
            wv = wall_scan(mp.mpf(delta), mp.mpf(sigma), 30)
            print('%sdelta=%-6g sigma=%-6g: min (rho/lambda)Xi/(delta rho^beta) = %s  [s=%s, b=(%s, %s), tau=%s]' % (
                ('kappa=%-6s ' % kp) if kp is not None else '', delta, sigma, mp.nstr(wv[0], 5), mp.nstr(wv[1], 3),
                mp.nstr(wv[2][0], 3), mp.nstr(wv[2][1], 3), wv[3]))
