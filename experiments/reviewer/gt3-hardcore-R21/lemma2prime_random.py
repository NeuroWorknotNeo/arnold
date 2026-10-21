"""Рецензент R21: случайная и «враждебная» проверка оценки (7.1) леммы 2'.

[Эксперимент] В точке множества из (A5) строятся векторы Y, grad rho, nabla_Y Y, матрица DY,
число A'(rho), значения W, P, rho*YW, удовлетворяющие (L0), (L1), (L2'), (L3') на грани
(худший случай), и проверяется, что (rho/lambda)*Xi по формуле (1.3) results/007 не меньше
правой части (7.1), если Gamma'^2 <= beta*mu. Это не доказательство, а поиск контрпримера.
Запуск: ~/venv/bin/python lemma2prime_random.py
"""
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(20261021)
NTRIALS = 600


def unit_perp(Y, z):
    z = z - np.dot(z, Y) / np.dot(Y, Y) * Y
    return z / np.linalg.norm(z)


def margin(params, x, n=3):
    """Возвращает (lhs - rhs)/(delta rho^beta) или None, если параметры недопустимы."""
    (beta, mu, a1, a3, a2, h0, h1, delta, eps0, eps1, th1, th2, th3, g1p, g2p) = params
    # распаковка свободных переменных точки
    rho = 1.0  # (7.1) однородно степени beta по rho (все члены ~ rho^beta); x[0] не используется
    h = h0 + (h1 - h0) * (np.tanh(x[1]) + 1) / 2
    A = (a1 + (a3 - a1) * (np.tanh(x[2]) + 1) / 2) * rho**beta
    Ap = a2 * np.tanh(x[3]) * rho**(beta - 1)
    P = (np.tanh(x[4]) + 1) / 2 * 1.5 * delta * rho**beta          # P >= 0
    W = P + eps0 * delta * rho**beta * np.tanh(x[5])              # |W-P| <= eps0 delta rho^b
    K = delta * rho**beta - W                                       # V = delta rho^beta
    if K < 0:
        return None
    lam = np.sqrt(2 * (A - delta * rho**beta) / h)
    # главный член: beta W - rho YW = mu P - eps1 delta rho^beta (на грани (L2'))
    main = beta * K + mu * P - eps1 * delta * rho**beta
    # геометрия
    Y = np.array([np.sqrt(h), 0.0, 0.0])
    e = unit_perp(Y, np.array([0.0, np.cos(x[6]), np.sin(x[6])]))
    vperp = np.sqrt(2 * K) * e
    s = np.sqrt(P / rho**beta)
    dnorm = th1 + g1p * s
    dvec = dnorm * unit_perp(Y, np.array([0.0, np.cos(x[7]), np.sin(x[7])]))
    gyy_perp = (th2 + g2p * s) / rho * unit_perp(Y, np.array([0.0, np.cos(x[8]), np.sin(x[8])]))
    gyy = gyy_perp + x[9] * Y
    # DY: на Y^perp форма rho <w, DY w> >= -th3 |w|^2; берём худший случай -th3
    DY = rng_DY(x[10:14], Y, rho, th3)
    T1 = rho / lam * (Ap - beta * delta * rho**(beta - 1)) * np.dot(dvec, vperp)
    T2 = -lam * rho * np.dot(vperp, gyy)
    T3 = rho * np.dot(vperp, DY @ vperp)
    lhs = main + T1 + T2 + T3
    c1 = 2 * (a2 + beta * a1 / 2) * np.sqrt(h1 / a1)
    c2 = 2 * np.sqrt(2 * a3 / h0)
    rhs = delta * rho**beta * (mu / 2 * (1 - eps0) - eps1 - (c1 * th1 + c2 * th2) / np.sqrt(delta) - 4 * th3)
    return (lhs - rhs) / (delta * rho**beta)


def rng_DY(z, Y, rho, th3):
    # симметричная часть на Y^perp равна -th3/rho * I (худший случай), плюс произвольные члены,
    # не влияющие на <w, DY w> при w perp Y (антисимметричная часть и строка/столбец Y)
    S = -th3 / rho * np.diag([0.0, 1.0, 1.0])
    Aanti = np.array([[0, z[0], z[1]], [-z[0], 0, z[2]], [-z[1], -z[2], 0]])
    col = np.zeros((3, 3)); col[:, 0] = z[3]
    return S + Aanti + col


worst = np.inf
nfail = 0
for trial in range(NTRIALS):
    beta = rng.uniform(2, 10)
    mu = rng.uniform(0.01, 1) * beta
    a1 = rng.uniform(0.1, 3); a3 = a1 * rng.uniform(1, 3); a2 = rng.uniform(0, 3) * beta * a3
    h0 = rng.uniform(0.2, 1); h1 = h0 * rng.uniform(1, 4)
    delta = a1 / 2 * rng.uniform(0.001, 1)
    eps0 = rng.uniform(0, 0.5); eps1 = rng.uniform(0, 0.5)
    th1, th2, th3 = rng.uniform(0, 0.3, 3) * rng.integers(0, 2, 3)
    g1p, g2p = rng.uniform(0, 1, 2)
    Gp = np.sqrt(2) * ((a2 + beta * delta) * np.sqrt(h1 / a1) * g1p + np.sqrt(2 * a3 / h0) * g2p)
    if Gp**2 > beta * mu:   # масштабируем gamma', чтобы Gamma'^2 = beta mu * t, t<=1
        t = rng.uniform(0.5, 1.0)
        f = np.sqrt(beta * mu * t) / Gp
        g1p *= f; g2p *= f
    params = (beta, mu, a1, a3, a2, h0, h1, delta, eps0, eps1, th1, th2, th3, g1p, g2p)
    fun = lambda x: (lambda m: 1e6 if m is None else m)(margin(params, x))
    best = np.inf
    for start in range(2):
        x0 = rng.normal(size=14)
        r = minimize(fun, x0, method='Nelder-Mead', options={"maxiter": 2000, "xatol": 1e-9, "fatol": 1e-12})
        best = min(best, r.fun)
    worst = min(worst, best)
    if trial % 100 == 99:
        print("испытаний:", trial + 1, "минимальный запас:", worst, flush=True)
    if best < -1e-9:
        nfail += 1
        print("FAIL", trial, best, params)
print("минимальный запас (lhs-rhs)/(delta rho^beta) по всем испытаниям:", worst)
print("нарушений:", nfail)

# Контроль: при Gamma'^2 заметно больше mu(2beta-mu) оценка должна ломаться
beta, mu = 6.0, 1.0
a1 = a3 = 1.0; a2 = beta; h0 = h1 = 1.0; delta = 0.01
eps0 = eps1 = th1 = th2 = th3 = 0.0
Gtarget = 1.5 * np.sqrt(mu * (2 * beta - mu))
g1p = Gtarget / (np.sqrt(2) * (a2 + beta * delta) * np.sqrt(h1 / a1)); g2p = 0.0
params = (beta, mu, a1, a3, a2, h0, h1, delta, eps0, eps1, th1, th2, th3, g1p, g2p)
fun = lambda x: (lambda m: 1e6 if m is None else m)(margin(params, x))
best = min(minimize(fun, rng.normal(size=14), method='Nelder-Mead',
                    options={'maxiter': 5000}).fun for _ in range(10))
print("контроль (Gamma' = 1.5 sqrt(mu(2beta-mu))): минимальный запас =", best, "(ожидается < 0)")
