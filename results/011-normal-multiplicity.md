# 011. Постоянная нормальная кратность конуса нулей ($n=3$): асимптотические траектории при вырожденном нормальном профиле

- **Статус:** [Проверено: reviewer R30, R31 (агенты), 21.10.2026 — доказательства в записке
  [`notes/prover/2026-10-21-normal-multiplicity.md`](../notes/prover/2026-10-21-normal-multiplicity.md);
  reviewer R35 (агент), 21.10.2026 — текст этого результата целиком: ошибок нет]; ждёт проверки человеком.
  - R35 ([`notes/reviewer/2026-10-21-result011.md`](../notes/reviewer/2026-10-21-result011.md)): все шаги
    §1–§10, включая лемму N5, вывод $s(t)\asymp t^{-2/(\beta-2)}$, константу $s_2'$, локальный минимум в
    N4(b), условие $g(x(t))\le\delta$ и конус $O(\sqrt\delta)$. Ошибок нет; редакционные замечания З1–З12
    учтены («Отличия от записки», «Правки по R35»). Главный агент проверил ключевую правку З2
    (условие $s<\sigma_1^N$ в определении $s_2(y_1)$, §3, п. 5).
  - R30 (reviewer, агент, 21.10.2026,
    [`notes/reviewer/2026-10-21-normal-mult-A.md`](../notes/reviewer/2026-10-21-normal-mult-A.md)):
    §1–§2 записки — постановка, лемма N1, первое ребро, леммы N2, N3, N4, определения. Ошибок нет;
    замечания З1–З11 редакционные.
  - R31 ([`...-B.md`](../notes/reviewer/2026-10-21-normal-mult-B.md)): §3–§5 записки — класс (GT3″),
    теорема 2″, теорема N, следствия N′, N″, примеры M1, M2; в §6–§8 — только метки. Ошибок нет;
    замечание 1 (оценка «конус раствора $O(\sqrt\delta)$» не выведена) закрыто дополнительным условием на
    $\sigma_*$ в теореме 2″; замечания 2–11 редакционные.
  - Все замечания R30, R31 учтены во второй редакции записки (её §9) и здесь (раздел «Отличия от
    записки»). Места, расширенные при оформлении, рецензенты не читали.
  - Метки: всё в разделе «Утверждение» — [Доказано]; лемма N3 — по модулю классической теоремы
    Ньютона–Пюизё (первоисточник не сверен). Замечания помечены каждое отдельно.
- **Автор:** prover (агент), записка `notes/prover/2026-10-21-normal-multiplicity.md` (21.10.2026).
  Оформление — prover (агент), 21.10.2026.
- **Зависит от:**
  - [007] = [`results/007-gt3.md`](007-gt3.md): теорема A, лемма 1 (формулы (0.1), (1.1), (1.3)),
    доказательство теоремы 2 (шаги 1, 3, 6; формулы (4.1), (4.2));
  - [008] = [`results/008-class-K.md`](008-class-K.md): §1 (аналитичность $\varphi$ и тождество (1.1)), лемма K3 и
    формулы (6.1), (6.2) (§6), лемма 2′ (§8, формула (8.1)), доказательство теоремы 2′ (§9), класс (GT3′);
  - стандартные факты: оценки Коши и теорема Вейерштрасса о равномерных пределах голоморфных
    функций, аналитическая теорема о неявной функции, формула Тейлора с интегральным остатком,
    подготовительная теорема Вейерштрасса и теорема Ньютона–Пюизё (только в лемме N3; [Литература:
    стандартная, например E. Casas-Alvero, *Singularities of Plane Curves*, LMS LN 276, CUP 2000, гл. 1
    «Newton–Puiseux algorithm»; сверено только название главы, текст не сверен]).
- **Проверочные скрипты** [Эксперимент]:
  - [`experiments/prover/normal-multiplicity/`](../experiments/prover/normal-multiplicity/) — автор записки
    (`frames_nm.py`, `newton_M1M2.py`, `floor_nm.py`, `exit_nm.py`);
  - `experiments/reviewer/normal-mult-R30/`, `experiments/reviewer/normal-mult-R31/` — рецензенты.

## Утверждение

### Обозначения

$\mathbb R^3$ с евклидовыми $\langle\cdot,\cdot\rangle$, $|\cdot|$, $B_r=\{|q|<r\}$. Система $\ddot q=-\nabla U(q)$;
**асимптотическая траектория** — решение $q(t)\ne0$, $t\ge0$, с $q(t)\to0$, $\dot q(t)\to0$ при $t\to+\infty$; из её
существования следует неустойчивость по Ляпунову ([007], теорема A, шаг 6). Обозначения
$p,h,v_\perp,K_\perp,W,V,\lambda,\Xi$, условия (D1)–(D4), (A4), (A5), (L0), (L1) — как в [007]; (L2′), (L3′) — как в
лемме 2′ [008].

**Дуга.** $\omega:\Lambda'\to S^2$ — аналитическая вложенная (инъективная) дуга с натуральным параметром $\theta$
на открытом интервале $\Lambda'\ni0$, $\omega(0)=\omega^*$; $\ell=\omega'$, $n=\omega\times\ell$; репер Дарбу
$$\omega'=\ell,\qquad\ell'=-\omega+k_gn,\qquad n'=-k_g\ell \tag{0.1}$$
($k_g$ — геодезическая кривизна, аналитична). По лемме K3 [008] найдутся $\theta_K>0$ и $t_1>0$ такие, что
$\Pi(s,\theta,\eta)=s\omega(\theta)+\eta n(\theta)$ — аналитический диффеоморфизм
$\mathcal P=\{s>0,\ |\theta|<\theta_K,\ |\eta|<t_1s\}$ на открытое подмножество $\mathbb R^3\setminus0$, причём
$|\Pi|^2=s^2+\eta^2$ и $\nabla s=\omega(\theta)$.

**Функция $\varphi$.** $U$ вещественно-аналитична в шаре, $U=\sum_{k\ge m}u_k$ ($u_k$ — однородные многочлены
степени $k$, $u_m\not\equiv0$, $m\ge2$), ряд Тейлора $U$ сходится абсолютно при $\max_i|q_i|\le R_0$. Положим
$$\varphi(s,\theta,y):=\sum_{k\ge m}s^{k-m}u_k\big(\omega(\theta)+y\,n(\theta)\big).$$
По [008], §1: $\varphi$ аналитична на $(-R_0/3,R_0/3)\times\Lambda'\times\{|y|<1\}$ и
$$U\big(s(\omega(\theta)+yn(\theta))\big)=s^m\varphi(s,\theta,y). \tag{0.2}$$
Коэффициенты $\varphi_{il}(\theta):=\frac1{i!\,l!}\partial_s^i\partial_y^l\varphi(0,\theta,0)$ аналитичны на $\Lambda'$; **носитель**
$\mathcal S:=\{(i,l)\in\mathbb N_0^2:\ \varphi_{il}\not\equiv0\ \text{на}\ \Lambda'\}$ (по теореме единственности $\not\equiv0$ на $\Lambda'$
равносильно $\not\equiv0$ на любом подинтервале). Предполагается $\mathcal S\ne\varnothing$.

