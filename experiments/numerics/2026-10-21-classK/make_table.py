"""make_table.py -- table.md (main summary table), from summary.json and valleys_compare.json"""
import json, os, math
HERE = os.path.dirname(os.path.abspath(__file__))
S = json.load(open(os.path.join(HERE, 'summary.json')))
VC = {r['id']: r for r in json.load(open(os.path.join(HERE, 'valleys_compare.json')))}
import comps
from kfib import homog_parts
um_str = {}
SIG = {
 'K1': '2 точки ±e_z', 'K2': '2 окружности Σ± (конус Q=0)', 'K3': '2 окружности Σ± (Q=0)', 'A1': '2 окружности Σ±', 'A2': '2 окружности Σ±',
 'A3': '2 окружности Σ±', 'A4': '2 окружности Σ±', 'A5': '2 окружности Σ±', 'A7': '2 окружности Σ± (Q=0)', 'C1': '2 овала Σ± (x²+2y²=z²)',
 'C2': '2 окружности Σ± (x²+y²=2z²)', 'D1': '2 окружности Σ± (Q=0)', 'D2': '2 окружности Σ±', 'F1': 'большой круг z=0',
 'M1': 'большой круг z=0', 'M2': 'большой круг z=0', 'P1': '2 точки ±e_z', 'P3': '8 точек (±1,±1,±1)/√3', 'P4': '6 точек ±e_i',
 'Z1': 'круг z=0 ∪ 2 полюса', 'S1': '2 больших круга x=±y; особые точки ±e_z', 'T1': '1 гладкая замкнутая кривая (кубика C=0)'}
MBS = {k: 'да' for k in SIG}
for k in ('K1', 'P1'): MBS[k] = 'НЕТ: D²u_4(±e_z)=0 (x⁴+y⁴)'
for k in ('M1', 'M2'): MBS[k] = 'НЕТ: D²u_4≡0 на Σ (z⁴)'
MBS['S1'] = 'нет в ±e_z (H=32(t²−2)²=0), да вне них'
for k in ('P3', 'P4'): MBS[k] = 'да (H≻0 во всех точках)'
MBS['Z1'] = 'да (круг: H=2(t²+1)²; полюса: H=2I)'
def f(v, n=5):
    return ('%.' + str(n) + 'g') % float(v)
