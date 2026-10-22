"""iso_check.py -- точные проверки: изолированность 0 над R (насыщение J : p^inf, p положительно определённая квадрика,
Singular), число Милнора (локальный порядок), явный свидетель U<0 (точная арифметика), симметрии (точный перебор
инвариантных плоскостей/прямых из zoo).  [Эксперимент: точно]
usage: python iso_check.py [ID ...]  -> iso.json, iso.md
"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '2026-10-21-zoo'))
import sympy as sp
import zoolib as zl
import criteria as cr
import fcat
from zoolib import x, y, z, P, parts


def witness(U, w):
    if w[0] == 'ray':
        k, c = zl.ray_series(U, tuple(w[1]))
        return dict(kind='ray', w=list(w[1]), order=int(k), coeff=str(c), negative=bool(c < 0))
    k, c = zl.curve_witness(U, w[1])
    return dict(kind='curve', curve=list(w[1]), order=int(k), coeff=str(c), negative=bool(c < 0))


def main(ids):
    out = []
    for e in fcat.CAT:
        if ids and e['id'] not in ids:
            continue
        t0 = time.time()
        U = P(e['U'])
        pr = parts(U)
        m = min(pr)
        r = dict(id=e['id'], U=str(U), m=m, forms={k: str(v)[:120] for k, v in pr.items()}, degree=max(pr))
        J = zl.grad(U)
        r['grad0'] = all(g.subs({x: 0, y: 0, z: 0}) == 0 for g in J) and U.subs({x: 0, y: 0, z: 0}) == 0
        if os.environ.get('ISO_SKIP'):
            r['mu'] = 'skipped'
            r['cert'] = None
            r['p'] = 'skipped (степень слишком велика)'
        else:
          try:
            r['mu'] = sp_mu = None
            import sing
            mu = sing.local_milnor(U)
            r['mu'] = None if mu < 0 else mu
          except Exception as ex:
            r['mu'] = 'err ' + repr(ex)[:80]
          try:
            ok, p = zl.real_isolation_cert(J)
            r['cert'] = bool(ok)
            r['p'] = str(p)
          except Exception as ex:
            r['cert'] = None
            r['p'] = 'err ' + repr(ex)[:80]
        # u_m >= 0: сертификат СКО (если задан) или численная проверка на сетке
        import numpy as np
        um = sp.lambdify((x, y, z), pr[m], 'numpy')
        th = np.linspace(0, np.pi, 801)
        ph = np.linspace(0, 2 * np.pi, 1601)
        TH, PH = np.meshgrid(th, ph, indexing='ij')
        v = um(np.sin(TH) * np.cos(PH), np.sin(TH) * np.sin(PH), np.cos(TH)) + 0 * TH
        r['um_min_grid'] = float(v.min())
        try:
            r['witness'] = witness(U, e['witness'])
        except Exception as ex:
            r['witness'] = 'err ' + repr(ex)[:100]
        try:
            inv = cr.invariant_subspace_search(U)
            r['invariant'] = [dict(kind=v_['kind'], verdict=v_['verdict'], note=str(v_.get('note'))[:100]) for v_ in inv]
            r['inv_yes'] = [v_ for v_ in r['invariant'] if v_['verdict'] == 'yes']
        except Exception as ex:
            r['invariant'] = 'err ' + repr(ex)[:100]
        r['seconds'] = round(time.time() - t0, 1)
        print(e['id'], 'm=', m, 'deg', r['degree'], 'mu', r['mu'], 'cert', r['cert'], r['p'], 'um_min_grid', r['um_min_grid'],
              'witness', r['witness'] if isinstance(r['witness'], str) else (r['witness']['order'], r['witness']['coeff']),
              'inv', r.get('invariant') if isinstance(r.get('invariant'), str) else [(v_['kind'], v_['verdict']) for v_ in r['invariant']],
              r['seconds'], 's', flush=True)
        out.append(r)
    json.dump(out, open(os.path.join(HERE, 'iso.json' if not ids else 'iso_%s.json' % '_'.join(ids)), 'w'), indent=1, ensure_ascii=False)


if __name__ == '__main__':
    main(sys.argv[1:])
