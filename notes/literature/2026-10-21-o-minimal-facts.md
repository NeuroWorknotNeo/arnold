# Сверка стандартных фактов (F1)–(F6) из §0 заметки Паламодова (плоскость)

Дата: 21.10.2026. Автор: literature (агент). Проверяемая заметка:
`notes/prover/2026-10-21-palamodov-plane-corrected.md`, §0. Правила меток — CLAUDE.md.

## Что реально открывалось (полный текст)

| Источник | Как получен | Что дал |
|---|---|---|
| L. van den Dries, *A generalization of the Tarski–Seidenberg theorem, and some nondefinability results*, Bull. AMS 15:2 (1986), 189–193 | свободный PDF на ams.org (журнал открытый), прочитан целиком (6 стр.) | о-минимальность, монотонность, полиномиальный рост, **разложение Пюизё** (с. 191–192) |
| M. Coste, *An introduction to o-minimal geometry* (Pisa, 1999; RAAG) | копия в Wayback Machine, прежний URL у Rennes выдаёт 403; PDF сканированный, текст получен OCR (tesseract), могут быть опечатки OCR | Thm 2.1, Ex. 2.3, Thm 3.1, Thm 3.2, Lemma 6.1, Thm 6.4, Cor. 6.5, Thm 6.6–6.7 |
| S. Starchenko, *Notes on o-minimality* (Fields Inst.) | свободный PDF | Thm 2.6, Thm 4.1, Thm 5.2, Thm 5.10, Claim 6.2, Fact 6.5 |
| E. Bierstone, P. Milman, *Semianalytic and subanalytic sets*, Publ. IHES 67 (1988), 5–42 | numdam, свободно | Thm 6.1, Lemma 6.3 (аналитические кривые) |
| M. Edmundo, arXiv:math/0012051 (обзор) | arXiv | только перечни; **теорем с формулировками нет** |

Не открывались (платные или недоступные): Denef–van den Dries, Ann. Math. 128 (1988); van den Dries–Miller,
Duke 84 (1996) (Project Euclid закрыт защитой от ботов, свободной копии не нашлось; на странице
Миллера лишь список исправлений `geofix.pdf`); книга van den Dries, *Tame topology and o-minimal
structures*, CUP 1998 (LMS 248); Wall, *Singular points of plane curves*; Brieskorn–Knörrer.
Номера теорем книги [vdD98] поэтому **не сверены**. Подтверждены только названия глав
(Cambridge Core, оглавление): гл. 3 «Cell Decomposition» (§1 — теорема о монотонности, с. 43),
гл. 6 «Point-set Topology in O-minimal Structures», гл. 7 «Smoothness». Номера разделов внутри глав
и ссылка «гл. 6, §1» на определимый выбор — по памяти и по строке чужого списка литературы (не
сверено).

Итог для заметки: вместо ссылок на [vdD98] с номерами надёжнее ссылаться на Coste и Starchenko
(номера ниже).

---

## (F1) о-минимальность $\mathbb R_{\rm an}$ и определимость

**Первоисточник.** [Литература: van den Dries 1986, Bull. AMS 15, с. 190–191, сверено с полным текстом]:

- Определения (i)–(iv) полуаналитических и субаналитических множеств; факты (1)–(4):
  (1) «The subanalytic subsets of R and R² are exactly the semianalytic subsets of R and R²» (Лоясевич);
  (3) ограниченные субаналитические множества — проекции ограниченных полуаналитических;
  (4) «The complement in R^m of a subanalytic set in R^m is subanalytic» (Габриэлов 1968).
- Определение: $X\subset\mathbb R^m$ *finitely subanalytic*, если его образ при
  $(x_i)\mapsto(x_i/\sqrt{1+x_i^2})$ субаналитичен.
- **THEOREM.** «Let $FS_m$ be the class of finitely subanalytic sets in $\mathbb R^m$. Then
  $(FS_m)_{m\in\mathbb N}$ is an O-minimal Tarski system on $\mathbb R$.»
  (о-минимальность: «the only sets in $\mathscr S_1$ are the subsets of $\mathbb R$ with only finitely many
  connected components».) Там же: структура поля с предикатами для всех ограниченных полуаналитических
  множеств модельно полна, и определимые в ней множества — ровно finitely subanalytic.

