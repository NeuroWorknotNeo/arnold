"""
check_plane.py -- прямая проверка «плоского» гессиана H_plane вдоль мягкого направления (c = 1):
срез плоскостью <q, omega_inf> = X (X = 1e-4), профиль P(y) = min_eta U(X omega + y e + eta nu), H = P''(0) / X^(beta-2);
сравнение с формулой H = lam_soft/r^(beta-2) - beta*a (lam_soft -- гессиан на сфере).   [Эксперимент]
"""
import json, os, sys
from vlib import *
from curves import min_theta

cat = load_catalog()
beta_a = json.load(open(os.path.join(HERE, 'summary.json')))
out = []
for eid in sys.argv[1:]:
    P = Pot(cat[eid]['U'])
    d = json.load(open(os.path.join(HERE, 'out', eid + '.json')))
    rec = d['radii'][-1]
    it = rec['minima'][0]
    w = unit([mp.mpf(c) for c in it['w']])
    eg = sorted(it['eigs'], key=lambda e: float(e['lam']))
    e = unit([mp.mpf(c) for c in eg[0]['dir']])
    dv = dot(e, w)
    e = unit([e[i] - dv * w[i] for i in range(3)])
    nu = unit(cross(w, e))
    beta = beta_a[eid]['beta_round']
    a = abs(beta_a[eid]['a_coef'][-1])
    X = mp.mpf('1e-4')
    def prof(y):
        # минимум по eta: одномерный Ньютон по смещению в направлении nu из точки q0 = X w + y e
        q0 = [X * w[i] + y * e[i] for i in range(3)]
        eta = mp.mpf(0)
        best = None
        for start in [mp.mpf(0), X ** 3, -X ** 3, X ** 2 / 10, -X ** 2 / 10, X ** 2 * 10, -X ** 2 * 10]:
            eta = start
            for _ in range(60):
                q = [q0[i] + eta * nu[i] for i in range(3)]
                U, g, H = P.full(q)
                d1 = dot(g, nu)
                d2 = sum(nu[a_] * H[a_][b_] * nu[b_] for a_ in range(3) for b_ in range(3))
                if d2 <= 0:
                    break
                st = -d1 / d2
                eta += st
                if abs(st) < mp.mpf(10) ** (-45) * X:
                    break
            q = [q0[i] + eta * nu[i] for i in range(3)]
            U = P.val(q)
            if d2 > 0 and (best is None or U < best):
                best = U
        return best
    res = []
    for hh in (mp.mpf('1e-3'), mp.mpf('3e-4')):
        h = hh * X
        P0, Pp, Pm = prof(mp.mpf(0)), prof(h), prof(-h)
        H = (Pp + Pm - 2 * P0) / h ** 2 / X ** (beta - 2)
        res.append(H)
    lam = mp.mpf(eg[0]['lam'])
    r = mp.mpf(10) ** mp.mpf(rec['logr'])
    pred = lam / r ** (beta - 2) - beta * a
    line = f"{eid}: H_plane(direct) = {mp.nstr(res[0], 8)} (h=1e-3 X), {mp.nstr(res[1], 8)} (h=3e-4 X); formula lam/r^(b-2) - beta a = {mp.nstr(pred, 8)}"
    print(line, flush=True)
    out.append(line)
open(os.path.join(HERE, 'check_plane.txt'), 'w').write("\n".join(out))
