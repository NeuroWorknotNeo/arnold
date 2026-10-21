"""[Эксперимент] Численная проверка конструкции леммы R (notes/vlad-claude/lemmaR-proof.md).

Рецензент, 21.10.2026. Это не доказательство: проверяются выкладки §3-§4 на конкретной
карте режима с нелинейной G (кривизна, зависимость от eps), n = 4.

Карта: q = (r, th, y1, y2); блоки: угловой (w=1, s=1), нормальные w1 = 3/2, w2 = 2;
N = 2, eps = r^(1/2), a1 = 1, a2 = 2.  Phi = r*G(th, eps*y1, eps^2*y2, eps).
U o Phi = r^d (F + r^e H).

Поле: A = V + W, V = r d_r, W как в §3 леммы R, с данным множеством блоков Jset.
DA^x = D_q(DPhi * Ahat) * DPhi^{-1}  (формула (*)), считается символьно (sympy),
вычисляется в mpmath с высокой точностью.

Режимы:
  good : e = 1, J = {1,2} (по лемме: w_k - w_j < e  <=>  w_j > 1); ожидание:
         lambda_min(sym DA) -> 1, отклонение ~ r^(1/2).
  radial: e = 3/2, J = все блоки и r (w_k - 1 = 1 < e); ожидание как в good.
  bad  : e = 1/2, но в J насильно включены блоки 1 и угловой (нарушение условия на J);
         ожидание: рост DA как r^(-1/2) (проверка чувствительности теста).
"""
import sys
import sympy as sp
import mpmath as mp

mp.mp.dps = 60

r, th, y1, y2 = sp.symbols('r theta y1 y2', positive=False, real=True)
q = [r, th, y1, y2]
eps = sp.sqrt(r)
mu1, mu2, ee = eps * y1, eps**2 * y2, eps

omega = sp.Matrix([sp.cos(th), sp.sin(th), 0, 0])
G = (omega
     + mu1 * sp.Matrix([0, 0, 1, 0])
     + mu2 * sp.Matrix([0, 0, 0, 1])
     + mu1**2 * sp.Matrix([sp.Rational(3, 10), sp.Rational(1, 5) * sp.cos(th), sp.Rational(1, 10), sp.Rational(2, 5)])
     + mu1 * mu2 * sp.Matrix([sp.Rational(1, 10), -sp.Rational(1, 5), sp.Rational(3, 10) * sp.sin(th), 0])
     + mu2**2 * sp.Matrix([0, sp.Rational(1, 7), 0, sp.Rational(1, 3)])
     + ee * sp.Matrix([sp.Rational(1, 5) * sp.sin(th), sp.Rational(1, 10), sp.Rational(3, 10), -sp.Rational(1, 5)])
     + ee * mu1 * sp.Matrix([sp.Rational(1, 4), 0, sp.cos(th), sp.Rational(1, 2)])
     + ee**2 * sp.Matrix([0, sp.Rational(1, 3), sp.Rational(1, 5), 0])
     + mu1**3 * sp.Matrix([sp.Rational(1, 6), 0, 0, sp.sin(th)]))
Phi = r * G
DPhi = Phi.jacobian(q)

c0 = sp.Rational(3, 10)


def S5(u):
    # C^2 smoothstep: S(0)=0, S(1)=1, S',S'' = 0 at ends
    return 6 * u**5 - 15 * u**4 + 10 * u**3


def build(mode):
    d = sp.Integer(2)
    if mode == 'good':
        e = sp.Integer(1)
        J = ['y1', 'y2']          # w_k - w_j < e: w_j in {3/2, 2}; angular (1) excluded
        radial_in_J = False
    elif mode == 'bad':
        e = sp.Rational(1, 2)
        J = ['th', 'y1', 'y2']    # lemma allows only y2 (2 - w_j < 1/2)
        radial_in_J = False
    elif mode == 'radial':
        e = sp.Rational(3, 2)
        J = ['th', 'y1', 'y2']    # w_k - 1 = 1 < e: все блоки и r входят в J
        radial_in_J = True
    else:
        raise ValueError(mode)
    F = y1**2 + y2**2 - 1 + sp.Rational(3, 10) * sp.sin(th) * y1
    H = sp.sin(th) * y1 * y2 + y2 + sp.cos(th) + eps * y1 + eps**2 * y2**2
    Uc = r**d * (F + r**e * H)          # U o Phi in chart coordinates
    Uplus = sp.simplify(r * sp.diff(Uc, r) - d * Uc)
    var = {'th': th, 'y1': y1, 'y2': y2}
    grads = [sp.diff(Uc, var[j]) for j in J]
    den = sum(g**2 for g in grads)
    rU = r * sp.diff(Uc, r)
    if radial_in_J:
        den = den + rU**2
    return d, e, F, H, Uc, Uplus, J, grads, den, rU, radial_in_J


