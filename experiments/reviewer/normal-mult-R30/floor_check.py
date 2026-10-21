"""R30. [Эксперимент] Лемма N2: равномерность оценки
   |min_{|y|<=y1} phi(s,theta,y) - s^{2r g} G_min(theta)| <= C s^{2r g + 1/N}
по theta (в том числе там, где многоугольник Ньютона в точке theta меняется),
и лемма N3: число вещественных критических точек в слое <= 2r-1.

phi — многочлен по y; минимум на [-y1,y1] ищется точно: корни d phi/dy (mpmath.polyroots,
60 знаков) плюс концы отрезка. G_min — минимум Phi_0 по eps тем же способом.
"""
import mpmath as mp

mp.mp.dps = 60


def poly_min(coeffs_y, lo, hi):
    """coeffs_y: список коэффициентов многочлена по y (от старшего). Минимум на [lo,hi]
    и число вещественных критических точек в (lo,hi)."""
    p = [c for c in coeffs_y]
    while abs(p[0]) == 0:
        p = p[1:]
    deg = len(p) - 1
    dp = [p[k]*(deg - k) for k in range(deg)]
    while abs(dp[0]) == 0:
        dp = dp[1:]
    cands = [lo, hi]
    ncrit = 0
    roots = []
    while len(dp) > 1 and dp[-1] == 0:   # корень y=0 кратности >=1: выделить
        dp = dp[:-1]
        roots.append(mp.mpf(0))
    if roots:
        roots = roots[:1]
    if len(dp) > 1:
        roots += mp.polyroots(dp, maxsteps=800, extraprec=800)
    if True:
        for r in roots:
            if abs(mp.im(r)) < mp.mpf(10)**(-40) * (1 + abs(r)):
                rr = mp.re(r)
                if lo < rr < hi:
                    cands.append(rr)
                    ncrit += 1
    val = lambda t: mp.polyval(p, t)
    return min(val(t) for t in cands), ncrit


def run(name, phi_coeffs, Phi0_coeffs, r, g, N, thetas, svals, y1=mp.mpf('0.2')):
    """phi_coeffs(s,theta) -> коэффициенты по y; Phi0_coeffs(theta) -> по eps."""
    print('=' * 72)
    print(name, f' r={r}, gamma_*={g}, N={N}')
    B = 2*r*mp.mpf(g)
    for s in svals:
        s = mp.mpf(s)
        worst = mp.mpf(0)
        wth = None
        maxcrit = 0
        for th in thetas:
            m, nc = poly_min(phi_coeffs(s, th), -y1, y1)
            G, _ = poly_min(Phi0_coeffs(th), mp.mpf(-50), mp.mpf(50))
            err = abs(m - s**B*G) / s**(B + mp.mpf(1)/N)
            maxcrit = max(maxcrit, nc)
            if err > worst:
                worst, wth = err, th
        print(f'  s={mp.nstr(s,3):>8}  sup_theta err/s^(2rg+1/N) = {mp.nstr(worst,6):>12}'
              f'  (theta={mp.nstr(wth,5)})  max #крит.точек = {maxcrit}  (<= {2*r-1})')


svals = ['1e-2', '1e-3', '1e-4', '1e-6', '1e-8', '1e-10', '1e-12']

# M1: phi = (y - s c^2)^4 + s G + s^3 g7
def m1_phi(s, th):
    c, sn = mp.cos(th), mp.sin(th)
    a = s*c**2
    G = c**5 + sn**5
    g7 = c*sn**6 + sn*c**6
    # (y-a)^4 = y^4 - 4a y^3 + 6a^2 y^2 - 4a^3 y + a^4
    return [1, -4*a, 6*a**2, -4*a**3, a**4 + s*G + s**3*g7]

def m1_Phi0(th):
    c, sn = mp.cos(th), mp.sin(th)
    return [1, 0, 0, 0, c**5 + sn**5]

th_circle = [2*mp.pi*k/400 for k in range(400)] + [3*mp.pi/4, 7*mp.pi/4, mp.pi, 3*mp.pi/2]
run('M1', m1_phi, m1_Phi0, 2, mp.mpf(1)/4, 4, th_circle, svals)

# M2: phi = y^4 + s f y + s^2 c^6 + s^2 y^5 (c + 2 sn)
def m2_phi(s, th):
    c, sn = mp.cos(th), mp.sin(th)
    f = c**4 + c**3*sn + sn**4
    return [s**2*(c + 2*sn), 1, 0, 0, s*f, s**2*c**6]

def m2_Phi0(th):
    c, sn = mp.cos(th), mp.sin(th)
    f = c**4 + c**3*sn + sn**4
    return [1, 0, 0, f, 0]

run('M2', m2_phi, m2_Phi0, 2, mp.mpf(1)/3, 3, th_circle, svals)

# Синтетика 1: phi = y^4 + th s y^2 + s^2 + s y^3; gamma_*=1/2, N=2,
# Phi0 = e^4 + th e^2 + 1, G_min только C^{1,1} в th=0.
ths = [mp.mpf(k)/200 - 1 for k in range(401)]
run('S1: y^4 + th s y^2 + s^2 + s y^3', lambda s, th: [1, s, th*s, 0, s**2],
    lambda th: [1, 0, th, 0, 1], 2, mp.mpf(1)/2, 2, ths, svals)

# Синтетика 2: phi = y^4 + th s y + s y^2 - s^2; gamma_*=1/3, N=3, Phi0 = e^4 + th e;
# в th=0 коэффициент вершины (1,1) обнуляется, поточечный многоугольник другой.
ths2 = ths + [mp.mpf(10)**(-k) for k in range(1, 12)] + [-mp.mpf(10)**(-k) for k in range(1, 12)]
run('S2: y^4 + th s y + s y^2 - s^2', lambda s, th: [1, 0, s, th*s, -s**2],
    lambda th: [1, 0, 0, th, 0], 2, mp.mpf(1)/3, 3, ths2, svals)

# Синтетика 3 (r=3): phi = y^6 + th s y^3 + s^2 y + s y^4; первое ребро:
# (1,3): 1/3, (2,1): 2/5, (1,4): 1/2 -> gamma_*=1/3, N=3, Phi0 = e^6 + th e^3
run('S3 (r=3): y^6 + th s y^3 + s^2 y + s y^4',
    lambda s, th: [1, 0, s, th*s, 0, s**2, 0],
    lambda th: [1, 0, 0, th, 0, 0, 0], 3, mp.mpf(1)/3, 3, ths2, svals)

# Число вещественных критических точек: пример с 3 = 2r-1 ветвями: (y^2 - s)^2 + s^3 y
run('S4: (y^2-s)^2 + s^3 y   [3 вещественные ветви]',
    lambda s, th: [1, 0, -2*s, s**3, s**2],
    lambda th: [1, 0, -2, 0, 1], 2, mp.mpf(1)/2, 2, [mp.mpf(0)], svals)
