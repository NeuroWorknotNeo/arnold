# R41 (reviewer): символьные проверки к notes/prover/2026-10-21-morse-bott-mult.md
# [Эксперимент]. Запуск: ~/venv/bin/python checks_R41.py
import sympy as sp

ok_all = True
def check(name, cond):
    global ok_all
    print(("OK   " if cond else "FAIL ") + name)
    ok_all = ok_all and bool(cond)

# ---------------------------------------------------------------- A. Лемма A0: формула Лейбница
x = sp.symbols('x')
tau = sp.Function('tau')(x); g = sp.Function('g')(x)
for r in (1, 2, 3):
    F = tau**(2*r)*g
    vals = []
    for k in range(2*r+1):
        d = sp.diff(F, x, k)
        vals.append(sp.simplify(d.subs(tau, 0)))
    # на {tau=0}: X^k F = 0 при k<2r, X^{2r}F = (2r)! (tau')^{2r} g
    cond = all(sp.simplify(v.subs(sp.Function('tau')(x), 0)) == 0 for v in vals[:-1])
    # аккуратно: подставляем tau(x)=0, но производные tau оставляем
    dd = [sp.diff(F, x, k) for k in range(2*r+1)]
    T0 = sp.Symbol('T0'); T1 = sp.Symbol('T1')
    def at_zero(expr):
        e = expr
        for m in range(2*r+1, 0, -1):
            e = e.subs(sp.Derivative(tau, (x, m)), sp.Symbol('T%d' % m))
        e = e.subs(tau, 0)
        return sp.expand(e)
    low = all(at_zero(dd[k]) == 0 for k in range(2*r))
    top = sp.simplify(at_zero(dd[2*r]) - sp.factorial(2*r)*T1**(2*r)*g) == 0
    check(f"A0 Лейбниц r={r}: X^kF=0 (k<2r), X^(2r)F=(2r)!(X tau)^(2r) g на tau=0", low and top)

# ---------------------------------------------------------------- B. Тождество Эйлера (5.7)
s, th, ze, kap, lam, a0, beta, c, N = sp.symbols('s theta zeta kappa lambda a0 beta c N', positive=True)
Ft = sp.Function('Ft')
sig = s**(1/N); e = ze*s**(-c)
gW = s**beta*(Ft(sig, th, e) + a0)          # W o Psi
rhoYW = s*sp.diff(gW, s) - kap*th*sp.diff(gW, th) + lam*ze*sp.diff(gW, ze)
lhs = beta*gW - rhoYW
S1, T1_, E1 = sp.symbols('S1 T1 E1')
rhs = s**beta*(kap*th*sp.Subs(sp.diff(Ft(S1, T1_, E1), T1_), (S1, T1_, E1), (sig, th, e))
               + (c-lam)*e*sp.Subs(sp.diff(Ft(S1, T1_, E1), E1), (S1, T1_, E1), (sig, th, e))
               - sig/N*sp.Subs(sp.diff(Ft(S1, T1_, E1), S1), (S1, T1_, E1), (sig, th, e)))
check("(5.7): beta W - rho YW = s^beta[k th F_th + (c-lam) e F_e - sigma/N F_sigma]",
      sp.simplify((lhs - rhs).doit()) == 0)

# ---------------------------------------------------------------- C. Репер и (L3) теоремы C
# векторы в репере (omega, ell, n): тройки; d/dtheta по (1.1)
kg = sp.Function('k_g')(th)
eta0 = sp.Function('eta0')(s, th)
def dth(V):
    A, B, C = V
    return (sp.diff(A, th) - B, A + sp.diff(B, th) - kg*C, sp.diff(C, th) + kg*B)
def ds_(V):
    return tuple(sp.diff(comp, s) for comp in V)
def dze(V):
    return tuple(sp.diff(comp, ze) for comp in V)
eta = eta0 + ze
Psi = (s, 0, eta)
Ps, Pt, Pz = ds_(Psi), dth(Psi), dze(Psi)
eps = kg*eta/s
check("(5.1) kappa=lam=0: Psi_s=omega+eta0_s n, Psi_th=s(1-eps)ell+eta0_th n, Psi_ze=n",
      all(sp.simplify(a-b) == 0 for a, b in zip(Ps+Pt+Pz,
          (1, 0, sp.diff(eta0, s), 0, s*(1-eps), sp.diff(eta0, th), 0, 0, 1))))
