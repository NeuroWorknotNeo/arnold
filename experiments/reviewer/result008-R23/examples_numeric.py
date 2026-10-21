"""R23: численная проверка R(s) ~ s^{j-m} g_j для примеров 1-3 и семейств Четаева примера 3.

[Эксперимент] mpmath, 50 знаков. R(s) = min_y phi(s,theta,y) находится методом Ньютона
по y в слое (критическая точка, стартуя с y=0), затем сравнивается R/s^{j-m} с g_j.
"""
import mpmath as mp

mp.mp.dps = 50


def U1(x, y, z):
    A = x**2 - z**2
    B = y**2 - z**2
    return A**2 + B**2 + z**5


def U2(x, y, z):
    P1 = x**2 - z**2 + z**3
    P2 = y**2 - z**2
    return P1**2 + P2**2 + z**7


def u7_3(x, y, z):
    return x * z**6 + x * y * z**5 + z**7 / 2


def U3(x, y, z):
    P = x**2 + y**2 - z**2 + z**3
    return P**2 + u7_3(x, y, z)


def EU(U, x, y, z):
    f = lambda t: U(t * x, t * y, t * z)
    return mp.diff(f, 1)


def crit_in_slice(U, s, w, basis, m):
    p = len(basis)
    yv = mp.matrix([0] * p)

    def phi(yy):
        pt = [s * (w[i] + sum(yy[a] * basis[a][i] for a in range(p))) for i in range(3)]
        return U(*pt) / s**m

    for it in range(60):
        g = mp.matrix(p, 1)
        Hm = mp.matrix(p, p)
        h = mp.mpf('1e-12')
        for a in range(p):
            ea = mp.matrix([0] * p)
            ea[a] = h
            g[a] = (phi(yv + ea) - phi(yv - ea)) / (2 * h)
            for b in range(p):
                eb = mp.matrix([0] * p)
                eb[b] = h
                Hm[a, b] = (phi(yv + ea + eb) - phi(yv + ea - eb) - phi(yv - ea + eb) + phi(yv - ea - eb)) / (4 * h * h)
        dy = mp.lu_solve(Hm, g)
        yv = yv - dy
        if mp.norm(dy) < mp.mpf('1e-30'):
            break
    return phi(yv), yv


mp.mp.dps = 60
sq3 = mp.sqrt(3)
w = [1 / sq3, 1 / sq3, -1 / sq3]
e1 = [1 / mp.sqrt(2), -1 / mp.sqrt(2), 0]
e2 = [1 / mp.sqrt(6), 1 / mp.sqrt(6), 2 / mp.sqrt(6)]
print('Example 1: R/s -> g5 =', -3**mp.mpf(-2.5))
for s in ['1e-2', '1e-3', '1e-4']:
    s = mp.mpf(s)
    R, yv = crit_in_slice(U1, s, w, [e1, e2], 4)
    print('  s=%s  R/s=%s  y*=%s' % (mp.nstr(s, 3), mp.nstr(R / s, 12), [mp.nstr(t, 6) for t in yv]))
print('Example 2: R/s^3 -> g7 =', -3**mp.mpf(-3.5), ' y*/s ->', mp.sqrt(2) / 12, mp.sqrt(6) / 36)
for s in ['1e-2', '1e-3', '1e-4']:
    s = mp.mpf(s)
    R, yv = crit_in_slice(U2, s, w, [e1, e2], 4)
    print('  s=%s  R/s^3=%s  y*/s=%s' % (mp.nstr(s, 3), mp.nstr(R / s**3, 12), [mp.nstr(t / s, 8) for t in yv]))
print('Example 3: R/s^3 -> G+(5pi/6) =', mp.sqrt(2) * (2 - 3 * sq3) / 64)
ph = 5 * mp.pi / 6
w3 = [mp.cos(ph) / mp.sqrt(2), mp.sin(ph) / mp.sqrt(2), 1 / mp.sqrt(2)]
n3 = [mp.cos(ph) / mp.sqrt(2), mp.sin(ph) / mp.sqrt(2), -1 / mp.sqrt(2)]
for s in ['1e-2', '1e-3', '1e-4']:
    s = mp.mpf(s)
    R, yv = crit_in_slice(U3, s, w3, [n3], 4)
    print('  s=%s  R/s^3=%s  y*/s=%s' % (mp.nstr(s, 3), mp.nstr(R / s**3, 12), mp.nstr(yv[0] / s, 8)))
for ph in [mp.pi / 2, 7 * mp.pi / 6, mp.pi]:
    w3 = [mp.cos(ph) / mp.sqrt(2), mp.sin(ph) / mp.sqrt(2), -1 / mp.sqrt(2)]
    n3 = [mp.cos(ph) / mp.sqrt(2), mp.sin(ph) / mp.sqrt(2), 1 / mp.sqrt(2)]
    Gm = mp.sqrt(2) / 32 * (2 * mp.cos(ph) - mp.sin(2 * ph) - 1)
    s = mp.mpf('1e-4')
    R, yv = crit_in_slice(U3, s, w3, [n3], 4)
    print('  Sigma_-: phi=%s  R/s^3=%s  G-=%s' % (mp.nstr(ph, 5), mp.nstr(R / s**3, 12), mp.nstr(Gm, 12)))

print('Example 3 Chetaev families (upper: phi=5pi/6, z=zeta; lower: phi=pi, z=-zeta)')
for zs in ['1e-2', '1e-3', '1e-4', '1e-5']:
    zeta = mp.mpf(zs)
    # upper
    cph, sph = mp.cos(5 * mp.pi / 6), mp.sin(5 * mp.pi / 6)

    def f_up(r):
        xx, yy, zz = r * cph, r * sph, zeta
        P = r**2 - zeta**2 + zeta**3
        return P - mp.sqrt(-u7_3(xx, yy, zz)) / 2

    a, b = zeta * mp.sqrt(1 - zeta), zeta
    assert f_up(a) < 0 < f_up(b)
    r = mp.findroot(f_up, (a, b), solver='bisect', tol=mp.mpf(10)**(-55))
    pt = (r * cph, r * sph, zeta)
    Uu, Eu = U3(*pt), EU(U3, *pt)

    def f_lo(r):
        xx, yy, zz = -r, 0, -zeta
        P = r**2 - zeta**2 - zeta**3
        return P + mp.sqrt(-u7_3(xx, yy, zz)) / 2

    a, b = zeta, mp.sqrt(zeta**2 + zeta**3)
    assert f_lo(a) < 0 < f_lo(b)
    r2 = mp.findroot(f_lo, (a, b), solver='bisect', tol=mp.mpf(10)**(-55))
    pt2 = (-r2, 0, -zeta)
    Ul, El = U3(*pt2), EU(U3, *pt2)
    print('  zeta=%s  up: U=%s EU/|U|=%s   low: U=%s EU/|U|=%s' % (zs, mp.nstr(Uu, 5), mp.nstr(Eu / abs(Uu), 5), mp.nstr(Ul, 5), mp.nstr(El / abs(Ul), 5)))
