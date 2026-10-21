"""
widths_scan.py -- скан направлений для вырожденного гессиана на ОДНОМ радиусе (параллелизуется по радиусам):
python widths_scan.py ID logr [Nang]   ->  out/scan_ID_<logr>.json ; затем  python widths_scan.py --merge ID.
Прямая и профильная ширины по Nang углам в [0, pi) в базисе собственных направлений. [Эксперимент]
"""
import sys, os, json
from vlib import *
from widths import half_width_profile

OUT = os.path.join(HERE, 'out')


def scan_one(eid, logr, nang=8):
    cat = load_catalog()
    P = Pot(cat[eid]['U'])
    d = json.load(open(os.path.join(OUT, eid + '.json')))
    rec = [x for x in d['radii'] if abs(x['logr'] - logr) < 1e-9][0]
    it = rec['minima'][0]
    r = mp.mpf(10) ** mp.mpf(rec['logr'])
    m = mp.mpf(it['m'])
    w = [mp.mpf(c) for c in it['w']]
    vs = []
    for e in it['eigs']:
        v = unit([mp.mpf(c) for c in e['dir']])
        dv = dot(v, w)
        vs.append(unit([v[i] - dv * w[i] for i in range(3)]))
    lam_ang = mp.mpf(it['eigs'][0]['lam']) * r ** 2
    scan = []
    for j in range(nang):
        al = mp.pi * j / nang
        v = [mp.cos(al) * vs[0][i] + mp.sin(al) * vs[1][i] for i in range(3)]
        ws, wst = [], []
        for sgn in (1, -1):
            h = half_width_profile(P, w, v, r, m, lam_ang, sgn)
            ws.append(None if h is None else float(h * r))
            h2 = half_width(P, w, v, r, m, lam_ang, sgn)
            wst.append(None if h2 is None else float(h2 * r))
        scan.append(dict(ang=float(al), wid=ws, wids=wst))
    json.dump(dict(logr=logr, scan=scan), open(os.path.join(OUT, f'scan_{eid}_{logr}.json'), 'w'))
    print(eid, logr, 'done', flush=True)


def merge(eid):
    path = os.path.join(OUT, eid + '.json')
    d = json.load(open(path))
    for rec in d['radii']:
        f = os.path.join(OUT, f"scan_{eid}_{float(rec['logr'])}.json")
        if os.path.exists(f):
            rec['minima'][0]['scan'] = json.load(open(f))['scan']
    json.dump(d, open(path, 'w'), indent=1)


if __name__ == '__main__':
    if sys.argv[1] == '--merge':
        merge(sys.argv[2])
    else:
        scan_one(sys.argv[1], float(sys.argv[2]), int(sys.argv[3]) if len(sys.argv) > 3 else 8)
