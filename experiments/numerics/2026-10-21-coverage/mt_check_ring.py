"""mt_check_ring.py -- УСЛОВНАЯ проверка (теорема MT [015] не принята!) статических условий (MT1) для D1-D4: кольцо G = const на C1 с узлами касания C2.
Полярная калибровка (P) [015], все направления конические (I_n = пусто, (MT3b) тривиально), карта (phi, w) на S^2 \\ {полюса}:
  omega = (rho cos(phi), rho sin(phi), z), rho = sqrt((1+w)/2), z = sqrt((1-w)/2), w = x^2+y^2-z^2  (C1 = {w=0}), окно K = {|w| < w0}.
Данные: beta = 9, a0 = -p_9|_{C1}, W(r,phi,w) = r^{-9} U(r omega) + a0 = sum_k r^{k-9} p_k + a0; mu_1 = 0, mu_0 = m, mu(kappa) = kappa m.
Поле xi = (xi^phi, xi^w): xi^w = 2w; xi^phi = chi(phi) cot(phi) (2 w rho'/rho - 1), где chi = 1 при |cos phi| <= 0.8 (вдоль всей части C2 с w <= w0), 0 около x = max.
Вблизи узлов в координатах (x, w): xi = x d_x + 2 w d_w, f1 = w, f2 = w - x^2/2 (точно: f1 - f2 = x^2/2) => xi(f2) = 2 f2, xi(p_8) = 8 p_8 (точно).
Проверяется на сетках:
  (W) W > delta на |w| = w0;
  (F) W >= -chi(r) на K;
  (B) min_K W <= chi(r);
  (E) для kappa in {1e-6, kappa0}: min_{W <= delta} [ -r dW/dr + kappa xi.grad W - kappa m (W - eps_b delta) ] >= -chi(r),   chi(r) = C r^{1/3} (печатается отношение).
[Эксперимент: численно, условный: даже если всё выполнено, это проверка условий НЕпринятой теоремы MT]"""
import sys, os, json
import numpy as np
import sympy as sp
from exlist import BY, HERE, x, y, z
from basic import forms

ph, w = sp.symbols('phi w', real=True)
rho = sp.sqrt((1 + w) / 2)
zz = sp.sqrt((1 - w) / 2)


def build(key):
    fm = forms(BY[key]['U'])
    sub = {x: rho * sp.cos(ph), y: rho * sp.sin(ph), z: zz}
    degs = sorted(k for k in fm if k >= 8)
    p = {k: fm[k].subs(sub, simultaneous=True) for k in degs}
    return p


def cutoff(c):
    """гладкая ступенька по |cos phi|: 1 при |cos|<=0.8, 0 при |cos|>=0.95 (там C2 вне окна: w = x^2/2 > w0)"""
    u = np.clip((np.abs(c) - 0.8) / 0.15, 0, 1)
    return 1 - u * u * u * (10 - 15 * u + 6 * u * u)


def make(key, mu_m):
    p = build(key)
    a0 = float(-p[9].subs({ph: 0.3, w: 0}))
    # проверка G = const на кольце: p_9(phi, 0) не зависит от phi
    chk = [float(p[9].subs({ph: v, w: 0})) for v in (0.1, 0.9, 2.0, 4.0)]
    assert max(chk) - min(chk) < 1e-12, chk
    degs = sorted(p)
    P = {k: sp.lambdify((ph, w), p[k], 'numpy') for k in degs}
    Pphi = {k: sp.lambdify((ph, w), sp.diff(p[k], ph), 'numpy') for k in degs}
    Pw = {k: sp.lambdify((ph, w), sp.diff(p[k], w), 'numpy') for k in degs}
    rho_f = lambda W_: np.sqrt((1 + W_) / 2)
    drho = lambda W_: 1 / (4 * rho_f(W_))

    def xi(Ph, Wg):
        c = np.cos(Ph); s_ = np.sin(Ph)
        with np.errstate(divide='ignore', invalid='ignore'):
            xp = cutoff(c) * (c / s_) * (2 * Wg * drho(Wg) / rho_f(Wg) - 1)
        xp = np.where(np.abs(s_) < 1e-9, 0.0, xp)
        return xp, 2 * Wg

    def evalW(rv, Ph, Wg):
        tot = 0.0
        for k in degs:
            val = P[k](Ph, Wg) * np.ones_like(Ph)
            tot = tot + (rv**(k - 9)) * val
        return tot + a0

    def eval_all(rv, kap, Ph, Wg, delta, epsb):
        W_ = 0.0; Wph = 0.0; Ww = 0.0; mrd = 0.0
        for k in degs:
            pk = P[k](Ph, Wg) * np.ones_like(Ph)
            c_ = rv**(k - 9)
            W_ = W_ + c_ * pk
            Wph = Wph + c_ * Pphi[k](Ph, Wg)
            Ww = Ww + c_ * Pw[k](Ph, Wg)
            mrd = mrd - (k - 9) * c_ * pk                # -r dW/dr
        W_ = W_ + a0
        xp, xw = xi(Ph, Wg)
        E = mrd + kap * (xp * Wph + xw * Ww) - kap * mu_m * (W_ - epsb * delta)
        return W_, E

    return a0, evalW, eval_all


