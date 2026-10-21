# 012. Свободное поле $Y$ в принципе Важевского: изолированный вырожденный нулевой луч ведущей формы

- **Статус:** [Проверено: reviewer R34, R36 (агенты), 21.10.2026 — доказательства в записке
  [`notes/prover/2026-10-21-point-degenerate.md`](../notes/prover/2026-10-21-point-degenerate.md); reviewer R39
  (агент), 21.10.2026 — текст этого результата целиком: ошибок нет]; ждёт проверки человеком.
  - R39 ([`notes/reviewer/2026-10-21-result012.md`](../notes/reviewer/2026-10-21-result012.md)): все шаги
    «Утверждения» и «Доказательства»; применимость теоремы A и леммы 2 [007] к свободному полю $Y$;
    тождества (I1)–(I4) символьно; ссылки на Bierstone–Milman 1988 сверены по Numdam. Ошибок нет;
    редакционные замечания 1–6 учтены («Отличия от записки», пп. 19–26). Главный агент прочитал правки,
    в том числе ручные доказательства изолированности $0$ у примеров X и R в замечании 4 (проверил).
  - R34 (reviewer, агент, 21.10.2026,
    [`notes/reviewer/2026-10-21-point-degenerate-A.md`](../notes/reviewer/2026-10-21-point-degenerate-A.md)):
    §1–§4 записки — лемма B, лемма 3, предложение N, утверждение Q (с примерами K1, P1), теорема 2U.
    Ошибок в доказательствах нет. Неверны были два побочных высказывания вне доказательств (замечание
    3.1 в общности утверждения Q, фраза о $-e_z$ у P1); оба исправлены. Литература леммы B сверена R34
    по полному тексту BM88.
  - R36 ([`...-B.md`](../notes/reviewer/2026-10-21-point-degenerate-B.md)): §5 записки — теорема C′,
    следствия R, X, SV, S, E, частные случаи §5.7, примеры. Ошибок нет; замечания 1–9 редакционные.
  - Все замечания R34, R36 учтены во второй редакции записки (её §11) и здесь («Отличия от записки»).
    Места, переписанные при оформлении, рецензенты не читали.
  - Метки: всё в разделе «Утверждение» — [Доказано], кроме двух помеченных [Эксперимент] фраз об
    изолированности критической точки в примерах Λ, SH (в выводах не используются). Замечания помечены
    каждое отдельно.
- **Автор:** prover (агент), записка `notes/prover/2026-10-21-point-degenerate.md` (21.10.2026), по
  заданию главного агента: обобщить теорему K0 ([008]) на изолированную, но вырожденную точку $\omega$
  множества нулей ведущей формы. Идея свободного поля $Y$ — `notes/main-agent/2026-10-21-free-Y.md`
  (главный агент, [Эскиз]); здесь она доказана в виде теоремы 2U. Оформление — prover (агент),
  21.10.2026.
- **Зависит от:**
  - [007] = [`results/007-gt3.md`](007-gt3.md): теорема A, лемма 2 (формула (3.1)), теорема 2,
    следствие 2;
  - [009] = [`results/009-euler-field.md`](009-euler-field.md): теорема E и следствие 6.1(a) (только в следствии E);
  - [BM88] E. Bierstone, P. D. Milman, *Semianalytic and subanalytic sets*, Publ. Math. IHÉS 67 (1988),
    5–42: определение 3.1, теорема 3.10 (теорема Габриэлова о дополнении), теорема 0.2
    (ректилинеаризация), определение 5.4 — только в лемме B. Сверено R34 по полному тексту (Numdam);
  - [008] = [`results/008-class-K.md`](008-class-K.md) — только для сравнения (теорема K0).
- **Проверочные скрипты** [Эксперимент]:
  - [`experiments/prover/point-degenerate/`](../experiments/prover/point-degenerate/) — автор
    (`check_2U_identities.py`, `examples.py`, `exit_check.py`, `exit_check_ring.py`, `sv2_check.py`,
    `diag_field_E.py`, `isolated_check.py`);
  - `experiments/reviewer/point-degenerate-R34/`, `experiments/reviewer/point-degenerate-R36/` —
    рецензенты (независимые реализации, в том числе символьная проверка тождеств (I1)–(I4) для
    произвольных $\gamma$, $L$, $\xi$, $P$).

## Утверждение

### Обозначения

$\mathbb R^n$ с евклидовыми $\langle\cdot,\cdot\rangle$, $|\cdot|$, $B_r=\{|q|<r\}$; $\|\cdot\|$ — операторная норма.
Система $\ddot q=-\nabla U(q)$. **Асимптотическая траектория** — решение $q(t)\ne0$, $t\ge0$, с $q(t)\to0$,
$\dot q(t)\to0$ при $t\to+\infty$; из её существования следует неустойчивость по Ляпунову ([007], теорема
A, шаг 6). Обозначения $W,V,K_\perp,\Omega,\Xi$, условия (D1)–(D4), (A4), (A5), (L0)–(L3) и константы
$L_1,L_2$ формулы (3.1) — как в [007]. Система инвариантна относительно ортогональных замен
координат, и мы пользуемся этим без оговорок.

**Аналитический случай.** $U$ вещественно-аналитична около $0\in\mathbb R^n$, $U(0)=0$, $\nabla U(0)=0$,
$U=\sum_{k\ge m}u_k$ — разложение на однородные формы, $u_m\not\equiv0$. $\Sigma=\{u_m=0\}\cap S^{n-1}$. Пусть
$\omega\in\Sigma$; после поворота $\omega=e_x$, $q=(x,y)\in\mathbb R\times\mathbb R^{n-1}$, и
$$p(y):=u_m(1,y).$$
**Предположение (Z):** $p\ge0$ около $y=0$ и $0$ — изолированный нуль $p$ (то есть $u_m\ge0$ около $\omega$ и
$\omega$ — изолированная точка $\Sigma$). Вырожденность $D^2p(0)$ не предполагается и не исключается.

**(H<0):** для каждого $\varepsilon>0$ есть точки $q=(x,y)$ со сколь угодно малым $|q|$, $|y|<\varepsilon x$ и $U(q)<0$.

Для $N\in\mathbb N$ положим $s=x^{1/N}$. Для весов $c=(c_i)\in(0,\infty)^{n-1}$: $C=\operatorname{diag}(c_i)$,
$x^c=\operatorname{diag}(x^{c_i})$, $c_{\min},c_{\max}$; для монома $s^kw^\alpha$ ($k\in\mathbb N_0$, $\alpha\in\mathbb N_0^{n-1}$)
**уровень** $\ell_c(k,\alpha):=k/N+c\cdot\alpha$ и **порядок** $k/N+|\alpha|$.

### Лемма B (дно)

Пусть $n\ge2$, выполнены (Z) и (H<0). Тогда найдутся $N\in\mathbb N$, $\varepsilon_0\in(0,1)$, $x_0>0$, сходящийся
ряд $\tilde\gamma(s)=\sum_{j>N}g_js^j$ ($g_j\in\mathbb R^{n-1}$) и числа $a>0$, $\beta\in\frac1N\mathbb N$, $\beta\ge m+1$, такие, что
при $\gamma(x):=\tilde\gamma(x^{1/N})$, $0<x<x_0$:

1. $U(x,\gamma(x))=\min_{|y|\le\varepsilon_0x}U(x,y)=:\underline U(x)$ и $|\gamma(x)|\le\varepsilon_0x/2$;
2. $\underline U(x)=\underline u(x^{1/N})$ с аналитической $\underline u$, и $\underline U(x)=-ax^\beta(1+O(x^{1/N}))$;
3. $\nabla_yU(x,\gamma(x))=0$; $\gamma=O(x^{1+1/N})$, $\gamma'(x)\to0$, $x\gamma''(x)\to0$;
4. $g(s,w):=U(s^N,\tilde\gamma(s)+w)-\underline u(s)$ аналитична около $(0,0)$, $g(s,0)=0$, $\nabla_wg(s,0)=0$, и
   $g(s,w)\ge0$ при $0<s<x_0^{1/N}$, $|\tilde\gamma(s)+w|\le\varepsilon_0s^N$;
5. $g(s,w)=u_m(s^N,w)+(\text{мономы порядка}>m)$.

### Лемма 3 (хвосты)

Пусть $G(s,w)=\sum a_{k\alpha}s^kw^\alpha$ сходится абсолютно при $|s|\le S$, $\max_i|w_i|\le\varrho$; $c\in(0,\infty)^{n-1}$,
$N\in\mathbb N$, $\beta>0$, $r>0$, $\theta>0$. Тогда мономов с $\ell_c<\beta+\theta$ конечное число, а
$$T_\theta(s,b):=\sum_{\ell_c(k,\alpha)\ge\beta+\theta}a_{k\alpha}\,s^{k+Nc\cdot\alpha-N\beta}\,b^\alpha$$
(хвост функции $x^{-\beta}G(s,x^cb)$, $x=s^N$) удовлетворяет $|T_\theta|+|\nabla_bT_\theta|+|s\partial_sT_\theta|\le K_\theta s^{N\theta}$ при
$0<s\le s_1$, $|b|\le r$, для некоторых $s_1,K_\theta>0$.

### Предложение N (веса оврага и профиль)

Пусть $n=3$, выполнены (Z), (H<0), и $g=\sum a_{k\alpha}s^kw^\alpha$ — из леммы B. Для $c\in(0,\infty)^2$ положим
$\varphi(c)=\min_{\operatorname{supp}g}\ell_c$ и при $\varphi(c)=\beta$
$$Q_c(b):=\sum_{\ell_c(k,\alpha)=\beta}a_{k\alpha}b^\alpha\qquad(\text{при каждом }\alpha\text{ не более одного }k);$$
$\mathcal T:=\{c:\ \varphi(c)=\beta\}$.

1. Если $\varphi(c)\ge\beta$, то $c_i\ge1+(\beta-m)/j_i>1$, где $j_i$ — порядок нуля $p$ на $i$-й оси.
2. Если $c\in\mathcal T$, то $Q_c\not\equiv0$ и $Q_c\ge0$ на всём $\mathbb R^2$.
3. $\mathcal T$ — локально выпуклая ломаная в открытом квадранте. Внутри её звена $Q_c$ обращается в нуль на
   координатной оси. Поэтому изолированный нуль $Q_c$ возможен только в вершинах $\mathcal T$, и тогда $Q_c$
   содержит чистые степени $b_1^{j_1'}$ и $b_2^{j_2'}$.
4. $\varphi(1,1)=m<\beta$, и на диагонали есть единственная точка $(c_*,c_*)\in\mathcal T$, $c_*>1$.

### Утверждение Q (профиль с весовым неравенством Эйлера; в частности квазиоднородный)

Пусть $n=3$, $U$ аналитична, $N\in\mathbb N$, веса $c\in(1,\infty)^2$, $Nc_i\in\mathbb N$, $\beta>0$, $N\beta\in\mathbb N$, и
$\gamma(x)=\tilde\gamma(x^{1/N})$, $\tilde\gamma(s)=\sum_{j>N}g_js^j$ — сходящийся ряд (например, дно леммы B, или
$\gamma\equiv0$). Пусть $\hat U(s,w):=U(s^N,\tilde\gamma(s)+w)=\sum a_{k\alpha}s^kw^\alpha$ и

- **(Q1)** все мономы $\hat U$ имеют $\ell_c(k,\alpha)\ge\beta$;
- **(Q2)** $F_0(b):=\sum_{\ell_c=\beta}a_{k\alpha}b^\alpha$ имеет $F_0(0)<0$, а $Q:=F_0-F_0(0)$ имеет строгий локальный
  минимум в $0$;
- **(Q3)** $\langle Cb,\nabla Q\rangle\ge\mu Q$ около $0$ для некоторого $\mu\in(0,\beta]$.

Тогда есть асимптотическая траектория $q(t)=(x(t),\gamma(x(t))+x(t)^cb(t))$, $x(t)\downarrow0$,
$\dot x\asymp-x^{\beta/2}$, $b(t)$ в компакте.

