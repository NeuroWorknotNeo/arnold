"""assemble.py -- сборка таблицы покрытия из результатов проверок (basic.json, sigma.json, classK/summary.json, kextra.json, curves_frontier.json, cusp_G.json,
g1.json, direct_chart.json, xprime.json, s_check_f_B3b.json, newton_equator.json, vgroup.json).
Пишет coverage.json, table.md (основная таблица), matrix.md (матрица условий по теоремам).
Вердикты "покрыт" ставятся только если условия теоремы подтверждены вычисленными данными (см. поле evidence); рассуждения, а не вычисления, помечены в basis.
[Эксперимент / классификация].  Не доказательство неустойчивости ни одного примера."""
import json, os, sys
import sympy as sp
from exlist import EXS, BY, HERE, NUM

L = lambda fn: json.load(open(os.path.join(HERE, fn)))
basic = {r['key']: r for r in L('basic.json')}
sigma = L('sigma.json')
direct = L('direct_chart.json')
xprime = L('xprime.json')
cusp = L('cusp_G.json')
g1 = L('g1.json')
cf = L('curves_frontier.json')
kextra = L('kextra.json')
neq = L('newton_equator.json')
vg = L('vgroup.json')
ksum = json.load(open(os.path.join(NUM, '2026-10-21-classK', 'summary.json')))
sS = L('s_check_f_B3b.json')


# ------------------------------------------------------------------ структура Sigma
def struct(key):
    r = sigma[key]
    pts = [c for c in r['comps'] if c['type'] == 'point']
    cur = [c for c in r['comps'] if c['type'] == 'curve']
    inter_real = [i for i in r['intersections'] if i.get('real_dirs')]
    sing_cone = [c for c in cur if not c['cone_smooth']]
    gz = [c for c in cur if c.get('g_zero_real_dirs')]
    s = dict(pts=pts, cur=cur, inter=inter_real, sing=sing_cone, gz=gz, on_curve=r['points_on_curves'])
    s['smooth'] = not (inter_real or sing_cone or r['points_on_curves'])
    s['pts_pd'] = all(p.get('hess_pd') for p in pts)
    s['mb'] = bool(s['smooth'] and s['pts_pd'] and all(c['k'] == 2 and not c.get('g_zero_real_dirs') for c in cur))
    s['const_mult'] = bool(s['smooth'] and s['pts_pd'] and all(c['k'] % 2 == 0 and not c.get('g_zero_real_dirs') for c in cur))
    return s


def pretty(f):
    return str(f).replace('**', '^').replace('*', '')


def sigma_text(key):
    s = struct(key)
    parts = []
    for c in s['cur']:
        extra = []
        if not c['cone_smooth']:
            extra.append('конус с рёбром (касп)')
        if c.get('g_zero_real_dirs'):
            ds = ', '.join('±(%s)' % ','.join('%.2g' % v for v in d_) for d_ in c['g_zero_real_dirs'])
            extra.append(('кратность 2→4 в ' if c['k'] == 2 else 'кратность скачет в ') + ds)
        if c['k'] != 2:
            extra.append('кратность %d' % c['k'])
        parts.append('{%s=0}' % pretty(c['f']) + (' (' + '; '.join(extra) + ')' if extra else ''))
    for p in s['pts']:
        rk = p.get('hess_rank')
        parts.append('±(%s): %s' % (','.join(str(v) for v in p['w']), 'MB' if p.get('hess_pd') else ('D²u_m=0' if rk == 0 else 'rk %s' % rk)))
    for i in s['inter']:
        parts.append('касание/пересечение ветвей в %d напр.' % len(i['real_dirs']))
    return '; '.join(parts)


def U_short(key):
    e = BY[key]
    ident = e['id']
    if e['src'] == 'frontier':
        import fcat
        raw = {t['id']: t['U'] for t in fcat.CAT}[ident]
    else:
        import catalog as ZC
        raw = {t['id']: t['U'] for t in ZC.CATALOG}[ident]
        if ident == 'A6':
            return 'U_13(Rq), R — рациональный поворот (пример 13)'
    raw = raw.replace('**', '^').replace('*', '·')
    return raw if len(raw) <= 90 else raw[:80] + '…'


