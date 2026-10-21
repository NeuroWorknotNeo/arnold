# [Experiment] Theorem B field (sec. 2.5, 4 of theoremB-proof.md), built exactly as in the
# proof (orthogonal tube parametrization, Morse map, shift eta, gradient for metric
# dtheta^2+da^2), for a family of examples; upper nappe of the cone x^2+y^2=z^2.
#   case 'A': U=(x^2+y^2-z^2)^2 + x z^4                          (m=4; Morse map = identity)
#   case 'B': U=(x^2+y^2-z^2)^2 (x^2+2y^2+3z^2) + x z^4 (x^2+y^2+z^2) + y^8   (m=6; nontrivial Morse map)
# Coordinates (eps,theta,a), r=eps^2. All Jacobians by central differences in mpmath.
import mpmath as mp, random, sys, functools
mp.mp.dps = 80
case = sys.argv[1] if len(sys.argv) > 1 else 'A'
NPTS = int(sys.argv[2]) if len(sys.argv) > 2 else 120
S2 = mp.sqrt(2)

def q(x, y, z): return x*x + y*y - z*z
if case == 'A':
    m = 4
    def um(x, y, z): return q(x, y, z)**2
    def um1(x, y, z): return x*z**4
    def U(x, y, z): return um(x, y, z) + um1(x, y, z)
else:
    m = 6
    def um(x, y, z): return q(x, y, z)**2*(x*x + 2*y*y + 3*z*z)
    def um1(x, y, z): return x*z**4*(x*x + y*y + z*z)
    def U(x, y, z): return um(x, y, z) + um1(x, y, z) + y**8

def om(T): return mp.matrix([mp.cos(T), mp.sin(T), 1])/S2
def nh(T): return mp.matrix([mp.cos(T), mp.sin(T), -1])/S2
def ev(F, v): return F(v[0], v[1], v[2])

# fibre function h_z(t)=u_m(z+t n), z = omega (|z|=1); Morse: t' = t*sqrt(M(t)/M(0)),
# M(t) = int_0^1 (1-s) h''(s t) ds = h(t)/t^2 (since h(0)=h'(0)=0)
def hfib(T, t): return ev(um, om(T) + t*nh(T))
@functools.lru_cache(maxsize=None)
def H(T): return mp.diff(lambda t: hfib(T, t), 0, 2)          # H_omega(n,n)
def Mf(T, t):
    if abs(t) < mp.mpf(10)**(-60): return H(T)/2
    return hfib(T, t)/t**2
def morse(T, t):  # nu -> nu'
    return t*mp.sqrt(Mf(T, t)/(H(T)/2))
def morse_inv(T, tp):
    if tp == 0: return mp.mpf(0)
    return mp.findroot(lambda t: morse(T, t) - tp, tp, tol=mp.mpf(10)**(-75))
@functools.lru_cache(maxsize=None)
def eta(T):  # H(eta, .) = <grad u_{m+1}(omega), n>
    L = mp.diff(lambda t: ev(um1, om(T) + t*nh(T)), 0)
    return L/H(T)
def g(T): return ev(um1, om(T))
def f(T, a): return H(T)/2*a*a + g(T)
def Phi(E, T, a):
    # Phi = r*Gamma(l,eps), Gamma = omega + nu(omega, eps a - eps^2 eta)
    mu = E*a - E**2*eta(T)
    return E**2*(om(T) + morse_inv(T, mu)*nh(T))
def hfun(E, T, a):
    x = Phi(E, T, a); r = E**2
    return (ev(U, x)/r**(m + 1) - f(T, a))/r

def d1(F, P, i, hs):
    Pp = list(P); Pm = list(P); Pp[i] += hs; Pm[i] -= hs
    return (F(*Pp) - F(*Pm))/(2*hs)
def jac(F, P, hs):
    J = mp.matrix(3, 3)
    for i in range(3):
        c = d1(F, P, i, hs[i])
        for j in range(3): J[j, i] = c[j]
    return J
