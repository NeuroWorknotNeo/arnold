"""
[Эксперимент] Численная проверка оценок предложения G записки notes/prover/2026-10-21-master.md
(не тождеств, а неравенств с явными константами) в случайных точках.

Калибровки: (P) полярная, Om(th) = (th1, th2, 1)/sqrt(1+|th|^2) (гномоническая карта сферы);
            (C) гномоническая плоская, Om(th) = (th1, th2, 1);
            (T) <<трубчатая>> общего вида: Om(th) = (cos th1, sin th1, 0) + th2 (0,0,1) + 0.3 th2^2 (cos th1, sin th1, 0).
Поле: v(s,th) -- случайный многочлен. В случайной точке (s,th) и для случайных w ⊥ Y проверяется:
 (i)   |<grad rho - Y/h, w>| <= Lam^2 |Y_T| |w|
 (ii)  |<w, s nabla_Y Y>|    <= (Lam |psi| + d2 |v|^2) |w|
 (iii) s<w, D_w Y>          >= -[ m (1+Lam^3 |Y_T|)^2 + (Lam^5+Lam^3) C_v |Y_T| + Lam d2 |v| ] |w|^2
где Lam = max(1, |Om|, ||DOm||, ||B^{-1}||), d2 >= ||D^2 Om|| (фробениусова оценка), m >= 0 -- наименьшее с
sym(G(I+D_th v)) >= -m G, C_v = ||I + D_th v|| + |s d_s v|, Y_T -- касательная к уровню rho составляющая Y.
"""
import numpy as np
import sympy as sp

rng = np.random.default_rng(7)
s, p1, p2 = sp.symbols('s p1 p2', real=True)
th = [p1, p2]

def make(Om_expr, vexpr):
    Om = sp.Matrix(Om_expr)
    DOm = Om.jacobian(th)
    D2 = [[sp.diff(Om, th[j], th[k]) for k in range(2)] for j in range(2)]
    v = sp.Matrix(vexpr)
    Dv = v.jacobian(th)
    vs = sp.diff(v, s)
    f = sp.lambdify((s, p1, p2), [Om, DOm, D2, v, Dv, vs], 'numpy')
    return f

def check(fun, pts, label):
    worst = [0.0, 0.0, 0.0]; cnt = 0; viol = 0
    for (sv, a1, a2) in pts:
        Om, DOm, D2, v, Dv, vs = fun(sv, a1, a2)
        Om = np.array(Om, float).reshape(3); DOm = np.array(DOm, float)
        D2 = np.array([[np.array(D2[j][k], float).reshape(3) for k in range(2)] for j in range(2)])
        v = np.array(v, float).reshape(2); Dv = np.array(Dv, float); vs = np.array(vs, float).reshape(2)
        B = np.column_stack([Om, DOm]); Bi = np.linalg.inv(B)
        nu = Bi.T @ np.array([1.0, 0, 0])
        y = Om + DOm @ v
        h = y @ y
        YT = y - (y @ nu) / (nu @ nu) * nu
        G = DOm.T @ DOm
        D2vv = sum(D2[j][k] * v[j] * v[k] for j in range(2) for k in range(2))
        psi = v + Dv @ v + sv * vs
        sDYY = DOm @ psi + D2vv
        Lam = max(1.0, np.linalg.norm(Om), np.linalg.norm(DOm, 2), np.linalg.norm(Bi, 2))
        d2 = np.sqrt(sum(np.sum(D2[j][k]**2) for j in range(2) for k in range(2)))
        M = G @ (np.eye(2) + Dv); Ms = (M + M.T) / 2
        Gh = np.linalg.cholesky(G); Ghi = np.linalg.inv(Gh)
        lam_min = np.linalg.eigvalsh(Ghi @ Ms @ Ghi.T).min()
        m = max(0.0, -lam_min)
        Cv = np.linalg.norm(np.eye(2) + Dv, 2) + np.linalg.norm(vs)
        for _ in range(30):
            w = rng.normal(size=3); w = w - (w @ y) / h * y   # w ⊥ Y
            ab = Bi @ w; al, tau = ab[0], ab[1:]
            # D_w Y: s D_w Y = B(0,(I+Dv)tau + al s v_s) + D2Om(v,tau)
            D2vt = sum(D2[j][k] * v[j] * tau[k] for j in range(2) for k in range(2))
            sDwY = DOm @ ((np.eye(2) + Dv) @ tau + al * sv * vs) + D2vt
            nw = np.linalg.norm(w)
            lhs1 = abs((nu - y / h) @ w); rhs1 = Lam**2 * np.linalg.norm(YT) * nw
            lhs2 = abs(w @ sDYY); rhs2 = (Lam * np.linalg.norm(psi) + d2 * (v @ v)) * nw
            lhs3 = w @ sDwY
            rhs3 = -(m * (1 + Lam**3 * np.linalg.norm(YT))**2 + (Lam**5 + Lam**3) * Cv * np.linalg.norm(YT)
                     + Lam * d2 * np.linalg.norm(v)) * nw**2
            cnt += 1
            r = [lhs1 / max(rhs1, 1e-300), lhs2 / max(rhs2, 1e-300), (-lhs3) / max(-rhs3, 1e-300)]
            worst = [max(worst[i], r[i]) for i in range(3)]
            if lhs1 > rhs1 * (1 + 1e-12) or lhs2 > rhs2 * (1 + 1e-12) or lhs3 < rhs3 * (1 + 1e-12) - 1e-14:
                viol += 1
    print('%s: проверено %d пар (точка, w); нарушений: %d; max отношения левой части к правой (i),(ii),(iii): %s'
          % (label, cnt, viol, ['%.3g' % x for x in worst]))

def randpoly(scale):
    c = rng.normal(size=6) * scale
    return c[0] + c[1]*p1 + c[2]*p2 + c[3]*s + c[4]*p1*p2 + c[5]*s*p1**2

pts = [(rng.uniform(0.01, 0.5), rng.uniform(-0.6, 0.6), rng.uniform(-0.6, 0.6)) for _ in range(60)]
for scale in (0.05, 0.5):
    vexpr = [randpoly(scale), randpoly(scale)]
    r = sp.sqrt(1 + p1**2 + p2**2)
    check(make([p1 / r, p2 / r, 1 / r], vexpr), pts, '(P) полярная, |v|~%.2f' % scale)
    check(make([p1, p2, 1], vexpr), pts, '(C) гномоническая, |v|~%.2f' % scale)
    check(make([sp.cos(p1) * (1 + 0.3 * p2**2), sp.sin(p1) * (1 + 0.3 * p2**2), p2], vexpr), pts,
          '(T) трубчатого типа, |v|~%.2f' % scale)

# стресс-тест (iii): поле с сильно отрицательной D_th v (m > 0), чтобы главный член был отрицателен
for k in (1.5, 3.0):
    vexpr = [-k * p1 + randpoly(0.1) + 0.7 * p2, -k * p2 + randpoly(0.1) - 0.4 * p1]
    r = sp.sqrt(1 + p1**2 + p2**2)
    check(make([p1 / r, p2 / r, 1 / r], vexpr), pts, '(P) стресс, D v ~ -%.1f I' % k)
    check(make([p1, p2, 1], vexpr), pts, '(C) стресс, D v ~ -%.1f I' % k)
    check(make([sp.cos(p1) * (1 + 0.3 * p2**2), sp.sin(p1) * (1 + 0.3 * p2**2), p2], vexpr), pts,
          '(T) стресс, D v ~ -%.1f I' % k)
