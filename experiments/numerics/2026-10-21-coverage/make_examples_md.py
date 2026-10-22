"""make_examples_md.py -- examples.md: полный список 44 примеров n = 3 (без дублей): полный многочлен U (как в каталоге полигона), m, u_m и его сумма квадратов, изолированность 0, свидетель U<0."""
import json, os
import sympy as sp
from exlist import EXS, BY, HERE
import catalog as ZC, fcat as FC
basic = {r['key']: r for r in json.load(open(os.path.join(HERE, 'basic.json')))}
zU = {t['id']: t['U'] for t in ZC.CATALOG}; fU = {t['id']: t['U'] for t in FC.CAT}
zname = {t['id']: t.get('name', '') for t in ZC.CATALOG}
lines = ['# Список примеров n = 3 из полигонов N2 (zoo, 24 + 3 калибровки), N3/N4 (те же 22 многочлена zoo), N5 (frontier, 17)', '',
         'Идентификатор `z:ID` — zoo (`experiments/numerics/2026-10-21-zoo/catalog.py`), `f:ID` — frontier (`.../2026-10-21-frontier/fcat.py`). Имена A1, A2, A3, D1, D2 встречаются в обоих полигонах — это РАЗНЫЕ многочлены. '
         'N3 (valleys) и N4 (classK) работали с 19 трудными примерами zoo и калибровками K1–K3; новых многочленов там нет. [Эксперимент: точная арифметика]', '',
         '| № | U | deg | m | u_m | SOS u_m (expand-проверка) | 0 изолирована над R | свидетель U<0 |', '|---|---|---|---|---|---|---|---|']
for e in EXS:
    k = e['key']; b = basic[k]
    U = (zU if e['src'] == 'zoo' else fU)[e['id']]
    if k == 'z:A6':
        U = 'U_13(Rq), в развёрнутом виде см. basic.json (поле U)'
    sos = ' + '.join('(%s)²' % p for c, p in b['sos']) if all(c == '1' for c, p in b['sos']) else ' + '.join('%s·(%s)²' % (c, p) for c, p in b['sos'])
    lines.append('| %s | `%s` | %d | %d | `%s` | `%s` ✓ | %s: %s | %s τ^%d |' % (k, U.replace('|', '\\|'), b['deg'], b['m'], b['u_m'].replace('|', '\\|'), sos.replace('**', '^'), b['isolation']['status'], b['isolation']['how'], b['witness']['coeff'][:30], b['witness']['order']))
open(os.path.join(HERE, 'examples.md'), 'w').write('\n'.join(lines) + '\n')
print(len(lines) - 6, 'rows')
