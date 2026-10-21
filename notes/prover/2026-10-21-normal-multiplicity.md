# Постоянная нормальная кратность $2r\ge4$: асимптотические траектории вдоль конуса нулей с вырожденным нормальным профилем ($n=3$)

- **Автор:** prover (агент), 21.10.2026. Задание главного агента: обобщить теоремы K1/K2 результата
  008 на компоненту-кривую $\Sigma_0$, вдоль которой $D^2u_m$ на нормали вырожден, а
  $u_m\asymp\operatorname{dist}(\cdot,\text{конус над }\Sigma_0)^{2r}$, $r\ge2$; проверить примеры
  полигона M1, M2.
- **Статус:** по пунктам — таблица в §0. Независимой проверки нет.
- **Зависит от:**
  - [007] = [`results/007-gt3.md`](../../results/007-gt3.md) [Проверено: R16, R17]: теорема A,
    лемма 1, шаги 1, 3, 6 доказательства теоремы 2;
  - [008] = [`results/008-class-K.md`](../../results/008-class-K.md): §1 (формула (1.1)), лемма K3,
    лемма 2′ (§8) и доказательство теоремы 2′ (§9). Доказательства проверены рецензентами R20–R22
    в записке `notes/prover/2026-10-21-gt3-hardcore.md`, но **результат 008 окончательно не
    принят** (текст на финальной проверке). Формулы (10.2)–(10.4) из 008 здесь выведены заново
    (§4.2) и проверены символьно для дна вида ряда Пюизё;
  - стандартные теоремы: аналитическая теорема о неявной функции, оценки Коши, теорема
    Ньютона–Пюизё (только в лемме N3; [Литература: стандартная, например E. Casas-Alvero,
    *Singularities of plane curves*, LMS LN 276, 2000, гл. 1; не сверено с первоисточником]).
  - Записка ГА `notes/main-agent/2026-10-21-free-Y.md` (свободное поле $Y$) и теорема E
    (`notes/prover/2026-10-21-euler-field.md`) **не используются**.
- **Скрипты** [Эксперимент]: [`experiments/prover/normal-multiplicity/`](../../experiments/prover/normal-multiplicity/), см. §8.

## 0. Сводка

**Основная идея.** У поворачивающейся полярной карты теоремы K2 [008] все члены, зависящие от
поперечной переменной $b$ (перекрёстные члены $\gamma_1|b|$, $\gamma_2|b|$ и кривизна $C_1|b|^2$),
на деле зависят только от **угловой** компоненты $b'=\theta$; нормальная компонента $b''=e$ входит в
геометрию карты лишь через величины, стремящиеся к нулю при $x\to0$ (нормальное направление узкое,
вес $c>1$, и карта в нём асимптотически плоская). Поэтому от профиля по $e$ нужна только
коэрцитивность и неравенство Эйлера, а не квадратичная нижняя оценка. Это снимает препятствие R3
из [007] (вырожденные поперечные минимумы в кривых картах) для **нормального** направления; для
углового направления препятствие остаётся (§7).

