# [Символьные тождества + Эксперимент] Тонкая трубка с бегущей перемычкой:
#   U3 = y^2 - T G,  T = x^3 - z^2,  G = (z - x^2)^2 + x^6,
#   U4 = (Y - x z)^2 - T G = U3∘Phi^{-1},  Phi(x,y,z) = (x, y + x z, z)  (несепарабельный вариант).
import sympy as sp, mpmath as mp
mp.mp.dps = 80
x,y,z,w,Y,mu,th = sp.symbols('x y z w Y mu theta', real=True)
T = x**3 - z**2; G = (z - x**2)**2 + x**6
U3 = y**2 - T*G
U4 = (Y - x*z)**2 - T*G
X3 = sp.Matrix([x,y,z]); X4 = sp.Matrix([x,Y,z])
g3 = sp.Matrix([sp.diff(U3,v) for v in X3]); g4 = sp.Matrix([sp.diff(U4,v) for v in X4])

# 1. Поле v3 = (x, y, z + x^2): <v3,gradU3> = 2 U3 + R(x,z)
v3 = sp.Matrix([x, y, z + x**2])
R = sp.expand((v3.T*g3)[0] - 2*U3)
print("1. R не зависит от y:", sp.diff(R,y) == 0)
Rw = sp.expand(R.subs(z, x**2 + w))
print("   R(x, x^2+w) =", sp.collect(Rw, w))
print("   Dv3 =", v3.jacobian(X3).tolist())
# поле v4 = Phi_* v3 = (x, Y + x z + x^3, z + x^2)
v4 = sp.Matrix([x, Y + x*z + x**3, z + x**2])
R4 = sp.expand((v4.T*g4)[0] - 2*U4)
print("   U4: <v4,gradU4> - 2U4 - R =", sp.expand(R4 - R), "; Dv4 =", v4.jacobian(X4).tolist())

# 1b. Проверка оценки R<0 на {0<x<=x0, z^2<x^3} (численно на сетке, для подстраховки)
Rf = sp.lambdify((x,z), R, 'mpmath')
mx = -mp.inf
for k in range(8, 41):
    xv = mp.mpf(10)**(-mp.mpf(k)/8)
    for j in range(-400, 401):
        zv = mp.mpf(j)/400*xv**mp.mpf('1.5')
        mx = max(mx, Rf(xv, zv)/xv**9)
print("   max R/x^9 на сетке {10^-5<=x<=0.1, |z|<x^1.5}:", mp.nstr(mx, 8))

# 2. Пары на "берегах" перед перемычкой: z = x^2 + mu x^3, y = +-sqrt(theta T G)
sub = {z: x**2 + mu*x**3}
TGs = sp.expand((T*G).subs(sub))
E3 = sp.expand((X3.T*g3)[0])
Es = sp.expand(E3.subs(sub).subs(y**2, th*TGs))
print("2. T G ~", sp.factor(sp.series(TGs, x, 0, 11).removeO()))
print("   <x,gradU3> ~", sp.factor(sp.series(Es, x, 0, 12).removeO()))

# 3. Численно: a, h, скорость сжатия минимального наклона, (tan th1 + tan th2)/h
def stats(gfun, p):
    G_ = gfun(*p); r = mp.sqrt(sum(c**2 for c in p)); xh = [c/r for c in p]
    nG = mp.sqrt(sum(c**2 for c in G_)); n = [c/nG for c in G_]
    a = sum(xh[i]*n[i] for i in range(3)); nt = [n[i]-a*xh[i] for i in range(3)]
    ntn = mp.sqrt(sum(c**2 for c in nt))
    tau0 = [-mp.asin(max(a,0))*c/ntn for c in nt]
    return dict(a=a, tan=a/ntn, tau0=tau0, xh=xh, nt=[c/ntn for c in nt], r=r)
g3f = sp.lambdify((x,y,z), list(g3), 'mpmath'); g4f = sp.lambdify((x,Y,z), list(g4), 'mpmath')
TGf = sp.lambdify((x,z), T*G, 'mpmath')
for name, gf, off in [("U3", g3f, lambda t,zz: 0), ("U4", g4f, lambda t,zz: t*zz)]:
    print("3.", name, ":  t       a(+)        a(-)         h        t*(tau0_y(+)-tau0_y(-))/h  t*(tan+ + tan-)/h   n_t(+)_z")
    for tv in ['0.01','0.003','0.001','0.0003']:
        t = mp.mpf(tv); zt = t**2 + t**3; y0 = mp.sqrt(TGf(t, zt)/2)
        P = stats(gf, [t, off(t,zt) + y0, zt]); M = stats(gf, [t, off(t,zt) - y0, zt])
        h = mp.sqrt(sum((P['xh'][i]-M['xh'][i])**2 for i in range(3)))
        print("        %-7s %11.3e %11.3e %11.3e %14.4f %18.4f %14.3e" % (tv, P['a'], M['a'], h,
              t*(P['tau0'][1]-M['tau0'][1])/h, t*(P['tan']+M['tan'])/h, P['nt'][2]))

# 4. Сечения плоскостями P_s = span{(1,0,s), e_y} для U3: phi(beta)-phi(alpha) < -pi на угловом расстоянии ~ s^{3.5}
print("4. U3, сечения:  t      s      (phi(b)-phi(a))/pi   (beta-alpha)/s^3.5")
for tv in ['0.01','0.003','0.001','0.0003']:
    t = mp.mpf(tv); zt = t**2 + t**3; s = zt/t; y0 = mp.sqrt(TGf(t,zt)/2)
    f1 = [1/mp.sqrt(1+s**2), 0, s/mp.sqrt(1+s**2)]; f2 = [0,1,0]; res = {}
    for sg in (+1,-1):
        p = [t, sg*y0, zt]; G_ = g3f(*p)
        q = (sum(p[i]*f1[i] for i in range(3)), sum(p[i]*f2[i] for i in range(3)))
        G2 = (sum(G_[i]*f1[i] for i in range(3)), sum(G_[i]*f2[i] for i in range(3)))
        phi = mp.atan2(-q[0]*G2[1]+q[1]*G2[0], -q[0]*G2[0]-q[1]*G2[1])
        res[sg] = (mp.atan2(q[1], q[0]), phi)
    (al, pa), (be, pb) = res[-1], res[+1]
    print("        %-7s %9.3e %16.8f %14.4f" % (tv, s, (pb-pa)/mp.pi, (be-al)/s**mp.mpf('3.5')))
