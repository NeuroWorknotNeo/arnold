# R40 (reviewer): independent numerical check of the strict exit condition (A5)
# for the construction of Theorem W on example W3 of
# notes/prover/2026-10-21-morse-bott-mult.md.   [Experiment, not a proof]
#
# U = z^4 + z^2 y r^2 - r^6 + y^2 r^4 + x z^5 + y^7,  r^2 = x^2 + y^2.
# Equator z = 0: omega = (cos th, sin th, 0), ell = (-sin th, cos th, 0), n = e_z, k_g = 0.
# Theorem W data at theta_0 = 0: eta_0 = 0 (y_0 = 0), N = 2, c = 3/2, beta = 6, a_0 = 1,
# P(th,e) = e^4 + sin(th) e^2 + sin(th)^2.
# Field (2.4):  Y = omega - kappa*th*ell + (lam*z/s) e_z,  rho = s = sqrt(x^2+y^2).
# Xi is computed by DIRECT differentiation of V - delta*rho^beta along the Hamiltonian
# vector field (not via Lemma 1 of [007]):
#   Xi = <grad_q (V - delta rho^beta), v> - <grad_v V, grad U>.
# Exit set: q in closure(D), E = 0, p < 0, V = delta rho^beta.
# Printed: min (rho/lambda_v) Xi / (delta rho^beta)  (must be > 0 for (A5)).
import sympy as sp
import mpmath as mp
import sys

mp.mp.dps = 80
x, y, z, vx, vy, vz = sp.symbols('x y z vx vy vz', real=True)
kap, lam, dl = sp.symbols('kappa lambda delta', real=True)
r2 = x**2 + y**2
U = z**4 + z**2*y*r2 - r2**3 + y**2*r2**2 + x*z**5 + y**7
s = sp.sqrt(r2)
th = sp.atan2(y, x)
om = sp.Matrix([x/s, y/s, 0])
el = sp.Matrix([-y/s, x/s, 0])
ez = sp.Matrix([0, 0, 1])
Y = om - kap*th*el + (lam*z/s)*ez
v = sp.Matrix([vx, vy, vz])
p = v.dot(Y)
h = Y.dot(Y)
beta = 6
A = s**beta                      # a_0 = 1
V = v.dot(v)/2 - p**2/(2*h) + U + A
Phi = V - dl*s**beta
q = [x, y, z]; vv = [vx, vy, vz]
gU = [sp.diff(U, t) for t in q]
Xi = sum(sp.diff(Phi, q[i])*vv[i] for i in range(3)) - sum(sp.diff(Phi, vv[i])*gU[i] for i in range(3))
args = (x, y, z, vx, vy, vz, kap, lam, dl)
Xif = sp.lambdify(args, Xi, 'mpmath')
Uf = sp.lambdify((x, y, z), U, 'mpmath')
Yf = sp.lambdify((x, y, z, kap, lam), Y, 'mpmath')

c = mp.mpf(3)/2

def Pf(t, e):
    return e**4 + mp.sin(t)*e**2 + mp.sin(t)**2

def point(S, t, e):
    return (S*mp.cos(t), S*mp.sin(t), S**c*e)

def Ftil_plus_a0(S, t, e):
    X = point(S, t, e)
    return Uf(*X)/S**beta + 1

def exit_value(S, t, e, K_, L_, D_, phi):
    X = point(S, t, e)
    W = Uf(*X) + S**beta
    Kp = D_*S**beta - W                      # K_perp = delta rho^beta - W >= 0
    if Kp < 0:
        return None
    Yv = mp.matrix(Yf(*X, K_, L_))
    hv = mp.fdot(Yv, Yv)
    lv = mp.sqrt(2*(1 - D_)*S**beta/hv)      # lambda_v = -p/h
    # orthonormal basis of Y^perp
    a = mp.matrix([0, 0, 1]) if abs(Yv[2]) < mp.mpf('0.5') else mp.matrix([1, 0, 0])
    e1 = a - (mp.fdot(a, Yv)/hv)*Yv; e1 = e1/mp.norm(e1)
    e2 = mp.matrix([Yv[1]*e1[2]-Yv[2]*e1[1], Yv[2]*e1[0]-Yv[0]*e1[2], Yv[0]*e1[1]-Yv[1]*e1[0]])
    e2 = e2/mp.norm(e2)
    vperp = mp.sqrt(2*Kp)*(mp.cos(phi)*e1 + mp.sin(phi)*e2)
    vvec = -lv*Yv + vperp
    E = mp.fdot(vvec, vvec)/2 + Uf(*X)
    xi = Xif(*X, vvec[0], vvec[1], vvec[2], K_, L_, D_)
    val = (S/lv)*xi/(D_*S**beta)
    return val, E/(S**beta)

