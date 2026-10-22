# [Эксперимент] R48: то же, что exit_check_wall.py, при теоретическом mu' = 12 delta / C_M^2 (предложение O2, п. 6).
import mpmath as mp
import exit_check as ec
import exit_check_wall as ew
mp.mp.dps = 110
kappas = [mp.mpf(t) for t in ('0', '1e-6', '1e-5', '1e-4', '1e-3', '1e-2', '0.1')]
for delta in (mp.mpf('0.01'), mp.mpf('0.002')):
    mth = 12*delta/ec.CM**2
    for s in (mp.mpf('1e-10'), mp.mpf('1e-16')):
        w = ew.scan_wall(s, mth, delta, kappas)
        print('delta=%s s=%s mu\'=%s: min = %s (min/mu\' = %s) at %s' % (mp.nstr(delta, 3), mp.nstr(s, 2), mp.nstr(mth, 4), mp.nstr(w[0], 6), mp.nstr(w[0]/mth, 6), w[1]), flush=True)
