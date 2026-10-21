# Сверка §3–§4 KNOWN_RESULTS.md: гладкие контрпримеры, нестрогие минимумы, гладкие изолированные точки

Дата: 2026-10-21. Агент: literature. Файл `problem/KNOWN_RESULTS.md` не правился.

## Как читать степени сверки

- «Полный текст» — текст прочитан целиком или нужные места (arXiv, numdam).
- «Рецензия zbMATH» — прочитана рецензия или аннотация в zbMATH Open (через API `api.zbmath.org`).
- «Вторичный источник» — результат процитирован в статье, которую я читал (в основном BP22 = arXiv:2208.01139v1,
  Introduction, прочитан целиком).
- Платные тексты (Springer ARMA, Elsevier, AMS) не скачивались. ScienceDirect, Springer, digibug, AMS, projecteuclid,
  core.ac.uk закрыты для сервера (403 или Cloudflare). Обходить защиту я не стал.
- JDE 1980 (Taliaferro) и JDE 2003 (Garcia–Tal) по OpenAlex лежат в открытом доступе на ScienceDirect, но
  с сервера не открылись. Тексты может взять владелец (открытые, не теневые).

Важная сводка по надёжности: формулы контрпримеров и теорема Уреньи сверены по статье BP22 (полный текст)
и по независимым рецензиям zbMATH. Первоисточники (Painlevé, Wintner, Laloy 1976, Ureña) не открывались.

---

## 1. Гладкие контрпримеры (§3)

### 1.1 Painlevé–Wintner

[Литература: BP22, arXiv:2208.01139v1, §1, полный текст статьи BP22; первоисточники не открывались]
Дословно: «The Lagrange - Dirichlet converse is false in the class of smooth potentials. The first example of this
phenomenon was given by P. Painlevé in 1904 and the following is the A. Wintner's version [Wi] of it: Consider the
one degree of freedom Newtonian system with the smooth potential U(x) = exp(−x^{−2}) cos(x^{−1}), x ≠ 0, U(0) = 0.
The origin is a critical point and it is not a local minimum. For every neighborhood of the origin, there is an
interval centered at it and contained in the neighborhood such that the potential is maximum and strictly greater
than zero on the interval's boundary. Therefore, for every neighborhood of the origin, every motion with small
enough energy is trapped in an interval contained in the neighborhood hence the origin is Lyapunov stable.»

Ссылки там: [Wi] A. Wintner, *The Analytical Foundations of Celestial Mechanics*, Princeton Univ. Press, 1941.
Painlevé 1904 по Alva–Garcia (arXiv:1508.07427v2, библиография): P. Painlevé, Sur la stabilité de l'équilibre,
C. R. Acad. Sci. Paris 138, 1555–1557 (вторичный источник).

Варианты формулы в литературе (все — гладкие, все дают устойчивость без минимума):
- Wintner в версии BP22: e^{−x^{−2}} cos(x^{−1});
- в BMP21 (arXiv:1906.11962v3, полный текст) «Painlevé»: U(x) = exp(−|x|^{−1}) sin(|x|^{−1}), «C^∞ potential»;
- у Rauch 2013–14 (numdam, полный текст): V(x) = e^{−1/|x|} sin 1/|x|; у Alva–Garcia: e^{−1/q²}... sin(1/q).
Вывод: «точной» формулы Painlevé из первоисточника у меня нет, форма меняется от автора к автору.

Критические точки накапливаются к 0 (изолированность нарушена): [Доказано, прямое вычисление]. U(x)=e^{−x^{−2}}cos(1/x)
обращается в нуль в точках 1/x = π/2 + kπ, они сходятся к 0; по теореме Ролля между соседними нулями есть
нуль U′. Те же рассуждения годятся для e^{−1/|x|} sin(1/|x|).
Ни один источник этого явно не пишет. Вывод мой, три строки.

Вердикт по строке «Painlevé (1904), Wintner»: **подтверждено**. Уточнить: формула с cos и e^{−1/x²} — версия Wintner (1941),
у других авторов sin и e^{−1/|x|}. Утверждение о накоплении критических точек верно (см. выше).

### 1.2 Laloy 1976

Первоисточник: M. Laloy, On equilibrium instability for conservative and partially dissipative systems,
Int. J. Non-Linear Mech. 11 (1976), 295–301, doi:10.1016/0020-7462(76)90015-9 (zbMATH 0335.70020).
[Литература, ссылка проверена по zbMATH; текст Laloy 1976 не открывался]

Формулы в трёх независимых источниках:

1. BP22, §1 (полный текст, рендер страницы проверен глазами): «U(x,y) = exp(−x^{−2}) cos(x^{−1}) − exp(−y^{−2})
   (cos(y^{−1}) + y²), x, y ≠ 0, and defined by its unique smooth extension on the coordinate axes. The origin is
   a critical point and it is not a local minimum. ... the set U^{−1}((−∞, 0]) contains the two diagonals x = ±y
   ... the projections of the motion on the respective coordinates are decoupled trapped motions as in the first
   example hence the origin is again Lyapunov stable.»
2. Рецензия zbMATH на Taliaferro 1990 (Zbl 0679.70003): «U(x1,x2) = e^{−x1^{−2}} cos(1/x1) − e^{−x2^{−2}}(x2² + cos(1/x2)),
   x1x2 ≠ 0, which is negative and decreasing on the line x2 = x1, x1 > 0, then the origin for (1) is stable»
   (n = 2, T = x′·x′).
3. BMP21 (полный текст) приводит другую формулу: U(x,y) = exp(−|x|^{−1}) sin(|x|^{−1}) − exp(−|y|^{−1}) sin(|y|^{−1}) − y²,
   «C^∞ potential». Это не та же функция, что в п. 1 и 2: в BMP21 множитель e^{−|y|^{−1}} не стоит перед y².
   Какой вариант у Laloy, я не знаю.

