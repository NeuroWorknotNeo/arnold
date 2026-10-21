# Гипотеза Ляпунова о струях при n >= 3: точное состояние (21.10.2026)

Автор: агент `literature`. Правки в `problem/KNOWN_RESULTS.md` не вносились: предложения в конце.

Что открывалось полностью (текст читался):

- Freire Jr., Garcia, Tal, препринт IME-USP RT-MAP-0801, январь 2008, 16 с. Это техотчёт с тем же названием, что и статья JDE 245 (2008) 490-504. Скачан со страницы репозитория USP: https://repositorio.usp.br/item/001639552 (прямая ссылка https://repositorio.usp.br/directbitstream/f97f8fae-adcb-4f98-acc2-090f737889af/1639552.pdf). Страницу ScienceDirect открыть не удалось (403), поэтому журнальную версию не сверяли. Аннотация из поисковой выдачи совпадает с аннотацией отчёта.
- Alva Morales, Garcia, arXiv:1508.07427v2 (QTDS 16 (2017) 371-389).
- Garcia, Tal, препринт 2001 (`/home/claudeagent/papers/garcia-tal-2001.pdf`, текст OCR с ошибками).
- Burgos–Paternain, arXiv:2208.01139, введение; Burgos, arXiv:2506.19135, введение.
- Kozyakin, arXiv:0907.0571, Thm 1.1 (вторичный источник по критерию Kuo).

Не открывались: JDE-версия FGT; Barone-Netto 1984 (Proc. AMS 92); Barone-Netto–Gorni–Zampieri 1996 (NoDEA 3); Garcia 1992 (RT-USP «k-decidibilidade e estabilidade de Liapunov»); Garcia–Tal 2005 (JDE 213); Bortolatto–Garcia–Tal 2011 (QTDS 10); Moauro–Negrini 1989; Maffei–Moauro–Negrini 1991; Taliaferro 1990; Alva Morales 2016 (Selecciones Matemáticas 3(2) 67-70, 4 стр.; по аннотации тот же класс результатов, текст недоступен); оригиналы Kuo, Kuiper, Bochnak–Łojasiewicz.

---

## 1. Определения

**Струя в точке** [Литература: FGT08, §2; AG17, Def. 1]. Функция $f:\Omega\to\mathbb R$ имеет *точечную струю порядка $k$* в нуле, если существует многочлен $P$ степени $\le k$ с $\lim_{x\to0}(f(x)-P(x))/\|x\|^k=0$; тогда $j^kf:=P$. Он единствен. Функция $f$ не обязана быть непрерывной вне нуля, глаже или вообще регулярной.

**Струя показывает отсутствие минимума** [Литература: FGT08, §2, дословно]: «We say that $j^kf$ shows that $f$ does not have minimum at the origin (or, equivalently, $j^kf$ shows that the origin is not a minimum for $f$) if $f$ is a function which has punctual jet of order $k$ at the origin and for every function $g$ such that $j^kf=j^kg$ we have that $g$ does not have a minimum (not even strictly weak) at the origin.» AG17, Def. 2 говорит то же («even a weak minimum»). Здесь «strictly weak» у FGT, видимо, опечатка или неточность формулировки; смысл: у $g$ нет даже нестрогого локального минимума в нуле.

Замечания [Доказано, элементарно]:

- Класс $g$ в определении широкий: достаточно существования точечной струи. Поэтому критерии $C^0$-достаточности (Kuo и др.), которые работают в классе $C^r$ или $C^{r+1}$, определение не покрывают напрямую. Но для аналитического $f$ нужное утверждение выводится прямо (п. 4).
- Для изолированной критической точки «не минимум» значит «нет локального минимума вообще». Нестрогий минимум в изолированной критической точке невозможен: другие точки того же уровня около нуля тоже были бы минимумами и, значит, критическими.

## 2. Результаты

### 2.1. Lyapunov / гессиан [Литература: AG17, введение, и FGT08; не сверено с первоисточником (Lyapunov 1897)]

Если гессиан $j^2\Pi$ показывает отсутствие минимума (то есть имеет отрицательное собственное значение), равновесие неустойчиво. Lyapunov работал в аналитическом классе; точная гладкость в его формулировке не проверена. Эту формулировку считать надёжной можно (она стандартна), но гладкость и условия на кинетику — по Lyapunov и Chetaev не сверены.

