# Условие треугольности (T) мастер-теоремы: полосовые треугольные поля Эйлера ($n=3$)

- **Автор:** prover (агент), 22.10.2026. Задание главного агента: выяснить, является ли условие (T) теоремы MT
  настоящим препятствием для асимптотической траектории, и доказать вариант MT без (T) или с ослабленным условием либо
  точно объяснить, почему евклидова схема не работает.
- **Статус (кратко).** Независимой проверки нет.
  - **(T) — не препятствие при $n=3$**, если предельный профиль $Q=\lim_{s\to0}\mathcal W(s,\cdot)$ аналитичен. Тогда
    треугольное поле с неравенством Эйлера **в полосовой форме** есть всегда (теорема T, [Доказано]). Ключ — лемма P о
    полярной кривой ([Доказано], ряды Пюизё). Полосовой формы MT и достаточно, поэтому все условия MT, кроме статики
    $\mathcal W\to Q$, выполняются автоматически (теорема MT₃, [Доказано] с опорой на MT из 015, на проверке).
  - **Отбросить (T) нельзя.** В плоской карте поле, нарушающее (T) в точке русла, нарушает строгий выход (A5) при всех
    малых $s$ и при любом $U$ (предложение N$_T$, [Доказано]). Евклидова схема требует (T), но (T) всегда достижимо.
  - Препятствие предложения 6.2 [009] касается только **полной** формы $\xi Q\ge\mu Q$ с равномерными константами около нуля.
    В полосе поле существует, но $\Lambda(\delta)\to\infty$ при $\delta\to0$ ([Доказано], численно $\Lambda\asymp\delta^{-0.91}$).
  - **Следствия** ([Доказано]):
    - модель U2 (профиль 6.2, все направления узкие) — через теорему 2U [012], проверена;
    - утверждение Q [012] без условия (Q3) при $n=3$ — через 2U;
    - двойная складка O2D и пример O1 с возмущениями — через MT;
    - **весь случай (W) записки M′ без (UR) и без каких-либо полей Эйлера** (теорема W$_{\rm band}$, через MT и [M′]).
  - Динамика U2 — [Эксперимент]:
    - асимптотическая траектория есть, стрельба назад сходится сверхэкспоненциально;
    - траектория падает в подвижное дно, узкая координата «подчинена» ему;
    - свободные поперечные колебания неустойчивы в относительной мере (узкие растут как $x^{-27}$, адиабатика);
    - провал поля без (T) — поточечный: производная функции Важевского содержит быструю осциллирующую часть
      $\sim1/x$ с нулевым средним.
- **Зависит от:**
  - 015 = [`results/015-master.md`](../../results/015-master.md) — **на проверке** у рецензентов: теорема MT, лемма W
    (формула (W1)), теорема Я, лемма 0.2;
  - [007] = [`results/007-gt3.md`](../../results/007-gt3.md): теорема A, лемма 1 ((1.1), (1.3));
  - [012] = [`results/012-free-field.md`](../../results/012-free-field.md): теорема 2U, утверждение Q и его
    доказательство (§4), лемма 3;
  - [009] = [`results/009-euler-field.md`](../../results/009-euler-field.md): предложение 6.2, факты [W], [NP] из §1
    (теоремы Вейерштрасса о подготовке и Ньютона–Пюизё; там — **не сверено** с первоисточником; здесь используются в
    той же форме);
  - [008]: лемма K3 (трубчатая карта). [M′] = [`notes/prover/2026-10-21-morse-bott-mult.md`](2026-10-21-morse-bott-mult.md)
    (проверена R40, R41; в `results/` не оформлена): §1.1–1.2, лемма N1 (1.3), лемма N2(a), предложение R′ — только
    для теоремы W$_{\rm band}$;
  - пример O2D — [`notes/prover/2026-10-21-fold.md`](2026-10-21-fold.md), §6.3 (prover, не проверено), пример O1 —
    [M′], §10.2.
- **Скрипты** [Эксперимент]: [`experiments/prover/condition-T/`](../../experiments/prover/condition-T/), таблица — §6. Файлы
  прежней оборванной попытки (`model_U.py`, `band_field.py`, `exit_check*.py`, `correction_check.py`, `polar_check.py`,
  `crit_*.py`, `dynamics.py`) перепроверены и частично повторены новыми скриптами; их выводы согласуются с новыми (§6).

## 0. Ответ на вопрос задания

**Где возникает (T).** В карте MT с весами $c_1<c_2$ ($b_1$ — широкое, $b_2$ — узкое направление) у матрицы $\mathfrak N$ в (W1)
есть элемент $-s^{\mathsf a_1-\mathsf a_2}\partial_{b_2}\xi_1$. Если $\partial_{b_2}\xi_1\ne0$, он растёт при $s\to0$, и оценка
$\rho\langle w,D_wY\rangle\ge-\vartheta_3|w|^2$ в лемме M пропадает.

**Что показано.**

1. Это **не дефект оценки, а свойство функции Важевского**. При нарушении (T) строгий выход (A5) неверен в каждой точке
   русла над точкой нарушения, при всех малых $s$, независимо от $U$ (предложение N$_T$). Модификации, линейные по $v_\perp$
   (поправка $C=\lambda\langle v_\perp,\Theta\rangle$), сводятся к замене поля (§4.2, тождество (4.1)). Неевклидова поперечная метрика
   порождает силовой член порядка $\rho^{1-c_2}$ ([Эскиз], §4.2).
2. Но (T) **всегда достижимо** при $n=3$. MT требует неравенство Эйлера лишь в форме $\mathcal E_\xi\mathcal W\ge\mu(\mathcal W-\varepsilon_b\delta)-\chi$
   при **фиксированном** $\delta$ (в полосе $\varepsilon_b\delta\le\mathcal W\le\delta$, лемма 0.2 из 015). Поле
   $$\xi^\Lambda=\big(f(b_1),\ \Lambda\,\partial_{b_2}Q\big),\qquad f(b_1)=b_1\ \ (\text{изолированный нуль }Q), \tag{0.1}$$
   ему удовлетворяет при большом $\Lambda=\Lambda(\delta)$. На полярной кривой $\Pi=\{\partial_{b_2}Q=0\}$ второе слагаемое
   $\xi^\Lambda\cdot\nabla Q=f\partial_1Q+\Lambda(\partial_2Q)^2$ обращается в нуль, и работает лемма P: $b_1\partial_1Q\ge eQ$ на $\Pi$. Вне
   $\Pi$ побеждает $\Lambda(\partial_2Q)^2$ (компактность). Широкая компонента $f(b_1)$ от узкой координаты не зависит.
3. Препятствие предложения 6.2 [009] (нет поля с $\xi_1=f(b_1)$ и $\xi Q\ge\mu Q$) — это свойство полной формы: оно
   выражается в $\Lambda(\delta)\to\infty$ при $\delta\to0$ (теорема T, дополнение). MT не требует $\delta\to0$: при отсутствии конических
   направлений $\delta$ вообще не связано с полем, а при коническом широком направлении поле умножается на $\kappa\le\kappa^*(\delta)$.

**Сводка утверждений.**

| № | Утверждение | Статус |
|---|---|---|
| Л. P | на полярной кривой аналитического $Q\ge0$: $(b_1-p_1)\partial_1Q\ge e_pQ$ около точки нулевого множества | [Доказано] (через [W], [NP]); [Эксперимент] `lemma_P_check` |
| Т. T | полосовое треугольное поле (0.1) существует; $\mu$ не зависит от $\delta$; для 6.2 $\Lambda(\delta)\to\infty$ | [Доказано]; [Эксперимент] `band_T` |
| Пр. N$_T$ | без (T) выход (A5) нарушен при всех малых $s$ (плоская карта, поле 2U) | [Доказано]; [Эксперимент] `exit_check`, `exit_O2D` |
| Т. MT₃ | MT при $n=3$ без проверки (T), (E), (MT3): достаточно аналитического предельного профиля | [Доказано], опора на MT (015, на проверке) |
| Сл. U2 | модель U2 (профиль 6.2): изолированная критическая точка, не минимум; траектория есть | [Доказано]: траектория — через 2U [012]; изолированность — по модулю строгого вычисления (`crit_U2`) |
| Сл. Q′ | утверждение Q [012] верно без (Q3) при $n=3$ | [Доказано] через 2U [012] |
| Сл. O | O2D, O1 и их возмущения высшего порядка: траектория есть | [Доказано] через MT₃ |
| Т. W$_{\rm band}$ | случай (W) [M′]: траектория есть всегда (без (UR), без полей Эйлера) | [Доказано] через MT₃ и [M′] |
| Зам. (T′) | (T) можно ослабить до $\lvert s^{\mathsf a_1-\mathsf a_2}\partial_{b_2}\xi_1\rvert\le\theta_T$ ценой $m_0\mapsto m_0+C_G\theta_T$ | [Доказано] как изменение доказательства MT |
| Пр. $C^\infty$ | для $C^\infty$-профиля с изолированным нулём лемма P и теорема T неверны | [Доказано] |
| §4 | обходы (2)–(4) | тождество (4.1) — [Доказано]; метрика — [Эскиз]; (3) — не исследовалось; (4) — нарушение (R2), [Доказано] |
| §5 | динамика U2 | [Эксперимент] |
| §9 | $n\ge4$: широкий блок размерности $\ge2$ | [Гипотеза]: аналог леммы P может быть неверен |

## 1. Обозначения

Данные MT — как в 015 (разделы «Однородная калибровка», «Взвешенные карты оврага: данные»). При $n=3$ поперечных
координат две: $b=(b_1,b_2)$; **$b_1$ — координата меньшего веса** ($c_1\le c_2$; при $c_1=1$ она коническая), $b_2$ — большего.
Если $c_1>c_2$, координаты переименовываются. Условие (T) при $n=3$: $\partial_{b_2}\xi_1\equiv0$, если $c_1<c_2$.

- $\mathcal W(s,b)=s^{-\beta}U(\Psi(s,b))+a_0$ — относительный избыток; $\mathcal E_\xi\mathcal W=\xi\cdot\nabla_b\mathcal W-s\partial_s\mathcal W$.
- **Полосовая форма** неравенства Эйлера ((E) в MT с $\varepsilon_b\in(0,\frac14]$):
  $\mathcal E_\xi\mathcal W\ge\mu(\mathcal W-\varepsilon_b\delta)-\chi(s)$ на $\{\mathcal W\le\delta\}$. Ниже везде $\varepsilon_b=\frac18$.
- Для функции $Q$ двух переменных: $Z:=Q^{-1}(0)$ — нулевое множество, $\Pi:=\{\partial_2Q=0\}$ — **полярная кривая**,
  $B_r(p)$ — открытый круг.
- [W] и [NP] — теоремы Вейерштрасса о подготовке и Ньютона–Пюизё в формулировках [009], §1 (не сверены с
  первоисточником, как и там).

## 2. Утверждения

### 2.1. Лемма P (полярная кривая)

**Лемма P.** [Доказано] Пусть $\mathcal O\subset\mathbb R^2$ (или $\subset(\mathbb R/L\mathbb Z)\times\mathbb R$) открыто, $Q:\mathcal O\to[0,\infty)$
вещественно-аналитична, $p=(p_1,p_2)\in\mathcal O$, $Q(p)=0$, и функция $e\mapsto Q(p_1,e)$ не постоянна ни в какой окрестности $p_2$.
Тогда есть $r_p>0$ и $e_p>0$ такие, что

