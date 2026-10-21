"""
traj_run.py -- «стрельба назад» от дна оврага с энергией 0 (как в experiments/prover/gt3/ex13_numerics.py, часть 3).  [Эксперимент]

Для радиусов r0_k -> 0: берём точку дна q0 = r0 * omega(r0) (глубочайший минимум U на S_{r0}), скорость вдоль касательной к дну
(направление оттока), |v| = sqrt(-2U(q0)) (энергия E = 0), интегрируем ПОТОК с обращённой скоростью (то есть назад по времени)
симплектической схемой Йошида-6 (long double) до сферы |q| = SIGMA. Получаем состояния входа Z_k на сфере. Если Z_k сходятся
при k -> infinity, предельное состояние Z_inf даёт траекторию, которая вперёд по времени идёт к 0 (идея доказательства
теоремы A из notes/prover/2026-10-21-gt3.md); затем прямой прогон из Z_inf (насколько он следует предсказанию
r(t) = (SIGMA^{-(b-2)/2} + (b-2)/2 sqrt(2a) t)^{-2/(b-2)}, b = beta).

Использование: python traj_run.py ID [--sigma 0.05] [--f 0.6,0.4,...]
Вывод: traj/ID.json, traj/ID.txt
"""
import sys, os, json, time, math
import numpy as np
from vlib import *
import run_valleys as RV
import traj_c

TRAJ = os.path.join(HERE, 'traj')
os.makedirs(TRAJ, exist_ok=True)
FACT = [0.6, 0.4, 0.25, 0.15, 0.09, 0.055, 0.033, 0.02]


def bottom(P, comps, ptsS, r0, rng, prev=None, seedinfo=None):
    """дно (ветвь, ближайшая к ref) на S_{r0} и касательная к кривой дна (конечные разности по r).
    seedinfo = (recs, a0, beta, ref): recs -- сохранённые минимумы out/ID.json; ref -- направление ветви при r = 1e-6."""
    w = None
    mins = None
    recs_, a0_, beta_, ref = seedinfo
    # быстрый путь: старт Ньютона из ближайшего по радиусу сохранённого дна той же ветви; проверка по a0 r^beta
    rec = min(recs_, key=lambda t: abs(math.log10(float(r0)) - t['logr']))
    cand_ = sorted(rec['minima'], key=lambda it_: np.linalg.norm(np.array([float(c) for c in it_['w']]) - ref))
    w0 = [mp.mpf(c) for c in cand_[0]['w']]
    w1_, U1_, gt_, Ht_, ee_, ok_ = newton_min(P, w0, r0, maxit=2000)
    if ok_ and U1_ < 0 and abs(float(U1_) / (-a0_ * float(r0) ** beta_) - 1) < 0.2:
        w, U = w1_, U1_
    if w is None:
        mins = RV.minima_at(P, comps, ptsS, r0, -9, rng, [] if prev is None else [prev])
        mins.sort(key=lambda t_: np.linalg.norm(np.array([float(c) for c in t_[0]]) - ref))
        w, U = mins[0][0], mins[0][1]
    pts = []
    for fct in (mp.mpf('1.001'), mp.mpf('0.999')):
        r1 = r0 * fct
        w1, U1, gt, Ht, ee, ok = newton_min(P, w, r1, maxit=200)
        pts.append([r1 * c for c in w1])
    t = unit([pts[0][i] - pts[1][i] for i in range(3)])
    q0 = [r0 * c for c in w]
    if dot(t, q0) < 0:
        t = [-c for c in t]
    return w, U, t, mins


