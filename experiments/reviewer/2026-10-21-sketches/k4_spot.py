# [Эксперимент] Независимая точечная проверка: поле ход 5 (V_b + евклидова поперечная коррекция, ℓ=r^{5/4}, λ=1),
# пример y-вар. K=200, r=1e-48, около точки t/r^{1/3}≈213.5, σ̂≈−7.4e−5 (из воспроизведения).
# Отличие от k4_perp.py: ∇U точный (sympy), DA — центральные разности с двумя шагами.
import sys, sympy as sp, mpmath as mp
mp.mp.dps = int(sys.argv[1]) if len(sys.argv) > 1 else 300
X, Y, Z = sp.symbols('x y z'); Kv = 200
q = X**2 + Y**2 - Z**2
Us = q**4 + X*Z**8 + Kv*q*Y*Z**6
Uf = sp.lambdify((X, Y, Z), Us, 'mpmath')
gf = sp.lambdify((X, Y, Z), [sp.diff(Us, v) for v in (X, Y, Z)], 'mpmath')
ALPHA = mp.mpf(5)/4; D = 9; LEXP = mp.mpf(5)/4; LAM = 1
def cart(s, th, sg):
    rho = (s + sg)/2; z = (s - sg)/2
    return [rho*mp.cos(th), rho*mp.sin(th), z]
def coords(x, y, z):
    rho = mp.sqrt(x*x + y*y); return rho + z, mp.atan2(y, x), rho - z
def bfun(t, r):
    u = mp.log(abs(t))/mp.log(r)
    x = (u - mp.mpf('0.05'))/(mp.mpf('0.3') - mp.mpf('0.05'))
    if x <= 0: return mp.mpf(0)
    if x >= 1: return mp.mpf(1)/3
    a = mp.exp(-1/x); b = mp.exp(-1/(1 - x)); return b/(a + b)/3
def A(p):
    r = mp.sqrt(sum(c*c for c in p)); s, th, sg = coords(*p)
    th0 = mp.pi/2 if th > 0 else -mp.pi/2; t = th - th0; b = bfun(t, r)
    rho = (s + sg)/2
    dth = [-rho*mp.sin(th), rho*mp.cos(th), 0]
    ds = [mp.cos(th)/2, mp.sin(th)/2, mp.mpf(1)/2]; dsg = [mp.cos(th)/2, mp.sin(th)/2, -mp.mpf(1)/2]
    V = [s*ds[k] + (ALPHA + b/4)*sg*dsg[k] + b*t*dth[k] for k in range(3)]
    g = gf(*p); U = Uf(*p)
    Up = sum(V[k]*g[k] for k in range(3)) - (D + b)*U
    e = [c/r for c in p]; gr = sum(g[k]*e[k] for k in range(3))
    gp = [g[k] - gr*e[k] for k in range(3)]
    den = sum(c*c for c in gp) + LAM*U*U/r**(2*LEXP)
    return [V[k] - Up*gp[k]/den for k in range(3)]
def lam_min(p, h):
    Dm = mp.matrix(3, 3)
    for j in range(3):
        pp = list(p); pm = list(p); pp[j] += h; pm[j] -= h
        a, b = A(pp), A(pm)
        for i in range(3): Dm[i, j] = (a[i] - b[i])/(2*h)
    S = (Dm + Dm.T)/2
    return min(mp.eigsy(S)[0])
r = mp.mpf('1e-48')
best = None
for sfac in ('0.7', '0.85', '1.0', '1.15', '1.3'):
    s = r*mp.mpf(sfac)
    for tt in ('200', '213.5', '230'):
        for sgn_t in (1, -1):
            for sh in ('-7.4e-5', '7.4e-5', '-2e-5', '-3e-4'):
                th = mp.pi/2 + sgn_t*mp.mpf(tt)*r**(mp.mpf(1)/3)
                p = cart(s, th, mp.mpf(sh)*s**ALPHA)
                U = Uf(*p)
                if U >= 0: continue
                rr = mp.sqrt(sum(c*c for c in p))
                h1 = rr*mp.mpf(10)**-62
                l1 = lam_min(p, h1)
                if best is None or l1 < best[0]: best = (l1, sfac, tt, sgn_t, sh, p)
print("худшая на сетке:", mp.nstr(best[0], 6), "s/r =", best[1], "t/r^(1/3) =", best[3], "*", best[2], "σ̂ =", best[4])
p = best[5]; rr = mp.sqrt(sum(c*c for c in p))
for hexp in (62, 66, 70):
    print(f"  шаг r·1e-{hexp}: λ_min = {mp.nstr(lam_min(p, rr*mp.mpf(10)**-hexp), 8)}")
g = gf(*p); Av = A(p)
print("  A(U)/U =", mp.nstr(sum(Av[k]*g[k] for k in range(3))/Uf(*p), 8), " U =", mp.nstr(Uf(*p), 5))
