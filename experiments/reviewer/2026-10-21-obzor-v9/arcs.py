# Check of step 2-3 (Brunella derivation): on a small circle |q|=r, count sign changes of F,
# alternation, number of negative arcs k; isolatedness of critical point via sympy.
import numpy as np, sympy as sp
x,y=sp.symbols('x y',real=True)
cases={
 'q1q2':x*y,
 'monkey':x**3-3*x*y**2,
 'y2-x3':y**2-x**3,
 'y2-x4':y**2-x**4,
 'curved':(y-x**2)**2-x**6,
 'x4-y4+xy^3 ...':x*y*(x**2-y**2),
 'max':-(x**2+y**2),
}
for name,F in cases.items():
    g=[sp.diff(F,v) for v in (x,y)]
    sol=sp.solve(g,[x,y],dict=True)
    f=sp.lambdify((x,y),F,'numpy')
    for r in (1e-2,1e-3):
        th=np.linspace(0,2*np.pi,2_000_001)[:-1]
        v=f(r*np.cos(th),r*np.sin(th))
        s=np.sign(v)
        ch=np.sum(s!=np.roll(s,1))
        neg_arcs=np.sum((s<0)&(np.roll(s,1)>=0))
        print(f"{name:16s} r={r:g} crit={sol} signchanges={ch} neg_arcs(k)={neg_arcs} allneg={np.all(s<0)}")
