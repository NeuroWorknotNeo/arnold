# Сверка остальных литературных утверждений ревизии (A-313, A-406, A-408, A-418, A-419)

Дата: 21.10.2026. Автор: агент `literature`. Правила меток: CLAUDE.md.
Источники утверждений: `notes/vlad-claude/theoremB.md`, `theoremB-proof.md` §7, `notes/vlad-claude-tg/overview.tex`.

## 0. Доступ и степень сверки

| Источник | Что открывалось |
|---|---|
| Burgos, arXiv:2506.19135 v1 | полный текст PDF: введение, §1.1, §12 (формулировки), список литературы |
| Alva–Garcia, arXiv:1508.07427 v2 | полный текст PDF, включая доказательства §3 и пример §4 |
| Burgos–Paternain, arXiv:2208.01139 v1 | введение (с.1–6) |
| Burgos–Maderna–Paternain, arXiv:1906.11962 | введение |
| Brunella, Ann. Inst. Fourier 48:5 (1998) (numdam, свободно) | введение и формулировка теоремы |
| Mather, Stability of C^∞ mappings III, Publ. IHES 35 (1968) (numdam, свободно) | введение, §3, §9 (полный текст, OCR с искажениями формул) |
| Tougeron, Ann. Inst. Fourier 18:1 (1968) (numdam) | открыт; о конечной определённости функций в нём ничего нет, не использован |
| Rauch, Sém. Laurent Schwartz 2013–14, exp. XII (numdam) | полный текст |
| Kozyakin, arXiv:0907.0571 | введение (формулировка теоремы Kuiper–Kuo–Bochnak–Łojasiewicz, вторично) |
| Rebelo–Reis, arXiv:1712.10286; Abramovich–Belotto–Temkin–Włodarczyk, arXiv:2503.00926; Panazzolo, arXiv:math/0506209 | введения / аннотация |
| zbMATH Open (API по Zbl-номерам) | рецензии: Taliaferro 1990, Wiener 1993, Kozlov 1986, Bertotti–Bolotin 2000 (+ Equadiff-аннотация); для MN89, MMN91, Sofer 1983, Kozlov 1982 (ФАН), Kozlov–Palamodov 1982 текстов рецензий нет |
| Паламодов 2020, 1977; Kozlov–Palamodov 1982; Kozlov 1982 (ФАН 16:4); Saito 1971; MN89; MMN91; Wiener, Taliaferro (полные тексты) | **не открывались**: Math-Net недоступен; Springer, Elsevier, Project Euclid (защита от ботов), mathjournals.org (liblynx) — платные или закрытые, обходить не стал |

Инструмент WebSearch был отклонён системой разрешений; повторно не вызывался. Поиск вёл через API arXiv, zbMATH, Crossref.

---

## 1. A-313: новизна теоремы B

Обозначения как в theoremB-proof.md: $u_m\ge0$, $\Sigma=\{u_m=0\}\cap S^{n-1}$, $g=u_{m+1}|_\Sigma$, (B3): у $g$ регулярный нуль.

**Предварительный факт [Доказано, элементарно].** Из (B1)–(B3) при $\Sigma\ne\varnothing$: $\Sigma=-\Sigma$ ($m$ чётно), $u_{m+1}$ нечётна, значит $g\not\equiv0$ (иначе (B3) нарушено) и $g$ принимает значения обоих знаков. В частности $u_{m+1}\not\equiv0$, то есть вторая ненулевая однородная часть ряда имеет степень ровно $m+1$.

### 1.1 Burgos, arXiv:2506.19135 — вердикт «подтверждено, не покрывает»

[Литература: Burgos arXiv:2506.19135v1, полный текст (формулировки); журнальная версия JDE 454 (2026) не сверялась]. Дословно:

- «Proposition 1.2 (Total instability criterion). Suppose that f is a Morse function and zero is a regular value. Then, the point p is totally unstable.» Здесь $f$ — ограничение первой ненулевой струи $U_{l_1}$ на единичную сферу.
- «Proposition 1.3 (Non-generic total instability criterion). If C(q) > 0 on every critical point q of f such that f(q) ≤ 0, then the point p is totally unstable.» Условия: $U=U_{l_1}+U_{l_2}+\dots$ — первая и вторая ненулевые однородные части, «Suppose that U is not a homogeneous polynomial»; $C(q)=-\delta^{\mu}_{l_2-l_1}(l_2-l_1)U_{l_2}(q)+\delta^{\mu}_{m}\,m\,U_{l_1}(q)\sum g^{(m)}_{ij}(q)q^iq^j$; $\mu=\min\{l_2-l_1,m\}$; предположение слабого магнетизма $d-l_1/2>\mu$ (в ньютоновском случае $m=\infty$, магнитного члена нет).
- «Corollary 1.4. In Newtonian mechanics, the point p is totally unstable if the second non-zero homogeneous term in the Maclaurin series of the potential is negative on the critical locus of the the first non-zero homogeneous term restricted to the unit sphere where the latter term is less than or equal to zero.» (то же — Cor. 12.5 в §12).
- Гладкость: вещественно-аналитические $U$, метрика, 1-форма.
- Во введении сказано: «As our knowledge goes, so far all of the instability criteria either in the total or Lyapunov sense, require the generic hypothesis that zero is a regular value of the function f.» (это утверждение автора B25; оно не совпадает с точным составом литературы, см. п. 1.3).

