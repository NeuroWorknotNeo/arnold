"""
widths.py -- «проекционные» ширины оврага вдоль собственных направлений гессиана на S_r.

Для направления e (единичный касательный вектор в точке дна omega) и знака sgn: точки w0(s) = cos s * omega + sin s * sgn*e
(геодезическая), n(s) -- единичная касательная нормаль к ней; профиль  P(s) = min_theta U(r (cos th w0(s) + sin th n(s))),
минимум по поперечному смещению (метод Ньютона с продолжением).  Ширина W = r * s*, где s* -- первый нуль P(s) - m/2
(m = U(omega) < 0).  Это размер множества {U < m/2} вдоль e с учётом изгиба оврага (прямая геодезическая сама по себе
выходит из изогнутого оврага; сравните §README).   [Эксперимент]

Использование: python widths.py ID [ID ...]  -- дописывает 'wid2' в out/ID.json.
"""
import sys, os, json, math
import numpy as np
from vlib import *
from curves import min_theta

OUT = os.path.join(HERE, 'out')


def profile_at(P, w, e, r, s, th0):
    c, sn = mp.cos(s), mp.sin(s)
    w0 = [c * w[i] + sn * e[i] for i in range(3)]
    t = [-sn * w[i] + c * e[i] for i in range(3)]
    n = unit(cross(w0, t))
    best = None
    starts = [th0, mp.mpf(0)]
    for pw in (1, 2):
        starts += [r ** pw, -r ** pw]
    thmax = mp.mpf('0.6') * s + 20 * r     # дно изогнуто умеренно: |theta| <= 0.6 s (не перескакиваем в другие овраги)
    for s0 in starts:
        res = min_theta(P, w0, n, r, s0)
        if res is None or abs(res[0]) > thmax:
            continue
        if best is None or res[1] < best[1]:
            best = res
    return best


def half_width_profile(P, w, e, r, m, Hgii, sgn, f=mp.mpf('0.5')):
    target = m * (1 - f)    # уровень U = (1-f) m; f = 1/2 по умолчанию
    ee = [sgn * c for c in e]
    s_est = mp.sqrt(2 * f * abs(m) / abs(Hgii)) if Hgii > 0 else mp.mpf('1e-6')
    s_lo = mp.mpf(0)
    th = mp.mpf(0)
    s = s_est / 16
    ratio = mp.mpf('1.5')
    last = None
    while True:
        best = profile_at(P, w, ee, r, s, th * (s / s_lo) ** 2 if s_lo > 0 else th)
        if best is None or best[1] >= target:   # нет локального минимума по поперечному смещению = вне оврага
            break
        th, s_lo = best[0], s
        s *= ratio
        if s > mp.mpf('2.5'):
            return None
    s_hi = s
    for _ in range(40):
        mid = (s_lo + s_hi) / 2
        best = profile_at(P, w, ee, r, mid, th)
        if best is not None and best[1] < target:
            s_lo, th = mid, best[0]
        else:
            s_hi = mid
    return (s_lo + s_hi) / 2


def run(eid, nmax=4):
    cat = load_catalog()
    P = Pot(cat[eid]['U'])
    path = os.path.join(OUT, eid + '.json')
    d = json.load(open(path))
    for rec in d['radii']:
        r = mp.mpf(10) ** mp.mpf(rec['logr'])
        mglob = mp.mpf(rec['minima'][0]['m']) if rec['minima'] else None
        for k, it in enumerate(rec['minima'][:nmax]):
            if 'eigs' not in it:
                continue
            m = mp.mpf(it['m'])
            if m > 0.1 * mglob:    # только ветви глубже 10% от глобального минимума (m < 0)
                continue
            w = [mp.mpf(c) for c in it['w']]
            for e in it['eigs']:
                v = unit([mp.mpf(c) for c in e['dir']])
                # проекция v на касательную плоскость в w (на случай погрешности направления)
                dv = dot(v, w)
                v = unit([v[i] - dv * w[i] for i in range(3)])
                lam_ang = mp.mpf(e['lam']) * r ** 2
                if e.get('wid2') and None not in e['wid2']:
                    continue
                ws = []
                fl_ = mp.mpf('0.5')
                for sgn in (1, -1):
                    h = half_width_profile(P, w, v, r, m, lam_ang, sgn, fl_)
                    ws.append(None if h is None else mp.nstr(h * r, 12))
                if None in ws:        # слишком широкое дно: уровень U = 0.9 m
                    fl_ = mp.mpf('0.1')
                    ws = []
                    for sgn in (1, -1):
                        h = half_width_profile(P, w, v, r, m, lam_ang, sgn, fl_)
                        ws.append(None if h is None else mp.nstr(h * r, 12))
                e['wid2'] = ws
                e['wid2_f'] = float(fl_)
            # вырожденный гессиан (равные собственные значения): направления произвольны -> сканируем 12 углов
            l1, l2 = [mp.mpf(e['lam']) for e in it['eigs']]
            if abs(l1 - l2) < mp.mpf('1e-8') * max(abs(l1), abs(l2)):
                vs = []
                for e in it['eigs']:
                    v = unit([mp.mpf(c) for c in e['dir']])
                    dv = dot(v, w)
                    vs.append(unit([v[i] - dv * w[i] for i in range(3)]))
                scan = []
                lam_ang = l1 * r ** 2
                for j in range(8):
                    al = mp.pi * j / 8
                    v = [mp.cos(al) * vs[0][i] + mp.sin(al) * vs[1][i] for i in range(3)]
                    ws, wst = [], []
                    for sgn in (1, -1):
                        h = half_width_profile(P, w, v, r, m, lam_ang, sgn)
                        ws.append(None if h is None else float(h * r))
                        h2 = half_width(P, w, v, r, m, lam_ang, sgn)
                        wst.append(None if h2 is None else float(h2 * r))
                    scan.append(dict(ang=float(al), wid=ws, wids=wst))
                it['scan'] = scan
        json.dump(d, open(path, 'w'), indent=1)
        print(eid, 'r=', rec['r'], 'done', flush=True)


if __name__ == '__main__':
    for a in sys.argv[1:]:
        run(a)
