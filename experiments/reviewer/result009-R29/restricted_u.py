"""R29: X2, X4 (неконстантная u) -- min xi log Q только по точкам |b| <= 0.01. [Эксперимент]"""
import mpmath as mp
from construction import EX, b2_grid
for nm in ['X2', 'X4']:
    ex = EX[nm]()
    for N in [1, ex.Nw]:
        mn = mp.inf
        for sgn in (1, -1):
            for kk in range(3, 8):
                b1 = sgn*mp.mpf(10)**(-kk)
                R = ex.rootdata(b1)
                for b2 in b2_grid(b1, R):
                    if mp.sqrt(b1**2 + b2**2) <= mp.mpf('0.01'):
                        mn = min(mn, ex.field(b1, b2, R, N)['xlQ'])
        print("%s N=%d: min xi log Q по |b|<=0.01, |b1|=1e-3..1e-7: %.4f (d=%d, d/4=%.2f)" % (nm, N, float(mn), ex.d, ex.d/4))