**Применение к теореме B** [Доказано, элементарно, из дословных формулировок]:
- Prop. 1.2 не применима: $f=u_m|_S\ge0$ и $f=0$ на $\Sigma\ne\varnothing$, то есть нуль — критическое значение.
- Prop. 1.3 / Cor. 1.4: критические точки $f$ с $f\le0$ — ровно $\Sigma$ (там минимум), $l_1=m$, $l_2=m+1$, $C(q)=-U_{m+1}(q)$ (ньютоновский случай). Условие $C>0$ на $\Sigma$ означает $u_{m+1}<0$ на всём $\Sigma$. Это невозможно (предварительный факт).
- Вывод: **утверждение theoremB.md / theoremB-proof.md §7 п. 3 о B25 подтверждено**: критерий в ситуации (B1)–(B3) не срабатывает никогда. Уточнение к формулировке: следует писать «условие $u_{m+1}<0$ на всём $\Sigma$» (а не «в точках $\Sigma$ вообще»), и что критерий требует $u_{m+1}\ne0$ как вторую ненулевую часть (в (B3) это автоматически).

### 1.2 Alva–Garcia 2017, arXiv:1508.07427 — вердикт «неточно — как исправить»

[Литература: Alva–Garcia, arXiv:1508.07427v2, полный текст]. Условия: $\Pi$ имеет $s$-джет в нуле, $C^2$, $j^1\Pi=0$, кинетическая энергия $C^2$; $A_s=(j^s\Pi)^{-1}(-\infty,0)$, $C_s=(R^s_\Pi)^{-1}(-\infty,0)$, $R^s_\Pi(q)=\langle\nabla j^s\Pi(q),q\rangle$. Класс $\mathcal H$ (§1.2, дословно):

- «(H1) $j^\ell\Pi(q)\ge0$ in some neighborhood of the origin if $\ell\le s-1$;
- (H2) $j^s\Pi$ show that $\Pi$ has not minimum at origin;
- (H3) There exist $\varepsilon>0$ with $B_\varepsilon\subset\Omega$ and a connected component $A_*$ of $A_s$, such that $(A_*\setminus\{0\})\cap B_\varepsilon\subset C_s^\circ\cap B_\varepsilon$.»

Теорема 1: если потенциал класса $\mathcal H$, то выполнено строгое условие Четаева (есть компонента $A$ множества $\Pi^{-1}(-\infty,0)$ с $R_\Pi<0$ на $(A\setminus0)\cap B_\varepsilon$); Предложение 8 даёт отсюда асимптотическую траекторию, значит неустойчивость.

**Что обнаружено.**

1. Во введении (с.3) условие (H3) описано иначе: «requires that **closure** of the region where $j^s\Pi$ is negative is contained within the region in which $\langle\nabla j^s\Pi(q)|q\rangle$ is negative». Формула (H3) в §1.2 про замыкание ничего не говорит. Доказательства (Лемма 1, Предл. 1, Предл. 4) используют именно замыкание: в доказательстве леммы 1 для точки $y$ с $j^s\Pi(y)=0$ на границе сказано «Of course $y\in A_s$», хотя $A_s$ открыто и $y\in\partial A_s$; для вывода «$\partial A_s\setminus\{0\}\cap Z_{s-1}=\emptyset$» в Предл. 1 тоже нужна версия с замыканием.
2. **Для примера $U=(x^2+y^2-z^2)^2+xz^4$ ($s=m+1=5$, $j^5U=U$) формула (H3) из §1.2 выполнена тривиально** [Доказано, элементарно]: на $A_5$ имеем $u_5=xz^4<-u_4\le0$, и $R^5=4j^5U+xz^4<0$, так что $A_5\subset C_5$. Вообще для любого $U$ из теоремы B при $s=m+1$: $A_s\subset C_s$, так как $u_{m+1}<-u_m\le0$ на $A_s$ и $R^s=m\,j^sU+u_{m+1}$. (H1) и (H2) тоже выполнены ($j^m=u_m\ge0$; $g<0$ где-то на $\Sigma$). Значит, **буквально прочитанная** теорема 1 покрывала бы теорему B (в части неустойчивости по Ляпунову).
3. Но буквальная теорема 1 — по-видимому, ложна, а лемма 1 (при буквальном (H3)) ложна точно. Лемма 1: алгебраическая кривая $\gamma\subset A_s$ касается луча $r_\gamma$, на котором $j^s\Pi|_{r_\gamma}$ имеет строгий максимум в нуле. Контрпример [Доказано, элементарно]: $\gamma(t)=(-t^2,\,t\sqrt{1-t^2},\,t)$, $q=0$, $j^5U(\gamma)=-t^6<0$, касательный луч $(0,1,1)$ — луч нуля $g$, и вдоль него $j^5U\equiv0$. Для $U_\epsilon=q^2+xz^4+z^6$ (струя $j^5$ та же) в точке $z=0.1$, $q=0$, $x=-0.011$: $U_\epsilon=-10^{-7}<0$, а $R_{U_\epsilon}=4q^2+5xz^4+6z^6=+5\cdot10^{-7}>0$; такие точки есть на всех масштабах вблизи лучей $g=0$. Принадлежность этих точек той же компоненте $\{U<0\}$ не проверялась строго [Эскиз], но вероятно, что заключение теоремы 1 (строгое условие Четаева) для $U_\epsilon$ неверно.
4. Со **замыканием** в (H3) (как задумано и как нужно доказательствам) пример теоремы B (H3) не удовлетворяет: в $\overline{A_5}\setminus0$ лежат лучи $(0,\pm1,\pm1)$, где $R^5=xz^4=0$, а $C_5$ открыто. Поэтому утверждение theoremB.md («(H3) нарушается в точках $\Sigma$, где $g=0$») верно для задуманного условия с замыканием.

