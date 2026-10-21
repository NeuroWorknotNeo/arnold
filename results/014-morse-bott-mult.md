# 014. Постоянная нормальная кратность кривых нулей младшей формы ($n=3$): широкий овраг, трубка, каскад и теорема M′

- **Статус:** [Проверено: reviewer R40, R41 (агенты), 21.10.2026 — доказательства в записке
  [`notes/prover/2026-10-21-morse-bott-mult.md`](../notes/prover/2026-10-21-morse-bott-mult.md); reviewer R43, R44
  (агенты), 21.10.2026 — текст этого результата целиком: ошибок нет]; ждёт проверки человеком.
  - R43 ([`notes/reviewer/2026-10-21-result014-A.md`](../notes/reviewer/2026-10-21-result014-A.md)): условия, теорема
    M′ (формулировка), леммы A0, T, предложение R′ (полно без изолированности), теорема W, леммы B, U, B′.
  - R44 ([`notes/reviewer/2026-10-21-result014-B.md`](../notes/reviewer/2026-10-21-result014-B.md)): теоремы C, D,
    предложение W′, теорема Z, теорема M′ и следствие M′$_R$, вывод теоремы M через лемму Адамара.
  - Редакционные правки по R43, R44 («Отличия от записки», пп. 6–19) внёс автор оформления; главный агент
    прочитал их, в том числе наблюдение (UR0) (распаковка определения (UR)) и доказательство для примера O2,
    и заменил фразу «задача (A) решена» на «(A) выполнено в этом классе».
  - R40 (reviewer, агент, 21.10.2026,
    [`notes/reviewer/2026-10-21-morse-bott-mult-A.md`](../notes/reviewer/2026-10-21-morse-bott-mult-A.md)): формулы
    (2.4), (5.1)–(5.7) записки (здесь (0.9), (3.1)–(3.7)), теорема W, леммы B, U, B′. Ошибок нет; формулы
    пересчитаны символьно и численно в $\mathbb R^3$, строгий выход для W3 проверен независимо. Замечания З1–З12
    редакционные.
  - R41 ([`...-B.md`](../notes/reviewer/2026-10-21-morse-bott-mult-B.md)): лемма A0, лемма T, предложения R′, W′,
    теоремы C, D, Z, M′, следствие M′$_R$, разделы об аналитичности и частных случаях, пример O2. Ошибок нет;
    замечания З1–З9 редакционные.
  - Все замечания R40, R41 учтены во второй редакции записки (её §15) и здесь (раздел «Отличия от записки»).
  - Метки: всё в разделе «Утверждение» — [Доказано]. Замечания помечены каждое отдельно.
- **Автор:** prover (агент), записка `notes/prover/2026-10-21-morse-bott-mult.md` (21.10.2026). Оформление —
  prover (агент), 21.10.2026.
- **Зависит от** (все — [Проверено агентами]; ждут проверки человеком):
  - [007] = [`results/007-gt3.md`](007-gt3.md): теорема A, лемма 1, лемма 2 (константы (3.1)), теорема 2 (класс (GT3),
    условия $(\Phi0)$–$(\Phi3)$, (F), $(V_0)$; пп. 1, 3, 4; п. 1 шага 6 доказательства);
  - [008] = [`results/008-class-K.md`](008-class-K.md): §1 (формула (1.1)), данные (S), лемма K1, лемма K3 (в том числе для
    замкнутой кривой), теорема K0, доказательство предложения K4(c) (§11);
  - [010] = [`results/010-morse-bott.md`](010-morse-bott.md): лемма N, п. (N3); лемма M (§4); лемма V (§7); доказательство
    теоремы Md, §8, пп. 1–5 (формулы (8.1)–(8.3));
  - [011] = [`results/011-normal-multiplicity.md`](011-normal-multiplicity.md): утверждение 1 (первое ребро), леммы N1, N2
    (формулировки и пп. 3–5 доказательства), лемма N5 (§7 доказательства);
  - стандартные факты: аналитическая теорема о неявной функции, теорема единственности для аналитических
    функций, формула Тейлора с интегральным остатком, лемма Адамара; через лемму V [010] — подготовительная
    теорема Вейерштрасса и теорема Ньютона–Пюизё (формулировки в [010], §7; с первоисточниками не сверены);
  - только в замечаниях: [009] = [`results/009-euler-field.md`](009-euler-field.md) (предложения 5.2, 5.4, следствие 6.1),
    [012] = [`results/012-free-field.md`](012-free-field.md) (теорема 2U).
- **Проверочные скрипты** [Эксперимент]:
  - [`experiments/prover/morse-bott-mult/`](../experiments/prover/morse-bott-mult/) — автор записки (`frames_W.py`,
    `examples_mult.py`, `check_DE.py`, `floor_mult.py`, `exit_W.py`, `exit_W3_wall.py`, `isolated.py`);
  - `experiments/reviewer/morse-bott-mult-R40/`, `experiments/reviewer/morse-bott-mult-R41/` — рецензенты.

## Утверждение

### Обозначения и условия (H)

$n=3$, $B_r=\{|q|<r\}$, система $\ddot q=-\nabla U(q)$. **Асимптотическая траектория** — решение $q(t)\ne0$, $t\ge0$, с
$q(t)\to0$, $\dot q(t)\to0$ при $t\to+\infty$; из её существования следует неустойчивость по Ляпунову ([007], теорема A,
шаг 6). Обозначения $p,h,v_\perp,K_\perp,W,V,\lambda,\Xi$, условия (D1)–(D4), (A4), (A5), (L0)–(L3) — как в [007]; буква $\lambda$
дальше — только $\lambda=-p/h$ из [007], а нормальный вес поля в теореме W обозначен $\lambda_n$. Буква $n$ — и размерность
($n=3$), и нормаль $n(\theta)$; $E$ — константа леммы N2 (энергия [007] явно не используется), трубчатое отображение —
$\mathcal E(\theta,y)$; $K$ — квадрат $K_W$ теоремы W, $K_\perp$ — из [007].

- **(H1)** $U$ вещественно-аналитична в окрестности $0$, $U(0)=0$, $U=\sum_{k\ge m}u_k$ ($u_k$ — однородные многочлены),
  $m\ge2$, $u_m\ge0$, $u_m\not\equiv0$. Тогда $m$ чётно, $\nabla U(0)=0$, $Z:=\{u_m=0\}=\{\nabla u_m=0\}$.
- **(H2)** $\Sigma:=Z\cap S^2$ — гладкое ($C^\infty$) компактное подмногообразие $S^2$; его компонент конечное число — точки
  и замкнутые кривые.
- **(H3)** В каждой точечной компоненте $\{\omega\}$: $D^2u_m(\omega)|_{\omega^\perp}\succ0$.
- **(H4)** Для каждой компоненты-кривой $\Sigma_0$ есть $r=r(\Sigma_0)\in\mathbb N$ такое, что около $\Sigma_0$ на $S^2$ $u_m=\tau_\Sigma^{2r}g_\Sigma$, где
  $\tau_\Sigma$, $g_\Sigma$ — $C^\infty$-функции, $\tau_\Sigma|_{\Sigma_0}=0$, $d\tau_\Sigma\ne0$ на $\Sigma_0$, $g_\Sigma>0$ («постоянная нормальная кратность $2r$»).

Изолированность критической точки $0$ не предполагается.

### Данные на компоненте-кривой

По лемме A0 ниже компонента-кривая $\Sigma_0$ аналитична; $\omega:\mathbb R\to\Sigma_0$ — натуральная $L$-периодическая
аналитическая параметризация, $\ell=\omega'$, $n=\omega\times\ell$, $k_g$ — геодезическая кривизна:
$$\omega'=\ell,\qquad\ell'=-\omega+k_gn,\qquad n'=-k_g\ell. \tag{0.1}$$
$\Pi(s,\theta,\eta)=s\omega(\theta)+\eta n(\theta)$ — аналитический диффеоморфизм $\{s>0,\ \theta\in\mathbb R/L\mathbb Z,\ |\eta|<t_1s\}$ на открытое
подмножество $\mathbb R^3\setminus0$, $|\Pi|^2=s^2+\eta^2$, $\nabla s=\omega(\theta)$ (лемма K3 [008] для замкнутой кривой; [010], (N3)).

- $\varphi(s,\theta,y):=\sum_{k\ge m}s^{k-m}u_k(\omega(\theta)+yn(\theta))$ аналитична на $(-R_0/3,R_0/3)\times\mathbb R\times(-1,1)$, $L$-периодична,
  $U(s(\omega+yn))=s^m\varphi$ ([008], (1.1)); $\varphi_{il}(\theta):=\frac1{i!\,l!}\partial_s^i\partial_y^l\varphi(0,\theta,0)$, $\mathcal S:=\{(i,l):\ \varphi_{il}\not\equiv0\}$. По (M)
  (лемма A0) $(0,l)\notin\mathcal S$ при $l<2r$ и $\varphi_{0,2r}=a(\cdot,0)>0$.
- Если $\mathcal S\cap\{l<2r\}\ne\varnothing$ — **первое ребро** ([011], утверждение 1): $\gamma_*:=\min\{\frac i{2r-l}:\ (i,l)\in\mathcal S,\ l<2r\}>0$,
  $N$ — знаменатель $\gamma_*$, $j:=m+2r\gamma_*$, $c:=1+\gamma_*$,
  $$\Phi_0(\theta,\varepsilon):=\sum_{(i,l)\in\mathcal S,\ i+\gamma_*l=2r\gamma_*}\varphi_{il}(\theta)\varepsilon^l=a(\theta,0)\varepsilon^{2r}+\sum_{l<2r}\varphi_{\gamma_*(2r-l),l}(\theta)\varepsilon^l \tag{0.2}$$
  — многочлен по $\varepsilon$ степени $2r$ с аналитическими $L$-периодическими коэффициентами, $a(\theta,0)>0$;
  $G_{\min}(\theta):=\min_\varepsilon\Phi_0(\theta,\varepsilon)$ — непрерывна и периодична. Иначе пишем $\gamma_*=\infty$; тогда $\varphi=y^{2r}A_\varphi$, $A_\varphi$ аналитична,
  $A_\varphi(0,\theta,0)=a(\theta,0)$ (§2, п. 4).
- **Дно уровня $c_0$**: $F_{c_0}:=\{(\theta,\varepsilon):\ \Phi_0(\theta,\varepsilon)=G_{\min}(\theta)=c_0\}$; **минимальное дно** $F_{\min}:=F_{\min G_{\min}}$ (непусто, его
  точки — точки глобального минимума $\Phi_0(\theta,\cdot)$).
- **Лемма N1 на окружности** ([011]). Доказательства лемм N1, N2 ([011], §2–§3) используют только аналитичность $\varphi$ в
  окрестности компакта $\Lambda=[0,L]$ (оценки Коши) и условие (M), но не инъективность дуги; коэффициенты $\varphi_{il}$
  периодичны, поэтому утверждения на $[0,L]$ переносятся на $\mathbb R$. Для $E'>0$ есть $\sigma_1>0$: $\tilde U(\sigma,\theta,\varepsilon):=\sum_{\mathcal S}\varphi_{il}(\theta)\sigma^{N(i+\gamma_*l-2r\gamma_*)}\varepsilon^l$ вещественно-аналитична
  в окрестности $[-\sigma_1,\sigma_1]\times\mathbb R\times[-E',E']$, $L$-периодична, $\tilde U(0,\cdot)=\Phi_0$ и
  $$U\big(s\omega(\theta)+s^c\varepsilon\,n(\theta)\big)=s^j\tilde U(s^{1/N},\theta,\varepsilon),\qquad0<s<\sigma_1^N,\ |\varepsilon|\le E'. \tag{0.3}$$