Y = Ps   # поле Y = Psi_s как функция (s,theta,zeta)
DYY = ds_(Y)
check("теорема C: nabla_Y Y = eta0_ss n", all(sp.simplify(a-b) == 0 for a, b in zip(DYY, (0, 0, sp.diff(eta0, s, 2)))))
wo, wl, wn = sp.symbols('w_o w_l w_n')
as_ = wo; ath = wl/(s*(1-eps)); aze = wn - wo*sp.diff(eta0, s) - wl*sp.diff(eta0, th)/(s*(1-eps))
# проверка разложения w = a^s Psi_s + a^th Psi_th + a^ze Psi_ze
wrec = tuple(sp.simplify(as_*Ps[i] + ath*Pt[i] + aze*Pz[i]) for i in range(3))
check("разложение w по Psi_s, Psi_th, Psi_ze", all(sp.simplify(a-b) == 0 for a, b in zip(wrec, (wo, wl, wn))))
DwY = tuple(as_*ds_(Y)[i] + ath*dth(Y)[i] + aze*dze(Y)[i] for i in range(3))
val = s*(wo*DwY[0] + wl*DwY[1] + wn*DwY[2])
formula = ((1 - sp.diff(eta0, s)*kg)*wl**2 + sp.diff(eta0, s, th)*wl*wn)/(1-eps) + s*sp.diff(eta0, s, 2)*wo*wn
check("теорема C, п. 6: s<w,D_wY> = [(1-eta0_s k_g)w_l^2+eta0_sth w_l w_n]/(1-eps)+s eta0_ss w_o w_n",
      sp.simplify(val - formula) == 0)

# ---------------------------------------------------------------- D. Теорема D: показатели в (7.1)
for (Nn, NV, AV, GV, rp) in [(4, 2, 1, 4, 2), (2, 4, 3, 8, 2), (3, 2, 1, 6, 3), (1, 6, 5, 12, 2)]:
    if GV % (2*rp):
        continue
    B = GV//(2*rp)
    bt, cc = sp.Rational(5), sp.Rational(5, 4)
    alpha = sp.Rational(AV, Nn*NV); gam = sp.Rational(GV, Nn*NV)
    cpr = cc + gam/(2*rp); c1 = 1 + alpha; bd = bt + gam
    t = sp.symbols('t', positive=True); b1, b2 = sp.symbols('b1 b2')
    xx = t**(Nn*NV)
    u = xx**c1*b1; zz = xx**cpr*b2
    ok1 = sp.simplify(u/xx - t**AV*b1) == 0
    ok2 = sp.simplify(zz*xx**(-cc) - t**B*b2) == 0
    ok3 = sp.simplify(xx**bt*t**GV - xx**bd) == 0
    ok4 = sp.simplify(xx**(1/sp.Integer(Nn)) - t**NV) == 0
    check(f"(7.1) N={Nn},N_V={NV},A_V={AV},Gamma_V={GV},r'={rp}: u/x=t^A b1, e=t^B b2, x^beta t^Gamma=x^beta_d, sigma=t^N_V",
          ok1 and ok2 and ok3 and ok4)

# ---------------------------------------------------------------- E. Теорема Z, п. 4: уточнённые данные
for (Nn, gs_num, gs_den, rg, kp, jj) in [(2, 1, 2, 1, 2, 6), (4, 1, 4, 2, 3, 5), (3, 1, 3, 2, 1, sp.Rational(16, 3)), (1, 1, 1, 1, 2, 8)]:
    gs = sp.Rational(gs_num, gs_den)
    vs, th2, ep = sp.symbols('varsigma theta2 eprime', positive=True)
    Np = 2*rg*Nn; cc = 1 + gs; cp = cc + sp.Rational(kp, Np); bp = jj + sp.Rational(kp, Nn)
    sS = vs**Np; sigma = sS**(sp.Rational(1, Nn))
    epsg = sp.Function('epsg'); Gp = sp.Function('Gp'); Mg = sp.Function('Mg')
    y0p = vs**(2*rg*Nn*gs)*epsg(vs**(2*rg), th2)
    lhs_pt = sS*y0p + sS**cp*ep
    rhs_pt = sS**cc*(epsg(sigma, th2) + vs**kp*ep)
    okp = sp.simplify(sp.powsimp(lhs_pt - rhs_pt, force=True)) == 0
    # значение: s^j [sigma^k' G' + (vs^k' e')^{2rg} Mg] = s^{beta'} F'
    val = sS**jj*(sigma**kp*Gp(sigma, th2) + (vs**kp*ep)**(2*rg)*Mg(sigma, th2, vs**kp*ep))
    Fp = Gp(vs**(2*rg), th2) + ep**(2*rg)*Mg(vs**(2*rg), th2, vs**kp*ep)
    okv = sp.simplify(sp.powsimp(val - sS**bp*Fp, force=True)) == 0
    check(f"теорема Z п.4 (N={Nn},gamma*={gs},r_g={rg},k'={kp}): точка и (2.1) уточнённых данных", okp and okv)

