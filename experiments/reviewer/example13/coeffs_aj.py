import sympy as sp
s,d,ph,eta=sp.symbols('s d phi eta',real=True)
c,sn=sp.symbols('c sn',real=True)  # cos, sin
r2=sp.sqrt(2)
rho=(s+d)/r2; Z=(s-d)/r2
x=rho*c; y=rho*sn; z=Z
U=(x**2+y**2-z**2)**2+z**5*x+z**4*x*y+sp.Rational(1,2)*z**6
U=sp.expand(U)
# reduce with c^2+sn^2=1 : substitute after
Q2=sp.expand(((x**2+y**2-z**2)**2).subs(c**2, 1-sn**2))
print('Q2 - 4s^2d^2 =', sp.simplify(sp.expand(Q2-4*s**2*d**2).subs(c**2,1-sn**2)))
U6=sp.expand(z**5*x+z**4*x*y+sp.Rational(1,2)*z**6)
P=sp.Poly(U6,s,d)
a={}
for j in range(7):
    a[j]=sp.simplify(P.coeff_monomial(s**(6-j)*d**j))
    print(j, sp.factor(a[j]))
G=c*(1+sn)+sp.Rational(1,2)
print('a0-G/8:', sp.simplify(a[0]-G/8))
a1claim=-sp.Rational(1,8)*2*sn*c-sp.Rational(1,2)*c-sp.Rational(3,8)
print('a1-claim:', sp.simplify(a[1]-a1claim))
