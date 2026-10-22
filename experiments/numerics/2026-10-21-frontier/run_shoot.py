"""
run_shoot.py -- стрельба назад от дна оврага (как valleys/traj_run.py) для примера ID.  [Эксперимент]
Для r0_k -> 0: q0 = r0 * w(r0) (глубочайший минимум на S_{r0}, ветвь, ближайшая к дну при r = 1e-6), скорость вдоль касательной к
кривой дна, |v| = sqrt(-2 U(q0)) (E = 0); обращённый поток Йошида-6 (long double) до сферы |q| = sigma; состояния входа Z_k;
сходимость |Z_{k+1} - Z_k|; прямой прогон из последнего Z_k (наклон d log r / d log t против -2/(beta-2)).
usage: python run_shoot.py ID [--sigma 0.05] [--f 0.6,0.4,...] [--branch k]
seed: детерминированно (случайных чисел нет, кроме выбора старта в flib.sigma_samples: SEED = 20261021)
"""
import sys, os, json, time, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flib import *
sys.path.insert(0, HERE)      # использовать локальную копию traj_c.py (сборка в ./build)
import traj_c

TRAJ = os.path.join(HERE, 'traj')
os.makedirs(TRAJ, exist_ok=True)
FACT = [0.6, 0.4, 0.25, 0.15, 0.09, 0.055, 0.033, 0.02, 0.012, 0.007]


def load(eid):
    return json.load(open(os.path.join(HERE, 'out', eid + '.json')))['radii']


def fit_beta(recs, k=5):
    """beta и a0 по последним k радиусам глубочайшего минимума"""
    xs, ys = [], []
    for rec in recs[-k:]:
        xs.append(math.log10(float(rec['r'])))
        ys.append(math.log10(-float(rec['minima'][0]['m'])))
    A = np.vstack([xs, np.ones(len(xs))]).T
    sl, ic = np.linalg.lstsq(A, np.array(ys), rcond=None)[0]
    return sl, 10 ** (ic + sl * xs[-1]) / (10 ** xs[-1]) ** sl


def bottom(P, recs, r0, ref):
    rec = min(recs, key=lambda t: abs(math.log10(r0) - t['logr']))
    cand = sorted(rec['minima'], key=lambda it: np.linalg.norm(np.array([float(c) for c in it['w']]) - ref))
    w0 = [mp.mpf(c) for c in cand[0]['w']]
    r0m = mp.mpf(r0)
    # продолжение к r0 несколькими шагами по r (от сохранённого радиуса)
    r_s = mp.mpf(10) ** mp.mpf(rec['logr'])
    n = 12
    w = w0
    for k in range(1, n + 1):
        r_k = r_s * (r0m / r_s) ** (mp.mpf(k) / n)
        w, U, gt, Ht, ee, ok = newton_min(P, w, r_k, maxit=400)
        if not (ok and U < 0):
            raise RuntimeError(f'newton failed r0={r0} k={k}')
    pts = []
    for fct in (mp.mpf('1.001'), mp.mpf('0.999')):
        w1, U1, gt, Ht, ee, ok = newton_min(P, w, r0m * fct, maxit=400)
        pts.append([r0m * fct * c for c in w1])
    t = unit([pts[0][i] - pts[1][i] for i in range(3)])
    q0 = [r0m * c for c in w]
    if dot(t, q0) < 0:
        t = [-c for c in t]
    return w, U, t