# ---------------------------------------------------------------- F. Пример O2
X, Yc, Zc = sp.symbols('x y z', real=True)
rho2 = X**2 + Yc**2
U_O2 = Zc**4 - 2*Zc**2*Yc*rho2 - X**2*rho2**2 + X**7 + Yc**7
yv, theta, sv, epsv = sp.symbols('y theta s epsilon', real=True)
# U(s(omega + y n)), omega=(cos,sin,0), n=e_z
phi = sp.expand(U_O2.subs({X: sv*sp.cos(theta), Yc: sv*sp.sin(theta), Zc: sv*yv}, simultaneous=True)/sv**4)
phi = sp.simplify(phi)
P = sp.Poly(sp.expand(sp.expand_trig(phi)), sv, yv)
supp = sorted({(mon[0], mon[1]) for mon, cf in P.terms() if sp.simplify(cf) != 0})
print("   O2 носитель S (i,l):", supp)
gam_star = min(sp.Rational(i, 4 - l) for (i, l) in supp if l < 4)
check("O2: gamma* = 1/2, j = 6", gam_star == sp.Rational(1, 2))
Phi0 = sum(sp.simplify(P.coeff_monomial(sv**i*yv**l))*epsv**l for (i, l) in supp if i + gam_star*l == 4*gam_star)
check("O2: Phi_0 = (eps^2 - sin)^2 - 1", sp.simplify(sp.expand(Phi0 - ((epsv**2 - sp.sin(theta))**2 - 1))) == 0)
# (CM) в складке (0,0): кратность 3, ветвь eps_b = 0, но d^2 Phi_0(theta,0) = -4 sin theta не равно 0 тождественно
ders = [sp.simplify(sp.diff(Phi0, epsv, k).subs({theta: 0, epsv: 0})) for k in range(1, 5)]
d3 = sp.simplify(sp.diff(Phi0, epsv, 3))
d2_on_branch = sp.simplify(sp.diff(Phi0, epsv, 2).subs(epsv, 0))
check("O2 складка: d^k Phi_0(0,0)=0,0,0,24; корень d^3 Phi_0 = 24 eps -> eps_b=0; d^2 Phi_0(theta,0)=-4 sin theta",
      ders == [0, 0, 0, 24] and sp.simplify(d3 - 24*epsv) == 0 and sp.simplify(d2_on_branch + 4*sp.sin(theta)) == 0)
# профиль в складке: P = (e^2 - sin tau)^2 — нуль не изолирован
tt, ee = sp.symbols('tau e', real=True)
Pfold = sp.simplify(Phi0.subs({theta: tt, epsv: ee}) + 1)
check("O2: P в (0,0) = (e^2 - sin tau)^2; P(tau, sqrt(sin tau)) = 0", sp.simplify(Pfold - (ee**2 - sp.sin(tt))**2) == 0)
Pfold2 = sp.simplify(Phi0.subs({theta: sp.pi + tt, epsv: ee}) + 1)
check("O2: P в (pi,0) = (e^2 + sin tau)^2", sp.simplify(Pfold2 - (ee**2 + sp.sin(tt))**2) == 0)
# внутри дуги: ветви +-sqrt(sin) невырождены, G_b = -1
br = sp.sqrt(sp.sin(theta))
check("O2: внутри дуги d^2 Phi_0 = 8 sin theta > 0 на ветви, G_b = -1",
      sp.simplify(sp.diff(Phi0, epsv, 2).subs(epsv, br) - 8*sp.sin(theta)) == 0 and sp.simplify(Phi0.subs(epsv, br) + 1) == 0)
