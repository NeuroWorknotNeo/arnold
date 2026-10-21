# [Эксперимент] то же поле (ход 5), y-вар. K=200: сетка в координатах лучевой трубки τ̂=t/r^{1/3}, σ̃=σ/r^{4/3}
src = open('k4_spot.py').read().split("r = mp.mpf('1e-48')")[0]
exec(src)
import sys
for rs, dps in (('1e-24', 200), ('1e-48', 300), ('1e-64', 350), ('1e-96', 450), ('1e-128', 600)):
    mp.mp.dps = dps
    r = mp.mpf(rs); worst = None; n = 0
    for sfac in ('0.85', '1.15'):
        s = r*mp.mpf(sfac)
        for tau in ('-1000', '-230', '-60', '-10', '10', '60', '230', '1000'):
            for st in ('-2', '-0.88', '-0.3', '-0.05', '0.05', '0.3', '0.88', '2'):
                th = mp.pi/2 + mp.mpf(tau)*r**(mp.mpf(1)/3)
                p = cart(s, th, mp.mpf(st)*r**(mp.mpf(4)/3))
                if Uf(*p) >= 0: continue
                n += 1
                rr = mp.sqrt(sum(c*c for c in p))
                l = lam_min(p, rr*mp.mpf(10)**-(24 + int(0.8*float(-mp.log10(rr)))))
                if worst is None or l < worst[0]: worst = (l, sfac, tau, st)
    print(f"r={rs}: {n} точек {{U<0}}, min λ = {mp.nstr(worst[0],6)} при s/r={worst[1]}, τ̂={worst[2]}, σ̃={worst[3]}", flush=True)
