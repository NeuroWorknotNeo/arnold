# [Эксперимент] Символьная проверка формул карт записки notes/prover/2026-10-21-morse-bott.md.
# Векторы — тройки коэффициентов в подвижном репере (omega, T, n) кривой Sigma_0 на S^2
# (натуральный параметр theta): omega' = T, T' = -omega + k n, n' = -k T.
# Производная по переменной v: D_v(a,b,c) = (a_v - b th_v, b_v + (a - c k) th_v, c_v + b k th_v).
# k(theta), eta*(s,theta), tau_v(x) — многочлены общего вида с символьными коэффициентами.
import sympy as sp

kc = sp.symbols('k0:3')
ac = sp.symbols('a0:3_0:3')
tc = sp.symbols('t1:3')
def kf(t): return sum(kc[i]*t**i for i in range(3))
def etaf(s, t): return sum(ac[3*i + j]*s**(i + 1)*t**j for i in range(3) for j in range(3))
def tauf(x): return sum(tc[i]*x**(i + 1) for i in range(2))   # роль ряда Пюизё: любая гладкая tau(x)

def D(vec, var, th):
    a, b, c = vec
    thv = sp.diff(th, var); k = kf(th)
    return (sp.diff(a, var) - b*thv, sp.diff(b, var) + (a - c*k)*thv, sp.diff(c, var) + b*k*thv)
def dot(u, v): return sp.expand(sum(p*q for p, q in zip(u, v)))
def z0(t):
    n, d = sp.fraction(sp.together(t))
    return sp.expand(n) == 0
def iszero(vec): return all(z0(t) for t in vec)
def sub(u, v): return tuple(sp.expand(p - q) for p, q in zip(u, v))
def lin(*pairs):   # линейная комбинация векторов
    return tuple(sp.expand(sum(cf*v[i] for cf, v in pairs)) for i in range(3))

S, TH, Z, kap = sp.symbols('s theta zeta kappa', positive=True)
s1, t1 = sp.symbols('s1 t1')
eS = sp.diff(etaf(s1, t1), s1).subs({s1: S, t1: TH})
eT = sp.diff(etaf(s1, t1), t1).subs({s1: S, t1: TH})
eta = etaf(S, TH) + Z
eps = kf(TH)*eta/S
k = kf(TH)

# ---------- карта Psi(s,theta,zeta) = s omega + (eta* + zeta) n ----------
Psi = (S, sp.Integer(0), eta)
Ps, Pt, Pz = D(Psi, S, TH), D(Psi, TH, TH), D(Psi, Z, TH)
print('Psi_s = omega + eta*_s n            :', iszero(sub(Ps, (1, 0, eS))))
print('Psi_theta = s(1-eps)T + eta*_theta n :', iszero(sub(Pt, (0, S*(1 - eps), eT))))
print('Psi_zeta = n                         :', iszero(sub(Pz, (0, 0, 1))))

# ---------- поле Y_kappa = Psi_s - (kappa theta/s) Psi_theta (теорема B; kappa=0 — теорема C) ----------
Yv = lin((1, Ps), (-kap*TH/S, Pt))
pi_ = eS - kap*TH*eT/S
print('Y = omega - k.th(1-eps)T + pi n      :', iszero(sub(Yv, (1, -kap*TH*(1 - eps), pi_))))
dsY, dtY, dzY = D(Yv, S, TH), D(Yv, TH, TH), D(Yv, Z, TH)
DYY = lin((1, dsY), (-kap*TH/S, dtY))
eps_s, eps_t = sp.diff(eps, S), sp.diff(eps, TH)
pi_s, pi_t = sp.diff(pi_, S), sp.diff(pi_, TH)
claim_sDYY = (-kap**2*TH**2*(1 - eps),
              kap*TH*(S*eps_s - 1 + kap*(1 - eps) - kap*TH*eps_t + pi_*k),
              S*pi_s + kap**2*TH**2*(1 - eps)*k - kap*TH*pi_t)
