"""R32: численная проверка цепочки теоремы Mc на примере C1 = Q0^2 - z^6 + x z^6.  [Эксперимент]

Q0 = x^2 + y^2 - z^2; u_4 = Q0^2, Sigma_+ = {z = 1/sqrt2} -- окружность (k_g != 0).
Ожидается: j = 6, G = -1/8 (константа, случай (c)), c = 2, mu = 2c = 4.

Проверяется (mpmath, 50 знаков):
 a) Ghat(s,theta) = R/s^{j-m} -> -1/8 равномерно по theta, поправка O(s) и зависит от theta;
 b) (2.4): U(Psi(s,theta,s^c e)) = s^j F(s^{1/2},theta,e), где F = Ghat + e^2 M (M -- квадратурой);
 c) дефект неравенства Эйлера (L2) с mu = 2c:
        Def(s,theta,e) := (beta W - rho Y W - mu W) / s^j,
    где YW = d/ds' U(Psi(s',theta,zeta))|_{zeta fixed} + A'(s), считается численным дифференцированием
    с пересчётом eta*(s',theta). Должно быть O(s) равномерно по theta и |e| <= R_e.
 d) theta_1 = sup|eta*_s|, theta_2 = sup s|eta*_ss|, theta_3 = sup(s|eta*_ss| + 2|eta*_{s theta}|) -> 0.
"""
import mpmath as mp

mp.mp.dps = 50
z0 = 1 / mp.sqrt(2)
r0 = mp.sqrt(1 - z0**2)
m, j = 4, 6
c = mp.mpf(j - m + 2) / 2
a0 = mp.mpf(1) / 8


def U(q):
    x, y, z = q
    Q0 = x**2 + y**2 - z**2
    return Q0**2 - z**6 + x * z**6


def frame(th):
    ph = th / r0  # natural parameter theta = r0*phi
    om = mp.matrix([r0 * mp.cos(ph), r0 * mp.sin(ph), z0])
    ell = mp.matrix([-mp.sin(ph), mp.cos(ph), 0])
    n = mp.matrix([om[1] * ell[2] - om[2] * ell[1], om[2] * ell[0] - om[0] * ell[2],
                   om[0] * ell[1] - om[1] * ell[0]])
    return om, ell, n


def phi(s, th, y):
    om, ell, n = frame(th)
    return U(s * (om + y * n)) / s**m


def ystar(s, th):
    y = mp.mpf(0)
    for _ in range(60):
        d1 = mp.diff(lambda t: phi(s, th, t), y, 1)
        d2 = mp.diff(lambda t: phi(s, th, t), y, 2)
        dy = d1 / d2
        y -= dy
        if abs(dy) < mp.mpf(10)**(-45):
            break
    return y


def etastar(s, th):
    return s * ystar(s, th)


def Psi(s, th, zeta):
    om, ell, n = frame(th)
    return s * om + (etastar(s, th) + zeta) * n


def Ghat(s, th):
    return phi(s, th, ystar(s, th)) / s**(j - m)


def Mfun(s, th, tau):
    ys = ystar(s, th)
    return mp.quad(lambda lam: (1 - lam) * mp.diff(lambda t: phi(s, th, t), ys + lam * tau, 2), [0, 1])


print('a) Ghat(s,theta):')
for s in [mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')]:
    vals = [Ghat(s, k * 2 * mp.pi * r0 / 6) for k in range(6)]
    print('  s=%s  Ghat+1/8 over theta: %s' % (mp.nstr(s, 3), [mp.nstr(v + a0, 5) for v in vals]))

print('b) (2.4) residual:')
for s in [mp.mpf('1e-2'), mp.mpf('1e-3')]:
    for th in [mp.mpf('0.3'), mp.mpf('2.1')]:
        for e in [mp.mpf('0.4'), mp.mpf('-0.25')]:
            lhs = U(Psi(s, th, s**c * e))
            F = Ghat(s, th) + e**2 * Mfun(s, th, s**(c - 1) * e)
            rhs = s**j * F
            print('  s=%s th=%s e=%s  rel.res=%s' % (mp.nstr(s, 2), mp.nstr(th, 2), mp.nstr(e, 2),
                                                  mp.nstr(abs(lhs - rhs) / abs(rhs), 3)))

print('c) Euler defect (beta W - rho YW - 2c W)/s^j:')
hstar = None
for s in [mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')]:
    worst = 0
    for k in range(8):
        th = k * 2 * mp.pi * r0 / 8
        for e in [mp.mpf(x) / 10 for x in (-4, -2, 0, 1, 3, 5)]:
            zeta = s**c * e
            W = lambda sp_: U(Psi(sp_, th, zeta)) + a0 * sp_**j
            Wv = W(s)
            YW = mp.diff(W, s)
            D = (j * Wv - s * YW - 2 * c * Wv) / s**j
            worst = max(worst, abs(D))
    print('  s=%s  max|Def| = %s   max|Def|/s = %s' % (mp.nstr(s, 2), mp.nstr(worst, 5), mp.nstr(worst / s, 5)))

print('d) theta_i:')
for s in [mp.mpf('1e-2'), mp.mpf('1e-3')]:
    t1 = t2 = t3 = 0
    for k in range(8):
        th = k * 2 * mp.pi * r0 / 8
        es_s = mp.diff(lambda u: etastar(u, th), s)
        es_ss = mp.diff(lambda u: etastar(u, th), s, 2)
        es_st = mp.diff(lambda u: mp.diff(lambda v: etastar(u, v), th), s)
        t1 = max(t1, abs(es_s))
        t2 = max(t2, s * abs(es_ss))
        t3 = max(t3, s * abs(es_ss) + 2 * abs(es_st))
    print('  s=%s  theta1=%s theta2=%s theta3=%s' % (mp.nstr(s, 2), mp.nstr(t1, 4), mp.nstr(t2, 4), mp.nstr(t3, 4)))
