# [Эксперимент] Символьная проверка формул карт §3–§5 записки
# notes/prover/2026-10-21-gt3-hardcore.md.
# Вектор хранится как тройка коэффициентов в подвижном репере (omega, T, n) кривой
# Sigma на S^2 с натуральным параметром theta:
#   omega' = T,  T' = -omega + k n,  n' = -k T   (k = k(theta) — геодезическая кривизна).
# Дифференцирование по переменной v: D_v(a,b,c) = (a_v - b th_v, b_v + (a - c k) th_v, c_v + b k th_v).
import sympy as sp

x, u, zeta, X, Yc, kap = sp.symbols('x u zeta X Y kappa', real=True)
s_, th_ = sp.symbols('s theta', real=True)
# Чтобы sympy не путался в Subs-производных, берём общие многочлены с символьными
# коэффициентами: тождества линейны по производным, этого достаточно для проверки.
_kc = sp.symbols('k0:4')
_ac = sp.symbols('a0:5_0:4')
def kf(t):
    return sum(_kc[i]*t**i for i in range(4))
class _Eta:
    def __call__(self, s, t):
        return sum(_ac[4*i + j]*s**(i + 1)*t**j for i in range(4) for j in range(4))
etaf = _Eta()

def D(vec, var, th):
    a, b, c = vec
    thv = sp.diff(th, var)
    k = kf(th)
    return (sp.diff(a, var) - b*thv,
            sp.diff(b, var) + (a - c*k)*thv,
            sp.diff(c, var) + b*k*thv)

def dot(v1, v2):
    return sp.expand(sum(p*q for p, q in zip(v1, v2)))

def simp(vec):
    return tuple(sp.simplify(sp.expand(t)) for t in vec)

def iszero(vec):
    return all(sp.simplify(sp.expand(sp.powsimp(sp.expand(t), force=True))) == 0 for t in vec)

# ---------------- Поворачивающаяся полярная карта ----------------
th = u*x**(-kap)
eta = etaf(x, th) + zeta
Phi = (x, sp.Integer(0), eta)          # x*omega + eta*n
Px = D(Phi, x, th)
# утверждаемая формула: Y = omega - kappa*theta*(1-eps) T + p n,
# eps = k*eta/x, p = eta*_s - kappa*theta*eta*_theta / x
s1, t1 = sp.symbols('s1 t1')
etas = sp.diff(etaf(s1, t1), s1).subs({s1: x, t1: th})
etat = sp.diff(etaf(s1, t1), t1).subs({s1: x, t1: th})
eps = kf(th)*eta/x
p = etas - kap*th*etat/x
Yclaim = (sp.Integer(1), -kap*th*(1 - eps), p)
print('rot: Y formula ok:', iszero(tuple(a - b for a, b in zip(Px, Yclaim))))

Pxx = D(Px, x, th)
# утверждаемая формула для x*Phi_xx
dxeps = sp.diff(eps, x)
dxp = sp.diff(p, x)
k = kf(th)
claim = (-kap**2*th**2*(1 - eps),
         -kap*th*(1 - kap*(1 - eps) - x*dxeps - p*k),
         kap**2*th**2*(1 - eps)*k + x*dxp)
print('rot: x*Phi_xx formula ok:', iszero(tuple(x*a - b for a, b in zip(Pxx, claim))))
# x*d_x eps = -kappa*theta*k'(theta)*eta/x + k*p - eps
kp = sp.diff(kf(t1), t1).subs(t1, th)
print('rot: x d_x eps formula ok:',
      iszero((x*dxeps - (-kap*th*kp*eta/x + k*p - eps),)))

