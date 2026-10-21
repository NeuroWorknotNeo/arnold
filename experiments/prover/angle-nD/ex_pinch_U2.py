# [Эксперимент + тождество] Несепарабельный вариант U2(x,Y,z) = (Y - x z)^2 - F(x,z) = U1∘Phi^{-1},
# Phi(x,y,z) = (x, y + x z, z).  Поле v2 = Phi_* v1 = (x, Y + x z + x^3, z + x^2).
import sympy as sp, mpmath as mp
mp.mp.dps = 60
x,Y,z,w = sp.symbols('x Y z w', real=True)
F = (x**2+z**2)*((z-x**2)**2 + x**6)
U2 = (Y - x*z)**2 - F
X = sp.Matrix([x,Y,z]); g = sp.Matrix([sp.diff(U2,v) for v in X])
v2 = sp.Matrix([x, Y + x*z + x**3, z + x**2])
P = sp.expand(-((v2.T*g)[0] - 2*U2)/2)
decomp = w**2*(w**2 + 3*x**2*w + x**2 + 2*x**4 + 3*x**6) + x**8*(3 + 7*w) + 4*x**10
print("<v2,gradU2> = 2 U2 - 2 P, P - (то же P, что для U1) =", sp.expand(P.subs(z, x**2+w) - decomp))
print("Dv2 =", v2.jacobian(X).tolist())
# минимальный наклон на "берегах" Y = x z +- sqrt(F/2) при z = x^2 + x^3
gf = sp.lambdify((x,Y,z), list(g), 'mpmath'); Ff = sp.lambdify((x,z), F, 'mpmath')
def tau0(p):
    G = gf(*p); r = mp.sqrt(sum(c**2 for c in p)); xh=[c/r for c in p]
    nG = mp.sqrt(sum(c**2 for c in G)); n=[c/nG for c in G]
    a = sum(xh[i]*n[i] for i in range(3)); nt=[n[i]-a*xh[i] for i in range(3)]
    ntn = mp.sqrt(sum(c**2 for c in nt))
    ap = max(a, 0)
    return a, [-mp.asin(ap)*c/ntn for c in nt], xh, a/mp.sqrt(1-a**2)   # a_+ ; signed tan(theta)
print(" t        a(q+)       a(q-)        h          t*(tau0_Y(q+)-tau0_Y(q-))/h   (tan th+ + tan th-)/h")
for tv in ['0.03','0.01','0.003','0.001']:
    t = mp.mpf(tv); zt = t**2+t**3; y0 = mp.sqrt(Ff(t,zt)/2)
    ap, tp, xp, Tp = tau0([t, t*zt + y0, zt]); am, tm, xm, Tm = tau0([t, t*zt - y0, zt])
    h = mp.sqrt(sum((xp[i]-xm[i])**2 for i in range(3)))
    print(" %-6s %11.4e %11.4e %11.4e %12.4f %22.4e" % (tv, ap, am, h, t*(tp[1]-tm[1])/h, (Tp+Tm)/h))
