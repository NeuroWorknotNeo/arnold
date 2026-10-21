import sympy as sp, mpmath as mp, numpy as np
exec(open('ex13_cross.py').read().split('for bv in')[0])
# 1) ограничимся точками {U<0}
bv = mp.mpf('0.1')
for sv in (mp.mpf('1e-3'), mp.mpf('1e-4'), mp.mpf('1e-5')):
    worst = mp.inf; cnt = 0
    for phi in np.linspace(1.85, 3.58, 30):
        for eta in np.linspace(-0.15, 0.15, 13):
            p = pt(sv, mp.mpf(phi), mp.mpf(eta))
            if Uf(*p, bv) >= 0: continue
            cnt += 1
            M = mp.matrix(Jf(*p, bv)); S = (M + M.T)/2
            worst = min(worst, min(mp.eigsy(S)[0]))
    print(f"b=0.1 s={mp.nstr(sv,3)}: {cnt} точек в {{U<0}}, min λ(Sym DV) = {mp.nstr(worst,6)}")
# 2) (Reg) с угловым блоком для F_b = 4η² + (b/√2)cosφ·η + G/8
ph = np.linspace(0, 2*np.pi, 200001)
G = np.cos(ph)*(1+np.sin(ph)) + 0.5; Gp = 1 - np.sin(ph) - 2*np.sin(ph)**2
bb = 0.1
best = np.inf
for eta in np.linspace(-0.3, 0.3, 1201):
    F = 4*eta**2 + bb/np.sqrt(2)*np.cos(ph)*eta + G/8
    Fe = 8*eta + bb/np.sqrt(2)*np.cos(ph); Fp = -bb/np.sqrt(2)*np.sin(ph)*eta + Gp/8
    best = min(best, np.min(F**2 + Fe**2 + Fp**2))
print("min (F² + F_η² + F_φ²) по сетке:", best)
