"""s_check.py -- численная проверка условий теоремы S [013] (S1)-(S3) для B3b (тэкнод с силой по нормали; следствие X' неприменимо:
p_9 + a_0 имеет линейный член по w).
Данные: карта (t, w) на S^2 около omega_0 = (1,0,1)/sqrt2 (y = t, x^2+y^2-z^2 = w), xi = (t, 2w), beta = 9, a0 = 2^{9/2}, p = 1.
W(r,t,w) = r^{-1} p_8 + A + r p_10, A = p_9 + a0 (точное разложение U по формам: u_8, u_9, u_10).
Проверяется на сетках (float64):
  m1(r) = min_{|theta|<=th0} [W - lam0 |theta|^2]   >= -chi(r)                                  (S1)
  m2(r;kappa) = min [ -r dW/dr + kappa xi.grad W - kappa mu0 W ]  >= -chi(r), kappa in {0+, kappa0}   (S2)
  W(r,0) <= chi(r)                                                                               (S3)
с chi(r) = C r^{1/3}; печатается m(r)/r^{1/3} (ограниченность этой величины при r -> 0 и означает существование chi).
Производные -- по цепному правилу из градиентов форм: x_t = -t/x, x_w = 1/(4x), z_w = -1/(4z).
[Эксперимент: численно на сетке, НЕ доказательство]"""
import sys, os, json
import numpy as np
import sympy as sp
from exlist import BY, HERE, x, y, z
from basic import forms


def make(key, mu0):
    fm = forms(BY[key]['U'])
    a0 = 2.0**4.5
    fU = {}
    for k in (8, 9, 10):
        uk = fm[k]
        fU[k] = (sp.lambdify((x, y, z), uk, 'numpy'), [sp.lambdify((x, y, z), sp.diff(uk, v), 'numpy') for v in (x, y, z)])

    def pk(k, T, Wg):
        X_ = np.sqrt((1 + Wg - 2 * T**2) / 2)
        Z_ = np.sqrt((1 - Wg) / 2)
        Xt = -T / X_
        Xw = 1 / (4 * X_)
        Zw = -1 / (4 * Z_)
        f, g = fU[k]
        val = f(X_, T, Z_)
        ux, uy, uz = [gg(X_, T, Z_) for gg in g]
        return val, ux * Xt + uy, ux * Xw + uz * Zw

    def f_W(R, T, Wg):
        p8, _, _ = pk(8, T, Wg)
        p9, _, _ = pk(9, T, Wg)
        p10, _, _ = pk(10, T, Wg)
        return p8 / R + (p9 + a0) + R * p10

    def f_S2(R, K, T, Wg):
        p8, p8t, p8w = pk(8, T, Wg)
        p9, p9t, p9w = pk(9, T, Wg)
        p10, p10t, p10w = pk(10, T, Wg)
        xi8 = T * p8t + 2 * Wg * p8w
        xi9 = T * p9t + 2 * Wg * p9w
        xi10 = T * p10t + 2 * Wg * p10w
        Wv = p8 / R + (p9 + a0) + R * p10
        xiW = xi8 / R + xi9 + R * xi10
        return (p8 / R - R * p10) + K * xiW - K * mu0 * Wv

    return f_W, f_S2


def run(key='f:B3b', th0=0.2, mu0=0.5, kap0=0.1, lam0=5.0):
    f_W, f_S2 = make(key, mu0)
    n = 260
    ts = np.concatenate([-np.logspace(-9, np.log10(th0), n)[::-1], [0.0], np.logspace(-9, np.log10(th0), n)])
    ws_base = np.concatenate([-np.logspace(-12, np.log10(th0), n)[::-1], [0.0], np.logspace(-12, np.log10(th0), n)])
    T, Wg = np.meshgrid(ts, ws_base, indexing='ij')
    out = []
    kaps = (1e-6, kap0)
    for rv in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-8, 1e-10, 1e-12]:
        best1 = (1e9, None)
        best2 = {k_: (1e9, None) for k_ in kaps}
        for fam in (0, 1):                       # w = ws  и  w = -t^2 + ws (вдоль второй ветви тэкнода f2 = w + t^2 = 0)
            Ww = Wg if fam == 0 else Wg - T**2
            ball = (T**2 + Ww**2) <= th0**2
            v1 = np.where(ball, f_W(rv, T, Ww) - lam0 * (T**2 + Ww**2), np.inf)
            idx = np.unravel_index(np.argmin(v1), v1.shape)
            if v1[idx] < best1[0]:
                best1 = (float(v1[idx]), (float(T[idx]), float(Ww[idx])))
            for kap in kaps:
                v2 = np.where(ball, f_S2(rv, kap, T, Ww), np.inf)
                idx = np.unravel_index(np.argmin(v2), v2.shape)
                if v2[idx] < best2[kap][0]:
                    best2[kap] = (float(v2[idx]), (float(T[idx]), float(Ww[idx])))
        w0 = float(f_W(rv, np.array(0.0), np.array(0.0)))
        row = dict(r=rv, m1=best1[0], m1_at=best1[1], m1_over_r13=best1[0] / rv**(1 / 3), W_r0=w0,
                   m2={str(k_): dict(val=v[0], at=v[1], over_r13=v[0] / rv**(1 / 3)) for k_, v in best2.items()})
        out.append(row)
        print(f"r={rv:7.0e}  S1: m1/r^(1/3)={row['m1_over_r13']:9.4f}   S2(k->0)/r^(1/3)={row['m2'][str(kaps[0])]['over_r13']:9.4f}"
              f"  S2(k0)/r^(1/3)={row['m2'][str(kap0)]['over_r13']:9.4f} at {best2[kap0][1]}   S3: W(r,0)={w0:.3e}", flush=True)
    return out


if __name__ == '__main__':
    key = sys.argv[1] if len(sys.argv) > 1 else 'f:B3b'
    res = run(key)
    json.dump(res, open(os.path.join(HERE, 's_check_%s.json' % key.replace(':', '_')), 'w'), indent=1)
