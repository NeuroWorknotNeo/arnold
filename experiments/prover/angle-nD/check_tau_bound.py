# [Эксперимент] Проверка оценки предложения 4' на случайных данных:
#   Q(xi) >= |xi|^2 (cos t - eps(1+t) - lam(1+t) - 2 t^2 |S_+| - t |K|),
# где Q -- форма из предложения 4' (точное выражение), N = S + K = nabla^S sigma.
# Касательное пространство T_omega S^{n-1} отождествляем с R^{n-1}; размерность m = n-1.
import numpy as np
rng = np.random.default_rng(0)
def sinc(t): return np.sin(t)/t
def sincp(t): return (t*np.cos(t)-np.sin(t))/t**2
import mpmath as mp
mp.mp.dps = 50
mx = max(abs((t*mp.cos(t)-mp.sin(t))/t**2)/(t/3) for t in [mp.mpf(k)/10000 for k in range(1, 10001)])
print("max_{0<t<=1} |sinc'(t)|/(t/3) (mpmath, 50 знаков) =", mp.nstr(mx, 12))
worst = np.inf
for trial in range(200000):
    m = rng.integers(1, 4)              # n = 2,3,4
    t = rng.uniform(1e-4, 1.0)
    tau = rng.normal(size=m); tau *= t/np.linalg.norm(tau); th = tau/t
    taur = rng.normal(size=m)*rng.uniform(0, 0.5)
    S = rng.normal(size=(m,m)); S = (S+S.T)/2*rng.uniform(0, 30)
    K = rng.normal(size=(m,m)); K = (K-K.T)/2*rng.uniform(0, 3)
    N = S + K
    xr = rng.normal(); xt = rng.normal(size=m)
    Nx = N@xt
    Q = (xr**2*(np.cos(t) - np.sin(t)*th@taur) + xr*sinc(t)*(xt@taur)
         + xr*sincp(t)*(th@taur)*(xt@tau) + np.cos(t)*(xt@xt)
         - xr*np.sin(t)*(th@Nx) + sinc(t)*(xt@Nx) + sincp(t)*(th@Nx)*(xt@tau))
    ev = np.linalg.eigvalsh(S)
    Sp = max(ev.max(), 0.0); lam = max(-ev.min(), 0.0)
    eps = np.linalg.norm(taur); Kn = np.linalg.norm(K, 2)
    bound = (np.cos(t) - eps*(1+t) - lam*(1+t) - 2*t**2*Sp - t*Kn)*(xr**2 + xt@xt)
    worst = min(worst, Q - bound)
print("min (Q - bound) over 200000 random trials:", worst, "(>= 0 ожидается)")
