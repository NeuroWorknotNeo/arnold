"""Отладка: разложить sym DA в худшей точке по базису (ω радиальное, θ-касательное, нормаль)."""
import sys, random
sys.argv = ['x', '200', '1']
exec(open('thmC_k4_K.py').read().split('random.seed(1)')[0])
random.seed(1); r = mp.mpf('1e-24'); best = None; n = 0
while n < 80:
    th = random.uniform(0, 6.2831853); s = r*random.uniform(0.7, 1.3)
    sig = random.uniform(-1.2, 1.2)*s**ALPHA*(abs(mp.cos(th))/512 + 1e-4)**0.25
    p = cart(s, th, sig)
    if U_cart(*p) >= 0: continue
    n += 1; l = lam_min(p)
    if best is None or l < best[0]: best = (l, p, th, sig/s**ALPHA)
l, p, th, sh = best
rr = mp.sqrt(sum(t*t for t in p)); h = rr*mp.mpf(10)**-22
Dm = mp.matrix(3, 3)
for j in range(3):
    pp = list(p); pm = list(p); pp[j] += h; pm[j] -= h
    a, b = A_cart(pp), A_cart(pm)
    for i in range(3): Dm[i, j] = (a[i] - b[i])/(2*h)
S = (Dm + Dm.T)/2
c, sn = mp.cos(th), mp.sin(th)
e_rad = mp.matrix([c/mp.sqrt(2), sn/mp.sqrt(2), 1/mp.sqrt(2)])
e_th = mp.matrix([-sn, c, 0])
e_nor = mp.matrix([c/mp.sqrt(2), sn/mp.sqrt(2), -1/mp.sqrt(2)])
B = [e_rad, e_th, e_nor]
M = mp.matrix(3, 3)
for i in range(3):
    for j in range(3): M[i, j] = (B[i].T*S*B[j])[0]
print('λmin', mp.nstr(l, 5), 'θ', th, 'σ̂', mp.nstr(sh, 5))
print(mp.nstr(M, 5))
