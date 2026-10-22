"""R46: [Эксперимент] то же, что exit_degenerate_G.py, но минимум ищется оптимизацией
(Нелдер-Мид из 40 случайных стартов) по точкам (A5): параметры (t,e) с calW(t,e)<=delta
(внутренность и граница) и угол phi вектора v_perp в плоскости Y^perp. Не доказательство."""
import sys, random
import mpmath as mp
sys.argv = ['x']
import importlib.util
spec = importlib.util.spec_from_file_location('eg', 'exit_degenerate_G.py')
# переиспользуем символьные функции, не запуская основной цикл
src = open('exit_degenerate_G.py').read().split("rng = random.Random(46)")[0]
ns = {}
exec(compile(src, 'exit_degenerate_G.py', 'exec'), ns)
fXi, fY, calW = ns['fXi'], ns['fY'], ns['calW']
from scipy.optimize import minimize
import numpy as np

def ratio(params, delta, kappa, sval):
    tt, e, phi = [mp.mpf(float(p)) for p in params]
    if calW(tt, e) > delta:
        return 1e3*float(calW(tt, e) - delta) + 1.0
    X = -sval*mp.cos(tt); Yc = -sval*mp.sin(tt); Z = sval**(mp.mpf(5)/4)*e
    Yv = mp.matrix(fY(X, Yc, Z, kappa)); hh = sum(Yv[i]**2 for i in range(3))
    Kp = delta*sval**5 - sval**5*calW(tt, e)
    a1 = mp.matrix([0, 0, 1]); a2 = mp.matrix([-Yv[1], Yv[0], 0]); a2 = a2/mp.sqrt(a2[0]**2+a2[1]**2)
    vp = (mp.cos(phi)*a1 + mp.sin(phi)*a2)*mp.sqrt(2*Kp)
    pp = -mp.sqrt(2*hh*(1-delta)*sval**5); vv = (pp/hh)*Yv + vp; lam = -pp/hh
    return float((sval/lam)*fXi(X, Yc, Z, vv[0], vv[1], vv[2], kappa, delta)/(delta*sval**5))

rng = np.random.default_rng(46)
for delta in (mp.mpf('0.01'), mp.mpf('0.001')):
    R = float(1.2*delta**0.25)
    for kappa in ('1e-3', '1e-2', '3e-2', '0.1'):
        kap = mp.mpf(kappa); sval = mp.mpf('1e-8')
        best = None
        for _ in range(40):
            x0 = [rng.uniform(-R, R), rng.uniform(-R, R), rng.uniform(0, 6.283)]
            r = minimize(ratio, x0, args=(delta, kap, sval), method='Nelder-Mead',
                         options={'maxfev': 300, 'xatol': 1e-6, 'fatol': 1e-10})
            if best is None or r.fun < best.fun: best = r
        print('delta=%s kappa=%s s=1e-8: min ratio=% .4e  (kappa/4=%.2e) at t=%.4f e=%.4f phi=%.3f' % (
            mp.nstr(delta, 2), kappa, best.fun, float(kap)/4, *best.x))
