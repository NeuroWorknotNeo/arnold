"""[Эксперимент] Проверка леммы 7.III статьи Паламодова (ФАН 11:4, 1977) на примере
u = -x2*(x1 - x2^2), компонента U^- = {x2 > 0, x1 > x2^2} (сектор между положительной
полуосью x1 и верхней ветвью параболы x1 = x2^2).

Что считаем (при фиксированном малом r, по дуге окружности |x| = r внутри U^-):
  phi(alpha, r)  -- направленный угол от -x к u'(x)  (лемма 2 статьи);
  delta          -- функция delta статьи (с. 48);
  delta'_alpha   -- конечными разностями;
  lambda_H(r) = -2 c r^d / gamma1, c r^d = sup(|phi| - pi/2) на окружности (лемма 3).
Затем поле v статьи в полосе у конца дуги, где Delta = delta (функции Delta_i, i>=1,
там равны нулю, т.к. delta'_alpha не принимает значений lambda_B, lambda_H),
и минимум симметрической части якобиана v' (условие (3) основной леммы).
Для сравнения -- исправленная Delta_fix = min(delta, касательная из конца дуги
с наклоном lambda_H).
Это численная иллюстрация, не доказательство.
"""
import numpy as np
from scipy.optimize import brentq


def grad(x1, x2):
    return np.array([-x2, -x1 + 3 * x2**2])


def phi(alpha, r):
    x1, x2 = r * np.cos(alpha), r * np.sin(alpha)
    g = grad(x1, x2)
    a_minus_x = np.arctan2(-x2, -x1)
    a_g = np.arctan2(g[1], g[0])
    d = a_g - a_minus_x
    return (d + np.pi) % (2 * np.pi) - np.pi


def delta_of_phi(p):
    if p >= np.pi / 2:
        return p - np.pi / 2
    if p <= -np.pi / 2:
        return p + np.pi / 2
    return 0.0


def delta(alpha, r):
    return delta_of_phi(phi(alpha, r))


def alpha_B(r):
    # x1 = x2^2 on the circle: r cos a = r^2 sin^2 a, a in (0, pi/2)
    return brentq(lambda a: np.cos(a) - r * np.sin(a) ** 2, 1e-9, np.pi / 2)


def sym_min_eig(field, x, h=1e-9):
    J = np.zeros((2, 2))
    for j in range(2):
        e = np.zeros(2)
        e[j] = h * max(1.0, np.linalg.norm(x))
        J[:, j] = (field(x + e) - field(x - e)) / (2 * e[j])
    S = 0.5 * (J + J.T)
    return np.linalg.eigvalsh(S)[0], J


def run(r, gamma1=0.5, eta1=2.0):
    aB = alpha_B(r)
    al = np.linspace(1e-6, aB - 1e-9, 200001)
    ph = np.array([phi(a, r) for a in al])
    excess = np.max(np.abs(ph) - np.pi / 2)
    crd = max(excess, 0.0)
    lamH = -2 * crd / gamma1
    de = np.array([delta_of_phi(p) for p in ph])
    neg = de < 0
    pos = de > 0
    print(f"r = {r:g}: arc (0, {aB:.8f}),  sup(|phi|-pi/2) = {excess:.3e} (= c r^d),"
          f"  lambda_H = {lamH:.3e},  lambda_B = eta1 = {eta1}")
    print(f"   points with delta>0: {pos.sum()},  delta<0: {neg.sum()}")
    if neg.any():
        a0, a1 = al[neg][0], al[neg][-1]
        print(f"   strip delta<0: alpha in [{a0:.8f}, {a1:.8f}] (width {a1 - a0:.3e},"
              f" pi/2 - alpha_B = {np.pi/2 - aB:.3e});  delta at end = {de[neg][-1]:.3e}")
        # derivative of delta inside the strip (away from the kink)
        idx = np.where(neg)[0]
        inner = idx[len(idx) // 10: -2]
        dd = np.gradient(de, al)[inner]
        print(f"   delta'_alpha in strip: min {dd.min():.4f}, max {dd.max():.4f}"
              f"  (lambda_H = {lamH:.3e}; is delta' < lambda_H everywhere there? {np.all(dd < lamH)})")
    # derivative of delta where it is nonzero vs lambda values (are there solutions of (11)?)
    dd_all = np.gradient(de, al)
    mask = (de != 0)
    mask[:-1] &= (de[1:] != 0)
    mask[1:] &= (de[:-1] != 0)
    if mask.any():
        print(f"   over all points with delta != 0 (both neighbours too): delta' in "
              f"[{dd_all[mask].min():.4f}, {dd_all[mask].max():.4f}]")

    # field v of the paper in the strip: Delta = delta there
    def v_paper(x):
        rr = np.hypot(*x)
        a = np.arctan2(x[1], x[0])
        D = delta(a, rr)
        c, s = np.cos(D), np.sin(D)
        return np.array([c * x[0] - s * x[1], s * x[0] + c * x[1]])

    # corrected Delta: tangent from the arc end with slope lambda_H, going left
    def Delta_fix(a, rr):
        aBr = alpha_B(rr)
        dB = delta_of_phi(phi(aBr, rr))  # value at the end (continuous extension)
        line = dB + lamH * (a - aBr) if dB < 0 else 0.0
        return min(delta(a, rr), line, 0.0) if dB < 0 else delta(a, rr)

    def v_fix(x):
        rr = np.hypot(*x)
        a = np.arctan2(x[1], x[0])
        D = Delta_fix(a, rr)
        c, s = np.cos(D), np.sin(D)
        return np.array([c * x[0] - s * x[1], s * x[0] + c * x[1]])

    if neg.any():
        idx = np.where(neg)[0]
        for frac in (0.3, 0.6, 0.9):
            a = al[idx[int(frac * (len(idx) - 1))]]
            x = np.array([r * np.cos(a), r * np.sin(a)])
            m_paper, _ = sym_min_eig(v_paper, x, h=1e-7 * r)
            m_fix, _ = sym_min_eig(v_fix, x, h=1e-7 * r)
            p = phi(a, r)
            # check (2) for both: <v,u'> <= 0
            g = grad(*x)
            print(f"   alpha = {a:.8f}: phi = {p:+.6f};  min eig sym(v'_paper) = {m_paper:+.4f},"
                  f"  <v_paper,u'> = {np.dot(v_paper(x), g):+.3e};"
                  f"  min eig sym(v'_fix) = {m_fix:+.4f}, <v_fix,u'> = {np.dot(v_fix(x), g):+.3e}")


if __name__ == "__main__":
    for r in (1e-1, 1e-2, 1e-3):
        run(r)
