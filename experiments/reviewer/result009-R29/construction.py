"""R29: независимая численная реализация поля теоремы E (results/009, (2.1)-(2.4)). [Эксперимент]

Корни phi_j уравнения P(b1, .) = 0 берутся из явных формул (P задан произведением/явно),
производные phi_j', phi_j'' -- неявным дифференцированием P. Поле:
  chi_j = b1 psi_j' - psi_j,  w_j = p_j^{-N}/sum p_k^{-N},  c = sum w_j chi_j,  xi = (b1, b2 + c).
Печатаются min xi.grad log Q, max |grad c|, max |c|/|b1|^{1+1/m} по сеткам при |b1| -> 0.
"""
import sys
import mpmath as mp
import sympy as sp

mp.mp.dps = 160
B1, B2 = sp.symbols('b1 b2')


def mk(expr):
    return sp.lambdify((B1, B2), expr, 'mpmath')


class Example:
    def __init__(self, name, P, u, roots, m, Nw):
        self.name, self.m, self.Nw = name, m, Nw
        self.P = mk(P)
        self.P1, self.P2 = mk(sp.diff(P, B1)), mk(sp.diff(P, B2))
        self.P11, self.P12, self.P22 = mk(sp.diff(P, B1, 2)), mk(sp.diff(P, B1, B2)), mk(sp.diff(P, B2, 2))
        self.u = mk(u)
        self.lu1, self.lu2 = mk(sp.diff(u, B1)/u), mk(sp.diff(u, B2)/u)
        self.Q = mk(P*u)
        self.Q1, self.Q2 = mk(sp.diff(P*u, B1)), mk(sp.diff(P*u, B2))
        self.roots = roots
        self.d = int(sp.Poly(P, B2).degree())

    def rootdata(self, b1):
        R = []
        for phi in self.roots(mp.mpf(b1)):
            res = abs(self.P(b1, phi))
            p2 = self.P2(b1, phi)
            d1 = -self.P1(b1, phi)/p2
            d2 = -(self.P11(b1, phi) + 2*self.P12(b1, phi)*d1 + self.P22(b1, phi)*d1**2)/p2
            R.append((phi, d1, d2, res))
        assert len(R) == self.d
        return R

    def field(self, b1, b2, R=None, N=None):
        N = self.Nw if N is None else N
        b1 = mp.mpf(b1); b2 = mp.mpf(b2)
        R = R or self.rootdata(b1)
        psi = [mp.re(r[0]) for r in R]; eta = [mp.im(r[0]) for r in R]
        dpsi = [mp.re(r[1]) for r in R]; deta = [mp.im(r[1]) for r in R]
        ddpsi = [mp.re(r[2]) for r in R]
        chi = [b1*dpsi[j] - psi[j] for j in range(self.d)]
        dchi = [b1*ddpsi[j] for j in range(self.d)]
        p = [(b2 - psi[j])**2 + eta[j]**2 for j in range(self.d)]
        gp = [(-2*(b2 - psi[j])*dpsi[j] + 2*eta[j]*deta[j], 2*(b2 - psi[j])) for j in range(self.d)]
        pmin = min(p)
        r = [(pmin/pj)**N for pj in p]
        S = sum(r)
        w = [rj/S for rj in r]
        c = sum(w[j]*chi[j] for j in range(self.d))
        avg = [sum(w[k]*gp[k][i]/p[k] for k in range(self.d)) for i in range(2)]
        gw = [[N*w[j]*(-gp[j][i]/p[j] + avg[i]) for i in range(2)] for j in range(self.d)]
        gc = [sum(w[j]*dchi[j] for j in range(self.d)) + sum(chi[j]*gw[j][0] for j in range(self.d)),
              sum(chi[j]*gw[j][1] for j in range(self.d))]
        xi2 = b2 + c
        # xi log P = sum_k Re[(xi2 - b1 phi_k')/(b2 - phi_k)]
        xlP = sum(mp.re((xi2 - b1*R[k][1])/(b2 - R[k][0])) for k in range(self.d))
        xlu = b1*self.lu1(b1, b2) + xi2*self.lu2(b1, b2)
        return dict(c=c, gc=gc, xlQ=xlP + xlu, psi=psi, eta=eta, w=w)


