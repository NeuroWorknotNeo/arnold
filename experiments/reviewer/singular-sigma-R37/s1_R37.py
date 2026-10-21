"""R37: пример S1 (§4.5): G = g5 на дуге x=y, минимум, G''+5G, h_n [Эксперимент]."""
import mpmath as mp
mp.mp.dps = 40
G = lambda f: mp.sin(f)**4*(3*mp.sqrt(2)*mp.sin(f) + 4*mp.cos(f))/8
# прямая проверка: u5 на дуге
u5 = lambda f: (lambda x, y, z: x**5 + 2*y**5 + z*(x**4 + y**4))(mp.sin(f)/mp.sqrt(2), mp.sin(f)/mp.sqrt(2), mp.cos(f))
print('max|u5-G| on grid:', max(abs(u5(k/100) - G(k/100)) for k in range(629)))
# глобальный минимум G на [0, 2pi]
fs = [2*mp.pi*k/2000 for k in range(2000)]
f0 = min(fs, key=G)
fstar = mp.findroot(lambda f: mp.diff(G, f), f0)
print('phi* =', mp.nstr(fstar, 12), ' G =', mp.nstr(G(fstar), 12), " G'' + 5G =", mp.nstr(mp.diff(G, fstar, 2) + 5*G(fstar), 12),
      ' h_n = 8 sin^2 =', mp.nstr(8*mp.sin(fstar)**2, 8))
