# Independent checks of Example 13 (section 6) - [Experiment]
import sympy as sp, numpy as np
X,xi,eta=sp.symbols('X xi eta',real=True)
b1,b2=sp.symbols('b1 b2',real=True)
phi0=5*sp.pi/6
ell=sp.sqrt(X**2+xi**2); th=sp.atan(xi/X); ph=phi0+sp.sqrt(2)*th
Nh=sp.Matrix([sp.cos(ph),sp.sin(ph),1])/sp.sqrt(2)
nu=sp.Matrix([sp.cos(ph),sp.sin(ph),-1])/sp.sqrt(2)
Phi=ell*Nh+eta*nu
x,y,z=Phi
U=(x**2+y**2-z**2)**2+z**5*x+z**4*x*y+sp.Rational(1,2)*z**6
# F claimed
S=sp.sqrt(1+b1**2); phb=phi0+sp.sqrt(2)*sp.atan(b1)
F=4*(1+b1**2)*b2**2+sp.Rational(1,8)*((S-X*b2)**5*(S+X*b2)*sp.cos(phb)+(S-X*b2)**4*(S+X*b2)**2*sp.cos(phb)*sp.sin(phb)+sp.Rational(1,2)*(S-X*b2)**6)
Fsub=F.subs({b1:xi/X,b2:eta/X**2})
fU=sp.lambdify((X,xi,eta),U,'mpmath'); fF=sp.lambdify((X,xi,eta),X**6*Fsub,'mpmath')
import mpmath as mp; mp.mp.dps=50
rng=np.random.default_rng(1)
mx=0
for _ in range(30):
    Xv=mp.mpf(rng.uniform(0.001,0.66)); t1=rng.uniform(-.25,.25); t2=rng.uniform(-.25,.25)
    xv=Xv*t1; ev=Xv**2*t2
    mx=max(mx,abs(fU(Xv,xv,ev)-fF(Xv,xv,ev))/Xv**6)
print("U o Phi - X^6 F rel max:",mx)
# symbolic: X->0 limit F0, gradient, Hessian exactly
F0=F.subs(X,0)
print("F0(0)=",sp.nsimplify(sp.simplify(F0.subs({b1:0,b2:0}))), float(F0.subs({b1:0,b2:0})))
g=[sp.simplify(sp.diff(F0,v).subs({b1:0,b2:0})) for v in (b1,b2)]
print("grad:",g)
H=sp.Matrix(2,2,lambda i,j: sp.simplify(sp.diff(F0,[b1,b2][i],[b1,b2][j]).subs({b1:0,b2:0})))
print("H:",H, [float(h) for h in H])
print("claimed H11:", float((6-3*sp.sqrt(3))/16))
# second derivatives and B
J=Phi.jacobian([X,xi,eta]); B=sp.simplify(J.T*J)
fJ=sp.lambdify((X,xi,eta),J,'numpy'); fB=sp.lambdify((X,xi,eta),B,'numpy')
d2=[sp.lambdify((X,xi,eta),sp.diff(J[:,0],v),'numpy') for v in (X,xi,eta)]
def check(r0,s0,M=200000):
    worst=dict(B=0,Bxu=0,Phi2=0,Phi3=0,Phi0=0)
    for _ in range(M//1000):
        Xv=rng.uniform(1e-4,s0,1000)
        rr=r0*np.sqrt(rng.uniform(0,1,1000)); ang=rng.uniform(0,2*np.pi,1000)
        t1=rr*np.cos(ang); t2=rr*np.sin(ang)
        for Xa,a1,a2 in zip(Xv,t1,t2):
            xa=Xa*a1; ea=Xa**2*a2; bn=np.hypot(a1,a2)
            Jm=np.array(fJ(Xa,xa,ea),dtype=float); Bm=Jm.T@Jm
            nB=np.linalg.norm(Bm-np.eye(3),2); worst['B']=max(worst['B'],nB)
            worst['Bxu']=max(worst['Bxu'],np.hypot(Bm[0,1],Bm[0,2])/(r0*Xa))  # compare with omega=5 r0 X
            Y=Jm[:,0]; e=Y/np.linalg.norm(Y)
            dXX=np.array(d2[0](Xa,xa,ea),dtype=float).ravel()
            perp=dXX-e*(e@dXX)
            # (Phi2): X|perp| <= 5|b|^2+5 r0 X ; record ratio
            worst['Phi2']=max(worst['Phi2'],Xa*np.linalg.norm(perp)/(5*bn**2+5*r0*Xa))
            # (Phi3): min over w perp Y of X<w,D_wY>/|w|^2 ; D_wY = M zeta, w=J zeta
            Mm=np.column_stack([np.array(d2[k](Xa,xa,ea),dtype=float).ravel() for k in range(3)])
            Jinv=np.linalg.inv(Jm)
            Lop=Mm@Jinv  # w -> D_w Y
            # restrict to Y-perp plane
            P=np.linalg.svd(e.reshape(1,3))[2][1:]  # 2x3 basis of perp
            Sm=P@(Xa*0.5*(Lop+Lop.T))@P.T
            lmin=np.linalg.eigvalsh(Sm).min()
            worst['Phi3']=max(worst['Phi3'],-lmin/(5*bn+5*r0*Xa))
            nq=np.linalg.norm(Jm[:,0])  # dummy
    return worst
print(check(0.25,2/3,40000))
print(check(0.05,1.0,20000))
