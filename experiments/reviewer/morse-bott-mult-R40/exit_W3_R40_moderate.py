# R40: (A5) for W3 at moderate s, interior and boundary minima reported separately [Experiment]
import sys
sys.argv = sys.argv[:1]
import mpmath as mp
import exit_W3_R40 as X

def scan_split(S, D_, K_, L_, nray=64, ngrid=9, nphi=16):
    bd = mp.inf; it = mp.inf
    for k in range(nray):
        t, e = X.boundary_point(S, D_, 2*mp.pi*k/nray)
        res = X.exit_value(S, t, e, K_, L_, D_, 0)
        if res: bd = min(bd, res[0])
    Tm = 1.3*mp.sqrt(4*D_/3); Em = 1.2*(16*D_/3)**mp.mpf(0.25)
    for i in range(-ngrid, ngrid+1):
        for j in range(-ngrid, ngrid+1):
            t = Tm*i/ngrid; e = Em*j/ngrid
            if X.Pf(t, e) >= 4*D_ or X.Ftil_plus_a0(S, t, e) > D_:
                continue
            for kph in range(nphi):
                res = X.exit_value(S, t, e, K_, L_, D_, 2*mp.pi*kph/nphi)
                if res: it = min(it, res[0])
    return bd, it

D_ = mp.mpf('1e-5')
CM = 15*mp.sqrt(3)/8*6 + 4
Rt = mp.asin(mp.sqrt(16*D_/3))
kd = 6*D_/(2*CM**2*Rt**2)
print("delta=1e-5, kappa(delta)=", mp.nstr(kd, 5))
for S in [mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4'), mp.mpf('1e-6')]:
    for name, L_ in [("W (lam=c-kappa/2)", X.c - kd/2), ("Mb (lam=0)", mp.mpf(0))]:
        bd, it = scan_split(S, D_, kd, L_)
        print(f"  s={mp.nstr(S,2):6s} {name:18s} boundary min = {mp.nstr(bd,6):>12s}   interior min = {mp.nstr(it,6):>12s}")
        sys.stdout.flush()
