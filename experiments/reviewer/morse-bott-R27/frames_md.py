"""[Эксперимент] R27: символьная проверка формул (5.3), (5.4) записки
notes/prover/2026-10-21-morse-bott.md (теорема Md).

Вектор задаётся координатами (a, b, c) в подвижном репере (omega, T, n) в точке theta,
и d/dtheta (a w + b T + c n) = (a'-b) w + (b'+a-k c) T + (c'+k b) n   (формулы (2.1)).
Карта: Psi(s,theta,zeta) = s*omega + (eta*(s,theta)+zeta) n,
Phi(x,u,zeta) = Psi(x, vartheta(x,u), zeta), vartheta = th0 + tau(x) + u/x.
Проверяем Phi_x, Phi_u, Phi_zeta, x Phi_xx, x d_u Phi_x, x d_zeta Phi_x.
"""
import sympy as sp

x, u, z, th0, S, TH = sp.symbols('x u zeta theta0 s theta', real=True)
k = sp.Function('k')
etas = sp.Function('etastar')
tau = sp.Function('tau')

vt = th0 + tau(x) + u/x          # vartheta(x,u)

def frame_deriv(vec, var, theta_expr):
    """Производная по var вектора vec=(a,b,c) в репере в точке theta_expr(var)."""
    a, b, c = vec
    th_v = sp.diff(theta_expr, var)
    kk = k(theta_expr)
    return (sp.diff(a, var) + th_v*(-b),
            sp.diff(b, var) + th_v*(a - kk*c),
            sp.diff(c, var) + th_v*(kk*b))

# Phi в координатах репера в точке vartheta
Phi = (x, sp.Integer(0), etas(x, vt) + z)

Phi_x = frame_deriv(Phi, x, vt)
Phi_u = frame_deriv(Phi, u, vt)
Phi_z = frame_deriv(Phi, z, vt)
Phi_xx = frame_deriv(Phi_x, x, vt)
Phi_xu = frame_deriv(Phi_x, u, vt)
Phi_xz = frame_deriv(Phi_x, z, vt)

# Обозначения записки, всё в точке (x, vartheta, zeta)
eta = etas(x, vt) + z
eps = k(vt)*eta/x
kt = x*sp.diff(vt, x)                       # tilde kappa
def d(f, *vars_):
    """Частные производные eta*(s,theta) в точке (x, vartheta)."""
    g = etas(S, TH)
    for v in vars_:
        g = sp.diff(g, v)
    return g.subs({S: x, TH: vt}, simultaneous=True)

es, eth = d(None, S), d(None, TH)
ess, esth, ethth = d(None, S, S), d(None, S, TH), d(None, TH, TH)
kv = k(vt)
kpv = sp.diff(k(TH), TH).subs(TH, vt)

# (5.3)
Phi_x_note = (1, kt*(1-eps), es + kt*eth/x)
Phi_u_note = (0, 1-eps, eth/x)
Phi_z_note = (0, 0, 1)
# Psi_{s theta}, Psi_{theta theta}, Psi_theta (в репере)
Psi_sth = (0, 1 - kv*es, esth)
Psi_thth = (-(x - kv*eta), -(kpv*eta + 2*kv*eth), (x - kv*eta)*kv + ethth)
Psi_th = (0, x*(1-eps), eth)
vxx = sp.diff(vt, x, 2)
# (5.4)
xPhi_xx_note = tuple(x*ess*nn + 2*kt*a + kt**2/x*b + x*vxx*c
                     for nn, a, b, c in zip((0, 0, 1), Psi_sth, Psi_thth, Psi_th))
xPhi_xu_note = tuple(p + q + kt/x*r for p, q, r in
                     zip((0, eps - kv*es, 0), (0, 0, esth - eth/x), Psi_thth))
xPhi_xz_note = (0, -kt*kv, 0)

def check(name, A, B):
    ok = all(sp.simplify(sp.expand(a - b)) == 0 for a, b in zip(A, B))
    print(f'{name}: {ok}')
    return ok

res = [
    check('Phi_x  (5.3)', Phi_x, Phi_x_note),
    check('Phi_u  (5.3)', Phi_u, Phi_u_note),
    check('Phi_z  (5.3)', Phi_z, Phi_z_note),
    check('x Phi_xx (5.4)', tuple(x*c for c in Phi_xx), xPhi_xx_note),
    check('x d_u Phi_x (5.4)', tuple(x*c for c in Phi_xu), xPhi_xu_note),
    check('x d_z Phi_x (5.4)', tuple(x*c for c in Phi_xz), xPhi_xz_note),
]
# (5.2): x^2 vartheta_xx = x^2 tau'' + 2 u/x, и u/x = x^alpha b1
print('x^2 vt_xx - x^2 tau\'\' - 2u/x =', sp.simplify(x**2*vxx - x**2*sp.diff(tau(x), x, 2) - 2*u/x))
print('ALL:', all(res))
