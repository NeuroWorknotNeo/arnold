"""[Эксперимент] Численная проверка конструкции теоремы E (notes/prover/2026-10-21-euler-field.md).

Поле:  xi(b) = ( b1 , b2 + sum_j w_j(b) * chi_j(b1) ),
   phi_j(b1) — d малых комплексных корней Q(b1, .) = 0 (d = ord Q, Q_d(0,1) != 0),
   psi_j = Re phi_j,  eta_j = Im phi_j,  chi_j = b1 psi_j' - psi_j,
   p_j = (b2 - psi_j)^2 + eta_j^2,  w_j = p_j^{-N} / sum_k p_k^{-N}.
Производные phi_j', phi_j'' — неявным дифференцированием Q(b1, phi(b1)) = 0.
Проверяется: min (xi.grad Q)/Q  и  max ||D xi|| (аналитически, сверка разностями).
Точность: mpmath, mp.dps = 60.
Запуск: ~/venv/bin/python construction.py
"""
import sys
import random
import sympy as sp
import mpmath as mp

mp.mp.dps = 60
b1s, b2s = sp.symbols('b1 b2')


class Field:
    def __init__(self, Q, N):
        self.Q = sp.expand(Q)
        P = sp.Poly(self.Q, b2s)
        self.coeffs = [sp.lambdify(b1s, c, 'mpmath') for c in P.all_coeffs()]
        self.d = min(sp.Poly(self.Q, b1s, b2s).monoms(), key=sum)
        self.d = min(sum(m) for m in sp.Poly(self.Q, b1s, b2s).monoms())
        Qd0 = sp.Poly(self.Q, b1s, b2s).coeff_monomial(b2s**self.d)
        assert Qd0 != 0, "нужно Q_d(0,1) != 0"
        f = lambda e: sp.lambdify((b1s, b2s), e, 'mpmath')
        self.fQ = f(self.Q)
        self.f1, self.f2 = f(sp.diff(self.Q, b1s)), f(sp.diff(self.Q, b2s))
        self.f11 = f(sp.diff(self.Q, b1s, 2))
        self.f12 = f(sp.diff(self.Q, b1s, b2s))
        self.f22 = f(sp.diff(self.Q, b2s, 2))
        self.N = N
        self._cache = {}

    def roots(self, x):
        key = mp.nstr(x, 50)
        if key in self._cache:
            return self._cache[key]
        cs = [mp.mpf(c(x)) if not callable(c) else c(x) for c in self.coeffs]
        cs = [mp.mpf(c) for c in cs]
        rts = mp.polyroots(cs, maxsteps=400, extraprec=400)
        rts = sorted(rts, key=lambda z: abs(z))[: self.d]
        out = []
        for ph in rts:
            ph = mp.mpc(ph)
            Q1, Q2 = self.f1(x, ph), self.f2(x, ph)
            d1 = -Q1 / Q2
            d2 = -(self.f11(x, ph) + 2*self.f12(x, ph)*d1 + self.f22(x, ph)*d1**2) / Q2
            out.append((ph, d1, d2))
        self._cache[key] = out
        return out

    def xi_and_D(self, x, y):
        x, y = mp.mpf(x), mp.mpf(y)
        R = self.roots(x)
        N = self.N
        psi = [mp.re(r[0]) for r in R]
        eta = [mp.im(r[0]) for r in R]
        dpsi = [mp.re(r[1]) for r in R]
        deta = [mp.im(r[1]) for r in R]
        ddpsi = [mp.re(r[2]) for r in R]
        chi = [x*dp - p for dp, p in zip(dpsi, psi)]
        dchi = [x*ddp for ddp in ddpsi]
        p = [(y - ps)**2 + et**2 for ps, et in zip(psi, eta)]
        pmin = min(p)
        a = [(pmin/pk)**N for pk in p]
        S = sum(a)
        w = [ak/S for ak in a]
        dp1 = [-2*(y - ps)*dps + 2*et*det for ps, dps, et, det in zip(psi, dpsi, eta, deta)]
        dp2 = [2*(y - ps) for ps in psi]
        m1 = sum(wk*g/pk for wk, g, pk in zip(w, dp1, p))
        m2 = sum(wk*g/pk for wk, g, pk in zip(w, dp2, p))
        dw1 = [N*wj*(-g/pj + m1) for wj, g, pj in zip(w, dp1, p)]
        dw2 = [N*wj*(-g/pj + m2) for wj, g, pj in zip(w, dp2, p)]
        c = sum(wj*cj for wj, cj in zip(w, chi))
        c1 = sum(wj*dcj for wj, dcj in zip(w, dchi)) + sum(cj*g for cj, g in zip(chi, dw1))
        c2 = sum(cj*g for cj, g in zip(chi, dw2))
        xi = (x, y + c)
        D = mp.matrix([[1, 0], [c1, 1 + c2]])
        return xi, D

    def ratio(self, x, y):
        xi, D = self.xi_and_D(x, y)
        x, y = mp.mpf(x), mp.mpf(y)
        r = (xi[0]*self.f1(x, y) + xi[1]*self.f2(x, y)) / self.fQ(x, y)
        nrm = mp.sqrt(max(mp.eig(D.T*D)[0], key=lambda z: mp.re(z)).real)
        return r, nrm, D


