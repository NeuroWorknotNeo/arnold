# [Эксперимент + символьные тождества] Пример U1 = y^2 - (x^2+z^2)((z-x^2)^2 + x^6) в R^3.
import sympy as sp
import mpmath as mp
mp.mp.dps = 60

x,y,z,w,t,mu,th = sp.symbols('x y z w t mu theta', real=True)
F = (x**2+z**2)*((z-x**2)**2 + x**6)
U = y**2 - F
gU = sp.Matrix([sp.diff(U,v) for v in (x,y,z)])
X = sp.Matrix([x,y,z])

# 1. Поле v = (x, y, z + x^2):  <v, grad U> = 2U - 2P
v = sp.Matrix([x, y, z + x**2])
P = sp.expand(-((v.T*gU)[0] - 2*U)/2)
Pw = sp.expand(P.subs(z, x**2 + w))
decomp = w**2*(w**2 + 3*x**2*w + x**2 + 2*x**4 + 3*x**6) + x**8*(3 + 7*w) + 4*x**10
print("1. P не зависит от y:", sp.diff(P, y) == 0)
print("   P(z=x^2+w) - разложение =", sp.expand(Pw - decomp))
Dv = v.jacobian(X); print("   Dv =", Dv.tolist())

# 2. Асимптотика на "берегах" перед перемычкой: z = x^2 + mu x^3, y^2 = theta F
sub = {z: x**2 + mu*x**3}
Fs = sp.expand(F.subs(sub))
E = sp.expand((X.T*gU)[0])                      # <x, grad U>
Es = sp.expand(E.subs(sub).subs(y**2, th*Fs))
print("2. <x,gradU> на z=x^2+mu x^3, y^2=theta F: ряд =",
      sp.factor(sp.series(Es, x, 0, 10).removeO()))

# 3. Численно: пара p_pm = (t, +-sqrt(theta F), t^2 + mu t^3), mu=1, theta=1/2
def num(expr, vals):
    return mp.mpf(sp.N(expr.subs(vals), 60))
def analyse(tv, muv=1, thv=sp.Rational(1,2)):
    zv = tv**2 + muv*tv**3
    Fv = F.subs({x: tv, z: zv})
    y0 = sp.sqrt(thv*Fv)
    out = {}
    for sgn in (+1, -1):
        p = {x: tv, y: sgn*y0, z: zv}
        G = [num(gi, p) for gi in gU]
        pv = [mp.mpf(sp.N(tv,60)), mp.mpf(sp.N(sgn*y0,60)), mp.mpf(sp.N(zv,60))]
        r = mp.sqrt(sum(c**2 for c in pv)); xh = [c/r for c in pv]
        nG = mp.sqrt(sum(c**2 for c in G)); n = [c/nG for c in G]
        a = sum(xh[i]*n[i] for i in range(3))
        nt = [n[i] - a*xh[i] for i in range(3)]
        ntn = mp.sqrt(sum(c**2 for c in nt))
        tau0 = [-mp.asin(a)*c/ntn for c in nt]     # минимальный наклон
        # наклон поля v=(x,y,z+x^2): касательная часть w - x^ (w = v/|v|)
        vv = [pv[0], pv[1], pv[2] + pv[0]**2]; vn = mp.sqrt(sum(c**2 for c in vv))
        out[sgn] = dict(r=r, a=a, nt=nt, tau0=tau0, xh=xh, U=num(U, p),
                        vgrad=sum(vv[i]*G[i] for i in range(3)))
    pp, pm = out[1], out[-1]
    h = mp.sqrt(sum((pp['xh'][i]-pm['xh'][i])**2 for i in range(3)))   # относит. расстояние
    # средняя "скорость сжатия": разность y-компонент tau0, делённая на h
    rate = (pp['tau0'][1] - pm['tau0'][1])/h
    return pp, pm, h, rate

print("3. t        a(p+)        a(p-)        h=|x^+ - x^-|   (tau0_y(p+)-tau0_y(p-))/h   t*rate   <v,gradU>(p+)")
for tv in [sp.Rational(1,10), sp.Rational(1,30), sp.Rational(1,100), sp.Rational(1,300), sp.Rational(1,1000)]:
    pp, pm, h, rate = analyse(tv)
    print(" %-7s %12.4e %12.4e %14.4e %16.4e %10.4f %12.4e" % (str(tv), pp['a'], pm['a'], h, rate,
          rate*mp.mpf(sp.N(tv,60)), pp['vgrad']))
    assert pp['U'] < 0 and pm['U'] < 0

# 4. Компоненты касательного градиента в p+: доля "вперёд" (e_z) и "поперёк" (e_y)
pp, pm, h, rate = analyse(sp.Rational(1,100))
print("4. n_t(p+) =", [mp.nstr(c, 6) for c in pp['nt']], " n_t(p-) =", [mp.nstr(c, 6) for c in pm['nt']])