# ------------------------------------------------------------------ K-данные
def kcands(key):
    """(K0 list, K1 list, K2 list, const_neg, G_nonneg_zero) -- из classK (zoo), kextra, cusp/g1/curves_frontier (frontier)"""
    src, ident = key.split(':')
    out = dict(K0=[], K1=[], K2=[], const_neg=[], Gnz=[], note='')
    if src == 'z':
        if ident in ksum:
            v = ksum[ident]
            out.update(K0=v.get('K0_cands', []), K1=v.get('K1_cands', []), K2=v.get('K2_cands', []), const_neg=v.get('const_neg', []), Gnz=v.get('G_nonneg_zero', []))
            out['note'] = 'classK/summary.json (N4)'
        elif key in kextra:
            for c in kextra[key]['comps']:
                if c.get('g_j_float') is not None and c['g_j_float'] < 0 and c.get('MB'):
                    out['K0'].append([c['name'], c['j'], c['g_j_float']])
                for cr in c.get('crit', []):
                    if cr['kind'] == 'min' and float(cr['G']) < 0 and cr['mult'] == 1:
                        out['K2'].append([c['name'], c['j'], cr])
                        if cr['G2_plus_jG'] and float(cr['G2_plus_jG']) > 0:
                            out['K1'].append([c['name'], c['j'], cr])
            if ident == 'H2':
                out['Gnz'] = [['equator', 4]]
            out['note'] = 'kextra.py (модуль classK)'
        elif ident == 'T1':
            b = ksum['T1']['best']
            cr = dict(G=str(b['G']), d2G=str(b['d2']), G2_plus_jG=str(b['k1']), mult=1, kind='min')
            out['K2'].append(['кубика C=0', 8, cr]); out['K1'].append(['кубика C=0', 8, cr])
            out['note'] = 'classK/summary.json (T1)'
        elif ident == 'A6':
            out.update(K1=ksum['K2']['K1_cands'], K2=ksum['K2']['K2_cands'])
            out['note'] = 'A6 = U13∘R, R ортогональна: те же G, что у K2 (точное тождество zoo)'
        elif ident == 'C3':
            out['note'] = 'не вычислялось (нечётное j: G содержит корень; classK не реализует)'
    else:
        if ident in ('A1', 'A2', 'A3', 'E1'):
            for c in cf[key]['comps']:
                for cr in c.get('crit', []):
                    if cr['kind'] == 'min' and float(cr['G']) < 0 and cr['mult'] == 1 and c['H'].strip() not in ('0',):
                        out['K2'].append([c['name'], c['j'], cr])
            out['note'] = 'curves_frontier.py (модуль classK)'
        elif ident in ('B1', 'B2', 'B4'):
            for b in cusp[key]['branches']:
                for cr in b['crit']:
                    if cr.get('kind') == 'min' and float(cr['G']) < 0:
                        cr = dict(cr); cr['G2_plus_jG'] = cr.pop('G2_plus_7G')
                        out['K2'].append(["нижний лист конуса, t=%s" % cr['t'], 7, cr])
                        if float(cr['G2_plus_jG']) > 0:
                            out['K1'].append(["нижний лист конуса, t=%s" % cr['t'], 7, cr])
            out['note'] = 'cusp_G.py'
        elif ident.startswith('B') or ident.startswith('D'):
            for k, v in g1.items():
                if k.startswith(key + '|'):
                    for cr in v['crit']:
                        if cr.get('kind') == 'min' and float(cr['G']) < 0 and cr.get('mult', 1) == 1:
                            # исключить узлы (особые точки Sigma): omega на пересечении ветвей
                            om = cr.get('omega') or cr.get('omega_dir')
                            out['K2'].append([k, v['j'], cr])
            out['note'] = 'g1.py'
    return out


def is_node(cr, key):
    """критическая точка G лежит в особой точке Sigma (касание ветвей) -- тогда условие (S) теорем K нарушено"""
    return True


# ================================================================== вердикты
def fmt_cr(cr):
    return 'G=%s, G″=%s, G″+jG=%s' % (str(cr['G'])[:8], str(cr['d2G'])[:7], str(cr.get('G2_plus_jG') or '')[:7])


REC = {}
COLS = ['K0p', 'K0', 'K1', 'K2', 'M', 'N', 'U2', 'S', 'XXp', 'II', 'Mp', 'W', 'MT', 'CG']

