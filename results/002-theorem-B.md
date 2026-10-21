# 002. Теорема B: тотальная неустойчивость, когда младшая форма — нестрогий минимум с гладким конусом нулей (Морс–Ботт)

- **Статус:** [Доказано], исправленная версия. Исходный текст проверен: reviewer R2, 21.10.2026
  ([`notes/reviewer/2026-10-21-theoremB-proof.md`](../notes/reviewer/2026-10-21-theoremB-proof.md)).
  Исправленная версия ждёт повторной независимой проверки.
  [Доказано] относится к теореме B и предложению (пример). В разделе «Замечания» есть утверждения с
  другими метками: в замечании 1 (компоненты $\Sigma$ разной размерности) и замечании 3 (о
  $C^{m+4}$) — [Эскиз], в замечаниях 4 (новизна) и 5 (обобщения) — [Гипотеза].
- **Автор(ы):** vlad-claude, 27.09.2026
  ([`notes/vlad-claude/theoremB-proof.md`](../notes/vlad-claude/theoremB-proof.md), раздел «Пример»
  в [`notes/vlad-claude/theoremB.md`](../notes/vlad-claude/theoremB.md)). Правки по отзыву R2 —
  prover (агент), 21.10.2026. Доказательство изолированности (§7) и разбор примера (§8) предложены
  рецензентом R2 в отзыве; здесь они перепроверены и выписаны полностью. Перечень отличий от
  исходного текста — в конце файла.
- **Зависит от:**
  - лемма 1 (критерий поля) — это лемма 1 результата [001](001-field-criterion.md)
    [Проверено: reviewer R1, 21.10.2026]; ниже она повторена с доказательством;
  - стандартные факты анализа. Опубликованные теоремы о неустойчивости не используются.
    - (F1) Теорема об обратной функции в вещественно-аналитическом классе: аналитическое
      отображение $n$-мерных аналитических многообразий с обратимым дифференциалом в точке $p$ —
      аналитический диффеоморфизм окрестности $p$ на открытое множество. Получается из
      голоморфной теоремы об обратной функции для комплексификации. Учебник: Krantz–Parks,
      *A Primer of Real Analytic Functions*, гл. 2 (номер теоремы не сверен).
    - (F2) Пусть $p\mapsto A(p)$ — аналитическое семейство вещественных симметричных матриц на
      открытом множестве, а $\gamma\subset\mathbb C$ — окружность, не пересекающая спектры
      $A(p)$. Тогда проектор Рисса $\frac1{2\pi i}\oint_\gamma(\lambda-A(p))^{-1}d\lambda$
      аналитичен по $p$ и равен ортогональному проектору на сумму собственных подпространств
      $A(p)$ с собственными числами внутри $\gamma$ (Като, *Теория возмущений линейных
      операторов*, гл. I, §5; номер пункта не сверен). Аналитичность видна прямо: подынтегральное
      выражение аналитично по $(p,\lambda)$, контур компактен.
    - (F3) Отображения $A\mapsto A^{-1}$ и $A\mapsto A^{1/2}$ (положительный корень) аналитичны на
      открытом конусе положительно определённых симметричных матриц. Для корня годится формула
      $A^{1/2}=\frac1{2\pi i}\oint_\gamma\lambda^{1/2}(\lambda-A)^{-1}d\lambda$, где $\gamma$
      лежит в правой полуплоскости и охватывает спектр.
    - (F4) Формула Тейлора с интегральным остатком по одной переменной с параметрами:
      если $\varphi(\ell,\varepsilon)$ аналитична (или класса $C^k$) и
      $\varphi(\ell,0)=\partial_\varepsilon\varphi(\ell,0)=0$, то
      $\varphi=\varepsilon^2\int_0^1(1-\tau)\,\partial_\varepsilon^2\varphi(\ell,\tau\varepsilon)\,d\tau$,
      и интеграл аналитичен (соответственно класса $C^{k-2}$).

## Утверждение

**Обозначения.** $U$ — вещественно-аналитическая функция в окрестности $0\in\mathbb R^n$,
$U(0)=0$, и $U=\sum_{k\ge m}u_k$ — разложение в ряд однородных многочленов, $\deg u_k=k$,
$u_m\not\equiv0$. *Движение* — решение уравнения $\ddot x=-\nabla U(x)$, его *энергия*
$E=\frac12|\dot x|^2+U(x)$ постоянна. Далее $B_\rho$ — открытый шар радиуса $\rho$ с центром $0$,
$S^{n-1}$ — единичная сфера, $\langle\cdot,\cdot\rangle$ и $|\cdot|$ — евклидовы.

**Предположения.**

- **(B1)** $u_m\ge0$ на $\mathbb R^n$. Множество $\Sigma=\{\omega\in S^{n-1}:\ u_m(\omega)=0\}$
  непусто и является гладким ($C^\infty$) компактным подмногообразием $S^{n-1}$ без края
  размерности $s$. Через $Z=\{t\omega:\ t\ge0,\ \omega\in\Sigma\}$ обозначим конус нулей.
- **(B2)** (Морс–Ботт.) Для $\omega\in\Sigma$ положим $T_\omega Z=\mathbb R\omega\oplus T_\omega\Sigma$,
  $N_\omega=(T_\omega Z)^\perp$ и $c=\dim N_\omega=n-1-s$. Квадратичная форма
  $H_\omega(\xi,\xi)=\langle D^2u_m(\omega)\xi,\xi\rangle$ положительно определена на $N_\omega$.
- **(B3)** Функция $g=u_{m+1}|_\Sigma$ имеет $0$ регулярным значением: если $\omega\in\Sigma$ и
  $g(\omega)=0$, то $dg(\omega)\ne0$. При $s=0$ это означает $g\ne0$ на $\Sigma$.

**Определение** (как в [001](001-field-criterion.md)). Пусть $U\in C^2$ в окрестности $\bar B_\rho$.
Точка $0$ *тотально неустойчива с шаром $B_\rho$*, если существует функция
$T\colon(-\infty,0)\to(0,\infty)$ со следующим свойством. Для любого движения с энергией $E<0$ и
любого отрезка $[t_1,t_2]$, на котором $x(t)\in B_\rho$, выполнено $t_2-t_1\le T(E)$.
Совпадение с определением 1 из [P20] не сверено с первоисточником.

**Теорема B.** Пусть выполнены (B1)–(B3). Тогда существует $\rho>0$ такое, что:

- **(a)** $0$ тотально неустойчива с шаром $B_\rho$. Точнее, существует $M>0$ такое, что можно
  взять $T(E)=2w(E)M/|E|$, где $w(E)=\sqrt{2(E-\min_{\bar B_\rho}U)}$;
- **(b)** $0$ — не точка локального минимума $U$, и равновесие $x=0$, $\dot x=0$ системы
  $\ddot x=-\nabla U(x)$ неустойчиво по Ляпунову;
- **(c)** $\nabla U(x)\ne0$ при $0<|x|<\rho$, то есть $0$ — изолированная критическая точка $U$.

Иначе говоря, изолированность в теореме не предполагается, но из (B1)–(B3) она **следует**.
Поэтому неизолированных критических точек теорема B не покрывает. Для класса потенциалов с
(B1)–(B3) теорема даёт утверждение задачи (A) и сверх того тотальную неустойчивость.

**Предложение (пример).** Пусть $n=3$ и $U=(x^2+y^2-z^2)^2+xz^4$. Тогда:

1. выполнены (B1)–(B3) с $m=4$, $s=1$, $c=1$;
2. $0$ — единственная вещественная критическая точка $U$ в $\mathbb R^3$;
3. $0$ — не точка локального минимума;
4. над $\mathbb C$ точка $0$ не изолирована: прямые $\{z=0,\ x=\pm iy\}\subset\mathbb C^3$ состоят
   из критических точек $U$.

## Доказательство

### Шаг 0. Элементарные следствия условий

**0.1.** $m$ чётно и $m\ge2$. Так как $U(0)=0$, имеем $m\ge1$. Если бы $m$ было нечётным, то
$u_m(-x)=-u_m(x)$, и из $u_m\ge0$ следовало бы $u_m\equiv0$.

**0.2.** $n\ge2$ и $1\le c$, то есть $s\le n-2$. При $n=1$ имеем $u_m=a x^m$ с $a>0$, и
$\Sigma=\varnothing$. При $n\ge2$ сфера $S^{n-1}$ связна. Если бы $\dim\Sigma=n-1$, то $\Sigma$ было
бы открыто (подмногообразие полной размерности) и замкнуто, то есть $\Sigma=S^{n-1}$ и
$u_m\equiv0$.

**0.3.** $g$ принимает отрицательное значение. Так как $m$ чётно, $\Sigma=-\Sigma$, а $u_{m+1}$
нечётна, поэтому $g(-\omega)=-g(\omega)$. Если бы $g\equiv0$, то в любой точке $\omega\in\Sigma$
(она есть, $\Sigma\ne\varnothing$) было бы $g(\omega)=0$ и $dg(\omega)=0$, вопреки (B3). Значит,
$g(\omega_0)\ne0$ для некоторого $\omega_0$, и одно из чисел $g(\pm\omega_0)$ отрицательно.
Обозначим соответствующую точку $\omega_1$.

**0.4.** $0$ — не точка локального минимума. Так как $u_m(\omega_1)=0$,
$U(t\omega_1)=t^{m+1}g(\omega_1)+O(t^{m+2})<0$ при малых $t>0$.

### §1. Критерий поля

**Лемма 1** (= лемма 1 из [001](001-field-criterion.md)). Пусть $U\in C^2$ в окрестности
$\bar B_\rho$, $U(0)=0$, $X=\{x\in B_\rho:\ U(x)<0\}$. Пусть на открытом множестве
$\mathcal O\supset X$ задано $C^1$-поле $A$ с $|A|\le M$ на $X$, и при некотором $p>0$ для всех
$x\in X$
$$\operatorname{sym}DA(x)\succeq0,\qquad\langle A(x),\nabla U(x)\rangle\le p\,U(x).$$
Тогда для любого движения с энергией $E<0$, лежащего в $B_\rho$ при $t\in[t_1,t_2]$, выполнено
$t_2-t_1\le2w(E)M/(p|E|)$, где $w(E)=\sqrt{2(E-\min_{\bar B_\rho}U)}$.