**Вердикт:** «неточно — как исправить»: писать «(H3) в виде, который используется в доказательствах (замыкание области $\{j^s\Pi<0\}$ внутри $\{R^s<0\}$), нарушено в точках $\Sigma$, где $g=0$; в формулировке §1.2 (без замыкания) оно выполнено, и тогда лемма 1 и теорема 1 Alva–Garcia, по-видимому, неверны (см. контрпример); в доказательстве лемма 1 использует $y\in\partial A_s$ как $y\in A_s$». Это пробел в чужой работе, не доказанный отзыв; перед использованием его нужно проверить рецензентом. Публикация: по ранее собранным данным Qual. Theory Dyn. Syst. 16 (2017) 371–389, сверялась только по метаданным.

### 1.3 Остальные критерии

| Критерий | Точная формулировка (источник) | Покрывает B? |
|---|---|---|
| Паламодов 2020, Thm 3 | $U=u_m+u_{m+1}+\dots$, $\nabla u_m\ne0$ при $x\ne0$ ⇒ тотальная неустойчивость. [Вторично: конспект `notes/vlad-claude/palamodov2020.md` (полный текст читал vlad-claude), и Burgos 2025 §1.1: «if the first non-zero jet of the potential at p has no critical point other than the origin, then the point p is totally unstable» — вещественно-аналитический $U$] | Нет: в B $\nabla u_m=0$ на $Z\ne\{0\}$ |
| Паламодов 2020, Thm 5 | сводит к ограничению на ядро квадратичной части (по конспекту vlad-claude; точная формулировка с условиями не сверена) | Частично, при $m=2$ — см. ниже |
| Паламодов 2020, Thm 6 | квазиоднородная главная часть (веса $w$) без критических точек вне 0, остаток $O(\lvert x\rvert\,\lvert x\rvert_w)$ (по конспекту) | Нет для примера $U=q^2+xz^4$ в исходных координатах (по theoremB-proof.md; отсутствие подходящей замены координат — [Гипотеза]) |
| Козлов–Паламодов 1982 | не открывался; zbMATH-рецензия пустая. В KP82 речь, по Burgos 2025 §1.2, об асимптотических орбитах при условии на первую ненулевую струю | **не удалось проверить**; утверждение «нужно, чтобы $u_m$ не имел минимума» — не сверено |
| Alva–Garcia 2017 | п. 1.2 выше | В задуманном виде нет; в буквальном виде — формально да, но см. п. 1.2 |
| Maffei–Moauro–Negrini, DIE 4:4 (1991) 767–782 | zbMATH-рецензии нет («contents unavailable»); вторично, Alva–Garcia, введение (полный текст): неустойчивость, если после замены координат $\pi(q)=\lVert(q_1,\dots,q_r)\rVert^2+\pi_s(q_{r+1},\dots)+R$, $\pi_s$ однородный степени $s\ge2$ без минимума в нуле, $R(q)/\lVert q\rVert^s\to0$ (индексы у $R$ в извлечённом тексте искажены) | Нет при $m\ge4$ (там $\pi_s=u_m\ge0$ имеет минимум); при $m=2$ см. ниже |
| Taliaferro 1990, ARMA 109 | [Литература: zbMATH Zbl 0679.70003, аннотация автора, проверено по тексту рецензии]: $T,U\in C^2$, $U^{(i)}(x)=U_p^{(i)}(x)+O(\lVert x\rVert^{p+\epsilon-i})$, $i=0,1,2$, $p>0$, $0<\epsilon\le1$, $U_p$ положительно однородна степени $p$ и трижды непрерывно дифференцируема; «If, for some $x\ne0$, $U_p(x)<0$ then we will prove that there is a solution $x(t)$ of (1) such that $\lVert x(t)\rVert+\lVert x'(t)\rVert\to0$ as $t\to0^+$, when $0<p<2$; and as $t\to-\infty$, when $p\ge2$» | Нет: $U_p=u_m\ge0$ |
| Wiener 1993, JDE 103:1, 58–67 | [Литература: zbMATH Zbl 0792.34046, рецензия Perko]: «The instability of a degenerate equilibrium position is studied through the formal solutions. The inversion of the Lagrange-Dirichlet stability theorem is proved in the case of two zero eigenvalues and a nondegenerate Newton's diagram.» Полный текст не открывался; что именно значит «two zero eigenvalues» (коранг гессиана 2) и «невырожденная диаграмма Ньютона», не установлено | Для примера ($u_2=0$, $n=3$, коранг 3) нет; при $m=2$ и $\dim\ker u_2=2$ (n≥3) пересечение не исключено |
| Kozlov 1986 (для $m=2$) | [Литература: zbMATH Zbl 0631.70018, рецензия]: «An existence theorem is proved for asymptotic trajectories on the assumption that the Maclaurin series for the potential energy has the form $V_2+V_m+V_{m+1}+\dots$ ($V_s$ is a homogeneous form of degree $s$) and the function $V_2+V_m$ does not have a local minimum at the equilibrium position» | При $m=2$ покрывает теорему B в части неустойчивости по Ляпунову — см. ниже |