HS_IN = mp.mpf(10)**(-25)
def Ahat(E, T, a):
    r = E**2; P = (E, T, a)
    f0 = f(T, a); fT = d1(lambda E_, T_, a_: f(T_, a_), P, 1, HS_IN); fA = d1(lambda E_, T_, a_: f(T_, a_), P, 2, HS_IN)
    h0 = hfun(E, T, a)
    hE = d1(hfun, P, 0, E*HS_IN); hT = d1(hfun, P, 1, HS_IN); hA = d1(hfun, P, 2, HS_IN)
    D = (m + 1)**2*f0**2 + fT**2 + fA**2
    p = (h0 + E*hE/2)/(m + 1)
    qq = ((m + 1)*f0*((m + 2)*h0 + E*hE/2) + fT*hT + fA*hA)/D
    c1 = -(m + 1)*f0*p/(D*(1 + r*qq)); YT = -p*fT/(D*(1 + r*qq)); YA = -p*fA/(D*(1 + r*qq))
    return r/(m + 1) + r**2*c1, r*YT, r*YA, D
def Ax(E, T, a):
    J = jac(Phi, (E, T, a), [E*HS_IN, HS_IN, HS_IN])
    Ar, AT, AA, D = Ahat(E, T, a)
    return Ar*J[:, 0]/(2*E) + AT*J[:, 1] + AA*J[:, 2]       # d/dr = (1/(2eps)) d/deps
def Vx(E, T, a):
    J = jac(Phi, (E, T, a), [E*HS_IN, HS_IN, HS_IN]); return E*J[:, 0]/2

def gradU(x):
    return mp.matrix([mp.diff(lambda s: U(s, x[1], x[2]), x[0]), mp.diff(lambda s: U(x[0], s, x[2]), x[1]),
                      mp.diff(lambda s: U(x[0], x[1], s), x[2])])

random.seed(2)
print(f"case {case}, m={m}", flush=True)
HS_OUT = mp.mpf(10)**(-12)
for rv in ['1e-2', '1e-3', '1e-4', '1e-6', '1e-8']:
    E = mp.sqrt(mp.mpf(rv))
    lamU = mp.inf; lamAll = mp.inf; wAU = 0; maxA = 0; cnt = 0; wV = 0; Dmin = mp.inf
    for k in range(NPTS):
        T = mp.mpf(random.uniform(0, 6.283185307179586))
        # sample a in [-amax, amax] so that a good share of points has U<0
        a = mp.mpf(random.uniform(-0.4, 0.4))
        P = (E, T, a); hs = [E*HS_OUT, HS_OUT, HS_OUT]
        JP = jac(Phi, P, hs); JA = jac(Ax, P, hs); JV = jac(Vx, P, hs)
        JPi = mp.inverse(JP)
        DA = JA*JPi; S = (DA + DA.T)/2; lam = min(mp.eigsy(S)[0])
        n = nh(T); PN = n*n.T
        DV = JV*JPi; wV = max(wV, mp.mnorm(DV - mp.eye(3) - PN/2, 1))
        lamAll = min(lamAll, lam)
        x = Phi(*P); U0 = ev(U, x)
        if U0 < 0:
            cnt += 1; lamU = min(lamU, lam)
            A = Ax(*P); AU = (A.T*gradU(x))[0]
            wAU = max(wAU, abs(AU/U0 - 1)); maxA = max(maxA, mp.norm(A)/mp.norm(x))
    print(f"r={rv}: N(U<0)={cnt}/{NPTS}; min eig sym DA: on U<0 {mp.nstr(lamU, 8)}, on whole sample {mp.nstr(lamAll, 8)}; "
          f"max|A(U)/U-1|={mp.nstr(wAU, 3)}; max|A|/|x|={mp.nstr(maxA, 5)}; max|DV-I-P_N/2|={mp.nstr(wV, 5)}; sqrt(r)={mp.nstr(E, 3)}",
          flush=True)
