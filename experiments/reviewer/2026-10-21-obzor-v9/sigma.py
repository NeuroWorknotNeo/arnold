# n=3 formula chi(link)=2chi(Sigma): (a) quadratic U, link of signature-(a,b) cone is S^{a-1}xS^{b-1};
# (b) [Experiment] chi(Sigma) via full subcomplex of an icosphere on {U<=0}.
import numpy as np
def chi_sphere(d): return 0 if d<0 else (2 if d%2==0 else 0)  # chi(S^d), S^{-1}=empty
print('quadratic U with n_+ plus, n_- minus squares (n=3):')
for nm in range(0,4):
    npl=3-nm
    # H=|p|^2/2+U : positive part 3+npl, negative part nm; link = S^{2+npl} x S^{nm-1}
    chi_link=chi_sphere(2+npl)*chi_sphere(nm-1)
    # Sigma={U<=0} on S^2: nm=0 empty(0); nm=1 two caps(2); nm=2 belt(0); nm=3 S^2(2)
    chiS={0:0,1:2,2:0,3:2}[nm]
    print(f'  n_-={nm}: chi(link)={chi_link}, 2chi(Sigma)={2*chiS}')
# icosphere
def icosphere(level):
    t=(1+5**0.5)/2
    V=[(-1,t,0),(1,t,0),(-1,-t,0),(1,-t,0),(0,-1,t),(0,1,t),(0,-1,-t),(0,1,-t),(t,0,-1),(t,0,1),(-t,0,-1),(-t,0,1)]
    F=[(0,11,5),(0,5,1),(0,1,7),(0,7,10),(0,10,11),(1,5,9),(5,11,4),(11,10,2),(10,7,6),(7,1,8),(3,9,4),(3,4,2),(3,2,6),(3,6,8),(3,8,9),(4,9,5),(2,4,11),(6,2,10),(8,6,7),(9,8,1)]
    V=[np.array(v,float)/np.linalg.norm(v) for v in V]
    for _ in range(level):
        cache={};NF=[]
        def mid(a,b):
            k=(min(a,b),max(a,b))
            if k not in cache:
                m=(V[a]+V[b]);V.append(m/np.linalg.norm(m));cache[k]=len(V)-1
            return cache[k]
        for a,b,c in F:
            ab,bc,ca=mid(a,b),mid(b,c),mid(c,a)
            NF+= [(a,ab,ca),(b,bc,ab),(c,ca,bc),(ab,bc,ca)]
        F=NF
    return np.array(V),F
Vx,Fs=icosphere(6)
E=set()
for a,b,c in Fs:
    for e in ((a,b),(b,c),(c,a)): E.add((min(e),max(e)))
def chi_sub(U,eps):
    P=eps*Vx; val=U(P[:,0],P[:,1],P[:,2]); inS=val<=0
    nv=inS.sum(); ne=sum(1 for a,b in E if inS[a] and inS[b]); nf=sum(1 for a,b,c in Fs if inS[a] and inS[b] and inS[c])
    return nv-ne+nf
tests={'z^2-x^2-y^2':lambda x,y,z:z**2-x**2-y**2,
       'x^2-y^2-z^2 ':lambda x,y,z:x**2-y**2-z**2,
       'x^3-3xy^2+z^2':lambda x,y,z:x**3-3*x*y**2+z**2,
       '-(x^2+y^2+z^2)':lambda x,y,z:-(x**2+y**2+z**2),
       'z^2-x^4-y^4':lambda x,y,z:z**2-x**4-y**4}
for n,U in tests.items():
    print(n,[chi_sub(U,e) for e in (0.3,0.1,0.03)])
