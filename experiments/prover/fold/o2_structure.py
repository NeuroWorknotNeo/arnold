# [Эксперимент] Пример O2 и леммы о треугольных полях Эйлера (записка notes/prover/2026-10-21-fold.md, §§2, 4, 5).
#   U = z^4 - 2 z^2 y rho^2 - x^2 rho^4 + x^7 + y^7.
# Проверяются: тождества карты первого ребра, разложение около луча складки, формула X f = (mu'/2) f,
# численные границы для поля X на окрестности N овала, тождества лемм F2, F3 (символьно).
import sympy as sp
import mpmath as mp

x, y, z, s, th, e, t, mu = sp.symbols('x y z s theta epsilon t mu', real=True)
rho2 = x**2 + y**2
U = z**4 - 2*z**2*y*rho2 - x**2*rho2**2 + x**7 + y**7
ok_all = True


def report(name, flag):
    global ok_all
    ok_all = ok_all and bool(flag)
    print(('OK   ' if flag else 'FAIL ') + name)


# 1. глобальная запись
report('U = (z^2 - y rho^2)^2 - rho^6 + x^7 + y^7', sp.expand(U - ((z**2 - y*rho2)**2 - rho2**3 + x**7 + y**7)) == 0)
# 2. карта первого ребра: x = s cos, y = s sin, z = s^(3/2) eps
UP = U.subs({x: s*sp.cos(th), y: s*sp.sin(th), z: s**sp.Rational(3, 2)*e})
g = sp.cos(th)**7 + sp.sin(th)**7
report('U o Pi = s^6 [(eps^2 - sin)^2 - 1 + s (cos^7 + sin^7)]',
       sp.simplify(sp.expand(UP - s**6*((e**2 - sp.sin(th))**2 - 1 + s*g))) == 0)
# 3. функция дна на дуге и её минимум в складке
gt = sp.series(g.subs(th, sp.pi - t), t, 0, 8).removeO()
print('      g(pi - t) =', sp.expand(gt))
report('g(pi - t) = -1 + 7/2 t^2 + O(t^4) (минимум -1 в складке)', sp.expand(gt).coeff(t, 2) == sp.Rational(7, 2)
       and sp.expand(gt).coeff(t, 0) == -1)
gp = sp.diff(g, th)
report("g'(theta) = 7 sin cos (sin^5 - cos^5)", sp.simplify(gp - 7*sp.sin(th)*sp.cos(th)*(sp.sin(th)**5 - sp.cos(th)**5)) == 0)
# 4. около луча складки theta = pi - t: W = U + s^6 + s^7 в координатах (s, t, z)
W = (z**2 - s**3*sp.sin(t))**2 + s**7*(1 - sp.cos(t)**7 + sp.sin(t)**7)
Ut = U.subs({x: -s*sp.cos(t), y: s*sp.sin(t)})
report('U + s^6 + s^7 = (z^2 - s^3 sin t)^2 + s^7 (1 - cos^7 t + sin^7 t) (theta = pi - t)',
       sp.simplify(sp.expand(Ut + s**6 + s**7 - W)) == 0)
Wser = sp.expand(sp.series(W, t, 0, 4).removeO())
mon = sorted(set((sp.degree(m, s), sp.degree(m, t), sp.degree(m, z)) for m in sp.Add.make_args(Wser)))
print('      мономы W до t^3 (показатели s,t,z):', mon)
# грань (z^2 - s^3 t)^2: весовая однородность при w_z = (3 + w_t)/2 для любого w_t
wt = sp.symbols('w_t', positive=True)
wz = (3 + wt)/2
degs = [4*wz, 3 + wt + 2*wz, 6 + 2*wt]
report('z^4, s^3 t z^2, s^6 t^2 одного веса при w_z = (3+w_t)/2 (грань — ребро, вырождена)',
       all(sp.simplify(d - degs[0]) == 0 for d in degs))
report('s^7 t^2 всегда выше: 7 + 2 w_t - (6 + 2 w_t) = 1 > 0', True)
# 5. двухуровневый профиль у складки: W/s^7 в переменных (eps, v), f = eps^2 - sin t = -sqrt(s) v
v = sp.symbols('v', real=True)
Gt = 1 - sp.cos(t)**7 + sp.sin(t)**7
prof = (v**2 + Gt).subs(t, sp.asin(e**2 + sp.sqrt(s)*v))
lim = sp.limit(prof, s, 0)
report('предел W/s^7 при s->0 в (eps, v): v^2 + G(asin eps^2), главная часть v^2 + 7/2 eps^4',
       sp.expand(sp.series(lim, e, 0, 6).removeO() - (v**2 + sp.Rational(7, 2)*e**4)) == 0)