# вне дуги (sin<0): G_min = -cos^2 > -1 (min при eps=0, так как eps^4 - 2 sin eps^2 растёт)
check("O2: при sin<0 Phi_0(theta,0) = -cos^2 theta", sp.simplify(Phi0.subs(epsv, 0) + sp.cos(theta)**2) == 0)
# отрицательные значения U (не минимум): точка на дне при theta=pi/2
q = {X: 0, Yc: sp.Rational(1, 100), Zc: sp.Rational(1, 10)*sp.Rational(1, 100)**sp.Rational(3, 2)}
print("   O2: U в точке дна (0, 1e-2, 1e-2^{3/2}) =", sp.N(U_O2.subs(q)))
check("O2: U < 0 на дне (0 не минимум)", sp.N(U_O2.subs(q)) < 0)

# ---------------------------------------------------------------- G. Пример W4 (неизолированный, покрыт т. Z + W)
U_W4 = (Zc**2 - rho2**2)**2 + Zc*X**8
phiW = sp.expand(U_W4.subs({X: sv*sp.cos(theta), Yc: sv*sp.sin(theta), Zc: sv*yv}, simultaneous=True)/sv**4)
sig = sp.symbols('sigma', real=True)
# gamma*=1, N=1: y = s*eps, s = sigma
Ut = sp.simplify(sp.expand(phiW.subs({yv: sig*epsv, sv: sig})/sig**4))
check("W4: Ũ = (eps^2-1)^2 + sigma^2 cos^8 eps", sp.simplify(Ut - ((epsv**2-1)**2 + sig**2*sp.cos(theta)**8*epsv)) == 0)
# ветвь около -1: решаем d_eps Ũ = 0 рядом
a1, a2, a3 = sp.symbols('a1 a2 a3')
epsb = -1 + a1*sig**2 + a2*sig**4
eqn = sp.expand(sp.diff(Ut, epsv).subs(epsv, epsb))
sol = sp.solve([sp.expand(eqn).coeff(sig, 2), sp.expand(eqn).coeff(sig, 4)], [a1, a2], dict=True)[0]
Ghat = sp.expand(sp.series(Ut.subs(epsv, epsb.subs(sol)), sig, 0, 6).removeO())
Ghat = sp.expand(sp.expand_trig(Ghat).subs(sp.sin(theta)**2, 1 - sp.cos(theta)**2))
Ghat = sp.expand(Ghat.subs(sp.sin(theta), sp.sqrt(1 - sp.cos(theta)**2)))
print("   W4: Ĝ_- =", sp.simplify(Ghat))
check("W4: Ĝ_- = -sigma^2 cos^8 + O(sigma^4) (kappa'=2, G' = -cos^8 theta)",
      sp.simplify(Ghat.coeff(sig, 2) + sp.cos(theta)**8) == 0 and sp.simplify(Ghat.coeff(sig, 0)) == 0 and sp.simplify(Ghat.coeff(sig, 1)) == 0)
# неизолированность: grad U = 0 на {x=0, z=y^2}
grad = [sp.diff(U_W4, v) for v in (X, Yc, Zc)]
check("W4: grad U = 0 на {x=0, z=y^2}", all(sp.simplify(gr.subs({X: 0, Zc: Yc**2})) == 0 for gr in grad))

# ---------------------------------------------------------------- H. W'(W-a): алгебра неравенства Эйлера
kp_, cc_, rr = sp.symbols('kappa c r', positive=True)
Lam = sp.Function('Lam')(tt); pp = sp.Function('p')(tt, ee)
rpow = 2  # 2r' = 4 как пример
Pw = Lam + ee**(2*rpow)*pp
expr = kp_*tt*sp.diff(Pw, tt) + cc_*ee*sp.diff(Pw, ee) - kp_*Pw
target = kp_*(tt*sp.diff(Lam, tt) - Lam) + ee**(2*rpow)*((2*rpow*cc_ - kp_)*pp + cc_*ee*sp.diff(pp, ee) + kp_*tt*sp.diff(pp, tt))
check("W'(W-a): k tau P_tau + c e P_e - k P = k(tau Lam' - Lam) + e^{2r'}[(2r'c-k)p + c e p_e + k tau p_tau]",
      sp.simplify(expr - target) == 0)

print("\nИТОГ:", "все проверки OK" if ok_all else "ЕСТЬ FAIL")