- **(P1)** $(b_1-p_1)\,\partial_1Q(b)\ \ge\ e_p\,Q(b)\ >0$ для всех $b\in(\Pi\setminus Z)\cap B_{r_p}(p)$;
- **(P2)** замыкание множества $(\Pi\setminus Z)\cap B_{r_p}(p)$ пересекает $Z\cap B_{r_p}(p)$ не более чем по точке $p$.

Если $p$ — изолированный нуль $Q$, то условие непостоянства выполнено автоматически. Уменьшив $r_p$, получаем
$Z\cap B_{r_p}(p)=\{p\}$, и (P1) верно на $\Pi\cap B_{r_p}(p)\setminus\{p\}$.

**Уточнение.** За $e_p$ годится любое число, меньшее $\min k/m$ (с меньшим $r_p$). Минимум берётся по вещественным полуветвям
$t\mapsto(p_1\pm t^m,\ p_2+\psi(t))$ кривой $\Pi$, не лежащим в $Z$; $k$ — порядок нуля $Q$ вдоль полуветви по $t$, $m$ — общий
знаменатель Пюизё. [Эксперимент `lemma_P_check`: для профиля 6.2 пределы отношения $b_1\partial_1Q/Q$ на ветвях равны
$4$ ($b_1<0$) и $4,6,7$ ($b_1>0$). Для O1 они равны $3,6$, в складках O2 — $2$. Минимум по полярным точкам круга радиуса
$0{,}5$ положителен для всех профилей (§6).]

### 2.2. Теорема T (полосовое треугольное поле Эйлера)

**Теорема T.** [Доказано] Пусть $Q:\mathcal O\to[0,\infty)$ вещественно-аналитична, $\mathcal O\subset\mathbb R\times\mathbb R$ или
$\subset(\mathbb R/L\mathbb Z)\times\mathbb R$ открыто, $\overline N\subset\mathcal O$ — компакт. Пусть $Z:=Q^{-1}(0)\cap\overline N$ лежит во внутренности
$N^\circ$, и при каждом $(b_1,b_2)\in Z$ функция $Q(b_1,\cdot)$ не постоянна ни в какой окрестности $b_2$. Тогда:

- **(a)** множество $S:=Z\cap\overline{\Pi\setminus Z}$ конечно. Пусть $\Theta_S:=\mathrm{pr}_1S$ — конечное множество значений $b_1$;
- **(b)** есть $e_*>0$ и $\rho>0$ со следующим свойством. Пусть $f$ — $C^1$-функция одной переменной $b_1$ (на $\mathrm{pr}_1\mathcal O$),
  причём $f(b_1)=b_1-\theta$ при $|b_1-\theta|<\rho$ для каждого $\theta\in\Theta_S$. Тогда для любого $\mu\in(0,e_*)$ есть $\delta_0>0$ такое, что
  при всех $\delta\in(0,\delta_0]$ и $\eta>0$ найдётся $\Lambda_0<\infty$, и при $\Lambda\ge\Lambda_0$ поле
  $$\xi^\Lambda(b):=\big(f(b_1),\ \Lambda\,\partial_2Q(b)\big)$$
  удовлетворяет
  $$\xi^\Lambda\cdot\nabla Q\ \ge\ \mu\,(Q-\eta)\qquad\text{на}\quad K_\delta:=\{b\in\overline N:\ Q(b)\le2\delta\}. \tag{2.1}$$
  Такая $f$ существует: например, $f=\sum_{\theta\in\Theta_S}(b_1-\theta)\,\chi(b_1-\theta)$, где $\chi\in C^\infty_c(-2\rho,2\rho)$, $\chi=1$ на $[-\rho,\rho]$
  (на окружности $b_1-\theta$ — представитель в $(-L/2,L/2)$; $\rho$ мало);
- **(c) изолированный нуль.** Если $Q$ определена около $0\in\mathbb R^2$, $Q\ge0$ и $0$ — изолированный нуль, то можно взять
  $f(b_1)=b_1$. Пусть $r_0:=r_p$, $e_0:=e_p$ из леммы P при $p=0$. Тогда для любого компакта $K\subset B_{r_0}(0)$, любого
  $\mu\in(0,e_0)$ и $\eta>0$ найдётся $\Lambda_0$, при котором $(b_1,\Lambda\partial_2Q)\cdot\nabla Q\ge\mu(Q-\eta)$ на $K$ для всех $\Lambda\ge\Lambda_0$.

Широкая компонента $f(b_1)$ поля не зависит от $b_2$; это (T). Число $\mu$ не зависит от $\delta$, $\eta$, $K$: от них зависит только
$\Lambda_0$. Компонента $\Lambda\partial_2Q$ аналитична, $f\in C^\infty$ (в (c) поле — многочлен, если $Q$ — многочлен).

**Дополнение (неизбежность $\Lambda\to\infty$).** [Доказано] Пусть $Q=AB$ — профиль предложения 6.2 [009], $\mu>0$, $K\supset\overline{B_\epsilon(0)}$.
Обозначим через $\Lambda_0(\eta)$ инфимум допустимых $\Lambda$ в (c). Тогда $\Lambda_0(\eta)\to\infty$ при $\eta\to0$. Численно при $\eta=\delta/8$,
$\mu=1$, $K=K_\delta\cap\overline{B_{0{,}45}}$: $\Lambda_0\approx332,\ 3{,}0\cdot10^3,\ 2{,}5\cdot10^4,\ 2{,}0\cdot10^5,\ 1{,}4\cdot10^6$ при
$\delta=10^{-4},\dots,10^{-8}$, то есть $\Lambda_0\asymp\delta^{-0.91}$ [Эксперимент `band_T`].

### 2.3. Предложение N$_T$ (без (T) евклидова схема не работает)

**Предложение N$_T$.** [Доказано] Пусть $n=3$, $1<c_1<c_2$, и задана плоская карта $\Phi(x,b)=(x,x^{c_1}b_1,x^{c_2}b_2)$. Пусть $U\in C^2$,
$F:=x^{-\beta}U\circ\Phi$, $P:=F+a_0$ ($a_0,\beta>0$), $\delta\in(0,a_0/2]$. Поле $\xi=\xi(x,b)$ класса $C^1$ в окрестности множества $\{(x,b^*):\ 0<x<x_0\}$, с ограниченными
$\xi$, $D_b\xi$, $x\partial_x\xi$. Положим $Y:=e_x+Z$, $Z_i:=x^{c_i-1}(c_ib_i-\xi_i)$ (поле (0.1) теоремы 2U [012] при $\gamma=0$, $L=I$),
$\rho:=x$, $A(r):=a_0r^\beta$. Пусть $|\partial_{b_2}\xi_1(x,b^*)|\ge c_*>0$ при малых $x$, $|P(x,b^*)|\le\delta/2$, и $\nabla_bP$, $x\partial_xP$
ограничены в точках $(x,b^*)$. Тогда при всех достаточно малых $x$ есть вектор $v$ со следующими свойствами. Точка $(q,v)$,
$q:=\Phi(x,b^*)$, удовлетворяет $E=0$, $p<0$, $V=\delta\rho^\beta$, и
$$\frac\rho\lambda\,\Xi(q,v)\ \le\ x^\beta\Big[C_1-\frac\delta3\,c_*\,x^{c_1-c_2}\Big]\ <\ 0 .$$
Значит, если $q\in\overline D$ (например, $b^*$ — точка окна, где $P<\delta$), условие (A5) теоремы A [007] с данными $(\rho,Y,A,\delta,D)$
нарушено. Это верно при любом $U$ и не зависит от способа оценки.

[Эксперимент: для U2 с полем $\xi=(\frac32b_1-\frac12b_2^2,\frac12b_2)$ (6.2(b) [009]) минимум $(\rho/\lambda)\Xi/(\delta\rho^\beta)$ равен
$-2{,}84\cdot10^7$, $-2{,}84\cdot10^9$, $-2{,}84\cdot10^{11}$ при $x=10^{-8},10^{-10},10^{-12}$ (`exit_check2.out`, прежняя попытка).
Порядок совпадает с оценкой $-\frac{K}{\delta\rho^\beta}|\partial_2\xi_1|x^{-1}$: при $K/(\delta\rho^\beta)\approx0{,}93$, $b_2\approx0{,}305$ получается $\approx-2{,}8\cdot10^{11}$
при $x=10^{-12}$. Для O2D с конической компонентой $\kappa(\theta+\varepsilon^2/2)$ — $-4{,}2\cdot10^1$ при $s=10^{-9}$ и
$-4{,}2\cdot10^4$ при $s=10^{-12}$ (`exit_O2D_level.out`), то есть $\propto s^{1-c}$.]

### 2.4. Теорема MT₃

**Теорема MT₃ ($n=3$).** [Доказано, с опорой на теорему MT (015, на проверке)] Пусть $n=3$, $U\in C^2(B_r)$, $U(0)=0$, $\nabla U(0)=0$.
Даны калибровка $(\mathcal V,\Upsilon)$, веса $1\le c_1\le c_2$ и образующая $\mathfrak P$ (015). Если $c_1=1$, то $\mathcal M_c$ — интервал или окружность
с координатой $b_1$. Пусть $\beta>0$, $a_0>0$, $\mathcal W(s,b):=s^{-\beta}U(\Psi(s,b))+a_0$, и есть компакт $\overline N$ в пространстве $b$
(при $c_1=1$ — в $\mathcal M_c\times\mathbb R$), для которого:

- **(Q)** $Q$ вещественно-аналитична на открытой окрестности $\mathcal O\supset\overline N$, $Q\ge0$ на $\mathcal O$. Множество
  $Z:=Q^{-1}(0)\cap\overline N$ непусто и лежит в $N^\circ$. При $(b_1,b_2)\in Z$ функция $Q(b_1,\cdot)$ не постоянна ни в какой окрестности
  $b_2$ (так, если $Z$ конечно или если $Q(b_1,\cdot)$ — непостоянный многочлен);
- **(L)** $\chi_L(s):=\sup_{b\in\overline N}\big(|\mathcal W-Q|+|\nabla_b(\mathcal W-Q)|+|s\partial_s\mathcal W|\big)(s,b)\to0$ при $s\to0$;
- **(R)** при некотором $s_0>0$ на $(0,s_0)\times\overline N$ выполнены (R1)–(R4) теоремы MT (с $\overline N$ вместо $\overline{\mathcal K}$). Если $c_2>1$,
  то ещё $\|\tilde G-I\|\to0$ равномерно на $\overline N$ при $s\to0$.

Тогда существует асимптотическая траектория $q(t)=\Psi(s(t),b(t))$, $s(t)\downarrow0$, $-k_2s^{\beta/2}\le\dot s\le-k_1s^{\beta/2}$. Равновесие
неустойчиво по Ляпунову, и $\beta\ge2$. Для любого достаточно малого $\delta>0$ траекторию можно выбрать с $b(t)\in\{b\in N^\circ:\ Q(b)<2\delta\}$
и $\mathcal W(s(t),b(t))\le\delta$.