def boundary_point(S, D_, psi):
    # point on {F~ + a0 = delta} along ray (t,e) = r*(cos psi*sqrt(D), sin psi*D^(1/4))
    f = lambda r: Ftil_plus_a0(S, r*mp.cos(psi)*mp.sqrt(D_), r*mp.sin(psi)*D_**mp.mpf(0.25)) - D_
    lo, hi = mp.mpf(0), mp.mpf(0.1)
    while f(hi) < 0:
        hi *= 2
    for _ in range(200):
        mid = (lo+hi)/2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    r = lo
    return r*mp.cos(psi)*mp.sqrt(D_), r*mp.sin(psi)*D_**mp.mpf(0.25)

def scan(S, D_, K_, L_, nray=64, ngrid=9, nphi=16):
    best = (mp.inf, None); maxE = mp.mpf(0)
    for k in range(nray):
        psi = 2*mp.pi*k/nray
        t, e = boundary_point(S, D_, psi)
        res = exit_value(S, t, e, K_, L_, D_, 0)
        if res is None:
            continue
        val, E = res; maxE = max(maxE, abs(E))
        if val < best[0]:
            best = (val, ('bdry', mp.nstr(t, 4), mp.nstr(e, 4)))
    # interior grid
    Tm = 1.3*mp.sqrt(4*D_/3); Em = 1.2*(16*D_/3)**mp.mpf(0.25)
    for i in range(-ngrid, ngrid+1):
        for j in range(-ngrid, ngrid+1):
            t = Tm*i/ngrid; e = Em*j/ngrid
            if Pf(t, e) >= 4*D_ or Ftil_plus_a0(S, t, e) > D_:
                continue
            for kph in range(nphi):
                res = exit_value(S, t, e, K_, L_, D_, 2*mp.pi*kph/nphi)
                if res is None:
                    continue
                val, E = res; maxE = max(maxE, abs(E))
                if val < best[0]:
                    best = (val, ('int', mp.nstr(t, 4), mp.nstr(e, 4), kph))
    return best, maxE

def euler_ratio_min(K_, c2, D_, n=400):
    # min over the level set {P = D_} (near 0, theta<0 branch included) of
    # (K theta P_theta + c2 e P_e)/P
    best = mp.inf
    for k in range(n):
        psi = 2*mp.pi*k/n
        f = lambda r: Pf(r*mp.cos(psi)*mp.sqrt(D_), r*mp.sin(psi)*D_**mp.mpf(0.25)) - D_
        lo, hi = mp.mpf(0), mp.mpf(0.1)
        while f(hi) < 0:
            hi *= 2
        for _ in range(100):
            mid = (lo+hi)/2
            if f(mid) < 0:
                lo = mid
            else:
                hi = mid
        t = lo*mp.cos(psi)*mp.sqrt(D_); e = lo*mp.sin(psi)*D_**mp.mpf(0.25)
        Pt = mp.cos(t)*e**2 + 2*mp.sin(t)*mp.cos(t)
        Pe = 4*e**3 + 2*mp.sin(t)*e
        best = min(best, (K_*t*Pt + c2*e*Pe)/Pf(t, e))
    return best

if __name__ == '__main__':
    # kappa(delta) from (2.3) for W3: mu0 = 1, beta = 6, a0 = 1, C_M = 15 sqrt3/8 *6 + 4,
    # R_theta(delta) = arcsin(sqrt(16 delta/3)) (sup |theta| over {P < 4 delta}).
    CM = 15*mp.sqrt(3)/8*6 + 4
    print("C_M =", mp.nstr(CM, 6))
    Dlist = [mp.mpf(a) for a in sys.argv[1:]] or [mp.mpf('1e-5'), mp.mpf('2e-3'), mp.mpf('1e-2')]
    for D_ in Dlist:
        Rt = mp.asin(mp.sqrt(16*D_/3))
        kd = min(mp.mpf(0.5), mp.mpf(6)/4, 6*D_/(2*CM**2*Rt**2))
        print(f"\n=== delta = {mp.nstr(D_,3)}:  R_theta = {mp.nstr(Rt,5)},  kappa(delta) by (2.3) = {mp.nstr(kd,5)}")
        for K_ in [kd, mp.mpf('0.05'), mp.mpf('0.1'), mp.mpf('0.2')]:
            er_W = euler_ratio_min(K_, K_/2, D_)
            er_M = euler_ratio_min(K_, c, D_)
            print(f"  kappa={mp.nstr(K_,4)}: Euler ratio min on {{P=delta}}: c2=kappa/2 -> {mp.nstr(er_W,5)};"
                  f"  c2=c -> {mp.nstr(er_M,5)}")
            for S in [mp.mpf('1e-8'), mp.mpf('1e-14'), mp.mpf('1e-20')]:
                for name, L_ in [("W (lam=c-kappa/2)", c - K_/2), ("Mb (lam=0)", mp.mpf(0))]:
                    (val, loc), maxE = scan(S, D_, K_, L_)
                    print(f"    s={mp.nstr(S,2):6s} {name:18s} min (rho/lam)Xi/(delta rho^b) = {mp.nstr(val,6):>12s}"
                          f"   at {loc}   max|E|/rho^b={mp.nstr(maxE,2)}")
                    sys.stdout.flush()