**Случай $m=2$ [Доказано, элементарно, из формулировок].**
- Для Kozlov 1986: при $m=2$ $\Sigma=S^{n-1}\cap\ker u_2$, $g=u_3|_\Sigma$ нечётна, $g\not\equiv0$ по (B3), значит $u_3|_{\ker u_2}$ принимает отрицательные значения, и $u_2+u_3$ не имеет минимума (вдоль луча в $\ker u_2$ с $u_3<0$ значение отрицательно). Условие рецензии Kozlov 1986 ($V_2+V_3+\dots$, $V_2+V_3$ без минимума) выполнено ⇒ существует асимптотическая траектория, Ляпунов-неустойчивость.
- Для Паламодова: при (B3) для ограничения $u_3|_{\ker u_2}$ выполнено $\nabla(u_3|_{\ker})\ne0$ вне нуля (в точках, где $u_3\ne0$, радиальная производная $3u_3\ne0$; где $u_3=0$, касательный градиент по (B3) ненулевой). Значит, если теорема 5 действительно сводит к ядру и подаёт ограничение в теорему 3, то $m=2$ покрыто и для тотальной неустойчивости. Это условно: теорема 5 не сверена.
- Следствие для статуса: новизна теоремы B по отношению к известным критериям остаётся только при $m\ge4$ (это согласуется с гипотезой R2 из AUDIT A-313).

**Вердикт A-313: «подтверждено» для B25, Taliaferro, Паламодов Thm 3; «неточно — как исправить» для Alva–Garcia (п. 1.2); для $m=2$ покрыто (Kozlov 1986; условно Паламодов Thm 5), то есть в списке «не покрыто» надо оговорить $m\ge4$; «не удалось проверить» для Козлов–Паламодов 1982, Maffei–Moauro–Negrini, Паламодов Thm 5, 6 (по первоисточнику), Wiener (по полному тексту).**

---

## 2. A-418: конечная определённость при вещественной, но не комплексной изолированности

### 2.1 Что точно известно

(a) **Конечная определённость в $C^\infty$.** [Литература: Mather, Stability of $C^\infty$ mappings III, Publ. IHES 35 (1968), 127–156, полный текст, OCR с искажениями формул]. Теорема (3.5): для групп эквивалентности $\mathcal R$ (правая), $\mathcal K$ (контактная), $\mathcal A$ и др. «necessary and sufficient condition that $f$ be f.d. rel. $\mathcal G$ is that $d(f,\mathcal G)<\infty$», где для правой эквивалентности $d(f,\mathcal R)=\dim_{\mathbb R}\mathcal E(f)/tf(B)$. Для $f:(\mathbb R^n,0)\to\mathbb R$ это $\dim_{\mathbb R}\mathcal E_n/J(f)\mathcal E_n$. Предложение (3.6): конечность $d$ равносильна выполнению для некоторого $k$ включения вида «образ $tf$ плюс высокая степень $\mathfrak m$ содержит $\mathfrak m^{l(k)}\mathcal E(f)$»; точный вид включения в OCR не читается [не сверено дословно]. Определение: $f$ $k$-определён, если любой $g$ с $j^kg=j^kf$ лежит в той же орбите; конечно определён — если $k$-определён при некотором $k$.

(b) **Аналитический случай.** [Литература: Mather III, §9.2, полный текст]. Теорема: для вещественно-аналитического ростка следующие условия равносильны: (a) конечная определённость при аналитических заменах; (b) то же при $C^\infty$-заменах; (c) то же для комплексного аналитического продолжения $\tilde f$ (для любой из групп). То есть конечная $C^\infty$-определённость аналитического ростка ⇔ конечная определённость его комплексификации.

(c) Для функции с критической точкой: конечная определённость комплексификации ⇔ $\dim_{\mathbb C}\mathcal O_n/J(\tilde f)<\infty$ ⇔ число Милнора $\mu<\infty$ ⇔ точка 0 изолирована среди критических точек комплексификации (по (3.5) в комплексной категории (§9.1) плюс стандартное тождество $\mu=\dim\mathcal O/J$ и нуль-стеллензац; последний шаг в Mather явно не выписан). Для аналитического $U$ это даёт: **$C^\infty$-конечная определённость ⇔ $\mu<\infty$ ⇔ комплексная изолированность.** Согласуется с пометкой ГА в AUDIT.

