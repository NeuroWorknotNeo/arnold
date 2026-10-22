"""
known_criteria.py -- какие из реализованных в zoo опубликованных критериев применимы к примерам «границы» (точно, sympy/Singular):
Lyapunov (u_2<0), KP82 (u_m принимает отрицательные значения; u_m>=0 здесь по явной СКО), Koz86, QH-linear (квазиоднородность в линейных
координатах), Pa20-T6 (грань многогранника Ньютона без вещественных критических точек + хвост), SYM (инвариантные плоскости/прямые).
usage: python known_criteria.py [ID ...] -> known.json
"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '2026-10-21-zoo'))
import sympy as sp
import zoolib as zl
import criteria as cr
import fcat
from zoolib import P, parts


def main(ids):
    out = {}
    for e in fcat.CAT:
        if ids and e['id'] not in ids:
            continue
        if e['id'] == 'V3' and not ids:
            continue
        t0 = time.time()
        U = P(e['U'])
        pr = parts(U)
        C = {}
        C['Lyapunov'] = cr.lyapunov(pr)
        C['KP82'] = cr.kozlov_palamodov(pr, dict(sos_ok=True, ncomp=1))
        C['Koz86'] = cr.kozlov86(pr)
        C['QH-linear'] = cr.quasi_homog_linear(U, pr)
        try:
            t6, data = cr.pa20_T6(U)
            C['Pa20-T6'] = t6
        except Exception as ex:
            C['Pa20-T6'] = dict(status='err', why=repr(ex)[:150])
        out[e['id']] = {k: dict(status=v['status'], why=v['why'][:300]) for k, v in C.items()}
        print(e['id'], {k: v['status'] for k, v in C.items()}, round(time.time() - t0, 1), 's', flush=True)
    json.dump(out, open(os.path.join(HERE, 'known%s.json' % ('_' + '_'.join(ids) if ids else '')), 'w'), indent=1, ensure_ascii=False)


if __name__ == '__main__':
    main(sys.argv[1:])