(Q3) выполнено, если $Q$ **градуированно положителен**: $Q=\sum_kQ^{(k)}$, где $Q^{(k)}$ — сумма мономов $Q$,
пришедших из $s^k$, и все $Q^{(k)}\ge0$ около нуля. Тогда $Q^{(k)}$ — $c$-квазиоднородный многочлен
степени $d_k=\beta-k/N>0$, и $\langle Cb,\nabla Q\rangle=\sum_kd_kQ^{(k)}\ge(\min_kd_k)Q$; в частности, если $Q$
$c$-квазиоднороден (один $k$), то $\mu=\beta-k/N$.

### Теорема 2U (свободное поле $Y$ в прямой карте)

**Данные.** $n\ge2$, $q=(x,y)\in\mathbb R\times\mathbb R^{n-1}$, $U\in C^2(B_r)$, $U(0)=0$, $\nabla U(0)=0$, и:

- $\beta>0$, $N\in\mathbb N$, веса $c\in(1,\infty)^{n-1}$, $s_0\in(0,1]$, $r_0>0$;
- $\gamma\in C^2((0,s_0);\mathbb R^{n-1})$ с $\gamma,\gamma',x\gamma''\to0$ при $x\to0$;
- $L\in C^2((0,s_0);GL_{n-1}(\mathbb R))$ с $L(x)\to I$, $x\|L'(x)\|\to0$, $x^2\|L''(x)\|\to0$;
- карта $\Phi(x,b)=(x,\ \gamma(x)+L(x)x^cb)$ на $\mathcal N=\{0<x<s_0,\ |b|<r_0\}$; $s_0$ так мал, что
  $\Phi(\mathcal N)\subset B_r\setminus\{0\}$ и $\|L\|,\|L^{-1}\|\le2$; $F(s,b):=x^{-\beta}U(\Phi(x,b))$ (класса $C^1$ при $s>0$);
- поле $\xi\in C^1\big((0,s_0^{1/N})\times B_{r_0};\mathbb R^{n-1}\big)$ с $|\xi|\le M_0$, $\|D_b\xi\|\le M_1$, $|s\partial_s\xi|\le M_2$ и
  - **(T)** $\partial_{b_j}\xi_i\equiv0$, если $c_i<c_j$;
  - **(Θ)** для каждого блока $J=\{i:\ c_i=c'\}$ симметричная часть матрицы $\big(c'\delta_{ij}-\partial_{b_j}\xi_i\big)_{i,j\in J}$
    неотрицательно определена (во всех точках).

**Условия.** Есть $a_0>0$, $\delta\in(0,a_0/2]$, $\mu\in(0,\beta]$, $r_1\in(0,r_0)$, $\varepsilon_E\in[0,\mu\delta/8]$ и функция
$\eta(s)\ge0$, $\eta(s)\to0$ при $s\to0$, такие, что при $0<s<s_0^{1/N}$ для $P:=F+a_0$:

- **(U1)** есть $b_0=b_0(s)$, $|b_0|<r_1$, с $P(s,b_0)\le\eta(s)$;
- **(U2)** $P(s,b)\ge-\eta(s)$ при $|b|<r_1$;
- **(U3)** $P(s,b)\ge2\delta$ при $|b|=r_1$;
- **(U4)** $\xi\cdot\nabla_bF-\frac sN\partial_sF\ge\mu P-\varepsilon_E-\eta(s)$ при $|b|<r_1$, $P(s,b)\le\delta$.

**Теорема 2U.** При этих данных и условиях есть решение $q(t)=\Phi(x(t),b(t))$, $t\ge0$, $q(t)\ne0$, с
$x(t)\downarrow0$, $-k_2x^{\beta/2}\le\dot x\le-k_1x^{\beta/2}$ ($0<k_1\le k_2$), $|b(t)|<r_1$, $q(t)\to0$, $\dot q(t)\to0$.
Равновесие неустойчиво по Ляпунову. Кроме того, $q(t)/|q(t)|\to e_x$.

Поле, с которым работает доказательство: $Y=e_x+\tilde Z$,
$$\tilde Z=\gamma'(x)+L'(x)x^cb+L(x)x^{c-1}\big(Cb-\xi(s,b)\big). \tag{0.1}$$
При $\xi=Cb$, $L=I$ это $Y=\partial_x\Phi$ (поле теоремы 2 [007]); при $\xi=(C-I)b$, $L=I$ — радиальное поле
с центром на дне $Y=e_x+\gamma'+(y-\gamma)/x$; при $\xi=0$, $\gamma=0$, $L=I$ — поле весовой гомотетии
$Y=e_x+Cy/x$.

### Теорема C′ (градуированный профиль)

Пусть даны $n,U,\beta,N,c,\gamma,L,\Phi,F$ и поле $\xi=\xi(b)$ (не зависящее от $s$) с (T), (Θ), $|\xi|\le M_0$,
$\|D\xi\|\le M_1$ — как в теореме 2U. Пусть на $(0,s_0^{1/N})\times B_{r_0}$
$$F(s,b)=-a_0+\sum_{j=1}^Js^{-e_j}R_j(b)+F_>(s,b), \tag{0.2}$$
где $a_0>0$, $e_j\ge0$, $R_j\in C^1(B_{r_0})$, $F_>\in C^1$ при $s>0$. Пусть $r_1\in(0,r_0)$, $\mu\in(0,\beta]$, $R_j\ge0$ на
$\overline{B_{r_1}}$, $\chi(s):=\sup_{|b|\le r_1}\big(|F_>|+|\nabla_bF_>|+|s\partial_sF_>|\big)\to0$ при $s\to0$, и

- **(C1)** все $R_j$ обращаются в нуль в общей точке $b_0$, $|b_0|<r_1$;
- **(C2)** $R:=\sum_jR_j>0$ на сфере $|b|=r_1$; $q_1:=\min_{|b|=r_1}R$, $\delta:=\min(a_0/2,q_1/4)$;
- **(C3)** $\xi\cdot\nabla R_j+\frac{e_j}NR_j\ge\mu R_j$ на $B_{r_1}$ для всех $j$ с $e_j>0$, и
  $\xi\cdot\nabla R^{(0)}\ge\mu R^{(0)}-\varepsilon_E$ на $B_{r_1}$ для $R^{(0)}:=\sum_{e_j=0}R_j$, где $0\le\varepsilon_E\le\mu\delta/8$.

Тогда (после уменьшения $s_0$) выполнены условия теоремы 2U, и есть асимптотическая траектория
$q(t)=\Phi(x(t),b(t))$, $|b(t)|<r_1$.

### Следствия

**Следствие R (профиль из ведущей формы; радиальное от дна поле).** Пусть $n=3$, выполнены (Z), (H<0), $g$ —
из леммы B, $c\in\mathcal T$, $Nc_i\in\mathbb N$, и все мономы $g$ уровня $\ell_c=\beta$ — мономы $u_m(s^N,w)$ (то есть
$k/N+|\alpha|=m$). Если $Q_c$ имеет строгий минимум в $0$, то есть асимптотическая траектория; поле —
$\xi=(C-I)b$.

**Следствие X («крест»).** Пусть $n=3$, $U$ аналитична, $c\in(1,\infty)^2$, $Nc_i,N\beta\in\mathbb N$, $\gamma$ — как в
утверждении Q, $L=I$, $\hat U(s,w)=U(s^N,\tilde\gamma(s)+w)=\sum a_{k\alpha}s^kw^\alpha$, и:

- $\hat U(s,0)=-a_0s^{N\beta}(1+O(s))$, $a_0>0$;
- все мономы $\hat U$ с $\alpha\ne0$ и $\ell_c<\beta$ имеют $a_{k\alpha}>0$ и $\alpha\in(2\mathbb N_0)^2$;
- $Q_c(b):=\sum_{\alpha\ne0,\ \ell_c=\beta}a_{k\alpha}b^\alpha$ имеет строгий минимум в $0$, и
  $\sum_i\lambda_ib_i\partial_iQ_c\ge\mu_0Q_c$ около $0$ при некоторых $0\le\lambda_i\le c_i$, $\mu_0>0$.

Тогда есть асимптотическая траектория; поле $\xi=(\lambda_ib_i)_i$, и годится
$\mu=\min\big(\mu_0,\ \min_j(\lambda\cdot\alpha_j+\beta-\ell_c^{(j)}),\ \beta\big)$, где $j$ пробегает мономы с $\ell_c<\beta$.

