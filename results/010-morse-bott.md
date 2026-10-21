# 010. Морс–Ботт при $n=3$: асимптотическая траектория у любой неминимальной критической точки

- **Статус:** [Проверено: reviewer R26, R27, R28 (агенты), 21.10.2026 — доказательства в записке
  [`notes/prover/2026-10-21-morse-bott.md`](../notes/prover/2026-10-21-morse-bott.md); reviewer R32, R33
  (агенты), 21.10.2026 — текст этого результата целиком: ошибок нет]; ждёт проверки человеком.
  - R32 ([`notes/reviewer/2026-10-21-result010-A.md`](../notes/reviewer/2026-10-21-result010-A.md)):
    обозначения, теорема M, лемма N, §2, предложение R, теорема Mc, сборка, раздел об аналитичности.
    Ошибок нет; подтверждено, что изолированность не используется (только «⇐» критерия K4(c) [008] в
    контрапозиции). Редакционные замечания З1–З8.
  - R33 ([`notes/reviewer/2026-10-21-result010-B.md`](../notes/reviewer/2026-10-21-result010-B.md)):
    лемма M, теорема Mb, лемма V, теорема Md. Ошибок нет; редакционные замечания З1–З9.
  - Правки по R32, R33 внёс автор оформления («Отличия от записки», пп. 25–39); новых утверждений
    нет. Главный агент прочитал их и сам прошёл логику снятия изолированности: точки с $U<0$ лежат в
    трубке одной компоненты (вне трубок $U>0$, [008] K4(c)); на ней $U\ge s^mR$, откуда $R\not\equiv0$ и,
    по аналитичности, $j<\infty$; дальше — ветви (P), (a/b), (c), (d).
  - R26 (reviewer, агент, 21.10.2026,
    [`notes/reviewer/2026-10-21-morse-bott-Mb.md`](../notes/reviewer/2026-10-21-morse-bott-Mb.md)):
    §6 записки — лемма M, теорема Mb, формула (6.7), замечания §6.3–§6.4. Ошибок нет; замечания
    З1–З8 редакционные.
  - R27 ([`...-Md.md`](../notes/reviewer/2026-10-21-morse-bott-Md.md)): §5 записки — лемма V,
    теорема Md. Ошибок нет; замечания З1–З6 редакционные (З5 — литература не сверена).
  - R28 ([`...-M.md`](../notes/reviewer/2026-10-21-morse-bott-M.md)): §1–§4, §7–§8 записки — лемма
    N, предложение R, теорема Mc, сборка теоремы M, раздел об аналитичности и изолированности.
    Ошибок нет. Замечание З1: изолированность не нужна. По нему теорема M здесь сформулирована при
    условии «$0$ — не точка локального минимума»; доказательство — то же без одного шага.
  - Все замечания R26–R28 учтены во второй редакции записки (§12 там) и здесь (раздел «Отличия от
    записки»).
  - Метки внутри файла: всё в разделе «Утверждение» — [Доказано]. Замечания помечены каждое
    отдельно.
- **Автор:** prover (агент), записка `notes/prover/2026-10-21-morse-bott.md` (21.10.2026). Оформление —
  prover (агент), 21.10.2026.
- **Зависит от:**
  - [007] = [`results/007-gt3.md`](007-gt3.md): теорема A, лемма 1 (формулы (1.1), (1.3)), лемма 2
    (формулировка и пп. 1–3 доказательства), теорема 2 (класс (GT3), условия $(\Phi0)$–$(\Phi3)$, (F),
    $(V_0)$, $(V_1)$);
  - [008] = [`results/008-class-K.md`](008-class-K.md): данные (S) и определения $R,\eta^*,g_k,j,G,\hat G,c$
    (раздел «Данные (S) и редуцированная функция», §3.2), (U1), (1.1), лемма K1 (§2), лемма K2 (§3,
    формулы (3.1), (3.2)), лемма K3 и карта с дном (§6, формулы (6.1), (6.2), (6.4); там сказано, что
    лемма K3 верна для замкнутой кривой с периодическим $\theta$), теорема K0, предложение K4 (a), (c);
  - [002] = [`results/002-theorem-B.md`](002-theorem-B.md), §2.1(f), §2.2 (аналитичность $\Sigma$), через
    [008];
  - литература (только в лемме V; формулировки — в доказательстве леммы V, п. 1; с первоисточниками
    не сверено): подготовительная теорема Вейерштрасса и теорема Ньютона–Пюизё.
- **Проверочные скрипты** [Эксперимент]:
  - [`experiments/prover/morse-bott/`](../experiments/prover/morse-bott/) — автор записки (тождества
    карт, примеры, дно оврага, строгий выход);
  - `experiments/reviewer/morse-bott-R26/`, `-R27/`, `-R28/` — рецензенты.

## Утверждение

### Обозначения

Обозначения [007] и [008]: $\mathbb R^3$, $B_r$, система $\ddot q=-\nabla U(q)$, асимптотическая траектория
(решение $q(t)\ne0$, $t\ge0$, с $q,\dot q\to0$), $p,h,v_\perp,K_\perp,W,V,\lambda,\Xi$, условия (D1)–(D4), (A4), (A5),
(L0)–(L3) — как в [007]. $U$ вещественно-аналитична в окрестности $0$, $U(0)=0$,
$$U=\sum_{k\ge m}u_k,\qquad m\ge2,\qquad u_m\ge0,\qquad u_m\not\equiv0$$
(тогда $m$ чётно и $\nabla U(0)=0$); $Z=\{u_m=0\}$, $\Sigma=Z\cap S^2$, $N_\omega=(\mathbb R\omega\oplus T_\omega\Sigma)^\perp$.
Условия класса (как (K1), (K2) в [008], но $\Sigma=\varnothing$ допускается):

- **(K1)** $\Sigma$ — гладкое компактное подмногообразие $S^2$ (компоненты — точки и замкнутые кривые);
- **(K2)** (Морс–Ботт) $D^2u_m(\omega)$ положительно определена на $N_\omega$ при всех $\omega\in\Sigma$.

**Кривая-компонента.** Пусть $\Sigma_0$ — компонента-кривая длины $L$; она аналитична ([008], §1; [002],
§2.1(f)). $\omega:\mathbb R\to\Sigma_0$ — натуральная $L$-периодическая аналитическая параметризация,
$\ell=\omega'$, $n=\omega\times\ell$, $k_g$ — геодезическая кривизна, так что ([008], (6.1))
$$\omega'=\ell,\qquad \ell'=-\omega+k_g\,n,\qquad n'=-k_g\,\ell. \tag{0.1}$$
$h_n(\theta):=D^2u_m(\omega(\theta))(n,n)>0$, $h_*:=\min h_n$, $\bar k_g:=\max\lvert k_g\rvert$. Функции
$\varphi$ ((U1) [008] с $p=1$, $e_1=n$), $y^*$, $R$, $\eta^*=sy^*$ (скаляр при $n(\theta)$), $g_k$, $j=j(\Sigma_0)$,
$G=g_j$, $\hat G$ ($R=s^{j-m}\hat G$), $c=\frac{j-m+2}2\ge\frac32$ — как в [008], но с $\theta\in\mathbb R/L\mathbb Z$ (лемма N).
Функция дна $F_{\rm fl}:=s^mR$ (при $j<\infty$ $F_{\rm fl}=s^j\hat G$). Карта с дном ([008], §6):
$$\Pi(s,\theta,\eta)=s\,\omega(\theta)+\eta\,n(\theta),\qquad \Psi(s,\theta,\zeta)=\Pi\big(s,\theta,\eta^*(s,\theta)+\zeta\big),\qquad \eta:=\eta^*+\zeta,\qquad \epsilon:=\frac{k_g\eta}s .$$
Для точечной компоненты $\{\omega\}$ через $R_\omega(s)$ обозначена функция $R$ данных (S) [008] с $d=0$.

### Теорема M (основная)

**Теорема M.** Пусть $n=3$, $U$ — как выше, и выполнены (K1), (K2). Если $0$ — не точка локального
минимума $U$, то у $\ddot q=-\nabla U(q)$ есть асимптотическая траектория, и равновесие $q=0$
неустойчиво по Ляпунову. Изолированность критической точки не предполагается.

В частности, при $n=3$ утверждение (A) выполнено для всех $U$, у которых младшая форма $u_m$
неотрицательна, а её нулевое множество на сфере — многообразие Морса–Ботта. Результат проверен
агентами и ждёт проверки человеком.

### Лемма N (нормальная форма вдоль всей замкнутой компоненты)

**Лемма N.** Пусть $\Sigma_0$ — кривая-компонента. Найдутся $s_1>0$, $y_1\in(0,1)$, $t_1>0$ с $y_1\le t_1$ и
$\bar k_gt_1\le\frac12$ такие, что:

- **(N1)** при $\lvert s\rvert<s_1$, $\theta\in\mathbb R$: $\partial_y^2\varphi(s,\theta,y)\ge h_*/2$ при $\lvert y\rvert<y_1$, и
  $\varphi(s,\theta,\cdot)$ имеет на $(-y_1,y_1)$ единственную критическую точку $y^*(s,\theta)\in(-y_1/2,y_1/2)$ —
  точку глобального минимума на $(-y_1,y_1)$; $y^*$ аналитична на $(-s_1,s_1)\times\mathbb R$, $L$-периодична по
  $\theta$, $y^*(0,\cdot)=0$;
- **(N2)** $R$ аналитична и $L$-периодична, $R(0,\cdot)=0$; если $j<\infty$, то $\hat G$ аналитична и
  $L$-периодична, $\hat G(0,\cdot)=G$. Функция
  $M(s,\theta,\tau):=\int_0^1(1-\lambda)\partial_y^2\varphi(s,\theta,y^*+\lambda\tau)\,d\lambda$ аналитична при $\lvert s\rvert<s_1$,
  $\theta\in\mathbb R$, $\lvert\tau\rvert<y_1/2$, $M\ge h_*/4$, $M(0,\theta,0)=\frac12h_n(\theta)$, и при $j<\infty$, $0<s<s_1$,
  $\lvert\zeta\rvert<\frac{y_1}2s$
  $$U\big(\Psi(s,\theta,\zeta)\big)=s^j\hat G(s,\theta)+s^{m-2}\zeta^2M(s,\theta,\zeta/s); \tag{0.2}$$
- **(N3)** $\Pi$ — аналитический диффеоморфизм $\{s>0,\ \theta\in\mathbb R/L\mathbb Z,\ \lvert\eta\rvert<t_1s\}$ на открытое
  подмножество $\mathbb R^3\setminus0$; $\Pi_s=\omega$, $\Pi_\theta=(s-k_g\eta)\ell$, $\Pi_\eta=n$, $\lvert\Pi\rvert^2=s^2+\eta^2$, функция
  $s\circ\Pi^{-1}$ имеет градиент $\omega(\theta)$;
- **(N4)** при $0<s<s_1$, $\lvert y\rvert<y_1$: $U\big(s(\omega(\theta)+y\,n(\theta))\big)\ge F_{\rm fl}(s,\theta)$.

### Предложение R (разбор случаев)

**Предложение R.** Пусть $n=3$, выполнены (K1), (K2), и $0$ — не точка локального минимума $U$. Тогда
$\Sigma\ne\varnothing$, и верно хотя бы одно из следующего:

- **(P)** есть точечная компонента $\{\omega\}$, у которой $R_\omega\not\equiv0$ и старший коэффициент $R_\omega$
  отрицателен;
- есть кривая-компонента $\Sigma_0$ с $j=j(\Sigma_0)<\infty$, для которой $G=g_j|_{\Sigma_0}$ удовлетворяет одному
  из условий:
  - **(a/b)** $\min G<0$, $G\not\equiv\mathrm{const}$; в точке $\theta_0$ глобального минимума
    $G(\theta_0+\theta)-G(\theta_0)=a\theta^{2p}(1+O(\theta))$ с $a>0$, $p\ge1$;
  - **(c)** $G\equiv\mathrm{const}<0$;
  - **(d)** $\min G=0$, и есть $\theta_0$ с $G(\theta_0)=0$ и точки $(s_k,\theta_k)\to(0,\theta_0)$, $s_k>0$, с
    $\hat G(s_k,\theta_k)<0$.