def grids(w0, n=300):
    # phi: плотно около узлов pi/2, 3pi/2 (x = rho cos phi, малые) + равномерно
    base = np.linspace(0, 2 * np.pi, 361)
    near = []
    for c0 in (np.pi / 2, 3 * np.pi / 2):
        near.append(c0 + np.concatenate([-np.logspace(-9, np.log10(0.6), n // 2)[::-1], [0.0], np.logspace(-9, np.log10(0.6), n // 2)]))
    phis = np.unique(np.concatenate([base] + near))
    ws = np.concatenate([-np.logspace(-12, np.log10(w0), n)[::-1], [0.0], np.logspace(-12, np.log10(w0), n)])
    return phis, ws


def run(key, w0, delta, mu_m=0.5, kap0=0.1, epsb=0.2, rs=(1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-8, 1e-10), chunk=40):
    a0, evalW, eval_all = make(key, mu_m)
    phis, ws = grids(w0)
    out = []
    for rv in rs:
        minF = 1e9; minE = {1e-6: 1e9, kap0: 1e9}; minB = 1e9; where = {}
        # семейства w: w = ws и w = x^2/2 + ws_small (вдоль C2: f2 = 0)
        for i0 in range(0, len(phis), chunk):
            Ph = phis[i0:i0 + chunk][:, None] * np.ones((1, len(ws)))
            for fam in (0, 1):
                if fam == 0:
                    Wg = np.ones((Ph.shape[0], 1)) * ws[None, :]
                else:
                    xx = np.sqrt((1 + 0) / 2) * np.cos(Ph)                # приближённо x на кольце
                    Wg = xx**2 / 2 + np.ones((Ph.shape[0], 1)) * ws[None, :]
                mask = np.abs(Wg) <= w0
                W_ = evalW(rv, Ph, Wg)
                minF = min(minF, float(np.min(np.where(mask, W_, np.inf))))
                minB = min(minB, float(np.min(np.where(mask, W_, np.inf))))
                for kap in minE:
                    W2, E = eval_all(rv, kap, Ph, Wg, delta, epsb)
                    sel = mask & (W2 <= delta)
                    v = np.where(sel, E, np.inf)
                    mv = float(np.min(v))
                    if mv < minE[kap]:
                        minE[kap] = mv
                        idx = np.unravel_index(np.argmin(v), v.shape)
                        where[kap] = (float(Ph[idx]), float(Wg[idx]))
        # стенки
        wallmin = 1e9
        for wv in (w0, -w0):
            Wp = evalW(rv, phis, np.full_like(phis, wv))
            wallmin = min(wallmin, float(Wp.min()))
        row = dict(r=rv, minW=minF, minW_over_r13=minF / rv**(1 / 3), wall_min=wallmin,
                   E={str(k_): dict(val=v_, over_r13=v_ / rv**(1 / 3), at=where.get(k_)) for k_, v_ in minE.items()})
        out.append(row)
        print(f"{key} r={rv:7.0e}  (F) minW/r^(1/3)={row['minW_over_r13']:8.3f}  (W) min_wall={wallmin:.4f} (delta={delta})  (E)k->0: {row['E'][str(1e-6)]['over_r13']:8.3f}  (E)k0: {row['E'][str(kap0)]['over_r13']:8.3f} at {where.get(kap0)}", flush=True)
    return dict(key=key, a0=a0, w0=w0, delta=delta, mu_m=mu_m, kap0=kap0, epsb=epsb, rows=out)


if __name__ == '__main__':
    keys = sys.argv[1:] or ['f:D1', 'f:D2', 'f:D3', 'f:D4']
    res = {}
    for k in keys:
        a0, _, _ = make(k, 0.5)
        # выбор w0 и delta: A(w0) = a0 - z(w0)... > delta на стенке
        w0, delta = (0.2, 0.2 * a0) if k in ('f:D1', 'f:D2') else (0.12, 1e-4)
        res[k] = run(k, w0, delta)
        json.dump(res, open(os.path.join(HERE, 'mt_check_ring.json'), 'w'), indent=1)
