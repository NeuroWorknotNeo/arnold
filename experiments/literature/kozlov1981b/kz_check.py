import sympy as sp
x,y,s_=sp.symbols('x y sigma',positive=True)  # x,y>0 branch
sig=sp.Rational(1,100)
Pi=x**3-y**2
a=(2,3); S=6
m=(S-a[0])*(S-a[1])
nrm=x**sp.Rational(1,2)+y**sp.Rational(1,3)
Vx=(sp.diff(Pi,x))**(sp.Rational(2*m,S-a[0])-1)
Vy=(sp.diff(Pi,y))**(sp.Rational(2*m,S-a[1])-1)
# y-derivative negative -> sign; use real odd power: (-2y)^7 = -128 y^7
Vy=-128*y**7
v=sp.Matrix([a[0]*x - sig*Vx/nrm**(2*m-S), a[1]*y - sig*Vy/nrm**(2*m-S)])
J=v.jacobian([x,y]); Js=(J+J.T)/2
f=sp.lambdify((x,y),Js,'mpmath')
import mpmath as mp
for r in [1e-1,1e-2,1e-3,1e-4]:
    M=mp.matrix(f(mp.mpf(r)**2,mp.mpf(r)**3))
    ev=mp.eigsy(M)[0]
    print(r,[mp.nstr(e,5) for e in ev])
print(J)
print(sp.N(J.subs({x:1e-8,y:1e-12})))
mp.mp.dps=40
for r in ['1e-6','1e-8','1e-10']:
    r=mp.mpf(r)
    M=mp.matrix(f(r**2,r**3)); ev=mp.eigsy(M)[0]
    print(r,[mp.nstr(e,5) for e in ev])
