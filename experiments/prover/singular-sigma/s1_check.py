# [Эксперимент] Пример S1 полигона: (x^2-y^2)^2 + x^5 + 2y^5 + z(x^4+y^4) + z^6.
# Полюса +-e_z (особые точки Sigma) — не овраги: phi(s,0,0) = s^2 > 0. На ветви x = y (большой круг,
# omega(phi) = (sin phi/sqrt2, sin phi/sqrt2, cos phi), натуральный параметр phi) j = 5, G = u_5|Sigma
# (u_5|Sigma не равна 0 тождественно, поэтому j = m+1 = 5 и G = g_5 = u_5|Sigma по [008], §3.3).
# Проверяем: минимум G, G'' + 5G > 0 (условие теоремы K1 [008]), H = D^2u_4(n,n) > 0 там.
import sympy as sp, mpmath as mp
mp.mp.dps = 40
x, y, z, ph, t = sp.symbols('x y z phi t', real=True)
U = (x**2 - y**2)**2 + x**5 + 2*y**5 + z*(x**4 + y**4) + z**6
u4 = (x**2 - y**2)**2; u5 = x**5 + 2*y**5 + z*(x**4 + y**4)
om = (sp.sin(ph)/sp.sqrt(2), sp.sin(ph)/sp.sqrt(2), sp.cos(ph))
G = sp.simplify(u5.subs({x: om[0], y: om[1], z: om[2]}, simultaneous=True))
print('G(phi) =', G)
n = (1/sp.sqrt(2), -1/sp.sqrt(2), 0)
Hn = sp.simplify(sp.diff(u4.subs({x: om[0] + t*n[0], y: om[1] + t*n[1], z: om[2]}, simultaneous=True), t, 2).subs(t, 0))
print('H_n(phi) =', Hn)
Gf = sp.lambdify(ph, G, 'mpmath'); G1 = sp.lambdify(ph, sp.diff(G, ph), 'mpmath'); G2 = sp.lambdify(ph, sp.diff(G, ph, 2), 'mpmath')
best = min((Gf(2*mp.pi*k/2000), 2*mp.pi*k/2000) for k in range(2000))
ps = mp.findroot(G1, best[1])
print('phi* =', mp.nstr(ps, 20), ' omega* =', [mp.nstr(mp.sin(ps)/mp.sqrt(2), 6), mp.nstr(mp.sin(ps)/mp.sqrt(2), 6), mp.nstr(mp.cos(ps), 6)])
print('G(phi*) =', mp.nstr(Gf(ps), 15), " G''(phi*) =", mp.nstr(G2(ps), 15), " G''+5G =", mp.nstr(G2(ps) + 5*Gf(ps), 15),
      ' H_n(phi*) =', mp.nstr(sp.lambdify(ph, Hn, 'mpmath')(ps), 10))
# значение в полюсах: phi(s,a,b) = U(s(a,b,+-1))/s^4 при a=b=0
s = sp.Symbol('s', positive=True)
print('U(0,0,+-s) =', sp.expand(U.subs({x: 0, y: 0, z: s})), sp.expand(U.subs({x: 0, y: 0, z: -s})))
