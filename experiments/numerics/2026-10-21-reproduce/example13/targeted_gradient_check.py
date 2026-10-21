"""[Эксперимент, дополнение к isolated_check.py] Целевая проверка min |grad U|/r^5 в тонкой полосе
вокруг конуса Q=x^2+y^2-z^2=0 для U = Q^2 + z^5 x + z^4 x y + z^6/2.
Полоса: rho = z + delta, delta = t*r^3 (Q ~ r^4), сетка phi (4000) x t (801, [-40,40]), оба знака z.
Q считается как (rho-z)(rho+z) (без потери точности). Сравнить с isolated_check.py (случайные точки)."""
import numpy as np
def gradU(x,y,z,Q):
    gx = 4*x*Q + z**5 + z**4*y
    gy = 4*y*Q + z**4*x
    gz = -4*z*Q + 5*z**4*x + 4*z**3*x*y + 3*z**5
    return np.sqrt(gx*gx+gy*gy+gz*gz)
def U(x,y,z,Q): return Q*Q + z**5*x + z**4*x*y + 0.5*z**6
phi = np.linspace(0,2*np.pi,4000,endpoint=False)[:,None]
for r in (0.1,0.03,0.01,0.003,0.001):
    for sgn in (1,-1):
        t = np.linspace(-40,40,801)[None,:]
        # on sphere |q|=r: rho^2+z^2=r^2, rho=z+delta  -> solve z from 2z^2+2 z delta+delta^2=r^2
        delta = t*r**3
        z0 = (-delta + np.sqrt(2*r*r - delta*delta))/2
        z = sgn*z0 if sgn>0 else -(( delta + np.sqrt(2*r*r - delta*delta))/2)
        rho = np.abs(z) + (delta if sgn>0 else delta)  # cone |z|=rho; delta = rho-|z|
        if sgn<0:
            # recompute: |z|=a, rho=a+delta, a from 2a^2+2a delta+delta^2=r^2
            a = (-delta + np.sqrt(2*r*r - delta*delta))/2; rho = a+delta; z = -a
        x = rho*np.cos(phi); y = rho*np.sin(phi)
        Q = (rho-np.abs(z))*(rho+np.abs(z))
        g = gradU(x,y,z,Q)/r**5
        u = U(x,y,z,Q)/r**6
        i = np.unravel_index(np.argmin(g), g.shape)
        print(f"r={r} sgn z={sgn:+d}: min|gradU|/r^5 = {g.min():.4f} at phi={phi[i[0],0]:.3f}, t={t[0,i[1]]:.1f}, U/r^6={u[i]:.3f}; min U/r^6 = {u.min():.3f}")
