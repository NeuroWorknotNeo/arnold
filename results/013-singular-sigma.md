# 013. Особая точка $\Sigma$ при $n=3$: овраг у пересечения ветвей нулевого множества ведущей формы

- **Статус:** [Проверено: reviewer R37, R38 (агенты), 21.10.2026 — доказательства в записке
  [`notes/prover/2026-10-21-singular-sigma.md`](../notes/prover/2026-10-21-singular-sigma.md); reviewer R42 (агент),
  21.10.2026 — текст этого результата целиком: ошибок в доказательствах нет]; ждёт проверки человеком.
  - R42 ([`notes/reviewer/2026-10-21-result013.md`](../notes/reviewer/2026-10-21-result013.md)): все шаги, в том числе
    места второй редакции (предложение 3.3 с возмущением $O(|q|^7)$, ручной вывод (8.1)–(8.2), изолированность каспа
    и касания тождествами, доводы о неприменимости других методов, S1 — интервально, независимо). Замечания З1–З10
    учтены («Отличия от записки», «Правки по R42»). Довод замечания 3 для прямых карт весов $(\frac32,\frac32)$ при
    любом центре дописан после R42; главный агент его прочитал и проверил (случаи $\beta<6$, $\beta>6$, $\beta=6$).
  - R37 (reviewer, агент, 21.10.2026,
    [`notes/reviewer/2026-10-21-singular-sigma-A.md`](../notes/reviewer/2026-10-21-singular-sigma-A.md)): §1–§4
    записки — теорема S, предложения 3.1, 3.3, теорема 3.2, следствия X, X′, примеры (принадлежность,
    изолированность), метки §7. Ошибок нет. Замечания 1–11 (уточнения формулировок, ручное доказательство
    изолированности каспа и касания) учтены.
  - R38 ([`...-B.md`](../notes/reviewer/2026-10-21-singular-sigma-B.md)): §5.1–§5.3 записки — пример $U_{\rm II}$,
    предложение 5.1, теорема II, «что даёт пример». Ошибок в доказательствах нет. Исправлена неверная формула
    профиля $F_0$ в комментарии (З4); утверждения о неприменимости других методов снабжены доказательствами
    или метками (З5). Остальные замечания З1–З8 учтены.
  - Все правки внесены во вторую редакцию записки (её §11) и перечислены здесь («Отличия от записки»).
    Места, добавленные во второй редакции и при оформлении, рецензенты не читали. Это доказательство
    предложения 3.3 с возмущением, ручной вывод тождеств (8.1), (8.2) и доводы о неприменимости в
    замечании 3. Тождества изолированности каспа и касания и доводы о неприменимости теоремы S и поля
    $e_z$ взяты из отзывов R37 и R38.
  - Метки: всё в разделе «Утверждение» — [Доказано]. Замечания помечены каждое отдельно.
- **Автор:** prover (агент), записка `notes/prover/2026-10-21-singular-sigma.md` (21.10.2026, вторая редакция), по
  заданию главного агента: асимптотическая траектория при $n=3$, когда дно оврага сходится к особой точке
  $\Sigma$ (пересечению ветвей). Оформление — prover (агент), 21.10.2026.
- **Зависит от:**
  - [007] = [`results/007-gt3.md`](007-gt3.md): теорема A, лемма 1 (формулы (0.1), (1.1), (1.3)), лемма 2
    (условия (L0)–(L3), формула (3.1));
  - [010] = [`results/010-morse-bott.md`](010-morse-bott.md): лемма M (условия (L2), (L3M), константа $\Gamma$,
    оценка (0.3), двусторонняя оценка $\dot\rho$ в п. 1);
  - [008] = [`results/008-class-K.md`](008-class-K.md): только в предложении 3.1(e) (формула $g_{m+2}$, §3.3, и
    условия теоремы K1) и в замечаниях.
  - Литература не используется.
- **Проверочные скрипты** [Эксперимент]:
  - [`experiments/prover/singular-sigma/`](../experiments/prover/singular-sigma/) — автор (`model_checks.py`,
    `geom_checks.py`, `exit_model.py`, `exit_cor.py`, `u2_checks.py`, `exit_u2.py`, `bottom.py`, `iso_identities.py`,
    `cusp_check.py`, `tangency_check.py`, `s1_check.py`, `s1_interval.py`);
  - `experiments/reviewer/singular-sigma-R37/`, `experiments/reviewer/singular-sigma-R38/` — рецензенты
    (независимые реализации, Singular: числа Милнора).

## Утверждение

### Обозначения

$\mathbb R^n$ с евклидовыми $\langle\cdot,\cdot\rangle$, $\lvert\cdot\rvert$, $B_r=\{\lvert q\rvert<r\}$, $\lVert\cdot\rVert$ — операторная норма. Система
$\ddot q=-\nabla U(q)$. **Асимптотическая траектория** — решение $q(t)\ne0$, $t\ge0$, с $q(t)\to0$, $\dot q(t)\to0$ при
$t\to+\infty$; из неё следует неустойчивость по Ляпунову ([007], теорема A, шаг 6). Обозначения
$p,h,v_\perp,K_\perp,W,V,\lambda,\Xi$, условия (D1)–(D4), (A4), (A5), (L0)–(L3) — как в [007]; (L2), (L3M), $\Gamma$,
$b'$, (0.3) — как в лемме M [010]. $U=\sum_{k\ge m}u_k$ — разложение на однородные формы, $u_m\ge0$,
$\Sigma=\{u_m=0\}\cap S^2$.

**Гномоническая карта** около $e_z$:
$$\omega(\theta)=c\,(\theta_1,\theta_2,1),\qquad c=c(\theta):=(1+\lvert\theta\rvert^2)^{-1/2};\qquad q=r\omega(\theta)\iff\theta=(x/z,\,y/z),\ r=\lvert q\rvert\quad(z>0).$$
В ней большие круги через $e_z$ — прямые через $0$.

### Теорема S (полярный $\kappa$-приём со свободным угловым полем)

**Теорема S.** Пусть $n\ge2$, $U\in C^2(B_{r_*})$, $U(0)=0$, $\nabla U(0)=0$. Пусть
$\omega:\overline{B_{\theta_0}}\to S^{n-1}$ ($\overline{B_{\theta_0}}\subset\mathbb R^{n-1}$) — инъективное погружение класса $C^3$ в
окрестности замкнутого шара, $\omega(0)=\omega_0$, $\Pi(r,\theta):=r\,\omega(\theta)$. Пусть $\xi\in C^1(\overline{B_{\theta_0}};\mathbb R^{n-1})$,
$\lvert\xi(\theta)\rvert\le K\lvert\theta\rvert$, $\lVert D\xi(\theta)\rVert\le K$. Пусть $\beta>0$, $a_0>0$, $r_0\in(0,r_*]$, и
$$\mathcal W(r,\theta):=r^{-\beta}U\big(r\omega(\theta)\big)+a_0,\qquad0<r<r_0,\ \lvert\theta\rvert<\theta_0 .$$
Предположим, что есть $p>0$, $\lambda_0>0$, $\mu_0\in(0,1]$, $\kappa_0\in(0,\frac12]$ и функция $\chi:(0,r_0)\to[0,\infty)$,
$\chi(r)\to0$ при $r\to0$, такие, что при всех $0<r<r_0$, $\lvert\theta\rvert<\theta_0$, $\kappa\in(0,\kappa_0]$:

- **(S1)** $\mathcal W(r,\theta)\ge\lambda_0\lvert\theta\rvert^{2p}-\chi(r)$;
- **(S2)** $-r\,\partial_r\mathcal W+\kappa\,\xi(\theta)\cdot\nabla_\theta\mathcal W\ge\kappa\mu_0\,\mathcal W-\chi(r)$;
- **(S3)** $\mathcal W(r,0)\le\chi(r)$.

Тогда $\beta\ge2$, и найдётся $\delta_*>0$ такое, что при каждом $\delta\in(0,\delta_*]$ есть асимптотическая
траектория $q(t)=r(t)\,\omega(\theta(t))$, $t\ge0$. Для неё $r(t)$ строго убывает к $0$,
$-k_2r^{\beta/2}\le\dot r\le-k_1r^{\beta/2}$ с постоянными $0<k_1\le k_2$, и $\lvert\theta(t)\rvert\le R_\theta(\delta):=(2\delta/\lambda_0)^{1/(2p)}$
при всех $t\ge0$. Равновесие неустойчиво по Ляпунову.

(S2) аффинно по $\kappa$, поэтому его достаточно проверить при $\kappa\to0^+$ и при $\kappa=\kappa_0$. Члены $r^{d-\beta}P(\theta)$
порядка $d<\beta$ с $P\ge0$ условие (F) [007] нарушают, но разрешены: их вклад в разность частей (S2) равен
$r^{d-\beta}\big[(\beta-d-\kappa\mu_0)P+\kappa\,\xi\cdot\nabla P\big]$, и он неотрицателен, если $\xi\cdot\nabla P\ge0$ и $\beta-d\ge\kappa_0\mu_0$.

### Модель

$$U_\varepsilon=x^2y^2+\varepsilon z^2(x^4+y^4)-z^6+x^6+y^6,\qquad\varepsilon\in\mathbb R .$$
Здесь $u_4=x^2y^2$, $\Sigma=\{x=0\}\cup\{y=0\}$ — два больших круга, пересекающиеся в $\pm e_z$; $u_5=0$.

**Предложение 3.1.**

- **(a)** Если $\nabla U_\varepsilon(q)=0$ и $1+2\varepsilon z^2>0$, то $q=0$. В частности, $0$ — изолированная критическая точка при
  любом $\varepsilon$ (при $\varepsilon\ge0$ — единственная в $\mathbb R^3$).
- **(b)** $0$ — не минимум: $U_\varepsilon(0,0,z)=-z^6$.
- **(c)** При $\varepsilon\ge-1$: $U_\varepsilon(q)+\lvert q\rvert^6\ge x^2y^2+\lvert q\rvert^4(x^2+y^2)$. Поэтому минимум $U_\varepsilon$ на сфере $\lvert q\rvert=r$
  равен $-r^6$ и достигается только в точках $(0,0,\pm r)$: дно оврага — ось $z$.
- **(d)** В гномонической карте
  $$U_\varepsilon(r\omega(\theta))=r^4c^4\theta_1^2\theta_2^2+r^6c^6\big(-1+E(\theta)\big),\qquad E:=\varepsilon(\theta_1^4+\theta_2^4)+\theta_1^6+\theta_2^6, \tag{1}$$
  $$\mathcal W:=r^{-6}U_\varepsilon+1=r^{-2}c^4\theta_1^2\theta_2^2+\Lambda(\theta),\qquad\Lambda:=1-c^6+c^6E=3\lvert\theta\rvert^2+O(\lvert\theta\rvert^4). \tag{2}$$
  $\delta$-глубокая область: $\{\mathcal W<\delta\}=\{\Lambda<\delta,\ \lvert\theta_1\theta_2\rvert<r\sqrt{\delta-\Lambda}/c^2\}$. (Пояснение, не
  утверждение: это крест, рукава которого идут вдоль ветвей на угловую длину порядка $\sqrt{\delta/3}$ — конический
  масштаб, — а поперёк ветви рукав гиперболически узок.)