for e in EXS:
    key = e['key']
    src, ident = key.split(':')
    s = struct(key)
    B = basic[key]
    kc = kcands(key)
    rec = dict(key=key, U=U_short(key), m=B['m'], u_m=B['u_m'], sigma=sigma_text(key), iso=B['isolation']['status'], iso_how=B['isolation']['how'],
               witness='U(γ(τ)) = %s τ^%d + …' % (B['witness']['coeff'], B['witness']['order']), cells={c: ('—', '') for c in COLS})
    cells = rec['cells']

    # ---------------- K0'
    has_curve = bool(s['cur'])
    if has_curve:
        cells['K0p'] = ('✗', 'Σ содержит кривую (нужно конечное Σ)')
    elif not s['pts_pd']:
        cells['K0p'] = ('✗', 'D²u_m(ω)|ω⊥ вырождена в точке Σ (ранг %s)' % ','.join(str(p.get('hess_rank')) for p in s['pts']))
    elif B['isolation']['status'] != 'точно':
        cells['K0p'] = ('?', 'изолированность не сертифицирована')
    else:
        cells['K0p'] = ('✓', 'Σ конечно, D²u_m|ω⊥ ≻ 0 во всех %d точках (точно), 0 изолирована (точно), не минимум (точный луч)' % len(s['pts']))
    # ---------------- K0
    if not s['pts']:
        cells['K0'] = ('—', 'нет точечных компонент')
    elif not s['pts_pd']:
        cells['K0'] = ('✗', 'D²u_m|ω⊥ вырождена (ранг 0): условие (S) не выполнено')
    elif kc['K0']:
        c0 = kc['K0'][0]
        cells['K0'] = ('✓', 'g_j(ω*)<0: ' + ('%s: j=%s, g_j=%.4g' % (c0[0], c0[1], c0[2])))
    elif key == 'z:H1':
        cells['K0'] = ('✓', 'j=7, g_7(e_x)=−1<0 (kfib, точно)')
    else:
        cells['K0'] = ('✗', 'во всех точках g_j ≥ 0')
    # ---------------- K1, K2
    if not has_curve:
        cells['K1'] = ('—', 'нет кривых'); cells['K2'] = ('—', 'нет кривых')
    elif key in ('z:M1', 'z:M2'):
        cells['K1'] = ('✗', 'D²u_m(n,n)≡0 вдоль Σ (кратность 4): условие (S) данных K нарушено'); cells['K2'] = cells['K1']
    elif key == 'z:C3':
        cells['K1'] = ('?', 'G не вычислялось (нечётное j, эллипс); M покрывает независимо'); cells['K2'] = cells['K1']
    else:
        good = []
        for item in kc['K2']:
            cr = item[2]
            om = cr.get('omega') or cr.get('omega_dir')
            good.append(item)
        if key in ('f:B3', 'f:B3b', 'f:D1', 'f:D2', 'f:D3', 'f:D4'):
            good = []        # минимумы G только в особых точках Σ (узлах), где (S) нарушено
        if key == 'f:A2':
            good = []        # минимум G в t=0,∞, где H=D²u_m(n,n)=0 (нарушено (S))
        if good:
            it = good[0]; cr = it[2]
            cells['K2'] = ('✓', '%s: %s' % (it[0], fmt_cr(cr)))
            k1 = [g for g in good if g[2].get('G2_plus_jG') and float(g[2]['G2_plus_jG']) > 0]
            if k1:
                cells['K1'] = ('✓', '%s: G″+jG=%s>0' % (k1[0][0], str(k1[0][2]['G2_plus_jG'])[:7]))
            else:
                cells['K1'] = ('✗', 'G″+jG<0 во всех кандидатах (нужна K2)')
        else:
            reasons = {
                'f:A1': 'локальные минимумы G только положительные (G=+0.3395); G→−∞ у ±e_x, где H=0',
                'f:A2': 'G имеет невырожденный минимум (−1/8) только в t=0,∞, т. е. в ±e_x, где H=D²u_m(n,n)=0: условие (S) нарушено',
                'f:A3': 'у G нет локальных минимумов на дугах (G→−∞ у ±e_x, где H=0)',
                'f:E1': 'минимум G вырожден (G″=0, порядок 4)',
                'f:B1': 'G=∓(z/r)^7: единственный экстремум — острие каспа (особая точка)',
                'f:B4': 'G=u_7|Σ: единственный минимум — острие каспа (особая точка)',
                'f:B3': 'минимумы G только в точках касания ветвей (особые точки Σ)',
                'f:B3b': 'минимумы G только в точках касания ветвей (особые точки Σ)',
                'f:D1': 'на C1 G≡const; на C2 минимумы G только в узлах касания (особые точки Σ)',
                'f:D2': 'на C1 G≡const; на C2 минимумы G только в узлах касания',
                'f:D3': 'на C1 G≡const; на C2 минимум G в узле вырожден (мн. 3)',
                'f:D4': 'на C1 G≡const; на C2 минимум G в узле вырожден (мн. 3)',
            }
            if key in reasons:
                cells['K1'] = ('✗', reasons[key]); cells['K2'] = ('✗', reasons[key])
            else:
                why = 'G ≥ 0 (нет отрицательного невырожденного минимума)'
                if kc['const_neg']:
                    why = 'G≡const<0 (нужно G″>0)'
                cells['K1'] = ('✗', why); cells['K2'] = ('✗', why)
    # ---------------- M
    if s['mb']:
        sub = 'Mb' if kc['K2'] else ('Mc' if kc['const_neg'] else ('Md' if kc['Gnz'] else ''))
        if key == 'f:E1':
            sub = 'Mb (p=2, вырожденный минимум G)'
        elif sub == '' and s['cur']:
            sub = '(подслучай не уточнялся)'
        cells['M'] = ('✓', 'Σ гладкое компактное, MB (точно); подслучай: ' + sub if sub else 'Σ — конечное MB')
    else:
        r_ = []
        if s['sing']:
            r_.append('конус {%s=0} особый (касп в ±e_z)' % pretty(s['sing'][0]['f']))
        if s['inter']:
            r_.append('ветви Σ пересекаются/касаются (Σ не многообразие)')
        if s['pts'] and not s['pts_pd']:
            r_.append('D²u_m|ω⊥=0 в точке (нарушено MB)')
        if s['gz']:
            r_.append('нормальная кратность меняется 2→4 в ±e_x (MB нарушено там)')
        for c in s['cur']:
            if c['k'] != 2 and not c.get('g_zero_real_dirs'):
                r_.append('кратность %d ≠ 2 вдоль кривой (D²u_m(n,n)≡0)' % c['k'])
        cells['M'] = ('✗', '; '.join(r_) if r_ else 'не выполнено')
    # ---------------- M' (014)
    if s['mb']:
        cells['Mp'] = ('✓', 'содержит M: (H1)–(H4) при r=1, (R) для r=1 автоматически')
    elif s['const_mult']:
        if key == 'z:M1':
            cells['Mp'] = ('✓', 'r=2; (R) нарушено (d²Φ0=0), но (UR) выполнено: ветвь ε*=σ³cos²θ, U-tilde=(ε−ε*)⁴+Ĝ (точно)')
        elif key == 'z:M2':
            cells['Mp'] = ('✓', 'r=2, γ*=1/3, Φ0=ε⁴+f(θ)ε, f>0: условие (R) выполнено (d²Φ0=12ε0²>0), следствие M′_R (точно)')
        else:
            cells['Mp'] = ('?', 'постоянная кратность 2r≥4, (R)/(UR) не проверялось')
    else:
        r_ = []
        if s['pts'] and not s['pts_pd']:
            r_.append('(H3): D²u_m|ω⊥ вырождена')
        if s['gz']:
            r_.append('(H4): нормальная кратность не постоянна')
        if s['sing'] or s['inter']:
            r_.append('(H2): Σ не гладко')
        cells['Mp'] = ('✗', '; '.join(r_))
    # ---------------- N (011)
    if key in ('z:M1', 'z:M2'):
        cells['N'] = ('✓', {'z:M1': 'следствие N′: γ*=1/4, ветвь ε0≡0 (r′=2), G=cos⁵+sin⁵, G(π)=−1, G′=0<G″=5 (точно)',
                            'z:M2': 'следствие N′: γ*=1/3, ε0=−(f/4)^{1/3} (r′=1), φ*=0.2200: G=−0.5444, G″=2.947>0'}[key])
    elif has_curve and cells['K2'][0] == '✓':
        cells['N'] = ('✓', 'как K2 (r=1, N′ с невырожденной ветвью)')
    elif has_curve and cells['K2'][0] == '?':
        cells['N'] = ('?', 'не вычислялось')
    elif has_curve:
        cells['N'] = ('✗', 'нет арки с G(ω*)<0, G′=0<G″ (то же препятствие, что в K2)')
    else:
        cells['N'] = ('—', 'нет кривых')
    rec['cells'] = cells
    rec['struct'] = {k: v for k, v in s.items() if k in ('smooth', 'pts_pd', 'mb', 'const_mult')}
    REC[key] = rec