Поле, неравенство Эйлера, (T) и (MT3) в условиях не фигурируют: они строятся по $Q$ (теорема T). Остаётся статика
(L) и регулярность карты (R).

### 2.5. Следствия

**Следствие U2 (модель с профилем 6.2).** Положим
$$U_2:=\hat A\hat B+y^{24}-x^{48}-x^{47}y,\qquad\hat A:=x^{12}(x^4y-z^2)^2+z^8,\qquad\hat B:=x^6(x^7y-x^3z^2-z^3)^2+z^8 .$$

- (i) [Доказано] $U_2(x,x^2b_1,x^3b_2)=x^{48}\big(-1+\tilde Q(b)-x\,b_1\big)$, где $\tilde Q:=AB+b_1^{24}$, $A=(b_1-b_2^2)^2+b_2^8$,
  $B=(b_1-b_2^2-b_2^3)^2+b_2^8$ (предложение 6.2 [009] при $x=b_1$, $y=b_2$).
- (ii) [Доказано по модулю строгого вычисления (`crit_U2.py`, python-flint)] $0$ — изолированная критическая точка $U_2$, и
  $U_2(x,0,0)=-x^{48}<0$, так что $0$ — не минимум.
- (iii) [Доказано] Весовое поле $Cb=(2b_1,3b_2)$ не удовлетворяет (Q3) [012]: в точках $(y^2+y^4,y)$ имеем
  $(Cb\cdot\nabla\tilde Q)/\tilde Q=-4/y^2+8/y+O(1)\to-\infty$. Поэтому утверждение Q [012] к $U_2$ неприменимо. Для профиля $AB$ поля с
  (T) и $\xi Q\ge\mu Q$ в полной форме нет ([009], 6.2(a)).
- (iv) [Доказано: теорема 2U [012] с полем теоремы T(c); или теорема MT₃] У $U_2$ есть асимптотическая траектория
  $q(t)=(x,x^2b_1,x^3b_2)(t)$, $x(t)\downarrow0$, $|b(t)|<r_1$, где $r_1>0$ сколь угодно мало.

**Следствие Q′ (утверждение Q [012] без (Q3)).** [Доказано через теорему 2U [012] и теорему T(c)] Пусть $n=3$ и выполнены условия
утверждения Q [012], кроме (Q3): $U$ аналитична, $N$, $c\in(1,\infty)^2$, $Nc_i\in\mathbb N$, $\beta$, $N\beta\in\mathbb N$, $\gamma$, (Q1), (Q2). Тогда есть
асимптотическая траектория $q(t)=(x(t),\gamma(x(t))+x(t)^cb(t))$, $x(t)\downarrow0$, $b(t)$ в сколь угодно малой окрестности $0$.

**Следствие O (O2D, O1 и их возмущения).** [Доказано через MT₃] Обозначения:
$\hat\theta=\sin\theta\cos\theta$, $\Psi(s,\theta,\varepsilon)=(s\cos\theta,s\sin\theta,s^c\varepsilon)$.

- $U_{\rm O2D}$ — многочлен из fold-записки, §6.3: $U_{\rm O2D}(\Psi(s,\theta,\varepsilon))=s^{32}\big(-1+A(\hat\theta,\varepsilon)B(\hat\theta,\varepsilon)\big)$, $c=2$;
- $U_{\rm O1}:=\sum_{l\le6}z^lh_l(x,y)$, $\deg h_l=4(6-l)$, $h_6=1$, — многочлен с $U_{\rm O1}(\Psi(s,\theta,\varepsilon))=s^{24}\big(-1+G_1G_2(\hat\theta,\varepsilon)\big)$,
  $c=4$, $\frac{8\sqrt3}7\le k<2$ (пример O1 [M′]; реализуемость — [Доказано] построением, проверка — `identities.py` (3)).

Пусть $U=U_{\rm O\ast}+R$, где $R\in C^2$ и $s^{-j}R(\Psi(s,\theta,\varepsilon))\to0$ вместе с $\nabla_{\theta,\varepsilon}$ и $s\partial_s$ равномерно около
$(\theta,\varepsilon)=(0,0)$ ($j=32$ или $24$). Например, $R=\sigma x^{32}y$ для O2D; тогда луч $\theta=0$ не инвариантен. Тогда у $U$ есть
асимптотическая траектория с $(\theta(t),\varepsilon(t))$ в сколь угодно малой окрестности $(0,0)$.

### 2.6. Теорема W$_{\rm band}$ (случай (W) без (UR))

**Теорема W$_{\rm band}$.** [Доказано через MT₃ (015 — на проверке) и [M′] (проверено R40, R41)] Пусть выполнены (H1)–(H4) [M′, §1.1], и
$\Sigma_0$ — компонента-кривая с $\gamma_*<\infty$ и $\min G_{\min}=:-a_0<0$ (случай (W) предложения R′ [M′]). Тогда есть асимптотическая
траектория $q(t)=s\,\omega(\theta)+s^c\varepsilon\,n(\theta)$, $s(t)\downarrow0$. При любом малом $\delta>0$ её можно выбрать с
$P(\theta(t),\varepsilon(t))<2\delta$, где $P:=\Phi_0+a_0$. Равновесие неустойчиво по Ляпунову.

**Следствие.** Теорема M′ [M′] в случае (W) верна без (UR) и без условий (W-a)–(W-f) предложений W′ [M′] и W″ (fold-записка,
§6.1). Препятствия (O1), (O2) [M′, §13] и O2D (fold-записка, §6.3) сняты. В случае (Z) условие (UR) по-прежнему используется.

### 2.7. Замечание (T′)

[Доказано как изменение доказательства MT, §3.6] В теореме MT условие (T) можно заменить на

- **(T′)** $\sup|s^{\mathsf a_i-\mathsf a_j}\partial_{b_j}\xi_i|\le\theta_T$ при $\mathsf a_i<\mathsf a_j$ (по $b\in\overline{\mathcal K}$, $\kappa$, $0<s<s_1$),

если в (MT3) и в определении $b_0$ заменить $m_0$ на $m_0':=m_0+C_G\theta_T$ ($C_G=C_P^4\Lambda^4$, как в 015) и потребовать $2m_0'<\beta-\mu_1$. В свете
предложения N$_T$ порядок $s^{\mathsf a_2-\mathsf a_1}$ для $\partial_{b_2}\xi_1$ точный. При $n=3$ (T′) не нужно: (T) достигается теоремой T.

### 2.8. Для $C^\infty$ лемма P и теорема T неверны

[Доказано] Положим $h(\sigma):=e^{-1/\sigma}\sin^2\!\big(\pi/(\sigma\ln4)\big)$ при $\sigma>0$, $h:=0$ при $\sigma\le0$, $g(\sigma):=\int_0^\sigma h$,
$Q(b):=b_1^2+g(b_2^2)$. Тогда $Q\in C^\infty$, $Q\ge0$, и $0$ — изолированный нуль (строгий минимум). При $\sigma_n:=1/(n\ln4)$ точки
$(0,\pm\sqrt{\sigma_n})$ критические, $Q=g(\sigma_n)>0$ и $g(\sigma_n)/g(\sigma_{n+1})\to4$. Значит:

- лемма P неверна: эти точки лежат на $\Pi$, но там $b_1\partial_1Q=0<eQ$;
- при каждом малом $\delta$ в интервале $(\delta/8,\delta)$ есть критическое значение $Q$. В соответствующей критической
  точке **никакое** поле не даёт $\xi\cdot\nabla Q\ge\mu(Q-\delta/8)$, так как левая часть равна нулю, а правая положительна.

## 3. Доказательства

### 3.1. Лемма P

Сдвинем $p$ в нуль: $\tau:=b_1-p_1$, $e:=b_2-p_2$, $g(\tau,e):=\partial_2Q(p+(\tau,e))$.

1. *Подготовка.* $p$ — точка минимума $Q\ge0$, так что $\nabla Q(p)=0$ и $g(0,0)=0$. Функция $g(0,e)=\frac d{de}Q(p_1,p_2+e)$ не равна
   тождественно нулю около $0$, иначе $Q(p_1,\cdot)$ постоянна около $p_2$. Пусть $d\ge1$ — порядок её нуля:
   $g(0,e)=e^d\cdot(\text{единица})$. По [W] $g=u\cdot P_W$, где $u(0)\ne0$,
   $P_W=e^d+\sum_{i=1}^da_i(\tau)e^{d-i}$, $a_i(0)=0$. По единственности и вещественности $g$ ряды $u$, $a_i$ вещественны
   (как в [009], §1, шаг 1). Выберем брус $B_0=(-\tau_0,\tau_0)\times(-e_0,e_0)$, где ряды сходятся и $u\ne0$, и уменьшим $e_0$ так, чтобы
   $g(0,e)\ne0$ при $0<|e|<e_0$. Тогда $\Pi\cap(p+B_0)=p+\{P_W=0\}\cap B_0$.
2. *Пюизё.* По [NP] (применённой к $P_W(\tau,e)$ и к $P_W(-\tau,e)$; общий знаменатель $m$) есть $t_1>0$ и
   $\varphi_j^\pm\in\mathbb C\{t\}$, $j=1,\dots,d$, сходящиеся при $|t|<t_1$, с $P_W(\pm t^m,e)=\prod_j(e-\varphi_j^\pm(t))$. Так как $P_W(0,e)=e^d$,
   все $\varphi^\pm_j(0)=0$.
3. *Вещественные корни.* Пусть $\varphi^\pm_j=\psi^\pm_j+i\eta^\pm_j$, где $\psi$, $\eta$ — ряды с вещественными коэффициентами. Если $\eta^\pm_j\not\equiv0$, то
   $\eta^\pm_j(t)\ne0$ при $0<t<t_2$ (нули аналитической функции изолированы). Пусть $J^\pm:=\{j:\ \eta^\pm_j\equiv0\}$. При $0<t<t_2$
   вещественные корни $P_W(\pm t^m,\cdot)$ — в точности $\psi^\pm_j(t)$, $j\in J^\pm$.
4. *Строение $\Pi$ около $p$.* Выберем $t_3\le t_2$ с $t_3^m<\tau_0$ и $|\psi^\pm_j(t)|<e_0$ при $|t|<t_3$. По п. 1 на $\tau=0$ в брусе лежит
   только точка $p$. Поэтому в брусе $B_1:=(-t_3^m,t_3^m)\times(-e_0,e_0)$
   $$\Pi\cap(p+B_1)=\{p\}\cup\bigcup_\pm\bigcup_{j\in J^\pm}\{\gamma^\pm_j(t):\ 0<t<t_3\},\qquad\gamma^\pm_j(t):=p+(\pm t^m,\ \psi^\pm_j(t)).$$
5. *$Q$ на полуветвях.* Функция $h(t):=Q(\gamma^\pm_j(t))$ вещественно-аналитична при $|t|<t_3$ (композиция). Она
   неотрицательна при $t>0$ и $h(0)=0$. Либо $h\equiv0$ (полуветвь лежит в $Z$), либо $h=a\,t^k(1+O(t))$ с $a>0$, $k\ge1$, и тогда
   $h(t)>0$ при малых $t>0$. Так как $\gamma^\pm_j(t)\in\Pi$, то
   $h'(t)=\partial_1Q(\gamma)\cdot(\pm mt^{m-1})+\partial_2Q(\gamma)\,\psi'(t)=\pm mt^{m-1}\partial_1Q(\gamma)$. Отсюда в точке $b=\gamma^\pm_j(t)$
   $$(b_1-p_1)\,\partial_1Q(b)=\pm t^m\cdot\frac{h'(t)}{\pm mt^{m-1}}=\frac{t\,h'(t)}m=\frac km\,h(t)\,\big(1+O(t)\big),$$
   так как $th'(t)/h(t)$ — аналитическая функция со значением $k$ в нуле.
