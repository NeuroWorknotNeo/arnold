"""[Эксперимент] R27: теорема Md на двух полных потенциалах в R^3 (свои примеры).

U_A = Q0^2 + z^4 (z-x)^2 - z^5 y^2,   U_B = Q0^2 + z^4 (z-x)^2 - z^7,   Q0 = x^2+y^2-z^2.
m=4, u_4=Q0^2>=0, Sigma -- две окружности (Морс--Ботт), компонента Sigma_0: z=1/sqrt2.
omega(th) = (cos phi, sin phi, 1)/sqrt2, phi = sqrt2*th (натуральный параметр), k == 1,
n = omega x T = (-cos phi, -sin phi, 1)/sqrt2, h_n = 8. j = 6, G = (1-cos phi)^2/8 >= 0, G(0)=0.
Изолированность 0 НЕ проверяется: теорема 2 [007] её не требует.

Предсказание леммы V (выкладки руками, см. отзыв):
 A: f ~ tau^4/8 - s tau^2/(4 sqrt2): ничья tau_v = +-2^{-1/4} s^{1/2}; N1=2, Gamma1=4, a=1/16,
    A'=1, alpha=1/2, gamma=2, beta=8, c'=3, Q_V = b^2/(2 sqrt2) + (c/2) b^3 + b^4/8, c=2^{-1/4}.
 B: f ~ tau^4/8 - s/(8 sqrt2): N1=1, Gamma1=1, a=1/(8 sqrt2), A'=1/4, alpha=1/4, gamma=1,
    beta=7, c'=5/2, Q_V = b^4/8 (вырожденный угловой минимум, k0=4).
Проверяем: U(Phi(x,u,zeta))/x^beta -> F_0(b) = -a + Q_V(b1) + 4 e^2 равномерно на сетке |b|<=r,
где Phi -- карта (5.1) с численно найденными tau_v(x) (крит. точка U на срезе s=x) и eta*(x,theta).
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 90
X, Y, Z = sp.symbols('X Y Z', real=True)
Q0 = X**2 + Y**2 - Z**2
U_A = Q0**2 + Z**4*(Z - X)**2 - Z**5*Y**2
U_B = Q0**2 + Z**4*(Z - X)**2 - Z**7
SQ2 = mp.sqrt(2)


def frame(th):
    ph = SQ2*th
    om = mp.matrix([mp.cos(ph), mp.sin(ph), 1])/SQ2
    T = mp.matrix([-mp.sin(ph), mp.cos(ph), 0])
    n = mp.matrix([-mp.cos(ph), -mp.sin(ph), 1])/SQ2
    return om, T, n


def make(Uexpr):
    Uf = sp.lambdify((X, Y, Z), Uexpr, 'mpmath')
    gr = [sp.lambdify((X, Y, Z), sp.diff(Uexpr, v), 'mpmath') for v in (X, Y, Z)]

    def U(q):
        return Uf(q[0], q[1], q[2])

    def grad(q):
        return mp.matrix([g(q[0], q[1], q[2]) for g in gr])
    return U, grad


def dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]


def eta_star(U, grad, s, th, guess=0):
    om, T, n = frame(th)
    f = lambda e: dot(grad(s*om + e*n), n)
    return mp.findroot(f, mp.mpf(guess), tol=mp.mpf(10)**(-80))


def bottom(U, grad, s, th_guess):
    """Критическая точка U на срезе {s*omega(th) + eta*n}: (th, eta)."""
    def F(th, e):
        om, T, n = frame(th)
        g = grad(s*om + e*n)
        return [dot(g, T), dot(g, n)]
    sol = mp.findroot(F, [mp.mpf(th_guess), mp.mpf(0)], tol=mp.mpf(10)**(-75))
    return sol[0], sol[1]


def Ghat(U, grad, s, th):
    e = eta_star(U, grad, s, th)
    om, T, n = frame(th)
    return U(s*om + e*n)/s**6


def run(name, Uexpr, beta, alpha, cprime, a, QV, tau_guess, grid_r, xs):
    U, grad = make(Uexpr)
    print('=' * 78)
    print(name, f' beta={beta} alpha={alpha} c\'={cprime} a={mp.nstr(a, 10)}')
    for x in xs:
        x = mp.mpf(x)
        if tau_guess is None:
            tv = mp.mpf(0)   # U_B симметричен по y -> -y, th=0 -- критическая точка Ghat(x,.)
        else:
            tv, _ = bottom(U, grad, x, tau_guess(x))
        depth = Ghat(U, grad, x, tv)
        # глобальность в окне: сетка по tau в [-0.2, 0.2]
        wmin = min(Ghat(U, grad, x, mp.mpf(i)/500) for i in range(-100, 101))
        sup = mp.mpf(0)
        worst = None
        for i in range(-6, 7):
            for jj in range(-6, 7):
                b1 = grid_r*mp.mpf(i)/6
                e = grid_r*mp.mpf(jj)/6
                if b1**2 + e**2 > grid_r**2:
                    continue
                vt = tv + x**alpha*b1
                zeta = x**cprime*e
                es = eta_star(U, grad, x, vt)
                om, T, n = frame(vt)
                q = x*om + (es + zeta)*n
                Fv = U(q)/x**beta
                F0 = -a + QV(b1) + 4*e**2
                if abs(Fv - F0) > sup:
                    sup, worst = abs(Fv - F0), (b1, e)
        print(f'  x={mp.nstr(x, 3):>7}  tau_v={mp.nstr(tv, 12):>16}  tau_v/x^(1/2)={mp.nstr(tv/mp.sqrt(x), 10):>13}'
              f'  Ghat(x,tau_v)/(-a x^gamma)={mp.nstr(depth/(-a*x**(beta-6)), 10):>13}'
              f'  min_grid Ghat - Ghat(tau_v)={mp.nstr(wmin - depth, 3):>10}'
              f'  sup|F-F0|={mp.nstr(sup, 4)}')


if __name__ == '__main__':
    c = mp.mpf(2)**(-0.25)
    QVA = lambda b: b**2/(2*SQ2) + c/2*b**3 + b**4/8
    run('U_A (ничья, k0=2, нечётные члены в Q_V)', U_A, 8, mp.mpf(1)/2, 3, mp.mpf(1)/16, QVA,
        lambda x: c*mp.sqrt(x), mp.mpf('0.5'), ['1e-3', '1e-4', '1e-5', '1e-6'])
    QVB = lambda b: b**4/8
    run('U_B (вырожденный угловой минимум, k0=4)', U_B, 7, mp.mpf(1)/4, mp.mpf(5)/2, 1/(8*SQ2), QVB,
        None, mp.mpf('0.5'), ['1e-4', '1e-6', '1e-8', '1e-10'])
