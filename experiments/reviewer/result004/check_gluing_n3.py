"""[Эксперимент] Независимая проверка предложения 3 (склейка карт) из results/004-lemmaR.md
(reviewer, 21.10.2026).

Карта alpha -- карта из check_chart_n3.py (n = 3, s = 1, k = 1, нелинейная G, H != 0).
Карта beta -- то же глобальное отображение в других координатах:
  (theta, y) = tau(theta', y') = (theta' + 0.3 sin theta',  g(theta') y' + h(theta')),
  g = 1.3 + 0.2 cos theta', h = 0.4 sin theta'.
Тогда G_beta(theta', mu', eps) = G_alpha(theta(theta'), g mu' + eps^a h, eps) класса C^infty,
(O) с теми же подпространствами, F_beta = F_alpha o tau, H_beta = H_alpha(tau(.), eps), (C1) выполнено.
Поле: A = V + phi_a W_alpha + (1 - phi_a) W_beta;  phi_a = psi(theta) (как в (C2)) или
psi(theta + 0.3 y) (зависит и от нормальной координаты -- проверка, нужна ли угловая зависимость).
Ожидание по предложению 3: ||DA - L|| = O(r^kappa_*), kappa_* = 1/4; A(U) = dU + (1-chi)U_+.

Запуск: ~/venv/bin/python check_gluing_n3.py
Это не доказательство: один пример.
"""
import sympy as sp
import mpmath as mp
from check_chart_n3 import make_chart, coords_data, What, DA_of, chi, hstep

mp.mp.dps = 80


def tau(tp, yp):
    g = mp.mpf('1.3') + mp.mpf('0.2') * mp.cos(tp)
    h = mp.mpf('0.4') * mp.sin(tp)
    return tp + mp.mpf('0.3') * mp.sin(tp), g * yp + h


def tau_inv(t_, y_):
    tp = mp.findroot(lambda u: u + mp.mpf('0.3') * mp.sin(u) - t_, t_ / mp.mpf('1.3'))
    g = mp.mpf('1.3') + mp.mpf('0.2') * mp.cos(tp)
    h = mp.mpf('0.4') * mp.sin(tp)
    return tp, (y_ - h) / g


def Dtau(tp, yp):
    """Jacobian of (r, theta', y') -> (r, theta, y)."""
    g = mp.mpf('1.3') + mp.mpf('0.2') * mp.cos(tp)
    dg = -mp.mpf('0.2') * mp.sin(tp)
    dh = mp.mpf('0.4') * mp.cos(tp)
    return mp.matrix([[1, 0, 0], [0, 1 + mp.mpf('0.3') * mp.cos(tp), 0], [0, dg * yp + dh, g]])


def make_Z_glued(C, Jset, phi):
    def Z(p):
        e_, t_, y_ = p
        r = e_**C['N']
        DP, rdrU, Ut, Uy, U, Fv = coords_data(C, p)
        Wa, _ = What(C, rdrU, Ut, Uy, U, Fv, r, Jset)
        # chart beta at the same point
        tp, yp = tau_inv(t_, y_)
        Dt = Dtau(tp, yp)
        Utp = Ut * Dt[1, 1] + Uy * Dt[2, 1]
        Uyp = Uy * Dt[2, 2]
        Wb, _ = What(C, rdrU, Utp, Uyp, U, Fv, r, Jset)
        Wb_in_alpha = Dt * mp.matrix(Wb)
        ph = phi(t_, y_)
        Ah = mp.matrix([r, 0, 0]) + ph * mp.matrix(Wa) + (1 - ph) * Wb_in_alpha
        return DP * Ah
    return Z


def run(C, Jset, phi, label, kappa, rs):
    L = mp.diag([1, 1, C['w1']])
    print(label)
    pts = []
    for t_ in ['0.35', '0.45', '0.6', '0.75', '0.85']:
        for i in range(17):
            pts.append((mp.mpf(t_), mp.mpf('-1.9') + mp.mpf('3.8') * i / 16))
        tv = mp.mpf(t_)
        for Fv in ['0.3', '0.4', '-0.3', '-0.4']:
            yy2 = mp.mpf(Fv) + mp.cos(tv) + mp.mpf('0.5')
            if yy2 > 0:
                pts += [(tv, mp.sqrt(yy2)), (tv, -mp.sqrt(yy2))]
    Z = make_Z_glued(C, Jset, phi)
    for rv in rs:
        r = mp.mpf(rv)
        e_ = r**(mp.mpf(1) / C['N'])
        dev, lmin, idmax, gl = 0, mp.inf, 0, 0
        for (t_, y_) in pts:
            p = [e_, t_, y_]
            DA = DA_of(Z, C, p)
            ev = mp.eigsy((DA + DA.T) / 2)[0]
            lmin = min(lmin, min(ev[i] for i in range(3)))
            dev = max(dev, mp.norm(DA - L, 2))
            DP, rdrU, Ut, Uy, U, Fv = coords_data(C, p)
            gx = mp.matrix([[rdrU / r, Ut, Uy]]) * mp.inverse(DP)
            AU = (gx * Z(p))[0, 0]
            idmax = max(idmax, abs(AU - C['d'] * U - (1 - chi(Fv)) * (rdrU - C['d'] * U)) / r**C['d'])
        print(f"  r={rv}: max||DA-L||_F={mp.nstr(dev, 6)}  /r^kappa={mp.nstr(dev / r**kappa, 6)}  "
              f"min eig sym DA={mp.nstr(lmin, 8)}  max|A(U)-dU-(1-chi)U+|/r^d={mp.nstr(idmax, 3)}")


if __name__ == '__main__':
    rs = ['1e-4', '1e-8', '1e-12', '1e-16', '1e-20', '1e-24']
    psi = lambda t_, y_: 1 - hstep((t_ - mp.mpf('0.3')) / mp.mpf('0.6'))
    psi_y = lambda t_, y_: 1 - hstep((t_ + mp.mpf('0.3') * y_ - mp.mpf('0.3')) / mp.mpf('0.6'))
    C1 = make_chart(4, sp.Rational(3, 2), sp.Rational(3, 4), 2)
    run(C1, {'r', '0', '1'}, psi, 'G1: E1-data, J={r,0,1}, phi_alpha = psi(theta)', mp.mpf(1) / 4, rs)
    run(C1, {'r', '0', '1'}, psi_y, 'G2: E1-data, J={r,0,1}, phi_alpha = psi(theta + 0.3 y) (not angular-only)',
        mp.mpf(1) / 4, rs)
    C2 = make_chart(4, sp.Rational(3, 2), sp.Rational(1, 4), 2)
    run(C2, {'1'}, psi_y, 'G3: E2-data (e=1/4), J={1}, phi_alpha = psi(theta + 0.3 y) (not angular-only)',
        mp.mpf(1) / 4, rs)