- **(e)** На ветви $\{y=0\}$ ($\omega=(\sin\varphi,0,\cos\varphi)$) в точках $\varphi\ne0$ (вне полюса) $j=6$ и
  $G=u_6\vert_\Sigma=\sin^6\varphi-\cos^6\varphi+\varepsilon\cos^2\varphi\sin^4\varphi$. Значения в полюсе — значения аналитического
  продолжения этой функции: $G(0)=-1$, $G''(0)=6$, $G''(0)+jG(0)=0$. В картезианских срезах $z=\mathrm{const}$ профиль вдоль ветви равен
  $-1+\varepsilon b^4+b^6$ ($b=x/z$). Теорема K1 [008] в точке $e_z$ неприменима: нарушены условие $G''+jG>0$ и данные
  (S) (нормальный гессиан $\partial_y^2u_4=2x^2$ обращается в нуль в полюсе).

**Теорема 3.2.** Для каждого $\varepsilon\in\mathbb R$ функция $U_\varepsilon$ удовлетворяет условиям теоремы S в $\omega_0=\pm e_z$ с
гномонической картой (для $-e_z$ — $c(\theta_1,\theta_2,-1)$), $\xi=\theta$, $K=1$, $\beta=6$, $a_0=1$, $p=1$, $\lambda_0=2$, $\mu_0=1$,
$\kappa_0=\frac12$, $\chi\equiv0$, $\theta_0=(9+\lvert\varepsilon\rvert)^{-1/2}$. Следовательно, при каждом малом $\delta>0$ есть
асимптотическая траектория в конусе $\lvert\theta\rvert\le\sqrt\delta$ вокруг луча $\mathbb R_+e_z$. То же верно для $U_\varepsilon+V$, где $V\in C^2$
около $0$, $\lvert V(q)\rvert\le C_V\lvert q\rvert^7$, $\lvert\nabla V(q)\rvert\le C_V\lvert q\rvert^6$ (тогда $\chi(r)=C'r$).

**Предложение 3.3** (картезианские срезы, $\varepsilon\ge0$). Пусть $\varepsilon\ge0$, $0<\delta<\frac18$, $0<\sigma<1$, и
$\mathcal G=\{0<z<1,\ x^2+y^2<z^2\}$, $\rho=z$, $Y=e_z$, $A(z)=z^6$, $W=U_\varepsilon+z^6$, $D=\{q\in\mathcal G:\ z<\sigma,\ W<\delta z^6\}$.
Тогда выполнены условия леммы 2 [007] с $\mu=4$, $\varepsilon_1=0$, $\theta_1=\theta_2=\theta_3=0$, и теорема A [007] даёт
асимптотическую траекторию в конусе $x^2+y^2\le(4\delta)^{1/3}z^2$. Для $U_\varepsilon+V$ с $V$ как в теореме 3.2 (пусть
$U_\varepsilon+V\in C^2(B_{2r_1})$) то же построение с $\mathcal G_1:=\{0<z<r_1,\ x^2+y^2<z^2\}$ вместо $\mathcal G$ и малым $\sigma<r_1$
(тогда $\varepsilon_1=O(\sigma)/\delta$) даёт асимптотическую траекторию в конусе $x^2+y^2\le(8\delta)^{1/3}z^2$.

### Следствие X (нормальное пересечение кратностей $2a,2b$, полюсное доминирование)

**Данные.** $n=3$, $U\in C^{j+1}$ около $0$, $U=\sum_{k=m}^ju_k+O(\lvert q\rvert^{j+1})$, $u_m\ge0$, $\omega_0\in\Sigma$,
$\omega:\overline{B_{\theta_0}}\to S^2$ — аналитическая карта (инъективное погружение около замкнутого круга), $\omega(0)=\omega_0$,
$p_k:=u_k\circ\omega$. Целые $a,b\ge1$, $P(\theta):=\theta_1^a\theta_2^b$.

- **(X0)** $p_m=P^2e$, $e\in C^1(\overline{B_{\theta_0}})$, $e\ge e_0>0$.
- **(X1)** При $m<k<j$: $p_k=q_k+P\,n_k$, где $q_k,n_k\in C^1(\overline{B_{\theta_0}})$, $q_k\ge0$, $q_k(0)=0$, $\theta\cdot\nabla q_k\ge-C_qq_k$, и
  $n_k\equiv0$ при $2k\le m+j$.
- **(X2)** $p_j=-a_0+\Lambda_1(\theta_1)+\Lambda_2(\theta_2)+P\,n_j$, где $a_0>0$, $n_j\in C^1$, $\Lambda_i\in C^1$ и при $\lvert t\rvert<\theta_0$
  $\Lambda_i(t)\ge\alpha_i\lvert t\rvert^{2p_i}$ ($\alpha_i,p_i>0$), $t\Lambda_i'(t)\ge\Lambda_i(t)$.

**Следствие X.** При (X0)–(X2) (после уменьшения $\theta_0$) выполнены условия теоремы S с $\beta=j$, $\xi=\theta$,
$p=\max(p_1,p_2)$, $\mu_0=1$, $\chi(r)=C(r+r^\nu)$, где $\nu:=\min\{2k-m-j:\ m<k\le j,\ n_k\not\equiv0\}>0$ ($\chi=Cr$, если
таких $k$ нет). Следовательно, есть асимптотическая траектория в конусе раствора $O(\delta^{1/(2p)})$ вокруг луча
$\omega_0$.

Условие (X0) означает, что около $\omega_0$ множество $\Sigma$ — две гладкие трансверсальные ветви, вдоль которых
$u_m$ обращается в нуль ровно в порядках $2a$ и $2b$, включая сам $\omega_0$. Условие (X2) означает, что
$u_j(\omega_0)<0$ и что сужения $u_j$ на ветви имеют строгий минимум в точке пересечения (их связь с эффективным
потенциалом [008] — замечание 5, [Эскиз]). Для
аналитических $\Lambda_i$ строгий локальный минимум в $0$ влечёт обе оценки (X2) при малом $\theta_0$. При $a=b=1$
разложение (X2) существует всегда.

### Следствие X′ (произвольная особенность, без перекрёстных членов)

**Следствие X′.** Пусть $n\ge2$, $U\in C^{j+1}$, $\omega$, $p_k$ — как выше, $\xi\in C^1$, $\xi(0)=0$, $\lVert D\xi\rVert\le K$. Пусть

- **(X′0)** $p_m\ge0$, $\xi\cdot\nabla p_m\ge-Cp_m$;
- **(X′1)** при $m<k<j$: $p_k\ge0$, $p_k(0)=0$, $\xi\cdot\nabla p_k\ge-Cp_k$;
- **(X′2)** $p_j(0)=-a_0<0$, $\Lambda:=p_j+a_0\ge\lambda_0\lvert\theta\rvert^{2p}$, $\xi\cdot\nabla\Lambda\ge\mu_0\Lambda$ ($\mu_0>0$).

Тогда выполнены условия теоремы S с этим $\xi$, $\beta=j$, $\chi=Cr$ и $\min(\mu_0,1)$ вместо $\mu_0$; асимптотическая
траектория есть.

(X′0) выполнено, если $p_m=e\prod_iF_i^{2a_i}$, $e(0)>0$, и $\xi_w\cdot\nabla F_i=d_iF_i$ для квазиоднородного поля
$\xi_w=(w_1\theta_1,\dots,w_{n-1}\theta_{n-1})$, $w_i>0$. Сюда входят пучок прямых, касп $\theta_2^2=\theta_1^3$ ($w=(2,3)$) и касание
$\{\theta_2=0\}\cup\{\theta_2=\theta_1^2\}$ ($w=(1,2)$).

### Примеры

Карта гномоническая. Во всех примерах $0$ — изолированная критическая точка и не минимум
($U(0,0,z)<0$ при $z>0$).

| Пример | $U$ | $m,j$ | Применимо |
|---|---|---|---|
| X1 | $x^2y^2+z(x^4+y^4)-z^6+x^6+y^6$ | $4,6$ | следствие X, $a=b=1$, $q_5=c^5(\theta_1^4+\theta_2^4)$ |
| X2 | $x^2y^2+xyz^4-z^7+x^8+y^8$ | $4,7$ | следствие X, $a=b=1$, перекрёстный член $n_6=c^6$, $\nu=1$ |
| Касп | $(y^2z-x^3)^2-z^8+x^8+y^8$ | $6,8$ | следствие X′, $\xi_w=(2\theta_1,3\theta_2)$ |
| Касание | $y^2(yz-x^2)^2-z^8+x^8+y^8$ | $6,8$ | следствие X′, $\xi_w=(\theta_1,2\theta_2)$ |

В каспе $\Sigma$ около $e_z$ — каспидальная кривая $\theta_2^2=\theta_1^3$, в касании — две ветви $\theta_2=0$ и
$\theta_2=\theta_1^2$, касающиеся в $e_z$. Модель удовлетворяет и следствию X ($a=b=1$). Во всех этих примерах ось $z$
инвариантна, так что сами по себе они тривиальны; ценность следствий — в устойчивости к возмущениям
$O(\lvert q\rvert^{j+1})$ (замечание 1).

### Пример $U_{\rm II}$: гиперболическое разрешение креста

$$U_{\rm II}=x^2y^2+2xyz^3+\eta z^6+x^6+y^6=H^2-(1-\eta)z^6+x^6+y^6,\qquad H:=xy+z^3,\qquad0<\eta<1 .$$
Здесь $u_4=x^2y^2$ (то же пересечение ветвей в $e_z$), $u_5=2xyz^3$ — перекрёстный член с $2k=10=m+j$, то есть
следствие X не применимо, а $u_6(e_z)=\eta>0$: полюс в овраг не входит.

**Предложение 5.1.** $0$ — изолированная критическая точка $U_{\rm II}$ в шаре $\lvert q\rvert<\big(\frac{1-\eta}{3\eta^2}\big)^{1/3}$ и не
минимум.

**Теорема II.** Пусть $0<\eta<1$, $V\in C^2$ около $0$, $\lvert V(q)\rvert\le C_V\lvert q\rvert^7$, $\lvert\nabla V(q)\rvert\le C_V\lvert q\rvert^6$, $U:=U_{\rm II}+V$.
Тогда при каждом достаточно малом $\delta>0$ есть асимптотическая траектория $q(t)=(x,y,z)(t)$ в квадранте
$\{x>0,y<0\}$ с $z(t)\downarrow0$, $-k_2z^3\le\dot z\le-k_1z^3$ и $(xy+z^3)^2+x^6+y^6\le2\delta z^6$ при всех $t$. Такая же
траектория есть в квадранте $\{x<0,y>0\}$. Равновесие неустойчиво по Ляпунову.

Доказательство использует свободное поле
$$Y=(\xi_1,\xi_2,1),\qquad z\xi=(3-e)\,g\,(1,-1)-ez^3\frac{(y,x)}{x^2+y^2},\qquad g:=\frac{x\lvert y\rvert}{x+\lvert y\rvert},\quad e\in(0,\tfrac12], \tag{3}$$
которое сохраняет гиперболу $\{H=0\}$ (точнее, семейство $\{H=cz^{3-e}\}$) с запасом $2e$.

## Доказательство

### 1. Теорема S

1. **Константы.** $M_1:=\max\lVert D\omega\rVert$, $M_2:=\max\lVert D^2\omega\rVert$, $M_3:=\max\lVert D\omega(\theta)^{-1}\rVert$ — по
   $\overline{B_{\theta_0}}$; $D\omega(\theta):\mathbb R^{n-1}\to T_{\omega(\theta)}S^{n-1}$ — изоморфизм. Положим $a_1=a_3:=a_0$, $a_2:=\beta a_0$, $h_0:=1$,
   $h_1:=\frac32$, $C_\Gamma:=\sqrt2\big[\frac32\beta\sqrt{\frac32}M_1K+\sqrt2K\big(M_1+K(M_1+M_2)\big)\big]$.
2. **$\beta\ge2$.** По (S3) $U(r\omega_0)=r^\beta(\mathcal W(r,0)-a_0)\le-\frac{a_0}2r^\beta$ при малых $r$, а $\lvert U(q)\rvert\le M\lvert q\rvert^2$
   ($U\in C^2$, $U(0)=0$, $\nabla U(0)=0$). Значит, $r^{\beta-2}\le2M/a_0$ при малых $r$, и $\beta\ge2$.
3. **Выбор констант.** $\theta_1:=\theta_0/2$,
   $\delta_*:=\min\{\frac{a_0}2,\frac{\lambda_0\theta_1^{2p}}4,\frac{\lambda_0}2,\frac{a_0}{6M_1^2K^2}\}$. Для $\delta\in(0,\delta_*]$ имеем
   $R_\theta:=(2\delta/\lambda_0)^{1/(2p)}\le1$ и $R_\theta\le2^{-1/(2p)}\theta_1<\theta_1$. Положим
   $$\kappa:=\min\Big\{\kappa_0,\ \frac1{2M_1KM_3},\ \frac1{\sqrt2M_1K},\ \frac\beta{8M_2KM_3},\ \frac{\beta\mu_0\delta}{2C_\Gamma^2a_0R_\theta^2}\Big\}$$
   (дроби с нулевым знаменателем — $+\infty$) и выберем $\sigma\in(0,r_0)$ с
   $\chi_\sigma:=\sup_{0<r<\sigma}\chi(r)\le\min(\frac\delta2,\frac{\kappa\mu_0\delta}8)$. Порядок: $\delta\to\kappa\to\sigma$.
4. **Данные теоремы A.** $\Pi$ — $C^3$-диффеоморфизм $(0,r_0)\times B_{\theta_0}$ на открытое $\mathcal G\subset B_{r_0}\setminus0$, так как
   $\omega$ — инъективный локальный диффеоморфизм на открытое подмножество $S^{n-1}$ и
   $\Pi^{-1}(q)=(\lvert q\rvert,\omega^{-1}(q/\lvert q\rvert))$. Положим $\rho:=\lvert q\rvert$, $A(r):=a_0r^\beta$, $\sigma_0:=r_0$, а $Y$ — образ координатного
   поля $\partial_r-\frac\kappa r\xi\cdot\partial_\theta$:
   $$Y\big(\Pi(r,\theta)\big)=\omega(\theta)-\kappa D\omega(\theta)\xi(\theta)=:y(\theta). \tag{1.1}$$
   $Y\in C^1(\mathcal G)$, $Y\rho=\partial_r(r)=1$, $W\circ\Pi=r^\beta\mathcal W$.
5. **(D1)–(D3).** $\mathcal D:=\{(r,\theta):\ 0<r<\sigma,\ \lvert\theta\rvert<\theta_1,\ \mathcal W<\delta\}$, $D:=\Pi(\mathcal D)$ — открыто, $D\subset\mathcal G$.
   - (D1): $\rho<\sigma$ на $D$. Если $q=\lim\Pi(r_k,\theta_k)$, $(r_k,\theta_k)\in\mathcal D$, то по подпоследовательности
     $r_k\to\bar r\in[0,\sigma]$, $\theta_k\to\bar\theta$, $\lvert\bar\theta\rvert\le\theta_1$. При $\bar r=0$ имеем $q=0$, иначе $q=\Pi(\bar r,\bar\theta)\in\mathcal G$. Далее
     $\sup\{\lvert q\rvert:\ q\in D,\ \rho<s\}\le s$, $\rho=\lvert q\rvert$.
   - (D2): пусть $q\in\partial D\setminus0$, $\rho(q)<\sigma$. Тогда $q=\Pi(\bar r,\bar\theta)$, $\bar r<\sigma$, $\lvert\bar\theta\rvert\le\theta_1$,
     $\mathcal W(\bar r,\bar\theta)\le\delta$. При $\lvert\bar\theta\rvert=\theta_1$ по (S1) $\mathcal W\ge4\delta-\frac\delta2>\delta$ — противоречие. Значит,
     $\lvert\bar\theta\rvert<\theta_1$, а $q\notin D$ ($D$ открыто), так что $\mathcal W=\delta$, то есть $W(q)=\delta\rho^\beta$.
   - (D3): $\mathcal W(r,0)\le\chi_\sigma<\delta$ по (S3).
6. **Угол на $D_\sigma$.** В $D_\sigma$ имеем $\mathcal W\le\delta$, и по (S1) $\lambda_0\lvert\theta\rvert^{2p}\le\delta+\chi_\sigma\le2\delta$, то есть $\lvert\theta\rvert\le R_\theta$.
7. **(L0), (L1).** $\lvert A'\rvert=\beta a_0r^{\beta-1}$, $\delta\le a_0/2$. Так как $\lvert\omega\rvert\equiv1$, $\langle\omega,D\omega\,v\rangle=0$, и
   $h=1+\kappa^2\lvert D\omega\,\xi\rvert^2\in[1,1+\kappa^2M_1^2K^2R_\theta^2]\subset[1,\frac32]$.
8. **(L2).** $W\ge-\chi_\sigma r^\beta\ge-\delta\rho^\beta$. В координатах
   $\rho\,YW=r^\beta(\beta\mathcal W+r\partial_r\mathcal W-\kappa\xi\cdot\nabla_\theta\mathcal W)$, поэтому по (S2)
   $\beta W-\rho\,YW=r^\beta(-r\partial_r\mathcal W+\kappa\xi\cdot\nabla_\theta\mathcal W)\ge\mu W-\varepsilon_1\delta\rho^\beta$ с $\mu:=\kappa\mu_0\in(0,\beta)$ и
   $\varepsilon_1:=\chi_\sigma/\delta\le\kappa\mu_0/8$.
9. **(L3M).** Пусть $q=\Pi(r,\theta)\in D_\sigma$. Каждый $w\in\mathbb R^n$ однозначно записывается как
   $w=a\omega+\tau=D\Pi(a,\alpha)$, где $\tau=D\omega(\theta)(r\alpha)\perp\omega$; при этом $\lvert\tau\rvert\le\lvert w\rvert$, $\lvert r\alpha\rvert\le M_3\lvert\tau\rvert$. Поле $Y\circ\Pi=y(\theta)$
   от $r$ не зависит, поток $Y$ в координатах — $\dot r=1$, $\dot\theta=-\kappa\xi/r$, а
   $Dy(\theta)v=D\omega\,v-\kappa[D^2\omega(\xi,v)+D\omega(D\xi\,v)]$. Отсюда $D_YY=-\frac\kappa rDy\,\xi$, $D_wY=Dy\,\alpha$ и
   $$rD_YY=-\kappa\big[D\omega\,\xi-\kappa D^2\omega(\xi,\xi)-\kappa D\omega(D\xi\,\xi)\big],\qquad
   r\langle w,D_wY\rangle=\lvert\tau\rvert^2-\kappa\langle w,D^2\omega(\xi,r\alpha)\rangle-\kappa\langle\tau,D\omega(D\xi\,r\alpha)\rangle \tag{1.2}$$
   (использовано $\langle w,D\omega\,v\rangle=\langle\tau,D\omega\,v\rangle$). Пусть $w\perp Y$.
   - $\nabla\rho=\omega$, поэтому $\langle\nabla\rho-Y/h,w\rangle=\langle\omega-y,w\rangle=\kappa\langle D\omega\,\xi,w\rangle$: $\vartheta_1=0$,
     $\gamma_1=\kappa M_1KR_\theta$.
   - По (1.2) и $\kappa\le1$, $R_\theta\le1$: $\vartheta_2=0$, $\gamma_2=\kappa R_\theta\big(M_1K+K^2(M_1+M_2)\big)$.
   - По (1.2) и $\kappa M_1KM_3\le\frac12$:
     $r\langle w,D_wY\rangle\ge(1-\kappa M_1KM_3)\lvert\tau\rvert^2-\kappa M_2KR_\theta M_3\lvert\tau\rvert\lvert w\rvert\ge-\kappa M_2KM_3R_\theta\lvert w\rvert^2$:
     $\vartheta_3:=\kappa M_2KM_3R_\theta\le\beta/8$.
10. **Лемма M [010].** $b'=\beta-\kappa\mu_0-2\vartheta_3\ge\beta-\frac12-\frac\beta4\ge\frac\beta2$ (так как $\beta\ge2$). Так как $a_2+\beta\delta\le\frac32\beta a_0$,
    имеем $\Gamma\le C_\Gamma\sqrt{a_0}\,\kappa R_\theta$ и
    $\frac{\Gamma^2}{4b'\delta}\le\frac{C_\Gamma^2a_0\kappa^2R_\theta^2}{2\beta\delta}\le\frac{\kappa\mu_0}4$. Скобка в (0.3) [010] не меньше
    $\kappa\mu_0(1-\frac18-\frac14)>0$: выполнено (A5). Условие п. 1 леммы M:
    $4\sqrt\delta\gamma_1\le2\sqrt\delta M_1K\le\sqrt{2a_0/3}=\sqrt{a_1/h_1}$; значит, выполнено (A4) с двусторонней оценкой
    $\dot\rho$. Выполнено и (D4).
11. **Вывод.** Теорема A [007] даёт решение в $\overline\Omega$ с $q(t)\ne0$, $q,v\to0$. По её шагу 5 $\rho(q(t))=r(t)$ строго
    убывает и меньше $\sigma$, так что $q(t)\in D_\sigma$ и $\lvert\theta(t)\rvert\le R_\theta$. Оценки $\dot r$ — п. 1 леммы M [010]. $\square$

### 2. Предложение 3.1

1. **(a)** $\nabla U_\varepsilon=\big(2x(y^2+2\varepsilon z^2x^2+3x^4),\ 2y(x^2+2\varepsilon z^2y^2+3y^4),\ 2z(\varepsilon(x^4+y^4)-3z^4)\big)$.
   - При $xy\ne0$: $y^2=-2\varepsilon z^2x^2-3x^4$, $x^2=-2\varepsilon z^2y^2-3y^4$; сумма даёт
     $(x^2+y^2)(1+2\varepsilon z^2)=-3(x^4+y^4)<0$ — невозможно при $1+2\varepsilon z^2>0$.
   - При $x=0\ne y$: $y^2(2\varepsilon z^2+3y^2)=0$ и $z(\varepsilon y^4-3z^4)=0$. При $z=0$ получаем $y=0$. При $z\ne0$:
     $y^2=-\frac23\varepsilon z^2$ (нужно $\varepsilon<0$) и $\varepsilon y^4=3z^4$, откуда $\frac49\varepsilon^3=3$, $\varepsilon>0$ — противоречие.
   - Случай $y=0\ne x$ симметричен; при $x=y=0$ имеем $-6z^5=0$.
2. **(b)** очевидно.
3. **(c)** Пусть $\lvert q\rvert=r$, $s=x^2+y^2=r^2-z^2$. Тогда $U_\varepsilon+r^6=x^2y^2+B$,
   $B=\varepsilon z^2(x^4+y^4)+x^6+y^6+s(r^4+r^2z^2+z^4)$. При $\varepsilon\ge-1$
   $\varepsilon z^2(x^4+y^4)\ge-z^2s^2\ge-r^2z^2s$, так что $B\ge s(r^4+z^4)\ge sr^4$. Отсюда
   $U_\varepsilon+r^6\ge x^2y^2+r^4(x^2+y^2)$, с нулём только при $x=y=0$.
4. **(d)** — подстановка $x=rc\theta_1$, $y=rc\theta_2$, $z=rc$ и разложение $(1+t)^{-3}$. Крест — переписанное неравенство
   $\mathcal W<\delta$.
5. **(e)** В точках ветви вне полюса данные (S) [008] выполнены ($H=2\sin^2\varphi>0$). При $u_5=0$ поправка к $g_6$ в
   формуле $g_{m+2}=u_{m+2}\vert_\Sigma-\frac12b_1^{\mathsf T}H^{-1}b_1$ ([008], §3.3) равна нулю ($b_1=\partial_nu_5=0$), так что там
   $G=u_6\vert_\Sigma$. Значения аналитического продолжения в полюсе: $G(0)=-1$ и $G''(0)=6$ (из
   $-\cos^6\varphi=-1+3\varphi^2+O(\varphi^4)$).
   Нормальный гессиан: $\partial_y^2(x^2y^2)=2x^2$. $\square$

### 3. Теорема 3.2

При $\lvert\theta\rvert<\theta_0$ имеем $t:=\lvert\theta\rvert^2<t_0:=(9+\lvert\varepsilon\rvert)^{-1}\le\frac19$; ниже всюду $t\le t_0$.

1. **(S1).** Для $f(t)=(1+t)^{-3}$ выполнено $f'''<0$ при $t\ge0$, поэтому $f\le1-3t+6t^2$ и $1-c^6\ge3t-6t^2$. Кроме
   того, $\lvert E\rvert\le\lvert\varepsilon\rvert t^2+t^3$ и $c^6\le1$. Значит, $\Lambda\ge3t-(7+\lvert\varepsilon\rvert)t^2\ge2t$, и $\mathcal W\ge\Lambda\ge2\lvert\theta\rvert^2$.
2. **(S3).** $\mathcal W(r,0)=0$.
3. **(S2).** $\theta\cdot\nabla(c^4\theta_1^2\theta_2^2)=\theta_1^2\theta_2^2\big(4c^4+\theta\cdot\nabla c^4\big)=\theta_1^2\theta_2^2(4c^4-4tc^6)=4c^6\theta_1^2\theta_2^2$, поэтому
   $$-r\partial_r\mathcal W+\kappa\theta\cdot\nabla\mathcal W-\kappa\mathcal W=(2+4\kappa c^2-\kappa)\frac{c^4\theta_1^2\theta_2^2}{r^2}+\kappa(\theta\cdot\nabla\Lambda-\Lambda).$$
   Первое слагаемое $\ge0$ при $\kappa\le\frac12$. Далее $\theta\cdot\nabla c^6=-6tc^8$, $\theta\cdot\nabla E=4E+2(\theta_1^6+\theta_2^6)$, и
   $$\theta\cdot\nabla\Lambda-\Lambda=6t(1+t)^{-4}-(1-c^6)+c^6\big[(3-6tc^2)E+2(\theta_1^6+\theta_2^6)\big]\ge6t-24t^2-3t-3\lvert E\rvert\ge3t-(27+3\lvert\varepsilon\rvert)t^2\ge0 .$$
   Использованы неравенства Бернулли $(1+t)^{-4}\ge1-4t$ и $(1+t)^{-3}\ge1-3t$, а также $0\le3-6tc^2\le3$ и $t\le t_0$.
4. Теорема S даёт траекторию; для $-e_z$ — то же, так как $U_\varepsilon$ чётна по $z$.
5. **Возмущение.** Добавка к $\mathcal W$ равна $r^{-6}V(r\omega)$; при $\lvert\theta\rvert<\theta_0$
   $\lvert r^{-6}V\rvert\le C_Vr$, $\lvert r\partial_r(r^{-6}V(r\omega))\rvert=\lvert-6r^{-6}V+r^{-5}\langle\nabla V,\omega\rangle\rvert\le7C_Vr$,
   $\lvert\theta\cdot\nabla_\theta(r^{-6}V(r\omega))\rvert=r^{-5}\lvert\langle\nabla V,D\omega\,\theta\rangle\rvert\le M_1\theta_0C_Vr$. Поэтому (S1)–(S3) выполнены с
   $\chi(r)=(8+\frac12M_1\theta_0)C_Vr$. $\square$

### 4. Предложение 3.3

1. $\nabla\rho=e_z=Y$, $h=1$, $DY=0$: (L1), (L3) выполнены с $h_0=h_1=1$, $\theta_i=0$. (L0): $a_1=a_3=1$, $a_2=6$, $\delta\le\frac12$.
2. (L2): $W=x^2y^2+\varepsilon z^2(x^4+y^4)+x^6+y^6\ge0$ и
   $6W-z\partial_zW-4W=2(x^6+x^2y^2+y^6)\ge0$ (так как $z\partial_z(\varepsilon z^2(x^4+y^4))=2\varepsilon z^2(x^4+y^4)$): $\mu=4$, $\varepsilon_1=0$.
3. (D1)–(D3): если $q\in\overline D\setminus0$, то $z>0$ и $(x^2+y^2)^3\le4(x^6+y^6)\le4W\le4\delta z^6$, так что
   $x^2+y^2\le(4\delta)^{1/3}z^2<z^2$. Значит, $\overline D\setminus0\subset\mathcal G$ и $\partial D\cap\{z<\sigma\}\subset\{W=\delta z^6\}$. (D3) — ось $z$.
4. Скобка (3.1) [007] равна $4>0$. Теорема A даёт траекторию.
5. **Возмущение.** Пусть $U_\varepsilon+V\in C^2(B_{2r_1})$; возьмём $\mathcal G_1=\{0<z<r_1,\ x^2+y^2<z^2\}\subset B_{2r_1}\setminus0$, $\sigma<r_1$ и
   $D=\{q\in\mathcal G_1:\ z<\sigma,\ W_V<\delta z^6\}$. На $\mathcal G_1$ $\lvert q\rvert\le\sqrt2z$, так что $\lvert V\rvert,z\lvert\partial_zV\rvert\le C'z^7$. Тогда
   $W_V=W+V\ge-C'z^7\ge-\delta z^6$ при $z\le\delta/C'$; $6W_V-z\partial_zW_V-4W_V\ge-3C'z^7$, то есть $\varepsilon_1=3C'\sigma/\delta$; в
   $\overline D\setminus0$ (там $z\le\sigma\le\delta/C'$) $(x^2+y^2)^3\le4(W_V-V)\le4(\delta+C'z)z^6\le8\delta z^6<z^6$, так что
   $\overline D\setminus0\subset\mathcal G_1$ и траектория лежит в конусе $x^2+y^2\le(8\delta)^{1/3}z^2$; на оси $W_V\le C'z^7<\delta z^6$. Скобка
   $4-3C'\sigma/\delta>0$ при малом $\sigma$. $\square$

### 5. Следствие X

Уменьшим $\theta_0$ так, что $\theta_0\le1$ и $\theta_0\le2(a+b)e_0/\lVert\nabla e\rVert_\infty$.

1. **Разложение.** $T:=U-\sum_{k\le j}u_k$ удовлетворяет $\lvert T(q)\rvert\le C_T\lvert q\rvert^{j+1}$, $\lvert\nabla T(q)\rvert\le C_T\lvert q\rvert^j$ (формула Тейлора,
   $U\in C^{j+1}$). Для $R:=r^{-j}T(r\omega)$: $\lvert R\rvert\le C_Tr$, $\lvert r\partial_rR\rvert\le(j+1)C_Tr$, $\lvert\nabla_\theta R\rvert\le M_1C_Tr$. По (X0)–(X2)
   $$\mathcal W=r^{m-j}eP^2+P\,N+\sum_{m<k<j}r^{k-j}q_k+\Lambda_1(\theta_1)+\Lambda_2(\theta_2)+R,\qquad N:=\sum_{m<k\le j}r^{k-j}n_k,$$
   и $n_k\equiv0$ при $2k\le m+j$. Если $k_n$ — наименьшее $k$ с $n_k\not\equiv0$, то при $r\le1$ $\lvert N\rvert\le C_Nr^{k_n-j}$ и
   $r^{j-m}N^2\le C_N^2r^\nu$.
2. **(S1).** $r^{m-j}eP^2+PN\ge-\frac{r^{j-m}N^2}{4e}\ge-\frac{C_N^2}{4e_0}r^\nu$, $q_k\ge0$, и
   $\Lambda_1+\Lambda_2\ge\alpha(\theta_1^{2p}+\theta_2^{2p})\ge\alpha2^{-p}\lvert\theta\rvert^{2p}$ ($\alpha=\min\alpha_i$; $\lvert t\rvert^{2p_i}\ge\lvert t\rvert^{2p}$ при $\lvert t\rvert\le1$).
3. **(S3).** $P(0)=q_k(0)=\Lambda_i(0)=0$ (последнее — из двух оценок (X2) при $t=0$), так что $\mathcal W(r,0)=R(r,0)\le C_Tr$.
4. **(S2)** при $\kappa\le\kappa_0:=\min\{\frac12,\frac1{C_q+1}\}$, $\mu_0=1$. Вклады в $-r\partial_r\mathcal W+\kappa\theta\cdot\nabla\mathcal W-\kappa\mathcal W$:
   - $r^{m-j}eP^2$: так как $\theta\cdot\nabla P=(a+b)P$, имеем $\theta\cdot\nabla(eP^2)=P^2(2(a+b)e+\theta\cdot\nabla e)\ge0$; вклад
     $\ge(j-m-\kappa)r^{m-j}eP^2\ge\frac{j-m}2r^{m-j}eP^2$;
   - $PN$: вклад равен $P\tilde N$, $\tilde N=\sum_kr^{k-j}\big[(j-k)n_k+\kappa((a+b-1)n_k+\theta\cdot\nabla n_k)\big]$, $\lvert\tilde N\rvert\le\tilde C_Nr^{k_n-j}$; по
     неравенству о средних $\lvert P\tilde N\rvert\le\frac{j-m}4r^{m-j}eP^2+\frac{\tilde C_N^2}{(j-m)e_0}r^\nu$;
   - $r^{k-j}q_k$: вклад $r^{k-j}[(j-k)q_k+\kappa(\theta\cdot\nabla q_k-q_k)]\ge r^{k-j}q_k(1-\kappa(C_q+1))\ge0$;
   - $\Lambda_i$: вклад $\kappa(\theta_i\Lambda_i'-\Lambda_i)\ge0$;
   - $R$: вклад $\ge-(\lvert r\partial_rR\rvert+\kappa\lvert\theta\rvert\lvert\nabla_\theta R\rvert+\kappa\lvert R\rvert)\ge-C_Rr$.

   Сумма $\ge-\chi(r)$ с $\chi:=(C_R+C_T)r+\big(\frac{\tilde C_N^2}{(j-m)e_0}+\frac{C_N^2}{4e_0}\big)r^\nu$, равномерно по $\kappa\in(0,\kappa_0]$.
5. Теорема S применима.
6. **Аналитический случай.** Если $\Lambda_i$ аналитична и имеет в $0$ строгий локальный минимум, то
   $\Lambda_i=\alpha_it^{2p_i}(1+O(t))$, $\alpha_i>0$, и $t\Lambda_i'=2p_i\alpha_it^{2p_i}(1+O(t))\ge\Lambda_i$ при малом $t$. При $a=b=1$ функция
   $p_j-p_j(\theta_1,0)-p_j(0,\theta_2)+p_j(0)$ обращается в нуль на обеих осях и делится на $\theta_1\theta_2$. $\square$

### 6. Следствие X′

Если $\mu_0>1$, заменим его на $1$: $\xi\cdot\nabla\Lambda\ge\mu_0\Lambda\ge\Lambda$, так как $\Lambda\ge0$. Пусть $R$ — как в п. 1 §5;
$\lvert\xi\rvert\le K\lvert\theta\rvert$ (из $\xi(0)=0$ и $\lVert D\xi\rVert\le K$ на выпуклом шаре), и вклад $R$ в (S2) не меньше
$-(j+1+\kappa K\theta_0M_1+\kappa)C_Tr$. Далее $\mathcal W=r^{m-j}p_m+\sum_{m<k<j}r^{k-j}p_k+\Lambda+R$. (S1): все слагаемые, кроме $\Lambda$ и
$R$, неотрицательны. (S3): $p_m(0)=0$ ($\omega_0\in\Sigma$), $p_k(0)=0$, $\Lambda(0)=0$. (S2) при
$\kappa\le\min\{\frac12,\frac1{2(C+\mu_0)}\}$: вклад $r^{k-j}p_k$ ($m\le k<j$) не меньше $r^{k-j}p_k(1-\kappa(C+\mu_0))\ge0$, вклад $\Lambda$ —
$\kappa(\xi\cdot\nabla\Lambda-\mu_0\Lambda)\ge0$. Если $p_m=e\prod F_i^{2a_i}$ с $\xi_w\cdot\nabla F_i=d_iF_i$, то
$\xi_w\cdot\nabla p_m=p_m(\sum2a_id_i+\xi_w\cdot\nabla e/e)\ge0$ около $0$. $\square$

### 7. Примеры

**Принадлежность.**

- **Модель** ($a=b=1$): $e=c^4$, $p_5=0$, $\Lambda_i(t)=1-(1+t^2)^{-3}(1-\varepsilon t^4-t^6)=3t^2+O(t^4)$.
- **X1**: $p_4=c^4\theta_1^2\theta_2^2$, $p_5=q_5=c^5(\theta_1^4+\theta_2^4)\ge0$, $q_5(0)=0$,
  $\theta\cdot\nabla q_5=q_5(4-5c^2\lvert\theta\rvert^2)\ge0$, $p_6=c^6(-1+\theta_1^6+\theta_2^6)$, $\Lambda_i(t)=1-(1+t^2)^{-3}(1-t^6)$.
- **X2**: $p_5=0$, $p_6=c^6\theta_1\theta_2$ ($n_6=c^6$, $2\cdot6=12>m+j=11$), $p_7=-c^7$, $\Lambda_i(t)=1-(1+t^2)^{-7/2}$; $\nu=1$.
- **Касп**: $p_6=c^6F^2$, $F=\theta_2^2-\theta_1^3$, $\xi_w=(2\theta_1,3\theta_2)$, $\xi_w\cdot\nabla F=6F$, $\xi_w\cdot\nabla c^6=-3c^8(4\theta_1^2+6\theta_2^2)$, так что
  $\xi_w\cdot\nabla p_6=p_6\frac{6(2-\theta_2^2)}{1+\lvert\theta\rvert^2}\ge0$ около $0$; $p_7=0$; $p_8=c^8(-1+\theta_1^8+\theta_2^8)$, $\Lambda=4\lvert\theta\rvert^2+O(\lvert\theta\rvert^4)$,
  $\xi_w\cdot\nabla\Lambda-\Lambda=12\theta_1^2+20\theta_2^2+O(\lvert\theta\rvert^4)\ge0$ около $0$.
- **Касание**: $p_6=c^6\theta_2^2(\theta_2-\theta_1^2)^2$, $\xi_w=(\theta_1,2\theta_2)$, $\xi_w\cdot\nabla p_6=p_6\frac{2(\theta_1^2-2\theta_2^2+4)}{1+\lvert\theta\rvert^2}\ge0$ около $0$;
  $p_7=0$; $\Lambda=4\lvert\theta\rvert^2+O(\lvert\theta\rvert^4)$, $\xi_w\cdot\nabla\Lambda-\Lambda=4\theta_1^2+12\theta_2^2+O(\lvert\theta\rvert^4)$.

[Эксперимент: все формулы — sympy, `model_checks.py`, `cusp_check.py`, `tangency_check.py`; независимо R37,
`examples_R37.py`.]

**Изолированность.**

- **X1**: $\partial_zU=x^4+y^4-6z^5=0$ даёт $z\ge0$; при $z=0$ $x=y=0$. При $z>0$ скобка в
  $\partial_xU=2x(y^2+2zx^2+3x^4)$ положительна при $x\ne0$, так что $x=0$; так же $y=0$; тогда $\partial_zU=-6z^5\ne0$. Итак,
  $0$ — единственная критическая точка.
- **X2**: при $z=0$ $\partial_xU=2x(y^2+4x^6)$ даёт $x=0$, а затем $\partial_yU=8y^7$ даёт $y=0$. При $z\ne0$
  $\partial_zU=z^3(4xy-7z^3)=0$ даёт $xy=\frac74z^3$, и $x\partial_xU=2x^2y^2+xyz^4+8x^8=z^6(\frac{49}8+\frac74z)+8x^8>0$ при $\lvert z\rvert<\frac72$.
- **Касп, касание** (замечание 1 R37): тождества
  $$\text{касп: }\tfrac y2U_y-zU_z=4(y^8+2z^8),\qquad\text{касание: }\tfrac y2U_y-\tfrac z2U_z=y^2(yz-x^2)^2+4y^8+4z^8 .$$
  Проверка: в каспе $F=y^2z-x^3$, $\frac y2U_y=2y^2zF+4y^8$, $zU_z=2y^2zF-8z^8$; в касании $F=yz-x^2$, $\frac y2U_y=y^2F^2+y^3zF+4y^8$,
  $\frac z2U_z=y^3zF-4z^8$. Значит, в вещественной критической точке $y=z=0$, и $U_x(x,0,0)=2x^5(4x^2+3)$ (касп),
  $8x^7$ (касание), откуда $x=0$: $0$ — единственная критическая точка в $\mathbb R^3$.

**Не минимум**: $U(0,0,z)=-z^j<0$ при $z>0$. $\square$

### 8. Предложение 5.1 и теорема II

**Предложение 5.1.** $\partial_zU_{\rm II}=6z^2(xy+\eta z^3)$. При $z=0$ $\partial_xU=2x(3x^4+y^2)=0$ даёт $x=0$, затем
$\partial_yU=6y^5=0$. При $z\ne0$ $xy=-\eta z^3$, и $\frac x2\partial_xU=3x^6+x^2y^2+xyz^3=3x^6-\eta(1-\eta)z^6$; аналогично для $y$.
Отсюда $\lvert x\rvert=\lvert y\rvert$, $x^4=x^2y^2=\eta^2z^6$, $x^6=\eta^3\lvert z\rvert^9$ и $\lvert z\rvert^3=\frac{1-\eta}{3\eta^2}$. Не минимум:
$U_{\rm II}(z^{3/2},-z^{3/2},z)=-(1-\eta)z^6+2z^9<0$. $\square$

**Теорема II.** Применяем теорему A [007] и лемму M [010] с $\rho=z$, $\beta=6$, $A(z)=a_0z^6$, $a_0:=1-\eta$ и полем (3).

1. **Тождества.** Обозначим $z\xi^{(0)}:=(3-e)g(1,-1)$, $z\zeta:=-ez^3\frac{(y,x)}{x^2+y^2}$. В квадранте $x>0$, $y<0$:
   $z\xi^{(0)}=(\lambda_xx,\lambda_yy)$ с $\lambda_x=\frac{(3-e)\lvert y\rvert}{x+\lvert y\rvert}$, $\lambda_y=\frac{(3-e)x}{x+\lvert y\rvert}$, $\lambda_x+\lambda_y=3-e$ (так как $\lambda_yy=-(3-e)g$).
   Далее $zY(xy)=(3-e)g(y-x)-ez^3=-(3-e)x\lvert y\rvert-ez^3=(3-e)xy-ez^3$ и $zY(z^3)=3z^3$, откуда
   $$zY(H)=(3-e)H. \tag{8.1}$$
   Пусть $W:=U+a_0z^6=H^2+x^6+y^6+V$. Тогда $zYW=2(3-e)H^2+6x^5(\lambda_xx+z\zeta_1)+6y^5(\lambda_yy+z\zeta_2)+zYV$ и
   $$6W-zYW=2eH^2+6(1-\lambda_x)x^6+6(1-\lambda_y)y^6-6(x^5z\zeta_1+y^5z\zeta_2)+\big[6V-z(\xi\cdot\nabla_{xy}V+\partial_zV)\big]. \tag{8.2}$$
   [Эксперимент: (8.1), (8.2) — `u2_checks.py` и R38, `sym_checks.py`.]
2. **Данные.** $\mathcal G:=\{0<z<r_1,\ 0<x<z,\ -z<y<0\}$, $r_1$ мало ($U\in C^2(B_{2r_1})$). На $\mathcal G$ $g$ и $\zeta$ аналитичны, $Y\in C^\infty$,
   $Y\rho=1$, $\lvert q\rvert\le\sqrt3z$, $\lvert V\rvert\le C'z^7$, $\lvert\nabla V\rvert\le C'z^6$. Пусть $\delta\in(0,\delta_*]$,
   $\delta_*:=\min\{\frac{a_0}2,\frac1{32}\}$, $D:=\{q\in\mathcal G:\ z<\sigma,\ W<\delta z^6\}$ с $\sigma<r_1$ (строго),
   $\sigma\le\min(\delta/C',\frac1{18})$; $\sigma$ ещё уменьшится.
3. **(D1)–(D3).** Пусть $q\in\overline D\setminus0$. Тогда $z>0$ (из $0\le x\le z$, $\lvert y\rvert\le z$), $H^2+x^6+y^6\le\delta z^6+C'z^7\le2\delta z^6$, и
   $x,\lvert y\rvert\le(2\delta)^{1/6}z<z$. При $x=0$ было бы $W=z^6+y^6+V\ge z^6-C'z^7>\delta z^6$; так же при $y=0$. Значит,
   $\overline D\setminus0\subset\mathcal G$, и $\partial D\cap\{z<\sigma\}\subset\{W=\delta z^6\}$; $\sup\{\lvert q\rvert:\ q\in D,\ z<s\}\le\sqrt3s$. (D3): точки
   $(z^{3/2},-z^{3/2},z)\in\mathcal G$, в них $W\le2z^9+C'z^7<\delta z^6$ при малом $z$.
4. **Оценки на $D_\sigma$.** $\lvert H\rvert\le\sqrt{2\delta}z^3\le\frac14z^3$, поэтому $x\lvert y\rvert=z^3-H\in[\frac34z^3,\frac54z^3]$.
   - $\lvert\xi^{(0)}\rvert=\sqrt2(3-e)g/z\le\frac3{\sqrt2}\sqrt{x\lvert y\rvert}/z\le2{,}4z^{1/2}$ (так как $x+\lvert y\rvert\ge2\sqrt{x\lvert y\rvert}$);
     $\lvert\zeta\rvert=\frac{ez^2}{\sqrt{x^2+y^2}}\le\frac{ez^2}{\sqrt{2x\lvert y\rvert}}\le0{,}9e\,z^{1/2}$; итак, $\lvert\xi\rvert\le3z^{1/2}$.
   - $D_{xy}(z\xi^{(0)})=(3-e)\begin{pmatrix}a&-b\\-a&b\end{pmatrix}$, $a=\frac{y^2}{(x+\lvert y\rvert)^2}=\partial_xg$, $b=\frac{x^2}{(x+\lvert y\rvert)^2}=-\partial_yg$, $a+b\le1$.
     Собственные значения симметричной части равны $\frac{3-e}2\big((a+b)\pm\sqrt{2(a^2+b^2)}\big)\ge-\frac{(3-e)(\sqrt2-1)}2$
     (так как $\sqrt{2(a^2+b^2)}\le\sqrt2(a+b)$), норма не больше $3\sqrt2$.
   - $D_{xy}\frac{(y,x)}{x^2+y^2}=\frac1{(x^2+y^2)^2}\begin{pmatrix}-2xy&x^2-y^2\\y^2-x^2&-2xy\end{pmatrix}$ имеет норму $\frac1{x^2+y^2}$ (строки ортогональны
     и равны по длине), поэтому $\lVert D_{xy}(z\zeta)\rVert=\frac{ez^3}{x^2+y^2}\le\frac{ez^3}{2x\lvert y\rvert}\le e$.
   - $z\partial_z\xi=\partial_z(z\xi)-\xi=3\zeta-\xi=2\zeta-\xi^{(0)}$, $\lvert z\partial_z\xi\rvert\le4z^{1/2}$.
5. **(L0), (L1).** $a_1=a_3=a_0$, $a_2=6a_0$, $\delta\le a_0/2$; $h=1+\lvert\xi\rvert^2\in[1,1+9\sigma]\subset[1,\frac32]$.
6. **(L2).** $W\ge-C'z^7\ge-\delta z^6$. Оценим (8.2):
   - $x^5z\zeta_1=\frac{ex^5\lvert y\rvert z^3}{x^2+y^2}\le\frac e2x^4z^3$, $y^5z\zeta_2=\frac{e\lvert y\rvert^5xz^3}{x^2+y^2}\le\frac e2y^4z^3$, поэтому
     $-6(\dots)\ge-3ez^3(x^4+y^4)\ge-6e(2\delta)^{2/3}z^7$;
   - член с $V$ не меньше $-C''z^7$;
   - при $u:=x/\lvert y\rvert$: $6(1-\lambda_x)x^6+6(1-\lambda_y)y^6=6\lvert y\rvert^6f(u)$, $f(u)=\frac{(u-2+e)u^6+1-(2-e)u}{1+u}$. При $u\ge4$
     числитель $\ge\frac u2u^6-2u\ge(\frac12-\frac1{2048})u^7$, так что $f\ge0{,}399u^6\ge0{,}398(u^6+1)$, и часть с $x^6,y^6$ не меньше
     $2{,}388(x^6+y^6)$. При $u\le\frac14$ — то же по симметрии $x\leftrightarrow\lvert y\rvert$ (переставляет $\lambda_x,\lambda_y$);
   - при $\frac14<u<4$: $\max(x,\lvert y\rvert)^2\le4x\lvert y\rvert\le5z^3$, $x^6+y^6\le250z^9$, $\lvert1-\lambda\rvert\le2$, так что часть с $x^6,y^6$ не меньше
     $-3000z^9$.

   С $\mu:=2e\le1$: $6W-zYW-\mu W\ge-3250z^9-(6e(2\delta)^{2/3}+C''+C')z^7$, то есть (L2) выполнено с
   $\varepsilon_1:=[3250\sigma^3+(6e(2\delta)^{2/3}+C''+C')\sigma]/\delta\to0$ при $\sigma\to0$.
7. **(L3M)** с $\gamma_1=\gamma_2=0$. Пусть $w\perp Y$, $\hat w=(w_x,w_y)$.
   - $\langle e_z,w\rangle=w_z=-\xi\cdot\hat w$: $\vartheta_1:=3\sigma^{1/2}$.
   - $zD_YY=(D_{xy}(z\xi)\hat\xi+z\partial_z\xi,0)$, $\lvert zD_YY\rvert\le(3\sqrt2+e)\cdot3z^{1/2}+4z^{1/2}\le19\sigma^{1/2}$: $\vartheta_2:=19\sigma^{1/2}$.
   - $z\langle w,D_wY\rangle=\hat w^{\mathsf T}D_{xy}(z\xi)\hat w+w_z\,\hat w\cdot z\partial_z\xi\ge-\big[\frac{(3-e)(\sqrt2-1)}2+e+4\sigma^{1/2}\big]\lvert w\rvert^2$:
     $\vartheta_3\le1{,}2$ при малом $\sigma$, и $b'=6-2e-2\vartheta_3>2$.
8. **Вывод.** Скобка (0.3) [010] равна $2e-\varepsilon_1-(L_1\vartheta_1+L_2\vartheta_2)/\sqrt\delta\to2e$ при $\sigma\to0$; выберем $\sigma$ так, что она
   $\ge e$, и $4\sqrt\delta\cdot3\sigma^{1/2}\le\sqrt{2a_0/3}$. Лемма M даёт (D4), (A4) с оценками $\dot z$, (A5); теорема A — траекторию в
   $\overline\Omega$, лежащую над $D_\sigma$, откуда $H^2+x^6+y^6\le2\delta z^6$ (п. 3). Квадрант $\{x<0,y>0\}$: $U_{\rm II}(-x,-y,z)=U_{\rm II}$,
   и доказанное применимо к $\tilde V(x,y,z):=V(-x,-y,z)$; отражение траектории даёт нужную. $\square$

## Где работают аналитичность и изолированность

1. **В доказанных утверждениях — нигде.** Теорема S требует только $U\in C^2$ и неравенств (S1)–(S3). Следствия
   X, X′ — условия на струю $j^jU$ плюс $U\in C^{j+1}$ для остатка. Аналитичны лишь данные струи: $p_k$ — многочлены
   на аналитической карте, ветви $\Sigma$ — аналитические кривые. Теорема II — условие на $j^6U$. Изолированность
   нигде не предполагается.
2. **Почему нет противоречия с $C^\infty$-контрпримерами** (Пенлеве–Уинтнер, Лалуа; по `problem/KNOWN_RESULTS.md`, с
   первоисточниками не сверено). Там функции плоские в $0$, а здесь условия конечно определены: зависят
   только от $j^jU$, и возмущение порядка $\ge j+1$ (даже $C^{j+1}$) их не нарушает. Открытыми в пространстве струй
   они не являются ($n_k\equiv0$, точное разложение $p_m=P^2e$, $u_m\ge0$). Для теоремы S: из (S3) следует
   $U(r\omega_0)\le-\frac{a_0}2r^\beta$, а у плоской функции такого направления нет.
3. **Где они понадобятся** — в недоказанной классификации (замечание 7):
   - аналитичность: конечность порядков, конечность многоугольника Ньютона перекрёстных коэффициентов,
     дихотомия «$A_i\equiv0$ или знакоопределённа около $0$», ряды Пюизё дна в подслучаях III–V;
   - изолированность: исключение бесконечного порядка вдоль ветви ([Гипотеза], у особой точки не проверено:
     по аналогии с предложением R [010] ветвь дна тогда состояла бы из критических точек).

## Замечания

### 1. Инвариантная ось и устойчивость к возмущениям [Доказано]

У модели и у примеров X1, X2, касп, касание $\partial_xU=\partial_yU=0$ при $x=y=0$. Поэтому ось $z$ инвариантна и даёт
явную асимптотическую траекторию энергии $0$: $\dot z=-\sqrt{-2U(0,0,z)}$, у модели
$z(t)=z_0(1+2\sqrt2z_0^2t)^{-1/2}$. Сами примеры поэтому тривиальны. Теорема 3.2 и следствия X, X′ этим не
пользуются и верны для $U+V$ с любым $V=O(\lvert q\rvert^{j+1})$ (в $C^{j+1}$, а для модели — в смысле теоремы 3.2), где оси уже
нет. Например, у $U_\varepsilon+xz^6+2y^2z^5$ дно уходит с оси вдоль ветви $\{y=0\}$ на угол $\theta_1=-r/6$ [Эксперимент:
`bottom.py`, $6\theta_1/r=-1{,}000000$ при $r=10^{-6}$]. У $U_{\rm II}$ ось не входит в овраг: $U_{\rm II}(0,0,z)=\eta z^6>0$.

### 2. Сферические и картезианские срезы [Доказано, кроме помеченного]

- «Квартичный профиль вдоль ветвей» (формулировка задания) — свойство картезианских срезов: там профиль
  $-1+\varepsilon b^4+b^6$, а $G''+jG=0$ точно. В сферических срезах профиль $\Lambda=3\lvert\theta\rvert^2+\dots$ квадратичный, и
  теорема 3.2 работает при любом $\varepsilon$.
- Предложение 3.3 при $\varepsilon\ge0$ обходится без $\kappa$-приёма: картезианский профиль положительно однороден по
  $(x,y)/z$. При $\varepsilon<0$ в картезианских срезах на оси $x$ ($y=0$, $x=bz$) $W=z^6b^4(\varepsilon+b^2)<0$ при
  $b^2<\min(\lvert\varepsilon\rvert,1)$; эти точки лежат в $\mathcal G$, и при малом $\delta$ там $W<-\delta z^6$, так что (L2) леммы 2 нарушено.
- Предложение 3.1(c) при $\varepsilon<-1$ может не выполняться: при $\varepsilon=-10$ в точке $x^2=z^2=r^2/2$, $y=0$
  $U=-1{,}25r^6<-r^6$.
- [Эксперимент: `exit_model.py`] В сферических срезах $\kappa$-сжатие нужно. При $\kappa=0$ на лучах вдоль ветвей
  $\min\frac\rho\lambda\Xi/(\delta\rho^6)\approx10^{-23}$; у модели с возмущением $xz^6+2y^2z^5$ он отрицателен ($-0{,}17$; $-0{,}036$). При
  $\kappa=0{,}05;0{,}2;0{,}5$ он примерно равен $2\kappa$. Независимо R37 (`exit_R37.py`) получил $0{,}107$–$0{,}437$ при $\kappa\in\{0{,}05;0{,}2\}$.

### 3. Неприменимость других методов к $U_{\rm II}$

- **Теорема S — ни при каком центре** [Доказано]. Для любого фиксированного $\omega$ $U_{\rm II}(r\omega)>0$ при малых $r>0$:
  вне $\Sigma$ положителен член $r^4u_4(\omega)$, на ветвях $x=0$ и $y=0$ $U_{\rm II}=\eta z^6+y^6$ и $\eta z^6+x^6$. А (S3) требует
  $U(r\omega_0)\le(\chi-a_0)r^\beta<0$.
- **Поле $Y=e_z$ с областью теоремы II** [Доказано]. В точке стенки с $v_\perp=0$ (при $V=0$) по (1.3) [007]
  $\frac\rho\lambda\Xi=6\delta z^6-z\partial_zW=6\delta z^6-6z^3H$. У вершины на стенке $H=\sqrt\delta z^3(1+o(1))$, и отношение к $\delta z^6$
  равно $6-6/\sqrt\delta+o(1)<0$. [Эксперимент: $-20{,}83$, $-36{,}43$, $-54$ при $\delta=0{,}05;0{,}02;0{,}01$.]
- **Теорема 2 [007] с прямыми картами весов $(\frac32,\frac32)$** [Доказано]. Рассмотрим прямую карту следствия 2 [007] с
  продольной координатой $z$: $(x,y)=\gamma(z)+z^{3/2}b$, $\gamma=z^{3/2}g(z)$. Тогда
  $$z^{-6}U=P_g(b)-(1-\eta)+z^3\big((g_1+b_1)^6+(g_2+b_2)^6\big)+O(z),\qquad P_g(b):=\big((g_1+b_1)(g_2+b_2)+1\big)^2,$$
  где $O(z)=z^{-6}V$ равномерно, и $F=z^{6-\beta}\cdot z^{-6}U$. Коэффициенты многочлена $P_g$ при $b_1^2b_2^2$, $b_1^2b_2$, $b_1b_2^2$
  равны $1$, $2g_2$, $2g_1$.
  - $\beta<6$: $F(s,0)\ge-(1-\eta+O(z))z^{6-\beta}\to0$, так что $F_0(0)\ge0$, а (V) требует $F_0(0)<0$.
  - $\beta\ge6$: по (F) $F$ ограничена на $[0,s_1]\times\overline{B_{r_0/2}}$, и $z^{6-\beta}\ge1$, поэтому ограничено $z^{-6}U$, а с ним
    (так как $z^3(\dots)\ge0$ и $P_g\ge0$) и $P_g$ на этом шаре, равномерно по $z$. Следовательно, ограничены их коэффициенты, в том числе $g$, и член $z^3(\dots)\to0$.
  - $\beta>6$: отсюда $P_g(b)\to1-\eta$ равномерно на шаре, что невозможно: коэффициент при $b_1^2b_2^2$ равен $1$.
  - $\beta=6$: $P_g\to F_0+(1-\eta)$ равномерно на шаре. Значит, коэффициенты сходятся, и существует предел
    $g\to g_0=(g_1,g_2)$. Тогда $F_0(b)=((g_1+b_1)(g_2+b_2)+1)^2-(1-\eta)$ и $\nabla F_0(0)=2(g_1g_2+1)(g_2,g_1)$. Обе формы (V) — $(V_0)$
    ($Q\ge0$ на открытом $\Omega_b\ni0$) и $(V_1)$ ($Q\ge\lambda_0\lvert b\rvert^2$) — дают $Q\ge0$ около $0$, то есть $\nabla F_0(0)=0$.
  - При $g_0=0$ (центр на оси): $F_0(0)=\eta>0$ — (V) нарушено.
  - При $g_0\ne0$, $g_1g_2\ne-1$: $\nabla F_0(0)\ne0$ — (V) нарушено.
  - При $g_1g_2=-1$ (центр в вершине, как $g_0=(1,-1)$): $Q=((g_1+b_1)(g_2+b_2)+1)^2$ обращается в нуль на ветви
    гиперболы $(g_1+b_1)(g_2+b_2)=-1$, проходящей через $0$. Эта ветвь связна и неограниченна. Поэтому
    $Q\ge\lambda_0\lvert b\rvert^2$ нарушено, и $(V_1)$ не выполнено. Её связная с $0$ часть в $B_{r_0}$ лежит в компоненте $\Omega_b\ni0$
    множества $\{Q<\delta\}$ и доходит до $\partial B_{r_0}$, так что $\overline{\Omega_b}\not\subset B_{r_0}$, и $(V_0)$ не выполнено.
    Например, при $g_0=(1,-1)$: $Q=(b_1b_2-b_1+b_2)^2$, ветвь $b_2=b_1/(1+b_1)$.
- **Теорема 2 [007] с криволинейными картами других весов** — [Гипотеза]: не разобрано.
- **Поля с постоянными весами** $Y=e_z+(\lambda_xx,\lambda_yy,0)/z$ — эвристика и [Эксперимент]. При $\lambda_x+\lambda_y=3$ семейство
  $\{H=cz^3\}$ сохраняется, но запас $6H^2-zY(H^2)=0$. При $\Lambda:=\lambda_x+\lambda_y<3$ появляется знакопеременный член
  $2(3-\Lambda)H(H-z^3)$ порядка $\sqrt\delta z^6\gg\delta z^6$. Численно (R38) строгого выхода нет ни при одном из проверенных
  наборов весов.
- **Лемма 2 [007] с полем (3)** не подходит [Доказано]. Фактический $\vartheta_3$ на рукавах равен $\frac{(3-e)(\sqrt2-1)}2\ge0{,}5$:
  собственное значение достигается в пределе $u\to\infty$. Такие точки лежат в $D_\sigma$, например $x=(2\delta)^{1/6}z/2$,
  $x\lvert y\rvert=z^3$; там $\lVert D(z\zeta)\rVert\to0$ и $z\partial_z\xi\to0$. Значит, $4\vartheta_3>2e\ge\mu$ при $e\le\frac12$. Лемма M требует
  лишь $2\vartheta_3<\beta-\mu$.

### 4. Пример S1 полигона [Доказано: интервальная арифметика (mpmath.iv); независимо пересчитано R42]

$S1=(x^2-y^2)^2+x^5+2y^5+z(x^4+y^4)+z^6$: в полюсах $U(0,0,\pm s)=s^6>0$, оврага нет; дно на гладкой дуге $x=y$,
$\omega(\varphi)=(\frac{\sin\varphi}{\sqrt2},\frac{\sin\varphi}{\sqrt2},\cos\varphi)$ ($\varphi$ — натуральный параметр). Условия теоремы K1 [008]:

- данные (S) на дуге: $u_4=(x-y)^2(x+y)^2$ обращается в нуль на $x=y$ вместе с градиентом, нормаль $n=\pm(1,-1,0)/\sqrt2$,
  $h_n=D^2u_4(n,n)=8\sin^2\varphi>0$ при $\sin\varphi\ne0$;
- $j=5$, $G=g_5=u_5\vert_\Sigma=\frac18\sin^4\varphi(3\sqrt2\sin\varphi+4\cos\varphi)\not\equiv0$ ([008], §3.3);
- на $I=[4{,}5464;4{,}5466]$ — интервальная арифметика с направленными округлениями (`mpmath.iv`, 40 знаков,
  `s1_interval.py`). Производные $8G'=5As^4c+4Bs^3c^2-Bs^5$, $8G''=5A(4s^3c^2-s^5)+4B(3s^2c^3-2s^4c)-5Bs^4c$ ($s=\sin\varphi$,
  $c=\cos\varphi$, $A=3\sqrt2$, $B=4$) выписаны вручную. Получено:
  - $G'(4{,}5464)\in[-3{,}4063;-3{,}4062]\cdot10^{-4}$, $G'(4{,}5466)\in[2{,}9665;2{,}9666]\cdot10^{-4}$, так что $G'(\varphi^*)=0$ при некотором $\varphi^*\in I$;
  - на всём $I$: $G''+5G\in[0{,}3194;0{,}3230]$, $G\in[-0{,}5732;-0{,}5729]$;
  - $h_n(I)\subset[7{,}7816;7{,}7822]$ (R42).

Итак, $G(\varphi^*)<0$, $G'(\varphi^*)=0$, $G''(\varphi^*)+5G(\varphi^*)>0$, и по теореме K1 [008] у S1 есть асимптотическая траектория.
Независимо R42 (`check_S1.py`, `mpmath.iv`, 30 знаков): $G(I)\subset[-0{,}57313;-0{,}57294]$,
$(G''+5G)(I)\subset[0{,}31969;0{,}32279]$, знаки $G'$ на концах те же. Числа подтверждал и R37.

### 5. Связь с эффективным потенциалом вдоль ветви [Эскиз]

При $b=1$ и $q_k(\theta_1,0)\equiv0$ ($k<j$) функция $-a_0+\Lambda_1(\theta_1)=u_j(\omega(\theta_1,0))$ должна совпадать с эффективным
потенциалом $g_j$ леммы K1 [008] в точках ветви $\theta_1\ne0$: минимум $\mathcal W(r,\theta_1,\cdot)$ по $\theta_2$ равен
$\Lambda_1(\theta_1)+O(r^\nu+r)$. Строго не выписано: срезы $\{\lvert q\rvert=r\}$ и слои леммы K1 различаются. Если
$q_k(\theta_1,0)\not\equiv0$ при некотором $k<j$, ветвь имеет свой меньший $j$ с $G\ge0$ и нулём в $\omega_0$ — каскад к точке
пересечения (пример X1).

### 6. Общий случай II [Эскиз]

При $a=b=1$ пусть $\varphi=r^{-m}U(r\omega)=\sum_ir^i\varphi_i$, $\varphi_i=c_i+A_i(\theta_1)+B_i(\theta_2)+\theta_1\theta_2n_i$,
$i_n=\min\{i:\ n_i\not\equiv0\}$, $n_{i_n}(0)\ne0$, $2i_n\le i_c=\min\{i:\ c_i\ne0\}$. Выделение квадрата
$e(\theta_1\theta_2+\frac{r^{i_n}n_{i_n}}{2e}+\dots)^2-\frac{r^{2i_n}n_{i_n}^2}{4e}$ даёт дно у вершины деформированной гиперболы
$\mathcal H:=\theta_1\theta_2+r^{i_n}\nu(\theta)+\dots=0$ на угловом расстоянии $\asymp r^{i_n/2}$. План: лоскутное поле
$Y=\partial_r+\frac1r(\lambda_1\theta_1,\lambda_2\theta_2)+\frac1r\zeta$, $\lambda_1+\lambda_2=i_n-e$, $\lambda_1=(i_n-e)/(1+u)$ ($u=\lvert\theta_1/\theta_2\rvert$),
поправка $\zeta\parallel\nabla_\theta\mathcal H$ с $Y\mathcal H=\frac{i_n-e}r\mathcal H$; на рукавах при сферической коэрцитивности — ещё
$\kappa$-сжатие. Не проверено: $\vartheta_3$ при зависимости $e,\nu$ от $\theta$, переходная зона, знак членов $A_i,B_i$ при
$i<2i_n$.

### 7. Перечень подслучаев нормального пересечения ($a=b=1$)

| Подслучай | Условие | Статус |
|---|---|---|
| I. Полюсное доминирование | $c_{i_c}<0$; $2i_n>i_c$; $A_i,B_i\ge0$ при $i<i_c$; $A_{i_c},B_{i_c}$ — строгий минимум в $0$ | [Доказано]: следствие X (при аналитичности эти условия влекут (X1), (X2)) |
| II. Гиперболическое разрешение | $2i_n\le i_c$, $n_{i_n}(0)\ne0$, глубина на гиперболе $<0$ | пример $U_{\rm II}+O(\lvert q\rvert^7)$ — [Доказано]; общий — [Эскиз] (замечание 6) |
| III. Дно подходит вдоль ветви | некоторая $A_i$ ($i<\min(i_c,2i_n)$) знакопеременна около $0$ | [Гипотеза]; если сдвиг дна вызван членами порядка выше $i_c$, это случай I |
| IV. Вырожденный профиль ветви | $A_{i_c}\equiv0$ | [Гипотеза]: каскад, не разобрано |
| V. Перекрёстный коэффициент исчезает в полюсе | $n_{i_n}(0)=0$, $2i_n\le i_c$ | [Гипотеза] |

Не разобраны также: кратности $2a\ge4$ или $2b\ge4$ без делимости перекрёстной части на $\theta_1^a\theta_2^b$; перекрёстные
члены у неквазиоднородных особенностей (касп, касание, три ветви); особенности без монотонности $u_m\circ\omega$ вдоль
квазиоднородного поля. Не доказано, что сходимость дна к особой точке $\Sigma$ всегда приводит к подслучаю I или II.

### 8. Эксперименты [Эксперимент]

- Строгий выход (A5) проверялся прямым численным дифференцированием $V-\delta\rho^\beta$ вдоль $(v,-\nabla U)$, без тождества
  (1.3). Модель, X1, X2 — при $\kappa=0{,}2$ минимум положителен. $U_{\rm II}$ с полем (3) — минимум стремится к $2e$ при
  $\sigma\to0$: $0{,}144$; $0{,}194$; $0{,}200$ при $e=0{,}1$. При $\sigma\le2\cdot10^{-3}$ минимум $2e$ достигается у вершины при $K_\perp=0$.
  Независимо R38 (120 знаков, оба рукава целиком, своё несимметричное возмущение): предел $2e$, (A4) с
  $\dot z/z^3\le-0{,}84$.
- Дно $U_{\rm II}$ на сфере — у вершины гиперболы: $\lvert\theta\rvert/\sqrt{2r}\to1$ (`bottom.py`; R38 — сетка и Ньютон). По симметрии
  $(x,y,z)\mapsto(x,-y,-z)$ ещё два минимума у $-e_z$.
- Числа Милнора (Singular, R37, R38): модель $65$, X1 $53$, X2 $102$, касп $213$, касание $215$, $U_{\rm II}$ $65$ — изолированность
  и над $\mathbb C$.
- Формулы (1.1), (1.2) теоремы S — `geom_checks.py` (нелинейные карта и $\xi$, невязка $<4\cdot10^{-40}$) и R37 `geom_S.py`.

## Отличия от записки

Записка — `notes/prover/2026-10-21-singular-sigma.md`, вторая редакция (её §11 — правки по R37, R38). Математика
§1–§5.3 записки перенесена без изменений, кроме перечисленного.

1. Нумерация: формулы (1), (2) модели — (3.1) записки; поле (3) — (5.1); (8.1), (8.2) — (5.2), (5.3); (1.1), (1.2) —
   (2.1), (2.2); (0.3) [010] — (M) записки. Названия утверждений сохранены.
2. Ссылки на лемму M — на [010]; нижняя оценка $\dot\rho$ берётся прямо из п. 1 леммы M [010] (в записке выведена
   отдельно, п. 11 теоремы S).
3. Тождества (8.1), (8.2) теоремы II выведены вручную (в записке — ссылка на sympy).
4. В шаге 6 теоремы II константа средней зоны уточнена ($\lvert1-\lambda\rvert\le2$, $3000z^9$ вместо $4500z^9$); на вывод не влияет.
5. В предложении 3.3 с возмущением константа $\varepsilon_1=3C'\sigma/\delta$ (в записке $6C'\sigma/\delta$, с запасом).
6. Пример S1, связь с эффективным потенциалом, общий случай II, перечень подслучаев и эксперименты перенесены в
   замечания. Строгий выход и дно — только [Эксперимент].
7. В предложении 5.1 утверждение о дне (там [Эксперимент]) вынесено в замечание 8.

**Правки по R37** (внесены в записку, §11):

1. Изолированность каспа и касания — полиномиальными тождествами (замечание 1 R37); метка [Эксперимент] и
   неточная оценка корней множителя $h$ сняты.
2. Пояснение к теореме S о членах порядка $d<\beta$: нужно $\beta-d\ge\kappa_0\mu_0$; $\xi\cdot\nabla P\ge-CP$ допустимо.
3. Следствие X: уменьшение $\theta_0$ оговорено в начале доказательства.
4. Следствие X′: $\mu_0\to\min(\mu_0,1)$.
5. Предложение 3.1(c) — при $\varepsilon\ge-1$, с примером $\varepsilon=-10$; (e) — оба нарушенных условия K1.
6. S1 — [Доказано] через интервальную арифметику (замечание 4).
7. «Открытые условия» → «конечно определённые»; пример Уреньи убран.
8. Оговорка об инвариантной оси во всех примерах (замечание 1).
9. «$D$ от $\kappa$ не зависит» — при фиксированном $\sigma$ (здесь: порядок $\delta\to\kappa\to\sigma$).
10. Перенос предложения 3.3 на $U_\varepsilon+V$ доказан (в первой редакции — эскиз).

**Правки по R38** (внесены в записку, §11):

1. З1: $\sigma<r_1$ строго.
2. З2: $6\cdot0{,}398=2{,}388$.
3. З3: квадрант $\{x<0,y>0\}$ — при любом $V$.
4. З4: $F_0=(b_1b_2+1)^2-(1-\eta)$; на гиперболе обращается в нуль $Q=F_0-\min F_0$.
5. З5: неприменимость теоремы S и поля $e_z$ — доказательства; прямые карты весов $(\frac32,\frac32)$ — [Доказано];
   криволинейные — [Гипотеза]; поля с постоянными весами — [Эксперимент] (замечание 3).
6. З6: «сохраняет семейство $\{H=cz^{3-e}\}$, в частности гиперболу $\{H=0\}$».
7. З7: ссылка на [010].
8. З8: комментарий о худших точках строгого выхода уточнён.

**Правки по R42** ([`notes/reviewer/2026-10-21-result013.md`](../notes/reviewer/2026-10-21-result013.md), текст результата; ошибок в
доказательствах нет):

1. З1: в §3 исправлено направление импликации ($\lvert\theta\rvert<\theta_0\Rightarrow t<t_0$); в теореме 3.2
   $\theta_0=(9+\lvert\varepsilon\rvert)^{-1/2}$ без лишнего $\min\{\frac12,\cdot\}$.
2. З2: в предложении 3.3 с возмущением область $\mathcal G_1=\{0<z<r_1,\dots\}$, где $U_\varepsilon+V\in C^2$; раствор конуса
   $(8\delta)^{1/3}$; «то же верно» заменено явной формулировкой.
3. З3: в замечании 3 довод для прямых карт весов $(\frac32,\frac32)$ дописан для всех центров $\gamma=z^{3/2}g$ (и всех $\beta$):
   $\nabla F_0(0)=2(g_1g_2+1)(g_2,g_1)$, при $g_1g_2=-1$ $Q$ обращается в нуль на гиперболе через $0$.
4. З4: метка [Доказано] у пункта о лемме 2 с полем (3), с указанием точек рукава в $D_\sigma$.
5. З5: метка примера S1 — «[Доказано: интервальная арифметика (mpmath.iv); независимо пересчитано R42]»; в файл
   перенесены интервалы и формулы производных.
6. З6: в 3.1(e) $G(0)$, $G''(0)$ — значения аналитического продолжения $u_6\vert_\Sigma$ (формула $g_{m+2}$ [008] применяется вне
   полюса).
7. З7: в разделе об аналитичности — «из (S3) следует», без (S1).
8. З8: в пояснении к следствию X — «сужения $u_j$ на ветви» вместо «эффективные потенциалы».
9. З9: в 3.1(d) описание креста помечено как пояснение; в замечании 2 точки с $W<0$ — при $b^2<\min(\lvert\varepsilon\rvert,1)$.
10. З10: в замечании 7 «в точности эти» заменено на «влекут».