Вердикт по строке «Laloy (1976)»: **подтверждено** (формула совпадает с п. 1 и 2), но формулу из BMP21 надо
помечать как другой вариант. Пометку «формула по вторичному источнику» оставить. Выяснить, какой вариант у Laloy,
можно только по тексту 1976 года (есть копия в репозитории UCLouvain: hdl.handle.net/2078.1/66672, доступ закрыт).

Недостающее в строке: точка 0 в примере Laloy **не изолированная критическая точка**. [Доказано, прямое
вычисление.] ∇U = (u′(x), −g′(y)) с u(x) = e^{−x^{−2}}cos(1/x), g(y) = e^{−y^{−2}}(cos(1/y) + y²). У u и у g
знак меняется бесконечно часто при x, y → 0 (у g — потому что cos(1/y) + y² меняет знак бесконечно часто).
Ролль даёт последовательности x_k → 0 и y_j → 0 с u′(x_k) = 0 и g′(y_j) = 0. Тогда (x_k, y_j) — критические
точки, накапливающиеся к 0. Значит, пример Laloy не опровергает (A) и неприменим к изолированному случаю.
BP22 этого не говорят.

### 1.3 Ureña 2020

[Литература: A. J. Ureña, To what extent are unstable the maxima of the potential?, Ann. Mat. Pura Appl. (4) 199
(2020), no. 5, 1763–1775, doi:10.1007/s10231-020-00941-2] Сверка: рецензия zbMATH (Zbl 1453.37055,
рецензент C. Lăzureanu), аннотация Springer (через поиск), формулировка теоремы из BP22. Полный текст не открывался
(Springer — подписка; копия в репозитории Гранады digibug.ugr.es/handle/10481/99448 по OpenAlex открытая, но с сервера
закрыта Cloudflare). **Версии на arXiv нет:** запросы arXiv API по автору и теме ничего не вернули.

Аннотация (Springer, по результатам поиска, цитата): «...we complement their theorems by presenting an example of
a smooth potential on the plane having an isolated maximum and such that the associated dynamical system has
a converging sequence of periodic orbits. This implies that the maximum is not unstable in a stronger sense
considered by Siegel and Moser.»