### Лемма M (вариант леммы 2 [007] с перекрёстными членами)

Обозначения теоремы A [007]; $L_1=2(a_2+\frac{\beta a_1}2)\sqrt{h_1/a_1}$, $L_2=2\sqrt{2a_3/h_0}$ — константы (3.1)
[007]; $D_\sigma=\{q\in\overline D:\ q\ne0,\ \rho(q)<\sigma\}$.

**Лемма M.** Пусть выполнено (D1), а на $D_\sigma$ — (L0), (L1) [007] и

- **(L2)** $W\ge-\delta\rho^\beta$ и $\beta W-\rho\,YW\ge\mu W-\varepsilon_1\delta\rho^\beta$, где $\mu\in(0,\beta)$, $\varepsilon_1\ge0$;
- **(L3M)** для всех $q\in D_\sigma$ и $w\perp Y(q)$:
  $\lvert\langle\nabla\rho-Y/h,w\rangle\rvert\le(\vartheta_1+\gamma_1)\lvert w\rvert$,
  $\rho\lvert\langle\nabla_YY,w\rangle\rvert\le(\vartheta_2+\gamma_2)\lvert w\rvert$,
  $\rho\langle w,D_wY\rangle\ge-\vartheta_3\lvert w\rvert^2$, где $\vartheta_i,\gamma_i\ge0$ — постоянные и $b':=\beta-\mu-2\vartheta_3>0$.

Положим $\Gamma:=\sqrt2\big[(a_2+\beta\delta)\sqrt{h_1/a_1}\,\gamma_1+\sqrt{2a_3/h_0}\,\gamma_2\big]$. Тогда выполнено (D4) и:

1. если $4\sqrt\delta(\vartheta_1+\gamma_1)\le\sqrt{a_1/h_1}$, то в точках $\overline\Omega$ с $q\ne0$, $\rho<\sigma$
   $$-\Big(\sqrt{2(a_3+\delta)/h_0}+\tfrac12\sqrt{a_1/h_1}\Big)\rho^{\beta/2}\le\dot\rho\le-\tfrac12\sqrt{a_1/h_1}\,\rho^{\beta/2}<0,$$
   в частности, выполнено (A4);