*Доказательство.* Так как $\frac12|\dot x|^2=E-U(x)\ge0$, имеем $U(x(t))\le E<0$, то есть
$x(t)\in X$ при $t\in[t_1,t_2]$, и $|\dot x|^2=2(E-U)\le w(E)^2$ (минимум по замкнутому шару
конечен, так как $U$ непрерывна на $\bar B_\rho$). Функция $F(t)=\langle\dot x(t),A(x(t))\rangle$
класса $C^1$ на $[t_1,t_2]$ ($x\in C^2$, $A\in C^1$ на открытом $\mathcal O\ni x(t)$), $|F|\le wM$, и
$$\dot F=\langle\ddot x,A\rangle+\langle\dot x,DA\,\dot x\rangle
=-\langle\nabla U,A\rangle+\langle\operatorname{sym}DA\,\dot x,\dot x\rangle\ge-pU(x)\ge p|E|.$$
Значит, $2wM\ge F(t_2)-F(t_1)\ge p|E|(t_2-t_1)$. ∎

**Следствие.** Если $0$ тотально неустойчива с шаром $B_\rho$ и $0$ не точка локального минимума,
то равновесие неустойчиво по Ляпунову. *Доказательство.* Возьмём $x_0$ со сколь угодно малым
$|x_0|$ и $U(x_0)<0$ и начальные данные $(x_0,0)$. Тогда $E=U(x_0)<0$. Пока $x(t)\in B_\rho$,
фазовая точка лежит в компакте $\bar B_\rho\times\{|\dot x|\le w(E)\}$, поэтому решение
продолжается, пока не выйдет из $B_\rho$. По определению это случится не позже момента $T(E)$:
$|x(t)|$ достигнет $\rho$. Это неустойчивость с $\varepsilon=\rho$. ∎

Остаток доказательства — построение поля $A$ с $A(U)=U$ (то есть $p=1$),
$\operatorname{sym}DA\succeq0$ и $|A|=O(|x|)$ на открытом множестве, содержащем $X$.

### §2. Геометрия около конуса

**2.1. Конус, гессиан, проектор.**

(a) $Z=u_m^{-1}(0)$, так как $u_m(x)=|x|^mu_m(x/|x|)$ при $x\ne0$.

(b) $Z=\{\nabla u_m=0\}$. На $Z$ функция $u_m\ge0$ достигает минимума $0$, поэтому $\nabla u_m=0$.
Обратно, из $\nabla u_m(x)=0$ по формуле Эйлера $mu_m(x)=\langle x,\nabla u_m(x)\rangle=0$.

(c) $Z\setminus0$ — гладкое подмногообразие $\mathbb R^n\setminus0$ размерности $s+1$: это образ
$(0,\infty)\times\Sigma$ при диффеоморфизме $(0,\infty)\times S^{n-1}\to\mathbb R^n\setminus0$,
$(t,\omega)\mapsto t\omega$. При этом $T_{t\omega}Z=\mathbb R\omega\oplus T_\omega\Sigma$,
$N_{t\omega}=N_\omega$, и $N_\omega\perp\omega$.

(d) Для $z\in Z\setminus0$ имеем $D^2u_m(z)v=0$ при $v\in T_zZ$: это производная тождества
$\nabla u_m\equiv0$ вдоль кривой в $Z$. Матрица $D^2u_m(z)$ симметрична, поэтому её образ лежит в
$(T_zZ)^\perp=N_z$. Так как $D^2u_m(t\omega)=t^{m-2}D^2u_m(\omega)$, по (B2) она положительно
определена на $N_z$. Значит, $\ker D^2u_m(z)=T_zZ$, $\operatorname{im}D^2u_m(z)=N_z$, и
$D^2u_m(z)=P D^2u_m(z)P$, где $P$ — ортопроектор на $N_z$. Положим
$$\lambda_0=\min\{H_\omega(\nu,\nu):\ \omega\in\Sigma,\ \nu\in N_\omega,\ |\nu|=1\},\qquad
\Lambda=\max\{\ldots\}.$$
Множество под знаком минимума компактно (единичное нормальное расслоение компактного $\Sigma$),
поэтому $0<\lambda_0\le\Lambda<\infty$. Спектр $D^2u_m(\omega)$ при $\omega\in\Sigma$ состоит из $0$
(собственное подпространство $T_\omega Z$) и чисел из $[\lambda_0,\Lambda]$ (собственные векторы в
$N_\omega$).

(e) *Аналитический проектор.* Пусть $\gamma$ — окружность с центром $(\lambda_0+\Lambda)/2$ радиуса
$(\Lambda-\lambda_0)/2+\lambda_0/4$. Она охватывает $[\lambda_0,\Lambda]$, не охватывает $0$, и
расстояние от $\gamma$ до $\{0\}\cup[\lambda_0,\Lambda]$ равно $\lambda_0/4$. Собственные числа
симметричной матрицы сдвигаются не больше чем на норму возмущения (неравенство Вейля). Поэтому
для $y$ из некоторой окрестности $\mathcal V\supset\Sigma$ в $\mathbb R^n$ (компактность $\Sigma$)
спектр $D^2u_m(y)$ не пересекает $\gamma$, и по (F2)
$$P(y)=\frac1{2\pi i}\oint_\gamma(\lambda-D^2u_m(y))^{-1}d\lambda$$
аналитичен на $\mathcal V$. При $\omega\in\Sigma$ это ортопроектор на $N_\omega$. Для
$z\in Z\setminus0$ положим $P(z)=P(z/|z|)$.

(f) *$\Sigma$ и $Z\setminus0$ — аналитические подмногообразия.* Пусть $z_0\in Z\setminus0$ и
$n_1,\dots,n_c$ — ортонормированный базис $N_{z_0}$. Отображение
$G(y)=(\langle n_i,\nabla u_m(y)\rangle)_{i=1}^c$ полиномиально, $Z\subset G^{-1}(0)$ по (b), и
$DG(z_0)=(n_i^{\mathsf T}D^2u_m(z_0))_i$ имеет ранг $c$, так как $D^2u_m(z_0)$ обратима на
$N_{z_0}$. Значит, около $z_0$ множество $W=G^{-1}(0)$ — аналитическое подмногообразие размерности
$n-c=s+1$. Возьмём шар $V\ni z_0$, для которого $W\cap V$ связно (в карте подмногообразия это шар).
Вложение $(Z\setminus0)\cap V\hookrightarrow W\cap V$ — инъективная иммерсия многообразий одной
размерности, поэтому его образ открыт в $W\cap V$. Он и замкнут в $W\cap V$, так как $Z$ замкнуто.
Значит, $Z\cap V=W\cap V$. Пересечение $\Sigma=(Z\setminus0)\cap S^{n-1}$ трансверсально (вектор
$z\in T_zZ$ трансверсален $T_zS^{n-1}=z^\perp$), поэтому $\Sigma$ аналитично.

Аналитичность $\Sigma$ нужна только для удобства: с $C^\infty$-объектами доказательство дословно то
же, ведь ниже используется лишь ограниченность производных на компактах.

(g) *Переформулировка (B3).* Так как $u_{m+1}|_Z$ однородна степени $m+1$, её дифференциал на
$Z\setminus0$ в точке $t\omega$ имеет радиальную часть $(m+1)t^mg(\omega)$ и касательную к $\Sigma$
часть $t^{m+1}dg(\omega)$. Поэтому (B3) равносильно тому, что $u_{m+1}|_{Z\setminus0}$ не имеет
критических точек на многообразии $Z\setminus0$.

**2.2. Карты и рамки.** Выберем конечный атлас аналитических карт $\omega=\omega_\alpha(\theta)$,
$\theta\in\Theta'_\alpha\subset\mathbb R^s$, многообразия $\Sigma$ и открытые
$\Theta_\alpha\Subset\Theta'_\alpha$ с $\bigcup_\alpha\omega_\alpha(\Theta_\alpha)=\Sigma$. При $s=0$
«карта» — точка. На каждом $\Theta'_\alpha$ выберем аналитическую ортонормированную рамку
$e^\alpha_1(\theta),\dots,e^\alpha_c(\theta)$ пространства $N_{\omega_\alpha(\theta)}$. Она
существует после уменьшения карт: около $\theta_0$ возьмём $v_1,\dots,v_c$ с базисом
$P(\omega(\theta_0))v_i$ в $N_{\omega(\theta_0)}$. Векторы $P(\omega(\theta))v_i$ аналитичны и
линейно независимы около $\theta_0$, а процесс Грама–Шмидта аналитичен. Индекс $\alpha$ ниже
опускаем.

Нормальное расслоение $\mathfrak N=\{(z,\nu):\ z\in Z\setminus0,\ \nu\in N_z\}\subset\mathbb R^n\times\mathbb R^n$
— аналитическое подмногообразие размерности $(s+1)+c=n$. Карты на нём:
$(t,\theta,b)\mapsto(t\omega(\theta),\sum_ib_ie_i(\theta))$, $t>0$, $b\in\mathbb R^c$. Растяжения
$\delta_t(z,\nu)=(tz,t\nu)$ сохраняют $\mathfrak N$. Положим
$E_\kappa=\{(z,\nu)\in\mathfrak N:\ |\nu|<\kappa|z|\}$.

**2.3. Трубка.** Пусть $\Phi_0(z,\nu)=z+\nu$ на $\mathfrak N$.

*Утверждение T.* Существует $\kappa_T>0$ такое, что при $0<\kappa\le\kappa_T$ отображение $\Phi_0$
— аналитический диффеоморфизм $E_\kappa$ на открытое коническое множество
$\mathcal N_\kappa=\Phi_0(E_\kappa)\subset\mathbb R^n\setminus0$. Для $x=z+\nu$, $(z,\nu)\in E_\kappa$,
$$|x|^2=|z|^2+|\nu|^2,\qquad |z|\le|x|\le\sqrt{1+\kappa^2}\,|z|.$$

*Доказательство.* Равенство $|x|^2=|z|^2+|\nu|^2$ верно, так как $\nu\perp z$ (п. 2.1(c)). Кроме того,
$\Phi_0\circ\delta_t=t\,\Phi_0$.

1. *Локальная обратимость.* В точке $(z,0)$ дифференциал $\Phi_0$ — это изоморфизм
   $T_zZ\oplus N_z\to\mathbb R^n$, $(v,w)\mapsto v+w$. Множество точек $\mathfrak N$, где $D\Phi_0$
   обратим, открыто и содержит $\Sigma\times\{0\}$. По компактности $\Sigma$ оно содержит
   $\{(\omega,\nu):\ \omega\in\Sigma,\ |\nu|\le\kappa_1\}$ при некотором $\kappa_1>0$. Иначе нашлись
   бы $(\omega_j,\nu_j)$ с $|\nu_j|\to0$ и вырожденным $D\Phi_0$, и предельная точка $(\omega_*,0)$
   была бы вырожденной (множество вырожденных точек замкнуто). По однородности $D\Phi_0$ обратим
   на $E_{\kappa_1}$.
