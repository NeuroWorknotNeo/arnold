# (GT3) для «жёсткого ядра» при $n=3$: класс $\mathcal K$ и асимптотические траектории

- **Автор:** prover (агент), 21.10.2026. Задание главного агента (этап 2, главная линия): доказать
  существование асимптотической траектории для широкого подкласса жёсткого ядра задачи (A) при
  $n=3$, проверив достаточное условие (GT3).
- **Опирается на:** [GT3] = `notes/prover/2026-10-21-gt3.md` (теорема A, леммы 1–2, теорема 2,
  следствия 1–2; [Проверено: reviewer, 21.10.2026, `notes/reviewer/2026-10-21-gt3.md`]);
  [B] = `results/002-theorem-B.md` (§2.1(f), §2.2: аналитичность $\Sigma$ и нормальной рамки);
  `notes/vlad-claude-tg/example13-proof.md` §6–7; `notes/literature/2026-10-21-jet-conjecture.md`,
  `notes/literature/2026-10-21-revision-rest.md` (что покрыто литературой).
- **Скрипты [Эксперимент]:** `experiments/prover/gt3-hardcore/` (список и выводы — §9.8) и
  `experiments/prover/gt3-result008/` (явные семейства §9.7).
- **Рецензии:** R20 (`notes/reviewer/2026-10-21-gt3-hardcore-A.md`: §2–§5, §10.1), R21
  (`...-B.md`: §7), R22 (`...-C.md`: §6, §8, §9.6–9.7). В основных утверждениях ошибок не найдено;
  неверной в формулировке оказалась только первая половина K4(c) (критерий минимума при
  $R_\omega\equiv0$). Все замечания внесены 21.10.2026 (места помечены ссылками на отзывы);
  оформленный результат — `results/008-class-K.md`.
- **Переобозначения по сравнению с [GT3]** (чтобы не путать с точкой $\omega\in\Sigma$ и нормальной
  координатой $\eta$): малая функция $\omega(x)$ из $(\Phi1)$–$(\Phi3)$ [GT3] здесь обозначена
  $\varpi(x)$; переменная $s=x^{1/N}$ из (F) [GT3] — $\sigma$; погрешность $\eta(s)$ из шага 3
  теоремы 2 [GT3] — $\eta_F$.

## 0. Итог

| № | Утверждение | Статус |
|---|---|---|
| Лемма K1 | Критическая точка в нормальном слое: аналитический «сдвиг» $\eta^*$, редуцированная функция $R(s,\theta)=\sum_{k>m}s^{k-m}g_k(\theta)$ | [Доказано] |
| Лемма K2 | Нормальная форма $U=s^j\tilde F(s^{1/2},\theta,e)$ около конуса нулей, $\tilde F(0,\theta,e)=G(\theta)+\frac12e^{\mathsf T}H(\theta)e$ | [Доказано] |
| Определение | Эффективный потенциал $G=g_j$ и класс $\mathcal K=\mathcal K^0\cup\mathcal K^1$ | — |
| Теорема K0 | $s=0$, любое $n\ge2$: луч Морса–Ботта $\omega^*$ с $g_j(\omega^*)<0$ $\Rightarrow$ асимптотическая траектория (через теорему 2 [GT3]) | [Доказано] |
| Следствие K0′ | Любое $n\ge2$: $u_m\ge0$, нули $u_m|_{S^{n-1}}$ конечны и невырождены $\Rightarrow$ строгий минимум, или неизолированная критическая точка, или асимптотическая траектория (два последних совместимы). **Задача (A) в этом классе решена** | [Доказано] |
| Лемма K3 | Трубка конуса над дугой $\Sigma\subset S^2$: диффеоморфизм, $\nabla s=\omega(\theta)$ | [Доказано] |
| Теорема K1 | $s=1$, $n=3$, $G''+jG>0$ в точке минимума: декартова карта развёртки, теорема 2 [GT3] | [Доказано] |
| Лемма 2′, теорема 2′ | Вариант теоремы 2 [GT3]: перекрёстные члены, линейные по $\lvert b\rvert$, допускаются при $\Gamma_*^2\le\beta\mu$ | [Доказано] (новое, на проверку) |
| Теорема K2 | $s=1$, $n=3$, только $G''>0$: поворачивающаяся полярная карта с малым $\kappa$, теорема 2′ | [Доказано] (зависит от теоремы 2′) |
| §9 | Примеры: пример 13, пример теоремы B, $Q_0^2+W_5$, $Q_0^2+W_7$, пример со сдвигом, два примера с «искривлённым дном» ($s=0$ и $s=1$), для которых не работают ни радиальное условие Четаева, ни класс $\mathcal H$ | выкладки [Эксперимент], принадлежность классу [Доказано] по формулам |
| Предложение K4 | $n=3$, $\Sigma$ Морса–Ботта: критические точки $U$ около конуса $\leftrightarrow$ критические точки функции дна; минимум $\Leftrightarrow$ функция дна $\ge0$ и $R_\omega\ge0$ в точечных компонентах (исправлено по R20) | [Доказано] |
| Следствие K4′ | Если $0$ — регулярное значение $G$ на каждой кривой-компоненте и $j<\infty$ в точечных, то $0$ — изолированная критическая точка | [Доказано] |
| §10 | Вне $\mathcal K$: постоянный $G$ на замкнутой компоненте, вырожденный минимум $G$, каскад, не-Морс–Ботт; подходы | [Эскиз] / [Гипотеза] |

**Главное.**

1. «Сдвиги» и «выбор $j$» корректно определяются через **критическую точку $U$ в нормальном
   слое** конуса нулей (лемма K1): $U_{\rm red}(s\omega)=U(s\omega+\eta^*(s\omega))=\sum_{k>m}s^kg_k(\omega)$,
   $j$ — первый номер с $g_k\not\equiv0$, $G=g_j$. Это канонично (не зависит от рамок и
   параметризаций) и задаётся струёй $j^jU$.
2. **$s=0$ (конечное число нулевых лучей) решено полностью при любом $n$** (следствие K0′): если
   $u_m\ge0$ и $u_m|_{S^{n-1}}$ невырожден в своих нулях, то изолированная неминимальная критическая
   точка имеет асимптотическую траекторию. Это прямое применение уже проверенной теоремы 2 [GT3]
   (следствие 2: прямая карта $w=y-\gamma(x)$ с $\gamma=\eta^*$).
3. **$s=1$, $n=3$.** Вопреки ожиданию, условия «$G''(\omega^*)>0$» для прямого применения теоремы 2
   [GT3] **не хватает**: декартов срез развёртки конуса даёт поперечный гессиан
   $G''+jG$ (теорема K1), а он отрицателен, например, у примера теоремы B
   ($G''+5G=-3\sqrt2/8$). Чтобы обойтись одним $G''>0$, нужна новая карта (поле $Y$ слегка
   «поворачивает» к лучу, вес $\kappa$ по углу) и вариант теоремы 2, в котором перекрёстные члены
   порядка $\kappa\lvert b\rvert$ гасятся неравенством о среднем арифметическом и геометрическом (теорема 2′). Получается
   теорема K2: **$G(\omega^*)<0$, $G'(\omega^*)=0$, $G''(\omega^*)>0$ достаточно.**
4. Двухчленные примеры ($Q_0^2+W$ с однородным $W$, пример 13, пример теоремы B) удовлетворяют
   радиальному условию Четаева $\langle\nabla U,q\rangle<0$ на $\{U<0\}$, так что неустойчивость там
   следует и из классики. **Новое — «искривлённое дно»** ($c=(j-m+2)/2>2$ и
   $\eta^*\not\equiv O(s^3)$): примеры $(x^2-z^2+z^3)^2+(y^2-z^2)^2+z^7$ ($s=0$) и
   $(x^2+y^2-z^2+z^3)^2+xz^6+xyz^5+\frac12z^7$ ($s=1$) — гессиан нулевой, $u_4\ge0$, точка изолирована, радиальное
   условие Четаева нарушено в каждой компоненте $\{U<0\}$ (явные семейства точек, §9.7; численно —
   у 34–48 % точек около дна), класс $\mathcal H$ Alva–Garcia не применим (по конспекту (H3));
   $U_{(8)}$ изолирована над $\mathbb R$, но не над $\mathbb C$; теоремы K0, K2 дают асимптотическую траекторию.
5. При $n=3$ и $\Sigma$ Морса–Ботта задача (A) сводится к двумерной «задаче на дне» (предложение
   K4); класс $\mathcal K$ — её невырожденный случай. Что осталось — §10.

**Чего нет.** Не доказано (A) для всего жёсткого ядра при $n=3$: вне $\mathcal K$ остаются
вырожденные минимумы $G$, каскады ($G\ge0$ с нулями), не-Морс–Ботт и особые $\Sigma$ (§10).

## 1. Что уточнено в постановке задания

1. **Эффективный потенциал** (п. 1 задания) определён через точную критическую точку $U$ в
   нормальном слое $s\omega+N_\omega$ (лемма K1), а не через конечный набор сдвигов. Тогда
   линейных по нормали членов нет вовсе (лемма K2), а $j$ — первый номер, при котором
   $g_k\not\equiv0$ на компоненте $\Sigma_0\ni\omega^*$. Формулы для первых $g_k$ — замечание 2 в §3.3.
   Без сдвига эффективный потенциал может быть неверным: в примере §9.5 ограничение $u_6|_\Sigma$
   постоянно, а истинный $G=g_6$ имеет невырожденные минимумы.
2. **Невырожденный минимум $G$ при $s=1$ не даёт карты теоремы 2 [GT3] автоматически.** Декартов
   срез развёртки конуса (как в примере 13) требует $G''+jG>0$ (теорема K1). При $G''>0\ge G''+jG$
   я доказываю асимптотическую траекторию через новую теорему 2′ (вариант теоремы 2 с
   перекрёстными членами) и поворачивающуюся полярную карту (теорема K2). Теорема 2′ — новое
   утверждение, ему нужна независимая проверка. Это то же явление, что численно нашёл агент
   numerics (`experiments/numerics/2026-10-21-valleys/README.md`, [Эксперимент]): гессиан в плоском
   срезе $H_{\rm plane}=\lambda_{\text{мягк}}/r^{\beta-2}-\beta a$ (в моих обозначениях $G''+jG$, $a=-G$)
   отрицателен у A1, A2, A5, A7, C2 и K3 (пример теоремы B) полигона, хотя минимум на сфере
   невырожден, а стрельба назад сходится. Чистые срезы сферами $\lvert q\rvert=\rho$ с радиальным $Y$
   (то есть $\kappa=0$) не годятся: углового запаса в неравенстве Эйлера нет (замечание 6.1, §9.8);
   нужен малый поворот $\kappa>0$. Относятся ли A1, A2, A5, A7, C2 к классу $\mathcal K$
   (Морс–Ботт, $s\le1$, невырожденный минимум $G$), я не проверял.
3. **Локальность.** Для теорем K0–K2 условия нужны только около $\omega^*$: $u_m(\omega^*)=0$,
   $\nabla u_m(\omega^*)=0$ (это так, если $u_m\ge0$ около $\omega^*$), гладкость $\Sigma$ около
   $\omega^*$ и положительность $D^2u_m$ на нормалях. Глобальные $u_m\ge0$ и гладкость всего
   $\Sigma$ нужны только в следствии K0′ и предложении K4.
4. **$m$.** Задание требует $m\ge4$ (жёсткое ядро: гессиан нулевой). Все доказательства годятся и
   при $m=2$, но этот случай покрыт FGT08 [Литература: FGT08, Thm A, по
   `notes/literature/2026-10-21-jet-conjecture.md` §2.3] и Козловым 1986 [Литература: Zbl 0631.70018, по
   `notes/literature/2026-10-21-revision-rest.md` §1.3].
5. **Случай $s=0$** решён при любом $n$, а не только при $n=3$; случай $s=1$ — при $n=3$
   (обобщение на $n\ge4$ — замечание 8.4, [Эскиз]).

## 2. Обозначения

$U$ вещественно-аналитична в шаре $B_{\rho_0}\subset\mathbb R^n$, $U(0)=0$, $U=\sum_{k\ge m}u_k$
(однородные многочлены, $u_m\not\equiv0$, $m\ge2$; ряд Тейлора сходится абсолютно при
$\max_i\lvert q_i\rvert\le R_0$). Система $\ddot q=-\nabla U(q)$. «Асимптотическая траектория» —
решение $q(t)\ne0$, $t\ge0$, с $q(t)\to0$, $\dot q(t)\to0$ при $t\to+\infty$; по теореме A [GT3],
шаг 6, из неё следует неустойчивость по Ляпунову.

$Z=\{u_m=0\}$, $\Sigma=Z\cap S^{n-1}$; для $\omega\in\Sigma$, около которой $\Sigma$ — гладкое
подмногообразие, $N_\omega=(\mathbb R\omega\oplus T_\omega\Sigma)^\perp$ (при изолированной точке
$\Sigma$ это $\omega^\perp$).

## 3. Нормальная форма около конуса нулей

### 3.1. Данные

**(S)** Пусть $d\in\{0,1\}$, $\Lambda'$ — открытый интервал в $\mathbb R$ (при $d=0$ — точка),
$\Lambda\subset\Lambda'$ — компактный интервал (при $d=0$ — та же точка), и заданы аналитические
$\omega:\Lambda'\to S^{n-1}$ (инъективная иммерсия при $d=1$) и $e_1,\dots,e_p:\Lambda'\to\mathbb R^n$,
$p=n-1-d$, такие, что при всех $\theta\in\Lambda'$:

