# [Эксперимент] R48: точка нарушения (A5) при delta=0.002, mu'=0.02 = 10 delta (K_perp = 0.003 delta rho^6):
# проверка независимости от s и от шага разностной производной.
import mpmath as mp
import exit_check as ec
mp.mp.dps = 110
delta, mup, kap = mp.mpf('0.002'), mp.mpf('0.02'), mp.mpf('0.003')
th = mp.mpf(-0.24) + 9*(mp.pi + mp.mpf(0.48))/47
src = open('exit_check.py').read()
for s in (mp.mpf('1e-8'), mp.mpf('1e-14'), mp.mpf('1e-20')):
    gth = mp.cos(th)**7 + mp.sin(th)**7
    f = mp.sqrt(delta*(1 - kap) - s*gth)
    ep = mp.sqrt(mp.sin(th) + f)
    vals = []
    for expo in (-20, -30):
        ns = {}
        exec(src.replace("mp.mpf(10)**-25*s", "mp.mpf(10)**%d*s" % expo).replace("if __name__ == '__main__':", "if False:"), ns)
        vals.append(mp.nstr(ns['ratio'](s, th, ep, mp.pi/2, mup, delta), 10))
    print('s=%s: ratio (steps 1e-20, 1e-30) = %s' % (mp.nstr(s, 2), vals))