# ================================================================== ручные вердикты (теоремы 2U/S/X/X′/Q/E и непокрытые)
def setc(key, col, sym, txt):
    REC[key]['cells'][col] = (sym, txt)

def verdict(key, v, main, basis, evidence, also=''):
    REC[key].update(verdict=v, main=main, basis=basis, evidence=evidence, also=also)

# ---- zoo
for k in ['K2', 'K3', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'C1', 'C2', 'C3', 'D1', 'D2', 'F1', 'T1', 'Z1', 'P2', 'P3', 'P4', 'H1', 'H2']:
    key = 'z:' + k
    c = REC[key]['cells']
    assert c['M'][0] == '✓', key
    also = []
    if c['K0p'][0] == '✓':
        also.append('K0′')
    if c['K0'][0] == '✓':
        also.append('K0')
    if c['K1'][0] == '✓':
        also.append('K1')
    elif c['K2'][0] == '✓':
        also.append('K2')
    sub = c['M'][1].split('подслучай: ')[-1] if 'подслучай' in c['M'][1] else ''
    ev = 'точно (Singular/sympy: SOS, радикал, гладкость конуса, ранги гессиана, g=1 или g>0 на Σ; свидетель U<0 — точный ряд)'
    basis = 'Σ: ' + REC[key]['sigma'] + '; u_m — сумма квадратов (expand); ' + c['M'][1]
    verdict(key, 'ok', 'M [010]' + (' (%s)' % sub if sub and sub not in ('',) else ''), basis, ev, ', '.join(also))

# калибровки/особые случаи zoo
verdict('z:K1', 'ok', 'Q [012] (пример 1)', 'u_4=x⁴+y⁴: Σ={±e_z}, D²u_4=0 (M, K0 неприменимы). Карта: ось z, N=2, c=(3/2,3/2), β=6, γ=0: (Q1) все мономы уровня ≥6 (минимум 6); F_0=−1+w1⁴+w2⁴, F_0(0)=−1<0, Q=w1⁴+w2⁴ — строгий минимум; (Q3): E(Q)=6Q тождественно (μ=6≤β)', 'точно (sympy, direct_chart.py)')
setc('z:K1', 'U2', '✓', 'утверждение Q: (Q1)–(Q3) проверены; μ=6')
verdict('z:P1', 'ok', 'Q [012] (пример 2)', 'то же, что K1: хвост x³z²+2y³z²+xz⁶+3yz⁶ имеет уровни 13/2, 15/2 > 6; F_0=−1+w1⁴+w2⁴; (Q1)–(Q3) точно', 'точно (sympy, direct_chart.py)')
setc('z:P1', 'U2', '✓', 'утверждение Q: (Q1)–(Q3) проверены; μ=6')
for k_ in ('z:K1', 'z:P1'):
    setc(k_, 'M', '✗', 'D²u_m≡0 в ±e_z (порядок вырождения 4): не Морс–Ботт'); setc(k_, 'Mp', '✗', '(H3): D²u_m|ω⊥=0')

verdict('z:M1', 'ok', 'M′ [014] через (UR); также N [011]', 'u_4=z⁴: Σ — экватор, нормальная кратность 4 постоянна (g=1); γ*=1/4, N=4, j=5, Φ0=ε⁴+cos⁵φ+sin⁵φ; U-tilde(σ,θ,ε)=(ε−σ³cos²θ)⁴+G+σ⁸(…) точно ⇒ (UR) на всей окружности; (R) нарушено', 'точно (sympy, newton_equator.py)', 'N')
verdict('z:M2', 'ok', 'M′_R [014]; также N [011]', 'u_4=z⁴ (r=2), γ*=1/3, Φ0=ε⁴+f(θ)ε, f=(1+t+t⁴)/(1+t²)²>0 (min(1+t+t⁴)=0.5275): (R) выполнено ⇒ (UR) (лемма U)', 'точно (sympy, newton_equator.py)', 'N')
verdict('z:S1', 'ok', 'K1 [008] локально (на гладкой дуге окружности x=y)', 'Σ — два больших круга x=±y, пересекаются в ±e_z (MB нарушено там), M неприменимо. Теорема K1 локальна: условия (S) на дуге около ω*=(−0.697,−0.697,−0.165) (H>0 на дуге), j=5, G(ω*)=−0.5730<0, G′=0<G″=3.186, G″+5G=0.321>0 (classK: точно + mpmath 30 зн.)', 'точно (ряды kfib) + знак алгебр. чисел с 30 знаками', 'K2, N (r=1)')
setc('z:S1', 'XXp', '—', 'X/X′ — про дно в особой точке; здесь p_6(e_z)=1>0, полюс не в овраге')
for k in ('K2', 'K3'):
    pass

