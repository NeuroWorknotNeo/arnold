# R38: recheck the sigma=1e-9 worst point with higher precision (is 0.19632 < 2e real or roundoff?)
import mpmath as mp, exit_check as ec
for dps in [60, 120, 200]:
    mp.mp.dps = dps
    ec.e = mp.mpf('0.1'); ec.mode = 'F'
    w, a4 = ec.sample(mp.mpf('0.01'), mp.mpf('1e-9'), 300, 7)
    print(dps, mp.nstr(w[0], 12), w[1:])