2. в каждой точке множества из (A5)
   $$\frac\rho\lambda\,\Xi\ \ge\ \delta\rho^\beta\Big[\mu-\varepsilon_1-\frac{\Gamma^2}{4b'\delta}-\frac{L_1\vartheta_1+L_2\vartheta_2}{\sqrt\delta}\Big]; \tag{0.3}$$
   в частности, (A5) выполнено, если скобка положительна.

### Теорема Mb (случаи (a), (b): отрицательный минимум конечного порядка)

**Теорема Mb.** Пусть $\Sigma_0$ — кривая-компонента, $j<\infty$, $\theta_0=0$ (сдвиг параметра),
$G(0)=-a_0<0$ и $\Lambda(\theta):=G(\theta)-G(0)=a\theta^{2p}(1+O(\theta))$, $a>0$, $p\ge1$. Тогда найдётся $\delta_1>0$
такое, что для каждого $\delta\in(0,\delta_1]$ есть асимптотическая траектория
$q(t)=\Psi\big(s(t),\theta(t),s(t)^ce(t)\big)$ с $s(t)\downarrow0$, $-k_2s^{j/2}\le\dot s\le-k_1s^{j/2}$ ($0<k_1\le k_2$),
$\lvert\theta(t)\rvert\le R_\theta(\delta):=(8\delta/a)^{1/(2p)}$, $\lvert e(t)\rvert\le4\sqrt{\delta/h_n(0)}$. Траектория строится по
теореме A [007] с полем
$$Y_\kappa=\Psi_s-\frac{\kappa\theta}s\Psi_\theta,\qquad \kappa=\kappa(\delta)=\min\Big\{\frac12,\ \frac j{2C_\Gamma^2a_0}\Big(\frac a8\Big)^{1/p}\delta^{1-1/p}\Big\},\qquad C_\Gamma=\frac{15\sqrt3}8j+4. \tag{0.4}$$

### Теорема Mc (случай (c): постоянный $G$)

**Теорема Mc.** Пусть $\Sigma_0$ — кривая-компонента, $j<\infty$, $G\equiv-a_0<0$ на $\Sigma_0$. Тогда есть
асимптотическая траектория $q(t)=\Psi\big(s(t),\theta(t),s(t)^ce(t)\big)$, $\theta\in\mathbb R/L\mathbb Z$, с $s(t)\downarrow0$,
$-k_2s^{j/2}\le\dot s\le-k_1s^{j/2}$ и $\lvert e(t)\rvert\le2\sqrt{2\delta/h_*}$, где $\delta>0$ можно взять сколь угодно
малым. Траектория строится по теореме A [007] с $\rho=s$, $Y=\Psi_s$ в трубке вокруг всего конуса над
$\Sigma_0$; об угле $\theta(t)$ ничего не утверждается.

### Лемма V (дно углового оврага)

**Лемма V.** Пусть $f(s,\tau)$ вещественно-аналитична около $(0,0)\in\mathbb R^2$, $f(0,\tau)=g(\tau)$, $g(0)=0$, $g\ge0$
около $0$, $g\not\equiv0$ (так что $g=g_{2q}\tau^{2q}+\dots$, $g_{2q}>0$, $q\ge1$), и $f(s_k,\tau_k)<0$ при некоторых
$s_k\downarrow0$, $\tau_k\to0$. Тогда есть $\tau_0>0$, $s_3>0$, чётное $N\in\mathbb N$, натуральное $A_V$, чётное натуральное
$\Gamma_V$, $a_V>0$, функция $T$, аналитическая около $0$ с $T(0)=0$, и многочлен $Q_V(b)=\sum_{k\in K_*}c_kb^k$,
$K_*\subset\{2,\dots,2q\}$, $c_k\ne0$, такие, что:

1. при $s\in(0,s_3)$ точка $\tau_v(s):=T(s^{1/N})\in(-\tau_0,\tau_0)$ — точка глобального минимума $f(s,\cdot)$ на
   окне $[-\tau_0,\tau_0]$, $\partial_\tau f(s,\tau_v(s))=0$, $f(s,\tau_v(s))<0$;
2. для любого $B>0$ функция $\hat\Phi(t,b):=t^{-\Gamma_V}f\big(t^N,T(t)+t^{A_V}b\big)$ продолжается до
   вещественно-аналитической на $\{\lvert t\rvert<t_2\}\times\{\lvert b\rvert<B\}$ при некотором $t_2=t_2(B)>0$, и
   $\hat\Phi(0,b)=-a_V+Q_V(b)$;
3. $Q_V\ge0$ на $\mathbb R$; младшая степень $k_0:=\min K_*$ чётна и $c_{k_0}>0$.

В терминах $s$: глубина дна $f(s,\tau_v(s))=-a_Vs^\gamma(1+o(1))$, $\gamma=\Gamma_V/N>0$; угловая ширина оврага
$s^\alpha$, $\alpha=A_V/N>0$.

### Теорема Md (случай (d): каскад)

**Теорема Md.** Пусть $\Sigma_0$ — кривая-компонента, $j<\infty$, $\theta_0\in\mathbb R$, $G\ge0$ около $\theta_0$,
$G(\theta_0)=0$, и $\hat G(s_k,\theta_k)<0$ при некоторых $s_k\downarrow0$, $\theta_k\to\theta_0$. Пусть $N,A_V,\Gamma_V,a_V,T,Q_V,k_0$ —
из леммы V для $f(s,\tau):=\hat G(s,\theta_0+\tau)$, $\alpha=A_V/N$, $\gamma=\Gamma_V/N$, $\tau_v(x)=T(x^{1/N})$,
$$\beta:=j+\gamma,\qquad c_1:=1+\alpha,\qquad c':=\frac{\beta-m+2}2>1 .$$
Тогда при подходящих $s_0,r_0$ карта
$$\Phi(x,u,\zeta):=\Psi\Big(x,\ \theta_0+\tau_v(x)+\frac ux,\ \zeta\Big),\qquad b=(b_1,e)=\big(u\,x^{-c_1},\ \zeta\,x^{-c'}\big), \tag{0.5}$$
задаёт принадлежность $U$ классу (GT3) [007] с $n=3$, весами $(c_1,c')$, этим $N$, $C_1=0$ и условием $(V_0)$
(при $k_0=2$ — и $(V_1)$). Следовательно, по теореме 2 [007] есть асимптотическая траектория
$q(t)=\Phi(x(t),u(t),\zeta(t))$ с $x(t)\downarrow0$, $x(t)\asymp t^{-2/(\beta-2)}$ ($\beta>m\ge2$), $b(t)$ в компакте внутри
$B_{r_0}$, и она касается луча: $q(t)/\lvert q(t)\rvert\to\omega(\theta_0)$.

## Доказательство

### 1. Лемма N

1. *(N1).* Доказательство леммы K1 [008, §2] использует только аналитичность данных и условия
   $u_m(\omega)=0$, $\nabla u_m(\omega)=0$, $h_n>0$ в каждой точке, но не инъективность $\omega$. Применим его с
   $\Lambda'=\mathbb R$, $\Lambda=[0,L]$ и получим $s_1,y_1$ и утверждения при $\theta\in\Lambda''\supset[0,L]$. Так как
   $\varphi(s,\theta+L,y)=\varphi(s,\theta,y)$, выпуклость и единственность критической точки переносятся на все
   $\theta$; единственность даёт $y^*(s,\theta+L)=y^*(s,\theta)$, а аналитичность в любой точке $\theta$ следует из
   $y^*(s,\theta)=y^*(s,\theta-kL)$. Константа $\lambda_H$ леммы K1 равна $h_*$.
2. *(N2).* Аналитичность $R$, $\hat G$ — [008, §3.2]; периодичность — из (N1). Формула (0.2) —
   доказательство леммы K2 [008, §3]: точка $\Psi(s,\theta,\zeta)$ равна $s\big(\omega+(y^*+\tau)n\big)$, $\tau=\zeta/s$,
   $\lvert\tau\rvert<y_1/2$; по (1.1) [008] $U=s^m\varphi(s,\theta,y^*+\tau)$; формула Тейлора с интегральным остатком
   в точке $y^*$, где $\partial_y\varphi=0$ (отрезок $[y^*,y^*+\tau]\subset(-y_1,y_1)$), даёт $\varphi=R+\tau^2M$, откуда
   $s^m(R+\zeta^2s^{-2}M)=s^j\hat G+s^{m-2}\zeta^2M$. Далее $M\ge\frac{h_*}2\int_0^1(1-\lambda)d\lambda=\frac{h_*}4$ и
   $M(0,\theta,0)=\frac12\partial_y^2\varphi(0,\theta,0)=\frac12h_n(\theta)$.
3. *(N3).* Лемма K3 [008, §6] для замкнутой кривой: $E(\theta,t)=(\omega+tn)/\sqrt{1+t^2}$ — локальный
   диффеоморфизм около $(\mathbb R/L\mathbb Z)\times\{0\}$ (столбцы $\ell,n$) и инъективен на этом компакте
   (вложенная кривая); значит, инъективен на $(\mathbb R/L\mathbb Z)\times[-t_1,t_1]$ при малом $t_1$. Из
   $\Pi=s\sqrt{1+t^2}E(\theta,\eta/s)$ следует инъективность $\Pi$; производные — по (0.1); они попарно
   ортогональны и ненулевые ($s-k_g\eta\ge s/2$ при $\bar k_gt_1\le\frac12$); $\nabla s=\Pi_s/\lvert\Pi_s\rvert^2=\omega$. В
   лемме K1 [008] $y_1$ можно брать сколь угодно малым (с меньшим $s_1$), поэтому сначала выбирается
   $t_1$, затем $y_1\le t_1$ и $s_1$.
4. *(N4)* — глобальная минимальность $y^*$ (N1) и (1.1) [008] при $s>0$. $\square$

### 2. Карта с дном, малые величины, нормальная форма в масштабе

Выберем $s_2\in(0,s_1)$ с $\lvert\eta^*\rvert\le\frac{y_1}4s$ при $0<s<s_2$. На
$\{0<s<s_2,\ \theta\in\mathbb R/L\mathbb Z,\ \lvert\zeta\rvert<\frac{y_1}4s\}$ отображение $\Psi$ — аналитический диффеоморфизм на
открытое множество (композиция $\Pi$ и сдвига $\zeta\mapsto\eta^*+\zeta$), координата $s$ у него та же, что у $\Pi$,
и $\nabla s=\omega(\theta)$. По [008, (6.4)]
$$\Psi_s=\omega+\eta^*_s\,n,\qquad \Psi_\theta=s(1-\epsilon)\ell+\eta^*_\theta\,n,\qquad \Psi_\zeta=n. \tag{2.1}$$

**Малые величины.** $y^*$ аналитична, периодична, $y^*(0,\cdot)=0$, поэтому равномерно по $\theta$:
$\eta^*=O(s^2)$, $\eta^*_s=O(s)$, $\eta^*_\theta=O(s^2)$, $\eta^*_{ss}=O(1)$, $\eta^*_{s\theta}=O(s)$, $\eta^*_{\theta\theta}=O(s^2)$. Если
$\lvert\zeta\rvert\le Cs^{c_\zeta}$ с $c_\zeta>1$, то $\epsilon\to0$, $s\epsilon_s=k_g\eta^*_s-\epsilon$, $\epsilon_\theta=(k_g'\eta+k_g\eta^*_\theta)/s$, и
$$\Delta(\sigma):=\sup_{0<s<\sigma}\Big(\lvert\epsilon\rvert+\lvert s\epsilon_s\rvert+\lvert\epsilon_\theta\rvert+\lvert\eta^*_s\rvert+\frac{\lvert\eta^*_\theta\rvert}s+s\lvert\eta^*_{ss}\rvert+\lvert\eta^*_{s\theta}\rvert+\frac{\lvert\eta^*_{\theta\theta}\rvert}s\Big)\xrightarrow[\sigma\to0]{}0 \tag{2.2}$$
(супремум по $\theta$ и $\zeta$ из указанной области).

**Нормальная форма в масштабе.** Пусть $j<\infty$. Положим (это $\tilde F$ леммы K2 [008] при $p=1$)
$$F(\varsigma,\theta,e):=\hat G(\varsigma^2,\theta)+e^2M\big(\varsigma^2,\theta,\varsigma^{j-m}e\big). \tag{2.3}$$
$F$ аналитична при малых $\lvert\varsigma\rvert$, $\theta\in\mathbb R$, $\lvert e\rvert\le1$ (нужно $\lvert\varsigma^{j-m}e\rvert<y_1/2$), и по (0.2)
($m-2+2c=j$, $s^{c-1}=\varsigma^{j-m}$ при $\varsigma=s^{1/2}$) при $0<s<s_1$, $\lvert s^{c-1}e\rvert<y_1/2$ (З6 R32)
$$U\big(\Psi(s,\theta,s^ce)\big)=s^jF(s^{1/2},\theta,e),\qquad F(0,\theta,e)=G(\theta)+\tfrac12h_n(\theta)e^2. \tag{2.4}$$

**Тождество Эйлера.** Пусть $Y=\Psi_s+\upsilon(s,\theta)\Psi_\theta$ (как поле в координатах $(s,\theta,\zeta)$:
$Y=\partial_s+\upsilon\partial_\theta$), $\rho=s$, $A(r)=a_0r^j$, $W=U+A(\rho)$. Для
$g(s,\theta,\zeta)=W(\Psi(s,\theta,\zeta))=s^j\big(F(s^{1/2},\theta,\zeta s^{-c})+a_0\big)$ имеем $s\,\partial_s(\zeta s^{-c})=-ce$ и
$$\beta W-\rho\,YW=s^j\Big[-s\upsilon\,\partial_\theta F+c\,e\,\partial_eF-\tfrac\varsigma2\partial_\varsigma F\Big]\qquad(\beta=j,\ \varsigma=s^{1/2},\ e=\zeta s^{-c}). \tag{2.5}$$
(Действительно, $\rho\,YW=s\partial_sg+s\upsilon\partial_\theta g=jW+s^j[\frac\varsigma2\partial_\varsigma F-ce\partial_eF+s\upsilon\partial_\theta F]$.) При
$\upsilon=0$ (теорема Mc) угловой член пропадает, при $\upsilon=-\kappa\theta/s$ (теорема Mb) он равен
$\kappa\theta\partial_\theta F$. [Эксперимент: `experiments/prover/morse-bott/euler_identity.py` — тождество (2.5) для
произвольных $F$, $\upsilon$: `True`; частные случаи проверены R26 и R28.]

### 3. Предложение R

1. *$\Sigma\ne\varnothing$.* Иначе $u_m\ge c\lvert q\rvert^m$, $c>0$, и $\lvert U-u_m\rvert\le C\lvert q\rvert^{m+1}$, так что $U>0$ в
   проколотой окрестности $0$ — строгий минимум.
2. *Компонента с отрицательными значениями и $j<\infty$.* По предложению K4(c) [008] (с трубками
   [008] и $y_1\le t_1$) $0$ — локальный минимум тогда и только тогда, когда $F_{\rm fl}\ge0$ при малых $s>0$
   на всех кривых-компонентах и $R_\omega(s)\ge0$ при малых $s>0$ во всех точечных компонентах.
   Компонент конечное число. Значит, есть точечная компонента и $s_k\downarrow0$ с $R_\omega(s_k)<0$ или
   кривая-компонента $\Sigma_0$ и $(s_k,\theta_k)$, $s_k\downarrow0$, с $s_k^mR(s_k,\theta_k)<0$. На этой компоненте
   $R\not\equiv0$, и по аналитичности $j<\infty$: если бы все $g_k\equiv0$, то при каждом $\theta$ аналитическая на
   $(-s_1,s_1)$ функция $R(\cdot,\theta)$ имела бы в $0$ все производные нулевыми и была бы $\equiv0$.
3. *Точечная компонента.* $R_\omega\not\equiv0$ аналитична и отрицательна в $s_k\downarrow0$, поэтому её старший
   коэффициент отрицателен — это (P).
4. *Кривая-компонента.* $s_k^j\hat G(s_k,\theta_k)<0$; после перехода к подпоследовательности
   $\theta_k\to\theta_*$ в $\mathbb R/L\mathbb Z$ и $G(\theta_*)\le0$. Если $\min G<0$ и $G\not\equiv\mathrm{const}$, то в точке
   $\theta_0$ глобального минимума аналитическая непостоянная $G-G(\theta_0)\ge0$ имеет нуль конечного чётного
   порядка с положительным старшим коэффициентом — (a/b). Если $G\equiv\mathrm{const}<0$ — (c). Если
   $\min G=0$, то $G(\theta_*)=0$ — (d) с $\theta_0=\theta_*$ (последовательность поднимается в $\mathbb R$ около $\theta_0$).
   $\min G>0$ противоречит $G(\theta_*)\le0$; $G\equiv0$ невозможно по определению $j$. $\square$

Изолированность в доказательстве не используется (замечание о ней — раздел «Где работают
аналитичность и изолированность»).

### 4. Лемма M

1. (D4) и оценки на $\overline\Omega\cap\{0<\rho<\sigma\}$: $K_\perp\le2\delta\rho^\beta$, $\lvert v_\perp\rvert\le2\sqrt\delta\rho^{\beta/2}$,
   $\sqrt{a_1/h_1}\rho^{\beta/2}\le\lambda\le\sqrt{2(a_3+\delta)/h_0}\rho^{\beta/2}$ — дословно пп. 1–2 доказательства леммы 2
   [007]; там используются только (L0), (L1) и $W\ge-\delta\rho^\beta$. По (1.1) [007]
   $\dot\rho=-\lambda+\langle\nabla\rho-Y/h,v_\perp\rangle$, и так как $v_\perp\perp Y$,
   $\lvert\langle\nabla\rho-Y/h,v_\perp\rangle\rvert\le(\vartheta_1+\gamma_1)2\sqrt\delta\rho^{\beta/2}\le\frac12\sqrt{a_1/h_1}\rho^{\beta/2}$. Это п. 1.
2. Точка множества из (A5): $V=\delta\rho^\beta$, $K:=K_\perp=\delta\rho^\beta-W\in[0,2\delta\rho^\beta]$, $\lvert v_\perp\rvert=\sqrt{2K}$,
   $\sqrt{a_1/h_1}\rho^{\beta/2}\le\lambda\le\sqrt{2a_3/h_0}\rho^{\beta/2}$ (п. 3 леммы 2 [007]). Главный член (1.3) [007]:
   $\beta\delta\rho^\beta-\rho YW=\beta K+(\beta W-\rho YW)\ge\beta K+\mu W-\varepsilon_1\delta\rho^\beta$.
3. $\lvert T_1\rvert\le\frac\rho\lambda(a_2+\beta\delta)\rho^{\beta-1}(\vartheta_1+\gamma_1)\sqrt{2K}\le(a_2+\beta\delta)\sqrt{h_1/a_1}\,\rho^{\beta/2}\big[2\vartheta_1\sqrt\delta\rho^{\beta/2}+\sqrt2\gamma_1\sqrt K\big]$;
   при $\delta\le a_1/2$ первое слагаемое $\le L_1\vartheta_1\sqrt\delta\rho^\beta$.
4. $\lvert T_2\rvert=\lambda\rho\lvert\langle v_\perp,\nabla_YY\rangle\rvert\le\sqrt{2a_3/h_0}\,\rho^{\beta/2}(\vartheta_2+\gamma_2)\sqrt{2K}\le L_2\vartheta_2\sqrt\delta\rho^\beta+\sqrt{2a_3/h_0}\,\sqrt2\gamma_2\sqrt K\rho^{\beta/2}$.
   Итак, $\lvert T_1\rvert+\lvert T_2\rvert\le(L_1\vartheta_1+L_2\vartheta_2)\sqrt\delta\rho^\beta+\Gamma\sqrt K\rho^{\beta/2}$.
5. $T_3\ge-\vartheta_3\lvert v_\perp\rvert^2=-2\vartheta_3K$.
6. По (1.3) [007]
   $\frac\rho\lambda\Xi\ge(\beta-2\vartheta_3)K+\mu W-\Gamma\sqrt K\rho^{\beta/2}-\big[\varepsilon_1+\frac{L_1\vartheta_1+L_2\vartheta_2}{\sqrt\delta}\big]\delta\rho^\beta$.
   Так как $b'K-\Gamma\sqrt K\rho^{\beta/2}+\frac{\Gamma^2}{4b'}\rho^\beta=\big(\sqrt{b'K}-\frac{\Gamma\rho^{\beta/2}}{2\sqrt{b'}}\big)^2\ge0$, то
   $(\beta-2\vartheta_3)K-\Gamma\sqrt K\rho^{\beta/2}\ge\mu K-\frac{\Gamma^2}{4b'}\rho^\beta$, и $\mu K+\mu W=\mu\delta\rho^\beta$ (знак $W$ не
   важен). Это (0.3). $\square$

### 5. Теорема Mb

**5.1. Формулы для $Y_\kappa$** (символьно для многочленов $k_g(\theta)$, $\eta^*(s,\theta)$ общего вида:
`experiments/prover/morse-bott/frames_mb.py`, R26 `sym_frames.py`, все `True` [Эксперимент]; первые
две — это (10.2), (10.4) [008] в координатах $\Psi$). Положим $\nu:=\eta^*_s-\kappa\theta\eta^*_\theta/s$. По (2.1)
$$Y_\kappa=\omega-\kappa\theta(1-\epsilon)\ell+\nu\,n,\qquad h=1+\kappa^2\theta^2(1-\epsilon)^2+\nu^2, \tag{5.1}$$
$$s\,D_{Y}Y=-\kappa^2\theta^2(1-\epsilon)\,\omega+\kappa\theta\big[s\epsilon_s-1+\kappa(1-\epsilon)-\kappa\theta\epsilon_\theta+\nu k_g\big]\ell+\big[s\nu_s+\kappa^2\theta^2(1-\epsilon)k_g-\kappa\theta\nu_\theta\big]n, \tag{5.2}$$
и для произвольного $w=w_\omega\omega+w_\ell\ell+w_nn$
$$
\begin{aligned}
s\langle w,D_wY_\kappa\rangle={}&\Big(\frac1{1-\epsilon}-\kappa\Big)w_\ell^2+\kappa\theta\,s\epsilon_s\,w_\omega w_\ell+s\nu_s\,w_\omega w_n+\kappa\theta\,w_\omega w_\ell\\
&+\frac{(\kappa\theta\epsilon_\theta-\nu k_g)\,w_\ell^2}{1-\epsilon}+\frac{\nu_\theta\,w_\ell w_n}{1-\epsilon}-\kappa\theta k_g\,w_\ell\Big(w_\omega\eta^*_s+\frac{w_\ell\eta^*_\theta}{s(1-\epsilon)}\Big).
\end{aligned} \tag{5.3}
$$
Вывод (5.3): $w=a^s\Psi_s+a^\theta\Psi_\theta+a^\zeta\Psi_\zeta$ с $a^s=w_\omega$, $a^\theta=w_\ell/(s(1-\epsilon))$,
$a^\zeta=w_n-w_\omega\eta^*_s-w_\ell\eta^*_\theta/(s(1-\epsilon))$ по (2.1); $D_wY=a^s\partial_sY+a^\theta\partial_\theta Y+a^\zeta\partial_\zeta Y$ с
производными (10.4) [008]; члены $\mp\kappa\theta k_gw_\ell w_n$ из $a^\theta\partial_\theta Y$ и $a^\zeta\partial_\zeta Y$ сокращаются.

**5.2. Доказательство.**

1. *Выбор $r_1$.* $r_1\in(0,\min(1,L/4))$ такое, что при $\lvert\theta\rvert\le r_1$: (r1) $\Lambda\ge\frac a2\theta^{2p}$ и
   $\theta\Lambda'\ge\Lambda$ (так как $\theta\Lambda'-\Lambda=(2p-1)a\theta^{2p}(1+O(\theta))$); (r2) $h_n(\theta)\ge\frac12h_n(0)$ и
   $\lvert\theta h_n'(\theta)\rvert\le h_n(\theta)$.
2. *Профиль и неравенство Эйлера.* По (2.4) $F_0(\theta,e):=F(0,\theta,e)=G(\theta)+\frac12h_n(\theta)e^2$,
   $Q:=F_0+a_0=\Lambda(\theta)+\frac12h_n(\theta)e^2\ge0$ при $\lvert\theta\rvert\le r_1$. Для $\kappa\in(0,\frac12]$, $\lvert\theta\rvert\le r_1$:
   $$\kappa\theta\partial_\theta Q+ce\,\partial_eQ=\kappa\theta\Lambda'+\tfrac\kappa2\theta h_n'e^2+ch_ne^2\ge\kappa\Lambda+\big(c-\tfrac\kappa2\big)h_ne^2\ge\kappa Q, \tag{5.4}$$
   так как $c-\frac\kappa2\ge\frac32-\frac14\ge\frac\kappa2$.
3. *Множество $\Omega_\delta$.* $\Omega_\delta:=\{(\theta,e):\ \lvert\theta\rvert<r_1,\ \lvert e\rvert<r_1,\ Q<4\delta\}$. На квадрате
   $Q\ge\frac a2\theta^{2p}+\frac{h_n(0)}4e^2$, поэтому $\Omega_\delta\subset\{\lvert\theta\rvert<R_\theta,\ \lvert e\rvert<R_e\}$, $R_\theta=(8\delta/a)^{1/(2p)}$,
   $R_e=4\sqrt{\delta/h_n(0)}$. Пусть $\delta_0\le a_0/2$ таково, что $R_\theta,R_e\le r_1/2$ при $\delta\le\delta_0$. Тогда
   $\overline{\Omega_\delta}$ лежит внутри квадрата, и на $\partial\Omega_\delta$ $Q=4\delta$ (граничная точка не в $\Omega_\delta$, но
   внутри квадрата, поэтому $Q\ge4\delta$; по непрерывности $Q\le4\delta$). $\Omega_\delta$ может быть несвязным;
   теорема A этого не запрещает.
4. *Данные теоремы A.* $\beta:=j$; уменьшим $s_2$ так, что $s_2^{c-1}<y_1/4$ и $\sqrt2s_2<r$ (шар $B_r$, где $U$
   аналитична); $\sigma_0:=s_2$, $A(r):=a_0r^j$ на $(0,\sigma_0)$;
   $\mathcal O:=\{\Psi(s,\theta,s^ce):\ 0<s<s_2,\ \lvert\theta\rvert<r_1,\ \lvert e\rvert<1\}\subset B_r\setminus0$ — открыто, $\Psi$ на нём
   инъективна ($2r_1<L$); $\rho:=s\circ\Psi^{-1}$, $Y:=Y_\kappa\circ\Psi^{-1}$ (аналитично), $Y\rho=1$. Функция $F$ аналитична в
   окрестности компакта $[0,\sigma_0^{1/2}]\times[-r_1,r_1]\times[-1,1]$, поэтому
   $$\chi(\sigma):=\sup\big\{\lvert F-F_0\rvert+\lvert\nabla_{\theta,e}(F-F_0)\rvert+\lvert\varsigma'\partial_\varsigma F\rvert:\ 0<\varsigma'\le\sigma,\ \lvert\theta\rvert\le r_1,\ \lvert e\rvert\le1\big\}\to0$$
   ($F$ и производные — в точке $(\varsigma',\theta,e)$). Выберем $\sigma_*\in(0,s_2)$ с $\chi(\sigma_*^{1/2})<\delta$ (дальше $\sigma_*$
   ещё уменьшится), $\chi:=\chi(\sigma_*^{1/2})$, и положим
   $$\mathcal D:=\{(s,\theta,e):\ 0<s<\sigma_*,\ (\theta,e)\in\Omega_\delta,\ F(s^{1/2},\theta,e)+a_0<\delta\},\qquad D:=\{\Psi(s,\theta,s^ce):\ (s,\theta,e)\in\mathcal D\}.$$
   При фиксированном $\sigma_*$ множество $D$ от $\kappa$ не зависит ($\sigma_*$ выбирается после $\kappa$, п. 7; З5 R33);
   число $\sigma$ теоремы A — это $\sigma_*$.
   - (D1): $\rho<\sigma_*$ на $D$. Если $q=\lim\Psi(s_k,\theta_k,s_k^ce_k)$, $(s_k,\theta_k,e_k)\in\mathcal D$, то по
     подпоследовательности $s_k\to\bar s\in[0,\sigma_*]$, $(\theta_k,e_k)\to(\bar\theta,\bar e)\in\overline{\Omega_\delta}$; при $\bar s>0$
     $q=\Psi(\bar s,\bar\theta,\bar s^c\bar e)\in\mathcal O$, при $\bar s=0$ $\lvert q\rvert=\lim\sqrt{s_k^2+\eta_k^2}=0$. Далее
     $\lvert\Psi\rvert^2=s^2+\eta^2\le2s^2$ и $\rho\le\lvert q\rvert$.
   - (D2): если $q\in\partial D\setminus0$, $\rho(q)<\sigma_*$, то $q=\Psi(\bar s,\bar\theta,\bar s^c\bar e)$ с $(\bar s,\bar\theta,\bar e)$ в замыкании
     $\mathcal D$, но не в $\mathcal D$; поэтому $\bar s<\sigma_*$, $(\bar\theta,\bar e)\in\overline{\Omega_\delta}$, $F+a_0\le\delta$, и либо
     $(\bar\theta,\bar e)\in\partial\Omega_\delta$ — тогда $F+a_0\ge Q-\chi=4\delta-\chi>3\delta$, противоречие, — либо $F+a_0=\delta$, то
     есть $W(q)=\delta\rho^j$.
   - (D3): точки $(s,0,0)\in\mathcal D$ ($Q=0$, $F+a_0\le\chi<\delta$), и там $W<\delta\rho^j$.
5. *(L0), (L1), (L2).* $a_1=a_3=a_0$, $a_2=ja_0$, $\delta\le a_0/2$. По (5.1) $h\in[1,\frac32]$, если
   $\lvert\epsilon\rvert,\lvert\nu\rvert\le\frac14$ (малое $s_2$; $\lvert\nu\rvert\le\lvert\eta^*_s\rvert+\lvert\eta^*_\theta\rvert/s$ равномерно по $\kappa$): $h_0=1$,
   $h_1=\frac32$. На $D_\sigma$ $(\theta,e)\in\overline{\Omega_\delta}$, $Q\ge0$, поэтому $W=s^j((F-F_0)+Q)\ge-\chi s^j\ge-\delta\rho^j$. По
   (2.5) с $\upsilon=-\kappa\theta/s$ и (5.4)
   $$\beta W-\rho YW=s^j\big[\kappa\theta\partial_\theta F+ce\partial_eF-\tfrac\varsigma2\partial_\varsigma F\big]\ge s^j\big[\kappa Q-(\kappa r_1+c+\tfrac12)\chi\big],$$
   и $\kappa W\le\kappa s^j(Q+\chi)$. Значит, (L2) выполнено с $\mu:=\kappa<\beta$, $\varepsilon_1:=(c+2)\chi/\delta$.
6. *(L3M).* Пусть $q\in D_\sigma$ (там $\lvert\theta\rvert\le R_\theta$), $w\perp Y$. Из $\langle Y,w\rangle=0$ и (5.1):
   $w_\omega=\kappa\theta(1-\epsilon)w_\ell-\nu w_n$.
   - $\lvert\langle\nabla\rho-Y/h,w\rangle\rvert=\lvert w_\omega\rvert\le(\frac54\kappa R_\theta+\lvert\nu\rvert)\lvert w\rvert$: $\gamma_1:=\frac54\kappa R_\theta$, $\vartheta_1:=\sup\lvert\nu\rvert$.
   - По (5.2): главный перекрёстный член $-\kappa(1-\kappa)\theta w_\ell$; квадратичные (коэффициенты при $\omega$ и
     $n$) не больше $\frac54\kappa^2\theta^2(1+\bar k_g)\lvert w\rvert$; остальные, при $\kappa\lvert\theta\rvert\le1$, не больше
     $(\lvert\epsilon\rvert+\lvert s\epsilon_s\rvert+\lvert\epsilon_\theta\rvert+\lvert\nu\rvert\bar k_g+\lvert s\nu_s\rvert+\lvert\nu_\theta\rvert)\lvert w\rvert$. Итак,
     $\gamma_2:=\kappa R_\theta+\frac54\kappa^2R_\theta^2(1+\bar k_g)$, а $\vartheta_2$ — супремум последней скобки.
   - По (5.3): первый член $\ge(\frac45-\frac12)w_\ell^2\ge0$; четвёртый равен
     $\kappa^2\theta^2(1-\epsilon)w_\ell^2-\kappa\theta\nu w_\ell w_n$, его первая часть $\ge0$; остальные — малые величины, умноженные
     на $\lvert w\rvert^2$. Значит, годится
     $\vartheta_3:=\sup\big(\lvert s\epsilon_s\rvert+\lvert s\nu_s\rvert+\lvert\nu\rvert+2(\lvert\epsilon_\theta\rvert+\lvert\nu\rvert\bar k_g+\lvert\nu_\theta\rvert)+\bar k_g(\lvert\eta^*_s\rvert+2\lvert\eta^*_\theta\rvert/s)\big)$.

   $\vartheta_1,\vartheta_2,\vartheta_3\to0$ при $\sigma_*\to0$ **равномерно по $\kappa\in(0,\frac12]$**: $\lvert\nu\rvert\le\lvert\eta^*_s\rvert+\lvert\eta^*_\theta\rvert/s$,
   $s\nu_s=s\eta^*_{ss}-\kappa\theta(\eta^*_{s\theta}-\eta^*_\theta/s)$, $\nu_\theta=\eta^*_{s\theta}-\kappa\eta^*_\theta/s-\kappa\theta\eta^*_{\theta\theta}/s$ — всё через $\Delta$
   из (2.2).
7. *Выбор констант.* Пусть $\delta_1\le\delta_0$ таково, что при $\delta\le\delta_1$: $\frac54R_\theta(1+\bar k_g)\le1$ и
   $5R_\theta\sqrt\delta\le\frac14\sqrt{2a_0/3}$. Для $\delta\in(0,\delta_1]$ возьмём $\kappa=\kappa(\delta)$ из (0.4); это то же, что
   $\kappa=\min\{\frac12,\ j\delta/(2C_\Gamma^2a_0R_\theta^2)\}$. Тогда $\gamma_2\le\frac32\kappa R_\theta\le2\kappa R_\theta$, и при $\delta\le a_0/2$
   $$\Gamma\le\sqrt2\Big[\tfrac32ja_0\sqrt{\tfrac3{2a_0}}\cdot\tfrac54\kappa R_\theta+\sqrt{2a_0}\cdot2\kappa R_\theta\Big]=C_\Gamma\sqrt{a_0}\,\kappa R_\theta .$$
   Выберем $\sigma_*$ так, что $\vartheta_3\le\frac14$, $\varepsilon_1+(L_1\vartheta_1+L_2\vartheta_2)/\sqrt\delta\le\kappa/4$ и
   $4\sqrt\delta\vartheta_1\le\frac14\sqrt{2a_0/3}$. Тогда $b'=j-\kappa-2\vartheta_3\ge j-1\ge\frac j2$,
   $\frac{\Gamma^2}{4b'\delta}\le\frac{C_\Gamma^2a_0\kappa^2R_\theta^2}{2j\delta}\le\frac\kappa4$, и скобка в (0.3) не меньше $\frac\kappa2>0$. Условие п. 1 леммы M:
   $4\sqrt\delta(\vartheta_1+\gamma_1)\le\frac14\sqrt{2a_0/3}+5\sqrt\delta\kappa R_\theta\le\frac12\sqrt{a_0/h_1}$.
8. *Вывод.* Лемма M даёт (D4), (A4), (A5); теорема A [007] — решение в $\overline\Omega$, $q\ne0$, $q,v\to0$; по
   шагу 5 теоремы A $\rho(q(t))\le\sigma_2<\sigma_*$, так что $q(t)\in D_\sigma$ и $(\theta,e)\in\overline{\Omega_\delta}$. Оценки $\dot s$ — п. 1
   леммы M. $\square$

Порядок констант: $r_1$ (по $G,h_n$) $\to\delta_0,\delta_1\to\delta\to\kappa(\delta)\to\sigma_*$; $s_2$ выбирается до всего этого и
равномерно по $\kappa\le\frac12$. От $\kappa$ зависят только $Y$, $\Omega$ теоремы A и $\sigma_*$.

### 6. Теорема Mc

1. *Данные.* $\beta:=j$; $s_2$ — как в §5.2, п. 4 ($s_2^{c-1}<y_1/4$, $\sqrt2s_2<r$); $\sigma_0:=s_2$;
   $\mathcal O:=\{\Psi(s,\theta,s^ce):\ 0<s<s_2,\ \theta\in\mathbb R/L\mathbb Z,\ \lvert e\rvert<1\}\subset B_r\setminus0$ — открыто (лемма N);
   $\rho:=s\circ\Psi^{-1}$, $Y:=\Psi_s\circ\Psi^{-1}$, $Y\rho=1$, $A(r):=a_0r^j$.
2. *Тождество Эйлера.* По (2.5) с $\upsilon=0$: $\beta W-\rho YW=s^j[ce\partial_eF-\frac\varsigma2\partial_\varsigma F]$.
3. *Область.* $F_0=-a_0+\frac12h_n(\theta)e^2$, $Q:=F_0+a_0=\frac12h_n(\theta)e^2$. Пусть $0<\delta\le\min(a_0/2,h_*/32)$,
   $\Omega_\delta:=\{(\theta,e):\ Q<4\delta\}$; на нём $\lvert e\rvert<R_e:=2\sqrt{2\delta/h_*}\le\frac12$. Положим
   $\chi(\sigma):=\sup\{\lvert F-F_0\rvert+\lvert\partial_eF-\partial_eF_0\rvert+\lvert\varsigma'\partial_\varsigma F\rvert:\ 0<\varsigma'\le\sigma,\ \theta\in\mathbb R,\ \lvert e\rvert\le1\}\to0$
   (аналитичность, периодичность, компактность $\mathbb R/L\mathbb Z$). Выберем $\sigma_*\in(0,s_2)$ с $\chi:=\chi(\sigma_*^{1/2})<\delta$ и
   положим $\mathcal D:=\{0<s<\sigma_*,\ (\theta,e)\in\Omega_\delta,\ F(s^{1/2},\theta,e)+a_0<\delta\}$, $D:=\{\Psi(s,\theta,s^ce)\}$; $\sigma$ теоремы
   A — это $\sigma_*$.
4. *(D1)–(D3)* — как в §5.2, п. 4: в (D1) предельный угол берётся по компактности окружности,
   $\lvert\bar e\rvert\le R_e<1$; в (D2) угловой границы нет ($\theta$ периодична), и на $\partial\Omega_\delta$ $Q=4\delta$; в (D3) —
   точки $(s,\theta,0)$.
5. *(L0)–(L2) леммы 2 [007].* $a_1=a_3=a_0$, $a_2=ja_0$; $h=1+\eta^{*2}_s\in[1,\frac32]$. На $D_\sigma$: $Q\ge0$,
   $W\ge-\chi s^j\ge-\delta\rho^j$; так как $ce\partial_eQ=2cQ$,
   $\beta W-\rho YW\ge s^j[2cQ-cR_e\chi-\frac\chi2]\ge2cW-s^j(cR_e+\frac12+2c)\chi$. Значит, (L2) выполнено с
   $\mu:=2c=j-m+2\in(0,\beta]$ и $\varepsilon_1:=(cR_e+\frac12+2c)\chi/\delta$.
6. *(L3) [007].* Для $w\perp Y$: $w_\omega+\eta^*_sw_n=0$, и $\nabla\rho-Y/h\perp Y$, поэтому
   $\lvert\nabla\rho-Y/h\rvert=\sup_{w\perp Y,\lvert w\rvert=1}\lvert w_\omega\rvert\le\lvert\eta^*_s\rvert=:\vartheta_1$. Далее $\nabla_YY=\partial_s(Y\circ\Psi)=\eta^*_{ss}n$:
   $\vartheta_2:=\sup s\lvert\eta^*_{ss}\rvert$. Наконец, $Y\circ\Psi=\omega+\eta^*_sn$ не зависит от $\zeta$,
   $\partial_\theta(Y\circ\Psi)=(1-k_g\eta^*_s)\ell+\eta^*_{s\theta}n$, и с $a^s=w_\omega$, $a^\theta=w_\ell/(s(1-\epsilon))$
   $$s\langle w,D_wY\rangle=\frac{(1-\eta^*_sk_g)w_\ell^2}{1-\epsilon}+s\eta^*_{ss}w_\omega w_n+\frac{\eta^*_{s\theta}w_\ell w_n}{1-\epsilon}\ge-\big(s\lvert\eta^*_{ss}\rvert+2\lvert\eta^*_{s\theta}\rvert\big)\lvert w\rvert^2$$
   при $\lvert\epsilon\rvert\le\frac14$, $\lvert\eta^*_sk_g\rvert\le1$ (это (5.3) при $\kappa=0$): $\vartheta_3:=\sup(s\lvert\eta^*_{ss}\rvert+2\lvert\eta^*_{s\theta}\rvert)$. Все
   $\vartheta_i\le2\Delta(\sigma_*)\to0$.
7. *Вывод.* При фиксированном $\delta$ величины $\varepsilon_1$, $(L_1\vartheta_1+L_2\vartheta_2)/\sqrt\delta$, $4\vartheta_3$ стремятся к $0$ при
   $\sigma_*\to0$; выберем $\sigma_*$ так, что их сумма $\le\mu/2$, $4\vartheta_1\sqrt\delta\le\sqrt{2a_0/3}$ и
   $\Delta(\sigma_*)\le\min\big(\frac14,(1+\bar k_g)^{-1}\big)$ (тогда на $D_\sigma$, где $s<\sigma_*$, выполнены $h\le\frac32$ из п. 5 и
   $\lvert\epsilon\rvert\le\frac14$, $\lvert k_g\eta^*_s\rvert\le1$ из п. 6; З1 R32). Лемма 2 [007] даёт
   (D4), (A4), (A5) (скобка (3.1) [007] $\ge\mu/2$), теорема A [007] — траекторию; оценки $\dot s$ — п. 1
   леммы 2, оценка $e$ — из $(\theta,e)\in\overline{\Omega_\delta}$. $\square$

Почему здесь не нужен угловой запас: в (2.5) при $\upsilon=0$ нет члена $\partial_\theta F$, а угловые поправки
$\hat G(s,\theta)+a_0=sg_{j+1}(\theta)+\dots$ входят только через $\lvert F-F_0\rvert\le\chi$ и $\lvert\varsigma\partial_\varsigma F\rvert\le\chi$. При
непостоянной $G$ член $\beta s^j(G-\min G)$ в $\beta W$ не компенсировался бы, поэтому для неё нужны угловые
стенки (теоремы Mb, Md).

### 7. Лемма V

1. *Полярная кривая.* $\partial_\tau f(0,\tau)=g'(\tau)$ имеет в $0$ нуль порядка ровно $2q-1$. [Литература:
   подготовительная теорема Вейерштрасса; напр. Krantz–Parks, *A Primer of Real Analytic Functions*,
   2002, §6.1; Brieskorn–Knörrer, *Plane Algebraic Curves*, 1986, §8.2; не сверено.] Формулировка: если $F$
   голоморфна около $0\in\mathbb C^2$ и $F(0,\tau)=\tau^d\cdot$(единица), то в некотором полидиске $F=uP$, где $u$ —
   единица, $P=\tau^d+\sum_{i<d}p_i(s)\tau^i$, $p_i$ голоморфны, $p_i(0)=0$, и такое разложение единственно. Для
   $F=\partial_\tau f$ с вещественными коэффициентами единственность даёт вещественность $u$, $p_i$ (сопряжение
   переводит разложение в разложение). [Литература: теорема Ньютона–Пюизё; Brieskorn–Knörrer, §8.3;
   C.T.C. Wall, *Singular Points of Plane Curves*, 2004, Thm 2.1.1; не сверено.] Формулировка: для такого $P$
   есть $N_1\in\mathbb N$ (годится $N_1=d!$) и голоморфные около $0$ функции $T_1,\dots,T_d$, $T_i(0)=0$, с
   $P(t^{N_1},\tau)=\prod_i(\tau-T_i(t))$ при малых $\lvert t\rvert$. Здесь $d=2q-1$.
2. *Вещественные корни.* $I_{\mathbb R}$ — те $i$, у которых все коэффициенты Тейлора $T_i$ вещественны. При
   $i\notin I_{\mathbb R}$ $\operatorname{Im}T_i(t)$ на вещественных $t$ — ненулевой сходящийся ряд, поэтому $\ne0$ при $0<t<t_3$.
   Значит, при $0<s<t_3^{N_1}$ вещественные корни $P(s,\cdot)$ — это ровно $T_i(s^{1/N_1})$, $i\in I_{\mathbb R}$.
3. *Окно.* $g>0$ на $[-\tau_1,\tau_1]\setminus0$. Выберем $\tau_0\le\tau_1$ и $s_4\in(0,t_3^{N_1}]$ так, что разложение $\partial_\tau f=uP$
   верно и $u\ne0$ на $[0,s_4]\times[-\tau_0,\tau_0]$, $f(s,\pm\tau_0)\ge\frac12\min\{g(\tau_0),g(-\tau_0)\}>0$ и $\lvert T_i(s^{1/N_1})\rvert<\tau_0$ при
   $s\in[0,s_4]$. Тогда при $s\in(0,s_4)$ минимум $m(s)$ функции $f(s,\cdot)$ на $[-\tau_0,\tau_0]$ достигается в $\pm\tau_0$ или
   в одной из точек $T_i(s^{1/N_1})$, $i\in I_{\mathbb R}$.
4. *Выбор ветви.* Множество $I_{\mathbb R}$ непусто: при $s>0$ $P(s,\cdot)$ — вещественный многочлен нечётной степени
   $2q-1$, у него есть вещественный корень (З3 R33). $v_i(t):=f(t^{N_1},T_i(t))$, $i\in I_{\mathbb R}$, вещественно-аналитичны около $0$, $v_i(0)=0$. Разность двух
   из них либо $\equiv0$, либо знакопостоянна на $(0,t_5)$; поэтому есть $i_*$ с $v_{i_*}\le v_i$ на $(0,t_5)$ при всех
   $i\in I_{\mathbb R}$ (ничьи допустимы — берётся любая). При больших $k$ $m(s_k)\le f(s_k,\tau_k)<0$, значит,
   $m(s_k)=v_{i_*}(s_k^{1/N_1})<0$. Поэтому $v_{i_*}\not\equiv0$ и $v_{i_*}(t)=-a_Vt^{\Gamma_1}(1+O(t))$, $a_V>0$, $\Gamma_1\ge1$. При малых
   $t>0$ $v_{i_*}(t)<0<f(s,\pm\tau_0)$, так что $m(s)=v_{i_*}(s^{1/N_1})$ достигается в $T_{i_*}(s^{1/N_1})$.
5. *Многоугольник Ньютона.* $\tilde f(t,\tau'):=f(t^{N_1},T_{i_*}(t)+\tau')$ аналитична около $(0,0)$, $\tilde f(t,0)=v_{i_*}(t)$,
   $\partial_{\tau'}\tilde f(t,0)=0$ ($T_{i_*}(t)$ — корень $P(t^{N_1},\cdot)$, $u\ne0$), и $\tilde f=\tilde f(t,0)+\sum_{k\ge2}a_k(t)\tau'^k$, где
   $a_k(0)=g^{(k)}(0)/k!$: $a_k(0)=0$ при $k<2q$, $a_{2q}(0)=g_{2q}>0$. Пусть $\nu_k=\operatorname{ord}_ta_k$: $\nu_{2q}=0$, $\nu_k\ge1$ при
   $2\le k<2q$. $E(A'):=\min_{2\le k\le2q}(\nu_k+kA')$ непрерывна, строго возрастает, $E(0)=0<\Gamma_1$, $E(\infty)=\infty$:
   есть единственное $A'_*>0$ с $E(A'_*)=\Gamma_1$, рациональное со знаменателем $\le2q$. При $k>2q$
   $\nu_k+kA'_*>2qA'_*\ge E(A'_*)$. Итак, $\nu_k+kA'_*\ge\Gamma_1$ при всех $k\ge2$, с равенством ровно при $k\in K_*\ne\varnothing$,
   $K_*\subset\{2,\dots,2q\}$.
6. *Целые показатели.* $\ell_*:=2\cdot(2q)!$, $N:=\ell_*N_1$, $T(t):=T_{i_*}(t^{\ell_*})$, $\Gamma_V:=\ell_*\Gamma_1$, $A_V:=\ell_*A'_*\in\mathbb N$. Замена
   $t\mapsto t^{\ell_*}$ умножает $\nu_k,\Gamma_1,A'_*$ на $\ell_*$; $N$ и $\Gamma_V$ чётны. Это даёт п. 1.
7. *Функция $\hat\Phi$.* $f(t^N,T(t)+\tau')=\sum f_{ik}t^i\tau'^k$ абсолютно сходится при $\lvert t\rvert<t_6$, $\lvert\tau'\rvert<\tau_6$;
   $f_{ik}\ne0$ только если $k=0$, $i\ge\Gamma_V$ или $k\ge2$, $i\ge\ell_*\nu_k$, и в обоих случаях $i+kA_V\ge\Gamma_V$. Поэтому
   $t^{-\Gamma_V}f(t^N,T(t)+t^{A_V}b)=\sum f_{ik}t^{i+kA_V-\Gamma_V}b^k$ — степенной ряд с неотрицательными показателями,
   абсолютно сходящийся при $\lvert t\rvert<t_2$, $\lvert b\rvert<B$, если $t_2<t_6$, $t_2^{A_V}B<\tau_6$. Его сумма $\hat\Phi$ аналитична,
   $\hat\Phi(0,b)=f_{\Gamma_V,0}+\sum_{k\in K_*}f_{\ell_*\nu_k,k}b^k=-a_V+Q_V(b)$, $c_k:=f_{\ell_*\nu_k,k}\ne0$ — старший коэффициент $a_k$.
8. *$Q_V\ge0$.* При малом $t>0$, $\lvert b\rvert\le B$ точка $T(t)+t^{A_V}b\in[-\tau_0,\tau_0]$, и по п. 1
   $\hat\Phi(t,b)\ge\hat\Phi(t,0)$; при $t\to0$ $Q_V(b)\ge Q_V(0)=0$, а $B$ любое. Ненулевой многочлен $Q_V\ge0$ без членов
   степеней $0$, $1$ имеет чётную младшую степень с положительным коэффициентом. $\square$

### 8. Теорема Md

*Условия леммы V* для $f(s,\tau)=\hat G(s,\theta_0+\tau)$: аналитичность — (N2); $f(0,\cdot)=G(\theta_0+\cdot)\ge0$; $G\not\equiv0$
около $\theta_0$, так как $G=g_j\not\equiv0$ на $\Sigma_0$ (определение $j$) и аналитична на связной $\Sigma_0$.

Обозначим $\hat\theta(x,u):=\theta_0+\tau_v(x)+u/x$; на $\mathcal N=\{0<x<s_0,\ \lvert b\rvert<r_0\}$ имеем $u/x=x^\alpha b_1$. Положим
$\tilde\kappa:=x\partial_x\hat\theta=x\tau_v'(x)-x^\alpha b_1$. Так как $\tau_v(x)=T(x^{1/N})$, $T(0)=0$:
$x\tau_v'=\frac1Nx^{1/N}T'(x^{1/N})=O(x^{1/N})$, $x^2\tau_v''=O(x^{1/N})$. Поэтому равномерно на $\mathcal N$ (при любом
фиксированном $r_0$)
$$\tilde\kappa\to0,\qquad x^2\partial_x^2\hat\theta=x^2\tau_v''+2x^\alpha b_1\to0,\qquad\hat\theta-\theta_0\to0,\qquad\lvert\zeta\rvert\le r_0x^{c'}. \tag{8.1}$$

1. *$(\Phi0)$.* $\mathcal L(x,u,\zeta):=(x,\hat\theta(x,u),\zeta)$ — гладкий диффеоморфизм $(0,s_0)\times\mathbb R^2$ на себя с обратным
   $(s,\theta,\zeta)\mapsto(s,\ s(\theta-\theta_0-\tau_v(s)),\ \zeta)$. При малом $s_0$ $\mathcal L(\mathcal N)$ лежит в области §2 с
   $\lvert\hat\theta-\theta_0\rvert<L/4$, где $\Psi$ инъективна. Значит, $\Phi=\Psi\circ\mathcal L$ — $C^\infty$-диффеоморфизм $\mathcal N$ на
   открытое множество, и $x\le\lvert\Phi\rvert=\sqrt{x^2+\eta^2}\le2x$: $c_0=1$, $\omega_0(x)=2x$.
2. *Производные* (символьно для $k_g(\theta)$, $\eta^*(s,\theta)$, $\tau_v(x)$ общего вида: `frames_mb.py`, R27
   `frames_md.py`, все `True` [Эксперимент]; вывод — дифференцирование $\Psi(x,\hat\theta,\zeta)$ по (2.1), (0.1)):
   $$\Phi_x=\omega+\tilde\kappa(1-\epsilon)\ell+\Big(\eta^*_s+\frac{\tilde\kappa\eta^*_\theta}x\Big)n,\qquad\Phi_u=(1-\epsilon)\ell+\frac{\eta^*_\theta}xn,\qquad\Phi_\zeta=n, \tag{8.2}$$
   $$x\Phi_{xx}=x\eta^*_{ss}n+2\tilde\kappa\Psi_{s\theta}+\frac{\tilde\kappa^2}x\Psi_{\theta\theta}+x\hat\theta_{xx}\Psi_\theta,\quad
   x\partial_u\Phi_x=(\epsilon-k_g\eta^*_s)\ell+\Big(\eta^*_{s\theta}-\frac{\eta^*_\theta}x\Big)n+\frac{\tilde\kappa}x\Psi_{\theta\theta},\quad
   x\partial_\zeta\Phi_x=-\tilde\kappa k_g\ell, \tag{8.3}$$
   где в точке $(x,\hat\theta,\zeta)$: $\Psi_{s\theta}=(1-k_g\eta^*_s)\ell+\eta^*_{s\theta}n$,
   $\Psi_{\theta\theta}=-(k_g'\eta+2k_g\eta^*_\theta)\ell+(s-k_g\eta)(-\omega+k_gn)+\eta^*_{\theta\theta}n$; отсюда $\lvert\Psi_{\theta\theta}\rvert\le C_\Psi x$,
   $\lvert\Psi_\theta\rvert\le2x$.
3. *$(\Phi1)$.* В репере $(\omega,\ell,n)$ матрица $J=(\Phi_x,\Phi_u,\Phi_\zeta)$ равна $I+E$, элементы $E$ по модулю не больше
   $\nu_1(x):=\sup(\lvert\tilde\kappa\rvert(1+\lvert\epsilon\rvert)+\lvert\eta^*_s\rvert+\lvert\tilde\kappa\eta^*_\theta\rvert/x+\lvert\epsilon\rvert+\lvert\eta^*_\theta\rvert/x)\to0$ по (8.1), (2.2) (здесь
   $c_\zeta=c'>1$), супремум — по точкам $\mathcal N$ с абсциссой $\le x$, так что $\nu_1$ — функция $x$ (З6 R33). $B=J^{\mathsf T}J=I+E+E^{\mathsf T}+E^{\mathsf T}E$, $\lVert E\rVert\le3\nu_1$, так что $\lVert B-I\rVert\le6\nu_1+9\nu_1^2\le\frac12$ при малом
   $s_0$, и $\lvert B_{xu}\rvert\le\lVert B-I\rVert\to0$.
4. *$(\Phi2)$ с $C_1=0$.* $x\lvert\Phi_{xx}\rvert\le x\lvert\eta^*_{ss}\rvert+2\lvert\tilde\kappa\rvert(1+\lvert\eta^*_{s\theta}\rvert+\bar k_g\lvert\eta^*_s\rvert)+C_\Psi\tilde\kappa^2+2\lvert x^2\hat\theta_{xx}\rvert\to0$.
5. *$(\Phi3)$ с $C_1=0$.* По (8.3) $x\lvert\partial_j\Phi_x\rvert\to0$ равномерно для $j\in\{x,u,\zeta\}$. Для $w=D\Phi\,\xi$ из $B\ge\frac12I$
   $\lvert\xi\rvert\le\sqrt2\lvert w\rvert$ и $x\lvert D_wY\rvert\le\sqrt6\max_jx\lvert\partial_j\Phi_x\rvert\,\lvert w\rvert$, так что
   $x\langle w,D_wY\rangle\ge-\omega(x)\lvert w\rvert^2$, $\omega(x)\to0$. Одно $\omega(x)$ — сумма оценок пп. 3–5.
6. *(F).* По (0.2) с $s=x=t^N$, $\theta=\hat\theta=\theta_0+T(t)+t^{A_V}b_1$, $\zeta=x^{c'}e$:
   $$U\circ\Phi=x^j\hat G(x,\hat\theta)+x^{m-2+2c'}e^2M(x,\hat\theta,x^{c'-1}e)=x^\beta\Big[\hat\Phi(t,b_1)+e^2M\big(t^N,\theta_0+T(t)+t^{A_V}b_1,\ t^{N(c'-1)}e\big)\Big]=:x^\beta F_d(t,b), \tag{8.4}$$
   так как $x^j\hat G(x,\hat\theta)=x^jf(t^N,T(t)+t^{A_V}b_1)=x^jt^{\Gamma_V}\hat\Phi$ и $m-2+2c'=\beta$; $N(c'-1)=\frac{N(j-m)+\Gamma_V}2\in\mathbb N$
   ($N$, $\Gamma_V$ чётны). $F_d$ аналитична около $\{0\}\times\overline{B_{r_0}}$ (лемма V, п. 2 с $B>r_0$; аналитичность $M$), а
   значит, на $(-\epsilon_F,\epsilon_F)\times B_{r_0+\epsilon_F}$. Выбор $s_0$: $s_0\le1$, $s_0<s_2$, $2s_0<r$ (чтобы $\Phi(\mathcal N)\subset B_r\setminus0$ в $(\Phi0)$, З2 R33), $r_0s_0^{c'-1}<y_1/4$,
   $s_0^{1/N}<\min(\epsilon_F,t_2(B))$ и малость из пп. 1, 3–5; тогда (0.2) и (8.4) верны на всём $\mathcal N$. Поэтому $F_d$,
   $\nabla_bF_d$ непрерывны вплоть до $t=0$ и $\sup_K\lvert t\partial_tF_d\rvert=O(t)$; переменная $s$ теоремы 2 [007] — это
   $t=x^{1/N}$. Предельный профиль:
   $$F_{d,0}(b_1,e)=-a_V+Q_V(b_1)+\tfrac12h_n(\theta_0)e^2,\qquad Q(b):=F_{d,0}(b)-F_{d,0}(0)=Q_V(b_1)+\tfrac12h_n(\theta_0)e^2. \tag{8.5}$$
7. *$(V_0)$.* $F_{d,0}(0)=-a_V<0$. Выберем $r_2>0$ так, что при $\lvert b_1\rvert\le r_2$ $Q_V(b_1)\ge\frac{c_{k_0}}2b_1^{k_0}$ и
   $b_1Q_V'(b_1)\ge\frac{k_0}2Q_V(b_1)\ge Q_V(b_1)$ (так как $Q_V=c_{k_0}b_1^{k_0}(1+O(b_1))$, $b_1Q_V'=k_0c_{k_0}b_1^{k_0}(1+O(b_1))$);
   $r_0:=r_2$. При $0<\delta\le\delta_2$ из $Q(b)<\delta$, $b\in B_{r_0}$ следуют $\lvert b_1\rvert<(2\delta/c_{k_0})^{1/k_0}$,
   $\lvert e\rvert<\sqrt{2\delta/h_n(\theta_0)}$, так что при малом $\delta_2$ $\{Q<\delta\}\cap B_{r_0}\subset B_{r_0/2}$, и компонента
   $\Omega_b\ni0$ имеет $\overline{\Omega_b}\subset B_{r_0}$; $Q\ge0$ всюду. На $\overline{\Omega_b}$
   $$c_1b_1\partial_{b_1}Q+c'e\,\partial_eQ=(1+\alpha)b_1Q_V'+c'h_n(\theta_0)e^2\ge Q_V+\tfrac12h_n(\theta_0)e^2=Q$$
   ($b_1Q_V'\ge0$, $c'>1$). Итак, $(V_0)$ выполнено с $\delta\in(0,\min(a_V/2,\delta_2)]$, $\mu=1\le\beta$. При $k_0=2$
   $Q\ge\min(c_{k_0}/2,h_n(\theta_0)/2)\lvert b\rvert^2$ на $B_{r_0}$ и неравенство Эйлера верно на всём $B_{r_0}$: $(V_1)$ с
   радиусом $r_1=r_0/2$ из $(V_1)$ [007] (это не окно $r_1$ теоремы Mb).
8. *Вывод.* Выполнены $(\Phi0)$–$(\Phi3)$ с $C_1=0$, (F), $(V_0)$; теорема 2 [007] даёт траекторию с $b(t)$ в
   компакте $\overline{\Omega'_b}\subset B_{r_0}$. Касание: $q=x\omega(\hat\theta)+\eta n(\hat\theta)$, $\hat\theta-\theta_0=\tau_v(x)+x^\alpha b_1\to0$,
   $\lvert\eta\rvert\le\lvert\eta^*\rvert+r_0x^{c'}=o(x)$, поэтому $q/\lvert q\rvert\to\omega(\theta_0)$. $\square$

### 9. Теорема M

По предложению R $\Sigma\ne\varnothing$ и реализуется один из случаев.

- (P): теорема K0 [008] с $\omega^*=\omega$: $u_m(\omega)=0$, $\nabla u_m(\omega)=0$ ($u_m\ge0$),
  $D^2u_m(\omega)|_{\omega^\perp}\succ0$ — это (K2) ($N_\omega=\omega^\perp$), $j<\infty$, $g_j(\omega)<0$.
- (a/b): теорема Mb в точке $\theta_0$ глобального минимума $G$ (условия Mb локальны, окно $\lvert\theta\rvert<r_1<L/4$).
- (c): теорема Mc.
- (d): теорема Md (здесь $G\ge0$ всюду).

Асимптотическая траектория даёт неустойчивость по Ляпунову: теорема A [007], шаг 6 (обратимость).
$\square$

## Где работают аналитичность и изолированность

1. **Изолированность не используется** (отзыв R28, З1). Единственное место первой редакции, где
   она была, — вывод «$j<\infty$ на всех компонентах»: при $R\equiv0$ поверхность дна состоит из
   критических точек ([008], §3.5, K4(b)). Но в доказательстве участвует одна компонента — та, в
   трубке которой $U<0$, — и на ней $R\not\equiv0$ следует из самих отрицательных значений
   (предложение R, п. 2). Теоремы K0, Mb, Mc, Md изолированности не требуют (R26 и R27 отметили это
   для Mb и Md). Поэтому теорема M верна и для неизолированных неминимальных критических точек
   класса. Пример (R28): $U=z^2-x^4$ ($m=2$, $\Sigma$ — окружность $z=0$, $G=-\cos^4\theta$, случай (a)) —
   ось $y$ состоит из критических точек, а асимптотическая траектория $x(t)=1/(\sqrt2t+C)$ по оси $x$
   есть.
2. **Аналитичность $U$ существенно работает в двух местах — (i) и (iii)** (З3 R32); пункты (ii), (iv)
   от аналитичности $U$ не зависят.
   - (i) *Конечность $j$* на компоненте, где $U<0$: аналитическая $R\not\equiv0$ имеет конечный порядок
     по $s$, и вдоль дна $U\approx s^jG$. Для $C^\infty$ функция $R$ может быть плоской и ненулевой (например,
     $R=-e^{-1/s^2}$): нет ни $j$, ни эффективного потенциала. Здесь проходит граница с гладкими
     примерами: у примеров Пенлеве–Уинтнера и Лалуа все однородные части нулевые ([008], замечание 1;
     по `problem/KNOWN_RESULTS.md`, с первоисточниками не сверено).
   - (ii) *Дихотомия (a/b)/(c)* — свойство $G$, а не $U$: $G=g_j$ определяется струёй $j^jU$ ([008], §3.3), а
     $\Sigma_0$ — аналитическая кривая, заданная многочленом $u_m$ с условием (K2). Поэтому $G$ аналитична на
     $\Sigma_0$ и для неаналитического $U$ с $j<\infty$: она либо постоянна, либо её минимумы изолированы и
     имеют конечный порядок $2p$. В теореме Mb используется только (r1): $\Lambda\ge\frac a2\theta^{2p}$,
     $\theta\Lambda'\ge\Lambda$. [Эскиз, R26 §7] Доказательство Mb прошло бы и для гладкой $\Lambda$ со строгим
     минимумом и $\theta\Lambda'\ge\Lambda$ (с $R_\theta$ из обращения $\Lambda$); «негладкое» условие Mb — $G(\theta_0)<0$ на
     конечной струе.
   - (iii) *Каскад (d):* подготовительная теорема Вейерштрасса и ряды Пюизё для полярной кривой
     $\partial_\theta\hat G=0$ (нужна совместная аналитичность $\hat G$ по $(s,\theta)$); сравнимость конечного числа
     ветвей (лемма V, п. 4: одна ветвь минимума сразу для всех малых $s$); конечный порядок глубины
     ($-a_Vs^\gamma$, $F_{d,0}(0)<0$); конечный многоугольник Ньютона и полиномиальный профиль $Q_V$;
     аналитичность $F_d$ по $t=x^{1/N}$. [Гипотеза] Для $C^\infty$-функции $\hat G$ минимизатор может
     бесконечно часто перескакивать с ветви на ветвь, глубина может быть плоской, а профиль — без
     степенного масштаба; тогда ни (F), ни $(V_0)$ не получаются.
   - (iv) *Нормальная форма* (0.2), (2.4) даёт условие (F) с непрерывным продолжением в $s=0$ во всех
     трёх теоремах. Для $C^\infty$-потенциала с $j<\infty$ она тоже верна: $\varphi$ гладка по лемме Адамара,
     $y^*$, $M$, $\hat G$ гладки по гладкой теореме о неявной функции (З3 R32).
3. **Чего здесь нет.** Теоремы Mb, Mc, Md — утверждения для $U$ с условиями конечного типа на струю.
   Для гладкого $U$ без них ничего не утверждается. Пример Уреньи (по `problem/KNOWN_RESULTS.md`, не
   сверено) не конфликтует: утверждается одна асимптотическая траектория, а не тотальная
   неустойчивость.

## Замечания

### 1. Точность $\kappa(\delta)$ и члены кривизны при $p\ge3$

- [Доказано] При $p\ge2$ линейная оценка перекрёстных членов в духе леммы 2 [007] даёт $L_1\gamma_1/\sqrt\delta\asymp\kappa\delta^{1/(2p)-1/2}$,
  что больше запаса $\kappa$ при малом $\delta$; поэтому нужна лемма M. По той же причине теорема 2′ [008]
  к случаю (b) не применима: условие $(V_1')$ требует $Q\ge\lambda_0\lvert b\rvert^2$, а при $p\ge2$ этого нет.
- Члены кривизны конуса оценку не ломают ни при каком $p$ [Доказано, это часть доказательства Mb]:
  в $\gamma_2$ они дают $\frac54\kappa^2R_\theta^2(1+\bar k_g)$, то есть вклад $\asymp\kappa^4R_\theta^4/\delta\asymp\kappa^2\delta\ll\kappa$ в $\Gamma^2/\delta$; в $T_3$ —
  только $2\vartheta_3<\beta-\mu$.
- [Эксперимент, R26, `experiments/reviewer/morse-bott-R26/`] При фиксированном $\kappa$ и $p\ge2$ ломается
  само (A5) для поля $Y_\kappa$: на модели $U=Q_0^2+u_5$ критическое $\kappa$ ведёт себя как $\approx5{.}4\,\delta^{1/2}$
  ($p=2$) и $\approx10{.}9\,\delta^{2/3}$ ($p=3$). Порядок $\kappa\asymp\delta^{1-1/p}$ в (0.4) численно точен для поля $Y_\kappa$
  (это не доказано и относится только к семейству $Y_\kappa$); константа (0.4) примерно в $10^3$ раз меньше
  критической.
- [Доказано] При $p=1$ (0.4) даёт $\kappa$, не зависящее от $\delta$, — того же вида, что (U3) [008]. Теорема Mb
  при $p=1$ заново доказывает основное утверждение теоремы K2 [008] (траектория и оценки
  $\lvert\theta\rvert,\lvert e\rvert\lesssim\sqrt\delta$) без теоремы 2′. Касание конуса $Z$ и конус раствора $O(\sqrt\delta)$ вокруг луча в
  теореме Mb не сформулированы (З7 R33).

### 2. Почему в (d) $C_1=0$

[Доказано: это (8.1), (8.3); пояснение] Поворот поля $Y=\Phi_x$ относительно радиального направления равен $\tilde\kappa=x\tau_v'-x^\alpha b_1$. В узком
овраге ($\alpha>0$) он стремится к нулю равномерно по $\lvert b\rvert<r_0$, и вместе с ним уходят все члены
кривизны (нормальная кривизна конуса входит через $\tilde\kappa^2\Psi_{\theta\theta}/x$). Запас Эйлера по углу
сохраняется: при фиксированной длине дуги $u$ и убывающем $x$ масштабированное смещение $b_1=u/x^{1+\alpha}$
растёт. В (a)/(b) овраг широкий ($\alpha=0$), и поворот, создающий угловой запас, имеет порядок
$\kappa\lvert\theta\rvert$ — отсюда лемма M.

### 3. Поле $Y=\partial_x\Phi+Z$

[Доказано: это (2.5)] В теоремах Mb, Mc поле задано прямо в координатах $(s,\theta,\zeta)$: $Y=\Psi_s+Z$, $Z=-\frac{\kappa\theta}s\Psi_\theta$ (Mc:
$\kappa=0$). По (2.5) оператор Эйлера равен $\xi F-\frac\varsigma2\partial_\varsigma F$ с $\xi=\kappa\theta\partial_\theta+ce\,\partial_e$. Лемма E
([`results/009-euler-field.md`](009-euler-field.md)) здесь не нужна: в (d) профиль (8.5) — сумма одномерного
углового и невырожденного нормального, и веса $(1+\alpha,c')$ годятся.

### 4. Примеры [Эксперимент; рецензентами не проверялись]

В записке (§9) разобраны примеры с $u_4=Q_0^2$, $Q_0=x^2+y^2-z^2$: C1 $=Q_0^2-z^6+xz^6$ и
C2 $=(Q_0+z^3)^2-z^7+xyz^6$ (случай (c)); D1 $=Q_0^2+y^2z^4+xz^6+xyz^5$, D2s $=Q_0^2+4y^4z^2+xz^6$,
D2 $=Q_0^2+4y^4z^2+xz^6+xyz^5$, D3 $=(Q_0+z^3)^2+y^2z^6+xz^8$ (случай (d); у D2, D2s угловой минимум
вырожден, $k_0=4$); B $=Q_0^2-z^6+4y^4z^2+xyz^5$ (случай (b), $p=2$). Ряды $g_k$ — точная арифметика sympy;
дно оврага D1, D2, D2s совпадает с прогнозом леммы V до $s=10^{-8}$; численный строгий выход (A5) в
областях теорем Mb, Mc, Md положителен (в (b) — только при $\kappa>0$); у C2 и D3 радиальное условие
Четаева нарушено (численно). Изолированность C1, D2s доказана в записке вручную, остальных —
по критериям K4′ [008] и лемме I записки. Для теоремы M изолированность не нужна.

### 5. Что остаётся открытым

- Касание траекторией луча в случаях (a), (b) (доказан только конус раствора $O(\delta^{1/(2p)})$) и в (c)
  (угол не контролируется) [Гипотеза: в (a), (b) касание есть]. В (d) касание доказано.
- Нарушение условия Морса–Ботта (вырожденная нормальная форма, например $u_8=Q_0^4$), особое $\Sigma$
  ($u_4=x^2y^2$), $n\ge4$ — здесь не рассматривались.
- Литература леммы V с первоисточниками не сверена.

## Отличия от записки

Записка `notes/prover/2026-10-21-morse-bott.md` во второй редакции уже содержит правки §12; ниже —
полный перечень отличий этого текста от первой редакции, прочитанной R26–R28.

**Правки по R28** (`notes/reviewer/2026-10-21-morse-bott-M.md`).

1. З1: изолированность убрана из предложения R и теоремы M; $j<\infty$ выводится из отрицательных
   значений и аналитичности (предложение R, п. 2). Раздел об аналитичности и изолированности
   переписан.
2. З2: ссылки переведены на нумерацию [008].
3. З3: ссылка на K0′(b) не нужна (шаг удалён).
4. З4: [002] внесён в «Зависит от»; аналитичность $\Sigma_0$ — по [008], §1.
5. З5: в теореме Mc явно $\sigma_0=s_2$, $\sigma=\sigma_*$ и условия на $s_2$.
6. З6: в предложении R разобран случай $\Sigma=\varnothing$.
7. З7: формула для $s\langle w,D_wY\rangle$ при $\kappa=0$ выведена прямо (§6, п. 6); (5.3) выведена в §5.1;
   утверждения о $C^\infty$ помечены [Эскиз]/[Гипотеза].

**Правки по R27** (`...-Md.md`).

8. З1: в лемме V, п. 3 $s_4\le t_3^{N_1}$.
9. З2: «$\Gamma$ чётно» внесено в формулировку леммы V.
10. З3: в §8 явно проверены условия леммы V, включая $G\not\equiv0$ около $\theta_0$.
11. З4: в §8, п. 6 зафиксирован выбор $s_0$.
12. З6: «глобальный минимум» — в окне $[-\tau_0,\tau_0]$.
13. Попутно: «при $\beta>2$» заменено на $\beta>m\ge2$; в $(V_1)$ указано $r_1=r_0/2$.

**Правки по R26** (`...-Mb.md`).

14. З1: в §5.2, п. 4 явно $s_2^{c-1}<y_1/4$, $\mathcal O\subset B_r$, $\sigma=\sigma_*$.
15. З2: аналитичность $F$ в окрестности компакта и $\chi\to0$ сказаны явно.
16. З3: $\vartheta_3$ взято без слагаемого $\frac54\kappa^2R_\theta^2$ (четвёртый член (5.3) разложен, его главная часть
    $\ge0$); соответственно в п. 7 условие $\frac54R_\theta^2\le\frac18$ больше не нужно.
17. З4: сравнение леммы M с леммой 2 — в записке; здесь лемма M названа вариантом, а не усилением.
18. З5, З6: в замечании 3 оператор Эйлера записан с членом $-\frac\varsigma2\partial_\varsigma F$; условие $2\vartheta_3<\beta-\mu$
    не отождествляется с «$\vartheta_3<\beta/2$».
19. З7: в §5.1 сказано, что сокращаются именно члены $\mp\kappa\theta k_gw_\ell w_n$.
20. З8: в замечание 1 добавлен численный порог $\kappa_{\rm crit}$ (R26).

**Уточнения при оформлении** (математика та же).

21. Обозначения [008]: $T\to\ell$, $k\to k_g$, $\varepsilon\to\epsilon$, $P\to\Pi$, нормальная компонента $Y_\kappa$: $\psi\to\nu$;
    открытое множество теоремы A $\mathcal G\to\mathcal O$; $\sigma=s^{1/2}\to\varsigma$; супремум малых величин
    $\nu(\sigma)\to\Delta(\sigma)$; угловая функция карты (5.1) записки $\vartheta(x,u)\to\hat\theta(x,u)$ (буква $\vartheta_i$ занята
    константами (L3)); профиль теоремы Md $F,F_0\to F_d,F_{d,0}$; показатель $\ell$ леммы V $\to\ell_*$ (буква $\ell$
    занята касательной).
22. Тождества Эйлера теорем Mb, Mc объединены в (2.5); лемма M дополнена нижней оценкой $\dot\rho$ (она
    дословно из п. 2 леммы 2 [007] и использовалась в записке в Mb, п. 8).
23. Нумерация формул (записка $\to$ здесь): (2.1) $\to$ (0.1); (2.2) $\to$ (U1), (1.1) [008]; (2.3) $\to$ (0.2);
    (2.5) $\to$ (2.1); (2.6) $\to$ (2.2); (2.7) $\to$ (2.3); (2.8) $\to$ (2.4); (4.1) и (6.4) $\to$ (2.5); (5.1) $\to$ (0.5);
    (5.2)–(5.6) $\to$ (8.1)–(8.5); (6.1) $\to$ (0.3); (6.2) $\to$ (5.4); (6.3) $\to$ (5.1); (6.5) $\to$ (5.2); (6.6) $\to$ (0.4);
    (6.7) $\to$ (5.3).
24. Лемма I, примеры §9 и численные эксперименты записки включены только как помеченное замечание
    4 (рецензентами не проверялись).

**Правки по R32, R33** (`notes/reviewer/2026-10-21-result010-A.md`, `...-B.md`; ошибок нет, правки
редакционные, новых утверждений нет).

25. R32, З1: в теореме Mc (§6, п. 7) в выбор $\sigma_*$ добавлено $\Delta(\sigma_*)\le\min(\frac14,(1+\bar k_g)^{-1})$; это даёт
    $h\le\frac32$, $\lvert\epsilon\rvert\le\frac14$, $\lvert k_g\eta^*_s\rvert\le1$ на $D_\sigma$.
26. R32, З2: в теореме Mc множество $\{Q<4\delta\}$ обозначено $\Omega_\delta$ (не путать с фазовым $\Omega$ теоремы A).
27. R32, З3: раздел «Где работают аналитичность и изолированность», п. 2: аналитичность $U$ существенно
    работает в (i) и (iii); в (ii) и (iv) указано, почему они верны и без неё ($G$ определяется струёй, $\Sigma_0$
    аналитична; нормальная форма гладкая по лемме Адамара и гладкой теореме о неявной функции).
28. R32, З4: пример плоской функции — $-e^{-1/s^2}$.
29. R32, З5: $F_{\rm fl}=s^j\hat G$ — только при $j<\infty$.
30. R32, З6: у (2.4) указана область: $0<s<s_1$, $\lvert s^{c-1}e\rvert<y_1/2$.
31. R32, З7: «задача (A) решена» заменено на «(A) выполнено в этом классе; результат проверен агентами и
    ждёт проверки человеком». R32, З8 — правка не нужна (рецензент проверил, что инъективность не
    используется).
32. R33, З1: показатели леммы V переименованы: $\Gamma\to\Gamma_V$, $A\to A_V$, $a\to a_V$ (не путать с $\Gamma$ леммы M, $A(r)$
    теоремы A, $a$ теоремы Mb); показатель в (2.2) $c_0\to c_\zeta$ (не путать с $c_0$ из $(\Phi0)$); отображение
    $L\to\mathcal L$ в §8, п. 1 (не путать с длиной $L$); в §8, п. 7 оговорено, что $r_1=r_0/2$ — радиус из $(V_1)$, а не
    окно теоремы Mb.
33. R33, З2: в §8, п. 6 в выбор $s_0$ добавлено $2s_0<r$.
34. R33, З3: в §7, п. 4 сказано, что $I_{\mathbb R}\ne\varnothing$.
35. R33, З4: $\frac12\min\{g(\tau_0),g(-\tau_0)\}$.
36. R33, З5: в §5.2, п. 4 — «при фиксированном $\sigma_*$ $D$ от $\kappa$ не зависит».
37. R33, З6: в §8, п. 3 $\nu_1(x)$ — супремум по точкам $\mathcal N$ с абсциссой $\le x$.
38. R33, З7: метки в замечаниях 1–3; «порядок $\kappa\asymp\delta^{1-1/p}$ точен» → «численно точен для поля
    $Y_\kappa$» [Эксперимент]; «Mb при $p=1$ заново доказывает K2» уточнено: основное утверждение K2
    (траектория и оценки $\lvert\theta\rvert,\lvert e\rvert$), без касания конуса $Z$ и конуса $O(\sqrt\delta)$ вокруг луча.
39. R33, З8 (литература леммы V не сверена) — без изменений, это отмечено в тексте. R33, З9
    (явные $k_1,k_2$ в теореме Mb) не вносилось: необязательно.
