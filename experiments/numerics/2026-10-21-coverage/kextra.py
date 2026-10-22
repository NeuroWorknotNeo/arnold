"""kextra.py -- недостающие в classK примеры zoo (P2, C3, H1, H2): те же расчёты K0/K1/K2 (G, критические точки) модулем classK.  [Эксперимент: точно (ряды), mpmath]"""
import sys, os, json
import sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '2026-10-21-classK'))
sys.path.insert(0, os.path.join(HERE, '..', '2026-10-21-zoo'))
import comps as KC
import classk_analyze as KA
from exlist import BY
x, y, z, t = KC.x, KC.y, KC.z, KC.t
fE = x**2 + 2*y**2 - z**2
out = {}
def run(key, comps_):
    KC.U[key] = BY[key]['U']
    m, um, parts = KA.lowest(KC.U[key])
    res = dict(key=key, m=int(m), comps=[])
    for comp in comps_:
        if comp[0] == 'curve':
            res['comps'].append(KA.analyse_curve(key, comp, m, um))
        else:
            res['comps'].append(KA.analyse_point(key, comp, m, um))
    return res
P8 = [(a, b, c) for a in (1, -1) for b in (1, -1) for c in (1, -1)]
out['z:P2'] = run('z:P2', [('point', str(q), list(q)) for q in P8])

out['z:H1'] = run('z:H1', [('point', '+e_x', [1, 0, 0]), ('point', '-e_x', [-1, 0, 0])])
out['z:H2'] = run('z:H2', KC.equator())
for k, v in out.items():
    print('==', k, 'm=', v['m'])
    for c in v['comps']:
        d = {kk: vv for kk, vv in c.items() if kk in ('name', 'MB', 'MB_on_component', 'j', 'G', 'g_j', 'g_j_float', 'H')}
        print('   ', d)
        for cr in c.get('crit', []):
            print('       crit', cr['t'][:10], 'G', cr['G'][:12], 'd2G', cr['d2G'][:10], 'G2+jG', (cr['G2_plus_jG'] or '')[:10], cr['kind'])
json.dump(out, open(os.path.join(HERE, 'kextra.json'), 'w'), indent=1, default=str)
