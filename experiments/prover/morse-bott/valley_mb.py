# [Эксперимент] Каскадные примеры D1, D2s, D2 (записка notes/prover/2026-10-21-morse-bott.md, §5, §9):
# функция дна F_fl(s,phi) = min_eta U(s omega(phi) + eta n(phi)) — точный минимум по нормальному
# слою (Ньютон по eta, mpmath), f = F_fl/s^6 = Ghat(s,theta). Около нуля phi = pi функции G = g_6
# на Sigma_+ ищется дно углового оврага theta_v(s) (глобальный минимум f(s,.) на |phi-pi|<0.5),
# глубина d(s) = f(s,theta_v) ~ -a s^gamma, сдвиг tau_v(s) = theta_v - theta_1 и профиль
# P(s,b) = (f(s, theta_v + s^alpha b) - f(s,theta_v)) / s^gamma, который по лемме V должен стремиться
# к Q(b). Прогноз (Ньютон-многоугольник, §9 записки): gamma = 1, a = sqrt2/16;
#   D1:  alpha = 1/2, Q = b^2/4,  tau_v ~ -s/4;
#   D2s: alpha = 1/4, Q = 2 b^4,  tau_v = 0 (симметрия y -> -y);
#   D2:  alpha = 1/4, Q = 2 b^4,  tau_v ~ -(s/64)^(1/3).
# theta — натуральный параметр (theta = phi/sqrt2).
import sys
import sympy as sp
import mpmath as mp
from examples_mb import EXAMPLES, x, y, z

mp.mp.dps = 40
S2 = mp.sqrt(2)
name = sys.argv[1] if len(sys.argv) > 1 else 'D1'
U, m = EXAMPLES[name]
Uf = sp.lambdify((x, y, z), U, 'mpmath')
dU = [sp.lambdify((x, y, z), sp.diff(U, v), 'mpmath') for v in (x, y, z)]
d2U = [[sp.lambdify((x, y, z), sp.diff(U, a, b), 'mpmath') for b in (x, y, z)] for a in (x, y, z)]
alpha = {'D1': mp.mpf(1)/2, 'D2s': mp.mpf(1)/4, 'D2': mp.mpf(1)/4}[name]
Qpred = {'D1': lambda b: b**2/4, 'D2s': lambda b: 2*b**4, 'D2': lambda b: 2*b**4}[name]
a_pred = S2/16

def frame(phv):
    return ([mp.cos(phv)/S2, mp.sin(phv)/S2, 1/S2], [-mp.cos(phv)/S2, -mp.sin(phv)/S2, 1/S2])

def Ffl(sv, phv):
    w, n = frame(phv)
    eta = mp.mpf(0)
    for _ in range(60):
        q = [sv*w[i] + eta*n[i] for i in range(3)]
        g = sum(dU[i](*q)*n[i] for i in range(3))
        H = sum(d2U[i][k](*q)*n[i]*n[k] for i in range(3) for k in range(3))
        step = g/H
        eta -= step
        if abs(step) < mp.mpf(10)**(-35)*sv:
            break
    q = [sv*w[i] + eta*n[i] for i in range(3)]
    return Uf(*q)

def f(sv, th):                       # th — натуральный параметр, th1 = pi/sqrt2
    return Ffl(sv, S2*th)/sv**6

th1 = mp.pi/S2
def valley(sv):
    lo, hi = th1 - mp.mpf('0.35'), th1 + mp.mpf('0.35')
    # грубая сетка, затем золотое сечение
    pts = [lo + (hi - lo)*i/400 for i in range(401)]
    vals = [f(sv, t) for t in pts]
    i0 = min(range(401), key=lambda i: vals[i])
    a, b = pts[max(i0 - 1, 0)], pts[min(i0 + 1, 400)]
    gr = (mp.sqrt(5) - 1)/2
    c, d = b - gr*(b - a), a + gr*(b - a)
    fc, fd = f(sv, c), f(sv, d)
    for _ in range(140):
        if fc < fd:
            b, d, fd = d, c, fc; c = b - gr*(b - a); fc = f(sv, c)
        else:
            a, c, fc = c, d, fd; d = a + gr*(b - a); fd = f(sv, d)
    t = (a + b)/2
    return t, f(sv, t)

print('пример', name, ': U =', U)
print('%-8s %-14s %-14s %-12s %s' % ('s', 'tau_v(s)', 'd(s)/(-a s)', 'прогноз tau', 'P(s,b)/Q(b) при b = 0.5, 1, 2'))
prev = None
for e in range(2, 9):
    sv = mp.mpf(10)**(-e)
    tv, dv = valley(sv)
    tau = tv - th1
    pred = {'D1': -sv/4, 'D2s': mp.mpf(0), 'D2': -mp.cbrt(sv/64)}[name]
    ratios = []
    for b in (mp.mpf('0.5'), mp.mpf(1), mp.mpf(2)):
        P = (f(sv, tv + sv**alpha*b) - dv)/sv
        ratios.append(P/Qpred(b))
    print('%-8s %-14s %-14s %-12s %s' % (mp.nstr(sv, 2), mp.nstr(tau, 6), mp.nstr(dv/(-a_pred*sv), 8),
          mp.nstr(pred, 6), '  '.join(mp.nstr(r, 6) for r in ratios)))
    if prev is not None:
        print('         наклон log|d| по log s: %s' % mp.nstr((mp.log(abs(dv)) - mp.log(abs(prev)))/mp.log(10)/(-1), 6))
    prev = dv
