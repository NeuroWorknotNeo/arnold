# R51: уточнённый скан около стенки для thmX_r3_R51.py: точки P = delta(1-kp), малые kp (K = kp*delta*s^beta).
# [Эксперимент].
import mpmath as mp
import thmX_r3_R51 as T

mp.mp.dps = 50
delta = mp.mpf('0.01')
CM = 15*mp.sqrt(3)/8*T.beta + 4
R = mp.sqrt(4*delta)
kmax = T.beta*delta/(CM**2*R**2)
s = mp.mpf('1e-10')


def wall_scan(kappa, kps, npsi=16, nphi=16):
    Yvec = T.make(kappa)
    best = None
    for kp in kps:
        for i in range(npsi):
            psi = 2*mp.pi*i/npsi
            r2 = delta*(1-kp)
            t = T.th0 + mp.sqrt(r2)*mp.cos(psi)
            e = mp.sqrt(r2/2)*mp.sin(psi)
            q = T.Pi(s, t, e)
            Y = Yvec(q); h = (Y.T*Y)[0]
            K = delta*s**T.beta - s**T.beta*T.P(t, e)
            o, l, n = T.frame(t)
            e1 = l - ((l.T*Y)[0]/h)*Y; e1 = e1/mp.sqrt((e1.T*e1)[0])
            e2 = n - ((n.T*Y)[0]/h)*Y - ((n.T*e1)[0])*e1; e2 = e2/mp.sqrt((e2.T*e2)[0])
            A = T.a0*s**T.beta
            p = -mp.sqrt(2*h*(A - delta*s**T.beta))
            lam = -p/h
            gU = T.gradU(q, s)
            for k in range(nphi):
                phi = 2*mp.pi*k/nphi
                vperp = mp.sqrt(2*max(K, 0))*(mp.cos(phi)*e1 + mp.sin(phi)*e2)
                v = p/h*Y + vperp
                f = lambda tau: T.Gfun(q + tau*v, v - tau*gU, Yvec, delta)
                Xi = mp.diff(f, 0, h=s*mp.mpf(10)**(-12)/mp.sqrt((v.T*v)[0]))
                val = (s/lam)*Xi/(delta*s**T.beta)
                if best is None or val < best[0]:
                    best = (val, kp, psi, phi)
    return best


kps = [mp.mpf(x) for x in ['0', '1e-5', '1e-4', '1e-3', '3e-3', '1e-2', '3e-2', '0.1', '0.3', '0.6', '0.9']]
for mult in [1, 10, 100, 300]:
    kappa = mult*kmax
    b = wall_scan(kappa, kps)
    print('kappa=%s (=%d*kmax, mu=%s): min (rho/lam)Xi/(delta rho^b)=%s  [kp=%s psi=%s phi=%s]; theorem bound mu/2=%s'
          % (mp.nstr(kappa, 4), mult, mp.nstr(2*kappa, 4), mp.nstr(b[0], 6), mp.nstr(b[1], 3), mp.nstr(b[2], 3),
             mp.nstr(b[3], 3), mp.nstr(kappa, 4)))
