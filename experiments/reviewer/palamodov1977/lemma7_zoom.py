"""[Эксперимент] То же, что lemma7_check.py, но для u2 = x1^5 - (x2 - x1^2)^2 на неравномерной
сетке, сгущённой у концов дуги и у левой ветви параболы (alpha ~ pi - r), где у delta
есть узкий отрицательный «горб» ширины ~ r^2. Цель: убедиться, что внутренние куски
Delta_i статьи этот горб обрабатывают (проверка реализации), а нарушение III остаётся
только у конца дуги."""
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lemma7_check as L

name = "u2=x1^5-(x2-x1^2)^2"
uu, phi = L.make(name)
gamma1, eta1 = 0.5, 2.0
for r in (1e-2, 1e-3):
    (a, b, _), = L.arcs(uu, r, n=2000000)
    eps = 1e-10
    parts = [np.linspace(a + eps, b - eps, 400001),
             np.linspace(a + eps, a + 20 * r, 400001),
             np.linspace(np.pi - 3 * r, np.pi + 2 * r, 2000001),
             np.linspace(b - 20 * r, b - eps, 400001)]
    al = np.unique(np.concatenate(parts))
    ph = phi(al, r)
    de = L.delta_of(ph)
    crd = float(np.max(np.abs(ph) - np.pi / 2))
    lamH, lamB = -2 * crd / gamma1, eta1
    dd = np.gradient(de, al)
    nz = de != 0
    nz2 = nz.copy(); nz2[1:] &= nz[:-1]; nz2[:-1] &= nz[1:]
    pieces, sols = [], []
    for lam in (lamB, lamH):
        f = dd - lam
        ch = np.where(nz2[:-1] & nz2[1:] & (np.sign(f[:-1]) != np.sign(f[1:])))[0]
        for k in ch:
            sols.append((al[k], lam, de[k]))
            pieces.append(L.tangent_piece(al, al[k], de[k], lam))
    D = L.combine(de, pieces)
    dD = np.gradient(D, al)
    bad = (dD < lamH - 1e-6) | (dD > lamB + 1e-6)
    print(f"r={r:g}: arc ({a:.6f},{b:.6f}), c r^d={crd:.3e}, lambda_H={lamH:.3e}; grid {al.size}")
    print("  solutions of (11) with delta != 0 (alpha_i, lambda, delta_i):",
          [(round(s[0], 7), round(s[1], 4), float('%.3e' % s[2])) for s in sols])
    neg = np.where(de < 0)[0]
    if neg.size:
        print(f"  delta<0 on alpha in [{al[neg[0]]:.7f}, {al[neg[-1]]:.7f}], min delta {de.min():.3e}")
    pos = np.where(de > 0)[0]
    if pos.size:
        print(f"  delta>0 on alpha in [{al[pos[0]]:.7f}, {al[pos[-1]]:.7f}], max delta {de.max():.3e}")
    if bad.any():
        ib = np.where(bad)[0]
        clusters = np.split(ib, np.where(np.diff(ib) > 5)[0] + 1)
        for c in clusters:
            print(f"  III violated on alpha in [{al[c[0]]:.7f}, {al[c[-1]]:.7f}] ({c.size} pts),"
                  f" Delta' in [{dD[c].min():.3f}, {dD[c].max():.3f}]")
    else:
        print("  III holds")
