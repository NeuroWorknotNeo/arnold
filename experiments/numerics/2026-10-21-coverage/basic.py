"""basic.py -- пункт 1: многочлен, m, u_m, u_m >= 0 (явная сумма квадратов, expand), свидетель U < 0 (точный), изолированность 0 (из логов
полигонов, статус).  Пишет basic.json.  [Эксперимент: точная рациональная арифметика sympy]"""
import json, glob, os, re
import sympy as sp
from exlist import EXS, HERE, NUM, x, y, z, LOC

tau, t = sp.symbols('tau t')

def forms(U):
    P = sp.Poly(U, x, y, z)
    d = {}
    for mon, c in P.terms():
        d[sum(mon)] = d.get(sum(mon), 0) + c * x**mon[0] * y**mon[1] * z**mon[2]
    return {k: sp.expand(v) for k, v in sorted(d.items()) if sp.expand(v) != 0}

# --- свидетели U<0 (из логов/каталогов полигонов; здесь пересчитан младший коэффициент точно)
import catalog as ZC, fcat as FC
zres = json.load(open(os.path.join(NUM, '2026-10-21-zoo', 'results.json')))
ZW = {r['id']: r['witness'] for r in zres}
ZISO = {r['id']: r['isolation'] for r in zres}
FW = {e['id']: e['witness'] for e in FC.CAT}

def lead_on_curve(U, cur):
    xs = [sp.sympify(c, locals={'tau': tau}) for c in cur]
    e = sp.expand(U.subs({x: xs[0], y: xs[1], z: xs[2]}, simultaneous=True))
    P = sp.Poly(e, tau)
    k = min(mon[0] for mon, c in P.terms())
    return k, P.coeff_monomial(tau**k)

def witness(key, U):
    src, ident = key.split(':')
    if src == 'z':
        w = ZW[ident]
        if w['kind'] == 'ray':
            cur = [str(c) + '*tau' for c in w['w']]
        else:
            cur = w['curve']
    else:
        w = FW[ident]
        if w[0] == 'ray':
            cur = [str(c) + '*tau' for c in w[1]]
        else:
            cur = list(w[1])
    k, c = lead_on_curve(U, cur)
    return dict(curve=cur, order=int(k), coeff=str(c), negative=bool(c < 0))

# --- изолированность
FISO = {}
for f in glob.glob(os.path.join(NUM, '2026-10-21-frontier', 'iso_*.json')):
    for r in json.load(open(f)):
        FISO[r['id']] = r
FSAT = {}
for l in open(os.path.join(NUM, '2026-10-21-frontier', 'iso_sat2.txt')):
    m_ = re.match(r'(\w+): K=.*НЕ содержится в m', l)
    if m_:
        FSAT[m_.group(1)] = l.strip()

def isolation(key):
    src, ident = key.split(':')
    if src == 'z':
        d = ZISO[ident]
        if d['mu'] is not None and d['mu'] >= 0:
            return dict(status='точно', how=f"число Милнора μ={d['mu']} конечно (Singular, локальный порядок) => изолирована над C, значит над R")
        return dict(status='точно', how=f"насыщение J:p^inf, p={d['p']}, K не лежит в m (Singular над Q) => 0 изолирована над R (над C нет: μ=inf)")
    r = FISO.get(ident, {})
    if r.get('mu') not in (None, 'skipped') and isinstance(r.get('mu'), int) and r['mu'] >= 0:
        return dict(status='точно', how=f"μ={r['mu']} конечно (Singular) => изолирована над C и над R")
    if ident in FSAT:
        return dict(status='точно', how='двойное насыщение (J:p1^inf):p2^inf, K не лежит в m (Singular над Q) => изолирована над R; см. iso_sat2.txt')
    if r.get('cert') is True:
        return dict(status='точно', how='насыщение J:p^inf, K не лежит в m (Singular)')
    return dict(status='не сертифицировано', how='сертификат не завершился (степень велика); см. README, раздел «Фоновые расчёты»')

def main():
    rows = []
    for e in EXS:
        U = e['U']
        fm = forms(U)
        m = min(fm)
        um = fm[m]
        sos_ok = sp.expand(sum(c * p**2 for c, p in e['sos']) - um) == 0
        w = witness(e['key'], U)
        rows.append(dict(key=e['key'], deg=int(max(fm)), m=int(m), forms_degrees=sorted(int(k) for k in fm),
                         u_m=str(sp.factor(um)), U=str(U), sos_ok=bool(sos_ok),
                         sos=[(str(c), str(p)) for c, p in e['sos']], witness=w, isolation=isolation(e['key']), calib=e['calib']))
        assert sos_ok, e['key']
        assert min(fm) >= 2 and 1 not in fm and 0 not in fm
    json.dump(rows, open(os.path.join(HERE, 'basic.json'), 'w'), indent=1, ensure_ascii=False)
    for r in rows:
        print(f"{r['key']:7s} deg={r['deg']:2d} m={r['m']:2d} SOS={r['sos_ok']} witness: tau^{r['witness']['order']} coeff {r['witness']['coeff'][:25]} neg={r['witness']['negative']} | iso: {r['isolation']['status']}")

if __name__ == '__main__':
    main()