def main(eid, sigma=0.05, fact=FACT, eps=0.1, nmax=4e9, orbit=0):
    cat = load_catalog()
    e = cat[eid]
    P = Pot(e['U'])
    rng = np.random.default_rng(RV.SEED)
    comps, ptsS = RV.setup_sigma(e)
    lib = traj_c.build(e['U'], f'{eid}_{os.getpid()}')
    import val_analyze as analyze
    summ = analyze.analyze(eid)
    beta = summ['beta_round']
    orb = summ['orbits_last'][orbit]
    a0 = abs(summ['a_coef'][-1]) * orb['ratio']          # коэффициент глубины данной ветви
    ref = np.array(orb['w'])
    recs_all = json.load(open(os.path.join(HERE, 'out', eid + '.json')))['radii']
    tag = eid + ('' if orbit == 0 else f'_o{orbit}')
    lines = []

    def pr(s):
        print(s, flush=True)
        lines.append(s)
    pr(f"{tag}: beta={beta}, a0={a0:.6g}, sigma={sigma}, eps={eps}, ветвь omega(1e-6)={np.round(ref, 6).tolist()}")
    entries = []
    recs = []
    for f in fact:
        r0 = sigma * f
        t0 = time.time()
        w, U, tau, mins = bottom(P, comps, ptsS, mp.mpf(r0), rng, None, (recs_all, a0, beta, ref))
        q0 = np.array([float(r0 * c) for c in w])
        speed = float(mp.sqrt(-2 * U))
        v0 = speed * np.array([float(c) for c in tau])      # поток с обращённой скоростью: сначала r растёт
        out, _ = traj_c.integrate(lib, q0, v0, 0, sigma, 1e30, eps, a0, beta, nmax)
        status = int(out[9])
        rec = dict(r0=r0, T=out[6], drift=out[7], E0=out[12], steps=out[8], status=status, q=out[0:3].tolist(),
                   v=out[3:6].tolist(), rfinal=out[10], wall=time.time() - t0)
        recs.append(rec)
        pr(f"  r0={r0:.4g}: status={status} T={out[6]:.4g} steps={out[8]:.3g} max|E-E0|/(a r^b)={out[7]:.2e} E0/(a r0^b)={out[12]:.1e} "
           f"entry q={np.round(out[0:3], 8).tolist()} v={np.array2string(out[3:6], precision=6)}  [{rec['wall']:.0f}s]")
        if status == 0:
            entries.append(np.concatenate([out[0:3], -out[3:6]]))   # реальное состояние: скорость обращена
    verdict = dict()
    if len(entries) >= 3:
        d = [float(np.linalg.norm(entries[k + 1] - entries[k])) for k in range(len(entries) - 1)]
        dq = [float(np.linalg.norm(entries[k + 1][:3] - entries[k][:3])) for k in range(len(entries) - 1)]
        dv = [float(np.linalg.norm(entries[k + 1][3:] - entries[k][3:])) for k in range(len(entries) - 1)]
        pr("  |Z_{k+1} - Z_k| (q,v): " + ", ".join(f"{x:.2e}" for x in d))
        pr("    q-part: " + ", ".join(f"{x:.2e}" for x in dq))
        pr("    v-part: " + ", ".join(f"{x:.2e}" for x in dv))
        rat = [d[k + 1] / d[k] for k in range(len(d) - 1) if d[k] > 0]
        pr("  ratios d_{k+1}/d_k: " + ", ".join(f"{x:.2f}" for x in rat))
        verdict['entry_dists'] = d
        verdict['ratios'] = rat
        gm = float(np.exp(np.mean(np.log(np.maximum(rat[-3:], 1e-300))))) if len(rat) >= 3 else None
        verdict['gm_last3'] = gm
        verdict['entries_converge'] = bool((gm is not None and gm < 0.85) or d[-1] < 1e-12)
        verdict['d_last'] = d[-1]
    # прямой прогон из последнего входа
    fwd = None
    if entries:
        Z = entries[-1]
        r_stop = sigma * fact[-1] / 4
        Tlast = recs[-1]['T']
        out, rec = traj_c.integrate(lib, Z[:3], Z[3:], 1, r_stop, 3 * Tlast, eps, a0, beta, nmax, nrec=60,
                                    t1=Tlast / 3000, rescape=2 * sigma)
        pr(f"  прямой прогон из Z_last: status={int(out[9])}, T={out[6]:.4g}, r_final={out[10]:.4g}, "
           f"max|E-E0|/(a r^b)={out[7]:.2e}, E0/(a r_start^b)={out[12]:.1e}")
        c = (beta - 2) / 2 * math.sqrt(2 * a0)
        pr("     t        r        r_pred      U/(a r^b)   (E-E0)/(a r^b)  |v|/sqrt(a r^b)")
        rows = []
        for row in rec:
            tt, rr = row[0], row[1]
            pred = (sigma ** (-(beta - 2) / 2) + c * tt) ** (-2 / (beta - 2))
            rows.append(dict(t=tt, r=rr, pred=pred, U=row[2], E=row[3], v=row[4]))
        for rw in rows[::4]:
            pr(f"  {rw['t']:10.4g} {rw['r']:.5g} {rw['pred']:.5g}  {rw['U']: .4f}  {rw['E']: .2e}  {rw['v']:.4f}")
        fwd = dict(status=int(out[9]), T=out[6], rfinal=out[10], drift=out[7], E0=out[12], rows=rows)
        # наименьший r, до которого r(t) следует предсказанию r_pred (±5%) и U/(a r^b) ~ -1 (±5%)
        rmin_follow = None
        for rw in rows:
            if abs(rw['r'] / rw['pred'] - 1) < 0.05 and abs(rw['U'] + 1) < 0.05:
                rmin_follow = rw['r']
            else:
                break
        verdict['fwd_rmin_follow'] = rmin_follow
        verdict['fwd_r_last'] = rows[-1]['r']
        verdict['fwd_status'] = fwd['status']
        verdict['fwd_floor_r'] = sigma * (1e-16) ** (1.0 / beta)   # оценка порога, где округление данных (double) мешает
    pr("  verdict: " + json.dumps(verdict))
    json.dump(dict(id=eid, orbit=orbit, sigma=sigma, beta=beta, a0=a0, eps=eps, recs=recs, fwd=fwd, verdict=verdict),
              open(os.path.join(TRAJ, tag + '.json'), 'w'), indent=1)
    open(os.path.join(TRAJ, tag + '.txt'), 'w').write("\n".join(lines))


if __name__ == '__main__':
    eid = sys.argv[1]
    sigma = 0.05
    fact = FACT
    orbit = 0
    for i, a in enumerate(sys.argv):
        if a == '--sigma':
            sigma = float(sys.argv[i + 1])
        if a == '--f':
            fact = [float(t) for t in sys.argv[i + 1].split(',')]
        if a == '--orbit':
            orbit = int(sys.argv[i + 1])
    main(eid, sigma, fact, orbit=orbit)
