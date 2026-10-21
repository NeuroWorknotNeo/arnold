# 008. Класс $\mathcal K$: асимптотические траектории при нестрогом минимуме младшей формы с невырожденным конусом нулей

- **Статус:** [Проверено: reviewer R20, R21, R22 (агенты), 21.10.2026 — доказательства в записке
  [`notes/prover/2026-10-21-gt3-hardcore.md`](../notes/prover/2026-10-21-gt3-hardcore.md); reviewer R23, R24
  (агенты), 21.10.2026 — текст этого результата целиком: ошибок нет]; ждёт проверки человеком.
  - R23 ([`notes/reviewer/2026-10-21-result008-A.md`](../notes/reviewer/2026-10-21-result008-A.md)):
    §1–§5, §11–§12, замечание 1 — леммы K1, K2, теорема K0, следствие K0′, предложение K4,
    следствие K4′, примеры. Ошибок нет; редакционные замечания З1–З7.
  - R24 ([`notes/reviewer/2026-10-21-result008-B.md`](../notes/reviewer/2026-10-21-result008-B.md)):
    §6–§10 — лемма K3, теорема K1, лемма 2′, теорема 2′, теорема K2. Ошибок нет; редакционные
    замечания пп. 1–4.
  - Правки по R23, R24 внёс автор оформления (перечень — «Отличия от записки», подраздел «Правки по
    R23, R24»); новых утверждений они не добавляют. Главный агент прочитал их; вычисление для $\Sigma_-$
    в примере 3 ($G_-(\varphi+\pi)=-G_+(\varphi)$, точка $7\pi/6$, $G''+7G=-(9\sqrt6+14\sqrt2)/64$) пересчитал.
  - R20 ([`notes/reviewer/2026-10-21-gt3-hardcore-A.md`](../notes/reviewer/2026-10-21-gt3-hardcore-A.md)):
    §2–§5 и §10.1 записки — леммы K1, K2, теорема K0, следствие K0′, предложение K4, следствие K4′.
    Ошибок нет, кроме формулировки критерия минимума в K4(c) при $R_\omega\equiv0$; здесь он
    исправлен (предложение K4(c)).
  - R21 ([`...-B.md`](../notes/reviewer/2026-10-21-gt3-hardcore-B.md)): §7 записки — лемма 2′ и
    теорема 2′. Ошибок нет.
  - R22 ([`...-C.md`](../notes/reviewer/2026-10-21-gt3-hardcore-C.md)): §6, §8, §9.6–9.7 записки —
    лемма K3, теоремы K1 и K2, примеры. Ошибок нет; $U_{(8)}$ изолирована над $\mathbb R$, но не над
    $\mathbb C$ (здесь это сказано явно).
  - Все замечания рецензентов R20–R24 учтены; перечень — в разделе «Отличия от записки».
  - Метки: всё в разделе «Утверждение» — [Доказано]. Замечания помечены каждое отдельно.
- **Автор:** prover (агент), записка `notes/prover/2026-10-21-gt3-hardcore.md` (21.10.2026).
  Оформление — prover (агент), 21.10.2026.
- **Зависит от:**
  - [007] = [`results/007-gt3.md`](007-gt3.md): теорема A, лемма 1 (формулы (0.1), (1.1), (1.3)),
    теорема 2 вместе с шагами 1–3 и 6 её доказательства, следствия 1 и 2;
  - [002] = [`results/002-theorem-B.md`](002-theorem-B.md): §2.1(f), §2.2 (аналитичность $\Sigma$ и
    аналитическая ортонормированная рамка нормалей), (F1) (аналитическая теорема об обратной
    функции), лемма 2, п. 1 (мажоранта для ряда по $s$);
  - стандартные факты: аналитическая теорема о неявной функции (выводится из (F1), применённой к
    $(s,\theta,y)\mapsto(s,\theta,\partial_y\varphi)$), теорема единственности для аналитических
    функций, формула Тейлора с интегральным остатком, теорема о промежуточном значении.
  - Литература используется только в замечаниях.
- **Проверочные скрипты** [Эксперимент]:
  - [`experiments/prover/gt3-hardcore/`](../experiments/prover/gt3-hardcore/) — автор записки;
  - [`experiments/prover/gt3-result008/`](../experiments/prover/gt3-result008/) — явные семейства
    примера 3 и комплексные критические прямые $U_{(8)}$ (сделано при оформлении);
  - `experiments/reviewer/gt3-hardcore-R20/`, `-R21/`, `-R22/` — рецензенты.

## Утверждение

### Обозначения

$\mathbb R^n$ с евклидовыми $\langle\cdot,\cdot\rangle$, $|\cdot|$; $B_r=\{|q|<r\}$, $S^{n-1}$ — единичная
сфера. $U$ вещественно-аналитична в шаре $B_{\rho_0}$, $U(0)=0$, и
$$U=\sum_{k\ge m}u_k,\qquad u_k\ \text{— однородный многочлен степени }k,\quad u_m\not\equiv0,\quad m\ge2;$$
ряд Тейлора $\sum_\alpha c_\alpha q^\alpha$ сходится абсолютно к $U$ при $\max_i|q_i|\le R_0$ (уменьшив
$R_0$, этого всегда можно добиться). Система $\ddot q=-\nabla U(q)$. **Асимптотическая траектория** —
решение $q(t)\ne0$, $t\ge0$, с $q(t)\to0$, $\dot q(t)\to0$ при $t\to+\infty$; из неё следует
неустойчивость по Ляпунову ([007], теорема A, шаг 6 доказательства). Обозначения $p,h,v_\perp,K_\perp,W,V,\lambda,\Xi$,
условия (D1)–(D4), (A4), (A5), (L0), (L1) — как в [007].

$Z=\{u_m=0\}$, $\Sigma=Z\cap S^{n-1}$. Если $u_m\ge0$, то $u_m$ чётна ($m$ чётно), $\Sigma=-\Sigma$ и
$Z=\{\nabla u_m=0\}$ ([002], §2.1(b)). Для $\omega\in\Sigma$, около которой $\Sigma$ — гладкое
подмногообразие, $N_\omega:=(\mathbb R\omega\oplus T_\omega\Sigma)^\perp$ (если $\omega$ — изолированная точка
$\Sigma$, то $N_\omega=\omega^\perp$). Через $\mathcal Eu(q):=\langle\nabla u(q),q\rangle$ обозначена
радиальная производная.

### Данные (S) и редуцированная функция

**(S)** Пусть $d\in\{0,1\}$, $\Lambda'$ — открытый интервал (при $d=0$ — точка), $\Lambda\subset\Lambda'$ —
компактный интервал (при $d=0$ — та же точка), и заданы аналитические $\omega:\Lambda'\to S^{n-1}$
(инъективная иммерсия при $d=1$) и $e_1,\dots,e_p:\Lambda'\to\mathbb R^n$, $p=n-1-d$, такие, что при всех
$\theta\in\Lambda'$:

