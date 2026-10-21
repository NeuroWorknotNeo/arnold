import sympy as sp, mpmath as mp, random
X,xi,eta=sp.symbols('X xi eta',real=True)
phi0=5*sp.pi/6
ell=sp.sqrt(X**2+xi**2); th=sp.atan(xi/X); ph=phi0+sp.sqrt(2)*th
Nh=sp.Matrix([sp.cos(ph),sp.sin(ph),1])/sp.sqrt(2)
nu=sp.Matrix([sp.cos(ph),sp.sin(ph),-1])/sp.sqrt(2)
tau=sp.Matrix([-sp.sin(ph),sp.cos(ph),0])
Phi=ell*Nh+eta*nu
c=X/ell; s=xi/ell; e=eta/ell
cl={
 'PhiX':(Phi.diff(X), c*Nh-(1+e)*s*tau),
 'Phixi':(Phi.diff(xi), s*Nh+(1+e)*c*tau),
 'PhiXX':(Phi.diff(X,2), -eta*s**2/ell**2*Nh-(1+e)*s**2/ell*nu+2*eta*s*c/ell**2*tau),
 'PhiXxi':(Phi.diff(X,xi), eta*s*c/ell**2*Nh+(1+e)*s*c/ell*nu+eta*(s**2-c**2)/ell**2*tau),
 'PhiXeta':(Phi.diff(X,eta), -s/ell*tau)}
mp.mp.dps=40; random.seed(3)
for k,(a,b) in cl.items():
    f=sp.lambdify((X,xi,eta),a-b,'mpmath')
    m=0
    for _ in range(10):
        Xv=mp.mpf(random.uniform(0.01,0.6)); m=max(m,max(abs(t) for t in f(Xv,Xv*random.uniform(-.2,.2),Xv**2*random.uniform(-.2,.2))))
    print(k,mp.nstr(m,3))
