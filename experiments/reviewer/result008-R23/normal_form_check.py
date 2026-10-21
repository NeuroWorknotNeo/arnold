"""R23: проверка нормальной формы (3.1)-(3.2) на примерах 1 и 2 (d=0) и 3 (d=1, точка дуги).

[Эксперимент] mpmath 60 знаков. Для s -> 0 сравниваем
  U(s w + eta*(s) + s^c sum_a e_a E_a) / s^j   с   G + 1/2 e^T H e,
где eta* = s * y*(s) находится Ньютоном в слое, c = (j-m+2)/2.
"""
import mpmath as mp

mp.mp.dps = 60


def U1(x, y, z):
    return (x**2 - z**2)**2 + (y**2 - z**2)**2 + z**5


def U2(x, y, z):
    return (x**2 - z**2 + z**3)**2 + (y**2 - z**2)**2 + z**7


def U3(x, y, z):
    P = x**2 + y**2 - z**2 + z**3
    return P**2 + x * z**6 + x * y * z**5 + z**7 / 2


def ystar(U, s, w, basis, m):
    p = len(basis)
    yv = mp.matrix([0] * p)

    def phi(yy):
        pt = [s * (w[i] + sum(yy[a] * basis[a][i] for a in range(p))) for i in range(3)]
        return U(*pt) / s**m

    h = mp.mpf('1e-15')
    for _ in range(80):
        g = mp.matrix(p, 1)
        Hm = mp.matrix(p, p)
        for a in range(p):
            ea = mp.matrix([0] * p); ea[a] = h
            g[a] = (phi(yv + ea) - phi(yv - ea)) / (2 * h)
            for b in range(p):
                eb = mp.matrix([0] * p); eb[b] = h
                Hm[a, b] = (phi(yv + ea + eb) - phi(yv + ea - eb) - phi(yv - ea + eb) + phi(yv - ea - eb)) / (4 * h * h)
        dy = mp.lu_solve(Hm, g)
        yv = yv - dy
        if mp.norm(dy) < mp.mpf('1e-40'):
            break
    return yv


def test(name, U, w, basis, m, j, G, H, evec):
    c = mp.mpf(j - m + 2) / 2
    target = G + sum(evec[a] * H[a][b] * evec[b] for a in range(len(basis)) for b in range(len(basis))) / 2
    print(name, ' c =', c, ' target G + 1/2 e^T H e =', mp.nstr(target, 12))
    for s in ['1e-2', '1e-3', '1e-4', '1e-5']:
        s = mp.mpf(s)
        yv = ystar(U, s, w, basis, m)
        pt = [s * w[i] + s * sum(yv[a] * basis[a][i] for a in range(len(basis)))
              + s**c * sum(evec[a] * basis[a][i] for a in range(len(basis))) for i in range(3)]
        print('   s=%s  U/s^j = %s' % (mp.nstr(s, 2), mp.nstr(U(*pt) / s**j, 12)))


sq3 = mp.sqrt(3)
w = [1 / sq3, 1 / sq3, -1 / sq3]
e1 = [1 / mp.sqrt(2), -1 / mp.sqrt(2), 0]
e2 = [1 / mp.sqrt(6), 1 / mp.sqrt(6), 2 / mp.sqrt(6)]
H = [[mp.mpf(8) / 3, 0], [0, 8]]
test('Example 1', U1, w, [e1, e2], 4, 5, -3**mp.mpf(-2.5), H, [mp.mpf('0.3'), mp.mpf('-0.2')])
test('Example 2', U2, w, [e1, e2], 4, 7, -3**mp.mpf(-3.5), H, [mp.mpf('0.3'), mp.mpf('-0.2')])
ph = 5 * mp.pi / 6
w3 = [mp.cos(ph) / mp.sqrt(2), mp.sin(ph) / mp.sqrt(2), 1 / mp.sqrt(2)]
n3 = [mp.cos(ph) / mp.sqrt(2), mp.sin(ph) / mp.sqrt(2), -1 / mp.sqrt(2)]
test('Example 3 (slice at phi=5pi/6)', U3, w3, [n3], 4, 7, mp.sqrt(2) * (2 - 3 * sq3) / 64, [[8]], [mp.mpf('0.1')])
