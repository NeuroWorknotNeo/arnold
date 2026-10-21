"""[Эксперимент] Исправленная конструкция угла поворота Delta
(notes/prover/2026-10-21-palamodov-plane-corrected.md, §5) на окружностях |x| = r.

Потенциалы:
    u1 = -x2 (x1 - x2^2)          обе компоненты U^- (из отзыва: пример 1);
    u2 = x1^5 - (x2 - x1^2)^2     одна компонента (из отзыва: пример 2);
    u3 = x1^3 - x2^2              одна компонента: круг без каспа (из отзыва: разрез угла);
    u4 = -(x2 - x1^2)^2 - x1^6    строгий максимум: рог -- весь проколотый круг (периодический случай);
    u5 = (x2 - x1^2)(x2 - x1^3)   рог x1^3 < x2 < x1^2 (взвешенные поля Эйлера не годятся);
    u6 = (x2 - x1^2)^2 - x1^6     узкие искривлённые рога вдоль параболы.

Конструкция: угол phi (от -x к grad u, главное значение) на дуге (a(r), b(r)) рога, угол alpha поднят на дугу;
    tau+ = max(phi - pi/2, 0),  tau- = min(phi + pi/2, 0);
    Delta+(alpha) = max_beta [tau+(beta) - k(beta - alpha)],  k(s) = lamB s^+ + |lamH| s^-;
    Delta-(alpha) = min_beta [tau-(beta) + k'(beta - alpha)], k'(s) = |lamH| s^+ + lamB s^-;
    Delta = Delta+ + Delta-;  lamB = eta1,  lamH = -2 eps1/gamma1,  eps1 = r + sup_arc (|phi| - pi/2)^+.
beta пробегает ЗАМКНУТУЮ дугу (на сетке -- точки, сгущённые к концам до 1e-13 длины дуги), так что
концевые касательные куски входят автоматически; на всей окружности -- периодически.
Максимум по сетке считается точно (кумулятивные максимумы); значение Delta в произвольной точке q
считается как максимум по (сетка U {q}) -- так получаем r*Delta_r без интерполяции.

Проверяем:
  (I)  phi - pi/2 <= Delta <= phi + pi/2;  носители Delta+ и Delta- не пересекаются;
  (III) разностные отношения Delta по alpha в [lamH, lamB] (на ячейке, где Delta+ сменяется на Delta-,
        дискретное отношение может доходить до 2 lamH -- нуль между узлами сеткой не разрешён);
  (2)  cos(phi - Delta) >= 0, т.е. <v, grad u> <= 0;
  (IV) r Delta_r -- центральная разность по r (относительный шаг h = min(0.02, 0.2 r)) при фиксированном alpha;
  (3)  mu = min eig sym Dv по точной формуле (сверена в jacobian_sympy.py) с односторонними Delta_alpha;
  лемма 5: (6') min (phi(b)-phi(a)+pi) >= 0 и (7') max (phi(b)-phi(a)-pi)/(b-a) <= eta1
       по парам 0 < b - a <= gamma1, которые могут быть существенны (подвыборка).
Это численная иллюстрация, не доказательство.
Запуск: ~/venv/bin/python -I construct.py > construct_out.txt
"""
import numpy as np
from scipy.optimize import brentq

GAMMA1 = 0.5
ETA1 = 2.0
N0 = 400001         # равномерная часть сетки
TOL_PHI = 2e-3      # первый проход измельчения: |phi_{i+1} - phi_i| <= TOL_PHI
TOL_REL = 5e-3      # второй проход: там, где |phi| > pi/2 - 3 eps1, |dphi| <= TOL_REL * eps1
MAXPTS = 4_000_000


# ---------------------------------------------------------------- примеры
def ex_u1():
    return (lambda x1, x2: -x2 * (x1 - x2 ** 2),
            lambda x1, x2: (-x2, -x1 + 3 * x2 ** 2))


def ex_u2():
    return (lambda x1, x2: x1 ** 5 - (x2 - x1 ** 2) ** 2,
            lambda x1, x2: (5 * x1 ** 4 + 4 * x1 * (x2 - x1 ** 2), -2 * (x2 - x1 ** 2)))


