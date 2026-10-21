# GT step 3: example with beta in (k-1,k): P = y^4 - x^5 y.
import sympy as sp, numpy as np
x,y=sp.symbols('x y',positive=True)
P=y**4-x**5*y
ys=sp.solve(sp.diff(P,y),y)
print('critical y:',ys)
m=sp.simplify(P.subs(y,ys[0]))
print('min over y:',m, ' exponent beta =', sp.Rational(20,3))
# j^6 does not show: P + |q|^(13/2) > 0 near 0 (except 0)
f=lambda X,Y: Y**4-X**5*Y+(X**2+Y**2)**(13/4)
X,Y=np.meshgrid(np.linspace(-0.2,0.2,2001),np.linspace(-0.2,0.2,2001))
V=f(X,Y); mask=(X**2+Y**2)>0
print('min of P+|q|^6.5 on grid (excl 0):',V[mask].min())
# a finer check along the critical curve y=(x^5/4)^(1/3)
xs=np.logspace(-8,-0.7,200)
yc=(xs**5/4)**(1/3)
print('min along valley of P+|q|^6.5:',f(xs,yc).min(), ' sign ok:',np.all(f(xs,yc)>0))
# j^7 shows: P + o(|q|^7) along valley: P/x^7 -> -inf
print('P(x,yc)/x^7 at small x:',[(xx,(yy**4-xx**5*yy)/xx**7) for xx,yy in zip(xs[:3],yc[:3])])
# GT (vii): with x(P2)_x < (k-1)delta x^b and V=delta x^b: |x(P2)_x - bV| > (b-k+1) delta x^b, here b-k+1=2/3<1
print('beta-k+1 =', sp.Rational(20,3)-7+1)