- **Лемма N2 на окружности** ([011], включая пп. 3–5 доказательства). Есть $E_0$, $y_2\in(0,1)$, $E\ge\max(1,E_0)$ и для каждого
  $y_1\in(0,y_2]$ число $s_2(y_1)\in(0,\sigma_1(E+1)^N]$ ($\sigma_1(E+1)$ — число леммы N1 при $E'=E+1$) такие, что: (a) при
  каждом $\theta$ точки глобального минимума $\Phi_0(\theta,\cdot)$ лежат в $(-E_0,E_0)$; при $0<s<s_2(y_1)$, $\theta\in\mathbb R$: (b) точки минимума $\varphi(s,\theta,\cdot)$ на $|y|\le y_1$ лежат в $|y|\le Es^{\gamma_*}$, и
  $\min_{|y|\le y_1}\varphi=s^{2r\gamma_*}\min_{|\varepsilon|\le E}\tilde U(s^{1/N},\theta,\varepsilon)$; (c) **функция дна**
  $$F_{\rm fl}(s,\theta):=\min_{|\eta|\le y_1s}U(s\omega(\theta)+\eta n(\theta))=s^j\big(G_{\min}(\theta)+O(s^{1/N})\big)\ \text{равномерно по }\theta. \tag{0.4}$$
  Числа $E_0$, $E$ и $\sigma_1:=\sigma_1(E+1)$ фиксируются раз и навсегда; ниже $\tilde U$ рассматривается при $|\varepsilon|\le E+1$, и
  условие (UR) формулируется относительно этих $E$, $\sigma_1$.

### Условия на ветви

- **(CM)** (постоянная кратность) в точке $(\theta',\varepsilon')$ с $\partial_\varepsilon\Phi_0(\theta',\varepsilon')=0$: есть $\rho_\theta>0$, $r'\in\mathbb N$ и аналитическая
  $\varepsilon_b$ на $(\theta'-\rho_\theta,\theta'+\rho_\theta)$, $\varepsilon_b(\theta')=\varepsilon'$, такие, что
  $$\Phi_0\big(\theta,\varepsilon_b(\theta)+e\big)=G_b(\theta)+e^{2r'}\mathsf p(\theta,e),\qquad G_b(\theta):=\Phi_0(\theta,\varepsilon_b(\theta)), \tag{0.5}$$
  где $\mathsf p$ — многочлен по $e$ с аналитическими по $\theta$ коэффициентами и $\mathsf p(\theta,0)>0$ при $|\theta-\theta'|<\rho_\theta$.
  (Так как $\Phi_0(\theta,\varepsilon_b+e)-G_b$ — многочлен по $e$, делящийся на $e^{2r'}$, частное $\mathsf p$ — многочлен; отдельный радиус по
  $e$ не нужен.) **Обоснование двух свойств.** (i) Если $\varepsilon'$ — критическая точка кратности $2r'-1$ с $\partial_\varepsilon^{2r'}\Phi_0(\theta',\varepsilon')>0$,
  то (CM) равносильно тому, что для ветви $\varepsilon_b$ простого корня $\partial_\varepsilon^{2r'-1}\Phi_0(\theta,\cdot)$ через $\varepsilon'$ (теорема о неявной
  функции) $\partial_\varepsilon^k\Phi_0(\theta,\varepsilon_b(\theta))\equiv0$, $1\le k\le2r'-2$: если (0.5), то $\partial_\varepsilon^k\Phi_0(\theta,\varepsilon_b)=0$ при $1\le k\le2r'-1$ и
  $\partial_\varepsilon^{2r'}\Phi_0(\theta,\varepsilon_b)=(2r')!\,\mathsf p(\theta,0)>0$, то есть $\varepsilon_b$ — та самая ветвь; обратно, формула Тейлора многочлена по $e$
  даёт (0.5) с $\mathsf p=\sum_{k\ge2r'}\frac1{k!}\partial_\varepsilon^k\Phi_0(\theta,\varepsilon_b)e^{k-2r'}$. (ii) Единственность: $\partial_e(e^{2r'}\mathsf p)=e^{2r'-1}(2r'\mathsf p+e\partial_e\mathsf p)$, и
  $2r'\mathsf p+e\partial_e\mathsf p>0$ при $|\theta-\theta'|\le\rho_\theta/2$, $|e|\le\rho'$ для некоторого $\rho'>0$ (компактность); поэтому при этих $\theta$
  единственная критическая точка $\Phi_0(\theta,\cdot)$ в $|\varepsilon-\varepsilon_b(\theta)|<\rho'$ — это $\varepsilon_b(\theta)$ (на меньшем интервале, чем интервал (CM)).
- **(DE)** в точке $(\theta_0,\varepsilon_0)\in F_{\min}$: для $P(\tau,e):=\Phi_0(\theta_0+\tau,\varepsilon_0+e)-\min G_{\min}$ ($P\ge0$, $P(0,0)=0$): **(W1)** $(0,0)$ —
  изолированный нуль $P$; **(DE)** есть $w,\mu_0,r_*>0$ с $\tau\partial_\tau P+w\,e\,\partial_eP\ge\mu_0P$ на $[-r_*,r_*]^2$.
- **(UR)** на компоненте-кривой с $\gamma_*<\infty$: для каждого $\theta'\in\mathbb R$ есть открытый интервал $J\ni\theta'$, числа
  $\sigma_J\in(0,\sigma_1]$, $e_J\in(0,\frac12]$ и конечный набор «ветвей» $(\varepsilon_k^*,\hat G_k,M_k,r_k)$: $\varepsilon_k^*,\hat G_k$ вещественно-аналитичны на
  $(-\sigma_J,\sigma_J)\times J$, $|\varepsilon_k^*|<E+\frac12$ там, $M_k$ вещественно-аналитична на $(-\sigma_J,\sigma_J)\times J\times(-e_J,e_J)$, $r_k\in\mathbb N$, и
  - **(UR1)** $\tilde U(\sigma,\theta,\varepsilon_k^*(\sigma,\theta)+e)=\hat G_k(\sigma,\theta)+e^{2r_k}M_k(\sigma,\theta,e)$ при $|\sigma|<\sigma_J$, $\theta\in J$, $|e|<e_J$; $M_k(0,\theta,0)>0$ на $J$;
  - **(UR2)** при $\theta\in J$, $0\le\sigma<\sigma_J$ каждая точка глобального минимума $\tilde U(\sigma,\theta,\cdot)$ на $[-E,E]$ равна $\varepsilon_k^*(\sigma,\theta)$ при
    некотором $k$.

  (UR1) — точная ветвь критических точек постоянной кратности $2r_k-1$ («жёсткий профиль»); при $\sigma=0$ это (CM).

  **Наблюдение (UR0).** (UR) влечёт (CM) во всех точках $F_{\min}$ (более того, во всех точках глобального минимума
  $\Phi_0(\theta,\cdot)$). Действительно, такая точка $(\theta',\varepsilon')$ лежит в $(-E_0,E_0)\subset[-E,E]$ (N2(a)); по (UR2) при $\sigma=0$
  $\varepsilon'=\varepsilon_k^*(0,\theta')$ для некоторой ветви, а (UR1) при $\sigma=0$ на интервале $|\theta-\theta'|<\rho_\theta$, лежащем в $J$, — это (0.5) с
  $\varepsilon_b=\varepsilon_k^*(0,\cdot)$, $r'=r_k$ и $\mathsf p(\theta,e)=M_k(0,\theta,e)$ (многочлен по $e$: $M_k(0,\theta,e)=e^{-2r_k}(\Phi_0(\theta,\varepsilon_k^*(0,\theta)+e)-G_k(\theta))$).
  В случае (W) из (UR) нужно только это.
- **(R)** при каждом $\theta$ каждая точка глобального минимума $\Phi_0(\theta,\cdot)$ невырождена: $\partial_\varepsilon^2\Phi_0>0$. Условие на многочлен
  первого ребра; проверяется по конечной струе $U$.

### Теорема M′ (основная)

**Теорема M′.** Пусть $n=3$, выполнены (H1)–(H4), и на каждой компоненте-кривой с $\gamma_*<\infty$ выполнено (UR).
Если $0$ — не точка локального минимума $U$, то у $\ddot q=-\nabla U(q)$ есть асимптотическая траектория, и
равновесие $q=0$ неустойчиво по Ляпунову. Изолированность критической точки не предполагается.

**Следствие M′$_R$.** В теореме M′ условие (UR) можно заменить проверяемым по конечной струе условием (R)
(лемма U). При (K1), (K2) [010] (Морс–Ботт) выполнены (H1)–(H4) с $r\equiv1$ и (R); получается теорема M [010].

В частности, при $n=3$ утверждение (A) выполнено для всех $U$ с $u_m\ge0$, гладким $\Sigma$, невырожденными
точечными компонентами, постоянной нормальной кратностью на кривых и условием (R) (или (UR)) на них. Результат
проверен агентами и ждёт проверки человеком.

### Лемма A0

**Лемма A0.** При (H1), (H2), (H4) каждая компонента-кривая $\Sigma_0$ вещественно-аналитична, и
$$u_m\big(\omega(\theta)+y\,n(\theta)\big)=y^{2r}a(\theta,y),\qquad a(\theta,0)>0, \tag{M}$$
где $a$ — многочлен по $y$ с аналитическими $L$-периодическими коэффициентами.

### Лемма T и предложение R′

**Лемма T.** Пусть выполнены (H1)–(H4). Для компоненты-кривой с $\gamma_*<\infty$ возьмём $y_1\le\min(y_2,t_1)$, $s_1:=\min(s_2(y_1),R_0/3)$; для
компоненты с $\gamma_*=\infty$ — $y_1\le\min(y',t_1)$, $s_1:=\min(s',R_0/3)$, где $y'<1$ и $A_\varphi\ge\frac12\min a(\cdot,0)$ при $|s|\le s'$, $|y|\le y'$.
**Трубка** $T(\Sigma_0):=\{s\omega(\theta)+\eta n(\theta):\ 0<s<s_1,\ |\eta|<y_1s\}$; $F_{\rm fl}(s,\theta):=\min_{|\eta|\le y_1s}U(s\omega+\eta n)$ с этим $y_1$ (при $\gamma_*<\infty$
для неё верна асимптотика (0.4), при $\gamma_*=\infty$ это только определение). Для точечной компоненты $\{\omega\}$: $R_\omega$ —
функция $R$ данных (S) [008] с $d=0$, $s_1(\omega)$, $y_1(\omega)$ — числа леммы K1 [008], и, как в предложении K4 [008],
$C_\omega:=\{q:\ \langle q,\omega\rangle>0,\ |q-\langle q,\omega\rangle\omega|<\frac{y_1(\omega)}2\langle q,\omega\rangle\}$. Тогда:

- **(a)** есть $r_*>0$ такое, что каждая точка $0<|q|<r_*$ лежит в некоторой трубке, или в некотором конусе $C_\omega$, или
  $U(q)>0$;
- **(b)** на $T(\Sigma_0)$: $U(s\omega+\eta n)\ge F_{\rm fl}(s,\theta)$; на $C_\omega$ при $0<x:=\langle q,\omega\rangle<s_1(\omega)$: $U(q)\ge x^mR_\omega(x)$;
- **(c)** $0$ — точка локального минимума $U$ тогда и только тогда, когда $F_{\rm fl}\ge0$ при малых $s>0$ на всех компонентах-
  кривых и $R_\omega(s)\ge0$ при малых $s>0$ во всех точечных компонентах.

**Предложение R′.** Пусть выполнены (H1)–(H4) и $0$ — не точка локального минимума $U$. Тогда $\Sigma\ne\varnothing$ и
выполнено хотя бы одно из трёх:

- **(P)** есть точечная компонента $\{\omega\}$ с $R_\omega\not\equiv0$ и отрицательным старшим коэффициентом $R_\omega$;
- **(W)** есть компонента-кривая с $\gamma_*<\infty$ и $\min G_{\min}<0$;
- **(Z)** есть компонента-кривая с $\gamma_*<\infty$, $\min G_{\min}=0$ и $F_{\rm fl}(s_n,\theta_n)<0$ при некоторых $s_n\downarrow0$.

### Теорема W (широкий овраг; аналог Mb [010])

**Данные (NF$_W$).** $\omega:(-\theta_K,\theta_K)\to S^2$ — натуральная параметризация аналитической дуги (в том числе дуги
замкнутой кривой), репер (0.1); $\theta_1\in(0,\theta_K)$, $t_1>0$ такие, что $\Pi$ — диффеоморфизм $\{s>0,\ |\theta|<\theta_1,\ |\eta|<t_1s\}$ на
открытое множество (лемма K3 [008]); $\bar k_g:=\max_{|\theta|\le\theta_1}|k_g|$. Числа $N\in\mathbb N$, $c>1$, $\beta>0$, $\sigma_1>0$; функции
$y_0\in C^2([0,\sigma_1]\times[-\theta_1,\theta_1])$ с $y_0(0,\cdot)\equiv0$ ($\eta_0(s,\theta):=s\,y_0(s^{1/N},\theta)$ — **приближённое дно**) и
$\tilde F:[0,\sigma_1]\times[-\theta_1,\theta_1]\times[-1,1]\to\mathbb R$, непрерывная вместе с $\partial_\theta\tilde F$, $\partial_e\tilde F$, дифференцируемая по $\sigma$ при $\sigma>0$,
$\sup_{\theta,e}|\sigma\partial_\sigma\tilde F|\to0$ при $\sigma\to0$, и
$$U\big(s\omega(\theta)+(\eta_0(s,\theta)+s^ce)\,n(\theta)\big)=s^\beta\tilde F(s^{1/N},\theta,e),\qquad0<s\le\sigma_1^N,\ |\theta|\le\theta_1,\ |e|\le1. \tag{0.6}$$

**Профиль (W).** $\tilde F(0,\theta,e)=-a_0+P(\theta,e)$, $a_0>0$, и для некоторого $r_W\in(0,\min(\theta_1/2,\frac14)]$, $K_W:=[-r_W,r_W]^2$:

- **(W1)** $P\ge0$ на $K_W$ и обращается в нуль на $K_W$ только в $(0,0)$;
- **(W2)** есть $\mu_0>0$, $\kappa_0\in(0,\frac12]$ и функция $c_2:(0,\kappa_0]\to(0,c]$ такие, что при всех $\kappa\in(0,\kappa_0]$
  $$\kappa\,\theta\,\partial_\theta P+c_2(\kappa)\,e\,\partial_eP\ge\kappa\mu_0P\quad\text{на }K_W. \tag{0.7}$$

Типичные выборы: $c_2\equiv c$ (профиль «распадается», как в теореме Mb [010] и теореме N [011]); $c_2(\kappa)=w\kappa$,
$\kappa_0\le c/w$ (условие (DE)). Ограничение $c_2\le c$ существенно для приведённого доказательства (§3.2, п. 7: при
$\lambda_n<0$ член $\lambda_nw_n^2$ даёт $\vartheta_3\ge|\lambda_n|$). [Гипотеза, R43] Так как лемма M требует от $\vartheta_3$ лишь $b'=\beta-\mu-2\vartheta_3>0$,
тот же метод, по-видимому, допускает $c_2<c+\frac{\beta-\mu}2$ (с другими константами в (0.8)); во всех применениях здесь $c_2\le c$.

**Теорема W.** Пусть $U\in C^2(B_r)$, $U(0)=0$, $\nabla U(0)=0$, выполнены (NF$_W$) и (W). Положим
$\Omega_\delta:=\{(\theta,e)\in(-r_W,r_W)^2:\ P<4\delta\}$, $R_\theta(\delta):=\sup_{\Omega_\delta}|\theta|$, $R_e(\delta):=\sup_{\Omega_\delta}|e|$ (тогда $0<R_\theta(\delta)\to0$, $R_e(\delta)\to0$),
$C_M:=\frac{15\sqrt3}8\beta+4$ и
$$\kappa(\delta):=\min\Big\{\kappa_0,\ \frac\beta{4\mu_0},\ \frac{\mu_0\beta\,\delta}{2C_M^2a_0R_\theta(\delta)^2}\Big\}. \tag{0.8}$$
Тогда есть $\delta_1>0$ такое, что для каждого $\delta\in(0,\delta_1]$ существует асимптотическая траектория
$q(t)=s\,\omega(\theta)+(\eta_0(s,\theta)+s^ce)\,n(\theta)$, $s=s(t)\downarrow0$, $-k_2s^{\beta/2}\le\dot s\le-k_1s^{\beta/2}$ ($0<k_1\le k_2$), с $(\theta(t),e(t))\in\overline{\Omega_\delta}$; в
частности, $|\theta(t)|\le R_\theta(\delta)$, $|e(t)|\le R_e(\delta)$. Она строится по теореме A [007] через лемму M [010] с $\rho=s$, $A(\rho)=a_0\rho^\beta$ и
полем
$$Y=\Psi_s-\frac{\kappa\theta}s\Psi_\theta+\lambda_n\frac\zeta s\Psi_\zeta,\qquad\kappa=\kappa(\delta),\quad\lambda_n:=c-c_2(\kappa)\in[0,c), \tag{0.9}$$
в координатах $(s,\theta,\zeta)$ карты $\Psi(s,\theta,\zeta):=s\omega(\theta)+(\eta_0(s,\theta)+\zeta)n(\theta)$. Ни аналитичность $U$, ни изолированность не
предполагаются.

### Теорема C (трубка; аналог Mc [010])

**Данные (NF$_C$).** $\Sigma_0$ — замкнутая аналитическая кривая длины $L$, натуральный $L$-периодический параметр; $N$, $c>1$,
$\beta>0$, $\sigma_1>0$; $y_0\in C^2([0,\sigma_1]\times\mathbb R)$, $L$-периодическая, $y_0(0,\cdot)\equiv0$; $\tilde F$ на $[0,\sigma_1]\times\mathbb R\times[-1,1]$, $L$-периодическая,
с регулярностью как в (NF$_W$), и (0.6) при всех $\theta\in\mathbb R$.

**Профиль (C).** $\tilde F(0,\theta,e)=-a_0+P(\theta,e)$, $a_0>0$, и для некоторого $e_C\in(0,1]$: **(C1)** $P(\theta,0)=0$ и $P(\theta,e)\ge q_0(|e|)$ при
$|e|\le e_C$, где $q_0$ непрерывна на $[0,e_C]$, $q_0(t)>0$ при $t>0$; **(C2)** $e\,\partial_eP\ge\mu_0P$ при $|e|\le e_C$, $\mu_0>0$.

**Теорема C.** Пусть $U\in C^2(B_r)$, $U(0)=0$, $\nabla U(0)=0$, выполнены (NF$_C$), (C). Тогда для каждого достаточно малого
$\delta>0$ есть асимптотическая траектория $q(t)=s\omega(\theta)+(\eta_0+s^ce)n(\theta)$, $\theta\in\mathbb R/L\mathbb Z$, $s(t)\downarrow0$,
$-k_2s^{\beta/2}\le\dot s\le-k_1s^{\beta/2}$, $|e(t)|\le R_e(\delta):=\sup\{|e|:\ |e|<e_C,\ P<4\delta\}\to0$. Она строится по теореме A [007] через лемму 2
[007] с $\rho=s$, $Y=\Psi_s$ в трубке вокруг всего конуса; об угле $\theta(t)$ ничего не утверждается.

### Теорема D (каскад; аналог Md [010])

**Данные (ND).** Аналитическая дуга $\omega$ около $\theta=0$ (натуральный параметр), $\theta_1,t_1$ — как в (NF$_W$); $N\in\mathbb N$, $c>1$, $\beta>0$,
$\sigma_J>0$, $e_J\in(0,1]$, $r'\in\mathbb N$; вещественно-аналитические $y_0$ на $(-\sigma_J,\sigma_J)\times(-\theta_1,\theta_1)$, $y_0(0,\cdot)\equiv0$, и $\tilde F$ на
$(-\sigma_J,\sigma_J)\times(-\theta_1,\theta_1)\times(-e_J,e_J)$ с (0.6) при $0<s<\sigma_J^N$, $|\theta|<\theta_1$, $|e|<e_J$. По формуле Тейлора по $e$
$$\tilde F=\hat G(\sigma,\theta)+\sum_{l=1}^{2r'-1}h_l(\sigma,\theta)\,e^l+e^{2r'}M(\sigma,\theta,e), \tag{0.10}$$
$\hat G=\tilde F(\cdot,\cdot,0)$, $h_l=\frac1{l!}\partial_e^l\tilde F(\cdot,\cdot,0)$, $M$ аналитична; $M_0:=M(0,0,0)>0$.

- **(D1)** $G:=\hat G(0,\cdot)\ge0$ около $0$, $G(0)=0$, $G\not\equiv0$ около $0$; $\hat G(\sigma_k,\theta_k)<0$ при некоторых $\sigma_k\downarrow0$, $\theta_k\to0$.
- **(D2)** Для некоторых данных $(N_V,A_V,\Gamma_V,a_V,T,Q_V,k_0)$ леммы V [010] для $f(\sigma,\tau):=\hat G(\sigma,\tau)$ (в [010] — $N,A_V,\Gamma_V,\dots$)
  с $2r'\mid\Gamma_V$, $B:=\Gamma_V/(2r')$: при $1\le l\le2r'-1$ в разложении $h_l(t^{N_V},T(t)+t^{A_V}b_1)=\sum_{i\ge0}H_{l,i}(b_1)t^i$ коэффициенты с
  $i\le\Gamma_V-lB$ тождественно равны нулю. (Данные с $2r'\mid\Gamma_V$ есть всегда: подстановка $t\mapsto t^{r'}$, §5, п. 1. (D2)
  выполнено, если $h_l\equiv0$ — точная ветвь постоянной кратности, — или если $h_l=\sigma^{\nu_l}\tilde h_l$, $N_V\nu_l>\Gamma_V-lB$.)

**Теорема D.** Пусть $U\in C^2(B_r)$, $U(0)=0$, $\nabla U(0)=0$, выполнены (ND), (D1), (D2). Положим $\alpha:=A_V/(NN_V)$,
$\gamma':=\Gamma_V/(NN_V)$, $\beta_d:=\beta+\gamma'$, $c_1:=1+\alpha$, $c':=c+\gamma'/(2r')$, $\tau_v(x):=T(x^{1/(NN_V)})$. Тогда при подходящих $s_0,r_0>0$ карта
$$\Phi(x,u,\zeta):=\Psi\big(x,\ \tau_v(x)+u/x,\ \zeta\big),\qquad b=(b_1,b_2)=\big(u\,x^{-c_1},\ \zeta\,x^{-c'}\big) \tag{0.11}$$
задаёт принадлежность $U$ классу (GT3) [007] с показателем $\beta_d$, весами $(c_1,c')$, числом $NN_V$ вместо $N$, $C_1=0$ и условием
$(V_0)$. По теореме 2 [007] есть асимптотическая траектория $q(t)=\Phi(x(t),u(t),\zeta(t))$, $x(t)\downarrow0$,
$-k_2x^{\beta_d/2}\le\dot x\le-k_1x^{\beta_d/2}$ (при $\beta_d>2$ отсюда $x\asymp t^{-2/(\beta_d-2)}$), касающаяся луча: $q/|q|\to\omega(0)$. Аналитичность
$U$ не нужна (нужна аналитичность данных $y_0$, $\tilde F$).

### Леммы о ветвях

**Лемма B.** Пусть $\gamma_*<\infty$, $c_0:=\min G_{\min}$, (CM) выполнено в каждой точке $F_{c_0}$, и в точке $(\theta_0,\varepsilon_0)\in F_{c_0}$ ветвь $\varepsilon_b$
из (CM) имеет $G_b\equiv c_0$ около $\theta_0$. Тогда есть аналитическая $L$-периодическая $\varepsilon_g:\mathbb R\to\mathbb R$, $\varepsilon_g(\theta_0)=\varepsilon_0$,
$(\theta,\varepsilon_g(\theta))\in F_{c_0}$ при всех $\theta$, $r'\in\mathbb N$ и многочлен $\mathsf p_g(\theta,e)$ по $e$ с аналитическими $L$-периодическими
коэффициентами, $\mathsf p_g(\theta,0)>0$, такие, что $\Phi_0(\theta,\varepsilon_g(\theta)+e)=c_0+e^{2r'}\mathsf p_g(\theta,e)$.

**Лемма U.** Если на компоненте-кривой с $\gamma_*<\infty$ выполнено (R), то выполнено (UR) со всеми $r_k=1$.

**Лемма B′.** Пусть выполнено (UR), $c_0:=\min G_{\min}$, и для ветви $k$ на $J\ni\theta_0$ $G_k:=\hat G_k(0,\cdot)\equiv c_0$ около $\theta_0$. Тогда есть
$\sigma_0,e_0>0$, $r_g\in\mathbb N$ и вещественно-аналитические $L$-периодические по $\theta$ $\varepsilon_g^*,\hat G_g$ на $(-\sigma_0,\sigma_0)\times\mathbb R$ и $M_g$ на
$(-\sigma_0,\sigma_0)\times\mathbb R\times(-e_0,e_0)$ с $|\varepsilon_g^*|<E+\frac12$, $\tilde U(\sigma,\theta,\varepsilon_g^*+e)=\hat G_g+e^{2r_g}M_g$, $M_g(0,\theta,0)>0$,
$\hat G_g(0,\cdot)\equiv c_0$, совпадающие с $(\varepsilon_k^*,\hat G_k,M_k,r_k)$ около $(0,\theta_0)$.

### Предложение W′ и теорема Z

**Предложение W′ (случай (W)).** Пусть выполнены (H1)–(H4), на компоненте-кривой $\gamma_*<\infty$ и $\min G_{\min}=-a_0<0$. Если
выполнено одно из условий

- **(W-a)** в некоторой точке $(\theta_0,\varepsilon_0)\in F_{\min}$ выполнено (CM) и $G_b\not\equiv-a_0$ около $\theta_0$;
- **(W-b)** в некоторой точке $(\theta_0,\varepsilon_0)\in F_{\min}$ выполнены (W1) и (DE);
- **(W-c)** (CM) выполнено во всех точках $F_{\min}$,

то есть асимптотическая траектория (теорема W при (W-a), (W-b); теорема W или C при (W-c)).

**Теорема Z (случай (Z)).** Пусть выполнены (H1)–(H4), на компоненте-кривой $\gamma_*<\infty$, $\min G_{\min}=0$, $F_{\rm fl}(s_n,\theta_n)<0$ при
$s_n\downarrow0$, и выполнено (UR). Тогда есть асимптотическая траектория (теорема D; если на ветви с отрицательными
значениями $G_k\equiv0$ — после одного шага уточнения теорема D, W или C).

## Доказательство

### 1. Лемма A0

1. *Аналитичность.* Пусть $\omega^*\in\Sigma_0$, $\chi(\xi):=(\omega^*+\xi)/|\omega^*+\xi|$ — аналитическая карта сферы ($\xi\in T_{\omega^*}S^2$ мало),
   $F:=u_m\circ\chi$, $\tilde\tau:=\tau_\Sigma\circ\chi$, $\tilde g:=g_\Sigma\circ\chi$, $C_0:=\chi^{-1}(\Sigma_0)$ — $C^\infty$-кривая через $0$. Пусть $X$ — постоянное векторное поле,
   трансверсальное к $C_0$ в $0$; так как $d\tilde\tau\ne0$ и $\ker d\tilde\tau(0)=T_0C_0$, $X\tilde\tau(0)\ne0$. По (H4) $F=\tilde\tau^{2r}\tilde g$; по формуле Лейбница в
   каждом слагаемом $X^kF$ не продифференцировано не меньше $2r-k$ множителей $\tilde\tau$. Поэтому $X^kF=0$ на $C_0$ при $k<2r$ и
   $X^{2r}F=(2r)!(X\tilde\tau)^{2r}\tilde g\ne0$ в $0$. Функция $H:=X^{2r-1}F$ аналитична, $H=0$ на $C_0$, $XH(0)\ne0$; по аналитической теореме о
   неявной функции есть окрестность $B\ni0$, в которой $\{H=0\}\cap B$ — связная аналитическая дуга (график над интервалом).
   Уменьшив $B$, считаем, что $C_0\cap B$ — связная одномерная подмногообразие, относительно замкнутое в $B$; оно лежит в
   дуге $\{H=0\}\cap B$, открыто в ней (инвариантность размерности) и замкнуто, значит, совпадает с ней. Значит, $\Sigma_0$ аналитична, как и её натуральная
   параметризация и репер.
2. *(M).* $\mathcal E(\theta,y):=(\omega+yn)/\sqrt{1+y^2}$, $u_m(\omega+yn)=(1+y^2)^{m/2}(\tau_\Sigma^{2r}g_\Sigma)(\mathcal E(\theta,y))$. $\tau_\Sigma(\mathcal E(\theta,0))=0$,
   $\partial_y\tau_\Sigma(\mathcal E)|_{y=0}=d\tau_\Sigma(n)\ne0$ ($n$ трансверсален $\Sigma_0$), поэтому $\tau_\Sigma(\mathcal E)=y\tau_1$, $\tau_1(\theta,0)\ne0$, и $u_m(\omega+yn)=y^{2r}a$,
   $a(\theta,0)=\tau_1^{2r}g_\Sigma(\omega)>0$. Левая часть — многочлен по $y$
   с аналитическими периодическими коэффициентами; его коэффициенты при $y^l$, $l<2r$, нулевые, так что $a$ — многочлен по
   $y$. $\square$

Аналитичность $U$ здесь не используется: только то, что $u_m$ — многочлен.

### 2. Лемма T и предложение R′

**Лемма T.**

1. *(a).* $O(\Sigma_0):=\mathcal E(\mathbb R\times(-y_1,y_1))$ ($\mathcal E$ — локальный диффеоморфизм: $\partial_\theta\mathcal E$, $\partial_y\mathcal E$ при $y=0$ — это $\ell$, $n$) и $C_\omega\cap S^2$
   открыты и содержат соответствующие компоненты. $\mathcal A:=S^2\setminus(\bigcup O(\Sigma_0)\cup\bigcup(C_\omega\cap S^2))$ компактно и не пересекает
   $\Sigma$, поэтому $u_m\ge c_*>0$ на $\mathcal A$ и $U(q)\ge c_*|q|^m-C|q|^{m+1}>0$ при $q/|q|\in\mathcal A$, $|q|<c_*/C$. Если $q/|q|=\mathcal E(\theta,t)$, $|t|<y_1$, то $q=s\omega+\eta n$ с
   $s=|q|/\sqrt{1+t^2}\le|q|$, $|\eta|<y_1s$, и при $|q|<s_1$ $q\in T(\Sigma_0)$. $r_*$ — меньше $c_*/C$, всех $s_1$ и всех $s_1(\omega)$.
2. *(b).* В трубке $s<R_0/3$, $|\eta/s|<y_1$, и $U=s^m\varphi(s,\theta,\eta/s)\ge s^m\min_{|y|\le y_1}\varphi=F_{\rm fl}$. Для конусов — [008], §11, доказательство
   K4(c) (лемма K1, п. 2) при $0<x<s_1(\omega)$.
3. *(c).* «⇐» — из (a), (b). «⇒»: $F_{\rm fl}(s,\theta)$ и $s^mR_\omega(s)=U(s\omega+\eta^*_\omega(s))$ — значения $U$ в точках нормы не больше $2s$. $\square$

**Предложение R′.**

1. При $\Sigma=\varnothing$ $u_m\ge c|q|^m$, и $0$ — строгий минимум.
2. По лемме T(c) есть точечная компонента и $s_n\downarrow0$ с $R_\omega(s_n)<0$, или компонента-кривая и $(s_n,\theta_n)$, $s_n\downarrow0$, с
   $F_{\rm fl}(s_n,\theta_n)<0$.
3. *Точка.* $R_\omega$ аналитична, $R_\omega(0)=0$, $R_\omega\not\equiv0$; $R_\omega=g_0\,s^i(1+O(s))$, $g_0<0$ — это (P) ($j(\omega)=m+i$, $g_{j(\omega)}(\omega)=g_0<0$).
4. *Кривая.* При $\gamma_*=\infty$ все $\varphi_{il}$ с $l<2r$ нулевые, и по аналитичности $\varphi=y^{2r}A_\varphi$ около $s=0$; по выбору $y_1$, $s_1$ $A_\varphi>0$, и
   $F_{\rm fl}\ge0$ — противоречие. Значит, $\gamma_*<\infty$, и по (0.4) $G_{\min}(\theta_n)+O(s_n^{1/N})<0$; для предельной точки $\theta_*$ $G_{\min}(\theta_*)\le0$:
   это (W) или (Z). $\square$

### 3. Теорема W

#### 3.1. Формулы

Обозначения: $\eta:=\eta_0+\zeta$, $\epsilon:=k_g\eta/s$, $\nu:=\eta_{0,s}-\kappa\theta\eta_{0,\theta}/s$, $\tilde\nu:=\nu+\lambda_n\zeta/s$; в координатах
$Y=\partial_s-\frac{\kappa\theta}s\partial_\theta+\frac{\lambda_n\zeta}s\partial_\zeta$. Прямым дифференцированием по (0.1) [Доказано; [Эксперимент] `frames_W.py`: 16 тождеств
символьно при общем $k_g$ и дне $s\,y_0(s^{1/3},\theta)$; независимо R40 символьно и численно в $\mathbb R^3$ на локсодроме]:
$$\Psi_s=\omega+\eta_{0,s}n,\qquad\Psi_\theta=s(1-\epsilon)\ell+\eta_{0,\theta}n,\qquad\Psi_\zeta=n; \tag{3.1}$$
$$Y=\omega-\kappa\theta(1-\epsilon)\ell+\tilde\nu\,n,\qquad h=1+\kappa^2\theta^2(1-\epsilon)^2+\tilde\nu^2; \tag{3.2}$$
$$\partial_\theta Y=\kappa\theta(1-\epsilon)\omega+\big[1-\kappa(1-\epsilon)+\kappa\theta\partial_\theta\epsilon-\tilde\nu k_g\big]\ell+\big[-\kappa\theta(1-\epsilon)k_g+\partial_\theta\tilde\nu\big]n,\quad
\partial_sY=\kappa\theta\partial_s\epsilon\,\ell+\partial_s\tilde\nu\,n,\quad\partial_\zeta Y=\frac{\kappa\theta k_g}s\ell+\frac\lambda_n sn; \tag{3.3}$$
$$s\,D_YY=-\kappa^2\theta^2(1-\epsilon)\omega+\kappa\theta\Big[s\partial_s\epsilon-1+\kappa(1-\epsilon)-\kappa\theta\partial_\theta\epsilon+\tilde\nu k_g+\frac{\lambda_n k_g\zeta}s\Big]\ell+\Big[s\partial_s\tilde\nu+\kappa^2\theta^2(1-\epsilon)k_g-\kappa\theta\partial_\theta\tilde\nu+\frac{\lambda_n^2\zeta}s\Big]n; \tag{3.4}$$
для $w=w_\omega\omega+w_\ell\ell+w_nn=a^s\Psi_s+a^\theta\Psi_\theta+a^\zeta\Psi_\zeta$, $a^s=w_\omega$, $a^\theta=\frac{w_\ell}{s(1-\epsilon)}$, $a^\zeta=w_n-w_\omega\eta_{0,s}-\frac{w_\ell\eta_{0,\theta}}{s(1-\epsilon)}$:
$$
\begin{aligned}
s\langle w,D_wY\rangle={}&\Big(\frac1{1-\epsilon}-\kappa\Big)w_\ell^2+\kappa\theta\,w_\omega w_\ell+\frac{(\kappa\theta\partial_\theta\epsilon-\tilde\nu k_g)w_\ell^2+\partial_\theta\tilde\nu\,w_\ell w_n}{1-\epsilon}\\
&+w_\omega\big[\kappa\theta\,s\partial_s\epsilon\,w_\ell+s\partial_s\tilde\nu\,w_n\big]-\kappa\theta k_g\,w_\ell\Big(w_\omega\eta_{0,s}+\frac{w_\ell\eta_{0,\theta}}{s(1-\epsilon)}\Big)+\lambda_n\,a^\zeta w_n
\end{aligned} \tag{3.5}
$$
(члены $\mp\kappa\theta k_gw_\ell w_n$ из $a^\theta\partial_\theta Y$ и $a^\zeta\partial_\zeta Y$ сокращаются);
$$w\perp Y\iff w_\omega=\kappa\theta(1-\epsilon)w_\ell-\tilde\nu w_n; \tag{3.6}$$
для $W:=U+a_0\rho^\beta$, $\rho=s$, $\sigma=s^{1/N}$, $e=\zeta s^{-c}$, $c_2=c-\lambda_n$
$$\beta W-\rho\,YW=s^\beta\Big[\kappa\theta\partial_\theta\tilde F+c_2e\partial_e\tilde F-\frac\sigma N\partial_\sigma\tilde F\Big]. \tag{3.7}$$
Вывод (3.7): для $g:=W\circ\Psi=s^\beta(\tilde F(s^{1/N},\theta,\zeta s^{-c})+a_0)$ $s\partial_sg=\beta g+s^\beta[\frac\sigma N\partial_\sigma\tilde F-ce\partial_e\tilde F]$,
$-\kappa\theta\partial_\theta g=-s^\beta\kappa\theta\partial_\theta\tilde F$, $\lambda_n\zeta\partial_\zeta g=s^\beta\lambda_n e\partial_e\tilde F$; сумма равна $\rho\,YW=s\,Yg$. Тождества:
$s\partial_s\epsilon=k_g\eta_{0,s}-\epsilon$, $\partial_\theta\epsilon=(k_g'\eta+k_g\eta_{0,\theta})/s$, $\partial_\theta\tilde\nu=\eta_{0,s\theta}-\kappa\eta_{0,\theta}/s-\kappa\theta\eta_{0,\theta\theta}/s$,
$s\partial_s\tilde\nu=s\eta_{0,ss}-\kappa\theta(\eta_{0,s\theta}-\eta_{0,\theta}/s)-\lambda_n\zeta/s$. При $\lambda_n=0$ это (2.1), (2.5), (5.1)–(5.3) [010] и (7.2)–(7.6) [011].

**Малые величины.** $\Delta(s'):=\sup\{|\epsilon|+|s\partial_s\epsilon|+|\partial_\theta\epsilon|+|\eta_{0,s}|+|\eta_{0,\theta}|/s+s|\eta_{0,ss}|+|\eta_{0,s\theta}|+|\eta_{0,\theta\theta}|/s+|\zeta|/s\}$ по
$0<s<s'$, $|\theta|\le\theta_1/2$, $|\zeta|\le s^c$, стремится к нулю при $s'\to0$ (доказательство леммы N5 [011]: $y_0\in C^2$, $y_0(0,\cdot)\equiv0$,
$|\zeta|/s\le s^{c-1}$). При $\kappa\le\frac12$, $\kappa|\theta|\le1$, $0\le\lambda_n\le c$:
$$|\tilde\nu|\le(2+c)\Delta,\qquad|\partial_\theta\tilde\nu|\le3\Delta,\qquad|s\partial_s\tilde\nu|\le(3+c)\Delta. \tag{3.8}$$

#### 3.2. Доказательство

1. *Окно.* $m(\rho'):=\min\{P:\ (\theta,e)\in K_W,\ \max(|\theta|,|e|)\ge\rho'\}>0$ по (W1); при $4\delta<m(\rho')$ $\Omega_\delta\subset(-\rho',\rho')^2$, так что $R_\theta,R_e\to0$;
   $R_\theta(\delta)>0$ ($\Omega_\delta$ — окрестность нуля). $\delta_0:=m(r_W/2)/8$; при $\delta\le\delta_0$ $\overline{\Omega_\delta}\subset[-\frac{r_W}2,\frac{r_W}2]^2$ и $P=4\delta$ на $\partial\Omega_\delta$.
2. *$s_2$* (равномерно по $\kappa\in(0,\frac12]$, $\lambda_n\in[0,c]$): $s_2<\min(1,\sigma_1^N)$, $10(1+\bar k_g+c)\Delta(s_2)\le\frac14$ (отсюда $|\epsilon|\le\frac1{40}$, $|\tilde\nu|\le\frac14$,
   $|\eta_{0,s}|+\frac43|\eta_{0,\theta}|/s\le1$, $|\eta_{0,s}k_g|\le1$), $|\eta|\le\frac12\min(t_1,\frac14)s$ при $s<s_2$ и $2s_2<r$. Тогда
   $\mathcal O:=\{\Psi(s,\theta,s^ce):\ 0<s<s_2,\ |\theta|<r_W,\ |e|<1\}$ открыто в $B_r\setminus0$, $\Psi$ инъективна (K3), $\rho=s\circ\Psi^{-1}$, $\nabla\rho=\omega(\theta)$,
   $Y:=(0.9)\circ\Psi^{-1}\in C^1$, $Y\rho=1$; $\sigma_0$ теоремы A — это $s_2$.
3. *$\delta_1$*: $\delta_1\le\min(\delta_0,a_0/2)$ и при $\delta\le\delta_1$: $\frac54R_\theta(1+\bar k_g)\le1$, $5R_\theta\sqrt\delta\le\frac14\sqrt{2a_0/3}$. Фиксируем $\delta\in(0,\delta_1]$,
   $\kappa:=\kappa(\delta)$, $c_2:=c_2(\kappa)$, $\lambda_n:=c-c_2$.
4. *$D$.* $\chi(\sigma'):=\sup\{|\tilde F-\tilde F_0|+|\partial_\theta(\tilde F-\tilde F_0)|+|\partial_e(\tilde F-\tilde F_0)|+|\sigma\partial_\sigma\tilde F|:\ 0<\sigma\le\sigma',\ |\theta|\le r_W,\ |e|\le1\}\to0$
   ($\tilde F_0:=\tilde F(0,\cdot)$; равномерная непрерывность). $\sigma_*\in(0,s_2)$ с $\chi:=\chi(\sigma_*^{1/N})<\delta$ (ещё уменьшится);
   $D:=\Psi(\{(s,\theta,s^ce):\ 0<s<\sigma_*,\ (\theta,e)\in\Omega_\delta,\ \tilde F+a_0<\delta\})$. (D1)–(D3) — как в [010], §5.2, п. 4: предел точек $D$ с $\bar s>0$
   лежит в $\mathcal O$, при $\bar s=0$ равен $0$ ($|\Psi|\le2s$), $\rho\le|q|$; на $\partial D$ с $\rho<\sigma_*$ либо $(\theta,e)\in\partial\Omega_\delta$ и $\tilde F+a_0\ge4\delta-\chi>3\delta$
   (невозможно), либо $W=\delta\rho^\beta$; точки $(s,0,0)$ дают (D3).
5. *(L0), (L1).* $a_1=a_3=a_0$, $a_2=\beta a_0$, $\delta\le a_0/2$; $1\le h<\frac32$ по (3.2): $h_0=1$, $h_1=\frac32$.
6. *(L2).* На $D_\sigma$ ($\sigma=\sigma_*$) $(\theta,e)\in\overline{\Omega_\delta}\subset K_W$, $W=s^\beta(P+\tilde F-\tilde F_0)\ge-\chi s^\beta\ge-\delta\rho^\beta$. По (3.7), (0.7):
   $\beta W-\rho YW\ge s^\beta[\kappa\mu_0P-(\kappa r_W+c+\frac1N)\chi]$; $\mu:=\kappa\mu_0\le\beta/4$, $\mu W\le\kappa\mu_0s^\beta(P+\chi)$, так что (L2) леммы M выполнено с
   $\varepsilon_1:=(\kappa r_W+c+\frac1N+\kappa\mu_0)\chi/\delta$.
7. *(L3M).* Для $q\in D_\sigma$ ($|\theta|\le R_\theta$, $\kappa|\theta|\le1$) и $w\perp Y$:
   - по (3.6) $|\langle\nabla\rho-Y/h,w\rangle|=|w_\omega|\le(\frac54\kappa R_\theta+|\tilde\nu|)|w|$: $\gamma_1:=\frac54\kappa R_\theta$, $\vartheta_1:=\sup|\tilde\nu|$;
   - по (3.4): $\omega$-компонента $\le\frac54\kappa^2\theta^2$; $\ell$-компонента $=-\kappa(1-\kappa)\theta+\kappa\theta[s\partial_s\epsilon-\kappa\epsilon-\kappa\theta\partial_\theta\epsilon+\tilde\nu k_g+\lambda_n k_g\zeta/s]$, второй
     член по модулю $\le|s\partial_s\epsilon|+\kappa|\epsilon|+|\partial_\theta\epsilon|+\bar k_g|\tilde\nu|+c\bar k_g|\zeta|/s$ ($\kappa|\theta|\le1$ использовано дважды, $\lambda_n\le c$); $n$-компонента
     $\le\frac54\kappa^2\theta^2\bar k_g+|s\partial_s\tilde\nu|+|\partial_\theta\tilde\nu|+c^2|\zeta|/s$. Итак, $\rho|\langle\nabla_YY,w\rangle|\le(\gamma_2+\vartheta_2)|w|$, $\gamma_2:=\kappa R_\theta+\frac54\kappa^2R_\theta^2(1+\bar k_g)\le\frac32\kappa R_\theta$,
     $\vartheta_2:=\sup(|s\partial_s\epsilon|+|\epsilon|+|\partial_\theta\epsilon|+\bar k_g|\tilde\nu|+c\bar k_g|\zeta|/s+|s\partial_s\tilde\nu|+|\partial_\theta\tilde\nu|+c^2|\zeta|/s)$;
   - по (3.5): первый член $\ge(\frac45-\frac12)w_\ell^2$; $\kappa\theta w_\omega w_\ell=\kappa^2\theta^2(1-\epsilon)w_\ell^2-\kappa\theta\tilde\nu w_\ell w_n\ge-|\tilde\nu||w|^2$; третий
     $\ge-\frac43(|\partial_\theta\epsilon|+\bar k_g|\tilde\nu|+|\partial_\theta\tilde\nu|)|w|^2$; четвёртый $\ge-(|s\partial_s\epsilon|+|s\partial_s\tilde\nu|)|w|^2$; пятый $\ge-\bar k_g(|\eta_{0,s}|+\frac43|\eta_{0,\theta}|/s)|w|^2$;
     последний $=\lambda_n w_n^2-\lambda_n w_n(w_\omega\eta_{0,s}+w_\ell\eta_{0,\theta}/(s(1-\epsilon)))\ge-c(|\eta_{0,s}|+\frac43|\eta_{0,\theta}|/s)|w|^2$ — **здесь существенно $\lambda_n\ge0$**
     ($c_2\le c$): при $\lambda_n<0$ член $\lambda_n w_n^2$ был бы порядка $1$. Итак, $s\langle w,D_wY\rangle\ge-\vartheta_3|w|^2$,
     $\vartheta_3:=\sup(|\tilde\nu|+\frac43(|\partial_\theta\epsilon|+\bar k_g|\tilde\nu|+|\partial_\theta\tilde\nu|)+|s\partial_s\epsilon|+|s\partial_s\tilde\nu|+(\bar k_g+c)(|\eta_{0,s}|+\frac43|\eta_{0,\theta}|/s))$.

   По (3.8) $\vartheta_i\le C_\vartheta(\bar k_g,c)\Delta(\sigma_*)\to0$ равномерно по $\kappa\in(0,\frac12]$, $\lambda_n\in[0,c]$.
8. *Константы леммы M.* $L_1=3\beta\sqrt{3a_0/2}$, $L_2=2\sqrt{2a_0}$; при $\delta\le a_0/2$
   $\Gamma_M:=\sqrt2[(a_2+\beta\delta)\sqrt{h_1/a_1}\gamma_1+\sqrt{2a_3/h_0}\gamma_2]\le(\frac{15\sqrt3}8\beta+3)\sqrt{a_0}\kappa R_\theta\le C_M\sqrt{a_0}\kappa R_\theta$. Уменьшим $\sigma_*$ так, что
   $\vartheta_3\le\beta/8$, $\varepsilon_1+(L_1\vartheta_1+L_2\vartheta_2)/\sqrt\delta\le\kappa\mu_0/4$, $4\sqrt\delta\vartheta_1\le\frac12\sqrt{2a_0/3}$. Тогда $b'=\beta-\mu-2\vartheta_3\ge\beta/2$,
   $\Gamma_M^2/(4b'\delta)\le C_M^2a_0\kappa^2R_\theta^2/(2\beta\delta)\le\kappa\mu_0/4$ (третий член (0.8)), и скобка в формуле (0.3) леммы M [010] не меньше $\kappa\mu_0/2>0$; условие п. 1 леммы
   M: $4\sqrt\delta(\vartheta_1+\gamma_1)\le\frac12\sqrt{2a_0/3}+\frac52R_\theta\sqrt\delta\le\frac58\sqrt{2a_0/3}<\sqrt{a_1/h_1}$.
9. *Вывод.* Лемма M [010] даёт (D4), (A4), (A5); теорема A [007] — решение с $q\ne0$, $q,\dot q\to0$; по шагу 5 теоремы A
   $q(t)\in D_\sigma$, $(\theta,e)\in\overline{\Omega_\delta}$; $k_1=\frac12\sqrt{2a_0/3}$, $k_2=\sqrt{2(a_0+\delta)}+k_1$ (п. 1 леммы M). $\square$

Порядок констант: $r_W$, $\delta_0$ → $s_2$ → $\delta_1$ → $\delta$ → $\kappa(\delta)$, $c_2$, $\lambda_n$ → $\sigma_*$. (0.7) используется лишь при $\kappa=\kappa(\delta)$.

### 4. Теорема C

1. $s_2$ — как в §3.2, п. 2, с $\kappa=\lambda_n=0$ и $\theta\in\mathbb R$ (периодичность); $\mathcal O:=\{\Psi(s,\theta,s^ce):\ 0<s<s_2,\ \theta\in\mathbb R/L\mathbb Z,\ |e|<1\}$ открыто,
   $\Psi$ инъективна ([010], (N3)); $\rho=s$, $Y=\Psi_s$, $Y\rho=1$, $A(r)=a_0r^\beta$.
2. По (3.7) при $\kappa=\lambda_n=0$: $\beta W-\rho YW=s^\beta[ce\partial_e\tilde F-\frac\sigma N\partial_\sigma\tilde F]$.
3. $\Omega:=\{|e|<e_C,\ P<4\delta\}$; при $\delta\le\delta_0:=\min(\frac{a_0}2,\frac18\min_{[e_C/2,e_C]}q_0)$ $\overline\Omega\subset\{|e|\le e_C/2\}$, $P=4\delta$ на $\partial\Omega$, $R_e(\delta)\to0$.
   $\chi(\sigma'):=\sup\{|\tilde F-\tilde F_0|+|\partial_e(\tilde F-\tilde F_0)|+|\sigma\partial_\sigma\tilde F|:\ 0<\sigma\le\sigma',\ \theta\in\mathbb R,\ |e|\le1\}\to0$; $\sigma_*$ с $\chi<\delta$;
   $D:=\Psi(\{0<s<\sigma_*,\ (\theta,e)\in\Omega,\ \tilde F+a_0<\delta\})$.
4. (D1)–(D3) — как в [010], §6, п. 4 (угловой границы нет; (D3) — точки $(s,\theta,0)$, $P(\theta,0)=0$).
5. $a_1=a_3=a_0$, $a_2=\beta a_0$; $h=1+\eta_{0,s}^2\in[1,\frac32]$ ($|\eta_{0,s}|\le\frac1{40}$). $W\ge-\chi s^\beta$; $\mu:=\min(c\mu_0,\beta)$; по (C2)
   $\beta W-\rho YW\ge s^\beta[c\mu_0P-cR_e\chi-\chi/N]\ge\mu W-s^\beta(c+\frac1N+\beta)\chi$: $\varepsilon_1:=(c+\frac1N+\beta)\chi/\delta$.
6. (L3) [007] (его константы $\theta_1,\theta_2,\theta_3$ здесь обозначены $\vartheta_1,\vartheta_2,\vartheta_3$, чтобы не путать с полушириной дуги $\theta_1$):
   $Y=\omega+\eta_{0,s}n$; $|\nabla\rho-Y/h|\le|\eta_{0,s}|=:\vartheta_1$ ($\nabla\rho-Y/h\perp Y$); $\nabla_YY=\eta_{0,ss}n$, $\vartheta_2:=\sup s|\eta_{0,ss}|$; по (3.5) при $\kappa=\lambda_n=0$
   $s\langle w,D_wY\rangle=\frac{(1-\eta_{0,s}k_g)w_\ell^2+\eta_{0,s\theta}w_\ell w_n}{1-\epsilon}+s\eta_{0,ss}w_\omega w_n\ge-(\frac43|\eta_{0,s\theta}|+s|\eta_{0,ss}|)|w|^2=:-\vartheta_3|w|^2$; все $\vartheta_i\le3\Delta(\sigma_*)\to0$.
7. При фиксированном $\delta$ уменьшим $\sigma_*$: $\varepsilon_1+(L_1\vartheta_1+L_2\vartheta_2)/\sqrt\delta+4\vartheta_3\le\mu/2$, $4\vartheta_1\sqrt\delta\le\sqrt{2a_0/3}$. Лемма 2 [007] даёт (D4),
   (A4), (A5), теорема A — траекторию. $\square$

### 5. Теорема D

1. *Лемма V.* Условия леммы V [010] для $f=\hat G$ — это (D1). Подстановка $t\mapsto t^m$ переводит данные $(N_V,A_V,\Gamma_V,a_V,T,Q_V,k_0)$ в
   $(mN_V,mA_V,m\Gamma_V,a_V,T(t^m),Q_V,k_0)$ и сохраняет утверждения леммы V ($\tau_v$ та же, $\hat\Phi_{\rm new}(t,b)=\hat\Phi(t^m,b)$, чётность
   сохраняется); при $m=r'$ $2r'\mid r'\Gamma_V$ ($\Gamma_V$ чётно). Индексы $i$, $\Gamma_V$ и $B$ умножаются на $m$, так что требование (D2) с
   рациональным $B$ равносильно (D2) для подставленных данных с целым $B$. Ниже данные — из (D2).
2. *Переменные.* $x=s$, $\sigma=x^{1/N}$, $t:=x^{1/(NN_V)}$, $\hat\theta:=\tau_v(x)+u/x=T(t)+t^{A_V}b_1$, $\zeta=x^{c'}b_2$, $e:=\zeta x^{-c}=t^Bb_2$ ($(c'-c)NN_V=B$).
3. *$(\Phi0)$–$(\Phi3)$, $C_1=0$* — дословно [010], §8, пп. 1–5, с $\eta^*\to\eta_0$, $\theta_0=0$: используются (8.1) [010] ($\tilde\kappa=x\tau_v'-x^\alpha b_1\to0$,
   $x^2\hat\theta_{xx}\to0$, $\hat\theta\to0$, $|\zeta|\le r_0x^{c'}$, $c'>1$), тождества (8.2), (8.3) [010] для любого $C^2$-дна и $\Delta\to0$ (лемма N5 [011]).
4. *(F).* По (0.6), (0.10):
   $$U\circ\Phi=x^\beta\tilde F(\sigma,\hat\theta,e)=x^{\beta_d}F_d(t,b),\qquad F_d:=\hat\Phi(t,b_1)+\sum_{l=1}^{2r'-1}t^{lB-\Gamma_V}H_l(t,b_1)\,b_2^l+b_2^{2r'}M\big(t^{N_V},T(t)+t^{A_V}b_1,t^Bb_2\big), \tag{5.1}$$
   $H_l(t,b_1):=h_l(t^{N_V},T(t)+t^{A_V}b_1)$. $\hat\Phi$ аналитична около $\{0\}\times[-r_0,r_0]$ (лемма V, п. 2), $t^{lB-\Gamma_V}H_l$ аналитична и равна нулю при
   $t=0$ (по (D2)), $M$ аналитична. Значит, $F_d$ аналитична около $\{0\}\times\overline{B_{r_0}}$, $\sup_K|t\partial_tF_d|=O(t)$ и
   $$F_{d,0}(b)=-a_V+Q_V(b_1)+M_0b_2^{2r'},\qquad Q:=F_{d,0}-F_{d,0}(0)=Q_V(b_1)+M_0b_2^{2r'}. \tag{5.2}$$
   $s_0$: $s_0\le1$, $s_0<\sigma_J^N$, $2s_0<r$, $r_0s_0^{B/(NN_V)}<e_J$, $|T(t)|+t^{A_V}r_0<\theta_1/2$ при $t<s_0^{1/(NN_V)}$, $s_0^{1/(NN_V)}$ меньше радиуса
   аналитичности $F_d$, и малость из п. 3.
5. *$(V_0)$.* $r_2$ с $Q_V\ge\frac{c_{k_0}}2b_1^{k_0}$ и $b_1Q_V'\ge Q_V$ при $|b_1|\le r_2$; $r_0:=r_2$. При малом $\delta_2$ $\{Q<\delta\}\cap B_{r_0}\subset B_{r_0/2}$ ($\delta\le\delta_2$),
   $\overline{\Omega_b}\subset B_{r_0}$, $Q\ge0$ (лемма V, п. 3), и $c_1b_1\partial_{b_1}Q+c'b_2\partial_{b_2}Q=(1+\alpha)b_1Q_V'+2r'c'M_0b_2^{2r'}\ge Q$: $(V_0)$ с $\mu=1$,
   $\delta\in(0,\min(a_V/2,\delta_2)]$; $\mu\le\beta_d$, так как $\beta_d\ge2$ по п. 1 шага 6 теоремы 2 [007] (использует только $(\Phi0)$, $(\Phi1)$, (F),
   $F_{d,0}(0)\ne0$, $U\in C^2$).
6. Теорема 2 [007] даёт траекторию; касание: $\hat\theta\to0$, $|\eta|\le|\eta_0|+r_0x^{c'}=o(x)$. $\square$

### 6. Леммы B, U, B′

**Лемма B.**

1. *Единственность.* Две непрерывные $\varepsilon',\varepsilon''$ на интервале с графиками в $F_{c_0}$, совпадающие в какой-нибудь точке, совпадают:
   множество совпадения замкнуто и, по (CM), открыто.
2. *Продолжение.* $I=(\theta_-,\theta_+)$ — максимальный интервал с аналитической $\varepsilon_g$, $\varepsilon_g(\theta_0)=\varepsilon_0$, $(\theta,\varepsilon_g)\in F_{c_0}$ (непуст: $\varepsilon_b$ около $\theta_0$,
   так как $c_0\le G_{\min}\le\Phi_0(\theta,\varepsilon_b)=G_b\equiv c_0$). Пусть $\theta_+<\infty$; $\varepsilon_g\in[-E_0,E_0]$, $\theta_k\uparrow\theta_+$, $\varepsilon_g(\theta_k)\to\varepsilon_1$, $(\theta_+,\varepsilon_1)\in F_{c_0}$
   ($F_{c_0}=\{\Phi_0=c_0\}$ замкнуто). Пусть $\varepsilon_b$, $\rho_\theta$ — из (CM) в $(\theta_+,\varepsilon_1)$, $\rho:=\rho_\theta/2$, и $\rho'$ — радиус единственности
   из (CM), (ii), общий для $|\theta-\theta_+|\le\rho$; уменьшив $\rho$, считаем $|\varepsilon_b-\varepsilon_1|<\rho'/4$ на $[\theta_+-\rho,\theta_++\rho]$ (непрерывность $\varepsilon_b$).
   При большом $k$ $\theta_k>\theta_+-\rho$ и $|\varepsilon_g(\theta_k)-\varepsilon_1|<\rho'/4$, так что $|\varepsilon_g(\theta_k)-\varepsilon_b(\theta_k)|<\rho'/2$ и $\varepsilon_g(\theta_k)=\varepsilon_b(\theta_k)$. Пусть
   $J_k$ — максимальный подинтервал $(\theta_+-\rho,\theta_+)$, содержащий $\theta_k$, на котором $|\varepsilon_g-\varepsilon_b|<\rho'$; на нём $\varepsilon_g=\varepsilon_b$ (обе —
   критические точки, а в $|\varepsilon-\varepsilon_b(\theta)|<\rho'$ критическая точка одна). Если бы правый конец $b_k$ интервала $J_k$ был меньше $\theta_+$, то
   по непрерывности $\varepsilon_g(b_k)=\varepsilon_b(b_k)$, и неравенство $|\varepsilon_g-\varepsilon_b|<\rho'$ выполнялось бы и правее $b_k$ — противоречие с
   максимальностью. Значит, $J_k\supset[\theta_k,\theta_+)$. $\varepsilon_b$ продолжает $\varepsilon_g$; $G_b$ аналитична и равна $c_0$ на $[\theta_k,\theta_+)$, значит, $G_b\equiv c_0$ около $\theta_+$ и
   $(\theta,\varepsilon_b)\in F_{c_0}$ — противоречие с максимальностью. Итак, $I=\mathbb R$.
3. *Периодичность.* $\varepsilon_g(\cdot+L)$ — такая же функция; по п. 1 либо совпадает с $\varepsilon_g$, либо разность знакопостоянна, и тогда
   $\varepsilon_g(\theta_0+kL)$ строго монотонна, хотя лежит в конечном множестве нулей ненулевого многочлена $\Phi_0(\theta_0,\cdot)-c_0$.
4. *Профиль.* Кратность из (CM) постоянна на интервале (CM), значит, вдоль $\varepsilon_g$; $\mathsf p_g:=\sum_{k\ge2r'}\frac1{k!}\partial_\varepsilon^k\Phi_0(\theta,\varepsilon_g)e^{k-2r'}$.
   Около каждой точки $\varepsilon_g$ совпадает с ветвью (CM) (п. 1), поэтому $\mathsf p_g(\theta,0)=\mathsf p(\theta,0)>0$ по (CM) (из минимальности
   следовало бы лишь $\ge0$). $\square$

**Лемма U.**

1. Точки глобального минимума $\Phi_0(\theta',\cdot)$ — $\varepsilon_1,\dots,\varepsilon_K\in(-E_0,E_0)$; по (R) они невырождены.
2. Для каждого $k$: радиус $\varrho_k\in(0,\frac12)$ и $V_k=(-\varsigma_k,\varsigma_k)\times(\theta'-\varsigma_k,\theta'+\varsigma_k)$ с $\partial_\varepsilon^2\tilde U\ge m_k>0$ на $\overline{V_k}\times[\varepsilon_k-\varrho_k,\varepsilon_k+\varrho_k]$;
   по аналитической теореме о неявной функции (после уменьшения $\varsigma_k$) аналитическая $\varepsilon_k^*$ на $V_k$, $\varepsilon_k^*(0,\theta')=\varepsilon_k$,
   $|\varepsilon_k^*-\varepsilon_k|<\varrho_k/2$ — единственный нуль $\partial_\varepsilon\tilde U(\sigma,\theta,\cdot)$ на $[\varepsilon_k-\varrho_k,\varepsilon_k+\varrho_k]$ (строгая выпуклость). Тейлор:
   $\tilde U(\sigma,\theta,\varepsilon_k^*+e)=\hat G_k+e^2M_k$, $M_k=\int_0^1(1-t)\partial_\varepsilon^2\tilde U(\sigma,\theta,\varepsilon_k^*+te)dt\ge m_k/2$ при $|e|<\varrho_k/2$: (UR1) с $r_k=1$.
3. *(UR2).* $\rho_U\in(0,\min_k\varrho_k/2)$ с непересекающимися $(\varepsilon_k-\rho_U,\varepsilon_k+\rho_U)\subset(-E_0,E_0)$, $O$ — их объединение;
   $d_U:=\min\{\Phi_0(\theta',\varepsilon)-G_{\min}(\theta'):\ \varepsilon\in[-E,E]\setminus O\}>0$; $\rho_U'\in(0,\rho_U)$ с $\Phi_0(\theta',\cdot)<G_{\min}(\theta')+\frac{d_U}3$ при $|\varepsilon-\varepsilon_k|<\rho_U'$;
   $J\ni\theta'$ и $\sigma_J\le\sigma_1$ с $(-\sigma_J,\sigma_J)\times J\subset V_k$ при всех $k$, $|\tilde U-\Phi_0(\theta',\cdot)|<\frac{d_U}3$ при $|\varepsilon|\le E+1$ и $|\varepsilon_k^*-\varepsilon_k|<\rho_U'$
   (так что $|\varepsilon_k^*|<E_0$). Тогда при $0\le\sigma<\sigma_J$ $\tilde U(\sigma,\theta,\varepsilon_k^*)<G_{\min}(\theta')+\frac{2d_U}3<\tilde U(\sigma,\theta,\varepsilon)$ вне $O$; точка глобального
   минимума на $[-E,E]$ лежит в некотором $(\varepsilon_k-\rho_U,\varepsilon_k+\rho_U)\subset(-E,E)$, критическая, и равна $\varepsilon_k^*$. $\square$

**Лемма B′.**

1. По наблюдению (UR0) в точках $F_{c_0}$ (это точки глобального минимума) выполнено (CM). Точка $(\theta_0,\varepsilon_k^*(0,\theta_0))$ лежит в
   $F_{c_0}$ ($c_0\le G_{\min}\le G_k\equiv c_0$), и ветвь (CM) в ней совпадает с $\varepsilon_k^*(0,\cdot)$ (единственность), так что $G_b=G_k\equiv c_0$ около $\theta_0$.
   Лемма B даёт периодическую $\varepsilon_g$ с $\varepsilon_g=\varepsilon_k^*(0,\cdot)$ около $\theta_0$; $|\varepsilon_g|<E_0$.
2. Покроем $[0,L]$ интервалами $J_1,\dots,J_p$ из (UR), $J_i'\subset J_i$ — компактные, их внутренности покрывают $[0,L]$. На $J_i$ есть
   ветвь $k_i$ с $\varepsilon_{k_i}^*(0,\cdot)=\varepsilon_g$ на всём $J_i$. Действительно, по (UR2) при $\sigma=0$ множества $A_k:=\{\theta\in J_i:\ \varepsilon_k^*(0,\theta)=\varepsilon_g(\theta)\}$
   покрывают $J_i$; каждое замкнуто (непрерывность) и открыто: если $\theta^\circ\in A_k$, то около $\theta^\circ$ и $\varepsilon_k^*(0,\cdot)$, и $\varepsilon_g$ —
   критические точки $\Phi_0(\theta,\cdot)$ в радиусе единственности ветви (UR1) при $\sigma=0$, значит, совпадают. $J_i$ связен, так что
   одно из $A_k$ — весь $J_i$. Для интервала, содержащего $\theta_0$, можно взять $k_i=k$.
3. *Склейка.* По (UR1) $2r_kM_k+e\partial_eM_k>0$ на $[0,\sigma']\times J_i'\times[-e',e']$, так что единственность критической точки около $\varepsilon_{k_i}^*$
   равномерна; на пересечениях $\varepsilon_{k_i}^*=\varepsilon_{k_{i'}}^*$ при малых $\sigma\ge0$, а по аналитичности — при $|\sigma|<\sigma_0$. Получаем $\varepsilon_g^*$ на
   $(-\sigma_0,\sigma_0)\times O$, $O\supset[0,L]$ открыто; около $(0,\theta_0)$ она совпадает с $\varepsilon_k^*$. Уменьшив $\sigma_0$, имеем $|\varepsilon_g^*|<E+\frac12$
   (так как $|\varepsilon_g^*(0,\cdot)|=|\varepsilon_g|<E_0$ и $[0,L]$ компактен).
4. *Периодичность.* $\theta\mapsto\varepsilon_g^*(\sigma,\theta+L)$ — ветвь критических точек ($\tilde U$ периодична), при $\sigma=0$ равная $\varepsilon_g^*(0,\theta)$; по
   равномерной единственности она равна $\varepsilon_g^*(\sigma,\theta)$ при малых $\sigma$, а по аналитичности — при $|\sigma|<\sigma_0$. Отсюда
   периодическое продолжение. $\hat G_g:=\tilde U(\sigma,\theta,\varepsilon_g^*)$, $M_g$ склеивается ($M_k=e^{-2r_k}(\tilde U(\sigma,\theta,\varepsilon_k^*+e)-\hat G_k)$ при $e\ne0$), $r_g$
   постоянно, $e_0:=\min e_{J_i}$. $\square$

### 7. Предложение W′ и теорема Z

**Предложение W′.**

1. *(W-a).* $G_b\ge G_{\min}\ge-a_0=G_b(\theta_0)$, $G_b$ аналитична и не постоянна около $\theta_0$: $\Lambda(\tau):=G_b(\theta_0+\tau)+a_0=a\tau^{2p}(1+O(\tau))$, $a>0$.
   Теорема W на дуге $|\tau|\le\theta_1$, $\theta_1<\min(\rho_\theta,L/4)$, $|\varepsilon_b|\le E$ на ней ($|\varepsilon_0|<E_0\le E$), $r_W\le\min(\theta_1/2,\frac14)$:
   $y_0:=\sigma^{N\gamma_*}\varepsilon_b(\theta_0+\tau)$ ($N\gamma_*\in\mathbb N$), $\tilde F:=\tilde U(\sigma,\theta_0+\tau,\varepsilon_b+e)$ ((0.6) — это (0.3), так как $sy_0+s^ce=s^c(\varepsilon_b+e)$),
   $P=\Lambda(\tau)+e^{2r'}\mathsf p(\theta_0+\tau,e)$. (W1): $P\ge\frac a2\tau^{2p}+\frac{\mathsf p_0}2e^{2r'}$ на малом квадрате. (W2) с $c_2\equiv c$, $\mu_0=1$: где $\tau\Lambda'\ge\Lambda$,
   $|e\partial_e\mathsf p|\le\mathsf p/4$, $|\tau\partial_\tau\mathsf p|\le\mathsf p$,
   $\kappa\tau\partial_\tau P+ce\partial_eP=\kappa\tau\Lambda'+e^{2r'}[2r'c\mathsf p+ce\partial_e\mathsf p+\kappa\tau\partial_\tau\mathsf p]\ge\kappa\Lambda+e^{2r'}(\frac74c-\frac12)\mathsf p\ge\kappa P$.
2. *(W-b).* Теорема W на дуге $|\tau|\le\theta_1<L/4$ с $y_0:=\sigma^{N\gamma_*}\varepsilon_0$, $\tilde F:=\tilde U(\sigma,\theta_0+\tau,\varepsilon_0+e)$ ($|\varepsilon_0|<E_0\le E$), $P$ из (DE),
   $r_W\le\min(r_*,\theta_1/2,\frac14)$, $\kappa_0:=\min(\frac12,c/w)$, $c_2(\kappa):=w\kappa$. (W1) на всём $K_W$ следует из (DE) и изолированности
   нуля: по (DE) функция $t\mapsto t^{-\mu_0}P(t\tau,t^we)$ не убывает на $(0,1]$ при $(\tau,e)\in[-r_*,r_*]^2$ (её производная равна
   $t^{-\mu_0-1}[(\tau'\partial_\tau P+w e'\partial_eP)-\mu_0P](t\tau,t^we)\ge0$, где $(\tau',e')=(t\tau,t^we)$), поэтому нуль $P$ в точке $(\tau,e)\ne0$ квадрата дал бы нули
   на всей дуге $\{(t\tau,t^we):\ 0<t\le1\}$, сходящейся к $0$, вопреки изолированности.
3. *(W-c).* В точке $F_{\min}$ $G_b$ имеет локальный минимум; если $G_b\not\equiv-a_0$ — это (W-a); иначе лемма B даёт $\varepsilon_g$, и теорема C с
   $y_0:=\sigma^{N\gamma_*}\varepsilon_g$, $\tilde F:=\tilde U(\sigma,\theta,\varepsilon_g+e)$, $P=e^{2r'}\mathsf p_g$: (C1) с $q_0(t)=\frac12\min\mathsf p_g(\cdot,0)t^{2r'}$, (C2) с $\mu_0=1$ на $|e|\le e_C$, где
   $|e\partial_e\mathsf p_g|\le\mathsf p_g/2$, $\mathsf p_g\ge\frac12\min\mathsf p_g(\cdot,0)$. $\square$

**Теорема Z.**

1. $\theta_*$ — предельная точка $\theta_n$, $J\ni\theta_*$ из (UR). По N2(b) $F_{\rm fl}(s_n,\theta_n)=s_n^j\tilde U(\sigma_n,\theta_n,\varepsilon^\circ)$, $\varepsilon^\circ$ — точка глобального минимума на $[-E,E]$;
   по (UR2) $\varepsilon^\circ=\varepsilon_{k_n}^*$; по подпоследовательности $k_n\equiv k$, $\hat G_k(\sigma_n,\theta_n)<0$.
2. $G_k\ge G_{\min}\ge0$ на $J$, $G_k(\theta_*)\le0$, так что $G_k(\theta_*)=0$.
3. *$G_k\not\equiv0$ около $\theta_*$.* Теорема D на дуге $[\theta_*-\theta_1,\theta_*+\theta_1]\subset J$, $\theta_1<L/4$, $\sigma_J\le\sigma_1$: $y_0:=\sigma^{N\gamma_*}\varepsilon_k^*(\sigma,\theta_*+\tau)$,
   $\tilde F:=\hat G_k+e^{2r_k}M_k$ ((0.6) — это (0.3)); $h_l\equiv0$, (D2) выполнено; $M_0=M_k(0,\theta_*,0)>0$; (D1) — пп. 1, 2.
4. *$G_k\equiv0$ около $\theta_*$.* Лемма B′ ($c_0=0$): глобальная ветвь $g$, $\hat G_g(\sigma_n,\theta_n)<0$. $\kappa':=\min\{i:\ \partial_\sigma^i\hat G_g(0,\cdot)\not\equiv0\}\in[1,\infty)$
   (иначе $\hat G_g\equiv0$ по аналитичности по $\sigma$); $\hat G_g=\sigma^{\kappa'}\hat G'$, $G':=\hat G'(0,\cdot)\not\equiv0$. **Уточнённые данные**: $\varsigma:=\sigma^{1/(2r_g)}$,
   $N':=2r_gN$, $c':=c+\kappa'/N'$, $\beta':=j+\kappa'/N$, $y_0'(\varsigma,\theta):=\varsigma^{2r_gN\gamma_*}\varepsilon_g^*(\varsigma^{2r_g},\theta)$,
   $\tilde F'(\varsigma,\theta,e'):=\hat G'(\varsigma^{2r_g},\theta)+e'^{2r_g}M_g(\varsigma^{2r_g},\theta,\varsigma^{\kappa'}e')$. Проверка (0.6): $s^{c'}e'=s^c\varsigma^{\kappa'}e'$, и
   $U(s\omega+(sy_0'+s^{c'}e')n)=s^j[\sigma^{\kappa'}\hat G'+\sigma^{\kappa'}e'^{2r_g}M_g(\sigma,\theta,\varsigma^{\kappa'}e')]=s^{\beta'}\tilde F'$; $\tilde F'(0,\theta,e')=G'(\theta)+M_g(0,\theta,0)e'^{2r_g}$.
   - $\min G'<0$, $G'\equiv\mathrm{const}$: теорема C, $P=M_g(0,\theta,0)e'^{2r_g}$, $\mu_0=2r_g$.
   - $\min G'<0$, $G'\not\equiv\mathrm{const}$: в точке глобального минимума $\theta_0$ — теорема W с $P=G'(\theta_0+\tau)-G'(\theta_0)+M_g(0,\theta_0+\tau,0)e'^{2r_g}$, $c_2\equiv c'$,
     $\mu_0=1$ (как в W′, п. 1).
   - $\min G'=0$: после перехода к подпоследовательности $\theta_n\to\theta_*$, и $G'(\theta_*)=\lim\hat G'(\sigma_n,\theta_n)\le0$, то есть $G'(\theta_*)=0$; $G'\ge0$,
     $G'\not\equiv0$ около $\theta_*$; теорема D в $\theta_*$ с уточнёнными данными ($h_l\equiv0$, $M'(0,\theta_*,0)=M_g(0,\theta_*,0)>0$, отрицательность в
     точках $(\sigma_n^{1/(2r_g)},\theta_n)$).
   - $\min G'>0$ невозможно: тогда $\hat G_g(\sigma_n,\theta_n)>0$. $\square$

### 8. Теорема M′ и следствие M′$_R$

По предложению R′ реализуется (P), (W) или (Z). (P): теорема K0 [008] ($u_m(\omega)=0$, $\nabla u_m(\omega)=0$, (H3), $j(\omega)<\infty$,
$g_{j(\omega)}(\omega)<0$). (W): по наблюдению (UR0) (после определения (UR)) выполнено (CM) во всех точках $F_{\min}$, и по предложению W′ (W-c) есть
траектория. (Z):
теорема Z. Неустойчивость — теорема A [007], шаг 6. Изолированность не использована. $\square$

**Следствие M′$_R$.** (R) ⇒ (UR) — лемма U. При (K1), (K2) [010]: точечные компоненты удовлетворяют (H3). Кривая-компонента
аналитична по [010] (§1; [008], §1) — лемма A0 здесь не используется, так как она предполагает (H4) (для леммы Адамара
хватило бы и $C^\infty$-карты). В трубчатой карте $\mathcal E(\theta,y)$ функция $f:=u_m\circ\mathcal E$ имеет $f(\theta,0)=\partial_yf(\theta,0)=0$
($\Sigma_0\subset\{\nabla u_m=0\}$), и по лемме Адамара $f=y^2g_H$, $g_H=\int_0^1(1-t)\partial_y^2f(\theta,ty)dt$, $g_H(\theta,0)=\frac12D^2u_m(\omega)(n,n)>0$ — это (H4)
с $r=1$, $\tau_\Sigma:=y\circ\mathcal E^{-1}$, $g_\Sigma:=g_H\circ\mathcal E^{-1}$ (после сужения окрестности, где $g_H>0$). При $r=1$
$\Phi_0=a(\theta,0)\varepsilon^2+b_1(\theta)\varepsilon+b_0(\theta)$, $a>0$: (R) выполнено. $\square$

## Где работают аналитичность и изолированность

1. **Изолированность не используется** нигде: ни в R′, ни в теоремах W, C, D, Z, M′. Места, где в [011] она «останавливала
   процесс» ($\gamma_*=\infty$; $\hat G\equiv0$), закрыты отрицательными значениями $U$: при $\gamma_*=\infty$ $U\ge0$ в трубке (R′, п. 4), при
   $\hat G_g\equiv0$ отрицательных значений на ветви нет (теорема Z, п. 4). Пример W4 (замечание 3) — неизолированная
   критическая точка, покрытая теоремой [Доказано вручную: кривые $\{x=0,\ z=\pm y^2\}$ состоят из критических точек].
2. **Аналитичность $U$ несёт нагрузку** в следующих местах [Доказано — это места доказательств]:
   - R′, п. 4: «все $\varphi_{il}=0$ при $l<2r$ ⇒ $\varphi=y^{2r}A_\varphi$», то есть $\gamma_*=\infty$ ⇒ $U\ge0$ в трубке. [Доказано, пример R41] Для $C^\infty$ неверно:
     у $z^4-e^{-1/(x^2+y^2)}$ $\gamma_*=\infty$, но $U<0$ около экватора;
   - леммы N1, N2 [011]: (0.3), (0.4) и данные (0.6) с непрерывным $\tilde F$ — конечный порядок глубины $-a_0s^j$;
   - условие (UR), лемма U: аналитичность $\tilde U$ по $\sigma$;
   - конечность $\kappa'$ (теорема Z, п. 4);
   - лемма V [010] в теореме D (Вейерштрасс, Ньютон–Пюизё).

   **Не зависят от аналитичности $U$**: лемма A0 (только полиномиальность $u_m$); коэффициенты $\Phi_0$ и функция $G_b$ определяются
   конечной струёй, так что дихотомия «конечный порядок или константа» в W′ и лемма B (теорема единственности для
   $G_b$ в п. 2, конечность нулей многочлена в п. 3) верны для любого $U$ с той же струёй.
3. **Теоремы W, C** — утверждения для $U\in C^2$ при данных (NF$_W$), (NF$_C$); **теорема D** — для $U\in C^2$ при аналитических данных.
   [Эскиз] С примерами Пенлеве–Уинтнера и Лалуа (по `problem/KNOWN_RESULTS.md`, не сверено) противоречия нет: если все
   однородные части нулевые, (0.6) с $a_0>0$ невозможно, а (H1) требует $u_m\not\equiv0$. Пример Уреньи касается тотальной
   неустойчивости; здесь утверждается одна асимптотическая траектория.
4. Все рассуждения вещественные; число Милнора не используется.

## Замечания

### 1. Частные случаи [Доказано]

- Теорема Mb [010] — теорема W с $y_0(\varsigma,\theta)=y^*(\varsigma^2,\theta)$, $N=2$, $c_2\equiv c$, $P=\Lambda+\frac12h_ne^2$, $\mu_0=1$ ((0.8) совпадает с формулой (0.4) теоремы Mb в [010] с точностью до
  константы; оценки $|\theta(t)|\le R_\theta(\delta)$, $|e(t)|\le R_e(\delta)$ — те же по порядку, с другими константами, чем явные
  $(8\delta/a)^{1/(2p)}$, $4\sqrt{\delta/h_n(0)}$ в Mb); теорема N [011] — случай $p=1$ (тогда $R_\theta^2\asymp\delta$ и $\kappa(\delta)$ отделено от нуля).
- $r\equiv1$: следствие M′$_R$ даёт теорему M [010]. При $r=1$ $2\gamma_*\in\mathbb N$, и по N2 $R=s^{2\gamma_*}(G_{\min}+O(s^{1/N}))$: при $G_{\min}\not\equiv0$ $j$ первого
  ребра совпадает с $j$ из [008]; при $G_{\min}\equiv0$ к нему ведёт один шаг уточнения.
- Однородный $U=u_m$: $\gamma_*=\infty$, $U\ge0$. Невырожденная $u_m$: $\Sigma=\varnothing$, строгий минимум.
- Квазиоднородный $U=z^{2r}+v(x,y)$, $\deg v=k>2r$: $\tilde U=\varepsilon^{2r}+v(\theta)$ точно, (UR) с жёсткой ветвью; траектория есть ⟺ $\min v|_{S^1}<0$ ⟺ $0$
  не минимум; плоскость $z=0$ инвариантна, ср. Козлов–Паламодов 1982 [по `problem/KNOWN_RESULTS.md`, не сверено].
- $n=2$: для $U=V(x,y)+z^{2r}$ (младшая степень $V$ больше $2r$) $\tilde U$ зависит от $\varepsilon$ только через $\varepsilon^{2r}$, (UR) выполнено; плоскость $z=0$
  инвариантна, и вывод согласуется с [005] в смысле неустойчивости.

### 2. Зачем свободный нормальный вес

[Доказано] Для $P_0=e^4+\theta e^2+\theta^2$ при $c_2=c$ форма $\kappa\theta\partial_\theta P_0+ce\partial_eP_0=4ce^4+(\kappa+2c)\theta e^2+2\kappa\theta^2$ неотрицательна при $e^2\ge0$ тогда и только
тогда, когда $(\kappa+2c)^2\le32c\kappa$, то есть $\kappa\ge(14-\sqrt{192})c\approx0{,}144c$: при меньших $\kappa$ неравенство (0.7) с $c_2=c$ неверно при любом $\mu_0\ge0$. При
$c_2=\kappa/2$ $\kappa(\theta\partial_\theta P_0+\frac12e\partial_eP_0)=2\kappa P_0$. [Эксперимент] Что поле Mb ($\lambda_n=0$) для примера W3 не даёт строгого выхода, видно
численно (замечание 6, R40 §1.7); это утверждение о методе, а не об отсутствии траектории.

### 3. Примеры

Во всех примерах $u_4=z^4$, $\Sigma$ — экватор, $r=2$, $k_g=0$; $\rho^2=x^2+y^2$. [Доказано вручную; [Эксперимент]
`examples_mult.py`]

| Пример | $U$ | $\gamma_*$, $j$, $c$ | $\Phi_0$ | Случай и теорема |
|---|---|---|---|---|
| W1 | $(z-x^2)^4+\frac32x\rho^4-\frac12x^3\rho^2+yz^5$ | $\frac14$, $5$, $\frac54$ | $\varepsilon^4+\frac12\cos\theta(3-\cos^2\theta)$ | (W), минимум в $\pi$ порядка $4$, $r'=2$; (CM), (UR) нет → W′(W-a) |
| W2 | $z^4+zf_4+x^6+yz^5$, $f_4|_{S^1}=9-8\sin^4\theta$ | $\frac13$, $\frac{16}3$, $\frac43$ | $\varepsilon^4+f\varepsilon$ | (W), (R), минимум $G$ порядка $4$, $r'=1$ → т. W |
| W3 | $z^4+z^2y\rho^2-\rho^6+y^2\rho^4+xz^5+y^7$ | $\frac12$, $6$, $\frac32$ | $(\varepsilon^2+\frac{\sin\theta}2)^2+\frac34\sin^2\theta-1$ | (W), расщепление ((CM) нет), (DE) с $w=\frac12$ → W′(W-b) |
| W4 | $(z^2-\rho^4)^2+zx^8$ | $1$, $8$, $2$ | $(\varepsilon^2-1)^2$ | (Z), (R), $G\equiv0$; уточнение $\kappa'=2$, $G'=-\cos^8\theta$ → т. W; $0$ не изолирована |
| C1 | $(z+xy)^4-\rho^6+x^7+z^3y^4$ | $\frac12$, $6$, $\frac32$ | $\varepsilon^4-1$ | (W), $G\equiv-1$, (CM) на всём дне → т. C |
| C2 | $z^4+z\rho^4+x^6z+y^7$ | $\frac13$, $\frac{16}3$, $\frac43$ | $\varepsilon^4+\varepsilon$ | (W), (R), $G\equiv-\frac38 2^{1/3}$ → т. C |
| D1 | $(z-xy-x^3)^4+y^2\rho^4+x^7$ | $\frac12$, $6$, $\frac32$ | $\varepsilon^4+\sin^2\theta$ | (Z), (UR) (жёсткая ветвь), $\hat G=\sin^2\theta+\sigma^2\cos^7\theta$ → т. D в $\pi$ |
| D2 | $(z^2-\rho^4)^2+y^2\rho^6+x^9+z^3x^6$ | $1$, $8$, $2$ | $(\varepsilon^2-1)^2+\sin^2\theta$ | (Z), (R) → т. D в $\pi$ |
| D3 | $(z^2-\rho^4)^2+z^2y^2\rho^4+x^{11}$ | $1$, $8$, $2$ | $(\varepsilon^2-1)^2$ | (Z), (R), $G\equiv0$; $\kappa'=2$, $G'=\sin^2\theta$ → т. D в $\pi$ |

Для W3 [Доказано]: $\tau\partial_\tau P+\frac12e\partial_eP-2P=(\tau\cos\tau-\sin\tau)(e^2+2\sin\tau)$, при $|\tau|\le0{,}2$ $P\ge0{,}36(\tau^2+e^4)$ и $|$правая часть$|\le0{,}17P$,
так что (DE) выполнено с $w=\frac12$, $\mu_0=1$. Изолированность $0$ [Эксперимент: Грёбнер, sympy]: W1, W2, W3, W4 $+\,y^{11}$, C1,
C2, D2, D3; D1 — вручную; W4 не изолирована (кривые $\{x=0,\ z=\pm y^2\}$ критические).

### 4. Открытое [Гипотеза]

Без (UR) полнота разбора не доказана. Остаются:

- **(O1)** расщепление ветви в точке минимального дна без диагонального поля Эйлера. Пример: $r=3$, $\gamma_*=3$,
  $\Phi_0=-1+G_1G_2$, $G_1=\varepsilon^2+k\hat\theta^2\varepsilon+\hat\theta^4$, $G_2=\hat\theta^2+k\hat\theta\varepsilon^2+\varepsilon^4$, $\hat\theta=\sin\theta\cos\theta$, $\frac{8\sqrt3}7\le k<2$ (реализуется многочленом
  $U=z^6+\sum_{l<6}z^lh_l$, $\deg h_l=4(6-l)$); у главной части $G_1G_2$ диагонального поля Эйлера нет ([009], предложение 5.4).
  Нужен недиагональный вариант теоремы W; трудность — угловая компонента поля не должна зависеть от узкой
  нормальной координаты (член порядка $s^{1-c}$ в $s\langle w,D_wY\rangle$); следствие 6.1 [009] здесь не применимо ($Q_d(0,1)=0$), теорема
  2U [012] относится к узким направлениям.
- **(O2)** складки минимального дна. Пример O2: $U=z^4-2z^2y\rho^2-x^2\rho^4+x^7+y^7$, $\Phi_0=(\varepsilon^2-\sin\theta)^2-1$, $G_{\min}\equiv-1$ на $[0,\pi]$,
  минимальное дно — овал $\{\varepsilon^2=\sin\theta,\ 0\le\theta\le\pi\}$ со складками в $\theta=0,\pi$.
  [Доказано] Ни одно из (W-a)–(W-c) не выполнено. Во внутренних точках дна ветви $\pm\sqrt{\sin\theta}$ невырождены
  ($\partial_\varepsilon^2\Phi_0=8\sin\theta>0$), но $G_b\equiv-1$ — нет (W-a); нуль профиля лежит на дуге дна и не изолирован — нет (W-b). В складке
  $(0,0)$ $\partial_\varepsilon^k\Phi_0=0,0,0,24$ ($k=1,2,3,4$); единственный кандидат в ветвь (CM) — корень $\varepsilon_b\equiv0$ многочлена $\partial_\varepsilon^3\Phi_0=24\varepsilon$, а
  $\partial_\varepsilon^2\Phi_0(\theta,0)=-4\sin\theta\not\equiv0$, так что (CM) нарушено (нет (W-c) и (W-a)); нуль $(e^2-\sin\tau)^2$ не изолирован (нет (W-b)); то же в
  $(\pi,0)$. [Доказано] $\tilde U=\Phi_0+\sigma^2(\cos^7\theta+\sin^7\theta)$ точно ($N=2$, $\sigma^2=s$), поэтому при малых $s$
  $F_{\rm fl}/s^6=G_{\min}(\theta)+s(\cos^7\theta+\sin^7\theta)$; на дуге $[0,\pi]$ это не меньше $-1-s$ с равенством только при $\theta=\pi$ ($\sin\theta\ge0$, $\cos^7\theta\ge-1$), а
  вне дуги $-\cos^2\theta+s(\cos^7\theta+\sin^7\theta)\ge-1+\sin^2\theta-s-s|\sin\theta|^7>-1-s$. Глобальный минимум функции дна достигается ровно в
  складке, так что препятствие не обходится уточнением во внутренней точке дуги (R41). $0$ изолирована [Эксперимент:
  Грёбнер в sympy; R41 — Singular, $\mu=86$]; при этом условии (UR) не следует из изолированности (так как (UR) влечёт (CM)
  на $F_{\min}$ по (UR0)).
- **(O3)** каскад при нежёстком вырожденном профиле: ветвь в слое меняет кратность при $\sigma>0$, и никакое приближённое
  дно не даёт (D2); профиль в $(t,b_1,b_2)$ задаётся трёхмерным многогранником Ньютона, и диагональное неравенство
  Эйлера не гарантировано.

### 5. Касание луча

В теореме D касание доказано. В теоремах W, C — нет (в W — только конус раствора $R_\theta(\delta)$; в C угол не контролируется).
[Гипотеза] В W касание есть.

### 6. Эксперименты [Эксперимент]

- `frames_W.py`: (3.1)–(3.7) символьно, 16 тождеств, отрицательный контроль. R40 — независимо, в том числе численно в
  $\mathbb R^3$ на локсодроме с переменной $k_g$.
- `floor_mult.py`: функция дна всех примеров совпадает с предсказанием (W: $\min_\theta F_{\rm fl}/s^j\to-a_0$; C: равномерно по $\theta$; D:
  $\min_\theta F_{\rm fl}/s^{\beta_d}\to-1$ при $\theta=\pi$).
- `exit_W.py`, `exit_W3_wall.py`: строгий выход (A5) прямым дифференцированием. W3 (по стенке, 256 лучей, $s=10^{-12}$): поле теоремы
  W даёт $\approx2\kappa>0$, поле Mb ($\lambda_n=0$) — $-0{,}357$, $-0{,}250$, $-0{,}035$ ($\delta=0{,}01$) и $-0{,}355$, $-0{,}248$, $-0{,}032$ ($\delta=0{,}002$) при $\kappa=0{,}05;0{,}1;0{,}2$
  (совпадает с минимумом отношения Эйлера; R40 — независимо, включая $\kappa=\kappa(\delta)$ при $\delta=10^{-5}$). W1, W2 ($p=2$): выход положителен лишь
  при $\kappa\lesssim\delta^{1/2}$, что согласуется с $\kappa(\delta)\asymp\delta^{1-1/p}$; асимптотический режим — при $s\lesssim10^{-16}$–$10^{-20}$.
- `isolated.py`, `check_DE.py` — см. замечание 3.

## Отличия от записки

Записка `notes/prover/2026-10-21-morse-bott-mult.md` (вторая редакция) уже содержит все правки по R40, R41 (её §15).
Здесь:

1. Нумерация формул: (1.1)–(1.5) → (0.1)–(0.5); (2.1)–(2.6) → (0.6)–(0.11); (5.1)–(5.8) → (3.1)–(3.8); (7.1), (7.2) → (5.1),
   (5.2); (M) — без изменений. Разделы доказательств: записка §3–§9 → здесь §1–§8.
2. Теорема M′ и следствие M′$_R$ вынесены в начало «Утверждения»; вывод (K2) ⇒ (H4) по лемме Адамара — в доказательстве
   следствия M′$_R$ (§8), а не в замечаниях.
3. Сокращены пояснения: пример O1 и пример O2 — в замечании 4; таблица примеров и эксперименты — в замечаниях 3, 6;
   численные таблицы записки (§10.3) не перенесены.
4. Правки по R40 (перечень в записке, §15, пп. 1–11): $\bar k_g$ для дуги и $\sigma_0=s_2$; дважды $\kappa|\theta|\le1$; существенность
   $\lambda_n\ge0$; (0.7) нужно лишь при $\kappa(\delta)$; переформулировка «зачем свободный нормальный вес» (замечание 2);
   радиусы в леммах B, U; периодичность в лемме B′; уточнения об аналитичности для теоремы D; перепроверка значения
   для поля Mb (замечание 6).
5. Правки по R41 (записка, §15, пп. 12–22): строгие неравенства и окна в W′; явные условия в (UR); $0<x<s_1(\omega)$ в лемме T(b);
   формулировка (D2); дуга внутри $J$ в теореме Z; раздел об аналитичности; (K2) ⇒ (H4); инвариантность плоскости в $n=2$;
   $h\le\frac32$ в теореме C; данные R41 по O2.

**Правки по R43, R44** (отзывы [`notes/reviewer/2026-10-21-result014-A.md`](../notes/reviewer/2026-10-21-result014-A.md) и
[`...-B.md`](../notes/reviewer/2026-10-21-result014-B.md); новых утверждений нет).

6. R43 З1: нормальный вес поля теоремы W переименован $\lambda\to\lambda_n$ (буква $\lambda$ — только $-p/h$ из [007]); трубчатое отображение
   $E(\theta,y)\to\mathcal E(\theta,y)$; функция $A\to A_\varphi$ в $\varphi=y^{2r}A_\varphi$, множество в лемме T(a) $\to\mathcal A$; квадрат $K\to K_W$; в (H4)
   $\tau,g\to\tau_\Sigma,g_\Sigma$; в лемме U $g,\rho,\rho'\to d_U,\rho_U,\rho_U'$, в R′ $g\to g_0$, в M′$_R$ коэффициенты $b,c\to b_1,b_0$; о перегрузке $n$, $E$, $K$ —
   фраза в «Обозначениях».
7. R43 З2, R44 З10: в (CM) один радиус $\rho_\theta$ (по $\theta$); сказано, что $\mathsf p$ — многочлен по $e$; добавлено обоснование
   эквивалентности с тождествами $\partial_\varepsilon^k\Phi_0(\theta,\varepsilon_b)\equiv0$ и единственности критической точки (на интервале $|\theta-\theta'|\le\rho_\theta/2$).
8. R43 З3, З4: в лемме B, п. 2 — $J_k\supset[\theta_k,\theta_+)$ и шаг о правом конце; в п. 4 положительность $\mathsf p_g(\theta,0)$ выведена из (CM).
9. R43 З5: в лемме T определён $C_\omega$ (как в K4 [008]); $y'<1$; при $\gamma_*=\infty$ $F_{\rm fl}$ — только определение-минимум.
10. R43 З6, R44 З3: в N2 на окружности (a) не зависит от $s$; $s_2(y_1)\le\sigma_1(E+1)^N$; $E_0$, $E$, $\sigma_1$ фиксированы, и (UR) сформулировано
    относительно них; сказано, что доказательства N1, N2 [011] не используют инъективности дуги.
11. R43 З10, З11: в лемме A0 выбрана окрестность $B$ со связной дугой $\{H=0\}\cap B$; в лемме B′, п. 2 расписана открытость множеств
    $A_k$ и совпадение с ветвью $k$ около $(0,\theta_0)$.
12. R43 З12: «ограничение $c_2\le c$ существенно для приведённого доказательства»; возможное ослабление $c_2<c+\frac{\beta-\mu}2$ — [Гипотеза].
13. R44 З1: вынесено наблюдение (UR0) «(UR) ⇒ (CM) на $F_{\min}$» с доказательством; ссылки из §8 и леммы B′ — на него.
14. R44 З2: в W′ (W-b) добавлен вывод (W1) на всём $K_W$ из (DE) и изолированности нуля.
15. R44 З4: в теореме Z, п. 4 предельная точка — та же $\theta_*$. R44 З5: в лемме B′ $|\varepsilon_g^*|<E+\frac12$ после уменьшения $\sigma_0$.
16. R44 З6: константы (L3) в теореме C — $\vartheta_1,\vartheta_2,\vartheta_3$.
17. R44 З7: в замечании 4 (пример O2) — доказательство того, что (W-a)–(W-c) не выполнены, вычисление минимума функции дна в
    складке [Доказано]; вывод «(UR) не следует из изолированности» — при условии изолированности, установленной лишь как
    [Эксперимент].
18. R44 З8: в замечании 1 — совпадение с Mb с точностью до констант и в оценках $|\theta(t)|$, $|e(t)|$.
19. R44 З9: в доказательстве M′$_R$ аналитичность кривой берётся из [010]/[008], а не из леммы A0 (иначе круг).
