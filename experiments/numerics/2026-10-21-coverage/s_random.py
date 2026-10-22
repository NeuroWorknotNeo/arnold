"""s_random.py -- контроль пробелов сетки в s_check.py / s_check_V.py: случайные точки (seed = 20261022), равномерные по лог-масштабу |t|, |w| (B3b) и |th_y|, |th_z| (V1, V2) и произвольные знаки.
Если случайный минимум ниже сеточного (по отношению к r^expo), это пробел сетки.   [Эксперимент]"""
import sys, numpy as np
import s_check as SB, s_check_V as SV

rng = np.random.default_rng(20261022)

def logu(n, lo, hi):
    return 10 ** rng.uniform(np.log10(lo), np.log10(hi), n) * rng.choice([-1, 1], n)

def b3b(rs=(1e-3, 1e-6, 1e-9), N=400000, th0=0.2, mu0=0.5, kap0=0.1, lam0=5.0):
    f_W, f_S2 = SB.make('f:B3b', mu0)
    for r in rs:
        t = logu(N, 1e-9, th0); w = logu(N, 1e-12, th0)
        t2 = np.concatenate([t, 0.0 * t]); w2 = np.concatenate([w, 0.0 * w])
        ball = (t2**2 + w2**2) <= th0**2
        m1 = np.min(np.where(ball, f_W(r, t2, w2) - lam0 * (t2**2 + w2**2), np.inf))
        m2 = np.min(np.where(ball, f_S2(r, kap0, t2, w2), np.inf))
        # вблизи второй ветви w = -t^2: w = -t^2 + s
        s = logu(N, 1e-14, 1e-1); w3 = -t**2 + s
        ball3 = (t**2 + w3**2) <= th0**2
        m1b = np.min(np.where(ball3, f_W(r, t, w3) - lam0 * (t**2 + w3**2), np.inf))
        m2b = np.min(np.where(ball3, f_S2(r, kap0, t, w3), np.inf))
        print(f"B3b r={r:.0e}: random m1/r^(1/3) = {min(m1, m1b)/r**(1/3):8.3f} (grid -11.9 .. -12.0)   random S2(k0)/r^(1/3) = {min(m2, m2b)/r**(1/3):8.4f} (grid ~ -0.79)", flush=True)

def vgroup(key, rs=(1e-4, 1e-8, 1e-12), N=400000, th0=0.3, mu0=0.5, kap0=0.1, lam0=0.1, pexp=5):
    a0, evalW, evalS2 = SV.make(key, mu0)
    expo = SV.CFG[key]['expo']
    for r in rs:
        tz = logu(N, 1e-13, th0); u = logu(N, 1e-16, th0)
        res = []
        for fam in (0, 1):
            ty = tz**2 + u if fam == 0 else tz**2 + tz**3 + u
            ball = (ty**2 + tz**2) <= th0**2
            m1 = np.min(np.where(ball, evalW(r, ty, tz) - lam0 * (ty**2 + tz**2)**pexp, np.inf))
            m2 = np.min(np.where(ball, evalS2(r, kap0, ty, tz), np.inf))
            res.append((m1, m2))
        # полностью случайные точки шара
        ty = logu(N, 1e-13, th0); tz2 = logu(N, 1e-13, th0)
        ball = (ty**2 + tz2**2) <= th0**2
        m1 = np.min(np.where(ball, evalW(r, ty, tz2) - lam0 * (ty**2 + tz2**2)**pexp, np.inf))
        m2 = np.min(np.where(ball, evalS2(r, kap0, ty, tz2), np.inf))
        res.append((m1, m2))
        print(f"{key} r={r:.0e}: random m1/r^{expo:.3f} = {min(a for a, b in res)/r**expo:8.4f}   random S2(k0)/r^{expo:.3f} = {min(b for a, b in res)/r**expo:8.5f}", flush=True)

if __name__ == '__main__':
    b3b(); vgroup('f:V1'); vgroup('f:V2')