Теорема, дословно по BP22, §1 (там: «Ureña's example ([Ur], Theorem 1.1)»):
«Theorem (A. J. Ureña). There exists a C^∞ function U : R² → R satisfying: (1) U(0) = max_{R²} U.
(2) ∇U(q) ≠ 0 for any q ≠ 0. (3) There exists a sequence T_n > 0 of positive numbers and a sequence
q_n : R/T_nZ → R² of nontrivial periodic solutions of q̈ = −∇U(q) such that
max_t (‖q_n(t)‖ + ‖q̇_n(t)‖) → 0 as n → +∞.»
Там же: «In Ureña's example, the periods T_n diverge and the closed orbits q_n do not encircle the origin.»
Рецензия zbMATH: «there is a C^∞(R²,R) function V such that (0,0) is a global maximum point of V, ∇V(q) ≠ (0,0)
for all q ≠ (0,0) and the Newtonian system ... has a sequence q_n of nontrivial periodic solutions with
max_t(‖q_n(t)‖ + ‖q̇_n(t)‖) → 0».

Условия: гладкость C^∞; n = 2; максимум **глобальный** и (из (2)) **строгий и изолированный** критический;
кинетическая энергия ньютоновская. Определение Зигеля–Мозера по BP22: равновесие неустойчиво в смысле
Зигеля–Мозера, если у него есть окрестность, в которой оно — максимальное инвариантное множество.

Вердикт по строке «Ureña (2020)»: **подтверждено**. Уточнения:
- максимум глобальный, а не просто строгий изолированный; из (2) он изолирован как критическая точка;
- у BP22 это пример того, что максимум не неустойчив по Зигелю–Мозеру. Лагранжево неустойчивость максимума
  по Hagedorn 1971 / Taliaferro 1980 остаётся (BP22, §1);
- последняя фраза §3 «Пример Уреньи показывает, что “полная неустойчивость” требует аналитичности» лучше
  звучит как «показывает, что в C^∞ тотальная неустойчивость неверна». «Требует аналитичности» — вывод, не теорема.
  BP22 пишут: тотальная неустойчивость (гипотеза Паламодова) исключила бы пример Уреньи в аналитическом классе.

---

## 2. Нестрогие минимумы (§4)

Предварительное замечание. [Доказано, тривиально.] Если 0 — **изолированная** критическая точка и не строгий
минимум, то 0 не является и нестрогим минимумом. Иначе точки с U = U(0) в любой окрестности были бы точками минимума,
значит, критическими, и 0 не была бы изолированной. Поэтому для задачи (A) нестрогие минимумы не нужны: они нужны
для полного обращения Лагранжа–Дирихле (гипотеза Ляпунова), которое слабее по формулировке и сильнее по сути (A).
Это стоит сказать прямо в §4.

### 2.1 Laloy–Peiffer 1982

M. Laloy, K. Peiffer, On the instability of equilibrium when the potential has a non-strict local minimum,
Arch. Rational Mech. Anal. 78 (1982), 213–222, doi:10.1007/BF00280037 (Zbl 0494.70021).
Сверка: zbMATH, только ключевые слова («two degrees of freedom», «improvement of results by G. Hamel and L. Silla»);
вторичные источники BMP21 и BP22 (полный текст). Сам текст не открывался (Springer).

BP22, §1: «The remaining case of a non strict local minimum was treated in [LP] by M. Laloy and K. Peiffer who showed
the instability of such a point for a real analytic potential. This completes the proof of the analytic
Lagrange - Dirichlet converse in dimension two.»
BMP21, §1: «The case of a non strict local minimum of the potential but with two degrees of freedom was treated in [LP].»
Тип неустойчивости (по Ляпунову) и n = 2 подтверждены вторично.

Вердикт: **неточно**. Что подтверждено: n = 2, аналитический потенциал, нестрогий локальный минимум,
неустойчивость по Ляпунову. Что **не подтверждено**: «достигается вдоль кривой через 0» и «при подходящей
гладкости». Из доступных текстов видно только «real analytic», кривая не упомянута. Исправить на: «n = 2, аналитический U,
0 — нестрогий локальный минимум ⇒ неустойчивость (по BP22, вторично); подробности формулировки не сверены».

### 2.2 Burgos–Maderna–Paternain 2021 (BMP21)

[Литература: J. M. Burgos, E. Maderna, M. Paternain, On the Lyapunov instability in Newtonian dynamics, Nonlinearity 34
(2021), no. 10, 6719–6726, doi:10.1088/1361-6544/ac1a1a; arXiv:1906.11962v3 (4.03.2021, 8 стр.), полный текст arXiv v3.]
Подтверждено Crossref и zbMATH (1483.37069).

Дословно (аннотация): «We prove Lyapunov instability for cases in which the local minimum of the potential energy is
reached on a hypersurface of the configuration space. In contrast to the known results in this direction, which hold
for potentials satisfying hypotheses on the first non-zero jet, this new result covers several real analytic cases
that the previous do not.»

Теорема (§1), дословно: «Hypothesis. The potential U is the composition g ∘ f such that zero is a regular value of f in
C³(R^n, R) and g in C²(R, R) verifies g ≥ 0 vanishing only at zero. In particular the set M = {x ∈ R^n | f(x) = 0} =
{x ∈ R^n | U(x) = 0} is a hypersurface of R^n and M × {0} consists entirely of equilibrium points of the Newtonian
dynamics. Theorem. Every point in M × {0} is Lyapunov unstable.»
Условия: ньютоновская динамика ẍ = −∇U в R^n, любое n; f ∈ C³, g ∈ C², U = g∘f ≥ 0, нестрого минимальный уровень —
гладкая гиперповерхность. Это не требует аналитичности; аналитичность нужна лишь для сравнения с критериями по джету
(пример U = (x² + 2y² + 3z² − 1)⁴, эллипсоид).

Вердикт: **подтверждено**, но формулировка в KNOWN неполна: нужно записать гипотезу U = g∘f (f ∈ C³ с 0 регулярным
значением, g ∈ C², g ≥ 0, g = 0 только в 0). Аналитичность в самой теореме не нужна («Покрывает аналитические
случаи» — это комментарий авторов, а не условие). Выводится именно неустойчивость по Ляпунову, не асимптотическая траектория
(доказательство идёт через масштабирование x_ε(τ) и предельную кривую в M).

### 2.3 Burgos–Paternain 2021 (BP21)

[Литература: J. M. Burgos, M. Paternain, On the Lyapunov instability in Lagrangian dynamics, arXiv:2108.05074v3
(21.12.2021); Proc. Amer. Math. Soc. 150 (2022), no. 10, 4335–4348 (zbMATH Zbl 1507.37073); Crossref DOI 10.1090/proc/15972.]
Публикация **найдена**: Proc. AMS 150:10 (2022), 4335–4348 (по zbMATH). Внимание: страница arXiv показывает
«related DOI 10.1088/1361-6544/ac1a1a» — это DOI статьи BMP21 из Nonlinearity, а не BP21. Не путать. Полный текст arXiv v3 прочитан.

Теорема 1.1, дословно: «Consider a zero potential point p and suppose there is a neighborhood V of p in N and a real
valued C³ regular function f on V such that dU(∇_ρ f) = O(U). Then, (p, 0) is a Lyapunov unstable equilibrium point
of the Lagrangian dynamics of (2).» Здесь (2): L_mech = Q_x(v) − U(x) на TN, Q — положительно определённая C²-форма,
U ≥ 0 — C²-функция, M = U^{−1}(0) непусто и замкнуто, ρ — риманова метрика с Q_x(v) = ‖v‖²_x/2. Уравнение (3):
Σ g^{ab} ∂_a U ∂_b f = O(U).
Следствие 2: квазиоднородный U ≥ 0 (в ньютоновской динамике): каждая точка (U^{−1}(0) ∩ V_α) × {0} неустойчива,
где V_α — множество, где некоторое α_i x_i ≠ 0. Примеры: (x² − y²z)², (x²z² + x³ − y²)². Главная теорема — вариант с
магнитным полем (условие ‖ι_{∇f} dμ‖ = O(U^{1/2})); при U = z², μ = x dy все точки плоскости z = 0 **устойчивы**.
Авторы пишут, что обращение теоремы Routh в общем случае неверно (с магнитным полем).

Вердикт: **подтверждено**. Уточнить: «гладкое решение» — это C³ функция f, регулярная в p (в тексте «regular function»,
определение регулярности не искал), с dU(∇_ρ f) = O(U), и условия на U (C², U ≥ 0). Опубликовано: Proc. AMS 150 (2022).
Критерий подходит для **неизолированных** нулей U, к (A) прямого отношения не имеет.
Авторы подчёркивают: критерий достаточен, но не необходим (U = x²y²).

### 2.4 Burgos–Paternain 2022 (BP22)

[Литература: J. M. Burgos, M. Paternain, On the Lagrange–Dirichlet converse in dimension three, arXiv:2208.01139v1
(1.08.2022), 44 с., полный текст arXiv v1.] **Публикация не найдена:** ни Crossref, ни zbMATH (там запись «Preprint»),
ни поиск не показывают журнальную версию (на 21.10.2026). Помечать как препринт.

Аннотация, дословно: «Consider a mechanical system with a real analytic potential. We prove that in dimension three,
there is an open and dense subset of the set of non strict local minimums of the potential such that every one of its
points is a Lyapunov unstable equilibrium point.»
Теорема 1.1 (дословно): «Consider a mechanical system on a three dimensional real analytic manifold with a real analytic
potential. Then, there is an open and dense subset of the set of non strict local minimums of the potential such that
every one of its points is a Lyapunov unstable equilibrium point.»
Условия: n = 3, вещественно-аналитическое многообразие, вещественно-аналитический потенциал, **любая** гладкая кинетическая
энергия (критерий не зависит от кинетического члена, Следствие 3.2). Результат — только про нестрогие локальные минимумы.
Это **не** решение (A) и не результат о критических точках, не являющихся минимумами. Открытое и плотное подмножество
в множестве нестрогих минимумов — не всё множество.

Критерий (Теорема 3.1), дословно: «Consider a nonnegative smooth potential U on a smooth manifold M and let p be a zero
potential point. If there is a locally Lipschitz continuous weakly logarithmic for U vector field in some neighbourhood
of p in M and non null at this point, then (p, 0) is a Lyapunov unstable equilibrium point of the Lagrangian dynamics
of (21).» Определение 2.10: поле V слабо логарифмическое для U, если V(U) = PU с P ограниченной на компактах.
Теорема 2.11 (коразмерность 1) и 2.12 (коразмерность 2) строят такие поля на открытом плотном подмножестве; размерность 3
используется в последнем разборе (X̊^(1), X̊^(2), X̊^(3)).

Что они пишут о n = 2 (дословно, §1): «For two degrees of freedom, this problem was completely solved. Indeed,
V. P. Palamodov in [Pa2] and S. D. Taliaferro in [Ta] showed independently the instability of a non local minimum
critical point of a real analytic potential in dimension two for a Newtonian kinetic term. Based on the previous
Palamodov's work, this result was generalized by V. V. Kozlov in [Ko] for an arbitrary kinetic term. The remaining case
of a non strict local minimum was treated in [LP] by M. Laloy and K. Peiffer ... This completes the proof of the
analytic Lagrange - Dirichlet converse in dimension two.»
Здесь [Pa2] = Palamodov 1977 (Funct. Anal. Appl. 11, 277–289), [Ta] = Taliaferro 1980 (JDE 35, 248–265), [Ko] = Kozlov,
Russian Math. Surveys 36 (1981), 238–239.

О Brunella: «In [Br], M. Brunella gave an alternative and very elegant proof of the Arnold's problem for two degrees of
freedom.» и «Applying his result to an appropriate energy level of a hamiltonian vector field in four dimensional space,
he solves the Arnold's conjecture for two degrees of freedom. This way, Brunella's result applied to hamiltonian vector
fields is about instability in two dimensional configuration space while ours concerns instability in three
dimensional configuration space.»

О задаче Арнольда и Palamodov (дословно): «Starting from A. M. Lyapunov [Ly] and continuing with [Ch], [Ha], [HM], [Ko2],
[Ko3], [Ku], [KP], [MN], [So], [Ta2], [Ta3], many partial results have been given towards the solution of the
Arnold's problem and their common feature is that the Lyapunov instability criteria involves the lack of a local
minimum at the origin of the first nonzero jet of the potential.» Пример: U = x⁴ + y⁴ − z⁶ в R³: «the origin is an
isolated critical point of the potential that is not a local minimum. However, the origin is a minimum of the first
non zero jet ... hence none of the mentioned results apply.»
«In [Pa], V. P. Palamodov stated a total instability result for non minimum critical points of the potential whose
proof is incomplete. This total instability conjecture would imply the Arnold's problem and the impossibility of
Ureña's example in the class of real analytic potentials as well. All of these remain as open problems.»
«We do not know whether there is a stable non strict local minimum point of a real analytic potential in the
Lagrangian dynamics of (1).»

Вердикт по строке «Burgos–Paternain 2022»: **подтверждено**, с уточнениями:
- препринт (публикации не найдено);
- результат — **открытое плотное подмножество** нестрогих минимумов, а не вся задача; о (A) в нём нет ничего нового;
- «по их обзору при n = 2 полное обращение следует из совокупности известных результатов (изящное доказательство — Brunella)»:
  это верно по смыслу, но точнее: полное аналитическое обращение при n = 2 следует из Palamodov 1977 + Taliaferro 1980
  (неэквивалентность минимума, ньютоновская кинетика) + Kozlov 1981 (произвольная кинетика) + Laloy–Peiffer 1982
  (нестрогий минимум); Brunella даёт другое доказательство (A) для n = 2, то есть изолированного случая;
- «при n > 2 задача открыта, известны лишь частичные результаты» — у BP22 слово «open» относится к аналитической
  гипотезе Лагранжа–Дирихле и к (A) без жёстких оговорок; формулировка KNOWN близка, но это пересказ, не цитата.

**Расхождение между BMP21 и BP22 (важно для главного агента).** BMP21 (2019/2021), §1: «Palamodov completely solves
the Arnold's problem giving a beautiful proof ... Concretely, he proves (Corollary 2.2 in [Pa], page 7): Let U be a
real analytic potential and p a critical point. If p belongs to the closure of the region where the potential is
strictly less than U(p), then p is Lyapunov unstable.» Здесь [Pa] = Palamodov 1995, Transl. AMS (2) 168, 5–20.
BP22 (2022), §1: тот же [Pa] «stated a total instability result ... whose proof is incomplete ... All of these remain
as open problems». То есть авторы за три года изменили оценку работы Palamodov 1995. Это согласуется с отзывом arXiv:2108.05829
(Burgos). Для KNOWN: Palamodov 1995 нельзя считать доказательством (A).

### 2.5 Brunella 1998

[Литература: M. Brunella, Instability of equilibria in dimension three, Ann. Inst. Fourier 48:5 (1998), 1345–1357,
doi:10.5802/aif.1657, numdam AIF_1998__48_5_1345_0. **Полный текст прочитан** (введение и формулировки; доказательство,
§1–§6, не вычитывалось).] Рецензия zbMATH 0930.37025 (T. de Jong) согласуется.
Замечание: в KNOWN указан numdam-идентификатор верно; по Crossref DOI = 10.5802/aif.1657, не aif.1659.

Теорема, дословно: «Let v be an analytic vector field defined on a neighbourhood U of 0 ∈ R^n and having at 0 an isolated
singular point. Let M ⊂ U be an analytic irreducible subvariety of dimension three, containing 0 and smooth outside 0,
invariant by v. Suppose that the link of M at 0 (which is a compact connected surface) has nonvanishing Euler
characteristic. Then there exists p ∈ M \ {0} and T ∈ {−∞, +∞} such that γ_p(t) → 0 as t → T, where γ_p denotes the
trajectory of v through p. In particular, 0 is an unstable singular point.»
Определение «стабильной» особой точки у Brunella: есть фундаментальная система окрестностей, инвариантных относительно v
(то же, что устойчивость по Ляпунову в прошлом и в будущем). «Of course, if n = 3 we may choose M = U.»
При n = 4 для гамильтонова поля нужна неприводимая компонента H^{−1}(H(0)) с ссылкой ненулевой эйлеровой характеристики
(она **не** обязана быть всем уровнем энергии, а уровень H = H(0) сингулярен в 0).

Следствие, дословно: «Consider the second order differential equation q̈ = −grad F where F is an analytic function on
a neighbourhood V of 0 ∈ R² such that 0 is an isolated critical point which is not a minimum nor a maximum. Then there
exists initial conditions (q_0, q̇_0) ∈ V × R² (resp. (q_1, q̇_1)) such that the corresponding solution tends to (0,0) as
the time tends to +∞ (resp. −∞).» Максимум Brunella исключил: ссылка тора (эйлерова характеристика 0), «we notice that it is
rather easy to prove the instability of (0,0) when F has a maximum point ... (Maupertuis principle and Hopf–Rinow
theorem)». Он называет следствие «refinement of a (not too) particular case of a theorem of Palamodov [Pa]».

Вердикт по строке «Brunella (1998)»: **неточно — как исправить**. Строка верна только для n = 3 («0 — изолированная
особая точка аналитического поля в R³ ⇒ траектория, стремящаяся к 0 в прошлом или будущем»). В общем виде:
M — трёхмерное аналитическое неприводимое инвариантное подмногообразие, гладкое вне 0, с линком ненулевой эйлеровой
характеристики. «Индексные соображения типа Пуанкаре–Хопфа» и «десингуляризация» (Cano, Sancho de Salas) в тексте есть
(введение). Применение к (A): только n = 2 (гамильтониан H = ½|p|² + F, четырёхмерное фазовое пространство).
Прямого вывода для n ≥ 3 из Brunella нет (BP22 это подтверждают).

---

## 3. Гладкие изолированные критические точки: что известно

### 3.1 Контрпример C^∞ с изолированной критической точкой и устойчивым равновесием

**Не найден.** Что проверено:
- Painlevé–Wintner и Laloy (разд. 1.1–1.2): критические точки накапливаются к 0 (доказано выше); Ureña — максимум,
  неустойчив по Ляпунову (Hagedorn 1971, Taliaferro 1980 по BP22).
- Поиск по zbMATH («Lagrange-Dirichlet converse», «inversion of the Lagrange-Dirichlet theorem»; ~35 записей), arXiv,
  Google-подобный поиск и ссылки BMP21/BP21/BP22/Rauch/Alva–Garcia: ни одной работы, где строился бы такой пример.
  Ни один из прочитанных авторов не заявляет, что такого примера нет, и не заявляет, что он есть.
- BMP21, цитируя комментарии к Arnold's Problems (стр. 250–253): «...The problem on the converse of the Lagrange-Dirichlet
  theorem makes therefore sense only under one or another additional assumptions (e.g., that of analyticity of the
  potential).» (вторично, текст Arnold 2004 не открывался.)
- BP22: «We do not know whether there is a stable non strict local minimum point of a real analytic potential.»

**Случай n = 1 тривиален.** [Доказано; U ∈ C¹ достаточно.] Если 0 — изолированный нуль U′ и не минимум, то U′ имеет
постоянный знак на (0, ε) и на (−ε, 0). Не минимум значит, что U < U(0) на одной из сторон на целой полуокрестности;
пусть U′ < 0 на (0, ε), тогда x″ = −U′ > 0 и частица, стартующая с нулевой скоростью в x > 0, движется вправо и уходит
из окрестности. Неустойчивость. При n = 1 (A) верна даже для C¹.

Вывод: в классе C^∞ вопрос «есть ли устойчивый изолированный не-минимум при n ≥ 2» мне в литературе не встретился
ни как теорема, ни как открытая проблема. Это пробел литературы или отсутствие интереса, но не ответ «нет».

### 3.2 Положительные результаты для гладких потенциалов

Все найденные результаты требуют условий на разложение Тейлора или на асимптотику, а не просто изолированности.

- **Kozlov, в формулировке Rauch** (Rauch, Séminaire Laurent Schwartz 2013–2014, exposé XII, numdam, полный текст),
  Теорема 4.1: «Suppose V ∈ C^∞, 0 is a critical point, and, 0 is not a local minimum. Suppose that the Taylor expansion
  at 0 is V ∼ V_m(x) + V_{m+1}(x) + ··· with V_j homogeneous of degree j. If the leading term V_m does not have a local
  minimum at 0, then the equilibrium (0, 0) is unstable.» Rauch ссылается на Kozlov 1986 (JAMM 50, 719–725) как [6] и
  на Taliaferro 1990 для ослабления гладкости («The differentiability hypothesis is radically reduced in [11]»).
  Условие: ряд Тейлора имеет **ненулевой** лидирующий член V_m (то есть U не плоская), и V_m без минимума. Это не изолированность.
- **Taliaferro 1990** (Arch. Rational Mech. Anal. 109, 183–194; рецензия zbMATH 0679.70003, цитата): T, U ∈ C², «U^{(i)}(x) =
  U_p^{(i)}(x) + O(‖x‖^{p+ε−i}) as x → 0, where p > 0 ... and U_p ... is positively homogeneous of degree p and three times
  continuously differentiable». Если U_p(x) < 0 в некоторой точке, существует решение x(t) → 0 (t → +∞ при 0 < p < 2, t → −∞
  при p ≥ 2); следовательно, неустойчивость. Условие — асимптотическая однородность с гладким U_p. Для плоских функций неприменимо.
- **Zbl-рецензия Kozlov 1986**: теорема существования асимптотических траекторий при ряде V₂ + V_m + V_{m+1} + ...
  и V₂ + V_m без локального минимума (без утверждения об изолированности).
- **Hagedorn 1971; Taliaferro 1980 (ARMA 73); Sofer 1983 (ZAMP 34); Barone-Netto–Zampieri 1994 (Proc. AMS 121:3,
  711–713)** — максимумы (в том числе нестрогие): неустойчивость при гладком U, любом гладком T (BP22; Zbl-рецензия на
  Barone-Netto–Zampieri: «from a point q₀ where V has a (weak) maximum, one can go near the boundary of any compact ball
  where V ≤ V(q₀)»). Изолированность тут не нужна.
- **Moauro–Negrini 1989 (Differential Integral Equations 2:4, 471–478), Maffei–Moauro–Negrini 1991 (DIE 4:4, 767–782)**:
  по Alva–Garcia (arXiv:1508.07427, введение, полный текст): неустойчивость, если после замены координат
  π(q) = ‖(q₁..q_r)‖² + π_s(q_{r+1}..q_n) + R, π_s однородный степени s ≥ 2 без минимума, R(q)/‖q‖^s → 0 (вторично).
- **Garcia–Tal 2003 (JDE 194, 364–381), Freire–Garcia–Tal 2008 (JDE 245, 490–504), Alva–Garcia 2017 (QTDS 16, 371–389;
  arXiv:1508.07427)** — условия «джет показывает отсутствие минимума» (формально: j^sΠ показывает отсутствие минимума, если
  каждая g с тем же s-джетом не имеет минимума); при n = 2 — Garcia–Tal; при n > 2 — Freire–Garcia–Tal требует Гессиан ≥ 0
  с ядром размерности ≤ 2 (по Alva–Garcia, вторично).
- **Rauch (2013–2014)**: теорема 1.2: «Suppose that the non constant real valued V ∈ C^∞(|x| < r) satisfies P(x, ∂)V = 0
  with P [вещественным, коэффициенты C^∞] elliptic at x. If x is an equilibrium for x″ = −∇V(x) and P is elliptic at x then the
  equilibrium is unstable.» Доказательство: сильная единственность для эллиптических уравнений ⇒ V не бесконечно плоская,
  V_m удовлетворяет Σ a_ij(0)∂_i∂_j V_m = 0, принцип минимума ⇒ V_m без минимума, затем теорема Kozlov. Palamodov 1995 не используется.
  Rauch пишет: «The conjecture is easy when d = 1. Taliaferro [10] proved the case d = 2 in 1980.»
  «Summary and prospects. i. I think that it is more important that V satisfies a second order equation, than that V is
  real analytic.»
- **Allaire–Rauch**: в тексте Rauch — «[1] G. Allaire and J. Rauch, In preparation.» Тема — Earnshaw для идеально
  проводящего заряженного тела (Maxwell, §116). Работа в поиске не найдена (arXiv, zbMATH, Google); анонс семинара (talks.cam, по
  поиску) говорит про проводники и диэлектрики. К задаче (A) прямого отношения не имеет. Утверждения «Allaire–Rauch
  пользуются результатами Паламодова» в доступных текстах **нет**: Rauch использует Kozlov; работа Allaire–Rauch не опубликована
  и не найдена. KNOWN не упоминает «Allaire–Rauch» (там только Rauch [А]). Строку Rauch в KNOWN лучше расширить: теорема 1.2 —
  C^∞, эллиптическое уравнение (в частности, гармонические потенциалы), опирается на Kozlov.

Прочее найденное и **не сверенное** (только названия или аннотации):
- Absil–Kurdyka, On the stable equilibrium points of gradient systems, Systems & Control Letters 55:7 (2006), 573–577,
  doi:10.1016/j.sysconle.2006.01.002 (по аннотации с сайта авторов): для **градиентного потока** ẋ = −∇f при аналитическом f
  устойчивость ⇔ локальный минимум; для C^∞ — ни необходимо, ни достаточно. Это другая динамика, не наша; полезно как
  аналог. Не открывалось.
- Bulatović (1992, 1995), Peiffer 1991 (JAMM 55:4, 436–441, «analytic function»), Sokol'skij 1981, Wiener 1993,
  Negrini 1995, Rumyantsev–Sosnitskij 1993: записи в zbMATH без текста; не изучались.
- Bertotti–Bolotin: M. L. Bertotti, S. V. Bolotin, Arch. Rational Mech. Anal. 152:1 (2000), 65–79 (zbMATH 0968.70016, по
  рецензии на Bortolatto–Garcia–Tal). Теорема (BP22, цитата): «For two degrees of freedom, there exist a smooth potential U and
  two smooth kinetic terms Q and Q̃ such that the equilibrium 0 is stable for the system L = Q − U and unstable for
  the system L̃ = Q̃ − U.» Условия C^∞ (и U, и T); Garcia–Tal 2003 дали явный пример. В аналитическом классе
  устойчивость/неустойчивость от кинетики не зависит (BP22, §1, по Garcia–Tal–Bortolatto). Это важно для (A): нельзя считать, что в
  гладком классе ответ не зависит от метрики. Для (A) аналитичность и метрика — отдельные оговорки.
- Garcia (Tal): другая ссылка на «Garcia–Tal 2005» в BP22: M. V. P. Garcia, F. A. Tal, The influence of the kinetic energy
  in equilibrium of Hamiltonian systems, JDE 213 (2005), 410–417 — в KNOWN нет.

Конечная определённость, кратность, неравенства Лоясевича в связи с (A): целенаправленный поиск (zbMATH, arXiv, ссылки перечисленных
работ) ничего не дал. Из прочитанных работ выводов типа «если критическая точка изолирована и U гладкая конечной
определённости (или U удовлетворяет неравенству Лоясевича), то …» нет. DK05 (D'Acunto–Kurdyka) в KNOWN упомянут, но
в прочитанных текстах по теме не цитируется. Связь с неравенством Лоясевича в литературе по (A) мне не встретилась.

---

## 4. Rauch и Allaire–Rauch (пункт 4 задания)

См. выше, разд. 3.2. Коротко:
- Rauch, Earnshaw's theorem in electrostatics and a conditional converse to Dirichlet's theorem, Sémin. Laurent Schwartz,
  EDP et applications, 2013–2014, exposé XII, 10 с., doi:10.5802/slsedp.56 (numdam; CC BY-ND 3.0 FR). [Литература: полный текст
  прочитан.] Доказано: теорема 1.2 (эллиптическое уравнение P V = 0 с C^∞ коэффициентами и неконстантный V ∈ C^∞ ⇒ любой
  равновесный 0 неустойчив). Использует только Kozlov (теорема 4.1, C^∞, ненулевой лидирующий член V_m без минимума).
  Результатов Palamodov не использует. Про (A): отмечает, что для d = 1 гипотеза Арнольда лёгкая, а d = 2 — Taliaferro 1980.
- Allaire–Rauch: «in preparation» (2014); найти не удалось.

---

## 5. Полное обращение при n = 2 для аналитических потенциалов (пункт 5 задания)

[Литература: BP22 §1 и BMP21 §1 (вторично, полный текст обеих)]
- Не минимум (Newton-кинетика): Palamodov, Funct. Anal. Appl. 11:4 (1977), 277–289 (Zbl 0415.70006) и Taliaferro, JDE 35 (1980),
  248–265 (Zbl 0398.34047) независимо; тексты не открывались, только вторичные цитаты. Условия по BP22: вещественно-аналитический
  потенциал в R², ньютоновская кинетика.
- Произвольная кинетическая энергия: Kozlov, Instability of equilibrium in a potential field, Russ. Math. Surv. 36:1 (1981),
  238–239 (УМН 36:1 (1981), 209–210; Zbl 0478.70004 / 0459.70005), «based on the previous Palamodov's work» (BP22).
  В KNOWN [Koz81] указан второй номер: УМН 36:3 (1981), 215–216. По zbMATH есть статья Kozlov, Russ. Math. Surv. 36:3 (1981),
  256–257, «On the instability of equilibrium in a potential field» (Zbl 0556.70003). Тут нужна сверка номеров УМН;
  первичный номер 36:1 подтверждается тремя записями.
- Нестрогий минимум: Laloy–Peiffer 1982 (см. 2.1).
- Другое доказательство (A) при n = 2 (изолированный случай): Brunella 1998.
- Итог: BP22 и BMP21 одинаково считают аналитическое обращение при n = 2 полностью решённым. Условия: вещественно-аналитический U на R²
  (или двумерном аналитическом многообразии), без других предположений.

---

## 6. Предлагаемые правки к KNOWN_RESULTS.md (список, файл не правился)

**§3**
1. Строка Painlevé–Wintner: указать, что формула с e^{−x^{−2}}cos(1/x) — версия Wintner (1941, *The Analytical Foundations of
   Celestial Mechanics*, по BP22), оригинал: Painlevé, C. R. Acad. Sci. Paris 138 (1904), 1555–1557 (по Alva–Garcia); у других авторов
   вариант e^{−1/|x|} sin(1/|x|). Добавить: накопление критических точек к 0 следует из теоремы Ролля (нули U сходятся к 0).
2. Строка Laloy 1976: дописать точную ссылку «Int. J. Non-Linear Mech. 11 (1976), 295–301, doi:10.1016/0020-7462(76)90015-9»;
   формула из KNOWN совпадает с BP22 и с zbMATH-рецензией на Taliaferro 1990. Добавить: в BMP21 приведена другая формула
   (exp(−|x|^{−1}) sin(|x|^{−1}) − exp(−|y|^{−1}) sin(|y|^{−1}) − y²); добавить, что точка 0 **не изолирована** как критическая
   (критические точки (x_k, y_j) → 0).
3. Строка Ureña: добавить «глобальный» максимум, условие ∇U(q) ≠ 0 при q ≠ 0, сведения «периоды T_n → ∞, орбиты не охватывают
   начало, max_t(‖q_n‖ + ‖q̇_n‖) → 0», слова «версии на arXiv не найдено». Последнюю фразу «требует аналитичности» заменить:
   «в C^∞ тотальная неустойчивость неверна; в аналитическом классе пример такого типа исключался бы гипотезой Паламодова (BP22)».
4. Фразу «Нам не известен гладкий пример…» оставить, добавив: поиск по литературе (zbMATH, arXiv, BMP21, BP21, BP22) такого примера
   и такой постановки не обнаружил; для n = 1 (A) верна и в C¹ (доказательство в 3.1 настоящего конспекта).

**§4**
5. Вступление к §4: добавить, что при изолированной критической точке нестрогий минимум невозможен (разд. 2 заметки); нестрогие
   минимумы — отдельная часть полной гипотезы Ляпунова.
6. Laloy–Peiffer: убрать «достигается вдоль кривой через 0» и «при подходящей гладкости»; написать «n = 2, аналитический U, нестрогий
   локальный минимум ⇒ неустойчивость (вторично по BP22/BMP21); формулировку из текста не сверяли».
7. BMP21: записать гипотезу U = g∘f, f ∈ C³ (0 — регулярное значение), g ∈ C², g ≥ 0, g = 0 только в нуле; вывод — неустойчивость по
   Ляпунову каждой точки M×{0}; ньютоновская динамика, любое n; «аналитичность» не нужна (убрать «Покрывает аналитические случаи» из
   условия или оформить как комментарий авторов).
8. BP21: добавить публикацию Proc. Amer. Math. Soc. 150:10 (2022), 4335–4348, DOI 10.1090/proc/15972; указать, что arXiv-страница ошибочно
   показывает «related DOI» статьи BMP21. Уточнить формулировку: C³-функция f, регулярная в p, dU(∇_ρ f) = O(U), потенциал U ≥ 0 класса C²,
   лагранжиан Q − U (и версия с магнитным полем).
9. BP22: пометить как препринт (публикации не найдено, на 21.10.2026). Привести дословно теорему 1.1. Сформулировать: «открытое и плотное
   подмножество множества нестрогих минимумов»; результат для любой гладкой кинетической энергии; n = 3.
10. BP22 о n = 2: переписать как «Palamodov 1977 и Taliaferro 1980 (ньютоновская кинетика), Kozlov 1981 (произвольная), Laloy–Peiffer 1982 (нестрогий
    минимум); Brunella — другое доказательство (A)» — точнее, чем «из совокупности известных результатов».
11. BP22 и Palamodov 1995: добавить предупреждение, что BP22 называют «total instability result» Palamodov [Pa] (Transl. AMS 168,
    1995) **с неполным доказательством**, тогда как BMP21 писали, что Palamodov «completely solves the Arnold's problem».
12. Brunella: исправить формулировку на дословную теорему (M — трёхмерное аналитическое неприводимое инвариантное подмногообразие,
    гладкое вне 0, линк с χ ≠ 0; для n = 3 M = U); применение к (A) — только n = 2 (H = ½|p|² + F, фазовое пространство R⁴; нужна
    неприводимая компонента нулевого уровня с линком χ ≠ 0). Брунелла исключает максимум (линк — тор, χ = 0) и минимум.
    DOI: 10.5802/aif.1657. В «Применяется к случаю двух степеней свободы (поток на трёхмерном уровне энергии)» заменить «трёхмерным уровнем
    энергии» на «трёхмерной неприводимой компонентой нулевого уровня».

**§2 и библиография (замечено попутно)**
13. [NLM79]: автор — M. Laloy, On the inversion of the Lagrange–Dirichlet theorem in the case of an analytic potential, Int. J. Non-Linear
    Mech. 14 (1979), 59–65, doi:10.1016/0020-7462(79)90029-5 (Zbl 0415.70030). Пример «ряд V₂ + V_m + ..., V₂ + V_m без минимума ⇒
    асимптотическая траектория» по zbMATH-рецензии принадлежит Kozlov 1986 (JAMM 50, 719–725), а не [NLM79]; что доказано у
    Laloy 1979, не сверялось (zbMATH: «Hessian matrix», «analytic potential»).
14. [AMM93]: PII 002189289190002C — это **K. Peiffer, On inversion of the Lagrange–Dirichlet theorem, J. Appl. Math. Mech. 55:4 (1991), 436–441**
    (Zbl 0788.70012, DOI 10.1016/0021-8928(91)90002-C), а не Moauro–Negrini. DOI 10.1007/BF00962611 принадлежит **M. Sofer, ZAMP 34 (1983), 1–12**.
    Moauro–Negrini: Differential Integral Equations 2:4 (1989), 471–478 (Zbl 0714.70024); Maffei–Moauro–Negrini: DIE 4:4 (1991), 767–782.
    Условие «C^h, h > 3» в строке не подтверждено ни одним найденным источником. Про Moauro–Negrini вторично известно (Alva–Garcia):
    потенциал вида ‖(q₁..q_r)‖² + π_s(q_{r+1}..q_n) + R, π_s однородный без минимума, R = o(‖q‖^s).
15. [Koz81]: УМН 36:1 (1981), 209–210 (английский перевод: Russian Math. Surveys 36:1, 238–239) подтверждено; второй номер УМН 36:3 215–216 не нашёл,
    zbMATH знает Russ. Math. Surv. 36:3 (1981), 256–257 (Zbl 0556.70003).
16. [Koz86]: J. Appl. Math. Mech. 50:6 (1986), 719–725, DOI 10.1016/0021-8928(86)90079-1 (англ. перевод ПММ 50:6, 928–937).
17. Строка Rauch: расширить: Теорема 1.2 (C^∞, эллиптическое уравнение, неконстантный V); доказательство через Kozlov (теорема 4.1), Palamodov не используется;
    «Allaire–Rauch» — «in preparation» (2014), опубликованной работы найти не удалось.
18. Добавить: Bertotti–Bolotin 2000 (ARMA 152, 65–79; C^∞, n = 2: устойчивость при одной кинетике и неустойчивость при другой) и Garcia–Tal 2005 (JDE 213,
    410–417, явный пример) — они показывают, что в гладком классе нельзя считать ответ независимым от кинетической энергии.