| № | Утверждение | Статус |
|---|---|---|
| Л. N1 | весовое перемасштабирование: $U(s\omega+s^{1+\gamma}\varepsilon n)=s^{m+\beta'}\tilde U(s^{1/N},\theta,\varepsilon)$, $\tilde U$ аналитична, $\tilde U(0,\cdot)=\Phi_0$ | [Доказано] |
| Л. N2 | функция дна: $F_{\rm fl}(s,\theta)=s^{j}\big(G_{\min}(\theta)+O(s^{1/N})\big)$ равномерно; $j=m+2r\gamma_*\in\mathbb Q$ | [Доказано] |
| Л. N3 | при фиксированном $\theta$: критические точки в слое — не более $2r-1$ вещественных ветвей Пюизё, $F_{\rm fl}(\cdot,\theta)$ — сходящийся ряд Пюизё | [Доказано] по модулю теоремы Ньютона–Пюизё |
| Л. N4 | невырожденная ветвь: точное аналитическое дно, $F_*=s^\beta\hat G(s^{1/N},\theta)$; уточнение при $\hat G(0,\cdot)\equiv0$ (аналог леммы K2) | [Доказано] |
| Т. 2″ | теорема 2′ [008] с расщеплением $b=(b',b'')$: перекрёстные члены только по $b'$, профиль по $b''$ может быть вырожденным | [Доказано], зависит от [007], [008] |
| Т. N | аналог K2: (NF), $G(0)<0$, $G'(0)=0<G''(0)$, профиль $e^{2r'}\mathsf p$, $\mathsf p(0,0)>0$, любое $r'\ge1$ ⇒ асимптотическая траектория | [Доказано], зависит от [007], [008] |
| Сл. N′ | то же для аналитического $U$ по данным многоугольника Ньютона | [Доказано] |
| Сл. N″ | струйный критерий: для $U\in C^{K+1}$, $K+1>j$, достаточно условий на $j^KU$ | [Доказано] |
| M1 | $(z-x^2)^4+x^5+y^5+xy^6+yx^6$: $2r=4$, $j=5$, $c=\frac54$, $G=\cos^5\phi+\sin^5\phi$, профиль $e^4$ ($r'=2$), минимумы $G=-1$, $G''=5$ в $-e_x,-e_y$ ⇒ асимптотические траектории | [Доказано] |
| M2 | $z^4+z(x^4+x^3y+y^4)+x^6+xz^5+2yz^5$: $2r=4$, $j=\frac{16}3$, $c=\frac43$, $G=-3\cdot4^{-4/3}f^{4/3}$, профиль невырожден после сдвига на $\varepsilon_0=-(f/4)^{1/3}$ ($r'=1$), минимумы $G$ в $\phi_*\approx0.22005$ и $\frac\pi2$ (и $+\pi$) ⇒ асимптотические траектории | [Доказано] |

В M1 и в M2 при $\phi=\frac\pi2$ выполнено $G''+jG=0$ (точно), то есть декартова карта развёртки
(теорема K1) не работает уже во втором порядке; нужна поворачивающаяся карта.

## 1. Постановка и обозначения

**1.1. Дуга и трубка.** $n=3$. $\omega:\Lambda'\to S^2$ — аналитическая дуга с натуральным параметром
$\theta$ на открытом интервале $\Lambda'\ni0$, $\omega(0)=\omega^*$; $\ell=\omega'$, $n=\omega\times\ell$;
репер Дарбу
$$\omega'=\ell,\qquad \ell'=-\omega+k_gn,\qquad n'=-k_g\ell \tag{1.1}$$
($k_g$ — геодезическая кривизна, аналитична). По лемме K3 [008] найдутся $\theta_{K}>0$ и $t_1>0$ такие,
что $\Pi(s,\theta,\eta)=s\omega(\theta)+\eta n(\theta)$ — аналитический диффеоморфизм
$\mathcal P=\{s>0,\ |\theta|<\theta_K,\ |\eta|<t_1s\}$ на открытое подмножество $\mathbb R^3\setminus0$,
$|\Pi|^2=s^2+\eta^2$, $\nabla s=\omega(\theta)$. Для большого круга ($k_g=0$) это элементарно.

**1.2. Функция $\varphi$.** $U$ аналитична в шаре, $U=\sum_{k\ge m}u_k$, $m\ge2$. Положим
$$\varphi(s,\theta,y):=\sum_{k\ge m}s^{k-m}u_k\big(\omega(\theta)+y\,n(\theta)\big).$$
По [008], §1: $\varphi$ аналитична на $(-R_0/3,R_0/3)\times\Lambda'\times\{|y|<1\}$ и
$U\big(s(\omega+yn)\big)=s^m\varphi(s,\theta,y)$ при этих $(s,\theta,y)$. Коэффициенты
$\varphi_{il}(\theta):=\frac1{i!\,l!}\partial_s^i\partial_y^l\varphi(0,\theta,0)$ аналитичны на $\Lambda'$;
**носитель** $\mathcal S:=\{(i,l)\in\mathbb N_0^2:\ \varphi_{il}\not\equiv0\ \text{на}\ \Lambda'\}$ (по теореме
единственности «$\not\equiv0$ на $\Lambda'$» равносильно «$\not\equiv0$ на любом подинтервале»).

**1.3. Нормальная кратность.** Говорим, что дуга имеет **постоянную нормальную кратность $2r$**
($r\in\mathbb N$), если
$$u_m\big(\omega(\theta)+y\,n(\theta)\big)=y^{2r}a(\theta,y),\qquad a(\theta,0)>0\quad(\theta\in\Lambda'). \tag{M}$$
Тогда $\varphi_{0l}\equiv0$ при $l<2r$ и $\varphi_{0,2r}=a(\cdot,0)$. Случай $r=1$ — условие Морса–Ботта
(K2) [008] вдоль дуги; здесь интересен $r\ge2$ ($D^2u_m(\omega)(n,n)=0$). Условие (M) не зависит от
выбора поперечной координаты: если около конуса $u_m=\tau^{2r}g$, $g>0$, где $\tau$ — гладкая
функция с $\tau=0$ на конусе и $d\tau\ne0$, то $\tau(\omega+yn)=y\,\tau_1(\theta,y)$, $\tau_1(\theta,0)\ne0$
(на конусе $\langle\nabla\tau,n\rangle\ne0$, так как $\nabla\tau$ — нормаль к конусу), и
$a=\tau_1^{2r}g>0$ [Доказано, элементарно]. Глобальное условие $u_m\ge0$ в этой записке не
используется: нужна только (M) около дуги.

**1.4. Весовые начальные формы.** Для рационального $\gamma>0$ пусть $N$ — знаменатель $\gamma$
(так что $N\gamma\in\mathbb N$). Положим
$$\beta'(\gamma):=\min\{i+\gamma l:\ (i,l)\in\mathcal S\},\qquad
\Phi_0^{(\gamma)}(\theta,\varepsilon):=\sum_{(i,l)\in\mathcal S,\ i+\gamma l=\beta'(\gamma)}\varphi_{il}(\theta)\,\varepsilon^l$$
(минимум существует: значения $i+\gamma l$ лежат в $\frac1N\mathbb N_0$; сумма конечна). Это
многочлен по $\varepsilon$ с аналитическими по $\theta$ коэффициентами. Ниже предполагается
$\mathcal S\ne\varnothing$ (иначе $U\equiv0$ на конусе над дугой).

## 2. Аналог леммы K1: перемасштабирование, дно, $j$, $G$, нормальный профиль

### Лемма N1 (весовое перемасштабирование) — [Доказано]

Пусть $\Lambda\subset\Lambda'$ — компактный интервал, $\gamma>0$ рационально, $N$, $\beta'=\beta'(\gamma)$,
$\Phi_0=\Phi_0^{(\gamma)}$ — как в 1.4. Для каждого $E>0$ найдётся $\sigma_1\in(0,1)$ такое, что ряд
$$\tilde U(\sigma,\theta,\varepsilon):=\sum_{(i,l)\in\mathcal S}\varphi_{il}(\theta)\,\sigma^{Ni+N\gamma l-N\beta'}\,\varepsilon^l$$
сходится абсолютно и равномерно на $[-\sigma_1,\sigma_1]\times\Lambda\times[-E,E]$ и задаёт функцию,
вещественно-аналитическую в окрестности этого множества, причём $\tilde U(0,\theta,\varepsilon)=\Phi_0(\theta,\varepsilon)$
и при $0<s<\sigma_1^N$, $\theta\in\Lambda$, $|\varepsilon|\le E$
$$U\big(s\omega(\theta)+s^{1+\gamma}\varepsilon\,n(\theta)\big)=s^{m+\beta'}\,\tilde U\big(s^{1/N},\theta,\varepsilon\big). \tag{2.1}$$

*Доказательство.*

1. $\varphi$ вещественно-аналитична в окрестности компакта $\{0\}\times\Lambda\times\{0\}$, поэтому
   продолжается до голоморфной функции в его комплексной окрестности. По компактности найдутся
   $\rho_s,\rho_y\in(0,1)$, комплексная окрестность $V\supset\Lambda$ и $M>0$ такие, что продолжение
   голоморфно и по модулю не больше $M$ на $\{|s|\le2\rho_s\}\times\overline V\times\{|y|\le2\rho_y\}$. По
   оценкам Коши (по $(s,y)$ при фиксированном $\theta\in V$) $|\varphi_{il}(\theta)|\le M(2\rho_s)^{-i}(2\rho_y)^{-l}$ на
   $V$, и $\varphi(s,\theta,y)=\sum\varphi_{il}(\theta)s^iy^l$ при $|s|<2\rho_s$, $|y|<2\rho_y$.
2. Для $(i,l)\in\mathcal S$ показатель $k_{il}:=Ni+N\gamma l-N\beta'$ — целое $\ge0$ (определение $\beta'$). Возьмём
   $\sigma_1$ с $(2\sigma_1)^N\le\rho_s$ и $(2\sigma_1)^{N\gamma}\,2E\le\rho_y$. При $|\sigma|\le2\sigma_1$, $|\varepsilon|\le2E$, $\theta\in V$
   $$|\varphi_{il}(\theta)\sigma^{k_{il}}\varepsilon^l|\le M(2\rho_s)^{-i}(2\rho_y)^{-l}(2\sigma_1)^{Ni}\big((2\sigma_1)^{N\gamma}2E\big)^l(2\sigma_1)^{-N\beta'}\le M(2\sigma_1)^{-N\beta'}2^{-i-l},$$
   так что ряд сходится абсолютно и равномерно; его члены голоморфны, значит, сумма голоморфна на
   открытом множестве $\{|\sigma|<2\sigma_1\}\times V\times\{|\varepsilon|<2E\}$ (теорема Вейерштрасса), и её сужение
   вещественно-аналитично в окрестности $[-\sigma_1,\sigma_1]\times\Lambda\times[-E,E]$.
3. При $\sigma=0$ остаются члены с $k_{il}=0$, то есть $\tilde U(0,\cdot)=\Phi_0$.
4. При $0<\sigma<\sigma_1$ и $s=\sigma^N$: $\sigma^{N\beta'}\tilde U=\sum\varphi_{il}(\theta)s^i(s^\gamma\varepsilon)^l=\varphi(s,\theta,s^\gamma\varepsilon)$
   (перегруппировка абсолютно сходящегося ряда; $|s^\gamma\varepsilon|\le\rho_y$). По 1.2
   $U\big(s(\omega+s^\gamma\varepsilon n)\big)=s^m\varphi(s,\theta,s^\gamma\varepsilon)=s^{m+\beta'}\tilde U(\sigma,\theta,\varepsilon)$. $\square$

### Первое ребро, $j$, $c$, $G_{\min}$

Пусть выполнено (M) и есть $(i,l)\in\mathcal S$ с $l<2r$. Положим
$$\gamma_*:=\min\Big\{\frac i{2r-l}:\ (i,l)\in\mathcal S,\ l<2r\Big\},\qquad j:=m+2r\gamma_*,\qquad c:=1+\gamma_*,\qquad G_{\min}(\theta):=\min_{\varepsilon\in\mathbb R}\Phi_0^{(\gamma_*)}(\theta,\varepsilon).$$

**Утверждение** [Доказано]. $\gamma_*>0$ — наклон ребра многоугольника Ньютона носителя $\mathcal S$ в
плоскости $(i,l)$, примыкающего к вершине $(0,2r)$; $\beta'(\gamma_*)=2r\gamma_*$ и
$$\Phi_0^{(\gamma_*)}(\theta,\varepsilon)=a(\theta,0)\,\varepsilon^{2r}+\sum_{l<2r,\ (\gamma_*(2r-l),\,l)\in\mathcal S}\varphi_{\gamma_*(2r-l),\,l}(\theta)\,\varepsilon^l .$$
*Доказательство.* $(0,l)\notin\mathcal S$ при $l<2r$ по (M), поэтому в определении $\gamma_*$ все $i\ge1$ и
$\gamma_*>0$; минимум существует (дроби $\frac i{2r-l}$ с $l<2r$ образуют дискретное множество в
$\frac1{(2r)!}\mathbb N$). Для $(i,l)\in\mathcal S$: при $l<2r$ имеем $i\ge\gamma_*(2r-l)$, то есть $i+\gamma_*l\ge2r\gamma_*$ с
равенством только при $i=\gamma_*(2r-l)$; при $l\ge2r$ $i+\gamma_*l\ge2r\gamma_*$ с равенством только в точке
$(0,2r)\in\mathcal S$. $\square$

Так как старший коэффициент $a(\theta,0)>0$, минимум в определении $G_{\min}$ достигается, а $G_{\min}$
непрерывна. Если $(i,l)\in\mathcal S$ с $l<2r$ нет, то $\varphi=y^{2r}\cdot(\dots)$ и конус над дугой состоит из
критических точек $U$ (§6) — у изолированной критической точки $\gamma_*<\infty$.

Связь с 008: при $r=1$ и $g_{m+1}=u_{m+1}|_\Sigma\not\equiv0$ имеем $\gamma_*=\frac12$, $j=m+1$, $c=\frac32$,
$\Phi_0=\frac12h_n\varepsilon^2+g_{m+1}$; при $g_{m+1}\equiv0$ (и $(1,1)$ или $(2,0)\in\mathcal S$) первое ребро даёт $\gamma_*=1$, $j=m+2$ и
$G_{\min}=u_{m+2}|_\Sigma-\frac{b_1^2}{2h_n}=g_{m+2}$ — те же $j$, $G$, $c=\frac{j-m+2}2$, что в [008]. В общем случае
$c=1+\frac{j-m}{2r}$ [проверено вручную].

### Лемма N2 (функция дна) — [Доказано]

Пусть выполнено (M) на $\Lambda'$ и $\gamma_*<\infty$; $\Lambda\subset\Lambda'$ — компактный интервал. Найдутся
$y_2\in(0,1)$, $s_2>0$, $C>0$ такие, что при $0<y_1\le y_2$, $0<s<s_2$ (с $s_2$, зависящим от $y_1$) и
$\theta\in\Lambda$
$$\Big|\min_{|y|\le y_1}\varphi(s,\theta,y)-s^{2r\gamma_*}G_{\min}(\theta)\Big|\le C\,s^{2r\gamma_*+1/N},$$
то есть **функция дна** $F_{\rm fl}(s,\theta):=\min_{|\eta|\le y_1s}U\big(s\omega(\theta)+\eta n(\theta)\big)=s^m\min_{|y|\le y_1}\varphi$
удовлетворяет
$$F_{\rm fl}(s,\theta)=s^{j}\big(G_{\min}(\theta)+O(s^{1/N})\big)\quad\text{равномерно по }\theta\in\Lambda. \tag{2.2}$$
Кроме того, минимум достигается при $|y|\le E\,s^{\gamma_*}$ с некоторым $E$, не зависящим от $s,\theta$.
Поскольку $F_{\rm fl}$ определена через нормальный слой (он зависит только от точки $\omega(\theta)$), $j$ и
$G_{\min}$ — инварианты дуги, не зависящие от параметризации.

*Доказательство.*

1. *Разложение.* В области сходимости из доказательства леммы N1
   $\varphi=y^{2r}A(s,\theta,y)+\sum_{l=0}^{2r-1}y^lB_l(s,\theta)$, где $B_l=\sum_i\varphi_{il}s^i$ и
   $A=\sum_{l\ge2r}\sum_i\varphi_{il}s^iy^{l-2r}$ аналитичны, $A(0,\theta,0)=a(\theta,0)$. Пусть $a_{\min}=\min_\Lambda a(\cdot,0)>0$.
   Уменьшив $y_2,s_2\le1$, получим $A\ge a_{\min}/2$ при $|s|\le s_2$, $|y|\le y_2$, $\theta\in\Lambda$. В $B_l$ ($l<2r$)
   участвуют только $i\ge i_l:=\lceil\gamma_*(2r-l)\rceil$, поэтому $|B_l(s,\theta)|\le C_Bs^{i_l}\le C_Bs^{\gamma_*(2r-l)}$
   при $0\le s\le s_2$ (оценка из п. 1 леммы N1).
2. *Внешняя зона.* Пусть $E\ge1$ и $Es^{\gamma_*}\le|y|\le y_2$. Тогда $s^{\gamma_*}\le|y|/E$ и
   $|y^lB_l|\le C_B|y|^l(|y|/E)^{2r-l}\le C_BE^{-1}|y|^{2r}$, откуда
   $\varphi\ge(a_{\min}/2-2rC_B/E)|y|^{2r}\ge\frac{a_{\min}}4|y|^{2r}\ge\frac{a_{\min}}4E^{2r}s^{2r\gamma_*}$, если $E\ge8rC_B/a_{\min}$.
3. *Где лежат минимумы $\Phi_0$.* $\Phi_0(\theta,\varepsilon)-\Phi_0(\theta,0)\ge a_{\min}|\varepsilon|^{2r}-\sum_{1\le l<2r}C'|\varepsilon|^l>0$ при
   $|\varepsilon|\ge E_0$ (константа $C'$ — максимум модулей коэффициентов на $\Lambda$). Значит, $G_{\min}$
   достигается при $|\varepsilon|<E_0$, и $|G_{\min}|\le G_+$ на $\Lambda$ для некоторого $G_+$.
4. *Выбор $E$ и внутренняя зона.* Возьмём $E\ge\max\big(E_0,\ 8rC_B/a_{\min},\ (4(G_++1)/a_{\min})^{1/(2r)}\big)$ и
   применим лемму N1 с этим $E$: при $|y|\le Es^{\gamma_*}$, то есть $y=s^{\gamma_*}\varepsilon$, $|\varepsilon|\le E$,
   $\varphi=s^{2r\gamma_*}\tilde U(\sigma,\theta,\varepsilon)$, $\sigma=s^{1/N}$, и $|\tilde U-\Phi_0|\le C_E\sigma$ ($\tilde U$ класса $C^1$ на компакте).
   Поэтому минимум $\varphi$ по внутренней зоне лежит в $s^{2r\gamma_*}[G_{\min}-C_E\sigma,\ G_{\min}+C_E\sigma]$.
5. По п. 2 во внешней зоне $\varphi\ge(G_++1)s^{2r\gamma_*}\ge(G_{\min}+1)s^{2r\gamma_*}$. При $C_E\sigma<1$ и
   $Es^{\gamma_*}\le y_1$ минимум по $|y|\le y_1$ достигается во внутренней зоне и равен
   $s^{2r\gamma_*}(G_{\min}+O(\sigma))$. $\square$

### Лемма N3 (ветви критических точек в слое) — [Доказано] по модулю теоремы Ньютона–Пюизё

Пусть выполнено (M), $\gamma_*<\infty$, и $\theta\in\Lambda$ фиксировано. Тогда при малых $s>0$:

- **(a)** критические точки функции $y\mapsto\varphi(s,\theta,y)$ в $|y|<y_3$ — это значения не более чем
  $2r-1$ сходящихся рядов Пюизё $y=\psi_k(s)=\sum_{q\ge1}a_{kq}s^{q/d_k}$ с вещественными коэффициентами
  (вещественные ветви);
- **(b)** минимум $\varphi(s,\theta,\cdot)$ по $|y|\le y_1$ ($y_1\le\min(y_2,y_3)$) при всех малых $s>0$ достигается на
  одной и той же ветви $\psi_{k_0}$, $|\psi_{k_0}(s)|\le Es^{\gamma_*}$, и $F_{\rm fl}(s,\theta)=s^m\varphi(s,\theta,\psi_{k_0}(s))$ —
  сходящийся ряд Пюизё по $s$; его старший член — $s^jG_{\min}(\theta)$, если $G_{\min}(\theta)\ne0$ (лемма N2).

*Доказательство.* $f(s,y):=\partial_y\varphi(s,\theta,y)$ аналитична около $(0,0)$ и
$f(0,y)=y^{2r-1}\big(2ra(\theta,0)+O(y)\big)$ имеет порядок $2r-1$. По теореме Ньютона–Пюизё
[Литература: стандартная; не сверено] при $0<s<s_3$ нули $f(s,\cdot)$ в $|y|<y_3$ с кратностями — это
$2r-1$ значений сходящихся рядов Пюизё $\psi_k(s)$ (вообще говоря, с комплексными коэффициентами),
$\psi_k(0)=0$. При $s>0$ функция $\operatorname{Im}\psi_k(s)$ — сходящийся вещественный ряд Пюизё: либо $\equiv0$,
либо $\ne0$ при всех малых $s>0$; отсюда (a). (b): при $Es^{\gamma_*}\le y_1$ по п. 2 леммы N2
$\varphi(s,\theta,\pm y_1)\ge\frac{a_{\min}}4y_1^{2r}>0$, а $\varphi(s,\theta,0)=B_0(s,\theta)\to0$; значит, при малых $s$ минимум
достигается внутри и является критической точкой, то есть лежит на вещественной ветви. Разности
$\varphi(s,\theta,\psi_k(s))-\varphi(s,\theta,\psi_{k'}(s))$ — сходящиеся ряды Пюизё (подстановка $s=\tau^d$ даёт
аналитическую функцию $\tau$), каждая либо $\equiv0$, либо знакопостоянна при малых $s>0$; поэтому
номер минимальной ветви при малых $s$ один и тот же. Оценка $|\psi_{k_0}|\le Es^{\gamma_*}$ — из п. 5 леммы N2. $\square$

**Неравномерность по $\theta$.** Лемма N3 — утверждение при фиксированном $\theta$. Ветви $\psi_k$ зависят от
$\theta$ аналитически только вне дискриминантного множества (где ветви сливаются или меняется
многоугольник Ньютона функции $f$). Равномерную картину даёт лемма N4 (невырожденная ветвь) или
гипотеза (E) теоремы N (вырожденная ветвь постоянной кратности).

### Лемма N4 (невырожденная ветвь: точное дно и уточнение) — [Доказано]

Пусть $\gamma>0$ рационально, $\Phi_0=\Phi_0^{(\gamma)}$, $\tilde U$ — из леммы N1, $\beta=m+\beta'(\gamma)$, $c=1+\gamma$,
$\Lambda_1$ — компактный интервал, $\varepsilon_0:\Lambda_1\to\mathbb R$ аналитична (на окрестности $\Lambda_1$),
$\partial_\varepsilon\Phi_0(\theta,\varepsilon_0(\theta))=0$ и $\partial_\varepsilon^2\Phi_0(\theta,\varepsilon_0(\theta))>0$. Тогда:

- **(a)** есть $\sigma_2,e_2>0$ и аналитическая $\varepsilon^*(\sigma,\theta)$ на $(-\sigma_2,\sigma_2)\times\Lambda_1$ с $\varepsilon^*(0,\theta)=\varepsilon_0(\theta)$
  такие, что $\varepsilon^*$ — единственная критическая точка $\tilde U(\sigma,\theta,\cdot)$ в $|\varepsilon-\varepsilon_0(\theta)|<e_2$ и там
  строгий минимум;
- **(b)** $\eta^*(s,\theta):=s^c\varepsilon^*(s^{1/N},\theta)$ — критическая точка (локальный минимум) функции
  $\eta\mapsto U(s\omega(\theta)+\eta n(\theta))$, и
  $$F_*(s,\theta):=U\big(s\omega+\eta^*n\big)=s^\beta\,\hat G(s^{1/N},\theta),\qquad\hat G(\sigma,\theta):=\tilde U(\sigma,\theta,\varepsilon^*(\sigma,\theta)),\qquad\hat G(0,\theta)=\Phi_0(\theta,\varepsilon_0(\theta)),$$
  $\hat G$ аналитична: значение на дне — сходящийся ряд Пюизё по $s$ с аналитическими по $\theta$
  коэффициентами;
- **(c)** (уточнение) если $\hat G\not\equiv0$, пусть $k:=\min\{i:\ \partial_\sigma^i\hat G(0,\cdot)\not\equiv0\ \text{на}\ \Lambda_1\}$ и
  $\hat G=\sigma^k\hat G^{(k)}$ (формула Тейлора с интегральным остатком; $\hat G^{(k)}$ аналитична,
  $\hat G^{(k)}(0,\theta)=G_k(\theta):=\frac1{k!}\partial_\sigma^k\hat G(0,\theta)$). Положим $M(\sigma,\theta,e):=\int_0^1(1-t)\,\partial_\varepsilon^2\tilde U(\sigma,\theta,\varepsilon^*+te)\,dt$,
  $\tau:=s^{1/(2N)}$, $c':=c+\frac k{2N}$, $\beta'':=\beta+\frac kN$. Тогда при малых $s>0$, $|e|\le1$
  $$U\big(s\omega+(\eta^*+s^{c'}e)\,n\big)=s^{\beta''}\Big[\hat G^{(k)}(\tau^2,\theta)+e^2M(\tau^2,\theta,\tau^ke)\Big],$$
  и квадратная скобка при $\tau=0$ равна $G_k(\theta)+\frac12\partial_\varepsilon^2\Phi_0(\theta,\varepsilon_0(\theta))\,e^2$ при $k\ge1$ и
  $\Phi_0(\theta,\varepsilon_0(\theta)+e)=G_0(\theta)+e^2M(0,\theta,e)$ при $k=0$ — нормальная форма (NF) теоремы N с $N'=2N$, $c'$,
  $\beta''$, $y_0=\tau^{2N\gamma}\varepsilon^*(\tau^2,\theta)$, $G=G_k$, $r'=1$, $\mathsf p=M(0,\theta,0)$ (при $k=0$ — $\mathsf p=M(0,\theta,e)$);
- **(d)** если $\hat G\equiv0$, то $\nabla U=0$ на поверхности $\{s\omega(\theta)+\eta^*(s,\theta)n(\theta)\}$, примыкающей к $0$:
  критическая точка $0$ неизолирована.

*Доказательство.* (a) На компакте $\{|\sigma|\le\sigma_2,\ \theta\in\Lambda_1,\ |\varepsilon-\varepsilon_0(\theta)|\le e_2\}$ при малых $\sigma_2,e_2$
по непрерывности $\partial_\varepsilon^2\tilde U\ge c_0>0$ и $\pm\partial_\varepsilon\tilde U(\sigma,\theta,\varepsilon_0\pm e_2)>0$; строгая выпуклость даёт
единственную критическую точку (минимум), аналитическая теорема о неявной функции — её
аналитичность (как в лемме K1 [008]). (b) Дифференцируя (2.1) по $\varepsilon$:
$s^c\partial_\eta U(s\omega+s^c\varepsilon n)=s^\beta\partial_\varepsilon\tilde U$, это $0$ при $\varepsilon=\varepsilon^*$. Остальное — (2.1).
(c) Формула Тейлора по $\varepsilon$ в точке $\varepsilon^*$ ($\partial_\varepsilon\tilde U=0$):
$\tilde U(\sigma,\theta,\varepsilon^*+e_1)=\hat G+e_1^2M(\sigma,\theta,e_1)$. Подставим $e_1=\tau^ke$, $\sigma=\tau^2$:
$s^\beta\tilde U=s^\beta\tau^{2k}[\hat G^{(k)}(\tau^2,\theta)+e^2M(\tau^2,\theta,\tau^ke)]$, $s^\beta\tau^{2k}=s^{\beta''}$, а $s^c\tau^ke=s^{c'}e$.
При $\tau=0$: $M(0,\theta,0)=\frac12\partial_\varepsilon^2\Phi_0(\theta,\varepsilon_0)$. Наконец, $\eta^*=s\cdot s^\gamma\varepsilon^*=s\cdot\tau^{2N\gamma}\varepsilon^*(\tau^2,\theta)$.
(d) Если $U(s\omega+\eta^*n)\equiv0$, то по (b) $\langle\nabla U,n\rangle=0$ на поверхности, а дифференцирование
тождества по $s$ и $\theta$ (с (1.1)) даёт $\langle\nabla U,\omega+\eta^*_sn\rangle=0$,
$\langle\nabla U,(s-k_g\eta^*)\ell+\eta^*_\theta n\rangle=0$, откуда $\langle\nabla U,\omega\rangle=\langle\nabla U,\ell\rangle=0$ (при малых $s$
$s-k_g\eta^*\ne0$). Точки поверхности ненулевые и стремятся к $0$. $\square$

Лемма N4(c) — аналог леммы K2 [008]: при невырожденном нормальном профиле итерации
«сдвинуть на точное дно и перемасштабировать» сводят всё к случаю $G\not\equiv0$; по (d) у изолированной
точки процесс останавливается.

### Определения: нормальный профиль и эффективный потенциал

Пусть выбраны рациональное $\gamma>0$ (обычно $\gamma=\gamma_*$) и **ветвь** $\varepsilon_0\in C^2$ критических точек
$\Phi_0^{(\gamma)}(\theta,\cdot)$ **постоянной кратности** $2r'-1$:
$$\partial_\varepsilon^k\Phi_0^{(\gamma)}(\theta,\varepsilon_0(\theta))=0\ (1\le k<2r'),\qquad \partial_\varepsilon^{2r'}\Phi_0^{(\gamma)}(\theta,\varepsilon_0(\theta))>0. \tag{E}$$
**Эффективный потенциал** $G(\theta):=\Phi_0^{(\gamma)}(\theta,\varepsilon_0(\theta))$; **нормальный профиль**
$$P(\theta,e):=\Phi_0^{(\gamma)}(\theta,\varepsilon_0(\theta)+e)-G(\theta)=e^{2r'}\mathsf p(\theta,e),\qquad \mathsf p(\theta,e)=\sum_{k\ge2r'}\frac{\partial_\varepsilon^k\Phi_0(\theta,\varepsilon_0)}{k!}e^{k-2r'},\quad\mathsf p(\theta,0)>0.$$
Профиль **невырожден**, если $r'=1$ (тогда достаточно невырожденного локального минимума
$\varepsilon_0(0)$ функции $\Phi_0(0,\cdot)$: ветвь существует и аналитична по теореме о неявной функции), и
**вырожден**, если $r'\ge2$. Если $\varepsilon_0(\theta)$ — точка глобального минимума $\Phi_0(\theta,\cdot)$, то $G=G_{\min}$.
Примеры: у M1 $\gamma_*=\frac14$, $\Phi_0=\varepsilon^4+G(\phi)$, $\varepsilon_0=0$, $r'=r=2$ (вырожденный профиль $e^4$); у M2
$\gamma_*=\frac13$, $\Phi_0=\varepsilon^4+f(\phi)\varepsilon$, минимум $\varepsilon^4+s f\,y$ (в переменной $y$) сдвинут в $y^*\sim s^{1/3}\varepsilon_0$, и после
сдвига профиль невырожден, $r'=1$ (§5).

## 3. Теорема 2″: расщепление поперечных переменных

### Класс (GT3″)

Данные — как у класса (GT3′) [008]: $U\in C^2(B_r)$, $U(0)=0$, $\nabla U(0)=0$, $\beta>0$, веса
$c=(c_1,\dots,c_{n-1})\in(0,\infty)^{n-1}$, $N\in\mathbb N$, $s_0\in(0,1]$, $r_0>0$, $b=(u_ix^{-c_i})_i$,
$\mathcal N=\{0<x<s_0,\ |b|<r_0\}$, карта $\Phi\in C^2(\mathcal N;\mathbb R^n)$, $Y=(\partial_x\Phi)\circ\Phi^{-1}$, $\rho=x\circ\Phi^{-1}$, $h=|Y|^2$,
$\varsigma=x^{1/N}$. Дополнительно задано разбиение индексов $\{1,\dots,n-1\}=I'\sqcup I''$, $b'=(b_i)_{i\in I'}$,
$b''=(b_i)_{i\in I''}$ (оба множества непусты; при $I''=\varnothing$ всё ниже совпадает с (GT3′) [008]).
$U$ **принадлежит классу (GT3″)**, если выполнены $(\Phi0)$, $(\Phi1')$, (F) из [008] и

- **$(\Phi2'')$** для $(x,u)\in\mathcal N$ и $w\perp\partial_x\Phi(x,u)$:
  $|\langle\nabla\rho-Y/h,w\rangle|\le(\gamma_1|b'|+\varpi(x))|w|$ и
  $x|\langle\partial_x^2\Phi,w\rangle|\le(\gamma_2|b'|+C_1|b'|^2+\varpi(x))|w|$;
- **$(\Phi3'')$** $x\langle w,D_wY\rangle\ge-(C_1|b'|+\varpi(x))|w|^2$ для $w\perp\partial_x\Phi$;
- **$(V'')$** $F_0(0)<0$; есть $\lambda_0>0$, $\mu\in(0,\beta]$, $r_1\in(0,r_0)$ и непрерывная $q_0:[0,r_1)\to[0,\infty)$ с
  $q_0(t)>0$ при $t>0$ такие, что при $|b|<r_1$
  $$Q(b)\ge\lambda_0|b'|^2+q_0(|b''|),\qquad \sum_ic_ib_i\partial_{b_i}Q(b)\ge\mu\,Q(b),$$
  и выполнено (U2) [008]: $\Gamma_*^2\le\beta\mu$, $\Gamma_*=\sqrt{a_0/\lambda_0}\,\big[\frac{3\sqrt3}2\beta\gamma_1+2\sqrt2\gamma_2\big]$, $a_0=-F_0(0)$.

Здесь $\gamma_1,\gamma_2,C_1\ge0$, $\varpi(x)\to0$ при $x\to0$; $Q=F_0-F_0(0)$, $F_0=F(0,\cdot)$.

Отличие от (GT3′): в $(\Phi2'')$, $(\Phi3'')$ стоит $|b'|$ вместо $|b|$, а квадратичная нижняя оценка $Q$
требуется только по $b'$; по $b''$ — лишь коэрцитивность $q_0$.

### Теорема 2″ — [Доказано; зависит от [007] и леммы 2′ [008]]

Если $U$ принадлежит классу (GT3″), то есть $\delta_*>0$ такое, что для каждого $\delta\in(0,\delta_*]$ есть
асимптотическая траектория $q(t)=\Phi(x(t),u(t))$, $x(t)\downarrow0$, $-k_2x^{\beta/2}\le\dot x\le-k_1x^{\beta/2}$
($0<k_1\le k_2$), причём $b(t)\in\overline{\Omega_\delta}$ при всех $t\ge0$, где $\Omega_\delta$ — компонента связности множества
$\{b\in B_{r_1}:\ Q(b)<2\delta\}$, содержащая $0$; в частности $|b'(t)|\le\sqrt{2\delta/\lambda_0}$ и $q_0(|b''(t)|)\le2\delta$.
Равновесие неустойчиво по Ляпунову; $\beta\ge2$.

### Доказательство

Повторяем доказательство теоремы 2′ [008] (§9 там; оно, в свою очередь, повторяет доказательство
теоремы 2 [007], §4), меняя шаг 2 (построение $\Omega_b'$) и константы шагов 4–5.

*Шаг 1* — дословно шаг 1 [008], §9: $\mathcal O=\Phi(\mathcal N)$, $\rho\in C^2$, $Y\in C^1$, $Y\rho=1$, $A(r)=a_0r^\beta$,
$W\circ\Phi=x^\beta(F-F_0(0))$ и $\beta W-\rho\,YW=x^\beta\big[\sum_ic_ib_i\partial_{b_i}F-\frac\varsigma N\partial_\varsigma F\big]$ (формулы (4.1),
(4.2) [007]). Используются только $(\Phi0)$, $Y\circ\Phi=\partial_x\Phi$, $b_i=u_ix^{-c_i}$ и (F).

*Шаг 2 (новый): множество $\Omega_\delta$.* Положим
$$\delta_1:=\min\Big(\frac{\lambda_0r_1^2}{32},\ \frac{q_0(r_1/4)}2\Big)>0$$
и пусть $0<\delta\le\delta_1$, $\Omega_\delta$ — как в формулировке ($0\in\Omega_\delta$, так как $Q(0)=0$).

- (2a) *$\overline{\Omega_\delta}\subset\{|b'|\le r_1/4,\ |b''|\le r_1/4\}\subset\overline{B_{r_1/2}}\subset B_{r_1}$.* На $\Omega_\delta$
  $\lambda_0|b'|^2\le Q<2\delta\le\lambda_0r_1^2/16$, то есть $|b'|<r_1/4$. Далее, $\Omega_\delta$ открыто и связно, значит, линейно
  связно, и образ $\Omega_\delta$ при непрерывном отображении $b\mapsto|b''|$ — промежуток, содержащий $0$.
  Если бы в $\Omega_\delta$ была точка с $|b''|\ge r_1/4$, нашлась бы точка с $|b''|=r_1/4$, где
  $Q\ge q_0(r_1/4)\ge2\delta$, — противоречие. Итак, $|b''|<r_1/4$ на $\Omega_\delta$ и $|b|<r_1/(2\sqrt2)$; замыкание —
  в $\{|b|\le r_1/(2\sqrt2)\}$.
- (2b) *$Q=2\delta$ на $\partial\Omega_\delta$.* Пусть $b_0\in\partial\Omega_\delta$; по (2a) $b_0\in B_{r_1}$ и по непрерывности $Q(b_0)\le2\delta$.
  Если $Q(b_0)<2\delta$, то шар вокруг $b_0$ лежит в $\{b\in B_{r_1}:Q<2\delta\}$, связен и пересекает $\Omega_\delta$,
  поэтому лежит в $\Omega_\delta$, и $b_0\in\Omega_\delta$ — невозможно для граничной точки открытого множества.
- Свойства шага 2 [007]/[008] с $\Omega_b':=\Omega_\delta$: (i) $Q\ge0$ на $\Omega_\delta$ (из $(V'')$); (ii) $Q=2\delta=\delta+\kappa'$ на
  $\partial\Omega_\delta$, $\kappa':=\delta$; (iii) $\sum c_ib_i\partial_{b_i}Q\ge\mu Q$ на $\overline{\Omega_\delta}\subset B_{r_1}$; (iv) $R_b:=\sup_{\Omega_\delta}|b|\le r_1/2$.
  Дополнительно (v) $R':=\sup_{\Omega_\delta}|b'|\le\sqrt{2\delta/\lambda_0}$ и (vi) $|b'|\le\sqrt{Q(b)/\lambda_0}$ на $\overline{\Omega_\delta}$.

*Шаг 3* — дословно шаг 3 [007] (и [008], §9, шаг 3): $\chi(\varsigma)$, $\bar\chi$, порог $\sigma_*<s_0$ по $x$ с
$\bar\chi(\sigma_*^{1/N})<\min(\delta,\kappa'/2)=\delta/2$,
$\mathcal D=\{x<\sigma_*,\ b\in\Omega_\delta,\ F-F_0(0)<\delta\}$, $D=\Phi(\mathcal D)$. Проверка (D1)–(D3) там использует только
$(\Phi0)$, (F), открытость $\Omega_\delta$, $0\in\Omega_\delta$, $\overline{\Omega_\delta}\subset B_{r_0}$ и свойство (ii). Ниже $\chi:=\bar\chi(\sigma_*^{1/N})$,
$\bar\varpi:=\sup_{x<\sigma_*}\varpi(x)$; $\sigma_*$ ещё уменьшится.

*Шаг 4 (константы леммы 2′ [008] на $D_{\sigma_*}$).* Каждая точка $D_{\sigma_*}$ — это $\Phi(x,u)$ с $x<\sigma_*$,
$b\in\overline{\Omega_\delta}$, $F-F_0(0)\le\delta$ (рассуждение из (D2) [007]).

- (L0): $a_1=a_3=a_0$, $a_2=\beta a_0$, $\delta\le a_0/2$. (L1): $h_0=\frac12$, $h_1=\frac32$ по $(\Phi1')$.
- (L2′): $\mathcal Q:=x^\beta Q(b)\ge0$; $|W-\mathcal Q|=x^\beta|F(\varsigma,b)-F_0(b)|\le\chi x^\beta$, то есть $\varepsilon_0=\chi/\delta$; по (4.2) [007],
  неравенству Коши–Буняковского $|\sum_ic_ib_i(\partial_{b_i}F-\partial_{b_i}Q)|\le c_{\max}R_b\chi$ и (iii):
  $\beta W-\rho\,YW\ge x^\beta[\mu Q-c_{\max}R_b\chi-\chi/N]$, то есть $\varepsilon_1=(c_{\max}R_b+1/N)\chi/\delta$.
- (L3′): по (vi) $|b'|\le\sqrt{\mathcal Q/(\lambda_0\rho^\beta)}$ ($\rho=x$). По $(\Phi2'')$: $\theta_1=\bar\varpi$, $\gamma_1'=\gamma_1/\sqrt{\lambda_0}$. Так как
  $\nabla_YY=\partial_x^2\Phi$ (поток $Y$ в карте — сдвиг по $x$), по $(\Phi2'')$ и (v): $\theta_2=C_1R'^2+\bar\varpi\le2C_1\delta/\lambda_0+\bar\varpi$,
  $\gamma_2'=\gamma_2/\sqrt{\lambda_0}$. По $(\Phi3'')$ и (v): $\theta_3=C_1R'+\bar\varpi\le C_1\sqrt{2\delta/\lambda_0}+\bar\varpi$. Все $\ge0$.
- $\Gamma'\le\Gamma_*$: при $\delta\le a_0/2$ $a_2+\beta\delta\le\frac32\beta a_0$, и $\Gamma'$ из леммы 2′ не больше $\Gamma_*$ (выкладка [008],
  §9, шаг 4); по (U2) $\Gamma'^2\le\beta\mu$.

*Шаг 5 (выбор $\delta$ и $\sigma_*$).* $L_1=3\beta\sqrt{3a_0/2}$, $L_2=4\sqrt{a_0}$. Члены (8.1) [008], зависящие только от $\delta$:
$$\frac{L_2\cdot2C_1\delta/\lambda_0}{\sqrt\delta}+4C_1\sqrt{\frac{2\delta}{\lambda_0}}=C_1\sqrt\delta\Big(\frac{8\sqrt{a_0}}{\lambda_0}+\frac{4\sqrt2}{\sqrt{\lambda_0}}\Big)$$
и (для п. 1 леммы 2′) $8\gamma_1'\delta$. Пусть $\delta_*\le\min(a_0/2,\delta_1)$ таково, что при $\delta\le\delta_*$ первое $\le\mu/8$, а
$8\gamma_1'\delta\le\frac12\sqrt{a_0/h_1}$. Для данного $\delta\in(0,\delta_*]$ выберем $\sigma_*$ так, чтобы $\varepsilon_0\le\frac14$, $\varepsilon_1\le\frac\mu{16}$,
$\frac{(L_1+L_2)\bar\varpi}{\sqrt\delta}+4\bar\varpi\le\frac\mu{16}$ и $4\sqrt\delta\,\bar\varpi\le\frac12\sqrt{a_0/h_1}$ (все эти величины стремятся к $0$ при
$\sigma_*\to0$ и фиксированном $\delta$). Тогда условие п. 1 леммы 2′ выполнено
($4\sqrt\delta(\theta_1+2\gamma_1'\sqrt\delta)\le\sqrt{a_0/h_1}$), $\varepsilon_0\le\frac12$, и скобка в (8.1) [008] не меньше
$\frac\mu2\cdot\frac34-\frac\mu{16}-\frac\mu8-\frac\mu{16}=\frac\mu8>0$.

*Шаг 6.* Лемма 2′ [008] даёт (D4), (A4), (A5); теорема A [007] — решение $(q(t),v(t))\in\overline\Omega$, $q(t)\ne0$,
$q(t)\to0$, $v(t)\to0$, и неустойчивость (шаг 6 теоремы A). Как в шаге 6 [007], п. 3: $q(t)\in D_{\sigma_*}$,
$q=\Phi(x,u)$, $x=\rho(q)$, и п. 1 леммы 2′ даёт $-k_2x^{\beta/2}\le\dot x\le-k_1x^{\beta/2}$ с $k_1=\frac12\sqrt{a_0/h_1}$,
$k_2=\sqrt{2(a_0+\delta/2)/h_0}+k_1$; $b(t)\in\overline{\Omega_\delta}$ (как в п. 4 [007]). $\beta\ge2$ — как п. 1 шага 6 [007]: там
используются только $(\Phi0)$, $|\partial_x\Phi|=\sqrt h\le\sqrt{3/2}$ и $U\in C^2$. $\square$

**Замечание 3.1.** Препятствие R3 из [007] (замечание 7: при $C_1>0$ и $Q\sim|b|^4$ член $\theta_2/\sqrt\delta$ не мал)
обходится не за счёт улучшения оценок, а за счёт структуры карты: кривизна $C_1$ и перекрёстные члены
действуют только по $b'$, где профиль квадратичен. Для вырожденного профиля **по $b'$** (вырожденный
минимум $G$) препятствие остаётся (§7).

## 4. Теорема N (аналог теоремы K2 при нормальной кратности $2r\ge4$)

### 4.1. Данные и формулировка

**(NF) — нормальная форма оврага над дугой.** Дуга $\omega$, репер (1.1), $\theta_K$, $t_1$ — как в 1.1. Заданы
$N\in\mathbb N$, $c>1$, $\beta>0$, $\theta_1\in(0,\theta_K)$, $\sigma_1>0$, $e_1>0$ и функции

- $y_0\in C^2\big([0,\sigma_1]\times[-\theta_1,\theta_1]\big)$ (односторонние производные при $\sigma=0$), $y_0(0,\theta)=0$;
- $\tilde F:[0,\sigma_1]\times[-\theta_1,\theta_1]\times[-e_1,e_1]\to\mathbb R$, непрерывная вместе с $\partial_\theta\tilde F$, $\partial_e\tilde F$, причём
  $\sup_{\theta,e}|\sigma\partial_\sigma\tilde F(\sigma,\theta,e)|\to0$ при $\sigma\to0$,

такие, что при $0<s\le\sigma_1^N$, $|\theta|\le\theta_1$, $|e|\le e_1$
$$U\Big(s\,\omega(\theta)+\big(s\,y_0(s^{1/N},\theta)+s^c e\big)\,n(\theta)\Big)=s^\beta\,\tilde F\big(s^{1/N},\theta,e\big). \tag{NF}$$
Обозначим $\eta_0(s,\theta):=s\,y_0(s^{1/N},\theta)$ (**приближённое дно**).

**(G) — эффективный потенциал и профиль.** $\tilde F(0,\theta,e)=G(\theta)+e^{2r'}\mathsf p(\theta,e)$, где $r'\in\mathbb N$, $G\in C^2$,
$\mathsf p\in C^1$ около $(0,0)$, $\mathsf p_0:=\mathsf p(0,0)>0$, и
$$G(0)<0,\qquad G'(0)=0,\qquad G''(0)>0 .$$

**Теорема N** [Доказано; зависит от [007], от леммы 2′ и леммы K3 [008]]. Пусть $U\in C^2(B_r)$,
$U(0)=0$, $\nabla U(0)=0$, выполнены (NF) и (G). Положим $a_0=-G(0)$, $\lambda_0=G''(0)/4$ и выберем
$$0<\kappa\le\min\Big(\frac12,\ \frac{\beta\lambda_0}{a_0\big(\frac{15\sqrt3}8\beta+2\sqrt2\big)^2}\Big). \tag{4.0}$$
Тогда $U$ принадлежит классу (GT3″) с картой (4.1) ниже, весами $(\kappa,c)$, $b=(\theta,e)$, $b'=\theta$, $b''=e$,
показателями $\beta$, $N$, $\mu=\kappa$, $\gamma_1=\frac54\kappa$, $\gamma_2=\kappa(1-\kappa)$, $C_1=\frac54\kappa^2(1+\bar k_g)+4\kappa\bar k_g$,
$q_0(t)=\frac{\mathsf p_0}2t^{2r'}$. Следовательно, есть $\delta_*>0$ такое, что для каждого $\delta\in(0,\delta_*]$ существует
асимптотическая траектория
$$q(t)=s(t)\,\omega(\theta(t))+\big(\eta_0(s(t),\theta(t))+s(t)^c e(t)\big)\,n(\theta(t)),\qquad s(t)\downarrow0,\quad-k_2s^{\beta/2}\le\dot s\le-k_1s^{\beta/2},$$
$$|\theta(t)|\le\sqrt{2\delta/\lambda_0},\qquad \mathsf p_0\,|e(t)|^{2r'}\le4\delta ,$$
и равновесие неустойчиво по Ляпунову. При $\beta>2$ $s(t)\asymp t^{-2/(\beta-2)}$. Траектория касается конуса
над дугой ($\operatorname{dist}(q,\mathbb R_+\omega(\theta))\le|\eta_0|+s^c|e|=o(|q|)$) и лежит в конусе раствора $O(\sqrt\delta)$ вокруг
луча $\mathbb R_+\omega^*$.

Ни аналитичность $U$, ни изолированность критической точки здесь не предполагаются; ни $r$
(нормальная кратность $u_m$), ни сама $u_m$ в формулировке не участвуют — всё в (NF), (G).

### 4.2. Карта и формулы

Пусть $0<\kappa\le\frac12$. Карта
$$\Phi(x,u,\zeta):=\Psi(x,\theta,\zeta),\quad\theta:=u\,x^{-\kappa};\qquad\Psi(s,\theta,\zeta):=s\,\omega(\theta)+\big(\eta_0(s,\theta)+\zeta\big)\,n(\theta);\qquad b=(\theta,e)=(ux^{-\kappa},\ \zeta x^{-c}). \tag{4.1}$$
Обозначим $\eta=\eta_0+\zeta$, $\epsilon:=k_g(\theta)\eta/s$, $\nu:=\eta_{0,s}-\kappa\theta\,\eta_{0,\theta}/s$ (в точках карты $s=x$). Из (1.1)
[все формулы ниже — Доказано прямым дифференцированием; [Эксперимент] `frames_nm.py`: проверены
символьно для $\eta_0=s\,y_0(s^{1/3},\theta)$ с общим многочленом $y_0$ и общим $k_g(\theta)$]:
$$\Psi_s=\omega+\eta_{0,s}n,\qquad\Psi_\theta=s(1-\epsilon)\ell+\eta_{0,\theta}n,\qquad\Psi_\zeta=n; \tag{4.2}$$
$$Y=\partial_x\Phi=\Psi_s-\frac{\kappa\theta}x\Psi_\theta=\omega-\kappa\theta(1-\epsilon)\ell+\nu n,\qquad h=1+\kappa^2\theta^2(1-\epsilon)^2+\nu^2; \tag{4.3}$$
$$x\,\partial_x^2\Phi=-\kappa\theta\big[(1-\kappa)+\kappa\epsilon-x\partial_x\epsilon-\nu k_g\big]\ell+\kappa^2\theta^2(1-\epsilon)(-\omega+k_gn)+x\partial_x\nu\,n, \tag{4.4}$$
где $x\partial_x=s\partial_s-\kappa\theta\partial_\theta$ — производная при постоянных $(u,\zeta)$, и $x\partial_x\epsilon=-\kappa\theta k_g'\eta/x+k_g\nu-\epsilon$.
(Вывод (4.4): $\frac{d\theta}{dx}=-\frac{\kappa\theta}x$, $\frac{d\omega}{dx}=-\frac{\kappa\theta}x\ell$, $\frac{d\ell}{dx}=-\frac{\kappa\theta}x(-\omega+k_gn)$, $\frac{dn}{dx}=\frac{\kappa\theta}xk_g\ell$, а
$\frac{d\eta}{dx}=\nu$; подставить в производную (4.3).) Как поле в координатах $(s,\theta,\zeta)$ карты $\Psi$
$Y=\omega-\kappa\theta(1-\epsilon)\ell+\nu n$ с $\epsilon=k_g(\eta_0+\zeta)/s$, $\nu=\eta_{0,s}-\kappa\theta\eta_{0,\theta}/s$, и
$$\partial_\theta Y=\kappa\theta(1-\epsilon)\omega+\big[1-\kappa(1-\epsilon)+\kappa\theta\partial_\theta\epsilon-\nu k_g\big]\ell+\big[-\kappa\theta(1-\epsilon)k_g+\partial_\theta\nu\big]n,\quad
\partial_sY=\kappa\theta\partial_s\epsilon\,\ell+\partial_s\nu\,n,\quad\partial_\zeta Y=\frac{\kappa\theta k_g}s\ell, \tag{4.5}$$
$s\partial_s\epsilon=k_g\eta_{0,s}-\epsilon$. Для $w=w_\omega\omega+w_\ell\ell+w_nn$: $w=a^s\Psi_s+a^\theta\Psi_\theta+a^\zeta\Psi_\zeta$ с $a^s=w_\omega$,
$a^\theta=\frac{w_\ell}{s(1-\epsilon)}$, $a^\zeta=w_n-w_\omega\eta_{0,s}-\frac{w_\ell\eta_{0,\theta}}{s(1-\epsilon)}$, и $D_wY=a^s\partial_sY+a^\theta\partial_\theta Y+a^\zeta\partial_\zeta Y$, откуда
$$x\langle w,D_wY\rangle=w_\ell^2\Big(\frac1{1-\epsilon}-\kappa\Big)+\mathcal E_r, \tag{4.6}$$
$$\mathcal E_r=\frac{w_\ell}{1-\epsilon}\Big[(\kappa\theta\partial_\theta\epsilon-\nu k_g)w_\ell+\big(-\kappa\theta(1-\epsilon)k_g+\partial_\theta\nu\big)w_n\Big]+\kappa\theta\,w_\ell w_\omega+w_\omega\big[\kappa\theta\,s\partial_s\epsilon\,w_\ell+s\partial_s\nu\,w_n\big]+a^\zeta\kappa\theta k_gw_\ell .$$
Если $w\perp Y$, то из (4.3) $w_\omega=\kappa\theta(1-\epsilon)w_\ell-\nu w_n$. Формулы (4.2)–(4.5) совпадают с (6.4), (10.2)–(10.4) [008]
(там $\eta^*$ аналитично по $s$; здесь $\eta_0$ — функция от $s^{1/N}$, но формулы — тождества для любого
$\eta_0\in C^2$ при $s>0$).

### 4.3. Малые величины

**Лемма N5** [Доказано]. Пусть $r_0\le\min(\theta_1/2,e_1,\frac14)$. На множестве
$\{0<s<\sigma_1^N,\ |\theta|\le r_0,\ |\zeta|\le r_0s^c\}$ величины
$$\frac{\eta}s,\ \epsilon,\ \nu,\ \eta_{0,s},\ \frac{\eta_{0,\theta}}s,\ \partial_\theta\epsilon,\ s\partial_s\epsilon,\ \partial_\theta\nu,\ s\partial_s\nu,\ x\partial_x\epsilon,\ x\partial_x\nu$$
стремятся к $0$ при $s\to0$ равномерно по $(\theta,\zeta)$.

*Доказательство.* С $\sigma=s^{1/N}$, $\frac d{ds}=\frac\sigma{Ns}\frac d{d\sigma}$:
$$\frac{\eta_0}s=y_0,\quad\eta_{0,s}=y_0+\tfrac\sigma Ny_{0,\sigma},\quad\frac{\eta_{0,\theta}}s=y_{0,\theta},\quad s\eta_{0,ss}=\tfrac\sigma N\big[(1+\tfrac1N)y_{0,\sigma}+\tfrac\sigma Ny_{0,\sigma\sigma}\big],\quad\eta_{0,s\theta}=y_{0,\theta}+\tfrac\sigma Ny_{0,\sigma\theta},\quad\frac{\eta_{0,\theta\theta}}s=y_{0,\theta\theta}.$$
Так как $y_0\in C^2$ на компакте и $y_0(0,\cdot)\equiv0$ (значит, $y_{0,\theta}(0,\cdot)=y_{0,\theta\theta}(0,\cdot)=0$), все шесть величин
стремятся к $0$ при $\sigma\to0$ равномерно по $\theta$. Далее $|\zeta|/s\le r_0s^{c-1}\to0$ ($c>1$). Отсюда:
$\epsilon=k_g(\eta_0+\zeta)/s\to0$; $\nu\to0$; $s\partial_s\epsilon=k_g\eta_{0,s}-\epsilon\to0$; $\partial_\theta\epsilon=(k_g'\eta+k_g\eta_{0,\theta})/s\to0$;
$\partial_\theta\nu=\eta_{0,s\theta}-\kappa\eta_{0,\theta}/s-\kappa\theta\eta_{0,\theta\theta}/s\to0$; $s\partial_s\nu=s\eta_{0,ss}-\kappa\theta(\eta_{0,s\theta}-\eta_{0,\theta}/s)\to0$;
$x\partial_x\epsilon=-\kappa\theta k_g'\eta/x+k_g\nu-\epsilon\to0$; $x\partial_x\nu=s\partial_s\nu-\kappa\theta\partial_\theta\nu\to0$ ($k_g,k_g'$ ограничены). $\square$

Пусть $\varpi_1(x)$ — супремум суммы модулей восьми величин $\epsilon,\nu,\partial_\theta\epsilon,s\partial_s\epsilon,\partial_\theta\nu,s\partial_s\nu,x\partial_x\epsilon,x\partial_x\nu$ по
$\{s\le x\}$; $\varpi_1\to0$. Положим $\varpi:=10(1+\bar k_g)\varpi_1$, $\bar k_g:=\max_{|\theta|\le\theta_1}|k_g|$.

### 4.4. Доказательство теоремы N

*Порядок выбора констант.* $\kappa$ — по (4.0); $r_1$ — по п. 7 ниже (не зависит от $\kappa\le\frac12$); затем
$r_0\in(r_1,\min(\theta_1/2,e_1,\frac14)]$; затем $s_0<\sigma_1^N$ так, что на $\mathcal N=\{0<x<s_0,\ |b|<r_0\}$:
$|\epsilon|\le\frac14$, $|\nu|\le\frac14$, $|\eta_{0,s}|+\frac43|\eta_{0,\theta}|/x\le1$, $|\eta|<\min(t_1,\frac14)\,x$ (лемма N5) и образ лежит в $B_r$.

1. **$(\Phi0)$.** $\Phi=\Pi\circ T\circ L$, где $L(x,u,\zeta)=(x,ux^{-\kappa},\zeta)$ — $C^\infty$-диффеоморфизм $\{x>0\}\times\mathbb R^2$ на себя,
   $T(s,\theta,\zeta)=(s,\theta,\eta_0(s,\theta)+\zeta)$ — $C^2$-диффеоморфизм $\{s>0,|\theta|<\theta_1\}\times\mathbb R$ на себя (обратный
   $(s,\theta,\eta)\mapsto(s,\theta,\eta-\eta_0)$; $\eta_0\in C^2$ при $s>0$, так как $s\mapsto s^{1/N}$ аналитично), а $T(L(\mathcal N))\subset\mathcal P$ по
   выбору $s_0$; $\Pi$ — аналитический диффеоморфизм $\mathcal P$ на открытое множество (лемма K3 [008]).
   $|\Phi|^2=x^2+\eta^2$, $|\eta|\le x/4$, так что $x\le|\Phi|\le2x$.
2. **$(\Phi1')$.** По (4.3) $1\le h\le1+\frac14\cdot\frac1{16}\cdot\frac{25}{16}+\frac1{16}<\frac32$.
3. **$(\Phi2'')$, первая оценка.** $\nabla\rho=\nabla s=\omega(\theta)$ (лемма K3: $s$ — та же функция на $\mathbb R^3$, что для $\Pi$). Для
   $w\perp Y$: $\langle\nabla\rho-Y/h,w\rangle=\langle\omega,w\rangle=\kappa\theta(1-\epsilon)w_\ell-\nu w_n$, и
   $|\langle\nabla\rho-Y/h,w\rangle|\le(\frac54\kappa|\theta|+|\nu|)|w|$: $\gamma_1=\frac54\kappa$, остаток — в $\varpi$.
4. **$(\Phi2'')$, вторая оценка.** По (4.4) для $|w|=1$ ($|\langle-\omega+k_gn,w\rangle|\le1+\bar k_g$, $\kappa|\theta|\le\frac18$):
   $|\langle x\partial_x^2\Phi,w\rangle|\le\kappa(1-\kappa)|\theta|+\frac54\kappa^2(1+\bar k_g)\theta^2+\frac18(\kappa|\epsilon|+|x\partial_x\epsilon|+\bar k_g|\nu|)+|x\partial_x\nu|$
   $\le\gamma_2|\theta|+C_1\theta^2+\varpi$.
5. **$(\Phi3'')$.** По (4.6) главный член $\ge(\frac45-\frac12)w_\ell^2\ge0$ ($|\epsilon|\le\frac14$). Для $w\perp Y$: $|w_\omega|\le(\frac54\kappa|\theta|+|\nu|)|w|\le|w|$,
   $|a^\zeta|\le|w_n|+|w|(|\eta_{0,s}|+\frac43|\eta_{0,\theta}|/x)\le2|w|$, $\frac1{1-\epsilon}\le\frac43$. Почленно:
   - первый член $\mathcal E_r$: $\le\big[\frac53\kappa\bar k_g|\theta|+\frac43(|\partial_\theta\epsilon|+\bar k_g|\nu|+|\partial_\theta\nu|)\big]|w|^2$;
   - $|\kappa\theta w_\ell w_\omega|\le(\frac54\kappa^2r_0|\theta|+|\nu|)|w|^2$;
   - $|w_\omega[\dots]|\le(|s\partial_s\epsilon|+|s\partial_s\nu|)|w|^2$;
   - $|a^\zeta\kappa\theta k_gw_\ell|\le2\kappa\bar k_g|\theta||w|^2$.

   Итого $|\mathcal E_r|\le\big[(\frac{11}3\kappa\bar k_g+\frac5{16}\kappa^2)|\theta|+6(1+\bar k_g)\varpi_1\big]|w|^2\le(C_1|\theta|+\varpi)|w|^2$, и
   $x\langle w,D_wY\rangle\ge-(C_1|b'|+\varpi)|w|^2$.
6. **(F).** $U(\Phi(x,u,\zeta))=U\big(x\omega(\theta)+(\eta_0(x,\theta)+x^ce)n(\theta)\big)=x^\beta\tilde F(x^{1/N},\theta,e)$ по (NF) ($|\theta|<r_0\le\theta_1$,
   $|e|<r_0\le e_1$). $F(\varsigma,b):=\tilde F(\varsigma,\theta,e)$ непрерывна с $\nabla_bF$ на $[0,s_0^{1/N})\times B_{r_0}$, и $\sup|\varsigma\partial_\varsigma F|\to0$.
7. **$(V'')$.** $F_0(\theta,e)=G(\theta)+e^{2r'}\mathsf p(\theta,e)$, $F_0(0)=-a_0<0$, $Q=G(\theta)-G(0)+e^{2r'}\mathsf p$. Возьмём $r_1$ так, что при
   $|\theta|,|e|<r_1$: $G(\theta)-G(0)\ge\frac14G''(0)\theta^2$ и $\theta G'(\theta)-(G(\theta)-G(0))\ge\frac14G''(0)\theta^2$ (обе левые части равны
   $\frac12G''(0)\theta^2+o(\theta^2)$, так как $G\in C^2$, $G'(0)=0$), $\mathsf p\ge\mathsf p_0/2$ и $c|e\,\partial_e\mathsf p|+|\theta\,\partial_\theta\mathsf p|\le\frac14(2r'c-\frac12)\mathsf p_0$. Тогда
   $Q\ge\lambda_0\theta^2+\frac{\mathsf p_0}2e^{2r'}=\lambda_0|b'|^2+q_0(|b''|)$, и при $\mu=\kappa$
   $$\kappa\theta\partial_\theta Q+c\,e\,\partial_eQ-\kappa Q=\kappa\big[\theta G'-(G-G(0))\big]+e^{2r'}\big[(2r'c-\kappa)\mathsf p+c\,e\,\partial_e\mathsf p+\kappa\theta\,\partial_\theta\mathsf p\big]\ge0,$$
   так как $(2r'c-\kappa)\mathsf p\ge(2r'c-\frac12)\frac{\mathsf p_0}2$, а модуль остальных членов скобки не больше $\frac14(2r'c-\frac12)\mathsf p_0$
   ($\kappa\le\frac12$; $2r'c-\frac12>0$). Наконец, $\Gamma_*=\sqrt{a_0/\lambda_0}\big[\frac{3\sqrt3}2\beta\cdot\frac54\kappa+2\sqrt2\kappa(1-\kappa)\big]\le\kappa\sqrt{a_0/\lambda_0}\big(\frac{15\sqrt3}8\beta+2\sqrt2\big)$, и
   по (4.0) $\Gamma_*^2\le\beta\kappa=\beta\mu$.

   Условие $\mu=\kappa\le\beta$: из (NF), (G) и $U\in C^2$ следует $\beta\ge2$. Действительно, при $\theta=0$, $e=0$ точка
   $q_s=s\omega^*+\eta_0(s,0)n$ имеет $|q_s|\le2s$, а $U(q_s)=s^\beta\tilde F(s^{1/N},0,0)$ и $\tilde F(\sigma,0,0)\to G(0)\ne0$; так как
   $|U(q)|\le M|q|^2$ около $0$ ($U\in C^2$, $U(0)=0$, $\nabla U(0)=0$), то $s^\beta|G(0)|/2\le4Ms^2$ при малых $s$, откуда $\beta\ge2>\kappa$.

Условия класса (GT3″) выполнены; теорема 2″ даёт траекторию $q=\Phi(x,u,\zeta)=x\omega(\theta)+(\eta_0+x^ce)n(\theta)$ с
$b(t)\in\overline{\Omega_\delta}$: $|\theta|\le\sqrt{2\delta/\lambda_0}$, $\frac{\mathsf p_0}2|e|^{2r'}\le2\delta$. Расстояние до луча $\mathbb R_+\omega(\theta)$ не больше $|\eta|=o(x)$,
а $|\omega(\theta)-\omega^*|\le|\theta|$. $\square$

**Замечание 4.1 (что изменилось по сравнению с K2 [008]).** (i) Профиль по $e$ может быть вырожденным
($r'\ge2$); (ii) дно $\eta_0$ — функция от $s^{1/N}$, а не аналитическая по $s$; (iii) $\lambda_0=G''(0)/4$ вместо
$\frac14\min(G''(0),h_n(0))$: нормальная жёсткость в (U2) не входит. При $r'=1$ можно применять и теорему 2′ [008]
напрямую (с $\lambda_0=\frac14\min(G''(0),2\mathsf p_0)$).

### 4.5. Следствия

**Следствие N′ (аналитический $U$, данные Ньютона)** [Доказано]. Пусть $U$ аналитична, дуга — как в
1.1, $\gamma>0$ рационально, $\Phi_0=\Phi_0^{(\gamma)}$, и на $[-\theta_1,\theta_1]$ есть ветвь $\varepsilon_0\in C^2$ постоянной кратности (E) с
$G(\theta)=\Phi_0(\theta,\varepsilon_0(\theta))$, $G(0)<0$, $G'(0)=0<G''(0)$. Тогда выполнены (NF), (G) с $\beta=m+\beta'(\gamma)$, $c=1+\gamma$,
$N$ — знаменатель $\gamma$, $y_0(\sigma,\theta)=\sigma^{N\gamma}\varepsilon_0(\theta)$, $\tilde F(\sigma,\theta,e)=\tilde U(\sigma,\theta,\varepsilon_0(\theta)+e)$, и по теореме N есть
асимптотическая траектория. При $r'=1$ достаточно, чтобы $\varepsilon_0(0)$ была невырожденным локальным
минимумом $\Phi_0(0,\cdot)$, а условия на $G$ выполнялись для ветви, продолженной по теореме о неявной
функции. Типичный выбор — $\gamma=\gamma_*$ (первое ребро) при условии (M).

*Доказательство.* Лемма N1 с $\Lambda=[-\theta_1,\theta_1]$ и $E\ge\max|\varepsilon_0|+e_1$: (2.1) при $\varepsilon=\varepsilon_0(\theta)+e$ — это
(NF), так как $s^{1+\gamma}(\varepsilon_0+e)=s\cdot s^\gamma\varepsilon_0+s^ce$ и $s^\gamma=\sigma^{N\gamma}$. $y_0\in C^2$, $y_0(0,\cdot)=0$ ($N\gamma\ge1$).
$\tilde F$ непрерывна, $\partial_\theta\tilde F=\partial_\theta\tilde U+\partial_\varepsilon\tilde U\,\varepsilon_0'$ и $\partial_e\tilde F=\partial_\varepsilon\tilde U$ непрерывны, $\sigma\partial_\sigma\tilde F=\sigma\partial_\sigma\tilde U\to0$.
$\tilde F(0,\theta,e)=\Phi_0(\theta,\varepsilon_0+e)=G+e^{2r'}\mathsf p$ по (E) и формуле Тейлора многочлена; $\mathsf p$ — многочлен по $e$ с
коэффициентами класса $C^2$ по $\theta$, $\mathsf p(0,0)>0$; $G\in C^2$. $\square$

**Следствие N″ (струйный критерий, $U\in C^{K+1}$)** [Доказано]. Пусть $U\in C^{K+1}(B_r)$, $U(0)=0$, $\nabla U(0)=0$,
$P:=j^KU$, и для многочлена $P$ выполнены условия следствия N′ с показателем $\beta<K+1$. Тогда (NF), (G)
выполнены и для $U$ (с теми же $y_0$, $G$, $\mathsf p$), и есть асимптотическая траектория.

*Доказательство.* $R:=U-P\in C^{K+1}$, $|R(q)|\le C|q|^{K+1}$, $|\nabla R(q)|\le C|q|^K$. Точка
$q=s\omega+(\eta_0+s^ce)n$ имеет $|q|\le2s$; положим $R_F(\sigma,\theta,e):=R(q)/s^\beta$ ($s=\sigma^N$). Тогда
$|R_F|\le Cs^{K+1-\beta}$, $|\partial_eR_F|=s^{c-\beta}|\langle\nabla R,n\rangle|\le C's^{c+K-\beta}$,
$|\partial_\theta R_F|=s^{-\beta}|\langle\nabla R,\partial_\theta q\rangle|\le C's^{K+1-\beta}$ ($|\partial_\theta q|\le C''s$ по (1.1)),
$|\sigma\partial_\sigma R_F|=N|s^{1-\beta}\langle\nabla R,\partial_sq\rangle-\beta R_F|\le C's^{K+1-\beta}$ ($|\partial_sq|\le C''$). Все стремятся к $0$ равномерно, поэтому
$\tilde F_U:=\tilde F_P+R_F$ (доопределённая при $\sigma=0$ значением $\tilde F_P(0,\cdot)$) удовлетворяет (NF) и (G) с тем же
$\tilde F_U(0,\cdot)$. $\square$

## 5. Примеры M1 и M2

Обе функции — из полигона (`experiments/numerics/2026-10-21-zoo/catalog.py`). У обеих $u_4=z^4$, $\Sigma$ —
большой круг $z=0$: $\omega=(\cos\phi,\sin\phi,0)$, $n=e_z$, $k_g=0$, натуральный параметр $\theta=\phi-\phi^*$ ($\phi$ —
полярный угол). $u_4(\omega+yn)=y^4$: (M) с $2r=4$, $a\equiv1$ на всём круге. Все выкладки ниже — точные,
вручную; [Эксперимент] `newton_M1M2.py` повторяет их в sympy (вывод `newton_M1M2.out`).

### 5.1. M1 $=(z-x^2)^4+x^5+y^5+xy^6+yx^6$

- $U(s\omega+\eta n)=(\eta-s^2\cos^2\phi)^4+s^5G(\phi)+s^7g_7(\phi)$, $G=\cos^5\phi+\sin^5\phi$, $g_7=\cos\phi\sin^6\phi+\sin\phi\cos^6\phi$;
  $\varphi=(y-s\cos^2\phi)^4+sG+s^3g_7$. Носитель $\mathcal S=\{(0,4),(1,3),(2,2),(3,1),(4,0),(1,0),(3,0)\}$.
- $\gamma_*=\min\big(\frac11,\frac22,\frac33,\frac44,\frac14,\frac34\big)=\frac14$ (точка $(1,0)$); $\beta'=1$, $j=5$, $c=\frac54$, $N=4$, $N\gamma_*=1$.
- $\Phi_0=\varepsilon^4+G(\phi)$; $\tilde U(\sigma,\phi,\varepsilon)=(\varepsilon-\sigma^3\cos^2\phi)^4+G(\phi)+\sigma^8g_7(\phi)$ — многочлен, тождество (2.1)
  $U(s\omega+s^{5/4}\varepsilon n)=s^5\tilde U(s^{1/4},\phi,\varepsilon)$ проверяется раскрытием скобок.
- Ветвь $\varepsilon_0\equiv0$: $\Phi_0(\phi,e)-G=e^4$ — **вырожденный профиль**, $r'=2$, $\mathsf p\equiv1$; $G=G_{\min}$.
- $G'=5\sin\phi\cos\phi(\sin^3\phi-\cos^3\phi)$; критические точки $\phi\in\{0,\frac\pi2,\pi,\frac{3\pi}2,\frac\pi4,\frac{5\pi}4\}$ со значениями
  $G=1,1,-1,-1,\frac{\sqrt2}4,-\frac{\sqrt2}4$ и $G''=-5,-5,5,5,\frac{15\sqrt2}4,-\frac{15\sqrt2}4$. Отрицательные невырожденные минимумы:
  $\phi^*=\pi$ ($\omega^*=-e_x$) и $\phi^*=\frac{3\pi}2$ ($\omega^*=-e_y$): $G=-1$, $G'=0$, $G''=5>0$, и $G''+jG=0$.
- Константы: $a_0=1$, $\lambda_0=\frac54$, (4.0): $\kappa\le0.01719$.
- **Вывод** [Доказано]: по следствию N′ (с $\gamma=\gamma_*$, $\varepsilon_0=0$, $r'=2$) у M1 есть асимптотические траектории
  вдоль $-e_y$ и вдоль $-e_x$: $q=s\omega(\theta)+s^{5/4}e\,e_z$, $|\theta|\le\sqrt{8\delta/5}$, $|e|\le(4\delta)^{1/4}$.
- Точное дно (для сравнения): $\partial_\eta U=4(\eta-s^2\cos^2\phi)^3$ в слое, единственная критическая точка
  $\eta^*=s^2\cos^2\phi$ (кратности 3), $F_{\rm fl}=s^5G+s^7g_7$ точно; профиль у точного дна $(\eta-\eta^*)^4$ вырожден при всех
  $s$. Мы используем приближённое дно $\eta_0=0$ (конус): $\eta^*=O(s^2)=o(s^{5/4})$ лежит внутри ширины оврага.
- Декартова карта развёртки (K1) здесь не годится: её поперечный гессиан $G''+jG=0$; в valleys это
  «$H_{\rm plane}=0$» ([Эксперимент], `experiments/numerics/2026-10-21-valleys/README.md`).

### 5.2. M2 $=z^4+z(x^4+x^3y+y^4)+x^6+xz^5+2yz^5$

- $U(s\omega+\eta n)=\eta^4+s^4f(\phi)\eta+s^6\cos^6\phi+s\eta^5(\cos\phi+2\sin\phi)$, $f=\cos^4\phi+\cos^3\phi\sin\phi+\sin^4\phi$;
  $\varphi=y^4+sf\,y+s^2\cos^6\phi+s^2y^5(\cos\phi+2\sin\phi)$, $\mathcal S=\{(0,4),(1,1),(2,0),(2,5)\}$.
- $\gamma_*=\min(\frac13,\frac24)=\frac13$ (точка $(1,1)$); $\beta'=\frac43$, $j=\frac{16}3$, $c=\frac43$, $N=3$, $N\gamma_*=1$.
- $\Phi_0=\varepsilon^4+f(\phi)\varepsilon$; $\tilde U=\varepsilon^4+f\varepsilon+\sigma^2\cos^6\phi+\sigma^7\varepsilon^5(\cos\phi+2\sin\phi)$.
- $f=\frac34+\frac14\cos4\phi+\frac14\sin2\phi+\frac18\sin4\phi\ge\frac18>0$. Единственная критическая точка $\Phi_0(\phi,\cdot)$ —
  $\varepsilon_0=-(f/4)^{1/3}$ (глобальный минимум), $\partial_\varepsilon^2\Phi_0=12\varepsilon_0^2>0$: **профиль невырожден**, $r'=1$;
  $G=\frac34f\varepsilon_0=-3\cdot4^{-4/3}f^{4/3}$, $\Phi_0(\varepsilon_0+e)-G=e^2\big[(e+2\varepsilon_0)^2+2\varepsilon_0^2\big]$, $\mathsf p\ge2\varepsilon_0^2>0$. В переменной $y$:
  минимум $y^4+sf\,y$ сдвинут в $y^*\approx s^{1/3}\varepsilon_0$, то есть дно $\eta_0=s^{4/3}\varepsilon_0(\phi)$.
- $G'=-4^{-1/3}f^{1/3}f'$, и в критических точках $G''=-4^{-1/3}f^{1/3}f''$. $f'=\cos^4\phi\,(4t^3-3t^2-4t+1)$, $t=\tan\phi$, и
  $f'(\frac\pi2)=0$. Кубика имеет три вещественных корня $t_1\in(-0.82633,-0.82632)$, $t_2\in(0.22366,0.22367)$,
  $t_3\in(1.35265,1.35266)$ (точная изоляция). $f''=-4\cos4\phi-\sin2\phi-2\sin4\phi$.
  - $\phi^*=\arctan t_2\approx0.2200471$: строго $t_2\in(0.22,0.23)$ (кубика равна $\frac{1087}{62500}>0$ и $-\frac{1877}{62500}<0$),
    так что $4\phi^*\in(0.8662,0.9043)\subset(0,\frac\pi2)$, $\cos4\phi^*>\cos0.9043>0.6$, $\sin2\phi^*,\sin4\phi^*>0$ и
    $f''(\phi^*)<-2.4$. Значит, $G'(\phi^*)=0$, $G''(\phi^*)>0$, $G(\phi^*)<0$. Численно $f(\phi^*)=1.112115$, $f''=-4.51577$,
    $G=-0.5443867$, $G''=2.947325$, $\varepsilon_0=-0.652674$; $G''+jG=0.0439$.
  - $\phi=\frac\pi2$ ($\omega^*=e_y$): $f=1$, $f''=-4$, $G=-3\cdot4^{-4/3}\approx-0.47247$, $G''=4^{2/3}\approx2.5198$, и $G''+jG=4^{2/3}-16\cdot4^{-4/3}=0$
    точно.
  - Так как $f(\phi+\pi)=f(\phi)$, те же минимумы в $\phi^*+\pi$ и $\frac{3\pi}2$; $t_1$, $t_3$ — максимумы $G$ (минимумы $f$).
- Константы (4.0): в $\phi^*$ $a_0=0.54439$, $\lambda_0=0.73683$, $\kappa\le0.01778$; в $\frac\pi2$ $a_0=0.47247$, $\lambda_0=0.62996$, $\kappa\le0.01752$.
- **Вывод** [Доказано]: по следствию N′ (с $r'=1$) у M2 есть асимптотические траектории вдоль четырёх
  направлений $\pm\omega(\phi^*)$, $\pm e_y$: $q=s\omega(\theta)+s^{4/3}(\varepsilon_0(\phi)+e)e_z$, $|\theta|\le\sqrt{2\delta/\lambda_0}$,
  $|e|\le\sqrt{2\delta/3}\,/|\varepsilon_0(\phi^*)|$ ($\mathsf p_0=6\varepsilon_0^2$). Невырожденный профиль: здесь годится и теорема 2′ [008].

### 5.3. Сравнение с численными данными [Эксперимент]

- `floor_nm.py`: $\min_\eta U(s\omega+\eta n)/s^j\to G(\phi)$ — M1 точно (разность $s^2g_7$), M2 с ошибкой $O(s^{2/3})$
  ($-0.50430,-0.54253,-0.54430,-0.544386,-0.5443867$ при $s=10^{-2},10^{-4},10^{-6},10^{-9},10^{-12}$ против
  $G(\phi^*)=-0.5443867$); точка минимума $\eta/s^{4/3}\to\varepsilon_0$. В нормальном слое один локальный
  экстремум (M2: кубика $4\eta^3+s^4f+\dots$ с одним вещественным корнем).
- Сравнение с `experiments/numerics/2026-10-21-valleys/` (глубина на сферах): M1 — $\beta=5$, $a=1$, два оврага
  $-e_x$, $-e_y$; M2 — $\beta=\frac{16}3$, $a=0.54424$ при $r=10^{-6}$ (у нас $0.544387$), направление $(0.97586,0.21831)$
  (у нас $(\cos\phi^*,\sin\phi^*)=(0.975887,0.218276)$), $z$-компонента $-0.0065\approx s^{1/3}\varepsilon_0$; второй овраг с отношением
  глубин $0.8680$ (у нас $G(\frac\pi2)/G(\phi^*)=0.8679$). Их «$\rho=H_{\rm plane}/(\beta a)$» $=0.015$ совпадает с
  $(G''+jG)/(-jG)=0.0151$. Изолированность $0$ у M1, M2 — по полигону (Singular: $\mu=48$, $59$); в теореме N
  она не используется.
- `exit_nm.py` — прямое численное дифференцирование $\Xi=\frac d{dt}(V-\delta\rho^\beta)$ вдоль потока на точках множества
  выхода (A5) для карты (4.1):
  - M1 ($\sigma\le0.05$): минимум $\frac\rho\lambda\Xi/(\delta\rho^\beta)$ равен $0.034$, $0.10$, $0.37$–$0.40$, $0.83$ при $\kappa=0.017,0.05,0.2,0.5$ (то есть $\approx2\kappa$ при малых $\kappa$),
    при $\kappa=0$ — положителен, но $\to0$ с $\delta,\sigma$;
  - M2: при $x\gtrsim10^{-4}$ условие выхода **нарушается** (минимум $\approx-1.2$ при всех $\kappa$, в точках с $K_\perp>0$): наклон
    дна $\nu=\eta_{0,s}=\frac43\varepsilon_0x^{1/3}$ убывает медленно, и член $L_1\theta_1/\sqrt\delta$ леммы 2′ ещё не мал. При
    $x\le10^{-6}$ ($\delta=0.01$) выход строгий при всех проверенных $\kappa$ ($0.046$ при $\kappa=0.0178$; $0.41$ при $\kappa=0.2$).
    Это согласуется с теоремой ($\sigma_*$ выбирается после $\delta$), но показывает, насколько глубоким может
    быть асимптотический режим при поправках Пюизё $x^{1/N}$.

## 6. Где работают аналитичность и изолированность

- **Теорема 2″ и теорема N** — утверждения для $U\in C^2$ при заданных (NF), (G); аналитичность и
  изолированность не используются. Вся «конечность типа» — в (NF), (G): вдоль дна
  $U=s^\beta(G(\theta)+o(1))$ с $G(0)<0$, поперёк — степенные стенки с запасом Эйлера.
- **Следствие N″** делает это явным: условия теоремы N — условия на конечную струю $j^KU$, $K+1>\beta$, и
  для $U\in C^{K+1}$ они достаточны. С гладкими контрпримерами (Пенлеве–Уинтнер, Лалуа; по
  `problem/KNOWN_RESULTS.md`, с первоисточниками не сверено) это не конфликтует: у них никакая конечная
  струя не даёт ветви с $G(0)<0$. Пример Уреньи касается тотальной неустойчивости; теорема N даёт одну
  асимптотическую траекторию.
- **Аналитичность работает** (i) в лемме N1: сходимость $\tilde U$ и непрерывность при $\sigma=0$ (это даёт (F)); (ii) в
  леммах N2–N4: описание дна, каноничность $j$ и $G_{\min}$, ветви Пюизё; (iii) в утверждениях «процесс
  останавливается»: если $(i,l)\in\mathcal S$ с $l<2r$ нет, то $\varphi=y^{2r}A$, $U(s\omega+\eta n)=s^{m-2r}\eta^{2r}A$ и $\nabla U=0$ на
  конусе над дугой (производная по $\eta$ — от $\eta^{2r}$, $2r\ge2$; вдоль конуса $U\equiv0$); если в лемме N4 $\hat G\equiv0$, то
  по N4(d) — поверхность критических точек. Для $C^\infty$ обе альтернативы ломаются: коэффициенты
  $\varphi_{il}$ могут быть «плоскими», и тогда нет ни конечного $\gamma_*$ или $k$, ни критического множества.
- **Изолированность** используется только в (iii): у изолированной критической точки $\gamma_*<\infty$, и
  уточнение леммы N4(c) останавливается. Ни в теореме N, ни в примерах она не нужна (M1, M2
  изолированы, но это не используется).
- **Над $\mathbb R$ и над $\mathbb C$.** Все рассуждения вещественные; конечность числа Милнора не используется.

## 7. Пробелы и что остаётся

**Пробелы этой записки.**

1. Теорема 2″ и теорема N опираются на лемму 2′ и лемму K3 [008] и на §1 [008] (формула
   $U(s(\omega+yn))=s^m\varphi$). Результат 008 окончательно не принят; если в этих местах найдут ошибку,
   её придётся переносить сюда. Формулы (4.2)–(4.6) выведены здесь заново и проверены символьно.
2. Лемма N3 опирается на теорему Ньютона–Пюизё без сверки с первоисточником (стандартный факт); в
   доказательствах теоремы N и следствий она не используется.
3. Для каждого $\delta$ своя траектория; касание самого луча $\mathbb R_+\omega^*$ не доказано (как в [007], [008]).
4. Граница (4.0) на $\kappa$ грубая (численно выход есть до $\kappa=0.5$); на результат это не влияет.

**Что остаётся вне теоремы N** (при $n=3$, $u_m\ge0$, кривые компоненты $\Sigma$).

1. **Переменная кратность вдоль $\Sigma_0$**: точки, где $a(\theta,0)=0$ (нормальная кратность прыгает), и точки,
   где меняется многоугольник Ньютона (обнуляется коэффициент вершины $\varphi_{il}(\theta)$). Если такая точка —
   $\omega^*$, ветвь $\varepsilon_0$ может быть не $C^2$: например, $\Phi_0=\varepsilon^4+\theta\varepsilon^2+G_1(\theta)$ даёт при $\theta<0$ два минимума и
   $G_{\min}=G_1-\frac{\theta^2}4\mathbf 1_{\theta<0}$ — только $C^{1,1}$. [Гипотеза] Нужна карта с «переменным профилем»
   (раздутие в $(\theta,\varepsilon)$).
2. **Вырожденный минимум $G$** ($G-G(0)\sim\theta^{2q}$, $q\ge2$): кривизна карты действует по $b'=\theta$, и препятствие R3 [007]
   остаётся; [Эскиз, не выписан] — $\kappa=\kappa(\delta)$ или другой выбор среза.
3. **Каскад в нормальном направлении:** $G_{\min}\equiv0$ на первом ребре при вырожденном профиле (следующие
   рёбра многоугольника Ньютона, ветви, сливающиеся при $\sigma\to0$). При невырожденном профиле это
   закрывает лемма N4(c).
4. **Угловые каскады** ($G\ge0$ с нулями) и $G\equiv{\rm const}<0$ на замкнутой $\Sigma_0$ — как в замечании 6 [008].
5. **Особые точки $\Sigma$** и точечные компоненты с вырожденным нормальным гессианом (типа $x^4+y^4-z^6$, P1):
   для последних, по-видимому, работает уже случай $(V_0)$ теоремы 2 [007] с прямой картой ([Гипотеза]:
   так прочитано в valleys README; здесь не проверялось). Формально теорема 2″ с $I'=\varnothing$ тоже их
   охватывает при коэрцитивном профиле с неравенством Эйлера.
6. **Сведение (A) к «задаче на дне».** Пусть $u_m\ge0$ и $\Sigma$ — объединение конечного числа замкнутых гладких
   кривых, вдоль каждой из которых выполнено (M). [Доказано, элементарно, по лемме N2 и рассуждению
   K4(c) [008]: вне трубок $\{s\omega+\eta n:\ |\eta|<y_1s\}$ направления отделены от $\Sigma$, там $u_m\ge c|q|^m$ и $U>0$; в
   трубке $U\ge F_{\rm fl}$ по определению; трубки замкнутых кривых — по лемме K3 [008] для периодического
   $\theta$.] Тогда $0$ — локальный минимум $U$ тогда и только тогда, когда $F_{\rm fl}(s,\theta)\ge0$ при малых $s>0$ на всех
   кривых. В частности, если $G_{\min}<0$ где-то, то $0$ не минимум, а если $G_{\min}>0$ на всех кривых — строгий
   минимум. Теорема N покрывает случай, когда у $G$ есть отрицательный невырожденный минимум с
   равномерной ветвью. Общий случай (пп. 1–4) открыт.
7. $n\ge4$ — не рассматривалось.

## 8. Эксперименты

Все — [Эксперимент], не доказательство. Запуск: `~/venv/bin/python <скрипт>` из
`experiments/prover/normal-multiplicity/`.

- `frames_nm.py` → `frames_nm.out`: символьная проверка (4.2)–(4.6), $s\partial_s\epsilon$, $x\partial_x\epsilon$, $h$, разложения $w$ по
  координатным полям и формулы $x\langle w,D_wY\rangle$ при $\eta_0=s\,y_0(s^{1/3},\theta)$ с общим многочленом $y_0$ (16
  коэффициентов, $y_0(0,\cdot)=0$) и общим $k_g$ (кубический многочлен): все 14 тождеств верны (sympy, точно).
- `newton_M1M2.py` → `newton_M1M2.out`: носители, $\gamma_*$, $j$, $c$, $\Phi_0$, $\tilde U$, тождество (2.1), ветви, $G$, критические
  точки и $G''$ (с точной изоляцией корней кубики для M2), профиль $\mathsf p$, константы (4.0).
- `floor_nm.py` → `floor_nm.out`: функция дна $F_{\rm fl}$ при $s=10^{-2}\dots10^{-12}$ (mpmath, 40 знаков), сравнение с $s^jG$.
- `exit_nm.py` → `exit_M1.out`, `exit_M2.out`, `exit_M2_deep.out`: строгий выход (A5) прямым дифференцированием
  вдоль потока; 120 точек множества выхода на каждую строку, 16 направлений $v_\perp$, контроль
  $|V-\delta\rho^\beta|/(\delta\rho^\beta)<10^{-15}$ в каждой точке; запуск `exit_nm.py M1`, `exit_nm.py M2`, `exit_nm.py M2 deep`
  (mpmath 30/50 знаков, $x$ до $10^{-31}$).