- $u_m(\omega(\theta))=0$ и $\nabla u_m(\omega(\theta))=0$;
- $e_1(\theta),\dots,e_p(\theta)$ — ортонормированный базис
  $N_\theta:=\big(\operatorname{span}(\omega(\theta),\omega'(\theta))\big)^\perp$ (при $d=0$: $N=\omega^\perp$);
- $H(\theta):=\big(D^2u_m(\omega(\theta))(e_a,e_b)\big)_{a,b\le p}\succ0$.

Положим
$$\varphi(s,\theta,y):=\sum_{k\ge m}s^{k-m}u_k\Big(\omega(\theta)+\sum_{a=1}^py_ae_a(\theta)\Big),\qquad y\in\mathbb R^p. \tag{U1}$$

По лемме K1 (§2 доказательства) при $|s|<s_1$, $\theta\in\Lambda''$ функция $\varphi(s,\theta,\cdot)$ имеет в шаре
$|y|<y_1$ единственную критическую точку $y^*(s,\theta)$, аналитическую по $(s,\theta)$, с $y^*(0,\theta)=0$.
**Определения:**
$$R(s,\theta):=\varphi\big(s,\theta,y^*(s,\theta)\big),\qquad \eta^*(s,\theta):=s\sum_ay^*_a(s,\theta)e_a(\theta)\in N_\theta,\qquad g_{m+i}(\theta):=\frac{\partial_s^iR(0,\theta)}{i!};$$
$$j:=\min\{k>m:\ g_k\not\equiv0\ \text{на}\ \Lambda''\},\qquad G:=g_j\ \ (\text{эффективный потенциал}),\qquad c:=\frac{j-m+2}2\ \ (\text{нормальный вес}).$$
При $0<s<s_1$ имеем $U\big(s\omega(\theta)+\eta^*(s,\theta)\big)=s^mR(s,\theta)=:U_{\rm red}(s,\theta)$, и
$s\omega+\eta^*$ — единственная критическая точка сужения $U$ на множество
$\{s\omega+\xi:\ \xi\in N_\theta,\ |\xi|<y_1s\}$. Поэтому $R$, $g_k$, $j$, $G$ не зависят от выбора рамки и
параметризации (§3). $R(0,\theta)=0$; если $j<\infty$, то $R=s^{j-m}\hat G(s,\theta)$ с аналитической $\hat G$,
$\hat G(0,\cdot)=G$, и $c\ge\frac32$. Первые члены: $g_{m+1}=u_{m+1}|_\Sigma$,
$g_{m+2}=u_{m+2}|_\Sigma-\frac12b_1^{\mathsf T}H^{-1}b_1$, $b_1=(\langle\nabla u_{m+1}(\omega),e_a\rangle)_a$; $G$
определяется струёй $j^jU$.

### Класс $\mathcal K$ ($n=3$)

$U$ принадлежит **классу $\mathcal K$**, если $n=3$, $m\ge2$ и

- **(K1)** $u_m\ge0$; $\Sigma\ne\varnothing$ — гладкое компактное подмногообразие $S^2$ (его компоненты —
  точки и замкнутые кривые);
- **(K2)** (Морс–Ботт) $D^2u_m(\omega)$ положительно определена на $N_\omega$ при всех $\omega\in\Sigma$;
- **(K3)** есть компонента $\Sigma_0$ и точка $\omega^*\in\Sigma_0$ такие, что для $j=j(\Sigma_0)<\infty$ и
  $G=g_j|_{\Sigma_0}$: $G(\omega^*)<0$, а при $\dim\Sigma_0=1$ ещё $G'(\omega^*)=0<G''(\omega^*)$ (производные
  по натуральному параметру $\Sigma_0$).

$\mathcal K^0$ — случай $\dim\Sigma_0=0$, $\mathcal K^1$ — $\dim\Sigma_0=1$; $\mathcal K^1_{\rm C}\subset\mathcal K^1$ —
подкласс с $G''(\omega^*)+jG(\omega^*)>0$.

**Теорема K (сводка).** Если $U\in\mathcal K$, то есть асимптотическая траектория, и равновесие
неустойчиво по Ляпунову: $\mathcal K^0$ — теорема K0, $\mathcal K^1$ — теорема K2 ($\mathcal K^1_{\rm C}$ —
также теорема K1). Изолированность критической точки не предполагается.

### Теорема K0 (любое $n\ge2$; $\Sigma$ — точка около $\omega^*$)

Пусть $n\ge2$, $\omega^*\in S^{n-1}$, $u_m(\omega^*)=0$, $\nabla u_m(\omega^*)=0$,
$H:=D^2u_m(\omega^*)|_{\omega^{*\perp}}\succ0$, и в обозначениях (S) с $d=0$, $N=\omega^{*\perp}$, $p=n-1$
выполнено $j<\infty$ и $g_j(\omega^*)<0$. Положим $\lambda_0=\lambda_{\min}(H)/4$. Тогда есть $\delta_*>0$ такое,
что для каждого $\delta\in(0,\delta_*]$ есть асимптотическая траектория
$$q(t)=x(t)\,\omega^*+\eta^*\big(x(t)\big)+x(t)^c\sum_ab_a(t)e_a,\qquad x(t)\downarrow0,\quad -k_2x^{j/2}\le\dot x\le-k_1x^{j/2},\quad|b(t)|\le2\sqrt{\delta/\lambda_0},$$
с постоянными $0<k_1\le k_2$; в частности, $x(t)\asymp t^{-2/(j-2)}$.

### Следствие K0′ (конечное $\Sigma$, любое $n\ge2$)

Пусть $n\ge2$, $u_m\ge0$, $\Sigma$ конечно и $D^2u_m(\omega)|_{\omega^\perp}\succ0$ при всех $\omega\in\Sigma$
(то есть $u_m|_{S^{n-1}}$ имеет в своих нулях невырожденные критические точки). Для $\omega\in\Sigma$
обозначим через $R_\omega(s)$ функцию $R$ при $d=0$, $\omega^*=\omega$. Тогда:

- **(a)** если при каждом $\omega\in\Sigma$ функция $R_\omega\not\equiv0$ и её старший коэффициент
  $g_{j(\omega)}(\omega)>0$, то $0$ — строгий локальный минимум $U$;
- **(b)** если $R_\omega\equiv0$ при некотором $\omega$, то кривая $x\mapsto x\omega+\eta^*_\omega(x)$, $0<x<s_1$,
  состоит из критических точек $U$, и $0$ — неизолированная критическая точка;
- **(c)** если $g_{j(\omega)}(\omega)<0$ при некотором $\omega$, то есть асимптотическая траектория.

В частности, **если $0$ — изолированная критическая точка $U$ и не локальный минимум, то есть
асимптотическая траектория, и равновесие неустойчиво по Ляпунову.** Если $\Sigma=\varnothing$, то $0$ —
строгий минимум.

### Класс (GT3′) и теорема 2′ (любое $n\ge2$)

Данные — как у класса (GT3) в [007]: $U\in C^2(B_r)$, $U(0)=0$, $\nabla U(0)=0$, $\beta>0$, веса
$c=(c_1,\dots,c_{n-1})\in(0,\infty)^{n-1}$, $c_{\max}=\max c_i$, $N\in\mathbb N$, $s_0\in(0,1]$, $r_0>0$,
$b=(u_ix^{-c_i})_i$, $\mathcal N=\{(x,u):\ 0<x<s_0,\ |b|<r_0\}$. Переменную $x^{1/N}$ (в [007] — $s$)
здесь обозначаем $\varsigma$, малую функцию $\omega(x)$ из [007] — $\varpi(x)$, функцию $\omega_0(x)$ из
$(\Phi0)$ — $\varpi_0(x)$. Карта $\Phi\in C^2(\mathcal N;\mathbb R^n)$, $Y:=(\partial_x\Phi)\circ\Phi^{-1}$,
$\rho:=x\circ\Phi^{-1}$, $h=|Y|^2$. $U$ **принадлежит классу (GT3′)**, если выполнены:

- **$(\Phi0)$** как в [007]: $\Phi$ — $C^2$-диффеоморфизм $\mathcal N$ на открытое подмножество
  $B_r\setminus\{0\}$, и $c_0x\le|\Phi(x,u)|\le\varpi_0(x)\to0$;
- **$(\Phi1')$** $\frac12\le h\le\frac32$ на $\mathcal N$;
- **$(\Phi2')$** есть $\gamma_1,\gamma_2,C_1\ge0$ и $\varpi(x)\to0$ ($x\to0$) такие, что при $(x,u)\in\mathcal N$ и
  $w\perp\partial_x\Phi(x,u)$
  $$|\langle\nabla\rho-Y/h,w\rangle|\le\big(\gamma_1|b|+\varpi(x)\big)|w|,\qquad x\,|\langle\partial_x^2\Phi,w\rangle|\le\big(\gamma_2|b|+C_1|b|^2+\varpi(x)\big)|w|;$$
- **$(\Phi3)$** как в [007]: $x\langle w,D_wY\rangle\ge-(C_1|b|+\varpi(x))|w|^2$ для $w\perp\partial_x\Phi$;
- **(F)** как в [007] (с $\varsigma$ вместо $s$): $U(\Phi(x,u))=x^\beta F(\varsigma,b)$, $F$ и $\nabla_bF$ непрерывно
  продолжаются на $[0,s_0^{1/N})\times B_{r_0}$, $\sup_{b\in K}|\varsigma\partial_\varsigma F|\to0$ на компактах;
  $F_0=F(0,\cdot)$, $Q=F_0-F_0(0)$, $a_0:=-F_0(0)$;
- **$(V_1')$** $F_0(0)<0$; есть $\lambda_0>0$, $\mu\in(0,\beta]$, $r_1\in(0,r_0)$ с $Q(b)\ge\lambda_0|b|^2$ и
  $\sum_ic_ib_i\partial_{b_i}Q(b)\ge\mu Q(b)$ при $|b|<r_1$, и
  $$\Gamma_*^2\le\beta\mu,\qquad\Gamma_*:=\sqrt{a_0/\lambda_0}\,\Big[\tfrac{3\sqrt3}2\,\beta\gamma_1+2\sqrt2\,\gamma_2\Big]. \tag{U2}$$

**Теорема 2′.** Если $U$ принадлежит классу (GT3′), то есть $\delta_*>0$ такое, что для каждого
$\delta\in(0,\delta_*]$ есть асимптотическая траектория $q(t)=\Phi(x(t),u(t))$ с $x(t)\downarrow0$,
$-k_2x^{\beta/2}\le\dot x\le-k_1x^{\beta/2}$ ($0<k_1\le k_2$) и $|b(t)|\le2\sqrt{\delta/\lambda_0}$ при всех
$t\ge0$. Равновесие неустойчиво по Ляпунову.

Карта класса (GT3) из [007] (условия $(\Phi1)$–$(\Phi3)$) удовлетворяет $(\Phi1')$–$(\Phi2')$ с
$\gamma_1=\gamma_2=0$ и $\varpi=2\sqrt2\,\omega$ ([007], шаг 4 доказательства теоремы 2:
$|\nabla\rho-Y/h|\le2\sqrt2|B_{xu}|$), и при $\gamma=0$ условие (U2) выполнено; поэтому случай $(V_1)$
теоремы 2 [007] — частный случай теоремы 2′. Новое: (i) $B=D\Phi^{\mathsf T}D\Phi$ может быть далеко от $I$
(важно только $h=B_{xx}$); (ii) допускаются перекрёстные члены, линейные по $|b|$, при условии (U2).

### Теорема K1 ($n=3$, декартова карта развёртки)

Пусть $n=3$, $\Sigma_0\subset S^2$ — аналитическая дуга около $\omega^*$ с натуральным параметром
$\theta$, $\omega(0)=\omega^*$, выполнены (S) с $d=1$, $e_1=n(\theta)$ (см. §6), $j<\infty$, $G(0)<0$, $G'(0)=0$ и
$G''(0)+jG(0)>0$. Тогда $U$ принадлежит классу (GT3) [007] с $\beta=j$, весами $(1,c)$, $N=2$, картой
(7.1) и условием $(V_1)$; по теореме 2 [007] есть асимптотическая траектория.

### Теорема K2 ($n=3$, поворачивающаяся полярная карта)

Пусть $n=3$, выполнены (S) для дуги около $\omega^*$ ($d=1$, натуральный параметр, $e_1=n$ — §6), $j<\infty$,
$G(0)<0$, $G'(0)=0$, $G''(0)>0$. Положим $a_0=-G(0)$, $h_n(\theta)=D^2u_m(\omega(\theta))(n,n)$,
$\lambda_0=\frac14\min(G''(0),h_n(0))$ и выберем
$$0<\kappa\le\min\Big(\frac12,\ \frac{j\lambda_0}{a_0\big(\frac{15\sqrt3}8j+2\sqrt2\big)^2}\Big). \tag{U3}$$
Тогда $U$ принадлежит классу (GT3′) с $\beta=j$, весами $(\kappa,c)$, $N=2$, картой (10.1), $\mu=\kappa$,
$\gamma_1=\frac54\kappa$, $\gamma_2=\kappa(1-\kappa)$. Следовательно, для каждого достаточно малого $\delta>0$ есть
асимптотическая траектория $q(t)=s(t)\omega(\theta(t))+\eta(t)n(\theta(t))$ с $s(t)\asymp t^{-2/(j-2)}$,
$|\theta(t)|\le2\sqrt{\delta/\lambda_0}$, $|\eta(t)-\eta^*(s(t),\theta(t))|\le2\sqrt{\delta/\lambda_0}\,s(t)^c$. Она касается конуса
$Z$ ($\operatorname{dist}(q,Z)\le|\eta|=O(|q|^{\min(2,c)})$) и лежит в конусе раствора $O(\sqrt\delta)$ вокруг луча
$\mathbb R_+\omega^*$.

### Предложение K4 и следствие K4′ ($n=3$, сведение к задаче на дне)

Пусть $n=3$, выполнены (K1), (K2). Для компоненты-кривой $\Sigma_0$ (покрытой конечным числом дуг;
$R$, $\eta^*$ от дуги не зависят) положим $F_{\rm fl}(s,\theta):=s^mR(s,\theta)$ — **функция дна**. Константу
$y_1$ леммы K1 возьмём не больше $t_1$ из леммы K3. **Трубка** компоненты-кривой —
$\{s\omega(\theta)+\eta n(\theta):\ 0<s<s_1,\ |\eta|<y_1s\}$, трубка точечной компоненты $\{\omega\}$ — конус
$C_\omega=\{q:\ \langle q,\omega\rangle>0,\ |q-\langle q,\omega\rangle\omega|<\frac{y_1}2\langle q,\omega\rangle\}$.

**Предложение K4.** При $0<s<s_1$:

- **(a)** $U(s\omega(\theta)+\eta n(\theta))\ge F_{\rm fl}(s,\theta)$ при $|\eta|<y_1s$, с равенством только при
  $\eta=\eta^*(s,\theta)$;
- **(b)** точка $q=s\omega(\theta)+\eta n(\theta)$ трубки компоненты-кривой критическая для $U$ тогда и только
  тогда, когда $\eta=\eta^*(s,\theta)$ и $(s,\theta)$ — критическая точка $F_{\rm fl}$;
- **(c)** около $0$ вне объединения трубок $\nabla U\ne0$ и $U>0$. Поэтому $0$ — локальный минимум $U$
  тогда и только тогда, когда $F_{\rm fl}\ge0$ при малых $s>0$ на всех кривых-компонентах и $R_\omega(s)\ge0$
  при малых $s>0$ во всех точечных компонентах (то есть $R_\omega\equiv0$ или её старший коэффициент
  положителен); $0$ — изолированная критическая точка тогда и только тогда, когда у $F_{\rm fl}$ нет
  критических точек при малых $s>0$ ни на одной кривой-компоненте и $R_\omega\not\equiv0$ во всех точечных
  компонентах.

**Следствие K4′.** Если, кроме (K1), (K2), на каждой компоненте-кривой $j<\infty$ и $0$ — регулярное
значение $G$, а в каждой точечной компоненте $j(\omega)<\infty$, то $0$ — изолированная критическая
точка $U$.

### Примеры

Обозначения: $Q_0=x^2+y^2-z^2$, $A=x^2-z^2$, $B=y^2-z^2$, $r_{xy}=\sqrt{x^2+y^2}$.

**Пример 1** ($s=0$). $U_{(5)}=A^2+B^2+z^5$. Здесь $\Sigma=\{(\pm1,\pm1,\pm1)/\sqrt3\}$, (K1), (K2) выполнены,
$j=5$ во всех точках $\Sigma$, $g_5(\omega)=z(\omega)^5$; в $\omega^*=(1,1,-1)/\sqrt3$ $g_5=-3^{-5/2}<0$, так что
$U_{(5)}\in\mathcal K^0$ и есть асимптотическая траектория. Точка $0$ изолирована (над $\mathbb R$), не минимум.

**Пример 2** ($s=0$, «искривлённое дно»). $U_{(7)}=P_1^2+P_2^2+z^7$, $P_1=x^2-z^2+z^3$, $P_2=y^2-z^2$.
Здесь $u_4=A^2+B^2$, $\Sigma$ — те же 8 точек, $g_5=g_6=0$, $j=7$, $g_7(\omega)=z(\omega)^7$; в $\omega^*=(1,1,-1)/\sqrt3$
$g_7=-3^{-7/2}<0$: $U_{(7)}\in\mathcal K^0$, есть асимптотическая траектория. Точка $0$ изолирована (над
$\mathbb R$), не минимум, гессиан нулевой. Радиальное условие Четаева нарушено: в каждой компоненте
множества $\{U_{(7)}<0\}\cap W_\varepsilon$, примыкающей к $0$ (окрестность $W_\varepsilon$ — §12), есть сколь угодно близкие к $0$
точки с $\mathcal EU_{(7)}>0$.

**Пример 3** ($s=1$, «искривлённое дно»). $U_{(8)}=P^2+u_7$, $P=Q_0+z^3$, $u_7=xz^6+xyz^5+\frac12z^7$.
Здесь $u_4=Q_0^2$, $\Sigma=\Sigma_+\cup\Sigma_-$ (окружности $z=\pm\frac1{\sqrt2}$), $g_5=g_6\equiv0$, $j=7$,
$$G_+=\tfrac{\sqrt2}{32}\big(1+2\cos\varphi+\sin2\varphi\big),\qquad G_-=\tfrac{\sqrt2}{32}\big(2\cos\varphi-\sin2\varphi-1\big)$$
($\varphi$ — полярный угол). Минимум $G_+$ — в $\varphi^*=\frac{5\pi}6$: $G_+=\frac{\sqrt2(2-3\sqrt3)}{64}<0$,
$G''=\frac{3\sqrt6}{16}>0$ (по натуральному параметру), $G''+7G=\frac{7\sqrt2}{32}-\frac{9\sqrt6}{64}<0$. Итак,
$U_{(8)}\in\mathcal K^1\setminus\mathcal K^1_{\rm C}$, и по теореме K2 есть асимптотическая траектория. Точка $0$ —
**изолированная над $\mathbb R$**, но **не над $\mathbb C$** (прямые $\{z=0,\ x=\pm iy\}$ состоят из комплексных
критических точек, число Милнора бесконечно); не минимум; гессиан нулевой. Радиальное условие
Четаева нарушено в каждой компоненте $\{U_{(8)}<0\}\cap W_\varepsilon$, примыкающей к $0$.

## Доказательство

### 1. Функция $\varphi$

Ряд $\tilde\varphi(s,z)=\sum_\alpha c_\alpha s^{|\alpha|-m}z^\alpha$ при $|s|<R_0/3$, $\max_i|z_i|<3$ мажорируется
рядом $3^mR_0^{-m}\sum_\alpha|c_\alpha|R_0^{|\alpha|}<\infty$ (так как $c_\alpha=0$ при $|\alpha|<m$ и
$(R_0/3)^{|\alpha|-m}3^{|\alpha|}=3^mR_0^{|\alpha|-m}$), поэтому $\tilde\varphi$ аналитична там ([002], лемма 2, п. 1).
При $|y|<1$ имеем $|\omega+\sum y_ae_a|=\sqrt{1+|y|^2}<2$, так что
$\varphi(s,\theta,y)=\tilde\varphi\big(s,\omega(\theta)+\sum y_ae_a(\theta)\big)$ аналитична на
$(-R_0/3,R_0/3)\times\Lambda'\times\{|y|<1\}$, и при этих $s$ любого знака (перегруппировка абсолютно
сходящегося ряда, $|sz_i|<R_0$)
$$U\Big(s\big(\omega(\theta)+\textstyle\sum_ay_ae_a(\theta)\big)\Big)=s^m\varphi(s,\theta,y). \tag{1.1}$$
Ссылка на [002] законна и при $\Sigma$ с компонентами разной размерности: используемые там места
(§2.1(f), §2.2) локальны и опираются только на $Z=\{\nabla u_m=0\}$ и невырожденность $D^2u_m$ на $N$.

### 2. Лемма K1 (критическая точка в слое)

**Лемма K1.** В условиях (S) найдутся $s_1\in(0,R_0/3)$, $y_1\in(0,1)$ и открытый интервал $\Lambda''$ с
$\Lambda\subset\Lambda''$, $\overline{\Lambda''}\subset\Lambda'$ (при $d=0$ — точка), такие, что при $|s|<s_1$,
$\theta\in\Lambda''$:

1. $\partial_y^2\varphi(s,\theta,y)\succeq\frac{\lambda_H}2I$ при $|y|<y_1$, где $\lambda_H:=\min_{\theta\in\Lambda}\lambda_{\min}H(\theta)>0$;
2. $\varphi(s,\theta,\cdot)$ имеет в шаре $|y|<y_1$ ровно одну критическую точку $y^*(s,\theta)$; она лежит в
   шаре $|y|<y_1/2$ и является точкой глобального минимума $\varphi(s,\theta,\cdot)$ на шаре $|y|<y_1$;
3. $y^*$ аналитична по $(s,\theta)$ и $y^*(0,\theta)=0$.

Кроме того, $y_1$ можно взять сколь угодно малым (уменьшив соответственно $s_1$).

*Доказательство.*

1. $\partial_y^2\varphi(0,\theta,0)=D^2u_m(\omega)(e_a,e_b)=H(\theta)\succeq\lambda_HI$ на $\Lambda$. По непрерывности
   $\lambda_{\min}\partial_y^2\varphi$ на компакте $[-s_1,s_1]\times\overline{\Lambda''}\times\{|y|\le y_1\}$ при малых
   $s_1,y_1$ и $\Lambda''$ близком к $\Lambda$ получаем п. 1 (сначала выбираются $y_1$ и $\Lambda''$, затем $s_1$).
2. $\partial_{y_a}\varphi(0,\theta,0)=\langle\nabla u_m(\omega(\theta)),e_a(\theta)\rangle=0$. Уменьшив $s_1$, по
   равномерной непрерывности получим $|\partial_y\varphi(s,\theta,0)|<\lambda_Hy_1/16$ при $|s|<s_1$,
   $\theta\in\overline{\Lambda''}$. Для $g(y)=\varphi(s,\theta,y)$ по п. 1 и формуле Тейлора
   $g(y)\ge g(0)+\langle\nabla g(0),y\rangle+\frac{\lambda_H}4|y|^2$, поэтому при $y_1/2\le|y|<y_1$
   $g(y)-g(0)\ge|y|\big(\frac{\lambda_H}4\cdot\frac{y_1}2-\frac{\lambda_Hy_1}{16}\big)>0$. Значит, минимум $g$ на замкнутом
   шаре $|y|\le y_1/2$ достигается внутри — это критическая точка $y^*$. Строгая выпуклость $g$ на
   выпуклом шаре $|y|<y_1$ даёт: критическая точка там единственна и является глобальным минимумом.
3. В точке $(s_0,\theta_0,y^*(s_0,\theta_0))$ матрица $\partial_y^2\varphi$ обратима; по аналитической теореме о
   неявной функции (из [002], (F1), применённой к $(s,\theta,y)\mapsto(s,\theta,\partial_y\varphi)$) решение
   $\partial_y\varphi=0$ около неё аналитично и по непрерывности остаётся в шаре $|y|<y_1$; по
   единственности (п. 2) оно совпадает с $y^*$. При $s=0$ $\partial_y\varphi(0,\theta,0)=0$, так что
   $y^*(0,\theta)=0$. $\square$

### 3. Свойства определений и лемма K2

**3.1. Каноничность.** При $s\ne0$ и $\xi=sy\in N_\theta$ по (1.1)
$\partial_{y_a}\big[U(s\omega+\xi)\big]=s\langle\nabla U(s\omega+\xi),e_a\rangle=s^m\partial_{y_a}\varphi$, так что критические
точки сужения $U$ на слой $s\omega+N_\theta$ (в шаре $|\xi|<y_1|s|$) — это критические точки $\varphi(s,\theta,\cdot)$.
Слой и шар зависят только от точки $\omega\in\Sigma$, а не от рамки; критическая точка единственна.
Поэтому $R$ и все $g_k$ — функции на $\Sigma$, не зависящие от рамки и параметризации (критическая
точка из меньшего шара лежит и в большем). Номер $j$ не зависит от выбора дуги на связной
компоненте по теореме единственности для аналитических функций на связной аналитической кривой.

**3.2. Ряд и $\hat G$.** $R$ аналитична, $R(0,\theta)=u_m(\omega(\theta))=0$. Равенство
$R=\sum_{i\ge1}s^ig_{m+i}$ верно в круге сходимости ряда по $s$ (не обязательно при всех $|s|<s_1$). Если
$j<\infty$, то $\partial_s^iR(0,\theta)=0$ при $i<j-m$, и по формуле Тейлора с интегральным остатком
$$R(s,\theta)=s^{j-m}\hat G(s,\theta),\qquad\hat G(s,\theta)=\int_0^1\frac{(1-\tau)^{j-m-1}}{(j-m-1)!}\,\partial_s^{j-m}R(\tau s,\theta)\,d\tau,$$
$\hat G$ аналитична, $\hat G(0,\theta)=g_j(\theta)=G(\theta)$. Так как $j\ge m+1$, $c=\frac{j-m+2}2\ge\frac32$.

**3.3. Первые члены.** $\varphi=\frac12y^{\mathsf T}Hy+O(|y|^3)+s\,u_{m+1}(\omega+y)+s^2u_{m+2}(\omega+y)+O(s^3)$, где
$u_k(\omega+y)$ понимается как $u_k(\omega+\sum y_ae_a)$. Из $\partial_y\varphi=0$: $y^*=-sH^{-1}b_1+O(s^2)$, и
$R=s\,u_{m+1}(\omega)+s^2\big(u_{m+2}(\omega)-\frac12b_1^{\mathsf T}H^{-1}b_1\big)+O(s^3)$. Почему $G$ определяется струёй $j^jU$: по лемме K1, п. 2, $R(s,\theta)=\min_{|y|<y_1}\varphi(s,\theta,y)$. Если $\tilde U$
имеет ту же струю $j^KU$ ($K\ge m$), то $\tilde\varphi-\varphi=O(s^{K+1-m})$ равномерно на шаре $|y|\le y_1$ (при общих для
$U$ и $\tilde U$ константах леммы K1, которые можно уменьшать), и так как $|\min f-\min g|\le\sup|f-g|$,
$\tilde R-R=O(s^{K+1-m})$. Значит, $g_k$ при $k\le K$ у $U$ и $\tilde U$ одинаковы, и $G=g_j$ определяется
струёй $j^jU$. [Эксперимент: формула для $g_{m+2}$ проверена R20 на 7 случайных примерах, точная
арифметика.]

**3.4. Чётность.** Пусть $u_m\ge0$ (так что $m$ чётно, $\Sigma=-\Sigma$, $N_{-\omega}=N_\omega$). При $s<0$ точка
$s(\omega+y^*(s,\omega))=|s|\big(-\omega\big)+s\,y^*$ лежит в слое через $|s|(-\omega)$ и критична там, поэтому
совпадает с $|s|(-\omega)+\eta^*(|s|,-\omega)$; по (1.1) $s^mR(s,\omega)=|s|^mR(|s|,-\omega)$, то есть
$R(-t,\omega)=R(t,-\omega)$ при $t>0$, и $g_k(-\omega)=(-1)^{k-m}g_k(\omega)=(-1)^kg_k(\omega)$. При нечётном $j$
функция $G$ нечётна на $\Sigma_0\cup(-\Sigma_0)$ и принимает там отрицательные значения.

**3.5. $j=\infty$.** Если $R\equiv0$ (то есть все $g_k=0$; аналитичность), то дно $\{s\omega(\theta)+\eta^*(s,\theta)\}$
состоит из критических точек $U$: при $d=0$ — следствие K0′(b), при $d=1$ — то же рассуждение
(на дне $\nabla U\perp N_\theta$ по 3.1, а производные $U$ вдоль дна по $s$ и $\theta$ — производные
$U_{\rm red}\equiv0$; при этом для $\Psi(s,\theta)=s\omega+\eta^*$ имеем $\Psi_s=\omega+O(s)$, $\Psi_\theta=s\omega'+O(s^2)$, а
$N_\theta\perp\operatorname{span}(\omega,\omega')$, так что при малых $s>0$ $\operatorname{span}(\Psi_s,\Psi_\theta)+N_\theta=\mathbb R^n$ и $\nabla U=0$; при $n=3$ это и предложение K4(b)). Поэтому у изолированной критической точки
$j<\infty$ на каждой компоненте.

**Лемма K2 (нормальная форма).** Пусть $j<\infty$. Положим
$$M(s,\theta,\tau):=\int_0^1(1-\lambda)\,\partial_y^2\varphi\big(s,\theta,y^*(s,\theta)+\lambda\tau\big)\,d\lambda,\qquad
\tilde F(\varsigma,\theta,e):=\hat G(\varsigma^2,\theta)+e^{\mathsf T}M\big(\varsigma^2,\theta,\varsigma^{j-m}e\big)\,e .$$
Тогда $\tilde F$ аналитична на $\{|\varsigma|<s_1^{1/2},\ \theta\in\Lambda'',\ |\varsigma^{j-m}e|<y_1/2\}$, $M\succeq\frac{\lambda_H}4I$,
$M(0,\theta,0)=\frac12H(\theta)$,
$$\tilde F(0,\theta,e)=G(\theta)+\tfrac12e^{\mathsf T}H(\theta)e, \tag{3.1}$$
и при $0<s<s_1$, $\theta\in\Lambda''$, $|s^{c-1}e|<y_1/2$
$$U\Big(s\omega(\theta)+\eta^*(s,\theta)+s^c\sum_ae_ae_a(\theta)\Big)=s^j\,\tilde F\big(s^{1/2},\theta,e\big). \tag{3.2}$$

*Доказательство.* $M$ определена при $|y^*|<y_1/2$, $|\tau|<y_1/2$ (отрезок $[y^*,y^*+\tau]$ лежит в шаре
$|y|<y_1$), аналитична как интеграл по компакту; $M\succeq\frac{\lambda_H}2\int_0^1(1-\lambda)d\lambda=\frac{\lambda_H}4$;
$M(0,\theta,0)=\frac12\partial_y^2\varphi(0,\theta,0)=\frac12H$. При $\varsigma=0$ условие на $e$ снимается ($j-m\ge1$).
Точка в (3.2) равна $s\big(\omega+\sum(y^*_a+\tau_a)e_a\big)$ с $\tau=s^{c-1}e$, и по (1.1) значение $U$ в ней
равно $s^m\varphi(s,\theta,y^*+\tau)$. Формула Тейлора по $y$ в точке $y^*$, где $\partial_y\varphi=0$, даёт
$\varphi(s,\theta,y^*+\tau)=R+\tau^{\mathsf T}M\tau$. Так как $m+2c-2=j$ и $s^{c-1}=(s^{1/2})^{j-m}$,
$U=s^m\big(s^{j-m}\hat G+s^{2c-2}e^{\mathsf T}Me\big)=s^j\tilde F(s^{1/2},\theta,e)$. $\square$

[Эксперимент: (3.2) проверено R20 в 12 точках примера теоремы B (mpmath, 40 знаков), невязка
$\le10^{-38}$.]

### 4. Доказательство теоремы K0

Применим следствие 2 [007] в ортонормированных координатах $q=x\omega^*+\sum_ay_ae_a$ с
$\gamma(x):=\eta^*(x)=x\,y^*(x)$ (в координатах $y$), весами $c_a=c$, $\beta=j$, $N=2$.

1. *Кривая.* $\gamma$ аналитична на $(-s_1,s_1)$, $\gamma=O(x^2)$ ($y^*(0)=0$), $\gamma'=y^*+xy^{*\prime}\to0$,
   $x|\gamma''|=x|2y^{*\prime}+xy^{*\prime\prime}|\to0$.
2. *(F).* По (3.2) $U(x,\gamma(x)+x^cb)=x^j\tilde F(x^{1/2},b)$ при $x<s_1$, $|x^{c-1}b|<y_1/2$. Возьмём $r_0=1$,
   $\sigma_0\in(0,s_1^{1/2})$ с $\sigma_0^{j-m}<y_1/2$ и $s_0:=\sigma_0^2$. Тогда $F:=\tilde F$ аналитична в окрестности
   $[0,\sigma_0]\times\overline{B_1}$ (включая $\varsigma<0$), поэтому $F$, $\nabla_bF$ непрерывны, а
   $\sup_{|b|\le1}|\varsigma\partial_\varsigma F|\le\varsigma\sup|\partial_\varsigma F|\to0$.
3. *(V).* По (3.1) $F_0(b)=g_j(\omega^*)+\frac12b^{\mathsf T}Hb$: $F_0(0)<0$, $\nabla F_0(0)=0$, $\nabla^2F_0(0)=H\succ0$,
   $C=cI$, $CH+HC=2cH\succ0$. Это условия следствия 1 [007], и оно даёт $(V_1)$ с
   $\lambda_0=\lambda_{\min}(H)/4$.

Следствие 2 [007] (после уменьшения $s_0$, чтобы образ лежал в шаре аналитичности) даёт класс (GT3)
с прямой картой $\Phi(x,u)=(x,\gamma(x)+u)$, $u=x^cb$; теорема 2 [007], пп. 3–4, даёт траекторию с
указанными оценками ($j\ge3>2$). $\square$

### 5. Доказательство следствия K0′

Так как $u_m\ge0$, в каждой $\omega\in\Sigma$ выполнено $\nabla u_m(\omega)=0$, и (S) с $d=0$ выполнено;
константы $s_1,y_1$ леммы K1 берём общими для конечного $\Sigma$. При $\nabla u_m(\omega)=0$
$\operatorname{Hess}_S(u_m|_S)(\omega)=D^2u_m(\omega)|_{\omega^\perp}$ (множитель Лагранжа нулевой).

**(a)** Пусть $C_\omega=\{q:\ \langle q,\omega\rangle>0,\ |q-\langle q,\omega\rangle\omega|<\frac{y_1}2\langle q,\omega\rangle\}$. Множество
$\mathcal S=S^{n-1}\setminus\bigcup_{\omega\in\Sigma}C_\omega$ компактно и не пересекает $\Sigma$, поэтому $u_m\ge c_{\mathcal S}>0$ на
$\mathcal S$ и $u_m(q)\ge c_{\mathcal S}|q|^m$ вне $\bigcup C_\omega$. Так как $|U-u_m|\le C'|q|^{m+1}$, вне $\bigcup C_\omega$ при
$0<|q|<c_{\mathcal S}/C'$ имеем $U>0$. Точка $q\in C_\omega$ записывается как $q=s(\omega+y)$,
$s=\langle q,\omega\rangle\in(0,|q|]$, $y\in\omega^\perp$, $|y|<y_1/2$, и по (1.1) и лемме K1, п. 2,
$U(q)=s^m\varphi(s,y)\ge s^mR_\omega(s)=s^{j(\omega)}\big(g_{j(\omega)}(\omega)+O(s)\big)>0$ при $0<s<s''$ ($s''$ общее для
конечного $\Sigma$). Итак, $U>0$ в проколотой окрестности нуля.

**(b)** Пусть $\gamma(s)=s(\omega+y^*(s))$. По 3.1 $\langle\nabla U(\gamma(s)),e_a\rangle=0$ при всех $a$, то есть
$\nabla U(\gamma(s))=\alpha(s)\omega$. Далее $\gamma'=\omega+y^*+sy^{*\prime}$, $\langle\omega,\gamma'\rangle=1$, и
$\frac d{ds}U(\gamma(s))=\alpha(s)$. Так как $U(\gamma(s))=s^mR_\omega(s)\equiv0$, то $\alpha\equiv0$. Точки
$\gamma(s)$ ненулевые ($\langle\gamma(s),\omega\rangle=s>0$) и стремятся к нулю.

**(c)** — теорема K0.

*«В частности».* Аналитическая $R_\omega$ либо $\equiv0$ на $(-s_1,s_1)$, либо имеет конечный порядок
$j(\omega)$ с $g_{j(\omega)}(\omega)\ne0$. Значит, каждая $\omega$ — ровно одного из типов: $R_\omega\equiv0$; старший
коэффициент $>0$; старший коэффициент $<0$. Изолированность исключает первый тип (b); если бы все
были второго типа, по (a) был бы минимум; значит, есть $\omega$ третьего типа, и работает (c). При
$\Sigma=\varnothing$ $u_m\ge c|q|^m$ на всём пространстве. $\square$

### 6. Геометрия конуса над дугой ($n=3$)

Пусть $\omega:(-\theta_0,\theta_0)\to\Sigma_0\subset S^2$ — натуральная параметризация аналитической дуги,
$\omega(0)=\omega^*$, $\ell=\omega'$, $n=\omega\times\ell$. Репер Дарбу кривой на единичной сфере:
$$\omega'=\ell,\qquad\ell'=-\omega+k_g\,n,\qquad n'=-k_g\,\ell, \tag{6.1}$$
$k_g(\theta)$ — геодезическая кривизна (аналитична). [$\ell'\perp\ell$, $\langle\ell',\omega\rangle=-1$;
$n'=\omega'\times\ell+\omega\times\ell'=k_g\,\omega\times n=-k_g\ell$.] Здесь $N_{\omega(\theta)}=\mathbb Rn(\theta)$, $p=1$,
$e_1=n$, $H(\theta)=h_n(\theta):=D^2u_m(\omega(\theta))(n,n)$.

**Лемма K3 (трубка конуса).** Пусть $\Pi(s,\theta,\eta)=s\,\omega(\theta)+\eta\,n(\theta)$. Найдутся
$\theta_1\in(0,\theta_0)$ и $t_1\in\big(0,1/(2\bar k_g+1)\big)$, $\bar k_g=\max_{|\theta|\le\theta_1}|k_g|$, такие, что $\Pi$ —
аналитический диффеоморфизм $\mathcal P=\{s>0,\ |\theta|<\theta_1,\ |\eta|<t_1s\}$ на открытое множество в
$\mathbb R^3\setminus0$, и
$$|\Pi|^2=s^2+\eta^2,\qquad\Pi_s=\omega,\quad\Pi_\theta=(s-k_g\eta)\,\ell,\quad\Pi_\eta=n,\qquad\nabla s=\omega(\theta). \tag{6.2}$$
То же верно для замкнутой кривой $\Sigma_0$ с периодическим $\theta$ (рассуждение то же).

*Доказательство.* Производные — из (6.1); они попарно ортогональны и ненулевые
($s-k_g\eta\ge s(1-\bar k_gt_1)>0$), так что $\Pi$ — локальный диффеоморфизм; для ортогональной системы
координат $\nabla s=\Pi_s/|\Pi_s|^2=\omega$; $|\Pi|^2=s^2+\eta^2$, так как $\omega\perp n$. Инъективность:
$\Pi=s\sqrt{1+t^2}\,E(\theta,t)$, $t=\eta/s$, $E=(\omega+tn)/\sqrt{1+t^2}\in S^2$. $E$ аналитично, $dE(\theta,0)$ имеет
столбцы $\ell,n$ (ранг 2), а на компакте $[-\theta_1',\theta_1']\times\{0\}$ $E$ инъективно (вложенная дуга).
Локальный гомеоморфизм, инъективный на компакте, инъективен в его окрестности; поэтому при малых
$\theta_1,t_1$ $E$ инъективно. Из $\Pi(s,\theta,\eta)=\Pi(s',\theta',\eta')$ следуют равенство направлений,
$(\theta,\eta/s)=(\theta',\eta'/s')$, и равенство норм, $s=s'$. Образ открыт. $\square$

*Обозначение.* При $n=3$, $d=1$ вектор $\eta^*\in N_\theta$ из (S) равен $\eta^*n(\theta)$; здесь и далее (в §6–§11 и в
предложении K4) $\eta^*(s,\theta)$ — этот скалярный коэффициент.

**Карта с дном.** $\Psi(s,\theta,\zeta):=\Pi\big(s,\theta,\eta^*(s,\theta)+\zeta\big)=s\omega(\theta)+\eta\,n(\theta)$,
$\eta:=\eta^*+\zeta$. Так как $\eta^*=sy^*=O(s^2)$, при малых $s$ и $|\zeta|<r_0s^c$ точка лежит в $\mathcal P$.
Функция $s$ на $\mathbb R^3$ та же, что для $\Pi$, поэтому $\nabla s=\omega(\theta)$. По (3.2)
$$U\big(\Psi(s,\theta,s^ce)\big)=s^j\tilde F(s^{1/2},\theta,e),\qquad\tilde F(0,\theta,e)=G(\theta)+\tfrac12h_n(\theta)e^2. \tag{6.3}$$
Координатные поля (проверено символьно с произвольными $k_g(\theta)$, $\eta^*(s,\theta)$: `frame_check.py`;
независимо R22):
$$\Psi_s=\omega+\eta^*_s\,n,\qquad\Psi_\theta=s(1-\epsilon)\,\ell+\eta^*_\theta\,n,\qquad\Psi_\zeta=n,\qquad\epsilon:=\frac{k_g(\theta)\eta}s. \tag{6.4}$$
**Малые величины.** На $\{0<s<s_0,\ |\theta|\le r_0,\ |\zeta|\le r_0s^c\}$ ($r_0\le\theta_1/2$) равномерно при $s\to0$
$$\epsilon,\quad s\partial_s\epsilon=k_g\eta^*_s-\epsilon,\quad\partial_\theta\epsilon=\frac{k_g'\eta+k_g\eta^*_\theta}s,\quad\eta^*_s,\quad\frac{\eta^*_\theta}s,\quad s\eta^*_{ss},\quad\eta^*_{s\theta},\quad\frac{\eta^*_{\theta\theta}}s\ \longrightarrow\ 0, \tag{6.5}$$
так как $\eta^*=sy^*$, $y^*$ аналитична, $y^*(0,\cdot)=0$ (отсюда $\eta^*=O(s^2)$, $\eta^*_s=O(s)$,
$\eta^*_\theta=O(s^2)$, $\eta^*_{ss}=O(1)$, $\eta^*_{s\theta}=O(s)$, $\eta^*_{\theta\theta}=O(s^2)$), а $|\eta|\le Cs^2+r_0s^c$, $c>1$.

### 7. Доказательство теоремы K1

*Карта.* В полярных координатах развёртки $X=s\cos\theta$, $Y_d=s\sin\theta$ ($X>0$, $|Y_d/X|<r_0$):
$$\Phi(X,Y_d,\zeta)=\Psi\Big(\sqrt{X^2+Y_d^2},\ \arctan\frac{Y_d}X,\ \zeta\Big),\qquad x=X,\ u=(Y_d,\zeta),\ b=(t,e)=\Big(\frac{Y_d}X,\frac\zeta{X^c}\Big). \tag{7.1}$$
Обозначим $r=\sqrt{X^2+Y_d^2}$, $\mathrm c=\cos\theta$, $\mathrm s=\sin\theta$,
$\nu_X=\mathrm c\,\eta^*_s-\mathrm s\,\eta^*_\theta/r$, $\nu_Y=\mathrm s\,\eta^*_s+\mathrm c\,\eta^*_\theta/r$. Формулы (символьно с
произвольными $k_g$, $\eta^*$: `frame_check.py`; независимо R22, `frames.py`):
$$\Phi_X=\mathrm c\,\omega-\mathrm s(1-\epsilon)\ell+\nu_Xn,\quad\Phi_{Y_d}=\mathrm s\,\omega+\mathrm c(1-\epsilon)\ell+\nu_Yn,\quad\Phi_\zeta=n,\quad
B_{XY_d}=\mathrm s\mathrm c\big(1-(1-\epsilon)^2\big)+\nu_X\nu_Y,\quad B_{X\zeta}=\nu_X,$$
$$\Phi_{XX}=\frac{\mathrm s^2\epsilon}r\,\omega+\Big(-\frac{\mathrm s\mathrm c\,\epsilon}r+\mathrm s\,\partial_X\epsilon+\frac{\nu_Xk_g\mathrm s}r\Big)\ell+\Big(\frac{\mathrm s^2(1-\epsilon)k_g}r+\partial_X\nu_X\Big)n,$$
$$\Phi_{XY_d}=-\frac{\mathrm s\mathrm c\,\epsilon}r\,\omega+\Big(\frac{\mathrm c^2\epsilon}r+\mathrm s\,\partial_{Y_d}\epsilon-\frac{\nu_Xk_g\mathrm c}r\Big)\ell+\Big(-\frac{\mathrm s\mathrm c(1-\epsilon)k_g}r+\partial_{Y_d}\nu_X\Big)n,\qquad\Phi_{X\zeta}=\frac{\mathrm s\,k_g}r\,\ell .$$

*Выбор констант.* $r_0\le\min(\frac14,\theta_1/2)$, $[-r_0,r_0]\subset\Lambda''$ (там определена $\tilde F$),
$\sigma_0<s_1^{1/2}$ с $\sigma_0^{j-m}r_0<y_1/2$, и $s_0\le\min(1,\sigma_0^2/2)$ (тогда $r^{1/2}<\sigma_0$) настолько мало, что
образ $\mathcal N$ лежит в $\mathcal P$ (лемма K3) и в шаре аналитичности $U$. В
$\mathcal N=\{0<X<s_0,\ |b|<r_0\}$: $|\mathrm s|\le|t|\le|b|$, $X\le r\le\frac{\sqrt{17}}4X$, и величины $\epsilon$, $\nu_X$, $\nu_Y$,
$r\partial_X\epsilon$, $r\partial_{Y_d}\epsilon$, $r\partial_X\nu_X$, $r\partial_{Y_d}\nu_X$ стремятся к нулю равномерно при $X\to0$ (они
выражаются через (6.5) и $\partial_Xr=\mathrm c$, $\partial_X\theta=-\mathrm s/r$, $\partial_{Y_d}r=\mathrm s$, $\partial_{Y_d}\theta=\mathrm c/r$).
Пусть $\varpi_1(X)\to0$ — сумма их супремумов по $\{X'\le X\}$; $s_0$ таково, что $\varpi_1\le\frac14$.

- $(\Phi0)$: $\Phi$ — композиция диффеоморфизма сектора $(X,Y_d)\mapsto(r,\theta)$ и $\Psi$ (лемма K3);
  $|\Phi|^2=r^2+\eta^2$, так что $X\le|\Phi|\le2r\le3X$.
- $(\Phi1)$: элементы $B-I$ в репере $(\omega,\ell,n)$ ограничены
  $3|\epsilon|+2(|\nu_X|+|\nu_Y|)+(|\nu_X|+|\nu_Y|)^2\to0$, так что $\|B-I\|\le\frac12$ при малом $s_0$, и
  $|B_{xu}|\le3|\epsilon|+|\nu_X|(1+|\nu_Y|)\le5\varpi_1\le\varpi$ (функция $\varpi$ — ниже, общая для $(\Phi1)$–$(\Phi3)$).
- $(\Phi2)$: $X|\Phi_{XX}|\le\mathrm s^2(1+|\epsilon|)\bar k_g+|\epsilon|(\mathrm s^2+|\mathrm s|)+r|\partial_X\epsilon|+|\nu_X|\bar k_g+r|\partial_X\nu_X|\le\frac54\bar k_g|b|^2+4\varpi_1(1+\bar k_g)$.
- $(\Phi3)$: для $w\perp\Phi_X$, $w=\zeta_X\Phi_X+\zeta_Y\Phi_{Y_d}+\zeta_\zeta\Phi_\zeta$, имеем $|\zeta|\le\sqrt2|w|$ ($B\succeq\frac12I$) и
  $D_wY=\zeta_X\Phi_{XX}+\zeta_Y\Phi_{XY_d}+\zeta_\zeta\Phi_{X\zeta}$. Из формул
  $X|\Phi_{XY_d}|\le\frac54|\mathrm s|\bar k_g+4\varpi_1(1+\bar k_g)$, $X|\Phi_{X\zeta}|\le\bar k_g|\mathrm s|$. Так как
  $|\zeta_X|+|\zeta_Y|+|\zeta_\zeta|\le\sqrt3|\zeta|\le\sqrt6|w|$,
  $X|\langle w,D_wY\rangle|\le\sqrt6|w|^2\big(\frac54\bar k_g|b|^2+\frac54\bar k_g|b|+\bar k_g|b|+8\varpi_1(1+\bar k_g)\big)\le(C_1|b|+\varpi)|w|^2$
  с $C_1=7\bar k_g$ ($|b|^2\le\frac14|b|$, $\sqrt6\cdot\frac{41}{16}<7$) и $\varpi=20(1+\bar k_g)\varpi_1$; те же $C_1$, $\varpi$
  годятся в $(\Phi2)$.
- (F): по (6.3) с $s=r=X\sqrt{1+t^2}$, $\theta=\arctan t$, $\zeta/r^c=e(1+t^2)^{-c/2}$:
  $U\circ\Phi=X^jF(X^{1/2},t,e)$,
  $$F(\varsigma,t,e)=(1+t^2)^{j/2}\,\tilde F\big(\varsigma(1+t^2)^{1/4},\arctan t,\ e(1+t^2)^{-c/2}\big),$$
  аналитична в окрестности $[0,\sigma_0']\times\overline{B_{r_0}}$ при $\sigma_0'=s_0^{1/2}$.
- $(V_1)$: $F_0(t,e)=(1+t^2)^{j/2}\big[G(\arctan t)+\frac12h_n(\arctan t)(1+t^2)^{-c}e^2\big]$. Так как
  $(1+t^2)^{j/2}=1+\frac j2t^2+O(t^4)$ и $G(\arctan t)=G(0)+\frac12G''(0)t^2+O(t^3)$: $F_0(0)=G(0)<0$, $\nabla F_0(0)=0$,
  $\nabla^2F_0(0)=\operatorname{diag}\big(G''(0)+jG(0),\ h_n(0)\big)\succ0$ (смешанная производная равна нулю, так как $F_0$
  зависит от $e$ через $e^2$). Матрица диагональна, $C=\operatorname{diag}(1,c)$; по следствию 1 [007] —
  $(V_1)$.

Карта кривая ($C_1>0$ при $\bar k_g>0$); случай $(V_1)$ теоремы 2 [007] это допускает. Теорема 2 [007]
даёт асимптотическую траекторию. ($G''(0)>0$ здесь не предполагается отдельно: оно следует из
$G''+jG>0$ и $G<0$.) $\square$

### 8. Лемма 2′

**Лемма 2′.** В обозначениях теоремы A [007] пусть выполнены (D1) и (L0) [007], а на
$D_\sigma=\{q\in\overline D:\ q\ne0,\ \rho(q)<\sigma\}$ — (L1) [007] и

- **(L2′)** есть функция $\mathcal Q:D_\sigma\to[0,\infty)$ и числа $\varepsilon_0\in[0,\frac12]$, $\varepsilon_1\ge0$,
  $\mu\in(0,\beta]$ с $|W-\mathcal Q|\le\varepsilon_0\delta\rho^\beta$ и $\beta W-\rho\,YW\ge\mu\mathcal Q-\varepsilon_1\delta\rho^\beta$;
- **(L3′)** есть числа $\theta_1,\theta_2,\theta_3\ge0$, $\gamma_1',\gamma_2'\ge0$ такие, что для всех $q\in D_\sigma$ и $w\perp Y(q)$:
  $|\langle\nabla\rho-Y/h,w\rangle|\le\big(\theta_1+\gamma_1'\sqrt{\mathcal Q/\rho^\beta}\big)|w|$,
  $\rho|\langle\nabla_YY,w\rangle|\le\big(\theta_2+\gamma_2'\sqrt{\mathcal Q/\rho^\beta}\big)|w|$,
  $\rho\langle w,D_wY\rangle\ge-\theta_3|w|^2$.

Тогда выполнено (D4) и

1. если $4\sqrt\delta\,(\theta_1+2\gamma_1'\sqrt\delta)\le\sqrt{a_1/h_1}$, то в точках $\overline\Omega$ с $q\ne0$, $\rho(q)<\sigma$
   $$-\Big(\sqrt{2(a_3+\delta/2)/h_0}+\tfrac12\sqrt{a_1/h_1}\Big)\rho^{\beta/2}\le\dot\rho\le-\tfrac12\sqrt{a_1/h_1}\,\rho^{\beta/2}<0,$$
   в частности, выполнено (A4);
2. если $\Gamma'^2\le\beta\mu$, где $\Gamma':=\sqrt2\big[(a_2+\beta\delta)\sqrt{h_1/a_1}\,\gamma_1'+\sqrt{2a_3/h_0}\,\gamma_2'\big]$, то
   в каждой точке множества из (A5)
   $$\frac\rho\lambda\,\Xi\ \ge\ \delta\rho^\beta\Big[\frac\mu2(1-\varepsilon_0)-\varepsilon_1-\frac{L_1\theta_1+L_2\theta_2}{\sqrt\delta}-4\theta_3\Big] \tag{8.1}$$
   с $L_1=2(a_2+\frac{\beta a_1}2)\sqrt{h_1/a_1}$, $L_2=2\sqrt{2a_3/h_0}$ из (3.1) [007].

*Доказательство.*

1. (D4): $A(r)-\delta r^\beta\ge(a_1-\delta)r^\beta\ge\frac{a_1}2r^\beta>0$ по (L0).
2. *Точки $\overline\Omega$ с $q\ne0$, $\rho<\sigma$.* Тогда $q\in D_\sigma$, и по шагу 0 теоремы A [007] $p<0$,
   $V\le\delta\rho^\beta$. Так как $\mathcal Q\ge0$, $W\ge\mathcal Q-\varepsilon_0\delta\rho^\beta\ge-\frac12\delta\rho^\beta$, поэтому
   $K_\perp=V-W\le\frac32\delta\rho^\beta$ и $|v_\perp|\le2\sqrt\delta\rho^{\beta/2}$; $\mathcal Q\le W+\frac12\delta\rho^\beta\le V+\frac12\delta\rho^\beta\le\frac32\delta\rho^\beta$
   ($W\le V$, так как $K_\perp\ge0$), так что $\sqrt{\mathcal Q/\rho^\beta}\le2\sqrt\delta$. По (0.1) [007]
   $\lambda^2h/2=A-V\in\big[(a_1-\delta)\rho^\beta,(a_3+\frac\delta2)\rho^\beta\big]$, откуда
   $\sqrt{a_1/h_1}\rho^{\beta/2}\le\lambda\le\sqrt{2(a_3+\delta/2)/h_0}\,\rho^{\beta/2}$. По (1.1) [007]
   $\dot\rho=-\lambda+\langle\nabla\rho-Y/h,v_\perp\rangle$, и по (L3′) с $w=v_\perp$
   $|\langle\nabla\rho-Y/h,v_\perp\rangle|\le(\theta_1+2\gamma_1'\sqrt\delta)\cdot2\sqrt\delta\rho^{\beta/2}\le\frac12\sqrt{a_1/h_1}\rho^{\beta/2}$. Это п. 1.
3. *Точка из (A5).* $V=\delta\rho^\beta$, $K:=K_\perp=\delta\rho^\beta-W\in[0,\frac32\delta\rho^\beta]$,
   $\lambda^2h/2=A-\delta\rho^\beta\in[\frac{a_1}2\rho^\beta,a_3\rho^\beta]$, так что
   $\sqrt{a_1/h_1}\rho^{\beta/2}\le\lambda\le\sqrt{2a_3/h_0}\rho^{\beta/2}$. В (1.3) [007] главный член
   $\beta\delta\rho^\beta-\rho\,YW=\beta K+(\beta W-\rho\,YW)\ge\beta K+\mu\mathcal Q-\varepsilon_1\delta\rho^\beta$.
4. $|T_1|\le\frac\rho\lambda(a_2+\beta\delta)\rho^{\beta-1}\big(\theta_1+\gamma_1'\sqrt{\mathcal Q/\rho^\beta}\big)\sqrt{2K}\le(a_2+\beta\delta)\sqrt{h_1/a_1}\big[\theta_1\rho^{\beta/2}\sqrt{2K}+\gamma_1'\sqrt{2K\mathcal Q}\big]$
   $\le L_1\theta_1\sqrt\delta\rho^\beta+\sqrt2(a_2+\beta\delta)\sqrt{h_1/a_1}\,\gamma_1'\sqrt{K\mathcal Q}$ (использованы $\sqrt{2K}\le2\sqrt\delta\rho^{\beta/2}$ и
   $\delta\le a_1/2$, $\theta_1\ge0$).
5. $|T_2|=\lambda\rho|\langle v_\perp,\nabla_YY\rangle|\le\lambda\big(\theta_2+\gamma_2'\sqrt{\mathcal Q/\rho^\beta}\big)\sqrt{2K}\le L_2\theta_2\sqrt\delta\rho^\beta+\sqrt2\sqrt{2a_3/h_0}\,\gamma_2'\sqrt{K\mathcal Q}$.
6. $T_3\ge-\theta_3|v_\perp|^2=-2\theta_3K\ge-4\theta_3\delta\rho^\beta$ ($\theta_3\ge0$; на деле даже $-3\theta_3\delta\rho^\beta$).
7. Складывая: $\frac\rho\lambda\Xi\ge\beta K+\mu\mathcal Q-\Gamma'\sqrt{K\mathcal Q}-\big[\varepsilon_1+\frac{L_1\theta_1+L_2\theta_2}{\sqrt\delta}+4\theta_3\big]\delta\rho^\beta$.
   При $\mu\le\beta$ имеем $\Gamma'^2\le\beta\mu\le\mu(2\beta-\mu)=4(\beta-\frac\mu2)\frac\mu2$, поэтому по неравенству о
   среднем арифметическом и геометрическом $(\beta-\frac\mu2)K+\frac\mu2\mathcal Q\ge2\sqrt{(\beta-\frac\mu2)\frac\mu2K\mathcal Q}\ge\Gamma'\sqrt{K\mathcal Q}$,
   то есть $\beta K+\mu\mathcal Q-\Gamma'\sqrt{K\mathcal Q}\ge\frac\mu2(K+\mathcal Q)$. Наконец
   $K+\mathcal Q\ge K+W-\varepsilon_0\delta\rho^\beta=(1-\varepsilon_0)\delta\rho^\beta$. Это (8.1). $\square$

Лемма 2′ — аналог леммы 2 [007], а не её обобщение: она требует $\mathcal Q\ge0$, а лемма 2 допускает
$W\ge-\delta\rho^\beta$, так что подставить $\mathcal Q=W$ при $\gamma_i'=0$ нельзя ($\mathcal Q=\max(W,0)$ дало бы $\varepsilon_0=1$).
Новое — члены $\gamma_i'\sqrt{K\mathcal Q}$: перекрёстные члены, линейные по поперечному смещению, гасятся
неравенством о средних, если они малы по сравнению с $\sqrt{\beta\mu}$.

### 9. Доказательство теоремы 2′

Повторяем доказательство теоремы 2 [007] (§4 там) в случае $(V_1)$, заменив лемму 2 на лемму 2′.
Матрица $B$ в [007] используется только в шаге 4 ((L1): $h=B_{xx}$; (L3): $\theta_1\le2\sqrt2\bar\omega$) и в
шаге 6, п. 1 ($|\partial_x\Phi|\le\sqrt{3/2}$); все эти места заменены условиями $(\Phi1')$, $(\Phi2')$ (проверено
R21, R22).

1. *Шаг 1 [007] дословно:* открытое множество $\mathcal O:=\Phi(\mathcal N)$ (в [007] — $G$), $\rho\in C^2(\mathcal O)$,
   $Y\in C^1(\mathcal O)$, $Y\rho=1$, $A(r)=a_0r^\beta$, $\sigma_0=s_0$, и (4.1), (4.2) [007]:
   $W\circ\Phi=x^\beta(F-F_0(0))$, $\beta W-\rho\,YW=x^\beta\big[\sum_ic_ib_i\partial_{b_i}F-\frac\varsigma N\partial_\varsigma F\big]$. Используются
   только $(\Phi0)$, $\rho=x\circ\Phi^{-1}$, $Y\circ\Phi=\partial_x\Phi$, $b_i=u_ix^{-c_i}$ и (F).
2. *Шаг 2 [007], случай $(V_1)$:* $\delta\le\min(a_0/2,\lambda_0r_1^2/16)$, $\Omega_b'=B_{2\sqrt{\delta/\lambda_0}}\subset B_{r_1/2}$,
   $R_b=2\sqrt{\delta/\lambda_0}$; (i) $Q\ge0$ и (iii) неравенство Эйлера с $\mu$ на $\overline{\Omega_b'}$ — по $(V_1')$;
   (ii) $Q\ge4\delta$ на $\partial\Omega_b'$, $\kappa'=3\delta$.
3. *Шаг 3 [007] дословно:* $\chi(\varsigma)$, $\bar\chi$, порог $\sigma_*<s_0$ по $x$ с $\bar\chi(\sigma_*^{1/N})<\min(\delta,\kappa'/2)$,
   $\mathcal D=\{x<\sigma_*,\ b\in\Omega_b',\ F-F_0(0)<\delta\}$, $D=\Phi(\mathcal D)$; (D1)–(D3) проверяются там только
   через $(\Phi0)$, (F), $\overline{\Omega_b'}\subset B_{r_0}$ и свойство (ii) шага 2. Ниже $\chi:=\bar\chi(\sigma_*^{1/N})$,
   $\bar\varpi:=\sup_{x<\sigma_*}\varpi(x)$; $\sigma_*$ ещё уменьшится.
4. *Константы леммы 2′ на $D_{\sigma_*}$.* Каждая точка $D_{\sigma_*}$ — это $\Phi(x,u)$ с $x<\sigma_*$, $b\in\overline{\Omega_b'}$,
   $F-F_0(0)\le\delta$ (рассуждение из (D2) [007]).
   - (L0): $a_1=a_3=a_0$, $a_2=\beta a_0$, $\delta\le a_0/2$. (L1): $h_0=\frac12$, $h_1=\frac32$ по $(\Phi1')$.
   - (L2′): $\mathcal Q:=x^\beta Q(b)\ge0$ (так как $Q\ge\lambda_0|b|^2$ на $B_{r_1}\supset\overline{\Omega_b'}$).
     $|W-\mathcal Q|=x^\beta|F(\varsigma,b)-F_0(b)|\le\chi x^\beta$: $\varepsilon_0=\chi/\delta$. По (4.2) [007], неравенству
     Коши–Буняковского $|\sum_ic_ib_i(\partial_{b_i}F-\partial_{b_i}Q)|\le c_{\max}R_b\chi$ и неравенству Эйлера
     $\beta W-\rho\,YW\ge x^\beta\big[\mu Q-c_{\max}R_b\chi-\chi/N\big]$: $\varepsilon_1=(c_{\max}R_b+1/N)\chi/\delta$.
   - (L3′): на $\overline{\Omega_b'}$ $|b|\le\sqrt{Q/\lambda_0}=\sqrt{\mathcal Q/(\lambda_0\rho^\beta)}$ ($\rho=x$). По $(\Phi2')$: $\theta_1=\bar\varpi$,
     $\gamma_1'=\gamma_1/\sqrt{\lambda_0}$. Так как $\nabla_YY=\partial_x^2\Phi$ (поток $Y$ в карте — сдвиг по $x$),
     $\theta_2=C_1R_b^2+\bar\varpi$, $\gamma_2'=\gamma_2/\sqrt{\lambda_0}$. По $(\Phi3)$: $\theta_3=C_1R_b+\bar\varpi$. Все $\ge0$.
   - $\Gamma'\le\Gamma_*$: при $\delta\le a_0/2$ $a_2+\beta\delta\le\frac32\beta a_0$, $\sqrt2\cdot\frac32\beta a_0\sqrt{3/(2a_0)}=\frac{3\sqrt3}2\beta\sqrt{a_0}$,
     $\sqrt2\sqrt{2a_0/(1/2)}=2\sqrt2\sqrt{a_0}$. По (U2) $\Gamma'^2\le\beta\mu$.
5. *Выбор $\delta$ и $\sigma_*$.* Здесь $L_1=3\beta\sqrt{3a_0/2}$, $L_2=4\sqrt{a_0}$. Члены, зависящие только от $\delta$:
   $\frac{L_2C_1R_b^2}{\sqrt\delta}+4C_1R_b=C_1\sqrt\delta\big(\frac{16\sqrt{a_0}}{\lambda_0}+\frac8{\sqrt{\lambda_0}}\big)$ и (для п. 1 леммы 2′)
   $8\gamma_1'\delta$. Пусть $\delta_*\le\min(a_0/2,\lambda_0r_1^2/16)$ таково, что при $\delta\le\delta_*$ первое $\le\mu/8$, а
   $8\gamma_1'\delta\le\frac12\sqrt{a_0/h_1}$. Для любого $\delta\in(0,\delta_*]$ выберем $\sigma_*$ так, чтобы
   $\varepsilon_0\le\frac14$, $\varepsilon_1\le\frac\mu{16}$, $\frac{(L_1+L_2)\bar\varpi}{\sqrt\delta}+4\bar\varpi\le\frac\mu{16}$ и
   $4\sqrt\delta\bar\varpi\le\frac12\sqrt{a_0/h_1}$ (все эти величины $\to0$ при $\sigma_*\to0$ и фиксированном $\delta$); уменьшив
   $\sigma_*$, считаем также $\sigma_*\le\sqrt\delta$ (все условия на $\sigma_*$ — оценки сверху; это нужно в теореме K2).
   Тогда условие п. 1 леммы 2′ выполнено, а скобка в (8.1) не меньше
   $\frac\mu2\cdot\frac34-\frac\mu{16}-\frac\mu8-\frac\mu{16}=\frac\mu8>0$.
6. Лемма 2′ даёт (D4), (A4), (A5); теорема A [007] — решение $(q(t),v(t))\in\overline\Omega$, $q(t)\ne0$,
   $q(t)\to0$, $v(t)\to0$. Как в шаге 6 [007], п. 3: $q(t)\in D_{\sigma_*}$, $q=\Phi(x,u)$, $x=\rho(q)$, и п. 1
   леммы 2′ даёт $-k_2x^{\beta/2}\le\dot x\le-k_1x^{\beta/2}$; как в п. 4 — $b(t)\in\overline{\Omega_b'}$, то есть
   $|b(t)|\le2\sqrt{\delta/\lambda_0}$. $\square$

### 10. Доказательство теоремы K2

**10.1. Карта.** Данные §6. При $\kappa\in(0,\frac12]$
$$\Phi(x,u,\zeta):=\Psi\big(x,\theta,\zeta\big),\quad\theta:=u\,x^{-\kappa};\qquad b=(\theta,e)=\big(u\,x^{-\kappa},\ \zeta\,x^{-c}\big),\quad\text{веса }(\kappa,c),\ N=2. \tag{10.1}$$
Срезы $\{x=\mathrm{const}\}$ — полярные ($s=x$), а $Y=\partial_x\Phi$ при постоянном $u$ поворачивает угол:
$\partial_x\theta=-\kappa\theta/x$. Обозначим $\nu:=\eta^*_s-\kappa\theta\eta^*_\theta/x$, $\epsilon=k_g\eta/x$. Формулы (символьно с
произвольными $k_g$, $\eta^*$: `frame_check.py`; независимо R22):
$$Y=\omega-\kappa\theta(1-\epsilon)\,\ell+\nu\,n,\qquad h=1+\kappa^2\theta^2(1-\epsilon)^2+\nu^2, \tag{10.2}$$
$$x\,\partial_x^2\Phi=-\kappa\theta\big[(1-\kappa)+\kappa\epsilon-x\partial_x\epsilon-\nu k_g\big]\ell+\kappa^2\theta^2(1-\epsilon)(-\omega+k_gn)+x\,\partial_x\nu\;n, \tag{10.3}$$
где $\partial_x$ — полная производная при постоянных $(u,\zeta)$, $x\partial_x\epsilon=-\kappa\theta k_g'\eta/x+k_g\nu-\epsilon$. Как поле в
координатах $(s,\theta,\zeta)$ карты $\Psi$: $Y=\omega-\kappa\theta(1-\epsilon)\ell+\nu n$ с $\epsilon=k_g(\eta^*+\zeta)/s$,
$\nu=\eta^*_s-\kappa\theta\eta^*_\theta/s$, и
$$\partial_\theta Y=\kappa\theta(1-\epsilon)\omega+\big[1-\kappa(1-\epsilon)+\kappa\theta\partial_\theta\epsilon-\nu k_g\big]\ell+\big[-\kappa\theta(1-\epsilon)k_g+\partial_\theta\nu\big]n,\quad
\partial_sY=\kappa\theta\,\partial_s\epsilon\,\ell+\partial_s\nu\,n,\quad\partial_\zeta Y=\frac{\kappa\theta k_g}s\,\ell. \tag{10.4}$$

**10.2. Проверка условий класса (GT3′).** Выберем $r_1$ (§10.2, п. 7), затем $r_0\in(r_1,\min(\theta_1/2,\frac14)]$ с
$[-r_0,r_0]\subset\Lambda''$, и $s_0$ так, что на $\mathcal N=\{0<x<s_0,\ |b|<r_0\}$: $|\epsilon|\le\frac14$, $|\nu|\le\frac14$,
$|\eta^*_s|+\frac43|\eta^*_\theta|/x\le1$, точки лежат в $\mathcal P$ (лемма K3), $s_0<s_1$ и
$s_0^{(j-m)/2}r_0<y_1/2$. Пусть $\varpi(x)$ — супремум по $\{x'\le x\}$ суммы модулей величин (6.5), $\nu$,
$x\partial_x\epsilon$, $x\partial_x\nu$, $\partial_\theta\nu$, $s\partial_s\nu$, умноженный на $10(1+\bar k_g)$; $\varpi\to0$ (так как $\nu=O(x)$,
$x\partial_x\nu=x\nu_s-\kappa\theta\nu_\theta=O(x)$, $\partial_\theta\nu=O(x)$, $s\partial_s\nu=O(x)$).

1. **$(\Phi0)$.** $\Phi=\Psi\circ L$, $L(x,u,\zeta)=(x,ux^{-\kappa},\zeta)$ — диффеоморфизм; $\Psi$ — диффеоморфизм на
   открытое множество (лемма K3 и сдвиг $\eta\mapsto\eta^*+\zeta$). $|\Phi|^2=x^2+\eta^2$, так что $x\le|\Phi|\le2x$.
2. **$(\Phi1')$.** По (10.2) $1\le h\le1+\frac{25}{16}\kappa^2r_0^2+\frac1{16}\le\frac32$.
3. **$(\Phi2')$, первая оценка.** $\nabla\rho=\nabla s=\omega$ (лемма K3). Для $w\perp Y$:
   $\langle\nabla\rho-Y/h,w\rangle=\langle\omega,w\rangle$, а из $\langle Y,w\rangle=0$ и (10.2)
   $\langle\omega,w\rangle=\kappa\theta(1-\epsilon)\langle\ell,w\rangle-\nu\langle n,w\rangle$. Значит,
   $|\langle\nabla\rho-Y/h,w\rangle|\le(\frac54\kappa|b|+|\nu|)|w|$: $\gamma_1=\frac54\kappa$.
4. **$(\Phi2')$, вторая оценка.** По (10.3) для единичного $w\perp Y$ ($|\langle-\omega+k_gn,w\rangle|\le1+\bar k_g$):
   $|\langle x\partial_x^2\Phi,w\rangle|\le\kappa(1-\kappa)|\theta|+\kappa r_0\big(\kappa|\epsilon|+|x\partial_x\epsilon|+|\nu|\bar k_g\big)+\frac54\kappa^2\theta^2(1+\bar k_g)+|x\partial_x\nu|$.
   Итак, $\gamma_2=\kappa(1-\kappa)$, $C_1\ge\frac54\kappa^2(1+\bar k_g)$, остальное — в $\varpi$.
5. **$(\Phi3)$.** Для $w\in\mathbb R^3$ разложим $w=a^s\Psi_s+a^\theta\Psi_\theta+a^\zeta\Psi_\zeta$. По (6.4)
   $a^s=w_\omega:=\langle w,\omega\rangle$, $a^\theta=w_\ell/(s(1-\epsilon))$, $w_\ell:=\langle w,\ell\rangle$,
   $a^\zeta=w_n-w_\omega\eta^*_s-w_\ell\eta^*_\theta/(s(1-\epsilon))$, $|a^\zeta|\le2|w|$. Тогда
   $D_wY=a^s\partial_sY+a^\theta\partial_\theta Y+a^\zeta\partial_\zeta Y$, и по (10.4)
   $$x\langle w,D_wY\rangle=w_\ell^2\Big(\frac1{1-\epsilon}-\kappa\Big)+\mathcal E_r,$$
   $$\mathcal E_r=\frac{w_\ell}{1-\epsilon}\Big[(\kappa\theta\partial_\theta\epsilon-\nu k_g)w_\ell+\big(-\kappa\theta(1-\epsilon)k_g+\partial_\theta\nu\big)w_n\Big]+\kappa\theta\,w_\ell w_\omega+w_\omega\big[\kappa\theta\,s\partial_s\epsilon\,w_\ell+s\partial_s\nu\,w_n\big]+a^\zeta\kappa\theta k_g\,w_\ell .$$
   Главный член $\ge(\frac45-\kappa)w_\ell^2\ge0$ (центробежный). Для $w\perp Y$ из п. 3
   $|w_\omega|\le(\frac54\kappa|\theta|+|\nu|)|w|$, поэтому почленно: $|\kappa\theta w_\ell w_\omega|\le(\frac54\kappa^2r_0|b|+\varpi)|w|^2$,
   $|\kappa\theta k_gw_\ell w_n|\le\kappa\bar k_g|b||w|^2$, $|a^\zeta\kappa\theta k_gw_\ell|\le2\kappa\bar k_g|b||w|^2$, а остальные члены в сумме не больше $\varpi|w|^2$ (множитель
   $10(1+\bar k_g)$ в определении $\varpi$ взят с запасом).
   Итак, $(\Phi3)$ выполнено с $C_1=\frac54\kappa^2(1+\bar k_g)+4\kappa\bar k_g$ (тот же $C_1$ годится в п. 4).
6. **(F).** $U\circ\Phi(x,u,\zeta)=U(\Psi(x,\theta,x^ce))=x^j\tilde F(x^{1/2},\theta,e)$ по (6.3); $F:=\tilde F$ аналитична в
   окрестности $[0,s_0^{1/2}]\times\overline{B_{r_0}}$.
7. **$(V_1')$.** $F_0(\theta,e)=G(\theta)+\frac12h_n(\theta)e^2$, $Q=G(\theta)-G(0)+\frac12h_n(\theta)e^2$, $F_0(0)=-a_0<0$. Возьмём
   $r_1$ (зависит только от $G$, $h_n$) так, что при $|\theta|<r_1$: $\theta G'(\theta)-(G(\theta)-G(0))\ge\frac14G''(0)\theta^2$ (левая
   часть равна $\frac12G''(0)\theta^2+O(\theta^3)$), $G(\theta)-G(0)\ge\frac14G''(0)\theta^2$, $h_n(\theta)\ge\frac12h_n(0)$ и
   $\frac12|\theta h_n'(\theta)|\le\frac12h_n(\theta)$. Тогда $Q\ge\lambda_0|b|^2$, и при $\mu=\kappa$
   $$\kappa\theta\partial_\theta Q+ce\,\partial_eQ-\kappa Q=\kappa\big[\theta G'-(G-G(0))\big]+e^2\Big[\big(c-\tfrac\kappa2\big)h_n+\tfrac\kappa2\theta h_n'\Big]\ge0,$$
   так как $c\ge\frac32$, $\kappa\le\frac12$. Наконец,
   $\Gamma_*=\sqrt{a_0/\lambda_0}\big[\frac{3\sqrt3}2j\cdot\frac54\kappa+2\sqrt2\kappa(1-\kappa)\big]\le\kappa\sqrt{a_0/\lambda_0}\big(\frac{15\sqrt3}8j+2\sqrt2\big)$, и
   $\Gamma_*^2\le j\kappa=\beta\mu$ по (U3).

Порядок выбора: $\kappa$ зависит только от $j$, $G(0)$, $G''(0)$, $h_n(0)$; $r_1$ — от $G$, $h_n$; $r_0$, $s_0$, $C_1$,
$\varpi$ — от $\kappa$ и карты; $\delta$ и $\sigma_*$ выбираются внутри теоремы 2′. Теорема 2′ даёт траекторию
$q=\Phi(x,u,\zeta)=x\omega(\theta)+(\eta^*+\zeta)n(\theta)$ с $|\theta|,|e|\le2\sqrt{\delta/\lambda_0}$, $\zeta=x^ce$; отсюда оценки
формулировки ($s=x$, $j\ge3$) и касание конуса ($\operatorname{dist}(q,Z)\le|q-x\omega(\theta)|=|\eta|$). Конус вокруг луча:
$|q/|q|-\omega^*|\le C\big(|\theta|+|\eta|/x\big)\le C\big(2\sqrt{\delta/\lambda_0}+C'x+2\sqrt{\delta/\lambda_0}\,x^{c-1}\big)$, где $C'x$ — от
$\eta^*=O(x^2)$; так как $x(t)<\sigma_*\le\sqrt\delta$ (§9, п. 5), это $O(\sqrt\delta)$. $\square$

Теорема K2 опирается на обе новые части теоремы 2′: перекрёстные члены ($\gamma_1,\gamma_2\ne0$) и
ослабление $(\Phi1)$ до $(\Phi1')$ (у карты (10.1) $|\partial_u\Phi|\asymp x^{1-\kappa}$, так что $B$ далеко от $I$).

### 11. Доказательство предложения K4 и следствия K4′

Лемма K1 верна при любом меньшем $y_1$ (с меньшим $s_1$), поэтому $y_1\le t_1$ можно считать; тогда при
$0<s<s_1$, $|\eta|<y_1s$ точка лежит в $\mathcal P$, и $D\Pi$ там обратим. На кривой-компоненте
$U(s\omega+\eta n)=s^m\varphi(s,\theta,\eta/s)$ по (1.1).

**(a)** — лемма K1, п. 2: $\varphi(s,\theta,\cdot)$ на шаре $|y|<y_1$ строго выпукла с минимумом в $y^*$.

**(b)** $U\circ\Psi(s,\theta,\zeta)=s^m\varphi(s,\theta,y^*+\zeta/s)$. «$\Rightarrow$» (цепное правило, обратимость $D\Psi$ не
нужна): если $\nabla U(q)=0$, то $\partial_\zeta(U\circ\Psi)=s^{m-1}\partial_y\varphi=0$, что по единственности
критической точки в слое даёт $\zeta=0$; при $\zeta=0$ $U\circ\Psi=F_{\rm fl}$, так что $\partial_sF_{\rm fl}=\partial_\theta F_{\rm fl}=0$.
«$\Leftarrow$»: $d(U\circ\Psi)=0$ в точке $(s,\theta,0)$ (производная по $\zeta$ — по критичности $y^*$), а $D\Psi$
обратим; значит, $\nabla U=0$.

**(c)** *Вне трубок.* Если $\nabla u_m(q)=0$, то $mu_m(q)=\mathcal Eu_m(q)=0$ и $q\in Z$. Множество направлений вне
трубок компактно и отделено от $\Sigma$: образ $E\big(\Sigma_0\times(-y_1,y_1)\big)$ — открытая окрестность
кривой-компоненты в $S^2$ ($E$ — локальный диффеоморфизм), $C_\omega\cap S^2$ — окрестность точки $\omega$. Поэтому
вне трубок $u_m\ge c|q|^m$ и $|\nabla u_m|\ge c'|q|^{m-1}$; вместе с $|U-u_m|\le C|q|^{m+1}$,
$|\nabla U-\nabla u_m|\le C|q|^m$ это даёт $U>0$ и $\nabla U\ne0$ при $0<|q|<\min(c,c')/C$.

*Критерий минимума.* «$\Leftarrow$»: в трубках кривых $U\ge F_{\rm fl}\ge0$ по (a), в конусах точек
$U\ge s^mR_\omega\ge0$ (лемма K1, п. 2), вне трубок $U>0$. «$\Rightarrow$»: $F_{\rm fl}(s,\theta)=U(\Psi(s,\theta,0))$ и
$s^mR_\omega(s)=U(s\omega+\eta^*_\omega(s))$ — значения $U$ в точках, сколь угодно близких к нулю.

*Критерий изолированности.* «$\Leftarrow$»: вне трубок критических точек нет; в трубке кривой критическая
точка дала бы по (b), «$\Rightarrow$», критическую точку $F_{\rm fl}$; в конусе $C_\omega$ критическая точка лежит на
дне (как в (b): $\langle\nabla U,e_a\rangle=0$ даёт $y=y^*$) и даёт нуль производной $s\mapsto s^mR_\omega(s)$, а
$(s^mR_\omega)'=s^{j-1}\big(jg_j(\omega)+O(s)\big)\ne0$ при $R_\omega\not\equiv0$. «$\Rightarrow$»: при $R_\omega\equiv0$ точка
неизолирована по K0′(b); критические точки $F_{\rm fl}$ со сколь угодно малыми $s$ дают по (b), «$\Leftarrow$»,
критические точки $U$ сколь угодно близко к нулю. $\square$

*Почему в критерии минимума стоит «$R_\omega\ge0$», а не «старший коэффициент $>0$».* Пример R20:
$U=x^2\big((y-x^2)^2+(z-x^2)^2\big)$, $u_4=x^2(y^2+z^2)$; $\Sigma$ — окружность $\{x=0\}$ и точки $(\pm1,0,0)$, (K1),
(K2) выполнены, в точках $R_\omega\equiv0$ ($y^*=(s,s)$), на окружности $F_{\rm fl}\equiv0$, а $U\ge0$ — минимум.

**Следствие K4′.** На кривой-компоненте $F_{\rm fl}=s^j\hat G(s,\theta)$, так что
$\partial_sF_{\rm fl}=s^{j-1}(j\hat G+s\partial_s\hat G)$, $\partial_\theta F_{\rm fl}=s^j\partial_\theta\hat G$. При $s=0$ вектор
$(j\hat G+s\partial_s\hat G,\partial_\theta\hat G)$ равен $(jG,G')\ne0$ (регулярность нуля; от параметризации не зависит);
по непрерывности на компактах (конечное покрытие дугами) он отделён от нуля и при малых $s$. Значит, у
$F_{\rm fl}$ нет критических точек с малым $s>0$. В точечных компонентах $j(\omega)<\infty$ даёт
$R_\omega\not\equiv0$. По (c) $0$ изолирована. (Используется только «$\Rightarrow$» в (b).) $\square$

### 12. Примеры

Общий приём для $j$ и $G$ (двусторонняя оценка; по отзыву R22, замечание 2). Пусть в слое
$\varphi(s,\theta,y)=\sum_\ell p_\ell(s,\theta,y)^2+s^{j-m}w(\theta,y)$, где $p_\ell$, $w$ аналитичны, $y^*=O(s)$, и система
$p_\ell(s,\theta,y)=0$ имеет решение $y_0(s,\theta)=O(s)$. Тогда
$s^{j-m}w(\theta,y^*)\le R=\varphi(s,\theta,y^*)\le\varphi(s,\theta,y_0)=s^{j-m}w(\theta,y_0)$, откуда
$R=s^{j-m}w(\theta,0)+O(s^{j-m+1})$ равномерно по $\theta$ на компакте: $g_k=0$ при $m<k<j$ и $g_j=w(\cdot,0)$, если
$w(\cdot,0)\not\equiv0$.

**Пример 1: $U_{(5)}=A^2+B^2+z^5$.** $u_4=A^2+B^2\ge0$, $\Sigma=\{A=B=0\}\cap S^2=\{(\pm1,\pm1,\pm1)/\sqrt3\}$. В
$\omega=(\epsilon_1,\epsilon_2,\epsilon_3)/\sqrt3$ ($\epsilon_i=\pm1$) $\nabla A=\frac2{\sqrt3}(\epsilon_1,0,-\epsilon_3)$,
$\nabla B=\frac2{\sqrt3}(0,\epsilon_2,-\epsilon_3)$ ортогональны $\omega$ и независимы, $D^2u_4=2(\nabla A\nabla A^{\mathsf T}+\nabla B\nabla B^{\mathsf T})\succ0$
на $\omega^\perp$: (K1), (K2) выполнены (в $\omega^*=(1,1,-1)/\sqrt3$, базис $e_1=(1,-1,0)/\sqrt2$, $e_2=(1,1,2)/\sqrt6$:
$H=\operatorname{diag}(\frac83,8)$). При $v=\omega+y$: $\varphi=A(v)^2+B(v)^2+s\,z(v)^5$; система $A(v)=B(v)=0$ разрешима
($y_0(s)=0$, так как $A(\omega)=B(\omega)=0$), так что по общему приёму $j=5$, $g_5(\omega)=z(\omega)^5=\pm3^{-5/2}$, и
$g_5(\omega^*)=-3^{-5/2}<0$: $U_{(5)}\in\mathcal K^0$, теорема K0 даёт асимптотическую траекторию.
*Изолированность* (над $\mathbb R$): $\partial_xU=4xA$, $\partial_yU=4yB$, $\partial_zU=-4zA-4zB+5z^4$; в случаях
$A=B=0$; $A=0,y=0$; $x=0,B=0$; $x=y=0$ уравнение $\partial_zU=0$ даёт $5z^4=0$, $z^3(4+5z)=0$, $z^3(4+5z)=0$,
$z^3(8+5z)=0$, и малый корень только $z=0$, откуда $x=y=0$. Не минимум: $U(t\omega^*)=-3^{-5/2}t^5<0$.
[Эксперимент, R22: число Милнора $\mu=31$, то есть изолированность и над $\mathbb C$.] Здесь
$\mathcal EU=4U+z^5<0$ на $\{U<0\}$ (там $z^5<-u_4\le0$): радиальное условие Четаева выполнено, и пример —
только иллюстрация (замечание 2).

**Пример 2: $U_{(7)}=P_1^2+P_2^2+z^7$.** $u_4=A^2+B^2$ (пример 1), $u_5=2Az^3$, $u_6=z^6$, $u_7=z^7$. При $v=\omega+y$
($\omega\in\Sigma$): $P_1(sv)=s^2\big(A(v)+sz(v)^3\big)$, $P_2(sv)=s^2B(v)$, так что
$\varphi=p_1^2+p_2^2+s^3z(v)^7$, $p_1=A(v)+sz(v)^3$, $p_2=B(v)$. Матрица Якоби $y\mapsto(p_1,p_2)$ при $s=0$, $y=0$ —
$(\langle\nabla A(\omega),e_a\rangle,\langle\nabla B(\omega),e_a\rangle)$, невырождена; по теореме о неявной функции
$y_0(s)=O(s)$ с $p_1=p_2=0$. По общему приёму $g_5=g_6=0$, $j=7$, $g_7(\omega)=z(\omega)^7=\pm3^{-7/2}$;
$g_7(\omega^*)=-3^{-7/2}<0$: $U_{(7)}\in\mathcal K^0$, теорема K0. [Эксперимент: в базисе $e_1,e_2$ примера 1
$y^*(s)=(\frac{\sqrt2}{12},\frac{\sqrt6}{36})s+O(s^2)$ — дно искривлено в первом порядке.]
*Изолированность* (над $\mathbb R$): $\partial_xU=4xP_1$, $\partial_yU=4yP_2$, и в случаях $P_1=P_2=0$; $P_1=0,y=0$;
$x=0,P_2=0$; $x=y=0$ получаем $\partial_zU=7z^6$, $z^3(7z^3+4)$, $z^3(7z^3+6z^2-10z+4)$, $z^3(7z^3+6z^2-10z+8)$;
малый корень только $z=0$, откуда $x=y=0$ (в первом и втором случаях $x^2=z^2-z^3=0$). Не минимум:
на кривой $P_1=P_2=0$, $z<0$ (она существует: $x^2=z^2(1-z)>0$, $y^2=z^2$) $U=z^7<0$. Гессиан нулевой.
[Эксперимент, R22: $\mu=39$.]

*Нарушение радиального условия Четаева.* $\mathcal EU_{(7)}=4U+2z^3P_1+3z^7$ (из $\mathcal Eu_k=ku_k$). Для
$q(\tau)=\big(\sqrt{\tau^2+\tau^3-\tau^{7/2}/2},\ \tau,\ -\tau\big)$, $\tau>0$: $P_1=-\frac12\tau^{7/2}$, $P_2=0$,
$U=-\frac34\tau^7<0$, $\mathcal EU=\tau^{13/2}-6\tau^7>0$ при $\tau<\frac1{36}$; $q(\tau)/|q(\tau)|\to\omega^*$ (семейство R22;
проверено символьно, `chetaev_families.py`).

**Пример 3: $U_{(8)}=P^2+u_7$, $P=Q_0+z^3$, $u_7=xz^6+xyz^5+\frac12z^7$.** $u_4=Q_0^2$, $u_5=2Q_0z^3$, $u_6=z^6$.
$\Sigma_\pm=\{z=\pm\frac1{\sqrt2},\ x^2+y^2=\frac12\}$, $D^2u_4=2\nabla Q_0\nabla Q_0^{\mathsf T}$ на конусе, $|\nabla Q_0|=2$ на
$\Sigma$, $h_n=8$: (K1), (K2) выполнены. Для $\omega\in\Sigma$ с нормалью $n$: $\varphi=p^2+s^3u_7(\omega+yn)$,
$p=Q_0(\omega+yn)+s\,z(\omega+yn)^3$, $\partial_yp|_{s=y=0}=\langle\nabla Q_0(\omega),n\rangle=\pm2\ne0$; по общему приёму
$g_5=g_6\equiv0$, $j=7$, $G_\pm=u_7|_{\Sigma_\pm}$. Подстановка $x=\frac{\cos\varphi}{\sqrt2}$, $y=\frac{\sin\varphi}{\sqrt2}$,
$z=\pm\frac1{\sqrt2}$ даёт формулы для $G_\pm$ из формулировки.

*Минимум.* $G_+'=0\iff\cos2\varphi=\sin\varphi\iff\sin\varphi\in\{\frac12,-1\}$: $\varphi\in\{\frac\pi6,\frac{5\pi}6,\frac{3\pi}2\}$, значения
$\frac{\sqrt2}{32}(1+\frac{3\sqrt3}2)$, $\frac{\sqrt2}{32}(1-\frac{3\sqrt3}2)$, $\frac{\sqrt2}{32}$. Глобальный минимум — $\varphi^*=\frac{5\pi}6$,
$\frac{d^2G_+}{d\varphi^2}(\varphi^*)=\frac{\sqrt2}{32}(-2\cos\varphi^*-4\sin2\varphi^*)=\frac{3\sqrt6}{32}$; натуральный параметр окружности
радиуса $\frac1{\sqrt2}$ — $\theta=\varphi/\sqrt2$, так что $G''=2\frac{d^2G_+}{d\varphi^2}=\frac{3\sqrt6}{16}$, и
$G''+7G=\frac{3\sqrt6}{16}+\frac{7\sqrt2(2-3\sqrt3)}{64}=\frac{14\sqrt2-9\sqrt6}{64}<0$ ($14\sqrt2\approx19.80<9\sqrt6\approx22.05$). Другие
точки (K3) на $\Sigma_+$ нет ($\frac\pi6$ — максимум, $\frac{3\pi}2$ — перегиб). На $\Sigma_-$ по 3.4 $G_-(\varphi+\pi)=-G_+(\varphi)$, так
что единственная точка (K3) — $\frac{7\pi}6$ (образ максимума $G_+$ в $\frac\pi6$; $\frac\pi2$ — перегиб, $G''=0$): там
$G_-=-\frac{\sqrt2(2+3\sqrt3)}{64}$, $G''=\frac{3\sqrt6}{16}$, $G''+7G=-\frac{9\sqrt6+14\sqrt2}{64}<0$ (отзыв R23, З3). Итак, ни одна пара
$(\Sigma_0,\omega^*)$ не даёт $G''+7G>0$: $U_{(8)}\in\mathcal K^1\setminus\mathcal K^1_{\rm C}$; теорема K2 ($\kappa\le0.0174$ по (U3)).

*Изолированность над $\mathbb R$* — по следствию K4′: $j=7$ на обеих окружностях, и $0$ — регулярное
значение $G_\pm$. Критические значения $G_+$ выписаны выше (ненулевые). $G_-'=0\iff2\sin^2\varphi-\sin\varphi-1=0\iff\sin\varphi\in\{1,-\frac12\}$:
$\varphi\in\{\frac\pi2,\frac{7\pi}6,\frac{11\pi}6\}$, значения $\frac{\sqrt2}{32}\cdot(-1)$, $\frac{\sqrt2}{32}(-1-\frac{3\sqrt3}2)$,
$\frac{\sqrt2}{32}(\frac{3\sqrt3}2-1)$ — ненулевые. [Независимо R22: Singular, разложение идеала Якоби над $\mathbb Q$.]
Не минимум: в точках дна $U\big(s\omega^*+\eta^*(s,\omega^*)\big)=s^7\big(G_+(\varphi^*)+O(s)\big)<0$ (на самом луче
$U(t\omega^*)=t^6z(\omega^*)^6+O(t^7)>0$: отрицательные значения есть только на искривлённом дне).

*Неизолированность над $\mathbb C$.* При $z=0$: $P=x^2+y^2$, $\partial_xU=4x(x^2+y^2)$, $\partial_yU=4y(x^2+y^2)$,
$\partial_zU=2P(-2z+3z^2)+6xz^5+5xyz^4+\frac72z^6=0$. Поэтому прямые $\{z=0,\ x=\pm iy\}\subset\mathbb C^3$ состоят из
критических точек комплексификации, и число Милнора бесконечно (проверено символьно,
`chetaev_families.py`; R22 — Singular).

*Нарушение радиального условия Четаева.* $\mathcal EU_{(8)}=4U+2z^3P+3u_7$ (из $\mathcal Eu_k=ku_k$:
$\mathcal EU=4Q_0^2+10Q_0z^3+6z^6+7u_7$).
- Верх: $\varphi=\frac{5\pi}6$, $z=\zeta>0$, $r_{xy}\in[\zeta\sqrt{1-\zeta},\zeta]$. Там $u_7=-\frac{\sqrt3}2r_{xy}\zeta^6-\frac{\sqrt3}4r_{xy}^2\zeta^5+\frac12\zeta^7=\zeta^7\big(\frac12-\frac{3\sqrt3}4+O(\zeta)\big)$,
  так что $c\zeta^7\le-u_7\le C\zeta^7$, а $P=r_{xy}^2-\zeta^2+\zeta^3$ возрастает от $0$ до $\zeta^3>\frac12\sqrt{-u_7}$ (при малом
  $\zeta$). По теореме о промежуточном значении есть $r_{xy}$ с $P=\frac12\sqrt{-u_7}$; тогда $U=-\frac34|u_7|<0$ и
  $\mathcal EU=\zeta^3\sqrt{|u_7|}-6|u_7|>0$, так как $\sqrt{|u_7|}\le\sqrt C\zeta^{7/2}<\zeta^3/6$ (семейство R22).
- Низ: $\varphi=\pi$, $z=-\zeta<0$, $r_{xy}\in[\zeta,\sqrt{\zeta^2+\zeta^3}]$. Здесь $y=0$, $u_7=-r_{xy}\zeta^6-\frac12\zeta^7<0$,
  $|u_7|\le2\zeta^7$, $P=r_{xy}^2-\zeta^2-\zeta^3$ возрастает от $-\zeta^3$ до $0$; есть $r_{xy}$ с $P=-\frac12\sqrt{-u_7}$. Тогда
  $2z^3P=\zeta^3\sqrt{|u_7|}$, $U=-\frac34|u_7|<0$, $\mathcal EU=\zeta^3\sqrt{|u_7|}-6|u_7|>0$ (добавлено при оформлении).

[Эксперимент `chetaev_families.py`: $\mathcal EU/|U|=7.0,\ 39,\ 141,\ 464$ (верх) и $2.9,\ 26,\ 101,\ 336$ (низ) при
$\zeta=10^{-2},\dots,10^{-5}$.]

*Все компоненты $\{U<0\}$ (примеры 2 и 3).* Компоненты считаем в окрестности
$W_\varepsilon:=\{\text{точки трубок с }s<\varepsilon\}\cup\{q:\ |q|<\varepsilon\ \text{вне трубок}\}$, $\varepsilon\le s_2$ (трубки — как в
предложении K4; для точечных компонент $s=\langle q,\omega\rangle$). Для шара $B_\varepsilon$ понадобился бы ещё шаг: слой трубки,
пересечённый с шаром, при $s\approx\varepsilon$ может не содержать точки дна; здесь он не выписан (отзыв R23, З4).
Около $0$ множество $\{U<0\}$ лежит в трубках над теми
точками (пример 2) или дугами (пример 3), где $G<0$: вне трубок $U>0$, над точками и дугами с $G>0$
$U\ge U_{\rm red}>0$ (следствие K0′(a), предложение K4(a)). В такой трубке $\{U<0\}$ связно: в каждом слое
это выпуклое множество (подуровень строго выпуклой $\varphi(s,\theta,\cdot)$), содержащее точку дна, а
множество $\{(s,\theta):\ R(s,\theta)<0\}$ при малых $s$ связно — для примера 2 это интервал по $s$; для примера 3
отрицательное множество $G_+$ и $G_-$ — по одной дуге (каждая компонента $\{G<0\}$ содержит локальный
минимум; у $G_+$ отрицательное критическое значение одно, у $G_-$ точка $\frac\pi2$ — перегиб ($G_-'\le0$ около
неё), минимум один — $\frac{7\pi}6$), и по теореме о неявной функции у регулярных нулей $G$ множество
$\{\hat G(s,\cdot)<0\}$ при малых $s$ — интервал между двумя непрерывными ветвями нулей. Итак, у
$U_{(7)}$ четыре компоненты, примыкающие к $0$ (лучи $(\pm1,\pm1,-1)/\sqrt3$; переводятся друг в друга
симметриями $x\mapsto-x$, $y\mapsto-y$), у $U_{(8)}$ — две, и семейства выше лежат в них при малых
параметрах. Следовательно, **в каждой компоненте $\{U<0\}\cap W_\varepsilon$, примыкающей к $0$, есть сколь угодно
близкие к $0$ точки с $\mathcal EU>0$.** $\square$

## Замечания

### 1. Где работают аналитичность и изолированность

- **Теорема 2′ и лемма 2′** — утверждения для $U\in C^2$ при заданной карте; аналитичность и
  изолированность в них не используются (как и в теореме 2 [007]). Всю «конечность типа» несут (F) и
  $(V_1')$: вдоль дна $U=x^\beta(F_0(0)+o(1))$, $F_0(0)<0$, поперёк — степенные стенки с запасом Эйлера.
- **В теоремах K0, K1, K2** аналитичность нужна, чтобы получить форму (F): $U=s^j\tilde F(s^{1/2},\theta,e)$ с
  конечным $j$ и $\tilde F$, непрерывно продолжимой в $s=0$ (леммы K1, K2), и чтобы дуга $\Sigma_0$, рамка и
  $y^*$ были аналитическими (малые величины (6.5)). Изолированность в теоремах K0–K2 не нужна: условие
  $G(\omega^*)<0$ уже даёт $j<\infty$. [Эскиз] Для $U\in C^\infty$ леммы K1, K2 верны с конечной гладкостью
  $\tilde F$ (нужная гладкость $U$ порядка $C^{j+3}$, не выписано), если $R$ имеет ненулевой конечный
  коэффициент Тейлора; так что теоремы K0–K2 — критерии по струе $j^jU$.
- **В следствии K0′ (и в критериях предложения K4) аналитичность и изолированность работают
  вместе.** Следствие K0′ — единственное место, где (A) выводится без дополнительных условий на
  струю; предложение K4 само (A) не выводит, а сводит её к функции дна $F_{\rm fl}$. Аналитическая $R_\omega$
  либо $\equiv0$ (тогда кривая критических точек — изолированность это исключает), либо имеет конечный
  порядок (тогда теорема K0 или минимум). Для $C^\infty$ это ломается: $R_\omega$ может быть плоской и
  ненулевой (например, $R_\omega(s)=-e^{-1/s}$), и тогда нет ни конечного $j$, ни кривой критических
  точек: без аналитичности дихотомия ломается. Гладкий контрпример такого типа (изолированная точка,
  плоская ненулевая $R_\omega$, устойчивое равновесие) не известен: у примеров Пенлеве–Уинтнера и
  Лалуа все однородные части нулевые и критическая точка неизолирована (по `problem/KNOWN_RESULTS.md`,
  с первоисточниками не сверено), так что под условия K0′ они не подпадают; а, например, для
  $U=y^2-e^{-1/x^2}$ функция $R_\omega$ плоская, но равновесие неустойчиво (отзыв R23, З5). Пример Уреньи касается тотальной
  неустойчивости; теоремы дают только одну асимптотическую траекторию и с ним не конфликтуют.
- **Изолированность над $\mathbb R$ и над $\mathbb C$.** Задача (A) требует только вещественной
  изолированности, и следствие K0′, предложение K4, следствие K4′ работают именно с ней. Пример 3
  изолирован над $\mathbb R$, но не над $\mathbb C$ ($\mu=\infty$): результаты, требующие конечности числа
  Милнора (теорема Сайто о квазиоднородности, конечная определённость по Мазеру; по конспекту
  `notes/literature/2026-10-21-revision-rest.md` §2–3, не сверено), к нему неприменимы.

### 2. Связь с литературой и новизна

- **$m=2$** [Литература, по конспектам `notes/literature/2026-10-21-jet-conjecture.md` §2.3 и
  `notes/literature/2026-10-21-revision-rest.md` §1.3; первоисточники не сверены]. Условие
  следствия K0′ при $m=2$ — гессиан $\succeq0$ ранга $n-1$; это покрыто FGT08, Thm A (ранг $\ge n-2$; нужна
  струя, показывающая отсутствие минимума, — по BGZ96, не сверено) и **частично** Козловым 1986
  (условие «$V_2+V_{m'}$ без минимума» для следующей ненулевой формы). [Доказано, элементарно]
  Пример $U=y^2(1+x)-x^4$ ($n=2$): $0$ изолирована и не минимум, условия K0′ выполнены
  ($R_{(\pm1,0)}=-s^2$), но $V_2+V_3=y^2(1+x)\ge0$, так что условие Козлова не выполнено (R20).
- **$m\ge4$ (жёсткое ядро).** [Литература, по конспекту `notes/literature/2026-10-21-jet-conjecture.md` §3; не
  сверено] Жёсткое ядро задачи (A) при $n=3$ — случай нулевого гессиана, $m\ge4$: при $m=2$ работают
  Ляпунов и FGT08, а при $u_m$ с отрицательными значениями — критерии по первой струе. Критерии по первой ненулевой струе (Ляпунов, MN89, MMN91, Taliaferro 1990,
  Паламодов 2020 Thm 3) требуют, чтобы $u_m$ принимала отрицательные значения или не имела
  критических точек вне нуля; здесь $u_m\ge0$, $\nabla u_m=0$ на $Z$. FGT08 требует ранг гессиана $\ge n-2$.
- **Радиальное условие Четаева** [Доказано, элементарно]. Если $U=u_m+u_k$ с одним однородным $u_k$,
  то $\mathcal EU=mU+(k-m)u_k<0$ на $\{U<0\}$ ($u_k<-u_m\le0$ там). Это относится к примеру 1, к примеру
  теоремы B $Q_0^2+xz^4$ и к $Q_0^2+W_k$ с однородным $W_k$; для примера 13 [007]
  $\mathcal EU=6U-2Q_0^2<0$ на $\{U<0\}$. Тогда неустойчивость следует из теоремы Четаева, а
  асимптотическая траектория — из AG17, Prop. 8 («строгое условие Четаева ⇒ асимптотическое
  движение») [Литература: AG17, по конспекту; не сверено]. **Для этих примеров теоремы K0–K2 нового не
  дают**; вероятно, это касается и новизны следствия 4 [007] (пример 13) — стоит сверить AG17, Prop. 8
  по первоисточнику.
- **«Искривлённое дно»** (примеры 2, 3): $c=\frac{j-m+2}2>2$ и $\eta^*\ne O(s^3)$. Здесь строгое условие
  Четаева не выполнено ни для одной компоненты $\{U<0\}\cap W_\varepsilon$, примыкающей к $0$ (доказано в §12), а условие (H3) класса
  $\mathcal H$ Alva–Garcia (для $j^7U=U$, в любом из двух вариантов, по конспекту
  `notes/literature/2026-10-21-revision-rest.md` §1.2) требует $\mathcal Ej^7U<0$ на компоненте
  $\{j^7U<0\}$ и потому тоже не выполнено [Литература: AG17 — формулировка (H3) по конспекту, не
  сверена]. По доступным в репозитории конспектам литературы (A) для таких примеров известно не было.
  Не проверено, не покрываются ли они теоремой 6 Паламодова 2020 (квазиоднородная главная часть без
  критических точек вне нуля) после аналитической замены координат, выпрямляющей дно: формулировка
  теоремы 6 есть только по конспекту, допустимость неевклидовой кинетической энергии там не ясна.
  Первоисточники MN89, MMN91, KP82 не открывались. Новизна — [Гипотеза].
- *Механизм* [Эскиз]: $\mathcal EU=jU-(c-1)s^jh_ne^2+O(s^{m+c})\cdot e$, где последний член — от $\partial_s\eta^*\ne0$;
  при $c>2$ он главнее $s^j$, и радиальная производная знакопеременна на $\{U<0\}$. Это ситуация «оврага»
  Гарсии–Тала, где нужна карта $\gamma(x)=\eta^*(x)$. В общем виде не доказано; для примеров 2, 3 —
  доказано явными семействами.

### 3. Плоский срез и сфера: зачем теорема 2′ [Эскиз + Эксперимент]

Декартов срез $\{X=x\}$ развёртки пересекает лучи под углом $\theta$, на нём $s=x/\cos\theta$, и
$s^jG(\theta)=x^j\big(1+\frac j2\theta^2+\dots\big)\big(G(0)+\frac12G''\theta^2+\dots\big)$: поперечный гессиан равен $G''+jG$, а
$G<0$ (§7). У примера 13 запас мал ($G''+6G=\frac{6-3\sqrt3}{16}\approx0.050$, это $H_{11}$ предложения 3 [007]), у
примера теоремы B отрицателен ($g_5=u_5|_\Sigma=\frac{\cos\varphi}{4\sqrt2}$ по §3.3, минимум при $\varphi=\pi$,
$G''+5G=-\frac{3\sqrt2}8$), у примера 3 тоже. Это же нашёл агент numerics на полигоне
(`experiments/numerics/2026-10-21-valleys/README.md`, [Эксперимент]: $H_{\rm plane}=\lambda_{\rm мягк}/r^{\beta-2}-\beta a<0$
у A1, A2, A5, A7, C2 и у примера теоремы B, хотя стрельба назад сходится). Полярный срез $\{s=x\}$ с
радиальным $Y$ даёт гессиан $G''$, но нулевой запас Эйлера по углу (вес $0$): [Эксперимент
`exit_check.py`] при $\kappa=0$ минимум $\frac\rho\lambda\Xi/(\delta\rho^j)$ на стенке мал ($0.02$, $0.01$ для
примера теоремы B) и меньше при меньших $(\delta,\sigma)$, при $\kappa=0.05$ — около $0.11$ и почти не меняется.
Поворот на малый угловой вес $\kappa$ даёт запас $\sim2\kappa$ и перекрёстные члены $\sim\kappa|\theta||v_\perp|\rho^{\beta/2}$;
квадратичная форма $\beta K+\kappa G''\theta^2\rho^\beta-C\kappa|\theta|\sqrt K\rho^{\beta/2}$ положительна при малом $\kappa$
(аналог функции Ляпунова $w^2+G''\theta^2-\varepsilon\theta w$ для линеаризации в раздутии Макги, где угловые
собственные числа $\lambda^2-\frac{j+2}2|v_0|\lambda+G''=0$ имеют положительные вещественные части). Попадают ли
примеры полигона A1, A2, A5, A7, C2 в класс $\mathcal K$, здесь не проверялось.

### 4. Ослабление условия (U2) [Эскиз] (отзыв R21, З5)

(i) В п. 7 доказательства леммы 2′ достаточно $\Gamma'^2\le\mu(2\beta-\mu)$. (ii) Если $\Gamma'^2<4\beta\mu$, то при
некотором $\varepsilon\in(0,\min(\beta,\mu))$ $\Gamma'^2\le4(\beta-\varepsilon)(\mu-\varepsilon)$ и $\beta K+\mu\mathcal Q-\Gamma'\sqrt{K\mathcal Q}\ge\varepsilon(K+\mathcal Q)$;
в (8.1) $\frac\mu2$ заменяется на $\varepsilon$. (iii) На множестве (A5) точнее $\lambda\ge\sqrt{2(a_0-\delta)/h_1}\,\rho^{\beta/2}$, и
коэффициент при $\gamma_1$ в $\Gamma'$ при $\delta\to0$ стремится к $\sqrt{a_0/\lambda_0}\cdot\frac{\sqrt6}2\beta$. Отсюда теорема 2′
должна оставаться верной при $\big[\sqrt{a_0/\lambda_0}(\frac{\sqrt6}2\beta\gamma_1+2\sqrt2\gamma_2)\big]^2<4\beta\mu$, что расширяет
допустимое $\kappa$ в теореме K2 примерно в 18 раз при больших $j$. В модельном примере R21 численный порог
строгого выхода в 10–100 раз выше обеих оценок [Эксперимент, R21]. Для теоремы 2′ в нынешней
формулировке не нужно.

### 5. Касание луча [Гипотеза]

Доказано только, что траектория теоремы K0 или K2 (своя для каждого $\delta$) лежит в конусе раствора
$O(\sqrt\delta)$ вокруг луча $\mathbb R_+\omega^*$ и касается конуса $Z$. Что одна траектория касается самого луча,
не доказано; путь — переменное $\delta(\rho)\downarrow0$, как в замечании 3 [007].

### 6. Что остаётся открытым

Предложение K4 сводит жёсткое ядро при $n=3$ и $\Sigma$ Морса–Ботта к семейству двумерных «задач на дне»:
аналитическая $F_{\rm fl}(s,\theta)=s^{m+1}(g_{m+1}+sg_{m+2}+\dots)$ на полуцилиндре $[0,s_1)\times\Sigma_0$ (развёртка —
плоский конус) плюс невырожденный «быстрый» нормальный овраг ширины $\asymp s^c$. Класс $\mathcal K$ —
невырожденный случай. Вне $\mathcal K$ (записка, §10.2):

1. $G$ постоянен и отрицателен на замкнутой компоненте (например, $Q_0^2-z^6+\dots$) [Эскиз]: трубка
   вокруг всего конуса над $\Sigma_0$ без угловых стенок, $Y=\Psi_s$, лемма 2 [007] с $C_1=0$; не выписаны
   (D1)–(D3) для кольцевой области.
2. Изолированный вырожденный минимум $G-G(0)\sim\theta^{2p}$, $p\ge2$ [Эскиз]: нужен аналог $(V_0)$ в
   карте (10.1) с $\kappa=\kappa(\delta)\lesssim\delta^{1-1/p}$ (кривизна карты даёт $C_1=O(\kappa)$).
3. Каскад: $G\ge0$ на $\Sigma_0$ с нулями [Гипотеза + план]: ветви Пюизё угловых минимумов $F_{\rm fl}$ и
   трёхмасштабная карта; при невырожденном угловом минимуме — теорема 2 [007]; нужен аналог факта 1
   Гарсии–Тала.
4. Нарушение Морса–Ботта (вырожденный нормальный овраг) и особое $\Sigma$ [Гипотеза]: $(V_0)$ в кривых
   картах (R3 записки GT3), раздутия в особых точках $\Sigma$.
5. $n\ge4$: при $\dim\Sigma_0=1$ [Эскиз] — та же схема с параллельной нормальной рамкой; при
   $\dim\Sigma_0\ge2$ [Гипотеза] — многомерный угловой поворот.

### 7. Эксперименты

Все — [Эксперимент], запуск `~/venv/bin/python <скрипт>`.

- `experiments/prover/gt3-hardcore/`: `frame_check.py` (формулы (6.4), (7.1)-карты, (10.2)–(10.4) в
  подвижном репере с общими многочленами $k_g(\theta)$, $\eta^*(s,\theta)$ — все тождества верны);
  `reduced.py`, `examples.py`, `examples_s0.py` (ряды $y^*$, $g_k$, $G$, нормальная форма (6.3));
  `chetaev_lower.py`; `exit_check.py` (строгий выход для карты (10.1) прямым дифференцированием вдоль
  поля, без формулы (1.3) [007]); `shooting_curved.py` (стрельба для примера 3: точки входа сходятся,
  прямой прогон идёт по закону $s^{-5/2}=s_{\rm in}^{-5/2}+\frac52\sqrt{2a_0}\,t$).
- `experiments/prover/gt3-result008/chetaev_families.py`: тождества для $\mathcal EU$, семейства §12,
  комплексные критические прямые $U_{(8)}$.
- `experiments/reviewer/gt3-hardcore-R20/`, `-R21/`, `-R22/`: независимые проверки рецензентов (в том
  числе числа Милнора $31$, $39$, $\infty$ — Singular, R22).

## Отличия от записки

**Правки по отзыву R20** (`notes/reviewer/2026-10-21-gt3-hardcore-A.md`).

1. *Предложение K4(c), критерий минимума* (замечание 1, ошибка формулировки). «Старшие коэффициенты
   $R_\omega$ положительны» заменено на «$R_\omega(s)\ge0$ при малых $s>0$»; приведён контрпример R20; выписано
   доказательство обеих импликаций. При изолированной точке формулировки совпадают.
2. *Лемма K1:* $\overline{\Lambda''}\subset\Lambda'$ (замечание 2); теорема о неявной функции выведена из (F1)
   (замечание 7); добавлено, что $y_1$ можно уменьшать.
3. *Теорема K0:* $\lambda_0=\lambda_{\min}(H)/4$, $\sigma_0<s_1^{1/2}$, $s_0=\sigma_0^2$ (замечание 3).
4. *K4(b), «$\Leftarrow$»:* $y_1\le t_1$ (обратимость $D\Psi$); трубки точечных компонент — конусы $C_\omega$
   (замечание 4).
5. *§3.3 записки:* ряд $R=\sum s^ig_{m+i}$ — в круге сходимости (замечание 5); замечание 3.3.4 для $d=1$ и любого
   $n$ (замечание 6); независимость $j$ от дуги — по теореме единственности; чётность — на
   $\Sigma_0\cup(-\Sigma_0)$.
6. *Литература, $m=2$* (замечание 8): «покрыто Козловым 1986» → «покрыто FGT08, частично Козловым 1986», с
   примером $y^2(1+x)-x^4$.
7. *Ссылка на [002] при компонентах разной размерности* (замечание 9) — §1.

**Правки по отзыву R21** (`...-B.md`).

8. З1: лемма 2′ названа аналогом леммы 2, а не обобщением (с объяснением).
9. З2: карта класса (GT3) удовлетворяет $(\Phi1')$–$(\Phi2')$ с $\varpi=2\sqrt2\,\omega$.
10. З3: константы $c_1,c_2\to L_1,L_2$; $x^{1/N}$ обозначено $\varsigma$, порог по $x$ — $\sigma_*$; ссылки на формулы — по
    нумерации [007] ((0.1), (1.1), (1.3), (3.1), (4.1), (4.2)); «Коши–Буняковский» в п. 7 заменён на неравенство о
    среднем арифметическом и геометрическом (Коши–Буняковский остался только в (L2′)).
11. З4: в лемме 2′ явно $\theta_i\ge0$, $\gamma_i'\ge0$.
12. З5: ослабление (U2) — замечание 4, [Эскиз].
13. Мелочи: в шаге 3 теоремы 2′ упомянуто свойство (ii) шага 2; нижняя оценка $\dot\rho$ в лемме 2′ — с
    $a_3+\delta/2$ (из $W\ge-\frac12\delta\rho^\beta$).

**Правки по отзыву R22** (`...-C.md`).

14. Замечание 1: $U_{(8)}$ изолирована над $\mathbb R$, но не над $\mathbb C$ — сказано в формулировке примера 3,
    доказано в §12 (прямые $\{z=0,x=\pm iy\}$), обсуждено в замечании 1.
15. Замечание 2: $j=7$ и $G=u_7|_\Sigma$ выведены двусторонней оценкой («общий приём» §12) вместо фразы «дно
    точное»; тем же приёмом — пример 1.
16. Замечание 3: в теоремах K1, K2 дописаны $r_0\le\theta_1/2$, $[-r_0,r_0]\subset\Lambda''$, $s_0\le\sigma_0^2/2$.
17. Замечание 4: «общий механизм» — [Эскиз]; утверждение о (H3) — с оговоркой о несверенной литературе;
    нарушение радиального условия Четаева доказано явными семействами R22 (вместо доли случайных точек).
18. Замечание 5: базис $e_1,e_2$ назван явно.
19. Замечание 6: сказано, что теорема K2 опирается на обе новые части теоремы 2′.

**Правки по R23, R24** (`notes/reviewer/2026-10-21-result008-A.md`, `...-B.md`; ошибок нет, правки редакционные).

- R23, З1: в 3.5 дописано, что при $d=1$ и общем $n$ $\operatorname{span}(\Psi_s,\Psi_\theta)+N_\theta=\mathbb R^n$ при малых $s$.
- R23, З2: фраза «жёсткое ядро — $m\ge4$» перенесена из «Утверждения» в замечание 2 с меткой [Литература, не сверено].
- R23, З3: в примере 3 проверена и $\Sigma_-$ (точка $\frac{7\pi}6$, $G''+7G=-\frac{9\sqrt6+14\sqrt2}{64}<0$), так что $U_{(8)}\notin\mathcal K^1_{\rm C}$ доказано полностью.
- R23, З4: компоненты $\{U<0\}$ считаются в окрестности $W_\varepsilon$ (определена в §12); для шаров нужен шаг, не выписанный здесь.
- R23, З5: замечание 1 — K4 само (A) не выводит; про Пенлеве–Уинтнера и Лалуа сказано точнее (точка неизолирована), пример $y^2-e^{-1/x^2}$; ссылка на теорему Сайто и Мазера — по конспекту, не сверено.
- R23, З6: обоснование «$G$ определяется струёй $j^jU$» через $R=\min_y\varphi$ и $|\min f-\min g|\le\sup|f-g|$ (3.3).
- R23, З7: в §6 оговорено, что при $n=3$ $\eta^*$ — скалярный коэффициент при $n(\theta)$.
- R24, п. 1: в §7 дописаны условия на $s_0$ (образ в $\mathcal P$ и в шаре аналитичности, $s_0\le1$) и оценка $|B_{xu}|\le5\varpi_1\le\varpi$.
- R24, п. 2: в §9, п. 5 — $\sigma_*\le\sqrt\delta$; в §10 выписан вывод «конус раствора $O(\sqrt\delta)$».
- R24, п. 3: в замечании 3 «убывает с $\sigma$» заменено на «меньше при меньших $(\delta,\sigma)$».
- R24, п. 4: в гипотезах теоремы K2 дописано $e_1=n$.

**Уточнения при оформлении** (не из отзывов R20–R22; их прочитали R23 и R24 — каждый свои разделы).

20. Для нижней компоненты $\{U_{(8)}<0\}$ построено своё семейство с $\mathcal EU>0$ ($\varphi=\pi$, $z<0$,
    $P=-\frac12\sqrt{-u_7}$) и выписан довод «каждая компонента $\{U<0\}$, примыкающая к $0$, содержит такие точки»
    (выпуклость слоёв, одна отрицательная дуга у $G_\pm$). Регулярность нулей $G_\pm$ проверена вручную
    (критические значения), а не результантом.
21. В примере 3 исправлено обоснование «не минимум»: на луче $\omega^*$ $U>0$, отрицательные значения — на
    дне.
22. Теоремы K0 и 2′ сформулированы с $\delta_*$ и оценками $-k_2x^{\beta/2}\le\dot x\le-k_1x^{\beta/2}$, как теорема 2
    [007]; в теореме K2 траектория записана в координатах $\Psi$.
23. Переобозначения (математика та же): касательный вектор $T\to\ell$; геодезическая кривизна $k\to k_g$;
    $\varepsilon=k\eta/s\to\epsilon$; нормальная компонента $Y$: $p\to\nu$, $p_X,p_Y\to\nu_X,\nu_Y$ (буква $p$ занята
    $\langle v,Y\rangle$ [007]); отображение леммы K3 $P\to\Pi$; функция леммы 2′ $P\to\mathcal Q$; $\sigma=x^{1/N}\to\varsigma$;
    открытое множество теоремы A $G\to\mathcal O$ (буква $G$ — эффективный потенциал); радиальная производная
    $R=\langle\nabla U,q\rangle\to\mathcal EU$; $R=\sqrt{x^2+y^2}\to r_{xy}$; координата $Y$ декартовой карты $\to Y_d$.
    Номера формул: (3.1) записки (определение $\varphi$) $\to$ (U1), (3.2) $\to$ (1.1), (3.3) $\to$ (3.1), (3.4) $\to$ (3.2);
    (6.1)–(6.5) сохранены, (6.6) $\to$ (7.1); (7.1) $\to$ (8.1), (7.2) $\to$ (U2); (8.1)–(8.4) $\to$ (10.1)–(10.4), (8.5) $\to$ (U3).
24. Исследовательские части записки (§9.1–9.5, §9.8, §10.2, §12) включены только как помеченные замечания.
