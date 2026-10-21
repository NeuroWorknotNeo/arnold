# Постоянная нормальная кратность на кривых компонентах $\Sigma$: широкий овраг, трубка, каскад и теорема M′ ($n=3$)

- **Автор:** prover (агент), 21.10.2026. Задание главного агента: распространить теорему M
  ([`results/010-morse-bott.md`](../../results/010-morse-bott.md)) на случай, когда каждая
  компонента-кривая $\Sigma$ имеет постоянную нормальную кратность $2r\ge2$ (не обязательно Морс–Ботт):
  аналоги теорем Mb, Mc, Md при $2r\ge4$ (вырожденный нормальный профиль $e^{2r'}\mathsf p$, дно — ряды
  Пюизё по $s$), аналог предложения R и итоговая теорема M′.
- **Статус:** по пунктам — таблица в §0.2. Независимой проверки нет. Главное:
  - теоремы W, C, D (аналоги Mb, Mc, Md) доказаны в общей форме «данные нормальной формы ⇒
    асимптотическая траектория»;
  - теорема M′ доказана при дополнительном условии (UR) на ветви дна в нормальном слое; (UR)
    следует из проверяемого условия (R) и выполняется при $r\equiv1$, так что теорема M — частный
    случай;
  - случай отрицательного минимума функции дна (W) закрыт при более слабых условиях (предложение W′);
  - **без (UR) полнота разбора не доказана**: остаются три явно описанных препятствия (O1)–(O3) (§13);
  - изолированность критической точки нигде не нужна.
- **Зависит от** (всё перечисленное проверено агентами-рецензентами и ждёт проверки человеком):
  - [007] = [`results/007-gt3.md`](../../results/007-gt3.md): теорема A, лемма 1, лемма 2, теорема 2
    (класс (GT3), условия $(\Phi0)$–$(\Phi3)$, (F), $(V_0)$, п. 1 шага 6 доказательства);
  - [008] = [`results/008-class-K.md`](../../results/008-class-K.md): §1 (формула (1.1)), лемма K1, лемма K3
    (в том числе для замкнутой кривой с периодическим $\theta$), теорема K0, доказательство предложения
    K4(c) (§11);
  - [010] = [`results/010-morse-bott.md`](../../results/010-morse-bott.md): лемма M (§4), лемма V (§7),
    доказательство теоремы Md (§8, пп. 1–5, формулы (8.1)–(8.3)), лемма N, п. (N3);
  - [011] = [`results/011-normal-multiplicity.md`](../../results/011-normal-multiplicity.md): утверждение 1
    (первое ребро), леммы N1, N2, лемма N5 (§7 доказательства);
  - [009] = [`results/009-euler-field.md`](../../results/009-euler-field.md): только предложения 5.2 и 5.4
    (для сравнения и для примера O1);
  - стандартные факты: аналитическая теорема о неявной функции, теорема единственности для
    аналитических функций, формула Тейлора с интегральным остатком; через лемму V [010] —
    подготовительная теорема Вейерштрасса и теорема Ньютона–Пюизё (формулировки в [010], §7; с
    первоисточниками не сверены).
- **Скрипты** [Эксперимент]: [`experiments/prover/morse-bott-mult/`](../../experiments/prover/morse-bott-mult/),
  список и выводы — §10.3.

## 0. Сводка

### 0.1. Идея

При $r=1$ (Морс–Ботт) дно оврага в нормальном слое — единственная невырожденная критическая
точка, аналитическая по $(s,\theta)$, и всё сводится к аналитической функции двух переменных
$\hat G(s,\theta)$. При $2r\ge4$ в нормальном слое до $2r-1$ критических точек. Их ветви — ряды Пюизё по
$s$, они могут сливаться и менять кратность при изменении $\theta$, а нормальный профиль бывает
вырожденным ($e^{2r'}$). Схема этой записки:

1. **Первое ребро** многоугольника Ньютона в нормальном слое ([011]: $\gamma_*$, $\Phi_0$) даёт масштаб
   $s^c$, глубину $s^j$ и функцию $G_{\min}(\theta)=\min_\varepsilon\Phi_0(\theta,\varepsilon)$. Знак $\min G_{\min}$ разделяет
   **широкий случай** (W) ($\min G_{\min}<0$) и **каскад** (Z) ($\min G_{\min}=0$, отрицательные значения функции
   дна появляются в следующих порядках). Это предложение R′.
2. **Широкий овраг** (теорема W; аналог Mb). Достаточно приближённого дна вида ряда Пюизё и
   локального профиля $P(\theta,e)$ в точке минимального дна. Нужны изолированный нуль $P$ и
   **диагональное** неравенство Эйлера $\kappa\theta\partial_\theta P+c_2e\partial_eP\ge\kappa\mu_0P$. Нормальный вес $c_2\le c$
   можно выбирать: в нормальную компоненту поля добавлен член $\lambda\zeta/s$, $\lambda=c-c_2$. Этот член
   мал, так как нормальное направление узкое. Угловой поворот $\kappa=\kappa(\delta)$ берётся из леммы M [010].
   Так покрываются одновременно вырожденный угловой минимум ($G-G(0)\sim\theta^{2p}$), вырожденный
   нормальный профиль ($e^{2r'}$) и часть случаев **расщепления ветви**, когда профиль не распадается
   в сумму углового и нормального (пример W3: без свободного нормального веса строгий выход
   нарушается, это видно и численно).
3. **Трубка** (теорема C; аналог Mc): эффективный потенциал постоянен на всей замкнутой кривой.
4. **Каскад** (теорема D; аналог Md): узкий угловой овраг по лемме V и нормальный профиль
   $e^{2r'}M$ на точной ветви постоянной кратности или на достаточно точном приближённом дне.
   Если на ветви $G\equiv0$, нужен ровно один шаг уточнения (теорема Z).
5. **Полнота разбора** при условии (UR): все точки глобального минимума в нормальном слое лежат на
   конечном числе аналитических ветвей постоянной кратности (теорема M′).

### 0.2. Таблица

| № | Утверждение | Статус |
|---|---|---|
| Л. A0 | компонента-кривая с постоянной нормальной кратностью аналитична; условие (M) | [Доказано] |
| Л. T, пр. R′ | $0$ не минимум ⇒ (P) точечная компонента с отрицательным старшим коэффициентом, или (W) $\min G_{\min}<0$, или (Z) $\min G_{\min}=0$ и $F_{\rm fl}<0$ при сколь угодно малых $s$ | [Доказано] |
| Т. W | широкий овраг: общий профиль с изолированным нулём и диагональным полем Эйлера, $\kappa=\kappa(\delta)$, нормальный вес $c_2(\kappa)\le c$, дно — ряд Пюизё | [Доказано] |
| Т. C | постоянный эффективный потенциал на всей кривой, вырожденный нормальный профиль | [Доказано] |
| Т. D | каскад: узкий угловой овраг, нормальный профиль $e^{2r'}M$ (точная ветвь или условие (D2)) | [Доказано] |
| Л. B, B′, U | глобальные ветви; (R) ⇒ (UR) | [Доказано] |
| Пр. W′ | случай (W) при (CM) или (DE) в точке минимального дна, или (CM) на всём минимальном дне | [Доказано] |
| Т. Z | случай (Z) при (UR) | [Доказано] |
| **Т. M′** | $n=3$, (H1)–(H4), (UR) на кривых, $0$ — не локальный минимум ⇒ асимптотическая траектория; изолированность не нужна | [Доказано] |
| Сл. M′$_R$ | то же при проверяемом условии (R); при $r\equiv1$ — теорема M [010] | [Доказано] |
| (O1)–(O3) | расщепление ветви без диагонального поля Эйлера; складки минимального дна; каскад с нежёстким вырожденным профилем | открыто; [Гипотеза] траектория есть |
| §10 | примеры W1–W4, C1, C2, D1–D3 (условия теорем выполнены), O2 (складка, вне теорем) | выкладки [Доказано] вручную; проверка — [Эксперимент] |

Все [Доказано] опираются на [007], [008], [010], [011] (проверены агентами, ждут проверки человеком).

## 1. Постановка и обозначения

### 1.1. Условия (H)

$n=3$, $B_r=\{|q|<r\}$, система $\ddot q=-\nabla U(q)$. **Асимптотическая траектория** — решение $q(t)\ne0$,
$t\ge0$, с $q(t)\to0$, $\dot q(t)\to0$ при $t\to+\infty$; из её существования следует неустойчивость по
Ляпунову ([007], теорема A, шаг 6). Обозначения $p,h,v_\perp,K_\perp,W,V,\lambda,\Xi$, условия (D1)–(D4), (A4),
(A5), (L0)–(L3) — как в [007].

- **(H1)** $U$ вещественно-аналитична в окрестности $0$, $U(0)=0$, $U=\sum_{k\ge m}u_k$ ($u_k$ — однородные
  многочлены), $m\ge2$, $u_m\ge0$, $u_m\not\equiv0$. Тогда $m$ чётно, $\nabla U(0)=0$, $Z:=\{u_m=0\}=\{\nabla u_m=0\}$.
- **(H2)** $\Sigma:=Z\cap S^2$ — гладкое ($C^\infty$) компактное подмногообразие $S^2$. Его компонент конечное
  число: точки и замкнутые кривые.
- **(H3)** В каждой точечной компоненте $\{\omega\}$: $D^2u_m(\omega)|_{\omega^\perp}\succ0$ (как в теореме K0 [008]).
- **(H4)** Для каждой компоненты-кривой $\Sigma_0$ есть $r=r(\Sigma_0)\in\mathbb N$ такое, что около $\Sigma_0$ на $S^2$
  выполнено $u_m=\tau^{2r}g$, где $\tau$, $g$ — $C^\infty$-функции, $\tau|_{\Sigma_0}=0$, $d\tau\ne0$ на $\Sigma_0$, $g>0$.

Число $r$ может зависеть от компоненты. При $r\equiv1$ (H4) — это условие Морса–Ботта (K2) [010].
Изолированность критической точки $0$ не предполагается.

### 1.2. Данные на компоненте-кривой

Пусть $\Sigma_0$ — компонента-кривая. По лемме A0 (§2) она аналитична; $\omega:\mathbb R\to\Sigma_0$ — натуральная
$L$-периодическая аналитическая параметризация, $\ell=\omega'$, $n=\omega\times\ell$, $k_g$ — геодезическая
кривизна, $\bar k_g:=\max|k_g|$:
$$\omega'=\ell,\qquad\ell'=-\omega+k_gn,\qquad n'=-k_g\ell. \tag{1.1}$$
$\Pi(s,\theta,\eta)=s\omega(\theta)+\eta n(\theta)$ — аналитический диффеоморфизм $\{s>0,\ \theta\in\mathbb R/L\mathbb Z,\ |\eta|<t_1s\}$ на
открытое подмножество $\mathbb R^3\setminus0$, $|\Pi|^2=s^2+\eta^2$, $\nabla s=\omega(\theta)$ (лемма K3 [008] для замкнутой
кривой; [010], лемма N, (N3)). Далее:

- $\varphi(s,\theta,y):=\sum_{k\ge m}s^{k-m}u_k(\omega(\theta)+yn(\theta))$ аналитична на $(-R_0/3,R_0/3)\times\mathbb R\times(-1,1)$,
  $L$-периодична, и $U(s(\omega+yn))=s^m\varphi(s,\theta,y)$ ([008], (1.1));
- $\varphi_{il}(\theta):=\frac1{i!\,l!}\partial_s^i\partial_y^l\varphi(0,\theta,0)$, носитель $\mathcal S:=\{(i,l):\ \varphi_{il}\not\equiv0\}$. По (M) (лемма A0)
  $(0,l)\notin\mathcal S$ при $l<2r$ и $\varphi_{0,2r}=a(\cdot,0)>0$;
- если $\mathcal S\cap\{l<2r\}\ne\varnothing$, то **первое ребро** ([011], утверждение 1): $\gamma_*:=\min\{\frac i{2r-l}:\ (i,l)\in\mathcal S,\ l<2r\}>0$,
  $N$ — знаменатель $\gamma_*$, $j:=m+2r\gamma_*$, $c:=1+\gamma_*$,
  $$\Phi_0(\theta,\varepsilon):=\sum_{(i,l)\in\mathcal S,\ i+\gamma_*l=2r\gamma_*}\varphi_{il}(\theta)\,\varepsilon^l=a(\theta,0)\varepsilon^{2r}+\sum_{l<2r}\varphi_{\gamma_*(2r-l),l}(\theta)\varepsilon^l, \tag{1.2}$$
  многочлен по $\varepsilon$ степени $2r$ с аналитическими $L$-периодическими коэффициентами и старшим
  коэффициентом $a(\theta,0)>0$; $G_{\min}(\theta):=\min_\varepsilon\Phi_0(\theta,\varepsilon)$ — непрерывная периодическая функция;
- **дно уровня $c_0$**: $F_{c_0}:=\{(\theta,\varepsilon):\ \Phi_0(\theta,\varepsilon)=G_{\min}(\theta)=c_0\}$; **минимальное дно** $F_{\min}:=F_{\min G_{\min}}$
  (непусто; каждая его точка — точка глобального минимума $\Phi_0(\theta,\cdot)$).

**Лемма N1 на окружности** ([011]; ряд $\tilde U$ имеет периодические коэффициенты, так что
утверждения на $\Lambda=[0,L]$ переносятся на $\mathbb R$). Для каждого $E'>0$ есть $\sigma_1>0$ такое, что
$$\tilde U(\sigma,\theta,\varepsilon):=\sum_{(i,l)\in\mathcal S}\varphi_{il}(\theta)\,\sigma^{N(i+\gamma_*l-2r\gamma_*)}\varepsilon^l$$
вещественно-аналитична в окрестности $[-\sigma_1,\sigma_1]\times\mathbb R\times[-E',E']$, $L$-периодична, $\tilde U(0,\cdot)=\Phi_0$ и
$$U\big(s\omega(\theta)+s^c\varepsilon\,n(\theta)\big)=s^j\,\tilde U(s^{1/N},\theta,\varepsilon),\qquad 0<s<\sigma_1^N,\ |\varepsilon|\le E'. \tag{1.3}$$

**Лемма N2 на окружности** ([011], включая пп. 3–5 доказательства). Есть $y_2\in(0,1)$, $E_0\le E$ ($E\ge1$) и
$C$ такие, что для каждого $y_1\in(0,y_2]$ есть $s_2(y_1)>0$, и при $0<s<s_2(y_1)$, $\theta\in\mathbb R$:
(a) все точки глобального минимума $\Phi_0(\theta,\cdot)$ лежат в $(-E_0,E_0)$; (b) все точки минимума $\varphi(s,\theta,\cdot)$ на
$|y|\le y_1$ лежат в $|y|\le Es^{\gamma_*}$, и $\min_{|y|\le y_1}\varphi=s^{2r\gamma_*}\min_{|\varepsilon|\le E}\tilde U(s^{1/N},\theta,\varepsilon)$; (c) **функция дна**
$$F_{\rm fl}(s,\theta):=\min_{|\eta|\le y_1s}U\big(s\omega(\theta)+\eta n(\theta)\big)=s^j\big(G_{\min}(\theta)+O(s^{1/N})\big)\quad\text{равномерно по }\theta. \tag{1.4}$$
Ниже $\tilde U$ рассматривается на $|\varepsilon|\le E+1$ (то есть $E'=E+1$).

Если $\mathcal S\cap\{l<2r\}=\varnothing$, пишем $\gamma_*=\infty$; тогда $\varphi=y^{2r}A(s,\theta,y)$, $A$ аналитична, $A(0,\theta,0)=a(\theta,0)>0$.

### 1.3. Условия на ветви

- **(CM)** (постоянная кратность) в точке $(\theta',\varepsilon')$ с $\partial_\varepsilon\Phi_0(\theta',\varepsilon')=0$: есть $\rho>0$, $r'\in\mathbb N$,
  аналитические $\varepsilon_b$ на $(\theta'-\rho,\theta'+\rho)$ и $\mathsf p$ на $(\theta'-\rho,\theta'+\rho)\times(-\rho,\rho)$ такие, что
  $\varepsilon_b(\theta')=\varepsilon'$, $\mathsf p(\theta,0)>0$ и
  $$\Phi_0\big(\theta,\varepsilon_b(\theta)+e\big)=G_b(\theta)+e^{2r'}\mathsf p(\theta,e),\qquad G_b(\theta):=\Phi_0(\theta,\varepsilon_b(\theta)). \tag{1.5}$$
  Проверка: если $\varepsilon'$ — критическая точка кратности $2r'-1$ с $\partial_\varepsilon^{2r'}\Phi_0(\theta',\varepsilon')>0$, то $\varepsilon_b$ — простой корень
  $\partial_\varepsilon^{2r'-1}\Phi_0(\theta,\cdot)$ через $\varepsilon'$ (теорема о неявной функции), и (CM) равносильно тождествам
  $\partial_\varepsilon^k\Phi_0(\theta,\varepsilon_b(\theta))\equiv0$, $1\le k\le2r'-2$. Из (1.5): при малом $\rho'$ единственная критическая точка $\Phi_0(\theta,\cdot)$ в
  $|\varepsilon-\varepsilon_b(\theta)|<\rho'$ — это $\varepsilon_b(\theta)$, так как $\partial_e(e^{2r'}\mathsf p)=e^{2r'-1}(2r'\mathsf p+e\partial_e\mathsf p)\ne0$ при $0<|e|<\rho'$.
- **(DE)** (диагональное поле Эйлера) в точке $(\theta_0,\varepsilon_0)\in F_{\min}$: для $P(\tau,e):=\Phi_0(\theta_0+\tau,\varepsilon_0+e)-\min G_{\min}$
  (так что $P\ge0$ на $\mathbb R^2$, $P(0,0)=0$):
  - (W1) $(0,0)$ — изолированный нуль $P$;
  - (DE) есть $w,\mu_0,r_*>0$ с $\tau\partial_\tau P+w\,e\,\partial_eP\ge\mu_0P$ на $[-r_*,r_*]^2$.
- **(UR)** (равномерная регулярность дна) на $\Sigma_0$ с $\gamma_*<\infty$: для каждого $\theta'\in\mathbb R$ есть открытый интервал
  $J\ni\theta'$, числа $\sigma_J,e_J>0$ и конечный набор «ветвей» $(\varepsilon_k^*,\hat G_k,M_k,r_k)$, $k=1,\dots,K$:
  $\varepsilon_k^*,\hat G_k$ вещественно-аналитичны на $(-\sigma_J,\sigma_J)\times J$ со значениями $|\varepsilon_k^*|<E+\frac12$, $M_k$
  вещественно-аналитична на $(-\sigma_J,\sigma_J)\times J\times(-e_J,e_J)$, $e_J\le\frac12$, $r_k\in\mathbb N$, причём
  - (UR1) $\tilde U(\sigma,\theta,\varepsilon_k^*+e)=\hat G_k(\sigma,\theta)+e^{2r_k}M_k(\sigma,\theta,e)$ и $M_k(0,\theta,0)>0$;
  - (UR2) при $\theta\in J$, $0\le\sigma<\sigma_J$ каждая точка глобального минимума $\tilde U(\sigma,\theta,\cdot)$ на $[-E,E]$ равна
    $\varepsilon_k^*(\sigma,\theta)$ при некотором $k$.

  (UR1) означает, что $\varepsilon_k^*$ — точная ветвь критических точек **постоянной кратности** $2r_k-1$ («жёсткий
  профиль»); при $\sigma=0$ это (CM). Точки глобального минимума $\Phi_0(\theta,\cdot)$ на $\mathbb R$ лежат в $(-E_0,E_0)\subset[-E,E]$,
  так что (UR2) при $\sigma=0$ относится к ним всем.
- **(R)** (невырожденность минимального дна в слое): при каждом $\theta\in\mathbb R$ каждая точка глобального
  минимума $\varepsilon$ функции $\Phi_0(\theta,\cdot)$ невырождена: $\partial_\varepsilon^2\Phi_0(\theta,\varepsilon)>0$. Это условие на многочлен первого
  ребра; оно проверяется по конечной струе $U$.

## 2. Утверждения

### Лемма A0 (аналитичность кривой и условие (M))

**Лемма A0.** При (H1), (H2), (H4) каждая компонента-кривая $\Sigma_0$ — вещественно-аналитическая
замкнутая кривая, и в обозначениях §1.2
$$u_m\big(\omega(\theta)+y\,n(\theta)\big)=y^{2r}a(\theta,y),\qquad a(\theta,0)>0, \tag{M}$$
где $a$ — многочлен по $y$ с аналитическими $L$-периодическими коэффициентами.

### Лемма T и предложение R′ (разбор случаев)

**Лемма T.** Пусть выполнены (H1)–(H4). Для каждой компоненты-кривой с $\gamma_*<\infty$ выберем
$y_1\le\min(y_2,t_1)$ и $s_1:=\min(s_2(y_1),R_0/3)$; для компоненты с $\gamma_*=\infty$ — $y_1\le\min(y',t_1)$ и $s_1:=\min(s',R_0/3)$,
где $A\ge\frac12\min a(\cdot,0)>0$ при $|s|\le s'$, $|y|\le y'$ (так можно по компактности и периодичности). **Трубка** —
$T(\Sigma_0):=\{s\omega(\theta)+\eta n(\theta):\ 0<s<s_1,\ \theta\in\mathbb R,\ |\eta|<y_1s\}$, функция дна $F_{\rm fl}$ — как в (1.4) с этим $y_1$.
Для точечной компоненты $\{\omega\}$ $C_\omega$ — конус и $R_\omega(s)$ — функция $R$ данных (S) [008] с $d=0$ (как в
предложении K4 [008]). Тогда:

- **(a)** есть $r_*>0$ такое, что каждая точка $0<|q|<r_*$ лежит в некоторой трубке $T(\Sigma_0)$, или в некотором
  конусе $C_\omega$, или $U(q)>0$;
- **(b)** на $T(\Sigma_0)$: $U(s\omega(\theta)+\eta n(\theta))\ge F_{\rm fl}(s,\theta)$; на $C_\omega$: $U(q)\ge x^mR_\omega(x)$, $x=\langle q,\omega\rangle$;
- **(c)** $0$ — точка локального минимума $U$ тогда и только тогда, когда $F_{\rm fl}(s,\theta)\ge0$ при малых $s>0$ на всех
  компонентах-кривых и $R_\omega(s)\ge0$ при малых $s>0$ во всех точечных компонентах.

**Предложение R′.** Пусть выполнены (H1)–(H4) и $0$ — не точка локального минимума $U$. Тогда $\Sigma\ne\varnothing$
и выполнено хотя бы одно из трёх:

- **(P)** есть точечная компонента $\{\omega\}$ с $R_\omega\not\equiv0$ и отрицательным старшим коэффициентом $R_\omega$;
- **(W)** есть компонента-кривая с $\gamma_*<\infty$ и $\min G_{\min}<0$;
- **(Z)** есть компонента-кривая с $\gamma_*<\infty$, $\min G_{\min}=0$ и точками $(s_n,\theta_n)$, $s_n\downarrow0$, с $F_{\rm fl}(s_n,\theta_n)<0$.

### Теорема W (широкий овраг; аналог Mb)

**Данные (NF$_W$).** $\omega:(-\theta_K,\theta_K)\to S^2$ — натуральная параметризация аналитической дуги (в том
числе дуги замкнутой кривой), репер (1.1); $\theta_1\in(0,\theta_K)$ и $t_1>0$ такие, что $\Pi$ — диффеоморфизм
$\{s>0,\ |\theta|<\theta_1,\ |\eta|<t_1s\}$ на открытое множество (лемма K3 [008]). Числа $N\in\mathbb N$, $c>1$, $\beta>0$,
$\sigma_1>0$ и функции:

- $y_0\in C^2([0,\sigma_1]\times[-\theta_1,\theta_1])$ с $y_0(0,\cdot)\equiv0$; $\eta_0(s,\theta):=s\,y_0(s^{1/N},\theta)$ — **приближённое дно**;
- $\tilde F:[0,\sigma_1]\times[-\theta_1,\theta_1]\times[-1,1]\to\mathbb R$, непрерывная вместе с $\partial_\theta\tilde F$, $\partial_e\tilde F$, дифференцируемая по
  $\sigma$ при $\sigma>0$, с $\sup_{\theta,e}|\sigma\partial_\sigma\tilde F(\sigma,\theta,e)|\to0$ при $\sigma\to0$;

и
$$U\big(s\omega(\theta)+(\eta_0(s,\theta)+s^ce)\,n(\theta)\big)=s^\beta\tilde F(s^{1/N},\theta,e),\qquad0<s\le\sigma_1^N,\ |\theta|\le\theta_1,\ |e|\le1. \tag{2.1}$$

**Профиль (W).** $\tilde F(0,\theta,e)=-a_0+P(\theta,e)$, $a_0>0$, и для некоторого $r_W\in(0,\min(\theta_1/2,\frac14)]$, $K:=[-r_W,r_W]^2$:

- **(W1)** $P\ge0$ на $K$, и на $K$ $P$ обращается в нуль только в $(0,0)$;
- **(W2)** есть $\mu_0>0$, $\kappa_0\in(0,\frac12]$ и функция $c_2:(0,\kappa_0]\to(0,c]$ такие, что при всех $\kappa\in(0,\kappa_0]$
  $$\kappa\,\theta\,\partial_\theta P+c_2(\kappa)\,e\,\partial_eP\ \ge\ \kappa\mu_0P\quad\text{на }K. \tag{2.2}$$

Типичные выборы: $c_2\equiv c$ — профиль «распадается» (так в теореме Mb [010] и в теореме N [011]);
$c_2(\kappa)=w\kappa$ при $\kappa_0\le c/w$ — условие (DE) с весом $w$ (§1.3).

**Теорема W.** Пусть $U\in C^2(B_r)$, $U(0)=0$, $\nabla U(0)=0$, выполнены (NF$_W$) и (W). Положим
$\Omega_\delta:=\{(\theta,e)\in(-r_W,r_W)^2:\ P<4\delta\}$, $R_\theta(\delta):=\sup_{\Omega_\delta}|\theta|$, $R_e(\delta):=\sup_{\Omega_\delta}|e|$ (тогда
$0<R_\theta(\delta)\to0$ и $R_e(\delta)\to0$ при $\delta\to0$), $C_M:=\frac{15\sqrt3}8\beta+4$ и
$$\kappa(\delta):=\min\Big\{\kappa_0,\ \frac\beta{4\mu_0},\ \frac{\mu_0\beta\,\delta}{2C_M^2a_0R_\theta(\delta)^2}\Big\}. \tag{2.3}$$
Тогда есть $\delta_1>0$ такое, что для каждого $\delta\in(0,\delta_1]$ существует асимптотическая траектория
$$q(t)=s\,\omega(\theta)+\big(\eta_0(s,\theta)+s^ce\big)\,n(\theta),\qquad s=s(t)\downarrow0,\quad-k_2s^{\beta/2}\le\dot s\le-k_1s^{\beta/2}\ (0<k_1\le k_2),$$
с $(\theta(t),e(t))\in\overline{\Omega_\delta}$; в частности, $|\theta(t)|\le R_\theta(\delta)$, $|e(t)|\le R_e(\delta)$. Равновесие неустойчиво по Ляпунову.
Траектория строится по теореме A [007] через лемму M [010] с $\rho=s$, $A(\rho)=a_0\rho^\beta$ и полем
$$Y=\Psi_s-\frac{\kappa\theta}s\Psi_\theta+\lambda\frac\zeta s\Psi_\zeta,\qquad\kappa=\kappa(\delta),\quad\lambda:=c-c_2(\kappa)\in[0,c), \tag{2.4}$$
в координатах $(s,\theta,\zeta)$ карты $\Psi(s,\theta,\zeta):=s\omega(\theta)+(\eta_0(s,\theta)+\zeta)n(\theta)$. Ни аналитичность $U$, ни
изолированность критической точки не предполагаются.

### Теорема C (трубка; аналог Mc)

**Данные (NF$_C$).** $\Sigma_0$ — замкнутая аналитическая кривая длины $L$, натуральный $L$-периодический
параметр; числа $N$, $c>1$, $\beta>0$, $\sigma_1>0$; $y_0\in C^2([0,\sigma_1]\times\mathbb R)$, $L$-периодическая по $\theta$,
$y_0(0,\cdot)\equiv0$; $\tilde F$ на $[0,\sigma_1]\times\mathbb R\times[-1,1]$, $L$-периодическая по $\theta$, с теми же свойствами
регулярности, что в (NF$_W$), и тождество (2.1) при всех $\theta\in\mathbb R$.

**Профиль (C).** $\tilde F(0,\theta,e)=-a_0+P(\theta,e)$, $a_0>0$, и для некоторого $e_C\in(0,1]$:

- **(C1)** $P(\theta,0)=0$ и $P(\theta,e)\ge q_0(|e|)$ при $\theta\in\mathbb R$, $|e|\le e_C$, где $q_0$ непрерывна на $[0,e_C]$ и $q_0(t)>0$ при $t>0$;
- **(C2)** $e\,\partial_eP\ge\mu_0P$ при $\theta\in\mathbb R$, $|e|\le e_C$, где $\mu_0>0$.

**Теорема C.** Пусть $U\in C^2(B_r)$, $U(0)=0$, $\nabla U(0)=0$, выполнены (NF$_C$) и (C). Тогда для каждого
достаточно малого $\delta>0$ есть асимптотическая траектория $q(t)=s\omega(\theta)+(\eta_0(s,\theta)+s^ce)n(\theta)$,
$\theta\in\mathbb R/L\mathbb Z$, $s(t)\downarrow0$, $-k_2s^{\beta/2}\le\dot s\le-k_1s^{\beta/2}$, $|e(t)|\le R_e(\delta):=\sup\{|e|:\ |e|<e_C,\ P<4\delta\}\to0$. Она
строится по теореме A [007] через лемму 2 [007] с $\rho=s$, $Y=\Psi_s$ (поле (2.4) при $\kappa=\lambda=0$) в трубке
вокруг всего конуса; об угле $\theta(t)$ ничего не утверждается.

### Теорема D (каскад; аналог Md)

**Данные (ND).** Аналитическая дуга $\omega$ около $\theta=0$ (натуральный параметр), $\theta_1,t_1$ — как в (NF$_W$);
$N\in\mathbb N$, $c>1$, $\beta>0$, $\sigma_J>0$, $e_J\in(0,1]$, $r'\in\mathbb N$; вещественно-аналитические $y_0$ на
$(-\sigma_J,\sigma_J)\times(-\theta_1,\theta_1)$ с $y_0(0,\cdot)\equiv0$ и $\tilde F$ на $(-\sigma_J,\sigma_J)\times(-\theta_1,\theta_1)\times(-e_J,e_J)$ с тождеством
(2.1) при $0<s<\sigma_J^N$, $|\theta|<\theta_1$, $|e|<e_J$. По формуле Тейлора по $e$
$$\tilde F(\sigma,\theta,e)=\hat G(\sigma,\theta)+\sum_{l=1}^{2r'-1}h_l(\sigma,\theta)\,e^l+e^{2r'}M(\sigma,\theta,e), \tag{2.5}$$
$\hat G=\tilde F(\cdot,\cdot,0)$, $h_l=\frac1{l!}\partial_e^l\tilde F(\cdot,\cdot,0)$, $M$ аналитична (интегральный остаток). Предполагается
$M_0:=M(0,0,0)>0$.

- **(D1)** $G:=\hat G(0,\cdot)\ge0$ около $0$, $G(0)=0$, $G\not\equiv0$ около $0$, и $\hat G(\sigma_k,\theta_k)<0$ для некоторых $\sigma_k\downarrow0$,
  $\theta_k\to0$.
- **(D2)** Для некоторых данных $(N_V,A_V,\Gamma_V,a_V,T,Q_V,k_0)$ леммы V [010] для $f(\sigma,\tau):=\hat G(\sigma,\tau)$ (в лемме V
  это $N,A_V,\Gamma_V,a_V,T,Q_V,k_0$), у которых $2r'$ делит $\Gamma_V$ (этого всегда можно добиться заменой
  $t\mapsto t^{r'}$, §7, п. 1), с $B:=\Gamma_V/(2r')$: при каждом $1\le l\le2r'-1$ в разложении
  $h_l(t^{N_V},T(t)+t^{A_V}b_1)=\sum_{i\ge0}H_{l,i}(b_1)t^i$ коэффициенты с $i\le\Gamma_V-lB$ равны нулю тождественно по $b_1$.

(D2) выполнено, если $h_l\equiv0$ (точная ветвь постоянной кратности, «жёсткий профиль»), а также если
$h_l=\sigma^{\nu_l}\tilde h_l$ с аналитическими $\tilde h_l$ и $N_V\nu_l>\Gamma_V-lB$.

**Теорема D.** Пусть $U\in C^2(B_r)$, $U(0)=0$, $\nabla U(0)=0$, выполнены (ND), (D1), (D2). Положим
$$\alpha:=\frac{A_V}{NN_V},\quad\gamma':=\frac{\Gamma_V}{NN_V},\quad\beta_d:=\beta+\gamma',\quad c_1:=1+\alpha,\quad c':=c+\frac{\gamma'}{2r'},\quad\tau_v(x):=T(x^{1/(NN_V)}).$$
Тогда при подходящих $s_0,r_0>0$ карта
$$\Phi(x,u,\zeta):=\Psi\big(x,\ \tau_v(x)+u/x,\ \zeta\big),\qquad b=(b_1,b_2)=\big(u\,x^{-c_1},\ \zeta\,x^{-c'}\big), \tag{2.6}$$
($\Psi$ — как в теореме W) задаёт принадлежность $U$ классу (GT3) [007] с $n=3$, показателем $\beta_d$, весами
$(c_1,c')$, числом $NN_V$ вместо $N$, $C_1=0$ и условием $(V_0)$. По теореме 2 [007] есть асимптотическая
траектория $q(t)=\Phi(x(t),u(t),\zeta(t))$, $x(t)\downarrow0$, $-k_2x^{\beta_d/2}\le\dot x\le-k_1x^{\beta_d/2}$ (при $\beta_d>2$ отсюда
$x(t)\asymp t^{-2/(\beta_d-2)}$; в применениях §9 $\beta_d>j>m\ge2$), касающаяся луча: $q(t)/|q(t)|\to\omega(0)$.

### Леммы о ветвях

**Лемма B (глобальная ветвь первого ребра).** Пусть $\gamma_*<\infty$, $c_0:=\min_\theta G_{\min}$, и (CM) выполнено в
каждой точке $F_{c_0}$. Если в точке $(\theta_0,\varepsilon_0)\in F_{c_0}$ ветвь $\varepsilon_b$ из (CM) имеет $G_b\equiv c_0$ около $\theta_0$, то
есть аналитическая $L$-периодическая $\varepsilon_g:\mathbb R\to\mathbb R$ с $\varepsilon_g(\theta_0)=\varepsilon_0$ и $(\theta,\varepsilon_g(\theta))\in F_{c_0}$ при всех $\theta$, число
$r'\in\mathbb N$, $e_g>0$ и аналитическая $L$-периодическая $\mathsf p_g$ на $\mathbb R\times(-e_g,e_g)$ с $\mathsf p_g(\theta,0)>0$ и
$\Phi_0(\theta,\varepsilon_g(\theta)+e)=c_0+e^{2r'}\mathsf p_g(\theta,e)$.

**Лемма U.** Если на компоненте-кривой с $\gamma_*<\infty$ выполнено (R), то выполнено (UR) со всеми $r_k=1$.

**Лемма B′ (глобальная ветвь при (UR)).** Пусть на компоненте-кривой выполнено (UR), $c_0:=\min G_{\min}$, и
для ветви $k$ на интервале $J\ni\theta_0$ функция $G_k:=\hat G_k(0,\cdot)$ тождественно равна $c_0$ около $\theta_0$. Тогда есть
$\sigma_0,e_0>0$, $r_g\in\mathbb N$ и вещественно-аналитические $L$-периодические по $\theta$ функции $\varepsilon_g^*,\hat G_g$ на
$(-\sigma_0,\sigma_0)\times\mathbb R$ и $M_g$ на $(-\sigma_0,\sigma_0)\times\mathbb R\times(-e_0,e_0)$ такие, что $\tilde U(\sigma,\theta,\varepsilon_g^*+e)=\hat G_g+e^{2r_g}M_g$,
$M_g(0,\theta,0)>0$, $\hat G_g(0,\cdot)\equiv c_0$, и $(\varepsilon_g^*,\hat G_g,M_g,r_g)=(\varepsilon_k^*,\hat G_k,M_k,r_k)$ около $(0,\theta_0)$.

### Сборка

**Предложение W′ (случай (W)).** Пусть выполнены (H1)–(H4) и на компоненте-кривой $\Sigma_0$ $\gamma_*<\infty$,
$\min G_{\min}=-a_0<0$. Если выполнено хотя бы одно из условий

- **(W-a)** в некоторой точке $(\theta_0,\varepsilon_0)\in F_{\min}$ выполнено (CM) и $G_b\not\equiv-a_0$ около $\theta_0$;
- **(W-b)** в некоторой точке $(\theta_0,\varepsilon_0)\in F_{\min}$ выполнены (W1) и (DE);
- **(W-c)** (CM) выполнено во всех точках $F_{\min}$,

то есть асимптотическая траектория. При (W-a) и (W-b) она строится теоремой W около луча $\omega(\theta_0)$, при (W-c) —
теоремой W или теоремой C.

**Теорема Z (случай (Z)).** Пусть выполнены (H1)–(H4), на компоненте-кривой $\Sigma_0$ $\gamma_*<\infty$,
$\min G_{\min}=0$, $F_{\rm fl}(s_n,\theta_n)<0$ при некоторых $s_n\downarrow0$, и на $\Sigma_0$ выполнено (UR). Тогда есть
асимптотическая траектория; она строится теоремой D, а если ветвь, на которой $F_{\rm fl}<0$, имеет $G_k\equiv0$, —
после одного шага уточнения теоремой D, W или C.

**Теорема M′.** Пусть $n=3$, выполнены (H1)–(H4), и на каждой компоненте-кривой с $\gamma_*<\infty$ выполнено
(UR). Если $0$ — не точка локального минимума $U$, то у $\ddot q=-\nabla U(q)$ есть асимптотическая траектория,
и равновесие $q=0$ неустойчиво по Ляпунову. Изолированность критической точки не предполагается.

**Следствие M′$_R$.** В теореме M′ условие (UR) можно заменить условием (R) (лемма U). В частности, при
$r(\Sigma_0)=1$ для всех кривых (Морс–Ботт) условие (R) выполнено автоматически: $\Phi_0$ — квадратный
трёхчлен со старшим коэффициентом $a(\theta,0)>0$. Получается теорема M [010], доказанная другим путём:
через первое ребро и не более одного шага уточнения.

**Замечание.** В доказательстве используется (UR) только на той компоненте, которую даёт
предложение R′. В случае (W) достаточно условий предложения W′, они слабее (UR).

## 3. Доказательство леммы A0

1. *Аналитичность.* Пусть $\omega^*\in\Sigma_0$; $\chi(\xi):=(\omega^*+\xi)/|\omega^*+\xi|$ — аналитическая карта сферы около
   $\omega^*$ ($\xi\in T_{\omega^*}S^2\cong\mathbb R^2$ мало), $F:=u_m\circ\chi$, $\tilde\tau:=\tau\circ\chi$, $\tilde g:=g\circ\chi$, $C_0:=\chi^{-1}(\Sigma_0)$ — $C^\infty$-кривая
   через $0$. Возьмём постоянное векторное поле $X$ на $T_{\omega^*}S^2$, трансверсальное к $C_0$ в $0$. Так как
   $d\tilde\tau\ne0$ и $d\tilde\tau$ обращается в нуль на $T_0C_0$, имеем $X\tilde\tau(0)\ne0$. По (H4) $F=\tilde\tau^{2r}\tilde g$. По формуле
   Лейбница $X^kF$ — сумма произведений, в каждом из которых не продифференцировано не меньше $2r-k$
   множителей $\tilde\tau$. Поэтому $X^kF=0$ на $C_0$ при $k<2r$, а $X^{2r}F=(2r)!\,(X\tilde\tau)^{2r}\tilde g\ne0$ в $0$. Функция
   $H:=X^{2r-1}F$ аналитична, равна нулю на $C_0$ и $XH(0)\ne0$. По аналитической теореме о неявной функции
   $\{H=0\}$ около $0$ — аналитическая кривая. Она содержит связную одномерную $C^\infty$-кривую $C_0$ и потому
   совпадает с ней около $0$. Итак, $\Sigma_0$ — аналитическое подмногообразие, его натуральная параметризация и
   репер аналитичны.
2. *(M).* Вывод — как в записке к [011] (§1.3 записки `notes/prover/2026-10-21-normal-multiplicity.md`).
   Пусть $E(\theta,y):=(\omega+yn)/\sqrt{1+y^2}$; тогда $u_m(\omega+yn)=(1+y^2)^{m/2}(\tau^{2r}g)(E(\theta,y))$. Далее $\tau(E(\theta,0))=0$, а
   $\partial_y\tau(E(\theta,y))|_{y=0}=d\tau(n)\ne0$: $n(\theta)\in T_\omega S^2$ трансверсален $\Sigma_0$. Поэтому $\tau(E(\theta,y))=y\tau_1(\theta,y)$ с
   $\tau_1(\theta,0)\ne0$, и $u_m(\omega+yn)=y^{2r}a$ с $a(\theta,0)=\tau_1(\theta,0)^{2r}g(\omega(\theta))>0$. Левая часть — многочлен по $y$
   (степени $m$) с аналитическими периодическими коэффициентами. Его коэффициенты при $y^l$, $l<2r$,
   равны нулю (они равны производным по $y$ в нуле), так что $a$ — многочлен по $y$. $\square$

## 4. Доказательство леммы T и предложения R′

**Лемма T.**

1. *(a).* Множества $O(\Sigma_0):=E\big(\mathbb R\times(-y_1,y_1)\big)\subset S^2$ ($E$ — как в §3, п. 2; $E$ — локальный
   диффеоморфизм, так как $\partial_\theta E$, $\partial_yE$ при $y=0$ равны $\ell$, $n$) и $C_\omega\cap S^2$ открыты и содержат
   соответствующие компоненты $\Sigma$. Множество $A:=S^2\setminus\big(\bigcup O(\Sigma_0)\cup\bigcup(C_\omega\cap S^2)\big)$ компактно и не
   пересекает $\Sigma$, поэтому $u_m\ge c_*>0$ на $A$. Для $q$ с $q/|q|\in A$ имеем $U(q)\ge c_*|q|^m-C|q|^{m+1}>0$ при $|q|<c_*/C$.
   Если $q/|q|=E(\theta,t)$, $|t|<y_1$, то $q=s\omega(\theta)+\eta n(\theta)$ с $s=|q|/\sqrt{1+t^2}\in(0,|q|]$, $\eta=ts$, $|\eta|<y_1s$, и при $|q|<s_1$
   $q\in T(\Sigma_0)$. Если $q/|q|\in C_\omega$, то $q\in C_\omega$. Возьмём $r_*$ меньше $c_*/C$, всех $s_1$ и радиусов,
   на которых действуют конусы $C_\omega$ (как в доказательстве K4(c) [008], §11).
2. *(b).* В трубке $0<s<s_1\le R_0/3$, $|\eta/s|<y_1$, поэтому $U(s\omega+\eta n)=s^m\varphi(s,\theta,\eta/s)\ge s^m\min_{|y|\le y_1}\varphi=F_{\rm fl}(s,\theta)$.
   Для конусов — [008], §11, доказательство K4(c) (лемма K1, п. 2).
3. *(c).* «⇐»: по (a), (b) около нуля $U\ge0$. «⇒»: $F_{\rm fl}(s,\theta)$ — значение $U$ в точке нормы $\le2s$, а
   $s^mR_\omega(s)=U(s\omega+\eta^*_\omega(s))$ — значение $U$ в точке нормы $\le2s$ ([008], лемма K1). $\square$

**Предложение R′.**

1. Если $\Sigma=\varnothing$, то $u_m\ge c|q|^m$, $c>0$, и $U>0$ в проколотой окрестности: $0$ — строгий минимум.
2. По лемме T(c) есть точечная компонента и $s_n\downarrow0$ с $R_\omega(s_n)<0$ или компонента-кривая и $(s_n,\theta_n)$,
   $s_n\downarrow0$, с $F_{\rm fl}(s_n,\theta_n)<0$ (компонент конечное число).
3. *Точка.* $R_\omega$ аналитична, $R_\omega(0)=0$, $R_\omega\not\equiv0$ (иначе $R_\omega(s_n)=0$). Значит, $R_\omega(s)=g\,s^{i}(1+O(s))$, $g\ne0$, и
   $g<0$, так как $R_\omega(s_n)<0$. Это (P): $j(\omega)=m+i<\infty$, $g_{j(\omega)}(\omega)=g<0$.
4. *Кривая.* Если $\gamma_*=\infty$, то $\varphi=y^{2r}A$ и по выбору $y_1$, $s_1$ в лемме T $A>0$, так что $F_{\rm fl}\ge0$ при
   $0<s<s_1$ — противоречие. Значит, $\gamma_*<\infty$. По (1.4)
   $s_n^{-j}F_{\rm fl}(s_n,\theta_n)=G_{\min}(\theta_n)+O(s_n^{1/N})<0$. Для предельной точки $\theta_*$ последовательности $\theta_n$ (по
   модулю $L$) $G_{\min}(\theta_*)\le0$, то есть $\min G_{\min}\le0$: это (W) или (Z). $\square$

Изолированность и аналитичность $u_m$ сверх (H1) здесь не используются.

## 5. Теорема W: формулы и доказательство

### 5.1. Формулы для поля (2.4)

Обозначения: $\eta:=\eta_0+\zeta$, $\epsilon:=k_g(\theta)\eta/s$, $\nu:=\eta_{0,s}-\kappa\theta\eta_{0,\theta}/s$, $\tilde\nu:=\nu+\lambda\zeta/s$; в координатах $(s,\theta,\zeta)$
$Y=\partial_s-\frac{\kappa\theta}s\partial_\theta+\frac{\lambda\zeta}s\partial_\zeta$. Прямым дифференцированием по (1.1) [Доказано; [Эксперимент]
`frames_W.py`: все тождества символьно при общем $k_g(\theta)$ и $\eta_0=s\,y_0(s^{1/3},\theta)$ с общим многочленом $y_0$;
отрицательный контроль — при удалении членов с $\lambda$ проверки (5.4), (5.5) не проходят]:
$$\Psi_s=\omega+\eta_{0,s}n,\qquad\Psi_\theta=s(1-\epsilon)\ell+\eta_{0,\theta}n,\qquad\Psi_\zeta=n; \tag{5.1}$$
$$Y=\omega-\kappa\theta(1-\epsilon)\ell+\tilde\nu\,n,\qquad h=1+\kappa^2\theta^2(1-\epsilon)^2+\tilde\nu^2; \tag{5.2}$$
$$\partial_\theta Y=\kappa\theta(1-\epsilon)\omega+\big[1-\kappa(1-\epsilon)+\kappa\theta\partial_\theta\epsilon-\tilde\nu k_g\big]\ell+\big[-\kappa\theta(1-\epsilon)k_g+\partial_\theta\tilde\nu\big]n,\quad
\partial_sY=\kappa\theta\partial_s\epsilon\,\ell+\partial_s\tilde\nu\,n,\quad\partial_\zeta Y=\frac{\kappa\theta k_g}s\ell+\frac\lambda sn; \tag{5.3}$$
$$s\,D_YY=-\kappa^2\theta^2(1-\epsilon)\,\omega+\kappa\theta\Big[s\partial_s\epsilon-1+\kappa(1-\epsilon)-\kappa\theta\partial_\theta\epsilon+\tilde\nu k_g+\frac{\lambda k_g\zeta}s\Big]\ell+\Big[s\partial_s\tilde\nu+\kappa^2\theta^2(1-\epsilon)k_g-\kappa\theta\partial_\theta\tilde\nu+\frac{\lambda^2\zeta}s\Big]n; \tag{5.4}$$
для $w=w_\omega\omega+w_\ell\ell+w_nn=a^s\Psi_s+a^\theta\Psi_\theta+a^\zeta\Psi_\zeta$, $a^s=w_\omega$, $a^\theta=\frac{w_\ell}{s(1-\epsilon)}$, $a^\zeta=w_n-w_\omega\eta_{0,s}-\frac{w_\ell\eta_{0,\theta}}{s(1-\epsilon)}$:
$$
\begin{aligned}
s\langle w,D_wY\rangle={}&\Big(\frac1{1-\epsilon}-\kappa\Big)w_\ell^2+\kappa\theta\,w_\omega w_\ell+\frac{(\kappa\theta\partial_\theta\epsilon-\tilde\nu k_g)w_\ell^2+\partial_\theta\tilde\nu\,w_\ell w_n}{1-\epsilon}\\
&+w_\omega\big[\kappa\theta\,s\partial_s\epsilon\,w_\ell+s\partial_s\tilde\nu\,w_n\big]-\kappa\theta k_g\,w_\ell\Big(w_\omega\eta_{0,s}+\frac{w_\ell\eta_{0,\theta}}{s(1-\epsilon)}\Big)+\lambda\,a^\zeta w_n
\end{aligned} \tag{5.5}
$$
(члены $\mp\kappa\theta k_gw_\ell w_n$ из $a^\theta\partial_\theta Y$ и $a^\zeta\partial_\zeta Y$ сокращаются, как в (5.3) [010]);
$$w\perp Y\iff w_\omega=\kappa\theta(1-\epsilon)w_\ell-\tilde\nu w_n; \tag{5.6}$$
наконец, для $W:=U+a_0\rho^\beta$, $\rho=s$, $\sigma=s^{1/N}$, $e=\zeta s^{-c}$ и $c_2:=c-\lambda$
$$\beta W-\rho\,YW=s^\beta\Big[\kappa\theta\,\partial_\theta\tilde F+c_2\,e\,\partial_e\tilde F-\frac\sigma N\partial_\sigma\tilde F\Big]\quad\text{в точке }(\sigma,\theta,e). \tag{5.7}$$
Вывод (5.7). Для $g(s,\theta,\zeta):=W(\Psi(s,\theta,\zeta))=s^\beta(\tilde F(s^{1/N},\theta,\zeta s^{-c})+a_0)$ (по (2.1)):
$s\partial_sg=\beta g+s^\beta[\frac\sigma N\partial_\sigma\tilde F-ce\partial_e\tilde F]$, $-\kappa\theta\partial_\theta g=-s^\beta\kappa\theta\partial_\theta\tilde F$,
$\lambda\zeta\partial_\zeta g=s^\beta\lambda e\partial_e\tilde F$. Их сумма равна $\rho\,YW=s\,Yg$, откуда (5.7). Вспомогательные тождества:
$s\partial_s\epsilon=k_g\eta_{0,s}-\epsilon$, $\partial_\theta\epsilon=(k_g'\eta+k_g\eta_{0,\theta})/s$, $\partial_\theta\tilde\nu=\eta_{0,s\theta}-\kappa\eta_{0,\theta}/s-\kappa\theta\eta_{0,\theta\theta}/s$,
$s\partial_s\tilde\nu=s\eta_{0,ss}-\kappa\theta(\eta_{0,s\theta}-\eta_{0,\theta}/s)-\lambda\zeta/s$.

При $\lambda=0$ это формулы (2.1), (2.5), (5.1)–(5.3) [010] и (7.2)–(7.6) [011] с приближённым дном.

**Малые величины.** Положим
$$\Delta(s'):=\sup\Big\{|\epsilon|+|s\partial_s\epsilon|+|\partial_\theta\epsilon|+|\eta_{0,s}|+\frac{|\eta_{0,\theta}|}s+s|\eta_{0,ss}|+|\eta_{0,s\theta}|+\frac{|\eta_{0,\theta\theta}|}s+\frac{|\zeta|}s\Big\},$$
супремум по $0<s<s'$, $|\theta|\le\theta_1/2$, $|\zeta|\le s^c$. Тогда $\Delta(s')\to0$ при $s'\to0$. Доказательство — дословно лемма
N5 [011]: тождества для производных $\eta_0=sy_0(s^{1/N},\theta)$ через $y_0\in C^2$, $y_0(0,\cdot)\equiv0$, и $|\zeta|/s\le s^{c-1}$. Отсюда
равномерно по $\kappa\in(0,\frac12]$, $\lambda\in[0,c]$, $|\theta|\le\theta_1/2$:
$$|\tilde\nu|\le(2+c)\Delta,\qquad|\partial_\theta\tilde\nu|\le3\Delta,\qquad|s\partial_s\tilde\nu|\le(3+c)\Delta\qquad(\kappa|\theta|\le1). \tag{5.8}$$

### 5.2. Доказательство теоремы W

1. *Окно и множества $\Omega_\delta$.* По (W1) и компактности $m(\rho'):=\min\{P(\theta,e):\ (\theta,e)\in K,\ \max(|\theta|,|e|)\ge\rho'\}>0$ при
   $\rho'\in(0,r_W]$. При $4\delta<m(\rho')$ имеем $\Omega_\delta\subset(-\rho',\rho')^2$. Значит, $R_\theta(\delta),R_e(\delta)\to0$; $R_\theta(\delta)>0$, так как
   $\Omega_\delta$ — открытая окрестность нуля. Положим $\delta_0:=m(r_W/2)/8$. При $\delta\le\delta_0$ имеем $\overline{\Omega_\delta}\subset[-\frac{r_W}2,\frac{r_W}2]^2$, и
   $P=4\delta$ на $\partial\Omega_\delta$: граничная точка лежит внутри квадрата, но не в $\Omega_\delta$, откуда $P\ge4\delta$, а по
   непрерывности $P\le4\delta$.
2. *Выбор $s_2$* (до выбора $\kappa$; равномерно по $\kappa\in(0,\frac12]$, $\lambda\in[0,c]$). $s_2\in(0,\min(1,\sigma_1^N))$ такое, что
   $10(1+\bar k_g+c)\Delta(s_2)\le\frac14$ (отсюда $|\epsilon|,|\tilde\nu|\le\frac14$, $|\eta_{0,s}|+\frac43|\eta_{0,\theta}|/s\le1$, $|\eta_{0,s}k_g|\le1$), $|\eta|\le|\eta_0|+s^c\le\frac12\min(t_1,\frac14)s$
   при $0<s<s_2$ и $2s_2<r$. Тогда $\mathcal O:=\{\Psi(s,\theta,s^ce):\ 0<s<s_2,\ |\theta|<r_W,\ |e|<1\}$ — открытое подмножество
   $B_r\setminus0$, $\Psi$ на нём инъективна (лемма K3), $\rho:=s\circ\Psi^{-1}\in C^1$, $\nabla\rho=\omega(\theta)$ (K3: $s$ — та же функция,
   что для $\Pi$), $Y:=(2.4)\circ\Psi^{-1}\in C^1$ ($\eta_0\in C^2$ при $s>0$), $Y\rho=1$.
3. *Выбор $\delta_1$.* $\delta_1\le\min(\delta_0,a_0/2)$ такое, что при $\delta\le\delta_1$: $\frac54R_\theta(\delta)(1+\bar k_g)\le1$ и
   $5R_\theta(\delta)\sqrt\delta\le\frac14\sqrt{2a_0/3}$. Зафиксируем $\delta\in(0,\delta_1]$, $\kappa:=\kappa(\delta)$ по (2.3), $c_2:=c_2(\kappa)$, $\lambda:=c-c_2$.
4. *Множество $D$.* По (NF$_W$) функция
   $\chi(\sigma'):=\sup\{|\tilde F-\tilde F_0|+|\partial_\theta(\tilde F-\tilde F_0)|+|\partial_e(\tilde F-\tilde F_0)|+|\sigma\partial_\sigma\tilde F|:\ 0<\sigma\le\sigma',\ |\theta|\le r_W,\ |e|\le1\}$, где
   $\tilde F_0:=\tilde F(0,\cdot)$, стремится к нулю: $\tilde F$, $\partial_\theta\tilde F$, $\partial_e\tilde F$ равномерно непрерывны на компакте. Выберем
   $\sigma_*\in(0,s_2)$ с $\chi:=\chi(\sigma_*^{1/N})<\delta$ ($\sigma_*$ ещё уменьшится) и положим
   $$\mathcal D:=\{(s,\theta,e):\ 0<s<\sigma_*,\ (\theta,e)\in\Omega_\delta,\ \tilde F(s^{1/N},\theta,e)+a_0<\delta\},\qquad D:=\{\Psi(s,\theta,s^ce):\ (s,\theta,e)\in\mathcal D\}.$$
   (D1)–(D3) проверяются дословно как в [010], §5.2, п. 4 (с $Q\to P$). (D1): предел точек $D$ либо лежит в $\mathcal O$, либо
   равен $0$, так как $|\Psi|\le\sqrt{s^2+\eta^2}\le2s$; $\rho\le|q|$. (D2): в граничной точке с $\rho<\sigma_*$ либо $(\theta,e)\in\partial\Omega_\delta$, и
   тогда $\tilde F+a_0\ge P-\chi=4\delta-\chi>3\delta$ — противоречие с $\tilde F+a_0\le\delta$; либо $\tilde F+a_0=\delta$, то есть $W=\delta\rho^\beta$. (D3):
   точки $(s,0,0)$, где $P=0$ и $\tilde F+a_0\le\chi<\delta$.
5. *(L0), (L1).* $A(r)=a_0r^\beta$: $a_1=a_3=a_0$, $a_2=\beta a_0$, $\delta\le a_0/2$. По (5.2) $1\le h\le1+\frac14\cdot\frac1{16}\cdot\frac{25}{16}+\frac1{16}<\frac32$:
   $h_0=1$, $h_1=\frac32$.
6. *(L2).* На $D_\sigma$ ($\sigma=\sigma_*$) $(\theta,e)\in\overline{\Omega_\delta}\subset K$, $P\ge0$, поэтому $W=s^\beta(P+\tilde F-\tilde F_0)\ge-\chi s^\beta\ge-\delta\rho^\beta$. По
   (5.7), (2.2) и $|\theta|\le r_W$, $|e|\le1$, $c_2\le c$:
   $$\beta W-\rho YW\ge s^\beta\big[\kappa\theta\partial_\theta P+c_2e\partial_eP-(\kappa r_W+c+\tfrac1N)\chi\big]\ge s^\beta\big[\kappa\mu_0P-(\kappa r_W+c+\tfrac1N)\chi\big].$$
   При $\mu:=\kappa\mu_0$ имеем $\mu W\le\kappa\mu_0s^\beta(P+\chi)$. Значит, (L2) леммы M выполнено с $\mu=\kappa\mu_0\le\beta/4<\beta$ и
   $\varepsilon_1:=(\kappa r_W+c+\frac1N+\kappa\mu_0)\chi/\delta\le(c+2+\mu_0)\chi/\delta$.
7. *(L3M).* Пусть $q\in D_\sigma$ (там $|\theta|\le R_\theta:=R_\theta(\delta)$, $\kappa|\theta|\le1$) и $w\perp Y(q)$.
   - По (5.6): $|\langle\nabla\rho-Y/h,w\rangle|=|w_\omega|\le(\frac54\kappa R_\theta+|\tilde\nu|)|w|$. Положим $\gamma_1:=\frac54\kappa R_\theta$, $\vartheta_1:=\sup|\tilde\nu|$.
   - По (5.4) и $\nabla_YY=D_YY$, $\rho=s$: $\omega$-компонента не больше $\frac54\kappa^2\theta^2$; $\ell$-компонента равна
     $-\kappa(1-\kappa)\theta+\kappa\theta[s\partial_s\epsilon-\kappa\epsilon-\kappa\theta\partial_\theta\epsilon+\tilde\nu k_g+\lambda k_g\zeta/s]$, второй член по модулю не больше
     $|s\partial_s\epsilon|+\kappa|\epsilon|+|\partial_\theta\epsilon|+\bar k_g|\tilde\nu|+c\bar k_g|\zeta|/s$; $n$-компонента не больше
     $\frac54\kappa^2\theta^2\bar k_g+|s\partial_s\tilde\nu|+|\partial_\theta\tilde\nu|+c^2|\zeta|/s$. Значит, $\rho|\langle\nabla_YY,w\rangle|\le(\gamma_2+\vartheta_2)|w|$ с
     $\gamma_2:=\kappa R_\theta+\frac54\kappa^2R_\theta^2(1+\bar k_g)\le\frac32\kappa R_\theta$ (п. 3) и
     $\vartheta_2:=\sup(|s\partial_s\epsilon|+|\epsilon|+|\partial_\theta\epsilon|+\bar k_g|\tilde\nu|+c\bar k_g|\zeta|/s+|s\partial_s\tilde\nu|+|\partial_\theta\tilde\nu|+c^2|\zeta|/s)$.
   - По (5.5): первый член $\ge(\frac45-\frac12)w_\ell^2\ge0$; по (5.6) $\kappa\theta w_\omega w_\ell=\kappa^2\theta^2(1-\epsilon)w_\ell^2-\kappa\theta\tilde\nu w_\ell w_n\ge-|\tilde\nu||w|^2$;
     третий член $\ge-\frac43(|\partial_\theta\epsilon|+\bar k_g|\tilde\nu|+|\partial_\theta\tilde\nu|)|w|^2$; четвёртый $\ge-(|s\partial_s\epsilon|+|s\partial_s\tilde\nu|)|w|^2$ ($|w_\omega|\le|w|$);
     пятый $\ge-\bar k_g(|\eta_{0,s}|+\frac43|\eta_{0,\theta}|/s)|w|^2$; последний равен
     $\lambda w_n^2-\lambda w_n(w_\omega\eta_{0,s}+w_\ell\eta_{0,\theta}/(s(1-\epsilon)))\ge-c(|\eta_{0,s}|+\frac43|\eta_{0,\theta}|/s)|w|^2$. Итак, $s\langle w,D_wY\rangle\ge-\vartheta_3|w|^2$ с
     $\vartheta_3:=\sup\big(|\tilde\nu|+\frac43(|\partial_\theta\epsilon|+\bar k_g|\tilde\nu|+|\partial_\theta\tilde\nu|)+|s\partial_s\epsilon|+|s\partial_s\tilde\nu|+(\bar k_g+c)(|\eta_{0,s}|+\frac43|\eta_{0,\theta}|/s)\big)$.

   По (5.8) $\vartheta_1,\vartheta_2,\vartheta_3\le C_\vartheta\Delta(\sigma_*)$, где $C_\vartheta$ зависит только от $\bar k_g$ и $c$; при $\sigma_*\to0$ они стремятся к нулю
   равномерно по $\kappa$ и $\lambda$.
8. *Константы леммы M.* $L_1=3\beta\sqrt{3a_0/2}$, $L_2=2\sqrt{2a_0}$. При $\delta\le a_0/2$
   $$\Gamma_M:=\sqrt2\Big[(a_2+\beta\delta)\sqrt{\tfrac{h_1}{a_1}}\gamma_1+\sqrt{\tfrac{2a_3}{h_0}}\gamma_2\Big]\le\sqrt2\Big[\tfrac32\beta a_0\sqrt{\tfrac3{2a_0}}\cdot\tfrac54\kappa R_\theta+\sqrt{2a_0}\cdot\tfrac32\kappa R_\theta\Big]=\Big(\tfrac{15\sqrt3}8\beta+3\Big)\sqrt{a_0}\,\kappa R_\theta\le C_M\sqrt{a_0}\,\kappa R_\theta .$$
   Уменьшим $\sigma_*$ так, чтобы $\vartheta_3\le\beta/8$, $\varepsilon_1+(L_1\vartheta_1+L_2\vartheta_2)/\sqrt\delta\le\kappa\mu_0/4$ и
   $4\sqrt\delta\,\vartheta_1\le\frac12\sqrt{2a_0/3}$. Это возможно: при фиксированных $\delta$, $\kappa$ все эти величины стремятся к
   нулю при $\sigma_*\to0$. Тогда $b'=\beta-\mu-2\vartheta_3\ge\beta-\frac\beta4-\frac\beta4=\frac\beta2$ и
   $$\frac{\Gamma_M^2}{4b'\delta}\le\frac{C_M^2a_0\kappa^2R_\theta^2}{2\beta\delta}\le\frac{\kappa\mu_0}4$$
   по третьему члену (2.3). Скобка в (0.3) [010] не меньше $\kappa\mu_0-\frac{\kappa\mu_0}4-\frac{\kappa\mu_0}4=\frac{\kappa\mu_0}2>0$. Условие п. 1 леммы M:
   $4\sqrt\delta(\vartheta_1+\gamma_1)\le\frac12\sqrt{2a_0/3}+5\kappa\sqrt\delta R_\theta\le\frac12\sqrt{2a_0/3}+\frac18\sqrt{2a_0/3}<\sqrt{a_1/h_1}$ (п. 3 и $\kappa\le\frac12$).
9. *Вывод.* Лемма M [010] даёт (D4), (A4) и (A5); теорема A [007] — решение в $\overline\Omega$ с $q\ne0$, $q,\dot q\to0$. По
   шагу 5 теоремы A $\rho(q(t))<\sigma_*$, так что $q(t)\in D_\sigma$ и $(\theta,e)\in\overline{\Omega_\delta}$. Оценки $\dot s$ — п. 1 леммы M с
   $k_1=\frac12\sqrt{2a_0/3}$, $k_2=\sqrt{2(a_0+\delta)}+k_1$. $\square$

Порядок констант: $r_W$, $\delta_0$ (по $P$) → $s_2$ (по данным, равномерно по $\kappa,\lambda$) → $\delta_1$ → $\delta$ → $\kappa(\delta)$, $c_2$,
$\lambda$ → $\sigma_*$.

### 5.3. Замечания к теореме W

- [Доказано] **Частные случаи.** Теорема Mb [010]: $y_0(\varsigma,\theta)=y^*(\varsigma^2,\theta)$, $N=2$, $c_2\equiv c$,
  $P=\Lambda(\theta)+\frac12h_n(\theta)e^2$, $\mu_0=1$, $R_\theta\le(8\delta/a)^{1/(2p)}$, и (2.3) совпадает с (0.4) [010] с точностью до
  константы. Теорема N [011] — случай $p=1$ с разделяющимся профилем, где $R_\theta^2\asymp\delta$ и $\kappa(\delta)$
  отделено от нуля.
- [Доказано] **Зачем свободный нормальный вес.** Если профиль не распадается, неравенство (2.2) с
  $c_2=c$ может нарушаться при всех допустимых $\kappa$. Пример: $P_0=e^4+\theta e^2+\theta^2$, квазиоднородный с весами
  $(\theta:1,e:\frac12)$. При $c_2=c$ квадратичная по $(\theta,e^2)$ форма
  $\kappa\theta\partial_\theta P_0+ce\partial_eP_0=4ce^4+(\kappa+2c)\theta e^2+2\kappa\theta^2$ неотрицательна только при $(\kappa+2c)^2\le32c\kappa$, то есть при
  $\kappa\ge(14-\sqrt{192})c\approx0{.}144c$. Это противоречит малости $\kappa$, которой требуют перекрёстные члены. При
  $c_2=\kappa/2$: $\kappa(\theta\partial_\theta P_0+\frac12e\partial_eP_0)=2\kappa P_0$ — неравенство Эйлера выполнено при любом $\kappa$. Цена —
  член $\lambda\zeta/s$ в нормальной компоненте $Y$. Он даёт вклад $O(s^{c-1})$ в $\vartheta_i$ и неотрицательный член
  $\lambda w_n^2$ в (5.5).
- [Эксперимент] Для разделяющегося профиля с медленным $s^{c-1}$ (пример W1, $c=\frac54$) поле с $\lambda>0$
  выходит на асимптотический режим лишь при $s\lesssim10^{-16}$. Поэтому при $c_2\equiv c$ (если (2.2) с ним
  выполнено) $\lambda=0$ практичнее (§10.3).

## 6. Теорема C: доказательство

1. *Данные.* $s_2$ — как в §5.2, п. 2, с $\kappa=\lambda=0$ и супремумом по всем $\theta\in\mathbb R$ (периодичность). $\mathcal O:=\{\Psi(s,\theta,s^ce):\ 0<s<s_2,\ \theta\in\mathbb R/L\mathbb Z,\ |e|<1\}$
   — открытое множество, $\Psi$ на нём инъективна (лемма K3 для замкнутой кривой, [010], (N3)); $\rho:=s\circ\Psi^{-1}$,
   $Y:=\Psi_s\circ\Psi^{-1}$, $Y\rho=1$, $A(r)=a_0r^\beta$.
2. *Эйлер.* По (5.7) с $\kappa=\lambda=0$ ($c_2=c$): $\beta W-\rho YW=s^\beta[ce\partial_e\tilde F-\frac\sigma N\partial_\sigma\tilde F]$.
3. *Область.* $\Omega:=\{(\theta,e):\ |e|<e_C,\ P<4\delta\}$. При $\delta\le\delta_0:=\min\big(\frac{a_0}2,\ \frac18\min_{e_C/2\le t\le e_C}q_0(t)\big)$ по (C1)
   $\Omega\subset\mathbb R\times(-\frac{e_C}2,\frac{e_C}2)$ и $P=4\delta$ на $\partial\Omega$; $R_e(\delta):=\sup_\Omega|e|\to0$ при $\delta\to0$ (так как $q_0>0$ на $(0,e_C]$). Функция
   $\chi(\sigma'):=\sup\{|\tilde F-\tilde F_0|+|\partial_e(\tilde F-\tilde F_0)|+|\sigma\partial_\sigma\tilde F|:\ 0<\sigma\le\sigma',\ \theta\in\mathbb R,\ |e|\le1\}$ стремится к нулю
   (периодичность и равномерная непрерывность на $[0,\sigma_1]\times[0,L]\times[-1,1]$). Выберем $\sigma_*$ с $\chi<\delta$,
   $\mathcal D:=\{0<s<\sigma_*,\ (\theta,e)\in\Omega,\ \tilde F+a_0<\delta\}$, $D:=\Psi(\{(s,\theta,s^ce)\})$; $\sigma$ теоремы A — это $\sigma_*$.
4. *(D1)–(D3)* — как в [010], §6, п. 4: предельный угол берётся по компактности окружности; угловой
   границы нет; на $\partial\Omega$ $P=4\delta$; в (D3) — точки $(s,\theta,0)$, где $P(\theta,0)=0$ по (C1).
5. *(L0)–(L2).* $a_1=a_3=a_0$, $a_2=\beta a_0$, $h=1+\eta_{0,s}^2\in[1,\frac32]$. На $D_\sigma$: $W\ge-\chi s^\beta\ge-\delta\rho^\beta$. Положим
   $\mu:=\min(c\mu_0,\beta)$. По (C2) и $P\ge0$: $\beta W-\rho YW\ge s^\beta[c\mu_0P-cR_e\chi-\frac\chi N]\ge\mu W-s^\beta(c+\frac1N+\beta)\chi$, то есть
   $\varepsilon_1:=(c+\frac1N+\beta)\chi/\delta$.
6. *(L3) [007].* При $\kappa=\lambda=0$: $Y=\omega+\eta_{0,s}n$; для $w\perp Y$ $w_\omega=-\eta_{0,s}w_n$, и так как $\nabla\rho-Y/h\perp Y$,
   $|\nabla\rho-Y/h|\le|\eta_{0,s}|=:\theta_1$. $\nabla_YY=\partial_s(\omega+\eta_{0,s}n)=\eta_{0,ss}n$: $\theta_2:=\sup s|\eta_{0,ss}|$. По (5.5) при $\kappa=\lambda=0$
   $s\langle w,D_wY\rangle=\frac{(1-\eta_{0,s}k_g)w_\ell^2+\eta_{0,s\theta}w_\ell w_n}{1-\epsilon}+s\eta_{0,ss}w_\omega w_n\ge-\big(\frac43|\eta_{0,s\theta}|+s|\eta_{0,ss}|\big)|w|^2$ ($|\eta_{0,s}k_g|\le1$):
   $\theta_3:=\sup(\frac43|\eta_{0,s\theta}|+s|\eta_{0,ss}|)$. Все $\theta_i\le3\Delta(\sigma_*)\to0$.
7. *Вывод.* При фиксированном $\delta$ уменьшим $\sigma_*$ так, чтобы
   $\varepsilon_1+(L_1\theta_1+L_2\theta_2)/\sqrt\delta+4\theta_3\le\mu/2$ и $4\theta_1\sqrt\delta\le\sqrt{2a_0/3}$. Лемма 2 [007] даёт (D4), (A4), (A5) (скобка
   (3.1) [007] не меньше $\mu/2$), теорема A [007] — траекторию; оценки $\dot s$ — п. 1 леммы 2, оценка $e$ — из
   $(\theta,e)\in\overline\Omega$. $\square$

Это доказательство теоремы Mc [010], §6, где точное дно $\eta^*$ заменено на приближённое $\eta_0$, а
профиль $\frac12h_ne^2$ — на $P$ с (C1), (C2).

## 7. Теорема D: доказательство

1. *Лемма V и замена $t\mapsto t^{r'}$.* $f(\sigma,\tau):=\hat G(\sigma,\tau)$ аналитична около $(0,0)$, $f(0,\cdot)=G\ge0$, $G\not\equiv0$,
   $f(\sigma_k,\theta_k)<0$ — условия леммы V [010] выполнены. Подстановка $t\mapsto t^{m}$ ($m\in\mathbb N$) переводит данные
   леммы V $(N_V,A_V,\Gamma_V,a_V,T,Q_V,k_0)$ в $(mN_V,mA_V,m\Gamma_V,a_V,T(t^m),Q_V,k_0)$ и сохраняет все её утверждения.
   Действительно, $\tau_v(\sigma)=T(\sigma^{1/N_V})$ не меняется, новая функция $\hat\Phi$ равна $\hat\Phi(t^m,b)$ и аналитична с тем же
   значением при $t=0$, чётность сохраняется. При $m=r'$ получаем $2r'\mid\Gamma_V$, так как $\Gamma_V$ чётно. Условие
   (D2) инвариантно относительно таких подстановок: $i$, $\Gamma_V$, $B$ умножаются на $m$. Ниже данные
   — из (D2), $B=\Gamma_V/(2r')\in\mathbb N$.
2. *Переменные.* $x=s$, $\sigma=x^{1/N}$, $t:=\sigma^{1/N_V}=x^{1/(NN_V)}$, $\hat\theta(x,u):=\tau_v(x)+u/x=T(t)+t^{A_V}b_1$, $\zeta=x^{c'}b_2$,
   $e:=\zeta x^{-c}=x^{c'-c}b_2=t^Bb_2$ (так как $(c'-c)NN_V=\Gamma_V/(2r')=B$).
3. *$(\Phi0)$–$(\Phi3)$ с $C_1=0$.* Дословно [010], §8, пп. 1–5, с заменой точного дна $\eta^*$ на $\eta_0$ и $\theta_0=0$.
   Используются только: (8.1) [010] — $\tilde\kappa:=x\partial_x\hat\theta=x\tau_v'-x^\alpha b_1\to0$, $x^2\partial_x^2\hat\theta\to0$, $\hat\theta\to0$,
   $|\zeta|\le r_0x^{c'}$, $c'>1$ (верно, так как $\tau_v(x)=T(x^{1/(NN_V)})$, $T(0)=0$); формулы (8.2), (8.3) [010] (тождества
   для любого $C^2$-дна, проверены символьно при общих $\eta^*(s,\theta)$, $k_g$, $\tau_v$); стремление к нулю величин
   $\Delta$ из §5.1 (лемма N5 [011]) для $\eta_0=sy_0(s^{1/N},\theta)$.
4. *(F).* По (2.1) и (2.5), $0<x<s_0$, $|b|<r_0$:
   $$U\circ\Phi=x^\beta\tilde F(\sigma,\hat\theta,e)=x^\beta\Big[f\big(t^{N_V},T(t)+t^{A_V}b_1\big)+\sum_{l=1}^{2r'-1}H_l(t,b_1)\,t^{lB}b_2^l+t^{2r'B}b_2^{2r'}M\big(t^{N_V},\hat\theta,t^Bb_2\big)\Big]=x^{\beta_d}F_d(t,b),$$
   $$F_d(t,b):=\hat\Phi(t,b_1)+\sum_{l=1}^{2r'-1}t^{lB-\Gamma_V}H_l(t,b_1)\,b_2^l+b_2^{2r'}M\big(t^{N_V},T(t)+t^{A_V}b_1,t^Bb_2\big), \tag{7.1}$$
   так как $x^\beta t^{\Gamma_V}=x^{\beta+\gamma'}$, $2r'B=\Gamma_V$, $H_l(t,b_1):=h_l(t^{N_V},T(t)+t^{A_V}b_1)$. По лемме V, п. 2 (с $B_V>r_0$), $\hat\Phi$
   аналитична около $\{0\}\times[-r_0,r_0]$. По (D2) $t^{lB-\Gamma_V}H_l=\sum_{i>\Gamma_V-lB}H_{l,i}(b_1)t^{i+lB-\Gamma_V}$ аналитична и равна нулю при
   $t=0$. $M$ аналитична около $(0,0,0)$. Значит, $F_d$ аналитична около $\{0\}\times\overline{B_{r_0}}$, $F_d$ и $\nabla_bF_d$
   непрерывны вплоть до $t=0$, $\sup_K|t\partial_tF_d|=O(t)$, и
   $$F_{d,0}(b)=-a_V+Q_V(b_1)+M_0b_2^{2r'},\qquad Q(b):=F_{d,0}(b)-F_{d,0}(0)=Q_V(b_1)+M_0b_2^{2r'}. \tag{7.2}$$
   Выбор $s_0$: $s_0\le1$, $s_0<\sigma_J^N$, $2s_0<r$, $r_0s_0^{B/(NN_V)}<e_J$, $|T(t)|+t^{A_V}r_0<\theta_1/2$ при $t<s_0^{1/(NN_V)}$,
   $s_0^{1/(NN_V)}$ меньше радиуса аналитичности $F_d$ и малость из п. 3. Переменная $s$ теоремы 2 [007] — это $t$, число
   $N$ теоремы 2 — это $NN_V$.
5. *$(V_0)$.* $F_{d,0}(0)=-a_V<0$. Выберем $r_2$ так, что при $|b_1|\le r_2$ $Q_V(b_1)\ge\frac{c_{k_0}}2b_1^{k_0}$ и $b_1Q_V'(b_1)\ge Q_V(b_1)$ (так как
   $Q_V=c_{k_0}b_1^{k_0}(1+O(b_1))$, $k_0\ge2$ чётно, $c_{k_0}>0$); $r_0:=r_2$. При малом $\delta_2$ из $Q<\delta\le\delta_2$, $b\in B_{r_0}$ следует
   $|b_1|<(2\delta/c_{k_0})^{1/k_0}$, $|b_2|<(\delta/M_0)^{1/(2r')}$, так что $\{Q<\delta\}\cap B_{r_0}\subset B_{r_0/2}$, и компонента $\Omega_b\ni0$ имеет
   $\overline{\Omega_b}\subset B_{r_0}$. $Q\ge0$ ($Q_V\ge0$ на $\mathbb R$ по лемме V, п. 3). На $\overline{\Omega_b}$
   $$c_1b_1\partial_{b_1}Q+c'b_2\partial_{b_2}Q=(1+\alpha)\,b_1Q_V'+2r'c'M_0b_2^{2r'}\ge Q_V+M_0b_2^{2r'}=Q.$$
   Это $(V_0)$ с $\mu=1$ и $\delta\in(0,\min(a_V/2,\delta_2)]$. Условие $\mu\le\beta_d$ выполнено: $\beta_d\ge2$ по рассуждению п. 1 шага 6
   теоремы 2 [007]. Оно использует только $(\Phi0)$, $(\Phi1)$, (F), $F_{d,0}(0)\ne0$ и $U\in C^2$.
6. *Вывод.* Теорема 2 [007] даёт траекторию $q=\Phi(x,u,\zeta)$ с $b(t)$ в компакте внутри $B_{r_0}$ и
   $-k_2x^{\beta_d/2}\le\dot x\le-k_1x^{\beta_d/2}$ (п. 3 теоремы 2; при $\beta_d>2$ отсюда $x(t)\asymp t^{-2/(\beta_d-2)}$). Касание:
   $q=x\omega(\hat\theta)+\eta n(\hat\theta)$, $\hat\theta=\tau_v(x)+x^\alpha b_1\to0$, $|\eta|\le|\eta_0|+r_0x^{c'}=o(x)$. $\square$

## 8. Ветви: доказательства лемм B, U, B′

**Лемма B.**

1. *Единственность.* Пусть $\varepsilon',\varepsilon''$ — непрерывные функции на интервале $I\ni\theta_0$ с $(\theta,\varepsilon'(\theta)),(\theta,\varepsilon''(\theta))\in F_{c_0}$ и
   $\varepsilon'(\theta_0)=\varepsilon''(\theta_0)$. Тогда $\varepsilon'=\varepsilon''$ на $I$. Множество совпадения замкнуто в $I$. Оно и открыто: в точке совпадения $\theta'$
   обе функции около $\theta'$ — критические точки $\Phi_0(\theta,\cdot)$ рядом с $\varepsilon'(\theta')$ и по (CM) в $(\theta',\varepsilon'(\theta'))$ совпадают с
   $\varepsilon_b$.
2. *Продолжение.* Пусть $I=(\theta_-,\theta_+)$ — максимальный интервал, на котором есть аналитическая $\varepsilon_g$ с $\varepsilon_g(\theta_0)=\varepsilon_0$ и
   $(\theta,\varepsilon_g)\in F_{c_0}$. Он корректно определён по п. 1 и непуст: ветвь $\varepsilon_b$ около $\theta_0$ годится, так как
   $\Phi_0(\theta,\varepsilon_b)=G_b\equiv c_0\le G_{\min}\le\Phi_0(\theta,\varepsilon_b)$. Пусть $\theta_+<\infty$. Значения $\varepsilon_g$ лежат в $[-E_0,E_0]$; возьмём $\theta_k\uparrow\theta_+$ с
   $\varepsilon_g(\theta_k)\to\varepsilon_1$. Тогда $(\theta_+,\varepsilon_1)\in F_{c_0}$ ($F_{c_0}$ замкнуто). Пусть $\varepsilon_b$, $\rho$ — из (CM) в $(\theta_+,\varepsilon_1)$; уменьшим $\rho$
   так, чтобы $|\varepsilon_b-\varepsilon_1|<\rho/2$ на $(\theta_+-\rho,\theta_++\rho)$, и пусть $\rho'\le\rho$ — радиус единственности из (CM). При
   большом $k$ $|\theta_k-\theta_+|<\rho$ и $|\varepsilon_g(\theta_k)-\varepsilon_1|<\rho'/2$, так что $\varepsilon_g(\theta_k)=\varepsilon_b(\theta_k)$. Пусть $J_k\ni\theta_k$ — максимальный
   подинтервал $(\theta_+-\rho,\theta_+)$, на котором $|\varepsilon_g-\varepsilon_b|<\rho'$. На $J_k$ $\varepsilon_g=\varepsilon_b$: обе функции — критические точки, а
   критическая точка в $|\varepsilon-\varepsilon_b(\theta)|<\rho'$ одна. Значит, $J_k=[\theta_k,\theta_+)$, иначе на правом конце $|\varepsilon_g-\varepsilon_b|=\rho'$ при
   $\varepsilon_g=\varepsilon_b$. Так $\varepsilon_b$ продолжает $\varepsilon_g$ за $\theta_+$. Функция $G_b$ аналитична и равна $c_0$ на $[\theta_k,\theta_+)$, поэтому
   $G_b\equiv c_0$ около $\theta_+$, и $c_0\le G_{\min}(\theta)\le\Phi_0(\theta,\varepsilon_b(\theta))=c_0$, то есть $(\theta,\varepsilon_b)\in F_{c_0}$. Это противоречит
   максимальности; значит, $I=\mathbb R$.
3. *Периодичность.* $\theta\mapsto\varepsilon_g(\theta+L)$ — тоже такая функция ($\Phi_0$ периодична). По п. 1 две такие функции
   либо совпадают всюду, либо не совпадают нигде; во втором случае разность $\varepsilon_g(\theta+L)-\varepsilon_g(\theta)$ знакопостоянна.
   Если она, например, положительна, то $\varepsilon_g(\theta_0+kL)$ строго возрастает по $k$. Но все эти значения лежат в
   конечном множестве нулей многочлена $\Phi_0(\theta_0,\cdot)-c_0\not\equiv0$ — противоречие. Итак, $\varepsilon_g$ периодична.
4. *Профиль.* По (CM) кратность $2r'-1$ локально постоянна вдоль $\varepsilon_g$, значит, постоянна. Определим
   $\mathsf p_g(\theta,e):=e^{-2r'}(\Phi_0(\theta,\varepsilon_g+e)-c_0)$, то есть интегральный остаток Тейлора порядка $2r'$. Он
   аналитичен и периодичен, и $\mathsf p_g(\theta,0)=\partial_\varepsilon^{2r'}\Phi_0(\theta,\varepsilon_g)/(2r')!>0$, так как это точка минимума с первой ненулевой
   производной порядка $2r'$. По компактности $e_g>0$ выбирается равномерно. $\square$

**Лемма U.**

1. Фиксируем $\theta'$. Точки глобального минимума $\Phi_0(\theta',\cdot)$ — конечное множество $\{\varepsilon_1,\dots,\varepsilon_K\}\subset(-E_0,E_0)$
   (нули многочлена $\Phi_0(\theta',\cdot)-G_{\min}(\theta')\not\equiv0$). По (R) $\partial_\varepsilon^2\Phi_0(\theta',\varepsilon_k)>0$.
2. По аналитической теореме о неявной функции для $\partial_\varepsilon\tilde U(\sigma,\theta,\varepsilon)=0$ в точке $(0,\theta',\varepsilon_k)$ (там
   $\partial_\varepsilon^2\tilde U=\partial_\varepsilon^2\Phi_0>0$) есть $\rho_k>0$ и аналитическая $\varepsilon_k^*$ на $(-\rho_k,\rho_k)\times(\theta'-\rho_k,\theta'+\rho_k)$ с $\varepsilon_k^*(0,\theta')=\varepsilon_k$.
   Это единственный нуль $\partial_\varepsilon\tilde U(\sigma,\theta,\cdot)$ в $(\varepsilon_k-\rho_k,\varepsilon_k+\rho_k)$, и там $\partial_\varepsilon^2\tilde U\ge m_k>0$. По формуле Тейлора
   $\tilde U(\sigma,\theta,\varepsilon_k^*+e)=\hat G_k+e^2M_k$, где $\hat G_k:=\tilde U(\sigma,\theta,\varepsilon_k^*)$ и
   $M_k:=\int_0^1(1-t)\partial_\varepsilon^2\tilde U(\sigma,\theta,\varepsilon_k^*+te)\,dt\ge m_k/2$ при малых $|e|$. Это (UR1) с $r_k=1$.
3. *(UR2).* Выберем $\rho\in(0,\min(1,\min_k\rho_k/2))$ так, что интервалы $(\varepsilon_k-\rho,\varepsilon_k+\rho)$ попарно не пересекаются и лежат в
   $(-E_0,E_0)$; $O_\rho$ — их объединение. Тогда $g:=\min\{\Phi_0(\theta',\varepsilon)-G_{\min}(\theta'):\ \varepsilon\in[-E,E]\setminus O_\rho\}>0$. Выберем
   $\rho'\in(0,\rho)$ с $\Phi_0(\theta',\varepsilon)<G_{\min}(\theta')+\frac g3$ при $|\varepsilon-\varepsilon_k|<\rho'$, затем $J\ni\theta'$ и $\sigma_J\le\min_k\rho_k$ такие, что при $\theta\in J$,
   $0\le\sigma<\sigma_J$: $|\tilde U(\sigma,\theta,\varepsilon)-\Phi_0(\theta',\varepsilon)|<\frac g3$ при $|\varepsilon|\le E+1$ и $|\varepsilon_k^*(\sigma,\theta)-\varepsilon_k|<\rho'$. Тогда
   $\tilde U(\sigma,\theta,\varepsilon_k^*)<G_{\min}(\theta')+\frac{2g}3<\tilde U(\sigma,\theta,\varepsilon)$ при $\varepsilon\in[-E,E]\setminus O_\rho$. Точка глобального минимума на $[-E,E]$
   лежит в некотором $(\varepsilon_k-\rho,\varepsilon_k+\rho)\subset(-E,E)$; это внутренняя критическая точка, и по п. 2 она равна $\varepsilon_k^*(\sigma,\theta)$. При
   $\sigma=0$ рассуждение то же. $\square$

**Лемма B′.**

1. *$\sigma=0$.* Каждая точка $F_{c_0}$ — точка глобального минимума $\Phi_0(\theta,\cdot)$. По (UR2) при $\sigma=0$ она равна $\varepsilon_k^*(0,\theta)$
   для некоторой ветви, и по (UR1) при $\sigma=0$ в ней выполнено (CM) (с $\varepsilon_b=\varepsilon_k^*(0,\cdot)$, $\mathsf p=M_k(0,\cdot,\cdot)$). Ветвь
   $\varepsilon_k^*(0,\cdot)$ имеет $G_b=G_k\equiv c_0$ около $\theta_0$. По лемме B получаем периодическую аналитическую $\varepsilon_g$ с
   $(\theta,\varepsilon_g)\in F_{c_0}$.
2. *Покрытие.* Покроем $[0,L]$ конечным числом интервалов $J_1,\dots,J_p$ из (UR) и выберем компактные
   $J_i'\subset J_i$, внутренности которых тоже покрывают $[0,L]$. На $J_i$ найдётся ветвь $k_i$ с $\varepsilon_{k_i}^*(0,\theta)=\varepsilon_g(\theta)$
   при всех $\theta\in J_i$. Для каждого $\theta$ такая ветвь есть (п. 1). Множество $\theta\in J_i$, где ею служит данная ветвь
   $k$, замкнуто (непрерывность) и открыто: по единственности критической точки около $(\theta,\varepsilon_g(\theta))$ две
   непрерывные ветви критических точек, совпадающие в точке, совпадают рядом. Так как $J_i$ связен,
   ветвь одна.
3. *Склейка при $\sigma>0$.* На $J_i\cap J_{i'}$ функции $\varepsilon_{k_i}^*$ и $\varepsilon_{k_{i'}}^*$ совпадают при $\sigma=0$. По (UR1) для ветви $k_i$
   единственная критическая точка $\tilde U(\sigma,\theta,\cdot)$ в $|\varepsilon-\varepsilon_{k_i}^*(\sigma,\theta)|<e'$ — это $\varepsilon_{k_i}^*$, где $e'>0$ равномерно на
   $J_i'\times[0,\sigma']$. При малом $\sigma$ $\varepsilon_{k_{i'}}^*$ лежит в этой окрестности, значит, функции совпадают при
   $(\sigma,\theta)\in[0,\sigma_0)\times(J_i'\cap J_{i'}')$ и, по аналитичности, при $|\sigma|<\sigma_0$. Получаем аналитическую $\varepsilon_g^*$ на
   $(-\sigma_0,\sigma_0)\times\mathbb R$. Она периодична, так как $\varepsilon_g$ периодична и по той же единственности. $\hat G_g:=\tilde U(\sigma,\theta,\varepsilon_g^*)$,
   $M_g$ равна $M_{k_i}$ на кусках и тоже склеивается. $r_g=r_{k_i}$ одно и то же (кратность при $\sigma=0$ вдоль $\varepsilon_g$
   постоянна), $e_0:=\min e_{J_i}$. $\square$

## 9. Сборка

**Предложение W′.** $a_0:=-\min G_{\min}>0$.

1. *(W-a).* $G_b(\theta)=\Phi_0(\theta,\varepsilon_b(\theta))\ge G_{\min}(\theta)\ge-a_0=G_b(\theta_0)$, так что $\theta_0$ — точка локального минимума
   аналитической непостоянной около $\theta_0$ функции $G_b$: $\Lambda(\tau):=G_b(\theta_0+\tau)+a_0=a\tau^{2p}(1+O(\tau))$, $a>0$, $p\ge1$.
   Применим теорему W на дуге $|\tau|<\theta_1\le\min(\rho,L/4)$ с центром $\theta_0$:
   - $y_0(\sigma,\tau):=\sigma^{N\gamma_*}\varepsilon_b(\theta_0+\tau)$ ($N\gamma_*\in\mathbb N$, так что $y_0$ аналитична и $y_0(0,\cdot)=0$);
   - $\tilde F(\sigma,\tau,e):=\tilde U(\sigma,\theta_0+\tau,\varepsilon_b(\theta_0+\tau)+e)$ (аналитична, $|\varepsilon_b+e|\le E+1$);
   - (2.1) — это (1.3), так как $s\,y_0+s^ce=s^c(\varepsilon_b+e)$;
   - $\tilde F(0,\tau,e)=-a_0+P(\tau,e)$, $P=\Lambda(\tau)+e^{2r'}\mathsf p(\theta_0+\tau,e)$ по (1.5).

   (W1) выполнено на малом квадрате: $P\ge\frac a2\tau^{2p}+\frac{\mathsf p_0}2e^{2r'}$, $\mathsf p_0:=\mathsf p(\theta_0,0)$. (W2) с $c_2\equiv c$, $\mu_0=1$: на квадрате, где
   $\tau\Lambda'\ge\Lambda$, $|e\partial_e\mathsf p|\le\mathsf p/4$, $|\tau\partial_\tau\mathsf p|\le\mathsf p$, имеем
   $$\kappa\tau\partial_\tau P+ce\partial_eP=\kappa\tau\Lambda'+e^{2r'}\big[2r'c\,\mathsf p+ce\partial_e\mathsf p+\kappa\tau\partial_\tau\mathsf p\big]\ge\kappa\Lambda+e^{2r'}\big(2c-\tfrac c4-\tfrac12\big)\mathsf p\ge\kappa P$$
   ($c>1$, $r'\ge1$, $\kappa\le\frac12$).
2. *(W-b).* Теорема W с $y_0:=\sigma^{N\gamma_*}\varepsilon_0$, $\tilde F:=\tilde U(\sigma,\theta_0+\tau,\varepsilon_0+e)$, $P$ из (DE), $r_W\le r_*$, $\kappa_0:=\min(\frac12,c/w)$,
   $c_2(\kappa):=w\kappa$: (2.2) — это (DE), умноженное на $\kappa$.
3. *(W-c).* Возьмём $(\theta_0,\varepsilon_0)\in F_{\min}$. По (CM) и п. 1 $G_b$ имеет в $\theta_0$ локальный минимум. Если $G_b\not\equiv-a_0$
   около $\theta_0$, это (W-a). Иначе по лемме B (с $c_0=-a_0$) есть глобальная периодическая ветвь $\varepsilon_g$ и
   $\Phi_0(\theta,\varepsilon_g+e)=-a_0+e^{2r'}\mathsf p_g$. Теорема C с $y_0:=\sigma^{N\gamma_*}\varepsilon_g(\theta)$, $\tilde F:=\tilde U(\sigma,\theta,\varepsilon_g(\theta)+e)$, $P=e^{2r'}\mathsf p_g$:
   (C1) с $q_0(t)=\frac12\min\mathsf p_g(\cdot,0)\,t^{2r'}$ и (C2) с $\mu_0=1$ на $|e|\le e_C$, где $|e\partial_e\mathsf p_g|\le\mathsf p_g/2$ и $\mathsf p_g\ge\frac12\min\mathsf p_g(\cdot,0)$. $\square$

**Теорема Z.**

1. *Ветвь с отрицательными значениями.* Пусть $\theta_*$ — предельная точка $\theta_n$ (по модулю $L$), $J\ni\theta_*$ — интервал из
   (UR). При больших $n$ $\theta_n\in J$, и по лемме N2(b) $F_{\rm fl}(s_n,\theta_n)=s_n^j\tilde U(\sigma_n,\theta_n,\varepsilon^\circ)$, где $\varepsilon^\circ$ — точка
   глобального минимума на $[-E,E]$. По (UR2) $\varepsilon^\circ=\varepsilon_{k_n}^*(\sigma_n,\theta_n)$; переходя к подпоследовательности, $k_n\equiv k$ и
   $\hat G_k(\sigma_n,\theta_n)<0$.
2. $G_k(\theta)=\Phi_0(\theta,\varepsilon_k^*(0,\theta))\ge G_{\min}(\theta)\ge0$ на $J$ и $G_k(\theta_*)=\lim\hat G_k(\sigma_n,\theta_n)\le0$, так что $G_k(\theta_*)=0$.
3. *$G_k\not\equiv0$ около $\theta_*$.* Теорема D на дуге с центром $\theta_*$: $y_0(\sigma,\tau):=\sigma^{N\gamma_*}\varepsilon_k^*(\sigma,\theta_*+\tau)$,
   $\tilde F(\sigma,\tau,e):=\tilde U(\sigma,\theta_*+\tau,\varepsilon_k^*+e)=\hat G_k+e^{2r_k}M_k$. Тождество (2.1) — это (1.3). В (2.5) $h_l\equiv0$, так что
   (D2) выполнено; $M_0=M_k(0,\theta_*,0)>0$; (D1) — п. 2 и п. 1.
4. *$G_k\equiv0$ около $\theta_*$.* По лемме B′ (с $c_0=0$) есть глобальная ветвь $g$, совпадающая с $k$ около $(0,\theta_*)$, так что
   $\hat G_g(\sigma_n,\theta_n)<0$ при больших $n$. Так как $\hat G_g\not\equiv0$, число $\kappa':=\min\{i:\ \partial_\sigma^i\hat G_g(0,\cdot)\not\equiv0\}$ конечно и $\ge1$.
   Иначе при каждом $\theta$ аналитическая по $\sigma\in(-\sigma_0,\sigma_0)$ функция $\hat G_g(\cdot,\theta)$ имела бы в нуле все производные
   нулевыми. По формуле Тейлора $\hat G_g=\sigma^{\kappa'}\hat G'$, $\hat G'$ аналитична и периодична, $G':=\hat G'(0,\cdot)\not\equiv0$.
   **Уточнённые данные**: $\varsigma:=\sigma^{1/(2r_g)}$, $N':=2r_gN$, $c':=c+\kappa'/N'$, $\beta':=j+\kappa'/N$,
   $$y_0'(\varsigma,\theta):=\varsigma^{2r_gN\gamma_*}\varepsilon_g^*(\varsigma^{2r_g},\theta),\qquad\tilde F'(\varsigma,\theta,e'):=\hat G'(\varsigma^{2r_g},\theta)+e'^{2r_g}M_g(\varsigma^{2r_g},\theta,\varsigma^{\kappa'}e').$$
   Проверка (2.1): при $s=\varsigma^{N'}$ $s^{c'}e'=s^c\varsigma^{\kappa'}e'$, поэтому
   $U(s\omega+(sy_0'+s^{c'}e')n)=s^j\tilde U(\sigma,\theta,\varepsilon_g^*+\varsigma^{\kappa'}e')=s^j[\sigma^{\kappa'}\hat G'+\sigma^{\kappa'}e'^{2r_g}M_g(\sigma,\theta,\varsigma^{\kappa'}e')]=s^{\beta'}\tilde F'$. Функция
   $\tilde F'$ аналитична при $|e'|\le1$ и малых $\varsigma$, и $\tilde F'(0,\theta,e')=G'(\theta)+M_g(0,\theta,0)e'^{2r_g}$.
   - $\min G'<0$, $G'\equiv\mathrm{const}$: теорема C с $P=M_g(0,\theta,0)e'^{2r_g}$; (C1), (C2) с $\mu_0=2r_g$ очевидны.
   - $\min G'<0$, $G'\not\equiv\mathrm{const}$: в точке $\theta_0$ глобального минимума $G'(\theta_0+\tau)-G'(\theta_0)=a\tau^{2p}(1+O(\tau))$; теорема W с
     $P=G'(\theta_0+\tau)-G'(\theta_0)+M_g(0,\theta_0+\tau,0)e'^{2r_g}$, $c_2\equiv c'$, $\mu_0=1$ (как в п. 1 предложения W′).
   - $\min G'=0$: $\hat G'(\sigma_n,\theta_n)<0$, так что для предельной точки $\theta_{**}$ $G'(\theta_{**})=0$; $G'\ge0$, $G'\not\equiv0$ около $\theta_{**}$
     (аналитична на связном $\mathbb R$). Теорема D в $\theta_{**}$ с уточнёнными данными: $h_l\equiv0$,
     $M'(0,\theta_{**},0)=M_g(0,\theta_{**},0)>0$, отрицательность — в точках $(\sigma_n^{1/(2r_g)},\theta_n)$.
   - $\min G'>0$ невозможно: тогда $\hat G'>0$ при малых $\sigma$ равномерно по $\theta$, и $\hat G_g(\sigma_n,\theta_n)>0$. $\square$

**Теорема M′.** По предложению R′ реализуется (P), (W) или (Z).

- (P): теорема K0 [008] с $\omega^*=\omega$. Условия: $u_m(\omega)=0$, $\nabla u_m(\omega)=0$, (H3), $j(\omega)<\infty$, $g_{j(\omega)}(\omega)<0$.
- (W): (UR) влечёт (CM) во всех точках $F_{\min}$ (лемма B′, п. 1). По предложению W′ (W-c) есть траектория.
- (Z): теорема Z.

Неустойчивость — теорема A [007], шаг 6. Изолированность нигде не использована. $\square$

**Следствие M′$_R$** — лемма U. При $r=1$ $\Phi_0=a(\theta,0)\varepsilon^2+b(\theta)\varepsilon+c(\theta)$ с $a(\theta,0)>0$: точка минимума одна и
невырождена. $\square$

## 10. Примеры и эксперименты

Во всех примерах $u_4=z^4$, так что $\Sigma$ — экватор $z=0$: $\omega=(\cos\theta,\sin\theta,0)$, $n=e_z$, $k_g=0$, $r=2$, $a\equiv1$;
$\rho^2:=x^2+y^2$. Выкладки — вручную; [Эксперимент] `examples_mult.py` повторяет их в sympy (носитель,
$\gamma_*$, $N$, $j$, $c$, $\Phi_0$, $\tilde U$, тождество (1.3), ветви, профили; вывод `examples_mult.out`).

### 10.1. Примеры, покрытые теоремами

| Пример | $U$ | $\gamma_*$, $j$, $c$ | $\Phi_0$ | Случай и теорема |
|---|---|---|---|---|
| W1 | $(z-x^2)^4+\frac32x\rho^4-\frac12x^3\rho^2+yz^5$ | $\frac14$, $5$, $\frac54$ | $\varepsilon^4+G$, $G=\frac12\cos\theta(3-\cos^2\theta)$ | (W): $G(\pi+\tau)=-1+\frac38\tau^4-\frac18\tau^6$ ($p=2$), $r'=2$; (CM) есть, (UR) нет; W′(W-a) → т. W |
| W2 | $z^4+zf_4+x^6+yz^5$, $f_4|_{S^1}=9-8\sin^4\theta$ | $\frac13$, $\frac{16}3$, $\frac43$ | $\varepsilon^4+f\varepsilon$ | (W), (R): $G=-3\cdot4^{-4/3}f^{4/3}$, минимум в $0,\pi$ порядка $4$, $r'=1$ → т. W |
| W3 | $z^4+z^2y\rho^2-\rho^6+y^2\rho^4+xz^5+y^7$ | $\frac12$, $6$, $\frac32$ | $(\varepsilon^2+\frac{\sin\theta}2)^2+\frac34\sin^2\theta-1$ | (W): $F_{\min}=\{(0,0),(\pi,0)\}$, ветвь расщепляется ((CM) нет); $P=e^4+\sin\tau\,e^2+\sin^2\tau$, (W1), (DE) с $w=\frac12$ → W′(W-b), т. W |
| W4 | $(z^2-\rho^4)^2+zx^8$ | $1$, $8$, $2$ | $(\varepsilon^2-1)^2$ | (Z) с $G\equiv0$, (R); уточнение $\kappa'=2$, ветвь $-1$: $G'=-\cos^8\theta$ → т. W ($p=1$); $0$ **не изолирована** |
| C1 | $(z+xy)^4-\rho^6+x^7+z^3y^4$ | $\frac12$, $6$, $\frac32$ | $\varepsilon^4-1$ | (W), $G\equiv-1$, профиль $e^4$; (CM) на всём дне, (UR) нет → W′(W-c), т. C |
| C2 | $z^4+z\rho^4+x^6z+y^7$ | $\frac13$, $\frac{16}3$, $\frac43$ | $\varepsilon^4+\varepsilon$ | (W), (R), $G\equiv-\frac38\,2^{1/3}$ → т. C |
| D1 | $(z-xy-x^3)^4+y^2\rho^4+x^7$ | $\frac12$, $6$, $\frac32$ | $\varepsilon^4+\sin^2\theta$ | (Z), (UR): точная ветвь $\varepsilon^*=\sigma\cos\theta\sin\theta+\sigma^3\cos^3\theta$ кратности 3, $\hat G=\sin^2\theta+\sigma^2\cos^7\theta$ → т. D в $\theta=\pi$ |
| D2 | $(z^2-\rho^4)^2+y^2\rho^6+x^9+z^3x^6$ | $1$, $8$, $2$ | $(\varepsilon^2-1)^2+\sin^2\theta$ | (Z), (R): $\hat G_\pm=\sin^2\theta+\sigma\cos^9\theta+O(\sigma^4)$ → т. D в $\pi$ |
| D3 | $(z^2-\rho^4)^2+z^2y^2\rho^4+x^{11}$ | $1$, $8$, $2$ | $(\varepsilon^2-1)^2$ | (Z), (R), $G\equiv0$: $\varepsilon^{*2}=1-\frac12\sigma^2\sin^2\theta$, $\hat G_\pm=\sigma^2\sin^2\theta+\sigma^3\cos^{11}\theta-\frac14\sigma^4\sin^4\theta$; уточнение $\kappa'=2$, $G'=\sin^2\theta$ → т. D в $\pi$ |

Пояснения (все выкладки точные).

- **W1.** $\varphi=(y-s\cos^2\theta)^4+sG(\theta)+s^2\sin\theta\,y^5$, $N=4$, $\tilde U=(\varepsilon-\sigma^3\cos^2\theta)^4+G+\sigma^9\sin\theta\,\varepsilon^5$. $G=g(\cos\theta)$,
  $g(c)=\frac12c(3-c^2)$, $g'(c)=\frac32(1-c^2)\ge0$ на $[-1,1]$: минимум $-1$ только при $\theta=\pi$. Ветвь $\varepsilon_b\equiv0$
  кратности 3 при всех $\theta$ ((CM)). Точная критическая точка при $\sigma>0$ — простой корень
  $4(\varepsilon-\sigma^3\cos^2\theta)^3+5\sigma^9\sin\theta\,\varepsilon^4=0$, так что кратность при $\sigma>0$ равна 1, а (UR1) нарушено. Для теоремы W это не
  важно: она берёт приближённое дно $y_0=0$. Профиль $P=G(\pi+\tau)+1+e^4$, (W2) с $c_2\equiv c$.
- **W2.** $\varphi=y^4+s(9-8\sin^4\theta)y+s^2\cos^6\theta+s^2\sin\theta\,y^5$. $f=9-8\sin^4\theta=-2u^2+4u+7$, $u=\cos2\theta$, так что
  $f\in[1,9]$, максимум $9$ — в $\theta=0,\pi$, $f(\tau)=9-8\tau^4+\dots$. Единственная критическая точка
  $\varepsilon_0=-(f/4)^{1/3}$ невырождена ($\Phi_0''=12\varepsilon_0^2$): (R), $r'=1$. $G=-3\cdot4^{-4/3}f^{4/3}$, $G(\tau)-G(0)=4\cdot2^{1/3}3^{2/3}\tau^4+\dots$ ($p=2$).
- **W3.** $\varphi=y^4+s\sin\theta\,y^2-s^2\cos^2\theta+s^2\cos\theta\,y^5+s^3\sin^7\theta$, $N=2$. $\Phi_0+1=(\varepsilon^2+\frac12\sin\theta)^2+\frac34\sin^2\theta\ge0$,
  равенство только при $\sin\theta=0$, $\varepsilon=0$. В $\theta=0$ критическая точка $\varepsilon=0$ тройная, а при $\sin\theta<0$ их три:
  (CM) нарушено. $P(\tau,e)=e^4+\sin\tau\,e^2+\sin^2\tau$ и
  $$\tau\partial_\tau P+\tfrac12e\partial_eP-2P=(\tau\cos\tau-\sin\tau)(e^2+2\sin\tau)$$
  (тождество, `examples_mult.py`). Оценка при $|\tau|\le0{.}2$ [Доказано]:
  - $P=(e^2+\frac12\sin\tau)^2+\frac34\sin^2\tau\ge\frac34\sin^2\tau$ и $P=(\sin\tau+\frac12e^2)^2+\frac34e^4\ge\frac34e^4$, откуда
    $P\ge\frac38(\sin^2\tau+e^4)\ge0{.}36(\tau^2+e^4)$ ($\sin\tau\ge0{.}99\,\tau$ при $0\le\tau\le0{.}2$);
  - $|\tau\cos\tau-\sin\tau|\le|\tau|^3/3$ (знакочередующийся ряд $-\frac{\tau^3}3+\frac{\tau^5}{30}-\dots$) и $\tau^2e^2\le\frac12(\tau^2+e^4)$, так что модуль
    правой части не больше $\frac{|\tau|^3}3(e^2+2|\tau|)\le(\frac{|\tau|}6+\frac23\tau^2)(\tau^2+e^4)\le0{.}17P$.

  Значит, $\tau\partial_\tau P+\frac12e\partial_eP\ge1{.}8P$: (DE) выполнено с $w=\frac12$, $\mu_0=1$. (W1) следует из той же нижней
  оценки. [Эксперимент, `check_DE.py`: на сетке $201\times201$ в $|\tau|\le0{.}2$, $|e|\le1$
  $\min P/(\tau^2+e^4)=0{.}497$, $\min(\tau P_\tau+\frac12eP_e)/P=1{.}971$.]
- **W4.** $\tilde U=(\varepsilon^2-1)^2+\sigma^2\cos^8\theta\,\varepsilon$ ($N=1$). Ветви $\pm1$ невырождены (R); $G_\pm\equiv0$, это случай (Z). Точные ветви
  $\varepsilon^*=\pm1-\frac18\sigma^2\cos^8\theta+O(\sigma^4)$, $\hat G_\pm=\pm\sigma^2\cos^8\theta+O(\sigma^4)$: $\kappa'=2$. На ветви $-1$ $G'=-\cos^8\theta$ имеет
  невырожденный минимум $-1$ в $0,\pi$. Глубина $-s^{10}$. Критическая точка $0$ **не изолирована**: на
  кривых $\{x=0,\ z=\pm y^2\}$ $\nabla U=0$. W4i $:=$ W4 $+\,y^{11}$ изолирована ([Эксперимент], Грёбнер), структура та же
  ($y^{11}$ даёт $\sigma^3\sin^{11}\theta$ в $\tilde U$).
- **C1.** $\tilde U=(\varepsilon+\sigma\sin\theta\cos\theta)^4-1+\sigma^2\cos^7\theta+\sigma^5\sin^4\theta\,\varepsilon^3$ ($N=2$): $G\equiv-1$, ветвь $\varepsilon=0$ кратности 3
  на всей окружности; член $\sigma^5\varepsilon^3$ ломает (UR1), теорема C его не требует.
- **C2.** $\tilde U=\varepsilon^4+\varepsilon+\sigma^5\sin^7\theta+\sigma^6\cos^6\theta\,\varepsilon$ ($N=3$): $\varepsilon_0=-4^{-1/3}$, $G=-\frac38\,2^{1/3}\approx-0{.}4725$ для всех $\theta$.
- **D1.** $\tilde U-(\varepsilon-\varepsilon^*)^4=\sin^2\theta+\sigma^2\cos^7\theta$ тождественно: (UR) с одной глобальной ветвью, $r'=2$, $M\equiv1$. В $\theta=\pi$:
  $f(\sigma,\tau)=\sin^2\tau-\sigma^2\cos^7\tau$, $\partial_\tau f=\sin\tau\cos\tau(2+7\sigma^2\cos^5\tau)$ — полярная кривая $\tau=0$, $f(\sigma,0)=-\sigma^2$,
  $\sigma^{-2}f(\sigma,\sigma b)\to b^2-1$. Значит, в $\sigma$: глубина $\sigma^2$, ширина $\sigma$, $Q_V=b^2$. После замены $t\mapsto t^2$
  ($2r'=4\mid\Gamma_V$): $\beta_d=7$, $\alpha=\frac12$, $c'=\frac74$. Изолированность $0$ [Доказано вручную]: из $\partial_zU=4P^3$
  ($P:=z-xy-x^3$) $P=0$; тогда $\partial_yU=2y\rho^2(\rho^2+2y^2)=0$ даёт $y=0$, $\partial_xU=7x^6=0$ даёт $x=0$, и $z=0$.
- **D2.** $\tilde U=(\varepsilon^2-1)^2+\sin^2\theta+\sigma\cos^9\theta+\sigma^4\cos^6\theta\,\varepsilon^3$ ($N=1$); ветви $\pm1$, $\hat G_\pm=\sin^2\theta+\sigma\cos^9\theta\pm\sigma^4\cos^6\theta+O(\sigma^5)$.
  В $\pi$: $\sigma^{-1}\hat G_\pm(\sigma,\pi+\sigma^{1/2}b)\to b^2-1$, глубина $-s^9$.
- **D3.** Точная ветвь $\varepsilon^{*2}=1-\frac12\sigma^2\sin^2\theta$ (критическая точка — тождество). $\hat G_\pm$ — в таблице; $G'=\sin^2\theta$, далее
  $\hat G'=\sin^2\theta+\sigma\cos^{11}\theta-\frac14\sigma^2\sin^4\theta$; в $\pi$ глубина $-\sigma$, то есть $F_{\rm fl}\approx-s^{11}$.

### 10.2. Примеры вне теорем

- **O2 (складка; открытый случай).** $U=z^4-2z^2y\rho^2-x^2\rho^4+x^7+y^7$, $\gamma_*=\frac12$, $j=6$,
  $\Phi_0=(\varepsilon^2-\sin\theta)^2-1$. $G_{\min}\equiv-1$ на дуге $[0,\pi]$ (две невырожденные ветви $\varepsilon=\pm\sqrt{\sin\theta}$) и
  $G_{\min}=-\cos^2\theta>-1$ вне её. Минимальное дно — овал $\{\varepsilon^2=\sin\theta,\ 0\le\theta\le\pi\}$ со складками в $\theta=0,\pi$. Там
  $\varepsilon=0$ — тройная критическая точка, которая при $\theta>0$ расщепляется: (CM) нарушено, профиль
  $P(\tau,e)=(e^2-\sin\tau)^2$ имеет неизолированный нуль. Внутри дуги ветви невырождены, но $G_b\equiv-1$. Ни
  одно из условий (W-a)–(W-c) не выполнено. $0$ изолирована ([Эксперимент], Грёбнер; без $y^7$ ось $y$
  состоит из критических точек).
- **O1 (расщепление без диагонального поля Эйлера).** $r=3$, первое ребро с $\gamma_*=3$,
  $\Phi_0=-1+G_1(\hat\theta,\varepsilon)G_2(\hat\theta,\varepsilon)$, $\hat\theta=\sin\theta\cos\theta$, $G_1=\varepsilon^2+k\hat\theta^2\varepsilon+\hat\theta^4$, $G_2=\hat\theta^2+k\hat\theta\varepsilon^2+\varepsilon^4$,
  $\frac{8\sqrt3}7\le k<2$. Такой $\Phi_0$ реализуется многочленом $U=z^6+\sum_{l<6}z^lh_l(x,y)$, $\deg h_l=4(6-l)$:
  точки $(4(6-l)+l-6,\,l)=(3(6-l),l)$ лежат на ребре $i=3(6-l)$; все $h_l|_{S^1}$ — многочлены от $\hat\theta$ нужной
  чётности, степени хватает. Минимальное дно — точки $\hat\theta=0$, $\varepsilon=0$. Главная часть профиля $G_1G_2$ не
  имеет диагонального поля Эйлера ни с какими весами ([009], предложение 5.4). [Гипотеза] То же верно и
  для полного профиля. Условия W′ здесь не выполнены. Пример не проверялся численно.

### 10.3. Эксперименты

Все результаты этого раздела — [Эксперимент], не доказательство. Запуск:
`~/venv/bin/python <скрипт>` из `experiments/prover/morse-bott-mult/`.

- `frames_W.py` → `frames_W.out`: тождества (5.1)–(5.7), разложение $w$ и формула (5.6) — 16 проверок `OK` (sympy;
  общие $k_g$ и дно Пюизё, $\lambda$ — символ). Отрицательный контроль: без членов с $\lambda$ в (5.4), (5.5) проверки
  этих формул дают `FAIL`.
- `examples_mult.py` → `examples_mult.out`: данные §10.1–10.2 (точная арифметика).
- `check_DE.py` → `check_DE.out`: профиль W3. При весе $c_2=c=\frac32$ отношение $\min(\kappa\tau P_\tau+ceP_e)/P$ равно $-0{.}358$,
  $-0{.}251$, $-0{.}039$, $+0{.}174$ при $\kappa=0{.}05,0{.}1,0{.}2,0{.}3$. Наивное поле Mb годится лишь при $\kappa\gtrsim0{.}22$, ср. §5.3.
- `floor_mult.py` → `floor_mult.out`: функция дна (минимум по слою — через корни $\partial_y\varphi$, mpmath, 50 знаков) при
  $s=10^{-2},10^{-3},10^{-4},10^{-6}$. Предсказания подтверждаются:
  - W1, W3, W4: $\min_\theta F_{\rm fl}/s^{j}\to-1$, у W4 $j=10$ после уточнения; W2: $-8{.}79905$, $-8{.}83502$, $-8{.}84285$, $-8{.}84490$
    против $G(0)=-8{.}84500$, угловое положение минимума сходится медленно (вырожденный минимум);
  - C1: $F_{\rm fl}/s^6\in[-1-s,-1+s]$ равномерно по $\theta$; C2: $F_{\rm fl}/s^{16/3}\to-0{.}4724704$ равномерно;
  - D1, D2, D3: $\min_\theta F_{\rm fl}/s^{\beta_d}\to-1$ ($\beta_d=7,9,11$), минимум при $\theta=\pi$.
- `exit_W.py` → `exit_W1.out`, `exit_W2.out`, `exit_W3.out` и `*_deep.out`: строгий выход (A5) конструкции теоремы W прямым
  численным дифференцированием $\Xi=\frac d{dt}(V-\delta\rho^\beta)$ вдоль потока. Точки множества выхода выбираются в $D$, по 16
  направлений $v_\perp$, контроль $|V-\delta\rho^\beta|/(\delta\rho^\beta)<10^{-12}$; печатается $\min(\rho/\lambda_v)\Xi/(\delta\rho^\beta)$ (нужно $>0$).
  - **W3** (профиль не распадается). Поле теоремы W ($\lambda=c-\frac\kappa2$): $0{.}0995$, $0{.}197$, $0{.}295$ при $\kappa=0{.}05,0{.}1,0{.}2$
    ($\delta=0{.}01$) и $0{.}0999$, $0{.}185$, $0{.}345$ ($\delta=0{.}002$), то есть $\approx2\kappa=\kappa\mu_0$. Поле Mb ($\lambda=0$): $-0{.}357$, $-0{.}249$,
    $-0{.}035$ и $-0{.}309$, $-0{.}202$, $+0{.}012$ — выход нарушается, причём значения совпадают с минимумом отношения
    Эйлера из `check_DE.out`. В глубоком режиме ($s\sim10^{-13}$–$10^{-17}$) числа те же.
  - **W1** ($p=2$, $r'=2$). В глубоком режиме ($s\le10^{-16}$) оба поля дают положительный выход при $\kappa\le0{.}1$
    ($\delta=0{.}01$) и $\kappa\le0{.}05$ ($\delta=0{.}002$) и отрицательный при $\kappa=0{.}2$, соответственно $\kappa=0{.}1$. Это согласуется с
    $\kappa(\delta)\asymp\delta^{1/2}$ при $p=2$, как у R26 для Mb. При $s\sim10^{-3}$ поле с $\lambda=c-\kappa$ ещё не в асимптотическом режиме
    (вклад $\lambda s^{c-1}|e|$ в $\vartheta_1$ при $c-1=\frac14$).
  - **W2** ($p=2$, дно Пюизё $\eta_0=s^{4/3}\varepsilon_0(\theta)$). Нужно $s\lesssim10^{-20}$ (наклон дна $\sim s^{1/3}$). Тогда выход
    положителен при $\kappa\le0{.}1$ ($\delta=0{.}01$) и $\kappa=0{.}02$ ($\delta=0{.}002$), отрицателен при больших $\kappa$.
- `isolated.py` → `iso_*.out`: нульмерность идеала $(\partial_xU,\partial_yU,\partial_zU)$ (базис Грёбнера, sympy). Изолированы (над
  $\mathbb C$, значит, и над $\mathbb R$) W1, W2, W3, W4i, C1, C2, D2, D3, O2. Для W4 идеал не нульмерен (и $0$ действительно не
  изолирована). Для D1 изолированность доказана вручную. Для теорем изолированность не нужна.

## 11. Где работают аналитичность и изолированность

1. **Изолированность не используется** нигде: ни в предложении R′, ни в теоремах W, C, D, Z, M′.
   Единственные места, где в прежних работах она «останавливала процесс» ($\gamma_*=\infty$; $\hat G\equiv0$), здесь
   закрыты отрицательными значениями $U$. При $\gamma_*=\infty$ $U\ge0$ в трубке (предложение R′, п. 4). При
   $\hat G_g\equiv0$ отрицательных значений на ветви нет (теорема Z, п. 4). Пример W4 с неизолированной
   критической точкой покрыт.
2. **Аналитичность работает:**
   - (i) лемма A0: гладкая компонента-кривая с постоянной кратностью аналитична (через аналитическую
     функцию $X^{2r-1}(u_m\circ\chi)$);
   - (ii) первое ребро и лемма N1: конечный носитель на ребре, $\Phi_0$ — многочлен по $\varepsilon$ с аналитическими
     коэффициентами, $\tilde U$ сходится и аналитична в $\sigma=0$ — это даёт (2.1) с непрерывным $\tilde F$; $\gamma_*<\infty$ при
     наличии отрицательных значений. Для $C^\infty$-функции все $\varphi_{il}$ могут быть нулями при ненулевой
     плоской добавке, и первого ребра нет;
   - (iii) дихотомия «конечный порядок или константа» для аналитических $G_b$, $G'$ на окружности:
     предложение W′ (W-a)/(W-c), теорема Z. Изолированность нулей $G\ge0$, $G\not\equiv0$ — для леммы V;
   - (iv) ветви: аналитическая теорема о неявной функции (лемма U), теорема единственности при
     продолжении ветвей (леммы B, B′); конечность порядка $\kappa'$ в уточнении (теорема Z, п. 4);
   - (v) лемма V [010] (Вейерштрасс, Ньютон–Пюизё) в теореме D: ветвь углового минимума, глубина
     $-a_Vs^{\gamma'}$, полиномиальный профиль $Q_V$.
3. **Теоремы W, C, D** — утверждения для $U\in C^2$ при заданных данных нормальной формы; аналитичность в
   них не нужна. Вся «конечность типа» — в предположениях. С примерами Пенлеве–Уинтнера и Лалуа (по
   `problem/KNOWN_RESULTS.md`, первоисточники не сверены) противоречия нет: у них нет конечной струи,
   дающей такие данные. Пример Уреньи касается тотальной неустойчивости, а здесь утверждается одна
   асимптотическая траектория.
4. Над $\mathbb R$ и над $\mathbb C$: все рассуждения вещественные; число Милнора не используется.

## 12. Частные случаи с известным ответом

1. **$r\equiv1$ (Морс–Ботт).** (R) выполнено, теорема M′ даёт теорему M [010]. Согласование: если
   $G_{\min}\not\equiv0$, то $j$ первого ребра совпадает с $j$ из [008] ([011], замечание 2). Если $G_{\min}\equiv0$, к $j$ из [008]
   ведёт один шаг уточнения (теорема Z, п. 4).
2. **Однородный $U=u_m$.** $\varphi=u_m(\omega+yn)=y^{2r}a$, так что $\gamma_*=\infty$ на всех кривых и $U\ge0$: $0$ — минимум; теорема
   M′ ничего не утверждает. Это верно.
3. **Невырожденная младшая форма** ($u_m>0$ на $S^2$): $\Sigma=\varnothing$, строгий минимум (предложение R′, п. 1).
4. **Квазиоднородный $U=z^{2r}+v(x,y)$**, $v$ однородна степени $k>2r$. Здесь $\varphi=y^{2r}+s^{k-2r}v(\theta)$,
   $\gamma_*=\frac{k-2r}{2r}$, $\tilde U=\varepsilon^{2r}+v(\theta)$ точно: (UR) с жёсткой ветвью $\varepsilon\equiv0$. Если $\min v|_{S^1}<0$, то $G=v|_{S^1}$ имеет
   отрицательный минимум конечного порядка (теорема W) или постоянна (теорема C). Если $\min v\ge0$, то
   $U\ge0$. Ответ «траектория есть ⟺ $0$ не минимум» согласуется с известным. Плоскость $z=0$
   инвариантна, а для однородной ведущей формы без минимума асимптотические движения есть (Козлов–Паламодов
   1982 [KP82]; по `problem/KNOWN_RESULTS.md`, формулировка по Neg95, первоисточник не сверен).
5. **$n=2$.** Теорема сформулирована для $n=3$. Для $U=V(x,y)+z^{2r}$ ($V$ аналитична, младшая степень $>2r$) первое
   ребро даёт $\Phi_0=\varepsilon^{2r}+v_k(\theta)$ с жёсткой ветвью: $\tilde U$ зависит от $\varepsilon$ только через $\varepsilon^{2r}$, (UR) выполнено.
   Вывод M′ «$0$ не минимум $V$ ⇒ асимптотическая траектория» согласуется со случаем $n=2$ задачи (A)
   (теорема Паламодова для плоскости, результат 005).

## 13. Пробелы и что остаётся

**Пробелы этой записки** (то, что не доказано или опирается на непроверенное):

1. Независимой проверки нет. Новые места, требующие внимания рецензента: формулы (5.2)–(5.7) с членом
   $\lambda\zeta/s$ (проверены символьно), оценки $\vartheta_i$ равномерно по $\kappa,\lambda$ (§5.2, п. 7), выбор констант (§5.2,
   пп. 3, 8), условие (D2) и формула (7.1), леммы B, B′ (продолжение ветвей), лемма U, сборка в §9.
2. Теорема M′ доказана **только при (UR)**, а предложение W′ — при (W-a), (W-b) или (W-c). Полнота разбора для
   всех $U$ с постоянной нормальной кратностью не доказана. Остаются три типа случаев:
   - **(O1) Расщепление ветви без диагонального поля Эйлера.** В точке минимального дна (CM) нарушено,
     и профиль $P$ не имеет поля $\tau\partial_\tau+we\partial_e$ с (DE) ни при каком $w$ (пример O1, §10.2). Нужно недиагональное
     поле Эйлера (лемма E [009]) и вариант теоремы W со «свободным $Y$» (`notes/main-agent/2026-10-21-free-Y.md`).
     Трудность: угловая компонента поля не должна зависеть от узкой нормальной координаты. Иначе
     $s\langle w,D_wY\rangle$ содержит член порядка $s^{1-c}$ — это условие $\partial_j\zeta_i\equiv0$ при $c_i<c_j$ из записки ГА. Следствие 6.1
     [009] даёт такое поле лишь при $Q_d(0,1)\ne0$, а у $G_1G_2$ это не так. Теорема 2U из
     `results/012-free-field.md` (свободное поле в прямой карте; на момент записи ждёт проверки текста)
     сюда напрямую не переносится: там все поперечные направления узкие, а здесь угловое широкое (не
     проверялось подробно). [Гипотеза] Траектория есть.
   - **(O2) Складки минимального дна.** $G_{\min}$ постоянна на дуге, но не на всей окружности, и ветви
     сливаются на концах дуги (пример O2). Угловая структура задаётся старшими порядками по $\sigma$. Порядки
     выше главного не видны в рамках фиксированного $\delta$ (стенки нужны той же глубины, что и $\delta\rho^\beta$), а
     трубка вокруг всей окружности (теорема C) неприменима. Поле, следующее за овалом дна около
     складки, должно поворачивать угол в зависимости от узкой координаты $e$ — та же трудность, что в (O1).
     [Гипотеза] Траектория есть.
   - **(O3) Каскад при нежёстком вырожденном профиле.** $\min G_{\min}=0$, а ветвь дна в слое не постоянной
     кратности (её кратность при $\sigma>0$ меньше, чем при $\sigma=0$), или ветви меняют структуру около $\theta_*$, и
     никакое приближённое дно не даёт (D2). Тогда профиль в переменных $(t,b_1,b_2)$ задаётся трёхмерным
     многогранником Ньютона, и неравенство Эйлера с диагональными весами не гарантировано. Член вида
     $t^{2A_V+2B}b_1^2b_2^2$ может оказаться ниже глубины. (D2) — достаточное условие, проверяемое на струе.
3. Касание луча траекторией в теоремах W, C не доказано (только конус раствора $R_\theta(\delta)$ в W; в C угол
   не контролируется). В теореме D касание есть.
4. (UR) в общем случае трудно проверить. Проверяемые достаточные условия — (R) (лемма U) и явная
   факторизация с точной ветвью, как в D1. Из изолированности критической точки (UR) и условия W′ не
   следуют: в примере O2 $0$ изолирована ([Эксперимент], Грёбнер), а (CM) в складках нарушено и
   (W-a)–(W-c) не выполнены (§10.2, это [Доказано]).

**Что остаётся вне записки** (этим занимаются другие агенты): переменная нормальная кратность вдоль
кривой (точки, где $a(\theta,0)=0$); вырожденные точечные компоненты; особые точки $\Sigma$; $n\ge4$.

## 14. Статус

- Лемма A0, лемма T, предложение R′, теоремы W, C, D, леммы B, B′, U, предложение W′, теорема Z,
  **теорема M′** (при (UR)) и следствие M′$_R$ — **[Доказано]**, при опоре на [007], [008], [010], [011] (проверены
  агентами-рецензентами, ждут проверки человеком). Независимой проверки этой записки нет.
- Общая теорема «$n=3$, $u_m\ge0$, $\Sigma$ гладкое с постоянной нормальной кратностью на кривых,
  невырожденные точки, $0$ не минимум ⇒ асимптотическая траектория» **без (UR)** — **[Гипотеза]**:
  препятствия (O1)–(O3) не сняты.
- Примеры §10.1: условия теорем проверены вручную [Доказано]; численные проверки — [Эксперимент].
