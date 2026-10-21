import numpy as np
rng=np.random.default_rng(0)
def mu(p,q,d): return np.cos(d)-0.5*p*np.sin(d)+0.5*q*np.cos(d)-0.5*np.sqrt(p*p+q*q)
def mineig(p,q,d):
    M=np.array([[np.cos(d)-p*np.sin(d), -(1+q)*np.sin(d)],[np.sin(d)+p*np.cos(d),(1+q)*np.cos(d)]])
    return np.linalg.eigvalsh((M+M.T)/2).min()
def survey_lb(p,q,d): return np.cos(d)-abs(p)-0.5*(1-np.cos(d))*q+0.5*min(q,0)
def pal_lb(p,q,d): return np.cos(d)-0.5*(abs(p)+p*np.sin(d))-0.5*(1-np.cos(d))*q+0.5*(q-abs(q))
def fixed_lb(p,q,d): return np.cos(d)-abs(p)-0.5*(1-np.cos(d))*q+min(q,0)
bad_s=bad_p=bad_f=0; maxerr=0
for _ in range(200000):
    p,q=rng.normal(scale=2,size=2); d=rng.uniform(-np.pi,np.pi)
    m=mu(p,q,d); e=mineig(p,q,d); maxerr=max(maxerr,abs(m-e))
    if survey_lb(p,q,d)>m+1e-12: bad_s+=1
    if pal_lb(p,q,d)>m+1e-12: bad_p+=1
    if fixed_lb(p,q,d)>m+1e-12: bad_f+=1
print("max |mu formula - min eig| =",maxerr)
print("violations: survey bound",bad_s," P77 bound",bad_p," corrected bound",bad_f)
print("example d=0,p=0,q=-1: mu=",mu(0,-1,0)," survey lower bound=",survey_lb(0,-1,0))