### 2.2. Garcia–Tal 2003, $n=2$ [Литература: препринт 2001, §1-2; JDE-версия не сверена]

Условия: $n=2$; $\pi\in C^2$, $\pi=P+R$, $P=j^k\pi$, $R=o(|q|^k)$, существует $j^{k-1}\nabla\pi$; $P$ показывает отсутствие минимума; $T$ — положительно определённая квадратичная форма по скоростям класса $C^2$. Вывод: траектория, асимптотическая к началу (в препринте — при $t\to-\infty$ по FGT08 и «asymptotic trajectory»), следовательно неустойчивость по Ляпунову. Тотальная неустойчивость не выводится. Препринт 2001 предполагает также, что $k$ — минимальный порядок, при котором струя показывает отсутствие минимума (это только упрощение).

### 2.3. Freire–Garcia–Tal 2008, любое $n$ [Литература: FGT08 (техотчёт RT-MAP-0801 января 2008), аннотация и Theorem A, с. 14; журнальная версия не сверена]

Аннотация (дословно): «In this work we show that, if $\mathcal L$ is a natural lagrangian system such that the $k$-jet of the potential energy ensures it does not have a minimum at the equilibrium and such that its hessian has rank at least $n-2$, then there is an asymptotic trajectory to the associated equilibrium point and so the equilibrium is unstable. This applies, in particular, to analytic potentials with a saddle point and a hessian with at most 2 null eigenvalues.»

**Theorem A** (дословно, с. 14, текст сверен с изображением страницы): «Consider the lagrangian system given by equation (1) and assume that $\mathcal L=T-\pi$ is such that $0$ is an equilibrium point, the $k$-jet of $\pi$ shows that the origin is not a minimum for $\pi$, that $\mathcal L$ is of class $C^{k+\lfloor\frac{k-3}{2}\rfloor+3}$, that $j^2\pi(0,0)$ is a positive semi-definite quadratic form of rank at least $n-2$ and that $T$ is a positive definite quadratic form in $\dot q$ for every $q$. Then there is a trajectory $\phi(t)$ such that $(\phi(t),\dot\phi(t))\to(0,0)$ as $t\to-\infty$.»

Замечания:

- Гессиан здесь положительно полуопределён с рангом $\ge n-2$ (в аннотации «rank at least $n-2$» без полуопределённости; случай гессиана с отрицательным значением покрывается Lyapunov). Кинетика зависит от $q$ (класс $C^{k+\lfloor(k-3)/2\rfloor+3}$ включает $T$); в доказательстве координаты меняются «subtle change of spatial coordinates», чтобы привести $T$ к виду $I+h$.
- Схема доказательства (из текста): расщепляющая лемма (splitting lemma, ссылка на Garcia–Tal 2003) приводит $\pi$ к виду $U(q_1..q_N)+\pi_2(q_{N+1}..q_n)$, $U\ge0$, при $n-N\le2$; случай $n-N=1$ и однородной $j^k\pi_2$ с седловой точкой даёт Maffei–Moauro–Negrini (1991); случай $n-N=2$ с неоднородной $j^k\pi_2$ или однородной седловой — Theorem 2 (теорема о неустойчивости для лагранжианов класса $\mathcal H_1$, модификация конструкции Garcia–Tal 2003).
- При аналитическом $\pi$ гладкость условия выполнена, а струя, показывающая отсутствие минимума, существует (п. 4). Поэтому для аналитических $U$ с гессианом $\ge0$ и $\dim\ker\le2$ неустойчивость доказана — это FGT08 на основе Garcia–Tal 2003. Дальнейшее (замечание главного агента) — [Эскиз].
- FGT08, введение: «In the general case of $n$ degrees of freedom, we have only partial results in the direction of this conjecture.» О Palamodov: «In the context of analytic lagrangians, in [8] it is shown that if the lagrangian is analytic and the potential energy does not have a minimum in the origin, then the origin is unstable. In this paper only the instability is proved, and the question on whether an asymptotic trajectory ... remains open.» Здесь [8] — Palamodov 1995; сегодня его доказательство считается неполным (Burgos 2021 и далее), поэтому эту ссылку не использовать как довод.
- При $n=3$ условие ранга $\ge n-2$ означает ранг гессиана $\ge1$.

