"""Механизм «отношения 10» в оценке (i): при Y_T -> 0 обе части (i) порядка |Y_T|, и в float64
отношение определяется ошибками округления. Берём v с Y_T = 0 (v = -DUps^+ Ups_T) плюс возмущение eps,
считаем отношение в float64 (check_prop_G_num.quantities) и в mpmath (50 знаков). [Эксперимент] R45."""
import numpy as np
import mpmath as mp
import check_prop_G_num as C

mp.mp.dps = 50
rng = np.random.default_rng(5)
n, m = 3, 2
for trial in range(5):
    U = rng.normal(size=n); DU = rng.normal(size=(n, m))
    D2U = rng.normal(size=(n, m, m)); D2U = 0.5 * (D2U + D2U.transpose(0, 2, 1))
    Dv = rng.normal(size=(m, m)); S = rng.normal(size=m)
    B = np.column_stack([U, DU]); nu = np.linalg.inv(B).T[:, 0]
    UT = U - nu / (nu @ nu)
    v0 = -np.linalg.lstsq(DU, UT, rcond=None)[0]
    for eps in (1e-3, 1e-8, 1e-13, 1e-16, 0.0):
        v = v0 + eps * rng.normal(size=m)
        r_float = C.quantities(n, U, DU, D2U, v, Dv, S)['r1']
        Bm = mp.matrix([[U[i]] + [DU[i, j] for j in range(m)] for i in range(n)])
        Binv = Bm ** -1
        num = mp.matrix([Binv[0, i] for i in range(n)])
        Y = mp.matrix([U[i] + sum(DU[i, j] * mp.mpf(v[j]) for j in range(m)) for i in range(n)])
        h = sum(Y[i] ** 2 for i in range(n)); N2 = sum(num[i] ** 2 for i in range(n))
        YT = Y - num / N2
        lhs = mp.sqrt(sum((num[i] - Y[i] / h) ** 2 for i in range(n)))
        sv = mp.svd_r(Binv, compute_uv=False)
        sD = mp.svd_r(mp.matrix([[DU[i, j] for j in range(m)] for i in range(n)]), compute_uv=False)
        Lam = max(mp.mpf(1), mp.norm(mp.matrix(list(U))), max(sD), max(sv))
        rhs = Lam ** 2 * mp.norm(YT)
        r_mp = lhs / rhs if rhs else mp.nan
        print(f'trial {trial} eps {eps:7.0e}  ratio float64 = {r_float:12.6g}   ratio mp = {mp.nstr(r_mp, 8)}')
