# R52 [Эксперимент]: независимая проверка строгого выхода (A5) для O2 с полем X = mu' X0 из доказательства,
# прямым дифференцированием Xi = d/dt (V - delta rho^6) вдоль потока (без формулы (1.3)).
# Цель: проверить строку таблицы замечания 3 (delta = 0.01, mu' = 12 delta / C_M^2): R/mu' = 1.0000 "в складке, K_perp = 0",
# и оценку R ~ mu'(1 - 0.125 mu'/delta) (минимум у стенки при K_perp ~ (mu'/(8 delta))^2 delta rho^6 около theta ~ 0.485).
import mpmath as mp, sys
mp.mp.dps = 90
c = mp.mpf(3)/2; beta = 6; a0 = 1
CM = 45*mp.sqrt(3)/4 + 4
def psi(u):
    if u <= 0: return mp.mpf(0)
    if u >= 1: return mp.mpf(1)
    a = mp.exp(-1/u); b = mp.exp(-1/(1 - u)); return a/(a + b)
def chi(th):
    d = min(abs(th), abs(th - mp.pi)); return 1 - psi((d - mp.pi/8)/(mp.pi/8))
def X0(th, e):
    ch = chi(th)
    Xt = ch*mp.tan(th)/2
    Xe = e/4 if ch == 1 else (e**2 - (1 - ch)*mp.sin(th))/(4*e)
    return Xt, Xe
def U(q):
    x, y, z = q; r2 = x*x + y*y
    return z**4 - 2*z*z*y*r2 - x*x*r2*r2 + x**7 + y**7
def gradU(q):
    x, y, z = q; r2 = x*x + y*y
    Ux = -2*z*z*y*2*x - (2*x*r2*r2 + x*x*2*r2*2*x) + 7*x**6
    Uy = -2*z*z*r2 - 2*z*z*y*2*y - x*x*2*r2*2*y + 7*y**6
    Uz = 4*z**3 - 4*z*y*r2
    return mp.matrix([Ux, Uy, Uz])
def coords(q):
    x, y, z = q; s = mp.sqrt(x*x + y*y); th = mp.atan2(y, x); e = z/s**c; return s, th, e
def Yfield(q, mu):
    s, th, e = coords(q)
    Xt, Xe = X0(th, e); Xt *= mu; Xe *= mu
    om = mp.matrix([mp.cos(th), mp.sin(th), 0]); el = mp.matrix([-mp.sin(th), mp.cos(th), 0]); n = mp.matrix([0, 0, 1])
    return om - Xt*el + s**(c - 1)*(c*e - Xe)*n
def G(q, v, mu, delta):
    Y = Yfield(q, mu); h = (Y.T*Y)[0]; p = (v.T*Y)[0]
    rho = coords(q)[0]
    V = (v.T*v)[0]/2 - p*p/(2*h) + U(q) + a0*rho**beta
    return V - delta*rho**beta
def R_at(s, th, branch, kappa, phi, mu, delta):
    g = mp.cos(th)**7 + mp.sin(th)**7
    f2 = delta*(1 - kappa) - s*g          # W = s^6 (f^2 + s g) = delta (1-kappa) s^6
    if f2 < 0: return None
    f = branch*mp.sqrt(f2); e2 = mp.sin(th) + f
    if e2 <= 0: return None
    e = mp.sqrt(e2)                      # eps > 0 (по симметрии eps -> -eps достаточно)
    q = mp.matrix([s*mp.cos(th), s*mp.sin(th), s**c*e])
    Y = Yfield(q, mu); h = (Y.T*Y)[0]
    # базис Y^perp
    a = mp.matrix([0, 0, 1]); e1 = a - Y*((a.T*Y)[0]/h); e1 = e1/mp.norm(e1)
    e2v = mp.matrix([Y[1]*e1[2] - Y[2]*e1[1], Y[2]*e1[0] - Y[0]*e1[2], Y[0]*e1[1] - Y[1]*e1[0]]); e2v = e2v/mp.norm(e2v)
    K = kappa*delta*s**beta
    vp = mp.sqrt(2*K)*(mp.cos(phi)*e1 + mp.sin(phi)*e2v)
    p = -mp.sqrt(2*h*(a0 - delta))*s**(beta/mp.mpf(2))
    v = (p/h)*Y + vp
    E = (v.T*v)[0]/2 + U(q)
    dGq = mp.diff(lambda tau: G(q + tau*v, v, mu, delta), 0)
    Xi = dGq - (vp.T*gradU(q))[0]
    lam = -p/h
    return (s/lam)*Xi/(delta*s**beta), E/(s**beta)
delta = mp.mpf('0.01'); mu = 12*delta/CM**2
s = mp.mpf('1e-12')
print('mu\' =', mp.nstr(mu, 8))
# 1) складка theta ~ 0, K_perp = 0
for th in [mp.mpf('0.0'), mp.mpf('0.02')]:
    for br in (1, -1):
        r = R_at(s, th, br, 0, 0, mu, delta)
        if r: print('theta', th, 'branch', br, 'kappa 0: R/mu\' =', mp.nstr(r[0]/mu, 8), ' E/s^6 =', mp.nstr(r[1], 3))
# 2) около theta ~ 0.485, малые kappa, минимум по phi (Xi квадратична по v_perp: гармоники 0,1,2)
best = None
for th in [mp.mpf(x)/1000 for x in range(440, 541, 15)]:
    for br in (1, -1):
        for kappa in [mp.mpf(k) for k in ('0', '1e-9', '1e-8', '3e-8', '7e-8', '1.5e-7', '3e-7', '1e-6', '1e-5')]:
            vals = []
            for j in range(16):
                r = R_at(s, th, br, kappa, 2*mp.pi*j/16, mu, delta)
                if r is None: break
                vals.append(r[0])
            if not vals: continue
            m = min(vals)/mu
            if best is None or m < best[0]: best = (m, th, br, kappa)
            if kappa in (0, mp.mpf('7e-8'), mp.mpf('1e-6')) and br == 1 and th in (mp.mpf('0.485'),):
                print(f'theta={mp.nstr(th,4)} br={br} kappa={mp.nstr(kappa,3)}: min_phi R/mu\' = {mp.nstr(m, 6)}')
print('overall min R/mu\' on this sample:', mp.nstr(best[0], 6), ' at theta', mp.nstr(best[1], 4), ' branch', best[2], ' kappa', mp.nstr(best[3], 3))
print('prediction mu\'(1-0.125 mu\'/delta)/mu\' =', mp.nstr(1 - mp.mpf('0.125')*mu/delta, 6))
