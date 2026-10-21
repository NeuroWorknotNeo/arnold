# [Эксперимент] Символьная проверка формул поворачивающейся полярной карты для записки
# notes/prover/2026-10-21-normal-multiplicity.md, §4 (формулы (4.2)-(4.6)).
# Отличие от experiments/prover/gt3-hardcore/frame_check.py: дно eta_0(s,theta) берётся
# ПЮИЗЁ-видным, eta_0 = s * y_0(s^(1/3), theta) с общими коэффициентами, и проверяется ещё
# формула для x<w, D_w Y> (главный член + E_r) и разложение w по координатным полям Psi.
#
# Вектор хранится тройкой коэффициентов в репере Дарбу (omega, l, n) кривой на S^2
# с натуральным параметром theta:  omega' = l,  l' = -omega + k n,  n' = -k l.
# Производная по переменной v, от которой зависит theta:
#   D_v(A,B,C) = (A_v - B th_v, B_v + (A - C k) th_v, C_v + B k th_v).
import sympy as sp

x, u, zeta, kap = sp.symbols('x u zeta kappa', positive=True)
S, TH, Z = sp.symbols('S TH Z', real=True)
sig = sp.symbols('sigma', positive=True)

kc = sp.symbols('k0:4')
ac = sp.symbols('a1:5_0:4')          # y_0 = sum a_ij sigma^i theta^j, i >= 1 (y_0(0, .) = 0)

def kf(t):
    return sum(kc[i]*t**i for i in range(4))

def y0f(sg, t):
    return sum(ac[4*(i-1) + j]*sg**i*t**j for i in range(1, 5) for j in range(4))

def eta0(s, t):
    # s > 0, sigma = s^(1/3)
    return s*y0f(s**sp.Rational(1, 3), t)

def D(vec, var, th):
    A, B, C = vec
    thv = sp.diff(th, var)
    k = kf(th)
    return (sp.diff(A, var) - B*thv, sp.diff(B, var) + (A - C*k)*thv, sp.diff(C, var) + B*k*thv)

import random
def zero(e):
    """Тождественный нуль: сначала sympy.simplify; если он не справился (дробные степени),
    то проверка в 6 случайных рациональных точках с точностью 60 знаков (|значение| < 1e-45)."""
    e = sp.expand(sp.powsimp(sp.expand(e), force=True))
    if sp.simplify(e) == 0:
        return True
    rnd = random.Random(7)
    for _ in range(6):
        sub = {v: sp.Rational(rnd.randint(-9, 9), rnd.randint(1, 9)) for v in e.free_symbols}
        for v in (x, S, sig, kap):
            if v in e.free_symbols:
                sub[v] = sp.Rational(rnd.randint(1, 9), rnd.randint(10, 19))
        val = sp.N(e.subs(sub), 60)
        if abs(val) > sp.Float('1e-45'):
            return False
    print('      (тождество подтверждено численно в 6 точках, 60 знаков; simplify не справился)')
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

# ---- координатные поля Psi(s,theta,zeta) = s omega + (eta_0 + zeta) n   (4.1)
etaS = eta0(S, TH) + Z
Psi = (S, sp.Integer(0), etaS)
PsiS, PsiT, PsiZ = D(Psi, S, TH), D(Psi, TH, TH), D(Psi, Z, TH)
eps = kf(TH)*etaS/S
e0s = sp.diff(eta0(S, TH), S)
e0t = sp.diff(eta0(S, TH), TH)
report('Psi_s = omega + eta_0,s n', vzero([a - b for a, b in zip(PsiS, (1, 0, e0s))]))
report('Psi_theta = s(1-eps) l + eta_0,theta n', vzero([a - b for a, b in zip(PsiT, (0, S*(1 - eps), e0t))]))
report('Psi_zeta = n', vzero([a - b for a, b in zip(PsiZ, (0, 0, 1))]))

# ---- карта Phi(x,u,zeta) = Psi(x, u x^-kappa, zeta), поле Y = d_x Phi   (4.2)
th = u*x**(-kap)
eta = eta0(x, th) + zeta
Phi = (x, sp.Integer(0), eta)
Y = D(Phi, x, th)
s1, t1 = sp.symbols('s1 t1', positive=True)
e0s_x = sp.diff(eta0(s1, t1), s1).subs({s1: x, t1: th})
e0t_x = sp.diff(eta0(s1, t1), t1).subs({s1: x, t1: th})
eps_x = kf(th)*eta/x
nu_x = e0s_x - kap*th*e0t_x/x
report('Y = omega - kappa theta (1-eps) l + nu n', vzero([a - b for a, b in zip(Y, (1, -kap*th*(1 - eps_x), nu_x))]))

