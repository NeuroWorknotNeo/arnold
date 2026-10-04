"""[Эксперимент] Пограничный случай теоремы C: U = (x^2+y^2-z^2)^4 + x z^8 (m = 8,
поперечный порядок k = 4, α = 5/4). Координаты s = ρ+z, θ, σ = ρ-z (u_8 = s^4 σ^4 точно),
веса s:1, θ:0, σ:5/4. F = s^4σ^4 + cosθ s^9/512. Линейный по σ член -7cosθ s^8σ/512 имеет
превышение 1/4 = α-1 (пограничный). Поле A = V/9 - U₊R/(1+R(v)) (как в thmB_example.py, без сдвига).
Печатаем min λ(sym DA) по масштабам: если предел отрицателен, конструкция не работает."""
import random
import mpmath as mp
mp.mp.dps = 80
import sys
KK = mp.mpf(sys.argv[1])
ALPHA = mp.mpf(5)/4; D = 9

def U_cart(x, y, z):
    return (x*x + y*y - z*z)**4 + x*z**8 + KK*(x*x+y*y-z*z)*x*z**6

def coords(x, y, z):
    rho = mp.sqrt(x*x + y*y); th = mp.atan2(y, x)
    return rho + z, th, rho - z

def cart(s, th, sig):
    rho = (s + sig)/2; z = (s - sig)/2
    return rho*mp.cos(th), rho*mp.sin(th), z

def U_c(s, th, sig): return U_cart(*cart(s, th, sig))
def F_c(s, th, sig): return s**4*sig**4 + mp.cos(th)*s**9/512
W = (1, 0, ALPHA)
CWSIG = mp.mpf(sys.argv[2])  # показатель: вес σ умножается на s^CWSIG

def grad_c(f, c, h):
    g = []
    for i in range(3):
        cp = list(c); cm = list(c); cp[i] += h[i]; cm[i] -= h[i]
        g.append((f(*cp) - f(*cm))/(2*h[i]))
    return g

def hs(s, e): return (s*mp.mpf(10)**-e, mp.mpf(10)**-e, s**ALPHA*mp.mpf(10)**-e)

def A_coords(c):
    s = c[0]; h = hs(s, 25)
    gU = grad_c(U_c, c, h); gF = grad_c(F_c, c, h)
    Vc = (s, 0, ALPHA*c[2])
    U = U_c(*c)
    Uplus = sum(Vc[i]*gU[i] for i in range(3))/D - U
    CW = (1, 1, s**CWSIG)
    den = sum(CW[j]*s**(2*W[j])*gF[j]**2 for j in range(3))
    r = [CW[i]*s**(2*W[i])*gF[i]/den for i in range(3)]
    Rv = sum(r[i]*(gU[i] - gF[i]) for i in range(3))
    return [Vc[i]/D - Uplus*r[i]/(1 + Rv) for i in range(3)]

def A_cart(p):
    c = coords(*p); Ac = A_coords(c); h = hs(c[0], 30)
    J = []
    for i in range(3):
        cp = list(c); cm = list(c); cp[i] += h[i]; cm[i] -= h[i]
        a, b = cart(*cp), cart(*cm)
        J.append([(a[k] - b[k])/(2*h[i]) for k in range(3)])
    return [sum(J[i][k]*Ac[i] for i in range(3)) for k in range(3)]

def lam_min(p):
    r = mp.sqrt(sum(t*t for t in p)); h = r*mp.mpf(10)**-22
    S = mp.matrix(3, 3); Dm = [[0]*3 for _ in range(3)]
    for j in range(3):
        pp = list(p); pm = list(p); pp[j] += h; pm[j] -= h
        a, b = A_cart(pp), A_cart(pm)
        for i in range(3): Dm[i][j] = (a[i] - b[i])/(2*h)
    for i in range(3):
        for j in range(3): S[i, j] = (Dm[i][j] + Dm[j][i])/2
    return min(mp.eigsy(S)[0])

random.seed(1)
for r in (() if len(sys.argv) > 3 else ('1e-16', '1e-24', '1e-32')):
    r = mp.mpf(r); worst = mp.inf; n = 0
    while n < 80:
        th = random.uniform(0, 6.2831853); s = r*random.uniform(0.7, 1.3)
        sig = random.uniform(-1.2, 1.2)*s**ALPHA*(abs(mp.cos(th))/512 + 1e-4)**0.25
        p = cart(s, th, sig)
        if U_cart(*p) >= 0: continue
        n += 1; worst = min(worst, lam_min(p))
    print(f"r={mp.nstr(r,3)}: min λ(sym DA) = {mp.nstr(worst,6)}", flush=True)

# отладка: худшая точка
if len(sys.argv) > 3:
    random.seed(1); r = mp.mpf('1e-8'); best = None; n = 0
    while n < 80:
        th = random.uniform(0, 6.2831853); s = r*random.uniform(0.7, 1.3)
        sig = random.uniform(-1.2, 1.2)*s**ALPHA*(abs(mp.cos(th))/512 + 1e-4)**0.25
        p = cart(s, th, sig)
        if U_cart(*p) >= 0: continue
        n += 1; l = lam_min(p)
        if best is None or l < best[0]: best = (l, th, sig/s**ALPHA, s)
    l, th, sh, s = best
    c = (s, mp.mpf(th), sh*s**ALPHA)
    print('worst', mp.nstr(l,5), 'θ=', th, 'σ̂=', mp.nstr(sh,5), 'f=', mp.nstr(F_c(*c)/s**9,5), 'U/s^9=', mp.nstr(U_c(*c)/s**9,5))
