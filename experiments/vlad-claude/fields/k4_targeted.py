"""[Эксперимент] Прицельная выборка около особого множества {σ̂≈0, g≈0} (θ≈π/2) для поля с
«евклидовым» весом σ (thmC_k4_eucl.py): σ̂ и θ−π/2 логарифмически равномерно."""
import sys, random
K, E = sys.argv[1], sys.argv[2]
sys.argv = ['x', K, E]
exec(open('thmC_k4_eucl.py').read().split('random.seed(1)\nfor r')[0])

def ratio(p):
    rr = mp.sqrt(sum(t*t for t in p)); h = rr*mp.mpf(10)**-22
    A = A_cart(p); g = []
    for j in range(3):
        pp = list(p); pm = list(p); pp[j] += h; pm[j] -= h
        g.append((U_cart(*pp) - U_cart(*pm))/(2*h))
    return sum(A[i]*g[i] for i in range(3))/U_cart(*p)

random.seed(7)
for r in ('1e-24', '1e-40'):
    r = mp.mpf(r); worst = (mp.inf, None); rmin = mp.inf; n = 0
    while n < 120:
        th = mp.pi/2 + random.choice([-1, 1])*mp.mpf(10)**random.uniform(-9, -0.5)
        s = r*random.uniform(0.7, 1.3)
        sh = random.choice([-1, 1])*mp.mpf(10)**random.uniform(-8, 0)
        p = cart(s, th, sh*s**ALPHA)
        if U_cart(*p) >= 0: continue
        n += 1; l = lam_min(p); rmin = min(rmin, ratio(p))
        if l < worst[0]: worst = (l, mp.nstr(th - mp.pi/2, 3), mp.nstr(sh, 3))
    print(f"K={K} r={mp.nstr(r,3)}: min λ = {mp.nstr(worst[0],5)} (θ−π/2={worst[1]}, σ̂={worst[2]}), min A(U)/U = {mp.nstr(rmin,6)}", flush=True)
