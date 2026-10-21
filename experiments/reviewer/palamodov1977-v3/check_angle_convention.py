import numpy as np
rng=np.random.default_rng(1); bad=0
for _ in range(100000):
    X=rng.normal(size=2); G=rng.normal(size=2); Dl=rng.uniform(-np.pi,np.pi)
    det=(-X[0])*G[1]-(-X[1])*G[0]
    phi=np.arctan2(det, np.dot(-X,G))
    R=np.array([[np.cos(Dl),-np.sin(Dl)],[np.sin(Dl),np.cos(Dl)]]); v=R@X
    diff=(Dl-phi+np.pi)%(2*np.pi)-np.pi
    if (np.dot(v,G)<=0) != (abs(diff)<=np.pi/2): bad+=1
print("angle-convention mismatches:",bad)
