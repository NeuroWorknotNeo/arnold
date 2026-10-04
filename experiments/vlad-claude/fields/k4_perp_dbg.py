import sys, os, random
sys.argv = ['x', '200', '1', '--y']
MODE = os.environ.get('MODE', 'targeted')
src = open('k4_perp.py').read().split('random.seed(3)')[0]
exec(src)
random.seed(3); r = mp.mpf('1e-96'); worst = None; n = 0
while n < 100:
    p = sample(r, MODE)
    if U_cart(*p) >= 0: continue
    n += 1; l, q = check(p)
    if worst is None or l < worst[0]: worst = (l, p)
l, p = worst
s, th, sig = coords(*p)
f = lambda: None
print('dps', mp.mp.dps, 'λ', mp.nstr(l, 6), 'θ−π/2', mp.nstr(th-mp.pi/2, 6), 'σ̂', mp.nstr(sig/s**ALPHA, 6), 't/r^(1/3)', mp.nstr((th-mp.pi/2)/r**(mp.mpf(1)/3),5), 'σ/r^(4/3)', mp.nstr(sig/r**(mp.mpf(4)/3),5))
