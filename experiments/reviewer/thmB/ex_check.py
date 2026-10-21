import sympy as sp
x,y,z=sp.symbols('x y z', real=True)
q=x**2+y**2-z**2
U=q**2+x*z**4
G=[sp.diff(U,v) for v in (x,y,z)]
print("grad U:",[sp.factor(g) for g in G])
# solve grad U = 0 over reals
sol=None
print("solve:",sol)
# Groebner basis check
GB=sp.groebner(G,x,y,z,order='lex')
print("groebner:",GB.exprs)
# radical / real solutions: case analysis
# B-conditions
th=sp.symbols('theta',real=True)
s2=sp.sqrt(2)
for sgn in (1,-1):
    om=sp.Matrix([sp.cos(th),sp.sin(th),sgn])/s2
    sub={x:om[0],y:om[1],z:om[2]}
    u4=sp.simplify(q.subs(sub)**2); u5=sp.simplify((x*z**4).subs(sub))
    H=sp.hessian(q**2,(x,y,z)).subs(sub)
    nvec=sp.Matrix([sp.cos(th),sp.sin(th),-sgn])/s2
    print("sgn",sgn,"u4 on Sigma",u4,"g",sp.simplify(u5),"H(n,n)",sp.simplify((nvec.T*H*nvec)[0]),
          "H*omega",sp.simplify(H*om).T, "H*dtheta omega", sp.simplify(H*om.diff(th)).T)
