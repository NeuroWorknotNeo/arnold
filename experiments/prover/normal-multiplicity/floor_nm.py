# [Эксперимент] Функция дна F_fl(s,theta) = min_{|eta| <= s/2} U(s omega(theta) + eta n) для M1, M2
# (лемма N3 записки notes/prover/2026-10-21-normal-multiplicity.md): проверка F_fl / s^j -> G(theta),
# число критических точек в нормальном слое, направление и глубина самого глубокого оврага
# (сравнение с experiments/numerics/2026-10-21-valleys: M1 a = 1, beta = 5; M2 a = 0.5444, beta = 16/3).
import mpmath as mp

mp.mp.dps = 40

def U_M1(xx, yy, zz):
    return (zz - xx**2)**4 + xx**5 + yy**5 + xx*yy**6 + yy*xx**6

def U_M2(xx, yy, zz):
    return zz**4 + zz*(xx**4 + xx**3*yy + yy**4) + xx**6 + xx*zz**5 + 2*yy*zz**5

def slice_min(U, s, ph, ngrid=400):
    """min по eta in [-s/2, s/2] функции eta -> U(s cos ph, s sin ph, eta): сетка + уточнение;
    возвращает (min, argmin, число локальных минимумов/максимумов на сетке)."""
    f = lambda e: U(s*mp.cos(ph), s*mp.sin(ph), e)
    es = [(-s/2) + s*k/ngrid for k in range(ngrid + 1)]
    vals = [f(e) for e in es]
    ncrit = sum(1 for k in range(1, ngrid) if (vals[k] - vals[k-1])*(vals[k+1] - vals[k]) < 0)
    k0 = min(range(len(vals)), key=lambda k: vals[k])
    a, b = es[max(k0 - 1, 0)], es[min(k0 + 1, ngrid)]
    gr = (mp.sqrt(5) - 1)/2
    for _ in range(200):
        c1 = b - gr*(b - a); c2 = a + gr*(b - a)
        if f(c1) < f(c2): b = c2
        else: a = c1
    em = (a + b)/2
    return f(em), em, ncrit

print('M1: G(phi) = cos^5 + sin^5, j = 5; omega* = (0,-1,0) (phi = -pi/2), ожидается F_fl/s^5 -> -1, eta*/s^2 = cos^2 phi')
for ph in [-mp.pi/2, -mp.pi/2 + mp.mpf('0.3')]:
    for s in [mp.mpf(10)**(-k) for k in (2, 4, 6, 8)]:
        m, em, nc = slice_min(U_M1, s, ph)
        G = mp.cos(ph)**5 + mp.sin(ph)**5
        print('  phi=%-8s s=%-6s F_fl/s^5 = %-22s G = %-14s eta_min/s^2 = %-12s cos^2 = %-10s экстр. на сетке: %d' % (
            mp.nstr(ph, 5), mp.nstr(s, 2), mp.nstr(m/s**5, 15), mp.nstr(G, 10), mp.nstr(em/s**2, 8), mp.nstr(mp.cos(ph)**2, 8), nc))

print()
f = lambda ph: mp.cos(ph)**4 + mp.cos(ph)**3*mp.sin(ph) + mp.sin(ph)**4
Gf = lambda ph: -3*mp.mpf(4)**(-mp.mpf(4)/3)*f(ph)**(mp.mpf(4)/3)
ths = mp.atan(mp.findroot(lambda t: 4*t**3 - 3*t**2 - 4*t + 1, mp.mpf('0.2237')))
print('M2: j = 16/3, G = -3*4^(-4/3) f^(4/3); theta* =', mp.nstr(ths, 15), ', G(theta*) =', mp.nstr(Gf(ths), 15))
for ph in [ths, mp.pi/2, ths + mp.mpf('0.2')]:
    for s in [mp.mpf(10)**(-k) for k in (2, 4, 6, 9, 12)]:
        m, em, nc = slice_min(U_M2, s, ph)
        e0 = -mp.cbrt(f(ph)/4)
        print('  phi=%-8s s=%-6s F_fl/s^(16/3) = %-20s G = %-16s eta_min/s^(4/3) = %-12s eps_0 = %-10s экстр.: %d' % (
            mp.nstr(ph, 5), mp.nstr(s, 2), mp.nstr(m/s**(mp.mpf(16)/3), 12), mp.nstr(Gf(ph), 10),
            mp.nstr(em/s**(mp.mpf(4)/3), 8), mp.nstr(e0, 8), nc))

print()
print('M2: самый глубокий овраг на сфере |q| = r (сравнение с valleys: a = 0.54424.., omega_inf = (0.97586, 0.21831, ...))')
for r in [mp.mpf(10)**(-k) for k in (4, 6, 9)]:
    # на сфере s = sqrt(r^2 - eta^2) ~ r; минимизируем по phi
    best = None
    for k in range(-40, 41):
        ph = ths + mp.mpf(k)/400
        m, em, nc = slice_min(U_M2, r, ph, ngrid=200)
        if best is None or m < best[0]:
            best = (m, ph, em)
    print('  r=%-6s min ~ %s * r^(16/3) при phi = %s (theta* = %s)' % (mp.nstr(r, 2), mp.nstr(best[0]/r**(mp.mpf(16)/3), 10),
          mp.nstr(best[1], 6), mp.nstr(ths, 6)))
