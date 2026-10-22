"""
v_weights.py -- класс (в): можно ли реализовать профиль Q = ((b1-b2^2)^2+b2^8)((b1-b2^2-b2^3)^2+b2^8) из results/009 §6.2 как предельный
профиль F_0 = -a + Q(b) настоящего оврага U(x,y1,y2) с изолированным нулём ведущей формы u_m в луче e_x?  [Эксперимент: точная арифметика]

Реализация: U = -x^beta + sum_alpha q_alpha x^{beta - c.alpha} y^alpha, веса c = (c1,c2), beta = max_alpha c.alpha (чтобы все показатели >= 0).
(Тогда U(x, x^c b) = x^beta (-1 + Q(b)) ТОЧНО.)  Целочисленность показателей: c1, c2 целые (в носителе Q есть мономы с b2^1-сдвигом).
Для каждой пары весов считаем m = min степень монома, u_m (младшая форма) и проверяем: u_m(1,y1,y2) имеет изолированный нуль в 0?
(Необходимо: u_m содержит чистые степени y1^j и y2^k.)  Дополнительно: «подкладка» (padding) чистыми степенями хвоста y1^J, y2^K с L_c > beta,
степень которых может быть меньше m: даёт изолированность при любых c1<c2, но требует beta > 16 c2 и большой степени.
usage: python v_weights.py
"""
import sympy as sp
import itertools

b1, b2, x, y1, y2 = sp.symbols('b1 b2 x y1 y2')
A = (b1 - b2**2)**2 + b2**8
B = (b1 - b2**2 - b2**3)**2 + b2**8
Q = sp.expand(A * B)
supp = [m for m, c in sp.Poly(Q, b1, b2).terms()]
coef = {m: c for m, c in sp.Poly(Q, b1, b2).terms()}
print('число мономов Q:', len(supp), ' Newton: max b1-степень', max(m[0] for m in supp), ' max b2-степень', max(m[1] for m in supp))


def analyse(c1, c2, K=1):
    beta = max(c1 * m[0] + c2 * m[1] for m in supp)
    terms = {}
    for m in supp:
        e = beta - c1 * m[0] - c2 * m[1]
        terms[(e, m[0], m[1])] = coef[m] * K
    terms[(beta, 0, 0)] = terms.get((beta, 0, 0), 0) - 1
    deg = {k: sum(k) for k in terms}
    mmin = min(deg.values())
    low = {k: v for k, v in terms.items() if deg[k] == mmin}
    pure1 = any(k[2] == 0 and k[1] > 0 for k in low)       # y1^j x^{m-j}
    pure2 = any(k[1] == 0 and k[2] > 0 for k in low)
    return beta, mmin, low, pure1, pure2, terms


print('\nвеса (c1,c2): beta, m, число мономов в u_m, есть чистая y1-степень, есть чистая y2-степень  [isolated нуль u_m на луче e_x возможен только если обе]')
for c1 in range(2, 8):
    for c2 in range(2, 8):
        beta, m, low, p1, p2, _ = analyse(c1, c2)
        orient = 'b1 шире (c1<c2)' if c1 < c2 else ('b1 уже (c1>c2)' if c1 > c2 else 'изотропно')
        print(f'  c=({c1},{c2}) {orient:18s}: beta={beta:3d}, m={m:3d}, |supp u_m|={len(low):2d}, pure y1: {p1}, pure y2: {p2}', '  <-- u_m изолирован' if (p1 and p2) else '')

print('\nподкладка: добавить y1^J x^{M-J} и y2^K x^{M-K} (M = степень), L_c = M + (c-1) J > beta; требуется M <= m (иначе не будут младшими)')
for (c1, c2) in [(2, 3), (2, 4), (3, 4), (2, 5)]:
    beta, m, low, p1, p2, _ = analyse(c1, c2)
    # чистая y1-степень степени M=m: L = m + (c1-1) m = m c1 ; нужно m c1 > beta
    ok = m * c1 > beta and m * c2 > beta
    print(f'  c=({c1},{c2}): beta={beta}, m={m}, y1^m: L={m*c1} > beta? {m*c1 > beta}; y2^m: L={m*c2} > beta? {m*c2 > beta} -> {"подкладка на степени m возможна" if ok else "нужно увеличить beta (степень растёт)"}')
    # минимальное beta' >= beta с m' = beta' - 16 (c2-1)... для c1<c2: m = beta - 16 (c2-1): условие m c1 > beta
    b = beta
    while True:
        mm = b - 16 * (c2 - 1)
        if mm * c1 > b:
            break
        b += 1
    print(f'      минимальное beta с подкладкой: beta={b}, m={b-16*(c2-1)}, степень U = max(beta, ...) >= {b}')
