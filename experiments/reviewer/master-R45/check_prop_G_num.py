"""Численная проверка оценок (i)-(iv) предложения G (notes/prover/2026-10-21-master.md, §4.3).

[Эксперимент] рецензента R45. Случайные струи: Upsilon, DUpsilon, D^2Upsilon (симметрична),
v, D_theta v, S = s d_s v в точке; n = 2..5. Вычисляем точные величины:
  (i)   sup_{w ⟂ Y, |w|=1} |<grad rho - Y/h, w>|  = |nu - Y/h|   (вектор nu - Y/h ⟂ Y);
  (ii)  sup_{|w|=1} |<w, s nabla_Y Y>| = |s nabla_Y Y|   (по (G2));
  (iii) min_{w ⟂ Y, |w|=1} s<w, D_w Y>  (по (G3), векторная форма; (G3) проверена символьно);
  (iv)  h, |Y_T|;
и сравниваем с правыми частями предложения G при наименьших допустимых Lambda, d_2, C_v, m.
Также -- случайный поиск с подъёмом (hill climbing) по отношению LHS/RHS.
"""
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(20261021)


def bilin_norm(T):
    """sup_{|a|=|b|=1} |T(a,b)|, T -- массив n x m x m.
    m = 1: точно; m = 2: сетка по углу a (для фиксированного a максимум по b -- спектральная
    норма матрицы n x 2) с уточнением; m >= 3: попеременный подъём с перезапусками."""
    n, m, _ = T.shape
    if m == 1:
        return np.linalg.norm(T[:, 0, 0]) * (1 + 1e-9)
    if m == 2:
        def g(al):
            a = np.array([np.cos(al), np.sin(al)])
            return np.linalg.norm(np.einsum('kij,i->kj', T, a), 2)
        grid = np.linspace(0, np.pi, 721)
        vals = [g(al) for al in grid]
        i0 = int(np.argmax(vals))
        lo, hi = grid[max(i0 - 1, 0)], grid[min(i0 + 1, len(grid) - 1)]
        for _ in range(60):
            a1, a2 = lo + (hi - lo) / 3, hi - (hi - lo) / 3
            if g(a1) < g(a2):
                lo = a1
            else:
                hi = a2
        return max(max(vals), g(0.5 * (lo + hi))) * (1 + 1e-9)
    best = 0.0
    for _ in range(6):
        a = rng.normal(size=m); a /= np.linalg.norm(a)
        for _ in range(200):
            Ma = np.einsum('kij,i->kj', T, a)          # n x m: b -> T(a,b)
            u, sv, vt = np.linalg.svd(Ma)
            b = vt[0]
            Mb = np.einsum('kij,j->ki', T, b)
            u2, sv2, vt2 = np.linalg.svd(Mb)
            a_new = vt2[0]
            if np.linalg.norm(a_new - a) < 1e-12 or np.linalg.norm(a_new + a) < 1e-12:
                a = a_new
                break
            a = a_new
        Ma = np.einsum('kij,i->kj', T, a)
        best = max(best, np.linalg.norm(Ma, 2))
    # слегка завышаем (оценка сверху надёжнее для проверки неравенств)
    return best * (1 + 1e-9)


