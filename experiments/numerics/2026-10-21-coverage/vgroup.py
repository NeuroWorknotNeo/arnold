"""vgroup.py -- V1-V4 (изолированный вырожденный нуль u_m в e_x): проверка условий утверждения Q / следствия E [012] в прямой карте (L = I, gamma = 0).
V3: Q1 ✓, Q2 ✓, E ✓ (direct_chart.py).  V4: (Q1),(Q2) ✓, но ориентация c1 > c2 -> Q_d(0,1) = 0 => E неприменимо.
V1, V2: перебор весов (c_y, c_z) > 1: есть ли допустимые веса, при которых все мономы имеют уровень >= beta (Q1)?  Если допустимые веса есть только с мономами
уровня < beta, профиль -- градуированный (C'), и знакоопределённость R_j проверяется.   [Эксперимент: точный]"""
import sys, json, os, itertools
import sympy as sp
from fractions import Fraction
from exlist import BY, HERE, x, y, z
import direct_chart as DC
w1, w2 = DC.w1, DC.w2

def v4():
    r, Qp, F0 = DC.check_Q('f:V4', 0, 1, (2, 3), 66, (0, 0))
    d, Qd = DC.lowest_form(Qp)
    # c = (2, 3) для (y, z): c1 = 2 <= c2 = 3 -> (b1, b2) = (y, z) = (w1, w2); Q_d(0,1) = Q_d(w1=0, w2=1)
    val = Qd.subs({w1: 0, w2: 1})
    r['ord_Q'] = d; r['Q_d'] = str(Qd); r['Q_d_at_(0,1)'] = str(val)
    # нули Q: Q = A B? сверим
    A = (w1 - w2**2)**2 + w2**8; B = (w1 - w2**2 - w2**3)**2 + w2**8
    r['Q_equals_A_times_B'] = bool(sp.expand(A*B - Qp) == 0)
    return r

def levels(key, c, beta, axis=0):
    """список (level, коэффициент-моном) по мономам U при весах c=(c_y,c_z)"""
    U = BY[key]['U']
    P = sp.Poly(U, x, y, z)
    rows = []
    for (a, j, k), co in P.terms():
        lev = a + c[0]*j + c[1]*k
        rows.append((lev, (a, j, k), co))
    rows.sort(key=lambda r: r[0])
    return rows

def scan_weights(key, beta, grid=60, lo=1, hi=3):
    """допустимые (c_y, c_z) на рациональной сетке: все мономы уровня >= beta"""
    U = BY[key]['U']
    P = sp.Poly(U, x, y, z)
    mons = [m for m, _ in P.terms()]
    ok = []
    for i in range(1, grid*(hi-lo)+1):
        cy = Fraction(lo) + Fraction(i, grid)
        for jj in range(1, grid*(hi-lo)+1):
            cz = Fraction(lo) + Fraction(jj, grid)
            if all(a + cy*j + cz*k >= beta for a, j, k in mons):
                ok.append((cy, cz))
    return ok

if __name__ == '__main__':
    out = {}
    out['f:V4'] = v4()
    print('V4', json.dumps({k: v for k, v in out['f:V4'].items() if k in ('Q1', 'min_level', 'Q_d', 'Q_d_at_(0,1)', 'ord_Q', 'Q_equals_A_times_B', 'F0_at_0')}, ensure_ascii=False))
    for key, beta in (('f:V1', 12), ('f:V2', 16)):
        ok = scan_weights(key, beta, grid=40, lo=1, hi=3)
        out[key] = dict(beta=beta, n_admissible=len(ok), examples=[(str(a), str(b)) for a, b in ok[:6]])
        print(key, 'допустимых весов (c_y, c_z) на сетке 1/40 в (1,3]^2 (все мономы уровня >= beta):', len(ok), out[key]['examples'][:6])
        # граница допустимой области: минимальные c_y, c_z
        if ok:
            print('   min c_y =', min(a for a, b in ok), ' min c_z =', min(b for a, b in ok))
    json.dump(out, open(os.path.join(HERE, 'vgroup.json'), 'w'), indent=1, ensure_ascii=False, default=str)


def graded_R(key, c, beta, N):
    """градуированный профиль в прямой карте (L=I, gamma=0): F = x^-beta U(x, x^c1 b1, x^c2 b2) = sum_l x^{l-beta} R_l(b); возвращает R_l для l <= beta"""
    U = BY[key]['U']
    P = sp.Poly(U, x, y, z)
    d = {}
    for (a, j, k), co in P.terms():
        lev = a + c[0]*j + c[1]*k
        if lev <= beta:
            d.setdefault(lev, 0)
            d[lev] += co*w1**j*w2**k
    return {l: sp.expand(v) for l, v in sorted(d.items())}

def sign_definite_numeric(R, box=1.5, n=121):
    import numpy as np
    f = sp.lambdify((w1, w2), R, 'numpy')
    g = np.linspace(-box, box, n)
    A, B = np.meshgrid(g, g, indexing='ij')
    v = f(A, B)
    return float(v.min()), float(v.max())

def c_prime_check():
    out = {}
    for key, c, beta, N in (('f:V1', (sp.Rational(7, 5), sp.Rational(6, 5)), 12, 5), ('f:V2', (sp.Rational(9, 7), sp.Rational(8, 7)), 16, 7)):
        Rs = graded_R(key, c, beta, N)
        out[key] = {}
        for l, R in Rs.items():
            lo, hi = sign_definite_numeric(R)
            out[key][str(l)] = dict(R=str(R)[:200], min_on_box=lo, max_on_box=hi, sign_indefinite=bool(lo < -1e-9 and hi > 1e-9))
            print(key, 'level', l, 'e = beta - level =', beta - l, ' R_l:', str(R)[:110], '| min/max on box [-1.5,1.5]^2:', round(lo, 3), round(hi, 3))
    return out

if __name__ == '__main__':
    cp = c_prime_check()
    r = json.load(open(os.path.join(HERE, 'vgroup.json')))
    r['graded'] = cp
    json.dump(r, open(os.path.join(HERE, 'vgroup.json'), 'w'), indent=1, ensure_ascii=False, default=str)