### 2.4. Maffei–Moauro–Negrini, Moauro–Negrini, Taliaferro [Литература: цитата в FGT08, введение; первоисточники не открывались]

Theorem (Maffei, Moauro, Negrini), в пересказе FGT08: лагранжиан $\mathcal L=T-\pi$ в $\mathbb R^{2(m+n)}$, $q=(u,v)$; существуют целое $k\ge3$ и $\omega_1..\omega_m$ такие, что (1) $\pi(u,v)=\frac12\langle l(u,v)u,u\rangle+\pi_{[k]}(u,v)+R(u,v)$, $l(0,0)=\mathrm{diag}(\omega_1^2,\dots)$, $\pi_{[k]}$ однородна степени $k$, $R=O(\|(u,v)\|^{k+1})$, $\min\{\pi_{[k]}(0,v):\|v\|=1\}=-1$; (2) $\mathcal L$ — класс $C^{k+3+\lfloor(k-3)/2\rfloor}$ (в OCR текст неразборчив, точная гладкость не проверена). Вывод: траектория $\phi(t)\to0$ при $t\to-\infty$. Условия на кинетику в пересказе FGT08 не видны: не сверено.

FGT08: если струя, показывающая отсутствие минимума, однородна, то в [Moauro–Negrini 1989] и независимо в [Taliaferro 1990] доказана неустойчивость «with some additional hypothesis on the regularity of the lagrangian». Подробности не сверены.

### 2.5. Alva Morales–Garcia 2017 [Литература: arXiv:1508.07427v2, прочитан полностью]

Условия: $\Pi\in C^2$, $T=\frac12\langle B(q)p,p\rangle$, $B$ симметрична положительно определена, $n$ любое; $\Pi$ имеет $s$-струю, $j^1\Pi=0$. Обозначения: $A_s=(j^s\Pi)^{-1}(-\infty,0)$, $C_s=(R^s_\Pi)^{-1}(-\infty,0)$, $R^s_\Pi(q)=\langle\nabla j^s\Pi(q),q\rangle$.

Класс $\mathcal H$ (дословно): (H1) $j^\ell\Pi(q)\ge0$ в некоторой окрестности нуля при $\ell\le s-1$; (H2) $j^s\Pi$ показывает, что у $\Pi$ нет минимума в нуле; (H3) существуют $\varepsilon>0$, $B_\varepsilon\subset\Omega$ и связная компонента $A^*$ множества $A_s$ такие, что $(A^*\setminus\{0\})\cap B_\varepsilon\subset C_s^\circ\cap B_\varepsilon$.