- $u_m(\omega(\theta))=0$ и $\nabla u_m(\omega(\theta))=0$;
- $e_1(\theta),\dots,e_p(\theta)$ — ортонормированный базис
  $N_\theta:=(\operatorname{span}(\omega(\theta),\omega'(\theta)))^\perp$ (при $d=0$:
  $N=\omega^\perp$);
- $H(\theta):=\big(D^2u_m(\omega(\theta))(e_a(\theta),e_b(\theta))\big)_{a,b\le p}$ положительно
  определена.

Если $u_m\ge0$ около $\omega(\theta)$, первое условие влечёт второе (минимум). Если выполнены (K1),
(K2) из §4, то $\Sigma$ — аналитическое подмногообразие и аналитическая ортонормированная рамка
нормалей существует [B, §2.1(f), §2.2]; при $n=3$, $d=1$ годится $e_1=n(\theta)=\omega\times\omega'$
(натуральный параметр). В [B] условие (B1) требует, чтобы все компоненты $\Sigma$ имели одну
размерность, а в (K1) размерности бывают разные; используемые рассуждения [B, §2.1(f), §2.2]
локальны (нужны только $Z=\{\nabla u_m=0\}$ и невырожденность $D^2u_m$ на $N$), так что ссылка
законна (отзыв R20, замечание 9).

Положим $\lambda_H:=\min_{\theta\in\Lambda}\lambda_{\min}(H(\theta))>0$ и

$$
\varphi(s,\theta,y):=\sum_{k\ge m}s^{k-m}u_k\Big(\omega(\theta)+\sum_{a=1}^py_ae_a(\theta)\Big).\tag{3.1}
$$

*Аналитичность и смысл $\varphi$.* Ряд $\tilde\varphi(s,z)=\sum_\alpha c_\alpha s^{\lvert\alpha\rvert-m}z^\alpha$
($c_\alpha$ — коэффициенты Тейлора $U$) мажорируется рядом
$3^mR_0^{-m}\sum_\alpha\lvert c_\alpha\rvert R_0^{\lvert\alpha\rvert}<\infty$ при $\lvert s\rvert<R_0/3$,
$\max_i\lvert z_i\rvert<3$; значит, $\tilde\varphi$ аналитична там (как в [B, лемма 2, п. 1]). При
$\lvert y\rvert<1$ имеем $\lvert\omega+\sum y_ae_a\rvert<2$, поэтому
$\varphi(s,\theta,y)=\tilde\varphi(s,\omega(\theta)+\sum y_ae_a(\theta))$ аналитична на
$(-R_0/3,R_0/3)\times\Lambda'\times\{\lvert y\rvert<1\}$, и для этих $s$ (любого знака)

$$
U\Big(s\big(\omega(\theta)+\textstyle\sum_ay_ae_a(\theta)\big)\Big)=s^m\varphi(s,\theta,y).\tag{3.2}
$$

### 3.2. Лемма K1 (критическая точка в слое) [Доказано]

**Лемма K1.** В условиях (S) найдутся $s_1>0$, $y_1\in(0,1)$ и открытый интервал
$\Lambda''$, $\Lambda\subset\Lambda''$, $\overline{\Lambda''}\subset\Lambda'$ (при $d=0$ — точка), такие, что при
$\lvert s\rvert<s_1$, $\theta\in\Lambda''$:

1. $\partial_y^2\varphi(s,\theta,y)\succeq\frac{\lambda_H}2I$ при $\lvert y\rvert<y_1$;
2. функция $y\mapsto\varphi(s,\theta,y)$ имеет в шаре $\lvert y\rvert<y_1$ ровно одну критическую
   точку $y^*(s,\theta)$; она лежит в шаре $\lvert y\rvert<y_1/2$ и является точкой глобального
   минимума $\varphi(s,\theta,\cdot)$ на шаре $\lvert y\rvert<y_1$;
3. $y^*$ аналитична по $(s,\theta)$ и $y^*(0,\theta)=0$.

*Доказательство.*

1. $\partial_y^2\varphi(0,\theta,0)=H(\theta)\succeq\lambda_HI$ на компакте $\Lambda$. По
   непрерывности $\partial_y^2\varphi$ на компактной окрестности $\{0\}\times\Lambda\times\{0\}$
   найдутся $s_1,y_1,\Lambda''$ с п. 1 (при $\lvert s\rvert\le s_1$, $\theta\in\overline{\Lambda''}$,
   $\lvert y\rvert\le y_1$).
2. $\partial_{y_a}\varphi(0,\theta,0)=\langle\nabla u_m(\omega(\theta)),e_a(\theta)\rangle=0$.
   Уменьшив $s_1$, получим $\lvert\partial_y\varphi(s,\theta,0)\rvert<\lambda_Hy_1/16$. Для
   $g(y)=\varphi(s,\theta,y)$ по п. 1 $g(y)\ge g(0)+\langle\nabla g(0),y\rangle+\frac{\lambda_H}4\lvert y\rvert^2$,
   поэтому при $y_1/2\le\lvert y\rvert<y_1$:
   $g(y)-g(0)\ge\lvert y\rvert\big(\frac{\lambda_H}4\cdot\frac{y_1}2-\frac{\lambda_Hy_1}{16}\big)>0$.
   Значит, минимум $g$ на замкнутом шаре $\lvert y\rvert\le y_1/2$ достигается внутри, это
   критическая точка $y^*$. Строгая выпуклость $g$ на шаре $\lvert y\rvert<y_1$ даёт
   единственность критической точки и то, что $y^*$ — глобальный минимум на этом шаре.
3. В точке $(s_0,\theta_0,y^*(s_0,\theta_0))$ матрица $\partial_y^2\varphi$ обратима, и по
   аналитической теореме о неявной функции (она получается из теоремы об обратной функции [B, (F1)],
   применённой к $(s,\theta,y)\mapsto(s,\theta,\partial_y\varphi)$) решение уравнения $\partial_y\varphi=0$ около
   неё аналитично (и по непрерывности остаётся в шаре $\lvert y\rvert<y_1$); по единственности (п. 2) оно совпадает с $y^*$. При $s=0$:
   $\partial_y\varphi(0,\theta,0)=0$, поэтому $y^*(0,\theta)=0$. $\square$

### 3.3. Определение: редуцированная функция, $g_k$, $j$, $G$

Положим

$$
R(s,\theta):=\varphi\big(s,\theta,y^*(s,\theta)\big),\qquad \eta^*(s,\theta):=s\sum_ay^*_a(s,\theta)e_a(\theta)\in N_\theta,
$$

$$
U_{\rm red}(s,\theta):=s^mR(s,\theta)=U\big(s\omega(\theta)+\eta^*(s,\theta)\big)\quad(0<s<s_1).
$$

$R$ аналитична, $R(0,\theta)=u_m(\omega(\theta))=0$. Положим $g_{m+i}(\theta):=\partial_s^iR(0,\theta)/i!$,
так что $R=\sum_{i\ge1}s^ig_{m+i}$ в круге сходимости этого ряда (не обязательно при всех
$\lvert s\rvert<s_1$; дальше используется только $\hat G$).

**Определение.** $j:=\min\{k>m:\ g_k\not\equiv0\text{ на }\Lambda''\}$ (при $d=0$: $g_k(\omega^*)\ne0$).
Если $j<\infty$, то **эффективный потенциал** $G:=g_j$, и
$R(s,\theta)=s^{j-m}\hat G(s,\theta)$, где
$\hat G(s,\theta)=\int_0^1\frac{(1-\tau)^{j-m-1}}{(j-m-1)!}\partial_s^{j-m}R(\tau s,\theta)\,d\tau$
аналитична и $\hat G(0,\theta)=G(\theta)$. **Нормальный вес** $c:=\frac{j-m+2}2\ge\frac32$.

**Замечания.**

1. *Каноничность.* Точка $s\omega+\eta^*(s,\omega)$ — единственная критическая точка $U$ на
   множестве $\{s\omega+\nu:\ \nu\in N_\omega,\ \lvert\nu\rvert<y_1\lvert s\rvert\}$. Значит, $R$ и все
   $g_k$ не зависят от выбора рамки $e_a$ и параметризации, это функции на $\Sigma$. Номер $j$ не
   зависит от выбора дуги на связной компоненте $\Sigma_0$ по теореме единственности для
   аналитических функций на связной аналитической кривой.
2. *Первые члены* (из разложения $\varphi=\frac12y^{\mathsf T}Hy+s\,u_{m+1}(\omega+y)+s^2u_{m+2}(\omega+y)+\dots$
   и $y^*=-sH^{-1}b_1+O(s^2)$, $b_1=(\langle\nabla u_{m+1}(\omega),e_a\rangle)_a$):
   $$g_{m+1}=u_{m+1}|_\Sigma,\qquad g_{m+2}=u_{m+2}|_\Sigma-\tfrac12\,b_1^{\mathsf T}H^{-1}b_1 .$$
   В общем случае $g_k$ — многочлен от производных $u_m,\dots,u_k$ в точках $\Sigma$ и
   элементов $H^{-1}$; поэтому $G$ определяется струёй $j^jU$. [Эксперимент: формулы для $g_5,g_6$
   совпадают с рядом из `reduced.py` на примере теоремы B: $g_5=\sqrt2\cos\varphi/8$,
   $g_6=-9\cos^2\varphi/512$, и вручную $\frac12(\partial_nu_5)^2/h_n=\frac12(3\cos\varphi/(4\sqrt2))^2/8$.]
3. *Чётность.* Для $\omega\in\Sigma$ и $s<0$ точка $s(\omega+y^*(s,\omega))$ — критическая точка в
   слое через $\lvert s\rvert(-\omega)$ (так как $N_{-\omega}=N_\omega$), поэтому
   $R(\lvert s\rvert,-\omega)=R(-\lvert s\rvert,\omega)$ ($m$ чётно), то есть
   $g_k(-\omega)=(-1)^kg_k(\omega)$. При нечётном $j$ функция $G$ нечётна как функция на
   $\Sigma_0\cup(-\Sigma_0)$ и принимает там отрицательные значения (если $-\Sigma_0\ne\Sigma_0$,
   отрицательное значение может оказаться на $-\Sigma_0$).
4. *$j=\infty$.* Если $R\equiv0$, то $U_{\rm red}\equiv0$, и кривая или поверхность дна
   $\{s\omega+\eta^*\}$ состоит из критических точек $U$ (при $d=0$ — следствие K0′(b); при $d=1$ и
   любом $n$ рассуждение K0′(b) переносится дословно: на дне $\nabla U\perp N_\theta$, а производные
   $U$ вдоль дна по $s$ и $\theta$ — это производные $U_{\rm red}\equiv0$; при $n=3$ это и предложение K4(b)). Для изолированной критической точки поэтому $j<\infty$ — здесь работают
   аналитичность и изолированность (§11).

### 3.4. Лемма K2 (нормальная форма) [Доказано]

**Лемма K2.** Пусть $j<\infty$. Положим

$$
M(s,\theta,\tau):=\int_0^1(1-\lambda)\,\partial_y^2\varphi\big(s,\theta,y^*(s,\theta)+\lambda\tau\big)\,d\lambda,\qquad
\tilde F(\sigma,\theta,e):=\hat G(\sigma^2,\theta)+e^{\mathsf T}M\big(\sigma^2,\theta,\sigma^{j-m}e\big)\,e .
$$

Тогда $\tilde F$ аналитична на $\{\lvert\sigma\rvert<s_1^{1/2},\ \theta\in\Lambda'',\ \lvert\sigma^{j-m}e\rvert<y_1/2\}$,
$M\succeq\frac{\lambda_H}4I$ там, $M(0,\theta,0)=\frac12H(\theta)$,

$$
\tilde F(0,\theta,e)=G(\theta)+\tfrac12e^{\mathsf T}H(\theta)e,\tag{3.3}
$$

и при $0<s<s_1$, $\theta\in\Lambda''$, $\lvert s^{c-1}e\rvert<y_1/2$:

$$
U\Big(s\omega(\theta)+\eta^*(s,\theta)+s^c\sum_ae_ae_a(\theta)\Big)=s^j\,\tilde F\big(s^{1/2},\theta,e\big).\tag{3.4}
$$

*Доказательство.* Точка в (3.4) равна $s(\omega+\sum_a(y^*_a+\tau_a)e_a)$ с $\tau=s^{c-1}e$. По (3.2)
значение $U$ в ней равно $s^m\varphi(s,\theta,y^*+\tau)$. Формула Тейлора по $y$ с интегральным
остатком в точке $y^*$, где $\partial_y\varphi=0$ (отрезок $[y^*,y^*+\tau]$ лежит в шаре
$\lvert y\rvert<y_1$, так как $\lvert y^*\rvert<y_1/2$), даёт
$\varphi(s,\theta,y^*+\tau)=R(s,\theta)+\tau^{\mathsf T}M(s,\theta,\tau)\tau$. Отсюда
$U=s^m\big(s^{j-m}\hat G+s^{2c-2}e^{\mathsf T}Me\big)=s^j\big(\hat G+e^{\mathsf T}Me\big)$, так как
$m+2c-2=j$, и $s^{c-1}=(s^{1/2})^{j-m}$. Аналитичность — композиция аналитических функций;
$M\succeq\frac{\lambda_H}4I$ по лемме K1, п. 1; $M(0,\theta,0)=\frac12\partial_y^2\varphi(0,\theta,0)=\frac12H$. $\square$

## 4. Класс $\mathcal K$

**Определение.** $n=3$, $U$ вещественно-аналитична около $0$, $U(0)=0$, $U=\sum_{k\ge m}u_k$,
$m\ge2$ чётно (жёсткое ядро: $m\ge4$), и

- **(K1)** $u_m\ge0$; $\Sigma=\{u_m=0\}\cap S^2\ne\varnothing$ — гладкое компактное подмногообразие
  $S^2$ (его компоненты — точки и замкнутые кривые);
- **(K2)** (Морс–Ботт) $D^2u_m(\omega)$ положительно определена на $N_\omega$ при всех
  $\omega\in\Sigma$;
- **(K3)** существуют компонента $\Sigma_0$ и точка $\omega^*\in\Sigma_0$ такие, что для
  $j=j(\Sigma_0)<\infty$ и $G=g_j|_{\Sigma_0}$ (§3.3 с дугой $\Sigma_0$ около $\omega^*$):
  $G(\omega^*)<0$, а при $\dim\Sigma_0=1$ ещё $G'(\omega^*)=0<G''(\omega^*)$ (производные по
  натуральному параметру $\Sigma_0$).

$\mathcal K^0$ — случай $\dim\Sigma_0=0$, $\mathcal K^1$ — случай $\dim\Sigma_0=1$;
$\mathcal K^1_{\rm C}\subset\mathcal K^1$ — подкласс с $G''(\omega^*)+jG(\omega^*)>0$.

**Теорема K (сводка).** Если $U\in\mathcal K$, то у $\ddot q=-\nabla U(q)$ есть асимптотическая
траектория, и равновесие неустойчиво по Ляпунову. [Доказано: $\mathcal K^0$ — теорема K0,
$\mathcal K^1_{\rm C}$ — теорема K1 (обе через проверенную теорему 2 [GT3]), $\mathcal K^1$ —
теорема K2 (через новую теорему 2′).]

Изолированность в теореме K не предполагается. Если $\Sigma$ конечно (все компоненты — точки),
(A) решается полностью (следствие K0′).

## 5. Случай $s=0$ (любое $n\ge2$)

### 5.1. Теорема K0 [Доказано]

**Теорема K0.** Пусть $n\ge2$, $\omega^*\in S^{n-1}$, $u_m(\omega^*)=0$, $\nabla u_m(\omega^*)=0$,
$H:=D^2u_m(\omega^*)|_{\omega^{*\perp}}\succ0$, и в обозначениях §3.3 (с $d=0$, $N=\omega^{*\perp}$,
$p=n-1$) $j<\infty$ и $g_j(\omega^*)<0$. Тогда есть асимптотическая траектория вида
$q(t)=x(t)\omega^*+\eta^*(x(t))+x(t)^c\sum_ab_a(t)e_a$, где $x(t)\downarrow0$,
$\dot x\asymp-x^{j/2}$ (так что $x(t)\asymp t^{-2/(j-2)}$), $\lvert b(t)\rvert\le2\sqrt{\delta/\lambda_0}$
при сколь угодно малом (выбираемом) $\delta>0$; здесь $\lambda_0=\lambda_{\min}(H)/4$ (следствие 1 [GT3]).

*Доказательство.* Применим следствие 2 [GT3] в ортонормированных координатах
$q=x\omega^*+\sum_ay_ae_a$ с $\gamma(x):=\eta^*(x)=x\,y^*(x)$ (в координатах $y$), весами
$c_a=c$, $\beta=j$, $N=2$.

1. *Кривая.* $\gamma$ аналитична на $(-s_1,s_1)$, $\gamma(x)=O(x^2)$ (так как $y^*(0)=0$),
   $\gamma'=y^*+xy^{*\prime}\to0$, $x\lvert\gamma''\rvert=x\lvert2y^{*\prime}+xy^{*\prime\prime}\rvert\to0$.
2. *(F).* По лемме K2 $U(x,\gamma(x)+x^cb)=x^jF(x^{1/2},b)$ с $F:=\tilde F$. Возьмём $r_0=1$,
   $\sigma_0\in(0,s_1^{1/2})$ с $\sigma_0^{j-m}<y_1/2$ и $s_0:=\sigma_0^2$: $F$ аналитична в окрестности $[0,\sigma_0]\times\overline{B_1}$,
   поэтому $F$, $\nabla_bF$ непрерывны, а $\sup_{b\in K}\lvert\sigma\partial_\sigma F\rvert\to0$.
3. *(V).* $F_0(b)=g_j(\omega^*)+\frac12b^{\mathsf T}Hb$ по (3.3): $F_0(0)<0$, $\nabla F_0(0)=0$,
   $\nabla^2F_0(0)=H\succ0$, $C=cI$, $CH+HC=2cH\succ0$. По следствию 1 [GT3] выполнено $(V_1)$.

Следствие 2 [GT3] (то есть теорема 2 [GT3] для прямой карты $\Phi(x,u)=(x,\gamma(x)+u)$) даёт
утверждение; оценки $\dot x$ и $b$ — из формулировки теоремы 2 [GT3]. $\square$

### 5.2. Следствие K0′ (трихотомия при конечном $\Sigma$) [Доказано]

**Следствие K0′.** Пусть $n\ge2$, $u_m\ge0$, $\Sigma=\{u_m=0\}\cap S^{n-1}$ конечно, и
$D^2u_m(\omega)|_{\omega^\perp}\succ0$ при всех $\omega\in\Sigma$ (то есть $u_m|_{S^{n-1}}$ имеет
в своих нулях невырожденные критические точки: там $\operatorname{Hess}_S(u_m|_S)=D^2u_m|_{\omega^\perp}$).
Для $\omega\in\Sigma$ пусть $R_\omega(s)$ — функция леммы K1. Тогда:

- **(a)** если для каждого $\omega\in\Sigma$ ряд $R_\omega\not\equiv0$ и его старший коэффициент
  $g_{j(\omega)}(\omega)>0$, то $0$ — строгий локальный минимум $U$;
- **(b)** если $R_\omega\equiv0$ для некоторого $\omega$, то $x\mapsto x\omega+\eta^*_\omega(x)$,
  $0<x<s_1$, — кривая критических точек $U$, и $0$ не изолирована;
- **(c)** если $g_{j(\omega)}(\omega)<0$ для некоторого $\omega$, то есть асимптотическая траектория
  (теорема K0).

В частности, **если $0$ — изолированная критическая точка и не локальный минимум, то есть
асимптотическая траектория, и равновесие неустойчиво по Ляпунову.** (Если $\Sigma=\varnothing$,
то $0$ — строгий минимум.)

*Доказательство.* Константы $s_1,y_1$ леммы K1 выберем общими для конечного $\Sigma$.

(a) Пусть $\varepsilon:=y_1/2$ и $C_\omega=\{q:\ \langle q,\omega\rangle>0,\ \lvert q-\langle q,\omega\rangle\omega\rvert<\varepsilon\langle q,\omega\rangle\}$.
Множество $K=S^{n-1}\setminus\bigcup_{\omega\in\Sigma}C_\omega$ компактно и не пересекает $\Sigma$,
поэтому $u_m\ge c_K>0$ на $K$ и $u_m(q)\ge c_K\lvert q\rvert^m$ вне $\bigcup C_\omega$. Так как
$\lvert U-u_m\rvert\le C'\lvert q\rvert^{m+1}$, вне $\bigcup C_\omega$ при $0<\lvert q\rvert<c_K/C'$
имеем $U>0$. Точка $q\in C_\omega$ записывается как $q=s(\omega+y)$, $s=\langle q,\omega\rangle\in(0,\lvert q\rvert]$,
$y\in\omega^\perp$, $\lvert y\rvert<\varepsilon<y_1$. По (3.2) и лемме K1, п. 2,
$U(q)=s^m\varphi(s,y)\ge s^mR_\omega(s)=s^{j(\omega)}\big(g_{j(\omega)}(\omega)+O(s)\big)>0$ при малом $s$.
Итак, $U>0$ в проколотой окрестности нуля.

