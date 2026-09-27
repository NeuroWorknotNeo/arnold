"""[Эксперимент] Проверка конструкции «теоремы B» (notes/vlad-claude/theoremB.md) на примере
U = (x^2+y^2-z^2)^2 + x z^4 около верхней полы конуса ρ = z.
Координаты: s = ρ+z, θ, σ' = (ρ - z) - (3/64) cosθ s^2  (σ = ρ - z = q/(ρ+z)).
Главная часть F = s^2 σ'^2 + cosθ s^5/32 (веса s:1, θ:0, σ':3/2, степень 5).
Поле A = V/5 + A_inf, V = s∂s + 1.5 σ'∂σ', A_inf = -U₊ R/(1+R(v)), U₊ = V(U)/5 - U,
v = U - F, R = Σ r_i ∂_i, r_i = s^{2w_i} ∂_iF / Σ_j s^{2w_j} (∂_jF)^2.
Проверяем A(U)/U (=1) и λ_min(sym DA) в декартовых координатах (конечные разности,
mpmath 60 знаков) в случайных точках {U<0} на масштабах r."""
import random
import mpmath as mp

mp.mp.dps = 60

def U_cart(x, y, z):
    return (x*x + y*y - z*z)**2 + x*z**4

def coords(x, y, z):
    rho = mp.sqrt(x*x + y*y); th = mp.atan2(y, x)
    s = rho + z; sig = rho - z
    return s, th, sig - mp.mpf(3)/64*mp.cos(th)*s**2

def cart(s, th, sp_):
    sig = sp_ + mp.mpf(3)/64*mp.cos(th)*s**2
    rho = (s + sig)/2; z = (s - sig)/2
    return rho*mp.cos(th), rho*mp.sin(th), z

def U_c(s, th, sp_):
    return U_cart(*cart(s, th, sp_))

def F_c(s, th, sp_):
    return s**2*sp_**2 + mp.cos(th)*s**5/32

W = (1, 0, mp.mpf(3)/2)

def grad_c(f, c, h):
    g = []
    for i in range(3):
        e = [0, 0, 0]; e[i] = h[i]
        cp = [c[k] + e[k] for k in range(3)]; cm = [c[k] - e[k] for k in range(3)]
        g.append((f(*cp) - f(*cm))/(2*h[i]))
    return g

def A_coords(c):
    s, th, sp_ = c
    h = (s*mp.mpf(10)**-20, mp.mpf(10)**-20, s**mp.mpf(1.5)*mp.mpf(10)**-20)
    gU = grad_c(U_c, c, h); gF = grad_c(F_c, c, h)
    Vc = (s, 0, W[2]*sp_)
    U = U_c(*c); F = F_c(*c); v = U - F
    VU = sum(Vc[i]*gU[i] for i in range(3))
    Uplus = VU/5 - U
    den = sum(s**(2*W[j])*gF[j]**2 for j in range(3))
    r = [s**(2*W[i])*gF[i]/den for i in range(3)]
    Rv = sum(r[i]*(gU[i] - gF[i]) for i in range(3))
    return [Vc[i]/5 - Uplus*r[i]/(1 + Rv) for i in range(3)]

def A_cart(p):
    c = coords(*p)
    Ac = A_coords(c)
    # push forward: dx = J dc, J = ∂(x,y,z)/∂(s,θ,σ')
    s = c[0]; h = (s*mp.mpf(10)**-25, mp.mpf(10)**-25, s**mp.mpf(1.5)*mp.mpf(10)**-25)
    J = []
    for i in range(3):
        e = [0, 0, 0]; e[i] = h[i]
        cp = cart(*[c[k] + e[k] for k in range(3)]); cm = cart(*[c[k] - e[k] for k in range(3)])
        J.append([(cp[k] - cm[k])/(2*h[i]) for k in range(3)])
    return [sum(J[i][k]*Ac[i] for i in range(3)) for k in range(3)]

def check(p):
    A = A_cart(p)
    r = mp.sqrt(sum(t*t for t in p)); h = r*mp.mpf(10)**-18
    D = [[0]*3 for _ in range(3)]
    for j in range(3):
        e = [0, 0, 0]; e[j] = h
        Ap = A_cart([p[k] + e[k] for k in range(3)]); Am = A_cart([p[k] - e[k] for k in range(3)])
        for i in range(3):
            D[i][j] = (Ap[i] - Am[i])/(2*h)
    S = mp.matrix(3, 3)
    for i in range(3):
        for j in range(3):
            S[i, j] = (D[i][j] + D[j][i])/2
    lam = min(mp.eigsy(S)[0])
    gradU = [((U_cart(*[p[k] + (h if k == j else 0) for k in range(3)]) -
               U_cart(*[p[k] - (h if k == j else 0) for k in range(3)]))/(2*h)) for j in range(3)]
    ratio = sum(A[i]*gradU[i] for i in range(3))/U_cart(*p)
    return lam, ratio

random.seed(0)
for r in (mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4'), mp.mpf('1e-6')):
    worst = mp.inf; rat = []
    n = 0
    while n < 60:
        th = random.uniform(0, 2*3.14159265)
        s = r*random.uniform(0.5, 1.5)
        spn = random.uniform(-1, 1) * mp.sqrt(abs(mp.cos(th))/32 + 1e-3) * s**mp.mpf(1.5)
        p = cart(s, th, spn)
        if U_cart(*p) >= 0:
            continue
        n += 1
        lam, ratio = check(p)
        worst = min(worst, lam); rat.append(ratio)
    print(f"r={mp.nstr(r,3)}: min λ(sym DA) = {mp.nstr(worst,6)}, A(U)/U ∈ [{mp.nstr(min(rat),8)}, {mp.nstr(max(rat),8)}]", flush=True)
