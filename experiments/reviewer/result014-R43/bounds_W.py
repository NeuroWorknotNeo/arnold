"""R43: случайная проверка поточечных оценок п. 7 §3.2 results/014 (теорема W).  [Эксперимент]

Независимые величины (в точке): eps, s*d_s eps, d_th eps, eta0s=eta_{0,s}, e0t=eta_{0,theta}/s,
nut=nu~, dtn=d_th nu~, sdn=s d_s nu~, zs=zeta/s, k=k_g (|k|<=kbar), kappa<=1/2, |kappa theta|<=1,
0<=lam<=c.  Ограничения из п. 2: |eps|<=1/40.
Проверяем для w ⊥ Y (|w|=1):
 (i)   |w_omega| <= (5/4 kappa|theta| + |nut|)
 (ii)  |<s D_YY, w>| <= kappa|theta| + 5/4 kappa^2 theta^2 (1+kbar) + th2,
       th2 = |sde|+|eps|+|dte|+kbar|nut|+c kbar|zs|+|sdn|+|dtn|+c^2|zs|
 (iii) s<w,D_wY> >= -th3,
       th3 = |nut| + 4/3(|dte|+kbar|nut|+|dtn|) + |sde|+|sdn| + (kbar+c)(|eta0s|+4/3|e0t|)
Минимизируем запас по w численно (плотная сетка на окружности w ⊥ Y + локальная оптимизация).
"""
import numpy as np

rng = np.random.default_rng(12345)


def unit_perp_basis(Y):
    Y = Y / np.linalg.norm(Y)
    a = np.array([1.0, 0, 0]) if abs(Y[0]) < 0.9 else np.array([0, 1.0, 0])
    u = np.cross(Y, a); u /= np.linalg.norm(u)
    v = np.cross(Y, u)
    return u, v


worst = {'i': np.inf, 'ii': np.inf, 'iii': np.inf}
worst_par = {}
for trial in range(200000):
    small = lambda scale=1.0: rng.uniform(-1, 1) * scale * 10 ** rng.uniform(-3, 0)
    kbar = rng.uniform(0, 5)
    k = rng.uniform(-kbar, kbar)
    c = rng.uniform(1.0, 4.0)
    kap = rng.uniform(0, 0.5)
    th = rng.uniform(-1, 1) * min(1.0 / max(kap, 1e-9), 3.0)
    lam = rng.uniform(0, c)
    eps = rng.uniform(-1, 1) / 40
    sde, dte, eta0s, e0t, nut, dtn, sdn = [small(0.3) for _ in range(7)]
    zs = small(0.3)
    Y = np.array([1.0, -kap * th * (1 - eps), nut])
    u, v = unit_perp_basis(Y)
    phis = np.linspace(0, 2 * np.pi, 721)
    W = np.outer(np.cos(phis), u) + np.outer(np.sin(phis), v)
    wo, wl, wn = W[:, 0], W[:, 1], W[:, 2]
    # (i)
    m_i = (1.25 * kap * abs(th) + abs(nut)) - np.abs(wo)
    # (ii)
    D = np.array([-kap**2 * th**2 * (1 - eps),
                  kap * th * (sde - 1 + kap * (1 - eps) - kap * th * dte + nut * k + lam * k * zs),
                  sdn + kap**2 * th**2 * (1 - eps) * k - kap * th * dtn + lam**2 * zs])
    th2 = abs(sde) + abs(eps) + abs(dte) + kbar * abs(nut) + c * kbar * abs(zs) + abs(sdn) + abs(dtn) + c**2 * abs(zs)
    m_ii = kap * abs(th) + 1.25 * kap**2 * th**2 * (1 + kbar) + th2 - np.abs(W @ D)
    # (iii)
    az = wn - wo * eta0s - wl * e0t / (1 - eps)
    lhs = ((1 / (1 - eps) - kap) * wl**2 + kap * th * wo * wl
           + ((kap * th * dte - nut * k) * wl**2 + dtn * wl * wn) / (1 - eps)
           + wo * (kap * th * sde * wl + sdn * wn)
           - kap * th * k * wl * (wo * eta0s + wl * e0t / (1 - eps))
           + lam * az * wn)
    th3 = (abs(nut) + 4 / 3 * (abs(dte) + kbar * abs(nut) + abs(dtn)) + abs(sde) + abs(sdn)
           + (kbar + c) * (abs(eta0s) + 4 / 3 * abs(e0t)))
    m_iii = lhs + th3
    for key, arr in (('i', m_i), ('ii', m_ii), ('iii', m_iii)):
        mn = arr.min()
        if mn < worst[key]:
            worst[key] = mn
            worst_par[key] = dict(kap=kap, th=th, lam=lam, eps=eps, nut=nut, k=k, c=c)
print('минимальный запас (должен быть >= 0 с точностью до сетки):')
for key in worst:
    print(key, worst[key], worst_par[key])

# Контроль: при lam<0 (c2>c) оценка (iii) ломается
viol = 0
for trial in range(2000):
    lam = -rng.uniform(0.1, 1.0)
    kap = rng.uniform(0, 0.5); th = rng.uniform(-1, 1)
    Y = np.array([1.0, -kap * th, 0.0])
    u, v = unit_perp_basis(Y)
    phis = np.linspace(0, 2 * np.pi, 361)
    W = np.outer(np.cos(phis), u) + np.outer(np.sin(phis), v)
    wo, wl, wn = W[:, 0], W[:, 1], W[:, 2]
    lhs = (1 - kap) * wl**2 + kap * th * wo * wl + lam * wn * wn
    if lhs.min() < -0.05:
        viol += 1
print('контроль lam<0: доля нарушений при нулевых малых величинах', viol / 2000)