2. *Инъективность на всех масштабах.* Пусть для каждого $j$ найдутся различные
   $p_j=(z_j,\nu_j)$ и $p'_j=(z'_j,\nu'_j)$ из $E_{1/j}$ с $\Phi_0(p_j)=\Phi_0(p'_j)=x_j$. Множество
   $E_{1/j}$ инвариантно относительно растяжений, поэтому можно считать $|x_j|=1$. Тогда
   $|z_j|,|z'_j|\in[(1+j^{-2})^{-1/2},1]\subset[2^{-1/2},1]$ и $|\nu_j|,|\nu'_j|\le1/j$. Переходя к
   подпоследовательности, получаем $z_j\to z_*\in Z$ с $|z_*|\ge2^{-1/2}$ и
   $z'_j=z_j+\nu_j-\nu'_j\to z_*$. Значит, $p_j,p'_j\to(z_*,0)$ в $\mathfrak N$. Но по п. 1 и (F1)
   $\Phi_0$ инъективно в окрестности $(z_*,0)$ — противоречие. Значит, при некотором
   $\kappa_T\le\kappa_1$ отображение $\Phi_0$ инъективно на $E_{\kappa_T}$.
3. Инъективный локальный аналитический диффеоморфизм $n$-мерных многообразий — аналитический
   диффеоморфизм на открытый образ (F1). Коничность $\mathcal N_\kappa$ следует из
   $\Phi_0\circ\delta_t=t\Phi_0$. ∎

*Вне трубки.* Множество $S^{n-1}\setminus\mathcal N_\kappa$ компактно и не пересекается с $\Sigma$
(точки $(\omega,0)$ лежат в $E_\kappa$), поэтому $u_m\ge c_\kappa>0$ на нём. По однородности
$$u_m(x)\ge c_\kappa|x|^m\qquad\text{при }x\notin\mathcal N_\kappa.\tag{2.1}$$

**2.4. Параметрическая лемма Морса на слоях.** Чтобы не работать с операторами на меняющихся
пространствах $N_z$, продолжим все операторы на $\mathbb R^n$. Для $z\in Z\setminus0$ и
$\nu\in\mathbb R^n$ положим ($P=P(z)$)
$$\tilde M(z,\nu)=\int_0^1(1-\tau)\,D^2u_m(z+\tau\nu)\,d\tau,\qquad
M(z,\nu)=P\tilde M(z,\nu)P+(I-P),\qquad M_0(z)=M(z,0)=\tfrac12D^2u_m(z)+(I-P)$$
(последнее — по п. 2.1(d)). Матрицы $M$ и $M_0$ симметричны, коммутируют с $P$ и равны $I$ на
$N_z^\perp$. $M_0(z)\succ0$. Где $M(z,\nu)\succ0$, положим
$$S=M_0^{-1/2}MM_0^{-1/2},\qquad B(z,\nu)=M_0^{-1/2}S^{1/2}M_0^{1/2},\qquad \mu_z(\nu)=B(z,\nu)\nu.$$
Все эти матрицы коммутируют с $P$: функции от матрицы, коммутирующей с $P$, коммутируют с $P$. На
$N_z^\perp$ они равны $I$. Объекты аналитичны по $(z,\nu)$ по (F2), (F3).

