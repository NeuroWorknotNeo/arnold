# check limit system of hand proof: h1 = 1 - sin - 2 sin^2 (=G'), h2 = sin(5c+4c sin+3)+c ; min |h1|+|h2| on circle
import numpy as np
p=np.linspace(0,2*np.pi,2000001); c=np.cos(p); sn=np.sin(p)
h1=1-sn-2*sn**2; h2=sn*(5*c+4*c*sn+3)+c
print('min |h1|+|h2| =', (np.abs(h1)+np.abs(h2)).min())
