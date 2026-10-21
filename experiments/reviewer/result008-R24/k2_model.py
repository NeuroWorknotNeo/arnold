"""R24: численная проверка карты (10.1) теоремы K2 и строгого выхода на модельном потенциале.

[Эксперимент]. Модель: дуга Sigma_0 — параллель широты alpha на S^2 (k_g = tan(alpha) != 0),
натуральный параметр theta (phi = theta / cos(alpha)); координаты Pi(s,theta,eta) = s*omega + eta*n
обращаются явно: s = r_xy cos(a) + z sin(a), eta = -r_xy sin(a) + z cos(a).
Потенциал (m=4, j=7, c=5/2): U = s^2 * h(theta)/2 * (eta - eta*(s,theta))^2 + s^7 * G(theta),
eta* = s^2 a1(theta) + s^3 a2(theta) (искривлённое дно). Тогда F~ = G + h e^2/2 точно (chi = 0).
G(0)<0, G'(0)=0, G''(0)>0, G''(0)+7G(0)<0 (вне K1).

Проверяется независимо от формул (10.2)-(10.4): все производные берутся в декартовых координатах
(sympy -> mpmath), Y(q) строится как поле d_x Phi o Phi^{-1}.
1. (Phi2'), (Phi3) с gamma1 = 5/4 kappa, gamma2 = kappa(1-kappa), C1 из §10.2: остаток -> 0 при x -> 0.
2. Строгий выход: (rho/lambda) Xi / (delta rho^beta) >= mu/8 = kappa/8 на множестве (A5)
   при kappa из (U3), delta <= delta_* и малом x (как в теореме 2').
"""
import sympy as sp
import mpmath as mp
import random

mp.mp.dps = 90
random.seed(12345)

alpha = sp.Rational(3, 5)
ca, sa = sp.cos(alpha), sp.sin(alpha)
kgv = sp.tan(alpha)              # геодезическая кривизна параллели (знак при n = omega x ell)
m_, j_ = 4, 7
c_ = sp.Rational(j_ - m_ + 2, 2)
G0, G2, G3 = sp.Rational(-1, 10), sp.Rational(3, 10), sp.Rational(1, 5)

th, S, ET = sp.symbols('theta s eta', real=True)
Gf = G0 + G2 / 2 * th ** 2 + G3 * th ** 3
hf = 8 + th
a1 = sp.Rational(7, 10) + sp.Rational(3, 10) * sp.sin(th)
a2 = -sp.Rational(1, 2) * sp.cos(th)
estar = S ** 2 * a1 + S ** 3 * a2

phi = th / ca
om = sp.Matrix([ca * sp.cos(phi), ca * sp.sin(phi), sa])
ell = sp.Matrix([-sp.sin(phi), sp.cos(phi), 0])
nn = sp.Matrix([-sa * sp.cos(phi), -sa * sp.sin(phi), ca])
# sanity: natural parameter and Darboux frame
assert sp.simplify(om.diff(th) - ell) == sp.zeros(3, 1)
assert sp.simplify(ell.diff(th) - (-om + kgv * nn)) == sp.zeros(3, 1)
assert sp.simplify(nn.diff(th) - (-kgv * ell)) == sp.zeros(3, 1)
assert sp.simplify(om.cross(ell) - nn) == sp.zeros(3, 1)

kap = sp.Symbol('kappa', positive=True)
a0 = -G0
lam0 = sp.Rational(1, 4) * sp.Min(G2, hf.subs(th, 0))
kmax = j_ * lam0 / (a0 * (15 * sp.sqrt(3) / 8 * j_ + 2 * sp.sqrt(2)) ** 2)
kbar = abs(kgv)
print('k_g =', sp.N(kgv, 6), ' lambda0 =', lam0, ' a0 =', a0, ' kappa_max(U3) =', sp.N(kmax, 6))

# ---- Cartesian functions of q
q1, q2, q3 = sp.symbols('q1 q2 q3', real=True)
rxy = sp.sqrt(q1 ** 2 + q2 ** 2)
s_q = rxy * ca + q3 * sa
eta_q = -rxy * sa + q3 * ca
th_q = sp.atan2(q2, q1) * ca

sub = {S: s_q, th: th_q}
U_q = (S ** 2 * hf / 2 * (ET - estar) ** 2 + S ** j_ * Gf).subs(ET, eta_q).subs(sub)

# K2 map and Y as a Cartesian field
x, u, z = sp.symbols('x u zeta', positive=True)


def Phi_of(kv):
    thx = u * x ** (-kv)
    return (x * om + (estar + z) * nn).subs(S, x).subs(th, thx)


