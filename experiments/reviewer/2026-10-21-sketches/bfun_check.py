# [проверка кода] bfun из experiments/vlad-claude/fields/k4_perp.py (скопирована дословно)
import mpmath as mp
def bfun_u(u):
    u1, u2 = mp.mpf('0.05'), mp.mpf('0.3')
    x = (u - u1)/(u2 - u1)
    if x <= 0: return mp.mpf(0)
    if x >= 1: return mp.mpf(1)/3
    a = mp.exp(-1/x); b = mp.exp(-1/(1 - x))
    return b/(a + b)/3
for u in ('0.0', '0.05', '0.0500001', '0.06', '0.1', '0.175', '0.25', '0.29', '0.2999999', '0.3', '0.31'):
    print(u, mp.nstr(bfun_u(mp.mpf(u)), 6))
