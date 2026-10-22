"""exlist.py -- единый список примеров n = 3 из полигонов zoo (N2) и frontier (N5); valleys (N3) и classK (N4) работают на тех же
многочленах zoo (K1-K3, A1..., 19 трудных).  Идентификатор: 'z:ID' (zoo, включая 3 калибровки) или 'f:ID' (frontier).
Дублей нет: имена A1, A2, A3, D1, D2 встречаются и в zoo, и в frontier -- это РАЗНЫЕ многочлены (поэтому префикс).
[Эксперимент] (данные, не доказательство)."""
import os, sys
import sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__))
NUM = os.path.join(HERE, '..')
sys.path.insert(0, os.path.join(NUM, '2026-10-21-zoo'))
sys.path.insert(0, os.path.join(NUM, '2026-10-21-frontier'))
import catalog as ZC
import fcat as FC
x, y, z = sp.symbols('x y z')
LOC = dict(x=x, y=y, z=z)

# явные суммы квадратов для u_m примеров frontier (zoo: из catalog.py, поле core['sos'])
Q1 = '(x**2+y**2-z**2)'
F2D = '(x**2/2+y**2-z**2)'
FSOS = {
    'A1': [(1, 'z*y'), (1, 'z**2')],
    'A2': [(1, 'z*y'), (1, 'z**2')],
    'A3': [(1, 'z*y**2'), (1, 'z**2*x'), (1, 'z**2*y'), (1, 'z**3')],
    'B1': [(1, 'y**2*z-x**3')], 'B2': [(1, 'y**2*z-x**3')], 'B4': [(1, 'y**2*z-x**3')],
    'B3': [(1, '(x**2+y**2-z**2)*(x**2+2*y**2-z**2)')], 'B3b': [(1, '(x**2+y**2-z**2)*(x**2+2*y**2-z**2)')],
    'V1': [(1, '(x*y-z**2)*(x**2*y-x*z**2-z**3)'), (1, 'z**5')],
    'V2': [(1, 'x**2*(x*y-z**2)*(x**2*y-x*z**2-z**3)'), (1, 'z**7')],
    'V3': [(1, 'x**6*y**2+z**8'), (1, 'y**8')],
    'V4': [(1, 'x**9*z**8'), (1, 'y**17'), (1, 'z**17')],
    'D1': [(1, Q1 + '*' + F2D)], 'D2': [(1, Q1 + '*' + F2D)], 'D3': [(1, Q1 + '*' + F2D)], 'D4': [(1, Q1 + '*' + F2D)],
    'E1': [(1, 'z*x'), (1, 'z*y'), (1, 'z**2')],
}


def build():
    out = []
    for e in ZC.CATALOG:
        out.append(dict(key='z:' + e['id'], src='zoo', id=e['id'], U=sp.expand(sp.sympify(e['U'], locals=LOC)),
                        sos=[(sp.Rational(c), sp.sympify(p, locals=LOC)) for c, p in e['core']['sos']],
                        calib=e['id'] in ('K1', 'K2', 'K3'), why=e.get('why', '')))
    for e in FC.CAT:
        out.append(dict(key='f:' + e['id'], src='frontier', id=e['id'], U=sp.expand(sp.sympify(e['U'], locals=LOC)),
                        sos=[(sp.Rational(c), sp.sympify(p, locals=LOC)) for c, p in FSOS[e['id']]], calib=False,
                        why=e.get('why', '')))
    return out

EXS = build()
BY = {e['key']: e for e in EXS}
if __name__ == '__main__':
    print(len(EXS), 'examples:', [e['key'] for e in EXS])
