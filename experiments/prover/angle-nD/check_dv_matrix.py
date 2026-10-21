# [Эксперимент] Явная матрица Dv в репере (e_r, e_theta, e_phi) для v = r*exp_{x^}(tau), n = 3:
#  Dv = [[cos t - sin t <th,tr>,  (-sin t N^T th - sinc t tau)^T],
#        [sinc t (tau + tr) + sinc'(t) <th,tr> tau,  cos t I + sinc t N + sinc'(t) tau th^T N]]
# где tau = (A,B) в репере (e_theta,e_phi), th = tau/|tau|, tr = r d_r tau, N = nabla^S sigma.
import sympy as sp, random
r, th_, ph = sp.symbols('r theta phi', positive=True)
R_ = sp.Rational
Af = R_(3,10)*sp.sin(r)*sp.cos(2*th_)*sp.exp(sp.sin(ph)) + R_(1,10)*r**2*th_
Bf = R_(1,5)*sp.cos(3*ph)*th_*r + R_(1,20)*sp.sin(th_*ph) + R_(1,100)
er  = sp.Matrix([sp.sin(th_)*sp.cos(ph), sp.sin(th_)*sp.sin(ph), sp.cos(th_)])
eth = sp.Matrix([sp.cos(th_)*sp.cos(ph), sp.cos(th_)*sp.sin(ph), -sp.sin(th_)])
eph = sp.Matrix([-sp.sin(ph), sp.cos(ph), 0])
tau3 = Af*eth + Bf*eph
t = sp.sqrt(Af**2 + Bf**2)
v = r*(sp.cos(t)*er + sp.sin(t)/t*tau3)
cols = [sp.diff(v, r), sp.diff(v, th_)/r, sp.diff(v, ph)/(r*sp.sin(th_))]
fr = [er, eth, eph]
Ddir = sp.Matrix(3,3, lambda i,j: (fr[i].T*cols[j])[0])
tau = sp.Matrix([Af, Bf]); that = tau/t
tr = r*sp.Matrix([sp.diff(Af,r), sp.diff(Bf,r)])
N = sp.Matrix([[sp.diff(Af,th_), sp.diff(Af,ph)/sp.sin(th_) - sp.cot(th_)*Bf],
               [sp.diff(Bf,th_), sp.diff(Bf,ph)/sp.sin(th_) + sp.cot(th_)*Af]])
s_ = sp.Symbol('s'); sincp = sp.diff(sp.sin(s_)/s_, s_).subs(s_, t); sinc = sp.sin(t)/t
d = lambda a,b: (a.T*b)[0]
Dform = sp.zeros(3,3)
Dform[0,0] = sp.cos(t) - sp.sin(t)*d(that, tr)
row = -sp.sin(t)*N.T*that - sinc*tau
Dform[0,1], Dform[0,2] = row[0], row[1]
col = sinc*(tau + tr) + sincp*d(that, tr)*tau
Dform[1,0], Dform[2,0] = col[0], col[1]
blk = sp.cos(t)*sp.eye(2) + sinc*N + sincp*tau*(that.T*N)
for i in range(2):
    for j in range(2): Dform[1+i,1+j] = blk[i,j]
random.seed(3); mx = 0
for k in range(10):
    vals = {r: R_(random.randint(10,90),100), th_: R_(random.randint(40,270),100), ph: R_(random.randint(0,600),100)}
    E = (Ddir - Dform).subs(vals)
    mx = max(mx, max(abs(sp.N(e, 40)) for e in E))
print("max |Dv_direct - Dv_formula| (10 точек, 40 знаков):", sp.N(mx, 5))
