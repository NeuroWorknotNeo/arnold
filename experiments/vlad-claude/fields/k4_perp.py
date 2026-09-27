"""[Эксперимент] Поле A = V/9 + W, W = −U₊ ∇_⊥U / (|∇_⊥U|² + λ U²/|x|²): коррекция по
евклидову градиенту, ортогональному радиусу; регуляризация λ выключает её там, где |∇_⊥U|
мал по сравнению с |U|/|x| (там коррекция не нужна). Идея: евклидов градиент автоматически
выбирает самое «тонкое» направление режима. Пример U = q⁴ + xz⁸ + K q x z⁶."""
import sys, random
import mpmath as mp
import os
mp.mp.dps = int(os.environ.get("DPS", "90"))
CX, CY = (0, 1) if "--y" in sys.argv else (1, 0)
sys.argv = [a for a in sys.argv if a != "--y"]
USEB = "--b" in sys.argv
LEXP = mp.mpf(os.environ.get("LEXP", "1"))
sys.argv = [a for a in sys.argv if a != "--b"]
K = mp.mpf(sys.argv[1]); LAM = mp.mpf(sys.argv[2]) if len(sys.argv) > 2 else mp.mpf(1)
ALPHA = mp.mpf(5)/4; D = 9

def U_cart(x, y, z):
    q = x*x + y*y - z*z
    return q**4 + x*z**8 + K*q*(x*CX + y*CY)*z**6

def cart(s, th, sig):
    rho = (s + sig)/2; z = (s - sig)/2
    return [rho*mp.cos(th), rho*mp.sin(th), z]

def coords(x, y, z):
    rho = mp.sqrt(x*x + y*y); return rho + z, mp.atan2(y, x), rho - z

def bfun(t, r):
    u = mp.log(abs(t))/mp.log(r) if t != 0 else mp.mpf(10)
    u1, u2 = mp.mpf('0.05'), mp.mpf('0.3')
    x = (u - u1)/(u2 - u1)
    if x <= 0: return mp.mpf(0)
    if x >= 1: return mp.mpf(1)/3
    a = mp.exp(-1/x); b = mp.exp(-1/(1 - x))
    return b/(a + b)/3

def V_cart(p):
    # V = s∂s + (5/4 + b/4) σ∂σ + b (θ−θ0) ∂θ в координатах (s,θ,σ), переведённое в декартовы
    s, th, sig = coords(*p)
    if USEB:
        th0 = mp.pi/2 if th > 0 else -mp.pi/2
        t = th - th0; b = bfun(t, mp.sqrt(sum(q*q for q in p)))
        rho = (s + sig)/2
        dth = [-rho*mp.sin(th), rho*mp.cos(th), 0]
        ds = [mp.cos(th)/2, mp.sin(th)/2, mp.mpf(1)/2]; dsg = [mp.cos(th)/2, mp.sin(th)/2, -mp.mpf(1)/2]
        return [s*ds[k] + (ALPHA + b/4)*sig*dsg[k] + b*t*dth[k] for k in range(3)]
    # ∂x/∂s = (cosθ/2, sinθ/2, 1/2), ∂x/∂σ = (cosθ/2, sinθ/2, −1/2)
    ds = [mp.cos(th)/2, mp.sin(th)/2, mp.mpf(1)/2]; dsg = [mp.cos(th)/2, mp.sin(th)/2, -mp.mpf(1)/2]
    return [s*ds[k] + ALPHA*sig*dsg[k] for k in range(3)]

def grad(f, p, h):
    g = []
    for j in range(3):
        pp = list(p); pm = list(p); pp[j] += h; pm[j] -= h
        g.append((f(*pp) - f(*pm))/(2*h))
    return g

