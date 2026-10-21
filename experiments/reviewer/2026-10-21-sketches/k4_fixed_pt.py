# [Эксперимент] исправленная b(u): устойчивость отрицательного λ к шагу и точности; K=1000 около складки σ̃³≈−K/512
import sys
_argv = sys.argv; sys.argv = [sys.argv[0]]
base = open('k4_spot.py').read().split("r = mp.mpf('1e-48')")[0]
def run(Kval, rs, tau_mult, st, sfac='1.15', dps_list=(None,), hexps=(0,)):
    g = {}
    exec(base.replace("Kv = 200", f"Kv = {Kval}"), g)
    mp = g['mp']
    def bfun(t, r):
        u = mp.log(abs(t))/mp.log(r)
        x = (u - mp.mpf('0.05'))/(mp.mpf('0.3') - mp.mpf('0.05'))
        if x <= 0: return mp.mpf(0)
        if x >= 1: return mp.mpf(1)/3
        a = mp.exp(-1/x); b = mp.exp(-1/(1 - x)); return a/(a + b)/3
    g['bfun'] = bfun
    out = []
    for dps in dps_list:
        r = mp.mpf(rs); L = float(-mp.log10(r)); mp.mp.dps = dps or int(150 + 4.5*L)
        tstar = r**(-mp.mpf(1)/30)
        s = r*mp.mpf(sfac); th = mp.pi/2 + mp.mpf(tau_mult)*tstar*r**(mp.mpf(1)/3)
        p = g['cart'](s, th, mp.mpf(st)*r**(mp.mpf(4)/3))
        if g['Uf'](*p) >= 0: out.append('U>=0'); continue
        rr = mp.sqrt(sum(c*c for c in p))
        for he in hexps:
            out.append(mp.nstr(g['lam_min'](p, rr*mp.mpf(10)**-(24 + int(0.8*float(-mp.log10(rr))) + he)), 7))
    return out
print("K=200 r=1e-48 τ̂=100τ̂* σ̃=-0.88, dps (умолч., 500) × шаг (×1, ×1e-4):", run(200, '1e-48', 100, '-0.88', dps_list=(None, 500), hexps=(0, 4)))
for rs in ('1e-64', '1e-96', '1e-128'):
    best = None
    for tm in ('1', '3', '10', '30', '100', '300', '-1', '-10', '-100'):
        for st in ('-1.0', '-1.15', '-1.25', '-1.35', '-1.5'):
            v = run(1000, rs, tm, st)[0]
            if v != 'U>=0' and (best is None or float(v) < best[0]): best = (float(v), tm, st)
    print(f"K=1000 r={rs}: min λ около складки = {best}", flush=True)
