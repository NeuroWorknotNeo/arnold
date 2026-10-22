# [Эксперимент] Рецензент R48: независимая численная проверка строгого выхода (A5) теоремы A [results/007]
# для конструкции предложения O2 (notes/prover/2026-10-21-fold.md, §5).
#   U = z^4 - 2 z^2 y rho^2 - x^2 rho^4 + x^7 + y^7,  rho = s = sqrt(x^2+y^2),  A(rho) = rho^6 (a0 = 1, beta = 6).
#   Pi(s,th,eps) = (s cos th, s sin th, s^{3/2} eps),  Y = Pi_s - (X^th/s) Pi_th - (X^eps/s) Pi_eps,
#   X = mu' X_0,  X_0^th = chi(th) tan(th)/2,  X_0^eps = (eps^2 - (1-chi) sin th)/(4 eps)  (= eps/4 при chi = 1).
# Множество выхода: q = Pi(s,th,eps) с |f| <= 2 sqrt(delta), f^2 + s g <= delta (q в замыкании D), E = 0, p < 0,
#   V = delta rho^6; v_perp ⟂ Y перебирается по окружности радиуса sqrt(2 K_perp), K_perp = delta rho^6 - W.
# Xi = d/dt (V - delta rho^6) вдоль (q', v') = (v, -grad U) -- разностная производная 4-го порядка, mpmath, 110 знаков.
# Печатается min (rho/lambda) Xi / (delta rho^6) по выборке (нужно > 0) и где он достигается.
# Запуск: ~/venv/bin/python exit_check.py
import sympy as sp
import mpmath as mp

mp.mp.dps = 110
X_, Y_, Z_ = sp.symbols('x y z', real=True)
r2 = X_**2 + Y_**2
Usym = Z_**4 - 2*Z_**2*Y_*r2 - X_**2*r2**2 + X_**7 + Y_**7
Uf = sp.lambdify((X_, Y_, Z_), Usym, 'mpmath')
gUf = [sp.lambdify((X_, Y_, Z_), sp.diff(Usym, v), 'mpmath') for v in (X_, Y_, Z_)]
CM = 45*mp.sqrt(3)/4 + 4


def step(t):
    if t <= 0:
        return mp.mpf(0)
    if t >= 1:
        return mp.mpf(1)
    a, b = mp.exp(-1/t), mp.exp(-1/(1-t))
    return a/(a+b)


def chi(th):
    d = min(abs(th), abs(th - mp.pi))
    return 1 - step((d - mp.pi/8)/(mp.pi/8))


def X0(th, e):
    c = chi(th)
    Xt = c*mp.tan(th)/2 if c != 0 else mp.mpf(0)
    if c == 1:
        Xe = e/4
    else:
        Xe = (e**2 - (1-c)*mp.sin(th))/(4*e)
    return Xt, Xe


def coords(q):
    s = mp.sqrt(q[0]**2 + q[1]**2)
    th = mp.atan2(q[1], q[0])
    if th < -mp.pi/4:
        th += 2*mp.pi
    return s, th, q[2]/s**mp.mpf(1.5)


def Yv(q, mup):
    s, th, e = coords(q)
    Xt, Xe = X0(th, e)
    Xt, Xe = mup*Xt, mup*Xe
    om = [mp.cos(th), mp.sin(th), 0]
    el = [-mp.sin(th), mp.cos(th), 0]
    nz = mp.sqrt(s)*(mp.mpf(3)/2*e - Xe)
    return [om[0] - Xt*el[0], om[1] - Xt*el[1], nz]


def dot(a, b):
    return sum(a[i]*b[i] for i in range(3))


def V(q, v, mup):
    Y = Yv(q, mup)
    h = dot(Y, Y)
    p = dot(v, Y)
    s = mp.sqrt(q[0]**2 + q[1]**2)
    return dot(v, v)/2 - p**2/(2*h) + Uf(*q) + s**6