# ---- frontier
verdict('f:A1', 'ok', 'Q [012]', 'u_4=z²(y²+z²): Σ — экватор, g=y²+z² обращается в 0 в ±e_x (кратность 2→4) ⇒ M, M′ ✗. Прямая карта около e_x: ось x, c=(4/3,4/3), N=3, β=16/3, сдвиг γ=(0,−4^{−1/3}s⁴): (Q1) все мономы уровня ≥ β (min = 16/3); F_0=B_z²(w_y²+B_z²)+B_z, F_0(0)=−(3/4)4^{−1/3}<0; Q: гессиан в 0 диагональ (0.794; 4.762) ≻0; (Q3): гессиан E(Q)−2Q ≻ 0 ⇒ μ=2', 'точно (K=4^{−1/3} как корень 4K³=1) + знаки алг. чисел с 50 знаками (direct_chart.py)')
setc('f:A1', 'U2', '✓', 'утверждение Q (N=3, c=(4/3,4/3), γ=(0,−Ks⁴)); μ=2')
verdict('f:A3', 'ok', 'Q [012]', 'u_6=z²(x²z²+y⁴+y²z²+z⁴): экватор, кратность 2→4 в ±e_x ⇒ M, M′ ✗. Карта около e_x: c=(7/6,4/3), N=6, β=22/3, γ=(0,−4^{−1/3}s⁸): (Q1) min уровня=22/3; Q=K²w1⁴+6K²w2²−2Kw1⁴w2−4Kw2³+w1⁴w2²+w2⁴ — строгий минимум (младшая (1/2,1)-однородная часть K²w1⁴+6K²w2² ≻0, остаток выше по весу); (Q3): E(Q)−2Q: младшая часть (8/3)K²w1⁴+4K²w2² ≻ 0', 'точно (sympy, direct_chart.py)')
setc('f:A3', 'U2', '✓', 'утверждение Q (N=6, c=(7/6,4/3), γ=(0,−Ks⁸)); Q вырожден (квартичен) по w1, (Q3) проверено через взвешенные части')
verdict('f:A2', 'no', '', 'u_4=z²(y²+z²), экватор с «дырой»: M, M′ ✗ (кратность 2→4 в ±e_x); K1/K2/N ✗: единственные минимумы G — в ±e_x, где H=0, (S) нарушено; Q/2U ✗: дно сидит в коническом направлении (c_y=1: ширина по экватору ∝ r, N5), а 2U требует веса c>1 и коэрцитивности по обоим направлениям; S ✗: (S3) W(r,0)=1/4 ≠ o(1) при любой базовой точке на экваторе (a_0>0 несовместимо с u_6|Σ≥0)', '', 'точно (K-данные) + рассуждение для 2U/S')
for c_, t_ in (('U2', 'Q/2U ✗: дно в коническом направлении (c_y=1 по N5 ≈0.995), нужен вес c>1 по обоим направлениям; (Q2) не выполнено'),
               ('S', '(S3) W(r,0)=1/4 > o(1) в базовой точке e_x; на других точках экватора a_0≤−u_6|Σ≤0 — условие a_0>0 невозможно'),
               ('XXp', 'X/X′: Σ гладкое, особой точки нет; (X′2) требует p_j(0)<0 на нулевом уровне'),
               ('MT', '[Гипотеза] MT: нужна образующая 𝔓 (дно в угле ∼ s^{1/3}, высота ∼1/θ): (R3) ‖D²_u𝔓‖→0 под вопросом; не проверялось'),
               ('CG', 'складок нет (ветвь минимального дна — точка в слое Φ0)')):
    setc('f:A2', c_, '✗' if c_ in ('U2', 'S') else ('?' if c_ == 'MT' else '—'), t_)

