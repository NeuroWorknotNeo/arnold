"""R46: независимая символьная проверка леммы W (записка notes/prover/2026-10-21-master.md, §5.2).

[Эксперимент] Не доказательство. Запуск: ~/venv/bin/python check_W.py

Размерность поперечного пространства n-1 = 3: индекс 0 -- конический (a_0 = 0),
индексы 1, 2 -- узкие с символьными весами a1, a2 > 0 (в том числе проверяется случай a1 = a2).
P(s,u) и xi(s,b) -- произвольные функции (sympy Function), т.е. цепное правило делает sympy.

Определения, от которых идём (только определения, без формул леммы):
  Theta(s,b) = P(s, s^A b);
  поток Y в (s,b): s db/ds = -xi;
  угловая скорость v = s d/ds Theta(s,b(s)) вдоль потока = s d_s Theta|_b - D_b Theta . xi;
  D_vartheta v = D_b(v o Theta) (D_b Theta)^{-1};
  psi = v + s dv/ds вдоль потока = v + s d_s v|_b - D_b v . xi;
  s d_s v|_vartheta = s d_s(v o Theta)|_b - D_vartheta v . s d_s Theta|_b (цепное правило).
"""
import sympy as sp

s = sp.symbols('s', positive=True)
a1, a2 = sp.symbols('a1 a2', positive=True)
b = sp.symbols('b0 b1 b2', real=True)
w = sp.symbols('w0 w1 w2', real=True)       # переменные u для частных производных P
avec = [sp.Integer(0), a1, a2]
A = sp.diag(*avec)
sA = sp.diag(*[s**ai for ai in avec])
sAinv = sp.diag(*[s**(-ai) for ai in avec])

uexpr = [s**avec[i]*b[i] for i in range(3)]
# Чтобы sympy не плодил несравнимые Subs, берём P и xi в виде многочленов степени 2 по u (по b)
# с коэффициентами -- ПРОИЗВОЛЬНЫМИ функциями s. Формулы леммы W поточечны и зависят лишь от
# 2-струи P по (s,u) (вместе с s-производными) и 1-струи xi; многочлены степени 2 с произвольными
# функциями s в коэффициентах реализуют любую такую струю в любой точке, так что проверка общая.
from itertools import combinations_with_replacement
def monos(vars_, deg):
    out = [sp.Integer(1)]
    for d in range(1, deg+1):
        for c in combinations_with_replacement(vars_, d):
            out.append(sp.Mul(*c))
    return out
mono_w = monos(w, 2)
mono_b = monos(b, 2)
P_w = sp.Matrix([sum(sp.Function('p%d_%d' % (i, k))(s)*m for k, m in enumerate(mono_w)) for i in range(3)])
xi = sp.Matrix([sum(sp.Function('x%d_%d' % (i, k))(s)*m for k, m in enumerate(mono_b)) for i in range(3)])
sub_u = dict(zip(w, uexpr))
def at_u(e):
    return e.subs(sub_u, simultaneous=True)
Theta = at_u(P_w)
bvec = sp.Matrix(b)

def D_b(vec):
    return vec.jacobian(bvec)

def sds(e):
    return s*sp.diff(e, s)

# --- определения ---
J = D_b(Theta)                       # D_b Theta
v = sds(Theta) - J*xi                # угловая скорость (вдоль потока)
Dbv = D_b(v)

# --- величины формул леммы ---
Pu = at_u(P_w.jacobian(sp.Matrix(w)))                    # P_u в точке u
sdsP = at_u(sds(P_w))                                    # s d_s P при постоянном u
sds_sdsP = at_u(sds(sds(P_w)))                           # s d_s(s d_s P)
sdsPu = at_u(sds(P_w.jacobian(sp.Matrix(w))))            # s d_s P_u при постоянном u
def D2P(x, y):
    # D_u^2 P(x,y) в точке u: вектор
    out = []
    for i in range(3):
        H = sp.hessian(P_w[i], w)
        out.append(at_u((sp.Matrix(x).T*H*sp.Matrix(y))[0, 0]))
    return sp.Matrix(out)
