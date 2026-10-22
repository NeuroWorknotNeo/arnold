"""build_readme.py -- собрать README.md из README_template.md, table.md, matrix.md, coverage.json, mt_ring_summary.json, логов фоновых расчётов."""
import json, os, re, glob, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
R = lambda fn: open(os.path.join(HERE, fn)).read()
cov = json.load(open(os.path.join(HERE, 'coverage.json')))

# ---- сводка
cnt = {}
for k, r in cov.items():
    cnt[r['verdict']] = cnt.get(r['verdict'], 0) + 1
by = {}
for k, r in cov.items():
    if r['verdict'] in ('ok', 'ok_num'):
        t = r['main']
        key = ('M [010]' if t.startswith('M [010]') else 'Q [012]' if t.startswith('Q [012]') else "M′/N [014],[011] (постоянная кратность 2r = 4)" if t.startswith('M′') else
               'K1 [008] (локальная теорема на гладкой дуге)' if t.startswith('K1') else "X′ [013]" if t.startswith('X′') else 'S [013] (численно)' if t.startswith('S ') else 'E [012]' if t.startswith('E ') else t)
        by.setdefault(key, []).append(k)
lines = ['| итог | число | примеры |', '|---|---|---|']
tot_ok = cnt.get('ok', 0)
lines.append('| **покрыт принятой теоремой, условия проверены точно** | %d | см. строки ниже |' % tot_ok)
for key, ks in by.items():
    if key.startswith('S [013]'):
        continue
    lines.append('| &nbsp;&nbsp;— %s | %d | %s |' % (key, len(ks), ', '.join(ks)))
lines.append('| **покрыт теоремой S [013], неравенства проверены численно** | %d | %s |' % (cnt.get('ok_num', 0), ', '.join(by.get('S [013] (численно)', []))))
lines.append('| **покрыт только условно** (MT/H [015], статика проверена численно) | %d | %s |' % (cnt.get('cond', 0), ', '.join(k for k, r in cov.items() if r['verdict'] == 'cond')))
lines.append('| **не покрыт** | %d | %s |' % (cnt.get('no', 0), ', '.join(k for k, r in cov.items() if r['verdict'] == 'no')))
lines.append('| всего | %d | |' % len(cov))
summary = '\n'.join(lines)

groups = '''### Группа I — дно в точке падения нормальной кратности, где G определена, но условия данных нарушены: **f:A2**

Σ = экватор, нормальная кратность 2 → 4 в ±e_x (u_4 = z²(y² + z²), g = y² + z² обращается в 0 в ±e_x). Эффективный потенциал
G(φ) = −cos⁶φ/8 + sin⁶φ + cos⁴φ sin²φ (j = 6) аналитичен и имеет невырожденный минимум −1/8 при φ = 0, π; **но** именно там H = D²u_4(n,n) = 2 sin²φ = 0, условие (S)
теорем K1, K2, N, W и Mb нарушено (поправка следующего порядка ∼ r²/(16 φ⁴) не ограничена); других отрицательных минимумов G нет (критические точки: максимумы G = 1 при t = ±1, минимумы только при t = 0, ∞).
M, M′ неприменимы (постоянная кратность нарушена). Прямая карта (утверждение Q, 2U, C′): дно по экватору имеет ширину ∝ r (c = 0.995, N5), а [012] требует весов c_i > 1 и коэрцитивности в окне |b| < r_1
(при c_y > 1 окно слишком узко и 𝒲 в нём почти не зависит от b_y — (U3) нарушено). Полярная теорема S [013]: (S3) W(r, 0) = 1/4 + a_0 в базовой точке e_x, а на любой другой точке экватора
a_0 ≤ −u_6|_Σ ≤ 0, т. е. условие a_0 > 0 невозможно. Условно MT: см. ниже.
*Что нужно*: теорема о дне в точке падения кратности с двумя несоизмеримыми масштабами (по углу ∼ r^{1/3}, по нормали ∼ r^{5/3}); критическая точка по нормали ∼ (r θ)^{1/3} не аналитична по θ в θ = 0.

### Группа II — изолированный вырожденный нуль u_m, подовраги неоднородны (плохая ориентация): **f:V4**

Σ = {±e_x}, D²u_m = 0. Точная реализация профиля §6.2 [009] с весами c = (2, 3) (b_1 = y/x² шире, b_2 = z/x³ уже): (Q1), (Q2) выполнены (Q = A·B, F_0(0) = −1),
но Q_4 = w_1⁴ ⇒ Q_d(0, 1) = 0 при c_1 < c_2, следствие E неприменимо; SV неприменимо (подовраги касаются *узкой* оси); по [009, пр. 6.2] нет липшицева поля Эйлера с ξ_1 = f(b_1) — условие (T) теоремы 2U недостижимо.
В полярной карте (теорема S) подовраги b_1 = b_2² и b_1 = b_2² + b_2³ в переменных θ имеют вид θ_y = θ_z²/r³ и т. д. — зависят от r, фиксированное поле ξ(θ) не может быть касательным к ним (в отличие от V1, V2 с однородными формами).
Изолированность 0 — точно (двойное насыщение, 959 с). *Что нужно*: поле Эйлера, зависящее от s, либо иная конструкция — вне принятых теорем.

### Группа III — плоское кольцо G ≡ const на компоненте Σ с узлами касания: **f:D1, D2, D3, D4** — *условно* покрыты MT [015]

Σ = C1 ∪ C2 (коники x² + y² = z² и x²/2 + y² = z²), касание порядка 2 в четырёх точках (0, ±1, ±1)/√2; G = u_9|_Σ ≡ −2^{−9/2} на C1 (D3, D4 — с точно нулевой нормальной силой), на C2 минимум G только в узлах.
M, M′ неприменимы (Σ не многообразие), K1/K2/N/W — нет дуги с G″ > 0 (на кольце G ≡ const, (W1) — нуль 𝒲 неизолирован), S — (S1) нарушено вдоль кольца (W = O(r) при |θ| ∼ θ_0), C [014] — P(θ, e) ≥ q_0(|e|) нарушено в узлах
(кратность 2 → 4). Дно выбирается следующим порядком (D1: y z⁹ — узел, N5: сдвиг ∼ r^{1/3}; D3: x·P — гладкая точка кольца; D4: y·P — узел). MT от выбора не зависит (см. раздел «Условно»).
'''

