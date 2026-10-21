"""R25: T6 for b1<0 with the N required by the theorem there (E=11.5 for b1<0, d=12 -> N=253). [Эксперимент]"""
import construction_check as cc
b1, b2 = cc.B1, cc.B2
Q = [((b2 - b1**2)**2 - b1**5)**2 + b1**14, (b2 - b1**2 - b1**3)**2 + b1**8,
     ((b2 - b1**2 + b1**3)**2 + b1**7)**2 + b1**30, (b2 + b1)**2 + b1**2]
cc.run('T6 left half-plane', Q, 253, [-10**(-e/2) for e in range(3, 13)], fdcheck=True)