rows = []
hdr = '| № | u_m (m) | Σ | Морс–Ботт | j | G; его (глоб.) минимум | G″+jG в нём | класс | применимая теорема | согласие с valleys |'
rows.append(hdr); rows.append('|' + '---|'*10)
for ex in comps.ALL:
    d = S[ex]; vc = VC[ex]
    m = d['m']
    umf = {'K1': 'x⁴+y⁴', 'P1': 'x⁴+y⁴', 'M1': 'z⁴', 'M2': 'z⁴', 'F1': 'z²·‖q‖²', 'Z1': 'z²(x²+y²)', 'S1': '(x²−y²)²', 'P3': '(x²−z²)²+(y²−z²)²',
           'P4': 'x²y²+y²z²+z²x²', 'T1': 'C², C=y²z−x³−xz²', 'A7': 'Q²·‖q‖²', 'C1': '(x²+2y²−z²)²', 'C2': '(x²+y²−2z²)²'}.get(ex, 'Q²')
    umcol = '%s (%d)' % (umf, m)
    jcol = '—'; Gcol = '—'; k1col = '—'
    if ex == 'T1':
        jcol = '8'; Gcol = 'u_8 на Σ; min = %s при ω=(%s)' % (f(d['best']['G'], 7), ', '.join('%.4f' % float(a) for a in d['best']['omega'])); k1col = f(d['best']['k1'], 4)
    elif ex in ('P3', 'P4'):
        pts = [c for c in d['comps'] if c.get('g_j_sign', 0) < 0]
        js = sorted(set(c['j'] for c in pts))
        jmin = min(js)
        best = min([c for c in pts if c['j'] == jmin], key=lambda c: c['g_j_float'])
        jcol = '5 (4 точки: g_5=∓2√3/27), 6 (4 точки)' if ex == 'P3' else '5 (±e_x,±e_y: g_5=∓1), 6 (±e_z: g_6=+1)'
        Gcol = 'g_5(%s)=%s = −2√3/27' % (best['name'], f(best['g_j_float'], 6)) if ex == 'P3' else 'g_5(−e_x)=g_5(−e_y)=−1'
        k1col = '—'
        if ex == 'P3':
            Gcol += '; в 4 точках j=6, g_6=−17/432'
    elif ex in ('K1', 'P1', 'M1', 'M2'):
        pass
    elif d['const_neg']:
        n, j, g = d['const_neg'][0]
        jcol = str(j); Gcol = 'G ≡ −1/16 (const) на Σ±; следующий g_9 не const (min −0.3842)'; k1col = '—'
    elif ex == 'A4':
        jcol = '6'; Gcol = 'min G = 0 (двойной нуль в ω₀=(1,0,1)/√2, G″=0.25); G≥0; g_7(ω₀)=−√2/16<0'; k1col = '—'
    else:
        curves = [c for c in d['comps'] if 'crit' in c]
        negmins = d['K2_cands']
        if curves:
            jcol = str(curves[0]['j'])
        pts = [c for c in d['comps'] if 'g_j' in c]
        parts = []
        if negmins:
            n, j, q = min(negmins, key=lambda c: float(c[2]['G']))
            parts.append('min G = %s при ω=(%s)' % (f(q['G'], 7), ', '.join('%.4f' % float(a) for a in q['omega'])))
            k1col = '%s (G″=%s)' % (f(q['G2_plus_jG'], 4), f(q['d2G'], 4))
        if ex == 'Z1':
            parts.append('полюс −e_z: g_5=−1')
            jcol = '5'
        Gcol = '; '.join(parts)
    # agreement with valleys
    ag = []
    if 'beta_p' in vc:
        ag.append('β=j=%d ✓' % vc['beta_p'] if abs(vc['beta_p'] - vc['beta_v']) < 1e-9 else 'β: j=%s, valleys %s ✗' % (vc['beta_p'], vc['beta_v']))
        ag.append('a=−G_min: %s vs %s %s' % (f(vc['a_p'], 5), f(vc['a_v'], 5), '✓' if abs(vc['a_p'] - vc['a_v']) < 2e-5*vc['a_v'] else '✗'))
        if 'om_dist' in vc:
            ag.append('ω∞=argmin G ✓ (%.0e)' % vc['om_dist'] if vc['om_dist'] < 1e-5 else 'ω∞: расхождение %.2g ✗' % vc['om_dist'])
        elif 'om_p' in vc:
            ag.append('ω∞=%s ✓' % vc['om_p'])
        if 'rho_p' in vc:
            ag.append('ρ=(G″+jG)/(−jG)=%s vs %s %s' % (f(vc['rho_p'], 4), f(vc['rho_v'], 4), '✓' if abs(vc['rho_p'] - vc['rho_v']) < 2e-4 else '✗'))
    if ex == 'A4':
        ag = ['β=7 ✓ (= из g_7(ω₀)); a=√2/16=0.08839 ✓; ω∞=ω₀ ✓; valleys: класс i-a (c>1)']
    if ex == 'D1':
        ag = ['β=j=8 ✓; a=1/16 ✓; ω∞ = точка min g_9 на Σ₋ (t=−6.0197) ✓; valleys: ii-b']
    if ex in ('K1', 'P1', 'M1', 'M2'):
        w = {'K1': 'β=6, c=(3/2,3/2)', 'P1': 'β=6, c=(3/2,3/2)', 'M1': 'β=5, c=(1,5/4)', 'M2': 'β=16/3, c=(1,4/3)'}[ex]
        ag = ['сверка с §10.2 п.4: c=(j−m+4)/4=β/4 для нормального веса: valleys %s ✓; класс valleys: %s' % (w, {'K1': 'ii-a', 'P1': 'ii-a', 'M1': 'ii-a', 'M2': 'i-a'}[ex])]
    if ex in ('P3', 'P4'):
        ag.append('c=(3/2,3/2)=(j−m+2)/2 ✓')
    rows.append('| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (ex, umcol, SIG[ex], MBS[ex], jcol, Gcol, k1col, d['class'], d['theorem'] + ('' if d['outside'] == '—' else '; ' + d['outside']), '; '.join(ag)))
open(os.path.join(HERE, 'table_raw.md'), 'w').write('\n'.join(rows))
print('\n'.join(rows[:6]))
