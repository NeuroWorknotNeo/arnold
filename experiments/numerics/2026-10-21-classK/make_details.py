"""make_details.py -- details.md: per example u_m, Sigma, Morse-Bott data, g_k, G, critical points of G (from out/*.json)."""
import json, os, sympy as sp
import comps
from comps import ALL, U
HERE = os.path.dirname(os.path.abspath(__file__))
S = json.load(open(os.path.join(HERE, 'summary.json')))
L = ['# Подробные результаты (автоматически из out/*.json)', '',
     'Обозначения: g_k — коэффициенты редуцированной функции R_ω(s)=Σ_{k>m} s^{k-m} g_k(ω) (лемма K1; нормировка на единичный ω, '
     'с учётом сдвига η*), G=g_j; t — параметр рациональной параметризации компоненты (см. comps.py); '
     'G\'\' — по натуральному параметру Σ (дуга единичной сферы). Все формулы в t — точные (sympy), числа — 25–30 знаков (mpmath) '
     'из точной изоляции вещественных корней. [Эксперимент: символьно, точно, где выписана формула.]', '']
for ex in ALL:
    d = S[ex]
    L += ['## %s' % ex, '', '- U = `%s`' % str(U[ex]), '- класс: **%s**; теорема: **%s**; вне K: %s' % (d['class'], d['theorem'], d['outside'])]
    if ex == 'T1':
        L += ['- m=6, u_6=C², C=y²z−x³−xz²; j=8, G=u_8|Σ=(y⁸/8−z⁸+yz⁷)|Σ (u_7=0). Критические точки G на Σ (одна на пару ±ω; G чётна), точно (результант, степень 29):', '']
        L += ['| ω | G | G\'\' | G\'\'+jG |', '|---|---|---|---|']
        for c in d['crit']:
            L.append('| %s | %s | %s | %s |' % (c['omega'], c['G'][:14], c['d2G'][:12], c['G2_plus_jG'][:12]))
        L.append('')
        continue
    r = json.load(open(os.path.join(HERE, 'out', ex + '.json')))
    L += ['- m=%d, u_m = `%s`; сертификат SOS: %s' % (r['m'], r['u_m'], r['sos_certificate_ok'])]
    for c in r['components']:
        L += ['', '### %s — %s' % (ex, c['name'])]
        if c.get('kind') == 'nonMB':
            L += ['не Морс–Ботт: D²u_m ≡ 0 на Σ (sigma_checks.txt); R_ω не определяется леммой K1.']
            continue
        if 'crit' in c or c.get('G_const'):
            L += ['- H(t)=D²u_m(p)(ν,ν) = `%s`; вещественные нули: %s ⇒ Морс–Ботт %s' % (c['H'], c['H_real_roots'], 'да' if c['MB_on_component'] else 'НЕТ (нули H — особые точки Σ)')]
            L += ['- g_k/нормировка: ' + '; '.join('g_%s = %s' % (k, v if len(v) < 200 else v[:200] + '…') for k, v in c['g_unit'].items() if v != '0')]
            L += ['- нулевые g_k: ' + ', '.join('g_%s' % k for k, v in c['g_unit'].items() if v == '0') if any(v == '0' for v in c['g_unit'].values()) else '- нулевых g_k среди k ≤ m+4 нет']
            L += ['- j = %d; G = `%s`' % (c['j'], c.get('G', c.get('G_value')))]
            if c.get('G_const'):
                L += ['- G постоянна (G\' ≡ 0)']
            for q in c.get('crit', []):
                L.append('  - крит. точка t=%s ω=%s: G=%s, G\'\'=%s, G\'\'+jG=%s, кратность нуля G\' = %s: **%s**' % (
                    q['t'][:12], q['omega'], q['G'][:14], q['d2G'][:14], (q['G2_plus_jG'] or '—')[:14], q['mult'], q['kind']))
        else:
            L += ['- точка; H (в базисе p^⊥) = %s, ведущие миноры %s ⇒ Морс–Ботт %s' % (c['H'], c['H_minors'], 'да' if c['MB'] else 'НЕТ')]
            L += ['- R_ω(s): ' + '; '.join('g_%s=%s' % (k, v) for k, v in c['g_unit'].items())]
            L += ['- j = %s, g_j = %s = %.6f (знак %s)' % (c['j'], c.get('g_j'), c.get('g_j_float', float('nan')), c.get('g_j_sign'))]
    L.append('')
open(os.path.join(HERE, 'details.md'), 'w').write('\n'.join(L))