(d) **$C^0$-достаточность.** [Литература: Kozyakin, arXiv:0907.0571, Thm 1.1 (вторично; текст теоремы там, ссылки на Kuiper 1966, Kuo 1969, Bochnak–Łojasiewicz 1971)]: «For $f\in E^{[r]}(n,1)$, the jet $j^rf(0)$ is $C^0$-sufficient in $E^{[r]}(n,1)$ if and only if there are positive numbers $C,\varepsilon$ such that $\lvert\operatorname{grad}f(x)\rvert\ge C\lvert x\rvert^{r-1}$ for $\lvert x\rvert<\varepsilon$. For $f\in E^{[r+1]}(n,1)$, the jet $j^rf(0)$ is $C^0$-sufficient in $E^{[r+1]}(n,1)$ if and only if there are numbers $C,\delta,\varepsilon>0$ such that $\lvert\operatorname{grad}f(x)\rvert\ge C\lvert x\rvert^{r-\delta}$ for $\lvert x\rvert<\varepsilon$.» (В извлечённом тексте арXiv знак truncation $(r)$ в градиенте потерян; по смыслу и по формуле (6) там же — градиент $r$-усечения $f^{(r)}$. Не сверено с оригиналами Kuo 1969 и Bochnak–Łojasiewicz 1971.) $C^0$-достаточность: любые $f,g$ с $j^rf=j^rg=w$ топологически эквивалентны ($f=g\circ h$, $h$ — гомеоморфизм).

(e) Gradient-Łojasiewicz и $\infty$-определённость. Теорема «если $\lvert\nabla f\rvert\ge c\lvert x\rvert^N$, то росток определён своей бесконечной струёй относительно $C^\infty$-диффеоморфизмов» (приписывается Тужрону) в доступных текстах не найдена: диссертация Tougeron 1968 в numdam этого не содержит, Idéaux de fonctions différentiables (Springer 1972) не открывалась. **Элементарное доказательство** [Доказано, здесь, нуждается в проверке рецензентом]: пусть $\lvert\nabla f(x)\rvert\ge c\lvert x\rvert^N$ и $\varphi$ плоская в нуле ($C^\infty$). Положим $f_t=f+t\varphi$, $t\in[0,1]$. Тогда $\lvert\nabla\varphi\rvert=o(\lvert x\rvert^{N})$, поэтому $\lvert\nabla f_t\rvert\ge\frac c2\lvert x\rvert^N$ в малой окрестности. Поле $X_t=-\varphi\nabla f_t/\lvert\nabla f_t\rvert^2$ определено при $x\ne0$, $X_t(0)=0$, и все его производные по $x,t$ ограничены $C_k\lvert x\rvert^{k}$ для любого $k$ (плоскость $\varphi$, степенная оценка знаменателя), то есть $X_t$ — $C^\infty$ и плоское в нуле. Поток $h_t$ — $C^\infty$-диффеоморфизмы, фиксирующие 0, и $\frac d{dt}(f_t\circ h_t)=0$. Значит $f+\varphi=f\circ h_1^{-1}$.

### 2.2 Применение к утверждению overview.tex §1.3

Пусть $U$ вещественно-аналитична, 0 — изолированная вещественная критическая точка, $\mu=\infty$ (например, $U=x_1(x_1^2+x_2^2)^2$: $\partial_1U=(x_1^2+x_2^2)(5x_1^2+x_2^2)$, $\partial_2U=4x_1x_2(x_1^2+x_2^2)$, общие комплексные нули на прямых $x_2=\pm ix_1$).

- Из 2.1(a)–(c): **$U$ не является конечно определённым ни в аналитической, ни в $C^\infty$ категории** (никакая конечная струя не определяет росток с точностью до диффеоморфизма).
- Из 2.1(e) (элементарно): росток $\infty$-определён (если по Łojasiewicz $\lvert\nabla U\rvert\ge c\lvert x\rvert^N$; оно выполнено для вещественно изолированной аналитической критической точки по неравенству Łojasiewicz для градиента — стандартный факт, здесь не перепроверялся).
- Из 2.1(d): струя $j^rU$ при $r\ge N+1$ $C^0$-достаточна в $C^{r+1}$ (в силу $\lvert\nabla j^rU\rvert\ge\frac c2\lvert x\rvert^N\ge C\lvert x\rvert^{r-\delta}$; вывод мой, элементарный). Для однородного $U$ степени $d$ с вещественно изолированной критической точкой $\lvert\nabla U\rvert\ge c\lvert x\rvert^{d-1}$, и условие (3) Kuiper–Kuo выполнено в $C^d$.

**Вердикт по overview.tex §1.3, фраза «по теореме Тужрона росток лишь $C^\infty$-конечно определён, и редукция идёт через гладкие (не аналитические) замены»: «неверно — как исправить».** При $\mu=\infty$ росток вообще не конечно определён (ни аналитически, ни $C^\infty$, по Mather III §9.2 и Thm 3.5). Сохраняются: $C^0$-достаточность струй достаточного порядка (Kuiper–Kuo–Bochnak–Łojasiewicz) и $\infty$-определённость (плоские возмущения не меняют класс; элементарно). Корректная формулировка: «если точка изолирована лишь над $\mathbb R$ ($\mu=\infty$), то ни один конечный джет не определяет росток с точностью до диффеоморфизма (Mather III, теорема 3.5 и §9.2); сохраняется $C^0$-достаточность джетов (Kuiper–Kuo–Bochnak–Łojasiewicz)». Мотив «редукция через гладкие замены» из доступных источников не подтверждается.

