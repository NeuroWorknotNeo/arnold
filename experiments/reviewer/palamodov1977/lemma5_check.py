"""[Эксперимент] Проверка неравенств (6), (7) леммы 5 на дуге U^- (угол поднят на (a, b))
для примеров u1, u2 при gamma1 = 0.5, eta1 = 2: чтобы убедиться, что нарушение III
в lemma7_check.py возникает не из-за нарушения посылок."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import lemma7_check as L

gamma1, eta1 = 0.5, 2.0
for name in L.EXAMPLES:
    uu, phi = L.make(name)
    for r in (1e-2, 1e-3):
        for (a, b, _) in L.arcs(uu, r, n=2000000):
            # dense near the ends, coarse in the middle
            al = np.unique(np.concatenate([np.linspace(a + 1e-12, b - 1e-12, 3001),
                                           np.linspace(a + 1e-12, a + 5 * r, 1001),
                                           np.linspace(b - 5 * r, b - 1e-12, 1001)]))
            ph = phi(al, r)
            A, B = np.meshgrid(al, al, indexing="ij")
            PA, PB = np.meshgrid(ph, ph, indexing="ij")
            ge = B >= A
            d = PB - PA
            m6 = (d + np.pi)[ge & (B - A <= gamma1)].min()
            m7 = (d - np.pi - eta1 * (B - A))[ge].max()
            print(f"{name}, r={r:g}, arc ({a:.5f},{b:.5f}): min[(6) phi(b)-phi(a)+pi] = {m6:+.3e} (>=0 needed),"
                  f" max[(7) phi(b)-phi(a)-pi-eta1(b-a)] = {m7:+.3e} (<=0 needed)")
