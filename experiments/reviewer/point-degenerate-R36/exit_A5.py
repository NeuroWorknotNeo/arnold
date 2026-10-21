"""R36: независимая численная проверка строгого выхода (A5) теоремы A [007]
для примеров Lambda (поле Y=q/z из следствия R и, для сравнения, Y=e_z) и X (Y=e_z, xi=Cb),
а также кольца R (Y = e_z + C(x,y,0)/z, xi=0, следствие S).

Xi = d/dt (V - delta rho^beta) вычисляется ПРЯМЫМ дифференцированием V(q,v) вдоль поля
системы (q' = v, v' = -grad U), без леммы 1 [007]. V = |v|^2/2 - <v,Y>^2/(2|Y|^2) + U + a0 rho^beta,
rho = z. Точки множества (A5): q = (z^c1 b1, z^c2 b2, z), P(s,b) = W/rho^beta <= delta,
v = -lam Y + sqrt(2 K_perp) e, e _|_ Y, |e| = 1, K_perp = delta rho^beta - W,
lam = sqrt(2(A - delta rho^beta)/|Y|^2)  (тогда E = 0, p < 0, V = delta rho^beta).
Печатается min (rho/lam) Xi / (delta rho^beta) по сетке.
[Эксперимент] mpmath, 40 знаков. Запуск: ~/venv/bin/python exit_A5.py
"""
import sys
import sympy as sp
import mpmath as mp

mp.mp.dps = 40
x, y, z, v1, v2, v3 = sp.symbols('x y z v1 v2 v3', real=True)
q = sp.Matrix([x, y, z])
v = sp.Matrix([v1, v2, v3])


def build(U, Y, beta, a0, delta):
    rho = z
    h = (Y.T * Y)[0]
    p = (v.T * Y)[0]
    V = (v.T * v)[0] / 2 - p**2 / (2 * h) + U + a0 * rho**beta
    G = V - delta * rho**beta
    gradU = sp.Matrix([sp.diff(U, w) for w in q])
    Xi = sum(sp.diff(G, q[i]) * v[i] for i in range(3)) + sum(sp.diff(G, v[i]) * (-gradU[i]) for i in range(3))
    fXi = sp.lambdify((x, y, z, v1, v2, v3), Xi, 'mpmath')
    fU = sp.lambdify((x, y, z), U, 'mpmath')
    fY = sp.lambdify((x, y, z), list(Y), 'mpmath')
    return fXi, fU, fY


def scan(name, U, Y, beta, a0, c, delta, rho_list, box, n=61, ndir=16, Pfun=None):
    fXi, fU, fY = build(U, Y, beta, a0, delta)
    res = []
    for rho in rho_list:
        rho = mp.mpf(rho)
        best = (mp.inf, None)
        cnt = 0
        for i in range(n):
            for j in range(n):
                bb1 = box[0][0] + (box[0][1] - box[0][0]) * mp.mpf(i) / (n - 1)
                bb2 = box[1][0] + (box[1][1] - box[1][0]) * mp.mpf(j) / (n - 1)
                X = rho**c[0] * bb1
                Yc = rho**c[1] * bb2
                Z = rho
                Uv = fU(X, Yc, Z)
                W = Uv + a0 * rho**beta
                if W > delta * rho**beta:      # вне D: P > delta
                    continue
                cnt += 1
                Yv = [mp.mpf(t) for t in fY(X, Yc, Z)]
                hv = sum(t * t for t in Yv)
                Kp = delta * rho**beta - W
                lam = mp.sqrt(2 * (a0 * rho**beta - delta * rho**beta) / hv)
                # ортонормированный базис Y^perp
                yn = [t / mp.sqrt(hv) for t in Yv]
                a = [1, 0, 0] if abs(yn[0]) < 0.9 else [0, 1, 0]
                d = sum(a[k] * yn[k] for k in range(3))
                e1 = [a[k] - d * yn[k] for k in range(3)]
                ne = mp.sqrt(sum(t * t for t in e1)); e1 = [t / ne for t in e1]
                e2 = [yn[1] * e1[2] - yn[2] * e1[1], yn[2] * e1[0] - yn[0] * e1[2], yn[0] * e1[1] - yn[1] * e1[0]]
                for kdir in range(ndir):
                    th = 2 * mp.pi * kdir / ndir
                    ee = [mp.cos(th) * e1[k] + mp.sin(th) * e2[k] for k in range(3)]
                    vv = [-lam * Yv[k] + mp.sqrt(2 * Kp) * ee[k] for k in range(3)]
                    # контроль: E = 0, V = delta rho^beta
                    E = sum(t * t for t in vv) / 2 + Uv
                    assert abs(E) < mp.mpf(10)**(-25) * rho**beta, E
                    val = (rho / lam) * fXi(X, Yc, Z, *vv) / (delta * rho**beta)
                    if val < best[0]:
                        best = (val, (float(bb1), float(bb2), float(th)))
        res.append((float(rho), float(best[0]), best[1], cnt))
        print(f"{name}: delta={delta}, rho={float(rho):.1e}: min (rho/lam)Xi/(delta rho^beta) = "
              f"{mp.nstr(best[0], 6)} at (b1,b2,theta)={best[1]}; points in D: {cnt}", flush=True)
    return res