def A_cart(p):
    r = mp.sqrt(sum(t*t for t in p)); h = r*mp.mpf(10)**-(30 + int(0.8*float(-mp.log10(r))))
    gU = grad(U_cart, p, h); U = U_cart(*p); V = V_cart(p)
    if USEB:
        s_, th_, sg_ = coords(*p); th0 = mp.pi/2 if th_ > 0 else -mp.pi/2
        Pb = D + bfun(th_ - th0, r)
        Up = sum(V[k]*gU[k] for k in range(3)) - Pb*U
        e = [t/r for t in p]; gr = sum(gU[k]*e[k] for k in range(3))
        gp = [gU[k] - gr*e[k] for k in range(3)]
        den = sum(t*t for t in gp) + LAM*U*U/r**(2*LEXP)
        return [V[k] - Up*gp[k]/den for k in range(3)]
    Up = sum(V[k]*gU[k] for k in range(3))/D - U
    e = [t/r for t in p]; gr = sum(gU[k]*e[k] for k in range(3))
    gp = [gU[k] - gr*e[k] for k in range(3)]
    den = sum(t*t for t in gp) + LAM*U*U/(r*r)
    return [V[k]/D - Up*gp[k]/den for k in range(3)]

def check(p):
    r = mp.sqrt(sum(t*t for t in p)); h = r*mp.mpf(10)**-(24 + int(0.8*float(-mp.log10(r))))
    Dm = [[0]*3 for _ in range(3)]
    for j in range(3):
        pp = list(p); pm = list(p); pp[j] += h; pm[j] -= h
        a, b = A_cart(pp), A_cart(pm)
        for i in range(3): Dm[i][j] = (a[i] - b[i])/(2*h)
    S = mp.matrix(3, 3)
    for i in range(3):
        for j in range(3): S[i, j] = (Dm[i][j] + Dm[j][i])/2
    A = A_cart(p); gU = grad(U_cart, p, r*mp.mpf(10)**-(30 + int(0.8*float(-mp.log10(r)))))
    return min(mp.eigsy(S)[0]), sum(A[k]*gU[k] for k in range(3))/U_cart(*p)

def sample(r, mode):
    s = r*random.uniform(0.7, 1.3)
    if mode == 'uniform':
        th = random.uniform(0, 6.2831853)
        sh = random.uniform(-1.2, 1.2)*(abs(mp.cos(th))/512 + 1e-4)**0.25
    else:  # около θ0 = π/2 и σ̂ ≈ 0, логарифмически
        th = mp.pi/2 + random.choice([-1, 1])*mp.mpf(10)**random.uniform(-3*float(-mp.log10(r))/4 - 3, -0.5)
        sh = random.choice([-1, 1])*mp.mpf(10)**random.uniform(-float(-mp.log10(r))/3 - 2, 0)
    return cart(s, th, sh*s**ALPHA)

random.seed(3)
for rs in sys.argv[3:] if len(sys.argv) > 3 else ('1e-16', '1e-32'):
    r = mp.mpf(rs)
    for mode in ('uniform', 'targeted'):
        worst = mp.inf; rmax = -mp.inf; rmin = mp.inf; n = 0
        while n < int(os.environ.get("NS", "100")):
            p = sample(r, mode)
            if U_cart(*p) >= 0: continue
            n += 1; l, q = check(p)
            if l < worst: wp = p
            worst = min(worst, l); rmax = max(rmax, q); rmin = min(rmin, q)
        s_, th_, sg_ = coords(*wp)
        print(f"K={K} λ={LAM} r={rs} {mode}: min λ(sym DA)={mp.nstr(worst,5)}, A(U)/U ∈ [{mp.nstr(rmin,6)}, {mp.nstr(rmax,6)}]; худшая: t={mp.nstr(th_-mp.pi/2,4)}, t/r^(1/3)={mp.nstr((th_-mp.pi/2)/r**(mp.mpf(1)/3),4)}, σ̂={mp.nstr(sg_/s_**ALPHA,4)}, σ/r^(4/3)={mp.nstr(sg_/r**(mp.mpf(4)/3),4)}", flush=True)
