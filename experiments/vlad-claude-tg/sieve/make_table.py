import json, collections, re
src = {'A': 'families_results_v1.json', 'B': 'families_results_B.json',
       'C': 'families_results_C.json', 'D': 'families_results_v1.json'}
desc = {'A': r'общие разреженные, степени 2--6', 'B': r'$U_2=U_3=0$, степени 4--6',
        'C': r'$(x^2+y^2-z^2)^2+W$, $\deg W=5..8$', 'D': r'неотр. квартика с конечн. нулями $+W$'}
cols = ['TOTALLY_UNSTABLE', 'UNSTABLE', 'MIN', 'NONISOLATED', 'UNDECIDED', 'SUSPICIOUS']
rows = []; surv = {}
for f in 'ABCD':
    try: R = json.load(open(src[f]))[f]
    except Exception as e: print('missing', f, e); continue
    c = collections.Counter(v for _, v, _, _ in R)
    rows.append((f, len(R), [c.get(k, 0) for k in cols]))
    kinds = collections.Counter()
    for s, v, why, _ in R:
        if v != 'SUSPICIOUS': continue
        if 'corank-2' in why: kinds['коранг 2, вырожденный приведённый потенциал'] += 1
        elif 'multiplicity' in why: kinds['жёлоб кратности $\\ge4$ (не Морс--Ботт)'] += 1
        elif 'vanishes identically' in why: kinds['эфф. потенциал тождественно 0 (жёлоб надо <<искать>>)'] += 1
        elif 'touching' in why: kinds['касающийся (чётнократный) нуль эфф. потенциала'] += 1
        elif 'odd-order' in why: kinds['нечётнократный нуль эфф. потенциала'] += 1
        elif 'degenerate transverse' in why: kinds['нулевое направление с вырожденной поперечной частью'] += 1
        else: kinds['прочее'] += 1
    surv[f] = kinds
lines = [r'\begin{center}\small', r'\begin{tabular}{llrrrrrrr}', r'\toprule',
         r'Сем. & Описание & $N$ & тот.\,неуст. & неуст. & мин. & неизол. & не реш. & подозр.\\', r'\midrule']
for f, n, v in rows:
    lines.append('%s & %s & %d & %s\\\\' % (f, desc[f], n, ' & '.join(str(t) for t in v)))
lines += [r'\bottomrule', r'\end{tabular}', r'\end{center}']
lines.append(r'Причины, по которым выживают <<подозрительные>>:')
lines.append(r'\begin{itemize}[leftmargin=*]')
for f in 'ABCD':
    if f in surv and surv[f]:
        lines.append(r'\item \textbf{%s}: ' % f + '; '.join('%s --- %d' % (k, v) for k, v in surv[f].most_common()) + '.')
lines.append(r'\end{itemize}')
open('results_table.tex', 'w').write('\n'.join(lines))
print('\n'.join(lines))
