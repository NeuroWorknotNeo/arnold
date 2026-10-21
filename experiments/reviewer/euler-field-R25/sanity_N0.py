"""R25 sanity check of the sampler: with N=0 (equal weights, no Voronoi cells) the field must FAIL
(xi.logQ < 0 somewhere) on examples with several thin pairs. [Эксперимент]"""
import mpmath as mp
import construction_check as cc
b1, b2 = cc.B1, cc.B2
ex = {'T1': [(b2 - b1**2 - i*b1**3)**2 + b1**10 for i in range(3)],
      'T4': [(b2 - b1**2 - i*b1**4)**2 + b1**12 for i in range(-1, 3)]}
for name, Q in ex.items():
    for N in [0, 1]:
        cc.run(name, Q, N, [10**-2, 10**-3, -10**-3], fdcheck=False)