def quantities(n, U, DU, D2U, v, Dv, S):
    m = n - 1
    I = np.eye(m)
    B = np.column_stack([U, DU])
    Binv = np.linalg.inv(B)
    nu = Binv.T[:, 0]
    Lam = max(1.0, np.linalg.norm(U), np.linalg.norm(DU, 2), np.linalg.norm(Binv, 2))
    d2 = bilin_norm(D2U)
    Cv = np.linalg.norm(I + Dv, 2) + np.linalg.norm(S)
    G = DU.T @ DU
    Gm12 = np.linalg.inv(np.linalg.cholesky(G))       # L^{-1}, G = L L^T
    Ssym = 0.5 * (G @ (I + Dv) + (G @ (I + Dv)).T)
    lam_min = np.linalg.eigvalsh(Gm12 @ Ssym @ Gm12.T).min()
    mm = max(0.0, -lam_min)
    Y = U + DU @ v
    h = Y @ Y
    UT = U - nu / (nu @ nu)
    YT = Y - nu / (nu @ nu)
    psi = v + Dv @ v + S
    D2vv = np.einsum('kij,i,j->k', D2U, v, v)
    # (i)
    lhs1 = np.linalg.norm(nu - Y / h)
    rhs1 = Lam**2 * np.linalg.norm(YT)
    # (ii)
    lhs2 = np.linalg.norm(DU @ psi + D2vv)
    rhs2 = Lam * np.linalg.norm(psi) + d2 * (v @ v)
    # (iii): M w = s D_w Y = DU((I+Dv) tau + alpha S) + D2U(v, tau), (alpha,tau) = B^{-1} w
    Pa = Binv[0, :]
    Pt = Binv[1:, :]
    D2v_ = np.einsum('kij,i->kj', D2U, v)             # n x m: tau -> D2U(v,tau)
    M = DU @ ((I + Dv) @ Pt + np.outer(S, Pa)) + D2v_ @ Pt
    # базис Y^perp
    Q, _ = np.linalg.qr(np.column_stack([Y / np.sqrt(h), rng.normal(size=(n, n - 1))]))
    Qp = Q[:, 1:]
    Mq = Qp.T @ M @ Qp
    lhs3 = np.linalg.eigvalsh(0.5 * (Mq + Mq.T)).min()
    nYT = np.linalg.norm(YT)
    rhs3 = -(mm * (1 + Lam**3 * nYT)**2 + (Lam**5 + Lam**3) * Cv * nYT + Lam * d2 * np.linalg.norm(v))
    # (iv)
    ok4 = (h >= Lam**-2 * (1 - 1e-12)) and (h <= Lam**2 * (1 + np.linalg.norm(v))**2 * (1 + 1e-12)) \
        and (nYT <= np.linalg.norm(UT) + Lam * np.linalg.norm(v) + 1e-12)
    return dict(r1=lhs1 / max(rhs1, 1e-300), r2=lhs2 / max(rhs2, 1e-300),
                r3=(lhs3 / rhs3 if rhs3 < 0 else (0.0 if lhs3 >= 0 else np.inf)),
                ok1=lhs1 <= rhs1 * (1 + 1e-9) + 1e-12, ok2=lhs2 <= rhs2 * (1 + 1e-9) + 1e-12,
                ok3=lhs3 >= rhs3 * (1 + 1e-9) - 1e-12, ok4=ok4)


def random_jet(n, scale):
    m = n - 1
    U = rng.normal(size=n) * scale[0]
    DU = rng.normal(size=(n, m)) * scale[1]
    D2U = rng.normal(size=(n, m, m)) * scale[2]
    D2U = 0.5 * (D2U + D2U.transpose(0, 2, 1))
    v = rng.normal(size=m) * scale[3]
    Dv = rng.normal(size=(m, m)) * scale[4]
    S = rng.normal(size=m) * scale[5]
    return U, DU, D2U, v, Dv, S


def main():
    viol = 0
    worst = {'r1': 0, 'r2': 0, 'r3': 0}
    N = 0
    for n in (2, 3, 4, 5):
        for trial in range(1500 if n <= 3 else 300):
            scale = 10 ** rng.uniform(-2, 1, size=6)
            jet = random_jet(n, scale)
            B = np.column_stack([jet[0], jet[1]])
            if abs(np.linalg.det(B)) < 1e-6 or np.linalg.cond(jet[1].T @ jet[1]) > 1e10:
                continue
            q = quantities(n, *jet)
            N += 1
            if not (q['ok1'] and q['ok2'] and q['ok3'] and q['ok4']):
                viol += 1
                print('VIOLATION', n, q)
            for key in worst:
                if np.isfinite(q[key]):
                    worst[key] = max(worst[key], q[key])
    print('random trials:', N, 'violations:', viol, 'max ratios LHS/RHS:', worst)

    # подъём по отношению для (iii) и (i): ищем нарушения
    for key in ('r1', 'r2', 'r3'):
        best = 0
        for n in (2, 3):
            m = n - 1
            size = n + n * m + n * m * m + m + m * m + m

            def unpack(x):
                i = 0
                U = x[i:i + n]; i += n
                DU = x[i:i + n * m].reshape(n, m); i += n * m
                D2U = x[i:i + n * m * m].reshape(n, m, m); i += n * m * m
                D2U = 0.5 * (D2U + D2U.transpose(0, 2, 1))
                v = x[i:i + m]; i += m
                Dv = x[i:i + m * m].reshape(m, m); i += m * m
                S = x[i:i + m]
                return U, DU, D2U, v, Dv, S

            def f(x):
                jet = unpack(x)
                B = np.column_stack([jet[0], jet[1]])
                if abs(np.linalg.det(B)) < 1e-4:
                    return 0.0
                try:
                    q = quantities(n, *jet)
                except np.linalg.LinAlgError:
                    return 0.0
                r = q[key]
                return -min(r, 10.0) if np.isfinite(r) else -10.0

            for rs in range(6 if n == 2 else 3):
                x0 = rng.normal(size=size)
                res = minimize(f, x0, method='Nelder-Mead',
                               options=dict(maxiter=1500 if n == 2 else 600,
                                            xatol=1e-8, fatol=1e-10))
                best = max(best, -res.fun)
        print(f'hill-climb max ratio {key}:', best)


if __name__ == '__main__':
    main()
