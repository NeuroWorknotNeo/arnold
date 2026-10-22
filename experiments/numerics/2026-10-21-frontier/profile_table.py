"""profile_table.py -- таблица профильных функций g_i(s) (out/ID.prof.json) на двух последних радиусах: сходимость масштабированного профиля.  -> profiles.md"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
SS = [-2, -1, -0.5, 0, 0.5, 1, 2]
L = ['| № | r | e_i | A_i (угл. ширина) | ' + ' | '.join(f's={s:g}' for s in SS) + ' |', '|---|---|---|---|' + '---|' * len(SS)]
for eid in sys.argv[1:]:
    p = os.path.join(HERE, 'out', eid + '.prof.json')
    if not os.path.exists(p):
        continue
    d = json.load(open(p))
    for rec in d[-2:]:
        for i in (0, 1):
            g = rec['g'][i]
            if g is None:
                continue
            L.append(f"| {eid} | 1e{rec['logr']:g} | e{i+1} | {float(rec['A'][i]):.3e} | " + ' | '.join(f"{float(v):.3f}" for v in g) + ' |')
open(os.path.join(HERE, 'profiles.md'), 'w').write('\n'.join(L) + '\n')
print('\n'.join(L))
