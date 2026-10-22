"""sigma.py -- строение нулевого множества Sigma = {u_m = 0} ∩ S^2 младшей формы, точно (Singular над Q + sympy).
Для каждого примера:
  * компоненты Sigma (простые идеалы radical(<p_j>)): точки (аффинная размерность 1) и конусы над кривыми (размерность 2);
  * для кривых: порождающая форма f, гладкость конуса ((f, grad f) m-примарен?), особые прямые, кратность f в u_m (u_m = f^k g),
    нули g на кривой (точки смены нормальной кратности), вещественность;
  * для точек: гессиан D^2 u_m(w) на w^perp (точно, ранг, положительная определённость);
  * пересечения компонент (идеал (f_i, f_j), длина).
[Эксперимент: точный]. usage: python sigma.py [KEY ...]  -> sigma.json"""
import sys, json, os, re, itertools
import sympy as sp
from exlist import EXS, BY, HERE, NUM, x, y, z, LOC
import sing

X3 = (x, y, z)
def S(e):
    return sing.to_sing(e)

def sing_comps(gens):
    """minAssGTZ(radical)  -> list of (dim, [gens as sympy])"""
    g = ','.join(S(p) for p in gens)
    out = sing.run(sing.HEAD + f'''ring r=0,(x,y,z),dp; ideal J={g}; list L=minAssGTZ(J); int i; ideal T;
    for(i=1;i<=size(L);i++){{ T=std(L[i]); print("COMP dim=" + string(dim(T)) + " : " + string(T)); }}''')
    res = []
    for l in out.splitlines():
        m = re.match(r'COMP dim=(\d+) : (.*)', l)
        if m:
            d = int(m.group(1))
            gs = [sp.sympify(s.replace('^', '**'), locals=LOC) for s in m.group(2).split(',')]
            res.append((d, gs))
    return res

def sing_dim(gens):
    g = ','.join(S(p) for p in gens)
    out = sing.run(sing.HEAD + f'ring r=0,(x,y,z),dp; ideal J={g}; print(dim(std(J)));')
    return int(out.split()[-1])

def sing_comps_dim_le1(gens):
    return sing_comps(gens)

def power_split(um, f):
    """u_m = f^k * g, g not divisible by f"""
    k = 0
    g = sp.Poly(um, *X3)
    fp = sp.Poly(f, *X3)
    while True:
        q, r = sp.div(g, fp)
        if r.is_zero:
            g = q; k += 1
        else:
            break
    return k, g.as_expr()

def hess_on_perp(um, w):
    """D^2 u_m(w) restricted to w^perp (rational basis); returns (matrix, eigen-signature info exact)"""
    H = sp.hessian(um, X3).subs({x: w[0], y: w[1], z: w[2]})
    ns = sp.Matrix([w]).nullspace()
    B = sp.Matrix.hstack(*ns)
    Hp = sp.simplify(B.T * H * B)
    return Hp

def pd_exact(M):
    n = M.shape[0]
    return all(sp.simplify(M[:k, :k].det()) > 0 for k in range(1, n + 1))

def real_unit_points_zero_dim(gens):
    """вещественные направления (единичные) нулевого множества проективной 0-мерной системы: три аффинные карты x=1 | x=0,y=1 | x=y=0,z=1"""
    pts = []
    for sub in ({x: 1}, {x: 0, y: 1}, {x: 0, y: 0, z: 1}):
        eqs = [sp.expand(g.subs(sub)) for g in gens]
        eqs = [e for e in eqs if e != 0]
        free = [v for v in X3 if v not in sub]
        if not eqs:
            if len(free) == 0:
                cand = [dict()]
            else:
                continue
        else:
            try:
                cand = sp.solve(eqs, free, dict=True)
            except Exception:
                continue
        for s in cand:
            if any(v not in s for v in free):
                continue
            vec = [sub.get(v, s.get(v)) for v in X3]
            vals = [complex(sp.N(c)) for c in vec]
            if all(abs(c.imag) < 1e-12 for c in vals):
                v = [c.real for c in vals]
                n = sum(c * c for c in v) ** 0.5
                pts.append(tuple(round(c / n, 12) for c in v))
    return sorted(set(pts))