Замечание к A-007: пометка «при вещественной изолированности теряется $C^\infty$-конечная определённость, но остаётся $C^0$-достаточность» **подтверждена**, добавить $\infty$-определённость и ссылку на Mather III §9.2.

---

## 3. A-406: теорема Сайто

[Литература: K. Saito, Quasihomogene isolierte Singularitäten von Hyperflächen, Invent. Math. 14 (1971), 123–142; Zbl 0224.32011 (MSC 32S05, 32S40). **Оригинал не открывался**, рецензии zbMATH нет.] Вторичный источник [Литература: arXiv:1708.09716, введение, полный текст страницы]: «K. Saito showed ([Sa71]) that $\mu/\tau=1$ holds, if and only if, $f$ is weighted homogeneous, i.e., analytically equivalent to such a polynomial.» Здесь $f:(\mathbb C^n,0)\to(\mathbb C,0)$ — голоморфный росток с изолированной особенностью, $\mu$ и $\tau$ — числа Милнора и Тюрины, $\tau=\dim\mathcal O/(f,J(f))$.

Общеизвестная формулировка теоремы (по памяти составителя и вторичным пересказам, в первоисточнике не проверена): для голоморфного ростка $f$ с изолированной критической точкой в 0 равносильны: (i) $f\in J(f)=(\partial f/\partial x_1,\dots,\partial f/\partial x_n)$; (ii) $\mu=\tau$; (iii) в подходящих **голоморфных** координатах $f$ квазиоднороден (с положительными рациональными весами). (i)⇔существование голоморфного поля $V=\sum a_i\partial_i$ с $V(f)=f$: тривиально, $a_i$ — коэффициенты выражения $f=\sum a_i\partial_if$.

**Применение к overview.tex §2.1 п. 1** («для ростка с изолированной особенностью аналитическое в нуле поле $V$ с $V(U)=U$ существует тогда и только тогда, когда $U$ квазиоднороден в подходящих координатах»):
- верно при комплексной изолированности ($\mu<\infty$); изолированность в теореме Сайто — над $\mathbb C$. При $\mu=\infty$ теорема не применима: (иллюстрация: однородный $U=x_1(x_1^2+x_2^2)^2$ квазиоднороден, но под теорему Сайто не подпадает);
- Сайто работает в голоморфной категории. Что в вещественно-аналитическом случае координаты можно взять вещественными, из доступных текстов не следует [не проверено];
- «и только тогда» следует из (i)⇔(iii); «если» — тривиально (поле Эйлера с весами).

**Вердикт:** «неточно — как исправить»: добавить «изолированность над $\mathbb C$ ($\mu<\infty$)», «голоморфные (над $\mathbb R$ — вещественные не проверено) координаты» и ссылку Invent. Math. 14 (1971) 123–142; оригинал не сверен. Выкладка с $U=-x^2+3y^2$ ($\partial_yV_*^y=-3/2$) — проверена здесь заново: в точках $(x,0)$ $\partial_yV_*^y=U\,U_{yy}/\lvert\nabla U\rvert^2=(-x^2)\cdot6/(4x^2)=-3/2$ [Доказано, элементарно].

---

## 4. A-408: редукция особенностей векторных полей

| Размерность | Результат | Источник и степень сверки |
|---|---|---|
| 2 | Seidenberg 1968: для голоморфного слоения в окрестности $0\in\mathbb C^2$ существует конечная цепочка раздутий точек, после которой все особые точки элементарны (хотя бы одно ненулевое собственное значение) | [Литература: Rebelo–Reis arXiv:1712.10286, введение, пересказ; Seidenberg, Amer. J. Math. 90 (1968) 248–269, Zbl 0159.33303; оригинал не открывался] |
| 3, вещественно-аналитический | Panazzolo, Acta Math. 197 (2006) 167–289: «Let X be an analytic vector field defined in a real analytic manifold of dimension three. We prove that all the singularities of X can be made elementary by a finite number of blowing-ups in the ambient space.» (аннотация arXiv:math/0506209); по рецензии Zbl 1112.37016 и по Rebelo–Reis используются взвешенные раздутия | [Литература: аннотация arXiv + рецензия zbMATH; текст не читался] |
| 3, комплексное | McQuillan–Panazzolo, J. Differential Geom. 95:2 (2013) 279–319 «Almost étale resolution of foliations» (препринт IHES/M/09/51); Cano–Roche–Spivakovsky, RACSAM 108 (2014) | [Литература: Rebelo–Reis arXiv:1712.10286 (полный текст введения); сами работы не читались] |
| 3, формальная | Cano, Desingularization strategies for three-dimensional vector fields, LNM 1259 (1987) (формальная локальная теорема; Cano 1987, Ann. Inst. Fourier 37:2, 151–193, Zbl 0607.58027) | [Литература: Brunella 1998, введение: «the (local) desingularization theorem of Cano [Ca1], [Ca2], which roughly speaking says that we can always reduce the singularities of a three-dimensional vector field to nonnilpotent ones»; Rebelo–Reis, введение] |
| ≥4 | Abramovich–Belotto da Silva–Temkin–Włodarczyk, arXiv:2503.00926 (v2, март 2025), §1.3: «Resolution of singularities of foliations is a problem which goes back to the beginning of the twentieth century [Ben01] and remains quite mysterious in high dimensions. In fact, the best results to date are either limited to foliations in threefolds [Ben01, Sei68, Pan06, MP13, Can04a, CC92a, CRS14, RR21, Pos24]; or are local in nature [BdS18, CCS89, CFD22].» Там же: пример Санчо–Санс показывает, что уже при $\dim=3$ нужны взвешенные раздутия | [Литература: arXiv:2503.00926, введение, полный текст страницы] |