# ---- MT ring
ms = json.load(open(os.path.join(HERE, 'mt_ring_summary.json')))
ml = ['| пример | (F) min 𝒲/r^{1/3} | (E) κ→0⁺: min / r^{1/3} | (E) κ=κ_0: min / r^{1/3} | (W) min_{∂K} 𝒲 / δ | замечание |', '|---|---|---|---|---|---|']
for k, v in ms.items():
    ml.append('| %s | %.3f | %.3f | %.3f | %.2f | w_0 = %s, δ = %s |' % (k, v['min_F'], v['min_E_k0plus'], v['min_E_kappa0'], v['min_wall_over_delta'], '0.2' if k in ('f:D1', 'f:D2') else '0.12', '0.2 a_0' if k in ('f:D1', 'f:D2') else '1e-4'))
mtring = '\n'.join(ml)

# ---- sat2
def head(fn):
    p = os.path.join(HERE, 'logs', fn)
    return open(p).read().strip() if os.path.exists(p) else '(нет файла)'
sat = ['| пример | индикатор над 𝔽_32003 (`logs/satp_*.log`) | сертификат над ℚ (`logs/sat2_*.log`) |', '|---|---|---|']
for ident in ('D3', 'D4', 'V3'):
    p = head('satp_%s.log' % ident) or '(идёт)'
    q = head('sat2_%s.log' % ident)
    q = q.splitlines()[-1][:160] if q and q != '(нет файла)' else '(нет файла: фаза 2 ещё не началась или идёт)'
    sat.append('| %s | %s | %s |' % (ident, p.splitlines()[-1][:170] if p else '(идёт)', q))
pid = head('queue_sat2.pid')
alive = subprocess.run(['bash', '-c', 'ps -p %s >/dev/null 2>&1 && echo жив || echo завершён' % pid], capture_output=True, text=True).stdout.strip() if pid.isdigit() else '—'
kids = subprocess.run(['bash', '-c', "ps -eo pid,etime,rss,args | grep -E 'iso_sat2|Singular' | grep -v grep | cut -c1-150"], capture_output=True, text=True).stdout.strip()
satt = '\n'.join(sat) + '\n\nPID очереди: %s (%s на момент сборки README). Дочерние процессы на момент сборки (pid, время, RSS кБ, команда):\n\n```\n%s\n```' % (pid, alive, kids or '(нет)')

t = R('README_template.md')
t = t.replace('{{SUMMARY}}', summary).replace('{{TABLE}}', R('table.md')).replace('{{MATRIX}}', R('matrix.md')).replace('{{GROUPS}}', groups).replace('{{MTRING}}', mtring).replace('{{SAT}}', satt)
open(os.path.join(HERE, 'README.md'), 'w').write(t)
print(len(t), 'chars')
