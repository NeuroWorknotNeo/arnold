"""Диагностика: в check_prop_G_num.py поиск Нелдера-Мида по отношению (i) дал 10 (потолок).
Повторяем поиск (n = 2), и каждую точку с отношением > 1 + 1e-6 пересчитываем в повышенной
точности (mpmath, 50 знаков), чтобы отличить нарушение от ошибки округления. [Эксперимент] R45."""
import numpy as np
import mpmath as mp
from scipy.optimize import minimize
import check_prop_G_num as C

mp.mp.dps = 50
rng = np.random.default_rng(1)
import sys
n = int(sys.argv[1]) if len(sys.argv) > 1 else 2
m = n - 1
size = n + n * m + n * m * m + m + m * m + m


def unpack(x):
    i = 0
    U = x[i:i + n]; i += n
    DU = x[i:i + n * m].reshape(n, m); i += n * m
    D2U = x[i:i + n * m * m].reshape(n, m, m); i += n * m * m
    v = x[i:i + m]; i += m
    Dv = x[i:i + m * m].reshape(m, m); i += m * m
    S = x[i:i + m]
    return U, DU, D2U, v, Dv, S


def f(x):
    jet = unpack(x)
    B = np.column_stack([jet[0], jet[1]])
    if abs(np.linalg.det(B)) < 1e-4:
        return 0.0
    q = C.quantities(n, *jet)
    r = q['r1']
    return -min(r, 10.0) if np.isfinite(r) else -10.0


def check_hp(x):
    U, DU, D2U, v, Dv, S = unpack(x)
    B = mp.matrix([[U[i]] + [DU[i, j] for j in range(m)] for i in range(n)])
    Binv = B ** -1
    nu = mp.matrix([Binv[0, i] for i in range(n)])
    Y = mp.matrix([U[i] + sum(DU[i, j] * mp.mpf(v[j]) for j in range(m)) for i in range(n)])
    h = sum(Y[i] ** 2 for i in range(n))
    N2 = sum(nu[i] ** 2 for i in range(n))
    YT = Y - nu / N2
    lhs = mp.sqrt(sum((nu[i] - Y[i] / h) ** 2 for i in range(n)))
    sv = mp.svd_r(Binv, compute_uv=False)
    sD = mp.svd_r(mp.matrix([[DU[i, j] for j in range(m)] for i in range(n)]), compute_uv=False)
    Lam = max(mp.mpf(1), mp.norm(mp.matrix(list(U))), max(sD), max(sv))
    rhs = Lam ** 2 * mp.norm(YT)
    print('   |Y_T| =', mp.nstr(mp.norm(YT), 8), ' lhs =', mp.nstr(lhs, 12), ' rhs =', mp.nstr(rhs, 12),
          ' ratio =', mp.nstr(lhs / rhs if rhs else mp.inf, 12), ' lhs<=rhs:', lhs <= rhs)


cnt = 0
for rs in range(40 if n == 2 else 8):
    res = minimize(f, rng.normal(size=size), method='Nelder-Mead', options=dict(maxiter=1500 if n == 2 else 800))
    if -res.fun > 1 + 1e-6:
        cnt += 1
        print('restart', rs, 'float ratio', -res.fun)
        check_hp(res.x)
print('done; suspicious points:', cnt)