def field_exprs(mode, branch):
    """branch: 'one' (chi=1), 'pos'/'neg' (transition, F>0 / F<0), 'zero' (chi=0)."""
    d, e, F, H, Uc, Uplus, J, grads, den, rU, radial_in_J = build(mode)
    if branch == 'one':
        chi = sp.Integer(1)
    elif branch == 'zero':
        chi = sp.Integer(0)
    elif branch == 'pos':
        chi = S5((c0 - F) / (c0 / 2))
    elif branch == 'neg':
        chi = S5((c0 + F) / (c0 / 2))
    Ahat = sp.Matrix([r, 0, 0, 0])
    idx = {'th': 1, 'y1': 2, 'y2': 3}
    for j, g in zip(J, grads):
        Ahat[idx[j]] += -chi * Uplus * g / den
    if radial_in_J:
        Ahat[0] += -chi * Uplus * rU / den * r
    Ax = DPhi * Ahat
    DAq = Ax.jacobian(q)
    AU = sum(Ahat[i] * sp.diff(Uc, q[i]) for i in range(4))
    return (sp.lambdify(q, DAq, 'mpmath'), sp.lambdify(q, DPhi, 'mpmath'),
            sp.lambdify(q, Ax, 'mpmath'), sp.lambdify(q, AU, 'mpmath'),
            sp.lambdify(q, Uc, 'mpmath'), sp.lambdify(q, F, 'mpmath'), d)


def which_branch(Fv):
    a = abs(Fv)
    if a <= c0 / 2:
        return 'one'
    if a >= c0:
        return 'zero'
    return 'pos' if Fv > 0 else 'neg'


def main(mode):
    cache = {}
    pts = []
    import random
    random.seed(1)
    Ff = sp.lambdify([th, y1, y2], build(mode)[2], 'mpmath')
    # точки: случайные в K = [-1,1] x {|y|<=1.6}, с перевесом около F ~ 0 и переходной зоны
    near = 0
    while len(pts) < 60:
        t = random.uniform(-1, 1)
        a = random.uniform(-1.6, 1.6)
        b = random.uniform(-1.6, 1.6)
        if a * a + b * b > 2.5:
            continue
        isnear = abs(float(Ff(t, a, b))) < float(c0)
        if not isnear and len(pts) - near >= 25:
            continue
        near += isnear
        pts.append((t, a, b))
    print(f"mode={mode}")
    for rv in ['1e-2', '1e-4', '1e-6', '1e-8', '1e-10']:
        R = mp.mpf(rv)
        worst_lmin = mp.inf
        worst_dev = 0
        worst_ratio = -mp.inf
        maxA = 0
        for (t, a, b) in pts:
            Fv = float(Ff(t, a, b))
            br = which_branch(Fv)
            if br not in cache:
                cache[br] = field_exprs(mode, br)
            DAq, DPh, Ax, AU, Uc, _, d = cache[br]
            M = mp.matrix(DAq(R, t, a, b)) * mp.inverse(mp.matrix(DPh(R, t, a, b)))
            Sym = (M + M.T) / 2
            ev = mp.eigsy(Sym)[0]
            lmin = min(ev[i] for i in range(4))
            worst_lmin = min(worst_lmin, lmin)
            # отклонение от P_omega + P_T + 1.5 P_N1 + 2 P_N2 (при eps=0 базис ортонормирован
            # и совпадает с e1..e4 после поворота на th)
            c, s = mp.cos(t), mp.sin(t)
            Rot = mp.matrix([[c, -s, 0, 0], [s, c, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
            L0 = Rot * mp.diag([1, 1, 1.5, 2]) * Rot.T
            dev = mp.mnorm(M - L0, 1)
            worst_dev = max(worst_dev, dev)
            Uv = Uc(R, t, a, b)
            if Uv < 0:
                ratio = AU(R, t, a, b) / Uv   # A(U) <= (d/2) U  <=>  ratio >= d/2
                worst_ratio = max(worst_ratio, -ratio)
            Axv = mp.matrix(Ax(R, t, a, b))
            maxA = max(maxA, mp.norm(Axv) / R)
        print(f"  r={rv}: min lambda_min(sym DA)={mp.nstr(worst_lmin, 8)}, "
              f"max|DA - L0|={mp.nstr(worst_dev, 6)}, "
              f"min over U<0 of A(U)/U={mp.nstr(-worst_ratio, 8)} (need >= d/2=1), "
              f"max|A|/r={mp.nstr(maxA, 6)}")


if __name__ == '__main__':
    for m in sys.argv[1:] or ['good', 'bad']:
        main(m)
