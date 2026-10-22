# [Эксперимент] R48: поле (F2) в складке (0,0) примера O2: X_p = theta d_theta + q(eps) d_eps,
# q = g/g', g(u) = arcsin(u^2); проверка X_p P / P >= k = 1 (P = f^2, f = eps^2 - sin theta) на квадрате.
import numpy as np
def ratio(th, e):
    f = e**2 - np.sin(th)
    q = np.where(e == 0, 0.0, np.arcsin(e**2)*np.sqrt(1 - e**4)/(2*np.where(e == 0, 1, e)))
    XP = 2*f*(th*(-np.cos(th)) + q*2*e)
    return XP/f**2
for r in (0.5, 0.3, 0.1):
    T, E = np.meshgrid(np.linspace(-r, r, 801), np.linspace(-r, r, 801))
    m = np.abs(E**2 - np.sin(T)) > 1e-12
    R = ratio(T[m], E[m])
    print('box r=%.2f: min X_pP/P = %.4f, max = %.4f' % (r, R.min(), R.max()))
