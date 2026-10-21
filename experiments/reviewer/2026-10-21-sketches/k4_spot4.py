# [Эксперимент] то же поле: переходная зона u∈[0.05,0.3] около конца (τ̂ ~ r^{-1/30}) на малых r
src = open('k4_spot.py').read().split("r = mp.mpf('1e-48')")[0]
exec(src)
for rs, dps in (('1e-96', 450), ('1e-128', 600), ('1e-192', 850)):
    mp.mp.dps = dps
    r = mp.mpf(rs); worst = None; n = 0
    tstar = r**(-mp.mpf(1)/30)
    for sfac in ('0.85', '1.15'):
        s = r*mp.mpf(sfac)
        for tf in ('0.5', '0.9', '1.5', '3', '10', '100'):
            for sg_t in (1, -1):
                tau = sg_t*mp.mpf(tf)*tstar
                for st in ('-8', '-4', '-2', '-0.88', '-0.3', '-0.05', '0.05', '0.3', '0.88', '2', '4', '8'):
                    th = mp.pi/2 + tau*r**(mp.mpf(1)/3)
                    p = cart(s, th, mp.mpf(st)*r**(mp.mpf(4)/3))
                    if Uf(*p) >= 0: continue
                    n += 1
                    rr = mp.sqrt(sum(c*c for c in p))
                    l = lam_min(p, rr*mp.mpf(10)**-(24 + int(0.8*float(-mp.log10(rr)))))
                    if worst is None or l < worst[0]: worst = (l, sfac, mp.nstr(tau, 4), st)
    print(f"r={rs} (τ̂*={mp.nstr(tstar,4)}): {n} точек {{U<0}}, min λ = {mp.nstr(worst[0],6)} при s/r={worst[1]}, τ̂={worst[2]}, σ̃={worst[3]}", flush=True)