def b2_grid(b1, R, extra=()):
    a = abs(b1)
    pts = set()
    for s in [-20, -8, -4, -2, -1.5, -1, -0.7, -0.4, -0.2, -0.1, -0.03, 0, 0.03, 0.1, 0.2, 0.4, 0.7, 1, 1.5, 2, 4, 8, 20]:
        pts.add(mp.mpf(s)*a)
    for s in [-0.3, -0.1, -0.03, 0.03, 0.1, 0.3]:
        pts.add(mp.mpf(s))
    psis = [mp.re(r[0]) for r in R]; etas = [abs(mp.im(r[0])) for r in R]
    for j in range(len(R)):
        for t in [-30, -5, -2, -1, -0.5, -0.2, 0, 0.2, 0.5, 1, 2, 5, 30]:
            pts.add(psis[j] + t*etas[j])
        # логарифмическая сетка от |eta_j|/100 до 10|b1| по обе стороны от psi_j
        lo = mp.log10(etas[j]) - 2; hi = mp.log10(a) + 1
        q = lo
        while q <= hi:
            pts.add(psis[j] + mp.mpf(10)**q); pts.add(psis[j] - mp.mpf(10)**q)
            q += mp.mpf(1)/6
        for k in range(len(R)):
            if k != j:
                for t in [0.25, 0.5, 0.75]:
                    pts.add(psis[j] + t*(psis[k] - psis[j]))
    return sorted(pts)


def run(ex, ks=range(1, 8), Ns=None):
    Ns = Ns or [ex.Nw]
    print("=== %s: d=%d, m=%d" % (ex.name, ex.d, ex.m))
    for N in Ns:
        print("  N = %d" % N)
        for sgn in (+1, -1):
            for kk in ks:
                b1 = sgn*mp.mpf(10)**(-kk)
                R = ex.rootdata(b1)
                maxres = max(r[3] for r in R)
                mn, mg, mc = mp.inf, 0, 0
                for b2 in b2_grid(b1, R):
                    F = ex.field(b1, b2, R, N)
                    mn = min(mn, F['xlQ'])
                    mg = max(mg, mp.sqrt(F['gc'][0]**2 + F['gc'][1]**2))
                    mc = max(mc, abs(F['c'])/abs(b1)**(1 + mp.mpf(1)/ex.m))
                print("    b1=%+.0e: min xi log Q = %8.4f  max|grad c| = %8.4f  max|c|/|b1|^(1+1/m) = %8.4f  (|P(root)|<=%.1e)"
                      % (float(b1), float(mn), float(mg), float(mc), float(maxres)))


def fd_check(ex, pts, N=None):
    """сверка grad c с конечными разностями; xi log Q с прямой формулой"""
    worst_g, worst_x = 0, 0
    for (b1, b2) in pts:
        b1 = mp.mpf(b1); b2 = mp.mpf(b2)
        F = ex.field(b1, b2, N=N)
        h = abs(b1)*mp.mpf(10)**(-40)
        c = lambda x, y: ex.field(x, y, N=N)['c']
        g1 = (c(b1 + h, b2) - c(b1 - h, b2))/(2*h)
        g2 = (c(b1, b2 + h) - c(b1, b2 - h))/(2*h)
        err = max(abs(g1 - F['gc'][0]), abs(g2 - F['gc'][1]))/(1 + abs(F['gc'][0]) + abs(F['gc'][1]))
        worst_g = max(worst_g, err)
        xlQ = (b1*ex.Q1(b1, b2) + (b2 + F['c'])*ex.Q2(b1, b2))/ex.Q(b1, b2)
        worst_x = max(worst_x, abs(xlQ - F['xlQ'])/(1 + abs(xlQ)))
    print("  проверка: отн. ошибка grad c (конечные разности) <= %.1e; xi log Q (прямая формула) <= %.1e"
          % (float(worst_g), float(worst_x)))


I = mp.mpc(0, 1)


def roots_X1(b1):  # P = (b2^2 - b1^3)^2 + b1^8 : b2^2 = b1^3 +- i b1^4
    out = []
    for s in (1, -1):
        r = mp.sqrt(b1**3 + s*I*b1**4)
        out += [r, -r]
    return out


def roots_X2(b1):  # три пары: b1 +- i b1^3, b1 +- i b1^5, b1 + b1^2 +- i b1^4
    return [b1 + I*b1**3, b1 - I*b1**3, b1 + I*b1**5, b1 - I*b1**5, b1 + b1**2 + I*b1**4, b1 + b1**2 - I*b1**4]


def roots_X3(b1):  # b2^3 = b1^5 +- i b1^6
    out = []
    for s in (1, -1):
        z = b1**5 + s*I*b1**6
        r = mp.root(z, 3)
        out += [r*mp.expjpi(mp.mpf(2*q)/3) for q in range(3)]
    return out


def roots_X4(b1):
    return [b1**2 + I*b1**3, b1**2 - I*b1**3, -b1**2 + I*b1**4, -b1**2 - I*b1**4, 2*b1 + I*b1, 2*b1 - I*b1]