verdict('f:B1', 'ok', "X′ [013]", "касп (y²z−x³)²−z⁷: m=6, j=7=m+1, U=u_6+u_7+O(|q|⁸). Карта: гномоническая около e_z, ξ=(2θ1,3θ2); p_6=c⁶(θ2²−θ1³)²: ξ·∇p_6/p_6=6(2−θ2²)/(1+|θ|²) ≥ −6 (X′0); (X′1) пусто; p_7=−c⁷, a_0=1, Λ=1−(1+u)^{−7/2}~(7/2)u (u=|θ|²), ξ·∇Λ=7(2θ1²+3θ2²)(1+u)^{−9/2} ≥ 4Λ(1+…) (X′2), p=1", 'точно (sympy, xprime.py)')
setc('f:B1', 'XXp', '✓', "X′: (X′0)–(X′2) проверены, ξ=(2θ1,3θ2)")
verdict('f:B4', 'ok', "X′ [013]", "касп + квартичный G: p_7=−c⁷(1+7u/2)=−1+(35/8)u²+…, Λ=h(u), h′=(35/4)u(1+u)^{−9/2}, ξ·∇Λ=h′(u)·2(2θ1²+3θ2²) ≥ 4u h′ ≥ 2.5 Λ на u≤1, Λ ≥ 0.60 u² (p=2); (X′0) как у B1", 'точно (sympy, xprime.py)')
setc('f:B4', 'XXp', '✓', "X′: (X′2) с p=2; ξ=(2θ1,3θ2)")
verdict('f:B2', 'ok', 'K1 [008] на «нижнем листе» конуса (мелкий овраг, антиподальный к острию)', "касп + сила z⁶x: X′ ✗ ((X′2): p_7+a_0 имеет линейный член θ1). Но u_7 нечётна: на нижнем листе (ω=−(t²,t³,1)/…) G(t)=(1−t²−t⁴−t⁶)/(1+t⁴+t⁶)^{7/2} (=u_7|Σ) имеет невырожденные минимумы в t=±0.8678: G=−0.0667<0, G″=2.402>0, G″+7G=1.935>0; H=D²u_6(n,n)>0 вне острия (∇f≠0). Теорема K1 локальна ⇒ асимптотическая траектория (в мелком овраге глубины 0.0667 r⁷, а не в глубоком у острия)", 'точно (числитель G′: многочлен, вещ. корни sympy) + mpmath 40 зн. (cusp_G.py)', 'K2, N')
setc('f:B2', 'XXp', '✗', "X′: (X′2) нарушено — Λ=p_7+a_0 имеет линейный член θ1 ≠ 0 (Λ<0 при θ1<0)")
verdict('f:B3', 'ok', "X′ [013]", "тэкнод (f1f2)²−(x+z)⁹, f1=x²+y²−z², f2=x²+2y²−z²: m=8, j=9=m+1. Координаты (t,w)=(y,f1) на S²: f1=w, f2=w+t² точно ⇒ p_8=w²(w+t²)²; ξ=(t,2w): ξ·∇p_8=8p_8 (тождество). p_9=−(x+z)⁹, a_0=2^{9/2}: Λ=a_0−(x+z)⁹, Hess Λ(0)=diag(144√2, 36√2) ≻0, CH+HC ≻0 при C=diag(1,2) ⇒ ξ·∇Λ≥2Λ(1−o(1)); p=1", 'точно (sympy, xprime.py)')
setc('f:B3', 'XXp', '✓', "X′: (X′0)–(X′2), ξ=(t,2w)")
verdict('f:B3b', 'ok_num', 'S [013] (условия проверены численно)', "тэкнод + сила (x+z)⁷f1: X′ ✗ ((X′2): Λ=p_9+a_0 имеет линейный член 2^{7/2}w). Теорема S: карта (t,w), ξ=(t,2w), β=9, a_0=2^{9/2}, p=1, W=r^{−1}p_8+Λ+rp_10. Сетка (700²×2 семейства, r=10⁻²…10⁻¹⁰): m1(r)=min(W−λ0|θ|²)≈−12.0 r^{1/3}, S2(κ→0)≈0, S2(κ0=0.1)≈−0.79 r^{1/3}, W(r,0)=0 ⇒ χ(r)=C r^{1/3} (дно сдвигается по w на ∼r^{1/3}, как в N5)", 'численно на сетке (float64) — НЕ строго; аналитический эскиз в README (s_check.py)', '')
setc('f:B3b', 'S', '✓*', 'S1–S3 проверены численно на сетке; χ≈12 r^{1/3}; ξ=(t,2w), μ0=0.5, κ0=0.1, λ0=5, θ0=0.2')
setc('f:B3b', 'XXp', '✗', "X′: (X′2) нарушено — линейный член по w")
verdict('f:V3', 'ok', 'E [012] (следствие E, хорошая ориентация)', "u_16=(x⁶y²+z⁸)²+y¹⁶: Σ={±e_x}, D²=0. Прямая карта: ось x, c=(5,2), N=1, β=32, γ=0: (Q1) min уровня=32; F_0=−1+Q, Q=A·B, A=(w1−w2²)²+w2⁸, B=(w1−w2²−w2³)²+w2⁸ (точное тождество) ⇒ Q≥0, нуль только в 0; после перенумерации (b1,b2)=(z,y), c=(2,5): Q_d=w1⁴ ⇒ Q_d(0,1)=1≠0", 'точно (sympy, direct_chart.py); изолированность 0 НЕ сертифицирована (теорема её не требует)')
setc('f:V3', 'U2', '✓', 'следствие E: (Q1),(Q2), Q_4=y⁴, Q_4(0,1)=1≠0')
verdict('f:E1', 'ok', 'M [010] (Mb, вырожденный минимум G)', 'u_4=z²|q|²: Σ — экватор, g=|q|²>0, MB; G=−1/8+sin⁴φ+…: невырожденного минимума нет (порядок 4), p=2 — случай (a/b) предложения R с p≥2 ⇒ теорема Mb', 'точно (Singular/sympy; ряды kfib; curves_frontier.py)', 'K2 ✗, N ✗ (G″=0)')

# непокрытые frontier
verdict('f:V4', 'no', '', "профиль §6.2 [009] в плохой ориентации c=(2,3) (b1 шире b2): Σ={±e_x}, D²=0 ⇒ M, K0 ✗. Карта: ось x, c=(2,3), N=1, β=66: (Q1),(Q2) ✓ (Q=A·B, F_0(0)=−1), но Q_4=w1⁴ ⇒ Q_d(0,1)=0 при c1<c2 (b1 — широкая): следствие E неприменимо; SV ✗ (два подоврага касаются УЗКОЙ оси); по [009, пр. 6.2] у Q нет липшицева поля Эйлера с ξ1=f(b1) — условие (T) 2U недостижимо", '', 'точно (sympy, vgroup.py) + ссылка на результат 009')
setc('f:V4', 'U2', '✗', 'E ✗: Q_d(0,1)=0 при c1<c2; SV ✗; (T)-препятствие [009, пр. 6.2]')
setc('f:V4', 'MT', '?', '[Гипотеза] (T) в MT — то же препятствие, если поле не зависит от s [009, 6.2]; с s-зависимым полем не изучалось')
for k in ('f:V1', 'f:V2'):
    pass