def ratio(s, th, e, phi, mup, delta):
    q = [s*mp.cos(th), s*mp.sin(th), s**mp.mpf(1.5)*e]
    U = Uf(*q)
    W = U + s**6
    K = delta*s**6 - W
    if K < 0:
        assert -K < mp.mpf(10)**-70*s**6, K/s**6
        K = mp.mpf(0)
    Y = Yv(q, mup)
    h = dot(Y, Y)
    # ортонормированный базис Y^perp
    a = [0, 0, 1] if abs(Y[2]) < mp.mpf('0.5') else [1, 0, 0]
    e1 = [a[i] - dot(a, Y)/h*Y[i] for i in range(3)]
    n1 = mp.sqrt(dot(e1, e1)); e1 = [c/n1 for c in e1]
    e2 = [Y[1]*e1[2]-Y[2]*e1[1], Y[2]*e1[0]-Y[0]*e1[2], Y[0]*e1[1]-Y[1]*e1[0]]
    n2 = mp.sqrt(dot(e2, e2)); e2 = [c/n2 for c in e2]
    vp = [mp.sqrt(2*K)*(mp.cos(phi)*e1[i] + mp.sin(phi)*e2[i]) for i in range(3)]
    pp = -mp.sqrt(h*(-2*U - 2*K))
    v = [pp/h*Y[i] + vp[i] for i in range(3)]
    g = [gf(*q) for gf in gUf]
    # проверки: E = 0 и V = delta rho^6
    E = dot(v, v)/2 + U
    Vv = V(q, v, mup)
    assert abs(E) < mp.mpf(10)**-80*s**6 and abs(Vv - delta*s**6) < mp.mpf(10)**-80*s**6
    lam = -pp/h
    hh = mp.mpf(10)**-25*s/mp.sqrt(dot(v, v))

    def Phi(t):
        qt = [q[i] + t*v[i] for i in range(3)]
        vt = [v[i] - t*g[i] for i in range(3)]
        st = mp.sqrt(qt[0]**2 + qt[1]**2)
        return V(qt, vt, mup) - delta*st**6
    Xi = (-Phi(2*hh) + 8*Phi(hh) - 8*Phi(-hh) + Phi(-2*hh))/(12*hh)
    return s/lam*Xi/(delta*s**6)


def scan(s, mup, delta, nth=36, nf=7, nphi=8):
    worst = (mp.inf, None)
    ths = [mp.mpf(-0.24) + k*(mp.pi + mp.mpf(0.48))/(nth-1) for k in range(nth)]
    # сгущение у складок и в зоне перехода chi
    ths += [mp.mpf(t) for t in ('0', '1e-3', '-1e-3', '0.01', '-0.01', '0.05', '0.4', '0.5', '0.6', '0.7', '0.78')]
    ths += [mp.pi - t for t in ths[-11:]]
    for th in ths:
        gth = mp.cos(th)**7 + mp.sin(th)**7
        fmax2 = min(4*delta, delta - s*gth)       # f^2 <= ...
        if fmax2 < 0:
            continue
        fm = mp.sqrt(fmax2)
        for j in range(nf):
            fv = -fm + 2*fm*j/(nf-1)
            e2 = mp.sin(th) + fv
            if e2 < 0:
                continue
            for sg in (1, -1):
                ep = sg*mp.sqrt(e2)
                if ep == 0 and chi(th) < 1:
                    continue
                for k in range(nphi):
                    phi = 2*mp.pi*k/nphi
                    r = ratio(s, th, ep, phi, mup, delta)
                    if r < worst[0]:
                        worst = (r, (float(th), float(fv), float(ep), float(phi)))
                if ep == 0:
                    break
    return worst


if __name__ == '__main__':
    for delta in (mp.mpf('0.01'), mp.mpf('0.002')):
        mth = 12*delta/CM**2
        for s in (mp.mpf('1e-6'), mp.mpf('1e-10'), mp.mpf('1e-16')):
            for mup in (mth, mp.mpf('0.002'), mp.mpf('0.02'), mp.mpf('0.1')):
                w = scan(s, mup, delta)
                print('delta=%s s=%s mu\'=%s: min (rho/lam)Xi/(delta rho^6) = %s at (th,f,eps,phi)=%s'
                      % (mp.nstr(delta, 3), mp.nstr(s, 2), mp.nstr(mup, 4), mp.nstr(w[0], 6), w[1]), flush=True)