print('s D_Y Y formula                      :', iszero(sub(lin((S, DYY)), claim_sDYY)))
# s <w, D_w Y> для произвольного w = (wo, wT, wn)
wo, wT, wn = sp.symbols('w_o w_T w_n')
as_ = wo; at_ = wT/(S*(1 - eps)); az_ = wn - wo*eS - wT*eT/(S*(1 - eps))
w_rec = lin((as_, Ps), (at_, Pt), (az_, Pz))
print('разложение w по Psi_s,Psi_th,Psi_z   :', iszero(sub(w_rec, (wo, wT, wn))))
DwY = lin((as_, dsY), (at_, dtY), (az_, dzY))
lhs = S*dot((wo, wT, wn), DwY)
terms = [wT**2*(1/(1 - eps) - kap),                        # 1 главный (центробежный)
         kap*TH*S*eps_s*wo*wT,                             # 2
         S*pi_s*wo*wn,                                     # 3
         kap*TH*wo*wT,                                     # 4
         (kap*TH*eps_t - pi_*k)*wT**2/(1 - eps),           # 5
         pi_t*wT*wn/(1 - eps),                             # 6
         -kap*TH*k*wT*(wo*eS + wT*eT/(S*(1 - eps)))]       # 7 (члены kappa theta k w_T w_n сократились)
print('s<w,D_wY> = сумма 7 членов           :', z0(lhs - sum(terms)))

# ---------- карта оврага (теорема D): Phi(x,u,zeta) = Psi(x, th1 + tau(x) + u/x, zeta) ----------
x, u, th1 = sp.symbols('x u theta1', positive=True)
vt = th1 + tauf(x) + u/x
etaD = etaf(x, vt) + Z
PhiD = (x, sp.Integer(0), etaD)
Px, Pu, Pz2 = D(PhiD, x, vt), D(PhiD, u, vt), D(PhiD, Z, vt)
epsD = kf(vt)*etaD/x
eSD = sp.diff(etaf(s1, t1), s1).subs({s1: x, t1: vt})
eTD = sp.diff(etaf(s1, t1), t1).subs({s1: x, t1: vt})
kt = x*sp.diff(vt, x)                                    # \tilde kappa = x * vartheta_x
print('D: Phi_x = omega + kt(1-eps)T + (eta*_s + kt eta*_th/x) n :',
      iszero(sub(Px, (1, kt*(1 - epsD), eSD + kt*eTD/x))))
print('D: Phi_u = (1-eps)T + (eta*_th/x) n  :', iszero(sub(Pu, (0, 1 - epsD, eTD/x))))
print('D: Phi_zeta = n                      :', iszero(sub(Pz2, (0, 0, 1))))
# x Phi_xx = x eta*_ss n + 2 kt Psi_sth + (kt^2/x) Psi_thth + x vartheta_xx Psi_th  (всё в точке (x, vt, zeta))
def at(expr): return expr.subs({S: x, TH: vt})
Psth = D(Ps, TH, TH); Pthth = D(Pt, TH, TH)
Psth_v = tuple(at(c) for c in Psth); Pthth_v = tuple(at(c) for c in Pthth)
Pt_v = tuple(at(c) for c in Pt); Pss_v = tuple(at(c) for c in D(Ps, S, TH))
vxx = sp.diff(vt, x, 2)
claimxx = lin((x, Pss_v), (2*kt, Psth_v), (kt**2/x, Pthth_v), (x*vxx, Pt_v))
print('D: x Phi_xx formula                  :', iszero(sub(lin((x, D(Px, x, vt))), claimxx)))
print('D: Psi_sth = (1-k eta*_s)T + eta*_sth n :', iszero(sub(Psth, (0, 1 - k*eS, sp.diff(eS, TH)))))
claim_thth = (-(S - k*eta), -(sp.diff(k, TH)*eta + k*eT) - k*eT, (S - k*eta)*k + sp.diff(eT, TH))
print('D: Psi_thth formula                  :', iszero(sub(Pthth, claim_thth)))
# x d_u Phi_x = (eps - k eta*_s) T + (eta*_sth - eta*_th/x) n + (kt/x) Psi_thth
claimxu = lin((1, (0, epsD - kf(vt)*eSD, at(sp.diff(eS, TH)) - eTD/x)), (kt/x, Pthth_v))
print('D: x d_u Phi_x formula               :', iszero(sub(lin((x, D(Px, u, vt))), claimxu)))
print('D: x d_zeta Phi_x = -kt k T          :', iszero(sub(lin((x, D(Px, Z, vt))), (0, -kt*kf(vt), 0))))
