# [Эксперимент] R48: границы поля X_0 предложения O2 на замыкании N = {theta in Theta, |eps^2 - sin theta| <= 1/4}.
# Производные -- аналитически по формулам, chi' -- через производную ступеньки. Сетка 1201 x 1201 (по theta и f).
import numpy as np
def step(t):
    t = np.clip(t, 1e-300, 1-1e-16)
    a, b = np.exp(-1/t), np.exp(-1/(1-t)); return a/(a+b)
def dstep(t):
    out = np.zeros_like(t); m = (t > 0) & (t < 1); tt = t[m]
    a, b = np.exp(-1/tt), np.exp(-1/(1-tt)); da, db = a/tt**2, -b/(1-tt)**2
    out[m] = (da*(a+b) - a*(da+db))/(a+b)**2; return out
def chi_and_d(th):
    d = np.minimum(np.abs(th), np.abs(th-np.pi)); sgn = np.where(np.abs(th) < np.abs(th-np.pi), np.sign(th), np.sign(th-np.pi))
    u = (d-np.pi/8)/(np.pi/8)
    c = 1-np.where(u <= 0, 0, np.where(u >= 1, 1, step(u))); dc = -dstep(u)*sgn/(np.pi/8)
    return c, dc
th0 = np.arcsin(0.25)
TH = np.linspace(-th0, np.pi+th0, 1201)
c, dc = chi_and_d(TH)
X0t = c*np.tan(TH)/2
dX0t = dc*np.tan(TH)/2 + c/(2*np.cos(TH)**2)
print('max|X0^th| on proj N = %.4f,  M1 = max|X0^th\'| = %.4f' % (np.max(np.abs(X0t)), np.max(np.abs(dX0t))))
M2 = -np.inf; minabs_e_off = np.inf
for t, cc in zip(TH, c):
    F = np.linspace(-0.25, 0.25, 1201); e2 = np.sin(t)+F; F = F[e2 >= 0]; e2 = e2[e2 >= 0]
    for sg in (1, -1):
        e = sg*np.sqrt(e2)
        if cc == 1:
            de = np.full_like(e, 0.25)
        else:
            if np.any(e == 0): print('eps=0 with chi<1 at theta', t)
            if e.size: minabs_e_off = min(minabs_e_off, np.min(np.abs(e)))
            de = 0.25 + (1-cc)*np.sin(t)/(4*e**2)        # d/d eps [(e^2-(1-chi) sin)/(4e)]
        if e.size: M2 = max(M2, np.max(de))
print('M2 = max d_eps X0^eps = %.4f;  min|eps| where chi<1: %.4f' % (M2, minabs_e_off))