if __name__ == '__main__':
    which = sys.argv[1:] or ['Lambda', 'X', 'R']
    k = sp.Rational(199, 100)
    if 'Lambda' in which:
        U = x**4 - k * x**2 * y * z + y**2 * z**2 + y**4 - z**8 + x * z**7
        # Q = (b2 - k/2 b1^2)^2 + 399/40000 b1^4 <= delta: |b1| <= (delta*40000/399)^(1/4), b2 около k/2 b1^2
        for delta in (mp.mpf('0.05'), mp.mpf('0.01')):
            b1max = float((delta * 40000 / 399)**0.25) * 1.05
            b2max = float(k / 2) * b1max**2 + float(mp.sqrt(delta)) * 1.1
            box = ((-b1max, b1max), (-float(mp.sqrt(delta)) * 1.1, b2max))
            Yrad = sp.Matrix([x / z, y / z, 1])
            scan('Lambda, Y=q/z', U, Yrad, 8, 1, (2, 3), delta, ['1e-3', '1e-4'], box, n=81)
            scan('Lambda, Y=e_z', U, sp.Matrix([0, 0, 1]), 8, 1, (2, 3), delta, ['1e-3', '1e-4'], box, n=81)
    if 'X' in which:
        U = x**6 + y**6 + y**4 * z**2 + x**2 * y**2 * z**2 - z**12 + x * z**11
        for delta in (mp.mpf('0.05'), mp.mpf('0.01')):
            b1max = float(delta**(mp.mpf(1) / 6)) * 1.05
            b2max = float(delta**(mp.mpf(1) / 4)) * 1.05
            box = ((-b1max, b1max), (-b2max, b2max))
            scan('X, Y=e_z', U, sp.Matrix([0, 0, 1]), 12, 1, (2, sp.Rational(5, 2)), delta,
                 ['1e-3', '1e-5'], box, n=81)
    if 'R' in which:
        U = (x**2 + y**2 - z**3)**2 - z**8 + x * z**8
        Yh = sp.Matrix([sp.Rational(3, 2) * x / z, sp.Rational(3, 2) * y / z, 1])
        for delta in (mp.mpf('0.05'),):
            box = ((-1.3, 1.3), (-1.3, 1.3))
            scan('R, Y=e_z+C(x,y)/z', U, Yh, 8, 1, (sp.Rational(3, 2), sp.Rational(3, 2)), delta,
                 ['1e-4', '1e-6', '1e-8'], box, n=161, ndir=8)