def ex_u3():
    return (lambda x1, x2: x1 ** 3 - x2 ** 2,
            lambda x1, x2: (3 * x1 ** 2, -2 * x2))


def ex_u4():
    return (lambda x1, x2: -(x2 - x1 ** 2) ** 2 - x1 ** 6,
            lambda x1, x2: (4 * x1 * (x2 - x1 ** 2) - 6 * x1 ** 5, -2 * (x2 - x1 ** 2)))


def ex_u5():
    return (lambda x1, x2: (x2 - x1 ** 2) * (x2 - x1 ** 3),
            lambda x1, x2: (-2 * x1 * (x2 - x1 ** 3) - 3 * x1 ** 2 * (x2 - x1 ** 2),
                            2 * x2 - x1 ** 2 - x1 ** 3))


def ex_u6():
    return (lambda x1, x2: (x2 - x1 ** 2) ** 2 - x1 ** 6,
            lambda x1, x2: (-4 * x1 * (x2 - x1 ** 2) - 6 * x1 ** 5, 2 * (x2 - x1 ** 2)))


def al_on_curve(f, sign=1):
    """угол точки (sign*t, f(t)), t > 0, лежащей на окружности радиуса r."""
    def al0(r):
        t = brentq(lambda t: np.hypot(t, f(t)) - r, 0, r)
        return np.arctan2(f(t), sign * t)
    return al0


CASES = [
    ("u1, Q1={x2>0, x1>x2^2}", ex_u1, lambda r: np.pi / 4),
    ("u1, Q2={x2<0, x1<x2^2}", ex_u1, lambda r: 5 * np.pi / 4),
    ("u2 (one horn)", ex_u2, lambda r: np.pi),
    ("u3 (one horn)", ex_u3, lambda r: np.pi),
    ("u4=-(x2-x1^2)^2-x1^6 (whole circle, periodic)", ex_u4, lambda r: 1.0),
    ("u5=(x2-x1^2)(x2-x1^3), horn x1^3<x2<x1^2", ex_u5, al_on_curve(lambda t: 0.5 * (t ** 2 + t ** 3))),
    ("u6=(x2-x1^2)^2-x1^6, right horn", ex_u6, al_on_curve(lambda t: t ** 2)),
    ("u6=(x2-x1^2)^2-x1^6, left horn", ex_u6, al_on_curve(lambda t: t ** 2, sign=-1)),
]


def make(exf):
    u, g = exf()

    def U(al, r):
        return u(r * np.cos(al), r * np.sin(al))

    def phi(al, r):
        x1, x2 = r * np.cos(al), r * np.sin(al)
        g1, g2 = g(x1, x2)
        dot = -x1 * g1 - x2 * g2           # <-x, g>
        cross = -x1 * g2 + x2 * g1         # det(-x, g)
        return np.arctan2(cross, dot)
    return U, phi


# ---------------------------------------------------------------- дуга и сетка
def arc(U, r, al0):
    """Дуга {U<0} на окружности радиуса r, содержащая al0: (a, b), a < al0 < b, или None (вся окружность).
    Смена знака ищется на объединении геометрической сетки расстояний от al0 (1e-15 .. 2pi, множитель 1.0005)
    и равномерной сетки с шагом 2pi/8e6."""
    assert U(al0, r) < 0, (al0, r)
    d = np.unique(np.concatenate([[0.0], 10.0 ** np.arange(-15, np.log10(2 * np.pi), np.log10(1.0005)),
                                  np.linspace(0, 2 * np.pi, 8_000_001)]))
    f = lambda t: U(t, r)
    res = []
    for sgn in (+1, -1):
        th = al0 + sgn * d
        s_ = U(th, r) < 0
        if s_.all():
            return None
        i = np.argmax(~s_)
        lo, hi = sorted((th[i - 1], th[i]))
        res.append(brentq(f, lo, hi, xtol=1e-16, rtol=1e-15))
    b, a = res
    return a, b