Theorem 1: если $\Pi$ класса $\mathcal H$, то выполнено строгое условие Chetaev («has the strict Cetaev's condition»: для некоторой компоненты $A$ множества $\Pi^{-1}(-\infty,0)$ имеем $R_\Pi<0$ на $(A\setminus0)\cap B_\varepsilon$). Proposition 8: строгое условие Chetaev ($C^2$-потенциал, критическая точка в нуле) даёт асимптотическое движение к нулю (при этом кинетика $T$ класса $C^2$ по виду из доказательства). Следствие: класс $\mathcal H$ даёт асимптотическую траекторию и неустойчивость.

Пример 1 (с. 18-19): $\pi=f+x^{14}$, $f(x,y)=\frac83y^6-3y^4x^4+\frac9{10}y^2x^8-\frac1{12}x^{12}-y^{12}$ (дроби восстановлены по $j^{11}\pi$ и OCR-тексту): (H2), (H3) при $s=12$ выполнены, но $\pi$ не потенциал Chetaev. Поэтому (H1) нельзя просто выбросить.

**Важная проверка (мой расчёт, [Доказано], 3 строки).** Для $U=x^4+y^4-z^6$: $j^\ell U\ge0$ при $\ell\le5$, $j^6U=U$ показывает отсутствие минимума (на оси $z$ значение $-z^6$), (H3) выполнено: на множестве $A_6=\{x^4+y^4<z^6\}$ радиальная производная $R=4(x^4+y^4)-6z^6<-2z^6<0$. Значит, $U\in\mathcal H$, и для него условие Chetaev выполняется прямо: компонента $\{U<0\}$ вблизи оси $z$ имеет $\langle\nabla U,q\rangle<0$. Поэтому неустойчивость $x^4+y^4-z^6$ следует из Chetaev (1952), а также из AG17. Замечание в `problem/KNOWN_RESULTS.md` («Не покрывает $x^4+y^4-z^6$») по моей проверке неверно; BP22 говорит о результатах, использующих *первую ненулевую струю* («none of the mentioned results apply», дословно в BP22, стр. 4-5), а AG17 использует струю $j^6U$, не первую. Прошу главного агента перепроверить.

### 2.6. Burgos и соавторы (о состоянии вопроса) [Литература: arXiv:2208.01139, введение; arXiv:2506.19135, введение; arXiv:1906.11962, аннотация]

- BP22: «Starting from A. M. Lyapunov [Ly] and continuing with [Ch], [Ha], [HM], [Ko2], [Ko3], [Ku], [KP], [MN], [So], [Ta2], [Ta3], many partial results have been given towards the solution of the Arnold's problem and their common feature is that the Lyapunov instability criteria involves the lack of a local minimum at the origin of the first nonzero jet of the potential.» FGT и AG17 в этом списке не названы.
- Burgos 2025 (arXiv:2506.19135, §1): «In dimension greater than two, the problem remains open and only partial results are known. Most of these partial results prove the existence of some asymptotic orbit assuming some non-degeneracy condition on the first non-zero jet of the potential.»
- BMP21 (arXiv:1906.11962v3, аннотация): «In contrast to the known results in this direction, which hold for potentials satisfying hypotheses on the first non-zero jet, this new result covers several real analytic cases that the previous do not.»

### 2.7. Другие работы

- Bortolatto–Garcia–Tal, «Kinetic energy and the stable set», QTDS 10 (2011) 1-10: по подписи в BP22 изучает влияние кинетики в аналитическом классе; про струи не сообщается. Не открывалась.
- Garcia–Tal 2005 (JDE 213, 410-417): пример влияния кинетики в $C^\infty$; к струям не относится.
- Поиск по цитированиям GT03 и AG17 новых работ по гипотезе о струях при $n\ge3$ за 2017-2026 не дал: ни в BP22, ни в Burgos 2025, ни в поисковых выдачах нет результатов, продвигающих её дальше FGT08 и AG17. Поиск неполный (zbMATH Open и Google Scholar по цитированиям не просматривались).
- Работа JDE 2018 «Instability of equilibrium solutions of Hamiltonian systems with $n$-degrees of freedom under the existence of a single resonance and an invariant ray» (sciencedirect S0022039618303863) — к теме не относится (резонансы гамильтониана с ненулевой линейной частью); не открывалась.
- Barone-Netto, «Jet-detectable extrema», Proc. AMS 92:4 (1984): определение струй и $k$-decidability; не открывалась. Страница Garcia «Finite Decidability» (ime.usp.br/~mane/kdcd.html) не загрузилась. Garcia 1992, RT-USP: однородный случай через $k$-decidability (по AG17).

## 3. Вывод для $n=3$: что покрыто в терминах гессиана $H=j^2U(0)$

Предположение: $U$ вещественно-аналитична, $0$ — изолированная критическая точка, не минимум; тогда (п. 4) некоторая струя показывает отсутствие минимума. Кинетика — положительно определённая квадратичная по скоростям, гладкая (для аналитики; (A) — случай $T=|\dot x|^2/2$).

| Гессиан | Что известно | Источник | Статус |
|---|---|---|---|
| Есть отрицательное собственное значение | неустойчивость | Lyapunov (по AG17, FGT08) | [Литература, вторично] |
| $H>0$ (ранг 3) | $0$ — строгий минимум, не наш случай | | |
| $H\ge0$, ранг 2 (ядро 1) | неустойчивость, асимптотическая траектория | FGT08 Thm A ($n-2=1$); при ядре 1 — также MMN91 после расщепления | [Литература: FGT08 Thm A, техотчёт] |
| $H\ge0$, ранг 1 (ядро 2) | то же | FGT08 Thm A, Thm 2 | [Литература: FGT08 Thm A, техотчёт] |
| $H=0$ (ранг 0), первая ненулевая форма $U_m$ принимает отрицательные значения | неустойчивость (однородная струя без минимума) | MN89, MMN91 ($r=0$), Taliaferro 1990 | [Литература, вторично, по FGT08 и AG17] |
| $H=0$, $U_m\ge0$ | только частные случаи: класс $\mathcal H$ (AG17), условие Chetaev для самого $U$, примеры типа $x^4+y^4-z^6$; в общем виде открыто | AG17; Burgos 2025 | [Литература: AG17], остальное — открыто |

Что остаётся открытым при $n=3$ для аналитического $U$ с изолированной критической точкой: случай $H=0$ (то есть $j^2U=0$) и такая первая ненулевая форма $U_m\ge0$ (с нулями на сфере, иначе минимум), для которой струя, показывающая отсутствие минимума, имеет порядок $s>m$ и не лежит в $\mathcal H$ (и $U$ не удовлетворяет условию Chetaev). Для таких $U$ нет ни доказательства, ни контрпримера в доступной литературе. [Гипотеза: поиск неполный.]

Гипотеза Ляпунова о струях при $n\ge3$ в общем виде (любая струя, любой гессиан) открыта: известно только FGT08 (гессиан $\ge0$, коранге $\le2$), MMN91/MN89/Taliaferro (однородная или специальной формы струя) и AG17 (класс $\mathcal H$, $C^2$-потенциал). Для $n\ge4$ открыты также случаи $H\ge0$ с ядром размерности $\ge3$.

## 4. Верно ли, что для изолированной критической точки аналитического $U$ некоторая струя показывает отсутствие минимума?

**[Литература: BGZ96]** A. Barone Netto, G. Gorni, G. Zampieri, «Local extrema of analytic functions», NoDEA 3:3 (1996), 287-303. По GT03 (препринт, §1) и FGT08 (введение): «for every analytical function $f$ without a minimum at $q_0$ there is an integer $k$ such that $j^kf$ shows that $f$ doesn't have a minimum at this point». Это пересказ; сама статья не открывалась (аннотация в репозитории Verona/Zampieri: «complete answer to the question of when the local extremal behavior of a real analytic function at a point can be settled by finitely many terms» — вторично). Изолированность в этой формулировке не требуется.

**[Доказано] (мой вывод, независимый от BGZ96)** Пусть $f$ вещественно-аналитична около $0$, $f(0)=0$, и $0$ не локальный минимум. Тогда существует $k$ такое, что $j^kf$ (многочлен Тейлора $P$ порядка $k$) показывает отсутствие минимума в смысле определения п. 1.

Доказательство. По лемме о выборе кривой (curve selection lemma, Milnor, Singular points of complex hypersurfaces, Thm 3.1; для аналитических и полуалгебраических множеств; ссылка не открывалась) в множестве $\{f<0\}$ есть аналитическая кривая $\gamma:[0,\delta)\to\mathbb R^n$, $\gamma(0)=0$, $f(\gamma(t))<0$ при $t>0$. Тогда $f\circ\gamma(t)=-ct^m+O(t^{m+1})$, $c>0$, $m\ge1$ целое (аналитическая функция, не равная нулю тождественно). Далее $\gamma(t)=t^a(v+O(t))$, $a\ge1$, $v\ne0$, так что $|\gamma(t)|\asymp t^a$. Возьмём $k\ge m+1$ (тогда $ak>m$). Пусть $g$ — любая функция с $j^kg=P$, то есть $g-P=o(|x|^k)$ (в частности $g(0)=0$). Тогда $g(\gamma(t))=f(\gamma(t))-(f-P)(\gamma(t))+(g-P)(\gamma(t))=-ct^m+O(t^{a(k+1)})+o(t^{ak})<0$ при малых $t>0$. Значит $g$ принимает отрицательные значения в сколь угодно малых окрестностях $0=g(0)$: минимума нет, ни строгого, ни нестрогого. $\square$

Замечания: изолированность критической точки не использована; аналитичность использована в лемме о выборе кривой и в том, что $f\circ\gamma$ имеет конечный порядок обращения в нуль (для плоских $C^\infty$-функций вроде Painlevé/Laloy это ломается: $j^kf\equiv0$). Порядок $k$ может быть сколь угодно большим, равномерной оценки по $f$ нет.

**Критерии $k$-определённости (Kuo, Kuiper, Bochnak–Łojasiewicz) — [Литература: Kozyakin, arXiv:0907.0571, Thm 1.1; вторично, оригиналы не открывались].** Классы: $E^{[r]}(n,1)$ — ростки $C^r$-функций. «For $f\in E^{[r]}(n,1)$, the jet $j^rf(0)$ is $C^0$-sufficient in $E^{[r]}(n,1)$ if and only if there are positive numbers $C,\varepsilon$ such that $|\mathrm{grad}f(x)|\ge C|x|^{r-1}$ for $|x|<\varepsilon$. For $f\in E^{[r+1]}(n,1)$, the jet $j^rf(0)$ is $C^0$-sufficient in $E^{[r+1]}(n,1)$ if and only if there are numbers $C,\delta,\varepsilon>0$ such that $|\mathrm{grad}f(x)|\ge C|x|^{r-\delta}$ for $|x|<\varepsilon$» (в градиенте имеется в виду $r$-усечение $f^{(r)}$; знак усечения в тексте arXiv потерян; ср. `notes/literature/2026-10-21-revision-rest.md`, (d)). $C^0$-достаточность: любые две функции с той же $r$-струёй $C^0$-эквивалентны, $f=g\circ h$, $h$ — гомеоморфизм. Оценка: для аналитического $f$ с изолированной критической точкой неравенство Лоясевича $|\mathrm{grad}f|\ge C|x|^N$ даёт $C^0$-достаточность $j^kf$ при $k\ge N+1$ в классе $C^{k+1}$ (так же, как в наблюдении главного агента) [Эскиз: оригиналы Kuo/Łojasiewicz не сверены]. Этот путь слабее п. 4: он не покрывает функции $g$, у которых есть только точечная струя; а для вывода «нет минимума» достаточно прямого аргумента выше. Takens (1971) — «A note on sufficiency of jets»: статья не открывалась.

## 5. Предлагаемые правки к `problem/KNOWN_RESULTS.md` (сам файл не правился)

1. Строка про FGT08: заменить «гессиан $\ge0$ с ядром размерности $\le2$ (по Alva–Garcia)» на дословную постановку: $\mathcal L\in C^{k+\lfloor(k-3)/2\rfloor+3}$, $T$ положительно определённая квадратичная форма по $\dot q$ (зависит от $q$), $j^2\pi(0,0)\ge0$ ранга $\ge n-2$, $k$-струя показывает отсутствие минимума ⇒ траектория $\phi(t)\to(0,0)$ при $t\to-\infty$. Пометка: [Т: техотчёт RT-MAP-0801, 2008; журнальная версия не сверена].
2. Строка про AG17: убрать «Не покрывает $x^4+y^4-z^6$». По проверке выше $x^4+y^4-z^6\in\mathcal H$ ($s=6$) и удовлетворяет условию Chetaev. Если у главного агента есть иное основание, указать его.
3. Добавить п. 4: доказательство существования струи, показывающей отсутствие минимума, через curve selection (и ссылка BGZ96 как «по пересказу GT03, FGT08»).
4. Добавить таблицу покрытия при $n=3$ (п. 3) и формулировку открытого случая: $H=0$, $U_m\ge0$, не-Chetaev.
5. Строка про Palamodov 1995 в FGT08 (аналитический случай «показано» ещё в 2008) — отметить, что FGT08 принимают результат Palamodov 1995 без оговорок; сегодняшняя оценка (неполнота) расходится.
6. Отметить, что BP22 и Burgos 2025 пишут «результаты по первой ненулевой струе», а FGT08 и AG17 работают с высшими струями; в литературе нет работ 2018-2026, продвинувших гипотезу о струях при $n\ge3$ дальше FGT08 и AG17 (поиск неполный).
