"""
run_profiles.py -- профильные функции g_i(s) = min_perp U(r pt)/|m| вдоль собственных направлений e_i (i=1,2) в единицах угловых
ширин A_i (из out/ID.json), s in {-2,-1,-0.5,0,0.5,1,2}; следуют за изогнутым дном (внутренний минимум по перпендикуляру).
Сравнение между радиусами: если g_i(s) сходятся, масштабы (A_i ~ r^{c_i-1}) согласованы и предельный профиль существует.  [Эксперимент]
usage: python run_profiles.py ID   ->  out/ID.prof.json
"""
import sys, os, json
from flib import *

SS = [-2, -1, -0.5, 0, 0.5, 1, 2]


def f2s(v, n=10):
    return mp.nstr(v, n)


def run(eid):
    e = cat()[eid]
    P = Pot(e['U'])
    d = json.load(open(os.path.join(HERE, 'out', eid + '.json')))['radii']
    out = []
    for rec in d:
        b = rec['minima'][0]
        if 'dirs' not in b or 'widths_angle' not in b:
            continue
        r = mp.mpf(10) ** mp.mpf(rec['logr'])
        w = [mp.mpf(c) for c in b['w']]
        v1 = [mp.mpf(c) for c in b['dirs'][0]]
        v2 = [mp.mpf(c) for c in b['dirs'][1]]
        m = mp.mpf(b['m'])
        W = b['widths_angle']
        A = []
        for row in W:
            vals = [mp.mpf(v) for v in row if v is not None]
            A.append(sum(vals) / len(vals) if vals else None)
        g = []
        for ax, (va, vb) in enumerate(((v1, v2), (v2, v1))):
            if A[ax] is None:
                g.append(None)
                continue
            row = []
            bprev = mp.mpf(0)
            for s in sorted(SS, key=lambda t: abs(t)):
                pass
            # идём от 0 наружу, чтобы внутренний минимум был непрерывным
            vals = {}
            for sg in (1, -1):
                bprev = mp.mpf(0)
                for s in [0, 0.5, 1, 2]:
                    a = sg * mp.mpf(s) * A[ax]
                    bn, Un = inner_min(P, r, w, va, vb, a, bprev, max(abs(bprev) * mp.mpf('0.05'), a * a, mp.mpf('1e-30')))
                    bprev = bn
                    vals[sg * s] = Un / abs(m)
            g.append([f2s(vals[s]) for s in SS])
        out.append(dict(logr=rec['logr'], A=[None if a is None else f2s(a) for a in A], g=g))
        print(eid, rec['logr'], flush=True)
    json.dump(out, open(os.path.join(HERE, 'out', eid + '.prof.json'), 'w'), indent=1)


if __name__ == '__main__':
    for a in sys.argv[1:]:
        run(a)