6. *Константы.* Полуветвей с $h\not\equiv0$ конечное число. Выберем $t_4\le t_3$ так, чтобы на каждой из них при $0<t<t_4$ было
   $h(t)>0$ и $th'/h\ge k/2$ (или $\ge(1-\epsilon')k$ для уточнения). Положим $e_p:=\min k/(2m)$ по таким полуветвям ($e_p:=1$, если их нет) и
   $r_p:=\min(t_4^m,e_0)$. Точка $b\in(\Pi\setminus Z)\cap B_{r_p}(p)$ отлична от $p$ и по п. 4 лежит на полуветви $\gamma^\pm_j(t)$ с $t^m=|b_1-p_1|<r_p\le t_4^m$.
   Так как $Q(b)>0$, эта полуветвь не лежит в $Z$. По п. 5, 6 $(b_1-p_1)\partial_1Q(b)\ge e_pQ(b)>0$. Это (P1).
7. *(P2).* Пусть $b^*\in Z\cap B_{r_p}(p)$ — предел точек $\gamma(t_k)\in\Pi\setminus Z$ на полуветвях с $h\not\equiv0$, $t_k\in(0,t_4)$. Переходя к
   подпоследовательности, полуветвь одна и $t_k\to t_*\in[0,t_4]$. Случай $t_*=t_4$ невозможен: $|\gamma(t)-p|\ge t^m$, а
   $t_4^m\ge r_p>|b^*-p|$. При $t_*\in(0,t_4)$ получаем $b^*=\gamma(t_*)$ и $Q(b^*)=h(t_*)>0$, что невозможно. Значит, $t_*=0$ и $b^*=p$.
8. *Изолированный нуль.* Если $Q(p_1,\cdot)$ постоянна около $p_2$, то она равна $0$, и нуль не изолирован. Уменьшение $r_p$ до
   $Z\cap B_{r_p}(p)=\{p\}$ сохраняет (P1). $\square$

### 3.2. Теорема T

**(a).** Для каждой $p\in Z$ лемма P даёт $r_p$. Компакт $Z$ покрыт конечным числом кругов $B_{r_{p_i}}(p_i)$. Пусть
$z\in Z\cap\overline{\Pi\setminus Z}$ и $z\in B_{r_{p_i}}(p_i)$. Круг открыт, поэтому $z\in\overline{(\Pi\setminus Z)\cap B_{r_{p_i}}(p_i)}$, и по (P2) $z=p_i$. Значит,
$S\subset\{p_1,\dots,p_M\}$.

**(b).**

1. Для $p\in S$ лемма P даёт $r_p$, $e_p$. Положим $e_*:=\min_{p\in S}e_p$ ($e_*:=1$ при $S=\varnothing$) и выберем
   $\rho\le\min_{p\in S}r_p$, $\rho<\frac14\min\{|\theta-\theta'|:\ \theta\ne\theta'\in\Theta_S\}$ (на окружности — расстояние по окружности).
2. Множество $C:=\overline{\Pi\setminus Z}\cap\overline N\setminus\bigcup_{p\in S}B_\rho(p)$ компактно. Оно не пересекается с $Z$, так как
   $\overline{\Pi\setminus Z}\cap Z=S\subset\bigcup B_\rho(p)$. Значит, $d:=\min_CQ>0$ ($d:=\infty$ при $C=\varnothing$). Положим $\delta_0:=d/4$.
3. Пусть $\delta\le\delta_0$, $\eta>0$, $g:=f\,\partial_1Q-\mu(Q-\eta)$. Покажем, что $g>0$ на $\Pi\cap K_\delta$.
   - Если $b\in Z$, то $\nabla Q(b)=0$ (минимум) и $g(b)=\mu\eta>0$.
   - Если $b\in(\Pi\setminus Z)\cap K_\delta$, то $Q(b)\le2\delta<d$, поэтому $b\notin C$, и $b\in B_\rho(p)$ для некоторой $p\in S$. Тогда
     $|b_1-p_1|<\rho$ и $f(b_1)=b_1-p_1$. По (P1) $f\,\partial_1Q=(b_1-p_1)\partial_1Q\ge e_pQ\ge e_*Q$, откуда $g(b)\ge(e_*-\mu)Q+\mu\eta>0$.
4. Множество $Z':=\{b\in K_\delta:\ g(b)\le0\}$ компактно и не пересекает $\Pi$, так что $c:=\min_{Z'}(\partial_2Q)^2>0$. Положим
   $\Lambda_0:=\max_{Z'}|g|/c$ ($\Lambda_0:=0$ при $Z'=\varnothing$). При $\Lambda\ge\Lambda_0$ на $Z'$
   $\xi^\Lambda\cdot\nabla Q-\mu(Q-\eta)=g+\Lambda(\partial_2Q)^2\ge-\max|g|+\Lambda_0c\ge0$, а вне $Z'$ имеем $g>0$ и $\Lambda(\partial_2Q)^2\ge0$. Это (2.1).
   Существование $f$ очевидно: носители слагаемых не пересекаются, так как $4\rho<\min|\theta-\theta'|$.

**(c).** По лемме P при $p=0$ на $(\Pi\setminus\{0\})\cap B_{r_0}$ выполнено $b_1\partial_1Q\ge e_0Q>0$, и $Z\cap B_{r_0}=\{0\}$. Для $g:=b_1\partial_1Q-\mu(Q-\eta)$ на
$\Pi\cap K$ имеем $g(0)=\mu\eta$ и $g\ge(e_0-\mu)Q+\mu\eta>0$ в остальных точках. Далее — п. 4. $\square$

**Дополнение.** Пусть $\Lambda_0(\eta_k)\le\bar\Lambda$ вдоль $\eta_k\to0$. При увеличении $\Lambda$ неравенство сохраняется ($(\partial_2Q)^2\ge0$), поэтому
$\xi^{\bar\Lambda}\cdot\nabla Q\ge\mu(Q-\eta_k)$ на $K$ при всех $k$, и $\xi^{\bar\Lambda}\cdot\nabla Q\ge\mu Q$ на $K\supset\overline{B_\epsilon}$. Поле $\xi^{\bar\Lambda}=(b_1,\bar\Lambda\partial_2(AB))$ —
многочлен, то есть липшицево на $B_\epsilon$, и $\xi_1=b_1$ не зависит от $b_2$. Это противоречит [009], предложение 6.2(a). $\square$

### 3.3. Предложение N$_T$

1. *Точка (A5).* Пусть $q=\Phi(x,b^*)$, $W=U+A(\rho)=x^\beta P(x,b^*)$, $K:=\delta\rho^\beta-W\in[\frac\delta2x^\beta,\frac{3\delta}2x^\beta]$, $h=|Y|^2=1+|Z|^2\in[1,2]$
   при малых $x$. Положим $\lambda:=\sqrt{2(A(\rho)-\delta\rho^\beta)/h}>0$ ($A-\delta\rho^\beta\ge\frac{a_0}2\rho^\beta$) и $v:=-\lambda Y+\sqrt{2K}\,\hat w$, где $\hat w\perp Y$,
   $|\hat w|=1$ выбран в п. 4. Тогда $\frac12|v|^2+U=A-\delta\rho^\beta+K+U=A-W+U=0$, $p=-\lambda h<0$, $V=K+W=\delta\rho^\beta$.
2. *Тождество.* По (1.3) [007] $\frac\rho\lambda\Xi=\big[\beta\delta\rho^\beta-\rho YW\big]+T_1+T_2+T_3$. Здесь $\beta\delta\rho^\beta-\rho YW=\beta K+(\beta W-\rho YW)$ и
   $\beta W-\rho YW=-x^{\beta+1}YP=x^\beta\big(\xi\cdot\nabla_bP-x\partial_xP\big)$. Действительно, $YP=\partial_xP|_y+Z\cdot\nabla_yP=\partial_xP|_b-\frac1x\xi\cdot\nabla_bP$, так как
   $x\partial_x|_yb_i=-c_ib_i$ и $Z_i\partial_{y_i}=x^{-1}(c_ib_i-\xi_i)\partial_{b_i}$. Значит, $|\beta\delta\rho^\beta-\rho YW|\le C x^\beta$.
3. *$T_1$, $T_2$.* $\nabla\rho=e_x$, $|\nabla\rho-Y/h|\le|Z|$ (лемма G (G1) из 015 с $\nu=e_x$, $Y_T=Z$), $\lambda\ge c\,x^{\beta/2}$, $|v_\perp|\le\sqrt{3\delta}\,x^{\beta/2}$, $|A'|\le\beta a_0x^{\beta-1}$.
   Поэтому $|T_1|\le Cx^\beta|Z|$. Далее $x\nabla_YY=x\partial_xZ+\sum_jZ_j\,x\partial_{y_j}Z$. Прямой подсчёт:
   $x\partial_xZ_i=x^{c_i-1}\big[-c_ib_i-(c_i-1)\xi_i+\sum_jc_jb_j\partial_j\xi_i-x\partial_x\xi_i\big]$ и
   $Z_j\,x\partial_{y_j}Z_i=x^{c_i-1}(c_jb_j-\xi_j)(c_i\delta_{ij}-\partial_j\xi_i)$. Отсюда $|x\nabla_YY|\le Cx^{c_1-1}$ и $|T_2|\le\lambda|v_\perp|Cx^{c_1-1}\le Cx^\beta$.
4. *$T_3$.* Для $w=(w_x,w_y)\perp Y$ имеем $w_x=-\langle Z,w_y\rangle$, $D_wY=(0,\ w_x\partial_xZ+\sum_jw_{y_j}\partial_{y_j}Z)$ и
   $$x\langle w,D_wY\rangle=\langle w_y,Mw_y\rangle+w_x\langle w_y,x\partial_xZ\rangle,\qquad M_{ij}=x\,\partial_{y_j}Z_i=x^{c_i-c_j}\big(c_i\delta_{ij}-\partial_j\xi_i\big)$$
   [символьно: `identities.py` (2)]. Возьмём $w_y:=(1,\sigma_*)/\sqrt2$, $\sigma_*:=\operatorname{sign}\partial_2\xi_1(x,b^*)$, и соответствующее $w$. Тогда
   $\langle w_y,Mw_y\rangle=\frac12\big[c_1-\partial_1\xi_1+c_2-\partial_2\xi_2-x^{c_1-c_2}|\partial_2\xi_1|-\sigma_*x^{c_2-c_1}\partial_1\xi_2\big]\le C-\frac12c_*x^{c_1-c_2}$, а
   $|w_x\langle w_y,x\partial_xZ\rangle|\le|Z|\,|x\partial_xZ|\to0$ и $|w|^2=1+O(|Z|^2)$. Для $\hat w=w/|w|$ при малых $x$ получаем
   $x\langle\hat w,D_{\hat w}Y\rangle\le C-\frac13c_*x^{c_1-c_2}$. Тогда $T_3=\rho\langle v_\perp,D_{v_\perp}Y\rangle=2K\cdot x\langle\hat w,D_{\hat w}Y\rangle\le3C\delta x^\beta-\frac\delta3c_*x^\beta x^{c_1-c_2}$
   (использовано $\frac\delta2x^\beta\le K\le\frac{3\delta}2x^\beta$).
