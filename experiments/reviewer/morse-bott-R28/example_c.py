"""R28: численная проверка нормальной формы (2.8) и неравенства (L2) теоремы Mc
на примере случая (c):  U = Q0^2 - z^6 + x z^6,  Q0 = x^2 + y^2 - z^2.   [Эксперимент]

m = 4, Sigma = две окружности z = +-1/sqrt2, на Sigma_+ : G = g_6 = -1/8 (константа),
h_n = 8, j = 6, c = 2, mu = 2c = 4, a0 = 1/8.  Поправка x z^6 даёт непостоянную по углу g_7.

Проверяется (mpmath, 50 знаков):
 1. U(Psi(s,th,s^c e))/s^j -> -1/8 + 4 e^2 при s -> 0 (равномерно по углу);
 2. на множестве  Q<4delta, F+a0<=delta  (замыкание D) величина
        [beta W - rho YW - mu W] / (delta s^j)  >= -eps_1(s) с eps_1 -> 0;
    Y = d/ds при фиксированных (th, zeta), производная — численно.
"""
import mpmath as mp

mp.mp.dps = 50
SQ2 = mp.sqrt(2)


def U(x, y, z):
    Q0 = x * x + y * y - z * z
    return Q0 ** 2 - z ** 6 + x * z ** 6


def frame(phi):
    om = (mp.cos(phi) / SQ2, mp.sin(phi) / SQ2, 1 / SQ2)
    nn = (-mp.cos(phi) / SQ2, -mp.sin(phi) / SQ2, 1 / SQ2)
    return om, nn


def point(s, phi, eta):
    om, nn = frame(phi)
    return tuple(s * om[i] + eta * nn[i] for i in range(3))


def varphi(s, phi, y):
    return U(*point(s, phi, s * y)) / s ** 4


def ystar(s, phi):
    f = lambda y: mp.diff(lambda t: varphi(s, phi, t), y)
    return mp.findroot(f, mp.mpf(0))


def etastar(s, phi):
    return s * ystar(s, phi)


def W(s, phi, zeta, a0=mp.mpf(1) / 8, j=6):
    return U(*point(s, phi, etastar(s, phi) + zeta)) + a0 * s ** j


j, c, mu, a0, hn = 6, 2, 4, mp.mpf(1) / 8, 8
print('1. нормальная форма: max_{phi,e} |U/s^6 - (-1/8 + 4e^2)|')
for s in [mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')]:
    err = 0
    for phi in [0, 1, 2, 3, 4, 5, 6]:
        for e in [-0.1, 0, 0.05, 0.1]:
            e = mp.mpf(e)
            val = U(*point(s, phi, etastar(s, phi) + s ** c * e)) / s ** j
            err = max(err, abs(val - (-a0 + hn / 2 * e ** 2)))
    print('   s =', mp.nstr(s, 3), ' err =', mp.nstr(err, 5))

print('2. (L2): min [beta W - s dW/ds - mu W]/(delta s^j) на замыкании D, delta = 0.01')
delta = mp.mpf('0.01')
Re = 2 * mp.sqrt(2 * delta / hn)
for s in [mp.mpf('1e-2'), mp.mpf('3e-3'), mp.mpf('1e-3')]:
    worst = mp.inf
    for phi in [0, 0.7, 1.5, 2.5, 3.14, 4, 5.5]:
        phi = mp.mpf(phi)
        for t in range(-10, 11):
            e = Re * t / 10
            zeta = s ** c * e
            Wv = W(s, phi, zeta)
            if Wv / s ** j > delta:   # вне замыкания D
                continue
            dW = mp.diff(lambda ss: W(ss, phi, zeta), s)
            val = (j * Wv - s * dW - mu * Wv) / (delta * s ** j)
            worst = min(worst, val)
    print('   s =', mp.nstr(s, 3), ' min =', mp.nstr(worst, 6))
