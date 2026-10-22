# [Эксперимент] R48: точка нарушения (A5) при delta=0.01, mu'=0.1 (зона перехода chi, K_perp = 0.01 delta rho^6):
# не зависит от s (коническая природа перекрёстного члена).
import mpmath as mp
import exit_check as ec
mp.mp.dps = 110
delta, mup = mp.mpf('0.01'), mp.mpf('0.1')
th = mp.mpf(-0.24) + 9*(mp.pi + mp.mpf(0.48))/47
print('theta =', mp.nstr(th, 8), ' chi(theta) =', mp.nstr(ec.chi(th), 6))
for s in (mp.mpf('1e-8'), mp.mpf('1e-12'), mp.mpf('1e-16'), mp.mpf('1e-20')):
    gth = mp.cos(th)**7 + mp.sin(th)**7
    f = mp.sqrt(delta*(1 - mp.mpf('1e-2')) - s*gth)
    ep = mp.sqrt(mp.sin(th) + f)
    print('s=%s: (rho/lam)Xi/(delta rho^6) = %s' % (mp.nstr(s, 2), mp.nstr(ec.ratio(s, th, ep, mp.pi/2, mup, delta), 10)))
