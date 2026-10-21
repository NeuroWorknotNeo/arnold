# [Эксперимент] Сечения U1 плоскостями P_s = span{(1,0,s), e_y}: нарушение (6) из [P77, лемма 5]
# на угловом расстоянии ~ s^3, т.е. константа gamma_1 леммы 5 не равномерна по плоскостям.
import sympy as sp, mpmath as mp
mp.mp.dps = 60
x,y,z = sp.symbols('x y z', real=True)
F = (x**2+z**2)*((z-x**2)**2 + x**6)
U = y**2 - F
gU = [sp.diff(U,v) for v in (x,y,z)]
gf = sp.lambdify((x,y,z), gU, 'mpmath'); Ff = sp.lambdify((x,z), F, 'mpmath')
print(" t        s=z/x       alpha(p-)     beta(p+)   phi(alpha)/pi  phi(beta)/pi  (phi(b)-phi(a))/pi  (beta-alpha)/s^3")
for tv in ['0.1','0.03','0.01','0.003','0.001']:
    t = mp.mpf(tv); zt = t**2 + t**3; s = zt/t
    y0 = mp.sqrt(Ff(t, zt)/2)
    f1 = [1/mp.sqrt(1+s**2), 0, s/mp.sqrt(1+s**2)]; f2 = [0,1,0]
    res = {}
    for sg in (+1,-1):
        p = [t, sg*y0, zt]
        G = gf(*p)
        q = (sum(p[i]*f1[i] for i in range(3)), sum(p[i]*f2[i] for i in range(3)))
        G2 = (sum(G[i]*f1[i] for i in range(3)), sum(G[i]*f2[i] for i in range(3)))
        mq = (-q[0], -q[1])
        phi = mp.atan2(mq[0]*G2[1]-mq[1]*G2[0], mq[0]*G2[0]+mq[1]*G2[1])
        res[sg] = (mp.atan2(q[1], q[0]), phi)
    (al, pa), (be, pb) = res[-1], res[+1]
    print(" %-6s %10.3e %13.4e %12.4e %12.6f %12.6f %16.6f %14.4f" % (tv, s, al, be, pa/mp.pi, pb/mp.pi,
          (pb-pa)/mp.pi, (be-al)/s**3))