5. Сложим пп. 2–4: $\frac\rho\lambda\Xi\le x^\beta\big[C_1-\frac\delta3c_*x^{c_1-c_2}\big]$, и $x^{c_1-c_2}\to\infty$. $\square$

Замечание. Для общей калибровки MT рассуждение то же: (G3) из 015 и (W1). Мешают лишь члены вида
$\alpha\,\mathbf k^{\mathsf T}(I+D_\vartheta v)\tau$ с $|\alpha|\le\Lambda^2|Y_T|$, которые тоже содержат большой элемент $\mathfrak N$. Поэтому вне плоской карты нужно
$|Y_T|$ мало (так при $I_c=\varnothing$ и при малом $\kappa$). Здесь это не выписано.

### 3.4. Теорема MT₃

1. *Окно.* Применим теорему T к $Q$, $\overline N$: получаем $S$, $e_*$, $\rho$, $\delta_0$. Возьмём $f$ из теоремы T(b) (при $Z=\{p\}$ можно $f=b_1-p_1$),
   $\mu:=e_*/2$ и $\delta\in(0,\min(\delta_0,\frac{a_0}2,\frac14\min_{\partial\overline N}Q)]$ ($Q>0$ на $\partial\overline N$, так как $Z\subset N^\circ$). Положим
   $\mathcal K:=\{b\in N^\circ:\ Q(b)<2\delta\}$. Оно открыто, $\overline{\mathcal K}\subset\{Q\le2\delta\}\cap\overline N=K_\delta$, и $\overline{\mathcal K}$ не пересекает $\partial\overline N$ (там $Q>2\delta$), так что
   $\overline{\mathcal K}\subset N^\circ$ компактно. Если $b\in\partial\mathcal K$, то $b\in N^\circ$, $b\notin\mathcal K$, то есть $Q(b)\ge2\delta$, и $Q(b)\le2\delta$ по
   непрерывности: $Q=2\delta$ на $\partial\mathcal K$. Наконец, $Z\subset\mathcal K$.
2. *Поле.* По теореме T(b) с $\eta:=\delta/8$ есть $\Lambda$ такое, что $\xi^1:=(f(b_1),\Lambda\partial_2Q)$ удовлетворяет $\xi^1\cdot\nabla Q\ge\mu(Q-\delta/8)$ на $K_\delta$.
   Поле $\xi^1$ класса $C^1$ на открытом $\mathcal M:=N^\circ\cap\mathcal O\supset\overline{\mathcal K}$. Положим $M_0:=\max_{K_\delta}|\xi^1|$, $M_1:=\max_{K_\delta}\|D\xi^1\|$
   (теорема MT использует $\mathcal M$ лишь как область определения карты и поля, содержащую $\overline{\mathcal K}$, — 015, доказательство леммы 5.1).
3. *(E) для $\nu\xi^1$, $\nu\in(0,1]$.* На $(0,s_1)\times\overline{\mathcal K}$
   $$\nu\xi^1\cdot\nabla_b\mathcal W-s\partial_s\mathcal W=\nu\xi^1\cdot\nabla Q+\nu\xi^1\cdot\nabla_b(\mathcal W-Q)-s\partial_s\mathcal W\ \ge\ \nu\mu(Q-\tfrac\delta8)-(M_0+1)\chi_L\ \ge\ \nu\mu(\mathcal W-\tfrac\delta8)-\chi,$$
   где $\chi:=(M_0+1+\mu)\chi_L\to0$ и $\varepsilon_b=\frac18$.
4. *Семейство полей MT по случаям.*
   - $c_1>1$ ($I_c=\varnothing$): $\xi:=t\,\xi^1$ с $t:=\min(1,1/M_1,\beta/(2\mu))$. В (E) $\mu_1=t\mu<\beta$, $\mu_0=0$. (T): $\xi_1=tf(b_1)$ не зависит от $b_2$.
     (MT3a): $\|\tilde G-I\|\to0$ по (R), и каждый узкий блок $\operatorname{sym}(c_JI-tD_{b_J}\xi^1_J)\succeq(c_J-tM_1)I\succeq0$ ($c_J>1\ge tM_1$), так что
     $m_0=0$. (R5): $K_n:=\max(M_0,M_1)$, $s\partial_s\xi=0$, $R<\infty$.
   - $c_1=1<c_2$: $\xi^{(\kappa)}:=\kappa\xi^1$, $\kappa\in(0,\kappa_0]$, $\kappa_0:=\min(1,1/M_1)$. Коническая часть $\xi^c=f(b_1)$ не зависит от $\kappa$ и от $b_2$;
     узкая $\xi^{(\kappa)}_n=\kappa\Lambda\partial_2Q$. (R5): $K_0:=\max|f|$, $K_1:=\max|f'|$, $K_s:=0$, $K_n:=\max(M_0,M_1)$ равномерно по $\kappa$. (MT3a):
     узкий блок $c_2-\kappa\Lambda\partial_2^2Q\ge c_2-1>0$, $m_0=0$. (E): $\mu(\kappa)=\kappa\mu$, $\mu_1=0$, $\mu_0=\mu$.
   - $c_1=c_2=1$: $\xi^{(\kappa)}:=\kappa\xi^1$ — всё коническое, $\xi^c:=\xi^1$; (MT3b) даёт $m_0=0$; $K_0:=M_0$, $K_1:=M_1$; $\mu(\kappa)=\kappa\mu$.
5. *(MT1).* Уменьшим $s_1$ так, чтобы $\chi_L<\delta$ на $(0,s_1)$. (W): на $\partial\mathcal K$ $\mathcal W\ge Q-\chi_L=2\delta-\chi_L>\delta$. (B): для $b_0\in Z\subset\mathcal K$
   $\mathcal W(s,b_0)\le\chi_L$. (F): $\mathcal W\ge Q-\chi_L\ge-\chi_L$ на $\overline{\mathcal K}$. (E) — п. 3. (MT2): (R1)–(R4) — из (R) ($\overline{\mathcal K}\subset\overline N$), (R5) — п. 4.
   (MT3) — п. 4.
6. *Вывод.* Теорема MT даёт $\kappa^*>0$ и при $\kappa\le\min(\kappa_0,\kappa^*)$ траекторию с $b(t)\in\mathcal K$ и $\mathcal W\le\delta$. $\square$

### 3.5. Следствия

**U2.**

- (i) $\hat A(x,x^2b_1,x^3b_2)=x^{12}(x^6b_1-x^6b_2^2)^2+x^{24}b_2^8=x^{24}A$; $\hat B=x^6(x^9b_1-x^9b_2^2-x^9b_2^3)^2+x^{24}b_2^8=x^{24}B$; $y^{24}=x^{48}b_1^{24}$;
  $x^{47}y=x^{49}b_1$. [Символьно: `model_U.py`.]
- (ii) Пусть $U_0:=\hat A\hat B+y^{24}-x^{48}$ (квазиоднородный: веса $(1,2,3)$, степень $48$) и $U_1:=-x^{47}y$ (вес $49$).
  - *$\nabla U_0\ne0$ вне нуля.* При $x\ne0$ $U_0=x^{48}F_0(b)$, $F_0=-1+\tilde Q$, и $\nabla U_0=0$ равносильно $\nabla\tilde Q(b)=0$, $48F_0-2b_1\partial_1F_0-3b_2\partial_2F_0=0$, то
    есть $\nabla\tilde Q=0$ и $\tilde Q(b)=1$. По `crit_U2.py` у $\tilde Q$ одна вещественная критическая точка $b=0$ со значением $0\ne1$:
    - результант $R(b_2)=\operatorname{Res}_{b_1}(\partial_1\tilde Q,\partial_2\tilde Q)$ равен $b_2^{57}$, умноженному на неприводимый многочлен степени 288 без вещественных
      корней (строгая изоляция в FLINT);
    - старший коэффициент $\partial_1\tilde Q$ по $b_1$ — константа $24$, так что у вещественной критической точки $b_2$ — корень $R$, то есть $b_2=0$;
    - $\partial_1\tilde Q(b_1,0)=4b_1^3(6b_1^{20}+1)$.

    При $x=0$ $U_0(0,y,z)=y^{24}+z^{16}$ и $\partial_yU_0=24y^{23}$, $\partial_zU_0=16z^{15}$, так как члены с $x^{12}$, $x^6$ дают нулевой вклад.
  - *Изолированность.* Пусть $N(q):=|x|+|y|^{1/2}+|z|^{1/3}$ и $\mathsf M(q):=\sum_i|\partial_iU_0(q)|^{1/(48-w_i)}$, $w=(1,2,3)$. Функция $\mathsf M$ квазиоднородна
    степени $1$, непрерывна и положительна на компакте $\{N=1\}$, поэтому $\mathsf M\ge m_*N$. Далее $|\partial_xU_1|=47|x^{46}y|\le CN^{48}$ и $|\partial_yU_1|=|x|^{47}\le N^{47}$.
    В критической точке $U$ имеем $\partial_iU_0=-\partial_iU_1$, откуда $\mathsf M\le C'N^{1+1/47}$ при $N\le1$ и $N\ge(m_*/C')^{47}$. Других критических точек
    около нуля нет.
  - $U_2(x,0,0)=-x^{48}$.
- (iii) Подстановка: `identities.py`/sympy-ряд даёт $(Cb\cdot\nabla Q)/Q|_{(y^2+y^4,y)}=-4y^{-2}+8y^{-1}+O(1)$ для $Q=AB$ и $Q=\tilde Q$. Вручную: при
  $b_1=y^2+\eta$ имеем $Cb\cdot\nabla\log A=\frac{\eta(4\eta-8y^2)+24y^8}{\eta^2+y^8}$, при $\eta=y^4$ это $-4y^{-2}+O(1)$, а $|Cb\cdot\nabla\log B|=O(y^{-1})$. Значит, (Q3) не
  выполнено ни в какой окрестности нуля.