**Нормальная кратность.** Дуга имеет **постоянную нормальную кратность $2r$** ($r\in\mathbb N$), если
$$u_m\big(\omega(\theta)+y\,n(\theta)\big)=y^{2r}a(\theta,y),\qquad a(\theta,0)>0\quad(\theta\in\Lambda'). \tag{M}$$
Тогда $\varphi_{0l}\equiv0$ при $l<2r$ и $\varphi_{0,2r}=a(\cdot,0)$. При $r=1$ это условие Морса–Ботта (K2) [008]
вдоль дуги; основной интерес — $r\ge2$, когда $D^2u_m(\omega)(n,n)=0$.

**Весовые начальные формы.** Для рационального $\gamma>0$ пусть $N$ — знаменатель $\gamma$ ($N\gamma\in\mathbb N$),
$$\beta'(\gamma):=\min\{i+\gamma l:\ (i,l)\in\mathcal S\},\qquad
\Phi_0^{(\gamma)}(\theta,\varepsilon):=\sum_{(i,l)\in\mathcal S,\ i+\gamma l=\beta'(\gamma)}\varphi_{il}(\theta)\,\varepsilon^l$$
(минимум существует, так как $i+\gamma l\in\frac1N\mathbb N_0$; сумма конечна; $\Phi_0^{(\gamma)}$ — многочлен по $\varepsilon$ с
аналитическими по $\theta$ коэффициентами).

**Первое ребро.** Если выполнено (M) и есть $(i,l)\in\mathcal S$ с $l<2r$, положим
$$\gamma_*:=\min\Big\{\frac i{2r-l}:\ (i,l)\in\mathcal S,\ l<2r\Big\},\qquad j:=m+2r\gamma_*,\qquad c:=1+\gamma_*,\qquad
G_{\min}(\theta):=\min_{\varepsilon\in\mathbb R}\Phi_0^{(\gamma_*)}(\theta,\varepsilon).$$
**Функция дна** $F_{\rm fl}(s,\theta):=\min_{|\eta|\le y_1s}U\big(s\omega(\theta)+\eta n(\theta)\big)$ ($y_1>0$ мало).

### Утверждение 1 (первое ребро)

При (M) и $\gamma_*<\infty$: $\gamma_*>0$. Многоугольник Ньютона здесь — нижняя граница выпуклой оболочки $\mathcal S+\mathbb R_+^2$ в
координатах $(l,i)$ (в $\mathcal S$ могут быть и точки $(0,l)$ с $l>2r$, то есть $(l,i)=(l,0)$). Его ребро, выходящее из вершины
$(l,i)=(2r,0)$ в сторону меньших $l$, лежит на прямой $i=\gamma_*(2r-l)$, и $\gamma_*$ — модуль наклона этого ребра;
$\beta'(\gamma_*)=2r\gamma_*$ и
$$\Phi_0^{(\gamma_*)}(\theta,\varepsilon)=a(\theta,0)\,\varepsilon^{2r}+\sum_{l<2r,\ (\gamma_*(2r-l),\,l)\in\mathcal S}\varphi_{\gamma_*(2r-l),\,l}(\theta)\,\varepsilon^l .$$
$G_{\min}$ достигается и непрерывна; $c=1+\frac{j-m}{2r}$. Числа $\gamma_*$, $j$, $c$ и функция $G_{\min}$ (как функция точки
дуги) не зависят от параметризации дуги и от выбора знака нормали. Если $(i,l)\in\mathcal S$ с $l<2r$ нет, то
$\nabla U=0$ на конусе $\{s\omega(\theta):\ 0<s<s',\ \theta\in\Lambda'\}$.

### Лемма N1 (весовое перемасштабирование)

Пусть $\Lambda\subset\Lambda'$ — компактный интервал, $\gamma>0$ рационально, $N$, $\beta'=\beta'(\gamma)$, $\Phi_0=\Phi_0^{(\gamma)}$ — как выше.
Для каждого $E>0$ найдётся $\sigma_1\in(0,1)$ такое, что ряд
$$\tilde U(\sigma,\theta,\varepsilon):=\sum_{(i,l)\in\mathcal S}\varphi_{il}(\theta)\,\sigma^{Ni+N\gamma l-N\beta'}\,\varepsilon^l$$
сходится абсолютно и равномерно на $[-\sigma_1,\sigma_1]\times\Lambda\times[-E,E]$ и задаёт функцию, вещественно-аналитическую
в окрестности этого множества, $\tilde U(0,\theta,\varepsilon)=\Phi_0(\theta,\varepsilon)$, и при $0<s<\sigma_1^N$, $\theta\in\Lambda$, $|\varepsilon|\le E$
$$U\big(s\omega(\theta)+s^{1+\gamma}\varepsilon\,n(\theta)\big)=s^{m+\beta'}\,\tilde U\big(s^{1/N},\theta,\varepsilon\big). \tag{0.3}$$

### Лемма N2 (функция дна)

Пусть выполнено (M), $\gamma_*<\infty$, $\Lambda\subset\Lambda'$ — компактный интервал, $N$ — знаменатель $\gamma_*$. Найдутся
$y_2\in(0,1)$, $C>0$ и $E\ge1$ такие, что для каждого $y_1\in(0,y_2]$ найдётся $s_2=s_2(y_1)>0$, и при $0<s<s_2$,
$\theta\in\Lambda$
$$\Big|\min_{|y|\le y_1}\varphi(s,\theta,y)-s^{2r\gamma_*}G_{\min}(\theta)\Big|\le C\,s^{2r\gamma_*+1/N},\qquad\text{то есть}\qquad
F_{\rm fl}(s,\theta)=s^{j}\big(G_{\min}(\theta)+O(s^{1/N})\big)$$
равномерно по $\theta\in\Lambda$; все точки минимума лежат в $|y|\le Es^{\gamma_*}$, так что при малых $s$ функция $F_{\rm fl}$ не
зависит от $y_1$. (Восстановить $j$ по одной $F_{\rm fl}$ можно лишь при $G_{\min}\not\equiv0$.)

### Лемма N3 (ветви критических точек в слое; по модулю теоремы Ньютона–Пюизё)

Пусть выполнено (M), $\gamma_*<\infty$, и $\theta\in\Lambda$ фиксировано. Найдутся $y_3>0$ и $s_3>0$ такие, что при
$0<s<s_3$:

- **(a)** критические точки $y\mapsto\varphi(s,\theta,y)$ в $|y|<y_3$ — значения не более чем $2r-1$ сходящихся
  рядов Пюизё $y=\psi_k(s)=\sum_{q\ge1}a_{kq}s^{q/d_k}$ с вещественными коэффициентами;
- **(b)** при $y_1\le\min(y_2,y_3)$ и всех достаточно малых $s>0$ минимум $\varphi(s,\theta,\cdot)$ по $|y|\le y_1$ достигается на
  одной и той же ветви $\psi_{k_0}$, $|\psi_{k_0}(s)|\le Es^{\gamma_*}$, и $F_{\rm fl}(s,\theta)=s^m\varphi(s,\theta,\psi_{k_0}(s))$ — сходящийся ряд
  Пюизё по $s$.

Равномерности по $\theta$ лемма не утверждает.

### Лемма N4 (невырожденная ветвь: точное дно и уточнение)

Пусть $\gamma>0$ рационально, $\Phi_0=\Phi_0^{(\gamma)}$, $\tilde U$ — из леммы N1, $\beta=m+\beta'(\gamma)$, $c=1+\gamma$; $\Lambda_1\subset\Lambda'$ —
компактный интервал; $\varepsilon_0$ аналитична в окрестности $\Lambda_1$, $\partial_\varepsilon\Phi_0(\theta,\varepsilon_0(\theta))=0$,
$\partial_\varepsilon^2\Phi_0(\theta,\varepsilon_0(\theta))>0$. Тогда:

- **(a)** есть $\sigma_2,e_2>0$ и аналитическая $\varepsilon^*(\sigma,\theta)$ на $(-\sigma_2,\sigma_2)\times\Lambda_1$, $\varepsilon^*(0,\theta)=\varepsilon_0(\theta)$, —
  единственная критическая точка $\tilde U(\sigma,\theta,\cdot)$ в $|\varepsilon-\varepsilon_0(\theta)|<e_2$, и это строгий минимум;
- **(b)** $\eta^*(s,\theta):=s^c\varepsilon^*(s^{1/N},\theta)$ — критическая точка (локальный минимум) $\eta\mapsto U(s\omega(\theta)+\eta n(\theta))$, и
  $$U(s\omega+\eta^*n)=s^\beta\hat G(s^{1/N},\theta),\qquad\hat G(\sigma,\theta):=\tilde U(\sigma,\theta,\varepsilon^*(\sigma,\theta)),\qquad\hat G(0,\theta)=\Phi_0(\theta,\varepsilon_0(\theta)),$$
  $\hat G$ аналитична (значение на дне — сходящийся ряд Пюизё по $s$ с аналитическими по $\theta$ коэффициентами);
- **(c)** если $\hat G\not\equiv0$, пусть $k:=\min\{i:\ \partial_\sigma^i\hat G(0,\cdot)\not\equiv0\ \text{на}\ \Lambda_1\}$, $\hat G=\sigma^k\hat G^{(k)}$ ($\hat G^{(k)}$ аналитична,
  $G_k(\theta):=\hat G^{(k)}(0,\theta)=\frac1{k!}\partial_\sigma^k\hat G(0,\theta)$), $M(\sigma,\theta,e):=\int_0^1(1-t)\,\partial_\varepsilon^2\tilde U(\sigma,\theta,\varepsilon^*+te)\,dt$, $\tau:=s^{1/(2N)}$,
  $c':=c+\frac k{2N}$, $\beta'':=\beta+\frac kN$. Тогда при малых $s>0$, $|e|\le1$
  $$U\big(s\omega+(\eta^*+s^{c'}e)\,n\big)=s^{\beta''}\Big[\hat G^{(k)}(\tau^2,\theta)+e^2M(\tau^2,\theta,\tau^ke)\Big];$$
  при $\tau=0$ скобка равна $G_k(\theta)+\frac12\partial_\varepsilon^2\Phi_0(\theta,\varepsilon_0)e^2$ ($k\ge1$) или $\Phi_0(\theta,\varepsilon_0+e)$ ($k=0$). Это нормальная
  форма (NF) и структурная часть (G) теоремы N ($\tilde F(0,\theta,e)=G_k(\theta)+e^2\mathsf p$, $\mathsf p>0$) с $N'=2N$, $c'$, $\beta''$,
  $y_0=\tau^{2N\gamma}\varepsilon^*(\tau^2,\theta)$, $G=G_k$, $r'=1$; знаковых условий $G(0)<0$, $G'(0)=0<G''(0)$ лемма не даёт;
- **(d)** если $\hat G\equiv0$, то $\nabla U=0$ на поверхности $\{s\omega(\theta)+\eta^*(s,\theta)n(\theta)\}$, примыкающей к $0$.

### Нормальный профиль и эффективный потенциал

Пусть выбраны рациональное $\gamma>0$ (обычно $\gamma=\gamma_*$) и **ветвь** $\varepsilon_0\in C^2$ критических точек
$\Phi_0^{(\gamma)}(\theta,\cdot)$ **постоянной кратности** $2r'-1$ ($r'\in\mathbb N$):
$$\partial_\varepsilon^k\Phi_0^{(\gamma)}(\theta,\varepsilon_0(\theta))=0\ (1\le k<2r'),\qquad\partial_\varepsilon^{2r'}\Phi_0^{(\gamma)}(\theta,\varepsilon_0(\theta))>0. \tag{E}$$
**Эффективный потенциал** $G(\theta):=\Phi_0^{(\gamma)}(\theta,\varepsilon_0(\theta))$, **нормальный профиль**
$$P(\theta,e):=\Phi_0^{(\gamma)}(\theta,\varepsilon_0(\theta)+e)-G(\theta)=e^{2r'}\mathsf p(\theta,e),\qquad\mathsf p(\theta,e)=\sum_{k\ge2r'}\frac{\partial_\varepsilon^k\Phi_0^{(\gamma)}(\theta,\varepsilon_0)}{k!}e^{k-2r'},\qquad\mathsf p(\theta,0)>0.$$
Профиль **невырожден** при $r'=1$ и **вырожден** при $r'\ge2$. Если $\varepsilon_0(\theta)$ — точка глобального минимума
$\Phi_0^{(\gamma_*)}(\theta,\cdot)$, то $G=G_{\min}$.

### Класс (GT3″) и теорема 2″ (любое $n\ge3$)

Данные — как у класса (GT3′) [008]: $U\in C^2(B_r)$, $U(0)=0$, $\nabla U(0)=0$, $\beta>0$, веса
$c=(c_1,\dots,c_{n-1})\in(0,\infty)^{n-1}$, $c_{\max}=\max c_i$, $N\in\mathbb N$, $s_0\in(0,1]$, $r_0>0$, $b=(u_ix^{-c_i})_i$,
$\mathcal N=\{(x,u):\ 0<x<s_0,\ |b|<r_0\}$, $\varsigma=x^{1/N}$, карта $\Phi\in C^2(\mathcal N;\mathbb R^n)$, $Y=(\partial_x\Phi)\circ\Phi^{-1}$,
$\rho=x\circ\Phi^{-1}$, $h=|Y|^2$. Дополнительно задано разбиение $\{1,\dots,n-1\}=I'\sqcup I''$ на два непустых
множества (поэтому $n\ge3$; при $I''=\varnothing$ это класс (GT3′) [008], случай $I'=\varnothing$ — замечание 3, п. 5),
$b'=(b_i)_{i\in I'}$, $b''=(b_i)_{i\in I''}$. $U$ **принадлежит классу (GT3″)**, если выполнены $(\Phi0)$,
$(\Phi1')$, (F) из [008] и

- **$(\Phi2'')$** при $(x,u)\in\mathcal N$ и $w\perp\partial_x\Phi(x,u)$:
  $|\langle\nabla\rho-Y/h,w\rangle|\le(\gamma_1|b'|+\varpi(x))|w|$ и $x|\langle\partial_x^2\Phi,w\rangle|\le(\gamma_2|b'|+C_1|b'|^2+\varpi(x))|w|$;
- **$(\Phi3'')$** $x\langle w,D_wY\rangle\ge-(C_1|b'|+\varpi(x))|w|^2$ для $w\perp\partial_x\Phi$;
- **$(V'')$** $F_0(0)<0$; есть $\lambda_0>0$, $\mu\in(0,\beta]$, $r_1\in(0,r_0)$ и непрерывная $q_0:[0,r_1)\to[0,\infty)$, $q_0(t)>0$ при $t>0$,
  такие, что при $|b|<r_1$
  $$Q(b)\ge\lambda_0|b'|^2+q_0(|b''|),\qquad\sum_ic_ib_i\partial_{b_i}Q(b)\ge\mu\,Q(b),$$
  и $\Gamma_*^2\le\beta\mu$, $\Gamma_*=\sqrt{a_0/\lambda_0}\,\big[\frac{3\sqrt3}2\beta\gamma_1+2\sqrt2\gamma_2\big]$ (условие (U2) [008]).

Здесь $\gamma_1,\gamma_2,C_1\ge0$, $\varpi(x)\to0$ при $x\to0$, $F_0=F(0,\cdot)$, $Q=F_0-F_0(0)$, $a_0=-F_0(0)$.

**Теорема 2″.** Если $U$ принадлежит классу (GT3″), то есть $\delta_*>0$ такое, что для каждого $\delta\in(0,\delta_*]$ есть
асимптотическая траектория $q(t)=\Phi(x(t),u(t))$, $x(t)\downarrow0$, $-k_2x^{\beta/2}\le\dot x\le-k_1x^{\beta/2}$ ($0<k_1\le k_2$), с
$b(t)\in\overline{\Omega_\delta}$ при всех $t\ge0$, где $\Omega_\delta$ — компонента связности множества $\{b\in B_{r_1}:\ Q(b)<2\delta\}$,
содержащая $0$; в частности $|b'(t)|\le\sqrt{2\delta/\lambda_0}$ и $q_0(|b''(t)|)\le2\delta$. Кроме того, для любой заданной
функции $g:(0,s_0)\to[0,\infty)$ с $g(x)\to0$ при $x\to0$ траекторию можно выбрать так, что $g(x(t))\le\delta$ при всех
$t\ge0$. Равновесие неустойчиво по Ляпунову; $\beta\ge2$.

### Теорема N ($n=3$; аналог теоремы K2 при нормальной кратности $2r\ge4$)

**(NF) — нормальная форма оврага над дугой.** Дуга $\omega$, репер (0.1), $\theta_K$, $t_1$ — как выше. Заданы $N\in\mathbb N$,
$c>1$, $\beta>0$, $\Theta\in(0,\theta_K)$, $\sigma_1>0$, $e_1>0$ и функции

- $y_0\in C^2\big([0,\sigma_1]\times[-\Theta,\Theta]\big)$ (при $\sigma=0$ — односторонние производные), $y_0(0,\theta)=0$;
- $\tilde F:[0,\sigma_1]\times[-\Theta,\Theta]\times[-e_1,e_1]\to\mathbb R$, непрерывная вместе с $\partial_\theta\tilde F$, $\partial_e\tilde F$, причём
  $\sup_{\theta,e}|\sigma\partial_\sigma\tilde F(\sigma,\theta,e)|\to0$ при $\sigma\to0$,

такие, что при $0<s\le\sigma_1^N$, $|\theta|\le\Theta$, $|e|\le e_1$
$$U\Big(s\,\omega(\theta)+\big(s\,y_0(s^{1/N},\theta)+s^c e\big)\,n(\theta)\Big)=s^\beta\,\tilde F\big(s^{1/N},\theta,e\big). \tag{NF}$$
(Производная $\partial_\sigma\tilde F$ при $\sigma>0$ существует автоматически: по (NF) $\tilde F$ — композиция $U\in C^2$ и $y_0\in C^2$.)
Обозначим $\eta_0(s,\theta):=s\,y_0(s^{1/N},\theta)$ (**приближённое дно**).

**(G) — эффективный потенциал и профиль.** $\tilde F(0,\theta,e)=G(\theta)+e^{2r'}\mathsf p(\theta,e)$, где $r'\in\mathbb N$, $G\in C^2$ и
$\mathsf p\in C^1$ в окрестности $(0,0)$, $\mathsf p_0:=\mathsf p(0,0)>0$, и
$$G(0)<0,\qquad G'(0)=0,\qquad G''(0)>0 .$$

**Теорема N.** Пусть $U\in C^2(B_r)$, $U(0)=0$, $\nabla U(0)=0$, выполнены (NF) и (G). Положим $a_0=-G(0)$, $\lambda_0=G''(0)/4$,
$\bar k_g=\max_{|\theta|\le\Theta}|k_g|$ и выберем
$$0<\kappa\le\min\Big(\frac12,\ \frac{\beta\lambda_0}{a_0\big(\frac{15\sqrt3}8\beta+2\sqrt2\big)^2}\Big). \tag{0.4}$$
Тогда $U$ принадлежит классу (GT3″) с картой (7.1) (§7), весами $(\kappa,c)$, $b=(\theta,e)$, $b'=\theta$, $b''=e$, показателями $\beta$,
$N$, $\mu=\kappa$, $\gamma_1=\frac54\kappa$, $\gamma_2=\kappa(1-\kappa)$, $C_1=\frac54\kappa^2(1+\bar k_g)+4\kappa\bar k_g$, $q_0(t)=\frac{\mathsf p_0}2t^{2r'}$. Следовательно,
есть $\delta_*>0$ такое, что для каждого $\delta\in(0,\delta_*]$ существует асимптотическая траектория
$$q(t)=s(t)\,\omega(\theta(t))+\big(\eta_0(s(t),\theta(t))+s(t)^ce(t)\big)\,n(\theta(t)),\qquad s(t)\downarrow0,\qquad-k_2s^{\beta/2}\le\dot s\le-k_1s^{\beta/2},$$
$$|\theta(t)|\le\sqrt{2\delta/\lambda_0},\qquad\mathsf p_0|e(t)|^{2r'}\le4\delta,\qquad\big|q(t)/|q(t)|-\omega^*\big|\le\sqrt\delta+\sqrt{2\delta/\lambda_0}\quad(t\ge0),$$
и равновесие неустойчиво по Ляпунову; $\beta\ge2$, и при $\beta>2$ $s(t)\asymp t^{-2/(\beta-2)}$ при $t\to+\infty$. Траектория касается конуса над
дугой: $\operatorname{dist}\big(q,\mathbb R_+\omega(\theta)\big)\le|\eta_0|+s^c|e|=o(|q|)$. Аналитичность $U$ и изолированность критической
точки не предполагаются.

### Следствие N′ (аналитический $U$, данные Ньютона)

Пусть $U$ аналитична, дуга — как выше, $\gamma>0$ рационально, $N$ — его знаменатель, $\Phi_0=\Phi_0^{(\gamma)}$, и на $[-\Theta,\Theta]$
($\Theta<\theta_K$, $[-\Theta,\Theta]\subset\Lambda'$) есть ветвь $\varepsilon_0\in C^2$ постоянной кратности (E), для которой
$G(\theta)=\Phi_0(\theta,\varepsilon_0(\theta))$ удовлетворяет $G(0)<0$, $G'(0)=0<G''(0)$. Тогда выполнены (NF), (G) с $\beta=m+\beta'(\gamma)$,
$c=1+\gamma$, $y_0(\sigma,\theta)=\sigma^{N\gamma}\varepsilon_0(\theta)$, $\tilde F(\sigma,\theta,e)=\tilde U(\sigma,\theta,\varepsilon_0(\theta)+e)$ и $\mathsf p$ из определения нормального
профиля; по теореме N есть асимптотическая траектория. При $r'=1$ достаточно, чтобы $\varepsilon_0(0)$ был
невырожденным локальным минимумом $\Phi_0(0,\cdot)$, а условия на $G$ выполнялись для ветви, продолженной по
теореме о неявной функции.

### Следствие N″ (струйный критерий)

Пусть $U\in C^{K+1}(B_r)$, $U(0)=0$, $\nabla U(0)=0$, $P:=j^KU$, и для многочлена $P$ выполнены условия следствия N′ с
показателем $\beta<K+1$. Тогда (NF), (G) выполнены и для $U$ (с теми же $y_0$, $G$, $\mathsf p$), и у $U$ есть асимптотическая
траектория.

### Примеры

Обе функции — из полигона (`experiments/numerics/2026-10-21-zoo/catalog.py`); у обеих $u_4=z^4$, и $\Sigma=\{u_4=0\}\cap S^2$ —
большой круг $z=0$: $\omega=(\cos\phi,\sin\phi,0)$, $n=e_z$, $k_g=0$, $\theta=\phi-\phi^*$; (M) выполнено с $2r=4$, $a\equiv1$.

**M1** $=(z-x^2)^4+x^5+y^5+xy^6+yx^6$. $\gamma_*=\frac14$, $N=4$, $j=5$, $c=\frac54$, $\Phi_0^{(\gamma_*)}=\varepsilon^4+G(\phi)$,
$G=\cos^5\phi+\sin^5\phi$; ветвь $\varepsilon_0\equiv0$ с вырожденным профилем $e^4$ ($r'=2$, $\mathsf p\equiv1$). Отрицательные
невырожденные минимумы $G$: $\phi^*=\pi$ и $\phi^*=\frac{3\pi}2$ ($\omega^*=-e_x$, $-e_y$), $G=-1$, $G''=5$, причём $G''+jG=0$. По
следствию N′ у M1 есть асимптотические траектории вдоль $-e_x$ и вдоль $-e_y$.

**M2** $=z^4+z(x^4+x^3y+y^4)+x^6+xz^5+2yz^5$. $\gamma_*=\frac13$, $N=3$, $j=\frac{16}3$, $c=\frac43$, $\Phi_0^{(\gamma_*)}=\varepsilon^4+f(\phi)\varepsilon$,
$f=\cos^4\phi+\cos^3\phi\sin\phi+\sin^4\phi\ge\frac18$; ветвь $\varepsilon_0=-(f/4)^{1/3}$ с невырожденным профилем ($r'=1$),
$G=-3\cdot4^{-4/3}f^{4/3}$. Невырожденные отрицательные минимумы $G$: $\phi^*=\arctan t_2\approx0.2200471$, где $t_2\in(0.22,0.23)$ —
корень $4t^3-3t^2-4t+1$ ($G\approx-0.5443867$, $G''\approx2.947325$), и $\phi=\frac\pi2$ ($G=-3\cdot4^{-4/3}$, $G''=4^{2/3}$, $G''+jG=0$), а
также $\phi^*+\pi$ и $\frac{3\pi}2$. По следствию N′ у M2 есть асимптотические траектории вдоль четырёх направлений
$\pm(\cos\phi^*,\sin\phi^*,0)$, $\pm e_y$.

## Доказательство

### 1. Утверждение 1 (первое ребро)

$(0,l)\notin\mathcal S$ при $l<2r$ по (M), поэтому в определении $\gamma_*$ все $i\ge1$ и $\gamma_*>0$; знаменатели $2r-l\in\{1,\dots,2r\}$
делят $(2r)!$, значения $\frac i{2r-l}$ лежат в дискретном множестве $\frac1{(2r)!}\mathbb N$, и минимум достигается. Для
$(i,l)\in\mathcal S$: при $l<2r$ имеем $i\ge\gamma_*(2r-l)$, то есть $i+\gamma_*l\ge2r\gamma_*$ с равенством только при $i=\gamma_*(2r-l)$; при
$l\ge2r$ $i+\gamma_*l\ge2r\gamma_*$ с равенством только в точке $(0,2r)$, которая лежит в $\mathcal S$, так как $a(\cdot,0)>0$. Отсюда
$\beta'(\gamma_*)=2r\gamma_*$ и формула для $\Phi_0^{(\gamma_*)}$; $c=1+\gamma_*=1+\frac{j-m}{2r}$.

$\Phi_0^{(\gamma_*)}(\theta,\cdot)$ — многочлен степени $2r$ со старшим коэффициентом $a(\theta,0)\ge a_{\min}>0$ на компактах, его
минимум достигается в шаре, радиус которого равномерен по $\theta$ из компакта (см. п. 3 §3), поэтому $G_{\min}$
непрерывна.

*Инвариантность.* $\varphi(s,\theta,\cdot)$ определяется точкой $\omega(\theta)$ и нормалью $n(\theta)$; перепараметризация дуги не
меняет функции в данной точке, а замена $n\to-n$ — это $y\to-y$: она сохраняет $\mathcal S$, (M) и заменяет $\Phi_0(\theta,\varepsilon)$
на $\Phi_0(\theta,-\varepsilon)$, не меняя минимума.

*Критический конус.* Если $(i,l)\in\mathcal S$ с $l<2r$ нет, то $\varphi=y^{2r}A(s,\theta,y)$ с аналитической $A$, и
$U(s\omega+\eta n)=s^{m-2r}\eta^{2r}A(s,\theta,\eta/s)$ по (0.2). На $\{\eta=0\}$ обращаются в нуль $U$ (поэтому и производные
вдоль конуса) и $\partial_\eta U$ ($2r\ge2$); так как $\Pi$ — диффеоморфизм, $\nabla U=0$ на конусе. $\square$

### 2. Лемма N1

1. $\varphi$ вещественно-аналитична в окрестности компакта $\{0\}\times\Lambda\times\{0\}$ и продолжается до голоморфной
   функции в комплексной окрестности. Найдутся $\rho_s,\rho_y\in(0,1)$ с $2\rho_s<R_0/3$, комплексная окрестность
   $V\supset\Lambda$ и $M>0$ такие, что продолжение голоморфно и по модулю не больше $M$ на
   $\{|s|\le2\rho_s\}\times\overline V\times\{|y|\le2\rho_y\}$. По оценкам Коши (по $(s,y)$ при фиксированном $\theta\in V$)
   $|\varphi_{il}(\theta)|\le M(2\rho_s)^{-i}(2\rho_y)^{-l}$ на $V$, и $\varphi=\sum\varphi_{il}(\theta)s^iy^l$ при $|s|<2\rho_s$, $|y|<2\rho_y$.
2. Для $(i,l)\in\mathcal S$ показатель $k_{il}:=Ni+N\gamma l-N\beta'$ — целое $\ge0$. Возьмём $\sigma_1$ с $(2\sigma_1)^N\le\rho_s$ и
   $(2\sigma_1)^{N\gamma}2E\le\rho_y$. При $|\sigma|\le2\sigma_1$, $|\varepsilon|\le2E$, $\theta\in V$
   $$|\varphi_{il}(\theta)\sigma^{k_{il}}\varepsilon^l|\le M(2\rho_s)^{-i}(2\rho_y)^{-l}(2\sigma_1)^{Ni}\big((2\sigma_1)^{N\gamma}2E\big)^l(2\sigma_1)^{-N\beta'}\le M(2\sigma_1)^{-N\beta'}2^{-i-l},$$
   так что ряд сходится абсолютно и равномерно, его сумма голоморфна на $\{|\sigma|<2\sigma_1\}\times V\times\{|\varepsilon|<2E\}$, а сужение
   вещественно-аналитично в окрестности $[-\sigma_1,\sigma_1]\times\Lambda\times[-E,E]$. Члены с $(i,l)\notin\mathcal S$ тождественно равны нулю.
3. При $\sigma=0$ остаются члены с $k_{il}=0$: $\tilde U(0,\cdot)=\Phi_0$.
4. При $0<\sigma<\sigma_1$, $s=\sigma^N$: $\sigma^{N\beta'}\tilde U=\sum\varphi_{il}(\theta)s^i(s^\gamma\varepsilon)^l=\varphi(s,\theta,s^\gamma\varepsilon)$ (перегруппировка абсолютно
   сходящегося ряда; $s<\rho_s$, $|s^\gamma\varepsilon|<\rho_y$). По (0.2) $U\big(s(\omega+s^\gamma\varepsilon n)\big)=s^{m+\beta'}\tilde U(\sigma,\theta,\varepsilon)$. $\square$

### 3. Лемма N2

1. *Разложение.* В области из п. 1 §2 $\varphi=y^{2r}A(s,\theta,y)+\sum_{l=0}^{2r-1}y^lB_l(s,\theta)$, $B_l=\sum_i\varphi_{il}s^i$,
   $A=\sum_{l\ge2r}\sum_i\varphi_{il}s^iy^{l-2r}$, $A(0,\theta,0)=a(\theta,0)$. Пусть $a_{\min}=\min_\Lambda a(\cdot,0)>0$; при малых $y_2,s_2'\le1$
   $A\ge a_{\min}/2$ для $|s|\le s_2'$, $|y|\le y_2$, $\theta\in\Lambda$. В $B_l$ ($l<2r$) участвуют только $i\ge i_l:=\lceil\gamma_*(2r-l)\rceil$, и по
   оценкам Коши $|B_l(s,\theta)|\le C_Bs^{i_l}\le C_Bs^{\gamma_*(2r-l)}$ при $0\le s\le s_2'$.
2. *Внешняя зона.* При $E\ge1$, $Es^{\gamma_*}\le|y|\le y_2$: $s^{\gamma_*}\le|y|/E$, $|y^lB_l|\le C_B|y|^l(|y|/E)^{2r-l}\le C_BE^{-1}|y|^{2r}$, откуда
   $\varphi\ge(a_{\min}/2-2rC_B/E)|y|^{2r}\ge\frac{a_{\min}}4|y|^{2r}\ge\frac{a_{\min}}4E^{2r}s^{2r\gamma_*}$ при $E\ge8rC_B/a_{\min}$.
3. *Минимумы $\Phi_0$.* $\Phi_0(\theta,\varepsilon)-\Phi_0(\theta,0)\ge a_{\min}|\varepsilon|^{2r}-\sum_{1\le l<2r}C'|\varepsilon|^l>0$ при $|\varepsilon|\ge E_0$ ($C'$ — максимум
   модулей коэффициентов на $\Lambda$). Значит, $G_{\min}$ достигается в $|\varepsilon|<E_0$, и $|G_{\min}|\le G_+$ на $\Lambda$.
4. *Внутренняя зона.* Возьмём $E\ge\max\big(1,E_0,8rC_B/a_{\min},(4(G_++1)/a_{\min})^{1/(2r)}\big)$ и лемму N1 с этим $E$. При
   $|y|\le Es^{\gamma_*}$, то есть $y=s^{\gamma_*}\varepsilon$, $|\varepsilon|\le E$: $\varphi=s^{2r\gamma_*}\tilde U(\sigma,\theta,\varepsilon)$ и $|\tilde U-\Phi_0|\le C_E\sigma$ ($\tilde U\in C^1$ на компакте).
   Минимум по внутренней зоне лежит в $s^{2r\gamma_*}[G_{\min}-C_E\sigma,\ G_{\min}+C_E\sigma]$.
5. Во внешней зоне $\varphi\ge(G_++1)s^{2r\gamma_*}\ge(G_{\min}+1)s^{2r\gamma_*}$. Пусть $s_2(y_1)$ таково, что при $s<s_2$: $s\le s_2'$, $s<\sigma_1^N$
   ($\sigma_1=\sigma_1(E)$ из леммы N1, чтобы в п. 4 работали (0.3) и оценка $|\tilde U-\Phi_0|\le C_E\sigma$), $C_E\sigma<1$, $Es^{\gamma_*}\le y_1$. Тогда все точки минимума по $|y|\le y_1$ лежат во внутренней зоне, и минимум равен
   $s^{2r\gamma_*}(G_{\min}+O(\sigma))$ с $C=C_E$, не зависящей от $y_1$. Наконец, $F_{\rm fl}=s^m\min_{|y|\le y_1}\varphi$ по (0.2) ($\eta=sy$). $\square$

### 4. Лемма N3

$f(s,y):=\partial_y\varphi(s,\theta,y)$ аналитична около $(0,0)$, $f(0,y)=y^{2r-1}(2ra(\theta,0)+O(y))$ — порядка $2r-1$. По
подготовительной теореме Вейерштрасса $f=e\cdot W$, $e(0,0)\ne0$, $W$ — многочлен Вейерштрасса степени $2r-1$ по $y$; при
$|s|<s_3$ у $f(s,\cdot)$ в $|y|<y_3$ ровно $2r-1$ нулей с кратностями. По теореме Ньютона–Пюизё (нужна её сходящаяся форма: корни
многочлена Вейерштрасса со сходящимися коэффициентами задаются сходящимися рядами Пюизё; [Литература:
Casas-Alvero, гл. 1 — по R35 сверено только оглавление, текст главы не сверен]) при
$0<s<s_3$ это значения сходящихся рядов Пюизё $\psi_k(s)$ (коэффициенты, вообще говоря, комплексные), $\psi_k(0)=0$. При $s>0$
$\operatorname{Im}\psi_k(s)$ — сходящийся вещественный ряд Пюизё: либо $\equiv0$ (тогда все коэффициенты вещественны), либо $\ne0$ при
всех малых $s>0$. Это (a).

(b) При $Es^{\gamma_*}\le y_1$ по п. 2 §3 $\varphi(s,\theta,\pm y_1)\ge\frac{a_{\min}}4y_1^{2r}>0$, а $\varphi(s,\theta,0)=B_0(s,\theta)\to0$; значит, при малых $s$
минимум достигается внутри, в критической точке, то есть на вещественной ветви. Разности $\varphi(s,\theta,\psi_k(s))-\varphi(s,\theta,\psi_{k'}(s))$
— сходящиеся ряды Пюизё (подстановка $s=\tau^d$ даёт аналитические функции $\tau$), каждая $\equiv0$ или знакопостоянна при малых
$s>0$; поэтому минимальная ветвь при малых $s$ одна и та же. $|\psi_{k_0}|\le Es^{\gamma_*}$ — п. 5 §3. $\square$

### 5. Лемма N4

Лемма N1 применяется с компактным $\Lambda$, $\Lambda_1\subset\Lambda\subset\Lambda'$, и $E:=\max_{\Lambda_1}|\varepsilon_0|+2$ (сам ряд $\tilde U$ от $E$ не
зависит); в (a) берём $e_2\le1$ и $\sigma_2\le\sigma_1(E)$. Тогда при $|\varepsilon^*-\varepsilon_0|<e_2$ и $|e|\le1$ отрезок $[\varepsilon^*,\varepsilon^*+e]$ лежит в
$|\varepsilon|\le E$, то есть в области (0.3).

(a) На компакте $\{|\sigma|\le\sigma_2,\ \theta\in\Lambda_1,\ |\varepsilon-\varepsilon_0(\theta)|\le e_2\}$ при малых $\sigma_2\le\sigma_1(E)$, $e_2\le1$ по непрерывности $\partial_\varepsilon^2\tilde U\ge c_0>0$ и
$\pm\partial_\varepsilon\tilde U(\sigma,\theta,\varepsilon_0\pm e_2)>0$; строгая выпуклость даёт единственную критическую точку (строгий минимум), аналитическая
теорема о неявной функции — её аналитичность.

(b) Дифференцируя (0.3) по $\varepsilon$: $s^c\partial_\eta U(s\omega+s^c\varepsilon n)=s^\beta\partial_\varepsilon\tilde U$, это $0$ при $\varepsilon=\varepsilon^*$; и $s^{2c}\partial_\eta^2U=s^\beta\partial_\varepsilon^2\tilde U>0$.
Остальное — (0.3) при $\varepsilon=\varepsilon^*$.

(c) Формула Тейлора по $\varepsilon$ в $\varepsilon^*$ ($\partial_\varepsilon\tilde U=0$): $\tilde U(\sigma,\theta,\varepsilon^*+e_1)=\hat G+e_1^2M(\sigma,\theta,e_1)$. Подставим $e_1=\tau^ke$,
$\sigma=\tau^2$: $s^\beta\tilde U=s^\beta\tau^{2k}[\hat G^{(k)}(\tau^2,\theta)+e^2M(\tau^2,\theta,\tau^ke)]$, где $s^\beta\tau^{2k}=s^{\beta''}$ и $s^c\tau^ke=s^{c'}e$. При $\tau=0$:
$M(0,\theta,0)=\frac12\partial_\varepsilon^2\Phi_0(\theta,\varepsilon_0)$ (при $k\ge1$ аргумент $\tau^ke$ обращается в нуль). Наконец,
$\eta^*=s\cdot s^\gamma\varepsilon^*=s\cdot\tau^{2N\gamma}\varepsilon^*(\tau^2,\theta)$, $y_0$ аналитична и $y_0(0,\cdot)=0$ ($N\gamma\ge1$), скобка аналитична по
$(\tau,\theta,e)$ — требования (NF) и структурной части (G) выполнены.

(d) Если $U(s\omega+\eta^*n)\equiv0$, то $\langle\nabla U,n\rangle=0$ на поверхности по (b), а дифференцирование тождества по $s$ и $\theta$ с
(0.1) даёт $\langle\nabla U,\omega+\eta^*_sn\rangle=0$ и $\langle\nabla U,(s-k_g\eta^*)\ell+\eta^*_\theta n\rangle=0$, откуда $\langle\nabla U,\omega\rangle=\langle\nabla U,\ell\rangle=0$
($s-k_g\eta^*\ne0$ при малых $s$). Точки поверхности ненулевые и стремятся к $0$. $\square$

### 6. Теорема 2″

Повторяем доказательство теоремы 2′ [008] (§9; оно повторяет доказательство теоремы 2 [007], §4), меняя шаг 2 и
константы шагов 4–5.

*Шаг 1* — дословно шаг 1 [008], §9: $\mathcal O=\Phi(\mathcal N)$, $\rho\in C^2$, $Y\in C^1$, $Y\rho=1$, $A(r)=a_0r^\beta$,
$W\circ\Phi=x^\beta(F-F_0(0))$, $\beta W-\rho\,YW=x^\beta\big[\sum_ic_ib_i\partial_{b_i}F-\frac\varsigma N\partial_\varsigma F\big]$ ((4.1), (4.2) [007]). Используются только
$(\Phi0)$, $Y\circ\Phi=\partial_x\Phi$, $b_i=u_ix^{-c_i}$ и (F).

*Шаг 2: множество $\Omega_\delta$.* Положим $\delta_1:=\min\big(\frac{\lambda_0r_1^2}{32},\frac{q_0(r_1/4)}2\big)>0$, $0<\delta\le\delta_1$.

- (2a) *$\overline{\Omega_\delta}\subset\{|b'|\le r_1/4,\ |b''|\le r_1/4\}\subset B_{r_1}$.* На $\Omega_\delta\subset B_{r_1}$: $\lambda_0|b'|^2\le Q<2\delta\le\lambda_0r_1^2/16$, так что
  $|b'|<r_1/4$. $\Omega_\delta$ открыто и связно, значит, линейно связно, и его образ при $b\mapsto|b''|$ — промежуток с нулём. Точка с
  $|b''|\ge r_1/4$ дала бы точку $\Omega_\delta$ с $|b''|=r_1/4$, где $Q\ge q_0(r_1/4)\ge2\delta$, — противоречие. Итак, $|b|<r_1/(2\sqrt2)$ на $\Omega_\delta$.
- (2b) *$Q=2\delta$ на $\partial\Omega_\delta$.* Для $b_0\in\partial\Omega_\delta$: $b_0\in B_{r_1}$, $Q(b_0)\le2\delta$; если $Q(b_0)<2\delta$, то шар вокруг $b_0$ лежит в
  $\{b\in B_{r_1}:Q<2\delta\}$, связен и пересекает $\Omega_\delta$, поэтому лежит в $\Omega_\delta$, и $b_0\in\Omega_\delta$ — невозможно.
- Свойства шага 2 [007] с $\Omega_b':=\Omega_\delta$: (i) $Q\ge0$ на $\Omega_\delta$; (ii) $Q=\delta+\kappa'$ на $\partial\Omega_\delta$, $\kappa':=\delta$; (iii) неравенство
  Эйлера на $\overline{\Omega_\delta}\subset B_{r_1}$; (iv) $R_b:=\sup_{\Omega_\delta}|b|\le r_1/2$. Кроме того, (v) $R':=\sup_{\Omega_\delta}|b'|\le\sqrt{2\delta/\lambda_0}$ и (vi)
  $|b'|\le\sqrt{Q(b)/\lambda_0}$ на $\overline{\Omega_\delta}$.

*Шаг 3* — дословно шаг 3 [007]: $\chi$, $\bar\chi$, порог $\sigma_*<s_0$ по $x$ с $\bar\chi(\sigma_*^{1/N})<\min(\delta,\kappa'/2)=\delta/2$,
$\mathcal D=\{x<\sigma_*,\ b\in\Omega_\delta,\ F-F_0(0)<\delta\}$, $D=\Phi(\mathcal D)$; проверка (D1)–(D3) использует только $(\Phi0)$, (F), открытость
$\Omega_\delta$, $0\in\Omega_\delta$, компактность $\overline{\Omega_\delta}\subset B_{r_0}$ и (ii). Ниже $\chi:=\bar\chi(\sigma_*^{1/N})$, $\bar\varpi:=\sup_{x<\sigma_*}\varpi(x)$.

*Шаг 4: константы леммы 2′ [008] на $D_{\sigma_*}$.* Каждая точка $D_{\sigma_*}$ — это $\Phi(x,u)$ с $x<\sigma_*$, $b\in\overline{\Omega_\delta}$, $F-F_0(0)\le\delta$.

- (L0): $a_1=a_3=a_0$, $a_2=\beta a_0$, $\delta\le a_0/2$; (L1): $h_0=\frac12$, $h_1=\frac32$ по $(\Phi1')$.
- (L2′): $\mathcal Q:=x^\beta Q(b)\ge0$; $|W-\mathcal Q|=x^\beta|F-F_0(b)|\le\chi x^\beta$, $\varepsilon_0=\chi/\delta$; по (4.2) [007], неравенству
  Коши–Буняковского и (iii) $\beta W-\rho\,YW\ge x^\beta[\mu Q-c_{\max}R_b\chi-\chi/N]$, $\varepsilon_1=(c_{\max}R_b+1/N)\chi/\delta$.
- (L3′): по (vi) $|b'|\le\sqrt{\mathcal Q/(\lambda_0\rho^\beta)}$. По $(\Phi2'')$: $\theta_1=\bar\varpi$, $\gamma_1'=\gamma_1/\sqrt{\lambda_0}$. Так как $\nabla_YY=\partial_x^2\Phi$, по
  $(\Phi2'')$ и (v): $\theta_2=C_1R'^2+\bar\varpi\le2C_1\delta/\lambda_0+\bar\varpi$, $\gamma_2'=\gamma_2/\sqrt{\lambda_0}$. По $(\Phi3'')$ и (v):
  $\theta_3=C_1R'+\bar\varpi\le C_1\sqrt{2\delta/\lambda_0}+\bar\varpi$.
- $\Gamma'\le\Gamma_*$ (выкладка [008], §9, п. 4), и по (U2) $\Gamma'^2\le\beta\mu$.

*Шаг 5: выбор $\delta$ и $\sigma_*$.* $L_1=3\beta\sqrt{3a_0/2}$, $L_2=4\sqrt{a_0}$. Члены (8.1) [008], зависящие только от $\delta$:
$\frac{L_2\cdot2C_1\delta/\lambda_0}{\sqrt\delta}+4C_1\sqrt{2\delta/\lambda_0}=C_1\sqrt\delta\big(\frac{8\sqrt{a_0}}{\lambda_0}+\frac{4\sqrt2}{\sqrt{\lambda_0}}\big)$ и (для п. 1 леммы 2′) $8\gamma_1'\delta$. Пусть
$\delta_*\le\min(a_0/2,\delta_1)$ таково, что при $\delta\le\delta_*$ первое $\le\mu/8$, а $8\gamma_1'\delta\le\frac12\sqrt{a_0/h_1}$. Для данного $\delta\in(0,\delta_*]$
выберем $\sigma_*$ так, чтобы $\varepsilon_0\le\frac14$, $\varepsilon_1\le\frac\mu{16}$, $\frac{(L_1+L_2)\bar\varpi}{\sqrt\delta}+4\bar\varpi\le\frac\mu{16}$, $4\sqrt\delta\,\bar\varpi\le\frac12\sqrt{a_0/h_1}$ и
$\sup_{x<\sigma_*}g(x)\le\delta$ (все условия — оценки сверху; их правые части стремятся к $0$ при $\sigma_*\to0$). Тогда выполнено условие
п. 1 леммы 2′, $\varepsilon_0\le\frac12$, и скобка в (8.1) [008] не меньше $\frac\mu2\cdot\frac34-\frac\mu{16}-\frac\mu8-\frac\mu{16}=\frac\mu8>0$.

*Шаг 6.* Лемма 2′ [008] даёт (D4), (A4), (A5); теорема A [007] — решение $(q(t),v(t))\in\overline\Omega$, $q(t)\ne0$, $q,v\to0$, и
неустойчивость. Как в шаге 6 [007]: $q(t)\in D_{\sigma_*}$, $q=\Phi(x,u)$, $x=\rho(q)<\sigma_*$ (поэтому $g(x(t))\le\delta$); п. 1 леммы 2′ даёт
$-k_2x^{\beta/2}\le\dot x\le-k_1x^{\beta/2}$ с $k_1=\frac12\sqrt{a_0/h_1}$, $k_2=\sqrt{2(a_0+\delta/2)/h_0}+k_1$; $b(t)\in\overline{\Omega_\delta}$. $\beta\ge2$ — как п. 1 шага 6
[007] (нужны только $(\Phi0)$, $|\partial_x\Phi|=\sqrt h\le\sqrt{3/2}$, (F) с $F_0(0)\ne0$ и $U\in C^2$). $\square$

### 7. Карта теоремы N, формулы и малые величины

**Карта.** При $0<\kappa\le\frac12$
$$\Phi(x,u,\zeta):=\Psi(x,\theta,\zeta),\quad\theta:=u\,x^{-\kappa};\qquad\Psi(s,\theta,\zeta):=s\,\omega(\theta)+\big(\eta_0(s,\theta)+\zeta\big)\,n(\theta);\qquad b=(\theta,e)=(ux^{-\kappa},\ \zeta x^{-c}). \tag{7.1}$$
Обозначим $\eta=\eta_0+\zeta$, $\epsilon:=k_g(\theta)\eta/s$, $\nu:=\eta_{0,s}-\kappa\theta\,\eta_{0,\theta}/s$ (в точках карты $s=x$). Прямым дифференцированием
с (0.1) [Доказано; [Эксперимент] `frames_nm.py` и независимо R31, `frames_R31.py`: символьно с общими $\eta_0$, $k_g$]:
$$\Psi_s=\omega+\eta_{0,s}n,\qquad\Psi_\theta=s(1-\epsilon)\ell+\eta_{0,\theta}n,\qquad\Psi_\zeta=n; \tag{7.2}$$
$$Y=\partial_x\Phi=\Psi_s-\frac{\kappa\theta}x\Psi_\theta=\omega-\kappa\theta(1-\epsilon)\ell+\nu n,\qquad h=1+\kappa^2\theta^2(1-\epsilon)^2+\nu^2; \tag{7.3}$$
$$x\,\partial_x^2\Phi=-\kappa\theta\big[(1-\kappa)+\kappa\epsilon-x\partial_x\epsilon-\nu k_g\big]\ell+\kappa^2\theta^2(1-\epsilon)(-\omega+k_gn)+x\partial_x\nu\,n, \tag{7.4}$$
где $x\partial_x=s\partial_s-\kappa\theta\partial_\theta$ — производная при постоянных $(u,\zeta)$, и $x\partial_x\epsilon=-\kappa\theta k_g'\eta/x+k_g\nu-\epsilon$. [Вывод (7.4):
$\frac{d\theta}{dx}=-\frac{\kappa\theta}x$, $\frac{d\omega}{dx}=-\frac{\kappa\theta}x\ell$, $\frac{d\ell}{dx}=-\frac{\kappa\theta}x(-\omega+k_gn)$, $\frac{dn}{dx}=\frac{\kappa\theta}xk_g\ell$, $\frac{d\eta}{dx}=\nu$; продифференцировать (7.3).]
Как поле в координатах $(s,\theta,\zeta)$: $Y=\omega-\kappa\theta(1-\epsilon)\ell+\nu n$ с $\epsilon=k_g(\eta_0+\zeta)/s$, $\nu=\eta_{0,s}-\kappa\theta\eta_{0,\theta}/s$, и
$$\partial_\theta Y=\kappa\theta(1-\epsilon)\omega+\big[1-\kappa(1-\epsilon)+\kappa\theta\partial_\theta\epsilon-\nu k_g\big]\ell+\big[-\kappa\theta(1-\epsilon)k_g+\partial_\theta\nu\big]n,\quad
\partial_sY=\kappa\theta\partial_s\epsilon\,\ell+\partial_s\nu\,n,\quad\partial_\zeta Y=\frac{\kappa\theta k_g}s\ell, \tag{7.5}$$
$s\partial_s\epsilon=k_g\eta_{0,s}-\epsilon$. Для $w=w_\omega\omega+w_\ell\ell+w_nn$: $w=a^s\Psi_s+a^\theta\Psi_\theta+a^\zeta\Psi_\zeta$ с $a^s=w_\omega$, $a^\theta=\frac{w_\ell}{s(1-\epsilon)}$,
$a^\zeta=w_n-w_\omega\eta_{0,s}-\frac{w_\ell\eta_{0,\theta}}{s(1-\epsilon)}$, и $D_wY=a^s\partial_sY+a^\theta\partial_\theta Y+a^\zeta\partial_\zeta Y$, откуда
$$x\langle w,D_wY\rangle=w_\ell^2\Big(\frac1{1-\epsilon}-\kappa\Big)+\mathcal E_r, \tag{7.6}$$
$$\mathcal E_r=\frac{w_\ell}{1-\epsilon}\Big[(\kappa\theta\partial_\theta\epsilon-\nu k_g)w_\ell+\big(-\kappa\theta(1-\epsilon)k_g+\partial_\theta\nu\big)w_n\Big]+\kappa\theta\,w_\ell w_\omega+w_\omega\big[\kappa\theta\,s\partial_s\epsilon\,w_\ell+s\partial_s\nu\,w_n\big]+a^\zeta\kappa\theta k_gw_\ell .$$
Если $w\perp Y$, то $w_\omega=\kappa\theta(1-\epsilon)w_\ell-\nu w_n$. Формулы (7.2)–(7.5) совпадают с (6.4), (10.2)–(10.4) [008] (там $\eta^*$ аналитично
по $s$; здесь — тождества для любого $\eta_0\in C^2$ при $s>0$).

**Лемма N5 (малые величины).** Пусть $r_0\le\min(\Theta/2,e_1,\frac14)$. На $\{0<s<\sigma_1^N,\ |\theta|\le r_0,\ |\zeta|\le r_0s^c\}$ величины
$$\frac\eta s,\ \epsilon,\ \nu,\ \eta_{0,s},\ \frac{\eta_{0,\theta}}s,\ \partial_\theta\epsilon,\ s\partial_s\epsilon,\ \partial_\theta\nu,\ s\partial_s\nu,\ x\partial_x\epsilon,\ x\partial_x\nu$$
стремятся к $0$ при $s\to0$ равномерно по $(\theta,\zeta)$.

*Доказательство.* С $\sigma=s^{1/N}$, $\frac d{ds}=\frac\sigma{Ns}\frac d{d\sigma}$:
$$\frac{\eta_0}s=y_0,\quad\eta_{0,s}=y_0+\tfrac\sigma Ny_{0,\sigma},\quad\frac{\eta_{0,\theta}}s=y_{0,\theta},\quad s\eta_{0,ss}=\tfrac\sigma N\big[(1+\tfrac1N)y_{0,\sigma}+\tfrac\sigma Ny_{0,\sigma\sigma}\big],\quad\eta_{0,s\theta}=y_{0,\theta}+\tfrac\sigma Ny_{0,\sigma\theta},\quad\frac{\eta_{0,\theta\theta}}s=y_{0,\theta\theta}.$$
Так как $y_0\in C^2$ на компакте и $y_0(0,\cdot)\equiv0$ (значит, $y_{0,\theta}(0,\cdot)=y_{0,\theta\theta}(0,\cdot)=0$), эти шесть величин стремятся к $0$
равномерно. Далее $|\zeta|/s\le r_0s^{c-1}\to0$ ($c>1$). Отсюда $\epsilon=k_g(\eta_0+\zeta)/s\to0$, $\nu\to0$, $s\partial_s\epsilon=k_g\eta_{0,s}-\epsilon\to0$,
$\partial_\theta\epsilon=(k_g'\eta+k_g\eta_{0,\theta})/s\to0$, $\partial_\theta\nu=\eta_{0,s\theta}-\kappa\eta_{0,\theta}/s-\kappa\theta\eta_{0,\theta\theta}/s\to0$,
$s\partial_s\nu=s\eta_{0,ss}-\kappa\theta(\eta_{0,s\theta}-\eta_{0,\theta}/s)\to0$, $x\partial_x\epsilon=-\kappa\theta k_g'\eta/x+k_g\nu-\epsilon\to0$,
$x\partial_x\nu=s\partial_s\nu-\kappa\theta\partial_\theta\nu\to0$ ($k_g$, $k_g'$ ограничены). $\square$

Пусть $\varpi_1(x)$ — супремум суммы модулей восьми величин $\epsilon,\nu,\partial_\theta\epsilon,s\partial_s\epsilon,\partial_\theta\nu,s\partial_s\nu,x\partial_x\epsilon,x\partial_x\nu$ по $\{s\le x\}$
(и $|\theta|\le r_0$, $|\zeta|\le r_0s^c$); $\varpi_1\to0$. Положим $\varpi:=10(1+\bar k_g)\varpi_1$.

### 8. Доказательство теоремы N

*Порядок выбора констант.* $\kappa$ — по (0.4); $r_1$ — по п. 7 ниже (не зависит от $\kappa\le\frac12$), причём $r_1<\min(\Theta/2,e_1,\frac14)$ и
квадрат $\{|\theta|,|e|\le r_1\}$ лежит в окрестности $(0,0)$, где $\mathsf p\in C^1$ и $G\in C^2$; затем $r_0\in(r_1,\min(\Theta/2,e_1,\frac14)]$; затем
$s_0<\min(1,\sigma_1^N)$ так, что на $\mathcal N=\{0<x<s_0,\ |b|<r_0\}$: $|\epsilon|\le\frac14$, $|\nu|\le\frac14$, $|\eta_{0,s}|+\frac43|\eta_{0,\theta}|/x\le1$, $|\eta|<\min(t_1,\frac14)x$
(лемма N5) и $\Phi(\mathcal N)\subset B_r$; затем $C_1$, $\varpi$; $\delta$ и $\sigma_*$ — внутри теоремы 2″.

1. **$(\Phi0)$.** $\Phi=\Pi\circ T\circ L$: $L(x,u,\zeta)=(x,ux^{-\kappa},\zeta)$ — $C^\infty$-диффеоморфизм $\{x>0\}\times\mathbb R^2$ на себя;
   $T(s,\theta,\zeta)=(s,\theta,\eta_0(s,\theta)+\zeta)$ — $C^2$-диффеоморфизм $\{0<s<\sigma_1^N,\ |\theta|<\Theta\}\times\mathbb R$ на себя (обратный
   $(s,\theta,\eta)\mapsto(s,\theta,\eta-\eta_0)$; $\eta_0\in C^2$ при $s>0$, так как $s\mapsto s^{1/N}$ аналитично); $T(L(\mathcal N))\subset\mathcal P$ по выбору $s_0$;
   $\Pi$ — аналитический диффеоморфизм $\mathcal P$ на открытое множество (лемма K3 [008]). $|\Phi|^2=x^2+\eta^2$, $|\eta|\le x/4$, поэтому
   $x\le|\Phi|\le2x$.
2. **$(\Phi1')$.** По (7.3) $1\le h\le1+\frac14\cdot\frac1{16}\cdot\frac{25}{16}+\frac1{16}<\frac32$.
3. **$(\Phi2'')$, первая оценка.** $\nabla\rho=\nabla s=\omega(\theta)$ (лемма K3: $s$ — та же функция на $\mathbb R^3$, что для $\Pi$). Для $w\perp Y$:
   $\langle\nabla\rho-Y/h,w\rangle=\langle\omega,w\rangle=\kappa\theta(1-\epsilon)w_\ell-\nu w_n$, так что $|\langle\nabla\rho-Y/h,w\rangle|\le(\frac54\kappa|\theta|+|\nu|)|w|$:
   $\gamma_1=\frac54\kappa$, $|\nu|\le\varpi$.
4. **$(\Phi2'')$, вторая оценка.** По (7.4) для $|w|=1$ ($|\langle-\omega+k_gn,w\rangle|\le1+\bar k_g$, $\kappa|\theta|\le\frac18$):
   $|\langle x\partial_x^2\Phi,w\rangle|\le\kappa(1-\kappa)|\theta|+\frac54\kappa^2(1+\bar k_g)\theta^2+\frac18(\kappa|\epsilon|+|x\partial_x\epsilon|+\bar k_g|\nu|)+|x\partial_x\nu|\le\gamma_2|\theta|+C_1\theta^2+\varpi$.
5. **$(\Phi3'')$.** По (7.6) главный член $\ge(\frac45-\frac12)w_\ell^2\ge0$ ($|\epsilon|\le\frac14$). Для $w\perp Y$: $|w_\omega|\le(\frac54\kappa|\theta|+|\nu|)|w|\le|w|$,
   $|a^\zeta|\le|w_n|+|w|(|\eta_{0,s}|+\frac43|\eta_{0,\theta}|/x)\le2|w|$, $\frac1{1-\epsilon}\le\frac43$. Почленно:
   - первый член $\mathcal E_r$: $\le\big[\frac53\kappa\bar k_g|\theta|+\frac43(|\partial_\theta\epsilon|+\bar k_g|\nu|+|\partial_\theta\nu|)\big]|w|^2$;
   - $|\kappa\theta w_\ell w_\omega|\le(\frac54\kappa^2r_0|\theta|+|\nu|)|w|^2$;
   - $|w_\omega[\dots]|\le(|s\partial_s\epsilon|+|s\partial_s\nu|)|w|^2$;
   - $|a^\zeta\kappa\theta k_gw_\ell|\le2\kappa\bar k_g|\theta||w|^2$.

   Итого $|\mathcal E_r|\le\big[(\frac{11}3\kappa\bar k_g+\frac5{16}\kappa^2)|\theta|+6(1+\bar k_g)\varpi_1\big]|w|^2\le(C_1|\theta|+\varpi)|w|^2$, и $x\langle w,D_wY\rangle\ge-(C_1|b'|+\varpi)|w|^2$.
6. **(F).** $U(\Phi(x,u,\zeta))=U\big(x\omega(\theta)+(\eta_0(x,\theta)+x^ce)n(\theta)\big)=x^\beta\tilde F(x^{1/N},\theta,e)$ по (NF) ($|\theta|<r_0\le\Theta$, $|e|<r_0\le e_1$);
   $F(\varsigma,b):=\tilde F(\varsigma,\theta,e)$ непрерывна вместе с $\nabla_bF$ на $[0,s_0^{1/N})\times B_{r_0}$, и $\sup|\varsigma\partial_\varsigma F|\to0$.
7. **$(V'')$.** $F_0(\theta,e)=G(\theta)+e^{2r'}\mathsf p(\theta,e)$, $F_0(0)=-a_0<0$, $Q=G(\theta)-G(0)+e^{2r'}\mathsf p$. Возьмём $r_1$ так, что при $|\theta|,|e|<r_1$:
   $G(\theta)-G(0)\ge\frac14G''(0)\theta^2$ и $\theta G'(\theta)-(G(\theta)-G(0))\ge\frac14G''(0)\theta^2$ (обе левые части равны $\frac12G''(0)\theta^2+o(\theta^2)$, так как
   $G\in C^2$, $G'(0)=0$), $\mathsf p\ge\mathsf p_0/2$ и $c|e\,\partial_e\mathsf p|+|\theta\,\partial_\theta\mathsf p|\le\frac14(2r'c-\frac12)\mathsf p_0$. Тогда $Q\ge\lambda_0\theta^2+\frac{\mathsf p_0}2e^{2r'}=\lambda_0|b'|^2+q_0(|b''|)$, и
   при $\mu=\kappa$
   $$\kappa\theta\partial_\theta Q+c\,e\,\partial_eQ-\kappa Q=\kappa\big[\theta G'-(G-G(0))\big]+e^{2r'}\big[(2r'c-\kappa)\mathsf p+c\,e\,\partial_e\mathsf p+\kappa\theta\,\partial_\theta\mathsf p\big]\ge0,$$
   так как $(2r'c-\kappa)\mathsf p\ge(2r'c-\frac12)\frac{\mathsf p_0}2$, а модуль остальных членов скобки не больше $\frac14(2r'c-\frac12)\mathsf p_0$ ($\kappa\le\frac12$, $2r'c-\frac12>0$).
   Далее $\Gamma_*=\sqrt{a_0/\lambda_0}\big[\frac{3\sqrt3}2\beta\cdot\frac54\kappa+2\sqrt2\kappa(1-\kappa)\big]\le\kappa\sqrt{a_0/\lambda_0}\big(\frac{15\sqrt3}8\beta+2\sqrt2\big)$, и по (0.4) $\Gamma_*^2\le\beta\kappa=\beta\mu$.
   Условие $\mu=\kappa\le\beta$: из (NF), (G) и $U\in C^2$ следует $\beta\ge2$. Действительно, $q_s=s\omega^*+\eta_0(s,0)n$ имеет $|q_s|\le2s$,
   $U(q_s)=s^\beta\tilde F(s^{1/N},0,0)$ и $\tilde F(\sigma,0,0)\to G(0)\ne0$; так как $|U(q)|\le M|q|^2$ около $0$, то $s^\beta|G(0)|/2\le4Ms^2$ при малых $s$,
   откуда $\beta\ge2>\kappa$.

Условия класса (GT3″) выполнены. Применим теорему 2″ с $g(x):=\big(\sup_{|\theta|\le r_0}|y_0(x^{1/N},\theta)|+r_0x^{c-1}\big)^2\to0$. Она даёт траекторию
$q=\Phi(x,u,\zeta)=x\omega(\theta)+(\eta_0+x^ce)n(\theta)$ ($s=x$) с $b(t)\in\overline{\Omega_\delta}$: $|\theta|\le\sqrt{2\delta/\lambda_0}$, $\frac{\mathsf p_0}2|e|^{2r'}\le2\delta$, и
$|\eta|/x\le|y_0|+r_0x^{c-1}\le\sqrt{g(x)}\le\sqrt\delta$. Так как $\omega\perp n$, $\big|q/|q|-\omega(\theta)\big|^2=2-2/\sqrt{1+(\eta/x)^2}\le(\eta/x)^2$, а $|\omega(\theta)-\omega^*|\le|\theta|$;
отсюда $\big|q/|q|-\omega^*\big|\le\sqrt\delta+\sqrt{2\delta/\lambda_0}$. Расстояние до луча $\mathbb R_+\omega(\theta)$ не больше $|\eta|=o(x)$; $|q|\ge x$. При $\beta>2$
$\frac d{dt}x^{1-\beta/2}\in[(\frac\beta2-1)k_1,(\frac\beta2-1)k_2]$, откуда $x(t)\asymp t^{-2/(\beta-2)}$ при $t\to+\infty$. $\square$

### 9. Доказательство следствий

**Следствие N′.** Лемма N1 с $\Lambda=[-\Theta,\Theta]$ и $E\ge\max|\varepsilon_0|+e_1$: (0.3) при $\varepsilon=\varepsilon_0(\theta)+e$ — это (NF), так как
$s^{1+\gamma}(\varepsilon_0+e)=s\cdot s^\gamma\varepsilon_0+s^ce$ и $s^\gamma=\sigma^{N\gamma}$. $y_0=\sigma^{N\gamma}\varepsilon_0\in C^2$, $y_0(0,\cdot)=0$ ($N\gamma\ge1$). $\tilde F$ непрерывна,
$\partial_\theta\tilde F=\partial_\theta\tilde U+\partial_\varepsilon\tilde U\,\varepsilon_0'$ и $\partial_e\tilde F=\partial_\varepsilon\tilde U$ непрерывны, $\sigma\partial_\sigma\tilde F=\sigma\partial_\sigma\tilde U\to0$. $\tilde F(0,\theta,e)=\Phi_0(\theta,\varepsilon_0+e)=G+e^{2r'}\mathsf p$ по (E) и
формуле Тейлора многочлена; $\mathsf p$ — многочлен по $e$ с коэффициентами класса $C^2$, $\mathsf p(0,0)>0$; $G\in C^2$. При $r'=1$ ветвь
даёт аналитическая теорема о неявной функции ($\Phi_0$ аналитична по $(\theta,\varepsilon)$). $\square$

**Следствие N″.** $R:=U-P\in C^{K+1}$, $|R(q)|\le C|q|^{K+1}$, $|\nabla R(q)|\le C|q|^K$. Точка $q=s\omega+(\eta_0+s^ce)n$ имеет $|q|\le2s$;
$R_F(\sigma,\theta,e):=R(q)/s^\beta$ ($s=\sigma^N$). Тогда $|R_F|\le C's^{K+1-\beta}$, $|\partial_eR_F|=s^{c-\beta}|\langle\nabla R,n\rangle|\le C's^{c+K-\beta}$,
$|\partial_\theta R_F|=s^{-\beta}|\langle\nabla R,\partial_\theta q\rangle|\le C's^{K+1-\beta}$ ($|\partial_\theta q|\le C''s$ по (0.1)),
$|\sigma\partial_\sigma R_F|=N|s^{1-\beta}\langle\nabla R,\partial_sq\rangle-\beta R_F|\le C's^{K+1-\beta}$ ($|\partial_sq|\le C''$). Все показатели положительны, и
$\tilde F_U:=\tilde F_P+R_F$ (доопределённая при $\sigma=0$ значением $\tilde F_P(0,\cdot)$) удовлетворяет (NF), (G) с тем же $\tilde F_U(0,\cdot)$. $\square$

### 10. Примеры

Ниже все выкладки точные, кроме десятичных значений — они численные; [Эксперимент] `newton_M1M2.py` и независимо R30 (`newton_check.py`), R31 (`examples_R31.py`).

**M1.** $U(s\omega+\eta n)=(\eta-s^2\cos^2\phi)^4+s^5G(\phi)+s^7g_7(\phi)$, $G=\cos^5\phi+\sin^5\phi$, $g_7=\cos\phi\sin^6\phi+\sin\phi\cos^6\phi$;
$\varphi=(y-s\cos^2\phi)^4+sG+s^3g_7$, $\mathcal S=\{(0,4),(1,3),(2,2),(3,1),(4,0),(1,0),(3,0)\}$. $\gamma_*=\min(\frac11,\frac22,\frac33,\frac44,\frac14,\frac34)=\frac14$
(точка $(1,0)$), $\beta'=1$, $j=5$, $c=\frac54$, $N=4$. $\Phi_0=\varepsilon^4+G(\phi)$, $\tilde U=(\varepsilon-\sigma^3\cos^2\phi)^4+G(\phi)+\sigma^8g_7(\phi)$ (многочлен).
Ветвь $\varepsilon_0\equiv0$: $\partial_\varepsilon^k\Phi_0(\phi,0)=0,0,0,24$ при $k=1,2,3,4$, то есть $r'=2$, $\mathsf p\equiv1$. $G'=5\sin\phi\cos\phi(\sin^3\phi-\cos^3\phi)$;
критические точки $\phi\in\{0,\frac\pi2,\pi,\frac{3\pi}2,\frac\pi4,\frac{5\pi}4\}$, значения $G=1,1,-1,-1,\frac{\sqrt2}4,-\frac{\sqrt2}4$, $G''=-5,-5,5,5,\frac{15\sqrt2}4,-\frac{15\sqrt2}4$.
В $\phi^*=\pi$ и $\frac{3\pi}2$: $G=-1$, $G'=0$, $G''=5$ (и $G''+5G=0$). Константы: $a_0=1$, $\lambda_0=\frac54$, (0.4): $\kappa\le0.01719$. По
следствию N′ (с $\Theta$ любым меньше $\theta_K=\frac\pi2$; для большого круга лемма K3 элементарна) — асимптотические траектории
$q=s\omega(\theta)+s^{5/4}e\,e_z$ с $|\theta|\le\sqrt{8\delta/5}$, $|e|\le(4\delta)^{1/4}$. (Точное дно $\eta^*=s^2\cos^2\phi$ — единственная, тройная,
критическая точка в слое; $F_{\rm fl}=s^5G+s^7g_7$; используется приближённое дно $\eta_0=0$, так как $\eta^*=o(s^{5/4})$.)

**M2.** $U(s\omega+\eta n)=\eta^4+s^4f(\phi)\eta+s^6\cos^6\phi+s\eta^5(\cos\phi+2\sin\phi)$; $\varphi=y^4+sf\,y+s^2\cos^6\phi+s^2y^5(\cos\phi+2\sin\phi)$,
$\mathcal S=\{(0,4),(1,1),(2,0),(2,5)\}$, $\gamma_*=\min(\frac13,\frac24)=\frac13$, $\beta'=\frac43$, $j=\frac{16}3$, $c=\frac43$, $N=3$. $\Phi_0=\varepsilon^4+f\varepsilon$,
$\tilde U=\varepsilon^4+f\varepsilon+\sigma^2\cos^6\phi+\sigma^7\varepsilon^5(\cos\phi+2\sin\phi)$.

- $f=\frac34+\frac14\cos4\phi+\frac14\sin2\phi+\frac18\sin4\phi\ge\frac18>0$. Единственная критическая точка $\Phi_0(\phi,\cdot)$ — $\varepsilon_0=-(f/4)^{1/3}$
  (глобальный минимум, аналитична по $\phi$), $\partial_\varepsilon^2\Phi_0=12\varepsilon_0^2>0$, $r'=1$; $G=\frac34f\varepsilon_0=-3\cdot4^{-4/3}f^{4/3}$,
  $\Phi_0(\varepsilon_0+e)-G=e^2[(e+2\varepsilon_0)^2+2\varepsilon_0^2]$, $\mathsf p=(e+2\varepsilon_0)^2+2\varepsilon_0^2\ge2\varepsilon_0^2$.
- $G'=-4^{-1/3}f^{1/3}f'$, в критических точках $G''=-4^{-1/3}f^{1/3}f''$. $f'=\cos^4\phi\,(4t^3-3t^2-4t+1)$, $t=\tan\phi$, и $f'(\frac\pi2)=0$; кубика
  имеет три вещественных корня $t_1\approx-0.8263205$, $t_2\approx0.2236688$, $t_3\approx1.3526517$ (точная изоляция); $f''=-4\cos4\phi-\sin2\phi-2\sin4\phi$.
- $\phi^*=\arctan t_2$: значения кубики в $0.22$ и $0.23$ равны $\frac{1087}{62500}>0$ и $-\frac{1877}{62500}<0$, поэтому $t_2\in(0.22,0.23)$,
  $4\phi^*\in(4\arctan0.22,4\arctan0.23)\subset(0.866,0.905)\subset(0,\frac\pi2)$, $\cos4\phi^*>\cos0.905>0.6$, $\sin2\phi^*,\sin4\phi^*>0$, и
  $f''(\phi^*)<-2.4$. Значит, $G'(\phi^*)=0$, $G''(\phi^*)>0$, $G(\phi^*)<0$. Численно $G=-0.5443867$, $G''=2.947325$, $\varepsilon_0=-0.652674$,
  $G''+jG=0.0439$; (0.4): $a_0=0.54439$, $\lambda_0=0.73683$, $\kappa\le0.01778$.
- $\phi=\frac\pi2$: $f=1$, $f''=-4$, $G=-3\cdot4^{-4/3}$, $G''=4^{2/3}$, $G''+jG=4^{2/3}-16\cdot4^{-4/3}=0$; (0.4): $\kappa\le0.01752$.
- $f(\phi+\pi)=f(\phi)$: те же минимумы в $\phi^*+\pi$ и $\frac{3\pi}2$; в $\arctan t_1$ и $\arctan t_3$ — максимумы $G$ ([Эксперимент]: численно
  $G''\approx-2.087$ и $-1.956$, пересчёт R35; нигде не используется).

По следствию N′ — асимптотические траектории $q=s\omega(\theta)+s^{4/3}(\varepsilon_0(\phi)+e)e_z$ вдоль четырёх направлений, $|\theta|\le\sqrt{2\delta/\lambda_0}$,
$|e|\le\sqrt{2\delta/3}/|\varepsilon_0(\phi^\circ)|$, где $\phi^\circ$ — та точка минимума, вдоль которой строится траектория
($\varepsilon_0(\phi^*)=-0.652674$, $\varepsilon_0(\frac\pi2)=-4^{-1/3}$). $\square$

## Замечания

### 1. Где работают аналитичность и изолированность

- **Теоремы 2″ и N** — утверждения для $U\in C^2$ при заданных (NF), (G); аналитичность и изолированность в них не
  используются. Вся «конечность типа» — в предположениях: вдоль дна $U=s^\beta(G(\theta)+o(1))$ с $G(0)<0$, поперёк —
  степенные стенки $e^{2r'}\mathsf p$ с запасом Эйлера.
- **Следствие N″**: условия теоремы N — условия на конечную струю $j^KU$, $K+1>\beta$, и для $U\in C^{K+1}$ они достаточны.
  [Эскиз] С гладкими контрпримерами (Пенлеве–Уинтнер, Лалуа; по `problem/KNOWN_RESULTS.md`, первоисточники не
  сверены) это не конфликтует: в известных формулировках у них все струи в нуле нулевые, так что никакая конечная
  струя не даёт ветви с $G(0)<0$. Пример Уреньи касается тотальной неустойчивости; теорема N даёт одну асимптотическую
  траекторию.
- **Аналитичность работает** (i) в лемме N1 (сходимость $\tilde U$ и непрерывность при $\sigma=0$ — это даёт (F) в
  следствии N′); (ii) в леммах N2–N4 (описание дна, ветви Пюизё); (iii) в альтернативах «процесс останавливается»:
  если $(i,l)\in\mathcal S$ с $l<2r$ нет, то конус над дугой состоит из критических точек (утверждение 1); если $\hat G\equiv0$, то
  поверхность дна состоит из критических точек (лемма N4(d)). [Эскиз] Для $C^\infty$ обе альтернативы ломаются: плоская
  добавка (например, $z^4+e^{-1/(x^2+y^2)}g$, пример R30) не меняет коэффициентов Тейлора, и $\gamma_*=\infty$ (или $k=\infty$)
  уже не влечёт существования критического конуса (поверхности).
- **Изолированность** используется только в (iii): у изолированной критической точки $\gamma_*<\infty$ и $\hat G\not\equiv0$. Ни в
  теореме N, ни в примерах она не нужна (M1, M2 изолированы и над $\mathbb C$: числа Милнора $48$ и $59$ по полигону,
  [Эксперимент, Singular]; это не используется).
- Все рассуждения вещественные; конечность числа Милнора не используется.

### 2. Связь с результатом 008

- [Доказано, элементарно] При $r=1$ (Морс–Ботт) и $g_{m+1}=u_{m+1}|_\Sigma\not\equiv0$ первое ребро даёт $\gamma_*=\frac12$, $j=m+1$,
  $c=\frac32$, $\Phi_0=\frac12h_n\varepsilon^2+g_{m+1}$; при $g_{m+1}\equiv0$ и $(1,1)$ или $(2,0)\in\mathcal S$ — $\gamma_*=1$, $j=m+2$,
  $G_{\min}=u_{m+2}|_\Sigma-\frac{b_1^2}{2h_n}=g_{m+2}$. Если $G_{\min}\not\equiv0$, это те же $j$, $G$, $c$, что в [008]. В [008] $j$ — номер первого
  ненулевого $g_k$, здесь — показатель первого ребра; при $G_{\min}\equiv0$ они различаются, и к [008] ведёт уточнение
  леммы N4(c) (один шаг; $\hat G$ — точное значение на дне).
- Лемма N4(c) не гарантирует условий теоремы N: $G_k$ может обращаться в нуль в нужной точке (пример R30:
  $\tilde U=(\varepsilon^2-1)^2+\sigma\theta\varepsilon+\sigma^2g$, ветвь $\varepsilon_0=1$, $\hat G=\sigma\theta+O(\sigma^2)$, $G_1=\theta$); тогда каскад переходит в угловое
  направление.
- [Эскиз] Теорема N при $r'=1$ — вариант теоремы K2 [008] с приближённым дном вида ряда Пюизё и $\lambda_0=G''(0)/4$ вместо
  $\frac14\min(G''(0),h_n(0))$. При $r'=1$ применима и теорема 2′ [008] напрямую, но с другой константой: тогда
  $Q\ge\min(\lambda_0,\mathsf p_0/2)|b|^2$, и в (0.4) $\lambda_0$ нужно заменить на $\min(G''(0)/4,\mathsf p_0/2)$.
- Препятствие R3 из [007] (замечание 7: при кривизне $C_1>0$ и $Q\sim|b|^4$ член $\theta_2/\sqrt\delta$ не мал) обходится за счёт
  структуры карты (7.1): кривизна и перекрёстные члены действуют только по угловой переменной $b'=\theta$, где профиль
  квадратичен, а по нормальной $b''=e$ карта асимптотически плоская (лемма N5). [Гипотеза] Для вырожденного профиля по
  $\theta$ этот приём не помогает, и препятствие остаётся.

### 3. Что остаётся открытым

1. **Переменная кратность вдоль $\Sigma_0$**: точки, где $a(\theta,0)=0$, и точки, где обнуляется коэффициент вершины
   многоугольника Ньютона. Если такая точка — $\omega^*$, ветвь $\varepsilon_0$ может быть не $C^2$: $\Phi_0=\varepsilon^4+\theta\varepsilon^2+G_1(\theta)$ даёт
   $G_{\min}=G_1-\frac{\theta^2}4\mathbf 1_{\theta<0}$ (только $C^{1,1}$). [Гипотеза] Нужна карта с переменным профилем.
2. **Вырожденный минимум $G$** ($G-G(0)\sim\theta^{2q}$, $q\ge2$) — препятствие R3 по угловой переменной.
3. **Каскад в нормальном направлении**: $G_{\min}\equiv0$ на первом ребре при вырожденном профиле (следующие рёбра,
   сливающиеся ветви). При невырожденном профиле — лемма N4(c).
4. **Угловые каскады** ($G\ge0$ с нулями) и $G\equiv{\rm const}<0$ на замкнутой $\Sigma_0$ — как в замечании 6 [008].
5. **Особые точки $\Sigma$** и точечные компоненты с вырожденным нормальным гессианом (типа $x^4+y^4-z^6$). [Эскиз] В
   определении (GT3″) оба множества $I'$, $I''$ непусты; доказательство теоремы 2″ проходит и при $I'=\varnothing$ ($R'=0$,
   $\gamma_1=\gamma_2=C_1=0$, $\delta_1=q_0(r_1/4)/2$, условие на $\lambda_0$ и (U2) отпадают); отдельно это не выписано.
6. **Сведение к задаче на дне** [Эскиз]. Если $u_m\ge0$ и $\Sigma$ — объединение замкнутых гладких кривых с условием (M),
   то вне трубок $\{s\omega+\eta n:\ |\eta|<y_1s\}$ $U>0$, а в трубках $U\ge F_{\rm fl}$; поэтому $0$ — минимум тогда и только тогда, когда
   $F_{\rm fl}\ge0$ при малых $s$, и по лемме N2 знак $G_{\min}$ решает вопрос, если $G_{\min}$ не обращается в нуль. Теорема N
   покрывает случай отрицательного невырожденного минимума $G$ с равномерной ветвью; остальное (пп. 1–4) открыто.
7. Касание самого луча $\mathbb R_+\omega^*$ (одна траектория с пределом направления) не доказано — как в [007], [008].
8. $n\ge4$ не рассматривалось.

### 4. Эксперименты

Все — [Эксперимент], не доказательство; запуск `~/venv/bin/python <скрипт>` из `experiments/prover/normal-multiplicity/`.

- `frames_nm.py`: символьная проверка (7.2)–(7.6) при $\eta_0=s\,y_0(s^{1/3},\theta)$ с общим многочленом $y_0$ и общим $k_g$ — 14
  тождеств, все верны.
- `newton_M1M2.py`: носители, $\gamma_*$, $j$, $c$, $\Phi_0$, $\tilde U$, тождество (0.3), $G$, критические точки, $G''$, профиль, константы (0.4).
- `floor_nm.py`: $F_{\rm fl}/s^j\to G$ (M2: $-0.50430,\dots,-0.5443867$ при $s=10^{-2}\dots10^{-12}$; ошибка $O(s^{2/3})$). Совпадение с
  `experiments/numerics/2026-10-21-valleys/` (глубина, направление дна, отношение глубин $0.868$ у M2).
- `exit_nm.py`: строгий выход (A5) прямым дифференцированием вдоль потока. M1: минимум $\frac\rho\lambda\Xi/(\delta\rho^\beta)\approx2\kappa$ при
  малых $\kappa$, положителен при всех $\kappa\in[0.017,0.5]$. M2: при $x\gtrsim10^{-4}$ выход нарушается (минимум $\approx-1.2$; наклон дна
  $\nu\approx\frac43\varepsilon_0x^{1/3}$ ещё не мал), при $x\le10^{-6}$ ($\delta=0.01$) строгий при всех проверенных $\kappa$ — согласуется с
  асимптотическим характером теоремы ($\sigma_*$ выбирается после $\delta$).

## Отличия от записки

**Правки по отзыву R30** (`notes/reviewer/2026-10-21-normal-mult-A.md`; внесены и в записку, её §9).

1. З1: в лемме N2 $E\ge1$ включено в максимум.
2. З2: инвариантность $\gamma_*$, $j$, $c$, $G_{\min}$ обоснована через зависимость $\varphi$ только от точки и нормали (знак нормали —
   $y\to-y$); добавлено, что $F_{\rm fl}$ при малых $s$ не зависит от $y_1$ и что по $F_{\rm fl}$ показатель $j$ восстанавливается лишь при
   $G_{\min}\not\equiv0$ (здесь — в утверждении 1 и лемме N2).
3. З3: оговорка о различии $j$ здесь (первое ребро) и в [008] (первый ненулевой $g_k$) — замечание 2.
4. З4: $2\rho_s<R_0/3$ в лемме N1. З5: выбор $\Lambda\supset\Lambda_1$ и $E$ в лемме N4. З6: подготовительная теорема Вейерштрасса
   в лемме N3, уточнена степень сверки литературы.
5. З7: замечание о лемме N4(c): уточнение за один шаг, $G_k$ может обращаться в нуль (пример R30) — замечание 2.
6. З8: опечатка $y^4+sf\,y$. З9: наклон в координатах $(l,i)$. З10: дуга вложенная. З11: порядок кванторов в лемме N2.

**Правки по отзыву R31** (`notes/reviewer/2026-10-21-normal-mult-B.md`; внесены и в записку).

7. Замечание 1: в теорему 2″ добавлено условие $g(x(t))\le\delta$ для любой заданной $g\to0$ (дополнительное уменьшение
   $\sigma_*$, аналог $\sigma_*\le\sqrt\delta$ в [008], §9, п. 5); в теореме N из него выведена оценка
   $|q/|q|-\omega^*|\le\sqrt\delta+\sqrt{2\delta/\lambda_0}$ (§8).
8. Замечания 2–6: порядок констант в §8 ($r_1<\min(\Theta/2,e_1,\frac14)$, квадрат $|\theta|,|e|\le r_1$ внутри области (G)); область
   определения $T$; полуширина интервала в (NF) переименована $\theta_1\to\Theta$ (буквы $\theta_1,\theta_2,\theta_3$ заняты леммой 2′);
   существование $\partial_\sigma\tilde F$ при $\sigma>0$; оценка $|e|$ для направления $e_y$ в M2.
9. Замечания 7–11: уточнена фраза о $G''+jG=0$ (в минимумах $G$); статус [008]; метки [Эскиз] в замечании 1 (гладкие
   контрпримеры) и в замечании 3, пп. 5–6.

**Правки по R35** (`notes/reviewer/2026-10-21-result011.md`; новых утверждений нет).

- З1: заголовок класса (GT3″) — «любое $n\ge3$» (оба множества $I'$, $I''$ непусты); сказано, что при $I''=\varnothing$ это (GT3′).
- З2: в определение $s_2(y_1)$ (§3, п. 5) добавлено условие $s<\sigma_1^N$ из леммы N1.
- З3: в лемме N4 $\Lambda_1\subset\Lambda'$; $E:=\max|\varepsilon_0|+2$ выбирается до $e_2$, а в (a) берутся $e_2\le1$, $\sigma_2\le\sigma_1(E)$.
- З4: в N4(c) «(NF) и структурная часть (G)»; оговорено, что знаковых условий на $G_k$ лемма не даёт.
- З5: в теореме N и в конце §8 — «$s(t)\asymp t^{-2/(\beta-2)}$ при $t\to+\infty$».
- З6: в замечании 2 метки [Эскиз] (п. 3) и [Гипотеза] (п. 4); для теоремы 2′ при $r'=1$ указана константа
  $\min(G''(0)/4,\mathsf p_0/2)$ вместо $\lambda_0$.
- З7: в §10 максимумы $G$ в $\arctan t_1$, $\arctan t_3$ помечены [Эксперимент]; оговорено, что десятичные значения численные.
- З8–З9: в утверждении 1 многоугольник Ньютона определён в координатах $(l,i)$ (нижняя граница оболочки $\mathcal S+\mathbb R_+^2$),
  вершина $(l,i)=(2r,0)$, $\gamma_*$ — модуль наклона; сказано, что в $\mathcal S$ возможны точки $(0,l)$ с $l>2r$.
- З10: в §6, шаг 6, в список используемого для $\beta\ge2$ добавлены (F) и $F_0(0)\ne0$.
- З11: в §8 $s_0<\min(1,\sigma_1^N)$.
- З12: в доказательстве леммы N3 уточнено, что нужна сходящаяся форма теоремы Ньютона–Пюизё, и что у Casas-Alvero
  сверено только оглавление (шапка не менялась).

**Переобозначения и уточнения при оформлении** (математика та же).

10. Нумерация: (1.1) записки (репер) $\to$ (0.1); тождество 1.2 записки $\to$ (0.2); (2.1) $\to$ (0.3); (4.0) $\to$ (0.4); карта (4.1) $\to$
    (7.1); (4.2)–(4.6) $\to$ (7.2)–(7.6). «Утверждение о первом ребре» записки — утверждение 1, вместе с альтернативой
    «критический конус» и инвариантностью; «Связь с 008» и замечание после N4 перенесены в замечание 2.
11. В лемме N2 явно выделена константа $s_2'$ (область разложения) и определение $s_2(y_1)$; в лемме N4(b) выписан
    локальный минимум; в доказательстве теоремы N добавлен вывод $x(t)\asymp t^{-2/(\beta-2)}$.
12. В примерах указаны независимые проверки R30, R31; численные данные §5.3 записки сокращены до замечания 4.