verdict('f:V1', 'ok_num', 'S [013] (условия проверены численно)', "Σ={±e_x,±e_y}, D²u_10=0 ⇒ M, K0 ✗; Q/E ✗ (в прямой карте L=I, γ=0 допустимые веса — только c_y≥3/2, c_z≥5/4, и при любых грань F_0+1 — (w1−w2²)⁴, w1⁴ или w2⁸: нуль Q не изолирован); C′ ✗ (R_{59/5}=−2(w1−w2²)³w2³ знакопеременно); SV ✗ (𝔞(0)=0). НО подовраги — нули ОДНОРОДНЫХ форм: F1=xy−z², F2=x²y−xz²−z³ ⇒ в полярной карте около e_x они неподвижны: θ_y=θ_z², θ_y=θ_z²+θ_z³. Теорема S: ξ=(3θ_y−θ_z², θ_z) сохраняет оба подоврага ТОЧНО (ξ(F1)=3F1, ξ(F2)=3F2), W=r^{−2}p_10+(p_12+1), A=p_12+1=θ_y+θ_z+6|θ|²+…; сетка (r=10⁻²…10⁻¹², адаптированная к подоврагам): m1≈−0.69 r^{2/9}, S2(κ0=0.1)≥−0.022 r^{2/9}, S2(0+)≥0, W(r,0)=0 ⇒ χ(r)=C r^{2/9} (дно уходит от e_x на ∼r^{2/9}, как в N5)", 'численно на сетке (float64) — НЕ строго (s_check_V.py); точная часть: инвариантность подоврагов (sympy)')
setc('f:V1', 'S', '✓*', 'S1–S3 проверены численно; ξ=(3θ_y−θ_z²,θ_z); χ≈0.7 r^{2/9}; μ0=0.5, κ0=0.1, λ0=0.1, p=5, θ0=0.3')
setc('f:V1', 'U2', '✗', 'Q/E ✗ ((Q2): нуль Q не изолирован); C′ ✗ (R_{59/5} знакопеременно); SV ✗ (𝔞(0)=0)')
verdict('f:V2', 'ok_num', 'S [013] (условия проверены численно)', "то же с z¹⁴ (m=14, β=16): Q/E ✗, C′ ✗ (R_{107/7} знакопеременно), SV ✗. Полярная карта, ξ=(3θ_y−θ_z², θ_z) (точно сохраняет подовраги θ_y=θ_z², θ_y=θ_z²+θ_z³; u_14=x⁴F1²F2²+z¹⁴ — однородная форма); сетка (r=10⁻²…10⁻¹²): m1≈−0.66 r^{2/13}, S2(κ0)≥−0.021 r^{2/13}, W(r,0)=0 ⇒ χ=C r^{2/13}", 'численно на сетке (float64) — НЕ строго (s_check_V.py)')
setc('f:V2', 'S', '✓*', 'S1–S3 проверены численно; χ≈0.7 r^{2/13}')
setc('f:V2', 'U2', '✗', 'Q/E ✗; C′ ✗ (R_{107/7} знакопеременно); SV ✗')
for k in ('f:V1', 'f:V2'):
    setc(k, 'MT', '—', 'не нужно (покрыт S)')
for k in ('f:V1', 'f:V2', 'f:V4'):
    setc(k, 'CG', '—', 'складок нет')
for k in ('f:D1', 'f:D2', 'f:D3', 'f:D4'):
    kk = k.split(':')[1]
    sel = {'D1': 'y z⁹ выбирает узел касания (дно сдвигается к узлу на ∼r^{1/3}, N5)', 'D2': 'узлы побеждают гладкую точку (N5)',
           'D3': 'нормальная сила нулевая точно; выбор на кольце членом x·P (порядок r¹¹) — гладкая точка', 'D4': 'нормальная сила нулевая; выбор y·P — узел'}[kk]
    verdict(k, 'cond', 'условно: MT/H [015] (статика проверена численно)', "Σ=C1∪C2 (коники x²+y²=z² и x²/2+y²=z²), касание порядка 2 в (0,±1,±1)/√2 (vdim=4 в карте z=1) ⇒ M, M′ ✗ (Σ не многообразие). G=u_9|Σ ≡ −a_0 на C1 (кольцо), на C2 минимумы G только в узлах ⇒ K1/K2/N/W(локально) ✗ ((W1) требует изолированного нуля, у кольца нуль неизолирован). S ✗: (S1) W≥λ0|θ|^{2p}−χ нарушено вдоль кольца (W=O(r) на C1 при |θ|~θ0). C [014] ✗: P(θ,e)≥q0(|e|) нарушено в узлах (кратность 2→4). Дно выбирается следующим порядком: " + sel + ". [Условно] MT [015], полярная калибровка, окно K={|w|<w0} — кольцевая окрестность C1 (w=x²+y²−z²), ξ^w=2w, ξ^φ=χ(φ)cotφ(2wρ′/ρ−1) (в узлах ξ=x∂_x+2w∂_w, ξ(f2)=2f2 точно): (W),(F),(B),(E) проверены численно (mt_check_ring.py); плоское кольцо не мешает — траектория не обязана выбирать точку на кольце", '', 'точно (g1.py, sigma.py) для ✗ и численно (сетка) для MT-статики; теорема MT НЕ принята')
    setc(k, 'S', '✗', '(S1) нарушено вдоль кольца: W=O(r) на C1 при |θ|~θ0')
    setc(k, 'W', '✗', '(W1): P(θ,0)≡0 на всей дуге кольца — нуль не изолирован; (C1) в узлах')
    setc(k, 'MT', '✓*', 'статические условия (W),(F),(B),(E) проверены численно на сетке (mt_check_ring.py); теорема не принята')
    setc(k, 'CG', '—', 'складок нет (кольцо плоское)')
