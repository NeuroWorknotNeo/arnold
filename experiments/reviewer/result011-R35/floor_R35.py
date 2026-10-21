"""R35: numeric illustration of Lemma N2 (F_fl = s^j (G_min + O(s^{1/N}))) for M1, M2,
and location of the minimiser |y| <= E s^{gamma_*}.  [Experiment]"""
import mpmath as mp
mp.mp.dps = 40

def phiM1(s, p, y):
    c, si = mp.cos(p), mp.sin(p)
    return (y - s*c**2)**4 + s*(c**5 + si**5) + s**3*(c*si**6 + si*c**6)

def phiM2(s, p, y):
    c, si = mp.cos(p), mp.sin(p)
    f = c**4 + c**3*si + si**4
    return y**4 + s*f*y + s**2*c**6 + s**2*y**5*(c + 2*si)

def minimise(fun, s, p, y1):
    # dense grid then local refinement (1-D)
    n = 4000
    best = min(((fun(s, p, -y1 + 2*y1*k/n), -y1 + 2*y1*k/n) for k in range(n + 1)))
    yb = best[1]
    h = 2*y1/n
    for _ in range(80):
        cand = [(fun(s, p, yb + h*t), yb + h*t) for t in (-1, -0.5, 0, 0.5, 1)]
        b2 = min(cand)
        yb = b2[1]; h *= 0.6
    return fun(s, p, yb), yb

t2 = mp.findroot(lambda q: 4*q**3 - 3*q**2 - 4*q + 1, 0.2236)
cases = [('M1 phi=pi', phiM1, mp.pi, mp.mpf(1)/4, 1, lambda p: mp.cos(p)**5 + mp.sin(p)**5),
         ('M2 phi*', phiM2, mp.atan(t2), mp.mpf(1)/3, mp.mpf(4)/3,
          lambda p: -3*mp.mpf(4)**(-mp.mpf(4)/3)*(mp.cos(p)**4 + mp.cos(p)**3*mp.sin(p) + mp.sin(p)**4)**(mp.mpf(4)/3)),
         ('M2 pi/2', phiM2, mp.pi/2, mp.mpf(1)/3, mp.mpf(4)/3,
          lambda p: -3*mp.mpf(4)**(-mp.mpf(4)/3)*(mp.cos(p)**4 + mp.cos(p)**3*mp.sin(p) + mp.sin(p)**4)**(mp.mpf(4)/3))]
for name, fun, p, gs, b1, Gmin in cases:
    print(name, ' G_min =', mp.nstr(Gmin(p), 10))
    for e in [2, 4, 6, 8, 10]:
        s = mp.mpf(10)**(-e)
        val, yb = minimise(fun, s, p, mp.mpf('0.2'))
        print(f'   s=1e-{e}: min phi / s^(2r g*) = {mp.nstr(val/s**b1, 12)}   y_min/s^g* = {mp.nstr(yb/s**gs, 8)}')
