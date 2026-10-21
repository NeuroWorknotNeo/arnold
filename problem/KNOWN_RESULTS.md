# Что известно: обзор литературы

> **Версия от 21.10.2026** (ревизия главного агента). Сверяли агенты `literature` L1–L4 по заданию
> главного агента; конспекты — `notes/literature/2026-10-21-*.md`; список изменений относительно версии
> 27.09.2026 и спорные места — [`notes/literature/2026-10-21-KNOWN_RESULTS-changes.md`](../notes/literature/2026-10-21-KNOWN_RESULTS-changes.md);
> реестр проверок — [`orchestrator/AUDIT.md`](../orchestrator/AUDIT.md).
>
> **Не открывалось** (Math-Net.Ru недоступен с сервера, остальное платное или закрыто): Паламодов 1977,
> 1995, 2020; Козлов 1981 и ДАН 1982; Taliaferro 1980; Laloy 1976, 1979; Laloy–Peiffer; Moauro–Negrini;
> Ureña; Козлов–Трещёв; журнальная версия Burgos 2025; книга «Задачи Арнольда» (русский текст и
> комментарий с. 250–253). Прежние пометки [Т] участника `vlad-claude` (27.09.2026) о Паламодове 1977 и
> 2020 в этой ревизии не воспроизведены.
>
> **Главное.**
> 1. Паламодов объявил теорему о «полной неустойчивости» в 1995 г. [[P95]](#P95); из неё следует (A).
>    Оценки в литературе расходятся: Негрини (1995) и BMP21 (arXiv v3) принимали её, Burgos 2021, BP22,
>    Allaire–Rauch считают доказательство неполным; в обзоре 2020 г. это «Гипотеза 1» (по прежней
>    пометке, не сверено). [В]
> 2. Препринт Burgos [[B21]](#B21) с «доказательством» гипотезы **отозван** (v5, 16.07.2022). Комментарий
>    автора: «There is a mistake in the proof. The second term of the last equation in Lemma 2.2 does not
>    have the desired asymptotic behavior. I am grateful with V. P. Palamodov for pointing out this
>    mistake». [Т]
> 3. **Случай (A) при $n\ge3$ открыт** по доступным данным. Burgos 2025: «Even this simplified version of
>    the Lagrange-Dirichlet converse remains open» [Т]; Enciso–Peralta-Salas (arXiv:2610.27893,
>    20.10.2026): для аналитических потенциалов в $\mathbb R^3$ «remains open» [Т]. Поиск неполный.

**Легенда.** [Т] — по полному тексту (для препринта — препринта, не журнала); [А] — по аннотации;
[Р] — по рецензии zbMATH/MR; [В: X] — по вторичному источнику X, чей текст прочитан; «не сверено» —
ни первоисточник, ни вторичные источники не подтверждают. Метка стоит в конце пункта. Выходные данные
сверены по Crossref и zbMATH (это не сверка текста). [Доказано]/[Гипотеза] — как в CLAUDE.md.
Обозначение: «функция сил» старой литературы $=-$ потенциальная энергия; ниже всё в потенциальной
энергии $U$. [Neg95] — обзор Негрини 1995 (открытый PDF, прочитан).

## 1. Формулировка задачи

- Текст задачи 1971-4 (дословно, одинаково в BMP21, BP22, B21): «Prove the instability of the equilibrium 0
  of the analytic system $\ddot x=-\partial U/\partial x$ in the case where the isolated critical point 0 of
  the potential U is not a minimum.» Источник — [[Arn04]](#Arn04) (Springer 2004; в BMP21 датирована 2002);
  русское издание — «Задачи Арнольда», ФАЗИС, 2000. [В: BMP21, BP22, B21]; книга не открывалась.
- Комментарий в книге (с. 250–253, несколько авторов), по BMP21: «The problem on the converse of the
  Lagrange-Dirichlet theorem makes therefore sense only under one or another additional assumptions (e.g.,
  that of analyticity of the potential).» Авторы комментария и перечень упомянутых результатов не
  установлены; русский текст не сверен. [В: BMP21]
- Rauch (2013–14): Арнольд поставил задачу в докладе 1976 г. (Proc. Symp. Pure Math.) в виде «$V\in C^\omega$,
  равновесие не локальный минимум ⇒ неустойчиво», без слова «isolated»; «easy when d=1», $d=2$ —
  Taliaferro 1980. Текст 1976 г. не сверен. [Т: Rauch]
- Вопрос Ляпунова (диссертация 1892, §25): «…will the position of equilibrium be unstable if the
  force-function is not maximum?» [В: B21, BP22]; об аналитичности в цитате ничего. Allaire–Rauch §1.7
  приписывают Ляпунову гипотезу для вещественно-аналитических $V$. [В: AR17]; у самого Ляпунова — не сверено.
- В PROBLEM.md «неустойчивость по Ляпунову» — перефразировка (в книге просто «instability»; смысл взят из
  комментариев Burgos). [Гипотеза]

## 2. Классические результаты: неустойчивость при отсутствии минимума

| Работа | Утверждение | Метка |
|---|---|---|
| Лагранж (1788), Дирихле (1846) [[Dir46]](#Dir46) | Строгий локальный минимум $U$ ⇒ устойчивость (достаточно $C^1$ по Taliaferro 1990; Негрини: $C^2$). | [В: BP22, Neg95] |
| Ляпунов (1892; 1897) [[Lia97]](#Lia97) | Если отсутствие минимума видно по гессиану ($U_2$ принимает отрицательные значения), равновесие неустойчиво. (Фраза прежней версии про «максимум по младшей форме $U_m$» не найдена ни в одном источнике, удалена.) | [В: Garcia–Tal, Rauch] |
| Четаев [[Che52]](#Che52) | Однородный потенциал степени $k\ge3$ без минимума в нуле ⇒ неустойчивость; изолированность не нужна. Общий критерий: $\langle\nabla\Pi(q),q\rangle<0$ на связной компоненте $\Pi^{-1}(-\infty,0)$, примыкающей к нулю. | [В: Neg95 Thm 1.2, Alva–Garcia] |
| Hagedorn (1971) [[Hag71]](#Hag71) | Неустойчивость **строгого локального максимума** потенциала для $C^2$-лагранжиана (методы Якоби–Мопертюи, Каратеодори); по BP22 — при любой гладкой кинетике. Критерий «$U_m$ принимает отрицательные значения» Hagedorn не доказывает (так было в прежней версии). | [В: Neg95 Thm 3.1, BP22] |
| Taliaferro (1980) [[Tal80a]](#Tal80a) | Неустойчивость максимумов потенциала ($C^1$). | [В: BP22, Neg95] |
| Taliaferro (1980) [[Tal80b]](#Tal80b) | **Неустойчивость** (не устойчивость, вопреки названию): $n=2$, $U$ аналитична, ньютоновская кинетика, не локальный минимум. Neg95 Thm 2.1 [функция сил]: «…critical point for U, which is not a maximum; then it is an unstable equilibrium». Точные условия (изолированность, асимптотика) не установлены. | [В: BP22, Neg95, Rauch] |
| Taliaferro (1990) [[Tal90]](#Tal90) | $T,U\in C^2$, $U^{(i)}=U_p^{(i)}+O(\|x\|^{p+\varepsilon-i})$ ($i=0,1,2$; $p>0$, $0<\varepsilon\le1$), $U_p$ положительно однородна степени $p$, $C^3$ вне нуля. Если $U_p<0$ где-то, есть решение $x(t)\to0$ при $t\to0^+$ ($p<2$) или $t\to-\infty$ ($p\ge2$) ⇒ неустойчивость. Аналитичности нет, $n$ любое. | [Р: zbMATH 4114130] |
| Козлов (1981) [[Koz81]](#Koz81) | $n=2$, $U$ аналитична, не минимум ⇒ неустойчивость; обобщение Паламодова/Taliaferro (ньютоновская кинетика) на произвольную. | [В: BP22]; не сверено |
| Козлов (1982, 1986) [[Koz82]](#Koz82), [[Koz86]](#Koz86) | [Koz86]: теорема существования асимптотических траекторий, если ряд $V_2+V_m+V_{m+1}+\dots$ и $V_2+V_m$ не имеет локального минимума ⇒ неустойчивость по Ляпунову. Версия Neg95 Thm 4.1: $L\in C^\infty$ натуральный, $U_{[2]}$ — форма с $U_{[2]}\ge0$ (потенциал), $U_{[k]}$ однородна, её ограничение на $\ker U_{[2]}$ не имеет минимума, остаток $o(|q|^k)$ ⇒ асимптотическое движение. Две формулировки не равнозначны дословно. [Koz82]: случай $V_2\equiv0$. Rauch Thm 4.1: $V\in C^\infty$, $V\sim V_m+\dots$, $V_m\not\equiv0$ без локального минимума ⇒ неустойчивость. | [Р: zbMATH 4026883]; [В: Neg95, Rauch] |
| Laloy (1979) [[Lal79]](#Lal79) (= «[NLM79]» прежней версии) | Статья об инверсии при аналитическом потенциале; аннотации нет, содержание не известно. Пример «$V_2+V_m$…» принадлежит Козлову 1986, не ей. | не сверено |
| Козлов–Паламодов (1982) [[KP82]](#KP82) | Аналитическая натуральная система, ведущая форма $U_{[k]}$, $k\ge3$, без минимума ⇒ неустойчивость и асимптотические движения (формулировка Neg95 Thm 2.2). | [В: Neg95] |
| Hagedorn, Mawhin (1992) [[HM92]](#HM92) | Обращение для (нестрогих) максимумов, $C^1$; вариационный метод (коэрцитивный функционал в гильбертовом пространстве). | [Р: zbMATH]; [В: Neg95 Thm 3.3] |
| Moauro–Negrini (1989) [[MN89]](#MN89); Maffei–Moauro–Negrini (1991) [[MMN91]](#MMN91) (прежнее «[AMM93]») | Неустойчивость, если $\pi=\|(q_1..q_r)\|^2+\pi_s(q_{r+1}..q_n)+R$, $\pi_s$ — однородный многочлен степени $s$ без минимума, $R=o(\|q\|^s)$. Neg95 Thm 4.4: $L\in C^h$, $h>k>2$, $U=U_{[k]}+W$, $W=o(|q|^k)$ ⇒ асимптотическое движение (соответствие Thm 4.4 ↔ [MN89] — интерпретация L1, [Гипотеза]). Условие «$C^h$, $h>3$» прежней версии не подтверждено. Peiffer 1991 [[Pei91]](#Pei91) и Sofer 1983 [[Sof83]](#Sof83) — другие работы, ошибочно слитые с «[AMM93]». | [В: Alva–Garcia, Neg95] |
| Garcia, Tal (2003) [[GT03]](#GT03) | $n=2$, потенциал и кинетика $C^2$, $\pi=P+R$ ($P$ — $k$-джет, $R=o(|q|^k)$); если джет показывает отсутствие минимума ⇒ асимптотическая траектория, неустойчивость. Для аналитических $U$ такой $k$ существует [[BGZ96]](#BGZ96). | [В: препринт 2001] |
| Alva Morales, Garcia (2017) [[AG17]](#AG17) | $\Pi\in C^2$, $T=\frac12\langle B(q)p,p\rangle$, $n$ любое. Класс $\mathcal H$: (H1) $j^\ell\Pi\ge0$ при $\ell<s$; (H2) $j^s\Pi$ показывает отсутствие минимума; (H3) есть компонента $A^*$ множества $(j^s\Pi)^{-1}(-\infty,0)$ с $(A^*\setminus0)\cap B_\varepsilon\subset\{\langle\nabla j^s\Pi(q),q\rangle<0\}^\circ$. Тогда строгое условие Четаева, асимптотическая траектория, неустойчивость. **Покрывает** $x^4+y^4-z^6$ при $s=6$ ($j^\ell\ge0$ при $\ell\le5$; на $\{U<0\}$: $\langle\nabla U,q\rangle=4(x^4+y^4)-6z^6<-2z^6<0$) — прежняя запись «не покрывает» была неверна (L8, 21.10.2026). Условие (H1) отбросить нельзя (пример 1 статьи). | [Т: arXiv v2] |
| Rauch (2013–14) [[Rau14]](#Rau14) | Теорема 1.2: $V\in C^\infty$ неконстантно, $P(x,\partial)V=0$, $P$ эллиптичен ($C^\infty$-коэффициенты) ⇒ равновесие неустойчиво; доказательство через Козлова (Thm 4.1), Паламодов не используется. | [Т] |
| Максимумы | Hagedorn 1971, Taliaferro 1980, Sofer 1983, Barone-Netto–Zampieri 1994 [[BNZ94]](#BNZ94): неустойчивость (нестрогих) максимумов при гладких $U,T$. | [В: BP22, zbMATH, AG17] |
| Freire, Garcia, Tal (2008) [[FGT08]](#FGT08) | Теорема A: $L=T-\pi\in C^{k+\lfloor(k-3)/2\rfloor+3}$, $T$ — положительно определённая квадратичная форма скоростей (зависит от $q$), $j^2\pi(0)\succeq0$ ранга $\ge n-2$, $k$-струя $\pi$ показывает отсутствие минимума ⇒ есть траектория, стремящаяся к равновесию при $t\to-\infty$. При $n=3$ закрывает случаи гессиана ранга 1 и 2. | [Т: техотчёт IME-USP RT-MAP-0801 (2008); журнальная версия не сверена] |

Общее свойство работ: критерий использует отсутствие минимума у джета или младшей формы (BP22: пример
$x^4+y^4-z^6$ — изолированная критическая точка, не минимум, но минимум первой струи, «none of the mentioned
results apply»). [В: BP22] При $n\ge3$ трудны ситуации, где отрицательные значения $U$ идут вдоль искривлённых
направлений, невидимых для младших форм. [Гипотеза: прежняя версия]

**Случай $n=2$, аналитический $U$.** BP22 §1: «V. P. Palamodov in [Pa2] and S. D. Taliaferro in [Ta] showed
independently the instability of a non local minimum critical point of a real analytic potential in dimension two
for a Newtonian kinetic term. Based on the previous Palamodov's work, this result was generalized by V. V. Kozlov
in [Ko] for an arbitrary kinetic term. The remaining case of a non strict local minimum was treated in [LP] by
M. Laloy and K. Peiffer … This completes the proof of the analytic Lagrange-Dirichlet converse in dimension two.»
[Т: BP22, B25 §1.2]. Состав: Паламодов 1977 и Taliaferro 1980 (ньютоновская кинетика), Козлов 1981
(произвольная), Laloy–Peiffer 1982 (нестрогий минимум), Garcia–Tal 2003 ($C^2$ + джет), Brunella 1998 (другое
доказательство (A), §4). Оригиналы Паламодова 1977, Taliaferro 1980, Козлова 1981, Laloy–Peiffer не сверены.

## 3. Контрпримеры в гладком классе

| Работа | Пример | Метка |
|---|---|---|
| Painlevé (1904) [[Pai04]](#Pai04), Wintner (1941) [[Win41]](#Win41) | $n=1$, $U=e^{-1/x^2}\cos(1/x)$, $U(0)=0$ (версия Wintner; оригинал Painlevé — C. R. 138 (1904), 1555–1557; в BMP21 и у Rauch — $e^{-1/|x|}\sin(1/|x|)$). 0 — критическая точка, не минимум; на любой окрестности есть интервал с центром в 0, на границе которого $U>0$ строго и максимально, поэтому движения малой энергии заперты, равновесие **устойчиво по Ляпунову**. Критические точки накапливаются к 0 (нули $U$ сходятся к 0, между ними по теореме Ролля нули $U'$): 0 **не изолирована**. | [В: BP22]; накопление — [Доказано: L2, независимо не проверено] |
| Laloy (1976) [[Lal76]](#Lal76) | $n=2$, $U=e^{-x^{-2}}\cos(x^{-1})-e^{-y^{-2}}(\cos(y^{-1})+y^2)$ (гладкое продолжение на оси): $U^{-1}((-\infty,0])$ содержит диагонали $x=\pm y$, движения по координатам разделены и заперты, 0 устойчиво. В BMP21 другая формула ($\exp(-|x|^{-1})\sin(|x|^{-1})-\exp(-|y|^{-1})\sin(|y|^{-1})-y^2$); какая у Laloy — неизвестно. 0 **не изолированная** критическая точка (критические точки $(x_k,y_j)\to0$ по теореме Ролля), пример (A) не опровергает. | [В: BP22, zbMATH]; неизолированность — [Доказано: L2, независимо не проверено] |
| Ureña (2020) [[Ure20]](#Ure20) | Теорема 1.1 (по BP22): «There exists a $C^\infty$ function $U:\mathbb R^2\to\mathbb R$ satisfying: (1) $U(0)=\max_{\mathbb R^2}U$. (2) $\nabla U(q)\ne0$ for any $q\ne0$. (3) There exists a sequence $T_n>0$ … of nontrivial periodic solutions of $\ddot q=-\nabla U(q)$ such that $\max_t(\|q_n(t)\|+\|\dot q_n(t)\|)\to0$.» Глобальный максимум, изолированный критический, ньютоновская кинетика; $T_n\to\infty$, орбиты не охватывают 0. Значит, максимум не неустойчив в смысле Зигеля–Мозера (максимальное инвариантное множество в окрестности), хотя по Ляпунову неустойчив (Hagedorn, Taliaferro). В $C^\infty$ тотальная неустойчивость неверна; в аналитическом классе такой пример исключила бы гипотеза Паламодова (BP22). На arXiv версии нет. | [В: BP22 дословно]; [Р: zbMATH 1453.37055] |
| Bertotti–Bolotin (2000) [[BB00]](#BB00); Garcia–Tal (2005) [[GT05]](#GT05) | $n=2$, $C^\infty$: есть гладкие $U$ и две гладкие кинетики $Q,\tilde Q$, при которых 0 устойчиво для $Q-U$ и неустойчиво для $\tilde Q-U$ (явный пример — GT05). В аналитическом классе от кинетики не зависит (BP22). | [В: BP22] |

Гладкий пример **изолированной** критической точки без минимума с устойчивым равновесием **не известен**;
в литературе (zbMATH, arXiv, BMP21, BP21, BP22, Rauch, Alva–Garcia) не найдено ни примера, ни утверждения о
его несуществовании, и как открытая проблема вопрос не поставлен (пробел литературы, не ответ «нет»). [Т: L2]
При $n=1$ (A) верна даже для $C^1$: если 0 — изолированный нуль $U'$ и не минимум, $U'$ знакопостоянна на
каждой из полуокрестностей, и частица с нулевой скоростью на стороне $U<U(0)$ уходит. [Доказано: L2, ГА проверил]

## 4. Нестрогие минимумы (соседняя часть задачи; к (A) не относится)

Если 0 — изолированная критическая точка и не строгий минимум, то она не нестрогий минимум: иначе точки с
$U=U(0)$ были бы точками минимума, значит, критическими, и 0 не была бы изолированной. [Доказано: L2] Нестрогие
минимумы нужны для полной гипотезы Ляпунова.

| Работа | Утверждение | Метка |
|---|---|---|
| Laloy, Peiffer (1982) [[LP82]](#LP82) | $n=2$, $U$ аналитична, нестрогий локальный минимум ⇒ неустойчивость по Ляпунову. Условия «вдоль кривой», «при подходящей гладкости» (прежняя версия) не подтверждены, удалены. | [В: BP22, BMP21]; не сверено |
| Burgos, Maderna, Paternain (2021) [[BMP21]](#BMP21) | Ньютоновская динамика в $\mathbb R^n$. Гипотеза: «$U=g\circ f$, zero is a regular value of $f$ in $C^3(\mathbb R^n,\mathbb R)$, $g\in C^2(\mathbb R,\mathbb R)$, $g\ge0$ vanishing only at zero»; тогда $M=\{f=0\}$ — гиперповерхность, и «Every point in $M\times\{0\}$ is Lyapunov unstable.» Аналитичность не нужна (она нужна лишь для сравнения с критериями по джету, напр. $U=(x^2+2y^2+3z^2-1)^4$). | [Т: arXiv v3] |
| Burgos, Paternain (2021) [[BP21]](#BP21) | Теорема 1.1: если у нуля потенциала $p$ есть окрестность и $C^3$-функция $f$ регулярная, с $dU(\nabla_\rho f)=O(U)$, то $(p,0)$ неустойчива по Ляпунову для лагранжиана $Q-U$ ($Q$ — положительно определённая $C^2$-форма, $U\ge0$ класса $C^2$). Следствие 2: квазиоднородный $U\ge0$. Критерий достаточен, не необходим ($U=x^2y^2$); с магнитным полем обращение Routh неверно (при $U=z^2$, $\mu=x\,dy$ плоскость $z=0$ устойчива). Для неизолированных нулей. | [Т: arXiv v3] |
| Burgos, Paternain (2022) [[BP22]](#BP22) | **Препринт.** Теорема 1.1: «Consider a mechanical system on a three dimensional real analytic manifold with a real analytic potential. Then, there is an open and dense subset of the set of non strict local minimums of the potential such that every one of its points is a Lyapunov unstable equilibrium point.» Любая гладкая кинетика; критерий: локально липшицево слабо логарифмическое поле, ненулевое в точке (Thm 3.1). Не решает (A). «We do not know whether there is a stable non strict local minimum point of a real analytic potential.» | [Т: arXiv v1] |
| Brunella (1998) [[Bru98]](#Bru98) | Аналитическое векторное поле $v$ на окрестности $0\in\mathbb R^n$ с изолированной особой точкой 0; $M$ — аналитическое неприводимое трёхмерное $v$-инвариантное подмногообразие, гладкое вне 0, с линком (компактная связная поверхность) ненулевой эйлеровой характеристики ⇒ есть $p\in M\setminus0$, $T\in\{\pm\infty\}$ с $\gamma_p(t)\to0$ при $t\to T$; в частности, 0 неустойчива. При $n=3$ можно взять $M=U$. Следствие: $F$ аналитична в окрестности $0\in\mathbb R^2$, 0 — изолированная критическая точка, не минимум и не максимум ⇒ есть решение $\ddot q=-\mathrm{grad}F$, стремящееся к $(0,0)$ при $t\to+\infty$ (и другое при $t\to-\infty$). Для (A) даёт только $n=2$ ($H=\frac12|p|^2+F$ в $\mathbb R^4$, нужна неприводимая компонента нулевого уровня с $\chi\ne0$); максимум исключён (линк — тор), он элементарен (Мопертюи, Хопф–Ринов). Брунелла называет следствие уточнением частного случая теоремы Паламодова [P77]. | [Т: введение и формулировки; доказательство не вычитывалось] |

## 5. Полная неустойчивость: гипотеза Паламодова и заявленное доказательство

- **Определения.** (i) T(E)-форма (теорема 2.1 [P95] в цитате Burgos 2021): у каждой точки $x_0$ есть окрестность $W$ и
  положительная функция $T$ на $(-\infty,U(x_0))$ такие, что любое движение с энергией $E<U(x_0)$, начавшееся в $W$,
  проводит в $W$ время не больше $T(E)$ ($M$ — вещественно-аналитическое многообразие, метрика гладкая, $U$ аналитична).
  [В: B21 v4] Определение 1 в [P20] (раздел 3, по B21 v4) «сгущает» эту формулировку; дословно не сверено.
  (ii) Burgos 2025 (§1.1): «A point p is totally unstable if there is a neighbourhood B ⊂ A of the point such that
  for any subcritical point z in TB, the positive orbit I+(z) is not contained in TB.» Без равномерной оценки $T(E)$;
  вообще говоря, слабее (i). [Т: arXiv v1]
- **Отсюда следует (A).** Пусть 0 не минимум; берём $x$ сколь угодно близко к 0 с $U(x)<U(0)$ и нулевую скорость:
  энергия $E<U(0)$, и по любому из определений движение покидает окрестность. Изолированность не нужна; нестрогие
  минимумы не охватываются. [Доказано: элементарно, ГА 21.10.2026] У Burgos 2021 это Corollary 2.2 [P95]: если $x_0$
  лежит в замыкании $\{U<U(x_0)\}$, то равновесие неустойчиво. [В: B21, BMP21]
- **Паламодов (1977)** [[P77]](#P77): $n=2$, $U$ аналитична, не минимум ⇒ неустойчивость. [В: BP22, B21, EPS26]
  Форма леммы по Neg95 (потенциал вместо силовой функции — знаки меняются): на компоненте $U_\rho^+$ с замыканием, содержащим 0, есть
  непрерывное поле $u$, $C^1$ вне конечного числа $C^\infty$-кривых, с $\langle u,\partial U/\partial q\rangle\ge0$ и
  $(\partial u_i/\partial q_j)w_iw_j\ge C|w|^2$; для аналитической $U$ в плоской области при малом $\rho$ в $U_\rho^+$ нет критических
  точек (здесь работает аналитичность). [В: Neg95] Прежняя запись «или $C^\infty$ с конечнократной критической точкой» не
  подтверждена и не опровергнута (Neg95 Cor. 2.4 относится к теореме Паламодова 1992 в любой размерности). Утверждение «в [P20] это называется
  тотальной неустойчивостью при $n=2$» не сверено. Общая теорема о тотальной неустойчивости и Cor. 2.2 приписаны у Burgos 1995 г., для $n=2$ — 1977.
  Страницы англ. версии 277–289 (Crossref) или 277–288 (страница Паламодова), год 1977 или 1978. Не сверено.
- **Паламодов (1992 препринт; 1995)** [[P92]](#P92), [[P95]](#P95): статья вышла в сб. под ред. Козлова, не открывалась. Результат объявлен,
  полного доказательства не опубликовано (Allaire–Rauch §1.7: «A detailed proof has never been published»; Burgos 2021: «…it is not a
  complete argument. It is believed that the argument can be completed [Pa2] but technically speaking, it does not constitute a proof
  leaving the announced Theorem so far as a conjecture», [Pa2] — личное сообщение Паламодова). Пробел публикациями не локализован. [В: AR17, B21, L3]
  **Расхождение оценок:** Neg95 Thm 2.3 (по препринту 1992, любая размерность, натуральная аналитическая система): «Let U(0)=0 be not a
  maximum. Then there exists a neighborhood $V_0$ such that any motion starting in $V_0$ with arbitrarily small positive energy E leaves $V_0$
  in a finite time τ(E)» — принято как теорема [В]; рецензия zbMATH 826088: «…inversion … for any critical point where the analytic potential
  function does not have a minimum» [Р]; BMP21 (arXiv v3): «Palamodov completely solves the Arnold's problem», остаётся лишь нестрогий минимум
  [Т: v3; в журнальной версии не проверено]; BP22 и B21: «total instability result … whose proof is incomplete … All of these remain as open problems»
  [Т]. В списке литературы [P20] статьи 1995 нет [В: rcsi.science, B21].
- **Паламодов (2020)** [[P20]](#P20), обзор (аннотация: «Problems related to instability of equilibria … and inversions of the Lagrange–Dirichlet
  theorem are discussed»; 42 названия). [А] Содержание по прежней записи участника, **в этой ревизии не сверено**: Определение 1 и Гипотеза 1
  (всякая точка равновесия аналитического потенциала тотально неустойчива); Теорема 2 (из [P77]): если на $X=\{U<U(x_0)\}\cup\{x_0\}$ есть
  $C^1$-поле $A$, (I) форма $\langle\xi,\nabla_\xi A\rangle$ в $x_0$ неотрицательна, (II) $\inf_XA(U)/U>0$, то $x_0$ тотально неустойчива (рост
  $F=\langle\dot x,A\rangle$); Теорема 3: $U=u_m+\dots$, $\nabla u_m\ne0$ при $x\ne0$ ⇒ тотальная неустойчивость; Теорема 5: то же для ограничения на
  ядро квадратичной части; Теорема 6: квазиоднородная главная часть без критических точек вне 0, остаток $O(|x||x|_w)$; Пример 3 — поле подобрано вручную.
  Вторично согласуется с Теоремой 3 (Burgos 2025: для аналитического потенциала, первая ненулевая струя которого не имеет критических точек, кроме нуля; у
  Burgos аналитичность указана, в прежней записи — нет). [В: B25] Замечание об аналитических системах общего вида без асимптотического движения — Козлов–Трещёв
  [[KT18]](#KT18): по аннотации и слайдам, для нечётных $n\ge3$ есть бездивергентные полиномиальные системы с изолированным неустойчивым равновесием без
  уходящих асимптотических траекторий. [А]; в [P20] не сверено.
- **Allaire–Rauch.** AR17 (§1.7) отмечают: из гипотезы Паламодова (набросок [P95]) следовали бы их теоремы об электростатике и неустойчивость заряженных
  твёрдых тел; полного доказательства нет. [В: AR17] (Прежняя фраза «пользуются результатами» неточна: AR17 вышла до [P20].) Rauch использует Козлова, не Паламодова.
- **Burgos (2021), отозвано** [[B21]](#B21): «первое подробное доказательство гипотезы Паламодова»; v1 12.08.2021, v2 17.08.2021, v3 03.09.2021, v4 11.09.2021,
  v5 16.07.2022 (withdrawn); комментарий — в шапке. Лемма 2.2 (v4): «There is a neighborhood W of x0 in M, a smooth vector field V and a smooth real valued
  function P both defined on W−V(U) such that P≥1, V(U)=PU and ⟨v,∇_vV⟩=(1+o(1))‖v‖² … as the point x approaches to x0.» Схема: мономиализация Хиронаки идеала
  $\mathfrak m_{x_0}\cdot I_U$ (Лемма 2.1, Spivakovsky), в картах поля Эйлера $\sum w_i\partial_{w_i}$, склейка разбиением единицы, затем рост $F=\langle\dot\gamma,V(\gamma)\rangle$.
  Лемма 2.2 — единственный технический шаг. Отождествление «второго слагаемого» с членом склейки $v(f_p)\langle v,V_p\rangle$ — интерпретация доски, не слова автора. [Т: v4]
  Разбор ошибки участником `vlad-claude` (`notes/vlad-claude/burgos-review.md`) проверен рецензентом
  (`notes/reviewer/2026-10-21-burgos-review.md`, 21.10.2026): пример с седлом $U=x(y-3x)$ (поле карты
  $x\partial_x+(2y-3x)\partial_y$, форма $v_1^2-3v_1v_2+2v_2^2$ знаконеопределена) верен, но опровергает **шаг
  доказательства** леммы 2.2 для поля одной карты, а не её формулировку; утверждение о члене склейки было оценкой
  порядка, рецензент построил явный пример ($U=xy$, две карты: склеивающий член не мал при $r\to0$).
- **Burgos (2025/2026)** [[B25]](#B25), электромагнитные лагранжевы системы $L=g(v,v)/2+\mu(v)-U$, всё вещественно-аналитическое; формулировки по arXiv v1, с журналом не сверены. [Т]
  Теорема 1.1: при слабом магнетизме ($d-l/2\ge1$, $l,d$ — степени первых ненулевых струй $U$ и $\mu$) на открытом плотном подмножестве идеала $I_k=\mathfrak m^k$ точка
  тотально неустойчива (метод — раздутие Макги). Prop. 1.2: «Suppose that f is a Morse function and zero is a regular value. Then, the point p is totally unstable» ($f$ —
  ограничение первой ненулевой струи $U$ на единичную сферу). Prop. 1.3 / Cor. 1.4 (негенерический, ньютоновский случай): $U$ не однородный многочлен, $U=U_{l_1}+U_{l_2}+\dots$;
  тотальная неустойчивость, если $U_{l_2}<0$ во всех критических точках $f$ с $f\le0$ (в общем виде — функция $C(q)>0$ из Prop. 1.3). Автор: в механическом случае Prop. 1.2
  слабее теоремы Паламодова, так как требует Морса; «so far all of the instability criteria … require the generic hypothesis that zero is a regular value of the function f»;
  негенерический критерий «bounds the field of possibilities in which to look for a counterexample». §1.2: «In dimension greater than two, the problem remains open and only
  partial results are known.» Доказательства доской не проверялись.
- **Новое (после 27.09.2026).** Enciso–Peralta-Salas [[EPS26]](#EPS26), arXiv:2610.27893 (20.10.2026): $\ddot x=\dot x\times B(x)$ в $\mathbb R^3$, без потенциала. Thm 1: $B\in C^1$, $B(0)\ne0$ ⇒
  $(0,0)$ неустойчива. Thm 2: $B$ аналитично, 0 — изолированный нуль ⇒ неустойчива (через Brunella). Thm 3: есть бездивергентное $C^\infty$-поле, плоское в изолированном нуле, с устойчивым равновесием.
  К (A) не относится; введение: для аналитических потенциалов в $\mathbb R^3$ «remains open». [Т] Работы 2023–2026 Козлова (соленоидальное поле, псевдориманово пространство, потенциал степени $-2$),
  Burgos (Nonlinearity 36 (2023)), Udwadia–Bulatovic (2026) к (A) не относятся. [А] Решения (A) или её частей ($n=3$, многочлены) ни в одной найденной работе нет; поиск неполный.

## 6. Что это значит для доски

1. Случай (A) при $n\ge3$ открыт (B25, BP22, EPS26). Это исследовательская задача, а не проверка чужого результата.
2. Входы: понять, почему не работает лемма 2.2 [B21] и что уцелело из подходов Burgos и Паламодова; искать своё доказательство методами §2 и §5, начиная с частных классов. Для $x^4+y^4-z^6$
   стоит проверить критерии Burgos 2025 (на сфере $f=x^4+y^4\ge0$ критические точки с $f>0$) — замечание L3, не литература.
3. Для **многочленов** есть явные средства. D'Acunto–Kurdyka [[DK05]](#DK05): для многочлена $f:\mathbb R^n\to\mathbb R$ степени $d\ge2$ с $f(0)=0$, $\nabla f(0)=0$ показатель Лоясевича в
   $|\nabla f|\ge C|f|^\varrho$ (в окрестности нуля) удовлетворяет «$\varrho_f\le1-1/(d(3d-3)^{n-1})$. More precisely $\varrho_f\le1-R(n,d)^{-1}$, where $R(n,d)=\max\{d(3d-4)^{n-1},2d(3d-3)^{n-2}\}$.»
   Окрестность зависит от $f$, константа $C$ не явная; изолированность не нужна. [Т] Уточнённая оценка не слабее формулы из аннотации [Доказано: сравнение выражений при $d\ge2$, не проверено независимо]. «Изолированность и
   неотрицательность многочлена проверяются алгоритмически» — не сверено; удобство полиномиального варианта для доказательства — [Гипотеза].
4. Отдельно открыты: неустойчивость нестрогих минимумов в аналитическом классе при $n\ge3$ (общий случай; BP22 — открытое плотное подмножество при $n=3$); гладкий контрпример для изолированной критической
   точки (§3).

## Библиография

Выходные данные по Crossref и zbMATH.

- <a id="Arn04"></a>[Arn04] V. I. Arnold (ed.), *Arnold's Problems*, Springer, 2004, doi:10.1007/b138219 (DOI не сверен). Рус.: *Задачи Арнольда*, М.: ФАЗИС, 2000.
- <a id="Dir46"></a>[Dir46] G. Lejeune Dirichlet, Über die Stabilität des Gleichgewichts, *J. Reine Angew. Math.* 32 (1846), 85–88.
- <a id="Lia97"></a>[Lia97] A. M. Liapounoff, Sur l'instabilité de l'équilibre dans certains cas où la fonction de forces n'est pas un maximum, *J. Math. Pures Appl.* (5) 3 (1897), 81–94. Диссертация 1892 (англ. *Ann. of Math. Studies* 17, 1947).
- <a id="Che52"></a>[Che52] Н. Г. Четаев, О неустойчивости равновесия в некоторых случаях, когда функция сил не есть максимум, *ПММ* 16:1 (1952), 89–93.
- <a id="Hag71"></a>[Hag71] P. Hagedorn, Die Umkehrung der Stabilitätssätze von Lagrange-Dirichlet und Routh, *Arch. Rational Mech. Anal.* 42:4 (1971), 281–316, doi:10.1007/BF00282334.
- <a id="Sof83"></a>[Sof83] M. Sofer, On the inversion of the Lagrange–Dirichlet stability theorem — mechanical and generalized systems, *ZAMP* 34:1 (1983), 1–12, doi:10.1007/BF00962611.
- <a id="Tal80a"></a>[Tal80a] S. D. Taliaferro, An inversion of the Lagrange-Dirichlet stability theorem, *Arch. Rational Mech. Anal.* 73:2 (1980), 183–190, doi:10.1007/BF00258236.
- <a id="Tal80b"></a>[Tal80b] S. D. Taliaferro, Stability for two dimensional analytic potentials, *J. Differential Equations* 35:2 (1980), 248–265, doi:10.1016/0022-0396(80)90042-X.
- <a id="Tal90"></a>[Tal90] S. D. Taliaferro, Instability of an equilibrium in a potential field, *Arch. Rational Mech. Anal.* 109:2 (1990), 183–194, doi:10.1007/BF00405242.
- <a id="Lal76"></a>[Lal76] M. Laloy, On equilibrium instability for conservative and partially dissipative systems, *Int. J. Non-Linear Mech.* 11 (1976), 295–301, doi:10.1016/0020-7462(76)90015-9.
- <a id="Lal79"></a>[Lal79] M. Laloy, On the inversion of the Lagrange–Dirichlet theorem in the case of an analytic potential, *Int. J. Non-Linear Mech.* 14:1 (1979), 59–65, doi:10.1016/0020-7462(79)90029-5.
- <a id="Koz81"></a>[Koz81] В. В. Козлов, Неустойчивость равновесия в потенциальном поле, *УМН* 36:1 (1981), 209–210; англ. *Russian Math. Surveys* 36:1 (1981), 238–239, doi:10.1070/RM1981v036n01ABEH002551. (Отдельная заметка *Russian Math. Surveys* 36:3 (1981), 256–257; русский номер УМН 36:3, 215–216 из прежней версии не проверен.)
- <a id="Koz82"></a>[Koz82] В. В. Козлов, Асимптотические решения уравнений классической механики, *ПММ* 46:4 (1982), 573–577; англ. *J. Appl. Math. Mech.* 46:4, 454–457, doi:10.1016/0021-8928(82)90029-6.
- <a id="KP82"></a>[KP82] В. В. Козлов, В. П. Паламодов, Об асимптотических решениях уравнений классической механики, *ДАН СССР* 263:2 (1982), 285–289; англ. *Soviet Math. Dokl.* 25 (1982), 335–339.
- <a id="Koz86"></a>[Koz86] V. V. Kozlov, Asymptotic motions and the inversion of the Lagrange-Dirichlet theorem, *J. Appl. Math. Mech.* 50:6 (1986), 719–725, doi:10.1016/0021-8928(86)90079-1; рус. *ПММ* 50:6 (1986), 928–937.
- <a id="LP82"></a>[LP82] M. Laloy, K. Peiffer, On the instability of equilibrium when the potential has a non-strict local minimum, *Arch. Rational Mech. Anal.* 78:3 (1982), 213–222, doi:10.1007/BF00280037.
- <a id="HM92"></a>[HM92] P. Hagedorn, J. Mawhin, A simple variational approach to a converse of the Lagrange-Dirichlet theorem, *Arch. Rational Mech. Anal.* 120:4 (1992), 327–335, doi:10.1007/BF00380318.
- <a id="MN89"></a>[MN89] V. Moauro, P. Negrini, On the inversion of Lagrange–Dirichlet theorem, *Differential Integral Equations* 2:4 (1989), 471–478, doi:10.57262/die/1371648438.
- <a id="MMN91"></a>[MMN91] C. Maffei, V. Moauro, P. Negrini, On the inversion of the Lagrange–Dirichlet theorem in a case of nonhomogeneous potential, *Differential Integral Equations* 4:4 (1991), 767–782, doi:10.57262/die/1371225014.
- <a id="Pei91"></a>[Pei91] K. Peiffer, On inversion of the Lagrange–Dirichlet theorem, *J. Appl. Math. Mech.* 55:4 (1991), 436–441, doi:10.1016/0021-8928(91)90002-C.
- Neg95: P. Negrini, *Resenhas IME-USP* 2:1 (1995), 83–114 (обзор инверсий; полное название не выписано).
- <a id="BGZ96"></a>[BGZ96] A. Barone Netto, G. Gorni, G. Zampieri, Local extrema of analytic functions, *NoDEA* 3:3 (1996), 287–303.
- <a id="BNZ94"></a>[BNZ94] Barone-Netto, Zampieri, *Proc. Amer. Math. Soc.* 121:3 (1994), 711–713.
- <a id="GT03"></a>[GT03] M. V. P. Garcia, F. A. Tal, Stability of equilibrium of conservative systems with two degrees of freedom, *J. Differential Equations* 194:2 (2003), 364–381, doi:10.1016/S0022-0396(03)00167-0.
- <a id="GT05"></a>[GT05] M. V. P. Garcia, F. A. Tal, The influence of the kinetic energy in equilibrium of Hamiltonian systems, *J. Differential Equations* 213 (2005), 410–417.
- <a id="FGT08"></a>[FGT08] M. P. Freire, M. V. P. Garcia, F. A. Tal, *J. Differential Equations* 245 (2008), 490–504; препринт RT-MAP-0801, IME-USP (2008).
- <a id="AG17"></a>[AG17] G. J. Alva Morales, M. V. P. Garcia, A partial reciprocal of Dirichlet–Lagrange theorem detected by jets, *Qual. Theory Dyn. Syst.* 16:2 (2017), 371–389, doi:10.1007/s12346-016-0196-x; arXiv:1508.07427.
- <a id="BB00"></a>[BB00] M. L. Bertotti, S. V. Bolotin, *Arch. Rational Mech. Anal.* 152:1 (2000), 65–79.
- <a id="Pai04"></a>[Pai04] P. Painlevé, Sur la stabilité de l'équilibre, *C. R. Acad. Sci. Paris* 138 (1904), 1555–1557.
- <a id="Win41"></a>[Win41] A. Wintner, *The Analytical Foundations of Celestial Mechanics*, Princeton Univ. Press, 1941.
- <a id="Ure20"></a>[Ure20] A. J. Ureña, To what extent are unstable the maxima of the potential?, *Ann. Mat. Pura Appl.* 199:5 (2020), 1763–1775, doi:10.1007/s10231-020-00941-2.
- <a id="Rau14"></a>[Rau14] J. Rauch, Earnshaw's theorem in electrostatics and a conditional converse to Dirichlet's theorem, *Sém. Laurent Schwartz, EDP et applications*, 2013–2014, exp. XII, doi:10.5802/slsedp.56.
- <a id="AR17"></a>[AR17] G. Allaire, J. Rauch, *Arch. Rational Mech. Anal.* 224 (2017), 233–268 (HAL hal-01321566; об электростатике и теореме Ирншоу).
- <a id="P77"></a>[P77] В. П. Паламодов, Об устойчивости равновесия в потенциальном поле, *Функц. анализ и его прил.* 11:4 (1977), 42–55; англ. *Funct. Anal. Appl.* 11:4, 277–289, doi:10.1007/BF01077142.
- <a id="P92"></a>[P92] V. P. Palamodov, On the instability of motion with several degrees of freedom, Preprint, Moscow, 1992 (по Neg95).
- <a id="P95"></a>[P95] V. P. Palamodov, Stability of motion and algebraic geometry, в сб.: V. V. Kozlov (ed.), *Dynamical Systems in Classical Mechanics*, *Amer. Math. Soc. Transl. (2)* 168 (1995), 5–20, doi:10.1090/trans2/168/02.
- <a id="P20"></a>[P20] В. П. Паламодов, Об обращении теоремы Лагранжа–Дирихле и неустойчивости консервативных систем, *УМН* 75:3 (2020), 107–122 (Math-Net.Ru: rm9945); англ. *Russian Math. Surveys* 75:3 (2020), 495–508, doi:10.1070/RM9945.
- <a id="KT18"></a>[KT18] V. V. Kozlov, D. V. Treschev, Instability, asymptotic trajectories and dimension of the phase space, *Mosc. Math. J.* 18:4 (2018), 681–692.
- <a id="BMP21"></a>[BMP21] J. M. Burgos, E. Maderna, M. Paternain, On the Lyapunov instability in Newtonian dynamics, *Nonlinearity* 34:10 (2021), 6719–6726, doi:10.1088/1361-6544/ac1a1a; arXiv:1906.11962.
- <a id="BP21"></a>[BP21] J. M. Burgos, M. Paternain, On the Lyapunov instability in Lagrangian dynamics, *Proc. Amer. Math. Soc.* 150:10 (2022), 4335–4348, doi:10.1090/proc/15972; arXiv:2108.05074.
- <a id="B21"></a>[B21] J. M. Burgos, A proof of the Palamodov's total instability conjecture, arXiv:2108.05829 (v1 12.08.2021 … v4 11.09.2021; v5 16.07.2022 — **отозвано автором**, ошибка в лемме 2.2).
- <a id="BP22"></a>[BP22] J. M. Burgos, M. Paternain, On the Lagrange-Dirichlet converse in dimension three, arXiv:2208.01139 (2022) — **препринт**, публикации не найдено.
- <a id="B25"></a>[B25] J. M. Burgos, McGehee blowup for Lagrangian systems and instability of equilibria, *J. Differential Equations* 454 (2026), 114005, doi:10.1016/j.jde.2025.114005; arXiv:2506.19135.
- <a id="Bru98"></a>[Bru98] M. Brunella, Instability of equilibria in dimension three, *Ann. Inst. Fourier* 48:5 (1998), 1345–1357, doi:10.5802/aif.1657.
- <a id="DK05"></a>[DK05] D. D'Acunto, K. Kurdyka, Explicit bounds for the Łojasiewicz exponent in the gradient inequality for polynomials, *Ann. Polon. Math.* 87 (2005), 51–61, doi:10.4064/ap87-0-5.
- <a id="EPS26"></a>[EPS26] A. Enciso, D. Peralta-Salas, Stability and instability for particle dynamics in magnetic fields, arXiv:2610.27893 (20.10.2026).
- Также: В. В. Козлов, С. Д. Фурта, *Асимптотики решений сильно нелинейных систем дифференциальных уравнений* (1996; англ. Springer 2013) — метод асимптотических траекторий (не сверено); Absil–Kurdyka, *Systems & Control Letters* 55:7 (2006), 573–577, doi:10.1016/j.sysconle.2006.01.002 (градиентный поток, не наша динамика; [А]).
