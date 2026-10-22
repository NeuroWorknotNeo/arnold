# R51: независимая символьная проверка формул (X.2)-(X.7) и лишних членов предложения N
# (results/016-fold.md, Доказательство, §2.1, §2.3, п. 1, п. 4).
# Векторы — тройки коэффициентов в подвижном репере (omega, ell, n) с правилами (0.1):
#   omega' = ell, ell' = -omega + kg n, n' = -kg ell.
# [Эксперимент] — символьная проверка тождеств, не доказательство.
import sympy as sp

s, th, ep, c, N = sp.symbols('s theta varepsilon c N', positive=True)
kg = sp.Function('k_g')(th)
Xt = sp.Function('X_t')(th, ep)    # общий X^theta(theta, eps)
Xe = sp.Function('X_e')(th, ep)
wo, wl, wn = sp.symbols('w_omega w_ell w_n')


def Dth(v):
    a, b, cc = v
    return [sp.diff(a, th) - b, a + sp.diff(b, th) - kg*cc, sp.diff(cc, th) + kg*b]


def Dx(v, x):
    return [sp.diff(comp, x) for comp in v]


def dot(u, v):
    return sum(ui*vi for ui, vi in zip(u, v))


def lin(*pairs):
    out = [0, 0, 0]
    for coef, v in pairs:
        out = [o + coef*vi for o, vi in zip(out, v)]
    return out


Pi = [s, 0, s**c*ep]
Pis, Pith, Piep = Dx(Pi, s), Dth(Pi), Dx(Pi, ep)
eps_ = s**(c-1)*ep*kg            # \epsilon
nu = s**(c-1)*(c*ep - Xe)

# (X.2)
chk = [sp.simplify(a-b) for a, b in zip(Pis, [1, 0, c*s**(c-1)*ep])]
chk += [sp.simplify(a-b) for a, b in zip(Pith, [0, s*(1-eps_), 0])]
chk += [sp.simplify(a-b) for a, b in zip(Piep, [0, 0, s**c])]
print('(X.2):', all(x == 0 for x in chk))

Y = lin((1, Pis), (-Xt/s, Pith), (-Xe/s, Piep))
Yclaim = [1, -Xt*(1-eps_), nu]
print('(X.3) Y:', all(sp.simplify(a-b) == 0 for a, b in zip(Y, Yclaim)))
h = dot(Y, Y)
print('(X.3) h:', sp.simplify(h - (1 + Xt**2*(1-eps_)**2 + nu**2)) == 0)

Ys, Yth, Yep = Dx(Y, s), Dth(Y), Dx(Y, ep)
sDYY = lin((s, Ys), (-Xt, Yth), (-Xe, Yep))

Xtp = sp.diff(Xt, th)
dth_eps = sp.diff(eps_, th)
dth_nu = sp.diff(nu, th)
C = lin((-Xt**2*(1-eps_), [1, 0, 0]), (-Xt*(1 - Xtp*(1-eps_)), [0, 1, 0]), (Xt**2*(1-eps_)*kg, [0, 0, 1]))
rest = lin(((c-1), [0, Xt*eps_, nu]),
           (-Xt*(Xt*dth_eps - nu*kg), [0, 1, 0]),
           (-Xt*dth_nu, [0, 0, 1]),
           (-s**(c-1)*Xe, [0, Xt*kg, (c - sp.diff(Xe, ep))]))
X4 = lin((1, C), (1, rest))
extra4 = [0, Xe*sp.diff(Xt, ep)*(1-eps_), 0]
diff4 = [sp.simplify(a - b - e) for a, b, e in zip(sDYY, X4, extra4)]
print('(X.4) + extra of Prop N:', all(d == 0 for d in diff4), diff4)

# (X.5)
w = [wo, wl, wn]
a_s = wo
a_th = wl/(s*(1-eps_))
a_ep = s**(-c)*(wn - c*s**(c-1)*ep*wo)
wback = lin((a_s, Pis), (a_th, Pith), (a_ep, Piep))
print('decomposition of w:', all(sp.simplify(a-b) == 0 for a, b in zip(wback, w)))
DwY = lin((a_s, Ys), (a_th, Yth), (a_ep, Yep))
lhs5 = sp.expand(s*dot(w, DwY))
X5 = ((1/(1-eps_) - Xtp)*wl**2 + (c - sp.diff(Xe, ep))*wn**2 + Xt*wo*wl
      + ((Xt*dth_eps - nu*kg)*wl**2 + dth_nu*wl*wn)/(1-eps_)
      + (c-1)*wo*(Xt*eps_*wl + nu*wn)
      - c*s**(c-1)*ep*wo*(Xt*kg*wl + (c - sp.diff(Xe, ep))*wn))
extra5 = -sp.diff(Xt, ep)*(1-eps_)*s**(1-c)*(wn - c*s**(c-1)*ep*wo)*wl
d5 = sp.simplify(lhs5 - X5 - extra5)
print('(X.5) + extra of Prop N:', d5 == 0, d5)

# (X.6)
print('(X.6):', sp.simplify(dot(w, Y) - (wo - Xt*(1-eps_)*wl + nu*wn)) == 0)

# triangular case: extras vanish identically when d/de X^theta = 0 -- by construction of extras above.

# (X.7): W(Pi) = s^beta (F(s^{1/N},th,ep) + a0)
beta, a0 = sp.symbols('beta a_0', positive=True)
F = sp.Function('F')
sig = s**(1/N)
g = s**beta*(F(sig, th, ep) + a0)
rhoYW = s*sp.diff(g, s) - Xt*sp.diff(g, th) - Xe*sp.diff(g, ep)
sg = sp.Symbol('sigma', positive=True)
Fs = F(sg, th, ep)
X7 = s**beta*(Xt*sp.diff(Fs, th) + Xe*sp.diff(Fs, ep) - sg/N*sp.diff(Fs, sg)).subs(sg, sig)
print('(X.7):', sp.simplify(beta*g - rhoYW - X7) == 0, sp.simplify(beta*g - rhoYW - X7))

# Prop N, п. 4: extra term at w = w_omega omega + ell/sqrt2 + varsigma n/sqrt2
vs = sp.Symbol('varsigma')
ex = extra5.subs({wl: 1/sp.sqrt(2), wn: vs/sp.sqrt(2)})
claim = (-sp.Rational(1, 2)*vs*sp.diff(Xt, ep)*(1-eps_)*s**(1-c)
         + c*ep/sp.sqrt(2)*sp.diff(Xt, ep)*(1-eps_)*wo)
print('Prop N, extra at w (vs*dX = kappa_0):', sp.simplify(ex - claim) == 0)
