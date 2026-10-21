# [Эксперимент] Радиальное условие Четаева для U_(8) = (Q0+z^3)^2 + x z^6 + x y z^5 + z^7/2 на нижней полости конуса
# (вторая компонента {U<0}): доля точек {U<0} около дна с <grad U, q> > 0.
import random
import sympy as sp
import mpmath as mp
from reduced import fiber_series, x, y, z, s
mp.mp.dps = 40
ph = sp.symbols('phi', real=True)
Q0 = x**2 + y**2 - z**2
U = (Q0 + z**3)**2 + x*z**6 + x*y*z**5 + z**7/2
om = [sp.cos(ph)/sp.sqrt(2), sp.sin(ph)/sp.sqrt(2), -1/sp.sqrt(2)]
nv = [sp.cos(ph)/sp.sqrt(2), sp.sin(ph)/sp.sqrt(2), 1/sp.sqrt(2)]   # нормаль к конусу
ys, R = fiber_series(U, 4, om, [nv], 4)
for i in range(1, 5):
    print('g_%d =' % (4 + i), sp.simplify(R.coeff(s, i)))
print('y* =', ys[0])
Uf = sp.lambdify((x, y, z), U, 'mpmath')
gr = [sp.lambdify((x, y, z), sp.diff(U, v), 'mpmath') for v in (x, y, z)]
es = sp.lambdify((s, ph), sp.expand(s*ys[0]), 'mpmath')
random.seed(5)
for sv in [mp.mpf('1e-2'), mp.mpf('1e-3')]:
    tot = bad = 0
    for _ in range(3000):
        phv = mp.pi + (2*random.random() - 1)*0.6
        e = (2*random.random() - 1)*0.3
        eta = es(sv, phv) + sv**mp.mpf(2.5)*e
        q = [(sv + eta)*mp.cos(phv)/mp.sqrt(2), (sv + eta)*mp.sin(phv)/mp.sqrt(2), (-sv + eta)/mp.sqrt(2)]
        if Uf(*q) < 0:
            tot += 1
            if sum(gr[i](*q)*q[i] for i in range(3)) > 0:
                bad += 1
    print('нижняя полость, s=%s: U<0 в %d точках, R>0 в %d' % (mp.nstr(sv, 2), tot, bad))
