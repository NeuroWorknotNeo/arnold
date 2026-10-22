"""make_iso_table.py -- сводная таблица точных проверок: iso_*.json (по времени изменения: поздние перекрывают ранние), iso_sat2.txt, mu_long.txt -> iso_table.md"""
import json, glob, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
import fcat
iso = {}
for f in sorted(glob.glob(os.path.join(HERE, 'iso_*.json')), key=os.path.getmtime):
    for r in json.load(open(f)):
        # не затирать полученное μ значением 'skipped'
        old = iso.get(r['id'])
        if old and r['mu'] in ('skipped', None) and isinstance(old.get('mu'), int):
            r['mu'] = old['mu']
        iso[r['id']] = r
sat2 = {}
if os.path.exists(os.path.join(HERE, 'iso_sat2.txt')):
    for l in open(os.path.join(HERE, 'iso_sat2.txt')):
        m = re.match(r'(\w+): (.*)', l.strip())
        if m:
            sat2[m.group(1)] = m.group(2)
mul = {}
if os.path.exists(os.path.join(HERE, 'mu_long.txt')):
    for l in open(os.path.join(HERE, 'mu_long.txt')):
        m = re.match(r'(\w+): mu = (-?\d+)', l.strip())
        if m:
            mul[m.group(1)] = int(m.group(2))
L = ['| № | deg U | m | μ (локальное, Singular) | сертификат изолированности над ℝ | свидетель U<0 | инвариантные плоскости/прямые с неустойчивостью (SYM) |', '|---|---|---|---|---|---|---|']
for e in fcat.CAT:
    r = iso.get(e['id'])
    if not r:
        continue
    mu = r['mu']
    if isinstance(mu, str) and mu.startswith('err'):
        mu = 'не вычислено (лимит времени)'
    if e['id'] in mul:
        mu = mul[e['id']]
    if mu is None:
        mu = '∞ (комплексные изотропные прямые)'
    cert = []
    if isinstance(mu, int):
        cert.append('μ конечно ⇒ изолирована над ℂ, значит и над ℝ')
    if r.get('cert'):
        cert.append(f"насыщение J:p^∞, p={r['p']}, K⊄𝔪")
    if e['id'] in sat2:
        cert.append('двойное насыщение: ' + sat2[e['id']])
    if not cert:
        cert.append('**не сертифицирована**')
    w = r['witness']
    wt = f"{w['kind']}: порядок {w['order']}, коэфф. {w['coeff']}" if isinstance(w, dict) else str(w)
    inv = r.get('invariant')
    if isinstance(inv, list):
        yes = [v for v in inv if v['verdict'] == 'yes']
        invt = f"{len(inv)} найдено, с неустойчивостью: {len(yes)}" if inv else 'инвариантных нет'
    else:
        invt = str(inv)
    L.append(f"| {e['id']} | {r['degree']} | {r['m']} | {mu} | {'; '.join(cert)} | {wt} | {invt} |")
open(os.path.join(HERE, 'iso_table.md'), 'w').write('\n'.join(L) + '\n')
print('\n'.join(L))
