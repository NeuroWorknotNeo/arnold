# [Эксперимент] R48: проверка реализации поля Y в exit_check.py: Y = Pi_* (d_s - X^th/s d_th - X^eps/s d_eps)
# через численное дифференцирование карты Pi; и Y rho = 1.
import mpmath as mp
import exit_check as ec
mp.mp.dps = 60
def Pi(s, th, e):
    return [s*mp.cos(th), s*mp.sin(th), s**mp.mpf(1.5)*e]
worst = 0
for (s, th, e, mup) in [(mp.mpf('1e-3'), mp.mpf('0.45'), mp.mpf('0.7'), mp.mpf('0.1')),
                        (mp.mpf('1e-4'), mp.mpf('0.1'), mp.mpf('-0.2'), mp.mpf('0.3')),
                        (mp.mpf('1e-2'), mp.mpf('3.0'), mp.mpf('0.3'), mp.mpf('0.05')),
                        (mp.mpf('1e-5'), mp.mpf('1.5'), mp.mpf('1.1'), mp.mpf('0.2'))]:
    Xt, Xe = ec.X0(th, e); Xt, Xe = mup*Xt, mup*Xe
    d = [mp.diff(lambda t: Pi(t, th, e)[i], s) - Xt/s*mp.diff(lambda t: Pi(s, t, e)[i], th)
         - Xe/s*mp.diff(lambda t: Pi(s, th, t)[i], e) for i in range(3)]
    Y = ec.Yv(Pi(s, th, e), mup)
    err = max(abs(d[i] - Y[i]) for i in range(3))
    yrho = Y[0]*mp.cos(th) + Y[1]*mp.sin(th)
    worst = max(worst, err)
    print('s=%s th=%s: |Y_impl - Pi_*(...)| = %s, Y.grad rho = %s' % (mp.nstr(s, 2), mp.nstr(th, 3), mp.nstr(err, 3), mp.nstr(yrho, 20)))