def roots_X5(b1):  # почти совпадающие пары
    return [b1**2 + I*b1**4, b1**2 - I*b1**4, b1**2 + I*(b1**4 + b1**5), b1**2 - I*(b1**4 + b1**5)]


def roots_X6(b1):  # Q_4 = (b2^2-b1^2)^2: нули Q_d вне оси b2
    return [b1 + I*b1**5, b1 - I*b1**5, -b1 + I*b1**5, -b1 - I*b1**5]


def roots_X7(b1):  # две тонкие пары с близкими вещественными частями, E = 6
    return [b1**2 + I*b1**6, b1**2 - I*b1**6, b1**2 + b1**3 + I*b1**6, b1**2 + b1**3 - I*b1**6]


def roots_X8(b1):  # три пары: psi = b1^2, b1^2+b1^3, b1^2+2b1^3; eta = b1^5, b1^7, b1^4
    return [b1**2 + I*b1**5, b1**2 - I*b1**5, b1**2 + b1**3 + I*b1**7, b1**2 + b1**3 - I*b1**7,
            b1**2 + 2*b1**3 + I*b1**4, b1**2 + 2*b1**3 - I*b1**4]


def roots_X9(b1):  # почти совпадающие пары с РАЗНЫМИ psi: расстояние b1^5 << eta ~ b1^4
    return [b1**2 + I*b1**4, b1**2 - I*b1**4, b1**2 + b1**5 + I*(b1**4 + b1**6), b1**2 + b1**5 - I*(b1**4 + b1**6)]


EX = {
    'X9': lambda: Example('X9: пары b1^2+-i b1^4 и b1^2+b1^5+-i(b1^4+b1^6)',
                          ((B2 - B1**2)**2 + B1**8)*((B2 - B1**2 - B1**5)**2 + (B1**4 + B1**6)**2),
                          sp.Integer(1), roots_X9, 1, 25),
    'X7': lambda: Example('X7: ((b2-b1^2)^2+b1^12)((b2-b1^2-b1^3)^2+b1^12)',
                          ((B2 - B1**2)**2 + B1**12)*((B2 - B1**2 - B1**3)**2 + B1**12), sp.Integer(1), roots_X7, 1, 41),
    'X8': lambda: Example('X8: три пары, psi через b1^3, eta = b1^5, b1^7, b1^4',
                          ((B2 - B1**2)**2 + B1**10)*((B2 - B1**2 - B1**3)**2 + B1**14)*((B2 - B1**2 - 2*B1**3)**2 + B1**8),
                          sp.Integer(1), roots_X8, 1, 73),
    'X1': lambda: Example('X1: (b2^2-b1^3)^2+b1^8', (B2**2 - B1**3)**2 + B1**8, sp.Integer(1), roots_X1, 2, 9),
    'X2': lambda: Example('X2: три пары, общий psi у двух, u=1+b1+2b2+b1 b2',
                          ((B2 - B1)**2 + B1**6)*((B2 - B1)**2 + B1**10)*((B2 - B1 - B1**2)**2 + B1**8),
                          1 + B1 + 2*B2 + B1*B2, roots_X2, 1, 49),
    'X3': lambda: Example('X3: (b2^3-b1^5)^2+b1^12', (B2**3 - B1**5)**2 + B1**12, sp.Integer(1), roots_X3, 3, 26),
    'X4': lambda: Example('X4: три пары разной толщины, u=exp(b1-b2)',
                          ((B2 - B1**2)**2 + B1**6)*((B2 + B1**2)**2 + B1**8)*((B2 - 2*B1)**2 + B1**2),
                          sp.exp(B1 - B2), roots_X4, 1, 37),
    'X5': lambda: Example('X5: почти совпадающие пары', ((B2 - B1**2)**2 + B1**8)*((B2 - B1**2)**2 + (B1**4 + B1**5)**2),
                          sp.Integer(1), roots_X5, 1, 25),
    'X6': lambda: Example('X6: ((b2-b1)^2+b1^10)((b2+b1)^2+b1^10)', ((B2 - B1)**2 + B1**10)*((B2 + B1)**2 + B1**10),
                          sp.Integer(1), roots_X6, 1, 33),
}

if __name__ == '__main__':
    names = sys.argv[1:] or list(EX)
    for nm in names:
        ex = EX[nm]()
        fd_check(ex, [(1e-2, 1.3e-4), (-1e-3, 2e-6), (1e-3, -1e-3), (3e-2, 0.05)])
        run(ex, Ns=sorted({0, 1, ex.Nw}))
