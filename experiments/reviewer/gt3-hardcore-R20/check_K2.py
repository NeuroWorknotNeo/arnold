"""[Эксперимент] R20: лемма K2 и формула для G-hat (§3.3) на примере теоремы B и на примере §9.5.

Численно (mpmath, 40 знаков) для U=(x^2+y^2-z^2)^2+x z^4 (m=4, j=5, c=3/2):
  * y*(s,theta) — корень d_y phi=0 в шаре (Ньютон);
  * R = phi(y*), G-hat = R/s^{j-m} и интегральная формула для G-hat;
  * M = int_0^1 (1-l) phi_yy(y*+l tau) dl, tau=s^{c-1} e;
  * тождество (3.4): U(s omega+eta* n+s^c e n) = s^j (G-hat + e^2 M);
  * предел s->0: F~(0,theta,e) = G + 1/2 h e^2, G=g_5=sqrt2 cos/8, h=8.
"""
import mpmath as mp

mp.mp.dps = 40


def U(q):
    x, y, z = q
    return (x * x + y * y - z * z)**2 + x * z**4


def frame(cphi, sphi):
    r2 = mp.sqrt(2)
    om = [cphi / r2, sphi / r2, 1 / r2]
    n = [-cphi / r2, -sphi / r2, 1 / r2]
    return om, n


def phi(s, y, om, n, m=4):
    q = [s * (om[i] + y * n[i]) for i in range(3)]
    return U(q) / s**m


def dphi(s, y, om, n):
    return mp.diff(lambda t: phi(s, t, om, n), y)


def ystar(s, om, n):
    return mp.findroot(lambda t: dphi(s, t, om, n), 0)


def check(cphi, s, e):
    sphi = mp.sqrt(1 - cphi**2)
    om, n = frame(cphi, sphi)
    m, j = 4, 5
    c = mp.mpf(j - m + 2) / 2
    ys = ystar(s, om, n)
    R = phi(s, ys, om, n)
    Ghat = R / s**(j - m)
    # интегральная формула: Ghat = int_0^1 (1-t)^{j-m-1}/(j-m-1)! R^{(j-m)}(t s) dt ; j-m=1 -> int R'(ts) dt
    Rf = lambda t: phi(t, ystar(t, om, n), om, n) if t != 0 else mp.mpf(0)
    Ghat_int = mp.quad(lambda t: mp.diff(Rf, t * s), [0, 1])
    tau = s**(c - 1) * e
    M = mp.quad(lambda l: (1 - l) * mp.diff(lambda t: phi(s, t, om, n), ys + l * tau, 2), [0, 1])
    eta = s * ys
    q = [s * om[i] + eta * n[i] + s**c * e * n[i] for i in range(3)]
    lhs = U(q)
    rhs = s**j * (Ghat + e * e * M)
    return lhs, rhs, Ghat, Ghat_int, M


for cphi in [mp.mpf('0.6'), mp.mpf(1), mp.mpf('-0.3')]:
    for s in [mp.mpf('0.01'), mp.mpf('0.001')]:
        for e in [mp.mpf('0.7'), mp.mpf(-2)]:
            lhs, rhs, Gh, Ghi, M = check(cphi, s, e)
            print('cos=%s s=%s e=%s  rel.err(3.4)=%.2e  Ghat-Ghat_int=%.2e  Ghat=%s (G=%s)  M=%s (h/2=4)' % (
                mp.nstr(cphi, 3), mp.nstr(s, 3), mp.nstr(e, 3), float(abs(lhs - rhs) / abs(rhs)),
                float(abs(Gh - Ghi)), mp.nstr(Gh, 8), mp.nstr(mp.sqrt(2) * cphi / 8, 8), mp.nstr(M, 8)))
