"""[Эксперимент] Теорема T (полосовое треугольное поле) — построение по рецепту доказательства.

Поле xi^Lam = (f(b1), Lam * d_2 Q(b)),  f(b1) = b1 - p1  (широкая компонента зависит только от b1: условие (T)).
Нужно на K = {|b - p| <= r', Q <= 2 delta}:
        xi^Lam . grad Q >= mu (Q - eta),   mu = 1 (меньше константы леммы P для всех профилей), eta = delta/8.
Рецепт: g := f d_1Q - mu (Q - eta);  Z := {g <= 0} ∩ K  (по лемме P Z не пересекает полярную кривую);
        Lam_0 := max_Z (-g) / (d_2 Q)^2.  Затем Lam = 1.5 Lam_0 проверяется на независимой случайной выборке K.
Печатаются: Lam_0(delta), min_Z |d_2 Q| (отделённость Z от полярной кривой), M1 = max_K ||D xi^Lam||,
и минимальный запас  min_K (xi.grad Q - mu (Q - eta)) / (mu eta)  на проверочной выборке (нужно >= 0).

Профили — как в lemma_P_check.py (x — широкая переменная профиля, y — узкая):
  Q62 = A*B (x = b1);  Qt2 = A*B + x^24;  PO2D = A*B (x = sin th cos th, b1 = th);
  PO1 = G1*G2 (x = sin th cos th, b1 = th, k = 1.99);  PO2 = (y^2 - x)^2 (x = sin th, b1 = th; локально у складки).
Запуск: ~/venv/bin/python band_T.py [имена профилей]
"""
import sys
import numpy as np
import sympy as sp

X, Y = sp.symbols('x y', real=True)
A_ = (X - Y**2)**2 + Y**8
B_ = (X - Y**2 - Y**3)**2 + Y**8
k = sp.Rational(199, 100)
G1 = Y**2 + k * X**2 * Y + X**4
G2 = X**2 + k * X * Y**2 + Y**4
ARCSIN2 = (lambda x: 0.5 * np.arcsin(2 * x), lambda x: 1.0 / np.sqrt(1 - 4 * x * x))   # th(x), dth/dx  (x = sin th cos th)
ARCSIN = (lambda x: np.arcsin(x), lambda x: 1.0 / np.sqrt(1 - x * x))                   # x = sin th
IDENT = (lambda x: x, lambda x: np.ones_like(x))
PROFILES = {
    'Q62': (A_ * B_, IDENT, 0.45),
    'Qt2': (A_ * B_ + X**24, IDENT, 0.45),
    'PO2D': (A_ * B_, ARCSIN2, 0.45),
    'PO1': (G1 * G2, ARCSIN2, 0.45),
    'PO2': ((Y**2 - X)**2, ARCSIN, 0.3),
}
MU = 1.0


