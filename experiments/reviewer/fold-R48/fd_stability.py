# [Эксперимент] R48: устойчивость разностной производной в exit_check.ratio к шагу (точка минимума у стенки).
import mpmath as mp
import exit_check as ec
mp.mp.dps = 110
s, delta, mup = mp.mpf('1e-10'), mp.mpf('0.01'), mp.mpf('0.02')
th = mp.mpf(-0.24) + 9*(mp.pi + mp.mpf(0.48))/47
gth = mp.cos(th)**7 + mp.sin(th)**7
f = mp.sqrt(delta*(1 - mp.mpf('1e-3')) - s*gth)
ep = mp.sqrt(mp.sin(th) + f)
src = open('exit_check.py').read()
for expo in (-20, -25, -30, -35):
    ns = {}
    exec(src.replace("mp.mpf(10)**-25*s", "mp.mpf(10)**%d*s" % expo).replace("if __name__ == '__main__':", "if False:"), ns)
    print('step 1e%d: ratio = %s' % (expo, mp.nstr(ns['ratio'](s, th, ep, mp.pi/2, mup, delta), 12)))