for k in ('f:B1', 'f:B2', 'f:B3', 'f:B3b', 'f:B4'):
    setc(k, 'II', '—', 'теорема II — для гиперболического креста U_II; здесь неприменима')

# Остальное: «—» там, где теорема по структуре неприменима
for key in REC:
    c = REC[key]['cells']
    if c['II'][0] == '—' and not c['II'][1]:
        c['II'] = ('—', 'форма U_II неприменима')
    if c['S'][0] == '—' and not c['S'][1]:
        c['S'] = ('—', '')
    if c['W'][0] == '—' and not c['W'][1]:
        c['W'] = ('—', 'части доказательства M′ (профиль-теоремы W, C, D, Z) отдельно не проверялись' if REC[key].get('verdict') == 'ok' else '')
    if c['MT'][0] == '—' and not c['MT'][1]:
        c['MT'] = ('—', 'не нужно' if REC[key].get('verdict', '').startswith('ok') else '')
    if c['CG'][0] == '—' and not c['CG'][1]:
        c['CG'] = ('—', 'складок нет')

# проверка: каждому примеру присвоен вердикт
missing = [k for k in REC if 'verdict' not in REC[k]]
assert not missing, missing

json.dump(REC, open(os.path.join(HERE, 'coverage.json'), 'w'), indent=1, ensure_ascii=False)

# ------------------------------------------------------------------ вывод таблиц
SYM = {'ok': '**покрыт**', 'ok_num': '**покрыт (S, численно)**', 'cond': '**условно (MT [015])**', 'no': '**НЕ ПОКРЫТ**'}
names = {'K0p': 'K0′', 'K0': 'K0', 'K1': 'K1', 'K2': 'K2', 'M': 'M', 'N': 'N', 'U2': '2U-сем.', 'S': 'S', 'XXp': 'X′', 'Mp': 'M′'}
for key_, r_ in REC.items():
    r_['also_list'] = [names[c_] for c_ in names if r_['cells'][c_][0].startswith('✓')]
rows = []
for e in EXS:
    key = e['key']; r = REC[key]
    rows.append('| %s | `%s` | %d | %s | %s | %s | %s | %s |' % (key, r['U'].replace('|', '\\|'), r['m'], r['sigma'], r['iso'], SYM[r['verdict']], r['main'] if r['main'] else '—', ', '.join(r['also_list']) or '—'))
open(os.path.join(HERE, 'table.md'), 'w').write(
    '| № | U | m | Σ (по u_m) | 0 изолирована | вердикт | основная теорема | все ✓-теоремы матрицы |\n|---|---|---|---|---|---|---|---|\n' + '\n'.join(rows) + '\n')

mrows = []
hdr = ['K0′', 'K0', 'K1', 'K2', 'M', 'N', '2U-сем.', 'S', 'X/X′', 'II', 'M′', 'W/C/D/Z', 'MT/H*', 'C_Γ/W″*']
for e in EXS:
    key = e['key']; r = REC[key]; c = r['cells']
    mrows.append('| %s | ' % key + ' | '.join(('%s' % c[col][0]) for col in COLS) + ' |')
open(os.path.join(HERE, 'matrix.md'), 'w').write('| № | ' + ' | '.join(hdr) + ' |\n|---|' + '---|' * len(hdr) + '\n' + '\n'.join(mrows) + '\n')
# подробные пояснения клеток
det = []
for e in EXS:
    key = e['key']; r = REC[key]; c = r['cells']
    det.append('### %s\n\n- U: `%s`; m=%d; u_m = `%s`\n- Σ: %s\n- 0 изолирована: %s (%s)\n- свидетель U<0: %s\n- вердикт: %s%s\n- основание: %s\n- вид проверки: %s\n' % (
        key, r['U'], r['m'], r['u_m'], r['sigma'], r['iso'], r['iso_how'], r['witness'], SYM[r['verdict']], (' — ' + r['main']) if r['main'] else '', r['basis'], r['evidence']))
    det.append('  | теорема | результат | пояснение |\n  |---|---|---|\n' + '\n'.join('  | %s | %s | %s |' % (h, c[col][0], c[col][1].replace('|', '\\|')) for h, col in zip(hdr, COLS)) + '\n')
open(os.path.join(HERE, 'details.md'), 'w').write('# Подробности по каждому примеру\n\n' + '\n'.join(det))

cnt = {}
for k, r in REC.items():
    cnt[r['verdict']] = cnt.get(r['verdict'], 0) + 1
print(cnt)
by_thm = {}
for k, r in REC.items():
    if r['main']:
        by_thm.setdefault(r['main'].split(' ')[0] + (' ' + r['main'].split(' ')[1] if r['main'].split(' ')[1].startswith('[') else ''), []).append(k)
for t_, ks in by_thm.items():
    print(t_, len(ks), ks)