def Y_field(kv):
    # Y = omega - kappa theta (1-eps) ell + nu n, eps = kg eta/s, nu = eta*_s - kappa theta eta*_theta/s
    eps = kgv * ET / S
    nu = sp.diff(estar, S) - kv * th * sp.diff(estar, th) / S
    Yexpr = om - kv * th * (1 - eps) * ell + nu * nn
    return Yexpr.subs(ET, eta_q).subs(sub)


def build(kv):
    Phi = Phi_of(kv)
    PhiX = Phi.diff(x)
    PhiXX = PhiX.diff(x)
    Yq = Y_field(kv)
    qv = sp.Matrix([q1, q2, q3])
    JY = Yq.jacobian(qv)
    grad_s = sp.Matrix([s_q]).jacobian(qv).T
    gradU = sp.Matrix([U_q]).jacobian(qv).T
    HU = None
    f = dict(
        Phi=sp.lambdify((x, u, z), Phi, 'mpmath'),
        PhiX=sp.lambdify((x, u, z), PhiX, 'mpmath'),
        PhiXX=sp.lambdify((x, u, z), PhiXX, 'mpmath'),
        Y=sp.lambdify((q1, q2, q3), Yq, 'mpmath'),
        JY=sp.lambdify((q1, q2, q3), JY, 'mpmath'),
        grad_s=sp.lambdify((q1, q2, q3), grad_s, 'mpmath'),
        s=sp.lambdify((q1, q2, q3), s_q, 'mpmath'),
        U=sp.lambdify((q1, q2, q3), U_q, 'mpmath'),
        gradU=sp.lambdify((q1, q2, q3), gradU, 'mpmath'),
    )
    return f


def vec(M):
    return mp.matrix([M[i] for i in range(3)])


def dotv(a, b):
    return sum(a[i] * b[i] for i in range(3))


def unit_perp(Yv):
    # random unit vector orthogonal to Yv
    while True:
        w = mp.matrix([mp.mpf(random.gauss(0, 1)) for _ in range(3)])
        w = w - dotv(w, Yv) / dotv(Yv, Yv) * Yv
        nrm = mp.sqrt(dotv(w, w))
        if nrm > 1e-6:
            return w / nrm


import os
RUN12 = os.environ.get('K2_PART3_ONLY') is None
kv = float(sp.N(kmax))
kvm = mp.mpf(sp.N(kmax, 50))
f = build(sp.nsimplify(sp.N(kmax, 30)))
C1 = mp.mpf(5) / 4 * kvm ** 2 * (1 + mp.mpf(sp.N(kbar, 50))) + 4 * kvm * mp.mpf(sp.N(kbar, 50))
gam1 = mp.mpf(5) / 4 * kvm
gam2 = kvm * (1 - kvm)
r0 = mp.mpf(1) / 4