# Поле Y как функция точки в координатах (s, theta, zeta) и его частные производные
S, TH, Z = sp.symbols('S TH Z', real=True)
etaS = etaf(S, TH) + Z
epsS = kf(TH)*etaS/S
pS = sp.diff(etaf(S, TH), S) - kap*TH*sp.diff(etaf(S, TH), TH)/S
Yfield = (sp.Integer(1), -kap*TH*(1 - epsS), pS)
dthY = D(Yfield, TH, TH)
kS = kf(TH)
dthY_claim = (kap*TH*(1 - epsS),
              1 - kap*(1 - epsS) + kap*TH*sp.diff(epsS, TH) - pS*kS,
              -kap*TH*(1 - epsS)*kS + sp.diff(pS, TH))
print('rot: d_theta Y formula ok:', iszero(tuple(a - b for a, b in zip(dthY, dthY_claim))))
dsY = D(Yfield, S, TH)   # theta не зависит от S
print('rot: d_s Y = (0, kappa*theta*d_s eps, d_s p):',
      iszero(tuple(a - b for a, b in zip(dsY, (0, kap*TH*sp.diff(epsS, S), sp.diff(pS, S))))))
dzY = D(Yfield, Z, TH)
print('rot: d_zeta Y = (0, kappa*theta*k/s, 0):',
      iszero(tuple(a - b for a, b in zip(dzY, (0, kap*TH*kS/S, 0)))))
# координатные поля карты Psi(s,theta,zeta) = s omega + (eta* + zeta) n
PsiS = (S, sp.Integer(0), etaS)
print('Psi_s =', simp(D(PsiS, S, TH)))
print('Psi_theta =', simp(D(PsiS, TH, TH)))
print('Psi_zeta =', simp(D(PsiS, Z, TH)))

# ---------------- Декартова карта развёртки ----------------
r = sp.sqrt(X**2 + Yc**2)
thc = sp.atan(Yc/X)
etac = etaf(r, thc) + zeta
PhiC = (r, sp.Integer(0), etac)
PX = D(PhiC, X, thc)
PY = D(PhiC, Yc, thc)
PZ = D(PhiC, zeta, thc)
epsC = kf(thc)*etac/r
etasC = sp.diff(etaf(s1, t1), s1).subs({s1: r, t1: thc})
etatC = sp.diff(etaf(s1, t1), t1).subs({s1: r, t1: thc})
c_, sn = X/r, Yc/r
pX = c_*etasC - sn*etatC/r
pY = sn*etasC + c_*etatC/r
print('cart: Phi_X ok:', iszero(tuple(a - b for a, b in zip(PX, (c_, -sn*(1 - epsC), pX)))))
print('cart: Phi_Y ok:', iszero(tuple(a - b for a, b in zip(PY, (sn, c_*(1 - epsC), pY)))))
print('cart: Phi_zeta = n:', iszero(tuple(a - b for a, b in zip(PZ, (0, 0, 1)))))
BXY = dot(PX, PY)
claimBXY = sn*c_*(1 - (1 - epsC)**2) + pX*pY
print('cart: B_XY formula ok:', sp.simplify(BXY - claimBXY) == 0)
PXX = D(PX, X, thc)
kc = kf(thc)
dXeps = sp.diff(epsC, X)
dXpX = sp.diff(pX, X)
claimXX = (sn**2*epsC/r,
           -sn*c_*epsC/r + sn*dXeps + pX*kc*sn/r,
           sn**2*(1 - epsC)*kc/r + dXpX)
print('cart: Phi_XX formula ok:', iszero(tuple(a - b for a, b in zip(PXX, claimXX))))
PXY = D(PX, Yc, thc)
dYeps = sp.diff(epsC, Yc)
dYpX = sp.diff(pX, Yc)
claimXY = (-sn*c_*epsC/r,
           c_**2*epsC/r + sn*dYeps - pX*kc*c_/r,
           -sn*c_*(1 - epsC)*kc/r + dYpX)
print('cart: Phi_XY formula ok:', iszero(tuple(a - b for a, b in zip(PXY, claimXY))))
PXZ = D(PX, zeta, thc)
print('cart: Phi_Xzeta = (0, sin*k/r, 0):',
      iszero(tuple(a - b for a, b in zip(PXZ, (0, sn*kc/r, 0)))))
