# [Эксперимент] исправленная b(u); сетка в координатах лучевой трубки + переходная зона; K задаётся argv
import sys
_argv = sys.argv; sys.argv = [sys.argv[0]]
src = open('k4_spot.py').read().split("r = mp.mpf('1e-48')")[0].replace("Kv = 200", "Kv = int(_argv[1])")
exec(src); sys.argv = _argv
def bfun(t, r):
    u = mp.log(abs(t))/mp.log(r)
    x = (u - mp.mpf('0.05'))/(mp.mpf('0.3') - mp.mpf('0.05'))
    if x <= 0: return mp.mpf(0)
    if x >= 1: return mp.mpf(1)/3
    a = mp.exp(-1/x); b = mp.exp(-1/(1 - x)); return a/(a + b)/3
for rs in sys.argv[2].split(','):
    r = mp.mpf(rs); L = float(-mp.log10(r)); mp.mp.dps = int(150 + 4.5*L)
    tstar = r**(-mp.mpf(1)/30); worst = None; n = 0
    taus = [mp.mpf(v) for v in ('1', '10', '60', '230', '1000')] + [tstar*mp.mpf(v) for v in ('0.5', '0.9', '1.1', '1.5', '3', '10', '100')]
    for sfac in ('0.85', '1.15'):
        s = r*mp.mpf(sfac)
        for ta in taus:
            for sg_t in (1, -1):
                for st in ('-8', '-4', '-2', '-0.88', '-0.3', '-0.05', '0.05', '0.3', '0.88', '2', '4', '8'):
                    th = mp.pi/2 + sg_t*ta*r**(mp.mpf(1)/3)
                    p = cart(s, th, mp.mpf(st)*r**(mp.mpf(4)/3))
                    if Uf(*p) >= 0: continue
                    n += 1
                    rr = mp.sqrt(sum(c*c for c in p))
                    l = lam_min(p, rr*mp.mpf(10)**-(24 + int(0.8*float(-mp.log10(rr)))))
                    if worst is None or l < worst[0]: worst = (l, sfac, mp.nstr(sg_t*ta, 4), st)
    print(f"[испр. b, сетка] K={Kv} r={rs}: {n} точек {{U<0}}, min λ = {mp.nstr(worst[0],6)} при s/r={worst[1]}, τ̂={worst[2]}, σ̃={worst[3]}", flush=True)
