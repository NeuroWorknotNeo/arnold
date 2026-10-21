"""R29: численные проверки к предложениям 5.4, 4.2(b) и к лемме 3.5. [Эксперимент]"""
import numpy as np
import mpmath as mp
from scipy.optimize import linprog

# ---------- 5.4: допустимость (l1,l2) по предельным условиям, ЛП
def lp_54(k, ntau=4001):
    taus = np.concatenate([np.linspace(-50, 50, ntau), [(-2 + np.sqrt(4 - k*k))/k, (-2 - np.sqrt(4 - k*k))/k]])
    g = taus**2 + k*taus + 1
    rho = taus*(2*taus + k)/g
    # условия: 6l1+(l2-2l1)rho >= mu, 6l2+(l1-2l2)rho >= mu; нормируем mu=1, ищем допустимость
    A, b = [], []
    for r in rho:
        A.append([-(6 - 2*r), -r]); b.append(-1)
        A.append([-r, -(6 - 2*r)]); b.append(-1)
    res = linprog(c=[0, 0], A_ub=A, b_ub=b, bounds=[(-1e6, 1e6)]*2, method='highs')
    return res.status  # 0 = допустимо, 2 = недопустимо

for k in [1.0, 1.5, 1.8, 1.9, 1.95, 1.97, 8*np.sqrt(3)/7, 1.985, 1.99, 1.999]:
    st = lp_54(k)
    R = 2/np.sqrt(4 - k*k) - 1
    print("5.4 k=%.4f R=%.3f: предельные условия %s" % (k, R, "допустимы" if st == 0 else "НЕдопустимы"))

# прямая проверка на Q при k=1.99 для пробных (l1,l2): min xi log Q на малых окружностях
def xilogQ(l1, l2, k, b1, b2):
    G1 = b2**2 + k*b1**2*b2 + b1**4; G2 = b1**2 + k*b1*b2**2 + b2**4
    G1x = 2*k*b1*b2 + 4*b1**3; G1y = 2*b2 + k*b1**2
    G2x = 2*b1 + k*b2**2; G2y = 2*k*b1*b2 + 4*b2**3
    return (l1*b1*(G1x/G1 + G2x/G2) + l2*b2*(G1y/G1 + G2y/G2))
k = 1.99
best = -1e9
for l1 in np.linspace(0.05, 1, 40):
    for l2 in np.linspace(0.05, 1, 40):
        mn = 1e9
        for t in np.linspace(-60, 60, 3001):
            b1 = 1e-3; mn = min(mn, xilogQ(l1, l2, k, b1, t*b1**2), xilogQ(l1, l2, k, t*b1**2, b1))
        best = max(best, mn)
print("5.4 k=1.99: max_{l1,l2 в [0.05,1]^2} min xi log Q на кривых b2=t b1^2, b1=t b2^2 (b=1e-3): %.4f" % best)

# ---------- 4.2(b): s g'(s)/g(s) в s_k = 2 a_k
mp.mp.dps = 60
lam = lambda u: mp.e**(-1/(u*(1 - u))) if 0 < u < 1 else mp.mpf(0)
def h(s, K=6):
    return sum(mp.e**(-1/s)*lam(2*s/mp.mpf(4)**(-k) - 1) for k in range(1, K + 1)) if s > 0 else mp.mpf(0)
for k in [1, 2, 3]:
    a = mp.mpf(4)**(-k); s = 2*a
    gp = h(s) + mp.e**(-1/s**2)
    pts = [mp.mpf(0)] + [mp.mpf(4)**(-j)*f for j in range(12, 0, -1) for f in (mp.mpf(1)/2, 1)] + [s]
    pts = sorted(set(p for p in pts if p <= s))
    g = sum(mp.quad(lambda t: h(t) + mp.e**(-1/t**2), [pts[i], pts[i + 1]]) for i in range(len(pts) - 1))
    print("4.2(b) k=%d: h(s_k)=%s, s g'/g = %s, оценка текста C e^{-1/(4a^2)+2/a}: %s"
          % (k, mp.nstr(h(s), 3), mp.nstr(s*gp/g, 5), mp.nstr(mp.e**(-1/(4*a*a) + 2/a)*4/mp.quad(lam, [0, 1]), 5)))

# ---------- лемма 3.5 как чисто алгебраическое неравенство (eps = 0)
rng = np.random.default_rng(1)
def worst_sum(b2, phi, E, N):
    d = len(phi); psi = phi.real
    dist = np.abs(b2 - phi); p = dist**2
    w = (p.min()/p)**N; w /= w.sum()
    tot = 0
    for j in range(d):
        s = 0
        for kk in range(d):
            z = (b2 - psi[j])/(b2 - phi[kk])
            # наихудший e in [1,E] для Re[e-(e-1)z] = 1 + (e-1)(1-Re z)
            e = E if z.real > 1 else 1.0
            s += (e - (e - 1)*z).real
        tot += w[j]*s
    return tot
viol = 0; mins = {}
for trial in range(200000):
    d = rng.integers(2, 7); E = rng.choice([1.5, 2, 3, 6]); N = int(np.ceil((4*d*(E - 1) + 1)/2))
    sc = 10.0**rng.uniform(-6, 0, size=d)
    phi = rng.normal(size=d)*rng.choice([1, 1e-3]) + 1j*sc*rng.choice([-1, 1], size=d)
    b2 = rng.normal()*rng.choice([1, 1e-3])
    v = worst_sum(b2, phi, E, N)
    bound = d*(1 - d*(E - 1)/(2*N - 1))
    mins[(d, E)] = min(mins.get((d, E), 1e9), v/d)
    if v < bound - 1e-9: viol += 1
print("лемма 3.5 (eps=0, случайные конфигурации, 2e5): нарушений нижней оценки:", viol)
print("  min (сумма)/d по (d,E):", {k: round(v, 3) for k, v in sorted(mins.items())})
# то же при N=0 (равные веса): есть ли отрицательные значения
neg = 0
for trial in range(50000):
    d = 4; E = 6
    phi = np.array([0.0 + 1e-6j, 0 - 1e-6j, 1e-3 + 1e-6j, 1e-3 - 1e-6j])
    b2 = rng.uniform(-1e-3, 2e-3)
    v = worst_sum(b2, phi, E, 0)
    neg = min(neg, v)
print("  N=0, две тонкие пары, E=6: min суммы =", round(neg, 2))