def analyse(key):
    e = BY[key]
    um = None
    from basic import forms
    fm = forms(e['U']); m = min(fm); um = fm[m]
    gens = [p for c, p in e['sos']]
    cs = sing_comps(gens)
    res = dict(key=key, m=int(m), u_m=str(sp.factor(um)), comps=[])
    for d, gs in cs:
        c = dict(dim=d, gens=[str(g) for g in gs])
        if d == 2:
            assert len(gs) == 1, (key, gs)
            f = gs[0]
            c['type'] = 'curve'; c['f'] = str(f); c['deg'] = int(sp.Poly(f, *X3).total_degree())
            # smoothness of the cone: (f, grad f) m-primary?
            jd = sing_dim([f] + [sp.diff(f, v) for v in X3])
            c['cone_smooth'] = (jd <= 0)
            if jd > 0:
                sc = sing_comps([f] + [sp.diff(f, v) for v in X3])
                c['sing_lines'] = [[str(g) for g in gg] for dd, gg in sc]
            k, g = power_split(um, f)
            c['k'] = int(k); c['g'] = str(sp.factor(g))
            if sp.Poly(g, *X3).total_degree() > 0 or g != 1:
                gd = sing_dim([f, g])
                c['g_zero_dim'] = gd      # 0: no common zeros; 1: finitely many projective points
                if gd >= 1:
                    sc = sing_comps([f, g])
                    c['g_zero_comps'] = [[str(q) for q in gg] for dd, gg in sc]
                    ptsr = []
                    for dd, gg in sc:
                        ptsr += real_unit_points_zero_dim(gg)
                    c['g_zero_real_dirs'] = [list(p) for p in ptsr]
            else:
                c['g_zero_dim'] = 0
        elif d == 1:
            c['type'] = 'point'
            pts = real_unit_points_zero_dim(gs)
            c['dirs'] = [list(p) for p in pts]
            # the prime has a rational generating direction w (for coordinate-type primes)
            c['hessians'] = []
        else:
            c['type'] = 'origin'
        res['comps'].append(c)
    # point components: Hessian on w^perp at +-w (rational direction from ideal): use sympy nullspace of linear forms
    for c in res['comps']:
        if c['type'] == 'point':
            lin = [g for g in map(sp.sympify, c['gens'])]
            if all(sp.Poly(g, *X3).total_degree() == 1 for g in lin) and len(lin) == 2:
                A = sp.Matrix([[sp.diff(g, v) for v in X3] for g in lin])
                w = A.nullspace()[0]
                den = sp.ilcm(*[sp.Rational(a).q for a in w]); w = [sp.Integer(a * den) for a in w]
                Hp = hess_on_perp(um, w)
                c['w'] = [int(a) for a in w]
                c['hess_perp'] = str(Hp.tolist())
                c['hess_rank'] = int(Hp.rank())
                c['hess_pd'] = bool(pd_exact(Hp))
    # intersections of curve components pairwise
    curves = [c for c in res['comps'] if c['type'] == 'curve']
    res['intersections'] = []
    for a, b in itertools.combinations(curves, 2):
        fa, fb = sp.sympify(a['f']), sp.sympify(b['f'])
        d_ = sing_dim([fa, fb])
        entry = dict(f1=a['f'], f2=b['f'], proj_points=bool(d_ >= 1))
        if d_ >= 1:
            sc = sing_comps([fa, fb])
            pts = []
            for dd, gg in sc:
                pts += real_unit_points_zero_dim(gg)
            entry['real_dirs'] = [list(p) for p in pts]
            # intersection multiplicity: vdim of (f1,f2,z-1)
            try:
                vd = sing.run(sing.HEAD + f'ring r=0,(x,y,z),dp; ideal J={S(fa)},{S(fb)},z-1; print(vdim(std(J)));')
                entry['vdim_chart_z1'] = int(vd.split()[-1])
            except Exception as ex:
                entry['vdim_chart_z1'] = None
        res['intersections'].append(entry)
    # point components lying on curve components?
    pts = [c for c in res['comps'] if c['type'] == 'point']
    res['points_on_curves'] = []
    for p in pts:
        if 'w' in p:
            for c in curves:
                if sp.sympify(c['f']).subs({x: p['w'][0], y: p['w'][1], z: p['w'][2]}) == 0:
                    res['points_on_curves'].append((p['w'], c['f']))
    return res

if __name__ == '__main__':
    keys = sys.argv[1:] or [e['key'] for e in EXS]
    out = {}
    fn = os.path.join(HERE, 'sigma.json')
    if os.path.exists(fn):
        out = json.load(open(fn))
    for k in keys:
        r = analyse(k)
        out[k] = r
        print('==', k, 'm=', r['m'], 'u_m =', r['u_m'])
        for c in r['comps']:
            print('   ', {kk: vv for kk, vv in c.items() if kk in ('type', 'dim', 'f', 'k', 'g', 'cone_smooth', 'sing_lines', 'g_zero_dim', 'g_zero_real_dirs', 'w', 'hess_rank', 'hess_pd', 'dirs')})
        for it in r['intersections']:
            print('    X:', it)
        if r['points_on_curves']:
            print('    pts on curves:', r['points_on_curves'])
    json.dump(out, open(fn, 'w'), indent=1, ensure_ascii=False)