- (iv) Теорема 2U [012]. Данные: $N=1$, $c=(2,3)$, $\beta=48$, $\gamma=0$, $L=I$, $F=-1+\tilde Q-xb_1$, $a_0=1$, $P=\tilde Q-xb_1$.
  1. Теорема T(c) для $\tilde Q$ (изолированный нуль) даёт $r_0$, $e_0$. Выберем $r_1<r_0':=\min(r_0,1)$, $\mu:=e_0/2$, $q_1:=\min_{|b|=r_1}\tilde Q>0$,
     $\delta:=\min(\frac12,\frac{q_1}4)$, $K:=\{|b|\le r_1,\ \tilde Q\le2\delta\}$, $\eta:=\delta/8$. Получаем $\Lambda$ с $\xi^1=(b_1,\Lambda\partial_2\tilde Q)$ и $\xi^1\cdot\nabla\tilde Q\ge\mu(\tilde Q-\delta/8)$ на $K$.
  2. Положим $\xi:=t\xi^1$, $t:=\min\big(1,\ 3/(\Lambda\max_{|b|\le r_0'}|\partial_2^2\tilde Q|+1)\big)$, $r_0:=r_0'$ в данных 2U. Тогда (T): $\partial_2\xi_1=0$. (Θ): блоки
     одномерны, $2-t\ge0$, $3-t\Lambda\partial_2^2\tilde Q\ge0$. $|\xi|$, $\|D\xi\|$ ограничены, $s\partial_s\xi=0$.
  3. Условия 2U:
     - (U1): $b_0=0$, $P(s,0)=0$;
     - (U2): $P\ge-xr_1$;
     - (U3): $P\ge q_1-xr_1\ge2\delta$ при малых $x$;
     - (U4): на $\{|b|<r_1,\ P\le\delta\}\subset K$ (при $xr_1\le\delta$)
       $\xi\cdot\nabla_bF-x\partial_xF=t\xi^1\cdot\nabla\tilde Q-tx\,\xi^1_1+xb_1=t\xi^1\cdot\nabla\tilde Q+(1-t)xb_1\ge t\mu(\tilde Q-\frac\delta8)-xr_1\ge t\mu(P-\frac\delta8)-(1+t\mu)xr_1$
       (здесь $\nabla_bF=\nabla\tilde Q-xe_1$, $x\partial_xF|_b=-xb_1$, $\xi^1_1=b_1$, $\tilde Q=P+xb_1\ge P-xr_1$).
       Это (U4) с $\mu_{2U}:=t\mu\le\beta$, $\varepsilon_E:=\mu_{2U}\delta/8$, $\eta(s):=C's$.
  4. Теорема 2U даёт траекторию с $|b(t)|<r_1$. По MT₃ то же получается напрямую (плоская калибровка, $\mathfrak P=u$, $\Theta=(xb_1,x^2b_2)$, $G=I$).

**Q′.** Как в доказательстве утверждения Q [012], §4, пп. 1–2:

1. $\gamma$ — ряд Пюизё с показателями $>1$, так что $\gamma,\gamma',x\gamma''\to0$.
2. $F(s,b)\to F_0(b)$ вместе с $\nabla_bF$ равномерно на $\overline{B_{r_0}}$, и $\sup|s\partial_sF|\to0$ (лемма 3 [012]).
3. $Q:=F_0-F_0(0)$ — многочлен со строгим локальным минимумом в $0$ по (Q2), то есть с изолированным нулём.
4. Дальше — дословно п. (iv) выше: теорема T(c) для $Q$ (с переименованием координат, если $c_1>c_2$; при $c_1=c_2$ (T) не нужно), $\xi=t\xi^1$,
   (Θ) масштабированием, (U1)–(U4) с $\eta(s)$, мажорирующей $|F-F_0|+|\nabla_b(F-F_0)|+|s\partial_sF|/N$ (умноженной на постоянную).
5. Теорема 2U даёт траекторию. $\square$

**O.**

1. *Калибровка и карта.* Трубчатая калибровка у экватора: $\omega=(\cos\theta,\sin\theta,0)$, $n=e_z$, $k_g=0$, $\Upsilon(\theta,y)=\omega+ye_z$. Тогда
   $\Pi(s,\theta,y)=(s\cos\theta,s\sin\theta,sy)$ — цилиндрические координаты, диффеоморфизм на $\{s>0\}$. Веса $(1,c)$, $\mathfrak P=u$,
   $\Theta=(\theta,s^{c-1}\varepsilon)$. (R1)–(R4): $\Theta$ лежит в компакте $[-\theta_1,\theta_1]\times[-s_1^{c-1}E,s_1^{c-1}E]$, $\mathfrak P_u=I$, $\pi\equiv0$, $\Upsilon_T=ye_z$ с $|y|=s^{c-1}|\varepsilon|\to0$.
   $G=\operatorname{diag}((1-k_gy)^2,1)=I$ (015, калибровка (T)).
2. *Профиль.* $Q:=P=AB(\hat\theta(\theta),\varepsilon)$ или $G_1G_2(\hat\theta,\varepsilon)$ аналитична. Около $(0,0)$ $\hat\theta$ — аналитическая замена ($\hat\theta'(0)=1$), а у
   $AB$ и $G_1G_2$ нуль $0$ изолирован. Для $AB$: $A=0$ только при $b_1=b_2^2$, $b_2=0$, то же для $B$ ([009], доказательство 6.2(a)). Для $G_1G_2$ дискриминант $G_1$ по $e$ равен
   $(k^2-4)\hat\theta^4<0$ при $k<2$, $\hat\theta\ne0$, так что $G_1>0$ вне нуля; то же для $G_2$ по $\hat\theta$.
3. *(L).* Для $U_{\rm O\ast}$ имеем $\mathcal W\equiv Q$ точно. Добавка $R$ даёт $\chi_L\to0$ по условию. MT₃ применима с $\overline N$ — маленький квадрат около $(0,0)$.
4. *Реализуемость O1.* У $-1+G_1G_2$ каждый моном $\hat\theta^k\varepsilon^l$ имеет $2k\le4(6-l)$ (`identities.py` (3)). Поэтому
   $h_l:=\sum_ka_{lk}(xy)^k(x^2+y^2)^{2(6-l)-k}$ ($h_0$ — с добавкой $-(x^2+y^2)^{12}$) — однородные многочлены степени $4(6-l)$, и
   $U_{\rm O1}(\Psi)=s^{24}\Phi_0$ тождественно. Младшая форма — $z^6$, $\Sigma$ — экватор. $\square$

**W$_{\rm band}$.**

1. *Карта.* $(\mathcal V,\Upsilon)$ — трубчатая калибровка $\Sigma_0$: $\mathcal V=\mathbb R/L\mathbb Z\times(-t_1,t_1)$, $\Upsilon(\theta,y)=\omega(\theta)+y\,n(\theta)$.
   $\Pi=s\Upsilon$ — инъективное погружение по лемме K3 [008] ([M′], §1.2). Веса $(1,c)$, $c=1+\gamma_*$, $\mathfrak P=u$, $\Theta(s,\theta,\varepsilon)=(\theta,s^{c-1}\varepsilon)$,
   $\Psi=s\omega+s^c\varepsilon n$. (R1)–(R4) и $\tilde G=\operatorname{diag}((1-k_gs^{c-1}\varepsilon)^2,1)\to I$ — как в п. 1 выше, при $s_1^{c-1}E_1<t_1$.
2. *Статика.* По (1.3) [M′] $\mathcal W:=s^{-j}U(\Psi)+a_0=\tilde U(s^{1/N},\theta,\varepsilon)+a_0$ при $|\varepsilon|\le E'$, где $\tilde U$ аналитична около
   $[-\sigma_1,\sigma_1]\times\mathbb R\times[-E',E']$ и $L$-периодична. Значит, (L) выполнено с $Q:=P=\Phi_0+a_0$ на $\overline N:=\mathbb R/L\mathbb Z\times[-E_1,E_1]$, $E_0<E_1<E'$:
   $s\partial_s\mathcal W=\frac\sigma N\partial_\sigma\tilde U\to0$.
3. *(Q).* $P\ge0$ (так как $\Phi_0\ge G_{\min}\ge-a_0$), аналитична на $\mathbb R/L\mathbb Z\times\mathbb R$. $Z=P^{-1}(0)\cap\overline N=F_{\min}$ компактно и лежит в
   $\{|\varepsilon|<E_0\}\subset N^\circ$ (лемма N2(a) [M′]: точки глобального минимума $\Phi_0(\theta,\cdot)$ лежат в $(-E_0,E_0)$). $P(\theta,\cdot)$ — многочлен степени
   $2r$ со старшим коэффициентом $a(\theta,0)>0$, то есть не постоянен.
4. MT₃ при $c_1=1<c_2=c$ (коническая $\theta$, узкая $\varepsilon$) даёт траекторию. Множество $\Theta_S$ конечно, $f$ — функция на окружности $\mathbb R/L\mathbb Z$. $\square$

### 3.6. Замечание (T′): изменения в доказательстве MT

Условие (T) в доказательстве MT (015, §7) используется в одном месте — в разборе (W1) по блокам и в (5.1): элементы
$s^{\mathsf a_i-\mathsf a_j}\partial_{b_j}\xi_i$ с $\mathsf a_i<\mathsf a_j$ полагаются нулевыми. Других мест нет:

- (W0) и (W2) содержат только $s^{\mathsf A}$ (неотрицательные степени);
- (W3) содержит $D_\vartheta v$, которое оценивается через $\|I+D_\vartheta v\|$.

При (T′) эти элементы образуют матрицу $E_T$ с $\|E_T\|\le\theta_T$ (для $n=3$ — один элемент; в общем случае
$\le(n-1)\theta_T$). Её добавляем к $E$ в (5.1). Тогда:

1. в п. 5 доказательства MT $\|I+D_\vartheta v\|\le C_P^2(1+\mathsf a^*+K_n+K_1+e_E+\theta_T)$, то есть $C_v$ конечно;
2. в оценке (H5) появляется слагаемое $-\theta_T\|\tilde G\||\tilde\tau|^2\ge-\theta_TC_G\,\tilde\tau^{\mathsf T}\tilde G\tilde\tau$, и $m=m_0+C_G\theta_T+\kappa K_1C_G$;
3. в (5.2) $m_0$ заменяется на $m_0'$, и $b_0:=\beta-\mu_1-2m_0'>0$.

Остальное без изменений. [Доказано при условии, что 015 верно в остальном; рецензенту — проверить, что (T) больше нигде не
используется.]

### 3.7. Пример §2.8

- $h\in C^\infty$, и $h$ плоская в нуле: производные $\sin^2(\pi/(\sigma\ln4))$ растут полиномиально по $1/\sigma$ и подавляются $e^{-1/\sigma}$.
  Поэтому $g\in C^\infty$ плоская, $Q\in C^\infty$.
- $h\ge0$ и не равна нулю ни на каком интервале, так что $g>0$ при $\sigma>0$.
- $\nabla Q=(2b_1,\ 2b_2h(b_2^2))$ обращается в нуль при $b_1=0$, $b_2^2=\sigma_n$.
- Подстановка $w=1/u$: $g(\sigma_n)=\int_{n\ln4}^\infty e^{-w}\sin^2(\pi w/\ln4)w^{-2}dw=4^{-n}\int_0^\infty e^{-t}\sin^2(\pi t/\ln4)(n\ln4+t)^{-2}dt$, откуда
  $g(\sigma_n)/g(\sigma_{n+1})\to4<8$.
- Соседние критические значения отличаются меньше чем в 8 раз, поэтому интервал $(\delta/8,\delta)$ при малом $\delta$ содержит
  хотя бы одно из них. $\square$

## 4. Обходы из задания (б)

### 4.1. Полосовое поле — работает

Это теоремы T и MT₃. Для профиля 6.2 и для O2D поле $(b_1,\Lambda\partial_2Q)$, соответственно $(\theta,\Lambda\partial_\varepsilon P)$, удовлетворяет полосовому
неравенству на всём $K_\delta$ (`band_T.out`). Минимальный запас равен $0{,}33$–$0{,}37\,\mu\eta$ на $(1{,}4$–$1{,}9)\cdot10^6$ проверочных точках при
$\Lambda=1{,}5\Lambda_0$. Строгий выход (A5) в $\mathbb R^3$ подтверждён прямым дифференцированием [Эксперимент]:

- для U2 (поле 2U, прежняя попытка, `exit_check.out`, `exit_check2.out`) минимум $(\rho/\lambda)\Xi/(\delta\rho^\beta)$ равен $0{,}237$ при $x=10^{-12}\dots10^{-20}$
  ($0{,}145$ в полярных точках полосы);
- для O2D с $\sigma=-1$ (коническое широкое направление, $\xi=\kappa(\theta,\Lambda\partial_\varepsilon P)$, `exit_O2D_level.out`) на уровне $\mathcal W=\delta$
  ($K_\perp=0$) $\min N/\kappa\approx3{,}86$–$3{,}95$ при $\kappa=10^{-5},\dots,10^{-2}$, $s=10^{-9},10^{-12}$. При $K_\perp=10^{-3}\delta\rho^\beta$ и $\kappa=10^{-2}$ выход
  нарушается ($N/\kappa\approx-3{,}5$), а при $\kappa\le10^{-3}$ — нет. Это согласуется с ограничением $\kappa\lesssim\kappa^*\asymp\delta/K_0^2$ теоремы MT ($\delta=10^{-4}$,
  $K_0\approx0{,}3$).

### 4.2. Изменённая функция Важевского

**Линейные по $v_\perp$ поправки — это замена поля.** [Доказано; символьно `identities.py` (1)] Пусть $Y'=Y+\Theta$, $v=-\lambda Y+v_\perp$, $v_\perp\perp Y$,
$h=|Y|^2$, $h'=|Y'|^2$, $V_Y=\frac12|v|^2-\langle v,Y\rangle^2/(2h)+W$. Тогда
$$V_{Y'}-V_Y=\frac{\lambda^2h|\Theta|^2+2\lambda h\langle v_\perp,\Theta\rangle-\big(\langle v_\perp,\Theta\rangle-\lambda\langle Y,\Theta\rangle\big)^2}{2h'}=\lambda\langle v_\perp,\Theta\rangle+O(|\Theta|^2|v|^2). \tag{4.1}$$
Поправка $C=\lambda\langle v_\perp,\Theta\rangle$ с $\Theta=x^{c_1-1}G(b)e_y$, $G=\xi_1(b)-\xi_1(b_1,0)$, — это линеаризация перехода к полю $\xi'=(\xi_1(b_1,0),\xi_2)$ с (T). Это
объясняет совпадение $N_C$ и $N_{Y'}$ в `correction_check.out` (прежняя попытка): $|N_C-N_{Y'}|\le8\cdot10^{-6}$ при $x=10^{-6}$, $c=(3,4)$. Остаток второго
порядка в (4.1) после дифференцирования и нормировки имеет порядок $x^{2c_1-1-c_2}$ ([Эскиз]: производная $\Theta$ по узкой
координате равна $x^{c_1-1-c_2}\partial_2G$; численно подтверждено в `correction_check.out`). Он мал при $2c_1-1>c_2$, но при $c=(2,3)$ не мал. Значит, такие поправки ничего
не добавляют к выбору поля: поле $\xi'$ с (T) всё равно должно удовлетворять неравенству Эйлера, и вопрос сводится к теореме T.

**Неевклидова поперечная метрика.** [Эскиз] Пусть $V_M:=V+\frac12\langle v_\perp,\mathsf N v_\perp\rangle$, $\mathsf N=\mathsf N(q)$ симметрична, $\mathsf NY=0$. Тогда
$$\dot V_M-\dot V=-\langle v_\perp,\mathsf N\nabla U\rangle+\lambda\langle v_\perp,\mathsf N\,D_vY\rangle+\tfrac12\langle v_\perp,(D_v\mathsf N)v_\perp\rangle\qquad(\text{из }\dot v_\perp=-\nabla U-\tfrac d{dt}(p/h)\,Y-(p/h)D_vY).$$
Силовой член: узкая компонента $\nabla U$ равна $x^{\beta-c_2}\partial_2F$. После нормировки $\rho/(\lambda\delta\rho^\beta)$ он имеет порядок
$|\mathsf Ne_2|\,\rho^{1-c_2}|\partial_2Q|/\sqrt\delta$. Чтобы он был ограничен, нужно $|\mathsf Ne_2|=O(\rho^{c_2-1})$. Но тогда вклад $\frac12\frac\rho\lambda\langle v_\perp,\dot{\mathsf N}v_\perp\rangle$ в перекрёстный член
есть $O(\rho\,d\mathsf N_{12}/d\rho)=O(\rho^{c_2-1})$, а компенсировать нужно член $\rho^{c_1-c_2}\partial_2\xi_1$, который растёт. Добавки к $W$, гасящие силовой член, имеют
размер $|\mathsf N|\rho^\beta$ и при $|\mathsf N|\gtrsim\rho^{c_1-c_2}$ разрушают уровень $\delta\rho^\beta$. Вывод (эвристический): в классе $V$, квадратичных по $v_\perp$, евклидова метрика по
существу вынуждена, и вся свобода — в выборе $Y$ (и $\rho$, $A$, $D$). Строгого доказательства нет.

### 4.3. Многомасштабные стенки

Не исследовалось подробно: после теоремы T они не нужны. Препятствие видно сразу. Отдельная функция для узкой грани,
например $\frac12v_2^2+(\text{узкая часть }W)$, имеет производную с обменным членом $-v_2\partial_{u_2}(W-W_2)$ порядка $\rho^{1-c_2}$ после нормировки. Он
осциллирует с частотой узкого колебания, и поточечный выход через узкую грань снова требует усреднения (§5, часть A).

### 4.4. Уточнение карты по одному подоврагу

[Доказано] В плоской калибровке с $c=(2,3)$ карта, следующая подоврагу $b_1=b_2^2$ (новая широкая координата $t=b_1-b_2^2$), имеет
$\vartheta_1=x b_1=x(t+b_2^2)$, то есть $\mathfrak P(s,u)=(u_1+u_2^2/s^3,\ u_2)$ при $u=(st,s^2b_2)$. Отсюда $\partial_{u_2}\mathfrak P_1=2u_2/s^3=2b_2/s\to\infty$ и
$\|D_u^2\mathfrak P\|=2/s^3$: (R2) и (R3) нарушены. Это частный случай (F1)(а) из 015: положение подоврага — функция $b$, а не $u$. Кроме
того, в координатах $(t,b_2)$ второй подовраг $t=b_2^3$ всё равно касается узкой оси. Обход не работает и, по теореме T, не нужен.

## 5. Динамика модели U2 (вопрос (а)) — [Эксперимент]

`dynamics_U2.py`. Масштабированные переменные (точные для $U=x^\beta F(x,b)$): $l=\log x$, $b$, $X=\dot x/x^{24}$, $V_i=\dot u_i/x^{24}$, время $\tau$ с
$dt=x^{-23}d\tau$. Узкая масштабированная частота равна $x^{1-c_2}\sqrt{\partial_2^2Q}=x^{-2}\sqrt{\cdot}$, широкая — $x^{-1}\sqrt{\cdot}$. Обе велики по сравнению со
скоростью спуска $|X|\approx\sqrt2$: движение адиабатическое, узкая координата колеблется быстрее широкой. Параметры: $\sigma=-1$, $x\in[0{,}002;0{,}05]$.
Это доасимптотический режим: наклон $\sigma xb_1$ сравним с профилем, и дно $b_0(x)$ уходит далеко по подовражку
($|b_0|\approx0{,}7$ при $x=0{,}05$).

1. **Стрельба назад** (шаг 3 теоремы A). Из точки дна $b_0(x_k)$ с $V=0$ интегрируем назад до $x=0{,}05$. Концы при
   $x_k=0{,}03;\,0{,}02;\,0{,}01;\,0{,}006;\,0{,}004;\,0{,}003$ сходятся сверхэкспоненциально: разности $5{,}8\cdot10^{-2}$, $8{,}7\cdot10^{-3}$, $7{,}9\cdot10^{-6}$, $4{,}4\cdot10^{-9}$,
   $1{,}6\cdot10^{-11}$. Предел при $x=0{,}05$: $b=(0{,}30563,0{,}44969)$, $X=-1{,}42466$. Асимптотическая траектория есть (численно); то, что в окне она по существу единственна, — [Гипотеза] по этим
   данным.
2. **Что с координатами.** Вдоль предельной траектории (от $x=0{,}05$ к $x\approx0{,}004$):
   - траектория падает в подвижное дно: избыток относительной энергии над дном $\mathrm{calV}-\mathcal W_{\min}(x)$ убывает с $1{,}7\cdot10^{-2}$ до
     $2{,}8\cdot10^{-5}$, примерно как $x^{2{,}8}$ (относительно $|\mathcal W_{\min}|$ — с $0{,}53$ до $0{,}016$), а $|b-b_0(x)|$ — с $0{,}47$ до $0{,}024$;
   - узкая кинетическая энергия $\frac12V_2^2$ падает с $9\cdot10^{-6}$ до $9\cdot10^{-10}$, широкая $\frac12V_1^2$ — с $4\cdot10^{-4}$ до $1{,}7\cdot10^{-5}$;
   - **свободного узкого колебания нет**: узкая координата подчинена дну, широкая следует за дном с запаздыванием.
3. **Неустойчивость свободных колебаний** (часть C). Возмущение $\delta V=10^{-13}$ к предельной траектории растёт вперёд по
   времени. Узкое возмущение в начальной фазе (три первых окна от $x=0{,}01$) растёт по энергии как $x^{-27{,}7}$, $x^{-26{,}8}$, $x^{-27{,}5}$. Это совпадает с
   адиабатическим прогнозом $x^{-(\beta/2+c_2)}=x^{-27}$: сохраняется действие $J=E_{\rm phys}/\omega_{\rm phys}$, $\omega_{\rm phys}\propto x^{\beta/2-c_2}$. Широкое возмущение растёт
   быстрее (огибающие $x^{-47}\dots x^{-81}$). Его масштабированная частота ($4$–$8$ при $x\approx0{,}05$, $37$–$53$ при $x\approx0{,}01$) меньше
   антизатухания $\beta|X|/2\approx34$ или того же порядка, так что режим не
   адиабатический. Возмущённая траектория затем разворачивается: $x$ начинает расти. Эвристически механизм неустойчивости тот же,
   что за неравенством Эйлера. Относительная поперечная энергия растёт вперёд по времени, поэтому асимптотическая траектория —
   «седловая» (предел стрельбы назад), и принцип Важевского — естественный инструмент.
4. **Где ломается поле без (T)** (часть A, $\sigma=0$, отрезки истинных траекторий). Нормированная производная
   $N=(\rho/\lambda)\Xi/(\delta\rho^\beta)$ функции Важевского:
   - для полей с (T) ($\xi=Cb$ и полосовое) $\max|N|\approx48$–$65$ при всех $x$;
   - для поля 6.2(b) без (T) $\max|N|=64,\ 51,\ 112,\ 771$ при $x_0=0{,}03;\ 0{,}01;\ 0{,}003;\ 0{,}001$, то есть $x_0\max|N|\approx0{,}3$–$0{,}8$ при $x_0\le0{,}01$: рост $\propto1/x=x^{c_1-c_2}$.

   При этом **средние** $N$ по отрезку у всех трёх полей совпадают ($44$–$49$), а сами функции близки. Плохой член
   $x^{c_1-c_2}\partial_2\xi_1v_1v_2$ осциллирует с частотой узкого колебания и в среднем равен нулю. Значит, провал без (T) — поточечный провал
   строгого выхода, а не свойство динамики. Ему нет динамической причины, и «правильное» поле с (T) его не имеет.

## 6. Эксперименты

Все результаты — [Эксперимент], не доказательство. Каталог `experiments/prover/condition-T/`, запуск `~/venv/bin/python <скрипт>`.

| Скрипт → вывод | Что проверяет | Результат |
|---|---|---|
| `lemma_P_check.py` → `.out` | лемма P: все вещественные полярные точки ($\partial_2Q=0$) при $b_1=\pm10^{-k}$ и на сетке, отношение $(b_1-p_1)\partial_1Q/Q$; профили 6.2, $\tilde Q$, O2D, O1 ($k=1{,}99$), складки O2 | минимум $>0$: $4$; $4$; $2{,}58$; $1{,}56$; $1{,}94$; пределы на ветвях — §2.1 |
| `band_T.py` → `.out` | теорема T по рецепту доказательства: $\mu=1$, $\eta=\delta/8$, $\Lambda_0=\max_Z(-g)/(\partial_2Q)^2$, проверка при $\Lambda=1{,}5\Lambda_0$ на независимой выборке $K_\delta$ ($0{,}4$–$1{,}9\cdot10^6$ точек, сгущение у минимумов по слою) | все запасы $\ge0{,}29\mu\eta$; $\Lambda_0\asymp\delta^{-0.91}$ (6.2, O2D), $\delta^{-0.66}$ (O1), $\delta^{-1.0}$ (складка O2) |
| `exit_O2D.py` → `exit_O2D.out`, `exit_O2D_level.out` | (A5) в $\mathbb R^3$ прямым дифференцированием для $U_{\rm O2D}-x^{32}y$ с полем MT $\kappa(\theta,\Lambda\partial_\varepsilon P)$ (трубчатая калибровка); точки на уровнях $K_\perp=k\delta\rho^\beta$, $k=0,10^{-7},10^{-5},10^{-3}$; контроль без (T) | §4.1; контроль: $-4{,}2\cdot10^4$ при $s=10^{-12}$, $\propto s^{-1}$ |
| `dynamics_U2.py` → `dynamics_U2_{A,B,C}.out` | динамика U2: части A, B, C | §5 |
| `identities.py` → `.out` | (1) тождество (4.1); (2) формула $x\langle w,D_wY\rangle$; (3) реализуемость O1 многочленом; (4) $\min(Cb\cdot\nabla\tilde Q)/\tilde Q=-2655$ на сетке | все невязки $0$; (3) младшая форма $z^6$ |
| `crit_U2.py` → `.out` | критические точки $\tilde Q$: результант, FLINT, строгая изоляция корней | $R=b_2^{57}\cdot(\deg288$, без вещественных корней$)$ |
| прежняя попытка: `model_U.py`, `band_field.py`, `exit_check.py`, `exit_check2.py`, `correction_check.py`, `polar_check.py`, `crit_detail.py` | тождества моделей, полосовое поле с другим выбором $\mu$, выход U2 для полей без (T) и полосового, поправка ГА | перечитаны; результаты согласуются с новыми (§2.3, §4.1, §4.2). `crit_sturm.out`, `dynamics.out` пусты (обрыв) и заменены `crit_U2.py`, `dynamics_U2.py` |

## 7. Где работают аналитичность и изолированность

- **Аналитичность работает в лемме P** (и через неё — в теоремах T, MT₃, W$_{\rm band}$):
  - у полярной кривой конечное число полуветвей Пюизё (подготовка Вейерштрасса);
  - ограничение $Q$ на полуветвь имеет конечный порядок $k$;
  - вертикальных полуветвей нет.

  Для $C^\infty$ это неверно (§2.8). Около изолированного нуля могут накапливаться критические точки $Q$ с положительными
  значениями, и тогда никакое поле не даёт полосового неравенства. Лемма P в частности утверждает, что у аналитического $Q\ge0$ около
  нулевого множества нет других критических точек.
- **Остальное — для $U\in C^2$.** Предложение N$_T$, вывод MT₃ из MT и замечание (T′) от аналитичности $U$ не зависят. Вся «конечность
  типа» сидит в предположении (L): существует аналитический предельный профиль в весовой карте. С гладкими контрпримерами
  (Пенлеве–Уинтнер, Лалуа; по `problem/KNOWN_RESULTS.md`, не сверено) противоречия нет: у них нет карт с (L), (Q), (R), иначе MT₃ дала
  бы неустойчивость.
- **Изолированность критической точки $U$ не используется** ни в MT₃, ни в W$_{\rm band}$. Используется изолированность **нуля профиля** $Q$ (в
  MT₃(a)) — это стенки, а не изолированность критической точки. Для W$_{\rm band}$ хватает компактности $F_{\min}$. Изолированность
  критической точки $U_2$ доказана отдельно (следствие U2(ii)), чтобы модель была законным примером задачи (A).
- **Вещественность.** Всё вещественно; число Милнора не используется.
- В W$_{\rm band}$ аналитичность $U$ работает и в построении данных первого ребра: лемма N1 [M′, 011] — аналитичность $\tilde U$ в $\sigma=0$.

## 8. Частные случаи с известным ответом

- **$n=2$.** Узкой координаты нет. Профиль $Q(b_1)=ab_1^{2k}(1+O(b_1))$, $a>0$, и $b_1Q'=2kQ(1+O(b_1))$: полное поле Эйлера $\xi=b_1$, $\Lambda$ не
  нужно. Согласуется с 015, 6.9 и с известным ответом ($n=2$ решено).
- **Однородный $U=u_m$.** Полярная калибровка, всё коническое. При изолированном минимуме $u_m|_{S^2}$ профиль
  $Q=u_m\circ\omega-\min u_m$ аналитичен с изолированным нулём, и MT₃ (случай $c_1=c_2=1$) даёт траекторию с полем $\kappa(b_1,\Lambda\partial_2Q)$ — без
  леммы E [009] и без сглаживания (лемма 5.1). Ответ известен (инвариантный луч), совпадает.
- **Квазиоднородный $U$** ($U(tx,t^{c}y)=t^\beta U$, $c_1<c_2$, $U(1,0)<0$, $0$ — изолированный локальный минимум $U(1,\cdot)$). Плоская калибровка,
  $\mathcal W=U(1,b)-U(1,0)$ не зависит от $x$. MT₃ применима **и при $Q_d(0,1)=0$**, где 015 (6.9) говорил «MT ничего не даёт». Ответ (ось $x$
  инвариантна) известен, совпадает.
- **Невырожденная младшая форма** ($m=2$, $\lambda_{\min}(D^2U(0))<0$): профиль $Q$ — невырожденная квадратичная форма. Полярная кривая — прямая, на ней
  $b_1\partial_1Q=2Q$, $\Lambda=0$ годится (полная форма). Совпадает с Ляпуновым.
- **Модель U2** — квазиоднородная главная часть $U_0$ с инвариантным лучом плюс член высшего веса. Возможно, этот случай покрывает
  теория асимптотических решений Козлова–Фурты (существование решения с асимптотикой лучевого решения укороченной
  системы) — **не сверено**, условия на показатели Ковалевской не проверялись. U2 здесь — тестовая модель, а не новый случай (A).

## 9. Пробелы

1. **Опора на непроверенное.**
   - MT₃, следствие O и W$_{\rm band}$ опираются на теорему MT (015, **на проверке**).
   - W$_{\rm band}$ — ещё на [M′] (проверено R40, R41, в `results/` не оформлено).
   - Следствия U2(iv) и Q′ опираются только на проверенные [012], [009], [007] и на новые лемму P, теорему T.
2. **[W], [NP]** — как в [009], не сверены с первоисточником.
3. **Изолированность критической точки $U_2$** — по модулю вычисления результанта и строгой изоляции корней в python-flint
   (корректность ПО не проверялась).
4. **Предложение N$_T$** доказано для плоской карты с полем 2U ($\gamma=0$, $L=I$). Для общей калибровки MT — только при малом $|Y_T|$ (замечание в §3.3), не
   выписано.
5. **Замечание (T′)** — при условии, что в доказательстве MT (T) больше нигде не используется; это стоит проверить рецензенту.
6. **Сингулярные члены $s^{-e}R(b)$** (теорема C′ [012], следствие X [013]) теоремой MT₃ не покрываются: (L) требует сходимости $\mathcal W\to Q$. Для
   полосового поля член $\xi\cdot\nabla R_j$ при $\Lambda\gg1$ не контролируется. Там (T) может остаться препятствием ((F1′)).
7. **$n\ge4$.** При широком блоке размерности $\ge2$ полярное множество $\{\nabla_{\text{узк}}Q=0\}$ — не кривая. Над одной точкой $b'$ могут лежать два листа с
   противоположными $\nabla_{b'}Q$, и тогда поля $f(b')$ с $f\cdot\nabla_{b'}Q>0$ на обоих нет. [Гипотеза] (T) может быть настоящим препятствием при $n\ge4$.
   Контрпример не построен.
8. **Динамика** (§5) — доасимптотический режим ($x\ge0{,}002$). Сходимость $b(t)$ к дну и касание луча не доказаны. Утверждение
   «асимптотическая траектория в окне единственна» — [Гипотеза].
9. **Обходы (3), (4)** исследованы лишь в объёме §4.3, §4.4. Неевклидова метрика — [Эскиз].
10. После MT₃ из программы SH₃ (015, замечание 4) препятствие (F1) снимается в случае сходящегося аналитического профиля.
    Остаются (F2)–(F7): листы без стенок, знакопеременные уровни, конечность уточнений, особые точки, переменная кратность,
    сингулярные члены.

## 10. Статус

- Лемма P, теорема T (с дополнением), предложение N$_T$, пример §2.8 — **[Доказано]**.
- Теорема MT₃ — **[Доказано]** с опорой на MT (015, на проверке).
- Следствие U2: (i), (iii), (iv) — **[Доказано]** (iv — через проверенную теорему 2U); (ii) — **[Доказано по модулю строгого вычисления]**.
- Следствие Q′ — **[Доказано]** через 2U [012].
- Следствие O — **[Доказано]** через MT₃.
- Теорема W$_{\rm band}$ и её следствие (случай (W) теоремы M′ без (UR)) — **[Доказано]** через MT₃ и [M′].
- Замечание (T′) — **[Доказано]** как изменение доказательства MT (пробел 5).
- Обходы §4: тождество (4.1) и §4.4 — [Доказано]; §4.2 (метрика) — [Эскиз]; §4.3 — не исследовалось.
- Динамика U2 (§5) — [Эксперимент].
- $n\ge4$ — [Гипотеза].
- Независимой проверки нет. Рецензенту — в первую очередь лемма P (пп. 4–7), теорема T(b) (пп. 2–3), вывод MT₃ (п. 4 — три
  случая весов) и предложение N$_T$ (п. 4).
