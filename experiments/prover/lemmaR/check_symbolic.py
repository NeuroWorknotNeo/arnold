"""[Эксперимент] Символьная проверка выкладок results/004-lemmaR.md (prover, 21.10.2026).

Вопрос: верны ли тождества шагов 1, 3, 4, 5 исправленного текста леммы R в общем виде
(F, H, G, Gamma, chi -- абстрактные функции sympy; d, e, N -- символы или конкретные числа):
  (A1) U_+ := r d_r U - d U = r^{d+e} P,  P = e H + eps H_eps / N;
  (A2) знаменатель = r^{2d} (D_J + r^e B) с B из шага 3 (J = {r, 0, 1} и J = {1});
  (A3) W^ = r^e (c r d_r + sum Y_j d_j) с c, Y_j из шага 3, и W^(U) = -chi(F) U_+;
  (A4) A(U) = d U + (1 - chi) U_+;
  (A5) r d_r^2 Phi = (eps/N)(1+1/N) Gamma_eps + (eps/N)^2 Gamma_epseps   (Phi = r Gamma(y, eps));
  (A6) r eps^{a} = r^{w}, w = 1 + a/N;  d_r d_{y1} Phi = (w s_1/r) D_mu G + s_1 (eps/(N r)) d/deps[D_mu G]
       для Phi = r G(y0, eps^a y1, eps), a = 1, 2, 3 при N = 2, 3 (здесь G -- конкретная
       нелинейная функция: для абстрактной sympy не приводит смешанные производные в Subs).
Метод: r = eps^N, r d_r = (eps/N) d_eps; упрощение разностей до нуля (sympy.simplify / expand).
Запуск: ~/venv/bin/python check_symbolic.py
Это не доказательство: проверяются отдельные алгебраические тождества.
"""
import sympy as sp

eps, N, d, e = sp.symbols('epsilon N d e', positive=True)
y0, y1, chi = sp.symbols('y0 y1 chi', real=True)


def ok(name, cond):
    print(('OK   ' if cond else 'FAIL ') + name)


F = sp.Function('F')(y0, y1)
H = sp.Function('H')(y0, y1, eps)
r = eps**N
re = eps**(N * e)          # r^e
rdr = lambda f: eps / N * sp.diff(f, eps)   # r d/dr при r = eps^N

U = r**d * (F + re * H)
Uplus = rdr(U) - d * U
P = e * H + eps * sp.diff(H, eps) / N
ok('(A1) U_+ = r^{d+e} (e H + eps H_eps / N)', sp.simplify(Uplus - r**(d) * re * P) == 0)

H1 = (d + e) * H + eps * sp.diff(H, eps) / N
Fj = {'y0': sp.diff(F, y0), 'y1': sp.diff(F, y1)}
Hj = {'y0': sp.diff(H, y0), 'y1': sp.diff(H, y1)}
var = {'y0': y0, 'y1': y1}

for Jname, radial, blocks in [('J={r,0,1}', True, ['y0', 'y1']), ('J={1}', False, ['y1'])]:
    rU = rdr(U)
    gU = {j: sp.diff(U, var[j]) for j in blocks}
    Den = (rU**2 if radial else 0) + sum(gU[j]**2 for j in blocks)
    DJ = (d**2 * F**2 if radial else 0) + sum(Fj[j]**2 for j in blocks)
    B = ((2 * d * F * H1 + re * H1**2) if radial else 0) + \
        sum(2 * Fj[j] * Hj[j] + re * Hj[j]**2 for j in blocks)
    ok(f'(A2) {Jname}: Den = r^(2d) (D_J + r^e B)',
       sp.simplify(sp.expand(Den - r**(2 * d) * (DJ + re * B))) == 0)
    # W^ components from the definition
    Wr = (-chi * Uplus * rU / Den) if radial else 0          # coefficient of r d_r
    Wj = {j: -chi * Uplus * gU[j] / Den for j in blocks}    # coefficient of d_j
    den2 = DJ + re * B
    c = (-chi * P * (d * F + re * H1) / den2) if radial else 0
    Y = {j: -chi * P * (Fj[j] + re * Hj[j]) / den2 for j in blocks}
    if radial:
        ok(f'(A3) {Jname}: radial coefficient = r^e c', sp.simplify(Wr - re * c) == 0)
    ok(f'(A3) {Jname}: d_j coefficients = r^e Y_j',
       all(sp.simplify(Wj[j] - re * Y[j]) == 0 for j in blocks))
    WU = (Wr * rU if radial else 0) + sum(Wj[j] * gU[j] for j in blocks)
    ok(f'(A3) {Jname}: W^(U) = -chi U_+', sp.simplify(WU + chi * Uplus) == 0)
    AU = rdr(U) + WU
    ok(f'(A4) {Jname}: A(U) = dU + (1-chi) U_+', sp.simplify(AU - d * U - (1 - chi) * Uplus) == 0)

# (A5)
Gam = sp.Function('Gamma')(y0, eps)
Phi = r * Gam
dr = lambda f: 1 / (N * eps**(N - 1)) * sp.diff(f, eps)   # d/dr
drPhi = dr(Phi)
ok('(A5a) d_r Phi = Gamma + (eps/N) Gamma_eps',
   sp.simplify(drPhi - (Gam + eps / N * sp.diff(Gam, eps))) == 0)
ok('(A5b) r d_r^2 Phi = (eps/N)(1+1/N) Gamma_eps + (eps/N)^2 Gamma_epseps',
   sp.simplify(r * dr(drPhi) - (eps / N * (1 + 1 / N) * sp.diff(Gam, eps)
                                + (eps / N)**2 * sp.diff(Gam, eps, 2))) == 0)

# (A6) Для абстрактной G sympy не сокращает смешанные производные внутри Subs, поэтому берём
# конкретную нелинейную G(y0, mu, eps) (тождество проверяется на ней).
mu, et = sp.symbols('mu eta')
Gexpr = lambda Y0, M, E: sp.exp(Y0 * M) * sp.cos(M + E**2) + M**3 * E + sp.sin(E * Y0) + M**2 * Y0
for Nv in (2, 3):
    for a in (1, 2, 3):
        rr = eps**Nv
        w = 1 + sp.Rational(a, Nv)
        s1 = rr**w
        ok(f'(A6a) N={Nv}, a={a}: r eps^a = r^w', sp.simplify(rr * eps**a - s1) == 0)
        PhiG = rr * Gexpr(y0, eps**a * y1, eps)
        dy1 = sp.diff(PhiG, y1)
        DmuG = sp.diff(Gexpr(y0, mu, et), mu).subs({mu: eps**a * y1, et: eps})
        ok(f'(A6b) N={Nv}, a={a}: d_y1 Phi = s_1 D_mu G', sp.simplify(dy1 - s1 * DmuG) == 0)
        lhs = 1 / (Nv * eps**(Nv - 1)) * sp.diff(dy1, eps)
        rhs = w * s1 / rr * DmuG + s1 * eps / (Nv * rr) * sp.diff(DmuG, eps)
        ok(f'(A6c) N={Nv}, a={a}: d_r d_y1 Phi = (w s_1/r) D_mu G + s_1 (eps/(N r)) d_eps[D_mu G]',
           sp.simplify(lhs - rhs) == 0)
