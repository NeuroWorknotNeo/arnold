"""s_check_V.py -- численная проверка условий (S1)-(S3) теоремы S [013] для V1, V2 (изолированный вырожденный нуль u_m в e_x, два подоврага y = z^2, y = z^2 + z^3).
Полярная карта: omega(theta) = c (1, th_y, th_z), c = (1 + |theta|^2)^(-1/2); W(r,theta) = sum_k r^{k-beta} p_k(theta) + a0, p_k = u_k o omega;
V1: m = 10, beta = 12, a0 = 1;  V2: m = 14, beta = 16, a0 = 1.
Поле xi = (3 th_y - th_z^2, th_z): сохраняет ОБА подоврага точно: xi(F1) = 3 F1, xi(F2) = 3 F2, F1 = th_y - th_z^2, F2 = F1 - th_z^3 (проверено sympy).
Проверка (S1) W - lam0 |theta|^{2p} >= -chi(r);  (S2) -r dW/dr + kappa xi.grad W - kappa mu0 W >= -chi(r) при kappa in {0+, kappa0};  (S3) W(r,0) <= chi(r),
chi(r) = C r^{2/9} (V1) / r^{2/13} (V2) (показатели смещения дна из N5); печатается отношение.
[Эксперимент: численно на сетке, НЕ доказательство]"""
import sys, os, json
import numpy as np
import sympy as sp
from exlist import BY, HERE, x, y, z
from basic import forms

ty, tz = sp.symbols('ty tz', real=True)
CFG = {'f:V1': dict(m=10, beta=12, expo=2 / 9.0), 'f:V2': dict(m=14, beta=16, expo=2 / 13.0)}


def make(key, mu0):
    cfg = CFG[key]
    fm = forms(BY[key]['U'])
    c = (1 + ty**2 + tz**2)**sp.Rational(-1, 2)
    sub = {x: c, y: c * ty, z: c * tz}
    ks = sorted(fm)
    p = {k: fm[k].subs(sub, simultaneous=True) for k in ks}
    a0 = -float(p[cfg['beta']].subs({ty: 0, tz: 0}))
    xi = (3 * ty - tz**2, tz)
    # проверка точной инвариантности подоврагов
    F1 = ty - tz**2; F2 = F1 - tz**3
    assert sp.expand(xi[0] * sp.diff(F1, ty) + xi[1] * sp.diff(F1, tz) - 3 * F1) == 0
    assert sp.expand(xi[0] * sp.diff(F2, ty) + xi[1] * sp.diff(F2, tz) - 3 * F2) == 0
    P = {k: sp.lambdify((ty, tz), p[k], 'numpy') for k in ks}
    XP = {k: sp.lambdify((ty, tz), xi[0] * sp.diff(p[k], ty) + xi[1] * sp.diff(p[k], tz), 'numpy') for k in ks}
    beta = cfg['beta']

    def evalW(r, TY, TZ):
        tot = a0
        for k in ks:
            tot = tot + r**(k - beta) * P[k](TY, TZ)
        return tot

    def evalS2(r, kap, TY, TZ):
        W_ = a0; xW = 0.0; mrd = 0.0
        for k in ks:
            c_ = r**(k - beta)
            pk = P[k](TY, TZ)
            W_ = W_ + c_ * pk
            xW = xW + c_ * XP[k](TY, TZ)
            mrd = mrd + (beta - k) * c_ * pk
        return mrd + kap * xW - kap * mu0 * W_

    return a0, evalW, evalS2


def run(key, th0=0.3, mu0=0.5, kap0=0.1, lam0=0.1, pexp=5, rs=(1e-2, 1e-3, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12)):
    a0, evalW, evalS2 = make(key, mu0)
    expo = CFG[key]['expo']
    n = 260
    tzs = np.concatenate([-np.logspace(-13, np.log10(th0), n)[::-1], [0.0], np.logspace(-13, np.log10(th0), n)])
    us = np.concatenate([-np.logspace(-16, np.log10(th0), n)[::-1], [0.0], np.logspace(-16, np.log10(th0), n)])
    TZ, U_ = np.meshgrid(tzs, us, indexing='ij')
    out = []
    for r in rs:
        best1 = 1e9; best2 = {1e-6: 1e9, kap0: 1e9}; at = {}
        for fam in (0, 1):
            TY = TZ**2 + U_ if fam == 0 else TZ**2 + TZ**3 + U_
            ball = (TY**2 + TZ**2) <= th0**2
            W_ = evalW(r, TY, TZ)
            v1 = np.where(ball, W_ - lam0 * (TY**2 + TZ**2)**pexp, np.inf)
            best1 = min(best1, float(v1.min()))
            for kap in best2:
                v2 = np.where(ball, evalS2(r, kap, TY, TZ), np.inf)
                mv = float(v2.min())
                if mv < best2[kap]:
                    best2[kap] = mv
                    idx = np.unravel_index(np.argmin(v2), v2.shape)
                    at[kap] = (float(TY[idx]), float(TZ[idx]))
        w0 = float(evalW(r, np.array(0.0), np.array(0.0)))
        row = dict(r=r, S1_over_r_expo=best1 / r**expo, S2_k0plus_over=best2[1e-6] / r**expo, S2_kappa0_over=best2[kap0] / r**expo, W_r0=w0, S2_at=at.get(kap0))
        out.append(row)
        print(f"{key} r={r:7.0e}  S1: m1/r^{expo:.3f}={row['S1_over_r_expo']:9.4f}   S2(k->0): {row['S2_k0plus_over']:9.4f}   S2(k0={kap0}): {row['S2_kappa0_over']:9.4f} at {at.get(kap0)}   S3: W(r,0)={w0:.2e}", flush=True)
    return dict(key=key, a0=a0, th0=th0, mu0=mu0, kap0=kap0, lam0=lam0, p=pexp, rows=out)


if __name__ == '__main__':
    keys = sys.argv[1:] or ['f:V1', 'f:V2']
    res = {}
    for k in keys:
        res[k] = run(k)
        json.dump(res, open(os.path.join(HERE, 's_check_V_%s.json' % '_'.join(kk.replace(':', '') for kk in keys)), 'w'), indent=1)