**Связь с $\mathbb R_{\rm an}$.** Определимость в $\mathbb R_{\rm an}$ (поле плюс ограничения на $[-1,1]^m$
аналитических функций, аналитичных в окрестности куба) совпадает с finitely subanalytic. Это стандартный
факт [Литература: Starchenko, Notes on o-minimality, §6.1, Claim 6.2 (оставлено как упражнение); Edmundo,
п. (4) на с. 5–6 — по обзору]. Строгое доказательство эквивалентности в 1986 г. не приведено (там
структура с предикатами, не с функциями); оно в Denef–van den Dries 1988 и/или vdD–Miller 1996
(не сверено). Для заметки это не критично: используются лишь о-минимальность и замкнутость
относительно формул первого порядка.

**Сравнение с §0.**

- Определение $\mathbb R_{\rm an}$ в §0 совпадает с Edmundo и Starchenko. Надо добавить: $U$ лежит в
  кубе $[-1,1]^2$ после масштабирования ($U(\rho_0 x)$ с $\rho_0\le1$ или замена переменных; умножение
  определимо).
- «Определимые множества — в точности глобально субаналитические»: совпадает (Starchenko, Claim 6.2).
- **Неточность атрибуции.** Теорема «$\mathbb R_{\rm an}$ о-минимальна» принадлежит van den Dries 1986
  (на основе теоремов Лоясевича и Габриэлова); Denef–van den Dries 1988 дают модельно-теоретическое
  доказательство, модельную полноту и (после добавления $1/x$) исключение кванторов
  (Edmundo, п. (4), (7): «model complete and o-minimal as remarked by van den Dries [D1]»; DD «give a proof of
  model completeness and o-minimality of Ran»). Предлагаю писать: «van den Dries 1986 (на основе
  Лоясевича и Габриэлова 1968); Denef–van den Dries 1988».
- Определимость $\cos,\sin$ только на **ограниченных** отрезках: верна (ограничение синуса на $[-1,1]$
  есть базисная функция; на $[-A,A]$ через формулы кратных углов от $\sin(\alpha/N)$,
  $\cos(\alpha/N)$). Синус на всей $\mathbb R$ не определим (van den Dries 1986, с. 189: «it couldn't
  possibly contain the sine function on all of R»). Это согласуется с оговоркой «на ограниченных
  множествах» в §0.
