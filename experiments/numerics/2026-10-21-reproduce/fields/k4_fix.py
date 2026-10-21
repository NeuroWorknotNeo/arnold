"""[Эксперимент] Попытка исправить поле в пограничном примере (K=200): A = V/9 + χ(f)·A'_∞,
A'_∞ = −U₊R'/(1+R'(W)), R' = ∇_ℓ f/(s^9 |∇_ℓ f|^2) — без r-компоненты, только около {f=0};
χ(f)=1 при |f|≤δ/2, 0 при |f|≥δ. Печатаем min λ(sym DA) и max A(U)/U (нужно < 1 с запасом)."""
import sys, random
KARG = sys.argv[1] if len(sys.argv) > 1 else '200'
DELTA = mp_delta = None
sys.argv = ['x', KARG, '1']
exec(open('thmC_k4_K.py').read().split('random.seed(1)')[0])
DELTA = mp.mpf('0.0006')

def chi(f):
    t = (abs(f) - DELTA/2)/(DELTA/2)
    if t <= 0: return mp.mpf(1)
    if t >= 1: return mp.mpf(0)
    a = mp.exp(-1/t); b = mp.exp(-1/(1 - t))
    return b/(a + b)

def A_coords(c):
    s = c[0]; h = hs(s, 25)
    gU = grad_c(U_c, c, h); gF = grad_c(F_c, c, h)
    Vc = (s, 0, ALPHA*c[2])
    U = U_c(*c); f = F_c(*c)/s**9
    Uplus = sum(Vc[i]*gU[i] for i in range(3))/D - U
    ch = chi(f)
    if ch == 0: return [Vc[i]/D for i in range(3)]
    # ∇_ℓ f в весовой метрике: θ вес 0, σ вес α (как R Паламодова, но без r-компоненты)
    den = sum(s**(2*W[j])*gF[j]**2 for j in (1, 2))
    r = [0, s**(2*W[1])*gF[1]/den, s**(2*W[2])*gF[2]/den]
    Rv = sum(r[i]*(gU[i] - gF[i]) for i in range(3))
    return [Vc[i]/D - ch*Uplus*r[i]/(1 + Rv) for i in range(3)]

def ratio(p):
    rr = mp.sqrt(sum(t*t for t in p)); h = rr*mp.mpf(10)**-22
    A = A_cart(p)
    g = []
    for j in range(3):
        pp = list(p); pm = list(p); pp[j] += h; pm[j] -= h
        g.append((U_cart(*pp) - U_cart(*pm))/(2*h))
    return sum(A[i]*g[i] for i in range(3))/U_cart(*p)

random.seed(1)
for r in ('1e-16', '1e-24', '1e-32'):
    r = mp.mpf(r); worst = mp.inf; rmin = mp.inf; n = 0
    while n < 80:
        th = random.uniform(0, 6.2831853); s = r*random.uniform(0.7, 1.3)
        sig = random.uniform(-1.2, 1.2)*s**ALPHA*(abs(mp.cos(th))/512 + 1e-4)**0.25
        p = cart(s, th, sig)
        if U_cart(*p) >= 0: continue
        n += 1; worst = min(worst, lam_min(p)); rmin = min(rmin, ratio(p))
    print(f"K={KARG} r={mp.nstr(r,3)}: min λ(sym DA) = {mp.nstr(worst,6)}, min A(U)/U = {mp.nstr(rmin,6)}", flush=True)