def dedup(x):
    x = np.unique(x)
    keep = np.concatenate([[True], np.diff(x) > 1e-13 * (1 + np.abs(x[1:]))])
    return x[keep]


def grid(phi, r, a, b):
    L = b - a
    u = np.linspace(0, 1, N0)[1:-1]
    t = 10.0 ** np.arange(-13, -1, 0.05)
    al = dedup(a + L * np.concatenate([u, t, 1 - t]))

    def refine(al, crit):
        for _ in range(60):
            p = phi(al, r)
            bad = crit(p)
            if not bad.any() or al.size > MAXPTS:
                break
            al = dedup(np.concatenate([al, 0.5 * (al[:-1][bad] + al[1:][bad])]))
        return al
    al = refine(al, lambda p: np.abs(np.diff(p)) > TOL_PHI)
    p = phi(al, r)
    eps1 = r + max(0.0, (np.abs(p) - np.pi / 2).max())
    rel = lambda p: ((np.maximum(np.abs(p[:-1]), np.abs(p[1:])) > np.pi / 2 - 3 * eps1)
                     & (np.abs(np.diff(p)) > TOL_REL * eps1))
    al = refine(al, rel)
    return al, phi(al, r)


# ---------------------------------------------------------------- огибающая
def _cummax_src(vals):
    run = np.maximum.accumulate(vals)
    idx = np.arange(vals.size)
    src = np.maximum.accumulate(np.where(vals >= run, idx, 0))
    return run, src


def envelope(al, p, eps1):
    lamB = ETA1
    lamH = -2 * eps1 / GAMMA1
    mH = -lamH
    t = al - al[0]
    tp = np.maximum(p - np.pi / 2, 0.0)
    tm = np.minimum(p + np.pi / 2, 0.0)
    n = al.size
    run, src = _cummax_src((tp - lamB * t)[::-1])
    R = run[::-1] + lamB * t; Rsrc = (n - 1 - src)[::-1]          # beta >= alpha
    run, Lsrc = _cummax_src(tp + mH * t)
    Lf = run - mH * t                                               # beta <= alpha
    run, src = _cummax_src((-(tm + mH * t))[::-1])
    Rm = -run[::-1] - mH * t; Rmsrc = (n - 1 - src)[::-1]
    run, Lmsrc = _cummax_src(-(tm - lamB * t))
    Lm = -run + lamB * t
    Dp = np.maximum(np.maximum(R, Lf), 0.0); srcp = np.where(R >= Lf, Rsrc, Lsrc)
    Dm = np.minimum(np.minimum(Rm, Lm), 0.0); srcm = np.where(Rm <= Lm, Rmsrc, Lmsrc)
    return dict(Dp=Dp, Dm=Dm, srcp=srcp, srcm=srcm, lamB=lamB, lamH=lamH, tp=tp, tm=tm,
                R=R, Lf=Lf, Rm=Rm, Lm=Lm)


def build(U, phi, r, al0):
    ab = arc(U, r, al0)
    periodic = ab is None
    if periodic:
        al1, _ = grid(phi, r, 0.0, 2 * np.pi)
        al1 = al1[al1 < 2 * np.pi]
        p1 = phi(al1, r)
        al = np.concatenate([al1 - 2 * np.pi, al1, al1 + 2 * np.pi]); p = np.concatenate([p1, p1, p1])
        a, b = 0.0, 2 * np.pi
    else:
        a, b = ab
        al, p = grid(phi, r, a, b)
    eps = max(0.0, (np.abs(p) - np.pi / 2).max())
    eps1 = r + eps
    E = envelope(al, p, eps1)
    c = dict(a=a, b=b, eps=eps, eps1=eps1, periodic=periodic, r=r, phi=phi,
             al_full=al, E_full=E)
    if periodic:
        n1 = al1.size
        sl_ = slice(n1, 2 * n1)
    else:
        sl_ = slice(0, al.size)
    c.update(al=al[sl_], p=p[sl_], Dp=E["Dp"][sl_], Dm=E["Dm"][sl_], D=E["Dp"][sl_] + E["Dm"][sl_],
             srcp=E["srcp"][sl_] - sl_.start, srcm=E["srcm"][sl_] - sl_.start,
             lamB=E["lamB"], lamH=E["lamH"], tp=E["tp"][sl_], tm=E["tm"][sl_])
    return c


