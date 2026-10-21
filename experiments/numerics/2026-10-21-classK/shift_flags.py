"""shift_flags.py -- where the shift eta* matters: compare G=g_j with the naive restriction u_j|Sigma (curves),
and b_1 = d_nu u_{m+1}|Sigma (first-order normal force).  [Experiment: symbolic, exact]"""
import json, sympy as sp
import comps
from comps import U, t, x, y, z, COMPS
from kfib import homog_parts
out = {}
for ex in [e for e in comps.ALL if e != 'T1']:
    r = json.load(open('out/%s.json' % ex))
    m = r['m']; parts = homog_parts(U[ex])
    for comp, cres in zip(COMPS[ex], r['components']):
        if comp[0] == 'curve' and cres.get('j'):
            _, name, p, nu, f = comp
            j = cres['j']
            lam = sp.sqrt(sp.factor(sum(c**2 for c in p))); lam = sp.simplify(lam)
            sub = {x: p[0], y: p[1], z: p[2]}
            uj = parts.get(j, 0)
            naive = sp.cancel(sp.expand(uj.subs(sub, simultaneous=True)) / lam**j) if uj != 0 else 0
            G = sp.sympify(cres['G'] if 'G' in cres else cres['G_value'], locals={'t': t})
            diff = sp.simplify(G - naive)
            um1 = parts.get(m + 1, 0)
            b1 = 0
            if um1 != 0:
                b1 = sp.simplify(sum(sp.diff(um1, v).subs(sub, simultaneous=True) * nu[i] for i, v in enumerate((x, y, z))))
            jn = None
            for k in sorted(parts):
                if k > m:
                    val = sp.simplify(sp.expand(parts[k].subs(sub, simultaneous=True)))
                    if val != 0:
                        jn = k
                        break
            out.setdefault(ex, {})[name] = dict(G_equals_naive=(diff == 0), b1_zero=(b1 == 0), j=j, j_naive=jn)
            print(ex, name, 'j=%d' % j, ' j_naive(first k>m with u_k|Sigma != 0)=%s' % jn, ' G == u_j|Sigma :', diff == 0, ' | b_1 = d_nu u_{m+1}|Sigma identically 0 :', b1 == 0)
json.dump(out, open('out/shift_flags.json', 'w'), indent=1)