Уточнения к тексту overview.tex §3.1: (1) «Кано; Панаццоло 2006; Маккуиллан–Панаццоло» — три разных контекста: формальное (Кано), вещественно-аналитическое (Панаццоло), комплексно-аналитическое (МП, КРС, Ребело–Рейс); (2) в Брюнелле (Ann. Inst. Fourier 48:5 (1998), 1345–1357) прямо используются: локальная десингуляризация Кано, эквидесингуляризация Санчо де Салас, формула Пуанкаре–Хопфа [Литература: Brunella, введение, numdam, полный текст]. Формулировка теоремы Брюнеллы в overview.tex (аналитическое поле в окрестности $0\in\mathbb R^N$ с изолированной особой точкой, $M$ — неприводимое трёхмерное аналитическое подмножество, гладкое вне 0, инвариантное, линк с ненулевой эйлеровой характеристикой ⇒ траектория, стремящаяся к 0 при $t\to\pm\infty$) **совпадает** с оригиналом дословно по смыслу (Brunella: «Let $M\subset U$ be an analytic irreducible subvariety of dimension three, containing 0 and smooth outside 0, invariant by $v$. Suppose that the link of $M$ at 0 (which is a compact connected surface) has nonvanishing Euler characteristic. Then there exists $p\in M\setminus\{0\}$ and $T\in\{-\infty,+\infty\}$ such that $\gamma_p(t)\to0$ as $t\to T$»).

**Вердикт A-408: «подтверждено» (с точностью «насколько известно по обзору 2025 г.»): в размерности $\ge4$ полной редукции особенностей векторных полей/слоений по состоянию на март 2025 в литературе нет; известны лишь локальные результаты и случай размерности $\le3$.** Формулировка «открытая проблема» оправдана, но текст источника говорит «remains quite mysterious in high dimensions», а не «open problem»; доказательства отсутствия результата не проверялись (поиск по arXiv и ссылкам трёх источников).

---

## 5. A-419

Источник утверждений: overview.tex §1.2 «Что известно», список литературы.

