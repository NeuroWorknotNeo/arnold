# [Experiment] direct check of (A5) for example 13 in R^3 coordinates (no use of (1.3)).
import sympy as sp, mpmath as mp, random
mp.mp.dps=60
x,y,z=sp.symbols('x y z',real=True); v=sp.symbols('v1:4',real=True)
phi0=5*sp.pi/6
R=sp.sqrt(x**2+y**2); ell=(R+z)/sp.sqrt(2); eta=(R-z)/sp.sqrt(2)
th=(sp.atan2(y,x)-phi0)/sp.sqrt(2); ph=phi0+sp.sqrt(2)*th
c=sp.cos(th); s=sp.sin(th); e=eta/ell
Nh=sp.Matrix([sp.cos(ph),sp.sin(ph),1])/sp.sqrt(2); tau=sp.Matrix([-sp.sin(ph),sp.cos(ph),0])
Y=c*Nh-(1+e)*s*tau
rho=ell*c
U=(x**2+y**2-z**2)**2+z**5*x+z**4*x*y+sp.Rational(1,2)*z**6
a0=-(sp.Rational(1,16)-3*sp.sqrt(3)/32)
a0n=-(mp.mpf(1)/16-3*mp.sqrt(3)/32)
dl,bt=sp.symbols('delta beta')
vv=sp.Matrix(v); h=(Y.T*Y)[0]; p=(vv.T*Y)[0]
V=sp.Rational(1,2)*(vv.T*vv)[0]-p**2/(2*h)+U+a0*rho**6
G=V-dl*rho**6
q=[x,y,z]
gradU=[sp.diff(U,t) for t in q]
Xi=sum(sp.diff(G,q[i])*v[i] for i in range(3))-sum(sp.diff(G,v[i])*gradU[i] for i in range(3))
fXi=sp.lambdify((x,y,z,*v,dl),Xi,'mpmath')
gradrho=[sp.diff(rho,t) for t in q]
frho=sp.lambdify((x,y,z),rho,'mpmath'); fY=sp.lambdify((x,y,z),Y,'mpmath'); fU=sp.lambdify((x,y,z),U,'mpmath')
fgr=sp.lambdify((x,y,z),gradrho,'mpmath')
# chart
Xs,b1,b2=sp.symbols('X b1 b2',real=True)
S=sp.sqrt(1+b1**2); phb=phi0+sp.sqrt(2)*sp.atan(b1)
F=4*(1+b1**2)*b2**2+sp.Rational(1,8)*((S-Xs*b2)**5*(S+Xs*b2)*sp.cos(phb)+(S-Xs*b2)**4*(S+Xs*b2)**2*sp.cos(phb)*sp.sin(phb)+sp.Rational(1,2)*(S-Xs*b2)**6)
fF=sp.lambdify((Xs,b1,b2),F,'mpmath')
def Phi(X,B1,B2):
    l=X*mp.sqrt(1+B1**2); et=X**2*B2; t=mp.atan(B1); f=mp.mpf(5)*mp.pi/6+mp.sqrt(2)*t
    N=mp.matrix([mp.cos(f),mp.sin(f),1])/mp.sqrt(2); n=mp.matrix([mp.cos(f),mp.sin(f),-1])/mp.sqrt(2)
    return l*N+et*n
lam0=(6-3*mp.sqrt(3))/16/4
F00=mp.mpf(1)/16-3*mp.sqrt(3)/32
random.seed(11)
for dlv,sig in [(mp.mpf('4e-5'),mp.mpf('1e-3')),(mp.mpf('1e-4'),mp.mpf('1e-2')),(mp.mpf('1e-3'),mp.mpf('0.05'))]:
    Rb=2*mp.sqrt(dlv/lam0); worst=mp.inf; cnt=0
    while cnt<300:
        X=mp.mpf(random.uniform(0.05,1))*sig
        r=Rb*mp.sqrt(mp.mpf(random.random())); a=random.uniform(0,2*3.14159265)
        B1,B2=r*mp.cos(a),r*mp.sin(a)
        Wn=F(X,B1,B2) if False else fF(X,B1,B2)-F00
        if Wn>dlv: continue  # closure of D requires F-F0(0)<=delta
        qv=Phi(X,B1,B2); xq,yq,zq=qv[0],qv[1],qv[2]
        rh=frho(xq,yq,zq)
        Yq=mp.matrix(fY(xq,yq,zq)); hq=(Yq.T*Yq)[0]
        Kp=dlv*rh**6-Wn*X**6   # K_perp so that V = delta rho^6
        # random unit w perp Y
        w=mp.matrix([random.gauss(0,1) for _ in range(3)]); w=w-Yq*((w.T*Yq)[0]/hq); w=w/mp.norm(w)
        vperp=w*mp.sqrt(2*Kp)
        pp=-mp.sqrt(2*hq*(a0n-dlv)*rh**6)
        vq=Yq*(pp/hq)+vperp
        E=(vq.T*vq)[0]/2+fU(xq,yq,zq)
        Xi=fXi(xq,yq,zq,vq[0],vq[1],vq[2],dlv)
        lam=-pp/hq
        val=rh/lam*Xi/(dlv*rh**6)
        worst=min(worst,val); cnt+=1
    print("delta",dlv,"sigma",sig,"min (rho/lam)Xi/(delta rho^6):",mp.nstr(worst,5),"(|E| check last:",mp.nstr(abs(E)/X**6,3),")")
