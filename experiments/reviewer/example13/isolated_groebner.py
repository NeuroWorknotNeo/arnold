import sympy as sp
x,y,z,t,b=sp.symbols('x y z t b')
U=(x**2+y**2-z**2)**2+z**5*x+z**4*x*y+sp.Rational(1,2)*z**6
g=[sp.expand(sp.diff(U,v)) for v in (x,y,z)]
GB=sp.groebner(g+[1-t*z],t,x,y,z,order='lex')
sat=[p for p in GB.exprs if not p.has(t)]
for p in sat: print(sp.factor(p)); print()
# complex lines z=0, x=±i y are critical:
for sgn in (1,-1):
    print([sp.simplify(gi.subs({z:0,x:sgn*sp.I*y})) for gi in g])
# reduced polynomial in b
p=sp.expand((1+b)**3*(4*b+1)**2-9*b)
print(sp.factor(p), ' real roots:', sp.Poly(p,b).count_roots(), [sp.N(r,8) for r in sp.real_roots(p)])
for r in sp.Poly(p,b).real_roots():
    rv=sp.N(r,30); a=-3*rv/((4*rv+1)*(rv+1)); print('b',sp.N(rv,8),'a',sp.N(a,8),'a^2+b^2',sp.N(a*a+rv*rv,8), 'a^2-b^2-b', sp.N(a*a-rv*rv-rv,5))
