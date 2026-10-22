"""R49: численная проверка предложения G (results/015-master.md), [Эксперимент].

Случайные струи (Upsilon, DUpsilon, D2Upsilon в точке; v, D_th v, d_s v), n = 2..5.
Величины D_q Y, grad rho считаются через D Pi^{-1} (как в check_G_sym.py), а не через формулы леммы G.
Константы: Lambda = max(1,|U|,||DU||,||B^{-1}||); d2 = sqrt(sum_i ||D2U_i||^2) >= ||D2U||;
C_v = ||I+Dv|| + |s d_s v|; m = max(0, -lambda_min(G^{-1/2} sym(G(I+Dv)) G^{-1/2})).
Проверяются (i)-(iv) для случайных w ⟂ Y. Ищем нарушения; плюс «экстремальные» w (собственные
векторы) для (iii).
"""
import numpy as np

rng = np.random.default_rng(20261022)


def trial(n, scale_v):
    m = n - 1
    U0 = rng.normal(size=n)
    U1 = rng.normal(size=(n, m))
    U2 = rng.normal(size=(n, m, m)) * rng.uniform(0, 2)
    U2 = 0.5 * (U2 + U2.transpose(0, 2, 1))
    B = np.column_stack([U0, U1])
    if abs(np.linalg.det(B)) < 1e-3:
        return None
    s = rng.uniform(0.01, 2)
    v0 = rng.normal(size=m) * scale_v
    V1 = rng.normal(size=(m, m)) * rng.uniform(0, 2)
    vs = rng.normal(size=m) * rng.uniform(0, 2)
    # Dy w.r.t. (s, th):  d_s y = U1 vs ; d_th_j y = U1[:,j] + U2[:,j,:] v0 + U1 V1[:,j]
    Dy = np.zeros((n, n))
    Dy[:, 0] = U1 @ vs
    for j in range(m):
        Dy[:, 1 + j] = U1[:, j] + U2[:, j, :] @ v0 + U1 @ V1[:, j]
    DPi = np.column_stack([U0, s * U1])
    DPinv = np.linalg.inv(DPi)
    DqY = Dy @ DPinv
    grad = DPinv[0, :]
    Y = U0 + U1 @ v0
    h = Y @ Y
    nu = np.linalg.inv(B).T @ np.eye(n)[0]
    YT = Y - nu / (nu @ nu)
    Lam = max(1, np.linalg.norm(U0), np.linalg.norm(U1, 2), np.linalg.norm(np.linalg.inv(B), 2))
    d2 = np.sqrt(sum(np.linalg.norm(U2[i], 2) ** 2 for i in range(n)))
    Cv = np.linalg.norm(np.eye(m) + V1, 2) + np.linalg.norm(s * vs)
    G = U1.T @ U1
    Sm = G @ (np.eye(m) + V1)
    Sm = 0.5 * (Sm + Sm.T)
    L = np.linalg.cholesky(G)
    Li = np.linalg.inv(L)
    mm = max(0.0, -np.linalg.eigvalsh(Li @ Sm @ Li.T).min())
    psi = v0 + V1 @ v0 + s * vs
    viol = []
    # (iv)
    if not (Lam ** -2 <= h * (1 + 1e-12) and h <= Lam ** 2 * (1 + np.linalg.norm(v0)) ** 2 * (1 + 1e-12)):
        viol.append('iv-h')
    if np.linalg.norm(YT) > np.linalg.norm(nu * 0 + (U0 - nu / (nu @ nu))) + Lam * np.linalg.norm(v0) + 1e-12:
        viol.append('iv-YT')
    # basis of Y^perp
    Q, _ = np.linalg.qr(np.column_stack([Y, rng.normal(size=(n, n - 1))]))
    P = Q[:, 1:]
    ws = [P @ rng.normal(size=n - 1) for _ in range(40)]
    # extremal w for (iii): eigenvectors of sym(P^T s D_qY P)
    M3 = P.T @ (s * DqY) @ P
    M3 = 0.5 * (M3 + M3.T)
    ev, evec = np.linalg.eigh(M3)
    ws += [P @ evec[:, i] for i in range(n - 1)]
    worst = []
    for w in ws:
        nw = np.linalg.norm(w)
        a = abs((grad - Y / h) @ w)
        if a > Lam ** 2 * np.linalg.norm(YT) * nw * (1 + 1e-9) + 1e-12:
            viol.append('i')
        b = abs(w @ (s * DqY @ Y))
        if b > (Lam * np.linalg.norm(psi) + d2 * np.linalg.norm(v0) ** 2) * nw * (1 + 1e-9) + 1e-12:
            viol.append('ii')
        c = s * (w @ DqY @ w)
        bound = -(mm * (1 + Lam ** 3 * np.linalg.norm(YT)) ** 2 + (Lam ** 5 + Lam ** 3) * Cv * np.linalg.norm(YT)
                  + Lam * d2 * np.linalg.norm(v0)) * nw ** 2
        if c < bound * (1 + 1e-9) - 1e-12:
            viol.append('iii')
        worst.append(c / bound if bound < 0 else 0)
    return viol, max(worst) if worst else 0


if __name__ == '__main__':
    tot = 0
    bad = 0
    ratios = []
    for n in (2, 3, 4, 5):
        for scale_v in (0.0, 0.1, 1.0):
            for _ in range(400):
                r = trial(n, scale_v)
                if r is None:
                    continue
                viol, wr = r
                tot += 1
                ratios.append(wr)
                if viol:
                    bad += 1
                    print('violation', n, scale_v, viol)
    print('trials:', tot, 'with violations:', bad)
    print('max ratio (actual lower value)/(bound) in (iii):', max(ratios))
