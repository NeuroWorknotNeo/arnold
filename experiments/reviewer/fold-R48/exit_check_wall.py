# [Эксперимент] R48: уточнённая проверка (A5) для O2 у стенки: K_perp = kappa * delta * rho^6 при малых kappa
# (там перекрёстный член T1+T2 ~ Gamma sqrt(K) соперничает с 6K + mu'), 16 направлений v_perp.
# Использует функции exit_check.py. Запуск: ~/venv/bin/python exit_check_wall.py
import mpmath as mp
import exit_check as ec
mp.mp.dps = 110


def scan_wall(s, mup, delta, kappas, nphi=16):
    worst = (mp.inf, None)
    ths = [mp.mpf(-0.24) + k*(mp.pi + mp.mpf(0.48))/47 for k in range(48)]
    ths += [mp.mpf(t) for t in ('0', '0.02', '-0.02', '0.06', '0.15', '0.3', '0.45', '0.6', '0.75')]
    ths += [mp.pi - t for t in ths[-9:]]
    for th in ths:
        gth = mp.cos(th)**7 + mp.sin(th)**7
        for kap in kappas:
            # W/s^6 = f^2 + s g = delta (1 - kap)  =>  K = kap delta s^6
            f2 = delta*(1 - kap) - s*gth
            if f2 < 0 or f2 > 4*delta:
                continue
            for sf in (1, -1):
                fv = sf*mp.sqrt(f2)
                e2 = mp.sin(th) + fv
                if e2 < 0:
                    continue
                for se in (1, -1):
                    ep = se*mp.sqrt(e2)
                    if ep == 0 and ec.chi(th) < 1:
                        continue
                    for k in range(nphi):
                        r = ec.ratio(s, th, ep, 2*mp.pi*k/nphi, mup, delta)
                        if r < worst[0]:
                            worst = (r, (float(th), float(fv), float(ep), float(kap), k))
    return worst


if __name__ == '__main__':
    kappas = [mp.mpf(t) for t in ('0', '1e-5', '1e-4', '1e-3', '3e-3', '1e-2', '3e-2', '0.1', '0.3')]
    s = mp.mpf('1e-10')
    for delta, mups in ((mp.mpf('0.01'), ('0.002', '0.02', '0.1', '0.4')), (mp.mpf('0.002'), ('0.002', '0.02', '0.1', '0.2', '0.4'))):
        for m in mups:
            w = scan_wall(s, mp.mpf(m), delta, kappas)
            print('delta=%s s=%s mu\'=%s: min = %s at (th,f,eps,kappa,phi#)=%s' % (mp.nstr(delta, 3), mp.nstr(s, 2), m, mp.nstr(w[0], 6), w[1]), flush=True)