# ---- x d_x^2 Phi   (4.3)
Yx = D(Y, x, th)
dxeps = sp.diff(eps_x, x)
dxnu = sp.diff(nu_x, x)
k = kf(th)
claim = (-kap**2*th**2*(1 - eps_x),
         -kap*th*((1 - kap) + kap*eps_x - x*dxeps - nu_x*k),
         kap**2*th**2*(1 - eps_x)*k + x*dxnu)
report('x Phi_xx formula', vzero([x*a - b for a, b in zip(Yx, claim)]))
kp = sp.diff(kf(t1), t1).subs(t1, th)
report('x d_x eps = -kappa theta k\' eta/x + k nu - eps', zero(x*dxeps - (-kap*th*kp*eta/x + k*nu_x - eps_x)))

# ---- Y как поле в координатах Psi и его производные   (4.4)
nuS = e0s - kap*TH*e0t/S
Yf = (sp.Integer(1), -kap*TH*(1 - eps), nuS)
dT = D(Yf, TH, TH); dS = D(Yf, S, TH); dZ = D(Yf, Z, TH)
kS = kf(TH)
report('d_theta Y formula', vzero([a - b for a, b in zip(dT, (kap*TH*(1 - eps),
       1 - kap*(1 - eps) + kap*TH*sp.diff(eps, TH) - nuS*kS,
       -kap*TH*(1 - eps)*kS + sp.diff(nuS, TH)))]))
report('d_s Y formula', vzero([a - b for a, b in zip(dS, (0, kap*TH*sp.diff(eps, S), sp.diff(nuS, S)))]))
report('d_zeta Y = (kappa theta k / s) l', vzero([a - b for a, b in zip(dZ, (0, kap*TH*kS/S, 0))]))

# ---- разложение w по Psi_s, Psi_theta, Psi_zeta и формула для s<w, D_w Y>   (4.5)-(4.6)
wo, wl, wn = sp.symbols('w_o w_l w_n', real=True)
w = (wo, wl, wn)
aS = wo
aT = wl/(S*(1 - eps))
aZ = wn - wo*e0s - wl*e0t/(S*(1 - eps))
recon = [aS*p + aT*q + aZ*r for p, q, r in zip(PsiS, PsiT, PsiZ)]
report('w = a^s Psi_s + a^theta Psi_theta + a^zeta Psi_zeta', vzero([a - b for a, b in zip(recon, w)]))
DwY = [aS*p + aT*q + aZ*r for p, q, r in zip(dS, dT, dZ)]
lhs = S*dot(w, DwY)
Er = (wl/(1 - eps))*((kap*TH*sp.diff(eps, TH) - nuS*kS)*wl + (-kap*TH*(1 - eps)*kS + sp.diff(nuS, TH))*wn) \
     + kap*TH*wl*wo + wo*(kap*TH*S*sp.diff(eps, S)*wl + S*sp.diff(nuS, S)*wn) + aZ*kap*TH*kS*wl
rhs = wl**2*(1/(1 - eps) - kap) + Er
report('s<w, D_w Y> = w_l^2 (1/(1-eps) - kappa) + E_r', zero(sp.together(lhs - rhs)))
# s d_s eps = k eta_0,s - eps (при постоянных theta, zeta)
report('s d_s eps = k eta_0,s - eps', zero(S*sp.diff(eps, S) - (kS*e0s - eps)))

# ---- <omega, w> для w ⟂ Y
Yv = Yf
wo_perp = sp.solve(sp.Eq(dot(Yv, w), 0), wo)[0]
report('<omega,w> = kappa theta (1-eps) w_l - nu w_n  при w ⟂ Y',
       zero(wo_perp - (kap*TH*(1 - eps)*wl - nuS*wn)))
# h = |Y|^2
report('h = 1 + kappa^2 theta^2 (1-eps)^2 + nu^2', zero(dot(Yv, Yv) - (1 + kap**2*TH**2*(1 - eps)**2 + nuS**2)))

print('ВСЕ ПРОВЕРКИ:', 'OK' if ok_all else 'ЕСТЬ ОШИБКИ')
