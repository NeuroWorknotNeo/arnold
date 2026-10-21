# R41: пример O2 — где лежит минимум функции дна. [Эксперимент]
# Ũ(σ,θ,ε) = (ε²-sinθ)² - 1 + σ² h(θ), h = cos^7+sin^7 (N=2, σ² = s); F_fl = s^6 min_ε Ũ.
import sympy as sp, mpmath as mp
X,Y,Z,s,th,y,sig,eps = sp.symbols('x y z s theta y sigma epsilon', real=True)
rho2 = X**2+Y**2
U = Z**4-2*Z**2*Y*rho2-X**2*rho2**2+X**7+Y**7
phi = sp.expand(U.subs({X:s*sp.cos(th),Y:s*sp.sin(th),Z:s*y},simultaneous=True)/s**4)
Ut = sp.simplify(sp.expand(phi.subs({y:sig*eps, s:sig**2})/sig**4))
h = sp.cos(th)**7+sp.sin(th)**7
print("Ũ - [(eps^2-sin)^2 - 1 + sigma^2 h] =", sp.simplify(Ut-((eps**2-sp.sin(th))**2-1+sig**2*h)))
# минимум по ε и по θ численно при малом s
mp.mp.dps = 30
def floor(sv, t):
    # min_ε Ũ: на дуге (sin>=0) ε²=sin, значение -1+s h; вне — ε=0, значение -cos²+s h
    st = mp.sin(t); hv = mp.cos(t)**7+mp.sin(t)**7
    return (-1 if st >= 0 else -mp.cos(t)**2) + sv*hv
for sv in (mp.mpf('1e-2'), mp.mpf('1e-4')):
    best = min((floor(sv, mp.pi*k/20000*2), mp.pi*k/20000*2) for k in range(20000))
    print("s=%s: min_theta F_fl/s^6 = %s при theta/pi = %s" % (sv, mp.nstr(best[0], 12), mp.nstr(best[1]/mp.pi, 8)))
# прямой контроль: минимум φ(s,θ,y) по y численно в θ=π и рядом
def phimin(sv, t):
    f = sp.lambdify(y, phi.subs({s:sv, th:t}), 'mpmath')
    df = sp.lambdify(y, sp.diff(phi, y).subs({s:sv, th:t}), 'mpmath')
    cands = [mp.mpf(0)]
    for y0 in (-0.5*mp.sqrt(sv), 0.5*mp.sqrt(sv), -mp.sqrt(sv), mp.sqrt(sv)):
        try: cands.append(mp.findroot(df, y0))
        except Exception: pass
    return min(f(c) for c in cands)/sv**2
sv = mp.mpf('1e-4')
for t in (mp.pi-0.05, mp.pi-0.01, mp.pi, mp.pi+0.01, mp.pi+0.05):
    print("  theta/pi=%s: min_y phi / s^2 = %s" % (mp.nstr(t/mp.pi,6), mp.nstr(phimin(float(sv), float(t)), 12)))
