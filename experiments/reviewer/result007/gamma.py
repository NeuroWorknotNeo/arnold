import numpy as np
from scipy.optimize import brentq
G=lambda f: 0.5+np.cos(f)+0.5*np.sin(2*f)
fs=np.linspace(0,2*np.pi,200001); g=G(fs)
idx=np.where(np.sign(g[:-1])!=np.sign(g[1:]))[0]
roots=[brentq(G,fs[i],fs[i+1]) for i in idx]
print("roots of Gamma:",roots, "min Gamma:",g.min(), "at", fs[g.argmin()])
for a,b in zip(roots,roots[1:]+[roots[0]+2*np.pi]):
    m=(a+b)/2; print("interval",a,b,"sign",np.sign(G(m)))
# Check: on a small sphere, {U<0} components (numerical, coarse)
