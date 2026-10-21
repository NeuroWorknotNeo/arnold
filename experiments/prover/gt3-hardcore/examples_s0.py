# [Эксперимент] Примеры с s = 0 (§7.6–7.7 записки notes/prover/2026-10-21-gt3-hardcore.md).
import sympy as sp
import mpmath as mp
import random
from reduced import fiber_series, x, y, z, s

mp.mp.dps = 40
w = [1/sp.sqrt(3), 1/sp.sqrt(3), -1/sp.sqrt(3)]          # omega* = (1,1,-1)/sqrt3
e1 = [1/sp.sqrt(2), -1/sp.sqrt(2), sp.Integer(0)]
e2 = [1/sp.sqrt(6), 1/sp.sqrt(6), 2/sp.sqrt(6)]
assert sp.simplify(sum(a*b for a, b in zip(w, e2))) == 0

def run(name, U, m, order):
    print('=' * 70)
    print(name, ': U =', U)
    Um = sum(t for t in sp.Add.make_args(sp.expand(U)) if sp.Poly(t, x, y, z).total_degree() == m)
    print('  U_m =', sp.factor(Um), ';  U_m(omega*) =', sp.simplify(Um.subs({x: w[0], y: w[1], z: w[2]})))
    H = sp.Matrix(2, 2, lambda a, b: sp.simplify(sum(sp.diff(Um, p, q)*[e1, e2][a][i]*[e1, e2][b][jj]
                   for i, p in enumerate((x, y, z)) for jj, q in enumerate((x, y, z))).subs({x: w[0], y: w[1], z: w[2]})))
    print('  H = D^2 U_m(omega*)|_N =', H.tolist(), ', собств. числа', [sp.nsimplify(v) for v in H.eigenvals()])
    ys, R = fiber_series(U, m, w, [e1, e2], order)
    print('  y*(s) =', [sp.nsimplify(t) for t in ys])
    for i in range(1, order + 1):
        print('  g_%d(omega*) =' % (m + i), sp.nsimplify(R.coeff(s, i)), '=', float(R.coeff(s, i)))
    return ys, R

U6 = (x**2 - z**2)**2 + (y**2 - z**2)**2 + z**5
run('E6 (s=0, j=5)', U6, 4, 2)
U7 = (x**2 - z**2 + z**3)**2 + (y**2 - z**2)**2 + z**7
ys, R = run('E7 (s=0, искривлённое дно, j=7)', U7, 4, 4)

# Радиальное условие Четаева: ищем точки с U<0 и R=<grad U, q> > 0 вблизи луча omega*
Uf = sp.lambdify((x, y, z), U7, 'mpmath')
gr = [sp.lambdify((x, y, z), sp.diff(U7, v), 'mpmath') for v in (x, y, z)]
random.seed(1)
for rad in ['1e-2', '1e-3', '1e-4']:
    r = mp.mpf(rad)
    ys0 = [mp.mpf(float(sp.N(t.subs(s, r)))) for t in ys]   # дно y*(r)
    cnt = 0; tot = 0; Rmax = None
    for _ in range(4000):
        a = (random.random()*2 - 1)*mp.mpf('0.1')*r**mp.mpf(2.5)   # нормальные отклонения ~ r^{c}, c = 5/2
        b = (random.random()*2 - 1)*mp.mpf('0.1')*r**mp.mpf(2.5)
        q = [r*(float(w[i]) + ys0[0]*float(e1[i]) + ys0[1]*float(e2[i])) + a*float(e1[i]) + b*float(e2[i]) for i in range(3)]
        Uv = Uf(*q)
        if Uv < 0:
            tot += 1
            Rv = sum(gr[i](*q)*q[i] for i in range(3))
            if Rv > 0:
                cnt += 1
                if Rmax is None or Rv/abs(Uv) > Rmax:
                    Rmax = Rv/abs(Uv)
    print('  |q|~%s: точек с U<0: %d, из них с R>0: %d, max R/|U| = %s' % (rad, tot, cnt, mp.nstr(Rmax, 5) if Rmax else None))

# Изолированность U7: dU/dx = 4x P1, dU/dy = 4y P2 (P1 = x^2-z^2+z^3, P2 = y^2-z^2);
# в каждом из четырёх случаев dU/dz сводится к многочлену от z, у которого около 0 только корень z=0.
P1 = x**2 - z**2 + z**3; P2 = y**2 - z**2
assert sp.expand(sp.diff(U7, x) - 4*x*P1) == 0 and sp.expand(sp.diff(U7, y) - 4*y*P2) == 0
Uz = sp.diff(U7, z)
cases = {'P1=P2=0': {x**2: z**2 - z**3, y**2: z**2}, 'P1=0,y=0': {x**2: z**2 - z**3, y: 0},
         'x=0,P2=0': {x: 0, y**2: z**2}, 'x=0,y=0': {x: 0, y: 0}}
for nm, sb in cases.items():
    ex = sp.expand(Uz)
    for k, v in sb.items():
        ex = sp.expand(ex.subs(k, v))
    ex = sp.factor(ex)
    pz = sp.Poly(ex, z)
    a = min(mon[0] for mon in pz.monoms())          # dU/dz = z^a * rest(z), rest(0) != 0
    rest = sp.Poly(sp.cancel(ex / z**a), z)
    rts = [r for r in rest.nroots(n=30, maxsteps=200) if abs(r) < 0.5]
    print('  случай', nm, ': dU/dz =', ex, '= z^%d * rest, rest(0) =' % a, rest.eval(0),
          '; корни rest с |z|<0.5:', rts)
