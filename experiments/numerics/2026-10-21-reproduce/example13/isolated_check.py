import numpy as np
# E4: U = Q^2 + z^5 x + z^4 x y + z^6/2,  Q = x^2+y^2-z^2
def grad(x,y,z):
    Q = x*x+y*y-z*z
    gx = 4*x*Q + z**5 + z**4*y
    gy = 4*y*Q + z**4*x
    gz = -4*z*Q + 5*z**4*x + 4*z**3*x*y + 3*z**5
    return np.array([gx,gy,gz])
def U(x,y,z):
    Q = x*x+y*y-z*z
    return Q*Q + z**5*x + z**4*x*y + 0.5*z**6
# roots of (1+b)^3 (4b+1)^2 - 9b
p = np.polymul(np.polymul([1,1],[1,1]),[1,1])
p = np.polymul(p, np.polymul([4,1],[4,1]))
p = np.polysub(p, [9,0])
r = np.roots(p); print("roots b:", r)
for b in r[np.abs(r.imag)<1e-9].real:
    a = -3*b/((4*b+1)*(b+1)); print("real root b=%.6f a=%.6f  a^2+b^2=%.6f"%(b,a,a*a+b*b))
# scan small spheres: min of |grad U| / r^5 over sphere (|grad| should be >= c r^5 ... at least nonzero)
rng = np.random.default_rng(0)
for rad in [1e-1,3e-2,1e-2,3e-3]:
    th = np.arccos(rng.uniform(-1,1,400000)); ph = rng.uniform(0,2*np.pi,400000)
    x = rad*np.sin(th)*np.cos(ph); y = rad*np.sin(th)*np.sin(ph); z = rad*np.cos(th)
    g = np.linalg.norm(grad(x,y,z),axis=0)
    u = U(x,y,z)
    print("r=%g  min|grad|/r^5=%.3e  min|grad|/r^3=%.3e   minU/r^6=%.3f  (U<0 fraction %.4f)"%(rad, g.min()/rad**5, g.min()/rad**3, u.min()/rad**6, (u<0).mean()))
# effective potential on the upper circle
phi = np.linspace(0,2*np.pi,100001); gp = np.cos(phi)+0.5*np.sin(2*phi)+0.5
i = gp.argmin(); print("min g+ = %.4f at phi=%.4f (5pi/6=%.4f)"%(gp[i],phi[i],5*np.pi/6))