**Следствие SV (подовраг, касательный к широкой оси).** Пусть $n=3$, $c_1<c_2$, и в (0.2) при $L$, $\gamma$ из
теоремы 2U $J=2$,
$$R_1=\mathfrak a(b)\big(b_2-\psi(b_1)\big)^2,\qquad R_2=\mathfrak b(b_1),$$
где $\psi\in C^2$, $\psi(0)=\psi'(0)=0$; $\mathfrak a\in C^1$, $\mathfrak a(0)>0$; $\mathfrak b\in C^1$, $\mathfrak b(0)=0$, $\mathfrak b>0$ при $b_1\ne0$,
$b_1\mathfrak b'(b_1)\ge\nu_B\mathfrak b(b_1)$ около $0$ ($\nu_B>0$); $e_1,e_2\ge0$; $F_>$ — как в теореме C′. Тогда есть
асимптотическая траектория; поле
$$\xi=\alpha\Big(b_1,\ b_1\psi'(b_1)+2\big(b_2-\psi(b_1)\big)\Big),\qquad0<\alpha\le c_1/2 .$$

**Следствие S (лист минимумов постоянной глубины).** Пусть $U\in C^2(B_r)$, $U(0)=0$, $\nabla U(0)=0$ (данные
теоремы 2U), $\gamma=0$, $L=I$, $c\in(1,\infty)^{n-1}$, $a_0>0$, $\beta>0$, и $U=h(x,y)-a_0x^\beta+r(x,y)$, где (так как $h\in C^2$) $r\in C^1$ при $x>0$, и

- $h\ge0$ — $(1,c)$-квазиоднородная функция класса $C^2$ степени $d_h<\beta$: $h(tx,t^cy)=t^{d_h}h(x,y)$;
- $Z_h=\{b:\ h(1,b)=0\}$ пересекает шар $B_{r_1}$, а на сфере $|b|=r_1$ $h(1,b)>0$;
- $x^{-\beta}\big(|r|+|x\partial_xr|+|\langle Cy,\nabla_yr\rangle|+\max_ix^{c_i}|\partial_{y_i}r|\big)\to0$ при $x\to0$ равномерно на
  $\{|x^{-c}y|\le r_1\}$.

Тогда есть асимптотическая траектория; поле — весовая гомотетия $Y=e_x+Cy/x$ ($\xi=0$), $\mu=\min(\beta-d_h,\beta)$.

**Следствие E (любой профиль с изолированным нулём).** Пусть $n=3$, выполнены условия (Q1), (Q2)
утверждения Q (в частности, мономов с $\ell_c<\beta$ нет), и $Q\ge0$ около $0$ с изолированным нулём в $0$. После
перенумерации осей $c_1\le c_2$ (при $c_1>c_2$ оси меняются местами). Пусть либо $c_1=c_2$, либо $c_1<c_2$ и младшая
однородная форма $Q_d$ ($d=\operatorname{ord}_0Q$) удовлетворяет
$Q_d(0,1)\ne0$. Тогда есть асимптотическая траектория.

### Частные случаи

**Теорема 2D ($n=2$).** Пусть $n=2$, выполнены (Z) и (H<0). Тогда есть асимптотическая траектория.

**Предложение S′ (отражательная симметрия).** Пусть $n=3$, выполнено (Z), $S$ — отражение относительно
плоскости $\Pi\ni\omega$, $U\circ S=U$, и (H<0) выполнено точками из $\Pi$. Тогда есть асимптотическая
траектория, лежащая в $\Pi$.

**Невырожденный случай (теорема K0 [008]).** Пусть $n=3$, выполнены (Z) и (H<0), $g$ — из леммы B, и
$D^2p(0)=H\succ0$. Тогда $(c_*,c_*)\in\mathcal T$,
$c_*=(\beta-m+2)/2$, $Q_{(c_*,c_*)}=\frac12b^{\mathsf T}Hb$ и выполнены условия утверждения Q с $\mu=\min(2c_*,\beta)$.

**Квазиоднородный $U$.** Если $U$ — $(1,c)$-квазиоднородна степени $\beta>0$ ($U(tx,t^cy)=t^\beta U(x,y)$), $U(1,0)<0$ и
$\nabla_yU(1,0)=0$, то ось $x$ инвариантна, и решение $q(t)=(x(t),0)$ с $\dot x=-\sqrt{2|U(1,0)|}\,x^{\beta/2}$ —
асимптотическая траектория (при $\beta\ge2$).

### Примеры

Луч $+e_z$, поперечные координаты $(x,y)$; везде $\Sigma=\{\pm e_z\}$ и $D^2p(0)$ вырожден.

1. **K1:** $U=x^4+y^4-z^6$. Утверждение Q: $c=(\frac32,\frac32)$, $N=2$, $\beta=6$, $\gamma=0$, $F=-1+b_1^4+b_2^4$, $\mu=6$.
2. **P1:** $U=x^4+y^4-z^6+x^3z^2+2y^3z^2+xz^6+3yz^6$. Утверждение Q: $c=(\frac32,\frac32)$, $N=2$, $\beta=6$, $\gamma=0$,
   $F=-1+b_1^4+b_2^4+s(b_1^3+2b_2^3)+s^3(b_1+3b_2)$, $\mu=6$. Траектории есть вдоль $+e_z$ и $-e_z$.
3. **Λ:** $U=x^4-k_0x^2yz+y^2z^2+y^4-z^8+xz^7$, $k_0=\frac{199}{100}$. Теорема C′ с полем $\xi=(C-I)b$:
   $c=(2,3)$, $N=1$, $\beta=8$, $F=-1+Q+sb_1+s^4b_2^4$, $Q=b_1^4-k_0b_1^2b_2+b_2^2$, $\mu=4$. При этом условие (Q3)
   с весами оврага нарушено на каждом уровне $\{Q=\delta\}$, и $(V_1)$ [007] тоже нарушено: теорема 2 [007]
   в этой карте не применяется. [Эксперимент: базис Грёбнера sympy] $0$ — изолированная критическая
   точка $U$ (в выводе не используется).
4. **SH:** $U=z^4(y-x^2-xz)^2+x^6+y^6-z^{12}+xz^{11}$. В прямой карте ($L=I$) с $c=(2,4)$ есть знакопеременные
   мономы уровня $<\beta$; в карте со сдвигом $L(z)=\begin{pmatrix}1&0\\ z&1\end{pmatrix}$
   $F=-1+(b_2-b_1^2)^2+b_1^6+sb_1+s^6(b_1+sb_2)^6$, и теорема C′ с $\xi=Cb$ даёт траекторию, $\mu=8$.
   [Эксперимент: базис Грёбнера sympy] $0$ — изолированная критическая точка $U$ (в выводе не используется).

## Доказательство

### 1. Лемма B

**Литература** [BM88; сверено R34]:

- (SA1) Проекция относительно компактного полуаналитического множества субаналитична
  (определение 3.1); дополнение к субаналитическому множеству субаналитично (теорема 3.10, теорема
  Габриэлова о дополнении); пересечение конечного числа субаналитических множеств субаналитично
  (§3, после определения 3.1).
- (SA2) Если $\mathcal Z\subset\mathbb R^n$ субаналитично, $0\notin\mathcal Z$, $0\in\overline{\mathcal Z}$, то есть вещественно-аналитическое
  $\lambda$ на окрестности $[0,1]$ с $\lambda(0)=0$ и $\lambda((0,1])\subset\mathcal Z$. *Вывод из теоремы 0.2 BM88*
  (ректилинеаризация, по R34): для компакта $\{0\}$ есть аналитические $\Psi_i:\mathbb R^n\to\mathbb R^n$ и компакты
  $\mathcal K_i$ ($i$ из конечного набора), такие что $\bigcup\Psi_i(\mathcal K_i)$ — окрестность $0$, а каждое $\Psi_i^{-1}(\mathcal Z)$ —
  объединение квадрантов (определение 5.4 BM88). Для $a_k\in\mathcal Z$, $a_k\to0$, имеем $a_k=\Psi_i(z_k)$, $z_k\in \mathcal K_i$;
  по подпоследовательности индекс $i$ и квадрант $\mathcal Q\ni z_k$ одни и те же, $z_k\to z_*$, $\Psi_i(z_*)=0$.
  Квадрант выпукл и $z_*\in\overline{\mathcal Q}$, поэтому $z_*+t(z_1-z_*)\in\mathcal Q$ при $t\in(0,1]$, и
  $\lambda(t)=\Psi_i(z_*+t(z_1-z_*))$ — искомая дуга.

*Доказательство леммы B.*

1. *Стенки конуса.* Возьмём $\varepsilon_0\in(0,1)$ так, что $p>0$ при $0<|y|\le\varepsilon_0$. При $|y|\le\varepsilon_0x$
   имеем $|q|\le2x$, $u_m(q)=x^mp(y/x)\ge0$ и $|U-u_m|\le C_U|q|^{m+1}$. Для $\varepsilon'\in(0,\varepsilon_0)$ положим
   $p_{\min}(\varepsilon')=\min_{\varepsilon'\le|z|\le\varepsilon_0}p(z)>0$. Тогда при $\varepsilon'x\le|y|\le\varepsilon_0x$ и
   $x<p_{\min}(\varepsilon')/(C_U2^{m+1})$
   $$U(x,y)\ge x^m\big(p_{\min}(\varepsilon')-C_U2^{m+1}x\big)>0. \tag{1.1}$$
2. *Отрицательный минимум.* $\mu_s(x):=\min_{|y|\le\varepsilon_0x}U(x,y)$ определён (компакт). По (H<0) с
   $\varepsilon=\varepsilon_0$ есть $x_k\to0$ с $\mu_s(x_k)<0$ (так как $|q|\ge x$).
3. *Субаналитичность.* Пусть $\mathcal S=\{0<x<x_0,\ |y|\le\varepsilon_0x\}$ и
   $\mathcal B=\{(x,y,y'):\ (x,y)\in\mathcal S,\ |y'|\le\varepsilon_0x,\ U(x,y')<U(x,y)\}$, где $x_0$ так мал, что $U$ аналитична около
   $\overline{\mathcal S}$. $\mathcal B$ полуаналитично и относительно компактно, поэтому по (SA1) множество минимизаторов
   $\mathcal Z=\mathcal S\setminus\pi(\mathcal B)$ ($\pi$ — проекция на $(x,y)$) субаналитично. Каждый срез $\mathcal Z\cap\{x\}$ непуст и лежит в
   $|y|\le\varepsilon_0x$, так что $0\in\overline{\mathcal Z}$; $0\notin\mathcal Z$.
4. *Кривая.* По (SA2) есть аналитическая дуга $\lambda(t)=(x(t),y(t))\in\mathcal Z$, $t\in(0,1]$, $\lambda(0)=0$. Так как
   $x(t)>0$ при $t>0$ и $x(0)=0$, $x(t)=t^Ne(t)$, $e(0)>0$. Замена $\tau=t\,e(t)^{1/N}$ аналитически обратима около
   $0$ и сохраняет ориентацию; в ней $x=\tau^N$, $y=\tilde\gamma(\tau)$ с аналитической $\tilde\gamma$. Каждое малое $x>0$
   даёт ровно одно $\tau=x^{1/N}$, поэтому $\gamma(x)=\tilde\gamma(x^{1/N})$ — минимизатор в срезе $x$ при всех
   $0<x<x_1$, и $\underline U(x)=\mu_s(x)=U(x,\gamma(x))=\underline u(x^{1/N})$, $\underline u(s):=U(s^N,\tilde\gamma(s))$ аналитична.
5. *Знак и порядок.* $\underline u\not\equiv0$, так как $\mu_s(x_k)<0$; значит, $\underline u(s)=u_{j_0}s^{j_0}(1+O(s))$, и знак
   $\underline u$ при малых $s>0$ постоянен, то есть отрицателен: $a:=-u_{j_0}>0$, $\beta:=j_0/N$. Из $u_m\ge0$ на конусе
   и $|U-u_m|\le C_U(2x)^{m+1}$: $\underline U(x)\ge-C_U(2x)^{m+1}$, откуда $\beta\ge m+1$.
6. *Дно внутри.* По (1.1) при любом $\varepsilon'>0$ и малых $x$ минимизатор (где $U=\underline U(x)<0$) лежит в
   $|y|<\varepsilon'x$. Значит, $\gamma(x)/x\to0$, то есть $g_j=0$ при $j\le N$; $\gamma=O(x^{1+1/N})$, $\gamma'=O(x^{1/N})$,
   $x\gamma''=O(x^{1/N})$, и минимум внутренний: $\nabla_yU(x,\gamma(x))=0$. Уменьшив $x_0$, получаем
   $|\gamma|\le\varepsilon_0x/2$.
7. *Свойства $g$.* Аналитичность — композиция. $g(s,0)=0$ по определению; $\nabla_wg(s,0)=0$ при $s>0$ по п. 6,
   при всех $s$ — по аналитичности; $g\ge0$, так как $\gamma$ — минимизатор в срезе. П. 5: $u_k(s^N,\tilde\gamma+w)$ при
   $k>m$ состоит из мономов порядка $\ge k>m$; $\underline u$ имеет порядок $\beta>m$; в
   $u_m(x,\tilde\gamma+w)=\sum_\alpha p_\alpha x^{m-|\alpha|}(\tilde\gamma+w)^\alpha$ каждая замена множителя $w_i$ на компоненту
   $\tilde\gamma$ (порядка $\ge1+\frac1N$) повышает порядок не менее чем на $\frac1N$. Порядок — функция монома, поэтому
   коэффициенты мономов порядка $m$ — это коэффициенты $u_m(s^N,w)$. $\square$

### 2. Лемма 3

Конечность: $\ell_c<\beta+\theta$ влечёт $k<N(\beta+\theta)$ и $|\alpha|<(\beta+\theta)/c_{\min}$. Пусть $s_1\le\min(S,1)/2$ и
$s_1^{Nc_i}r\le\varrho/2$. Для монома хвоста показатель $e=N(\ell_c-\beta)\ge N\theta$, и при $s\le s_1$
$$s^e|b^\alpha|\le s^{N\theta}s_1^{e-N\theta}r^{|\alpha|}=s^{N\theta}s_1^{-N(\beta+\theta)}\,s_1^k\prod_i(s_1^{Nc_i}r)^{\alpha_i}\le s^{N\theta}s_1^{-N(\beta+\theta)}(S/2)^k(\varrho/2)^{|\alpha|}.$$
Ряд $\sum|a_{k\alpha}|(S/2)^k(\varrho/2)^{|\alpha|}\varpi(k,\alpha)$ сходится для любого многочлена $\varpi$, так как
$\sum|a_{k\alpha}|S^k\varrho^{|\alpha|}<\infty$, а $\varpi(k,\alpha)2^{-k-|\alpha|}$ ограничено. Оператор $s\partial_s$ даёт множитель
$e\le k+Nc_{\max}|\alpha|$, оператор $\partial_{b_i}$ — множитель $\alpha_i$ и замену $r^{|\alpha|}$ на $r^{|\alpha|-1}$ (оценка та же
множитель $1/r$). Ряды производных сходятся равномерно, так что почленное дифференцирование
законно. $\square$

### 3. Предложение N

1. По лемме B, п. 5, в $g$ есть моном $p_{(j_1,0)}s^{N(m-j_1)}w_1^{j_1}$, $p_{(j_1,0)}\ne0$ ($p(y_1,0)\not\equiv0$, иначе нуль
   $p$ не изолирован; $j_1$ — порядок нуля $p(y_1,0)$). Его уровень $m+j_1(c_1-1)\ge\varphi(c)\ge\beta>m$. Так же для
   $c_2$.
2. Минимум достигается на каком-то мономе (мономов с $\ell_c\le\beta+1$ конечное число), и его коэффициент
   входит в $Q_c$, так что $Q_c\not\equiv0$. Для фиксированного $b$ и малых $x$ точка $\gamma+x^cb$ лежит в конусе
   $|y|\le\varepsilon_0x$ (так как $c_i>1$ по п. 1), поэтому $x^{-\beta}g(x^{1/N},x^cb)\ge0$. Мономов с $\ell_c<\beta$ нет, уровни
   дискретны, и по лемме 3 (с $\theta$ меньше зазора между $\beta$ и следующим уровнем) это выражение
   стремится к $Q_c(b)$. Значит, $Q_c\ge0$.
3. На области $\{\varphi\le\beta+1\}$ функция $\varphi$ — минимум конечного числа аффинных функций, то есть вогнута и
   кусочно-линейна. $\mathcal T=\partial\{\varphi\ge\beta\}$ в открытом квадранте: внутренних точек $\{\varphi\ge\beta\}$ в $\mathcal T$ нет (иначе
   вогнутая $\varphi$ была бы локально постоянна, а $\varphi(c+t(1,1))>\beta$ при $t>0$). Поэтому $\mathcal T$ — локально выпуклая
   ломаная. Пусть $c$ лежит внутри звена: $c+tv\in\mathcal T$ при малых $|t|$. Для монома уровня $\beta$ в точке $c$:
   $\beta+t\,v\cdot\alpha=\ell_{c+tv}\ge\varphi(c+tv)=\beta$ при $t$ обоих знаков, откуда $v\cdot\alpha=0$. Случай $v_1v_2>0$ невозможен
   (тогда $\alpha=0$, а у $g$ все $|\alpha|\ge2$). При $v_1v_2<0$ все такие $\alpha$ пропорциональны одному $\alpha_0\in\mathbb N^2$ с
   $\alpha_0>0$ покомпонентно, и $Q_c=f_0(b^{\alpha_0})$, $f_0(0)=0$; при $v_2=0$ все $\alpha_1=0$, при $v_1=0$ все $\alpha_2=0$. В
   каждом случае $Q_c$ обращается в нуль на координатной оси. Если нуль $Q_c$ изолирован, то
   $Q_c(b_1,0)\not\equiv0$ и $Q_c(0,b_2)\not\equiv0$.
4. По лемме B, п. 5, $(1,1)$-уровень, то есть порядок, мономов $g$ не меньше $m$ и равен $m$ у мономов $u_m(s^N,w)$:
   $\varphi(1,1)=m<\beta$. Функция $t\mapsto\varphi(t,t)$ непрерывна, строго возрастает (все $|\alpha|\ge2$) и стремится к $\infty$.
   $\square$

### 4. Утверждение Q

Проверим условия следствия 2 [007] для прямой карты $\Phi(x,u)=(x,\gamma(x)+u)$.

1. $\gamma\in C^2((0,s_0))$ и $\gamma,\gamma',x\gamma''\to0$: ряд Пюизё с показателями $>1$ (пример из формулировки
   следствия 2 [007]).
2. (F): по (Q1) $F(s,b):=x^{-\beta}U(x,\gamma+x^cb)=\sum a_{k\alpha}s^{k+Nc\cdot\alpha-N\beta}b^\alpha$, и показатели $s$ —
   неотрицательные целые (так как $Nc_i,N\beta\in\mathbb N$). Конечная часть (уровни $<\beta+1$) — многочлен от $(s,b)$,
   хвост мал вместе с производными по лемме 3 (применённой к $\hat U$ и любому $r_0$). Поэтому $F$ и $\nabla_bF$
   продолжаются непрерывно на $[0,s_1]\times\overline{B_{r_0}}$, $F(0,\cdot)=F_0$ и $\sup_{|b|\le r_0}|s\partial_sF|\to0$.
3. $(V_0)$: выберем $r_1$ так, что $Q>0$ на $0<|b|\le r_1$ и (Q3) верно на $B_{r_1}$; положим $r_0=r_1$,
   $q_1=\min_{|b|=r_1/2}Q>0$ и $\delta\in(0,\min(q_1,|F_0(0)|/2))$. Компонента $\Omega_b$ множества $\{Q<\delta\}$, содержащая
   $0$, связна и не пересекает сферу $|b|=r_1/2$, поэтому $\overline{\Omega_b}\subset\overline{B_{r_1/2}}\subset B_{r_0}$; $Q\ge0$ на $\Omega_b$;
   неравенство Эйлера на $\overline{\Omega_b}$ — (Q3).

Следствие 2 [007] даёт карту класса (GT3) с $C_1=0$ и условием $(V_0)$; теорема 2 [007] — траекторию с
указанными свойствами. Градуированная положительность: мономы $Q^{(k)}$ удовлетворяют
$c\cdot\alpha=\beta-k/N$, а оператор $\langle Cb,\nabla\rangle$ умножает $b^\alpha$ на $c\cdot\alpha$; $d_k>0$, так как $\alpha\ne0$, и $d_k\le\beta$. $\square$

### 5. Теорема 2U

#### 5.1. Тождества

В координатах $(x,b)$: $b=x^{-c}L^{-1}(y-\gamma)$; $Y\cdot\nabla$ — производная вдоль $Y=e_x+\tilde Z$.

**(I1)** $Y\cdot\nabla b=-\xi/x$, $Y\cdot\nabla x=1$; значит, на функциях от $(x,b)$:
$Y\cdot\nabla=\partial_x|_b-\frac1x\,\xi\cdot\nabla_b$.

*Вывод.* $\partial_x|_yb=-Cb/x-x^{-c}L^{-1}L'x^cb-x^{-c}L^{-1}\gamma'$ (использовано $(L^{-1})'=-L^{-1}L'L^{-1}$),
$\partial_yb=x^{-c}L^{-1}$. По (0.1) $x^{-c}L^{-1}\tilde Z=x^{-c}L^{-1}\gamma'+x^{-c}L^{-1}L'x^cb+(Cb-\xi)/x$ (диагональные
матрицы коммутируют), и $Y\cdot\nabla b=\partial_x|_yb+x^{-c}L^{-1}\tilde Z=-Cb/x+(Cb-\xi)/x=-\xi/x$.

**(I2)** Для $W\circ\Phi=x^\beta P(s,b)$: $x\,Y\cdot\nabla W=x^\beta\big[\beta P+\frac sN\partial_sP-\xi\cdot\nabla_bP\big]$. Следует из (I1) и
$x\partial_x|_bP=\frac sN\partial_sP$.

**(I3)** $\mathcal M:=x\,\partial_y\tilde Z=xL'L^{-1}+L\mathcal AL^{-1}$, где $\mathcal A_{ij}=x^{c_i-c_j}\big(c_i\delta_{ij}-\partial_{b_j}\xi_i\big)$.

*Вывод.* $\partial_b\tilde Z=L'x^c+Lx^{c-1}(C-D_b\xi)$ и $\partial_y=\partial_b\cdot x^{-c}L^{-1}$.

**(I4)** $x\,Y\cdot\nabla\tilde Z=x\gamma''+xL''x^cb+L'Cx^cb+L'x^c(Cb-\xi)+L(C-I)x^{c-1}(Cb-\xi)
-L'x^c\xi-Lx^{c-1}\big(C\xi-D_b\xi\,\xi\big)-Lx^{c-1}\tfrac sN\partial_s\xi$.

*Вывод.* $x\,Y\cdot\nabla=x\partial_x|_b-\xi\cdot\nabla_b$ по (I1); почленно дифференцируем (0.1), учитывая
$x\partial_x(x^{c-1})=(C-I)x^{c-1}$ и $x\partial_x|_b\xi=\frac sN\partial_s\xi$.

[Эксперимент] (I1)–(I4) проверены символьно: автором — для конкретных нелинейных $\gamma$ (ряд Пюизё),
$L(x)$, $\xi(s,b)$, $P(s,b)$ в 8 точках с 50 знаками (расхождение $\le6\cdot10^{-46}$); R34 — для произвольных
функций и символьных весов (невязки тождественно $0$), с контролем чувствительности.

#### 5.2. Доказательство

Применяем теорему A и лемму 2 [007]. Они сформулированы для любых данных $(G,\rho,Y,A)$ с
$Y\in C^1(G)$ и $\langle\nabla\rho,Y\rangle\equiv1$; равенство $Y=\partial_x\Phi$ используется только в доказательстве
теоремы 2 [007], на которую мы не ссылаемся. Данные: $G=\Phi(\mathcal N)$, $\rho=x$, $Y=e_x+\tilde Z$, $A(r)=a_0r^\beta$,
$\sigma_0=s_0$, и
$$\mathcal D=\{(x,b):\ 0<x<\sigma,\ |b|<r_1,\ P(s,b)<\delta\},\qquad D=\Phi(\mathcal D),$$
где $\sigma<s_0$ выбирается в шаге 6.

1. *Данные.* $\Phi$ — $C^2$-диффеоморфизм $\mathcal N$ на открытое множество
   $\{0<x<s_0,\ |x^{-c}L^{-1}(y-\gamma)|<r_0\}$ с обратным $(x,y)\mapsto(x,x^{-c}L^{-1}(y-\gamma))$. $\rho\in C^2(G)$, $\rho>0$.
   $Y\in C^1(G)$: $\gamma',L'\in C^1$, $\xi\in C^1$, $b(x,y)\in C^2$, $s=x^{1/N}$ гладко при $x>0$.
   $\langle\nabla\rho,Y\rangle=1$. $W\circ\Phi=x^\beta P$.
2. *Малые величины.* При $x<\sigma$, $|b|\le r_1$ положим
   $$\zeta(\sigma):=\sup|\tilde Z|\le\sup_{x<\sigma}\Big(|\gamma'|+\|L'\|x^{c_{\min}}r_1+2x^{c_{\min}-1}(c_{\max}r_1+M_0)\Big),\qquad
   \theta_2(\sigma):=\sup|x\,Y\cdot\nabla\tilde Z| .$$
   По (I4) каждое слагаемое $\theta_2$ оценивается через $x|\gamma''|$, $x^2\|L''\|\,x^{c_{\min}-1}$, $x\|L'\|\,x^{c_{\min}-1}$,
   $x^{c_{\min}-1}$ с множителями из $c_{\max},r_1,M_0,M_1,M_2$ (используем $x<1$, $x^{c_i}\le x^{c_{\min}}$). Так как
   $c_{\min}>1$, $\zeta(\sigma)\to0$ и $\theta_2(\sigma)\to0$ при $\sigma\to0$.
3. *(D1)–(D3).* (D1): на $D$ $\rho=x<\sigma$. Если $q=\lim\Phi(x_k,b_k)$, $(x_k,b_k)\in\mathcal D$, то по подпоследовательности
   $x_k\to\bar x$, $b_k\to\bar b$, $|\bar b|\le r_1$; при $\bar x>0$ $q=\Phi(\bar x,\bar b)\in G$, при $\bar x=0$
   $|q|\le x_k+|\gamma(x_k)|+2x_k^{c_{\min}}r_1\to0$. Отсюда $\overline D\setminus0\subset G$ и $\sup\{|q|:\ q\in D,\ \rho<\epsilon'\}\to0$ при $\epsilon'\to0$;
   $\rho(q)=x\le|q|$. (D2): пусть $q\in\partial D\setminus0$, $\rho(q)<\sigma$. Тогда $q=\Phi(\bar x,\bar b)$, и $(\bar x,\bar b)$ лежит
   в замыкании $\mathcal D$ в $\mathcal N$, но не в $\mathcal D$ ($\Phi$ — гомеоморфизм): $|\bar b|\le r_1$, $P\le\delta$ и ($|\bar b|=r_1$
   или $P\ge\delta$). Случай $|\bar b|=r_1$ невозможен по (U3) ($P\ge2\delta>\delta$). Значит, $P(\bar s,\bar b)=\delta$ и
   $W(q)=\delta\rho^\beta$. (D3): при $\eta(x^{1/N})<\delta$ точка $\Phi(x,b_0)$ лежит в $D$ и $W\le\eta x^\beta<\delta\rho^\beta$ по (U1).
4. *Точки $D_\sigma$.* Как в (D2), каждая точка $\overline D$ с $q\ne0$, $\rho<\sigma$ имеет вид $\Phi(x,b)$ с $|b|<r_1$, $P\le\delta$.
5. *Константы леммы 2 [007].*
   - (L0): $a_1=a_3=a_0$, $a_2=\beta a_0$, $\delta\le a_0/2$.
   - (L1): $h=1+|\tilde Z|^2\in[1,\frac32]$ при $\zeta\le1/\sqrt2$; $h_0=1$, $h_1=\frac32$.
   - (L2): $W=x^\beta P\ge-\eta x^\beta\ge-\delta\rho^\beta$ по (U2) (при $\eta\le\delta$). По (I2) и (U4) (применимо по шагу 4)
     $\beta W-\rho\,YW=x^\beta\big[\xi\cdot\nabla_bF-\frac sN\partial_sF\big]\ge\mu W-(\varepsilon_E+\bar\eta)\rho^\beta$, где
     $\bar\eta:=\sup_{s<\sigma^{1/N}}\eta$; то есть $\varepsilon_1=(\varepsilon_E+\bar\eta)/\delta\ge0$.
   - (L3), $\theta_1$: $\nabla\rho-Y/h=\big((h-1)/h,\,-\tilde Z/h\big)$, $|\nabla\rho-Y/h|^2=|\tilde Z|^2/h$; $\theta_1=\zeta$.
   - (L3), $\theta_2$: первая компонента $\nabla_YY$ равна $Y\cdot\nabla1=0$, поэтому $\rho|(\nabla_YY)^\perp|\le|xY\cdot\nabla\tilde Z|\le\theta_2$.
   - (L3), $\theta_3$: пусть $w=(w_x,w_y)\perp Y$; тогда $w_x=-\langle\tilde Z,w_y\rangle$, $|w_x|\le\zeta|w|$. Так как
     $Y=\partial_x|_y+\tilde Z\cdot\partial_y$, имеем $w\cdot\nabla=w_x\,Y\cdot\nabla+(w_y-w_x\tilde Z)\cdot\partial_y$ и
     $$\rho\langle w,D_wY\rangle=\langle w_y,\,x(w\cdot\nabla)\tilde Z\rangle=w_x\langle w_y,xY\cdot\nabla\tilde Z\rangle+\langle w_y,\mathcal Mw_y\rangle-w_x\langle w_y,\mathcal M\tilde Z\rangle .$$
     По (I3) $\langle w_y,\mathcal Mw_y\rangle\ge\langle w_y,\mathcal Aw_y\rangle-\big(x\|L'L^{-1}\|+\|L\mathcal AL^{-1}-\mathcal A\|\big)|w|^2$. В
     $\langle w_y,\mathcal Aw_y\rangle=\sum_{i,j}\mathcal A_{ij}w_iw_j$ пары с $c_i<c_j$ дают $0$ по (T) ($i\ne j$, $\mathcal A_{ij}=-x^{c_i-c_j}\partial_{b_j}\xi_i=0$);
     пары внутри блоков дают в сумме $\ge0$ по (Θ) (там $x^{c_i-c_j}=1$); каждая пара с $c_i>c_j$ даёт не меньше
     $-x^{\Delta}M_1|w|^2$, $\Delta:=\min\{c_i-c_j>0\}$ (если все веса равны, таких пар нет). По (T) элементы $\mathcal A$
     ограничены числом $c_{\max}+M_1$, так что $\|\mathcal A\|\le\mathcal A_*:=(n-1)(c_{\max}+M_1)$, и
     $\|L\mathcal AL^{-1}-\mathcal A\|\le\mathcal A_*(2\|L-I\|+\|L^{-1}-I\|)\to0$, $\|\mathcal M\|\le2x\|L'\|+4\mathcal A_*$. Итого
     $$\theta_3(\sigma)=\sup_{x<\sigma}\Big[\zeta\big(\theta_2+\|\mathcal M\|\zeta\big)+2x\|L'\|+\mathcal A_*(2\|L-I\|+\|L^{-1}-I\|)+(n-1)^2M_1x^{\Delta}\Big]\to0 .$$
6. *Выбор $\sigma$.* Возьмём $\sigma<s_0$ так, что $\zeta\le1/\sqrt2$, $\bar\eta\le\min(\delta/4,\mu\delta/8)$,
   $(L_1\theta_1+L_2\theta_2)/\sqrt\delta+4\theta_3\le\mu/4$, где $L_1=3\beta\sqrt{3a_0/2}$, $L_2=2\sqrt{2a_0}$ — константы (3.1) [007]
   при $h_0=1$, $h_1=\frac32$, и $4\theta_1\sqrt\delta\le\sqrt{a_0/h_1}$. Тогда $\varepsilon_1\le\mu/8+\mu/8$, и скобка (3.1) [007] не
   меньше $\mu-\mu/4-\mu/4=\mu/2>0$.

Лемма 2 [007] даёт (D4), (A4), (A5) и оценку $\dot\rho$ (её п. 1); теорема A [007] — решение в $\overline\Omega$ с
$q(t)\ne0$, $q,\dot q\to0$, и неустойчивость. По шагу 4 $q(t)=\Phi(x(t),b(t))$, $|b(t)|<r_1$.

*Направление.* Поперечная часть $q(t)$ равна $\gamma(x)+L(x)x^cb$, и $|\gamma(x)|\le x\sup_{(0,x)}|\gamma'|=o(x)$ (так как
$\gamma\to0$), $|Lx^cb|\le2r_1x^{c_{\min}}=o(x)$. Так как $|q|\ge x$, $|q/|q|-e_x|\le2(|\gamma|+2r_1x^{c_{\min}})/x\to0$. $\square$

### 6. Теорема C′

$P=F+a_0=\sum_js^{-e_j}R_j+F_>$; при $s<1$ имеем $s^{-e_j}\ge1$. Уменьшим $s_0$ так, чтобы $\chi\le q_1/2$ при
$s<s_0^{1/N}$ (данные теоремы 2U при этом сохраняются). Положим $\eta:=(M_0+\frac1N+\mu+1)\chi\ge0$.

- (U1): $P(s,b_0)=F_>(s,b_0)\le\chi\le\eta$ по (C1).
- (U2): $P\ge-\chi\ge-\eta$ на $B_{r_1}$, так как $R_j\ge0$.
- (U3): на $|b|=r_1$ $P\ge R-\chi\ge q_1/2\ge2\delta$.
- (U4): оператор $\mathcal E_\xi:=\xi\cdot\nabla_b-\frac sN\partial_s$ даёт $\mathcal E_\xi(s^{-e_j}R_j)=s^{-e_j}\big(\xi\cdot\nabla R_j+\frac{e_j}NR_j\big)$ и
  $|\mathcal E_\xi F_>|\le(M_0+\frac1N)\chi$ на $\overline{B_{r_1}}$. По (C3)
  $$\mathcal E_\xi F\ge\mu\sum_{e_j>0}s^{-e_j}R_j+\mu R^{(0)}-\varepsilon_E-(M_0+\tfrac1N)\chi=\mu(P-F_>)-\varepsilon_E-(M_0+\tfrac1N)\chi\ge\mu P-\varepsilon_E-\eta .$$

Константы: $\delta=\min(a_0/2,q_1/4)\in(0,a_0/2]$, $\varepsilon_E\le\mu\delta/8$, $\mu\in(0,\beta]$; $M_2=0$. Теорема 2U. $\square$

### 7. Следствия

**Следствие R.** Для монома $u_m(s^N,w)$: $k/N=m-|\alpha|$, и $\ell_c=\beta$ означает $(c-1)\cdot\alpha=\beta-m$. Значит, $Q_c$ —
$(c-1)$-квазиоднородный многочлен степени $\beta-m>0$ ($\beta\ge m+1$ по лемме B) и
$\langle(C-I)b,\nabla Q_c\rangle=(\beta-m)Q_c$. Положим $\Phi(x,b)=(x,\gamma+x^cb)$ ($L=I$, $\gamma$ — дно леммы B),
$F=x^{-\beta}\underline U(x)+x^{-\beta}g(s,x^cb)$. Так как $c\in\mathcal T$, мономов с $\ell_c<\beta$ нет, и
$F=-a+Q_c(b)+F_>$, $F_>=\big(x^{-\beta}\underline U+a\big)+(\text{мономы }g\text{ с }\ell_c>\beta)$; по лемме B, п. 2, и лемме 3
$\chi=O(s)$ (показатели $s$ натуральные, так как $Nc_i\in\mathbb N$). Теорема C′: $J=1$, $R_1=Q_c\ge0$ на $\mathbb R^2$
(предложение N, п. 2), $e_1=0$, $b_0=0$, $a_0=a$; $\xi=(C-I)b$: (T) — диагонально, (Θ): $c_i-(c_i-1)=1\ge0$;
$\mu=\min(\beta-m,\beta)=\beta-m$, $\varepsilon_E=0$; $r_1$ — радиус, при котором $Q_c>0$ на $0<|b|\le r_1$; $r_0>r_1$ любое. $\square$

**Следствие X.** Теорема C′ с $\xi=(\lambda_ib_i)_i$ и $\Phi(x,b)=(x,\gamma+x^cb)$: $F=x^{-\beta}\hat U(s,x^cb)$. Слагаемые:
$R^{(0)}=Q_c$ ($e=0$); каждый моном $a_{k\alpha}b^\alpha$ с $\alpha\ne0$, $\ell_c<\beta$ — отдельное $R_j=a_{k\alpha}b^\alpha\ge0$ с
$e_j=N(\beta-\ell_c^{(j)})>0$ (таких мономов конечное число, лемма 3); $F_>=x^{-\beta}\hat U(s,0)+a_0+(\text{мономы с }\alpha\ne0,\ \ell_c>\beta)$,
$\chi=O(s)$ по лемме 3 и условию на $\hat U(s,0)$. Для монома
$\xi\cdot\nabla R_j+\frac{e_j}NR_j=(\lambda\cdot\alpha_j+\beta-\ell_c^{(j)})R_j$, и $\lambda\cdot\alpha_j\ge0$. (C3) — с указанным $\mu$
($\varepsilon_E=0$); $r_0$ берём так, что $Q_c\ge0$ на $B_{r_0}$ и неравенство для $\lambda$ верно там. (T): диагонально;
(Θ): $c_i-\lambda_i\ge0$. (C2): $R\ge Q_c>0$ на сфере малого радиуса $r_1$. (C1): $b_0=0$ ($\alpha\ne0$). $\square$

**Следствие SV.** Положим $t=b_2-\psi(b_1)$. Тогда $\xi\cdot\nabla b_1=\alpha b_1$,
$\xi\cdot\nabla t=\alpha\big(b_1\psi'+2t\big)-\psi'\alpha b_1=2\alpha t$, так что $\xi\cdot\nabla(\mathfrak at^2)=(4\alpha \mathfrak a+\xi\cdot\nabla \mathfrak a)t^2$ и
$\xi\cdot\nabla \mathfrak b=\alpha b_1\mathfrak b'\ge\alpha\nu_B\mathfrak b$. Возьмём $r_0$ так мало, что $\mathfrak a\ge \mathfrak a(0)/2$ и $\mathfrak b\ge0$ на $B_{r_0}$; тогда
$R_1,R_2\ge0$ там. Так как $|\xi|\le C_\psi\alpha|b|$ ($\psi(0)=\psi'(0)=0$), при малом $r_1$ имеем
$|\xi\cdot\nabla \mathfrak a|\le\alpha C_\psi r_1\sup|\nabla \mathfrak a|\le\alpha \mathfrak a(0)\le2\alpha \mathfrak a$, откуда $\xi\cdot\nabla R_1\ge2\alpha R_1$. Члены $\frac{e_j}NR_j\ge0$ только
помогают: (C3) с $\mu=\min(\alpha\min(2,\nu_B),\beta)$, $\varepsilon_E=0$. (T): $\xi_1=\alpha b_1$ не зависит от $b_2$, а
$\partial_1\xi_2\ne0$ разрешено, так как $c_2>c_1$. (Θ): блоки одномерны, $c_1-\alpha\ge0$, $c_2-2\alpha\ge c_1-2\alpha\ge0$.
$\xi\in C^1$ с ограниченной производной ($\psi\in C^2$). (C1): $b_0=0$. (C2): если $R_1(b)=R_2(b)=0$, то $b_2=\psi(b_1)$
и $b_1=0$, то есть $b=0$; значит, $R>0$ на сфере $|b|=r_1$. Теорема C′. $\square$

**Следствие S.** $F=-a_0+s^{-e}R_1(b)+F_>$ с $R_1=h(1,b)$, $e=N(\beta-d_h)>0$ (квазиоднородность:
$x^{-\beta}h(x,x^cb)=x^{d_h-\beta}h(1,b)$), $F_>=x^{-\beta}r(x,x^cb)$. Далее
$\nabla_bF_>=x^{-\beta}\big(x^{c_i}\partial_{y_i}r\big)_i$ и $x\partial_x|_bF_>=x^{-\beta}\big(-\beta r+x\partial_xr+\langle Cy,\nabla_yr\rangle\big)$; по условию на $r$
$\chi\to0$ на $\overline{B_{r_1}}$. Теорема C′ (с этим $r_1$ и любым $r_0>r_1$ в пределах карты): $\xi=0$, (T) пусто,
(Θ): $c'I\succeq0$; (C3): $0+\frac eNR_1=(\beta-d_h)R_1$, $R^{(0)}=0$; (C1): $b_0\in Z_h\cap B_{r_1}$; (C2): $R_1>0$ на сфере. $\square$

**Следствие E.** $Q$ — многочлен (мономов уровня $\beta$ конечное число). $Q>0$ в проколотой окрестности нуля.

1. *Поле.* Теорема E [009] — при $c_1<c_2$ в данных координатах (там предполагается $Q_d(0,1)\ne0$), при
   $c_1=c_2$ после поворота $\mathcal R$ плоскости $b$, при котором $Q_d(0,1)\ne0$ ($Q_d\ge0$, $Q_d\not\equiv0$ имеет
   конечное число нулевых прямых), — даёт диск $D_r$, числа $K\ge1$, $m_E\in\mathbb N$ и поле
   $\xi^0=(b_1,\,b_2+\kappa_E(b))$ с $\kappa_E\in C^1(D_r\setminus0)\cap C^0(D_r)$, $|\kappa_E|\le K|b_1|^{1+1/m_E}$, $\|D\xi^0\|\le K$ на
   $D_r\setminus0$, $\xi^0\cdot\nabla Q\ge\frac d4Q$ (в [009] поправка обозначена $c(b)$).
2. *Гладкость в нуле.* Пусть $\vartheta\in C^\infty$, $\vartheta=1$ на $[0,1]$, $\vartheta=0$ на $[2,\infty)$, $|\vartheta'|\le2$,
   $\vartheta_\epsilon(b)=\vartheta(|b|/\epsilon)$, $0<\epsilon\le\frac12$, $2\epsilon<r$. Положим $\xi^\epsilon=(b_1,\ b_2+(1-\vartheta_\epsilon)\kappa_E)$. Это
   $C^1$ на $D_r$ (около нуля $\xi^\epsilon=b$), $\xi^\epsilon_1=b_1$,
   $D\xi^\epsilon=(1-\vartheta_\epsilon)D\xi^0+\vartheta_\epsilon I-(0,\kappa_E\nabla\vartheta_\epsilon)$, и
   $\|D\xi^\epsilon\|\le K+1+K(2\epsilon)^{1+1/m_E}\cdot\frac2\epsilon\le5K+1=:K'$. Далее
   $\xi^\epsilon\cdot\nabla Q=(1-\vartheta_\epsilon)\,\xi^0\cdot\nabla Q+\vartheta_\epsilon\langle b,\nabla Q\rangle\ge\frac d4Q-\mathrm{err}(\epsilon)$,
   $\mathrm{err}(\epsilon):=\sup_{|b|\le2\epsilon}\big(\frac d4Q+|b||\nabla Q|\big)\to0$ при $\epsilon\to0$.
3. *Поворот.* При $c_1=c_2$ берём $\mathcal R\xi^\epsilon(\mathcal R^{-1}b)$: $D$ сопрягается поворотом, норма и знак
   симметричной части $cI-D\xi$ сохраняются; (T) пусто.
4. *(Θ) масштабированием.* $\xi:=\alpha\xi^\epsilon$, $\alpha=\min(1,c_{\min}/K')$. При $c_1=c_2=c$:
   $cI-\alpha\,\mathrm{sym}D\xi^\epsilon\succeq(c-\alpha K')I\succeq0$. При $c_1<c_2$: блоки одномерны, $c_1-\alpha\ge0$,
   $c_2-\alpha\partial_2\xi_2^\epsilon\ge c_2-c_{\min}\ge0$; (T): $\xi_1=\alpha b_1$ — здесь существенно, что у поля теоремы E
   $\xi_1\equiv b_1$ (следствие 6.1(a) [009]).
5. *Теорема C′* с $J=1$, $R_1=Q$, $e_1=0$, $b_0=0$, $F_>=F-F_0$ ($\chi=O(s)$ по лемме 3), $\mu=\min(\alpha d/4,\beta)$, $r_1<r_0\le r$ с
   $Q>0$ на $0<|b|\le r_1$ и $Q\ge0$ на $B_{r_0}$, $\delta=\min(a_0/2,q_1/4)$. Константы $\alpha$, $\mu$ от $\epsilon$ не зависят;
   выбираем $\epsilon$ с $\alpha\,\mathrm{err}(\epsilon)\le\mu\delta/8=:\varepsilon_E$. Тогда (C3) выполнено. $\square$

### 8. Частные случаи

**Теорема 2D.** Лемма B ($n=2$, поперечная переменная $w\in\mathbb R$) даёт $\gamma$, $\beta$, $g=\sum a_{kj}s^kw^j$, все $j\ge2$.
Пусть $\varphi(c)=\min_{\operatorname{supp}g}(k/N+cj)$: $\varphi(1)=m<\beta$ (лемма B, п. 5), $\varphi$ непрерывна, строго возрастает и
$\to\infty$; пусть $c>1$ — решение $\varphi(c)=\beta$. Оно рационально ($c=(\beta-k/N)/j$), и, заменив $N$ кратным (ряд
$\tilde\gamma$ переписывается через $s=s'^{N'}$), считаем $Nc\in\mathbb N$. Профиль $Q(b)=\sum_{k/N+cj=\beta}a_{kj}b^j\not\equiv0$, $Q\ge0$
(довод предложения N, п. 2, дословно при $n=2$); значит, младший коэффициент $q_{j_0}>0$, $j_0\ge2$ чётно, и
$0$ — изолированный нуль. Около нуля $cbQ'=cj_0q_{j_0}b^{j_0}(1+O(b))$ и $Q=q_{j_0}b^{j_0}(1+O(b))$, так что
$cbQ'\ge\frac{cj_0}2Q$ при $|b|\le r_1$. Доказательство утверждения Q дословно проходит при $n=2$ (следствие 2
[007] — для любого $n$; (Q1) для $\hat U=g+\underline u$ выполнено, мономы $\underline u$ на уровне $\ge\beta$),
$\mu=\min(\frac{cj_0}2,\beta)$. $\square$

**Предложение S′.** Из $U\circ S=U$: $S\nabla U(Sq)=\nabla U(q)$, и при $q\in\Pi$ ($Sq=q$) $\nabla U(q)\in\Pi$. Решение плоской
системы с потенциалом $U|_\Pi$ — решение полной системы (ускорение $-\nabla U\in\Pi$ совпадает с градиентом
$U|_\Pi$). Ведущая форма $U|_\Pi$ — $u_m|_\Pi\ge0$; она $\not\equiv0$ (на большой окружности $\Pi\cap S^2$ точка $\omega$ —
изолированный нуль $u_m$), и $\omega$ — её изолированный нуль. Теорема 2D. $\square$

**Невырожденный случай.** $c_*-1=(\beta-m)/2$. Моном $s^kw^\alpha$ с $|\alpha|\ge3$ на уровне $\le\beta$ при весах
$(c_*,c_*)$ имел бы порядок $\le\beta-(c_*-1)|\alpha|\le(3m-\beta)/2<m$, а мономов порядка $<m$ нет. Мономы с $|\alpha|=2$
на уровне $\le\beta$ имеют порядок $\le\beta-2(c_*-1)=m$, то есть ровно $m$ (мономы $u_m$), и уровень ровно $\beta$.
Значит, $\varphi(c_*,c_*)=\beta$ и $Q=\frac12b^{\mathsf T}Hb$; $\langle C_*b,\nabla Q\rangle=2c_*Q$. Утверждение Q с $\gamma$ из леммы B,
$\mu=\min(2c_*,\beta)$ (после замены $N$ кратным, чтобы $Nc_*\in\mathbb N$). $\square$

**Квазиоднородный $U$.** $\nabla_yU(x,0)=\big(x^{\beta-c_i}\partial_{y_i}U(1,0)\big)_i=0$, так что ось $x$ инвариантна. На ней
$\ddot x=-\partial_xU(x,0)=\beta|U(1,0)|x^{\beta-1}$; решение нулевой энергии $\dot x=-\sqrt{2|U(1,0)|}\,x^{\beta/2}$ стремится к $0$
вместе с $\dot x$ при $\beta\ge2$. $\square$

### 9. Примеры

[Эксперимент: выкладки — sympy, точная арифметика, `examples.py`; пересчитаны R34 (K1, P1) и R36 (Λ, SH).]

1. **K1.** $u_4=x^4+y^4$, $p=y_1^4+y_2^4$. $\gamma=0$, $c=(\frac32,\frac32)$, $N=2$, $\beta=6$: $F=z^{-6}U(z^{3/2}b_1,z^{3/2}b_2,z)=-1+b_1^4+b_2^4$
   точно; (Q1) ✓, $Q=b_1^4+b_2^4$ — строгий минимум, $\langle Cb,\nabla Q\rangle=6Q$. Утверждение Q. (Ось $z$ инвариантна, и $\dot z=-\sqrt2z^3$ — тоже асимптотическая траектория; совпадает ли она с
   траекторией утверждения Q, не утверждается.)
2. **P1.** $u_4=x^4+y^4$. $\gamma=0$, $c=(\frac32,\frac32)$, $N=2$: $F=-1+b_1^4+b_2^4+s(b_1^3+2b_2^3)+s^3(b_1+3b_2)$; показатели $s$
   неотрицательны, $Q=b_1^4+b_2^4$, $\mu=6$. Утверждение Q. Все степени $z$ в P1 чётны, $U(x,y,-z)\equiv U(x,y,z)$, так
   что для $-e_z$ всё то же. Точное дно (не нужно для вывода): $U(z^2X_1,z^2X_2,z)=-z^6+z^8(f_1(X_1)+f_2(X_2))$,
   $f_1=X_1^4+X_1^3+X_1$, $f_2=X_2^4+2X_2^3+3X_2$; единственные критические точки $X_1=-1$ и $X_{2*}\approx-1.746017$;
   $\gamma(z)=z^2(-1,X_{2*})$, $\underline U(z)=-z^6-7.589968z^8$.
3. **Λ.** $u_4=(yz-\frac{k_0}2x^2)^2+(1-\frac{k_0^2}4)x^4+y^4\ge0$ ($1-k_0^2/4=399/40000$), $p=y_2^2-k_0y_1^2y_2+y_1^4+y_2^4$,
   $D^2p(0)$ ранга 1. $\gamma=0$, $c=(2,3)$, $N=1$, $\beta=8$: $F=-1+Q+sb_1+s^4b_2^4$, $Q=b_1^4-k_0b_1^2b_2+b_2^2=
   (b_2-\frac{k_0}2b_1^2)^2+(1-\frac{k_0^2}4)b_1^4>0$ вне нуля. $Q$ — $(1,2)$-квазиоднороден степени 4, и $(1,2)=c-1$:
   $\langle(C-I)b,\nabla Q\rangle=4Q$. Теорема C′: $\xi=(b_1,2b_2)$, $J=1$, $R_1=Q$, $e_1=0$, $b_0=0$, $F_>=sb_1+s^4b_2^4$, (T)
   диагонально, (Θ): $(2-1,3-2)=(1,1)$, $\mu=4$, $\varepsilon_E=0$. (Это поле следствия R, но само следствие R не
   применяется: $\gamma\equiv0$ — не дно леммы B.)
   *Теорема 2 [007] в этой карте не применяется.* $\langle Cb,\nabla Q\rangle=8b_1^4-7k_0b_1^2b_2+6b_2^2$; как форма от
   $\tau=b_2/b_1^2$ её дискриминант $49k_0^2-192=\frac{20449}{10000}>0$; например, $Q(1,1.16)=\frac{93}{2500}>0$,
   $\langle Cb,\nabla Q\rangle(1,1.16)=-\frac{213}{2500}<0$. Обе формы $(1,2)$-квазиоднородны степени 4, поэтому отрицательные
   значения есть на каждом уровне $\{Q=\delta\}$: $(V_0)$ нарушено при любом $\delta$; $(V_1)$ нарушено ($Q$ без члена
   $b_1^2$). Изолированность $0$: идеал $(\nabla U)$ нульмерен над $\mathbb C$ (базис Грёбнера, `isolated_check.py`).
4. **SH.** $u_6=x^6+y^6+y^2z^4$, $p=y_1^6+y_2^2+y_2^6$. В прямой карте с $c=(2,4)$ ($L=I$):
   $F=-1+s^{-2}b_1^2+s^{-1}(2b_1^3-2b_1b_2)+(b_2-b_1^2)^2+b_1^6+\dots$ — знакопеременный член $s^{-1}$ не укладывается в
   (0.2) с $R_j\ge0$. С $L(z)=\begin{pmatrix}1&0\\ z&1\end{pmatrix}$ ($L\to I$, $z\|L'\|=z\to0$, $L''=0$):
   $F=-1+(b_2-b_1^2)^2+b_1^6+sb_1+s^6(b_1+sb_2)^6$ точно. Теорема C′: $R_1=(b_2-b_1^2)^2$, $R_2=b_1^6$ ($e=0$),
   $\xi=Cb=(2b_1,4b_2)$: $\xi R_1=8R_1$, $\xi R_2=12R_2$, $\mu=8$; (T), (Θ) ($C-C=0$) выполнены; $F_>=sb_1+s^6(\dots)$.
   Изолированность $0$ — нульмерность идеала $(\nabla U)$ (`isolated_check.py`).

## Где работают аналитичность и изолированность

1. **Теорема 2U и теорема C′ — утверждения для $U\in C^2$.** Аналитичность в них не используется. Её
   роль играют степенные условия (U1)–(U4): отрицательный овраг глубины $-a_0x^\beta$ с конечным $\beta$, стенки
   и запас Эйлера степенного порядка. В гладких примерах Пенлеве–Уинтнера и Лалуа (устойчивое
   равновесие при $0$ — не минимуме; по CLAUDE.md и `problem/KNOWN_RESULTS.md`, с первоисточниками не
   сверено) отрицательные значения $U$ около нуля плоские (меньше любой степени $|q|$), так что (U1)–(U4) с
   конечным $\beta$ невыполнимы, и противоречия нет [Эскиз: по формулам из `problem/KNOWN_RESULTS.md`].
   Строгая часть [Доказано, сразу из теоремы 2U]: если равновесие устойчиво по Ляпунову, то данных и
   условий теоремы 2U для $U$ нет.
2. **Аналитичность работает в лемме B, лемме 3 и теореме E.** (а) [Доказано: лемма B] Дно — ряд Пюизё,
   глубина — $-ax^\beta(1+o(1))$ с конечным рациональным $\beta$ (субаналитичность множества минимизаторов,
   выбор кривой). [Эскиз] Для $C^\infty$ глубина может быть плоской (например, $\underline U(x)=-e^{-1/x}$), и
   степенной шкалы нет. (б) [Доказано: лемма 3] У сходящегося ряда уровни $\ell_c$ дискретны, мономов ниже
   любого уровня конечное число, хвосты равномерно малы; профили — многочлены. (в) [Литература:
   [009], раздел «Для $C^\infty$ лемма E неверна»] Теорема E требует аналитического профиля; для $C^\infty$ она
   неверна.
3. [Доказано: предложение N, п. 1; теорема 2U, шаги 2, 5] **Изолированность $\omega$ в $\Sigma$** даёт веса оврага $c_i>1$ (предложение N, п. 1): все поперечные
   направления узкие. Поэтому в теореме 2U $\zeta,\theta_2,\theta_3\to0$ при любом ограниченном $\xi$, и не нужен
   $\kappa$-приём теоремы 2′ [008], который требуется на кривых компонентах $\Sigma$ (там есть направление с весом
   $1$). Она же даёт стенки конуса (1.1) в лемме B.
4. **Изолированность критической точки $0$ не используется** ни в одной теореме: траектория выводится
   из (H<0). [Доказано] Если $u_m\ge0$ и $\Sigma$ конечно, то (H<0) для некоторой $\omega\in\Sigma$ следует уже из того,
   что $0$ — не минимум: точки $q_k\to0$ с $U(q_k)<0$ имеют $u_m(q_k/|q_k|)<C_U|q_k|\to0$, их направления
   накапливаются в конечном $\Sigma$, и около некоторой $\omega$ их бесконечно много в каждом конусе.
5. [Доказано, сразу из формулировок] Пример Уреньи (гладкий, тотальная неустойчивость нарушена; по
   `problem/KNOWN_RESULTS.md`, не сверено) с результатами не конфликтует: утверждается одна асимптотическая
   траектория, а не тотальная неустойчивость.

## Замечания

### 1. Что нового по сравнению с [007]

- Поле $Y$ свободно: условие Эйлера измеряется вдоль поля $\xi$ на плоскости $b$, а не вдоль весового
  оператора $\langle Cb,\nabla\rangle$. Пример Λ показывает, что это существенно, по крайней мере для данной прямой карты
  ($\gamma=0$, $c=(2,3)$): в ней теорема 2 [007] не применяется, а радиальное от дна поле работает; другие карты
  класса (GT3) не исключены. [Эксперимент `exit_check.py`, прямое
  дифференцирование $\Xi$ в $\mathbb R^3$ без леммы 1 [007]: минимум $(\rho/\lambda)\Xi/(\delta\rho^8)$ по точкам множества (A5)
  равен $-2.27$ и $-2.48$ ($\delta=0.05$, $0.01$) для $Y=e_z$ и $+3.54$, $+3.69$ для $Y=q/z$; у R36 на границе $P=\delta$
  значения стремятся к $\mu=4$.]
- Условие (F) не нужно: в (U1)–(U4) разрешены члены $s^{-e}R(b)$ с $e>0$ («крест», «кольцо»); они дают
  дополнительный запас $e/N$.
- Сдвиг/поворот $L(x)\to I$ (наклонные и вращающиеся овраги, пример SH).
- (T) и (Θ). Для **данного способа** оценки $\theta_3$ условие (T) необходимо: при $\partial_{b_j}\xi_i\ne0$, $c_i<c_j$
  элемент $\mathcal A_{ij}\sim x^{c_i-c_j}\to\infty$, и форма $\langle w_y,\mathcal Aw_y\rangle$ не ограничена снизу. Что без (T) теорема
  неверна, не доказано [Гипотеза: открыто]. (Θ) достигается масштабированием: если $\xi$ удовлетворяет (T) и
  (C3) с $\mu$, то $\alpha\xi$ при $\alpha\le\min(1,c_{\min}/M_1)$ удовлетворяет (T), (Θ) и (C3) с $\alpha\mu$; $\alpha\le1$ нужно, потому что
  член $\frac{e_j}NR_j$ (от $-\frac sN\partial_sF$) не масштабируется. [Доказано]

### 2. Касание луча

[Доказано, теорема 2U] $q(t)/|q(t)|\to\omega$: траектория касается луча в смысле направления. В [007]
(пример 13, коническое направление с весом 1) этого не было. **Не утверждается** сходимость к дну оврага
($b(t)\to0$; аналог вопроса R4 [007]).

### 3. Градуированные профили с двумя уровнями

[Доказано] Если $Q\ge0$ на всём $\mathbb R^2$ (так для профиля $Q_c$ предложения N, п. 2), то крайние части
градуированного $Q$ (наибольшей и наименьшей степени $d_k$) неотрицательны: на орбите $t\mapsto t^cb$
$Q(t^cb)=\sum_kt^{d_k}Q^{(k)}(b)\ge0$, и при $t\to0$ ($t\to\infty$) доминирует младшая (старшая) часть. Поэтому при двух
уровнях $k$ такой профиль градуированно положителен автоматически. При трёх и более уровнях средняя
часть может быть отрицательной (пример Λ). Без глобальной неотрицательности утверждение о старшей
части неверно (контрпример R34): у $U=-z^8+z^4(x^2+y^2)-z^2x^3$ ($c=(2,2)$, $N=1$, $\beta=8$) $F=-1+b_1^2+b_2^2-b_1^3$,
$Q^{(4)}=b_1^2+b_2^2$, $Q^{(2)}=-b_1^3\not\ge0$; утверждение Q при этом применимо ((Q3) около нуля при $\mu<4$).

### 4. Другие примеры [Доказано в записке, §5; проверено R36; в «Утверждение» не включены]

Луч $+e_z$, $\Sigma=\{\pm e_z\}$.

- **X** («крест»): $U=x^6+y^6+y^4z^2+x^2y^2z^2-z^{12}+xz^{11}$, $c=(2,\frac52)$, $N=2$:
  $F=-1+(b_1^6+b_2^4)+s^{-2}b_1^2b_2^2+s^2b_1+s^6b_2^6$. Следствие X ($\lambda=c$, $\mu=10$). В прямой карте с $\gamma=0$
  никакие веса не дают (F) с изолированным нулём профиля (вершины $\mathcal T$: $(2,3)$ и $(\frac52,\frac52)$, профили
  $b_1^6+b_1^2b_2^2$ и $b_2^4+b_1^2b_2^2$ с нулями на осях). [Доказано] $0$ — изолированная критическая точка:
  $\partial_yU=2y(3y^4+2y^2z^2+x^2z^2)$, и скобка положительна при $y\ne0$, так что $y=0$; тогда
  $\partial_xU=6x^5+z^{11}$, $\partial_zU=z^{10}(11x-12z)$: либо $z=0$ и $x=0$, либо $x=\frac{12}{11}z$ и
  $z^5\big(6(\frac{12}{11})^5+z^6\big)=0$, то есть $z=0$. (Подтверждено базисом Грёбнера — [Эксперимент].)
- **SV2** (R36): $U=(z^4y-z^4x^2-z^2x^3)^2+x^8+y^8-z^{16}+xz^{15}$, $c=(2,4)$, $N=1$:
  $F=-1+(b_2-b_1^2-b_1^3)^2+b_1^8+sb_1+s^{16}b_2^8$. Следствие SV с полем $(b_1,2b_2+b_1^3)$:
  $\xi\cdot\nabla Q=4t^2+8b_1^8\ge4Q$. Ни $\langle Cb,\nabla\rangle$ (при $t=b_1^3/4$: $\frac12b_1^6(32b_1^2-1)<0$), ни диагональные поля не
  годятся.
- **R** (кольцо минимумов): $U=(x^2+y^2-z^3)^2-z^8+xz^8$, $h=(|w|^2-z^3)^2$, $d_h=6<\beta=8$,
  $Z_h=\{|b|=1\}$. Следствие S: траектория у кольца $|w|\approx z^{3/2}$, без симметрии; второе доказательство —
  предложение S′ (плоскость $y=0$ инвариантна). [Доказано, довод R39] $0$ изолирована над $\mathbb R$:
  $\partial_yU=4y(x^2+y^2-z^3)$; при $y\ne0$ имеем $x^2+y^2=z^3$, и тогда $\partial_xU=z^8=0$, $z=0$, $x=y=0$ —
  противоречие; при $y=0$ из $\partial_zU=z^2\big(-6(x^2-z^3)-8z^5+8xz^5\big)=0$ либо $z=0$ (и $\partial_xU=4x^3=0$), либо
  $x^2-z^3=\frac43z^5(x-1)$, и подстановка в $\partial_xU=4x(x^2-z^3)+z^8=0$ даёт $3z^3=16x(1-x)$; при малых $x$ это
  $x=O(z^3)$, откуда $x^2-z^3=-z^3(1+O(z^3))$ против $\frac43z^5(x-1)=O(z^5)$ — при $z\ne0$ невозможно. [Доказано]
  Над $\mathbb C$ точка $0$ не изолирована: на прямых $\{z=0,\ x=\pm iy\}$ все три производные обращаются в нуль
  (каждое слагаемое содержит множитель $x^2+y^2-z^3$ или степень $z$) — пример к ловушке из CLAUDE.md; выводы
  от этого не зависят.
- **E** (два подоврага): $U=x^{12}+y^{12}+z^4(x^2-yz^2)^2(x^3-yz^4)^2-z^{24}+xz^{23}$, $c=(2,2)$, $N=1$:
  $F=-1+Q+sb_1$, $Q=(b_2-b_1^2)^2(b_2-b_1^3)^2+b_1^{12}+b_2^{12}$. Следствие E. Диагонального поля нет: на кривых
  $b_2=b_1^2+\tau b_1^4$ и $b_2=b_1^3+\tau b_1^4$ главные члены $\xi Q$ равны $2\tau(\lambda_2-2\lambda_1)b_1^{10}$ и
  $2\tau(\lambda_2-3\lambda_1)b_1^{11}$ при $Q\asymp b_1^{12}$, откуда $\lambda_2=2\lambda_1=3\lambda_1$, $\xi=0$.

### 5. Общий случай и что остаётся открытым

[Эскиз] *Схема.* Лемма B даёт дно и профиль $g$. В фиксированных осях «чистые» веса $c_i^{\rm p}$ — наклоны
многоугольников Ньютона ограничений $g(s,w_1,0)$, $g(s,0,w_2)$ на уровне $\beta$. Далее: (α) мономов с $\ell<\beta$
нет и $Q_{c^{\rm p}}$ имеет изолированный нуль — утверждение Q, следствия R, SV, E, диагональные поля; (β) мономов
с $\ell<\beta$ нет, но нуль $Q_{c^{\rm p}}$ не изолирован — сдвиг $L(x)$, поле, приспособленное к подоврагу, или трубка
вокруг листа (следствие S); (γ) есть мономы с $\ell<\beta$ — следствия X, S, SV с $e_j>0$, иначе сдвиг $L(x)$
(пример SH). Оси и сдвиги — ряды Пюизё, $L=I+O(x^{1/N})$.

**Пробелы.**

- **G1** [Эскиз]. Лист (кольцо, кривой подовраг), вдоль которого глубина меняется в порядке $x^\beta$. Нужна
  угловая стенка около минимума глубины на листе и поле, касательное к листу. При невырожденном листе
  и минимуме конечного порядка, вероятно, годится $\kappa\cdot$(одномерное поле Эйлера вдоль листа) с малым $\kappa$;
  не выписано. Что при $\xi=0$ следствие S здесь не работает, показал R36: у $U=(x^2+y^2-z^6)^2-z^{16}+xz^{13}$
  ($c=(3,3)$, $\beta=16$) $F=-1+s^{-4}(|b|^2-1)^2+b_1$, и (U2) или (U4) нарушено.
- **G2** [Гипотеза]. Анизотропия ($c_1<c_2$) с подоврагами, касающимися узкой оси ($Q_d(0,1)=0$): поля с
  (T) может не быть (предложение 6.2 [009]). Встречается ли такой профиль при правильно выбранных весах
  оврага, не известно.
- **G3** [Гипотеза]. Знакопеременные младшие уровни, которые не раскладываются в неотрицательные
  слагаемые с общим полем и не устраняются сдвигом $L(x)$.
- **G4** [Гипотеза]. Конечность процесса уточнения карты (аналог Ньютона–Пюизё с параметром).

**Гипотеза NP.** [Гипотеза] Пусть $n=3$, $U$ аналитична, выполнены (Z) и (H<0). Тогда найдутся $N$, ряд
Пюизё $\gamma$, матрица $L(x)=I+O(x^{1/N})$ из рядов Пюизё, веса $c\in(1,\infty)^2$ и поле $\xi(s,b)$ с (T), (Θ), для
которых выполнены (U1)–(U4) теоремы 2U. Из неё и теоремы 2U следовало бы: при $n=3$, $u_m\ge0$ и
конечном $\Sigma$ (любой вырожденности) задача (A) решена, и даже без предположения об изолированности
критической точки (п. 4 раздела выше). Задача (A) этим результатом **не решена**.

### 6. Эксперименты

Все — [Эксперимент], не доказательство; `experiments/prover/point-degenerate/`, запуск
`~/venv/bin/python <скрипт>`.

| Скрипт → вывод | Что проверяет | Результат |
|---|---|---|
| `check_2U_identities.py` | (I1)–(I4) для конкретных нелинейных $\gamma$, $L$, $\xi(s,b)$, $P$, $c=(\frac32,\frac73)$, $N=2$, 8 точек, 50 знаков | расхождение $\le6\cdot10^{-46}$ |
| `examples.py` | $F$ и тождества Эйлера для K1, P1, Λ, X, SV, SH (обе карты), R, E | точно |
| `exit_check.py` | (A5) прямым дифференцированием в $\mathbb R^3$: Λ ($Y=e_z$ и $Y=q/z$), X ($Y=e_z$) | Λ: $-2.27$, $-2.48$ и $3.54$, $3.69$; X: $9.80$, $9.97$ |
| `exit_check_ring.py` | (A5) для R с полем гомотетии | $\delta=0.05$: $1.41\to1.98$ при $\rho\to5\cdot10^{-4}$; при $\delta=0.01$, $\rho=10^{-2}$ отрицательно ($\sigma$ ещё велико) |
| `sv2_check.py`, `diag_field_E.py` | примеры SV2 и E | точно / численно согласуется с доказательством |
| `isolated_check.py` | нульмерность идеала $(\nabla U)$ | Λ, SV, SH, X — да; R — нет (над $\mathbb C$); E — не досчитался за 1500 с |

У R36 — независимая реализация (A5) (mpmath, 40 знаков), включая точки границы $P=\delta$, где минимум
стремится к $\mu$ теории: Λ — к $4$, X — к $10$, R — к $2$, SV2 — к $4$.

## Отличия от записки

Записка — `notes/prover/2026-10-21-point-degenerate.md` (вторая редакция, её §11). Математика §1–§5
записки перенесена без изменений, кроме перечисленного.

**Правки по R34** (внесены и в записку).

1. Лемма B: ссылка (SA2) заменена на теорему 0.2 BM88 с выводом леммы о выборе кривой; (SA1) —
   определение 3.1 и теорема 3.10 BM88; $\nabla_wg(s,0)=0$ при $s\le0$ — по аналитичности.
2. Предложение N, п. 3: формулировка через вершины локально выпуклой ломаной; довод упрощён, случай
   $v_1v_2>0$ разобран.
3. Замечание о двух уровнях сужено до $Q\ge0$ на $\mathbb R^2$, приведён контрпример (здесь — замечание 3).
4. P1: $U(x,y,-z)\equiv U(x,y,z)$.
5. Теорема 2U: $\eta\ge0$; «(T) необходимо» — только для данного способа оценки $\theta_3$; при
   масштабировании поля $\alpha\le1$.

**Правки по R36** (внесены и в записку).

6. Теорема E принята ([009]); оговорка «при условии теоремы E» снята.
7. Теорема C′: явное уменьшение $s_0$ в (U3); требования на $R_j$ и $\chi$ — только на $\overline{B_{r_1}}$.
8. Следствие R: $\chi\to0$ (здесь $\chi=O(s)$, так как $Nc_i\in\mathbb N$ входит в условие). Пример Λ — теорема C′ с полем
   следствия R.
9. Следствие X: формула для $\mu$ с $\lambda\cdot\alpha_j$ и $\wedge\beta$; следствие SV: $\mu\le\beta$, неотрицательность на $B_{r_0}$.
10. Следствие S: условия на $r$ на $\{|x^{-c}y|\le r_1\}$ с $\max_ix^{c_i}|\partial_{y_i}r|$; радиусы согласованы через п. 7.
11. Пример E: отсутствие диагональных полей доказано (довод R36).
12. Теорема 2D: замена $N$ кратным, $n=2$ в утверждении Q; K0: «на уровне $\le\beta$»; квазиоднородный $U$ —
    прямой довод про инвариантный луч.
13. Добавлен пример SV2 (R36); согласованы формулировки о касании луча.

**Уточнения при оформлении** (рецензенты не читали).

14. Обозначения изменены, чтобы уменьшить конфликты с [007] (оставшиеся устранены по R39, п. 19): глубина дна $\underline U(x)$, $\underline u(s)$ (в записке $m(x)$,
    $\tilde m(s)$ — конфликт со степенью $m$); уровень $\ell_c$ (в записке $L_c$ — конфликт с $L(x)$ и $L_1,L_2$); матрицы
    $\mathcal A,\mathcal M$ (в записке $A$, $M$ — конфликт с $A(r)$ теоремы A и $M_0,M_1,M_2$); кривая $\mathcal T$ (в записке
    $T$ — конфликт с условием (T)); $\hat U$ (в записке $G$ — конфликт с множеством $G$ теоремы A); оператор
    $\mathcal E_\xi$; срезка $\vartheta_\epsilon$ (в записке $\chi_\epsilon$ — конфликт с $\chi(s)$); поправка теоремы E — $\kappa_E$; константа
    примера Λ — $k_0$; порядок теоремы E в следствии E — $m_E$; направление звена в предложении N — $v$; показатель
    в следствии SV — $\nu_B$; степень в следствии S — $d_h$.
15. В теорему 2U явно внесено утверждение $q(t)/|q(t)|\to e_x$ с доказательством (в записке — §9, п. 5).
16. В формулировки следствий R, X явно внесено $Nc_i\in\mathbb N$ (в записке — замечание 5.1 о рациональности весов).
17. Константа в $\zeta(\sigma)$: множитель $2$ при $\|L'\|$ убран (по R34 — лишний).
18. В «Утверждение» включены примеры K1, P1, Λ, SH; X, SV2, R, E — в замечании 4 (доказаны в записке,
    проверены R36).

**Правки по R39** (`notes/reviewer/2026-10-21-result012.md`; новых утверждений нет).

19. Замечание 1 (обозначения): константа леммы B — $C_U$ (было $C$, совпадало с $C=\operatorname{diag}(c_i)$); константа
    следствия SV — $C_\psi$; в (SA2) множество — $\mathcal Z$, отображения — $\Psi_i$, компакты — $\mathcal K_i$ (были $A$,
    $\varphi_i$, $L_i$); в лемме B множества $\mathcal B$, $\mathcal Z$ (были $B$, $A$); предположение — (Z) (было (P), совпадало
    с $P=F+a_0$), нулевое множество в следствии S — $Z_h$; многочлен в предложении N, п. 3 — $f_0$, многочлен в
    лемме 3 — $\varpi$, радиус полидиска — $\varrho$ (было $\rho$); функции следствия SV — $\mathfrak a(b)$, $\mathfrak b(b_1)$, подовраг —
    $\psi(b_1)$ (были $A$, $B$, $\phi$); переменные примера P1 — $X_1,X_2$, функции — $f_1,f_2$ (были $\xi,\eta$, $a,b$);
    погрешность в следствии E — $\mathrm{err}(\epsilon)$ (было $e(\epsilon)$); в (D1) теоремы 2U — $\epsilon'$ вместо $s$.
20. Замечание 2: в следствие S явно внесены $U\in C^2$, $U(0)=0$, $\nabla U(0)=0$, $a_0>0$, $\beta>0$, $r\in C^1$ при $x>0$.
21. Замечание 3: в следствии E — перенумерация осей ($c_1\le c_2$); в «Зависит от» добавлено следствие 6.1(a) [009].
22. Замечание 4: невырожденный случай сформулирован при $n=3$, (Z), (H<0) (вместо «в условиях следствия R»);
    у K1 «то же решение» заменено на «тоже асимптотическая траектория».
23. Замечание 5: в лемме 3 уменьшать $s_1$ для производных по $b$ не нужно (множитель $1/r$).
24. Замечание 6: метки в пп. 1, 2, 3, 5 раздела «Где работают аналитичность и изолированность».
25. Замечание 7: в замечании 4 изолированность $0$ для X и R — с доказательствами (для R — довод R39), метка
    [Доказано]; неизолированность над $\mathbb C$ для R — тоже с доводом.
26. Замечание 8: в замечании 1 вывод из примера Λ ограничен данной прямой картой.
