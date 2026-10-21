# Sanity experiment for Proposition 1 with m=5: U = Q^2 + z^4 x  (G_+ = cos(phi)/2^{5/2}, simple zeros)
import numpy as np
SQ2=np.sqrt(2.0); KAP=0.01; KAPP=0.02; ALPHA=0.5; m=5; w=(m-2)/2
def fields(x,y,z):
    rho=np.sqrt(x*x+y*y)
    s=(rho+z)/SQ2; d=(rho-z)/SQ2
    Q=(rho-z)*(rho+z)
    Ux=4*x*Q+z**4; Uy=4*y*Q; Uz=-4*z*Q+4*z**3*x
    n=(x/rho/SQ2, y/rho/SQ2, -1/SQ2+0*x)
    dU_d=Ux*n[0]+Uy*n[1]+Uz*n[2]
    dU_phi=x*Uy-y*Ux   # = -y z^4 exactly (Q-terms cancel)
    dU_phi=-y*z**4
    U=Q*Q+z**4*x
    V=[(q+(w-1)*d*ni)/m - KAP*dU_d/s**2*ni - KAPP*dU_phi/s**m*ri
       for q,ni,ri in zip((x,y,z),n,(-y,x,0*x))]
    return U,(Ux,Uy,Uz),V
def jac(x,y,z,h):
    J=np.zeros(x.shape+(3,3))
    for k in range(3):
        dx=[0j,0j,0j]; dx[k]=1j*h
        _,_,V=fields(x+dx[0],y+dx[1],z+dx[2])
        for i in range(3): J[...,i,k]=np.imag(V[i])/h
    return J
for s in [1e-1,1e-2,1e-3,1e-4]:
    ph=np.linspace(0,2*np.pi,721)[:-1]; eta=np.linspace(-1,1,401)
    P,E=np.meshgrid(ph,eta); d=s**w*E
    rho=(s+d)/SQ2; z=(s-d)/SQ2; x=rho*np.cos(P); y=rho*np.sin(P)
    J=jac(x+0j,y+0j,z+0j,1e-30*s); S=0.5*(J+np.swapaxes(J,-1,-2))
    lmin=np.linalg.eigvalsh(S)[...,0]
    U,g,V=fields(x,y,z); ip=g[0]*V[0]+g[1]*V[1]+g[2]*V[2]; neg=U<=0
    print('s=%g min eig SymDV=%.4f ; max (<gradU,V>-aU)/s^m on U<=0: %.3e ; frac U<0 %.3f'%(s,lmin.min(),((ip-ALPHA*U)/s**m)[neg].max(),neg.mean()))