(b) Пусть $\gamma(s)=s\omega+\eta^*(s)=s(\omega+y^*(s))$. Так как $y^*$ — критическая точка
$\varphi(s,\cdot)$, по (3.2) $s\langle\nabla U(\gamma(s)),e_a\rangle=\partial_{y_a}[s^m\varphi]=0$ для всех
$a$, то есть $\nabla U(\gamma(s))=\alpha(s)\omega$. Далее
$\frac d{ds}U(\gamma(s))=\langle\nabla U(\gamma),\gamma'\rangle=\alpha(s)\langle\omega,\omega+y^{*\prime}s+y^*\rangle=\alpha(s)$
($y^*,y^{*\prime}\perp\omega$). Так как $U(\gamma(s))=s^mR_\omega(s)\equiv0$, то $\alpha\equiv0$. Точки
$\gamma(s)\ne0$ стремятся к нулю.

(c) Теорема K0.

«В частности». Каждая $\omega\in\Sigma$ — ровно одного из типов: $R_\omega\equiv0$; старший
коэффициент $>0$; старший коэффициент $<0$ (аналитическая $R_\omega$ либо $\equiv0$, либо имеет
конечный порядок). Изолированность исключает первый тип у всех $\omega$. Если бы у всех был второй
тип, по (a) был бы минимум. Значит, у некоторой $\omega$ третий тип, и работает (c). $\square$