def D2P_mat(x):
    # матрица eta -> D_u^2 P(x, eta)
    cols = []
    for j in range(3):
        e = [0, 0, 0]; e[j] = 1
        cols.append(D2P(x, e))
    return sp.Matrix.hstack(*cols)

ubar = sA*(A*bvec - xi)
sAAb = sA*A*bvec
dsPu = sdsPu + D2P_mat(sAAb)                              # d_s P_u
I3 = sp.eye(3)

def is_zero(M, name):
    M = sp.Matrix(M)
    bad = []
    for idx, e in enumerate(M):
        r = sp.simplify(sp.expand(e.doit()))
        if r != 0:
            bad.append((idx, r))
    print(name, 'OK' if not bad else 'FAIL', '' if not bad else bad[:2])
    return not bad

ok = True
# (0) J = P_u s^A (цепное правило)
ok &= is_zero(J - Pu*sA, 'J = P_u s^A')
# (W0)
ok &= is_zero(v - (sdsP + Pu*ubar), '(W0)')
# (W1): I + D_th v = P_u N P_u^{-1}  <=>  (J + D_b v) = P_u N P_u^{-1} J = P_u N s^A
#        P_u N = P_u (I+A) + [d_s P_u - D^2P(s^A xi, .)] - P_u s^A D_b xi s^{-A}
PuN = Pu*(I3 + A) + (dsPu - D2P_mat(sA*xi)) - Pu*sA*D_b(xi)*sAinv
ok &= is_zero((J + Dbv) - PuN*sA, '(W1)')
# (W2)
psi_def = v + sds(v) - Dbv*xi
bracket = (I3 + A)*ubar - sA*(A*xi + sds(xi) - D_b(xi)*xi)
psi_W2 = sdsP + sds_sdsP + 2*sdsPu*ubar + D2P(ubar, ubar) + Pu*bracket
ok &= is_zero(psi_def - psi_W2, '(W2)')
# (W3) и согласование с определением psi леммы G: psi = v + D_th v . v + s d_s v|_th.
#   D_th v = D_b v J^{-1}. Проверяем без обращения: умножаем на J справа там, где можно.
#   s d_s v|_th = s d_s(v o Theta)|_b - D_th v (s d_s P + P_u s^A A b)   (W3)
#   psi_G = v + D_th v (v - (s d_s P + P_u s^A A b)) + s d_s v|_b
#   Так как v - s d_s Theta|_b = -J xi, D_th v (-J xi) = -D_b v xi.  Проверим, что
#   s d_s Theta|_b = s d_s P + P_u s^A A b  (это и есть множитель в (W3)):
ok &= is_zero(sds(Theta) - (sdsP + Pu*sAAb), '(W3) множитель')
# и формулу из шага 5 доказательства MT для s d_s(v o Theta)|_b:
sds_v_formula = sds_sdsP + sdsPu*sAAb + dsPu*ubar + Pu*(A*ubar - sA*sds(xi))
ok &= is_zero(sds(v) - sds_v_formula, 'шаг 5 MT: s d_s(v o Theta)|_b')
print('ALL OK' if ok else 'SOME FAIL')

# --- контроль чувствительности: заведомо испорченные формулы должны давать FAIL ---
print('--- контроль чувствительности (ожидается FAIL) ---')
is_zero(v - (sdsP + Pu*sA*(bvec - xi)), '(W0) с I вместо A')
PuN_bad = Pu*(I3) + (dsPu - D2P_mat(sA*xi)) - Pu*sA*D_b(xi)*sAinv
is_zero((J + Dbv) - PuN_bad*sA, '(W1) без A')
bracket_bad = ubar - sA*(A*xi + sds(xi) - D_b(xi)*xi)
psi_bad = sdsP + sds_sdsP + 2*sdsPu*ubar + D2P(ubar, ubar) + Pu*bracket_bad
is_zero(psi_def - psi_bad, '(W2) с I вместо I+A')
