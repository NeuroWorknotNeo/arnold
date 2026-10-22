"""R47: независимая символьная проверка формул (3.2)-(3.7) записки fold (теорема X).
Абстрактный репер Дарбу: omega' = l, l' = -omega + kg n, n' = -kg l.
Вектор = тройка коэффициентов в (omega, l, n). Общие функции kg(th), Xt(th), Xe(th,e), символ c.
Контроль: Xt = Xt(th, e) -- выделяем дополнительный член.
"""
import sympy as sp

s, th, e, c, beta, N, a0 = sp.symbols('s theta epsilon c beta N a0', positive=True)
wo, wl, wn = sp.symbols('w_o w_l w_n', real=True)
kg = sp.Function('k')(th)

def dvec(v, var):
    a, b, cc = v
    if var == th:
        return (sp.diff(a, th) - b, sp.diff(b, th) + a - kg*cc, sp.diff(cc, th) + kg*b)
    return tuple(sp.diff(x, var) for x in v)

def add(*vs):
    return tuple(sp.Add(*[v[i] for v in vs]) for i in range(3))

def mul(k, v):
    return tuple(k*x for x in v)

def dot(u, v):
    return sum(u[i]*v[i] for i in range(3))

def simp(v):
    return tuple(sp.simplify(sp.expand(x)) for x in v)

def run(Xt, Xe, label):
    print('=====', label)
    Pi = (s, 0, s**c*e)
    Pis, Pith, Pie = dvec(Pi, s), dvec(Pi, th), dvec(Pi, e)
    eps_ = s**(c-1)*e*kg
    nu = s**(c-1)*(c*e - Xe)
    ok = lambda name, A, B: print(name, 'OK' if all(sp.simplify(sp.expand(A[i]-B[i])) == 0 for i in range(3)) else ('FAIL', simp(tuple(A[i]-B[i] for i in range(3)))))
    ok('(3.2) Pi_s', Pis, (1, 0, c*s**(c-1)*e))
    ok('(3.2) Pi_th', Pith, (0, s*(1-eps_), 0))
    ok('(3.2) Pi_e', Pie, (0, 0, s**c))
    Y = add(Pis, mul(-Xt/s, Pith), mul(-Xe/s, Pie))
    ok('(3.3) Y', Y, (1, -Xt*(1-eps_), nu))
    h = dot(Y, Y)
    print('(3.3) h', sp.simplify(h - (1 + Xt**2*(1-eps_)**2 + nu**2)) == 0)
    Ys, Yth, Ye = dvec(Y, s), dvec(Y, th), dvec(Y, e)
    Xtp = sp.diff(Xt, th)
    dth_eps = sp.diff(eps_, th); dth_nu = sp.diff(nu, th)
    ok('dY/ds', Ys, mul((c-1)/s, (0, Xt*eps_, nu)))
    ok('dY/dth', Yth, (Xt*(1-eps_), 1 - Xtp*(1-eps_) + Xt*dth_eps - nu*kg, dth_nu - Xt*(1-eps_)*kg))
    ok('dY/de', Ye, mul(s**(c-1), (0, Xt*kg, c - sp.diff(Xe, e))))
    sDYY = add(mul(s, Ys), mul(-Xt, Yth), mul(-Xe, Ye))
    C = (-Xt**2*(1-eps_), -Xt*(1 - Xtp*(1-eps_)), Xt**2*(1-eps_)*kg)
    rest = add(mul(c-1, (0, Xt*eps_, nu)), (0, -Xt*(Xt*dth_eps - nu*kg), -Xt*dth_nu),
               mul(-s**(c-1)*Xe, (0, Xt*kg, c - sp.diff(Xe, e))))
    ok('(3.4) sD_YY', sDYY, add(C, rest))
    # coordinates of w
    as_, ath, ae = sp.symbols('a_s a_th a_e')
    sol = sp.solve([sp.Eq(add(mul(as_, Pis), mul(ath, Pith), mul(ae, Pie))[i], (wo, wl, wn)[i]) for i in range(3)], [as_, ath, ae], dict=True)[0]
    print('a^s', sp.simplify(sol[as_] - wo) == 0,
          'a^th', sp.simplify(sol[ath] - wl/(s*(1-eps_))) == 0,
          'a^e', sp.simplify(sol[ae] - s**(-c)*(wn - c*s**(c-1)*e*wo)) == 0)
    w = (wo, wl, wn)
    DwY = add(mul(sol[as_], Ys), mul(sol[ath], Yth), mul(sol[ae], Ye))
    Q = sp.expand(s*dot(w, DwY))
    Qnote = ((1/(1-eps_) - Xtp)*wl**2 + (c - sp.diff(Xe, e))*wn**2 + Xt*wo*wl
             + ((Xt*dth_eps - nu*kg)*wl**2 + dth_nu*wl*wn)/(1-eps_)
             + (c-1)*wo*(Xt*eps_*wl + nu*wn) - c*s**(c-1)*e*wo*(Xt*kg*wl + (c - sp.diff(Xe, e))*wn))
    diff = sp.simplify(sp.together(Q - Qnote))
    print('(3.5) s<w,D_wY> - note =', diff)
    print('(3.6) <w,Y> - note =', sp.simplify(dot(w, Y) - (wo - Xt*(1-eps_)*wl + nu*wn)))
    # (3.7)
    F = sp.Function('F')
    g = s**beta*(F(s**(1/N), th, e) + a0)
    rhoYW = s*sp.diff(g, s) - Xt*sp.diff(g, th) - Xe*sp.diff(g, e)
    sig = sp.Symbol('sigma', positive=True)
    rhs = s**beta*(Xt*sp.diff(F(s**(1/N), th, e), th) + Xe*sp.diff(F(s**(1/N), th, e), e)
                   - (s**(1/N)/N)*sp.diff(F(sig, th, e), sig).subs(sig, s**(1/N)))
    print('(3.7) beta W - rho YW - note =', sp.simplify(beta*g - rhoYW - rhs))
    return diff, sDYY, add(C, rest)

Xt1 = sp.Function('X_t')(th)
Xe1 = sp.Function('X_e')(th, e)
run(Xt1, Xe1, 'triangular X^theta(theta)')

Xt2 = sp.Function('X_t')(th, e)
diff, sDYY, note34 = run(Xt2, Xe1, 'control X^theta(theta, epsilon)')
eps_ = s**(c-1)*e*kg
claimed = -sp.diff(Xt2, e)*(1-eps_)*s**(1-c)*(wn - c*s**(c-1)*e*wo)*wl
print('control: extra term in (3.5) minus claimed  =', sp.simplify(sp.together(diff - claimed)))
print('control: extra term in (3.4) =', [sp.simplify(sDYY[i]-note34[i]) for i in range(3)])
