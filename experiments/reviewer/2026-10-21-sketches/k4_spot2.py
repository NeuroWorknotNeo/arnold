import sys
src = open('k4_spot.py').read().split("r = mp.mpf('1e-48')")[0]
exec(src)
for dps in (300, 500):
    mp.mp.dps = dps
    r = mp.mpf('1e-48'); s = r*mp.mpf('1.15')
    for tt in ('-230', '-1000', '-60', '230'):
        th = mp.pi/2 + mp.mpf(tt)*r**(mp.mpf(1)/3)
        p = cart(s, th, mp.mpf('-7.4e-5')*s**ALPHA)
        U = Uf(*p); rr = mp.sqrt(sum(c*c for c in p))
        l = lam_min(p, rr*mp.mpf(10)**-64) if U < 0 else None
        print(f"dps={dps} t/r^(1/3)={tt}: U<0? {U<0}, λ_min={mp.nstr(l,8) if l is not None else '-'}")