**Замечание 5.1** (связь с литературой). При $m=2$ условие означает: гессиан $\succeq0$ ранга
$n-1$; это покрыто FGT08, Thm A (ранг $\ge n-2$; нужна ещё струя, показывающая отсутствие
минимума, — она есть по BGZ96, первоисточник не сверялся) и **частично** Козловым 1986. Условие
Козлова (по рецензии Zbl 0631.70018) — «$V_2+V_{m'}$ не имеет локального минимума» для следующей
ненулевой формы $V_{m'}$; оно не выполнено, например, для $U=y^2(1+x)-x^4$ ($n=2$): $0$
изолирована и не минимум, условия K0′ выполнены ($R_{(\pm1,0)}=-s^2$, $g_4=-1$), но
$V_2+V_3=y^2(1+x)\ge0$ (отзыв R20, замечание 8). При $m\ge4$ (гессиан нулевой) известные
мне по конспектам репозитория критерии (первая ненулевая струя: Ляпунов, MN89, MMN91, Taliaferro
1990, Паламодов 2020 Thm 3; FGT08; класс $\mathcal H$ AG17) это не покрывают: $u_m\ge0$, а
радиальное условие типа (H3) нарушается на «искривлённом дне» (пример $U_{(7)}$, §9.7). Новизну по
первоисточникам я не проверял.

## 6. Случай $s=1$, $n=3$: геометрия конуса и декартова карта

### 6.1. Данные и лемма K3

Пусть $\Sigma_0\subset S^2$ — гладкая (аналитическая) кривая, $\omega:(-\theta_0,\theta_0)\to\Sigma_0$
— натуральная параметризация, $\omega(0)=\omega^*$, $T=\omega'$, $n=\omega\times T$. Тогда
(репер Дарбу кривой на единичной сфере)

$$
\omega'=T,\qquad T'=-\omega+k\,n,\qquad n'=-k\,T,\tag{6.1}
$$

$k(\theta)$ — геодезическая кривизна, аналитична. ($T'\perp T$, $\langle T',\omega\rangle=-1$; $n'$:
$n'=\omega'\times T+\omega\times T'=k\,\omega\times n=-kT$.) Нормаль $N_{\omega(\theta)}=\mathbb Rn(\theta)$,
$p=1$, $e_1=n$, $h_n(\theta):=D^2u_m(\omega(\theta))(n,n)>0$. Применяем §3 с $d=1$; $\Lambda$ —
отрезок около $0$.

**Лемма K3 (трубка конуса).** Пусть $P(s,\theta,\eta)=s\,\omega(\theta)+\eta\,n(\theta)$. Найдутся
$\theta_1\in(0,\theta_0)$, $t_1\in(0,1/(2\bar k+1))$ ($\bar k=\max_{\lvert\theta\rvert\le\theta_1}\lvert k\rvert$)
такие, что $P$ — аналитический диффеоморфизм
$\mathcal P=\{s>0,\ \lvert\theta\rvert<\theta_1,\ \lvert\eta\rvert<t_1s\}$ на открытое множество в
$\mathbb R^3\setminus0$, и

$$
\lvert P\rvert^2=s^2+\eta^2,\qquad P_s=\omega,\quad P_\theta=(s-k\eta)T,\quad P_\eta=n,\qquad \nabla s=\omega(\theta).\tag{6.2}
$$

*Доказательство.* (6.2) для производных — из (6.1); они попарно ортогональны и ненулевые
($s-k\eta\ge s(1-\bar kt_1)>0$), так что $P$ — локальный диффеоморфизм. Для ортогональной системы
координат градиент координатной функции равен $P_s/\lvert P_s\rvert^2=\omega$; $\lvert P\rvert^2=s^2+\eta^2$,
так как $\omega\perp n$. Инъективность: $P=s\sqrt{1+t^2}\,E(\theta,t)$, $t=\eta/s$,
$E(\theta,t)=(\omega(\theta)+tn(\theta))/\sqrt{1+t^2}\in S^2$. Отображение $E$ аналитично, в точках
$(\theta,0)$ его дифференциал имеет столбцы $T,n$ (ранг 2), а на компакте
$[-\theta_1',\theta_1']\times\{0\}$ оно инъективно (вложенная дуга). Локальный гомеоморфизм,
инъективный на компакте, инъективен в его окрестности; значит, при малых $\theta_1,t_1$ $E$
инъективно. Из $P(s,\theta,\eta)=P(s',\theta',\eta')$ следуют равенство направлений, то есть
$(\theta,\eta/s)=(\theta',\eta'/s')$, и равенство норм $s\sqrt{1+t^2}=s'\sqrt{1+t^2}$. Образ открыт
(локальный диффеоморфизм). $\square$

**Карта с дном.** $\Psi(s,\theta,\zeta):=P\big(s,\theta,\eta^*(s,\theta)+\zeta\big)=s\omega(\theta)+\eta\,n(\theta)$,
$\eta:=\eta^*(s,\theta)+\zeta$. Так как $\eta^*=s\,y^*=O(s^2)$, при малом $s$ и
$\lvert\zeta\rvert<r_0s^c$ точка лежит в $\mathcal P$. Функция $s$ на $\mathbb R^3$ одна и та же для
$P$ и $\Psi$, поэтому $\nabla s=\omega(\theta)$ и в карте $\Psi$. По лемме K2

$$
U\big(\Psi(s,\theta,s^ce)\big)=s^j\tilde F(s^{1/2},\theta,e),\qquad \tilde F(0,\theta,e)=G(\theta)+\tfrac12h_n(\theta)e^2.\tag{6.3}
$$

Координатные поля $\Psi$ (проверено символьно, `frame_check.py`):

$$
\Psi_s=\omega+\eta^*_s\,n,\qquad \Psi_\theta=s(1-\varepsilon)T+\eta^*_\theta\,n,\qquad\Psi_\zeta=n,\qquad \varepsilon:=\frac{k(\theta)\eta}{s}.\tag{6.4}
$$

**Малые величины.** На множестве $\{0<s<s_0,\ \lvert\theta\rvert\le r_0,\ \lvert\zeta\rvert\le r_0s^c\}$
(при $r_0\le\theta_1/2$) равномерно при $s\to0$:

$$
\varepsilon,\ \ s\partial_s\varepsilon=k\eta^*_s-\varepsilon,\ \ \partial_\theta\varepsilon=\frac{k'\eta+k\eta^*_\theta}s,\ \
\eta^*_s,\ \ \frac{\eta^*_\theta}s,\ \ s\,\eta^*_{ss},\ \ \eta^*_{s\theta},\ \ \frac{\eta^*_{\theta\theta}}s\ \longrightarrow\ 0,\tag{6.5}
$$

так как $\eta^*=s\,y^*(s,\theta)$ с аналитической $y^*$, $y^*(0,\cdot)=0$ (то есть $\eta^*=O(s^2)$,
$\eta^*_s=O(s)$, $\eta^*_\theta=O(s^2)$, вторые производные $\eta^*_{ss}=O(1)$, $\eta^*_{s\theta}=O(s)$,
$\eta^*_{\theta\theta}=O(s^2)$), а $\lvert\eta\rvert\le C s^2+r_0s^c$ и $c>1$.

### 6.2. Теорема K1 (декартова карта развёртки) [Доказано]

**Теорема K1.** Пусть $n=3$, выполнены (S) для дуги $\Sigma_0$ около $\omega^*$ ($d=1$),
$j<\infty$, $G(0)<0$, $G'(0)=0$ и $G''(0)+jG(0)>0$. Тогда $U$ принадлежит классу (GT3) [GT3, §5.1]
с $\beta=j$, весами $(1,c)$, $N=2$, картой (6.6) и условием $(V_1)$; по теореме 2 [GT3] есть
асимптотическая траектория.

*Карта.* В полярных координатах развёртки $X=s\cos\theta$, $Y=s\sin\theta$ ($X>0$, $\lvert Y/X\rvert<r_0$):

$$
\Phi(X,Y,\zeta)=\Psi\Big(\sqrt{X^2+Y^2},\ \arctan\frac YX,\ \zeta\Big),\qquad x=X,\ u=(Y,\zeta),\ b=(t,e)=\Big(\frac YX,\frac\zeta{X^c}\Big).\tag{6.6}
$$

Обозначим $r=\sqrt{X^2+Y^2}$, $\mathrm c=\cos\theta$, $\mathrm s=\sin\theta$,
$p_X=\mathrm c\,\eta^*_s-\mathrm s\,\eta^*_\theta/r$, $p_Y=\mathrm s\,\eta^*_s+\mathrm c\,\eta^*_\theta/r$.
Формулы (все проверены символьно с произвольными $k(\theta)$, $\eta^*(s,\theta)$, `frame_check.py`):

$$
\Phi_X=\mathrm c\,\omega-\mathrm s(1-\varepsilon)T+p_Xn,\quad \Phi_Y=\mathrm s\,\omega+\mathrm c(1-\varepsilon)T+p_Yn,\quad\Phi_\zeta=n,
$$

$$
B_{XY}=\mathrm s\mathrm c\big(1-(1-\varepsilon)^2\big)+p_Xp_Y,\qquad B_{X\zeta}=p_X,
$$

$$
\Phi_{XX}=\frac{\mathrm s^2\varepsilon}r\,\omega+\Big(-\frac{\mathrm s\mathrm c\,\varepsilon}r+\mathrm s\,\partial_X\varepsilon+\frac{p_Xk\mathrm s}r\Big)T+\Big(\frac{\mathrm s^2(1-\varepsilon)k}r+\partial_Xp_X\Big)n,
$$

$$
\Phi_{XY}=-\frac{\mathrm s\mathrm c\,\varepsilon}r\,\omega+\Big(\frac{\mathrm c^2\varepsilon}r+\mathrm s\,\partial_Y\varepsilon-\frac{p_Xk\mathrm c}r\Big)T+\Big(-\frac{\mathrm s\mathrm c(1-\varepsilon)k}r+\partial_Yp_X\Big)n,\qquad
\Phi_{X\zeta}=\frac{\mathrm s\,k}r\,T .
$$

*Доказательство.* Пусть $r_0\le\min(\frac14,\theta_1/2)$, $[-r_0,r_0]\subset\Lambda''$ (область, где
определена $\tilde F$), $\sigma_0$ мало (так, что $\sigma_0^{j-m}r_0<y_1/2$, $\sigma_0<s_1^{1/2}$) и
$s_0\le\sigma_0^2/2$ (тогда $r<\sigma_0^2$; поправка по отзыву R22, замечание 3). В $\mathcal N=\{0<X<s_0,\ \lvert b\rvert<r_0\}$:
$\lvert\mathrm s\rvert\le\lvert t\rvert\le\lvert b\rvert$, $X\le r\le\frac{\sqrt{17}}4X$, и по (6.5) величины
$\varepsilon$, $p_X$, $p_Y$, $r\partial_X\varepsilon$, $r\partial_Y\varepsilon$, $r\partial_Xp_X$, $r\partial_Yp_X$
стремятся к нулю равномерно при $X\to0$ (они выражаются через (6.5) и
$\partial_Xr=\mathrm c$, $\partial_X\theta=-\mathrm s/r$, $\partial_Yr=\mathrm s$, $\partial_Y\theta=\mathrm c/r$).
Обозначим через $\varpi_1(X)\to0$ сумму их супремумов по $\{X'\le X\}$.

- $(\Phi0)$: $\Phi$ — композиция диффеоморфизма $(X,Y)\mapsto(r,\theta)$ сектора и карты $\Psi$
  (лемма K3); $\lvert\Phi\rvert^2=r^2+\eta^2$, поэтому $X\le\lvert\Phi\rvert\le2r\le3X$.
- $(\Phi1)$: в ортонормированном репере $(\omega,T,n)$ все элементы $B-I$ ограничены
  $3\lvert\varepsilon\rvert+2(\lvert p_X\rvert+\lvert p_Y\rvert)+(\lvert p_X\rvert+\lvert p_Y\rvert)^2$,
  так что $\lVert B-I\rVert\le\frac12$ при малом $s_0$; $\lvert B_{xu}\rvert\le3\lvert\varepsilon\rvert+\lvert p_X\rvert(1+\lvert p_Y\rvert)\to0$.
- $(\Phi2)$: $X\lvert\Phi_{XX}\rvert\le\mathrm s^2(1+\lvert\varepsilon\rvert)\bar k+\lvert\varepsilon\rvert(\mathrm s^2+\lvert\mathrm s\rvert)+r\lvert\partial_X\varepsilon\rvert+\lvert p_X\rvert\bar k+r\lvert\partial_Xp_X\rvert\le\frac54\bar k\lvert b\rvert^2+4\varpi_1(X)(1+\bar k)$.
- $(\Phi3)$: для $w\perp\Phi_X$, $w=\zeta_X\Phi_X+\zeta_Y\Phi_Y+\zeta_\zeta\Phi_\zeta$, имеем
  $\lvert\zeta\rvert\le\sqrt2\lvert w\rvert$ ($B\succeq\frac12I$) и
  $D_wY=\zeta_X\Phi_{XX}+\zeta_Y\Phi_{XY}+\zeta_\zeta\Phi_{X\zeta}$. Из формул:
  $X\lvert\Phi_{XY}\rvert\le\lvert\mathrm s\rvert\bar k(1+\lvert\varepsilon\rvert)+4\varpi_1(1+\bar k)$,
  $X\lvert\Phi_{X\zeta}\rvert\le\bar k\lvert\mathrm s\rvert$. Значит
  $X\lvert\langle w,D_wY\rangle\rvert\le\sqrt6\,\lvert w\rvert^2\big(\tfrac54\bar k\lvert b\rvert^2+\tfrac54\bar k\lvert b\rvert+\bar k\lvert b\rvert+8\varpi_1(1+\bar k)\big)\le(C_1\lvert b\rvert+\varpi(X))\lvert w\rvert^2$
  с $C_1=7\bar k$ ($\lvert b\rvert^2\le\frac14\lvert b\rvert$, $\sqrt6\cdot\frac{41}{16}<7$) и $\varpi=20(1+\bar k)\varpi_1$ (тот же $C_1$ и $\varpi$ годятся в $(\Phi2)$).
- (F): по (6.3) с $s=r=X\sqrt{1+t^2}$, $\theta=\arctan t$, $\zeta/r^c=e(1+t^2)^{-c/2}$:
  $U\circ\Phi=X^jF(X^{1/2},t,e)$,
  $$F(\sigma,t,e)=(1+t^2)^{j/2}\,\tilde F\big(\sigma(1+t^2)^{1/4},\arctan t,\ e(1+t^2)^{-c/2}\big),$$
  аналитична в окрестности $[0,\sigma_0]\times\overline{B_{r_0}}$ при малом $\sigma_0$.
- $(V_1)$: $F_0(t,e)=(1+t^2)^{j/2}\big[G(\arctan t)+\frac12h_n(\arctan t)(1+t^2)^{-c}e^2\big]$. Так как
  $(1+t^2)^{j/2}=1+\frac j2t^2+O(t^4)$ и $G(\arctan t)=G(0)+\frac12G''(0)t^2+O(t^3)$ ($G'(0)=0$):
  $F_0(0)=G(0)<0$, $\nabla F_0(0)=0$, $\nabla^2F_0(0)=\operatorname{diag}\big(G''(0)+jG(0),\ h_n(0)\big)\succ0$
  (смешанная производная равна нулю: $F_0$ зависит от $e$ только через $e^2$). Матрица диагональна,
  $C=\operatorname{diag}(1,c)$; по следствию 1 [GT3] выполнено $(V_1)$.

Карта кривая ($C_1>0$ при $\bar k>0$), поэтому нужен именно случай $(V_1)$ теоремы 2 [GT3]; он есть. $\square$

**Замечание 6.1** (почему $G''+jG$). Декартов срез $\{X=x\}$ пересекает лучи под углом $\theta$, и
на срезе $s=x/\cos\theta$, так что $s^jG(\theta)=x^j(1+\frac j2\theta^2+\dots)(G(0)+\frac12G''\theta^2+\dots)$:
поперечный гессиан равен $G''+jG$, а $G<0$. У примера 13 запас мал
($G''+6G\approx0.050$, совпадает с $H_{11}$ [GT3, §6.3]), у примера теоремы B он отрицателен (§9.2).
Полярный срез $\{s=x\}$ даёт гессиан $G''$, но при радиальном $Y$ нет запаса в неравенстве Эйлера
по углу (вес $0$). Теорема K2 берёт полярный срез и поле $Y$ с малым угловым весом $\kappa$.

## 7. Теорема 2′: вариант теоремы 2 [GT3] с перекрёстными членами

### 7.1. Лемма 2′ [Доказано]

Обозначения §2–§4 [GT3]: $V=K_\perp+W$, $K_\perp=\frac12\lvert v_\perp\rvert^2$, $W=U+A(\rho)$,
$\Omega$, $\Xi$, условия (D1)–(D4), (A4), (A5), (L0), (L1), константы
$L_1=2(a_2+\frac{\beta a_1}2)\sqrt{h_1/a_1}$, $L_2=2\sqrt{2a_3/h_0}$ из (4.1) [GT3] (в записке [GT3] они
назывались $c_1,c_2$; переименованы, чтобы не путать с весами $c_i$, как в `results/007-gt3.md`).

*Нумерация формул.* В этом разделе ссылки (2.1), (3.1), (3.3), (4.1), (5.1), (5.2) [GT3] даны по записке
[GT3]; в `results/007-gt3.md` им соответствуют (0.1), (1.1), (1.3), (3.1), (4.1), (4.2), а
погрешность $\eta$ там обозначена $\chi$ (отзыв R21, З3). *Буква $\sigma$* в лемме 2′ — порог
$\rho<\sigma$, как в теореме A; в теореме 2′ $\sigma=x^{1/N}$ — переменная из (F), а порог по $x$
обозначен $\sigma_*$ (так что $\sigma_*^{1/N}$ — значение переменной $\sigma$).

**Лемма 2′.** Пусть выполнены (D1), а на $D_\sigma=\{q\in\overline D:\ q\ne0,\ \rho(q)<\sigma\}$ —
(L0), (L1) и

- **(L2′)** есть функция $P:D_\sigma\to[0,\infty)$, числа $\varepsilon_0\in[0,\frac12]$, $\varepsilon_1\ge0$,
  $\mu\in(0,\beta]$ с $\lvert W-P\rvert\le\varepsilon_0\delta\rho^\beta$ и
  $\beta W-\rho\,YW\ge\mu P-\varepsilon_1\delta\rho^\beta$;
- **(L3′)** с числами $\theta_1,\theta_2,\theta_3\ge0$, $\gamma_1',\gamma_2'\ge0$ (отзыв R21, З4): для всех $q\in D_\sigma$ и $w\perp Y(q)$:
  $\lvert\langle\nabla\rho-Y/h,w\rangle\rvert\le\big(\theta_1+\gamma_1'\sqrt{P/\rho^\beta}\big)\lvert w\rvert$,
  $\rho\lvert\langle\nabla_YY,w\rangle\rvert\le\big(\theta_2+\gamma_2'\sqrt{P/\rho^\beta}\big)\lvert w\rvert$,
  $\rho\langle w,D_wY\rangle\ge-\theta_3\lvert w\rvert^2$.

Тогда (D4) выполнено и

1. если $4\sqrt\delta\,(\theta_1+2\gamma_1'\sqrt\delta)\le\sqrt{a_1/h_1}$, то на
   $\overline\Omega\cap\{0<\rho<\sigma\}$ выполнено $\dot\rho\le-\frac12\sqrt{a_1/h_1}\,\rho^{\beta/2}<0$, то есть (A4);
2. если $\Gamma'^2\le\beta\mu$, где $\Gamma':=\sqrt2\big[(a_2+\beta\delta)\sqrt{h_1/a_1}\,\gamma_1'+\sqrt{2a_3/h_0}\,\gamma_2'\big]$,
   то в каждой точке множества из (A5)
   $$\frac\rho\lambda\,\Xi\ \ge\ \delta\rho^\beta\Big[\frac\mu2(1-\varepsilon_0)-\varepsilon_1-\frac{L_1\theta_1+L_2\theta_2}{\sqrt\delta}-4\theta_3\Big].\tag{7.1}$$

*Доказательство.*

1. (D4) — как в лемме 2 [GT3], п. 1 (только (L0)).
2. *Оценки на $\overline\Omega\cap\{0<\rho<\sigma\}$.* $W\ge P-\varepsilon_0\delta\rho^\beta\ge-\frac12\delta\rho^\beta$,
   поэтому $K_\perp=V-W\le\frac32\delta\rho^\beta$ и $\lvert v_\perp\rvert\le2\sqrt\delta\rho^{\beta/2}$;
   $P\le W+\varepsilon_0\delta\rho^\beta\le V+\frac12\delta\rho^\beta\le\frac32\delta\rho^\beta$, так что
   $\sqrt{P/\rho^\beta}\le2\sqrt\delta$. По (2.1) [GT3] $\lambda^2h/2=A-V\ge(a_1-\delta)\rho^\beta\ge\frac{a_1}2\rho^\beta$,
   откуда $\lambda\ge\sqrt{a_1/h_1}\rho^{\beta/2}$. По (3.1) [GT3]
   $\dot\rho=-\lambda+\langle\nabla\rho-Y/h,v_\perp\rangle$, и
   $\lvert\langle\nabla\rho-Y/h,v_\perp\rangle\rvert\le(\theta_1+2\gamma_1'\sqrt\delta)\cdot2\sqrt\delta\rho^{\beta/2}\le\frac12\sqrt{a_1/h_1}\rho^{\beta/2}$.
   Это п. 1.
3. *Точка из (A5).* $V=\delta\rho^\beta$, $K:=K_\perp=\delta\rho^\beta-W\in[0,2\delta\rho^\beta]$,
   $\sqrt{a_1/h_1}\rho^{\beta/2}\le\lambda\le\sqrt{2a_3/h_0}\rho^{\beta/2}$ (как в лемме 2 [GT3], п. 3).
   В (3.3) [GT3] главный член $\beta\delta\rho^\beta-\rho YW=\beta K+(\beta W-\rho YW)\ge\beta K+\mu P-\varepsilon_1\delta\rho^\beta$.
4. $\lvert T_1\rvert\le\frac\rho\lambda(a_2+\beta\delta)\rho^{\beta-1}\big(\theta_1+\gamma_1'\sqrt{P/\rho^\beta}\big)\sqrt{2K}
   \le(a_2+\beta\delta)\sqrt{h_1/a_1}\big[\theta_1\rho^{\beta/2}\sqrt{2K}+\gamma_1'\sqrt{2KP}\big]
   \le L_1\theta_1\sqrt\delta\rho^\beta+\sqrt2(a_2+\beta\delta)\sqrt{h_1/a_1}\,\gamma_1'\sqrt{KP}$
   (использованы $\sqrt{2K}\le2\sqrt\delta\rho^{\beta/2}$ и $\delta\le a_1/2$).
5. $\lvert T_2\rvert=\lambda\rho\lvert\langle v_\perp,\nabla_YY\rangle\rvert\le\lambda\big(\theta_2+\gamma_2'\sqrt{P/\rho^\beta}\big)\sqrt{2K}
   \le L_2\theta_2\sqrt\delta\rho^\beta+\sqrt2\sqrt{2a_3/h_0}\,\gamma_2'\sqrt{KP}$.
6. $T_3\ge-\theta_3\lvert v_\perp\rvert^2=-2\theta_3K\ge-4\theta_3\delta\rho^\beta$.
7. Сумма: $\frac\rho\lambda\Xi\ge\beta K+\mu P-\Gamma'\sqrt{KP}-\big[\varepsilon_1+\frac{L_1\theta_1+L_2\theta_2}{\sqrt\delta}+4\theta_3\big]\delta\rho^\beta$.
   При $\mu\le\beta$ имеем $\Gamma'^2\le\beta\mu\le\mu(2\beta-\mu)=4(\beta-\frac\mu2)\frac\mu2$, поэтому
   $(\beta-\frac\mu2)K+\frac\mu2P\ge2\sqrt{(\beta-\frac\mu2)\frac\mu2KP}\ge\Gamma'\sqrt{KP}$, то есть
   $\beta K+\mu P-\Gamma'\sqrt{KP}\ge\frac\mu2(K+P)$. Наконец
   $K+P\ge K+W-\varepsilon_0\delta\rho^\beta=(1-\varepsilon_0)\delta\rho^\beta$. Это (7.1). $\square$

Лемма 2′ — аналог леммы 2 [GT3], а не её обобщение (отзыв R21, З1): лемма 2′ требует $P\ge0$,
а лемма 2 допускает $W\ge-\delta\rho^\beta$, так что подставить $P=W$ при $\gamma_i'=0$ нельзя
(а $P=\max(W,0)$ дало бы $\varepsilon_0=1>\frac12$). На теорему 2′ это не влияет: случай $(V_1)$
теоремы 2 [GT3] — её частный случай (с $P=x^\beta Q$). Новое — члены $\gamma_i'\sqrt{KP}$: перекрёстные члены, линейные по поперечному
смещению, гасятся неравенством о средних, если они малы по сравнению с $\sqrt{\beta\mu}$.

### 7.2. Теорема 2′ [Доказано]

**Данные** — как в [GT3, §5.1]: $n\ge2$, $m'=n-1$, $U\in C^2(B_r)$, $U(0)=0$, $\nabla U(0)=0$,
$\beta>0$, веса $c\in(0,\infty)^{m'}$, $N\in\mathbb N$, $s_0\in(0,1]$, $r_0>0$,
$b=(u_ix^{-c_i})_i$, $\sigma=x^{1/N}$, $\mathcal N=\{(x,u):\ 0<x<s_0,\ \lvert b\rvert<r_0\}$,
$\Phi\in C^2(\mathcal N;\mathbb R^n)$, $Y:=\partial_x\Phi$ (как поле на $\Phi(\mathcal N)$),
$\rho:=x\circ\Phi^{-1}$, $h=\lvert Y\rvert^2$. Условия:

- **$(\Phi0)$** как в [GT3].
- **$(\Phi1')$** $\frac12\le h\le\frac32$ на $\mathcal N$.
- **$(\Phi2')$** есть $\gamma_1,\gamma_2,C_1\ge0$ и $\varpi(x)\to0$ ($x\to0$) такие, что для
  $(x,u)\in\mathcal N$ и $w\perp\partial_x\Phi(x,u)$:
  $$\lvert\langle\nabla\rho-Y/h,w\rangle\rvert\le\big(\gamma_1\lvert b\rvert+\varpi(x)\big)\lvert w\rvert,\qquad
  x\,\lvert\langle\partial_x^2\Phi,w\rangle\rvert\le\big(\gamma_2\lvert b\rvert+C_1\lvert b\rvert^2+\varpi(x)\big)\lvert w\rvert .$$
- **$(\Phi3)$** $x\langle w,D_wY\rangle\ge-(C_1\lvert b\rvert+\varpi(x))\lvert w\rvert^2$ для $w\perp\partial_x\Phi$.
- **(F)** как в [GT3]; $F_0=F(0,\cdot)$, $Q=F_0-F_0(0)$, $a_0:=-F_0(0)$.
- **$(V_1')$** $F_0(0)<0$; есть $\lambda_0>0$, $\mu\in(0,\beta]$, $r_1\in(0,r_0)$ с
  $Q(b)\ge\lambda_0\lvert b\rvert^2$ и $\sum_ic_ib_i\partial_{b_i}Q(b)\ge\mu Q(b)$ при $\lvert b\rvert<r_1$, и
  $$\Gamma_*^2\le\beta\mu,\qquad \Gamma_*:=\sqrt{a_0/\lambda_0}\,\Big[\tfrac{3\sqrt3}2\,\beta\gamma_1+2\sqrt2\,\gamma_2\Big].\tag{7.2}$$

**Теорема 2′.** При этих условиях есть решение $q(t)$, $t\ge0$, $q(t)\ne0$, $q(t)\to0$,
$\dot q(t)\to0$ при $t\to+\infty$; равновесие неустойчиво по Ляпунову. При этом
$q(t)=\Phi(x(t),u(t))$, $x(t)\downarrow0$, $\dot x\asymp-x^{\beta/2}$, и $\lvert b(t)\rvert\le2\sqrt{\delta/\lambda_0}$
при всех $t$, где $\delta>0$ можно взять сколь угодно малым.

Карта теоремы 2 [GT3] с $(\Phi1)$–$(\Phi3)$ удовлетворяет $(\Phi1')$–$(\Phi2')$ с $\gamma_1=\gamma_2=0$ и
$\varpi=2\sqrt2\,\omega$ (шаг 4 теоремы 2 [GT3]: $\lvert\nabla\rho-Y/h\rvert\le2\sqrt2\lvert B_{xu}\rvert$; отзыв R21, З2), так что случай
$(V_1)$ теоремы 2 [GT3] — частный случай теоремы 2′. Требование $B\approx I$ в $(\Phi1)$ здесь
ослаблено до $(\Phi1')$: оно в доказательстве теоремы 2 [GT3] нужно только для $h$ и $\theta_1$.

*Доказательство.* Повторяем доказательство теоремы 2 [GT3] с заменой леммы 2 на лемму 2′.

1. *Шаг 1 [GT3] дословно:* $G=\Phi(\mathcal N)$, $\rho\in C^2(G)$, $Y\in C^1(G)$, $Y\rho=1$,
   $A(r)=a_0r^\beta$, $W\circ\Phi=x^\beta(F-F_0(0))$ (5.1), и (5.2):
   $\beta W-\rho YW=x^\beta\big[\sum_ic_ib_i\partial_{b_i}F-\frac\sigma N\partial_\sigma F\big]$. Там используются
   только $\rho=x\circ\Phi^{-1}$, $Y=\partial_x\Phi$, $b_i=u_ix^{-c_i}$ и (F).
2. *Шаг 2 (случай $(V_1)$ [GT3]):* $\delta\le\min(a_0/2,\lambda_0r_1^2/16)$ (окончательно — в п. 5),
   $\Omega_b'=B_{2\sqrt{\delta/\lambda_0}}$, $R_b=2\sqrt{\delta/\lambda_0}$; $Q\ge4\delta$ на $\partial\Omega_b'$,
   $\kappa'=3\delta$; $Q\ge\lambda_0\lvert b\rvert^2$ и неравенство Эйлера с $\mu$ на $\overline{\Omega_b'}$.
3. *Шаг 3 [GT3] дословно:* $\eta_F(\sigma)$, $\sigma_*$ с $\bar\eta_F(\sigma_*^{1/N})<\min(\delta,\kappa'/2)$,
   $\mathcal D=\{x<\sigma_*,\ b\in\Omega_b',\ F-F_0(0)<\delta\}$, $D=\Phi(\mathcal D)$; (D1)–(D3)
   проверяются там только через $(\Phi0)$, (F), $\overline{\Omega_b'}\subset B_{r_0}$ и свойство (ii) шага 2. Ниже
   $\eta_F:=\bar\eta_F(\sigma_*^{1/N})$, $\bar\varpi:=\sup_{x<\sigma_*}\varpi(x)$, и $\sigma_*$ ещё уменьшится.
4. *Константы леммы 2′ на $D_{\sigma_*}$* (там $b\in\overline{\Omega_b'}$, $F-F_0(0)\le\delta$):
   - (L0): $a_1=a_3=a_0$, $a_2=\beta a_0$; (L1): $h_0=\frac12$, $h_1=\frac32$ по $(\Phi1')$.
   - (L2′): $P:=x^\beta Q(b)\ge0$. $\lvert W-P\rvert=x^\beta\lvert F(\sigma,b)-F_0(b)\rvert\le\eta_Fx^\beta$, то есть
     $\varepsilon_0=\eta_F/\delta$. По (5.2) и неравенству Эйлера
     $\beta W-\rho YW\ge x^\beta\big[\mu Q-c_{\max}R_b\eta_F-\eta_F/N\big]$, то есть
     $\varepsilon_1=(c_{\max}R_b+1/N)\eta_F/\delta$.
   - (L3′): на $\overline{\Omega_b'}\subset B_{r_1}$ имеем $\lvert b\rvert\le\sqrt{Q/\lambda_0}=\sqrt{P/(\lambda_0\rho^\beta)}$. По
     $(\Phi2')$: $\theta_1=\bar\varpi$, $\gamma_1'=\gamma_1/\sqrt{\lambda_0}$. Так как $Y\circ\Phi=\partial_x\Phi$,
     $\nabla_YY=\partial_x^2\Phi$, и $\rho\lvert\langle\nabla_YY,w\rangle\rvert\le(\gamma_2\lvert b\rvert+C_1R_b^2+\bar\varpi)\lvert w\rvert$:
     $\theta_2=C_1R_b^2+\bar\varpi$, $\gamma_2'=\gamma_2/\sqrt{\lambda_0}$. По $(\Phi3)$: $\theta_3=C_1R_b+\bar\varpi$.
   - $\Gamma'\le\Gamma_*$: при $\delta\le a_0/2$ имеем $a_2+\beta\delta\le\frac32\beta a_0$,
     $\sqrt2\cdot\frac32\beta a_0\sqrt{3/(2a_0)}=\frac{3\sqrt3}2\beta\sqrt{a_0}$ и
     $\sqrt2\sqrt{2a_0/(1/2)}=2\sqrt2\sqrt{a_0}$. По (7.2) $\Gamma'^2\le\beta\mu$.
5. *Выбор $\delta$ и $\sigma_*$.* Здесь $L_1=3\beta\sqrt{3a_0/2}$, $L_2=4\sqrt{a_0}$. Члены, зависящие
   только от $\delta$: $\frac{L_2C_1R_b^2}{\sqrt\delta}+4C_1R_b=C_1\sqrt\delta\big(\frac{16\sqrt{a_0}}{\lambda_0}+\frac8{\sqrt{\lambda_0}}\big)$
   и (для п. 1 леммы 2′) $8\gamma_1'\delta$. Выберем $\delta$ так, чтобы первое было $\le\mu/8$, а
   $8\gamma_1'\delta\le\frac12\sqrt{a_0/h_1}$. Затем $\sigma_*$ так, чтобы $\varepsilon_0\le\frac14$,
   $\varepsilon_1\le\frac\mu{16}$, $\frac{(L_1+L_2)\bar\varpi}{\sqrt\delta}+4\bar\varpi\le\frac\mu{16}$ и
   $4\sqrt\delta\,\bar\varpi\le\frac12\sqrt{a_0/h_1}$. Тогда условие п. 1 леммы 2′ выполнено, а
   скобка в (7.1) не меньше $\frac\mu2\cdot\frac34-\frac\mu8-\frac\mu{16}-\frac\mu{16}=\frac\mu8>0$.

Лемма 2′ даёт (A4), (A5), (D4); теорема A [GT3] — искомое решение. Оценка
$\dot x\asymp-x^{\beta/2}$ — из п. 1 леммы 2′ и верхней оценки
$\lambda\le\sqrt{2(a_0+\delta/2)/h_0}\,\rho^{\beta/2}$ (из $V\ge W\ge-\frac12\delta\rho^\beta$), как в лемме 2 [GT3], п. 1. $\square$

**Замечание 7.1** (ослабление (7.2); по отзыву R21, З5) [Эскиз]. (i) В п. 7 леммы 2′ достаточно
$\Gamma'^2\le\mu(2\beta-\mu)$. (ii) Если $\Gamma'^2<4\beta\mu$, то при некотором $\varepsilon\in(0,\min(\beta,\mu))$
$\Gamma'^2\le4(\beta-\varepsilon)(\mu-\varepsilon)$ и $\beta K+\mu P-\Gamma'\sqrt{KP}\ge\varepsilon(K+P)$; в (7.1) $\frac\mu2$
заменяется на $\varepsilon$. (iii) На множестве (A5) точнее $\lambda\ge\sqrt{2(a_0-\delta)/h_1}\,\rho^{\beta/2}$, и
коэффициент при $\gamma_1$ в $\Gamma'$ при $\delta\to0$ стремится к $\sqrt{a_0/\lambda_0}\cdot\frac{\sqrt6}2\beta$.
Отсюда теорема 2′ должна оставаться верной при
$\big[\sqrt{a_0/\lambda_0}\,(\frac{\sqrt6}2\beta\gamma_1+2\sqrt2\gamma_2)\big]^2<4\beta\mu$, что расширяет допустимое $\kappa$
в теореме K2 примерно в 18 раз при больших $j$. Не выписано полностью; для теоремы 2′ в нынешней
формулировке не нужно. В модельном примере R21 порог строгого выхода численно в 10–100 раз выше
обеих оценок [Эксперимент, R21].

## 8. Случай $s=1$, $n=3$: поворачивающаяся полярная карта (теорема K2)

### 8.1. Карта

Данные §6.1. Для $\kappa\in(0,\frac12]$ положим

$$
\Phi(x,u,\zeta):=\Psi\big(x,\ \theta,\ \zeta\big),\quad \theta:=u\,x^{-\kappa};\qquad b=(\theta,e)=\big(u\,x^{-\kappa},\ \zeta\,x^{-c}\big),\quad\text{веса }(\kappa,c),\ N=2.\tag{8.1}
$$

Срезы $\{x=\mathrm{const}\}$ — «сферы» $\{s=\mathrm{const}\}$ развёртки (полярный срез), а
$Y=\partial_x\Phi$ при постоянном $u$ сдвигает угол: $\partial_x\theta=-\kappa\theta/x$. Обозначим
$p:=\eta^*_s-\kappa\theta\,\eta^*_\theta/x$, $\varepsilon=k\eta/x$ (как в (6.4), $s=x$). Формулы
(проверены символьно, `frame_check.py`):

$$
Y=\partial_x\Phi=\omega-\kappa\theta(1-\varepsilon)\,T+p\,n,\qquad h=1+\kappa^2\theta^2(1-\varepsilon)^2+p^2,\tag{8.2}
$$

$$
x\,\partial_x^2\Phi=-\kappa\theta\big[(1-\kappa)+\kappa\varepsilon-x\partial_x\varepsilon-pk\big]T+\kappa^2\theta^2(1-\varepsilon)(-\omega+kn)+x\,\partial_xp\;n,\tag{8.3}
$$

где $\partial_x$ — полная производная при постоянных $(u,\zeta)$, $x\partial_x\varepsilon=-\kappa\theta k'\eta/x+kp-\varepsilon$.
Как поле на $G=\Phi(\mathcal N)$ в координатах $(s,\theta,\zeta)$ карты $\Psi$:
$Y=\omega-\kappa\theta(1-\varepsilon)T+pn$ с $\varepsilon=k(\eta^*+\zeta)/s$, $p=\eta^*_s-\kappa\theta\eta^*_\theta/s$, и

$$
\partial_\theta Y=\kappa\theta(1-\varepsilon)\omega+\big[1-\kappa(1-\varepsilon)+\kappa\theta\partial_\theta\varepsilon-pk\big]T+\big[-\kappa\theta(1-\varepsilon)k+\partial_\theta p\big]n,
$$

$$
\partial_sY=\kappa\theta\,\partial_s\varepsilon\,T+\partial_sp\,n,\qquad \partial_\zeta Y=\frac{\kappa\theta k}s\,T.\tag{8.4}
$$

### 8.2. Теорема K2 [Доказано, в предположении теоремы 2′]

**Теорема K2.** Пусть $n=3$, выполнены (S) для дуги $\Sigma_0$ около $\omega^*$ ($d=1$, натуральный
параметр), $j<\infty$, $G(0)<0$, $G'(0)=0$, $G''(0)>0$. Положим $a_0=-G(0)$,
$\lambda_0=\frac14\min(G''(0),h_n(0))$ и

$$
0<\kappa\le\min\Big(\frac12,\ \frac{j\lambda_0}{a_0\big(\frac{15\sqrt3}8j+2\sqrt2\big)^2}\Big).\tag{8.5}
$$

Тогда для карты (8.1) при малых $r_0,s_0$ выполнены условия теоремы 2′ с $\beta=j$, весами
$(\kappa,c)$, $\mu=\kappa$, $\gamma_1=\frac54\kappa$, $\gamma_2=\kappa(1-\kappa)$. Следовательно, есть
асимптотическая траектория $q(t)=\Psi(x(t),\theta(t),\zeta(t))$ с $x(t)\asymp t^{-2/(j-2)}$,
$\lvert\theta(t)\rvert\le2\sqrt{\delta/\lambda_0}$, $\lvert\zeta(t)\rvert\le2\sqrt{\delta/\lambda_0}\,x(t)^c$. Траектория
касается конуса $Z$ (расстояние до $Z$ не больше $\lvert\eta\rvert=O(\lvert q\rvert^{\min(2,c)})$) и лежит в
конусе раствора $O(\sqrt\delta)$ вокруг луча $\mathbb R_+\omega^*$ ($\delta$ любое малое; касание
самого луча не доказано).

*Доказательство.* Выберем $r_1\in(0,\theta_1/2)$ и $r_0\in(r_1,\min(\theta_1/2,\frac14)]$ с
$[-r_0,r_0]\subset\Lambda''$ (поправка по отзыву R22, замечание 3), а $s_0$ так,
чтобы на $\mathcal N=\{0<x<s_0,\ \lvert b\rvert<r_0\}$ было $\lvert\varepsilon\rvert\le\frac14$,
$\lvert p\rvert\le\frac14$, $\lvert\eta^*_s\rvert+\frac43\lvert\eta^*_\theta\rvert/x\le1$, и точки лежали в
$\mathcal P$ леммы K3. Через $\varpi(x)$ обозначим супремум по $\{x'\le x\}$ суммы модулей малых
величин (6.5), $p$, $x\partial_x\varepsilon$, $x\partial_xp$, $\partial_\theta p$, $s\partial_sp$
(все стремятся к нулю: $p=O(x)$, $x\partial_xp=xp_s-\kappa\theta p_\theta=O(x)$, $\partial_\theta p=O(x)$,
$s\partial_sp=O(x)$), умноженный на константу $10(1+\bar k)$. Все оценки ниже равномерны на $\mathcal N$.

1. **$(\Phi0)$.** $\Phi=\Psi\circ L$, $L(x,u,\zeta)=(x,ux^{-\kappa},\zeta)$ — диффеоморфизм, $\Psi$ —
   диффеоморфизм на открытое множество (лемма K3 и сдвиг $\eta\mapsto\eta^*+\zeta$).
   $\lvert\Phi\rvert^2=x^2+\eta^2$, так что $x\le\lvert\Phi\rvert\le2x$.
2. **$(\Phi1')$.** По (8.2) $1\le h\le1+\frac{25}{16}\kappa^2r_0^2+\frac1{16}\le\frac32$.
3. **$(\Phi2')$, первая оценка.** $\nabla\rho=\nabla s=\omega$ (лемма K3). Для $w\perp Y$:
   $\langle\nabla\rho-Y/h,w\rangle=\langle\omega,w\rangle$, а из $\langle Y,w\rangle=0$ и (8.2)
   $\langle\omega,w\rangle=\kappa\theta(1-\varepsilon)\langle T,w\rangle-p\langle n,w\rangle$. Значит
   $\lvert\langle\nabla\rho-Y/h,w\rangle\rvert\le(\frac54\kappa\lvert b\rvert+\lvert p\rvert)\lvert w\rvert$: $\gamma_1=\frac54\kappa$.
4. **$(\Phi2')$, вторая оценка.** По (8.3) для единичного $w\perp Y$:
   $\lvert\langle x\partial_x^2\Phi,w\rangle\rvert\le\kappa(1-\kappa)\lvert\theta\rvert+\kappa r_0\big(\kappa\lvert\varepsilon\rvert+\lvert x\partial_x\varepsilon\rvert+\lvert p\rvert\bar k\big)+\frac54\kappa^2\theta^2(1+\bar k)+\lvert x\partial_xp\rvert$.
   Итак, $\gamma_2=\kappa(1-\kappa)$, $C_1\ge\frac54\kappa^2(1+\bar k)$, остальное — в $\varpi$.
5. **$(\Phi3)$.** Для $w\in\mathbb R^3$ разложим $w=a^s\Psi_s+a^\theta\Psi_\theta+a^\zeta\Psi_\zeta$. По (6.4)
   $a^s=w_\omega:=\langle w,\omega\rangle$, $a^\theta=w_T/(s(1-\varepsilon))$, $w_T:=\langle w,T\rangle$,
   $a^\zeta=w_n-w_\omega\eta^*_s-w_T\eta^*_\theta/(s(1-\varepsilon))$, $\lvert a^\zeta\rvert\le2\lvert w\rvert$. Тогда
   $D_wY=a^s\partial_sY+a^\theta\partial_\theta Y+a^\zeta\partial_\zeta Y$ и по (8.4)
   $$x\langle w,D_wY\rangle=w_T^2\Big(\frac1{1-\varepsilon}-\kappa\Big)+\mathcal E,$$
   $$\mathcal E=\frac{w_T}{1-\varepsilon}\Big[(\kappa\theta\partial_\theta\varepsilon-pk)w_T+\kappa\theta(1-\varepsilon)w_\omega+\big(-\kappa\theta(1-\varepsilon)k+\partial_\theta p\big)w_n\Big]+w_\omega\big[\kappa\theta\,s\partial_s\varepsilon\,w_T+s\partial_sp\,w_n\big]+a^\zeta\kappa\theta k\,w_T .$$
   Главный член $\ge(\frac45-\kappa)w_T^2\ge0$ (центробежный). Для $w\perp Y$ из п. 3
   $\lvert w_\omega\rvert\le(\frac54\kappa\lvert\theta\rvert+\lvert p\rvert)\lvert w\rvert$, поэтому
   $\lvert\mathcal E\rvert\le\big[\frac54\kappa^2r_0\lvert b\rvert+\frac53\kappa\bar k\lvert b\rvert+2\kappa\bar k\lvert b\rvert+\varpi(x)\big]\lvert w\rvert^2$.
   Итак, $(\Phi3)$ выполнено с $C_1=\frac54\kappa^2(1+\bar k)+4\kappa\bar k$ (и п. 4 тоже).
6. **(F).** $U\circ\Phi(x,u,\zeta)=U(\Psi(x,\theta,x^ce))=x^j\tilde F(x^{1/2},\theta,e)$ по (6.3): $F:=\tilde F$,
   аналитична в окрестности $[0,\sigma_0]\times\overline{B_{r_0}}$ при $\sigma_0^{j-m}r_0<y_1/2$, $r_0<\theta_1$.
7. **$(V_1')$.** $F_0(\theta,e)=G(\theta)+\frac12h_n(\theta)e^2$, $Q=G(\theta)-G(0)+\frac12h_n(\theta)e^2$,
   $F_0(0)=-a_0<0$. Возьмём $r_1$ (зависит только от $G$, $h_n$) так, чтобы при $\lvert\theta\rvert<r_1$:
   $\theta G'(\theta)-(G(\theta)-G(0))\ge\frac14G''(0)\theta^2$ (левая часть равна $\frac12G''(0)\theta^2+O(\theta^3)$),
   $G(\theta)-G(0)\ge\frac14G''(0)\theta^2$, $h_n(\theta)\ge\frac12h_n(0)$ и
   $\frac12\lvert\theta h_n'(\theta)\rvert\le\frac12h_n(\theta)$. Тогда $Q\ge\lambda_0\lvert b\rvert^2$, и при $\mu=\kappa$
   $$\kappa\theta\partial_\theta Q+ce\,\partial_eQ-\kappa Q=\kappa\big[\theta G'-(G-G(0))\big]+e^2\Big[\big(c-\tfrac\kappa2\big)h_n+\tfrac\kappa2\theta h_n'\Big]\ge0,$$
   так как $c\ge\frac32$, $\kappa\le\frac12$. Наконец (7.2):
   $\Gamma_*=\sqrt{a_0/\lambda_0}\big[\frac{3\sqrt3}2j\cdot\frac54\kappa+2\sqrt2\kappa(1-\kappa)\big]\le\kappa\sqrt{a_0/\lambda_0}\big(\frac{15\sqrt3}8j+2\sqrt2\big)$,
   и $\Gamma_*^2\le j\kappa=\beta\mu$ по (8.5).

Теорема K2 опирается на **обе** новые части теоремы 2′: на перекрёстные члены $\gamma_1,\gamma_2$ и на
ослабление $(\Phi1)$ до $(\Phi1')$ (у карты (8.1) $\lvert\partial_u\Phi\rvert\asymp x^{1-\kappa}$, так что $B$ далеко
от $I$; отзыв R22, замечание 6).

Порядок выбора констант корректен: $\kappa$ зависит только от $j$, $G(0)$, $G''(0)$, $h_n(0)$; $r_1$ —
от $G$, $h_n$; $r_0,s_0$, $C_1$, $\varpi$ — от $\kappa$ и карты; затем $\delta$ и $\sigma_*$ выбираются
внутри теоремы 2′. Теорема 2′ даёт утверждение. $\square$

**Замечание 8.1** (смысл $\kappa$). Запас Эйлера по углу равен $\approx2\kappa\cdot\frac12G''\theta^2$
(вес $\kappa$), а перекрёстные члены $T_1,T_2$ имеют порядок $\kappa\lvert\theta\rvert\lvert v_\perp\rvert\rho^{\beta/2}$.
Квадратичная форма $\beta K+\kappa G''\theta^2\rho^\beta-C\kappa\lvert\theta\rvert\sqrt K\rho^{\beta/2}$
положительна при $C^2\kappa^2<4\beta\kappa G''$, то есть при малом $\kappa$. Это аналог функции Ляпунова
$w^2+G''\theta^2-\varepsilon\theta w$ для линеаризации в раздутии Макги: там угловые собственные
числа $\lambda^2-\frac{j+2}2\lvert v_0\rvert\lambda+G''=0$ имеют положительные вещественные части, то
есть стенки трубки — выход. Оценка (8.5) грубая: численно выход строгий уже при $\kappa\in[0.007,0.5]$
(§9.8), а при $\kappa=0$ запас стремится к нулю вместе с $\sigma$.

**Замечание 8.2** (теорема K1 и K2). Карты разные: в K1 срез декартов, $Y\perp$ срезу; в K2 срез
полярный, а $Y$ — нет. При $G''+jG>0$ годятся обе.

**Замечание 8.3** (связь с предложением 1 `example13-proof.md` §6). Там: круговой конус,
$W=W_{m'}+\dots$, $m'\ge5$, $G_\pm=W_{m'}|_{\Sigma_\pm}$ с регулярным нулём ⇒ тотальная
неустойчивость [Эскиз]. Здесь $j=m'$, $G=W_{m'}|_\Sigma$ (так как $u_5=\dots=u_{m'-1}=0$, все $g_k$ с
$k<m'$ равны нулю, а $g_{m'}=W_{m'}|_\Sigma$ по замечанию 3.3.2 при $m'=5$ и по прямому разложению при
$m'>5$). Теорема K2 даёт асимптотическую траекторию при невырожденном отрицательном минимуме
$G$ на одной из окружностей. Условия разные (регулярный нуль против невырожденного минимума);
для типичного $W$ выполнены оба.

**Замечание 8.4** ($n\ge4$, $\dim\Sigma_0=1$) [Эскиз]. Конус над кривой в $S^{n-1}$ по-прежнему
развёртывается; нормальное пространство $(n-2)$-мерно, рамку $e_a(\theta)$ можно взять
параллельной относительно нормальной связности. Тогда в (6.1) появятся члены кручения
$e_a'=-k_aT+\sum_b\tau_{ab}e_b$ с $\tau=0$ для параллельной рамки, и выкладки §6, §8 повторяются с
$kn\to\sum_ak_ae_a$. Не выписано.

## 9. Примеры

Везде $Q_0=x^2+y^2-z^2$, верхняя окружность $\Sigma_+$:
$\omega(\varphi)=\frac1{\sqrt2}(\cos\varphi,\sin\varphi,1)$, натуральный параметр $\theta=\varphi/\sqrt2$,
$T=(-\sin\varphi,\cos\varphi,0)$, $n=\omega\times T=\frac1{\sqrt2}(-\cos\varphi,-\sin\varphi,1)$, $k=1$,
$h_n=2\lvert\nabla Q_0\rvert^2=8$. Для $u_4=Q_0^2$ (K1), (K2) выполнены: $\Sigma=\Sigma_+\cup\Sigma_-$,
$D^2u_4=2\nabla Q_0\nabla Q_0^{\mathsf T}$ на конусе. $G''$ — по $\theta$, то есть $G''=2\,d^2G/d\varphi^2$.
Ряды $y^*(s)$ и $g_k$ посчитаны в `examples.py` (точная арифметика sympy), проверка (6.3) — численно:
$U(\Psi(s,\theta,s^ce))/s^j-\tilde F(0,\theta,e)=O(s^{1/2})$ или лучше при $s=10^{-2},10^{-3},10^{-4}$
в трёх точках $(\theta,e)$ [Эксперимент].

| Пример | $j$ | $c$ | $\varphi^*$ | $G(\omega^*)$ | $G''$ | $G''+jG$ | класс | $\kappa$ по (8.5) |
|---|---|---|---|---|---|---|---|---|
| 9.1 Пример 13: $Q_0^2+z^5x+z^4xy+\frac12z^6$ | 6 | 2 | $5\pi/6$ | $\frac1{16}-\frac{3\sqrt3}{32}$ | $\frac{3\sqrt3}8$ | $0.0502$ | $\mathcal K^1_{\rm C}$ | $0.0196$ |
| 9.2 Теорема B: $Q_0^2+xz^4$ | 5 | 3/2 | $\pi$ | $-\frac{\sqrt2}8$ | $\frac{\sqrt2}4$ | $-\frac{3\sqrt2}8$ | $\mathcal K^1\setminus\mathcal K^1_{\rm C}$ | $0.0069$ |
| 9.3 $Q_0^2+xz^4+y^2z^3$ | 5 | 3/2 | $\pi$ | $-\frac{\sqrt2}8$ | $\frac{3\sqrt2}4$ | $\frac{\sqrt2}8$ | $\mathcal K^1_{\rm C}$ | $0.0206$ |
| 9.4 $Q_0^2+xz^6+xy^2z^4$ | 7 | 5/2 | $\arccos(-\sqrt{2/3})$ | $-\frac{\sqrt3}{18}$ | $\frac{\sqrt3}6$ | $-\frac{2\sqrt3}9$ | $\mathcal K^1\setminus\mathcal K^1_{\rm C}$ | $0.0080$ |
| 9.5 Сдвиг: $Q_0^2+2Q_0z^2x-\frac1{10}z^6$ | 6 | 2 | $0,\pi$ | $-\frac{11}{80}$ | $\frac12$ | $-\frac{13}{40}$ | $\mathcal K^1\setminus\mathcal K^1_{\rm C}$ | $0.0110$ |
| 9.7 Искривлённое дно: $(Q_0+z^3)^2+xz^6+xyz^5+\frac12z^7$ | 7 | 5/2 | $5\pi/6$ | $\frac{\sqrt2(2-3\sqrt3)}{64}$ | $\frac{3\sqrt6}{16}$ | $-0.0351$ | $\mathcal K^1\setminus\mathcal K^1_{\rm C}$ | $0.0174$ |

Принадлежность классу проверяется по точным значениям из таблицы (они получены точно, но
программой; ниже для каждого примера — ручная проверка главного).

### 9.1. Пример 13

$u_5=0$, поэтому $y^*=O(s^2)$, $g_5=0$, $g_6=u_6|_{\Sigma_+}=\frac1{16}+\frac18\cos\varphi+\frac1{16}\sin2\varphi$
(как в [GT3, §6.3] с $G_{\rm GT3}=8g_6$). $G''+6G=\frac38-\frac{3\sqrt3}{16}\approx0.0502$ совпадает с
$H_{11}$ из [GT3, §6.3]: теорема K1 воспроизводит предложение 3 [GT3] (с картой, отличающейся
сдвигом $\eta^*=O(s^3)$). Теорема K2 даёт то же другой картой.

### 9.2. Пример теоремы B: $U=Q_0^2+xz^4$

$g_5=u_5|_{\Sigma_+}=\frac{\cos\varphi}{4\sqrt2}$ (вручную: $x=\frac{\cos\varphi}{\sqrt2}$, $z^4=\frac14$), минимум
при $\varphi=\pi$, $G=-\frac1{4\sqrt2}$, $G''=2\cdot\frac1{4\sqrt2}$, $G''+5G=-\frac3{4\sqrt2}<0$. Декартова
карта не годится, теорема K2 — годится. [Эксперимент: $g_6=-\frac9{512}\cos^2\varphi$ по ряду совпадает с
формулой замечания 3.3.2.] Это даёт асимптотическую траекторию в ситуации теоремы B. Правда, для
этого примера неустойчивость следует и из радиального условия Четаева (§9.6).

### 9.3–9.4. $Q_0^2+W_5$ и $Q_0^2+W_7$

9.3: $G=\frac{\cos\varphi+\sin^2\varphi}{4\sqrt2}$, $d^2G/d\varphi^2(\pi)=\frac{3}{4\sqrt2}$, $G''+5G=\frac{1}{4\sqrt2}>0$.
9.4: $u_5=u_6=0$, $G=W_7|_{\Sigma_+}=\frac{\sqrt2}{16}(1+\sin^2\varphi)\cos\varphi=\frac{\sqrt2}{16}(2\cos\varphi-\cos^3\varphi)$;
минимум по $\mathrm c=\cos\varphi\in[-1,1]$ функции $2\mathrm c-\mathrm c^3$ — при $\mathrm c=-\sqrt{2/3}$, то есть
**не** при $\varphi=\pi$ (там $d^2G/d\varphi^2<0$). $G''+7G<0$: нужна теорема K2.

### 9.5. Пример со сдвигом: $U=Q_0^2+2Q_0z^2x-\frac1{10}z^6$

$u_5=2Q_0z^2x$ обращается в нуль на $\Sigma$, но $\partial_nu_5=2\lvert\nabla Q_0\rvert z^2x\ne0$. Наивное
ограничение $u_6|_{\Sigma_+}=-\frac1{80}$ постоянно (вырожденный случай), а по замечанию 3.3.2
$G=g_6=u_6-\frac12(\partial_nu_5)^2/h_n=-\frac{z^6}{10}-z^4x^2=-\frac18\big(\cos^2\varphi+\frac1{10}\big)$
(равенство проверено и рядом, расхождение $<10^{-16}$ на сетке). Минимумы $\varphi=0,\pi$ невырождены:
сдвиг необходим, и он меняет ответ. Это вид $U=(Q_0+z^2x)^2-z^4x^2-\frac1{10}z^6$ («жёлоб надо
искать», `example13-proof.md` §7).

### 9.6. $s=0$: $U=(x^2-z^2)^2+(y^2-z^2)^2+z^5$

$\Sigma=\{(\pm1,\pm1,\pm1)/\sqrt3\}$ (8 точек; $u_4=A^2+B^2$, $A=x^2-z^2$, $B=y^2-z^2$). В
$\omega^*=(1,1,-1)/\sqrt3$: $\nabla A=\frac2{\sqrt3}(1,0,1)$, $\nabla B=\frac2{\sqrt3}(0,1,1)$ ортогональны
$\omega^*$ и независимы, $D^2u_4=2(\nabla A\nabla A^{\mathsf T}+\nabla B\nabla B^{\mathsf T})\succ0$ на
$\omega^{*\perp}$ (в базисе $e_1=(1,-1,0)/\sqrt2$, $e_2=(1,1,2)/\sqrt6$: $H=\operatorname{diag}(\frac83,8)$).
$j=5$, $g_5(\omega^*)=z^5=-3^{-5/2}<0$. По теореме K0 есть асимптотическая траектория. Точка $0$
изолирована: $\partial_xU=4xA$, $\partial_yU=4yB$, и в каждом из четырёх случаев
($x=0$ или $A=0$; $y=0$ или $B=0$) уравнение $\partial_zU=0$ сводится к многочлену от $z$ с
единственным малым корнем $z=0$ (аналогично §9.7, проверено вручную). Здесь, однако, радиальное
условие Четаева выполнено тривиально: на $\{U<0\}$ имеем $z^5<0$ и
$\langle\nabla U,q\rangle=4U+z^5<0$.

**Радиальное условие Четаева в двухчленных примерах.** Если $U=u_m+u_k$ с одним однородным
$u_k$, то $\langle\nabla U,q\rangle=mU+(k-m)u_k$, а на $\{U<0\}$ $u_k<-u_m\le0$; значит
$\langle\nabla U,q\rangle<0$ на $\{U<0\}$. Это относится к §9.2, 9.3, 9.4, 9.6. Для примера 13
$\langle\nabla U,q\rangle=6U-2Q_0^2<0$ на $\{U<0\}$ (так в [GT3, §9]). Тогда по теореме Четаева
равновесие неустойчиво, а по AG17, Prop. 8 («строгое условие Четаева ⇒ асимптотическое
движение») [Литература: AG17, по конспекту `notes/literature/2026-10-21-revision-rest.md` §1.2; не
сверено] есть и асимптотическая траектория. **Для этих примеров теоремы K0–K2 нового не дают**;
вероятно, это касается и вывода «следствие 4 [GT3] — новое» для примера 13 (стоит сверить AG17,
Prop. 8 по первоисточнику). Пример 9.5 не двухчленный ($u_5$ и $u_6$); для него радиальное
условие не доказано, но численно не нарушается. [Эксперимент `examples.py`: для 9.1, 9.2, 9.4, 9.5
среди 1400–2000 случайных точек $\{U<0\}$ около дна при $s=10^{-2},10^{-3}$ нет ни одной с
$\langle\nabla U,q\rangle>0$.]

### 9.7. Искривлённое дно: где теоремы K0, K2 дают новое

Исправлено по отзыву R22 (замечания 1, 2, 4, 5): выписан вывод $j=7$ и $G=u_7|_\Sigma$
двусторонней оценкой, нарушение радиального условия Четаева доказано явными семействами,
оговорена неизолированность $U_{(8)}$ над $\mathbb C$, расставлены метки.

**$U_{(7)}=P_1^2+P_2^2+z^7$, $P_1=x^2-z^2+z^3$, $P_2=y^2-z^2$ ($s=0$).** Здесь $u_4=A^2+B^2$ с
$A=x^2-z^2$, $B=y^2-z^2$, как в §9.6: $\Sigma=\{(\pm1,\pm1,\pm1)/\sqrt3\}$, (K1), (K2) выполнены.

*$j=7$ и $g_7(\omega)=z(\omega)^7$ во всех точках $\Sigma$* [Доказано]. Пусть $\omega\in\Sigma$,
$e_1,e_2$ — ортонормированный базис $\omega^\perp$, $v=\omega+y_1e_1+y_2e_2$. Так как
$P_1(sv)=s^2\big(A(v)+s\,z(v)^3\big)$ и $P_2(sv)=s^2B(v)$,
$$\varphi(s,y)=p_1^2+p_2^2+s^3z(v)^7,\qquad p_1=A(v)+s\,z(v)^3,\quad p_2=B(v).$$
Снизу: $R(s)=\varphi(s,y^*)\ge s^3z(\omega+y^*)^7=s^3z(\omega)^7+O(s^4)$, так как $y^*=O(s)$ (лемма K1).
Сверху: отображение $y\mapsto(p_1,p_2)$ при $s=0$, $y=0$ имеет матрицу Якоби
$(\langle\nabla A(\omega),e_a\rangle,\langle\nabla B(\omega),e_a\rangle)$, а $\nabla A(\omega)$, $\nabla B(\omega)$
независимы и ортогональны $\omega$ (§9.6). По теореме о неявной функции есть $y_0(s)=O(s)$ с
$p_1=p_2=0$, и $R(s)\le\varphi(s,y_0)=s^3z(\omega+y_0)^7=s^3z(\omega)^7+O(s^4)$. Значит,
$g_5=g_6=0$, $g_7(\omega)=z(\omega)^7=\pm3^{-7/2}$, $j=7$. В $\omega^*=(1,1,-1)/\sqrt3$
$g_7=-3^{-7/2}=-\frac{\sqrt3}{81}<0$: $U_{(7)}\in\mathcal K^0$, и по теореме K0 есть асимптотическая
траектория. [Эксперимент `examples_s0.py`: в базисе $e_1=(1,-1,0)/\sqrt2$, $e_2=(1,1,2)/\sqrt6$
ряд даёт $y^*(s)=(\frac{\sqrt2}{12},\frac{\sqrt6}{36})s+O(s^2)$ — дно искривлено уже в первом порядке;
при $e_2\mapsto-e_2$ знак второй компоненты меняется.]

*Изолированность* [Доказано]: $\partial_xU=4xP_1$, $\partial_yU=4yP_2$, и
- $P_1=P_2=0$: $\partial_zU=7z^6$, значит $z=0$, $x=y=0$;
- $P_1=0$, $y=0$: $\partial_zU=z^3(7z^3+4)$;
- $x=0$, $P_2=0$: $\partial_zU=z^3(7z^3+6z^2-10z+4)$;
- $x=y=0$: $\partial_zU=z^3(7z^3+6z^2-10z+8)$;

в трёх последних случаях малый корень только $z=0$, откуда $x=y=0$. Над $\mathbb C$ точка тоже
изолирована: число Милнора $\mu=39$ [Эксперимент: Singular, отзыв R22]. Гессиан нулевой,
$u_4\ge0$, $0$ — не минимум ($U=z^7<0$ на кривой $P_1=P_2=0$, $z<0$): жёсткое ядро.

**$U_{(8)}=P^2+u_7$, $P=Q_0+z^3$, $u_7=xz^6+xyz^5+\frac12z^7$ ($s=1$).** Здесь $u_4=Q_0^2$,
$\Sigma=\Sigma_+\cup\Sigma_-$, $h_n=8$.

*$j=7$ и $G_\pm=u_7|_{\Sigma_\pm}$* [Доказано]. Для $\omega\in\Sigma$ с нормалью $n$:
$\varphi(s,y)=p(s,y)^2+s^3u_7(\omega+yn)$, $p=Q_0(\omega+yn)+s\,z(\omega+yn)^3$. Снизу
$R\ge s^3u_7(\omega+y^*n)=s^3u_7(\omega)+O(s^4)$. Сверху: $\partial_yQ_0(\omega+yn)|_{y=0}=\langle\nabla Q_0(\omega),n\rangle=\pm2\ne0$,
по теореме о неявной функции есть $y_0(s)=O(s)$ с $p=0$, и $R\le s^3u_7(\omega+y_0n)=s^3u_7(\omega)+O(s^4)$.
Оценки равномерны на компактном $\Sigma$. Значит, $g_5=g_6\equiv0$, $j=7$ на обеих окружностях и
$$G_+=\tfrac{\sqrt2}{32}\big(1+2\cos\varphi+\sin2\varphi\big),\qquad G_-=\tfrac{\sqrt2}{32}\big(2\cos\varphi-\sin2\varphi-1\big)$$
(подстановка $x=\frac{\cos\varphi}{\sqrt2}$, $y=\frac{\sin\varphi}{\sqrt2}$, $z=\pm\frac1{\sqrt2}$). Критические точки $G_+$:
$\cos2\varphi=\sin\varphi$, то есть $\sin\varphi\in\{\frac12,-1\}$, $\varphi\in\{\frac\pi6,\frac{5\pi}6,\frac{3\pi}2\}$, значения
$\frac{\sqrt2}{32}(1+\frac{3\sqrt3}2)$, $\frac{\sqrt2}{32}(1-\frac{3\sqrt3}2)$, $\frac{\sqrt2}{32}$. Глобальный минимум —
$\varphi^*=5\pi/6$: $G_+(\varphi^*)=\frac{\sqrt2(2-3\sqrt3)}{64}\approx-0.0706$, $\frac{d^2G_+}{d\varphi^2}=\frac{\sqrt2}{32}\cdot3\sqrt3$,
$G''=2\frac{d^2G_+}{d\varphi^2}=\frac{3\sqrt6}{16}\approx0.459$ (по натуральному параметру),
$G''+7G=\frac{7\sqrt2}{32}-\frac{9\sqrt6}{64}\approx-0.035<0$. Итак, $U_{(8)}\in\mathcal K^1\setminus\mathcal K^1_{\rm C}$:
теорема K2 (не K1) даёт асимптотическую траекторию, $\kappa\le0.0174$ по (8.5).

*Изолированность над $\mathbb R$* [Доказано] — по следствию K4′: $j=7$ на обеих окружностях, и $0$ —
регулярное значение $G_\pm$. Для $G_+$ все критические значения выше ненулевые. Для $G_-$:
$G_-'=0\iff2\sin^2\varphi-\sin\varphi-1=0\iff\sin\varphi\in\{1,-\frac12\}$, $\varphi\in\{\frac\pi2,\frac{7\pi}6,\frac{11\pi}6\}$,
значения $\frac{\sqrt2}{32}\cdot(-1)$, $\frac{\sqrt2}{32}(-1-\frac{3\sqrt3}2)$, $\frac{\sqrt2}{32}(\frac{3\sqrt3}2-1)$ — ненулевые.
(Раньше это проверялось результантом $-376832\ne0$ в `examples.py`; независимо — Singular, отзыв R22.)

*Над $\mathbb C$ точка $0$ не изолирована* [Доказано] (отзыв R22, замечание 1): при $z=0$
$\nabla U_{(8)}=\big(4x(x^2+y^2),\,4y(x^2+y^2),\,0\big)$, так что комплексные прямые $\{z=0,\ x=\pm iy\}$
состоят из критических точек, и число Милнора бесконечно. Это ровно ловушка из CLAUDE.md:
изолированность над $\mathbb R$ не влечёт изолированность над $\mathbb C$. Для задачи (A) нужна
только вещественная изолированность, но результаты, требующие $\mu<\infty$, к $U_{(8)}$ неприменимы.
У $U_{(7)}$ и у §9.6 $\mu=39$ и $31$ [Эксперимент, R22].

Плоскость через $\omega^*$ и ось $z$ не инвариантна: при $\varphi=\varphi^*$ вне конуса
$\partial_\varphi u_7=\frac{Rz^5}2(R-z)\ne0$, $R=\sqrt{x^2+y^2}$; так что очевидного сведения к $n=2$
нет. (Первый вариант примера, $(Q_0+z^3)^2+xz^6$, чётен по $y$, и плоскость $y=0$ инвариантна.)

**Радиальное условие Четаева нарушено** [Доказано] (семейства — из отзыва R22, замечание 4(c),
нижняя полость $U_{(8)}$ добавлена здесь). Тождества (проверены символьно,
`experiments/prover/gt3-result008/chetaev_families.py`):
$$\langle\nabla U_{(7)},q\rangle=4U_{(7)}+2z^3P_1+3z^7,\qquad\langle\nabla U_{(8)},q\rangle=4U_{(8)}+2z^3P+3u_7 .$$
- $U_{(7)}$: $q(\tau)=\big(\sqrt{\tau^2+\tau^3-\tau^{7/2}/2},\ \tau,\ -\tau\big)$, $\tau>0$. Тогда $P_1=-\frac12\tau^{7/2}$,
  $P_2=0$, $U=-\frac34\tau^7<0$ и $\langle\nabla U,q\rangle=\tau^{13/2}-6\tau^7>0$ при $\tau<\frac1{36}$;
  $q(\tau)/\lvert q(\tau)\rvert\to\omega^*$.
- $U_{(8)}$, верхняя полость: $\varphi=\frac{5\pi}6$, $z=\zeta>0$. На отрезке $R\in[\zeta\sqrt{1-\zeta},\zeta]$
  имеем $u_7=\zeta^7\big(\frac12-\frac{3\sqrt3}4+O(\zeta)\big)$, то есть $c\zeta^7\le-u_7\le C\zeta^7$, а
  $P=R^2-\zeta^2+\zeta^3$ возрастает от $0$ до $\zeta^3>\frac12\sqrt{-u_7}$. По теореме о промежуточном
  значении есть $R$ с $P=\frac12\sqrt{-u_7}$. Тогда $U=-\frac34\lvert u_7\rvert<0$ и
  $\langle\nabla U,q\rangle=\zeta^3\sqrt{\lvert u_7\rvert}-6\lvert u_7\rvert>0$ (так как $\sqrt{\lvert u_7\rvert}\le\sqrt C\zeta^{7/2}<\zeta^3/6$).
- $U_{(8)}$, нижняя полость: $\varphi=\pi$, $z=-\zeta<0$, $R\in[\zeta,\sqrt{\zeta^2+\zeta^3}]$. Здесь $y=0$,
  $u_7=-R\zeta^6-\frac12\zeta^7<0$, $P$ возрастает от $-\zeta^3$ до $0$, и есть $R$ с $P=-\frac12\sqrt{-u_7}$.
  Тогда $2z^3P=\zeta^3\sqrt{\lvert u_7\rvert}$, $U=-\frac34\lvert u_7\rvert<0$, $\langle\nabla U,q\rangle=\zeta^3\sqrt{\lvert u_7\rvert}-6\lvert u_7\rvert>0$.

[Эксперимент `chetaev_families.py`: $\langle\nabla U,q\rangle/\lvert U\rvert=7.0$, $39$, $141$, $464$ (верх) и
$2.9$, $26$, $101$, $336$ (низ) при $\zeta=10^{-2},\dots,10^{-5}$.]

*Все компоненты.* [Доказано] Около $0$ множество $\{U<0\}$ лежит в конических трубках над теми
лучами (у $U_{(7)}$) или дугами (у $U_{(8)}$), где $G<0$ (вне трубок $U>0$, а над лучами и дугами с
$G>0$ $U\ge U_{\rm red}>0$; следствие K0′(a), предложение K4(a)). В каждой такой трубке
$\{U<0\}$ связно: в каждом слое это выпуклое подмножество (подуровень строго выпуклой функции
$\varphi(s,\theta,\cdot)$), содержащее точку дна, а точки дна образуют связное множество (у $U_{(8)}$:
$\{(s,\theta):\ R(s,\theta)<0\}$ при малых $s$ — криволинейная полоса между двумя ветвями нулей $\hat G$,
выходящими из регулярных нулей $G$ по теореме о неявной функции; отрицательные множества $G_+$
и $G_-$ — по одной дуге, так как каждая компонента $\{G<0\}$ содержит минимум, а отрицательные
критические значения $G_+$ — одно, $G_-$ — два на одной дуге). У $U_{(7)}$ таких трубок четыре
(лучи $(\pm1,\pm1,-1)/\sqrt3$, переводятся друг в друга симметриями $x\mapsto-x$, $y\mapsto-y$),
у $U_{(8)}$ — две. Семейства выше лежат в этих трубках, поэтому **в каждой компоненте $\{U<0\}$,
примыкающей к $0$, есть точки с $\langle\nabla U,q\rangle>0$ сколь угодно близко к $0$**: строгое
условие Четаева (в форме AG17, Prop. 8) не выполнено ни для одной компоненты.

*Класс $\mathcal H$ Alva–Garcia.* Здесь $U$ — многочлен степени 7, $j^7U=U$, и условие (H3) (в
любом из двух вариантов: с замыканием и без, по конспекту `notes/literature/2026-10-21-revision-rest.md`
§1.2) требует $\langle\nabla j^7U,q\rangle<0$ на компоненте $\{j^7U<0\}$. По доказанному выше это не
так. [Литература: AG17 — формулировка (H3) по конспекту, с первоисточником не сверена.]
Первая ненулевая форма $u_4\ge0$, гессиан нулевой — критерии по первой струе и FGT08 тоже не
работают. **По доступным в репозитории конспектам литературы (A) для этих примеров не было
известно** (поиск неполный; MN89, MMN91, KP82, Паламодов 2020 Thm 6 не открывались).

[Эксперимент: доля точек $\{U<0\}$ около дна с $\langle\nabla U,q\rangle>0$ — $500/1219$ и $515/1151$
($U_{(8)}$, верх, $s=10^{-2},10^{-3}$), $595/1759$ и $792/1769$ (низ), $882/2536$, $1169/2585$, $1229/2545$
($U_{(7)}$, $\lvert q\rvert\sim10^{-2},10^{-3},10^{-4}$); `examples.py`, `examples_s0.py`, `chetaev_lower.py`.]

*Общий механизм* [Эскиз]: $\langle\nabla U,q\rangle=jU-(c-1)s^jh_ne^2+O(s^{m+c})\cdot e$, где последний член
— от $\partial_s\eta^*\ne0$; при $c>2$ он главнее $s^j$, и радиальная производная знакопеременна на
$\{U<0\}$. Это ситуация «оврага» Гарсии–Тала (искривлённая кривая дна), в которой нужна карта
$\gamma(x)=\eta^*(x)$. Не доказано в общем виде; для двух примеров выше — доказано явными семействами.

### 9.8. Эксперименты [Эксперимент]

Все скрипты — в `experiments/prover/gt3-hardcore/`, запуск `~/venv/bin/python <скрипт>`.

| Скрипт | Что проверяет | Результат |
|---|---|---|
| `frame_check.py` | формулы (6.4), (8.2)–(8.4) и декартовы формулы §6.2 в подвижном репере (6.1) с многочленами $k(\theta)$, $\eta^*(s,\theta)$ общего вида | все тождества: `True` |
| `reduced.py` | ряды $y^*(s)$, $R(s)$ (порядок за порядком из $\partial_y\varphi=0$) | — (модуль) |
| `examples.py` → `examples.out` | §9.1–9.5, 9.7 ($s=1$): $g_k$, $j$, $G$, минимум (сетка + уточнение корня $G'$), $G''$, $G''+jG$, $\kappa$ из (8.5), нормальная форма (6.3), радиальное условие Четаева | см. таблицу §9; $U/s^j-\tilde F(0,\cdot)\to0$ как $s^{1/2}$ или быстрее |
| `examples_s0.py` → `examples_s0.out` | §9.6, 9.7 ($s=0$): $H$, $y^*$, $g_5..g_8$, Четаев, изолированность $U_{(7)}$ по случаям | $H=\operatorname{diag}(\frac83,8)$; $g_5=-\frac{\sqrt3}{27}$ (9.6); $g_7=-\frac{\sqrt3}{81}$ (9.7) |
| `chetaev_lower.py` → `chetaev_lower.out` | $U_{(8)}$ на нижней полости: $g_k$, $y^*$, радиальное условие Четаева | $g_7=G_-$; нарушение в 34–45 % точек |
| `shooting_curved.py` → `shooting_curved.out` | $U_{(8)}$: стрельба по схеме теоремы A [GT3] — из точек дна $\Psi(x_0,0,0)$, $x_0=0.04,\dots,0.004$, назад по времени до $s=0.12$ (DOP853, rtol $10^{-12}$); затем прямой прогон из последней точки входа | точки входа сходятся: $\lvert q_k-q_{\rm last}\rvert=5.1\cdot10^{-5},\,1.3\cdot10^{-5},\,3.0\cdot10^{-6},\,7.3\cdot10^{-7}$; прямой прогон до $t=3\cdot10^6$ идёт по закону $s^{-5/2}=s_{\rm in}^{-5/2}+\frac52\sqrt{2a_0}\,t$ (совпадение в 2–4 знаках), $\lvert\varphi-\varphi^*\rvert\le3.3\cdot10^{-3}$, $y/\lvert q\rvert\to0.3533\approx\sin\varphi^*/\sqrt2$ |
| `../gt3-result008/chetaev_families.py` → `chetaev_families.out` | §9.7: тождества для $\langle\nabla U,q\rangle$, явные семейства с $U<0<\langle\nabla U,q\rangle$ ($U_{(7)}$ точно, $U_{(8)}$ — обе полости), комплексные критические прямые $U_{(8)}$ | см. §9.7 |
| `exit_check.py thmB`, `exit_check.py curved` → `exit_check_*.out` | строгий выход (A5) для карты (8.1): $\Xi=\frac d{dt}(V-\delta\rho^j)$ — прямым численным дифференцированием вдоль поля $(v,-\nabla U)$ в $\mathbb R^3$, без формулы (3.3) [GT3]; точки стенки $W=\delta\rho^j$ с $K_\perp=\tau\delta\rho^j$, $\tau\in\{0,10^{-3},10^{-2},0.05,0.2,0.5\}$, все направления $v_\perp\perp Y$ (24 угла), 40 точек стенки; плюс 600 случайных точек | см. ниже |

Минимум $\frac\rho\lambda\Xi/(\delta\rho^j)$ по перебору стенки (пример теоремы B, `exit_check_thmB.out`):

| $\kappa$ | $\delta=0.01$, $\sigma=0.05$ | $\delta=0.002$, $\sigma=0.005$ |
|---|---|---|
| 0 | 0.0206 | 0.0114 |
| 0.007 | 0.0348 | 0.0255 |
| 0.05 | 0.118 | 0.108 |
| 0.2 | 0.359 | 0.346 |
| 0.5 | 0.639 | 0.621 |

Для $U_{(8)}$ (`exit_check_curved.out`) картина та же: при $\kappa=0,\,0.007,\,0.05,\,0.2,\,0.5$
минимумы $0.041/0.023$, $0.055/0.037$, $0.140/0.123$, $0.415/0.402$, $0.882/0.874$ (для
$(\delta,\sigma)=(0.01,0.05)/(0.002,0.005)$). При $\kappa=0$ запас мал и убывает вместе с $\sigma$: он
создаётся только членом $-\frac\sigma N\partial_\sigma F$ (у примера теоремы B $g_6<0$), который
исчезает при $\sigma\to0$, — это согласуется с замечанием 6.1. При $\kappa>0$ запас порядка
$2\kappa$ и от $\sigma$ почти не зависит. Это не доказательство.

## 10. Вне класса $\mathcal K$ и подходы

### 10.1. Предложение K4 (сведение к задаче на дне, $s=1$, $n=3$) [Доказано]

**Предложение K4.** Пусть $n=3$, выполнены (K1), (K2) и $\Sigma_0$ — компонента-кривая. В
обозначениях §6 (дуги $\Sigma_0$ покрываются конечным числом карт; $R,\eta^*$ от карты не зависят,
замечание 3.3.1) положим $F_{\rm fl}(s,\theta):=s^mR(s,\theta)=U_{\rm red}$ («функция дна»). Константу
$y_1$ леммы K1 возьмём не больше $t_1$ из леммы K3 (лемма K1 верна при любом меньшем $y_1$, если
соответственно уменьшить $s_1$; поправка по отзыву R20, замечание 4); тогда при $0<s<s_1$ и
$\lvert\eta\rvert<y_1s$ отображение $P$ — локальный диффеоморфизм. «Конической трубкой» точечной
компоненты $\{\omega\}$ называем конус $C_\omega$ из доказательства следствия K0′(a). Тогда при
$0<s<s_1$:

- **(a)** $U(s\omega(\theta)+\eta n(\theta))\ge F_{\rm fl}(s,\theta)$ при $\lvert\eta\rvert<y_1s$, с равенством
  только при $\eta=\eta^*(s,\theta)$;
- **(b)** точка $q=\Psi(s,\theta,\zeta)$ конической трубки $\{\lvert\eta\rvert<y_1s\}$ критическая для $U$
  тогда и только тогда, когда $\zeta=0$ и $(s,\theta)$ — критическая точка $F_{\rm fl}$;
- **(c)** если все компоненты $\Sigma$ удовлетворяют (K2), то около $0$ вне объединения
  конических трубок $\nabla U\ne0$ и $U>0$. Следовательно, $0$ — локальный минимум $U$ тогда и
  только тогда, когда $F_{\rm fl}\ge0$ при малых $s>0$ на всех кривых-компонентах и
  $R_\omega(s)\ge0$ при малых $s>0$ во всех точечных компонентах (то есть $R_\omega\equiv0$ или её
  старший коэффициент положителен); $0$ изолирована тогда и только тогда, когда у $F_{\rm fl}$ нет
  критических точек при малых $s>0$ и $R_\omega\not\equiv0$ в точечных компонентах.

  (В первой версии записки критерий минимума требовал «старшие коэффициенты $R_\omega$
  положительны»; при $R_\omega\equiv0$ это неверно. Контрпример R20 (замечание 1):
  $U=x^2\big((y-x^2)^2+(z-x^2)^2\big)$ — $\Sigma$ — окружность $\{x=0\}$ и точки $(\pm1,0,0)$, (K1), (K2)
  выполнены, в точках $R_\omega\equiv0$, на окружности $F_{\rm fl}\equiv0$, а $U\ge0$ — минимум. При
  изолированной точке $R_\omega\not\equiv0$, и обе формулировки совпадают.)

*Доказательство.* (a) — лемма K1, п. 2, и (3.2). (b) $U\circ\Psi(s,\theta,\zeta)=s^m\varphi(s,\theta,y^*+\zeta/s)$.
«$\Rightarrow$» (цепное правило, обратимость $D\Psi$ не нужна): если $\nabla U(q)=0$, то
$\partial_\zeta(U\circ\Psi)=s^{m-1}\partial_y\varphi=0$, что возможно только при $\zeta=0$
(единственность критической точки в слое); при $\zeta=0$ $U\circ\Psi=F_{\rm fl}$, так что
$\partial_s,\partial_\theta$ от $U\circ\Psi$ — это $\partial_s,\partial_\theta$ от $F_{\rm fl}$, и они равны нулю.
«$\Leftarrow$»: $d(U\circ\Psi)=0$ в точке $(s,\theta,0)$, а $D\Psi$ там обратим (выбор $y_1\le t_1$, лемма K3),
поэтому $\nabla U=0$. (c) Если
$\nabla u_m(q)=0$, то $mu_m(q)=\langle\nabla u_m(q),q\rangle=0$ и $q\in Z$; вне конической трубки
$\lvert\nabla u_m(q)\rvert\ge c\lvert q\rvert^{m-1}$ и $u_m\ge c\lvert q\rvert^m$ (компактность и
однородность), а $\lvert\nabla U-\nabla u_m\rvert\le C\lvert q\rvert^m$, $\lvert U-u_m\rvert\le C\lvert q\rvert^{m+1}$.
Критерий минимума: «$\Leftarrow$» — в трубках кривых $U\ge F_{\rm fl}\ge0$ по (a), в конусах точек
$U\ge s^mR_\omega\ge0$ (лемма K1, п. 2), вне трубок $U>0$; «$\Rightarrow$» — $F_{\rm fl}(s,\theta)=U(\Psi(s,\theta,0))$ и
$s^mR_\omega(s)=U(s\omega+\eta^*_\omega(s))$ — значения $U$ в точках, сколь угодно близких к нулю. Критерий
изолированности: «$\Leftarrow$» — вне трубок критических точек нет, в трубке кривой критическая точка
дала бы критическую точку $F_{\rm fl}$ по (b), «$\Rightarrow$», в конусе точки — критическую точку функции
$s\mapsto s^mR_\omega(s)$ (как в K0′(b)), а у неё $(s^mR_\omega)'=s^{j-1}(jg_j+O(s))\ne0$; «$\Rightarrow$» — если
$R_\omega\equiv0$, точка неизолирована по K0′(b), а критические точки $F_{\rm fl}$ со сколь угодно малыми $s$
дают по (b), «$\Leftarrow$», критические точки $U$ сколь угодно близко к нулю. $\square$

**Следствие K4′ (изолированность по $G$)** [Доказано]. Пусть $n=3$, выполнены (K1), (K2), на
каждой компоненте-кривой $\Sigma_0$ число $j(\Sigma_0)$ конечно и $0$ — регулярное значение
$G=g_j|_{\Sigma_0}$, а в каждой точечной компоненте $j(\omega)<\infty$. Тогда $0$ — изолированная
критическая точка $U$.

*Доказательство.* На кривой-компоненте $F_{\rm fl}=s^j\hat G(s,\theta)$, так что
$\partial_sF_{\rm fl}=s^{j-1}\big(j\hat G+s\partial_s\hat G\big)$, $\partial_\theta F_{\rm fl}=s^j\partial_\theta\hat G$.
На компактной $\Sigma_0$ функция $(jG)^2+G'^2$ положительна (регулярность нуля), значит
$(j\hat G+s\partial_s\hat G)^2+(\partial_\theta\hat G)^2\ge c>0$ при малом $s$, и у $F_{\rm fl}$ нет
критических точек с малым $s>0$. Для точечной компоненты то же рассуждение с
$\frac d{ds}\big(s^mR_\omega(s)\big)=s^{j-1}\big(jg_j(\omega)+O(s)\big)\ne0$ и аналогом п. (b) (как в
доказательстве следствия K0′(b): критическая точка в конической трубке лежит на дне и критична
для $s\mapsto s^mR_\omega(s)$). Вне трубок критических точек нет по п. (c). $\square$

Это аналог вывода изолированности из (B3) в теореме B [B, (c)], для любого $j$. Пример §9.7
($U_{(8)}$) изолирован по этому следствию.

Итак, **при $n=3$ и $\Sigma$ Морса–Ботта жёсткое ядро — это семейство двумерных задач «на дне»**:
аналитическая функция $F_{\rm fl}(s,\theta)=s^{m+1}\big(g_{m+1}(\theta)+sg_{m+2}(\theta)+\dots\big)$ на
полуцилиндре $[0,s_1)\times\Sigma_0$ (развёртка — плоский конус), без критических точек при
$s>0$, принимающая отрицательные значения; нормальное направление — невырожденный
«быстрый» овраг ширины $\asymp s^{c}$. Класс $\mathcal K^1$ — случай, когда у главного члена $G$
есть невырожденный отрицательный минимум.

### 10.2. Что остаётся вне $\mathcal K$

1. **$G$ постоянен и отрицателен на замкнутой компоненте $\Sigma_0$** (например, вращательно
   симметричные $U=Q_0^2-z^6+\dots$). [Эскиз] Берётся трубка вокруг **всего** конуса над $\Sigma_0$
   без угловых стенок: $\rho=s$, $Y=\Psi_s=\omega+\eta^*_sn$ (вес по углу $0$), $D$ задаётся
   условиями $\lvert e\rvert<E$, $\tilde F-G<\delta$, угол $\theta\in\Sigma_0$ любой. Тогда по (6.4), (6.5)
   $\lvert\nabla\rho-Y/h\rvert\le2\lvert\eta^*_s\rvert\to0$, $s\lvert(\partial_s^2\Psi)^\perp\rvert=O(s)$,
   $s\langle w,D_wY\rangle\ge w_T^2(1-o(1))-o(1)\lvert w\rvert^2$ (центробежный член), запас Эйлера
   $2c$ по $e$; угловой запас не нужен, так как угловых стенок нет. Лемма 2 [GT3] применима
   с $C_1=0$. Не выписаны (D1)–(D3) для кольцевой области (теорема 2 [GT3] сформулирована для
   $b$ в шаре $\mathbb R^{m'}$, здесь $\theta$ периодична). Впрочем, при вращательной симметрии
   задача сводится к плоскости $y=0$ (инвариантна, если $U$ чётна по $y$).
2. **Изолированный вырожденный минимум $G$**: $G-G(0)\sim a\theta^{2p}$, $p\ge2$. [Эскиз] В карте
   (8.1) условие $(V_1')$ нарушено ($Q\not\ge\lambda_0\lvert b\rvert^2$); нужен аналог $(V_0)$. Трубка:
   $\lvert\theta\rvert\lesssim\delta^{1/(2p)}$, $\lvert e\rvert\lesssim\sqrt\delta$. Перекрёстный член
   $\sim\kappa\lvert\theta\rvert\sqrt K\rho^{\beta/2}$ против запаса $\beta K+2p\kappa P$: по оценке типа п. 7 леммы 2′
   достаточно $\kappa\lesssim\delta^{1-1/p}$, то есть $\kappa$ надо выбирать **после** $\delta$. Кривизна
   карты даёт $C_1=O(\kappa)$ (п. 4–5 доказательства теоремы K2), так что члены $C_1R_b^2/\sqrt\delta$
   тоже малы при $\kappa=\kappa(\delta)$. Правдоподобно, что вариант теоремы 2′ «$(V_0)$ с
   $\kappa=\kappa(\delta)$» проходит; не выписано. Это частный случай R3 [GT3, §10].
3. **Каскад**: $G\ge0$ на $\Sigma_0$ с нулями, а отрицательные значения $F_{\rm fl}$ появляются в
   следующих порядках по $s$. [Гипотеза + план] По предложению K4 это двумерная задача на дне:
   около нуля $\theta_1$ функции $G$ кривые «угловых минимумов» $F_{\rm fl}(s,\cdot)$ — ряды Пюизё
   $\theta=\theta_v(s)=\theta_1+as^{\alpha}+\dots$ (как у Гарсии–Тала при $n=2$, но на плоском конусе).
   Карта из трёх масштабов: продольный $s$, угловой $\theta-\theta_v(s)=s^{\alpha'}b_\theta$ (вес
   $1+\alpha'$ по длине дуги, $>1$ — «овраг», не однородное направление, так что $\kappa$-трюк не
   нужен), нормальный $s^{c'}b_e$. При невырожденном угловом минимуме это карта теоремы 2 [GT3]
   (прямая в развёртке по углу, кривая по нормали: $C_1>0$, случай $(V_1)$). Нужно: (i) существование
   ветви Пюизё с $F_{\rm fl}<0$ и невырожденным поперечным минимумом — аналог факта 1 Гарсии–Тала
   (у них он, по [GT3, §7.1] и отзыву, неточен для струй-максимумов); (ii) при вырожденном угловом
   минимуме — $(V_0)$ в кривой карте (R3).
4. **Нарушение Морса–Ботта**: $D^2u_m|_{N_\omega}$ вырождена (например, $u_8=Q_0^4$, поперечный
   порядок 4). Тогда нормальный овраг вырожден: $F_0=G+\alpha e^4$, нормальный вес
   $c=(j-m+4)/4$; карта кривая ($C_1>0$), поэтому нужен $(V_0)$ в кривой карте — R3 [GT3].
   [Гипотеза] При постоянной кратности ($u_m=Q^{2r}\cdot(\text{положит.})$ с гладким $Q$) аналог
   леммы K1 есть, но критическая точка в слое уже не обязана быть аналитической по $s$ (ряды
   Пюизё), а поперечный минимум $\tilde F(0,\theta,\cdot)$ — степени $2r$; нужен $(V_0)$ в кривой карте.
5. **Особое $\Sigma$** (например, $u_4=x^2y^2$: две пересекающиеся большие окружности, или
   изолированные особые точки кривой нулей). Около особых точек Морс–Ботт нарушен по
   существу; нужны раздутия в особых точках $\Sigma$ (взвешенные, по многограннику Ньютона
   $u_m$ в точке $\Sigma$). Это открытая часть.
6. **$n\ge4$, $\dim\Sigma_0\ge2$.** Конус над поверхностью не развёртывается; угловое направление
   многомерно. Ожидаю, что работает «поворачивающаяся полярная» карта с угловыми координатами
   на $\Sigma_0$ (геодезические нормальные координаты в $\omega^*$) и $Y=\partial_s-\kappa\,s^{-1}\theta\cdot\partial_\theta$;
   кривизна $\Sigma_0$ даст члены $O(\kappa\lvert\theta\rvert^2)$. [Гипотеза]

## 11. Где работают аналитичность и изолированность

1. **В теоремах K0–K2 и теореме 2′** аналитичность используется только для формы (F): $U$ около
   конуса равен $s^j\tilde F(s^{1/2},\theta,e)$ с конечным $j$ и $\tilde F$, непрерывно продолжимой в
   $s=0$ (лемма K2). Для $U\in C^\infty$ лемма K2 верна (с конечной гладкостью $\tilde F$ вместо
   аналитичности; нужная гладкость $U$ порядка $C^{j+3}$ — [Эскиз], не выписано), если
   $R(s,\theta)$ имеет ненулевой конечный коэффициент Тейлора; так что сами теоремы — критерии по
   конечной струе $j^jU$ (замечание 3.3.2). Неравенство Эйлера и $G<0$ — «конечный тип»; для
   плоских потенциалов типа Пенлеве–Уинтнера ($j=\infty$) ничего не утверждается. Изолированность в
   теоремах K0–K2 не нужна.
2. **В следствии K0′** аналитичность и изолированность работают вместе, и это единственное место,
   где (A) выводится без дополнительных условий на струю: аналитическая $R_\omega$ либо $\equiv0$ (тогда
   кривая критических точек — изолированность исключает), либо имеет конечный порядок (тогда
   работает теорема K0 или $0$ — минимум). Для $C^\infty$ это ломается: $R_\omega$ может быть плоской
   ненулевой (например, $R_\omega(s)=-e^{-1/s}$), тогда нет ни конечного $j$, ни кривой критических
   точек. Именно здесь проходит граница с гладкими контрпримерами.
3. **В предложении K4** — то же: «функция дна» аналитична, поэтому двумерная задача на дне имеет
   конечный тип (ряды Пюизё), а изолированность $U$ равносильна отсутствию критических точек
   $F_{\rm fl}$.
4. Пример Уреньи (гладкий изолированный максимум без тотальной неустойчивости) с теоремами
   не конфликтует: утверждается лишь существование одной асимптотической траектории.

## 12. Пробелы

1. Шаги 1–3 доказательства теоремы 2′ ссылаются на дословный текст теоремы 2 [GT3]; R21 проверил,
   что $(\Phi1)$ там не используется (кроме $h$ и $\theta_1$, заменённых на $(\Phi1')$, $(\Phi2')$).
   Пробела нет, но оформленный текст `results/008-class-K.md` ещё не читал рецензент.
2. Касание траекторией луча $\omega^*$ не доказано (как и в [GT3]): только конус раствора
   $O(\sqrt\delta)$ и касание конуса $Z$.
3. Новизна следствия K0′ и теоремы K2 по литературе не проверена: первоисточники MN89, MMN91, KP82,
   Taliaferro 1990, AG17 (Prop. 8, (H3)), FGT08, BGZ96 не открывались; литературный агент искал по
   конспектам. Не проверено и то, не покрываются ли примеры §9.7 теоремой 6 Паламодова 2020
   (квазиоднородная главная часть без критических точек вне нуля) после аналитической замены
   координат, выпрямляющей дно (формулировка теоремы 6 есть только по конспекту, допустимость замен
   координат там не ясна). Для $U_{(8)}$ надо учитывать, что $\mu=\infty$ (изолированность только
   над $\mathbb R$).
4. §10.2 — [Эскиз]/[Гипотеза]: вырожденный минимум $G$, каскад, не-Морс–Ботт, особое $\Sigma$, $n\ge4$.
   Принадлежность классу $\mathcal K$ примеров полигона с $H_{\rm plane}<0$ (A1, A2, A5, A7, C2;
   `experiments/numerics/2026-10-21-valleys/README.md`) мной не проверялась; для тех из них, что в
   $\mathcal K^1$, теорема K2 даёт асимптотическую траекторию, а теорема K1 (и прямое применение
   теоремы 2 [GT3]) — нет.
5. Замечание 8.4 ($n\ge4$, $\dim\Sigma_0=1$) и замечание 7.1 (ослабление (7.2)) — [Эскиз].
6. «Общий механизм» нарушения радиального условия Четаева в §9.7 — [Эскиз]; для двух примеров
   нарушение доказано явными семействами (по отзыву R22).

## 13. Статус

- Леммы K1–K3, теорема K0, следствие K0′, теорема K1, предложение K4 (в исправленной формулировке
  (c)), следствие K4′, лемма 2′, теорема 2′, теорема K2: **[Доказано]**; доказательства прочитаны
  рецензентами R20 (§2–§5, §10.1), R21 (§7), R22 (§6, §8, §9.6–9.7), ошибок не найдено, кроме
  формулировки критерия минимума в K4(c) (исправлена). Оформление — `results/008-class-K.md`
  (ждёт проверки рецензентом как текст).
- Примеры §9.6–9.7: принадлежность классам, $j$, $G$, изолированность над $\mathbb R$ (и
  неизолированность $U_{(8)}$ над $\mathbb C$), нарушение радиального условия Четаева —
  **[Доказано]** (выкладки вручную, проверены R22); числа таблицы §9 — точная арифметика sympy;
  строгий выход и стрельба §9.8, числа Милнора — [Эксперимент].
- §10.2 — [Эскиз] / [Гипотеза]. Задача (A) при $n=3$ этим **не решена**: доказан класс
  $\mathcal K$ (и полностью — случай конечного $\Sigma$ Морса–Ботта при любом $n$).