- Формулы первого порядка ($\sup$, $\inf$, пределы, частные производные там, где существуют):
  корректно. $\sup$ непустого определимого множества существует в $\mathbb R\cup\{\pm\infty\}$ и
  определим; множество точек дифференцируемости определимо, производная определима [Литература:
  Starchenko, текст перед Thm 5.2; Coste, Lemma 6.1 — определимость $f'_{\pm}$].

Вердикт: **совпадает; поправить атрибуцию и сослаться на Starchenko Claim 6.2 / Bull. AMS 1986, THEOREM.**
Степень сверки: THEOREM о о-минимальности — полный текст; эквивалентность с функциональным
определением $\mathbb R_{\rm an}$ — вторично (Starchenko, Edmundo).

## (F2) Теорема о монотонности

**Формулировка.** [Литература: Coste, Thm 2.1, сверено с OCR-текстом]: «Let $f:(a,b)\to\mathbb R$ be a
definable function. There exists a finite subdivision $a=a_0<a_1<\dots<a_k=b$ such that, on each interval
$(a_i,a_{i+1})$, $f$ is continuous and either constant or strictly monotone.» Тот же текст:
[Литература: Starchenko, Thm 2.6; van den Dries 1986, «PIECEWISE MONOTONICITY», с. 191–192, для любой
о-минимальной системы Тарского].

**Следствия из §0.**

- Предел в $[-\infty,+\infty]$: [Литература: Coste, Exercise 2.3] «$\lim_{x\to a+}f(x)$ and $\lim_{x\to b-}f(x)$
  exist in $\mathbb R\cup\{\pm\infty\}$». Совпадает.
- Постоянство знака, непрерывность и монотонность на $(0,\varepsilon')$: берём $\varepsilon'=a_1$. Совпадает.
- $f\in C^1(0,\varepsilon')$: [Литература: Coste, Thm 6.4 и Cor. 6.5, $\mathbb R$-структура на поле
  вещественных чисел]. Thm 6.4: «Let $f:I\to\mathbb R$ be a definable continuous function on an open interval $I$.
  Then, for all but finitely many points in $I$, we have $f'_l(x)=f'_r(x)\in\mathbb R$»; Cor. 6.5: «For all
  $k\in\mathbb N$, there is a finite subset $M(k)$ of $I$ such that $f$ is of class $C^k$ on $I\setminus M(k)$»
  (без предположения непрерывности: по монотонности сначала выделяется непрерывность). Также Starchenko,
  Thm 5.2. Совпадает; ссылка на [vdD98, гл. 7, §2] не сверена, замените на Coste 6.4–6.5.
- «Если $f$ непрерывна на интервале, а $f^{-1}(t)$ бесконечно, то $f$ постоянна на подинтервале»:
  следует из Thm 2.1 (строго монотонные куски имеют не более одного прообраза). Верно.

Вердикт: **совпадает.** Степень сверки: полный текст (Coste через OCR, Starchenko).
Номер в книге ([vdD98] гл. 3, §1) — только по оглавлению Cambridge Core (гл. 3, §1, с. 43); номер
«(1.2)» не сверен.

## (F3) Определимый выбор

**Формулировка.** [Литература: Coste, Thm 3.1 (Definable Choice), OCR]: «Let $A$ be a definable subset of
$\mathbb R^m\times\mathbb R^n$. Denote by $p:\mathbb R^m\times\mathbb R^n\to\mathbb R^m$ the projection on the
first $m$ coordinates. There is a definable function $f:p(A)\to\mathbb R^n$ such that, for every
$x\in p(A)$, $(x,f(x))$ belongs to $A$.» Starchenko Thm 4.1 даёт более сильную версию (согласованную
по эквивалентным слоям) для о-минимального расширения упорядоченной группы.

**Сравнение с §0.** В §0 параметр записан первым, $A\subset\mathbb R^{1+k}$, слои над интервалом $I$
непусты, выбирается $f:I\to\mathbb R^k$. Это частный случай Thm 3.1 ($m=1$, $p(A)\supset I$,
ограничение на $I$). Совпадает.

Вердикт: **совпадает.** Полный текст (Coste, Starchenko). Заодно: Curve Selection [Coste, Thm 3.2; Starchenko
Cor. 4.3] — это то, что нужно для переноса на $n\ge3$ вместо (F6).

## (F4) $C^1$-клеточное разложение

**Формулировка.** [Литература: Starchenko, Thm 5.10 (Smooth Cell Decomposition), $r\ge1$]: «(1) For any
definable $A_1,\dots,A_k\subseteq\mathbb R^n$ there is a $C^r$-cell decomposition of $\mathbb R^n$ compatible
with each $A_i$. (2) For any definable function $f:A\to\mathbb R$, $A\subseteq\mathbb R^n$ there is a $C^r$
cell decomposition of $\mathbb R^n$ compatible with $A$ such that $f|_C$ is $C^r$ on each cell $C\subseteq A$.»
Там же Def. 5.8: «$f$ is $C^r$ on $A$ if there is an open $U\subseteq\mathbb R^n$ and a definable
$C^r$-map $F:U\to\mathbb R^m$ extending $f$»; Def. 5.9: клетка — $C^r$-клетка, если все функции в её
построении класса $C^r$. [Литература: Coste, Thm 6.6 ($C^k$CDCD) и Thm 6.7 (PC$^k$)]: у Coste
«piecewise $C^k$» сформулировано как разбиение на $C^k$-подмногообразия, но доказательство
(одновременная индукция) даёт вариант Starchenko. Условие «o-минимальное расширение поля
$\mathbb R$»: у Coste выполнено; $\mathbb R_{\rm an}$ — такое.

**Сравнение с §0.** Совпадает: клетки в $\mathbb R^2$ — точки, графики $C^1$-функций над интервалами и
вертикальные интервалы, открытые полосы и области («открытые подмножества» — склейка
под/над графиками). «Согласованное с $A$» = «compatible with $A$». Уточнение: «$f$ класса $C^1$ на
клетке» в [Starchenko] означает продолжимость до $C^1$-отображения на открытое множество; для
вашего использования (дифференцируемость вдоль дуг) хватает и слабого смысла.

Вердикт: **совпадает.** Степень сверки: полный текст (Starchenko, Thm 5.10; Coste 6.6–6.7). Ссылка
[vdD98, гл. 7, §3] не сверена (гл. 7 «Smoothness» — по оглавлению).

## (F5) Полиномиальная ограниченность $\mathbb R_{\rm an}$

**Первоисточник.** [Литература: van den Dries 1986, Bull. AMS 15, с. 192, сверено с полным текстом]:

> POLYNOMIAL GROWTH. Given a finitely subanalytic function $f:(0,\infty)\to\mathbb R$, there is
> $d\in\mathbb N$ and $a>0$ such that $|f(t)|\le t^d$ for $t>a$.

Доказательство там же (набросок, но полный по идее): подстановка $t=1/x$, получаем $g:(0,\varepsilon)\to\mathbb R$
с субаналитическим графом и $g(x)\to0$; по (1) граф полуаналитичен в $(0,0)$; ненулевой ряд
$F(X,Y)=\sum a_{mn}X^mY^n$ с $F(x,g(x))=0$; подготовка Вейерштрасса; из непрерывности $g$ — сходящееся
разложение Пюизё $c_1x^{1/k}+c_2x^{2/k}+\dots$ (подробнее ниже). Сказано: $f(t)\sim ct^r$ при $t\to\infty$.
Тот же факт: Starchenko Fact 6.5 (без доказательства): «The structure $\mathbb R_{\rm an}$ IS polynomially
bounded», определение 6.3: $|f(x)|<x^N$ при больших $x$.

**Сравнение с §0.** В §0: «если $g:(0,\varepsilon)\to(0,\infty)$ определима, то $g(r)\ge r^N$ при некотором
$N$ и малых $r$». Это следует из роста на $+\infty$ применением к $f(t):=1/g(1/t)$ при $t>1/\varepsilon$
(и $f:=0$ иначе; определима, значит finitely subanalytic): $1/g(1/t)\le t^d$ при $t>a$, то есть
$g(r)\ge r^d$ при $r<1/a$. Верно. В §0 атрибуция «van den Dries–Miller, Duke 1996» не сверена;
первоисточник — Bull. AMS 1986, с. 192. Формулировку в §0 стоит записать так: «[van den Dries 1986,
с. 192, POLYNOMIAL GROWTH, с заменой $t=1/r$ и $f=1/g$]».

Вердикт: **верно, при указанном переводе с $+\infty$ на $0^+$.** Полный текст (Bull. AMS 1986).

### Разложение Пюизё одноместной определимой функции

**Верно ли, что функция $f:(0,\varepsilon)\to\mathbb R$, определимая в $\mathbb R_{\rm an}$, на $(0,\delta)$ раскладывается
в сходящийся ряд Пюизё?** Да; точная ссылка и вывод:

- [Литература: van den Dries 1986, с. 192, доказательство POLYNOMIAL GROWTH, сверено]: для $g:(0,\varepsilon)\to\mathbb R$
  с субаналитическим графом (то есть для ограниченной определимой функции) и $g(x)\to0$ при $x\to0$,
  $g\not\equiv0$ около $0$: «by Weierstrass preparation ... $F=Y^k+a_1(X)Y^{k-1}+\dots+a_k(X)$ ...
  continuity of $g$ near 0 gives us a Puiseux expansion (with real coefficients)
  $c_1x^{1/k}+c_2x^{2/k}+\dots$ converging to $g(x)$ for small positive $x$.»
- Общий случай: по (F2) $L=\lim_{x\to0}f$ существует в $[-\infty,\infty]$. Если $L\in\mathbb R$, применить к
  $g=f-L$ (граф ограниченной определимой функции — ограниченное определимое, значит субаналитическое
  в $\mathbb R^2$ множество; по факту (1) — полуаналитическое). Если $L=\pm\infty$ — к $1/f$ (определима,
  $\to0$) и инвертировать ряд; получается ряд Пюизё–Лорана $x^{-p/k}\sum_{i\ge0}c_ix^{i/k}$.
  Если $f\equiv\mathrm{const}$ или $f\equiv L$ около $0$ — тривиально.
- Вторичное подтверждение: arXiv:0705.1851 («The Riemann mapping theorem for semianalytic domains and o-minimality»; ссылка в тексте на
  [vdD86, p.192]) повторяет: «A bounded semianalytic function on the positive real line is given
  locally at 0 by a convergent Puiseux series $\sum a_nt^{n/d}$ for some $d\in\mathbb N$ (see for
  example [7, p.192])» и «subanalytic functions in one variable are given by such series». Сверено только
  как цитата чужой статьи.
- Оговорка. Доказательство Пюизё у van den Dries занимает три строки; шаг «график $g$ полуаналитичен в
  $(0,0)$ $\Rightarrow$ существует $F\ne0$ с $F(x,g(x))=0$» (используется, что множество, заданное
  только неравенствами, не может лежать в графике) и шаг «непрерывная $g$ совпадает с одной из ветвей
  Пюизё на малом интервале» опущены как стандартные. Оба верны; оформленное доказательство в
  литературе есть в vdD–Miller Duke 1996 и van den Dries–Macintyre–Marker, Ann. Math. 140 (1994)
  (не открывались, **не сверено**).
- Оговорка 2. Это только для $\mathbb R_{\rm an}$ (аналитические данные). Для $\mathbb R_{\rm an}^*$ (сходящиеся
  обобщённые степенные ряды, van den Dries–Speissegger, Trans. AMS 350 (1998)) разложение другого типа
  (вещественные показатели).

**Где используется в заметке.**

- Само разложение Пюизё одноместной функции **нигде не используется напрямую**; оно стоит за (F5).
- (F5) используется ровно один раз: Лемма 6, шаг 6 (стр. ~341), чтобы исключить $\beta-\alpha=O(r^M)$
  для всех $M$ (формула (7')); и в замечании к концу §4, где упомянуто «оценка $cr^d$ из (F5) и
  разложения Пюизё функции $\varepsilon_0$» (стр. ~691): там оно необязательно, «Количественная оценка не нужна».
- (F2) и (F6) от Пюизё одной переменной не зависят.

## (F6) Ньютон–Пюизё для вещественных аналитических кривых

**Что прочитано.** Wall, гл. 2, и Brieskorn–Knörrer, §8.3 (по заметке) — платные, **не открывались**,
точные номера не проверены. Свободный источник для близкого утверждения:
[Литература: Bierstone–Milman 1988, Lemma 6.3 (1), сверено]: «Let $\mathcal M$ be a real analytic manifold.
(1) Let $A\subset\mathcal M$ be a semianalytic subset of dimension 1. Let $a\in A$. Assume $A-\{a\}$ is locally
connected at $a$. Then there exist $\varepsilon>0$ and a real analytic mapping
$\gamma:(-\varepsilon,\varepsilon)\to\mathcal M$ such that $\gamma(0)=a$ and $\gamma((0,\varepsilon))$ is a
neighbourhood of $a$ in $A-\{a\}$.» (Доказательство там: «immediate from Theorem 0.1 (Uniformization).
(Alternatively, it can be proved by induction on dim $\mathcal M$, using Puiseux's theorem.)»)
Кроме того [там же, Thm 6.1]: «If $\dim X\le1$, $X$ is semianalytic; if $\dim\mathcal M\le2$, $X$ is
semianalytic.»

**Сравнение с §0.** Формулировка (F6) в заметке верна, но содержит больше, чем даёт Lemma 6.3. Разбор:

1. $\{F=0\}$ имеет размерность $\le1$ при $F\not\equiv0$, и в проколотом круге малого радиуса это
   конечное объединение полуветвей (после поворота $F(0,y)=y^k\cdot\text{unit}$, затем подготовка
   Вейерштрасса и Ньютон–Пюизё над $\mathbb C$; вещественные корни при $x>0$ — те ветви с вещественными
   коэффициентами в $t=x^{1/m}$). Совпадает со стандартным изложением; не сверено по Wall/B–K.
2. Параметр $r=|\gamma|$: $\frac d{dt}|\gamma|^2>0$ при малых $t>0$ (для ветви $y\sim cx^{\alpha}$ имеем $2x+2yy'>0$
   при $\alpha>0$). Верно. Но при $m>1$ переход $t\mapsto r$ даёт $\gamma(r)$ аналитическую **на $(0,r_0)$**
   и рядом Пюизё по $r^{1/m}$ в нуле — а не аналитическую в нуле. В заметке так и сказано
   («аналитична на $(0,r_0)$»), корректно.
3. Утверждения $\gamma'\ne0$, существование предела $\gamma_j(r)/r$ (касательное направление), замкнутость
   $\Gamma_j$ в $B_{r_0}\setminus0$, дизъюнктность различных $\Gamma_j$ — следуют из конечности числа
   ветвей и разложений; для замкнутости и дизъюнктности нужно, чтобы множество $\{r:\gamma_i(r)=\gamma_j(r)\}$
   не накапливалось в 0: следует из рядов Пюизё (различные ветви различаются в старшем члене или
   совпадают тождественно), но **этот шаг в заметке только заявлен** («Различные ветви не пересекаются
   вне нуля»), и в Lemma 6.3 его нет.
4. Изолированные нули $F$ в проколотом круге невозможны (оба вида: нет вещественных корней с
   комплексными коэффициентами, как выше).

Вердикт: **формулировка верна, но не сверена по первоисточнику; остаются шаги 1 и 3, которые следует либо
сослаться (Milnor, *Singular points of complex hypersurfaces*, §8, или Bochnak–Coste–Roy, гл. 8 — не
открывались), либо вывести из Lemma 6.3 + конечности (В–М Thm 6.1 даёт полуаналитичность множества
$\{F=0\}$ в $\mathbb R^2$)**. Для $n\ge3$ (F6) заменяется Curve Selection (Coste, Thm 3.2; Starchenko,
Cor. 4.3; Bierstone–Milman, Lemma 6.3) — но тогда «одна дуга на окружности» и «конечное число рогов»
(Лемма 1) требуют отдельной о-минимальной аргументации (рог = компонента связности определимого
множества $\{U<0\}\cap B_\rho$; конечность числа компонент — [Литература: vdD 1986, с. 190–191, факт (2)/(3) и
THEOREM; Coste, §3.2 «Connected components»]).

---

## Сводная таблица

| Факт | Соответствие §0 | Степень сверки | Что поправить |
|---|---|---|---|
| F1 | совпадает | THEOREM vdD 1986 — полный текст; эквивалентность с функциональным $\mathbb R_{\rm an}$ — вторично | атрибуция о-минимальности (vdD 1986, затем Denef–vdD 1988); ссылка на Starchenko Claim 6.2; $\rho_0\le1$ |
| F2 | совпадает | полный текст (Coste 2.1, 6.4, 6.5, Ex. 2.3; Starchenko 2.6, 5.2) | заменить [vdD98 гл. 3, §1; гл. 7, §2] на Coste/Starchenko |
| F3 | совпадает | полный текст (Coste 3.1; Starchenko 4.1) | ссылка Coste 3.1 вместо [vdD98 гл. 6] |
| F4 | совпадает | полный текст (Starchenko 5.10; Coste 6.6–6.7) | ссылка Starchenko 5.10 вместо [vdD98 гл. 7, §3] |
| F5 | верно с переводом $+\infty\to0^+$, $f=1/g$ | полный текст (vdD 1986, с. 192) | атрибуция: vdD 1986 с. 192, а не vdD–Miller 1996 |
| F6 | верно, не сверено | не сверено (Wall, B–K платны); близкое утверждение — B–M Lemma 6.3 (1) | дизъюнктность ветвей, замкнутость $\Gamma_j$ — дать вывод или ссылку |

## Предложения по правкам

В заметку (§0 и «Пробелы»; сам файл не правлю, он чужой):

1. Заменить «сверено только по Edmundo»: Edmundo вообще не содержит формулировок теорем и номеров
   (проверено, прочитан весь текст); для F1–F5 заменить цитаты на Starchenko / Coste / vdD 1986 (номера выше).
2. Нумерацию [vdD98] не использовать, пока не открыта книга. Подтверждены только названия глав.
3. F5: цитировать vdD 1986, с. 192 (POLYNOMIAL GROWTH, там же и разложение Пюизё), сделать явным переход
   $f(t)=1/g(1/t)$.
4. F1: поправить атрибуцию; добавить оговорку об ограничении на $[-1,1]^2$.
5. F6: дополнить доказательством (или точной ссылкой) дизъюнктности и замкнутости ветвей.

В `problem/KNOWN_RESULTS.md` (предложение): в раздел о-минимальных фактов добавить ссылки «van den Dries
1986, Bull. AMS 15, 189–193 (открытый доступ): THEOREM о-минимальности, PIECEWISE MONOTONICITY,
POLYNOMIAL GROWTH + разложение Пюизё»; «Coste, *Introduction to o-minimal geometry*, Thm 2.1, 3.1, 3.2, 6.4–6.7»;
«Starchenko, *Notes on o-minimality*, Thm 2.6, 4.1, 5.10». Что-либо большее по этим фактам сейчас не
подтверждено.

## Пробелы этой сверки

- Не открыты Denef–van den Dries 1988, vdD–Miller 1996, книга vdD 1998, Wall, Brieskorn–Knörrer.
- Coste читался через OCR; номера теорем сверены, дословность — с точностью до ошибок распознавания.
- Строгое доказательство «определимо в $\mathbb R_{\rm an}$ $\iff$ finitely subanalytic» не прочитано.
- Подробное доказательство разложения Пюизё для одной переменной в литературе (кроме набросков vdD 1986)
  не открывалось.
- Вторая запись о Пюизё в arXiv:0705.1851 использована только как косвенное подтверждение.
