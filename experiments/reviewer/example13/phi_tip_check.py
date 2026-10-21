import sympy as sp, numpy as np
s,d,eta=sp.symbols('s d eta',real=True)
c,sn=sp.symbols('c sn',real=True)
r2=sp.sqrt(2); rho=(s+d)/r2; Z=(s-d)/r2
x=rho*c; y=rho*sn; z=Z
U6=sp.expand(z**5*x+z**4*x*y+sp.Rational(1,2)*z**6)
P=sp.Poly(U6,s,d)
a=[sp.expand(P.coeff_monomial(s**(6-j)*d**j)) for j in range(7)]
# derivative wrt phi of polynomial in c,sn: dc=-sn, dsn=c
dphi=lambda f: sp.expand(-sn*sp.diff(f,c)+c*sp.diff(f,sn))
Ut=4*eta**2+sum(a[j]*s**j*eta**j for j in range(7))
Ut_eta=sp.diff(Ut,eta); Ut_phi=dphi(Ut)
ghat=sum(sp.Rational(j,6)*a[j]*s**(j-1)*eta**j for j in range(1,7))
kap=0.01; kapp=0.02; al=0.5
Phi=(1-al)*Ut+s*ghat-kap*Ut_eta**2-kapp*Ut_phi**2
fU=sp.lambdify((s,c,sn,eta),Ut,'numpy'); fP=sp.lambdify((s,c,sn,eta),Phi,'numpy')
PH=np.linspace(0,2*np.pi,8001); ET=np.linspace(-0.3,0.3,1201)
A,E=np.meshgrid(PH,ET); C=np.cos(A); S=np.sin(A)
for sv in [0.3,0.2,0.1,0.03,0.01,0.001,0.0]:
    u=fU(sv,C,S,E); p=fP(sv,C,S,E)
    m=u<=0
    print('s=%g  max Phi on {Ut<=0} = %.4e   max|eta| on {Ut<0} = %.4f'%(sv,p[m].max(),np.abs(E[u<0]).max()))
print('predicted tip values at s=0: ', -(kapp/64)*np.array([1.838**2,1.051**2]))
