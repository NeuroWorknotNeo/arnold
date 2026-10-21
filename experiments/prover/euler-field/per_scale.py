"""[Эксперимент] Те же величины, что в construction.py, но по масштабам |b1| = 10^{-s}:
показывает, что max||D xi|| и min xi.gradQ/Q не ухудшаются при b1 -> 0.
Запуск: ~/venv/bin/python per_scale.py
"""
import mpmath as mp
from construction import Field, EXAMPLES, sample_points

for name in ['E3 (b2^2-b1^4)^2+b1^10', 'E6 три подоврага', 'E5 G1*G2, k=1.99 (поворот)', 'C  A*B (b1=y, b2=x)']:
    Q, rad = EXAMPLES[name]
    F = Field(Q, 4)
    print(name, " N=4")
    for s in [1.5, 2.5, 3.5, 4.5, 5.5]:
        pts = [p for p in sample_points(F, mp.mpf(rad), [s]) if abs(abs(p[0]) - mp.mpf(10)**(-s)) < mp.mpf(10)**(-s-5)]
        rs, ds = [], []
        for (x, y) in pts:
            r, nrm, _ = F.ratio(x, y)
            rs.append(r); ds.append(nrm)
        if not pts:
            continue
        print(f"   |b1|=1e-{s}: точек {len(pts)}, min ratio = {mp.nstr(min(rs), 6)}, max||Dxi|| = {mp.nstr(max(ds), 6)}", flush=True)