def query(c, q):
    """Delta в точках q (на радиусе c['r']) как max/min по (сетка U {q}). Возвращает (Delta, inside)."""
    al, E = c["al_full"], c["E_full"]
    if c["periodic"]:
        q = np.mod(q, 2 * np.pi)
        inside = np.ones(q.size, bool)
    else:
        inside = (q > c["a"]) & (q < c["b"])
    pq = c["phi"](q, c["r"])
    tpq = np.maximum(pq - np.pi / 2, 0.0); tmq = np.minimum(pq + np.pi / 2, 0.0)
    lamB, mH = E["lamB"], -E["lamH"]
    j = np.searchsorted(al, q) - 1               # al[j] < q <= al[j+1]
    n = al.size
    jr = np.clip(j + 1, 0, n - 1); jl = np.clip(j, 0, n - 1)
    hasr = (j + 1 <= n - 1); hasl = (j >= 0)
    R = np.where(hasr, E["R"][jr] - lamB * (al[jr] - q), -np.inf)
    Lf = np.where(hasl, E["Lf"][jl] - mH * (q - al[jl]), -np.inf)
    Rm = np.where(hasr, E["Rm"][jr] + mH * (al[jr] - q), np.inf)
    Lm = np.where(hasl, E["Lm"][jl] + lamB * (q - al[jl]), np.inf)
    Dp = np.maximum(np.maximum(np.maximum(R, Lf), tpq), 0.0)
    Dm = np.minimum(np.minimum(np.minimum(Rm, Lm), tmq), 0.0)
    return Dp + Dm, inside


