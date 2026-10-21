# [Эксперимент] thmC_k4_K.py (поле теоремы C без сдвига), K=50: прицельная выборка около лучей cosθ=0
import sys, random
src = open('/home/claudeagent/arnold/experiments/vlad-claude/fields/thmC_k4_K.py').read().split("random.seed(1)")[0]
sys.argv = ['x', sys.argv[1], '1', 'noscan']
exec(src)
mp.mp.dps = 120
random.seed(5)
for rs in ('1e-16', '1e-24'):
    r = mp.mpf(rs); L = float(-mp.log10(r)); worst = (mp.inf,); n = 0
    while n < 150:
        th = mp.pi/2 + random.choice([-1, 1])*mp.mpf(10)**random.uniform(-L/3 - 2, -0.3)
        s = r*random.uniform(0.7, 1.3)
        w = (abs(mp.cos(th))/512)**0.25
        sig = random.uniform(-1.3, 1.3)*s**ALPHA*w
        p = cart(s, th, sig)
        if U_cart(*p) >= 0: continue
        n += 1; l = lam_min(p)
        if l < worst[0]: worst = (l, mp.nstr(th - mp.pi/2, 3), mp.nstr(sig/s**ALPHA/w, 3))
    print(f"K={KK} r={rs}: прицельно min λ = {mp.nstr(worst[0],6)} (t={worst[1]}, σ̂/ширина={worst[2]})", flush=True)
