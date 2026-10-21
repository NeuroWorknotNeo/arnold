# [Эксперимент] Дно оврага (минимум U на сферах |q| = r) около полюса e_z в примерах записки singular-sigma:
#   M   — модель U = x^2y^2 + eps z^2(x^4+y^4) - z^6 + x^6 + y^6 (eps = 0.1): дно — ось z (точно, по симметрии);
#   MP  — модель + x z^6 + 2 y^2 z^5 (симметрия сломана): дно уходит с оси вдоль ветви {y = 0} на угол ~ -r/6;
#   II  — U_II = x^2y^2 + 2xyz^3 + z^6/2 + x^6 + y^6: дно — у вершины гиперболы x y = -z^3, угол ~ sqrt(2 r).
# W~(r, theta) = U(r omega(theta))/r^6 + a0 в гномонической карте; минимум — сетка + Ньютон (mpmath, 40 знаков).
# Печатается: r, theta_min, |theta_min|, W~min (= глубина относительно -a0 r^6), а для M — ширина креста:
# угловая длина рукава вдоль ветви и поперечная полуширина при |theta_1| = 0.05 на уровне W~ = delta.
import mpmath as mp
mp.mp.dps = 40
EPS = mp.mpf('0.1')
def Ufun(name, X, Y, Z):
    if name in ('M', 'MP'):
        v = X**2*Y**2 + EPS*Z**2*(X**4 + Y**4) - Z**6 + X**6 + Y**6
        if name == 'MP': v += X*Z**6 + 2*Y**2*Z**5
        return v
    return X**2*Y**2 + 2*X*Y*Z**3 + Z**6/2 + X**6 + Y**6
A0 = {'M': 1, 'MP': 1, 'II': mp.mpf(1)/2}
def Wt(name, r, t1, t2):
    c = 1/mp.sqrt(1 + t1**2 + t2**2)
    return Ufun(name, r*c*t1, r*c*t2, r*c)/r**6 + A0[name]
def argmin(name, r, start):
    f = lambda a, b: Wt(name, r, a, b)
    g = lambda a, b: [mp.diff(lambda u: f(u, b), a), mp.diff(lambda u: f(a, u), b)]
    sol = mp.findroot(g, start)
    return sol[0], sol[1], f(sol[0], sol[1])
for name in ('M', 'MP', 'II'):
    print('== пример', name)
    for r in [mp.mpf(10)**(-k) for k in (2, 3, 4, 5, 6)]:
        # стартовая точка: грубая сетка
        best = None
        n = 40
        R = mp.mpf('0.3') if name != 'II' else 4*mp.sqrt(r)
        for i in range(-n, n + 1):
            for j in range(-n, n + 1):
                a, b = R*i/n, R*j/n
                if name == 'II' and not (a > 0 and b < 0): continue
                v = Wt(name, r, a, b)
                if best is None or v < best[0]: best = (v, a, b)
        try:
            a, b, v = argmin(name, r, [best[1], best[2]])
        except Exception as ex:
            a, b, v = best[1], best[2], best[0]
        extra = ''
        if name == 'MP': extra = '   theta_1*6/r = %s' % mp.nstr(a*6/r, 6)
        if name == 'II': extra = '   |theta|/sqrt(2r) = %s, theta1*theta2/(-r) = %s' % (
            mp.nstr(mp.sqrt(a**2 + b**2)/mp.sqrt(2*r), 6), mp.nstr(a*b/(-r), 6))
        print('r=%-8s theta*=(%s, %s)  W~min=%s%s' % (mp.nstr(r, 2), mp.nstr(a, 6), mp.nstr(b, 6), mp.nstr(v, 6), extra))
# ширина креста в модели M на уровне delta
print('== модель M: крест {W~ < delta}, delta = 0.01')
d = mp.mpf('0.01')
for r in [mp.mpf(10)**(-k) for k in (2, 4, 6)]:
    arm = mp.findroot(lambda t: Wt('M', r, t, 0) - d, 0.05)
    t1 = mp.mpf('0.03')
    half = mp.findroot(lambda t: Wt('M', r, t1, t) - d, r)
    print('r=%-8s длина рукава |theta_1| = %s (прогноз sqrt(delta/3) = %s); полуширина при theta_1=0.03: %s, /(r sqrt(delta - Lambda)/theta_1) = %s' % (
        mp.nstr(r, 2), mp.nstr(arm, 6), mp.nstr(mp.sqrt(d/3), 6), mp.nstr(half, 6),
        mp.nstr(half/(r*mp.sqrt(d - Wt('M', 1, t1, 0) + 0)/t1), 6)))
