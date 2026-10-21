# Пример S1, дуга x = y: G(phi) = sin^4(phi) (3 sqrt2 sin(phi) + 4 cos(phi)) / 8.
# Интервальная арифметика mpmath.iv (направленные округления): знаки G' на концах отрезка
# I = [4.5464, 4.5466] и нижняя граница G'' + 5G, верхняя граница G на всём I (интервальное
# расширение по всему отрезку). Плюс грубая ручная оценка: l1-норма коэффициентов Фурье G не больше
# (3 sqrt2 + 4)/8 < 1.04, степень 5, поэтому |(G''+5G)'| <= (125 + 25) * 1.04 < 156 (для контроля).
from mpmath import iv, mp
iv.dps = 40; mp.dps = 40
def G(p):  return iv.sin(p)**4*(3*iv.sqrt(2)*iv.sin(p) + 4*iv.cos(p))/8
def G1(p):  # производная, выписанная вручную: d/dp [s^4 (A s + B c)]/8 = [4 s^3 c (A s + B c) + s^4 (A c - B s)]/8
    s, c, A, B = iv.sin(p), iv.cos(p), 3*iv.sqrt(2), iv.mpf(4)
    return (4*s**3*c*(A*s + B*c) + s**4*(A*c - B*s))/8
def G2(p):  # вторая производная через численно устойчивую формулу: d/dp G1
    s, c, A, B = iv.sin(p), iv.cos(p), 3*iv.sqrt(2), iv.mpf(4)
    # G1*8 = 4 s^3 c (A s + B c) + s^4 (A c - B s) = 4A s^4 c + 4B s^3 c^2 + A s^4 c - B s^5
    #      = 5A s^4 c + 4B s^3 c^2 - B s^5
    # d/dp: 5A(4 s^3 c^2 - s^5) + 4B(3 s^2 c^3 - 2 s^4 c) - 5B s^4 c
    return (5*A*(4*s**3*c**2 - s**5) + 4*B*(3*s**2*c**3 - 2*s**4*c) - 5*B*s**4*c)/8
a, b = iv.mpf('4.5464'), iv.mpf('4.5466')
I = iv.mpf(['4.5464', '4.5466'])
print("G'(4.5464) in", G1(a))
print("G'(4.5466) in", G1(b))
print("G''+5G on I in", G2(I) + 5*G(I))
print("G on I in", G(I))
# контроль формул производных по mpmath.diff в точке
import mpmath
f = lambda p: mpmath.sin(p)**4*(3*mpmath.sqrt(2)*mpmath.sin(p) + 4*mpmath.cos(p))/8
p0 = mpmath.mpf('4.5465069')
print('контроль G1:', mpmath.nstr(mpmath.diff(f, p0) - (G1(iv.mpf(p0)).a), 5),
      ' G2:', mpmath.nstr(mpmath.diff(f, p0, 2) - (G2(iv.mpf(p0)).a), 5))
