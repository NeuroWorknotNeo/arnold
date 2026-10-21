#!/usr/bin/env python3
"""run_zoo.py -- run the exact analysis for every catalogue entry, write results.json, table.md, matrix.md, details.md.

usage:  python run_zoo.py [id ...]          (no seed: everything is deterministic)
"""
import sys, json, time
import sympy as sp
import analyze, catalog

SHORT = ['Lyapunov', 'KP82', 'Koz86', 'FGT08*', 'Pa20-T3', 'QH-linear', 'Pa20-T6', 'Bu25-P1.2', 'Bu25-C1.4',
         'ThmB', 'N13', 'N13*', 'SYM']


def shorten(s, n=60):
    s = str(s)
    return s if len(s) <= n else s[:n - 1] + '…'


def witness_text(w):
    if not w:
        return 'не найден'
    if w['kind'] == 'ray':
        return f"луч w={tuple(w['w'])}: U(tw) = {w['coeff']}·t^{w['order']} + …"
    return f"кривая γ(τ)=({', '.join(shorten(c, 38) for c in w['curve'])}): U(γ) = {w['coeff']}·τ^{w['order']} + …"


def iso_text(i):
    mu = f"μ={i['mu']} (Singular, локальный базис, конечен ⇒ изолирована и над ℂ)" if i['mu'] is not None else \
        'μ=∞ (над ℂ не изолирована)'
    cert = f"над ℝ: насыщение J:p^∞, p={i['p']}, K⊄𝔪 ✓" if i['cert'] else 'над ℝ НЕ сертифицирована'
    return mu + '; ' + cert


def applicable(res):
    out = []
    for k in SHORT:
        st = res['criteria'][k]['status']
        if st == 'yes':
            out.append(k)
        elif st == 'maybe':
            out.append(k + '?')
    return out


def main():
    ids = sys.argv[1:]
    results = []
    t0 = time.time()
    for e in catalog.CATALOG:
        if ids and e['id'] not in ids:
            continue
        print('...', e['id'], flush=True)
        r = analyze.analyze(e)
        r['why'] = e.get('why', '')
        r['U_src'] = e['U'] if len(e['U']) < 200 else 'U_13(Rq) (см. catalog.py)'
        results.append(r)
        print('    done in', r['seconds'], 's; covered_known', r['covered_known'], 'ours', r['covered_ours'],
              'soft', r['covered_soft'], 'NOT_COVERED', r['not_covered'], flush=True)
    # ---- calibration assertions
    by = {r['id']: r for r in results}
    if 'K1' in by:
        assert 'QH-linear' in by['K1']['covered_known'], 'calibration K1 failed'
    if 'K2' in by:
        assert by['K2']['covered_known'] == [] and by['K2']['covered_ours'] == ['N13'], 'calibration K2 failed'
    # ---- json
    slim = []
    for r in results:
        r2 = dict(r)
        r2['isolation'] = {k: v for k, v in r['isolation'].items() if k != 'comps'}
        r2['isolation']['comps'] = [shorten(c, 160) for c in r['isolation']['comps']]
        r2.pop('T6data', None)
        slim.append(r2)
    json.dump(slim, open('results.json', 'w'), indent=1, ensure_ascii=False, default=str)
    # ---- main table
    lines = ['| № | Пример U | Изолированность (метод) | Не минимум (свидетельство) | Применимые критерии | Статус |',
             '|---|---|---|---|---|---|']
    for r in results:
        app = applicable(r)
        if r['not_covered']:
            status = '**НЕ ПОКРЫТ**'
        elif r['not_covered_by_proved']:
            status = 'только условные/эскизные: ' + ', '.join(r['covered_soft'])
        else:
            status = 'покрыт'
        lines.append(f"| {r['id']} | {r['name']}<br>`{shorten(r['U_src'], 110)}` | {iso_text(r['isolation'])} | "
                     f"{witness_text(r['witness'])} | {', '.join(app) if app else '—'} | {status} |")
    open('table.md', 'w').write('\n'.join(lines) + '\n')
    # ---- matrix
    sym = {'yes': '✓', 'no': '·', 'maybe': '?'}
    m = ['| № | ' + ' | '.join(SHORT) + ' |', '|---|' + '---|' * len(SHORT)]
    for r in results:
        m.append(f"| {r['id']} | " + ' | '.join(sym[r['criteria'][k]['status']] for k in SHORT) + ' |')
    open('matrix.md', 'w').write('\n'.join(m) + '\n')
    # ---- details
    d = []
    for r in results:
        d.append(f"## {r['id']}: {r['name']}\n")
        d.append(f"- U = `{r['U']}`")
        d.append(f"- why: {r['why']}")
        d.append(f"- lowest degree m = {r['m']}; forms: " + '; '.join(f'u_{k}={shorten(v, 90)}' for k, v in r['forms'].items()))
        d.append(f"- isolation: {iso_text(r['isolation'])}; components of V(grad U): {r['isolation']['comps']}")
        d.append(f"- not a minimum: {witness_text(r['witness'])}")
        if r['core']:
            c = r['core']
            d.append(f"- hard core: u_m>=0 by explicit SOS: {c['sos_ok']}; zero set complete over C: {c['sigma_complete_C']}; "
                     f"B1={c['B1']} {c['B1_notes']}; B2={c['B2']} {c['B2_notes']}; B3={c['B3']} {c['B3_notes']}; l2={c['l2']}")
        if r.get('gutter'):
            d.append(f"- naive restriction to the conic gutter (first form not vanishing identically on it): {r['gutter']['terms']}")
        d.append('- criteria:')
        for k, v in r['criteria'].items():
            d.append(f"  - **{k}**: {v['status']} — {v['why']}")
        d.append(f"- invariant planes/lines of the dynamics (exact search): {r['invariant_subspaces']}")
        d.append(f"- covered by known: {r['covered_known']}; ours: {r['covered_ours']}; soft: {r['covered_soft']}; "
                 f"NOT COVERED: {r['not_covered']}; ({r['seconds']} s)\n")
    open('details.md', 'w').write('\n'.join(d))
    print('total seconds', round(time.time() - t0, 1))
    print('examples', len(results), 'not covered at all', sum(r['not_covered'] for r in results),
          'not covered by proved', sum(r['not_covered_by_proved'] for r in results))


if __name__ == '__main__':
    main()
