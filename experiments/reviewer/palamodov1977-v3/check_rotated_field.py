import sympy as sp
r,a=sp.symbols('r alpha',positive=True)
D=sp.Function('D')(a,r)
x=r*sp.cos(a); y=r*sp.sin(a)
v=sp.Matrix([r*sp.cos(a+D), r*sp.sin(a+D)])
# Jacobian w.r.t. Cartesian via chain rule: d/dx = cos a d/dr - sin a/r d/da, d/dy = sin a d/dr + cos a / r d/da
def ddx(f): return sp.cos(a)*sp.diff(f,r)-sp.sin(a)/r*sp.diff(f,a)
def ddy(f): return sp.sin(a)*sp.diff(f,r)+sp.cos(a)/r*sp.diff(f,a)
J=sp.Matrix([[ddx(v[0]),ddy(v[0])],[ddx(v[1]),ddy(v[1])]])
er=sp.Matrix([sp.cos(a),sp.sin(a)]); ea=sp.Matrix([-sp.sin(a),sp.cos(a)])
P=sp.Matrix.hstack(er,ea)
Jp=sp.simplify(P.T*J*P)
Dr=sp.diff(D,r); Da=sp.diff(D,a)
claimed=sp.Matrix([[sp.cos(D)-r*Dr*sp.sin(D), -(1+Da)*sp.sin(D)],[sp.sin(D)+r*Dr*sp.cos(D),(1+Da)*sp.cos(D)]])
print("polar-frame Dv matches survey:", sp.simplify(Jp-claimed)==sp.zeros(2,2))
# Palamodov Cartesian form: R(D) + r(-sin(a+D),cos(a+D))^T grad D
gD=sp.Matrix([[ddx(D),ddy(D)]])
Pal=sp.Matrix([[sp.cos(D),-sp.sin(D)],[sp.sin(D),sp.cos(D)]])+r*sp.Matrix([-sp.sin(a+D),sp.cos(a+D)])*gD
print("Cartesian Dv matches P77 p.52:", sp.simplify(J-Pal)==sp.zeros(2,2))
# min eigenvalue formula (Lemma 8)
a11,a12,a21,a22=sp.symbols('a11 a12 a21 a22',real=True)
A=sp.Matrix([[a11,a12],[a21,a22]]); S=(A+A.T)/2
ev=S.eigenvals()
mu=sp.Rational(1,2)*(a11+a22-sp.sqrt(a11**2+a12**2+a21**2+a22**2-2*A.det()))
print("Lemma 8:", [sp.simplify(sp.expand((e-mu)*(e+mu-(a11+a22))) ) for e in ev])
# substitute
p,q,d=sp.symbols('p q d',real=True)  # p=r*Dr, q=Da, d=Delta
M=sp.Matrix([[sp.cos(d)-p*sp.sin(d), -(1+q)*sp.sin(d)],[sp.sin(d)+p*sp.cos(d),(1+q)*sp.cos(d)]])
rad=sp.simplify(sp.trigsimp(sum(M[i,j]**2 for i in range(2) for j in range(2))-2*M.det()))
print("radicand:", rad)
mu_sub=sp.simplify((M[0,0]+M[1,1])/2)
print("trace/2:", sp.expand(mu_sub))
