import numpy as np
SQ2=np.sqrt(2.0); KAP=0.01; KAPP=0.02; ALPHA=0.5
def fields(x,y,z):
    rho=np.sqrt(x*x+y*y)
    s=(rho+z)/SQ2; d=(rho-z)/SQ2
    Q=(rho-z)*(rho+z)
    Ux=4*x*Q+z**5+z**4*y; Uy=4*y*Q+z**4*x; Uz=-4*z*Q+5*z**4*x+4*z**3*x*y+3*z**5
    n=(x/rho/SQ2, y/rho/SQ2, -1/SQ2+0*x)
    dU_d=Ux*n[0]+Uy*n[1]+Uz*n[2]
    dU_phi=z**4*(x*x-y*y-y*z)   # = x Uy - y Ux exactly
    U=Q*Q+z**5*x+z**4*x*y+0.5*z**6
    V=[ (q+d*ni)/6 - KAP*dU_d/s**2*ni - KAPP*dU_phi/s**6*ri
        for q,ni,ri in zip((x,y,z),n,(-y,x,0*x))]
    return U,(Ux,Uy,Uz),V,s,d
def jac(x,y,z,h):
    J=np.zeros(x.shape+(3,3))
    for k in range(3):
        dx=[0j,0j,0j]; dx[k]=1j*h
        _,_,V,_,_=fields(x+dx[0],y+dx[1],z+dx[2])
        for i in range(3): J[...,i,k]=np.imag(V[i])/h
    return J
# check the dU_phi identity at random point
x,y,z=0.3,-0.2,0.5
U,g,V,s,d=fields(np.array(x),np.array(y),np.array(z))
print('identity check', x*g[1]-y*g[0], z**4*(x*x-y*y-y*z))
A=0.6314; C0=np.sqrt(2*A)
print('C0',C0)
for s in [1e-1,5e-2,2e-2,1e-2,3e-3,1e-3]:
    ph=np.linspace(0,2*np.pi,721)[:-1]; eta=np.linspace(-2*C0,2*C0,401)
    P,E=np.meshgrid(ph,eta); d=s*s*E
    rho=(s+d)/SQ2; z=(s-d)/SQ2
    x=rho*np.cos(P); y=rho*np.sin(P)
    J=jac(x+0j,y+0j,z+0j,1e-30*s)
    S=0.5*(J+np.swapaxes(J,-1,-2))
    lmin=np.linalg.eigvalsh(S)[...,0]
    U,g,V,ss,dd=fields(x,y,z)
    ip=g[0]*V[0]+g[1]*V[1]+g[2]*V[2]
    neg=U<0
    # Phi = (<gradU,V> - alpha U)/s^6, check on U<=0
    Phi=(ip-ALPHA*U)/s**6
    print('s=%g min eig SymDV on N+ = %.4f ; on U<0: %.4f ; max Phi on U<0: %.3e ; min ratio <g,V>/U on U<0: %.4f ; frac U<0 %.3f'%(
        s,lmin.min(),lmin[neg].min(),Phi[neg].max(),(ip[neg]/U[neg]).min(),neg.mean()))