print('\n--- 1. map inequalities (Phi2\'), (Phi3): max residual over random samples, by x ---')
print('  residual1 = |<grad rho - Y/h, w>| - gamma1|b|;  residual2 = x|<Phi_xx,w>| - gamma2|b| - C1|b|^2;')
print('  residual3 = -(x<w,D_wY>) - C1|b|   (all for unit w perp Y; must be <= varpi(x) -> 0)')
for xe in ([mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4'), mp.mpf('1e-5')] if RUN12 else []):
    R1 = R2 = R3 = mp.mpf(-10)
    Rgrad = mp.mpf(0)
    for _ in range(300):
        # b = (theta, e), |b| < r0
        while True:
            bt, be = random.uniform(-0.25, 0.25), random.uniform(-0.25, 0.25)
            if bt * bt + be * be < 0.0625:
                break
        bt, be = mp.mpf(bt), mp.mpf(be)
        uu = bt * xe ** kvm
        zz = be * xe ** c_
        P = vec(f['Phi'](xe, uu, zz))
        PX = vec(f['PhiX'](xe, uu, zz))
        PXX = vec(f['PhiXX'](xe, uu, zz))
        Yv = vec(f['Y'](*P))
        Rgrad = max(Rgrad, mp.sqrt(dotv(Yv - PX, Yv - PX)))     # Y o Phi == d_x Phi ?
        gs = vec(f['grad_s'](*P))
        # grad rho == omega(theta) ?
        h = dotv(Yv, Yv)
        JY = f['JY'](*P)
        bn = mp.sqrt(bt ** 2 + be ** 2)
        for _k in range(3):
            w = unit_perp(Yv)
            r1 = abs(dotv(gs - Yv / h, w)) - gam1 * bn
            r2 = xe * abs(dotv(PXX, w)) - gam2 * bn - C1 * bn ** 2
            DwY = JY * w
            r3 = -(xe * dotv(w, DwY)) - C1 * bn
            R1, R2, R3 = max(R1, r1), max(R2, r2), max(R3, r3)
    print(f'  x={mp.nstr(xe, 2):>6}: |Y o Phi - Phi_x|max={mp.nstr(Rgrad, 3):>9}  res1={mp.nstr(R1, 4):>11}  '
          f'res2={mp.nstr(R2, 4):>11}  res3={mp.nstr(R3, 4):>11}')

print('\n--- 2. strict exit on the (A5) set: min (rho/lambda) Xi / (delta rho^beta) vs mu/8 = kappa/8 ---')
beta = j_
mu = kvm
a0m = mp.mpf(sp.N(a0, 50))
lam0m = mp.mpf(sp.N(lam0, 50))


def Xi_hat(xe, bt, be, delta, dirangle):
    uu = bt * xe ** kvm
    zz = be * xe ** c_
    P = vec(f['Phi'](xe, uu, zz))
    Yv = vec(f['Y'](*P))
    h = dotv(Yv, Yv)
    rho = f['s'](*P)
    Uv = f['U'](*P)
    A = a0m * rho ** beta
    W = Uv + A
    Kp = delta * rho ** beta - W
    if Kp < 0:
        return None
    lam = mp.sqrt(2 * (A - delta * rho ** beta) / h)
    # orthonormal basis of Y^perp
    e1 = unit_perp(Yv)
    cr = mp.matrix([Yv[1] * e1[2] - Yv[2] * e1[1], Yv[2] * e1[0] - Yv[0] * e1[2], Yv[0] * e1[1] - Yv[1] * e1[0]])
    e2 = cr / mp.sqrt(dotv(cr, cr))
    vp = mp.sqrt(2 * Kp) * (mp.cos(dirangle) * e1 + mp.sin(dirangle) * e2)
    v = -lam * Yv + vp
    # check E = 0 and V = delta rho^beta
    E = dotv(v, v) / 2 + Uv
    p = dotv(v, Yv)
    V = dotv(v, v) / 2 - p ** 2 / (2 * h) + W
    assert abs(E) < mp.mpf(10) ** (-40) * max(1, abs(A)) * 1e10 or abs(E / A) < 1e-30
    # Xi = grad_q f . v - grad_v f . gradU, f = |v|^2/2 - p^2/(2h) + U + (a0 - delta) rho^beta
    JY = f['JY'](*P)
    gU = vec(f['gradU'](*P))
    gs = vec(f['grad_s'](*P))
    # grad_q of -p^2/(2h): p = <v,Y>, dp = JY^T v, dh = 2 JY^T Y
    JYT = JY.T
    dp = JYT * v
    dh = 2 * (JYT * Yv)
    gq = -(p / h) * dp + (p ** 2 / (2 * h ** 2)) * dh + gU + (a0m - delta) * beta * rho ** (beta - 1) * gs
    gv = v - (p / h) * Yv
    Xi = dotv(gq, v) - dotv(gv, gU)
    return (rho / lam) * Xi / (delta * rho ** beta), V / (delta * rho ** beta)


def sample_min(xe, delta, N=400):
    worst = mp.mpf(10)
    for _ in range(N):
        # b with Q(b) <= delta: Q = G(theta)-G(0) + h(theta) e^2/2 ; sample in ellipse then filter
        rad = mp.sqrt(delta / lam0m)
        bt = mp.mpf(random.uniform(-1, 1)) * rad
        be = mp.mpf(random.uniform(-1, 1)) * rad
        # push some samples to the boundary Q = delta (worst case K_perp = 0) and some inside
        res = Xi_hat(xe, bt, be, delta, random.uniform(0, 6.283))
        if res is None:
            continue
        val, Vn = res
        worst = min(worst, val)
    return worst


for delta in ([mp.mpf("1e-2"), mp.mpf("1e-4"), mp.mpf("2e-7")] if RUN12 else []):
    for xe in [mp.mpf("1e-3"), mp.mpf("1e-6"), mp.mpf("1e-9"), mp.mpf("1e-12")]:
        w = sample_min(xe, delta)
        print(f'  delta={mp.nstr(delta, 2):>6} x={mp.nstr(xe, 2):>6}: min Xi_hat = {mp.nstr(w, 6):>10}   '
              f'(kappa/8 = {mp.nstr(kvm / 8, 4)}, kappa = {mp.nstr(kvm, 4)})')


print('\n--- 3. strict exit, targeted sampling of the (A5) set: Q(b) = (1-tau) delta, K_perp = tau delta x^beta ---')
print('  b = r_b (cos psi, sin psi) with r_b solving Q(b) = (1-tau) delta; v_perp direction random in Y^perp')
Gl = sp.lambdify(th, Gf, 'mpmath')
hl = sp.lambdify(th, hf, 'mpmath')
G0m = mp.mpf(sp.N(G0, 50))


def Qb(bt, be):
    return Gl(bt) - G0m + hl(bt) * be ** 2 / 2


def b_on_level(psi, level):
    cps, sps = mp.cos(psi), mp.sin(psi)
    f1 = lambda rr: Qb(rr * cps, rr * sps) - level
    hi = mp.sqrt(level / lam0m) * 2
    lo = mp.mpf(0)
    for _ in range(200):
        mid = (lo + hi) / 2
        if f1(mid) > 0:
            hi = mid
        else:
            lo = mid
    rr = (lo + hi) / 2
    return rr * cps, rr * sps


def targeted(xe, delta, Npsi=48, taus=(0, mp.mpf('1e-4'), mp.mpf('1e-2'), mp.mpf('0.1'), mp.mpf('0.5'), mp.mpf('0.9'), 1), Ndir=4):
    worst = (mp.mpf(10), None)
    for ip in range(Npsi):
        psi = 2 * mp.pi * ip / Npsi + mp.mpf('0.013')
        for tau in taus:
            level = (1 - mp.mpf(tau)) * delta
            if level <= 0:
                bt, be = mp.mpf(0), mp.mpf(0)
            else:
                bt, be = b_on_level(psi, level)
            for idr in range(Ndir):
                res = Xi_hat(xe, bt, be, delta, 2 * 3.14159265 * idr / Ndir + 0.1)
                if res is None:
                    continue
                if res[0] < worst[0]:
                    worst = (res[0], (float(bt / mp.sqrt(delta)), float(be / mp.sqrt(delta)), float(tau)))
    return worst


RUN3 = os.environ.get('K2_PART4_ONLY') is None
for delta, xs in ([] if not RUN3 else [(mp.mpf('1e-2'), [mp.mpf('1e-4'), mp.mpf('1e-8')]),
                  (mp.mpf('1e-4'), [mp.mpf('1e-6'), mp.mpf('1e-10')]),
                  (mp.mpf('2e-7'), [mp.mpf('1e-9'), mp.mpf('1e-13')])]):
    for xe in xs:
        w, where = targeted(xe, delta)
        print(f'  delta={mp.nstr(delta, 2):>6} x={mp.nstr(xe, 2):>6}: min Xi_hat = {mp.nstr(w, 6):>10}  at (theta,e)/sqrt(delta), tau = {where}'
              f'   [kappa/8 = {mp.nstr(kvm / 8, 4)}, 2kappa = {mp.nstr(2 * kvm, 4)}]')


if not RUN3:
    print('\n--- 4. strict exit near purely angular b (e ~ 0), small K_perp, 16 directions of v_perp ---')
    for delta, xe in [(mp.mpf('1e-4'), mp.mpf('1e-8')), (mp.mpf('2e-7'), mp.mpf('1e-11'))]:
        worst = (mp.mpf(10), None)
        for psi in [mp.mpf(0), mp.pi, mp.mpf('1e-3'), mp.pi - mp.mpf('1e-3'), mp.mpf('0.01'), mp.pi + mp.mpf('0.01')]:
            for tau in [0, mp.mpf('1e-8'), mp.mpf('1e-6'), mp.mpf('1e-4'), mp.mpf('1e-3'), mp.mpf('1e-2'), mp.mpf('0.05'), mp.mpf('0.2')]:
                bt, be = b_on_level(psi, (1 - mp.mpf(tau)) * delta)
                for idr in range(16):
                    res = Xi_hat(xe, bt, be, delta, 2 * 3.14159265 * idr / 16)
                    if res is not None and res[0] < worst[0]:
                        worst = (res[0], (float(bt / mp.sqrt(delta)), float(be / mp.sqrt(delta)), float(tau), idr))
        print(f'  delta={mp.nstr(delta, 2):>6} x={mp.nstr(xe, 2):>6}: min Xi_hat = {mp.nstr(worst[0], 6)} at {worst[1]}'
              f'   [kappa/8 = {mp.nstr(kvm / 8, 4)}, 2kappa = {mp.nstr(2 * kvm, 4)}]')