# 6. поле X для O2: X f = (mu'/2) f при f = eps^2 - sin theta, chi — произвольная функция
chi = sp.Function('chi')(th)
Xt = mu*chi*sp.tan(th)/2
Xe = mu*(e**2 - (1 - chi)*sp.sin(th))/(4*e)
f = e**2 - sp.sin(th)
report('X f = (mu/2) f (chi произвольна)', sp.simplify(Xt*sp.diff(f, th) + Xe*sp.diff(f, e) - mu*f/2) == 0)
report('при chi = 1: X^eps = mu eps/4 (гладко при eps = 0)', sp.simplify(Xe.subs(chi, 1) - mu*e/4) == 0)
# 7. лемма F2 (вертикальная точка): X^th = (theta - th_v), X^eps = g/g' даёт X F1 = F1, F1 = theta - th_v - g(eps)
thv = sp.symbols('theta_v', real=True)
G = sp.Function('g')(e)
F1 = th - thv - G
report('лемма F2: (theta - th_v) d_th F1 + (g/g\') d_eps F1 = F1',
       sp.simplify((th - thv)*sp.diff(F1, th) + G/sp.diff(G, e)*sp.diff(F1, e) - F1) == 0)
# 8. лемма F3 (пересечение двух графиков): a(theta) = (theta - th_p) h, X^eps = a [phi1' + (eps - phi1) m]
ph1, ph2, hh = sp.Function('phi1')(th), sp.Function('phi2')(th), sp.Function('h')(th)
a = (th - thv)*hh
m = (sp.diff(ph2, th) - sp.diff(ph1, th))/(ph2 - ph1)
XeF = a*(sp.diff(ph1, th) + (e - ph1)*m)
for i, ph in ((1, ph1), (2, ph2)):
    expr = a*sp.diff(e - ph, th) + XeF*sp.diff(e - ph, e) - a*m*(e - ph)
    report('лемма F3: X(eps - phi%d) = a m (eps - phi%d)' % (i, i), sp.simplify(expr) == 0)

# 9. численные границы поля X_0 (mu' = 1) на N = {theta in (-pi/4, 5pi/4), |f| < 1/4}
mp.mp.dps = 30


def psi(u):
    if u <= 0:
        return mp.mpf(0)
    if u >= 1:
        return mp.mpf(1)
    A, B = mp.exp(-1/u), mp.exp(-1/(1 - u))
    return A/(A + B)


def chin(T):
    d = min(abs(T), abs(T - mp.pi))
    return 1 - psi((d - mp.pi/8)/(mp.pi/8))


def X0(T, E):
    c = chin(T)
    a = c*mp.tan(T)/2 if c > 0 else mp.mpf(0)
    b = E/4 if c == 1 else (E**2 - (1 - c)*mp.sin(T))/(4*E)
    return a, b


sup = {'|X0^th|': 0, "|X0^th'|": 0, '|X0^eps|': 0, 'd_eps X0^eps (max)': -10, '|d_th X0^eps|': 0, 'min |eps| при chi<1': 10}
nT, nE = 400, 400
for i in range(nT + 1):
    T = -mp.pi/4 + (mp.mpf(3)*mp.pi/2)*i/nT
    for j in range(nE + 1):
        E = -mp.mpf('1.2') + mp.mpf('2.4')*j/nE
        if abs(E**2 - mp.sin(T)) >= mp.mpf(1)/4:
            continue
        if chin(T) < 1:
            sup['min |eps| при chi<1'] = min(sup['min |eps| при chi<1'], abs(E))
        a, b = X0(T, E)
        sup['|X0^th|'] = max(sup['|X0^th|'], abs(a))
        sup["|X0^th'|"] = max(sup["|X0^th'|"], abs(mp.diff(lambda TT: X0(TT, E)[0], T)))
        sup['|X0^eps|'] = max(sup['|X0^eps|'], abs(b))
        sup['d_eps X0^eps (max)'] = max(sup['d_eps X0^eps (max)'], mp.diff(lambda EE: X0(T, EE)[1], E))
        sup['|d_th X0^eps|'] = max(sup['|d_th X0^eps|'], abs(mp.diff(lambda TT: X0(TT, E)[1], T)))
for kk, vv in sup.items():
    print('      %-22s = %s' % (kk, mp.nstr(vv, 6)))
report('sup |X0^th| <= 1/2 на N', sup['|X0^th|'] <= mp.mpf(1)/2 + mp.mpf('1e-20'))
report('на N при chi < 1: |eps| > 0.36', sup['min |eps| при chi<1'] > mp.mpf('0.36'))
print('ИТОГ:', 'все проверки OK' if ok_all else 'есть FAIL')
