# [Эксперимент] Символьная проверка формул теоремы W записки
# notes/prover/2026-10-21-morse-bott-mult.md, §5.1 (формулы (5.1)-(5.7)):
# поле Y = Psi_s - (kappa theta / s) Psi_theta + lambda (zeta / s) Psi_zeta
# в координатах (s, theta, zeta) карты Psi(s,theta,zeta) = s omega(theta) + (eta_0(s,theta) + zeta) n(theta),
# где eta_0 = s * y_0(s^(1/3), theta) — дно вида ряда Пюизё (общий многочлен y_0 с y_0(0,.) = 0),
# k_g(theta) — общий кубический многочлен. lambda — произвольный параметр (в теореме lambda = c - w kappa).
#
# Вектор хранится тройкой коэффициентов в репере Дарбу (omega, l, n):
#   omega' = l,  l' = -omega + k n,  n' = -k l   (производные по theta).
# Производная по переменной v при theta = theta(v):
#   D_v(A,B,C) = (A_v - B th_v, B_v + (A - C k) th_v, C_v + B k th_v).
import random
import sympy as sp

S, TH, Z = sp.symbols('S TH Z', real=True)
kap, lam = sp.symbols('kappa lambda', real=True)
kc = sp.symbols('k0:4')
ac = sp.symbols('a1:5_0:4')


def kf(t):
    return sum(kc[i]*t**i for i in range(4))


def y0f(sg, t):
    return sum(ac[4*(i - 1) + j]*sg**i*t**j for i in range(1, 5) for j in range(4))


def eta0(s, t):
    return s*y0f(s**sp.Rational(1, 3), t)


def D(vec, var, th):
    A, B, C = vec
    thv = sp.diff(th, var)
    k = kf(th)
    return (sp.diff(A, var) - B*thv, sp.diff(B, var) + (A - C*k)*thv, sp.diff(C, var) + B*k*thv)


def zero(e):
    e = sp.expand(sp.powsimp(sp.expand(e), force=True))
    if sp.simplify(e) == 0:
        return True
    rnd = random.Random(11)
    for _ in range(6):
        sub = {v: sp.Rational(rnd.randint(-9, 9), rnd.randint(1, 9)) for v in e.free_symbols}
        if S in e.free_symbols:
            sub[S] = sp.Rational(rnd.randint(1, 9), rnd.randint(10, 19))
        val = sp.N(e.subs(sub), 60)
        if abs(val) > sp.Float('1e-45'):
            return False
    print('      (тождество подтверждено численно в 6 точках, 60 знаков)')
    return True


def vzero(v):
    return all(zero(t) for t in v)


def dot(a, b):
    return sum(p*q for p, q in zip(a, b))


ok_all = True


def report(name, flag):
    global ok_all
    ok_all = ok_all and flag
    print(('OK   ' if flag else 'FAIL ') + name)


# ---- координатные поля
etaS = eta0(S, TH) + Z
Psi = (S, sp.Integer(0), etaS)
PsiS, PsiT, PsiZ = D(Psi, S, TH), D(Psi, TH, TH), D(Psi, Z, TH)
eps = kf(TH)*etaS/S
e0s = sp.diff(eta0(S, TH), S)
e0t = sp.diff(eta0(S, TH), TH)
kS = kf(TH)
report('(5.1) Psi_s = omega + eta_0,s n', vzero([a - b for a, b in zip(PsiS, (1, 0, e0s))]))
report('(5.1) Psi_theta = s(1-eps) l + eta_0,theta n', vzero([a - b for a, b in zip(PsiT, (0, S*(1 - eps), e0t))]))
report('(5.1) Psi_zeta = n', vzero([a - b for a, b in zip(PsiZ, (0, 0, 1))]))

# ---- поле Y в координатах: Y = d_s + upsilon d_theta + (lambda zeta / s) d_zeta, upsilon = -kappa theta / s
ups = -kap*TH/S
lz = lam*Z/S
V = tuple(PsiS[i] + ups*PsiT[i] + lz*PsiZ[i] for i in range(3))
nu = e0s - kap*TH*e0t/S
nut = nu + lam*Z/S
report('(5.2) Y = omega - kappa theta (1-eps) l + nu~ n,  nu~ = nu + lambda zeta/s',
       vzero([a - b for a, b in zip(V, (1, -kap*TH*(1 - eps), nut))]))
report('(5.2) h = 1 + kappa^2 theta^2 (1-eps)^2 + nu~^2',
       zero(dot(V, V) - (1 + kap**2*TH**2*(1 - eps)**2 + nut**2)))


def Yop(vec):
    """Производная векторного поля vec(s,theta,zeta) вдоль Y."""
    dS_, dT_, dZ_ = D(vec, S, TH), D(vec, TH, TH), D(vec, Z, TH)
    return tuple(dS_[i] + ups*dT_[i] + lz*dZ_[i] for i in range(3))