| Утверждение | Результат сверки | Источник, степень |
|---|---|---|
| Гипотеза Козлова 1982 об асимптотических траекториях | Существование работы подтверждено: В. В. Козлов, «Гипотеза о существовании асимптотических движений в классической механике», Функц. анализ и его прил. 16:4 (1982), 72–73; англ.: «A conjecture on the existence of asymptotic motions in classical mechanics», Funct. Anal. Appl. 16:4 (1982), 303–304, doi:10.1007/bf01077859. **Содержание не проверено.** Каких-либо свободных пересказов формулировки не найдено (Rauch 2013 в формулировке Арнольда её не цитирует; аннотация Козлов–Трещёв 2018: «We give partial answers to such questions and present some conjectures») | [Литература: Crossref, zbMATH Zbl 0505.70024 — только заглавие; не сверено с первоисточником] |
| Bertotti–Bolotin 2000 | [Литература: zbMATH Zbl 0968.70016, рецензия Marinca; Equadiff'99 Zbl 0979.70015, summary]: «natural Lagrangian systems $(T,\Pi)$ on $\mathbb R^2$ ... there exists a $C^\infty$ potential energy $\Pi$ and two $C^\infty$ kinetic energies $T$ and $\tilde T$, such that the equilibrium $q(t)\equiv0$ is stable for the system $(T,\Pi)$ and unstable for the system $(\tilde T,\Pi)$.» Подтверждено и Burgos–Paternain 2022 (дословно «For two degrees of freedom, there exist a smooth potential U and two smooth kinetic terms Q and Q̃…»). Равенство «в аналитическом классе неверно» (Equadiff-summary) | Размерность 2 — условие. Изолированность критической точки в рецензии не сказана [не установлена]. Формулировка overview.tex («в $C^\infty$ устойчивость может зависеть от кинетической энергии») — подтверждено; добавить «при $n=2$» |
| [MN89] Moauro–Negrini, DIE 2:4 (1989) 471–478 | zbMATH Zbl 0714.70024 — рецензия недоступна («contents unavailable due to conflicting licenses»). Вторично (Alva–Garcia, введение; Burgos 2025 §1.2: «prove the existence of some asymptotic orbit assuming some non-degeneracy condition on the first non-zero jet of the potential [..] [MN]») | **не удалось проверить** по тексту; общий характер (условие на первую струю) подтверждён вторично |
| [Ta90] Taliaferro 1990 | см. п. 1.3, подтверждено по рецензии zbMATH (асимптотическая траектория при $U_p<0$ где-то; условия $C^2$ и асимптотика $U^{(i)}=U^{(i)}_p+O(\lVert x\rVert^{p+\epsilon-i})$) | рецензия |
| [Wi93] Wiener 1993 | см. п. 1.3, коранг 2 и невырожденная диаграмма Ньютона (по рецензии) | рецензия |
| Sofer 1983, ZAMP 34, 1–12 | Zbl 0509.70010, рецензии нет. Вторично: Burgos 2025 и BP22: Sofer — неустойчивость локальных максимумов для обобщённых (финслеровых) систем | не сверено с первоисточником |
| Неполнота [Pa95] признана в [BP22], [Bu21], [AR17] | **[BP22]**: «In [Pa], V. P. Palamodov stated a total instability result for non minimum critical points of the potential whose proof is incomplete. This total instability conjecture would imply the Arnold's problem and the impossibility of Ureña's example in the class of real analytic potentials as well. All of these remain as open problems.» — **подтверждено**. **[Bu21]** (arXiv:2108.05829 v4; по `2026-10-21-total-instability.md`, полный текст): «although the proof is illuminating and has very inspiring ideas, unfortunately it is not a complete argument» — **подтверждено**. **[AR17]** (HAL-препринт, §1.7 по тому же файлу): «In 1995 Palamodov [15] outlined a very interesting proof. A detailed proof has never been published.» — это **не** прямое признание неполноты: сказано, что подробного доказательства не опубликовано. | BP22 — полный текст введения (этот отчёт); Bu21, AR17 — по ранее собранному конспекту |

Дополнительно из BP22 (введение, полный текст): Arnold 1971-4 приведена дословно «Prove the instability of the equilibrium 0 of the analytic system $\ddot x=-\partial U/\partial x$ in the case where the isolated critical point 0 of the potential U is not a minimum»; пример $U=x^4+y^4-z^6$ в $\mathbb R^3$ (изолированная критическая точка не минимум, но минимум первой ненулевой струи) назван недоступным для перечисленных критериев. Это пример того же класса, что и $u_m\ge0$, но с вырожденным $Z$ (для $u_4=x^4+y^4$ условие Морса–Ботта (B2) не выполнено).

**Вердикт A-419:** «подтверждено» — Bertotti–Bolotin (при $n=2$), Taliaferro 1990, Wiener 1993 (в пределах рецензии), BP22 и Bu21 о неполноте [Pa95]; «неточно — как исправить» — AR17 (не «признание неполноты», а «outlined … detailed proof has never been published»); «не удалось проверить» — гипотеза Козлова 1982 (только заглавие), [MN89] и Sofer (только вторичные упоминания), Kozlov–Palamodov 1982.

---

## 6. Предложения по правкам `problem/KNOWN_RESULTS.md` (сам файл не правился)

1. §2, строка Alva–Garcia: добавить условия класса $\mathcal H$ (H1)–(H3) дословно; пометить, что (H3) в §1.2 написано без замыкания, а доказательства используют замыкание (п. 1.2), и что есть вероятный пробел в лемме 1 (требует проверки рецензентом).
2. §2, строки Wiener, Taliaferro 1990: добавить условия по рецензиям zbMATH (п. 1.3).
3. §5 (Burgos 2025): добавить дословные Prop. 1.3, Cor. 1.4/12.5 (п. 1.1).
4. §2 (Козлов): добавить Zbl-рецензию Kozlov 1986 (дословная формулировка в п. 1.3), заглавие Козлов 1982 ФАН 16:4.
5. Новая заметка о конечной определённости: п. 2.1 (Mather III, §9.2, Thm 3.5; Kuiper–Kuo; элементарная $\infty$-определённость).
6. Теорема Сайто: оговорить комплексную изолированность и голоморфные координаты.
7. Редукция особенностей: статус по arXiv:2503.00926 (п. 4).
8. Bertotti–Bolotin: добавить «$n=2$».
9. Allaire–Rauch: формулировка «outlined, detailed proof never published», не «признание неполноты».

## 7. Что осталось не проверенным

- Паламодов 2020: дословные Thm 3, 5, 6 (Math-Net недоступен); для $m=2$ — формулировка Thm 5.
- Kozlov–Palamodov 1982, Kozlov 1982 (ФАН 16:4), Moauro–Negrini 1989, Maffei–Moauro–Negrini 1991, Sofer 1983, Wiener 1993 (полный текст), Taliaferro 1990 (полный текст), Saito 1971.
- Контрпример к лемме 1 / теореме 1 Alva–Garcia (п. 1.2): нужна независимая проверка и проверка связности компоненты.
- Элементарное доказательство $\infty$-определённости (п. 2.1(e)): нужна независимая проверка.
