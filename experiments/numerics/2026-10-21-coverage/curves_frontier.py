"""curves_frontier.py -- эффективный потенциал G на экваторе Sigma для A1, A2, A3, E1 (frontier), точно (sympy, рациональные ряды лемм K1 [008]).
Использует модуль classK (kfib/classk_analyze) без изменений.  Для каждой дуги: j, G, критические точки G (G, G'', G''+jG), точки, где H=D^2u_m(n,n)=0.
Вывод: curves_frontier.json.   [Эксперимент: точно (ряды) + вещественные корни (sympy.real_roots), значения mpmath]"""
import sys, os, json, time
import sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '2026-10-21-classK'))
sys.path.insert(0, os.path.join(HERE, '..', '2026-10-21-zoo'))
import comps as KC
import classk_analyze as KA
from exlist import BY
x, y, z = KC.x, KC.y, KC.z
t = KC.t

def curve(name, p, f, sign=1):
    p = [sp.expand(sign * c) for c in p]
    return KC.mk(name, p, f)

def equator():
    return [curve('equator z=0 (φ=2 arctan t)', [1 - t**2, 2*t, 0], z)]

COMPS = {'f:A1': equator(), 'f:A2': equator(), 'f:A3': equator(), 'f:E1': equator()}
# (кусп и коники: j = m+1, G = u_{m+1}|Sigma -- см. cusp_G.py и g1.py; общий модуль kfib для них не нужен и для коник с нечётным j даёт sqrt)

def run(key):
    ex = key
    KC.U[ex] = BY[key]['U']
    m, um, parts = KA.lowest(KC.U[ex])
    out = dict(key=key, m=int(m), comps=[])
    for comp in COMPS[key]:
        t0 = time.time()
        try:
            r = KA.analyse_curve(ex, comp, m, um)
        except Exception as e:
            r = dict(name=comp[1], error=repr(e))
        r['seconds'] = time.time() - t0
        out['comps'].append(r)
    return out

if __name__ == '__main__':
    keys = sys.argv[1:] or list(COMPS)
    fn = os.path.join(HERE, 'curves_frontier.json')
    allr = json.load(open(fn)) if os.path.exists(fn) else {}
    for k in keys:
        r = run(k)
        allr[k] = r
        print('==', k, 'm=', r['m'])
        for c in r['comps']:
            if 'error' in c:
                print('  ', c['name'], 'ERROR', c['error']); continue
            print('  ', c['name'], '| H =', c['H'], '| MB:', c['MB_on_component'], '| H real roots:', c.get('H_real_roots'), '| j =', c.get('j'), '| G =', str(c.get('G'))[:160])
            for cr in c.get('crit', []):
                print('       crit t=%s G=%s d2G=%s G2+jG=%s mult=%s kind=%s' % (cr['t'][:12], cr['G'][:14], cr['d2G'][:12], (cr['G2_plus_jG'] or '')[:12], cr['mult'], cr['kind']))
        json.dump(allr, open(fn, 'w'), indent=1, default=str)