(M1) *Морс.* Для $\nu\in N_z$ имеем $\mu_z(\nu)\in N_z$ и $u_m(z+\nu)=Q_z(\mu_z(\nu))$, где
$Q_z(\nu')=\frac12H_z(\nu',\nu')$. Действительно, по формуле Тейлора с $u_m(z)=0$,
$\nabla u_m(z)=0$ получаем $u_m(z+\nu)=\nu^{\mathsf T}\tilde M\nu=\nu^{\mathsf T}M\nu$ (так как
$\nu=P\nu$). С другой стороны, $\nu'=\mu_z(\nu)$:
$$\nu'^{\mathsf T}M_0\nu'=\nu^{\mathsf T}M_0^{1/2}S^{1/2}M_0^{-1/2}M_0M_0^{-1/2}S^{1/2}M_0^{1/2}\nu
=\nu^{\mathsf T}M_0^{1/2}SM_0^{1/2}\nu=\nu^{\mathsf T}M\nu,$$
и $\nu'^{\mathsf T}M_0\nu'=\frac12\nu'^{\mathsf T}D^2u_m(z)\nu'=Q_z(\nu')$ при $\nu'\in N_z$.

(M2) *Однородность.* $P(tz)=P(z)$, $\tilde M(tz,t\nu)=t^{m-2}\tilde M(z,\nu)$. На $N_z$:
$M(tz,t\nu)=t^{m-2}M(z,\nu)$ и $M_0(tz)=t^{m-2}M_0(z)$, на $N_z^\perp$ всё равно $I$. Отсюда
$S(tz,t\nu)=S(z,\nu)$, $B(tz,t\nu)=B(z,\nu)$ и $\mu_{tz}(t\nu)=t\mu_z(\nu)$.

(M3) *Выбор $\kappa$.* Матрица $M(z,\nu)$ блочно-диагональна относительно $N_z\oplus N_z^\perp$:
её блоки — $P\tilde MP|_{N_z}$ и $I$. При $\omega\in\Sigma$ имеем $M_0(\omega)|_{N_\omega}=\frac12H_\omega\succeq\frac{\lambda_0}2$.
Производные $\tilde M$ ограничены на компакте $\{(\omega,\nu)\in\Sigma\times\mathbb R^n:\ |\nu|\le1\}$.
Поэтому найдётся $\kappa'\in(0,1]$ с $P\tilde M(\omega,\nu)P|_{N_\omega}\succeq\frac{\lambda_0}4$ при
$|\nu|\le\kappa'$; тогда $M(\omega,\nu)\succeq\min(\frac{\lambda_0}4,1)$, и $B$ аналитична в
окрестности компакта $\{(\omega,\nu)\in\Sigma\times\mathbb R^n:\ |\nu|\le\kappa'\}$, а её производные
там ограничены. Кроме того, $B(\omega,0)=I$ (так как $S(\omega,0)=I$), поэтому производная
$D_\nu(B(\omega,\nu)\nu)$ при $\nu=0$ равна $I$. Значит, найдутся $\kappa_M\in(0,\kappa']$ и $C_\mu$
такие, что при $\omega\in\Sigma$, $\nu\in N_\omega$, $|\nu|\le\kappa_M$:
$$\|D_\nu\mu_\omega(\nu)-I\|\le\tfrac12,\qquad |\mu_\omega(\nu)-\nu|\le C_\mu|\nu|^2.$$
Зафиксируем
$$\kappa=\min(\kappa_T,\kappa_M,1).$$
По (M2) при $(z,\nu)\in E_\kappa$:
$\|D\mu_z(\nu)-I\|\le\frac12$ и $|\mu_z(\nu)-\nu|\le C_\mu|\nu|^2/|z|$. Отсюда:

- $\mu_z$ инъективно на $\{\nu\in N_z:\ |\nu|<\kappa|z|\}$, причём
  $|\mu_z(\nu_1)-\mu_z(\nu_2)-(\nu_1-\nu_2)|\le\frac12|\nu_1-\nu_2|$ (неравенство о среднем на
  выпуклом шаре) и $\frac12|\nu|\le|\mu_z(\nu)|\le\frac32|\nu|$;
- образ содержит шар $\{|\nu'|<\kappa|z|/2\}$ в $N_z$. Для такого $\nu'$ отображение
  $T(\nu)=\nu-\mu_z(\nu)+\nu'$ — сжатие с константой $\frac12$ замкнутого шара радиуса
  $2|\nu'|<\kappa|z|$ в себя, так как $|T(\nu)|\le\frac12|\nu|+|\nu'|$. Его неподвижная точка
  — прообраз $\nu'$.

(M4) *Обратное отображение.* $\Psi(z,\nu)=(z,\mu_z(\nu))$ — аналитическое инъективное
отображение $E_\kappa\to\mathfrak N$. В картах п. 2.2 его якобиан блочно-треугольный с
диагональными блоками $I$ и $D\mu_z$, поэтому обратим. По (F1) $\Psi$ — аналитический
диффеоморфизм на открытое множество $\Psi(E_\kappa)\supset E_{\kappa/2}$. Обратное запишем как
$(z,\nu')\mapsto(z,\nu(z,\nu'))$. Тогда $\nu(z,\nu')\in N_z$ и
$$\nu(tz,t\nu')=t\,\nu(z,\nu'),\quad |\nu(z,\nu')|\le2|\nu'|,\quad \|D_{\nu'}\nu(z,\nu')\|\le2,\quad
|\nu(z,\nu')-\nu'|\le\frac{4C_\mu|\nu'|^2}{|z|},\quad D_{\nu'}\nu(z,0)=I_{N_z}.$$

**2.5. Сдвиг.** Для $z\in Z\setminus0$ положим $L_z(\nu')=\langle\nabla u_{m+1}(z),\nu'\rangle$ и
$$\eta(z)=\bigl(D^2u_m(z)+I-P(z)\bigr)^{-1}P(z)\nabla u_{m+1}(z).$$
Матрица в скобках блочно-диагональна: она равна $H_z$ на $N_z$ и $I$ на $N_z^\perp$. Поэтому
$\eta(z)\in N_z$ и $H_z(\eta(z),\nu')=L_z(\nu')$ для всех $\nu'\in N_z$. Отображение $\eta$
аналитично. Так как $H_{tz}=t^{m-2}H_z$ и $\nabla u_{m+1}(tz)=t^m\nabla u_{m+1}(z)$, имеем
$\eta(tz)=t^2\eta(z)$. Положим $\eta_*=\max_\Sigma|\eta|$.

**2.6. Координаты произведения.** Пусть $C>0$ — число, которое будет зафиксировано в лемме 3. До
этого все построения §2.6–§5 годятся при любом фиксированном $C$. Положим
$$L_C=\{\ell=(\omega,\hat\nu):\ \omega\in\Sigma,\ \hat\nu\in N_\omega,\ |\hat\nu|\le C\},\qquad
L^\circ_{2C}=\{\ldots,\ |\hat\nu|<2C\},$$
и выберем $\varepsilon_1=\varepsilon_1(C)>0$ с $2C\varepsilon_1+\varepsilon_1^2\eta_*<\kappa/2$. Для
$\ell\in L^\circ_{2C}$ и $|\varepsilon|<\varepsilon_1$ положим
$$\Gamma(\ell,\varepsilon)=\omega+\nu\bigl(\omega,\ \varepsilon\hat\nu-\varepsilon^2\eta(\omega)\bigr),\qquad
\Phi(r,\ell)=r\,\Gamma(\ell,r^{1/2}),\quad 0<r<\varepsilon_1^2.$$
Аргумент $\nu(\omega,\cdot)$ по норме меньше $\kappa/2$, так что он лежит в области из (M4). По
однородности $\nu$ и $\eta$
$$\Phi(r,\ell)=z+\nu\bigl(z,\ \nu''-\eta(z)\bigr),\qquad z=r\omega,\quad \nu''=r^{3/2}\hat\nu.$$

*$\Phi$ — аналитический диффеоморфизм $(0,\varepsilon_1^2)\times L^\circ_{2C}$ на открытое
множество в $\mathcal N_\kappa$, и $r\le|\Phi(r,\ell)|\le2r$.* Это композиция четырёх инъективных
аналитических локальных диффеоморфизмов $n$-мерных многообразий:

1. $(r,\omega,\hat\nu)\mapsto(z,\nu'')=(r\omega,r^{3/2}\hat\nu)\in\mathfrak N$; обратное:
   $r=|z|$, $\omega=z/|z|$, $\hat\nu=|z|^{-3/2}\nu''$;
2. сдвиг слоя $(z,\nu'')\mapsto(z,\nu''-\eta(z))$; образ лежит в $E_{\kappa/2}$, так как
   $|\nu''-\eta(z)|\le(2Cr^{1/2}+r\eta_*)r<\frac\kappa2r$;
3. $\Psi^{-1}$ на $E_{\kappa/2}$ (M4);
4. $\Phi_0$ на $E_\kappa$ (утверждение T).

Оценка $r\le|\Phi|\le\sqrt{1+\kappa^2}\,r\le2r$ следует из утверждения T и $\kappa\le1$.

*В карте.* Пусть $\ell\leftrightarrow(\theta,a)$, $\hat\nu=\sum_ia_ie_i(\theta)$, $|\hat\nu|=|a|$.
Положим $\tilde\nu(\theta,b)=\nu(\omega(\theta),\sum_jb_je_j(\theta))$ и
$\tilde\eta_j(\theta)=\langle\eta(\omega(\theta)),e_j(\theta)\rangle$. Тогда
$\Gamma(\theta,a,\varepsilon)=\omega(\theta)+\tilde\nu(\theta,\varepsilon a-\varepsilon^2\tilde\eta(\theta))$.
Функция $\tilde\nu$ аналитична, $\tilde\nu(\theta,0)=0$ и $\partial_b\tilde\nu(\theta,0)=(e_1(\theta),\dots,e_c(\theta))$
по (M4). Поэтому $\Gamma(\theta,a,0)=\omega(\theta)$ и $\partial_\varepsilon\Gamma(\theta,a,0)=\sum a_ie_i(\theta)$,
и по (F4)
$$\Gamma(\theta,a,\varepsilon)=\omega(\theta)+\varepsilon\sum_ia_ie_i(\theta)+\varepsilon^2\Gamma_2(\theta,a,\varepsilon),\tag{2.2}$$
где $\Gamma_2$ аналитична на $\Theta'\times\{|a|<2C\}\times(-\varepsilon_1,\varepsilon_1)$.

*Равномерность.* Все функции от $(\theta,a,\varepsilon)$ ниже аналитичны на
$\Theta'_\alpha\times\{|a|<2C\}\times(-\varepsilon_1,\varepsilon_1)$ или на аналогичной области с
меньшим $\varepsilon$. Поэтому они и их производные фиксированного порядка ограничены на компактах
$K_\alpha=\bar\Theta_\alpha\times\{|a|\le C\}\times[0,\varepsilon_0]$, где $\varepsilon_0$ выбрано в
п. 5.1. Запись $O(\cdot)$ ниже означает оценку с константой, общей для всех $\alpha$ и всех
точек $K_\alpha$. Эта константа зависит от $C$, $\gamma$, $\varepsilon_0$ и атласа, но не от $\rho$.

*Метрика на $L^\circ_{2C}$.* Возьмём метрику, индуцированную вложением
$L^\circ_{2C}\subset\mathbb R^n\times\mathbb R^n$, $(\omega,\hat\nu)\mapsto(\omega,\hat\nu)$. В карте
это аналитическая положительно определённая матрица $G(\theta,a)$. Для функции $f$ на $L^\circ_{2C}$
через $\nabla f$ обозначим её градиент в этой метрике. Это векторное поле на $L^\circ_{2C}$, не
зависящее от карты; в карте $\nabla f=G^{-1}df$. Подойдёт и любая другая аналитическая (или
гладкая) метрика.

### §3. Разложение $U$ в координатах

**Лемма 2.** Пусть $f(\ell)=Q_\omega(\hat\nu)+g(\omega)$ на $L^\circ_{2C}$. Существуют
$\varepsilon_2\in(0,\varepsilon_1]$ и функция $h$, аналитическая на
$L^\circ_{2C}\times(-\varepsilon_2,\varepsilon_2)$, такие, что при $0<r<\varepsilon_2^2$
$$U(\Phi(r,\ell))=r^{m+1}\bigl(f(\ell)+r\,h(\ell,r^{1/2})\bigr).$$

*Доказательство.* Положим $\varepsilon=r^{1/2}$.

1. *Ряд.* Пусть ряд Тейлора $\sum_\alpha c_\alpha x^\alpha$ функции $U$ в нуле сходится абсолютно
   при $\max_i|x_i|\le R$, и $U$ равна его сумме там. Положим
   $\tilde U_2(\tau,y)=\sum_{|\alpha|\ge m+2}c_\alpha\tau^{|\alpha|-m-2}y^\alpha$ и $\delta=R/3$. При
   $|\tau|<\delta$, $\max_i|y_i|<3$ имеем
   $|c_\alpha\tau^{|\alpha|-m-2}y^\alpha|\le\delta^{-m-2}|c_\alpha|R^{|\alpha|}$. Значит, это
   абсолютно сходящийся степенной ряд по $(\tau,y)$, и $\tilde U_2$ аналитична на этой области.
   При $0<\tau<\delta$ ещё и $|\tau y_i|<R$, поэтому
   $U(\tau y)=\tau^mu_m(y)+\tau^{m+1}u_{m+1}(y)+\tau^{m+2}\tilde U_2(\tau,y)$.
2. Возьмём $\varepsilon_2=\min(\varepsilon_1,\delta^{1/2})$. Так как $\nu(\omega,\mu)\perp\omega$ и
   $|\nu(\omega,\mu)|<\kappa\le1$, имеем $|\Gamma|\le\sqrt2<3$ при всех $|\varepsilon|<\varepsilon_1$. Поэтому
   $\tilde U_2(\varepsilon^2,\Gamma(\ell,\varepsilon))$ аналитична по $(\ell,\varepsilon)$ при
   $|\varepsilon|<\varepsilon_2$, и при $\varepsilon>0$
   $$r^{-(m+1)}U(\Phi)=\varepsilon^{-2}u_m(\Gamma)+u_{m+1}(\Gamma)+\varepsilon^2\tilde U_2(\varepsilon^2,\Gamma).$$
3. *Член $u_m$.* $\Gamma=\omega+\nu(\omega,\mu)$ с $\mu=\varepsilon\hat\nu-\varepsilon^2\eta(\omega)\in N_\omega$.
   По (M1) и (M4) $u_m(\Gamma)=Q_\omega(\mu)$, то есть
   $$\varepsilon^{-2}u_m(\Gamma)=Q_\omega(\hat\nu)-\varepsilon H_\omega(\hat\nu,\eta(\omega))+\varepsilon^2Q_\omega(\eta(\omega)).$$
4. *Член $u_{m+1}$.* Пусть $\varphi(\varepsilon)=u_{m+1}(\Gamma(\ell,\varepsilon))$. По (2.2)
   $\varphi(0)=g(\omega)$ и $\varphi'(0)=\langle\nabla u_{m+1}(\omega),\hat\nu\rangle=L_\omega(\hat\nu)$.
   По (F4) $\varphi=g(\omega)+\varepsilon L_\omega(\hat\nu)+\varepsilon^2k(\ell,\varepsilon)$ с
   аналитической $k$.
5. *Сокращение.* По п. 2.5 $H_\omega(\hat\nu,\eta(\omega))=L_\omega(\hat\nu)$, и члены порядка
   $\varepsilon$ сокращаются. Остаётся $f(\ell)+\varepsilon^2h$, где
   $h=Q_\omega(\eta(\omega))+k(\ell,\varepsilon)+\tilde U_2(\varepsilon^2,\Gamma(\ell,\varepsilon))$
   аналитична. ∎

**Лемма 3.** Пусть $\rho_1\in(0,1]$ и $C'$ таковы, что $\bar B_{\rho_1}$ лежит в области
аналитичности $U$ и при $|x|\le\rho_1$
$$|U(x)-u_m(x)|\le C'|x|^{m+1},\qquad|\nabla U(x)-\nabla u_m(x)|\le C'|x|^m\tag{3.1}$$
(они существуют, так как ряд $U-u_m$ начинается со степени $m+1$). Положим
$$C_1=\bigl(2^{m+2}C'/\lambda_0\bigr)^{1/2},\qquad C=2(C_1+\eta_*).$$
Тогда при $0<\rho\le\min\bigl(\rho_1,\ c_\kappa/(2C'),\ \varepsilon_1(C)^2\bigr)$ каждая точка
$x\in B_\rho$ с $U(x)<0$ представляется как $x=\Phi(r,\ell)$, где $0<r\le|x|<\rho$ и
$\ell=(\omega,\hat\nu)$, $|\hat\nu|<C/2$. Иначе говоря,
$X\subset\Phi\bigl((0,\rho)\times L^\circ_{C/2}\bigr)$.

*Доказательство.* $x\ne0$, так как $U(0)=0$. Если $x\notin\mathcal N_\kappa$, то по (2.1) и (3.1)
$U(x)\ge c_\kappa|x|^m-C'|x|^{m+1}\ge\frac{c_\kappa}2|x|^m>0$. Значит, $x\in\mathcal N_\kappa$:
$x=z+\nu$, $(z,\nu)\in E_\kappa$, $|z|\le|x|\le2|z|$. Пусть $\nu'=\mu_z(\nu)$. По (M1) и (3.1)
$$U(x)\ge Q_z(\nu')-C'|x|^{m+1}\ge\tfrac{\lambda_0}2|z|^{m-2}|\nu'|^2-2^{m+1}C'|z|^{m+1},$$
так как $H_z=|z|^{m-2}H_{z/|z|}$. Из $U(x)<0$ следует $|\nu'|<C_1|z|^{3/2}$. Положим
$\nu''=\nu'+\eta(z)$. Так как $|z|\le1$, имеем
$|\nu''|<C_1|z|^{3/2}+\eta_*|z|^2\le\frac C2|z|^{3/2}$. Пусть $r=|z|$, $\omega=z/r$,
$\hat\nu=r^{-3/2}\nu''\in N_\omega$. Тогда $|\hat\nu|<C/2$ и
$\Phi(r,\ell)=z+\nu(z,\nu''-\eta(z))=z+\nu(z,\nu')=z+\nu=x$ по (M4). ∎

С этого места **$C$ фиксировано** формулой леммы 3.

**Лемма 4.** Функция $D(\ell)=(m+1)^2f(\ell)^2+|\nabla f(\ell)|^2$ удовлетворяет
$D\ge\gamma^2$ на $L_C$ при некотором $\gamma=\gamma(C)>0$.

*Доказательство.* $D$ непрерывна, а $L_C$ компактно, поэтому достаточно проверить $D>0$ в каждой
точке. Пусть $f(\ell)=0$ и $df(\ell)=0$ (это не зависит от метрики). В карте
$f=\frac12a^{\mathsf T}\tilde H(\theta)a+g(\omega(\theta))$, где
$\tilde H_{ij}(\theta)=H_{\omega(\theta)}(e_i,e_j)\succ0$. Из $\partial_af=\tilde H a=0$ следует $a=0$.
Тогда $\partial_\theta f=\frac12a^{\mathsf T}\partial_\theta\tilde H\,a+\partial_\theta(g\circ\omega)=\partial_\theta(g\circ\omega)$,
и получаем $g(\omega)=0$ и $dg(\omega)=0$, вопреки (B3). При $s=0$ переменной $\theta$ нет, и
противоречие даёт уже $g(\omega)=f=0$. ∎

### §4. Поле

Далее $r<\rho\le\varepsilon_0^2$, где $\varepsilon_0\le\varepsilon_2/2$ выбрано в п. 5.1, и
$\ell\in L^\circ_C$. Пишем $U$ вместо $U\circ\Phi$ и $\varepsilon=r^{1/2}$. На
$(0,\rho)\times L^\circ_C$ положим $V=r\partial_r$ (генератор растяжений
$(r,\ell)\mapsto(tr,\ell)$), $F=r^{m+1}f(\ell)$, $W=U-F=r^{m+2}h(\ell,r^{1/2})$ и
$$R=\frac{(m+1)f\,r\partial_r+\nabla f}{r^{m+1}D(\ell)},$$
где $\nabla f$ поднято как поле без $r$-компоненты. Тогда
$$R(F)=\frac{(m+1)f\cdot(m+1)r^{m+1}f+r^{m+1}|\nabla f|^2}{r^{m+1}D}=1.$$
Далее $V(F)=(m+1)F$ и $V(r^{m+2}h(\ell,r^{1/2}))=r^{m+2}\bigl((m+2)h+\frac12\varepsilon h_\varepsilon\bigr)$,
поэтому
$$U_+:=\tfrac1{m+1}V(U)-U=r^{m+2}p(\ell,\varepsilon),\qquad p=\tfrac1{m+1}\bigl(h+\tfrac12\varepsilon h_\varepsilon\bigr),$$
$$R(W)=r\,q(\ell,\varepsilon),\qquad
q=\frac{(m+1)f\bigl((m+2)h+\frac12\varepsilon h_\varepsilon\bigr)+\nabla f(h)}{D},$$
где $\nabla f(h)$ — производная $h(\cdot,\varepsilon)$ вдоль $\nabla f$. Функции $p$, $q$ аналитичны
на $L^\circ_{2C}\times(-\varepsilon_2,\varepsilon_2)$ там, где $D>0$, в частности в окрестности
компакта $L_C\times[0,\varepsilon_2/2]$ (лемма 4). Пусть $q_*=\max_{L_C\times[0,\varepsilon_2/2]}|q|$.
В п. 5.1 $\varepsilon_0$ выбирается так, что $\varepsilon_0^2q_*\le\frac12$; поэтому
$1+\varepsilon^2q\ge\frac12$ на $L_C\times[0,\varepsilon_0]$, а значит, и $1+rq\ge\frac12$ при $r<\rho$.
Положим
$$A=\frac{V}{m+1}+A_\infty,\qquad A_\infty=-\frac{U_+}{1+R(W)}R=r\bigl(c_1\,V+Y\bigr),$$
$$c_1=-\frac{(m+1)fp}{D(1+rq)},\qquad Y=-\frac{p\,\nabla f}{D(1+rq)},$$
где $c_1(\ell,\varepsilon)$ и поле $Y(\ell,\varepsilon)$ без $r$-компоненты аналитичны по
$(\ell,\varepsilon)$ в окрестности $L_C\times[0,\varepsilon_0]$.

**Лемма 5.** $A(U)=U$ на $(0,\rho)\times L^\circ_C$.

*Доказательство.* $A(U)=\frac1{m+1}V(U)-\frac{U_+}{1+R(W)}\bigl(R(F)+R(W)\bigr)=\frac1{m+1}V(U)-U_+=U$. ∎

### §5. Оценка $DA$ в евклидовых координатах

Работаем в карте $(r,\theta,a)$, $\varepsilon=r^{1/2}$; строки и столбцы матриц нумеруются блоками
$(r\,|\,\theta\,|\,a)$ размеров $1,s,c$. Евклидово представление поля $\hat A$, заданного в
координатах, — это $A^x(\Phi(y))=D\Phi(y)\hat A(y)$. Дифференцируя по $y$, получаем
$$DA^x=\bigl(D^2\Phi[\hat A,\cdot]+D\Phi\,D\hat A\bigr)D\Phi^{-1},\tag{*}$$
где $j$-й столбец $D^2\Phi[\hat A,\cdot]$ равен $\sum_i\hat A_i\,\partial_i\partial_j\Phi$.

**5.1. Якобиан $\Phi$ и выбор $\varepsilon_0$.** Из $\Phi=r\Gamma(\theta,a,r^{1/2})$ и (2.2):
$$\partial_r\Phi=\Gamma+\tfrac12\varepsilon\Gamma_\varepsilon,\qquad\partial_\theta\Phi=r\Gamma_\theta,\qquad
\partial_a\Phi=r\Gamma_a,$$
$$\Gamma_\theta=\partial_\theta\omega+\varepsilon\,a\cdot\partial_\theta e+\varepsilon^2\partial_\theta\Gamma_2,\qquad
\Gamma_{a_i}=\varepsilon\bigl(e_i+\varepsilon\,\partial_{a_i}\Gamma_2\bigr),\qquad
\Gamma_\varepsilon=a\cdot e+2\varepsilon\Gamma_2+\varepsilon^2\partial_\varepsilon\Gamma_2 .$$
Значит, $D\Phi=Q\cdot\operatorname{diag}(1,\ rI_s,\ r\varepsilon I_c)$, где
$$Q(\theta,a,\varepsilon)=\bigl[\ \Gamma+\tfrac12\varepsilon\Gamma_\varepsilon\ \big|\ \Gamma_\theta\ \big|\ e+\varepsilon\,\partial_a\Gamma_2\ \bigr]$$
аналитична вплоть до $\varepsilon=0$ и $Q(\theta,a,0)=[\,\omega\,|\,\partial_\theta\omega\,|\,e\,]$. Столбцы
$Q(\theta,a,0)$ — базис $\mathbb R^n$, согласованный с ортогональным разложением
$\mathbb R\omega\oplus T_\omega\Sigma\oplus N_\omega$. Поэтому $\det Q(\cdot,\cdot,0)\ne0$ на компакте
$\bar\Theta_\alpha\times\{|a|\le C\}$. По равномерной непрерывности существует
$\varepsilon_Q>0$, при котором $|\det Q|$ отделён от нуля на
$\bar\Theta_\alpha\times\{|a|\le C\}\times[0,\varepsilon_Q]$ для всех $\alpha$. Положим
$$\varepsilon_0=\min\bigl(\varepsilon_Q,\ \varepsilon_2/2,\ (2q_*)^{-1/2}\bigr)$$
($q_*$ из §4; при $q_*=0$ последний член опускается). Тогда $c_1$, $Y$ аналитичны в окрестности
$L_C\times[0,\varepsilon_0]$, и их производные там ограничены константами, не зависящими от $\rho$.
Кроме того, $Q$ и $Q^{-1}$ ограничены вместе с производными на $K_\alpha$, и
$$D\Phi^{-1}=\operatorname{diag}\bigl(1,\ r^{-1}I_s,\ (r\varepsilon)^{-1}I_c\bigr)\,Q^{-1}:$$
строки $D\Phi^{-1}$, отвечающие $r$, $\theta$, $a$, имеют порядки $O(1)$, $O(1/r)$,
$O(1/(r\varepsilon))$. Вторые производные по (2.2):
$$\partial_\theta^2\Phi=O(r),\quad\partial_\theta\partial_a\Phi=r\bigl(\varepsilon\,\partial_\theta e+O(\varepsilon^2)\bigr)=O(r\varepsilon),\quad
\partial_a^2\Phi=r\varepsilon^2\partial_a^2\Gamma_2=O(r\varepsilon^2),$$
$$\partial_r\partial_\theta\Phi=\Gamma_\theta+\tfrac12\varepsilon\Gamma_{\varepsilon\theta}=O(1),\qquad
\partial_r\partial_a\Phi=\Gamma_a+\tfrac12\varepsilon\Gamma_{\varepsilon a}=O(\varepsilon).$$
Производная $\partial_r^2\Phi=O(r^{-1/2})$ ниже не нужна: (*) применяется только к полю без
$r$-компоненты (п. 5.3), а поля $V$ и $rc_1V$ разобраны отдельно.

**5.2. Поле $V$.** $DV^x=I+\frac12P_{N_\omega}+O(r^{1/2})$, где $\omega=\omega(\ell(x))$.

*Доказательство.* $V^x=r\partial_r\Phi=r\Gamma+\frac12r^{3/2}\Gamma_\varepsilon=x+\frac12r^{3/2}K$, где
$K=\Gamma_\varepsilon(\theta,a,\varepsilon)$. Значит,
$DV^x=I+D_{(r,\theta,a)}\bigl(\tfrac12r^{3/2}K\bigr)\,D\Phi^{-1}$. Разберём столбцы:

- по $r$: $\partial_r(\frac12r^{3/2}K)=\frac34r^{1/2}K+\frac14rK_\varepsilon=O(r^{1/2})$; умножение
  на строку $O(1)$ даёт $O(r^{1/2})$;
- по $\theta$: $\frac12r^{3/2}K_\theta=O(r^{3/2})$; умножение на строки $O(1/r)$ даёт $O(r^{1/2})$;
- по $a_i$: $K_{a_i}=e_i+O(\varepsilon)$ по (2.2). Строка $a_i$ матрицы $D\Phi^{-1}$ равна
  $(r\varepsilon)^{-1}(Q^{-1})_{a_i}$, и $(Q^{-1})_{a_i}(\theta,a,\varepsilon)=(Q^{-1})_{a_i}(\theta,a,0)+O(\varepsilon)$.
  Вклад: $\frac{r^{3/2}}{2r\varepsilon}\sum_i(e_i+O(\varepsilon))\otimes(Q^{-1})_{a_i}=\frac12\sum_ie_i\otimes(Q^{-1}(\theta,a,0))_{a_i}+O(\varepsilon)$.

При $\varepsilon=0$ строка $e_i^{\mathsf T}$ даёт $e_i^{\mathsf T}\omega=0$,
$e_i^{\mathsf T}\partial_\theta\omega=0$ и $e_i^{\mathsf T}e_j=\delta_{ij}$. Значит, строки
$(Q^{-1}(\theta,a,0))_{a_i}=e_i^{\mathsf T}$, и $\sum_ie_ie_i^{\mathsf T}=P_{N_\omega}$. ∎

**5.3. Член $rY$.** Вклад поля $\hat A_Y=(0,\ rY^\theta,\ rY^a)$ в $DA^x$ есть $O(r^{1/2})$.

*Доказательство.* Применим (*).

(i) $D\Phi\,D\hat A_Y\,D\Phi^{-1}=Q\bigl(S\,D\hat A_Y\,S^{-1}\bigr)Q^{-1}$, где
$S=\operatorname{diag}(1,rI_s,r\varepsilon I_c)$. Элементы $D\hat A_Y$: строка $r$ нулевая; столбец
$r$ — $\partial_r(rY)=Y+\frac12\varepsilon Y_\varepsilon=O(1)$; остальные — $r\,\partial_{\theta,a}Y=O(r)$.
Сопряжение умножает блок $(i,j)$ на $s_i/s_j$:

| блок | порядок |
|---|---|
| $(\theta,r)$ | $r\cdot O(1)=O(r)$ |
| $(a,r)$ | $r\varepsilon\cdot O(1)=O(r^{3/2})$ |
| $(\theta,\theta)$, $(a,a)$ | $O(r)$ |
| $(\theta,a)$ | $\frac{r}{r\varepsilon}O(r)=O(r^{1/2})$ |
| $(a,\theta)$ | $\frac{r\varepsilon}{r}O(r)=O(r^{3/2})$ |

(ii) Столбцы $D^2\Phi[\hat A_Y,\cdot]=rY^\theta\partial_\theta\partial_j\Phi+rY^a\partial_a\partial_j\Phi$:
при $j=r$ это $r\,O(1)+r\,O(\varepsilon)=O(r)$; при $j=\theta$ — $r\,O(r)+r\,O(r\varepsilon)=O(r^2)$; при
$j=a$ — $r\,O(r\varepsilon)+r\,O(r\varepsilon^2)=O(r^2\varepsilon)$. Умножение справа на $D\Phi^{-1}$
(строки $O(1)$, $O(1/r)$, $O(1/(r\varepsilon))$) даёт $O(r)$. ∎

**5.4. Член $rc_1V$.** Его евклидово представление $(rc_1)\,V^x$, и
$D\bigl((rc_1)V^x\bigr)=rc_1\,DV^x+V^x\otimes\nabla_x(rc_1)$. Первое слагаемое $O(r)$ по п. 5.2.
Далее $\nabla_x(rc_1)=D_{(r,\theta,a)}(rc_1)\,D\Phi^{-1}$, где $\partial_r(rc_1)=c_1+\frac12\varepsilon c_{1,\varepsilon}=O(1)$,
$\partial_\theta(rc_1)=O(r)$, $\partial_a(rc_1)=O(r)$. Отсюда
$\nabla_x(rc_1)=[O(1),O(1),O(1/\varepsilon)]\,Q^{-1}=O(r^{-1/2})$. Так как $|V^x|=r|\Gamma+\frac12\varepsilon\Gamma_\varepsilon|=O(r)$,
второе слагаемое — $O(r^{1/2})$. ∎

**Итог §5.** Существуют $K_5$ и $K_A$, не зависящие от $\rho$, такие, что на
$\mathcal O:=\Phi\bigl((0,\rho)\times L^\circ_C\bigr)$
$$\Bigl\|DA^x-\tfrac1{m+1}\bigl(I+\tfrac12P_{N_\omega}\bigr)\Bigr\|\le K_5\,r^{1/2},\qquad |A^x|\le K_A\,r\le K_A|x|.$$
Вторая оценка: $A^x=\frac{V^x}{m+1}+rc_1V^x+D\Phi\,(0,rY)$, где $|V^x|=O(r)$ и
$|D\Phi\,(0,rY)|=|r\Gamma_\theta\,rY^\theta+r\Gamma_a\,rY^a|=O(r^2)$. При $K_5\rho^{1/2}\le\frac1{2(m+1)}$
$$\operatorname{sym}DA^x\succeq\tfrac1{m+1}I-K_5r^{1/2}I\succeq\tfrac1{2(m+1)}I\qquad\text{на }\mathcal O.$$

### §6. Порядок выбора констант и завершение

Константы выбираются в таком порядке, без порочного круга:

1. $\lambda_0,\Lambda$ (п. 2.1(d)); проектор $P$ на окрестности $\mathcal V$ (п. 2.1(e)).
2. Атлас и рамки (п. 2.2); они не зависят от последующих констант.
3. $\kappa=\min(\kappa_T,\kappa_M,1)$ (утверждение T, (M3)); затем $c_\kappa$ (2.1), $C_\mu$ (M3) и
   $\eta_*$ (п. 2.5).
4. $\rho_1$, $C'$ из (3.1).
5. $C=2(C_1+\eta_*)$ (лемма 3), затем $\varepsilon_1(C)$ (п. 2.6) и метрика на $L^\circ_{2C}$.
6. $\gamma=\gamma(C)$ (лемма 4).
7. $\varepsilon_2$ (лемма 2), $q_*$ (§4), $\varepsilon_Q$ и
   $\varepsilon_0=\min(\varepsilon_Q,\varepsilon_2/2,(2q_*)^{-1/2})$ (п. 5.1).
8. $K_5$, $K_A$ (§5). Они зависят от предыдущих констант, но не от $\rho$: все оценки §5 — оценки
   аналитических функций на фиксированных компактах $K_\alpha$.
9. Наконец, $\rho>0$ с
   $$\rho\le\min\Bigl(\rho_1,\ \frac{c_\kappa}{2C'},\ \varepsilon_0^2,\ \frac1{(2(m+1)K_5)^2},\ \rho_7\Bigr),$$
   где $\rho_7$ — из §7. Строго говоря, ещё нужно $\rho<\rho_1$, чтобы $U$ была аналитична в
   окрестности $\bar B_\rho$; так и считаем.

*Завершение.* Множество $\mathcal O=\Phi\bigl((0,\rho)\times L^\circ_C\bigr)$ открыто (§2.6), и
$X\subset\mathcal O$ по лемме 3, так как $L^\circ_{C/2}\subset L^\circ_C$. Поле $A^x$ аналитично на
$\mathcal O$: это $D\Phi\cdot\hat A\circ\Phi^{-1}$, где $\Phi$ — аналитический диффеоморфизм, а
$\hat A$ аналитично. По лемме 5 $\langle A^x,\nabla U\rangle=U$ на $\mathcal O$, то есть условие
леммы 1 выполнено с $p=1$. По §5 $\operatorname{sym}DA^x\succeq0$ и $|A^x|\le M:=K_A\rho$ на
$\mathcal O$. $U$ аналитична, тем более класса $C^2$, около $\bar B_\rho$. По лемме 1 получаем (a)
с $T(E)=2w(E)M/|E|$. Из (a), п. 0.4 и следствия леммы 1 получаем (b). Утверждение (c) доказано в
§7. ∎

### §7. Изолированность: доказательство (c)

Положим
$$\rho_7=\min\Bigl(\frac{mc_\kappa}{2C'},\ \Bigl(\frac C{2\eta_*}\Bigr)^2,\ \Bigl(\frac{\lambda_0C}{2^{m+3}C'}\Bigr)^2\Bigr)$$
(при $\eta_*=0$ второй член опускается). Пусть $0<|x|<\rho$. Покажем, что $\nabla U(x)\ne0$.

1. *$x\notin\mathcal N_\kappa$.* По формуле Эйлера, (2.1) и (3.1)
   $\langle x,\nabla U(x)\rangle=mu_m(x)+\langle x,\nabla(U-u_m)(x)\rangle\ge mc_\kappa|x|^m-C'|x|^{m+1}>0$,
   так как $|x|<\rho\le mc_\kappa/(2C')$.
2. *$x\in\mathcal N_\kappa$*: $x=z+\nu$, $(z,\nu)\in E_\kappa$, $\nu'=\mu_z(\nu)$,
   $\nu''=\nu'+\eta(z)$, $|z|\le|x|<\rho$.
   - *(2a) $|\nu''|<C|z|^{3/2}$.* Тогда, как в конце доказательства леммы 3, $x=\Phi(r,\ell)$ с
     $r=|z|<\rho$ и $\ell\in L^\circ_C$, то есть $x\in\mathcal O$. На $\mathcal O$ поле $R$ из §4
     определено, и $R(U\circ\Phi)=R(F)+R(W)=1+rq\ge\frac12$. Если бы $\nabla U(x)=0$, то
     $d(U\circ\Phi)=0$ в точке $\Phi^{-1}(x)$ и $R(U\circ\Phi)=0$ там — противоречие.
   - *(2b) $|\nu''|\ge C|z|^{3/2}$.* Тогда $|\nu'|\ge C|z|^{3/2}-\eta_*|z|^2\ge\frac C2|z|^{3/2}$, так
     как $\eta_*|z|^{1/2}\le C/2$. Пусть $e=\nu'/|\nu'|\in N_z$. Образ слоя
     $\{\mu_z(\nu):\ |\nu|<\kappa|z|\}$ открыт (M3, M4), поэтому кривая
     $x(\tau)=z+\nu(z,\nu'+\tau e)$ определена при малых $|\tau|$ и $x(0)=x$. По (M1)
     $u_m(x(\tau))=Q_z(\nu'+\tau e)$, поэтому
     $$\frac{d}{d\tau}\Big|_0U(x(\tau))=H_z(\nu',e)+\bigl\langle\nabla(U-u_m)(x),\ D_{\nu'}\nu(z,\nu')\,e\bigr\rangle.$$
     Первый член равен $H_z(\nu',\nu')/|\nu'|\ge\lambda_0|z|^{m-2}|\nu'|\ge\frac{\lambda_0C}2|z|^{m-1/2}$.
     Второй по модулю не больше $C'|x|^m\cdot2\le2^{m+1}C'|z|^m$ по (3.1), (M4) и $|x|\le2|z|$. Сумма
     не меньше $|z|^{m-1/2}\bigl(\frac{\lambda_0C}2-2^{m+1}C'|z|^{1/2}\bigr)>0$, так как
     $|z|^{1/2}<\rho_7^{1/2}\le\lambda_0C/(2^{m+3}C')$. Значит, $\nabla U(x)\ne0$. ∎

### §8. Пример: доказательство предложения

$U=q^2+xz^4$, $q=x^2+y^2-z^2$; $u_4=q^2$, $u_5=xz^4$, $u_k=0$ при $k\ge6$.

1. *(B1).* $u_4=q^2\ge0$, и $\Sigma=\{x^2+y^2=z^2,\ x^2+y^2+z^2=1\}$ — две окружности
   $\omega_\pm(\theta)=(\cos\theta,\sin\theta,\pm1)/\sqrt2$, $s=1$.
2. *(B2).* На $Z$ имеем $q=0$, поэтому $D^2u_4=2\nabla q\,\nabla q^{\mathsf T}+2qD^2q=2\nabla q\,\nabla q^{\mathsf T}$,
   где $\nabla q=(2x,2y,-2z)$. В точке $\omega_\pm(\theta)$:
   $\nabla q=\sqrt2(\cos\theta,\sin\theta,\mp1)$, и он ортогонален
   $\omega_\pm$ и $\partial_\theta\omega_\pm=(-\sin\theta,\cos\theta,0)/\sqrt2$. Значит,
   $N_{\omega_\pm}=\mathbb R\,n_\pm$, $n_\pm=(\cos\theta,\sin\theta,\mp1)/\sqrt2$, и
   $H(n_\pm,n_\pm)=2\langle\nabla q,n_\pm\rangle^2=2\cdot2^2=8>0$.
3. *(B3).* $g(\omega_\pm(\theta))=\frac{\cos\theta}{\sqrt2}\cdot\frac14=\frac{\cos\theta}{2^{5/2}}$ на
   обеих окружностях. Нули: $\theta=\pm\pi/2$, там $\frac{dg}{d\theta}=\mp2^{-5/2}\ne0$.
4. *Не минимум.* Для $\omega\in\Sigma$ имеем $U(t\omega)=t^5g(\omega)$ (так как $u_4(\omega)=0$ и
   старших членов нет). Это меньше нуля при $t>0$ и $\cos\theta<0$.
5. *Единственность вещественной критической точки.*
   $\nabla U=\bigl(4xq+z^4,\ 4yq,\ -4z(q-xz^2)\bigr)$. Пусть $\nabla U=0$, $(x,y,z)\in\mathbb R^3$.
   - Если $q=0$, то из первой компоненты $z=0$, тогда $x^2+y^2=q=0$, и $x=y=0$.
   - Если $q\ne0$, то из второй $y=0$. При $z=0$ имеем $q=x^2$, и первая компонента
     $4x^3=0$ даёт $x=0$, $q=0$ — противоречие. При $z\ne0$ из третьей $q=xz^2$, и первая
     компонента равна $4x^2z^2+z^4=z^2(4x^2+z^2)>0$ — противоречие.

   Итак, $0$ — единственная вещественная критическая точка. Это согласуется с теоремой B(c).
6. *Над $\mathbb C$.* При $z=0$, $x=\pm iy$ имеем $q=x^2+y^2=0$, и все три компоненты $\nabla U$
   равны нулю. Через $0$ проходят две комплексные прямые критических точек: над $\mathbb C$ точка
   $0$ не изолирована. Это иллюстрирует ловушку «изолированность над $\mathbb R$ не влечёт
   изолированность над $\mathbb C$». Теорема B комплексной изолированности не требует. Методы,
   которым она нужна (например, конечность числа Милнора), к этому примеру неприменимы. ∎

## Где работает аналитичность или изолированность

- **Изолированность** не предполагается и не используется. Она **выводится** из (B1)–(B3) (§7).
  Значит, теорема B ничего не говорит о неизолированных критических точках.
- **Аналитичность** используется в двух местах:
  1. в лемме 2 — чтобы остаток $h$ был гладким (аналитическим) вплоть до $\varepsilon=0$; это
     единственное место, где участвует весь ряд $U$, а не $u_m$ и $u_{m+1}$;
  2. в лемме 3 и в §7 — только через тейлоровские оценки (3.1), для которых хватает $C^{m+1}$.

  Аналитичность конуса $Z$, проектора $P$, отображения Морса, сдвига $\eta$ и функции $\Gamma$
  следует из того, что $u_m$ и $u_{m+1}$ — многочлены. Для этих объектов аналитичность $U$ не
  нужна.
- **Почему нет противоречия с $C^\infty$-контрпримерами.** Работу, которую в задаче (A) должна
  делать аналитичность, здесь делают условия невырожденности (B1)–(B3) на $(m+1)$-струю
  (см. замечание 3). Известные гладкие контрпримеры этим условиям не удовлетворяют:
  - Пенлеве–Уинтнер и Лалуа: потенциал плоский в $0$, $u_m$ не существует, (B1) нарушено (формулы
    по вторичным источникам, `notes/literature/2026-10-21-counterexamples-nonstrict.md`);
  - Уренья: $0$ — локальный максимум (по вторичным источникам, не сверено). Для любого локального
    максимума младшая ненулевая форма $u_m\le0$, а с $u_m\not\equiv0$ условие $u_m\ge0$ из (B1)
    невыполнимо; если ряд плоский, (B1) тоже нарушено;
  - $U=y^2+e^{-1/x^2}\cos(1/x)$ на $\mathbb R^2$ (пример рецензента R2) — $C^\infty$, выполнены
    (B1), (B2): $u_2=y^2$, $\Sigma=\{(\pm1,0)\}$, $H=2$. Но $u_3\equiv0$, то есть $g\equiv0$ и (B3)
    нарушено. При этом равновесие **устойчиво** по Ляпунову [Доказано]: переменные разделяются;
    $y$ — гармонический осциллятор, а для $x$ при $x_K=1/(2\pi K)$ имеем
    $\varphi(\pm x_K)=e^{-(2\pi K)^2}>0$, где $\varphi(x)=e^{-1/x^2}\cos(1/x)$. Начальные данные с
    $|x_0|<x_K$ и $\frac12\dot x_0^2+\varphi(x_0)<\varphi(x_K)$ (они заполняют окрестность нуля)
    дают $|x(t)|<x_K$ при всех $t$ по сохранению энергии $x$-подсистемы $E_x$: в точках $\pm x_K$
    было бы $\frac12\dot x^2=E_x-\varphi(x_K)<0$. Заодно $\dot x^2=2(E_x-\varphi(x))<4\varphi(x_K)$,
    так как $|\varphi(x)|\le e^{-1/x^2}\le\varphi(x_K)$ при $|x|\le x_K$. Значит, в гладком классе
    (B3) отбросить нельзя. (Здесь $0$ — неизолированная критическая точка: критические точки
    $\varphi$ накапливаются к $0$.)

## Замечания

**1. Об условиях.** Всё в шаге 0: $m\ge2$ чётно, $n\ge2$, $s\le n-2$, а условие
$\Sigma\ne\varnothing$ необходимо (иначе $u_m>0$ на сфере и $0$ — строгий минимум). (B3) равносильно
тому, что $u_{m+1}|_{Z\setminus0}$ не имеет критических точек (п. 2.1(g)). [Эскиз] Компоненты
$\Sigma$ разной размерности доказательство, по-видимому, тоже допускает: всё делается
покомпонентно (трубки над разными компонентами при малом $\kappa$ не пересекаются), а константы
берутся худшие из конечного числа. Это наблюдение R2 (замечание 8); отдельно не выписано и не
проверено, поэтому в формулировке (B1) размерность $s$ общая.

**2. Частные случаи с известным ответом** (проверка согласованности).

- *$n=2$:* $s=0$, $\Sigma$ — конечное множество, симметричное относительно $0$. Условия означают,
  что в каждой точке $\omega\in\Sigma$ форма $u_m$ имеет нуль ровно второго порядка по нормали к
  лучу, а $u_{m+1}(\omega)\ne0$. Пример: $U=y^2+x^3$; здесь
  $\eta=0$, $h=0$, $A=V/3=(x/3,\ y/2)$, $A(U)=U$ и $DA=\operatorname{diag}(\frac13,\frac12)=\frac13(I+\frac12P_N)$
  точно. При $n=2$ тотальная неустойчивость для любого аналитического $U$ приписывается Паламодову
  1977 [P77] (по вторичным источникам; не сверено), так что при $n=2$ теорема B нового не даёт.
- *Однородный $U=u_m$:* $u_{m+1}\equiv0$, (B3) нарушено. Так и должно быть: здесь $0$ — нестрогий
  минимум, и заключение (b) было бы ложным.
- *Невырожденная младшая форма* ($\nabla u_m\ne0$ при $x\ne0$, случай теоремы 3 [P20]) несовместима
  с (B1): на $\Sigma\ne\varnothing$ имеем $\nabla u_m=0$. Области применимости не пересекаются.
- *Квазиоднородный пример* $U=y^2+x^3$ (веса $2,3$) покрывается и теоремой B, и (по пересказу)
  теоремой 6 [P20]. Противоречия нет.

**3. Гладкий случай.** [Эскиз] Пусть $U\in C^k$ около $0$, $k\ge m+4$, $u_j$ — однородные части
многочлена Тейлора, и выполнены (B1)–(B3). Тогда заключения (a)–(c) верны.

*Эскиз.* Аналитичность $U$ используется только так, как перечислено в разделе «Где работает
аналитичность». (i) §2 строится по многочленам $u_m$, $u_{m+1}$ и не меняется. (ii) В лемме 2 шаг 1
заменяется формулой Тейлора с интегральным остатком для $\tau\mapsto U(\tau y)$:
$$\tilde U_2(\tau,y)=\int_0^1\frac{(1-\sigma)^{m+1}}{(m+1)!}\,D^{m+2}U(\sigma\tau y)[y^{\otimes(m+2)}]\,d\sigma\in C^{k-m-2},$$
и тогда $h\in C^{k-m-2}\subset C^2$. (iii) $p$, $q$ содержат первые производные $h$, поэтому
$c_1,Y\in C^{k-m-3}\subset C^1$. В §5 нужны только первые производные $c_1$, $Y$ (и производные
$\Gamma$, которая аналитична), а $\varepsilon_0$, $q_*$, $K_5$ — оценки непрерывных функций на
компактах. (iv) Лемме 3 и §7 нужны (3.1), то есть $C^{m+1}$; лемме 1 нужна $C^2$. *Пробел:* §4–§5
не перечитаны построчно в классе $C^{k-m-3}$ и эскиз не проверен рецензентом. Порог $m+4$ может
быть не точным. Ср. отзыв R2, замечание 2.

**4. Новизна и сравнение с литературой.** Что сверено и что нет:

- *Сверено* рецензентом R2 по PDF: Burgos, arXiv:2506.19135, следствие 12.5 (= 1.4; ньютонов
  случай). Оно требует $U_{l_2}<0$ на критических точках $U_{l_1}|_{S^{n-1}}$ с $U_{l_1}\le0$.
  При (B1)–(B3) это $\Sigma$ и $U_{l_2}=u_{m+1}$, а $g$ нечётна (шаг 0.3). Значит, условие
  невыполнимо, и области применимости не пересекаются. Сам препринт Burgos 2025 нами не проверен.
- *Не сверено, первоисточник недоступен с сервера* (Math-Net.Ru): Паламодов [P20], УМН 75:3
  (2020). Пересказ теорем — в конспекте `notes/vlad-claude/palamodov2020.md` (vlad-claude,
  27.09.2026; не проверен).
  - Теорема 3 (по пересказу $\nabla u_m\ne0$ при $x\ne0$) неприменима: см. замечание 2.
  - Теорема 6 (по пересказу: квазиоднородная невырожденная главная часть). R2 проверил
    [Эскиз], что в исходных координатах примера ни одна взвешенная срезка не невырождена:
    показатель $(1,0,4)$ монома $xz^4$ лежит строго выше многогранника Ньютона $q^2$, и все
    срезки — грани $q^2$, они вырождены. Что никакая аналитическая замена координат не делает
    главную часть невырожденной квазиоднородной — [Гипотеза].
  - Теорема 5 (по пересказу: сведение к ограничению на ядро квадратичной части). **[Гипотеза]
    (R2): случай $m=2$ теоремы B покрывается теоремой 5 [P20].** Довод в её пользу [Доказано]:
    при $m=2$ конус $Z=K:=\ker u_2$ — линейное подпространство, (B2) выполнено автоматически, а
    (B3) равносильно тому, что кубическая форма $u_3|_K$ не имеет критических точек на
    $K\setminus0$ (п. 2.1(g)). Это условие теоремы 3 для ограничения на ядро. Формулировку
    теоремы 5 сверить не удалось. Поэтому новизну следует ограничить случаем $m\ge4$ (и $n\ge3$).
  - Теорема 1 (Козлов–Паламодов: по пересказу $u_m$ не имеет минимума) неприменима: $u_m\ge0$.
- *Не сверено, по рецензиям zbMATH:* Taliaferro 1990 (ARMA 109; асимптотическое решение, если
  младшая положительно однородная часть принимает отрицательные значения; здесь $u_m\ge0$).
  Wiener 1993 (JDE 103; коранг 2 квадратичной части). **Новое наблюдение:** при $m=2$, $s=1$
  коранг $u_2$ равен $s+1=2$, так что при $m=2$ теорема B может пересекаться с Wiener 1993.
  В исходном тексте Wiener исключён только для примера ($m=4$).
- *Не открывались:* Alva–Garcia 2017 (условие (H3); утверждение исходного текста, что на примере
  оно нарушается, не проверено), Maffei–Moauro–Negrini 1989, 1991, Козлов–Фурта (гл. 4),
  Laloy–Peiffer 1982.
- *Неустойчивость по Ляпунову* в условиях теоремы B, возможно, получается и известными методами
  асимптотических траекторий (Козлов, Фурта, степенная геометрия Брюно) в тех же координатах:
  точка минимума $g$ при $\hat\nu=0$ даёт «луч» укороченной системы. [Гипотеза] (исходный текст).
  Тогда новое в теореме B — **тотальная** неустойчивость для этого класса при $m\ge4$, $n\ge3$.
  Это тоже [Гипотеза] до сверки с [P20].

**5. Обобщения** [Гипотеза] (из исходного текста, не проверялись). Вместо $u_{m+1}$ можно брать
первый член $u_{m+j}$, не равный тождественно нулю на $\Sigma$, с весами $1$ и $1+j/2$. Тогда
члены промежуточных степеней надо убирать сдвигами. Другой вариант — $\Sigma$ как Морс–Боттово
многообразие критических точек $u_m|_{S^{n-1}}$ седлового типа.

**6. Эксперименты** (подкрепляют, но не доказывают).

- R2: `experiments/reviewer/thmB/`. Поле построено ровно по §2.6, §4 (mpmath, 80 знаков) для
  примера ($m=4$) и для $U=(x^2+y^2-z^2)^2(x^2+2y^2+3z^2)+xz^4(x^2+y^2+z^2)+y^8$ ($m=6$,
  нетривиальное отображение Морса). На масштабах $r=10^{-2}\ldots10^{-8}$:
  $|A(U)/U-1|<10^{-48}$, $\lambda_{\min}(\operatorname{sym}DA)\to\frac1{m+1}$, а
  $\|DV-I-\frac12P_N\|$ убывает как $r^{1/2}$. 200 траекторий не нарушили оценку леммы 1.
- prover: `experiments/prover/thmB/check_thmB.py` (sympy, точная арифметика), вывод в
  `experiments/prover/thmB/out.txt`. Проверено: разбор примера (§8, включая комплексные прямые);
  на примере в точной параметризации §2.6 — разложение леммы 2 ($h$ — многочлен), тождество
  леммы 5 $A(U)=U$, $Q(\cdot,0)=[\omega|\partial_\theta\omega|e]$ (п. 5.1) и
  $DV^x=I+\frac12P_N+O(\varepsilon)$, $DA^x=\frac15(I+\frac12P_N)+O(\varepsilon)$ в нескольких
  точках (ряд по $\varepsilon$); для $m=6$ с нетривиальным отображением Морса — сокращение члена
  порядка $\varepsilon$ в лемме 2 (ряд по $\varepsilon$); случай $n=2$, $U=y^2+x^3$.

## Пробелы

- В доказательстве теоремы B (§0–§7) и предложения (§8) пробелов не известно. Исправленный текст
  ещё не прошёл независимую проверку.
- Стандартные факты (F1)–(F3) приведены с точными формулировками, но номера теорем в учебниках
  не сверены.
- Вне доказательства: замечание 1 (компоненты разной размерности) и замечание 3 ($C^{m+4}$) —
  [Эскиз]; утверждения о литературе в замечании 4 частично не сверены (перечислено там же).

## Отличия от исходного текста

Математика доказательства не менялась. Изменения:

1. **Формулировка.** Фраза «изолированность не предполагается» заменена утверждением (c):
   изолированность следует из (B1)–(B3); добавлен §7 с доказательством (по замечанию 1 R2,
   перепроверено). Элементарные следствия условий (чётность $m$, $s\le n-2$, $n\ge2$,
   необходимость $\Sigma\ne\varnothing$, знак $g$) собраны в шаге 0.
2. **Лемма 1.** Указано $U\in C^2$ в окрестности $\bar B_\rho$; дано определение тотальной
   неустойчивости, как в 001; в следствие добавлена продолжаемость решения.
3. **П. 2.1.** Добавлены аналитический проектор $P$ (проектор Рисса) и
   подробное доказательство аналитичности $Z\setminus0$.
4. **П. 2.2–2.3 (пробел (а), замечание 4 R2).** Карты и рамки вынесены в начало. Инъективность
   $\Phi_0$ на всей конической области доказана (утверждение T, п. 2).
5. **П. 2.4 (пробел (б), замечание 5 R2).** Операторы на слоях $N_z$ продолжены на $\mathbb R^n$
   (блочно, с $I$ на $N_z^\perp$), отсюда аналитичность по $(z,\nu)$. Выписаны явные константы
   инъективности и образа отображения Морса, оценки обратного.
6. **П. 2.6 и §5.** Введено разложение (2.2) $\Gamma=\omega+\varepsilon a\cdot e+\varepsilon^2\Gamma_2$,
   из которого все порядки §5.1 читаются сразу. Метрика на $L_C$ зафиксирована (индуцированная).
7. **Лемма 2.** Обоснована аналитичность $\tilde U_2$ вплоть до $\tau=0$ (шаг 1).
8. **Лемма 3, §6 (пробел (в), замечания 6–7 R2).** Константы выписаны явно. Выбор $\varepsilon_0$
   в п. 5.1 сделан явно, порядок выбора всех констант — в §6.
9. **§8 (пробел (д), замечание 3 R2).** Разбор примера выписан полностью: изолированность над
   $\mathbb R$, «не минимум», (B1)–(B3), неизолированность над $\mathbb C$. В исходном тексте
   ссылка «[Доказано, разбор случаев в theoremB.md]» вела на отсутствующий разбор.
10. **Замечания (пробелы (е), (ж)).** Замечание о $C^k$ помечено [Эскиз] с порогом $k\ge m+4$.
    Раздел о новизне разделён на сверенное и несверенное. Добавлены [Гипотеза] R2 о $m=2$ и
    теореме 5 [P20], довод в её пользу и наблюдение о Wiener 1993 при $m=2$, $s=1$. Добавлены
    раздел «Где работает аналитичность или изолированность» и частные случаи.

## Найденные проблемы

Новых ошибок в математике не найдено. Найденные недочёты исходного текста (все исправлены выше):

1. Ссылка на «разбор случаев в `theoremB.md`» для изолированности в примере вела на отсутствующий
   текст (уже отмечено R2).
2. Сравнение с Wiener 1993 в исходном тексте сделано только для примера ($u_2=0$). Для самой
   теоремы B при $m=2$, $s=1$ коранг $u_2$ равен 2, и пересечение с Wiener 1993 возможно. Это
   вопрос о новизне, а не о верности; вместе с [Гипотеза] R2 о теореме 5 [P20] это говорит за то,
   чтобы заявлять новизну только при $m\ge4$.
