# [Эксперимент] example13 §5: угловая поправка Z2 = -κ' (∂_φU/s^6) ∂_φ при перекрёстном члене η·c(φ) в F.
# U_b = U_13 + b*Q*z^2*x даёт F = 4η^2 + (b/√2) cosφ η + G/8 (вес 6), ∂_φ∂_η F ≠ 0.
import sympy as sp, mpmath as mp
mp.mp.dps = 40
X, Y, Z, b = sp.symbols('x y z b', real=True)
Q = X**2 + Y**2 - Z**2
U = Q**2 + Z**5*X + Z**4*X*Y + sp.Rational(1, 2)*Z**6 + b*Q*Z**2*X
rho = sp.sqrt(X**2 + Y**2)
s = (rho + Z)/sp.sqrt(2); d = (rho - Z)/sp.sqrt(2)
es = sp.Matrix([X/rho/sp.sqrt(2), Y/rho/sp.sqrt(2), 1/sp.sqrt(2)])
n = sp.Matrix([X/rho/sp.sqrt(2), Y/rho/sp.sqrt(2), -1/sp.sqrt(2)])
dphi = sp.Matrix([-Y, X, 0])
gU = sp.Matrix([sp.diff(U, v) for v in (X, Y, Z)])
dU_d = (gU.T*n)[0]; dU_phi = (gU.T*dphi)[0]
kap, kap2 = sp.Rational(1, 100), sp.Rational(1, 50)
V = (s*es + 2*d*n)/6 - kap*dU_d/s**2*n - kap2*dU_phi/s**6*dphi
J = V.jacobian([X, Y, Z])
Jf = sp.lambdify((X, Y, Z, b), J, 'mpmath')
Uf = sp.lambdify((X, Y, Z, b), U, 'mpmath')
def pt(sv, phi, eta):
    dv = eta*sv**2
    r_ = (sv + dv)/mp.sqrt(2); z_ = (sv - dv)/mp.sqrt(2)
    return r_*mp.cos(phi), r_*mp.sin(phi), z_
for bv in (0, mp.mpf('0.1')):
    for sv in (mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4'), mp.mpf('1e-5')):
        worst = mp.inf
        for phi in [mp.mpf(k)/20*2*mp.pi for k in range(20)]:
            for eta in (-0.2, 0, 0.2):
                p = pt(sv, phi, mp.mpf(eta))
                M = mp.matrix(Jf(*p, bv)); S = (M + M.T)/2
                worst = min(worst, min(mp.eigsy(S)[0]))
        print(f"b={bv} s={mp.nstr(sv,3)}: min λ(Sym DV) по сетке = {mp.nstr(worst,6)}")
