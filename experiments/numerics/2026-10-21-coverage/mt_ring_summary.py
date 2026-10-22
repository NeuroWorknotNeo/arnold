"""mt_ring_summary.py -- разбор логов mt_check_ring.py (logs/mt_ring_D*.log) в сводку: min по r отношений (F), (E), и минимум на стенке / delta."""
import re, json, os, glob
HERE = os.path.dirname(os.path.abspath(__file__))
out = {}
for f in sorted(glob.glob(os.path.join(HERE, 'logs', 'mt_ring_D*.log'))):
    key = 'f:' + os.path.basename(f)[8:10]
    rows = []
    for l in open(f):
        m = re.search(r'r=\s*([0-9.e+-]+)\s+\(F\) minW/r\^\(1/3\)=\s*([-0-9.]+)\s+\(W\) min_wall=([0-9.e+-]+) \(delta=([0-9.e+-]+)\)\s+\(E\)k->0:\s*([-0-9.]+)\s+\(E\)k0:\s*([-0-9.]+)', l)
        if m:
            r, F, wall, delta, E0, Ek = m.groups()
            rows.append(dict(r=float(r), F_over_r13=float(F), wall_min=float(wall), delta=float(delta), E_k0plus_over_r13=float(E0), E_kappa0_over_r13=float(Ek)))
    out[key] = dict(rows=rows, min_F=min(r['F_over_r13'] for r in rows), min_E_k0plus=min(r['E_k0plus_over_r13'] for r in rows), min_E_kappa0=min(r['E_kappa0_over_r13'] for r in rows),
                    min_wall_over_delta=min(r['wall_min'] / r['delta'] for r in rows), n_r=len(rows))
    print(key, {k: v for k, v in out[key].items() if k != 'rows'})
json.dump(out, open(os.path.join(HERE, 'mt_ring_summary.json'), 'w'), indent=1)
