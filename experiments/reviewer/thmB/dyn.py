# [Experiment] exit times from B_rho for E<0 motions of U=(x^2+y^2-z^2)^2+x z^4 vs Lemma 1 bound
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
rho=0.1
def U(p):
    x,y,z=p; q=x*x+y*y-z*z; return q*q+x*z**4
def gU(p):
    x,y,z=p; q=x*x+y*y-z*z
    return np.array([4*x*q+z**4, 4*y*q, -4*z*q+4*x*z**3])
def rhs(t,s): return np.concatenate([s[3:], -gU(s[:3])])
# min of U on closed ball (sample + local opt)
rng=np.random.default_rng(0)
best=0
for k in range(20000):
    p=rng.normal(size=3); p=p/np.linalg.norm(p)*rho*rng.random()**(1/3)
    best=min(best,U(p))
umin=best
for k in range(50):
    p=rng.normal(size=3); p=p/np.linalg.norm(p)*rho
    r=minimize(lambda v: U(v) if np.linalg.norm(v)<=rho else 1.0, p, method='Nelder-Mead',options={'xatol':1e-12,'fatol':1e-16})
    umin=min(umin,r.fun)
print("min U on ball ~",umin)
M=0.2*rho*1.05   # |A|<=~0.2|x| from field numerics, with margin
def exitev(t,s): return np.dot(s[:3],s[:3])-rho**2
exitev.terminal=True; exitev.direction=1
worst=0; n=0
while n<200:
    p=rng.normal(size=3); p=p/np.linalg.norm(p)*rho*0.9*rng.random()
    if U(p)>=0: continue
    v0=rng.normal(size=3); v0*=rng.random()*np.sqrt(-U(p))  # keep E<0
    E=0.5*v0@v0+U(p)
    if E>=0: continue
    n+=1
    vmax=np.sqrt(2*(E-umin)); T=2*vmax*M/abs(E)
    sol=solve_ivp(rhs,[0,3*T],np.concatenate([p,v0]),events=exitev,rtol=1e-10,atol=1e-14)
    sol2=solve_ivp(rhs,[0,3*T],np.concatenate([p,-v0]),events=exitev,rtol=1e-10,atol=1e-14)
    tf=sol.t_events[0][0] if len(sol.t_events[0]) else np.inf
    tb=sol2.t_events[0][0] if len(sol2.t_events[0]) else np.inf
    worst=max(worst,(tf+tb)/T)
print("max over 200 motions of (time spent in B_rho)/(bound 2vM/|E|) =",worst)