def main(eid, sigma=0.05, fact=FACT, eps=0.1, nmax=4e9, branch=0):
    e = cat()[eid]
    P = Pot(e['U'])
    recs = load(eid)
    beta, a0 = fit_beta(recs)
    last = recs[-1]['minima']
    ref = np.array([float(c) for c in last[branch]['w']])
    lib = traj_c.build(e['U'], f'{eid}_{os.getpid()}')
    tag = eid + ('' if branch == 0 else f'_b{branch}')
    lines = []

    def pr(s):
        print(s, flush=True)
        lines.append(s)
    pr(f"{tag}: beta_fit={beta:.4f}, a0={a0:.5g}, sigma={sigma}, eps={eps}, ветвь w(1e-6)={np.round(ref, 8).tolist()}")
    entries, recs_out = [], []
    for f in fact:
        r0 = sigma * f
        t0 = time.time()
        try:
            w, U, tau = bottom(P, recs, r0, ref)
        except Exception as ex:
            pr(f"  r0={r0:.4g}: {ex}")
            continue
        q0 = np.array([float(r0 * c) for c in w])
        speed = float(mp.sqrt(-2 * U))
        v0 = speed * np.array([float(c) for c in tau])
        out, _ = traj_c.integrate(lib, q0, v0, 0, sigma, 1e200, eps, a0, beta, nmax)
        status = int(out[9])
        rec = dict(r0=r0, T=out[6], drift=out[7], E0=out[12], steps=out[8], status=status, q=out[0:3].tolist(),
                   v=out[3:6].tolist(), rfinal=out[10], wall=time.time() - t0)
        recs_out.append(rec)
        pr(f"  r0={r0:.4g}: status={status} T={out[6]:.4g} steps={out[8]:.3g} max|E-E0|/(a r^b)={out[7]:.2e} "
           f"entry q={np.round(out[0:3], 8).tolist()} v={np.array2string(out[3:6], precision=6)} [{rec['wall']:.0f}s]")
        if status == 0:
            entries.append(np.concatenate([out[0:3], -out[3:6]]))
    verdict = {}
    if len(entries) >= 3:
        d = [float(np.linalg.norm(entries[k + 1] - entries[k])) for k in range(len(entries) - 1)]
        rat = [d[k + 1] / d[k] for k in range(len(d) - 1) if d[k] > 0]
        pr("  |Z_{k+1}-Z_k|: " + ", ".join(f"{x:.2e}" for x in d))
        pr("  ratios: " + ", ".join(f"{x:.2f}" for x in rat))
        gm = float(np.exp(np.mean(np.log(np.maximum(rat[-3:], 1e-300))))) if len(rat) >= 3 else None
        r0s = [r['r0'] for r in recs_out if r['status'] == 0]
        pfit = None
        if len(d) >= 4:
            xs = np.log([math.sqrt(r0s[k] * r0s[k + 1]) for k in range(len(d))])[-5:]
            ys = np.log(np.maximum(d, 1e-300))[-5:]
            pfit = float(np.polyfit(xs, ys, 1)[0])
        verdict.update(p_fit=pfit)
        pr(f"  степенной показатель сходимости |Z_(k+1)-Z_k| ~ r0^p: p = {pfit}")
        verdict.update(entry_dists=d, ratios=rat, gm_last3=gm, d_last=d[-1],
                       entries_converge=bool((pfit is not None and pfit > 0.1 and d[-1] < d[0] / 10) or d[-1] < 1e-12))
    # прямой прогон из последнего входа
    if entries and '--nofwd' not in sys.argv:
        Z = entries[-1]
        r_stop = sigma * fact[-1] / 4
        Tlast = recs_out[-1]['T']
        out, rec = traj_c.integrate(lib, Z[:3], Z[3:], 1, r_stop, 3 * Tlast, eps, a0, beta, nmax, nrec=60, t1=Tlast / 3000, rescape=2 * sigma)
        pr(f"  прямой прогон: status={int(out[9])}, T={out[6]:.4g}, r_final={out[10]:.4g}, max|E-E0|/(a r^b)={out[7]:.2e}")
        rows = [dict(t=row[0], r=row[1], U=row[2], E=row[3], v=row[4]) for row in rec]
        # локальный наклон d log r / d log t на последней трети записей
        sl = None
        good = [rw for rw in rows if abs(rw['E']) < 1e-3]          # только там, где дрейф энергии мал
        if len(good) > 12:
            ts = np.log([rw['t'] for rw in good[len(good) // 2:]])
            rs = np.log([rw['r'] for rw in good[len(good) // 2:]])
            sl = float(np.polyfit(ts, rs, 1)[0])
        verdict.update(fwd_status=int(out[9]), fwd_slope=sl, fwd_slope_pred=-2 / (beta - 2), fwd_r_last=rows[-1]['r'] if rows else None,
                       fwd_drift=out[7])
        for rw in rows[::6]:
            pr(f"   t={rw['t']:.4g} r={rw['r']:.5g} U/(a r^b)={rw['U']:.4f} dE/(a r^b)={rw['E']:.2e}")
    pr('  verdict: ' + json.dumps(verdict))
    json.dump(dict(id=eid, beta=beta, a0=a0, sigma=sigma, recs=recs_out, verdict=verdict), open(os.path.join(TRAJ, tag + '.json'), 'w'), indent=1)
    open(os.path.join(TRAJ, tag + '.txt'), 'w').write("\n".join(lines))


if __name__ == '__main__':
    eid = sys.argv[1]
    sigma, fact, branch = 0.05, FACT, 0
    for i, a in enumerate(sys.argv):
        if a == '--sigma':
            sigma = float(sys.argv[i + 1])
        if a == '--f':
            fact = [float(t) for t in sys.argv[i + 1].split(',')]
        if a == '--branch':
            branch = int(sys.argv[i + 1])
    main(eid, sigma, fact, branch=branch)
