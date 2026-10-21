"""[Эксперимент] К замечанию R2 заметки notes/prover/2026-10-21-gt3.md («κ-срезы»).

Однородный потенциал U = (x^2 - y^2)(x^2 + y^2)^2 на плоскости, beta = 6, направление оврага --
ось y (f = U|_S имеет там невырожденный минимум -1, f'' = 4 < beta|f| = 6), поэтому
декартов («вертикальный») срез y = const не даёт минимума на дне и условие (V) теоремы 2 в
декартовой карте нарушено. Проверяем численно знак Xi на границе множества Omega для срезов
rho_k = r^(1-k) y^k, Y = grad rho / |grad rho|^2 (0 < k < 1), по формуле (3.3) заметки.
Это не доказательство.
"""
import numpy as np
from scipy.optimize import minimize_scalar, brentq

BETA = 6


def U(q):
    x, y = q
    return (x * x - y * y) * (x * x + y * y) ** 2


def gradU(q, e=1e-7):
    return np.array([(U(q + e * d) - U(q - e * d)) / (2 * e) for d in np.eye(2)])


def make(k):
    def rho(q):
        x, y = q
        r = np.hypot(x, y)
        return r ** (1 - k) * y ** k

    def grho(q, e=1e-7):
        return np.array([(rho(q + e * d) - rho(q - e * d)) / (2 * e) for d in np.eye(2)])

    def Y(q):
        g = grho(q)
        return g / (g @ g)

    def DY(q, w, e=1e-6):
        return (Y(q + e * w) - Y(q - e * w)) / (2 * e)

    # точка среза rho = 1 с полярным углом alpha от оси y
    def slice_pt(al):
        d = np.array([np.sin(al), np.cos(al)])
        return d / rho(d)

    res = minimize_scalar(lambda al: U(slice_pt(al)), bounds=(-0.5, 0.5), method='bounded')
    a = -res.fun
    return rho, grho, Y, DY, slice_pt, a, res.x


def scan(k, delta, nal=200, nsign=2):
    rho, grho, Y, DY, slice_pt, a, al0 = make(k)
    worst = np.inf
    for al in np.linspace(-0.6, 0.6, nal):
        q = slice_pt(al)
        W = U(q) + a  # A(rho) = a rho^6, rho = 1
        K = delta - W
        if K < 0:
            continue
        Yv = Y(q)
        h = Yv @ Yv
        tdir = np.array([-Yv[1], Yv[0]]) / np.sqrt(h)
        for sg in ([1, -1] if K > 0 else [1]):
            vperp = sg * np.sqrt(2 * K) * tdir
            pi = -np.sqrt(2 * h * (a - delta))
            lam = -pi / h
            YW = gradU(q) @ Yv + BETA * a  # A'(rho) Y rho = 6a
            main = BETA * delta - YW
            T2 = -lam * (vperp @ DY(q, Yv))
            T3 = vperp @ DY(q, vperp)
            val = (main + T2 + T3) / delta
            worst = min(worst, val)
    return worst, a, al0


if __name__ == '__main__':
    print('k=1 (декартов срез): минимум U на срезе не на оси y:')
    for k in [1.0, 0.5, 0.3, 0.2, 0.1, 0.05]:
        try:
            rho, grho, Y, DY, slice_pt, a, al0 = make(k)
            vert = U(slice_pt(0.0)) + a
            print(f'k={k}: argmin угла на срезе = {al0:+.4f}, W(ось y) = {vert:.3e}')
        except Exception as ex:
            print(k, ex)
    for k in [0.5, 0.3, 0.2, 0.1, 0.05]:
        for delta in [0.02, 0.05, 0.1]:
            w, a, al0 = scan(k, delta)
            print(f'k={k:4.2f} delta={delta:5.2f}: min (rho/lambda) Xi/(delta rho^6) = {w:+.4f}   (a={a:.4f})')