def sample_points(F, radius, s_list):
    pts = []
    for s in s_list:
        for sg in (1, -1):
            x = sg*mp.mpf(10)**(-s)
            R = F.roots(x)
            ys = [x*mp.mpf(t)/10 for t in range(-40, 41, 2)]
            for r in R:
                ps, et = mp.re(r[0]), abs(mp.im(r[0]))
                ys.append(ps)
                for u in [mp.mpf(i)/4 for i in range(-12, 13)]:
                    for sgn in (1, -1):
                        ys.append(ps + sgn*et*mp.mpf(10)**u)
            psis = sorted(set(mp.nstr(mp.re(r[0]), 40) for r in R))
            psis = [mp.mpf(v) for v in psis]
            for i in range(len(psis)):
                for j in range(i+1, len(psis)):
                    mid = (psis[i] + psis[j])/2
                    for t in [mp.mpf(q)/20 for q in range(-10, 11)]:
                        ys.append(mid + t*(psis[j] - psis[i]))
            for y in ys:
                if x*x + y*y < radius**2:
                    pts.append((x, y))
    # окрестность оси b2 (|b1| << |b2|)
    for t in range(1, 10):
        yv = radius*mp.mpf(t)/10
        for s in [3, 5, 8]:
            for sg in (1, -1):
                for sy in (1, -1):
                    pts.append((sg*yv*mp.mpf(10)**(-s), sy*yv))
    return pts


def fd_check(F, x, y, h):
    x, y = mp.mpf(x), mp.mpf(y)
    _, D = F.xi_and_D(x, y)
    ex = lambda a, b: F.xi_and_D(a, b)[0]
    c1 = (ex(x + h, y)[1] - ex(x - h, y)[1])/(2*h)
    c2 = (ex(x, y + h)[1] - ex(x, y - h)[1])/(2*h)
    return max(abs(c1 - D[1, 0]), abs(c2 - D[1, 1]))


EXAMPLES = {
    'E1 (b2-b1^2)^2+b1^6': ((b2s - b1s**2)**2 + b1s**6, 0.1),
    'E2 (b2-b1^2-b1^3)^2+b1^8': ((b2s - b1s**2 - b1s**3)**2 + b1s**8, 0.1),
    'E3 (b2^2-b1^4)^2+b1^10': ((b2s**2 - b1s**4)**2 + b1s**10, 0.1),
    'E4 b2^2+1.5 b1^2 b2+b1^4': (b2s**2 + sp.Rational(3, 2)*b1s**2*b2s + b1s**4, 0.1),
    'E6 три подоврага': (((b2s - b1s**2)**2 + b1s**6)*((b2s - b1s**2 - b1s**3)**2 + b1s**10)
                         * ((b2s + b1s)**2 + b1s**4), 0.05),
}
# E5: G1*G2 при k = 1.99 в повёрнутых координатах b = A v, A = [[1,1],[-1,1]]
k = sp.Rational(199, 100)
u1, u2 = b1s + b2s, -b1s + b2s
G1 = u2**2 + k*u1**2*u2 + u1**4
G2 = u1**2 + k*u1*u2**2 + u2**4
EXAMPLES['E5 G1*G2, k=1.99 (поворот)'] = (G1*G2, 0.02)
# контрпример к анизотропии, с переставленными ролями (Weierstrass по x): b1:=y, b2:=x
xx, yy = b2s, b1s
EXAMPLES['C  A*B (b1=y, b2=x)'] = ((((xx - yy**2)**2 + yy**8)*((xx - yy**2 - yy**3)**2 + yy**8)), 0.05)

if __name__ == '__main__':
    names = sys.argv[1:] or list(EXAMPLES)
    random.seed(1)
    for name in names:
        Q, rad = EXAMPLES[name]
        for N in (2, 6):
            F = Field(Q, N)
            pts = sample_points(F, mp.mpf(rad), [1.5, 2, 2.5, 3, 3.5])
            worst_r, worst_D = mp.inf, 0
            arg_r = arg_D = None
            for (x, y) in pts:
                r, nrm, _ = F.ratio(x, y)
                if r < worst_r:
                    worst_r, arg_r = r, (x, y)
                if nrm > worst_D:
                    worst_D, arg_D = nrm, (x, y)
            # сверка производной разностями в случайных точках
            errs = []
            for (x, y) in random.sample(pts, 15):
                scale = min(abs(x), max(abs(F.xi_and_D(x, y)[0][1] - y), mp.mpf(10)**-40))
                h = abs(x)*mp.mpf(10)**-20
                errs.append(fd_check(F, x, y, h))
            print(f"{name}: d={F.d}, N={N}, точек={len(pts)}; min xi.gradQ/Q = {mp.nstr(worst_r, 6)} "
                  f"(в {mp.nstr(arg_r[0], 3)}, {mp.nstr(arg_r[1], 3)}); max||Dxi|| = {mp.nstr(worst_D, 6)} "
                  f"(в {mp.nstr(arg_D[0], 3)}, {mp.nstr(arg_D[1], 3)}); max ошибка FD = {mp.nstr(max(errs), 3)}",
                  flush=True)
