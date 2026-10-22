"""Повтор check_prop_G_num.main() с тем же зерном (тот же расход случайных чисел) и с перехватом
minimize: каждая найденная точка с отношением > 1 + 1e-6 пересчитывается в mpmath (50 знаков);
печатаются |Y_T| и отношение (i) в повышенной точности. [Эксперимент] R45."""
import numpy as np
import mpmath as mp
import check_prop_G_num as C

mp.mp.dps = 50
_orig_min = C.minimize


def hp_r1(n, x):
    m = n - 1
    i = 0
    U = x[i:i + n]; i += n
    DU = x[i:i + n * m].reshape(n, m); i += n * m
    i += n * m * m
    v = x[i:i + m]
    Bm = mp.matrix([[U[a]] + [DU[a, b] for b in range(m)] for a in range(n)])
    Binv = Bm ** -1
    nu = mp.matrix([Binv[0, a] for a in range(n)])
    Y = mp.matrix([U[a] + sum(DU[a, b] * mp.mpf(v[b]) for b in range(m)) for a in range(n)])
    h = sum(Y[a] ** 2 for a in range(n)); N2 = sum(nu[a] ** 2 for a in range(n))
    YT = Y - nu / N2
    lhs = mp.sqrt(sum((nu[a] - Y[a] / h) ** 2 for a in range(n)))
    sv = mp.svd_r(Binv, compute_uv=False)
    sD = mp.svd_r(mp.matrix([[DU[a, b] for b in range(m)] for a in range(n)]), compute_uv=False)
    Lam = max(mp.mpf(1), mp.norm(mp.matrix(list(U))), max(sD), max(sv))
    rhs = Lam ** 2 * mp.norm(YT)
    return mp.norm(YT), (lhs / rhs if rhs else mp.inf)


def wrapped(f, x0, **kw):
    res = _orig_min(f, x0, **kw)
    if -res.fun > 1 + 1e-6:
        n = 2 if len(x0) == 2 + 2 + 2 + 1 + 1 + 1 else 3
        nYT, r = hp_r1(n, res.x)
        print(f'  suspicious: n={n} float ratio={-res.fun:.6g}  |Y_T|(mp)={mp.nstr(nYT, 6)}  '
              f'ratio (i) mp={mp.nstr(r, 10)}', flush=True)
    return res


C.minimize = wrapped
C.main()
