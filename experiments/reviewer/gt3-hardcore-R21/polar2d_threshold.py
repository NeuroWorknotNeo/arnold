"""Рецензент R21: порог kappa, при котором в модельном примере polar2d_exit.py пропадает
строгий выход (A5), и сравнение с допустимыми по (7.2) значениями.

[Эксперимент] Не доказательство: иллюстрация того, что перекрёстные члены реально мешают
(при большом kappa выход пропадает), и того, насколько условие (7.2) грубое.
Запуск: ~/venv/bin/python polar2d_threshold.py
"""
import numpy as np
from polar2d_exit import min_exit

for (b_, a_, g_) in [(6, 1.0, 1.0), (6, 1.0, 0.2), (4, 1.0, 0.05), (10, 1.0, 1.0)]:
    lam0 = g_ / 4
    k72 = b_ * lam0 / (a_ * (1.5 * np.sqrt(3) * b_ + 2 * np.sqrt(2))**2)
    # ослабленный вариант (замечание рецензента): [sqrt(a0/lam0)(sqrt6/2 b g1 + 2sqrt2 g2)]^2 < 4 b mu
    # с g1 = kappa, g2 <= kappa, mu = kappa
    krel = 4 * b_ * lam0 / (a_ * (np.sqrt(6) / 2 * b_ + 2 * np.sqrt(2))**2)
    lo, hi = 1e-4, 1.0
    if min_exit(b_, a_, g_, hi, 1e-6, npts=401)[0] > 0:
        print(b_, a_, g_, "выход есть при kappa=1")
        continue
    for _ in range(40):
        mid = np.sqrt(lo * hi)
        if min_exit(b_, a_, g_, mid, 1e-6, npts=401)[0] > 0:
            lo = mid
        else:
            hi = mid
    print(f"beta={b_} a0={a_} g={g_}: порог kappa ~ {lo:.4f};  (7.2) допускает kappa <= {k72:.5f};"
          f"  ослабленное условие — kappa < {krel:.4f}")