# ---- производные поля
dSV, dTV, dZV = D(V, S, TH), D(V, TH, TH), D(V, Z, TH)
report('(5.3) d_theta Y', vzero([a - b for a, b in zip(dTV, (
    kap*TH*(1 - eps),
    1 - kap*(1 - eps) + kap*TH*sp.diff(eps, TH) - nut*kS,
    -kap*TH*(1 - eps)*kS + sp.diff(nut, TH)))]))
report('(5.3) d_s Y', vzero([a - b for a, b in zip(dSV, (0, kap*TH*sp.diff(eps, S), sp.diff(nut, S)))]))
report('(5.3) d_zeta Y = (kappa theta k/s) l + (lambda/s) n', vzero([a - b for a, b in zip(dZV, (0, kap*TH*kS/S, lam/S))]))

# ---- s D_Y Y   (5.4)
sDYY = tuple(S*c for c in Yop(V))
claim = (-kap**2*TH**2*(1 - eps),
         kap*TH*(S*sp.diff(eps, S) - 1 + kap*(1 - eps) - kap*TH*sp.diff(eps, TH) + nut*kS + lam*Z*kS/S),
         S*sp.diff(nut, S) + kap**2*TH**2*(1 - eps)*kS - kap*TH*sp.diff(nut, TH) + lam**2*Z/S)
report('(5.4) s D_Y Y', vzero([a - b for a, b in zip(sDYY, claim)]))
report('     s d_s eps = k eta_0,s - eps', zero(S*sp.diff(eps, S) - (kS*e0s - eps)))
report('     d_theta nu~ = d_theta nu', zero(sp.diff(nut, TH) - sp.diff(nu, TH)))
report('     s d_s nu~ = s d_s nu - lambda zeta/s', zero(S*sp.diff(nut, S) - (S*sp.diff(nu, S) - lam*Z/S)))

# ---- разложение w и формула для s<w, D_w Y>   (5.5)
wo, wl, wn = sp.symbols('w_o w_l w_n', real=True)
w = (wo, wl, wn)
aS = wo
aT = wl/(S*(1 - eps))
aZ = wn - wo*e0s - wl*e0t/(S*(1 - eps))
recon = [aS*p + aT*q + aZ*r for p, q, r in zip(PsiS, PsiT, PsiZ)]
report('(5.5) w = a^s Psi_s + a^theta Psi_theta + a^zeta Psi_zeta', vzero([a - b for a, b in zip(recon, w)]))
DwY = [aS*p + aT*q + aZ*r for p, q, r in zip(dSV, dTV, dZV)]
lhs = S*dot(w, DwY)
rhs = (wl**2*(1/(1 - eps) - kap) + kap*TH*wo*wl
       + ((kap*TH*sp.diff(eps, TH) - nut*kS)*wl**2 + sp.diff(nut, TH)*wl*wn)/(1 - eps)
       + wo*(kap*TH*S*sp.diff(eps, S)*wl + S*sp.diff(nut, S)*wn)
       - kap*TH*kS*wl*(wo*e0s + wl*e0t/(S*(1 - eps)))
       + lam*aZ*wn)
report('(5.5) s<w, D_w Y> (с сокращением членов -+ kappa theta k w_l w_n)', zero(sp.together(lhs - rhs)))

# ---- w ⟂ Y
wo_perp = sp.solve(sp.Eq(dot(V, w), 0), wo)[0]
report('(5.6) <omega,w> = kappa theta (1-eps) w_l - nu~ w_n  при w ⟂ Y',
       zero(wo_perp - (kap*TH*(1 - eps)*wl - nut*wn)))

# ---- тождество Эйлера (5.7): g = s^beta (F(s^(1/N), theta, zeta s^-c) + a0)
beta, c, a0, wgt = sp.symbols('beta c a0 w', positive=True)
Nn = sp.Integer(3)
F = sp.Function('F')
sg = S**(1/Nn)
e_ = Z*S**(-c)
g = S**beta*(F(sg, TH, e_) + a0)
lam_val = c - wgt*kap
Yg = sp.diff(g, S) + ups*sp.diff(g, TH) + (lam_val*Z/S)*sp.diff(g, Z)
s1, t1, e1 = sp.symbols('s1 t1 e1')
Fs = sp.Derivative(F(s1, t1, e1), s1).subs({s1: sg, t1: TH, e1: e_})
Ft = sp.Derivative(F(s1, t1, e1), t1).subs({s1: sg, t1: TH, e1: e_})
Fe = sp.Derivative(F(s1, t1, e1), e1).subs({s1: sg, t1: TH, e1: e_})
euler_rhs = S**beta*(kap*TH*Ft + wgt*kap*e_*Fe - (sg/Nn)*Fs)
diff_ = sp.simplify((beta*g - S*Yg - euler_rhs).doit())
diff_ = sp.simplify(sp.expand(diff_))
report('(5.7) beta W - rho Y W = s^beta [kappa theta F_theta + w kappa e F_e - (sigma/N) F_sigma]',
       diff_ == 0)

print('ВСЕ ПРОВЕРКИ:', 'OK' if ok_all else 'ЕСТЬ ОШИБКИ')
