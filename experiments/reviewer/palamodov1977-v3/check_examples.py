import sympy as sp
x,y,mu,a,lam=sp.symbols('x y mu a lambda',real=True)
U=(y-x**2)**2-x**6; s=y-x**2
g=sp.Matrix([sp.diff(U,x),sp.diff(U,y)])
rad=sp.expand(x*g[0]+y*g[1])
print("radial:", sp.simplify(rad-(2*s**2-2*x**2*s-6*x**6))==0)
print("on s=-mu x^3:", sp.expand(rad.subs(y,x**2-mu*x**3)))
w=sp.expand(x*g[0]+2*y*g[1])
print("(x,2y):", sp.simplify(w-(4*U-2*x**6))==0)
# isolated crit point
print(sp.solve([g[0],g[1]],[x,y],dict=True))
f=y-x**2; h=y-x**3; V=f*h
gv=sp.Matrix([sp.diff(V,x),sp.diff(V,y)])
e=sp.expand(x*gv[0]+a*y*gv[1])
print("two weights:", sp.simplify(e-(2*a*f*h+(a-2)*x**2*h+(a-3)*x**3*f))==0)
print("f=0:", sp.factor(e.subs(y,x**2)), "  g=0:", sp.factor(e.subs(y,x**3)))
