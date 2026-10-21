# [Эксперимент] Поле хода 5 с ИСПРАВЛЕННОЙ интерполяцией b(u): гладкий рост 0 → 1/3 при u: 0.05 → 0.3
# (в k4_perp.py ступенька перевёрнута и разрывна). y-вар., ℓ=r^{5/4}, λ=1. Прицельная выборка как в k4_perp.py.
import sys, random
src = open('k4_spot.py').read().split("r = mp.mpf('1e-48')")[0]
_argv = sys.argv; sys.argv = [sys.argv[0]]; src = src.replace("Kv = 200", "Kv = int(__import__(\"os\").environ.get(\"KV\", \"200\"))"); exec(src); sys.argv = _argv
Kv_ = Kv
def bfun(t, r):
    u = mp.log(abs(t))/mp.log(r)
    x = (u - mp.mpf('0.05'))/(mp.mpf('0.3') - mp.mpf('0.05'))
    if x <= 0: return mp.mpf(0)
    if x >= 1: return mp.mpf(1)/3
    a = mp.exp(-1/x); b = mp.exp(-1/(1 - x)); return a/(a + b)/3
NS = int(sys.argv[2]) if len(sys.argv) > 2 else 200
random.seed(11)
for rs in sys.argv[1].split(','):
    r = mp.mpf(rs); L = float(-mp.log10(r)); mp.mp.dps = int(150 + 4.5*L)
    worst = None; n = 0; qmin = mp.inf
    while n < NS:
        s = r*random.uniform(0.7, 1.3)
        th = mp.pi/2 + random.choice([-1, 1])*mp.mpf(10)**random.uniform(-3*L/4 - 3, -0.5)
        sh = random.choice([-1, 1])*mp.mpf(10)**random.uniform(-L/3 - 2, 0)
        p = cart(s, th, sh*s**ALPHA)
        if Uf(*p) >= 0: continue
        n += 1
        rr = mp.sqrt(sum(c*c for c in p))
        l = lam_min(p, rr*mp.mpf(10)**-(24 + int(0.8*float(-mp.log10(rr)))))
        g = gf(*p); Av = A(p); qq = sum(Av[k]*g[k] for k in range(3))/Uf(*p); qmin = min(qmin, qq)
        if worst is None or l < worst[0]:
            worst = (l, mp.nstr((th - mp.pi/2)/r**(mp.mpf(1)/3), 4), mp.nstr(sh, 3), mp.nstr(mp.log(abs(th-mp.pi/2))/mp.log(rr), 4))
    print(f"[испр. b] K={Kv_} r={rs} NS={NS}: min λ(sym DA) = {mp.nstr(worst[0],6)}; min A(U)/U = {mp.nstr(qmin,6)}; худшая τ̂={worst[1]}, σ̂={worst[2]}, u={worst[3]}", flush=True)