# ---------------------------------------------------------------- лемма 5 (подвыборка)
def lemma5_check(al, p, eps1, cap=4000):
    hi = np.where(p > np.pi / 2 - 2 * eps1 - 1e-3)[0]
    lo = np.where(p < -np.pi / 2 + 2 * eps1 + 1e-3)[0]

    def sub(ix):
        if ix.size > cap:
            ix = np.unique(np.concatenate([ix[np.linspace(0, ix.size - 1, cap).astype(int)],
                                           ix[np.argsort(np.abs(p[ix]))[-cap // 4:]]]))
        return ix
    hi, lo = sub(hi), sub(lo)
    m6, q7 = np.inf, -np.inf
    if hi.size and lo.size:
        A = al[hi][:, None]; B = al[lo][None, :]
        mask = (B > A) & (B - A <= GAMMA1)
        if mask.any():
            m6 = (p[lo][None, :] - p[hi][:, None] + np.pi)[mask].min()
        A = al[lo][:, None]; B = al[hi][None, :]
        mask = (B > A) & (B - A <= GAMMA1)
        if mask.any():
            q7 = ((p[hi][None, :] - p[lo][:, None] - np.pi) / np.where(mask, B - A, 1.0))[mask].max()
    return m6, q7


def mu_of(Da, rDr, D):
    return np.cos(D) - 0.5 * rDr * np.sin(D) + 0.5 * Da * np.cos(D) - 0.5 * np.sqrt(rDr ** 2 + Da ** 2)


def run_case(name, exf, al0, radii):
    U, phi = make(exf)
    print("=" * 110)
    print(name)
    for r in radii:
        h = min(0.02, 0.2 * r)
        c0 = build(U, phi, r, al0(r))
        cp = build(U, phi, r * (1 + h), al0(r * (1 + h)))
        cm = build(U, phi, r * (1 - h), al0(r * (1 - h)))
        al, p, D = c0["al"], c0["p"], c0["D"]
        eps1, lamB, lamH = c0["eps1"], c0["lamB"], c0["lamH"]
        print("-" * 110)
        print(f"r={r:.0e}: arc=({c0['a']:.10f}, {c0['b']:.10f}){' periodic' if c0['periodic'] else ''}, "
              f"grid {al.size} pts; eps=sup(|phi|-pi/2)^+={c0['eps']:.3e}; max|phi|={np.abs(p).max():.6f} (<pi); "
              f"lamB={lamB}, lamH={lamH:.3e}; eps1<=eta1*gamma1/2: {eps1 <= ETA1 * GAMMA1 / 2}")
        H = p + np.pi / 2; Lb = p - np.pi / 2
        overlap = np.sum((c0["Dp"] > 0) & (c0["Dm"] < 0))
        print(f"  (I): max(Delta-(phi+pi/2))={np.max(D - H):.2e}, max((phi-pi/2)-Delta)={np.max(Lb - D):.2e}; "
              f"#(Delta+>0 & Delta-<0)={overlap}; max|Delta|={np.abs(D).max():.3e} (eps1={eps1:.3e})")
        sl = np.diff(D) / np.diff(al)
        slt = np.diff(c0['tp'] + c0['tm']) / np.diff(al)
        big = np.diff(al) > 1e-9 * (al[-1] - al[0])   # ячейки короче 1e-9 длины дуги дают шум округления
        print(f"  (III): slopes of Delta in [{sl[big].min():.4f}, {sl[big].max():.4f}] vs [lamH, lamB]=[{lamH:.4f}, {lamB}] "
              f"(cells longer than 1e-9 arc length); slopes of tau=Delta_0 in [{slt[big].min():.3f}, {slt[big].max():.3e}]")
        n = al.size
        if c0["periodic"]:
            frac_end = 0.0
        else:
            nend = 300
            endp = (c0["Dp"] > 0) & ((c0["srcp"] < nend) | (c0["srcp"] >= n - nend))
            endm = (c0["Dm"] < 0) & ((c0["srcm"] < nend) | (c0["srcm"] >= n - nend))
            m = (endp | endm) & (np.abs(D - (c0['tp'] + c0['tm'])) > 1e-14)
            frac_end = np.sum(np.diff(al)[m[:-1]]) / (c0['b'] - c0['a'])
        print(f"  endpoint pieces (extremum attained at an arc end and Delta != tau): {frac_end:.3e} of arc length")
        print(f"  (2): min cos(phi-Delta)={np.cos(p - D).min():.3e}  (>=0 <=> <v,grad u> <= 0)")
        Dpl, inp = query(cp, al)
        Dmi, inm = query(cm, al)
        sel = inp & inm
        rDr = (Dpl[sel] - Dmi[sel]) / (2 * h)
        print(f"  (IV): max|r Delta_r| = {np.abs(rDr).max():.3e} (central difference, h={h:g}, "
              f"{sel.sum()} of {n} pts inside arcs at r(1-h), r, r(1+h))")
        Da_f = np.concatenate([sl, sl[-1:]]); Da_b = np.concatenate([sl[:1], sl])
        mm = np.minimum(mu_of(Da_f[sel], rDr, D[sel]), mu_of(Da_b[sel], rDr, D[sel]))
        k = np.argmin(mm)
        mu0 = np.minimum(mu_of(Da_f, 0 * Da_f, D), mu_of(Da_b, 0 * Da_b, D)).min()
        print(f"  (3): min mu = {mm.min():.4f} at alpha={al[sel][k]:.9f} (Delta={D[sel][k]:.2e}, "
              f"Delta_a={Da_f[sel][k]:.3f}/{Da_b[sel][k]:.3f}, rDelta_r={rDr[k]:.2e}); "
              f"min mu with r*Delta_r:=0 over all pts: {mu0:.4f}")
        m6, q7 = lemma5_check(al, p, eps1)
        print(f"  lemma 5 (relevant pairs 0<b-a<=gamma1): (6') min(phi(b)-phi(a)+pi)={m6:.3e} (need >=0; inf: none), "
              f"(7') max (phi(b)-phi(a)-pi)/(b-a)={q7:.3e} (need <=eta1={ETA1}; -inf: none)")


if __name__ == "__main__":
    radii = [1e-1, 1e-2, 1e-3]
    for name, exf, al0 in CASES:
        run_case(name, exf, al0, radii)
