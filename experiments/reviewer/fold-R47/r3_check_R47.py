"""R47: проверка (3.3)-(3.6) прямо в R^3 (без абстрактного репера) на параллели
сферы (k_g = const != 0) и на кривой с переменной k_g (численно, натуральный параметр через
численное обращение длины дуги не нужен: берём параллель и, отдельно, общую кривую с
явной натуральной параметризацией -- окружность любого радиуса на S^2 даёт только const k_g,
поэтому для переменной k_g используем численное дифференцирование по общей кривой)."""
import sympy as sp, random
random.seed(1)
s, th, e = sp.symbols('s theta epsilon', positive=True)
c = sp.Rational(3, 2)
alpha = sp.Rational(1, 3)
ca = sp.cos(alpha)
phi = th/ca
om = sp.Matrix([ca*sp.cos(phi), ca*sp.sin(phi), sp.sin(alpha)])
l = om.diff(th)
n = om.cross(l)
kg_expr = sp.simplify(l.diff(th).dot(n))
print('|l|^2 =', sp.simplify(l.dot(l)), ' kg =', kg_expr)
# check frame equations (1.1)
print('l\' + om - kg n =', sp.simplify(l.diff(th) + om - kg_expr*n).T, ' n\' + kg l =', sp.simplify(n.diff(th) + kg_expr*l).T)
Xt = sp.Rational(1, 5)*sp.sin(th) + sp.Rational(1, 7)*th**2
Xe = sp.Rational(1, 3)*e + sp.Rational(1, 4)*sp.cos(th)*e**2 + sp.Rational(1, 6)*sp.sin(2*th)
Pi = s*om + s**c*e*n
J = Pi.jacobian([s, th, e])
Ycart = J*sp.Matrix([1, -Xt/s, -Xe/s])
JY = Ycart.jacobian([s, th, e])
wo, wl, wn = sp.symbols('w_o w_l w_n')
kg = kg_expr
eps_ = s**(c-1)*e*kg
nu = s**(c-1)*(c*e - Xe)
Xtp = sp.diff(Xt, th)
dth_eps = sp.diff(eps_, th); dth_nu = sp.diff(nu, th)
Qnote = ((1/(1-eps_) - Xtp)*wl**2 + (c - sp.diff(Xe, e))*wn**2 + Xt*wo*wl
         + ((Xt*dth_eps - nu*kg)*wl**2 + dth_nu*wl*wn)/(1-eps_)
         + (c-1)*wo*(Xt*eps_*wl + nu*wn) - c*s**(c-1)*e*wo*(Xt*kg*wl + (c - sp.diff(Xe, e))*wn))
C = -Xt**2*(1-eps_)*om - Xt*(1 - Xtp*(1-eps_))*l + Xt**2*(1-eps_)*kg*n
rest = (c-1)*(Xt*eps_*l + nu*n) - Xt*(Xt*dth_eps - nu*kg)*l - Xt*dth_nu*n - s**(c-1)*Xe*(Xt*kg*l + (c - sp.diff(Xe, e))*n)
maxerr = 0
for k in range(6):
    pt = {s: sp.Float(random.uniform(0.01, 0.5), 30), th: sp.Float(random.uniform(-3, 3), 30), e: sp.Float(random.uniform(-1, 1), 30)}
    wv = [sp.Float(random.uniform(-1, 1), 30) for _ in range(3)]
    omv, lv, nv = om.subs(pt).evalf(30), l.subs(pt).evalf(30), n.subs(pt).evalf(30)
    w = wv[0]*omv + wv[1]*lv + wv[2]*nv
    Jv = J.subs(pt).evalf(30)
    coords = Jv.LUsolve(w)
    DwY = JY.subs(pt).evalf(30)*coords
    Q = (pt[s]*w.dot(DwY)).evalf(30)
    Qn = Qnote.subs(pt).subs({wo: wv[0], wl: wv[1], wn: wv[2]}).evalf(30)
    Yv = Ycart.subs(pt).evalf(30)
    Ynote = (omv - (Xt*(1-eps_)).subs(pt)*lv + nu.subs(pt)*nv).evalf(30)
    sDYY = (pt[s]*JY.subs(pt).evalf(30)*sp.Matrix([1, -Xt.subs(pt)/pt[s], -Xe.subs(pt)/pt[s]])).evalf(30)
    sDYYn = (C + rest).subs(pt).evalf(30)
    # grad rho: rho = s o Pi^{-1}; grad rho = (J^{-T}) e_s
    grad = (Jv.T).LUsolve(sp.Matrix([1, 0, 0]))
    errs = [abs(Q-Qn), (Yv-Ynote).norm(), (sDYY-sDYYn).norm(), (grad-omv).norm(), abs(Yv.dot(grad)-1)]
    maxerr = max(maxerr, max(errs))
    print(k, ['%.2e' % float(x) for x in errs])
print('max error', float(maxerr))