class Profile:
    def __init__(self, Q, chart, r):
        self.r = r
        self.th, self.dth = chart
        self.f = sp.lambdify((X, Y), [Q, sp.diff(Q, X), sp.diff(Q, Y), sp.diff(Q, Y, 2), sp.diff(Q, X, Y)], 'numpy')
        P = sp.Poly(sp.expand(Q), X)
        self.cx = [sp.lambdify(Y, c, 'numpy') for c in P.all_coeffs()]

    def eval(self, x, y):
        """Значения в координатах (b1, b2) = (th(x), y): Q, d1Q, d2Q, d22Q, d12Q (d1 = d/db1)."""
        Q, Qx, Qy, Qyy, Qxy = [np.broadcast_to(np.asarray(v, dtype=float), np.shape(x)) for v in self.f(x, y)]
        dxdb = 1.0 / self.dth(x)                    # dx/db1
        return Q, Qx * dxdb, Qy, Qyy, Qxy * dxdb

    def sample(self, delta, ny, nx, rng=None):
        """Точки K = {|b| <= r, Q <= 2 delta}: по узкой y — сетка, по x — интервалы {Q(., y) <= 2delta} (корни)."""
        r = self.r
        ys = np.concatenate([np.linspace(-r, r, ny), np.sign(np.linspace(-1, 1, 600)) * np.logspace(-7, np.log10(r), 600)])
        xs_all, ys_all = [], []
        for y in ys:
            c = np.array([float(cf(y)) for cf in self.cx])
            c[-1] -= 2 * delta
            rts = np.roots(c)
            rts = np.sort(rts[np.abs(rts.imag) < 1e-10].real)
            xmax = 0.499 if self.th is ARCSIN2[0] else (0.999 if self.th is ARCSIN[0] else 10.0)
            ends = np.concatenate([[-xmax], rts[(rts > -xmax) & (rts < xmax)], [xmax]])
            for a, b in zip(ends[:-1], ends[1:]):
                mid = 0.5 * (a + b)
                if self.eval(np.array([mid]), y)[0][0] > 2 * delta:
                    continue
                t = rng.random(nx) if rng is not None else 0.5 - 0.5 * np.cos(np.pi * np.linspace(0, 1, nx))
                xs = a + (b - a) * t
                # сгущение (лог-шкала) около критических точек Q(., y) на интервале: там тонкий слой у нулевого множества
                dc = np.polyder(c)
                crit = np.roots(dc) if len(dc) > 1 else np.array([])
                crit = crit[np.abs(crit.imag) < 1e-10].real
                crit = crit[(crit > a) & (crit < b)]
                if len(crit):
                    hs = np.logspace(-14, np.log10(max(b - a, 1e-14)), 40)
                    if rng is not None:
                        hs = hs * (0.5 + rng.random(40))
                    extra = np.concatenate([cc + sg * hs for cc in crit for sg in (1, -1)] + [crit])
                    xs = np.concatenate([xs, extra[(extra > a) & (extra < b)]])
                keep = self.th(xs)**2 + y * y <= r * r
                xs_all.append(xs[keep])
                ys_all.append(np.full(keep.sum(), y))
        return np.concatenate(xs_all), np.concatenate(ys_all)


def run(name, delta, ny=3001, nx=80):
    Q, chart, r = PROFILES[name]
    pr = Profile(Q, chart, r)
    eta = delta / 8
    x, y = pr.sample(delta, ny, nx)
    b1 = pr.th(x)
    Qv, Q1, Q2, Q22, Q12 = pr.eval(x, y)
    g = b1 * Q1 - MU * (Qv - eta)
    Z = g <= 0
    if Z.any():
        lam0 = np.max(-g[Z] / Q2[Z]**2)
        sepZ = np.min(np.abs(Q2[Z]))
    else:
        lam0, sepZ = 0.0, np.inf
    lam = 1.5 * lam0
    # ||D xi|| для xi = (b1, lam d2Q): D xi = [[1, 0], [lam d12Q, lam d22Q]]
    M1 = np.max(np.sqrt(1 + (lam * Q12)**2 + (lam * Q22)**2))
    rng = np.random.default_rng(12345)
    xc, yc = pr.sample(delta, 2 * ny + 1, nx, rng)
    b1c = pr.th(xc)
    Qc, Q1c, Q2c, _, _ = pr.eval(xc, yc)
    marg = (b1c * Q1c + lam * Q2c**2 - MU * (Qc - eta)) / (MU * eta)
    i = np.argmin(marg)
    print(f'{name:5s} delta={delta:.0e}: |K-sample|={len(x)}, |Z|={Z.sum()}, Lam_0={lam0:.4e}, min_Z|d2Q|={sepZ:.3e}, '
          f'M1(Lam=1.5Lam_0)={M1:.3e}; check on {len(xc)} pts: min margin/(mu eta)={marg[i]:.4f} '
          f'at b=({b1c[i]:.4f},{yc[i]:.4f}), Q/delta={Qc[i] / delta:.3f}', flush=True)
    return lam0


if __name__ == '__main__':
    names = sys.argv[1:] or list(PROFILES)
    for nm in names:
        res = []
        for d in (1e-4, 1e-5, 1e-6, 1e-7, 1e-8):
            res.append((d, run(nm, d)))
        ds = np.log10([a for a, _ in res]); ls = np.log10([max(b, 1e-300) for _, b in res])
        if all(b > 0 for _, b in res):
            print(f'   {nm}: fitted Lam_0 ~ delta^{np.polyfit(ds, ls, 1)[0]:.3f}')
