"""[Эксперимент, дополнение] Прицельная выборка для thmB_example.py около нулей g(θ)=cosθ (θ≈±π/2),
где рог {U<0} тоньше всего и где в thmC_* поле ломалось. θ = ±π/2 + ε·10^{-u}, u∈[0.5,8] равномерно;
σ' = ±s^{3/2}·sqrt(|cosθ|/32 + 1e-3)·w, w∈(0,1.5) логарифмически. Как в оригинале: mpmath 60 знаков.
seed 5. Выводит min λ(sym DA) и диапазон A(U)/U."""
import random
src = open('thmB_example.py').read().split('random.seed(0)')[0]
exec(src)
random.seed(5)
for r in (mp.mpf('1e-3'), mp.mpf('1e-4'), mp.mpf('1e-6')):
    worst = mp.inf; rat = []; n = 0; tries = 0; wp = None
    while n < 60 and tries < 20000:
        tries += 1
        th = mp.pi/2*random.choice([-1, 1]) + random.choice([-1, 1])*mp.mpf(10)**(-random.uniform(0.5, 8))
        s = r*random.uniform(0.5, 1.5)
        w = mp.mpf(10)**(-random.uniform(0, 4))*random.choice([-1, 1])
        spn = w*mp.sqrt(abs(mp.cos(th))/32 + mp.mpf('1e-3'))*s**mp.mpf(1.5)
        p = cart(s, th, spn)
        if U_cart(*p) >= 0: continue
        n += 1
        lam, ratio = check(p)
        if lam < worst: worst, wp = lam, (th, spn/s**mp.mpf(1.5))
        rat.append(ratio)
    print(f"r={mp.nstr(r,3)}: {n} points (tries {tries}), min λ(sym DA) = {mp.nstr(worst,6)} at θ-π/2*sgn={mp.nstr(wp[0]%(mp.pi),6) if wp else None}, A(U)/U ∈ [{mp.nstr(min(rat),8) if rat else None}, {mp.nstr(max(rat),8) if rat else None}]", flush=True)
