# Independent symbolic check of Lemma 1, (1.1)-(1.3), for arbitrary U, rho, Y, A, n=3.
import sympy as sp
n=3
q=sp.symbols('q1:%d'%(n+1), real=True)
v=sp.symbols('v1:%d'%(n+1), real=True)
U=sp.Function('U')(*q)
rho=sp.Function('rho')(*q)
Y=[sp.Function('Y%d'%i)(*q) for i in range(n)]
A=sp.Function('A')
beta,delta=sp.symbols('beta delta',positive=True)
qv=sp.Matrix(q); vv=sp.Matrix(v); Yv=sp.Matrix(Y)
gradU=sp.Matrix([sp.diff(U,qi) for qi in q])
gradrho=sp.Matrix([sp.diff(rho,qi) for qi in q])
h=(Yv.T*Yv)[0]
p=(vv.T*Yv)[0]
vperp=vv-(p/h)*Yv
W=U+A(rho)
V=sp.Rational(1,2)*(vv.T*vv)[0]-p**2/(2*h)+W
def ddt(f):
    return sum(sp.diff(f,q[i])*v[i] for i in range(n))+sum(sp.diff(f,v[i])*(-gradU[i]) for i in range(n))
def Dw(Z,w):  # directional derivative of vector field Z along w
    return sp.Matrix([sum(sp.diff(Z[j],q[i])*w[i] for i in range(n)) for j in range(n)])
# Note: identity (1.1) requires <grad rho, Y> = 1. Impose by substitution: not easy for arbitrary functions;
# instead verify a version without the constraint, then add constraint terms.
# Generic: rho_dot = <grad rho, v> = (p/h)<grad rho,Y> + <grad rho, vperp>
Ap=sp.Symbol('Ap')
rhodot=ddt(rho)
# (1.2) general (without using <grad rho,Y>=1): V_dot = (p/h)<gradU,Y> + A'(rho)*rhodot - (p/h)^2<vperp,D_Y Y> - (p/h)<vperp, D_vperp Y>
Vdot=ddt(V)
DYY=Dw(Yv,Yv); Dvp=Dw(Yv,vperp)
rhs_general=(p/h)*(gradU.T*Yv)[0]+sp.diff(A(rho),rho).subs(rho,rho)*0  # placeholder
Aprime=sp.Subs(sp.Derivative(A(sp.Symbol('r')),sp.Symbol('r')),sp.Symbol('r'),rho).doit()
rhs_general=(p/h)*(gradU.T*Yv)[0]+Aprime*rhodot-(p/h)**2*(vperp.T*DYY)[0]-(p/h)*(vperp.T*Dvp)[0]
diff=sp.simplify(sp.expand(Vdot-rhs_general))
print("(1.2) generic residual:", diff)
# Now with <grad rho, Y> = 1, rhodot = p/h + <grad rho, vperp>; check algebraic identity:
gY=(gradrho.T*Yv)[0]
print("rhodot - [(p/h)<grad rho,Y> + <grad rho,vperp>]:", sp.simplify(rhodot-((p/h)*gY+(gradrho.T*vperp)[0])))
# (1.3): Xi = Vdot - beta delta rho^(beta-1) rhodot; with lambda=-p/h; under gY=1
lam=-p/h
Xi=Vdot-beta*delta*rho**(beta-1)*rhodot
YW=(gradU.T*Yv)[0]+Aprime*gY
T1=(rho/lam)*(Aprime-beta*delta*rho**(beta-1))*((gradrho-Yv/h).T*vperp)[0]
T2=-lam*rho*(vperp.T*DYY)[0]
T3=rho*(vperp.T*Dvp)[0]
res=(rho/lam)*Xi-(beta*delta*rho**beta-rho*YW+T1+T2+T3)
# residual should be proportional to (gY-1)
res=sp.simplify(sp.expand(res))
print("(1.3) residual (should vanish when <grad rho,Y>=1):")
# substitute numeric-free check: replace d rho/dq_1 by solving gY=1
sol=sp.solve(sp.Eq(gY,1), sp.diff(rho,q[0]))[0]
res2=sp.simplify(res.subs(sp.diff(rho,q[0]),sol))
print(res2)
