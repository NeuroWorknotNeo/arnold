"""[Эксперимент] Проверка предложения 1(б) results/004-lemmaR.md (prover, 21.10.2026).

Вопрос: если omega инъективно на K~_0, то Phi инъективно на (0, rho) x K~ при малом rho,
причём без малости K~ по y_{>=1}. Ключевая оценка доказательства ("градуированная теорема о
среднем"): |Phi(p') - Phi(p)| >= c |S(r)(p' - p)| для p, p' в (0, rho) x K~ с c > 0.
Здесь численно оценивается inf отношения
    ratio(p, p') = |Phi(p') - Phi(p)| / |S(r) (p' - p)|,   S(r) = diag(1, r, r^{3/2}).
Карта: n = 3, s = 1 (угол theta), k = 1, c_1 = 1, w_1 = 3/2, N = 2, a_1 = 1, eps = r^{1/2},
  G(th, mu, eps) = (cos th, sin th, 0) + mu (0,0,1) + mu^2 (0.3 cos th, 0.2, -0.5)
                 + eps (0.2 sin th, 0.1, 0.3) + eps mu (0.25, -0.1 cos th, 0.4) + mu^3 (0.1, 0, 0.2 sin th),
  Phi(r, th, y) = r G(th, eps y, eps).  (O): D_mu G(th,0,0) = (0,0,1) _|_ omega, omega'.
  K~ = [-1, 1] x [-4, 4]  (по y -- "широкий" компакт), omega инъективно на [-1, 1].
Метод: numpy, double; seed 20261021; на каждом r: 200000 случайных пар трёх типов
  (равномерные с r' in [r/2, 2r]; "опасные" близкие по (r, theta) и далёкие по y;
  близкие пары), затем Nelder--Mead (scipy) из 30 худших пар с проекцией на K~.
Ожидание по доказательству: min ratio отделён от нуля при малых r. При r = 0.1 (eps = 0.32,
  |mu| <= 1.26) карта складывается по y (D_y Phi_3 меняет знак), и min ratio -> 0:
  это иллюстрирует, что rho_Phi зависит от R_K, хотя малость R_K не требуется.
Запуск: ~/venv/bin/python check_injectivity.py
Это не доказательство: конечная выборка, одна карта.
"""
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(20261021)
TH, YM = 1.0, 4.0


def Phi(r, th, y):
    eps = np.sqrt(r)
    mu = eps * y
    c, s = np.cos(th), np.sin(th)
    g1 = c + mu**2 * 0.3 * c + eps * 0.2 * s + eps * mu * 0.25 + mu**3 * 0.1
    g2 = s + mu**2 * 0.2 + eps * 0.1 - eps * mu * 0.1 * c
    g3 = mu - 0.5 * mu**2 + eps * 0.3 + eps * mu * 0.4 + mu**3 * 0.2 * s
    return np.asarray(r)[..., None] * np.stack([g1, g2, g3], axis=-1)


def ratio(r, th, y, r2, th2, y2):
    num = np.linalg.norm(Phi(r2, th2, y2) - Phi(r, th, y), axis=-1)
    den = np.sqrt((r2 - r)**2 + (r * (th2 - th))**2 + (r**1.5 * (y2 - y))**2)
    return num / den


def sample(r, m):
    out = []
    # (1) uniform pairs
    th, y = rng.uniform(-TH, TH, m), rng.uniform(-YM, YM, m)
    r2 = r * np.exp(rng.uniform(np.log(0.5), np.log(2), m))
    th2, y2 = rng.uniform(-TH, TH, m), rng.uniform(-YM, YM, m)
    out.append((np.full(m, r), th, y, r2, th2, y2))
    # (2) dangerous: close in (r, theta) at scale eps, far in y
    eps = np.sqrt(r)
    th, y = rng.uniform(-TH, TH, m), rng.uniform(-YM, YM, m)
    r2 = r * (1 + eps * rng.uniform(-2, 2, m))
    th2 = np.clip(th + eps * rng.uniform(-2, 2, m), -TH, TH)
    y2 = rng.uniform(-YM, YM, m)
    out.append((np.full(m, r), th, y, r2, th2, y2))
    # (3) close pairs
    th, y = rng.uniform(-TH, TH, m), rng.uniform(-YM, YM, m)
    h = 10.0**rng.uniform(-6, -1, m)
    r2 = r * (1 + h * rng.uniform(-1, 1, m))
    th2 = np.clip(th + h * rng.uniform(-1, 1, m), -TH, TH)
    y2 = np.clip(y + h * rng.uniform(-1, 1, m) / eps, -YM, YM)
    out.append((np.full(m, r), th, y, r2, th2, y2))
    return [np.concatenate(z) for z in zip(*out)]


def refine(r, start):
    def f(v):
        th, y, lr2, th2, y2 = v
        th, th2 = np.clip(th, -TH, TH), np.clip(th2, -TH, TH)
        y, y2 = np.clip(y, -YM, YM), np.clip(y2, -YM, YM)
        r2 = r * np.exp(np.clip(lr2, np.log(0.5), np.log(2)))
        if abs(r2 - r) + abs(th2 - th) + abs(y2 - y) < 1e-12:
            return 1e3
        return float(ratio(r, th, y, r2, th2, y2))
    res = minimize(f, start, method='Nelder-Mead', options={'xatol': 1e-12, 'fatol': 1e-14, 'maxiter': 4000})
    return res.fun


for r in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
    R, th, y, r2, th2, y2 = sample(r, 200000 // 3)
    q = ratio(R, th, y, r2, th2, y2)
    order = np.argsort(q)[:30]
    best = q[order[0]]
    for i in order:
        st = [th[i], y[i], np.log(r2[i] / r), th2[i], y2[i]]
        best = min(best, refine(r, st))
    print(f"r={r:.0e}: min ratio over samples = {q.min():.4f}, after Nelder-Mead = {best:.4f}")
