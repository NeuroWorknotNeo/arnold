# 004. Лемма R: векторное поле в одном режиме

- **Статус:** [Проверено: reviewer R13 (агент), 21.10.2026,
  [`notes/reviewer/2026-10-21-result004.md`](../notes/reviewer/2026-10-21-result004.md)]; ждёт
  проверки человеком. Исходный текст проверил reviewer R4
  ([`notes/reviewer/2026-10-21-lemmaR-proof.md`](../notes/reviewer/2026-10-21-lemmaR-proof.md)),
  исправленную версию со всеми новыми частями — R13 (ошибок нет). Редакционные замечания R13
  (радиус в шаге 8; сужение $\Omega_U$ в (Д5); сохранение (C1), (C2) при уменьшении радиуса;
  операторная норма блока в (f); метки у замечаний 3(а), 3(в), 2(в)) не влияют на верность и
  перечислены в отзыве. R13 попутно заметил [Доказано в отзыве]: всегда $\kappa=1/N$, и в (C2)
  достаточно $\varphi_\alpha\circ\Phi_\alpha=\psi_\alpha(\hat y)$ с ограниченным $D\psi_\alpha$.
  Метки внутри файла. Лемма R, предложения 1 и 3, следствия 2 и 4 — [Доказано]. В исходном тексте
  не было предложения 1(б), предложения 3 и следствия 4: они добавлены при исправлении по
  замечаниям 1 и 6 R4, и R4 их не читал. Замечания 2(а) и 3(б) — [Эскиз]. Результаты скриптов —
  [Эксперимент].
- **Авторы:** vlad-claude, 27.09.2026
  ([`notes/vlad-claude/lemmaR-proof.md`](../notes/vlad-claude/lemmaR-proof.md)). Правки по отзыву
  R4 — prover (агент), 21.10.2026. Перечень правок — в разделе «Отличия от исходного текста».
- **Зависит от:**
  - лемма 1 и следствие 4 результата [001](001-field-criterion.md) (критерий поля)
    [Проверено: reviewer R1, 21.10.2026] — только в следствиях 2 и 4 ниже;
  - теорема об обратной функции класса $C^2$ (стандартный факт): если $C^2$-отображение открытых
    множеств $\mathbb R^n$ имеет обратимый дифференциал в точке $p$, то оно —
    $C^2$-диффеоморфизм некоторой окрестности $p$ на открытое множество;
  - элементарный анализ: теорема о среднем в интегральной форме, ряд Неймана, компактность.

  Оценки §5 теоремы B ([002](002-theorem-B.md)) — частный случай оценок шагов 5–7 (замечание 3).
  На 002 этот текст не опирается.
- **Проверочные скрипты** [Эксперимент]: [`experiments/prover/lemmaR/`](../experiments/prover/lemmaR/)
  (выкладки, добавленные или изменённые здесь) и
  [`experiments/reviewer/lemmaR/`](../experiments/reviewer/lemmaR/) (рецензент R4, построение
  поля в одной карте).

## Утверждение

**Обозначения.** $|\cdot|$ — евклидова норма вектора, $\|\cdot\|$ — операторная норма матрицы,
$Y^\circ$ — внутренность множества $Y$, $\operatorname{sym}M=\frac12(M+M^{\mathsf T})$,
$(u\otimes v)_{ij}=u_iv_j$. Для подпространства $X\subset\mathbb R^n$ через $P_X$ обозначен
ортопроектор на $X$, $P_\omega:=P_{\mathbb R\omega}$.

### Данные карты режима

**(Д1) Блоки и веса.** Даны целые $n\ge1$, $s\ge0$, $k\ge0$, $c_1,\dots,c_k\ge1$ с
$1+s+c_1+\dots+c_k=n$. Точку $\mathbb R^{n-1}$ записываем как $\hat y=(\hat y_0,\hat y_1,\dots,\hat y_k)$,
где $\hat y_0\in\mathbb R^s$ — угловой блок (при $s=0$ его нет), $\hat y_i\in\mathbb R^{c_i}$ —
нормальные блоки; $\hat y_{\ge1}:=(\hat y_1,\dots,\hat y_k)$. Веса — рациональные числа
$w_0=1<w_1<\dots<w_k$; радиальной координате $r>0$ приписан вес $w_r:=1$. Целое $N\ge1$ таково,
что $a_i:=N(w_i-1)\in\mathbb Z$ (тогда $a_i\ge1$ при $i\ge1$, $a_0=0$). Положим
$$\sigma_j:=r^{w_j}\ (j=0,\dots,k;\ \sigma_0=r),\qquad
S(r):=\operatorname{diag}\bigl(1,\ rI_s,\ \sigma_1I_{c_1},\dots,\sigma_kI_{c_k}\bigr).$$
Радиальной строке и радиальному столбцу $S$ отвечает масштаб $1$.

**(Д2) Отображение.** $\tilde K\subset\mathbb R^{n-1}$ — компакт, $\tilde K_0\subset\mathbb R^s$ — его
проекция на $\hat y_0$, $R_K:=\max_{\hat y\in\tilde K}|\hat y_{\ge1}|$, $\varepsilon_0>0$. Дано
отображение $G\colon\mathcal D\to\mathbb R^n$ класса $C^2$ на открытом множестве
$\mathcal D\subset\mathbb R^s\times\mathbb R^{n-1-s}\times\mathbb R$ переменных $(\hat y_0,\mu,\varepsilon)$,
$\mu=(\mu_1,\dots,\mu_k)$, $\mu_i\in\mathbb R^{c_i}$, причём
$\mathcal D\supset\tilde K_0\times\{0\}\times[0,\varepsilon_0]$. Положим
$$\Gamma(\hat y,\varepsilon):=G\bigl(\hat y_0,\ \varepsilon^{a_1}\hat y_1,\dots,\varepsilon^{a_k}\hat y_k,\ \varepsilon\bigr),\qquad
\Phi(r,\hat y):=r\,\Gamma(\hat y,r^{1/N}).$$
По шагу 0 найдутся открытое $\Omega_G\supset\tilde K$ и $\varepsilon_G\in(0,\min(\varepsilon_0,1)]$
такие, что $\Gamma\in C^2(\Omega_G\times(-\varepsilon_G,\varepsilon_G))$ и
$\Phi\in C^2\bigl((0,\varepsilon_G^N)\times\Omega_G\bigr)$. Всюду ниже $\varepsilon:=r^{1/N}$. Тогда
$r\varepsilon^{a_i}=\sigma_i$.

**(Д3) Ортогональность (O).** Для $\hat y_0\in\tilde K_0$ положим $\omega(\hat y_0):=G(\hat y_0,0,0)$,
$T_0:=\operatorname{im}D_{\hat y_0}G(\hat y_0,0,0)$, $N_i:=\operatorname{im}D_{\mu_i}G(\hat y_0,0,0)$.
Требуется: $|\omega(\hat y_0)|=1$, $\dim T_0=s$, $\dim N_i=c_i$, и
$$\mathbb R^n=\mathbb R\omega\oplus T_0\oplus N_1\oplus\dots\oplus N_k$$
— сумма попарно ортогональных подпространств. Положим
$$L(\hat y_0):=P_\omega+P_{T_0}+\sum_{i=1}^kw_iP_{N_i}.$$

**(Д4) Инъективность (Φ).** Существует $\rho_\Phi\in(0,\varepsilon_G^N]$ такое, что $\Phi$ инъективно
на $(0,\rho_\Phi)\times\tilde K^\circ$. (Когда это выполнено, говорит предложение 1.)

**(Д5) Потенциал и разложение.** $U\in C^1(\mathcal U)$, $\mathcal U\subset\mathbb R^n$ открыто. Даны
число $d>0$, число $e>0$ с $Ne\in\mathbb Z$, открытое $\Omega_U$ с $\tilde K\subset\Omega_U\subset\Omega_G$,
число $\varepsilon_U\in(0,\varepsilon_G]$, функции $F\in C^2(\Omega_U)$,
$H\in C^2\bigl(\Omega_U\times(-\varepsilon_U,\varepsilon_U)\bigr)$ и $\rho_U\in(0,\varepsilon_U^N]$
такие, что $\Phi\bigl((0,\rho_U)\times\Omega_U\bigr)\subset\mathcal U$ и
$$U(\Phi(r,\hat y))=r^d\bigl(F(\hat y)+r^eH(\hat y,r^{1/N})\bigr),\qquad 0<r<\rho_U,\ \hat y\in\Omega_U.\tag{R}$$
Заметим: $r^e=\varepsilon^{Ne}$, и $Ne$ — натуральное число.

**(Д6) Множество $J$ и условие (Reg).** Положим
$J_{\max}:=\{b\in\{r,0,1,\dots,k\}:\ w_b>w_k-e\}$ (блок $0$ учитывается, только если $s\ge1$).
Так как $w_r=w_0=1$, имеем $r\in J_{\max}\iff0\in J_{\max}\iff w_k-1<e$. Блок $k$ лежит в $J_{\max}$
всегда. Зафиксируем любое $J\subset J_{\max}$ и положим
$$D_J(\hat y):=[r\in J]\,d^2F(\hat y)^2+\sum_{j\in J\setminus\{r\}}|\partial_{\hat y_j}F(\hat y)|^2,$$
где $[r\in J]\in\{0,1\}$, а $\partial_{\hat y_j}F$ — вектор частных производных по координатам блока
$j$ (евклидова метрика карты).

**(Reg)** Даны компакт $K\subset\tilde K^\circ$ и $c_0>0$ такие, что для всех $\hat y\in K$
$$|F(\hat y)|\le c_0\ \Longrightarrow\ D_J(\hat y)\ge c_0^2.$$

Положим
$$\kappa:=\min\Bigl(\{1/N\}\cup\{e+w_j-w_k:\ j\in J\}\Bigr)>0 .$$

### Построение поля

Зафиксируем $\chi\in C^\infty(\mathbb R)$ с $0\le\chi\le1$, $\chi=1$ на $[-c_0/2,c_0/2]$ и $\chi=0$ вне
$(-c_0,c_0)$. В координатах $(r,\hat y)\in(0,\rho_U)\times\Omega_U$ пишем $U$ вместо $U\circ\Phi$ и
полагаем
$$V:=r\partial_r,\qquad U_+:=V(U)-dU,$$
$$\hat W:=-\chi(F)\,U_+\,\frac{[r\in J]\,(r\partial_rU)\,r\partial_r+\sum_{j\in J\setminus\{r\}}\langle\partial_{\hat y_j}U,\partial_{\hat y_j}\rangle}
{[r\in J]\,(r\partial_rU)^2+\sum_{j\in J\setminus\{r\}}|\partial_{\hat y_j}U|^2},\qquad \hat A:=V+\hat W,$$
где $\langle\partial_{\hat y_j}U,\partial_{\hat y_j}\rangle=\sum_\alpha\frac{\partial U}{\partial\hat y_j^\alpha}\frac{\partial}{\partial\hat y_j^\alpha}$,
и $\hat W:=0$ в точках, где $\chi(F(\hat y))=0$. Евклидово представление поля $\hat Z$, заданного в
координатах, — это поле $Z^x$ с $Z^x(\Phi(p)):=D\Phi(p)\,\hat Z(p)$. Положим $A:=A^x=V^x+W^x$.

### Лемма R

**Лемма R.** [Доказано] Пусть выполнены (Д1)–(Д6). Тогда существуют
$\rho'\in(0,\min(\rho_\Phi,\rho_U,1)]$ и $C_A>0$ такие, что:

- **(a)** $\Phi$ — $C^2$-диффеоморфизм $(0,\rho')\times\tilde K^\circ$ на открытое множество, и
  $\frac34r\le|\Phi(r,\hat y)|\le\frac54r$ на $(0,\rho')\times\tilde K$. Множество
  $\mathcal O:=\Phi\bigl((0,\rho')\times K^\circ\bigr)$ открыто.
- **(b)** $\hat W$ корректно определено и класса $C^1$ на $(0,\rho')\times K^\circ$: в окрестности
  каждой точки, где $\chi(F)\ne0$, знаменатель положителен. Поле $A$ класса $C^1$ на $\mathcal O$.
- **(c)** На $\mathcal O$ выполнено $\langle A,\nabla U\rangle=dU+(1-\chi(F))U_+$, где
  $U_+=\langle V^x,\nabla U\rangle-dU$, а $F=F(\hat y)$ для $x=\Phi(r,\hat y)$. В точках
  $x\in\mathcal O$ с $U(x)<0$ выполнено $\langle A(x),\nabla U(x)\rangle\le\frac d2U(x)$.
- **(d)** $\operatorname{sym}DA(x)\succeq\frac12I$ на $\mathcal O$.
- **(e)** $|A(x)|\le C_A|x|$ на $\mathcal O$.
- **(f)** (оценки для склейки) В точке $x=\Phi(r,\hat y)\in\mathcal O$:
  $$\|DV^x(x)-L(\hat y_0)\|\le C_Ar^{1/N},\quad |V^x(x)|\le C_Ar,\quad |W^x(x)|\le C_Ar^{1+e},\quad
  \|DW^x(x)\|\le C_Ar^{\kappa},$$
  $\langle W^x,\nabla U\rangle(x)=-\chi(F(\hat y))\,U_+(x)$, и строки матрицы $D\Phi(r,\hat y)^{-1}$,
  отвечающие блоку $0$, по норме не больше $C_A/r$.

### Об условии (Φ)

**Предложение 1.** [Доказано] Пусть выполнены (Д1)–(Д3).

- **(а)** Существует $\rho_Q>0$ такое, что $D\Phi(r,\hat y)$ обратим при $0<r<\rho_Q$,
  $\hat y\in\tilde K$. Если при некотором $\rho\le\rho_Q$ отображение $\Phi$ инъективно на
  $(0,\rho)\times\tilde K^\circ$, то $\Phi$ — $C^2$-диффеоморфизм $(0,\rho)\times\tilde K^\circ$ на
  открытое подмножество $\mathbb R^n$.
- **(б)** Если $\omega$ инъективно на $\tilde K_0$, то существует $\rho_\Phi>0$, при котором $\Phi$
  инъективно на $(0,\rho_\Phi)\times\tilde K$. В частности, выполнено (Φ). Малость $R_K$, то есть
  близость $\tilde K$ к $\{\hat y_{\ge1}=0\}$, не требуется. От $R_K$ зависит только $\rho_\Phi$.
- **(в)** Без инъективности $\omega$ условие (Φ) может нарушаться при всех $\rho>0$, даже при $k=0$,
  когда $\tilde K\subset\{\hat y_{\ge1}=0\}$ тривиально. Пример: $n=2$, $s=1$, $k=0$, $N=1$,
  $G(\theta,\varepsilon)=(\cos\theta,\sin\theta)$, $\tilde K=[0,4\pi]$.

### Одна карта: тотальная неустойчивость

**Следствие 2.** [Доказано] Пусть выполнены (Д1)–(Д6), а $\rho'$, $\mathcal O$, $A$, $C_A$ — из
леммы R. Пусть, кроме того, $\rho''>0$ и

- (i) $U\in C^2$ в окрестности замкнутого шара $\bar B_{\rho''}$ и $U(0)=0$;
- (ii) $X:=\{x\in B_{\rho''}:\ U(x)<0\}\subset\mathcal O$.

Тогда $0$ тотально неустойчива с шаром $B_{\rho''}$ в смысле [001](001-field-criterion.md): каждый
связный промежуток времени, когда движение с энергией $E<0$ лежит в $B_{\rho''}$, не длиннее
$T(E)=4C_A\rho''w(E)/(d|E|)$, где $w(E)=\sqrt{2(E-\min_{\bar B_{\rho''}}U)}$. Если вдобавок $0$ не
точка локального минимума $U$, то равновесие $x=0$ системы $\ddot x=-\nabla U(x)$ неустойчиво по
Ляпунову.

### Несколько карт одного режима

**Предложение 3 (склейка по угловой координате).** [Доказано] Пусть для $\alpha=1,\dots,m$ заданы
данные (Д1)–(Д6) («карта $\alpha$») с общими $n$, $d$ и общей функцией $U\in C^1(\mathcal U)$.
Остальные данные у каждой карты свои: $s_\alpha$, веса, $N_\alpha$, $G_\alpha$, $\tilde K_\alpha$,
$K_\alpha$, $F_\alpha$, $H_\alpha$, $e_\alpha$, $J_\alpha$, $c_{0,\alpha}$. Положим
$c_0:=\min_\alpha c_{0,\alpha}$: (Reg) при меньшем $c_0$ сохраняется, так как из $|F|\le c_0$
следует $|F|\le c_{0,\alpha}$ и $D_J\ge c_{0,\alpha}^2\ge c_0^2$. Поля всех карт строим с одной и
той же $\chi$. Пусть $\Phi_\alpha$, $\rho'_\alpha$, $C_{A,\alpha}$, $\kappa_\alpha$, $V_\alpha^x$,
$W_\alpha^x$ — из леммы R для карты $\alpha$. Положим $\rho_*:=\min_\alpha\rho'_\alpha$,
$\mathcal O_\alpha^*:=\Phi_\alpha\bigl((0,\rho_*)\times K_\alpha^\circ\bigr)$ и
$\mathcal O^*:=\bigcup_\alpha\mathcal O_\alpha^*$. Предположим:

- **(C1)** (общая радиальная структура) Если $\Phi_\alpha(r,\hat y)=\Phi_\beta(r',\hat y')$, где
  $(r,\hat y)\in(0,\rho_*)\times K_\alpha^\circ$ и $(r',\hat y')\in(0,\rho_*)\times K_\beta^\circ$, то
  $r=r'$ и $\Phi_\alpha(t,\hat y)=\Phi_\beta(t,\hat y')$ при всех $t\in(0,\rho_*)$.
- **(C2)** (разбиение единицы по углу) Заданы функции $\varphi_\alpha\in C^1(\mathcal O^*)$ с
  $0\le\varphi_\alpha\le1$ и $\sum_\alpha\varphi_\alpha\equiv1$ на $\mathcal O^*$. Замыкание в
  $\mathcal O^*$ множества $\{\varphi_\alpha\ne0\}$ лежит в $\mathcal O_\alpha^*$. На
  $\mathcal O_\alpha^*$ функция $\varphi_\alpha$ зависит только от угловой координаты карты
  $\alpha$: $\varphi_\alpha(\Phi_\alpha(r,\hat y))=\psi_\alpha(\hat y_0)$, где $\psi_\alpha$ класса
  $C^1$ на открытом множестве, содержащем проекцию $K_{\alpha,0}$ компакта $K_\alpha$ на
  $\hat y_0$, и $|D\psi_\alpha|\le L_\psi$ на $K_{\alpha,0}$. При $s_\alpha=0$ функция $\psi_\alpha$
  постоянна.

Тогда найдётся $\rho_{**}\in(0,\rho_*]$ со следующим свойством. На открытом множестве
$\mathcal O^{**}:=\bigcup_\alpha\Phi_\alpha\bigl((0,\rho_{**})\times K_\alpha^\circ\bigr)$ поле
$$A:=V^x+\sum_\alpha\varphi_\alpha W_\alpha^x$$
корректно определено (слагаемое $\varphi_\alpha W_\alpha^x$ продолжено нулём вне $\mathcal O_\alpha^*$)
и класса $C^1$. Здесь $V^x=V^x_\alpha$ на $\mathcal O^*_\alpha$, и оно не зависит от $\alpha$.
Функции $r(x)$ и $F(x):=F_\alpha(\hat y)$ при $x=\Phi_\alpha(r,\hat y)$ тоже не зависят от карты.
Выполнено:
$\langle A,\nabla U\rangle=dU+(1-\chi(F))U_+$; $\langle A,\nabla U\rangle\le\frac d2U$ там, где $U<0$;
$\operatorname{sym}DA\succeq\frac12I$; $|A(x)|\le C|x|$ при некотором $C$.

**Следствие 4.** [Доказано] Пусть в условиях предложения 3 выполнены (i) из следствия 2 и
$\{x\in B_{\rho''}:\ U(x)<0\}\subset\mathcal O^{**}$. Тогда $0$ тотально неустойчива с шаром
$B_{\rho''}$, с $T(E)=4C\rho''w(E)/(d|E|)$. Если $0$ не точка локального минимума $U$, равновесие
неустойчиво по Ляпунову.

Если образы карт попарно не пересекаются, (C1) и (C2) не нужны: поле на объединении непересекающихся
открытых множеств задаётся на каждом отдельно.

## Доказательство

**Соглашение об $O$.** Запись $Z=O(r^a)$, где $Z$ — число, вектор или матрица, зависящие от точки,
означает $|Z|\le Cr^a$ (соответственно $\|Z\|\le Cr^a$) с константой $C$, не зависящей от $r$ и
от точки $\hat y$ указанного компакта. Так же $O(\varepsilon^a)$. Все константы ниже зависят
только от данных (Д1)–(Д6) и от $\chi$.

### Шаг 0. Области определения

Компакт $\mathcal K:=\tilde K_0\times\{0\}\times[0,\varepsilon_0]$ лежит в открытом $\mathcal D$, поэтому
найдётся $\delta\in(0,1]$ с
$$\mathcal K_\delta:=\{(\hat y_0,\mu,\varepsilon):\ \operatorname{dist}(\hat y_0,\tilde K_0)\le\delta,\
|\mu|\le\delta,\ -\delta\le\varepsilon\le\varepsilon_0+\delta\}\subset\mathcal D.$$
Действительно, $\mathcal K_\delta$ компактно и лежит в замкнутой $\sqrt3\delta$-окрестности
$\mathcal K$, а расстояние от $\mathcal K$ до $\mathbb R^n\setminus\mathcal D$ положительно. Положим
$$\Omega_G:=\{\hat y:\ \operatorname{dist}(\hat y_0,\tilde K_0)<\delta,\ |\hat y_{\ge1}|<R_K+1\},\qquad
\varepsilon_G:=\min\bigl(\varepsilon_0,\ \delta/(R_K+1)\bigr)\le1.$$
При $\hat y\in\Omega_G$ и $|\varepsilon|<\varepsilon_G$ имеем $|\varepsilon|<1$, поэтому
$|\varepsilon^{a_i}\hat y_i|\le|\varepsilon||\hat y_i|$. Отсюда
$|\mu|\le|\varepsilon||\hat y_{\ge1}|<\delta$, и
$(\hat y_0,\mu,\varepsilon)\in\mathcal K_\delta\subset\mathcal D$. Значит,
$\Gamma\in C^2(\Omega_G\times(-\varepsilon_G,\varepsilon_G))$ как композиция $G$ с полиномиальным
отображением, и $\Phi\in C^2((0,\varepsilon_G^N)\times\Omega_G)$, так как $r\mapsto r^{1/N}$ гладко
при $r>0$. При $\operatorname{dist}(\hat y_0,\tilde K_0)<\delta$ определено и
$\omega(\hat y_0)=G(\hat y_0,0,0)$, причём $\Gamma(\hat y,0)=\omega(\hat y_0)$ для всех
$\hat y\in\Omega_G$.

Положим $\check K:=\{\hat y:\ \operatorname{dist}(\hat y_0,\tilde K_0)\le\delta/2,\ |\hat y_{\ge1}|\le R_K\}$
— компакт с $\tilde K\subset\check K\subset\Omega_G$ — и $\varepsilon_2:=\varepsilon_G/2$. Всякая
функция, непрерывная на $\Omega_G\times(-\varepsilon_G,\varepsilon_G)$, ограничена на
$\check K\times[0,\varepsilon_2]$. В частности, ограничены $\Gamma$ и её частные производные до
второго порядка, а также $G$ и её производные до второго порядка в точках
$(\hat y_0,\mu(\hat y,\varepsilon),\varepsilon)$. По теореме о среднем по $\varepsilon$:
$$|\Gamma(\hat y,\varepsilon)-\omega(\hat y_0)|\le C_\Gamma\varepsilon\quad\text{на }\check K\times[0,\varepsilon_2],\qquad
C_\Gamma:=\max_{\check K\times[0,\varepsilon_2]}|\Gamma_\varepsilon|.\tag{0.1}$$

### Шаг 1. Якобиан и вторые производные $\Phi$

Пусть $(r,\hat y)\in(0,\varepsilon_G^N)\times\Omega_G$. Производные $G$ ниже берутся в точке
$(\hat y_0,\mu(\hat y,\varepsilon),\varepsilon)$. Так как $\partial_r\varepsilon=\varepsilon/(Nr)$ и
$r\varepsilon^{a_i}=\sigma_i$,
$$\partial_r\Phi=\Gamma+\tfrac{\varepsilon}N\Gamma_\varepsilon,\qquad
\partial_{\hat y_0}\Phi=r\,D_{\hat y_0}G,\qquad \partial_{\hat y_i}\Phi=\sigma_i\,D_{\mu_i}G\ \ (i\ge1).\tag{1.1}$$
Значит, $D\Phi=Q\,S(r)$, где
$$Q(\hat y,\varepsilon):=\bigl[\ \Gamma+\tfrac\varepsilon N\Gamma_\varepsilon\ \big|\ D_{\hat y_0}G\ \big|\ D_{\mu_1}G\ \big|\dots\big|\ D_{\mu_k}G\ \bigr]$$
— квадратная матрица порядка $1+s+\sum c_i=n$. Её элементы — это $\Gamma$, $\Gamma_\varepsilon$ и
первые производные $G$, взятые в точке, которая гладко зависит от $(\hat y,\varepsilon)$. Так как
$G\in C^2$, имеем $Q\in C^1(\Omega_G\times(-\varepsilon_G,\varepsilon_G))$. При $\varepsilon=0$ получаем
$\mu=0$, и
$$Q(\hat y,0)=Q_0(\hat y_0):=\bigl[\ \omega\ \big|\ D_{\hat y_0}G(\hat y_0,0,0)\ \big|\ D_{\mu_1}G(\hat y_0,0,0)\ \big|\dots\bigr].$$
По теореме о среднем по $\varepsilon$
$$\|Q(\hat y,\varepsilon)-Q_0(\hat y_0)\|\le C_1\varepsilon\quad\text{на }\check K\times[0,\varepsilon_2].\tag{1.2}$$
По (O) при $\hat y_0\in\tilde K_0$ столбцы $Q_0$ поблочно — базисы слагаемых $\mathbb R\omega$, $T_0$,
$N_i$ прямого разложения $\mathbb R^n$, поэтому $Q_0(\hat y_0)$ обратима. По непрерывности и
компактности $C_0:=\max_{\tilde K_0}\|Q_0^{-1}\|<\infty$. Положим
$\varepsilon_Q:=\min(\varepsilon_2,\ 1/(2C_0C_1))$ и $\rho_Q:=\varepsilon_Q^N$. При $\hat y\in\tilde K$,
$0\le\varepsilon\le\varepsilon_Q$ имеем $Q=Q_0\bigl(I+Q_0^{-1}(Q-Q_0)\bigr)$ и
$\|Q_0^{-1}(Q-Q_0)\|\le\frac12$. Значит, $Q$ обратима и
$$\|Q^{-1}\|\le2C_0,\qquad \|Q^{-1}-Q_0^{-1}\|=\|Q^{-1}(Q-Q_0)Q_0^{-1}\|\le2C_0^2C_1\varepsilon.\tag{1.3}$$
Итак, при $0<r<\rho_Q$, $\hat y\in\tilde K$ дифференциал $D\Phi$ обратим и
$D\Phi^{-1}=S(r)^{-1}Q^{-1}$. Строки $D\Phi^{-1}$, отвечающие блоку $b\in\{r,0,\dots,k\}$, по норме
не больше $2C_0/\sigma_b$ (где $\sigma_r:=1$):
$$\text{строки } r:\ O(1);\qquad \text{строки блока } j\ge0:\ O(1/\sigma_j).\tag{1.4}$$

*Вторые производные* при $\hat y\in\tilde K$, $0<r<\rho_Q$. Для блоков $i,j\in\{0,\dots,k\}$ (с
$\mu_0:=\hat y_0$, $a_0=0$):
$$\partial_{\hat y_i}\partial_{\hat y_j}\Phi=r\varepsilon^{a_i+a_j}D_{\mu_i}D_{\mu_j}G=\frac{\sigma_i\sigma_j}r\,O(1),\qquad
\partial_r\partial_{\hat y_j}\Phi=\frac{w_j\sigma_j}rD_{\mu_j}G+\sigma_j\frac{\varepsilon}{Nr}\,\frac{d}{d\varepsilon}\Bigl[D_{\mu_j}G\bigl(\hat y_0,\mu(\hat y,\varepsilon),\varepsilon\bigr)\Bigr]=\frac{\sigma_j}r\,O(1).\tag{1.5}$$
Здесь $\partial_{\hat y_i}\partial_{\hat y_j}\Phi$ — семейство векторов
$\partial^2\Phi/\partial\hat y_i^\alpha\partial\hat y_j^\beta$. Производная по $\varepsilon$ в квадратных
скобках непрерывна по $(\hat y,\varepsilon)$, так как $G\in C^2$; поэтому она ограничена на
компакте. Формулы (1.1) и (1.5) проверены в sympy [Эксперимент, `check_symbolic.py`, (A6)].

*Норма.* $|\Phi(r,\hat y)|=r|\Gamma|$ и по (0.1) $\bigl||\Gamma|-1\bigr|\le C_\Gamma\varepsilon$. При
$r\le\rho_5:=\min\bigl(\rho_Q,(4C_\Gamma)^{-N}\bigr)$ и $\hat y\in\tilde K$
$$\tfrac34r\le|\Phi(r,\hat y)|\le\tfrac54r.\tag{1.6}$$
Кроме того, $|\partial_r\Phi|=O(1)$, поэтому $|r\partial_r\Phi|=O(r)$.

### Шаг 2. Доказательство предложения 1

**(а)** Первое утверждение — это (1.3)–(1.4). Пусть $\Phi$ инъективно на открытом множестве
$(0,\rho)\times\tilde K^\circ$, $\rho\le\rho_Q$. Там $\Phi\in C^2$ и $D\Phi$ обратим. По теореме об
обратной функции у каждой точки есть окрестность, которую $\Phi$ $C^2$-диффеоморфно отображает
на открытое множество. Поэтому $\Phi$ — открытое отображение, его образ открыт, а обратное
отображение (оно существует по инъективности) непрерывно. Локально оно совпадает с локальными
$C^2$-обратными, значит, оно класса $C^2$.

**(б)** Пусть $\omega$ инъективно на $\tilde K_0$.

1. *Равномерная инъективность $\omega$.* Для $\eta>0$ положим
   $m(\eta):=\min\{|\omega(a)-\omega(b)|:\ a,b\in\tilde K_0,\ |a-b|\ge\eta\}$ (минимум по пустому
   множеству равен $+\infty$). Множество пар компактно, функция непрерывна и положительна, поэтому
   $m(\eta)>0$. Значит, из $a,b\in\tilde K_0$ и $|\omega(a)-\omega(b)|<m(\eta)$ следует $|a-b|<\eta$.
2. *Выбор констант.* Пусть $\varpi$ — модуль непрерывности $Q_0$ на компакте
   $\{\hat y_0:\ \operatorname{dist}(\hat y_0,\tilde K_0)\le\delta/2\}$ и $\Theta:=(5/3)^{w_k}$.
   Выберем $\eta\in(0,\delta/2]$ с $\varpi(\eta)\le1/(4C_0\Theta^2)$, затем $\rho_\Phi\in(0,\rho_Q]$ с
   $$C_\Gamma\rho_\Phi^{1/N}\le\tfrac14,\qquad 4C_\Gamma\rho_\Phi^{1/N}<m(\eta),\qquad C_1\rho_\Phi^{1/N}\le\frac1{4C_0\Theta^2}.$$
3. Пусть $p=(r,\hat y)$, $p'=(r',\hat y')\in(0,\rho_\Phi)\times\tilde K$ и
   $\Phi(p)=\Phi(p')=:x$. Обозначим $\varepsilon=r^{1/N}$, $\varepsilon'=r'^{1/N}$.
   - (i) По (1.6) $\frac34r\le|x|\le\frac54r$ и так же для $r'$. Отсюда $r'/r\in[3/5,5/3]$.
   - (ii) $x/|x|=\Gamma/|\Gamma|$, где $\Gamma=\Gamma(\hat y,\varepsilon)$, и
     $\bigl|\Gamma/|\Gamma|-\omega(\hat y_0)\bigr|\le\bigl||\Gamma|-1\bigr|+|\Gamma-\omega(\hat y_0)|\le2C_\Gamma\varepsilon$
     по (0.1). То же верно для $p'$, поэтому
     $|\omega(\hat y_0)-\omega(\hat y'_0)|\le2C_\Gamma(\varepsilon+\varepsilon')<4C_\Gamma\rho_\Phi^{1/N}<m(\eta)$.
     По п. 1 $|\hat y_0-\hat y'_0|<\eta$.
   - (iii) *Отрезок.* Положим $p_\tau=p+\tau(p'-p)=(r_\tau,\hat y_\tau)$, $\tau\in[0,1]$. Тогда
     $r_\tau$ лежит между $r$ и $r'$, поэтому $r_\tau/r\in[3/5,5/3]$. Далее,
     $|\hat y_{0,\tau}-\hat y_0|<\eta\le\delta/2$ при $\hat y_0\in\tilde K_0$, а
     $|\hat y_{\ge1,\tau}|\le R_K$ по выпуклости шара. Значит, $\hat y_\tau\in\check K$ и
     $\varepsilon_\tau:=r_\tau^{1/N}<\varepsilon_Q$.
   - (iv) *Градуированная теорема о среднем.* Так как $\Phi\in C^1$ в окрестности отрезка,
     $$0=\Phi(p')-\Phi(p)=\int_0^1Q(\hat y_\tau,\varepsilon_\tau)S(r_\tau)\,d\tau\,(p'-p)=\mathcal M\,S(r)(p'-p),\qquad
     \mathcal M:=\int_0^1Q(\hat y_\tau,\varepsilon_\tau)\Lambda_\tau\,d\tau,$$
     где $\Lambda_\tau:=S(r_\tau)S(r)^{-1}=\operatorname{diag}\bigl(1,\ (r_\tau/r)I_s,\ (r_\tau/r)^{w_1}I_{c_1},\dots\bigr)$.
     Элементы $\Lambda_\tau$ лежат в $[\Theta^{-1},\Theta]$. Запишем
     $\mathcal M=Q_0(\hat y_0)\bar\Lambda+\mathcal E$, где $\bar\Lambda:=\int_0^1\Lambda_\tau d\tau$ —
     диагональная матрица с элементами из $[\Theta^{-1},\Theta]$, а
     $\mathcal E:=\int_0^1\bigl(Q(\hat y_\tau,\varepsilon_\tau)-Q_0(\hat y_0)\bigr)\Lambda_\tau d\tau$. По (1.2)
     и выбору $\eta$
     $$\|Q(\hat y_\tau,\varepsilon_\tau)-Q_0(\hat y_0)\|\le\|Q(\hat y_\tau,\varepsilon_\tau)-Q_0(\hat y_{0,\tau})\|+\|Q_0(\hat y_{0,\tau})-Q_0(\hat y_0)\|
     \le C_1\varepsilon_\tau+\varpi(\eta)\le\frac1{2C_0\Theta^2},$$
     откуда $\|\mathcal E\|\le1/(2C_0\Theta)$. Кроме того,
     $\|(Q_0\bar\Lambda)^{-1}\|\le\|\bar\Lambda^{-1}\|\,\|Q_0^{-1}\|\le\Theta C_0$. Значит,
     $\|(Q_0\bar\Lambda)^{-1}\mathcal E\|\le\frac12$, и матрица $\mathcal M$ обратима. Отсюда
     $S(r)(p'-p)=0$, то есть $p=p'$.

   Нигде не использовалась малость $R_K$: она входит только в константы $C_\Gamma$, $C_1$, $\varpi$,
   а значит, в $\rho_\Phi$.

**(в)** $G(\theta,\varepsilon)=(\cos\theta,\sin\theta)$ — класса $C^\infty$. Условие (O): $|\omega|=1$,
$D_\theta G=(-\sin\theta,\cos\theta)$ имеет ранг $1$ и ортогонален $\omega$, и
$\mathbb R\omega\oplus T_0=\mathbb R^2$. Но $\Phi(r,\theta)=r(\cos\theta,\sin\theta)$ и
$\Phi(r,\pi)=\Phi(r,3\pi)$, где $\pi,3\pi\in\tilde K^\circ=(0,4\pi)$, при каждом $r>0$. Нормальных
блоков нет, так что $\tilde K\subset\{\hat y_{\ge1}=0\}$, и никакое уменьшение $\rho$ или окрестности
не помогает. ∎

### Шаг 3. Построение $\hat W$ и формулы для него

Пусть $0<r<\rho_U$ и $\hat y\in\Omega_U$. На функциях от $(\hat y,\varepsilon)$, $\varepsilon=r^{1/N}$,
имеем $r\partial_r=\frac\varepsilon N\partial_\varepsilon$. Из (R):
$$\partial_{\hat y_j}U=r^d\bigl(\partial_{\hat y_j}F+r^e\partial_{\hat y_j}H\bigr),\qquad
r\partial_rU=r^d\bigl(dF+r^eH_1\bigr),\qquad U_+=r^{d+e}H_+,\tag{3.1}$$
$$H_1:=(d+e)H+\tfrac\varepsilon NH_\varepsilon,\qquad H_+:=eH+\tfrac\varepsilon NH_\varepsilon .$$
Так как $H\in C^2$, имеем $H_1,H_+\in C^1(\Omega_U\times(-\varepsilon_U,\varepsilon_U))$. Знаменатель
$\hat W$ равен
$$\mathrm{Den}=r^{2d}\bigl(D_J+\varepsilon^{Ne}\mathcal B\bigr),\qquad
\mathcal B:=[r\in J]\bigl(2dFH_1+\varepsilon^{Ne}H_1^2\bigr)+\sum_{j\in J\setminus\{r\}}\bigl(2\langle\partial_{\hat y_j}F,\partial_{\hat y_j}H\rangle+\varepsilon^{Ne}|\partial_{\hat y_j}H|^2\bigr),\tag{3.2}$$
и $\mathcal B$ непрерывна на $\Omega_U\times(-\varepsilon_U,\varepsilon_U)$. Где $\mathrm{Den}>0$,
подстановка (3.1) в определение даёт
$$\hat W=r^e\Bigl(Y_r\,r\partial_r+\sum_{j\in J\setminus\{r\}}\langle Y_j,\partial_{\hat y_j}\rangle\Bigr),\qquad
Y_r:=-[r\in J]\frac{\chi(F)H_+\,(dF+\varepsilon^{Ne}H_1)}{D_J+\varepsilon^{Ne}\mathcal B},\quad
Y_j:=-\frac{\chi(F)H_+\,(\partial_{\hat y_j}F+\varepsilon^{Ne}\partial_{\hat y_j}H)}{D_J+\varepsilon^{Ne}\mathcal B}.\tag{3.3}$$
Тождества (3.1)–(3.3) проверены в sympy для абстрактных $F$, $H$, $\chi$ и символьных $d,e,N$
[Эксперимент, `check_symbolic.py`, (A1)–(A3)].

*Окрестность носителя $\chi(F)$ и выбор $\varepsilon_1$.* Множество
$K_F:=\{\hat y\in K:\ |F(\hat y)|\le c_0\}$ компактно, и по (Reg) $D_J\ge c_0^2$ на $K_F$. Функция $D_J$
непрерывна на $\Omega_U$, поэтому открытое множество $\{\hat y\in\Omega_U:\ D_J(\hat y)>c_0^2/2\}$
содержит $K_F$. Выберем открытое $\mathcal V\supset K_F$ с компактным замыканием
$\bar{\mathcal V}\subset\{D_J>c_0^2/2\}$, например достаточно малую метрическую окрестность $K_F$.
Пусть $M_{\mathcal B}:=\max_{\bar{\mathcal V}\times[0,\varepsilon_U/2]}|\mathcal B|$. Выберем
$\varepsilon_1\in(0,\varepsilon_U/2]$ с $\varepsilon_1^{Ne}M_{\mathcal B}\le c_0^2/4$. Тогда
$$D_J+\varepsilon^{Ne}\mathcal B\ge c_0^2/4\quad\text{на }\bar{\mathcal V}\times[0,\varepsilon_1].\tag{3.4}$$
По непрерывности неравенство $D_J+\varepsilon^{Ne}\mathcal B>c_0^2/8$ выполнено на открытом множестве,
содержащем $\bar{\mathcal V}\times[0,\varepsilon_1]$. На нём правые части (3.3) — функции класса
$C^1$ от $(\hat y,\varepsilon)$: числители и знаменатель составлены из $\chi(F)$, $F$, $\partial F$,
$H$, $\partial H$, $H_\varepsilon$ и $\varepsilon^{Ne}$, а $F,H\in C^2$, $Ne\in\mathbb Z_{\ge1}$. Поэтому
$Y_b$ и их первые производные по $\hat y$ и $\varepsilon$ ограничены на компакте
$\bar{\mathcal V}\times[0,\varepsilon_1]$.

*Определение на $(0,\rho_3)\times K^\circ$, $\rho_3:=\min(\rho_U,\varepsilon_1^N)$.* Положим
$\mathcal Z:=\{\hat y\in\Omega_U:\ |F(\hat y)|>c_0\}$ — открытое множество, на котором
$\chi(F)\equiv0$. Так как $K=K_F\cup(K\setminus K_F)\subset\mathcal V\cup\mathcal Z$, открытые
множества $K^\circ\cap\mathcal V$ и $K^\circ\cap\mathcal Z$ покрывают $K^\circ$. На первом
$\mathrm{Den}>0$ по (3.4), и $\hat W$ задано формулой, то есть (3.3). На втором $\hat W:=0$, и
$Y_b:=0$. На пересечении обе формулы дают нуль. Значит, $\hat W$ корректно определено и класса $C^1$
на $(0,\rho_3)\times K^\circ$ (функция $r\mapsto r^{1/N}$ гладкая при $r>0$). Точки, где
$\chi(F)\ne0$, лежат в $\mathcal V$, то есть в области, где знаменатель положителен. Кроме того,
существует $M_W$ такое, что
$$|Y_b|,\ |\partial_{\hat y}Y_b|,\ |\partial_\varepsilon Y_b|\le M_W\quad\text{на }K^\circ\times(0,\varepsilon_1],\ b\in J.\tag{3.5}$$

### Шаг 4. Значение $A(U)$: пункт (c)

Для поля $\hat Z$ в координатах цепное правило даёт
$\langle Z^x,\nabla U\rangle\circ\Phi=D(U\circ\Phi)\,\hat Z=\hat Z(U\circ\Phi)$ (здесь нужно
$U\in C^1$). По определению $V(U)=dU+U_+$. На $\mathcal V$ числитель $\hat W$, применённый к $U$,
равен $\mathrm{Den}$, поэтому $\hat W(U)=-\chi(F)U_+$. На $\mathcal Z$ обе части равны нулю. Итак,
$$\hat A(U)=dU+(1-\chi(F))\,U_+\quad\text{на }(0,\rho_3)\times K^\circ\tag{4.1}$$
[Эксперимент, `check_symbolic.py`, (A3)–(A4)].

Пусть $M_H:=\max_{K\times[0,\varepsilon_1]}|H|$, $M_+:=\max_{K\times[0,\varepsilon_1]}|H_+|$ и
$\rho_4\in(0,\rho_3]$ таково, что $\rho_4^eM_H\le c_0/4$ и $\rho_4^eM_+\le dc_0/8$. Пусть
$0<r<\rho_4$, $\hat y\in K^\circ$ и $U=U(\Phi(r,\hat y))<0$.

- Если $\chi(F(\hat y))=1$, то $\hat A(U)=dU<\frac d2U$.
- Если $\chi(F(\hat y))<1$, то $|F|>c_0/2$. Из $U<0$ следует $F<-r^eH\le r^eM_H\le c_0/4$, значит
  $F<-c_0/2$. Тогда $U=r^d(F+r^eH)\le r^d(-c_0/2+c_0/4)=-r^dc_0/4$, то есть $|U|\ge r^dc_0/4$.
  Кроме того, $|(1-\chi)U_+|\le r^{d+e}M_+\le r^d\,dc_0/8\le\frac d2|U|$ (здесь $0\le1-\chi\le1$).
  Значит, $\hat A(U)\le dU+\frac d2|U|=\frac d2U$.

### Шаг 5. Формула (*) и поле $V$

Пусть $\hat Z$ — поле класса $C^1$ в координатах, а $\Phi$ — $C^2$-диффеоморфизм. Дифференцируя
$Z^x(\Phi(p))=D\Phi(p)\hat Z(p)$ по $p$, получаем
$$DZ^x\circ\Phi=\bigl(D^2\Phi[\hat Z,\cdot]+D\Phi\,D\hat Z\bigr)\,D\Phi^{-1},\tag{*}$$
где столбец $b$ матрицы $D^2\Phi[\hat Z,\cdot]$ равен $\sum_i\hat Z_i\,\partial_i\partial_b\Phi$.

Для $V$: $V^x(\Phi(p))=r\partial_r\Phi(p)$, и $DV^x\circ\Phi=D_p(r\partial_r\Phi)\,D\Phi^{-1}$ по цепному
правилу. Вычислим столбцы $D_p(r\partial_r\Phi)$ при $\hat y\in\tilde K$, $0<r<\rho_Q$.

- Столбец $r$: $\partial_r(r\partial_r\Phi)=\partial_r\Phi+r\partial_r^2\Phi$, причём
  $r\partial_r^2\Phi=\frac\varepsilon N\bigl(1+\frac1N\bigr)\Gamma_\varepsilon+\bigl(\frac\varepsilon N\bigr)^2\Gamma_{\varepsilon\varepsilon}=O(\varepsilon)$
  [Эксперимент, (A5)]. Здесь $\Gamma_\varepsilon$, $\Gamma_{\varepsilon\varepsilon}$ ограничены, так как
  $\Gamma\in C^2$ (шаг 0).
- Столбцы блока $j\in\{0,\dots,k\}$: $\partial_{\hat y_j}(r\partial_r\Phi)=r\partial_r(\partial_{\hat y_j}\Phi)=w_j\,\partial_{\hat y_j}\Phi+\sigma_j\,O(\varepsilon)$
  по (1.1), (1.5): $r\partial_r\sigma_j=w_j\sigma_j$, а второе слагаемое в (1.5), умноженное на $r$,
  есть $\sigma_j\frac\varepsilon N\cdot O(1)$.

Значит, $D_p(r\partial_r\Phi)=D\Phi\,\Lambda+E'S(r)$, где
$\Lambda:=\operatorname{diag}(1,I_s,w_1I_{c_1},\dots,w_kI_{c_k})$ и $\|E'\|=O(\varepsilon)$. Так как $S$
и $\Lambda$ диагональны и коммутируют,
$$DV^x=(QS\Lambda+E'S)S^{-1}Q^{-1}=Q\Lambda Q^{-1}+E'Q^{-1}.$$
По (1.2), (1.3)
$Q\Lambda Q^{-1}-Q_0\Lambda Q_0^{-1}=(Q-Q_0)\Lambda Q^{-1}+Q_0\Lambda(Q^{-1}-Q_0^{-1})=O(\varepsilon)$.

Наконец, $Q_0\Lambda Q_0^{-1}=L(\hat y_0)$. Действительно, пусть $v\in\mathbb R^n$ и $v=\sum_bv_b$ —
разложение по слагаемым $X_r=\mathbb R\omega$, $X_0=T_0$, $X_i=N_i$. Оно ортогонально по (O), поэтому
$v_b=P_{X_b}v$. Вектор $Q_0^{-1}v_b$ — координатный вектор с носителем в блоке $b$ ($Q_0$ взаимно
однозначно отображает координатные векторы блока $b$ на $X_b$). $\Lambda$ умножает его на $\lambda_b$,
где $\lambda_r=\lambda_0=1$, $\lambda_i=w_i$. Значит, $Q_0\Lambda Q_0^{-1}v=\sum_b\lambda_bP_{X_b}v$.
Итак,
$$\|DV^x-L(\hat y_0)\|\le C_V\,r^{1/N}\quad\text{на }\Phi\bigl((0,\rho_Q)\times\tilde K\bigr),\qquad |V^x|=O(r).\tag{5.1}$$
$L$ симметрична, её спектр лежит в $\{1,w_1,\dots,w_k\}\subset[1,w_k]$.

### Шаг 6. Радиальная часть $\hat W$

Если $r\notin J$, то $Y_r\equiv0$. Пусть $r\in J$, то есть $w_k-1<e$. Слагаемое
$\hat W_r:=r^eY_r\,V$ имеет евклидово представление $W_r^x=(r^eY_r)\,V^x$, где $r^eY_r$ понимается как
функция точки $x$. Поэтому
$$DW_r^x=r^eY_r\,DV^x+V^x\otimes\nabla_x(r^eY_r),\qquad \nabla_x(r^eY_r)\circ\Phi=D_p(r^eY_r)\,D\Phi^{-1}.$$
По (3.5) и (5.1) первое слагаемое — $O(r^e)$. Далее, по (3.5)
$\partial_r\bigl(r^eY_r(\hat y,r^{1/N})\bigr)=er^{e-1}Y_r+r^{e-1}\frac\varepsilon N\partial_\varepsilon Y_r=O(r^{e-1})$
и $\partial_{\hat y_b}(r^eY_r)=O(r^e)$. С учётом (1.4)
$$|\nabla_x(r^eY_r)|=O(r^{e-1})+\sum_bO(r^e/\sigma_b)=O(r^{e-w_k}),$$
так как при $r<1$ имеем $r^{e-1}\le r^{e-w_k}$ и $r^e/\sigma_b=r^{e-w_b}\le r^{e-w_k}$. Так как
$|V^x|=O(r)$, второе слагаемое — $O(r^{1+e-w_k})$. Показатели $e$ и $1+e-w_k=e+w_r-w_k$ не меньше
$\kappa$, поэтому $\|DW_r^x\|=O(r^\kappa)$.

### Шаг 7. Угловая и нормальные части $\hat W$

Пусть $\hat W_Y:=r^e\sum_{j\in J\setminus\{r\}}\langle Y_j,\partial_{\hat y_j}\rangle$ — поле без
$r$-компоненты. Применим (*).

**(a)** $D\Phi\,D\hat W_Y\,D\Phi^{-1}=Q\bigl(S\,D\hat W_Y\,S^{-1}\bigr)Q^{-1}$. В матрице $D\hat W_Y$
ненулевые только блочные строки $j\in J\setminus\{r\}$. Блок $(j,b)$ при $b\in\{0,\dots,k\}$ равен
$r^e\partial_{\hat y_b}Y_j=O(r^e)$, а блок $(j,r)$ равен
$\partial_r(r^eY_j)=O(r^{e-1})$ по (3.5). Сопряжение умножает блок $(j,b)$ на $\sigma_j/\sigma_b$, а
блок $(j,r)$ на $\sigma_j$. Получаем
$$(j,b):\ O(r^{e+w_j-w_b})\le O(r^{e+w_j-w_k}),\qquad (j,r):\ O(r^{e-1+w_j})\le O(r^e).$$
Оба порядка не хуже $O(r^\kappa)$, так как $j\in J$ и $w_j\ge1$. Матрицы $Q$, $Q^{-1}$ ограничены
по (1.3).

**(b)** Столбец $b\in\{0,\dots,k\}$ матрицы $D^2\Phi[\hat W_Y,\cdot]$ равен
$\sum_jr^e\langle Y_j,\partial_{\hat y_j}\rangle\partial_{\hat y_b}\Phi=O(r^e\sigma_j\sigma_b/r)$ по
(1.5). Столбец $r$ равен $O(r^e\sigma_j/r)$. При умножении справа на $D\Phi^{-1}$ столбец $b$
умножается на строки блока $b$ порядка $O(1/\sigma_b)$, а столбец $r$ — на строку порядка $O(1)$
(1.4). Получаем $O(r^{e+w_j-1})\le O(r^e)\le O(r^\kappa)$.

Итак, $\|DW_Y^x\|=O(r^\kappa)$.

### Шаг 8. Итог: пункты (a), (b), (d), (e), (f) и выбор $\rho'$

По шагам 5–7 на $\Phi\bigl((0,\rho_3)\times K^\circ\bigr)$, с учётом $\kappa\le1/N$,
$$\|DA-L(\hat y_0)\|\le\|DV^x-L\|+\|DW_r^x\|+\|DW_Y^x\|\le K_8\,r^\kappa .$$
Положим
$$\rho':=\min\Bigl(\rho_\Phi,\ \rho_Q,\ \rho_3,\ \rho_4,\ \rho_5,\ (2K_8)^{-1/\kappa},\ \tfrac12\Bigr).$$
Для симметричной $L\succeq I$ и любой матрицы $M$ имеем
$\operatorname{sym}(L+M)\succeq(1-\|M\|)I$, откуда $\operatorname{sym}DA\succeq(1-K_8r^\kappa)I\succeq\frac12I$.
Это (d).

Далее, $W^x=QS(r)\hat W$. Компоненты $S(r)\hat W$: радиальная $r^eY_r\cdot r$, блока $j$ —
$\sigma_jr^eY_j$. Так как $\sigma_j\le r$ при $r<1$, имеем $|W^x|=O(r^{1+e})$. Вместе с
$|V^x|=O(r)$ и (1.6) получаем $|A(x)|\le Cr\le\frac43C|x|$. Это (e).

(a): по предложению 1(а), так как $\rho'\le\min(\rho_\Phi,\rho_Q)$, а оценка нормы — (1.6).
Множество $\mathcal O$ открыто как образ открытого множества при диффеоморфизме.

(b): $\hat W\in C^1$ (шаг 3), $V=r\partial_r$ гладкое. $A=(D\Phi\cdot\hat A)\circ\Phi^{-1}$, где
$D\Phi\in C^1$, $\hat A\in C^1$, $\Phi^{-1}\in C^2$. Значит, $A\in C^1(\mathcal O)$.

(c): это (4.1) и шаг 4 (по $\rho'\le\rho_4$).

(f): оценки (5.1), $|V^x|=O(r)$, $|W^x|=O(r^{1+e})$, $\|DW^x\|=O(r^\kappa)$ из шагов 6–7, оценка (1.4)
для строк блока $0$ и равенство $\hat W(U)=-\chi(F)U_+$ из шага 4. В качестве $C_A$ берём максимум
всех констант. ∎

### Шаг 9. Доказательство следствия 2

Применим лемму 1 результата [001](001-field-criterion.md) к шару $B_{\rho''}$, открытому
множеству $\mathcal O\supset X$, полю $A$ класса $C^1$ на $\mathcal O$ и $p=d/2$. По лемме R(d)
$\operatorname{sym}DA\succeq\frac12I\succeq0$ на $X$. По лемме R(c)
$\langle A,\nabla U\rangle\le\frac d2U$ на $X\subset\mathcal O\cap\{U<0\}$. По лемме R(e)
$|A(x)|\le C_A|x|<C_A\rho''=:M$ на $X$. Гладкость $U\in C^2$ около $\bar B_{\rho''}$ и $U(0)=0$ даны
в (i). Лемма 1 даёт оценку $t_2-t_1\le2w(E)M/(p|E|)=4C_A\rho''w(E)/(d|E|)$. Неустойчивость по
Ляпунову, если $0$ не локальный минимум, — следствие 4 результата 001. ∎

### Шаг 10. Доказательство предложения 3 и следствия 4

Пусть $\rho_{**}\in(0,\rho_*]$ будет выбрано ниже и
$\mathcal O_\alpha^{**}:=\Phi_\alpha((0,\rho_{**})\times K_\alpha^\circ)$. Пусть
$x\in\mathcal O_\alpha^*\cap\mathcal O_\beta^*$, $x=\Phi_\alpha(r,\hat y)=\Phi_\beta(r',\hat y')$. По (C1)
$r=r'$ и $\Phi_\alpha(t,\hat y)=\Phi_\beta(t,\hat y')$ при $t\in(0,\rho_*)$. Отсюда:

1. *$V^x$ не зависит от карты.* Дифференцируя по $t$ при $t=r$, получаем
   $V_\alpha^x(x)=r\partial_t\Phi_\alpha(t,\hat y)|_{t=r}=r\partial_t\Phi_\beta(t,\hat y')|_{t=r}=V_\beta^x(x)$.
   Поэтому $V^x$ — корректно определённое поле класса $C^1$ на $\mathcal O^*$ (оно $C^1$ на
   каждом открытом $\mathcal O_\alpha^*$). Функция $r(x)$ тоже корректно определена. Кроме того,
   $\mathcal O_\alpha^*\cap\mathcal O^{**}=\mathcal O_\alpha^{**}$: если $x=\Phi_\alpha(r,\hat y)$ с $r<\rho_*$ и
   $x\in\mathcal O_\beta^{**}$, то $r<\rho_{**}$.
2. *$F$ не зависит от карты.* По (R) для обеих карт при малых $t>0$
   $F_\alpha(\hat y)+t^{e_\alpha}H_\alpha(\hat y,t^{1/N_\alpha})=F_\beta(\hat y')+t^{e_\beta}H_\beta(\hat y',t^{1/N_\beta})$.
   Функции $H_\alpha(\hat y,\cdot)$ и $H_\beta(\hat y',\cdot)$ непрерывны в $0$, а значит,
   ограничены около $0$. При $t\to0$ получаем $F_\alpha(\hat y)=F_\beta(\hat y')$. Поэтому
   $F(x)$, $\chi(F(x))$ и $U_+=\langle V^x,\nabla U\rangle-dU$ — функции точки $x$, не зависящие от
   карты.
3. *Гладкость.* Пусть $Z_\alpha$ — замыкание $\{\varphi_\alpha\ne0\}$ в $\mathcal O^*$. По (C2)
   $Z_\alpha\subset\mathcal O_\alpha^*$, и $\mathcal O^*=\mathcal O_\alpha^*\cup(\mathcal O^*\setminus Z_\alpha)$
   — объединение двух открытых множеств. На первом $\varphi_\alpha W_\alpha^x$ — произведение
   $C^1$-функций, на втором оно равно нулю. Значит, $\varphi_\alpha W_\alpha^x\in C^1(\mathcal O^*)$ и
   $A\in C^1(\mathcal O^*)$.
4. *$A(U)$.* В точке $x\in\mathcal O^*$ для каждого $\alpha$ с $x\in\mathcal O_\alpha^*$ по лемме R(f)
   $\langle W_\alpha^x,\nabla U\rangle(x)=-\chi(F(x))U_+(x)$, а при $x\notin\mathcal O_\alpha^*$
   имеем $\varphi_\alpha(x)=0$. Так как $\sum\varphi_\alpha=1$,
   $$\langle A,\nabla U\rangle=dU+U_+-\chi(F)U_+\sum_\alpha\varphi_\alpha=dU+(1-\chi(F))U_+ .$$
   Возьмём любое $\alpha$ с $x\in\mathcal O_\alpha^*$. Правая часть равна
   $\langle V^x+W_\alpha^x,\nabla U\rangle(x)$, и по лемме R(c) для карты $\alpha$ она не больше
   $\frac d2U(x)$, если $U(x)<0$.
5. *$DA$.* Пусть $x\in\mathcal O^{**}$. Если $x\notin\mathcal O_\alpha^*$, то $x\notin Z_\alpha$, и
   $\varphi_\alpha W_\alpha^x\equiv0$ около $x$. Поэтому
   $$DA=DV^x+\sum_{\alpha:\ x\in\mathcal O_\alpha^*}\bigl(\varphi_\alpha DW_\alpha^x+W_\alpha^x\otimes\nabla\varphi_\alpha\bigr).$$
   Возьмём $\beta$ с $x\in\mathcal O_\beta^*$. По лемме R(f) для карты $\beta$
   $\|DV^x-L_\beta\|\le C_{A,\beta}r^{1/N_\beta}$, и $\operatorname{sym}DV^x\succeq(1-C_{A,\beta}r^{1/N_\beta})I$.
   Далее, $\|\varphi_\alpha DW_\alpha^x\|\le C_{A,\alpha}r^{\kappa_\alpha}$. На $\mathcal O_\alpha^*$
   $$\nabla\varphi_\alpha(x)=D_p(\varphi_\alpha\circ\Phi_\alpha)\,D\Phi_\alpha^{-1}=\bigl(0,\ D\psi_\alpha(\hat y_0),\ 0,\dots,0\bigr)D\Phi_\alpha^{-1},$$
   то есть $D\psi_\alpha$, умноженное на строки блока $0$ матрицы $D\Phi_\alpha^{-1}$. По (C2) и
   лемме R(f) $|\nabla\varphi_\alpha|\le L_\psi C_{A,\alpha}/r$. Вместе с
   $|W_\alpha^x|\le C_{A,\alpha}r^{1+e_\alpha}$ получаем
   $\|W_\alpha^x\otimes\nabla\varphi_\alpha\|\le L_\psi C_{A,\alpha}^2r^{e_\alpha}$. Пусть
   $\kappa_*:=\min_\alpha\min(\kappa_\alpha,e_\alpha,1/N_\alpha)>0$. Тогда при $r<1$
   $\operatorname{sym}DA\succeq(1-C_\Sigma r^{\kappa_*})I$ с константой $C_\Sigma$, не зависящей от $x$.
   Возьмём $\rho_{**}\le\min(\rho_*,1)$ с $C_\Sigma\rho_{**}^{\kappa_*}\le\frac12$.
6. *$|A|$.* $|A|\le|V^x|+\sum_\alpha|W_\alpha^x|\le Cr\le\frac43C|x|$ по лемме R(a), (f).

Следствие 4 получается из пп. 4–6 и леммы 1 результата 001 так же, как в шаге 9, с
$\mathcal O^{**}$ вместо $\mathcal O$. ∎

## Где работает аналитичность или изолированность

- **Нигде.** Лемма R, предложения 1 и 3 — утверждения о данных класса $C^2$: $G\in C^2$,
  $F,H\in C^2$, $U\in C^1$. В следствиях 2 и 4 добавляется $U\in C^2$ около $\bar B_{\rho''}$, чтобы
  работала лемма 1 результата 001. Изолированность критической точки не используется.
- Поэтому лемма R не различает аналитический и $C^\infty$ случаи. Для задачи (A) она сама по себе
  ничего не даёт. Вся трудность переходит в **построение карт**:
  1. разложение (R) с $F$, не зависящей от $\varepsilon$, и $H$ класса $C^2$ вплоть до
     $\varepsilon=0$;
  2. (Reg) на $K$;
  3. покрытие $\{U<0\}\cap B_{\rho''}$ множеством $\mathcal O$ или $\mathcal O^{**}$;
  4. при нескольких картах — общая радиальная структура (C1) и разбиение единицы по углу (C2).

  Именно здесь аналитичность (или конечная определённость) должна работать в доказательстве (A).
  Для плоского в нуле $U$ (тип Пенлеве–Уинтнера) $r^{-d}U\circ\Phi\to0$ при любом $d$, то есть
  $F\equiv0$. Тогда при $\hat y\in K\ne\varnothing$ выполнено $|F|=0\le c_0$ и $D_J=0<c_0^2$, и (Reg)
  нарушено. [Доказано: это прямая проверка.]
- Из заключения (c) следует, что в $\mathcal O\cap\{U<0\}$ нет критических точек $U$: там
  $\langle A,\nabla U\rangle\le\frac d2U<0$. Значит, условия следствий 2 и 4 исключают критические
  точки с отрицательным значением около $0$. Для аналитического $U$ таких точек около $0$ и нет
  (001, замечание 1). Для гладкого $U$ с такими точками условия следствий выполниться не могут.
- Пример Уреньи с леммой не сверялся: точной формулы потенциала под рукой нет (так же у R4).

## Замечания

**1. Ослабления условий** (из отзыва R4; доказательство их не использует).

- В (O) достаточно ортогональности подпространств *разных* весов. Если $\mathbb R\omega\oplus T_0$,
  $N_1,\dots,N_k$ попарно ортогональны, то шаг 5 проходит без изменений:
  $Q_0\Lambda Q_0^{-1}=P_{\mathbb R\omega\oplus T_0}+\sum_iw_iP_{N_i}$. Впрочем, $\omega\perp T_0$
  во внутренних точках $\tilde K_0$ выполнено автоматически: достаточно продифференцировать
  $|\omega|^2\equiv1$.
- $J$ — любое подмножество $J_{\max}$. Больше $J$ — слабее (Reg), так что выгоднее всего
  $J=J_{\max}$.
- Условие $0\le\chi\le1$ не обязательно: в шаге 4 достаточно $\|1-\chi\|_\infty<\infty$, это
  поглощается выбором $\rho_4$.
- Достаточно, чтобы $H$ была класса $C^2$ на $\Omega_U\times(0,\varepsilon_U)$ и её производные до
  второго порядка непрерывно продолжались на $\varepsilon=0$: используются лишь оценки на
  компактах вида $K\times[0,\varepsilon_1]$. В тексте для простоты взята открытая область по
  $\varepsilon$.

**2. Проверка на случаях с известным ответом.**

- **(а) Невырожденная младшая форма** [Эскиз]. Пусть $U\in C^{m+3}$ около $0$, $m\ge2$,
  $U=u_m+O(|x|^{m+1})$ и $\nabla u_m(x)\ne0$ при $x\ne0$. Карты: конечный атлас
  $\omega_\alpha\colon\Theta_\alpha\to S^{n-1}$, $\Phi_\alpha(r,\theta)=r\omega_\alpha(\theta)$; $s=n-1$,
  $k=0$, $N=1$, $d=m$, $e=1$, $F_\alpha=u_m\circ\omega_\alpha$. Функцию
  $H_\alpha(\theta,\varepsilon)=\sum_{|\beta|=m+1}\omega_\alpha^\beta g_\beta(\varepsilon\omega_\alpha)$ дают
  формула Тейлора с интегральным остатком, $g_\beta\in C^2$. Далее $J=J_{\max}=\{r,0\}$, и (Reg)
  следует из $|\nabla u_m|^2=m^2u_m^2+|\nabla_Su_m|^2$ на сфере и сравнимости метрик. (C1): общий
  полярный радиус. (C2): разбиение единицы на $S^{n-1}$. Покрытие: $\mathcal O^{**}=B_{\rho_{**}}\setminus0$.
  Следствие 4 даёт тотальную неустойчивость. Это согласуется с примером 5 результата 001, где тот
  же вывод получен прямо при $U\in C^{m+1}$. Пробел: регулярность $H_\alpha$ и сравнение метрик
  не выписаны. Численный аналог при $n=2$ с двумя картами — `check_gluing.py` (ниже).
- **(б) Квазиоднородный пример $U=y^2+x^3$, $n=2$** [Доказано: прямая проверка]. Карта для
  $x<0$: $s=0$, $k=1$, $c_1=1$, $w_1=3/2$, $N=2$, $a_1=1$, $G(\mu,\varepsilon)=(-1,\mu)$, то есть
  $\Phi(r,\hat y_1)=(-r,\ r^{3/2}\hat y_1)$. (O): $\omega=(-1,0)$, $N_1=\mathbb R(0,1)$. Далее
  $U\circ\Phi=r^3(\hat y_1^2-1)$, то есть $F=\hat y_1^2-1$, $H\equiv0$, $d=3$; возьмём $e=1$. Тогда
  $J_{\max}=\{r,1\}$ и $D_J=9(\hat y_1^2-1)^2+4\hat y_1^2\ge32/9$, так что (Reg) выполнено при
  $c_0=1$. Здесь $U_+=0$, $\hat W=0$, $A=V^x=(x,\frac32y)$, $DA=\operatorname{diag}(1,\frac32)=P_\omega+\frac32P_{N_1}$
  и $\langle A,\nabla U\rangle=3U$. Покрытие: $\{U<0\}=\{x<0,\ |y|<|x|^{3/2}\}=\Phi((0,\infty)\times(-1,1))$,
  $K=[-1,1]$, $\tilde K=[-2,2]$. Следствие 2 даёт тотальную неустойчивость с шаром $B_{\rho''}$
  при $\rho''\le\rho'$. Здесь равенства $A=(x,\frac32y)$ и $\langle A,\nabla U\rangle=3U$ точны при
  всех $r$, так что годится и любой шар. Это согласуется с известным для $n=2$ и с замечанием 2 к
  теореме B в 002, где $A=V/3$ (там нормировка $p=1$).
- **(в) Однородный $U=u_m$.** В полярных картах $H\equiv0$, $U_+=0$, $A=V^x=x$,
  $\langle A,\nabla U\rangle=mU$, $DA=I$. Заключение леммы верно и без (Reg); оно может нарушаться,
  если у $u_m|_{S^{n-1}}$ есть вырожденные нули, но тогда лемма 1 из 001 применима к $A=x$
  напрямую. Если $u_m\ge0$, то $\{U<0\}=\varnothing$ и $0$ — нестрогий минимум: тотальная
  неустойчивость пуста, неустойчивость по Ляпунову не утверждается. Противоречия нет.
- **(г) $n=2$.** Лемма от $n$ не зависит. Тотальная неустойчивость при $n=2$ для любого
  аналитического $U$ приписывается Паламодову 1977 (не сверено с первоисточником). Лемма R этого
  не воспроизводит: нужны режимы, покрывающие $\{U<0\}$, и их склейка.
- **(д) Пенлеве–Уинтнер** (плоский $U$): $F\equiv0$, (Reg) нарушено (см. раздел про
  аналитичность). Противоречия с устойчивостью в этом примере нет.

**3. Связь с теоремой B** ([002](002-theorem-B.md)).

- **(а)** Оценки §5 теоремы B — частный случай оценок шагов 5–7: $N=2$, $w_1=3/2$, $a_1=1$,
  $d=m+1$, $e=1$, $J=J_{\max}$ (все блоки и $r$, так как $3/2-1<1$),
  $G(\theta,\mu,\varepsilon)=\omega(\theta)+\nu\bigl(\omega(\theta),\ \sum_i\mu_ie_i(\theta)-\varepsilon^2\eta(\omega(\theta))\bigr)$.
  Это проверил R4 (замечание 7 отзыва). Поле теоремы B другое: без $\chi$, с нормировкой
  $p=1$. Но оно имеет тот же вид $r^e(Y_r\,r\partial_r+\sum_j\langle Y_j,\partial_j\rangle)$ с
  $C^1$-коэффициентами, и оценки шагов 6–7 переносятся на него дословно.
- **(б)** [Эскиз] Утверждение (a) теоремы B получается и из леммы R, предложения 3 и следствия 4.
  Карты $\alpha$ — сужения одного глобального $\Phi(r,\ell)=r\Gamma(\ell,r^{1/2})$ из §2.6 работы 002
  на картах $(\theta,a)$ атласа $\Sigma$ с рамками. Переходы $(r,\theta,a)\mapsto(r,\theta',g(\theta)a)$
  не меняют $r$, и $\Phi$ глобально инъективно, поэтому (C1) выполнено. Для (C2) годится
  $\varphi_\alpha(x)=\psi_\alpha(\omega(x))$, где $\psi_\alpha$ — разбиение единицы на $\Sigma$,
  подчинённое $\{\omega_\alpha(\Theta_\alpha)\}$. (Reg) следует из леммы 4 работы 002 со сравнением
  индуцированной метрики и евклидовой метрики карты на компакте. Покрытие $X$ даёт лемма 3 работы
  002. Не выписаны: выбор $\tilde K_\alpha\supset K_\alpha$ и проверка (C2) по шагам. Теорема B в
  002 доказана прямо, так что это лишь согласованность.
- **(в)** Без сдвига $\eta$ (п. 2 §5 исходного текста; замечание 8 R4) имеем $e=1/2$ и
  $J=\{\text{нормальный блок}\}$. (Reg) нарушается в точках $\hat\nu=0$, $g(\omega)=0$, а исключить
  их из $K$ нельзя: рядом есть точки с $U<0$. Слова исходного текста «нужен подрежим и лемма о
  склейке» — план, а не доказанное утверждение.

**4. О склейке.** (C1) — главное условие предложения 3. Оно гарантирует, что $V^x$ одно и то же
во всех картах. Без него в $DA$ появился бы член $(V_\alpha^x-V_\beta^x)\otimes\nabla\varphi_\alpha$
порядка $O(r)\cdot O(1/r)=O(1)$, который может испортить $\operatorname{sym}DA\succeq0$ (ср. 001,
замечание 3, и разбор леммы 2.2 Burgos в `orchestrator/AUDIT.md`, A-301). Условия R4 о сохранении
блоков и линейности переходов по $\hat y_{\ge1}$ в доказательстве не используются. Они лишь
удобный способ построить разбиение единицы из (C2). Склейка **разных** режимов (разные веса или
разная радиальная структура) предложением 3 не покрывается. Ср. лемму G и гипотезу П в
`notes/vlad-claude/toolkit.md`, которые по отзыву R7 (`notes/reviewer/2026-10-21-sketches.md`)
имеют пробелы.

**5. Эксперименты** [Эксперимент; подкрепляют, но не доказывают].
Скрипты: `experiments/prover/lemmaR/`, выводы — в `out_*.txt` там же.

- `check_symbolic.py` (sympy, точные тождества при абстрактных $F$, $H$, $\chi$ и символьных
  $d,e,N$). Проверены: (3.1), (3.2) и (3.3) для $J=\{r,0,1\}$ и $J=\{1\}$; $\hat W(U)=-\chi U_+$;
  (4.1); формула для $r\partial_r^2\Phi$ (шаг 5); (1.1) и (1.5) для $\partial_{\hat y_1}\Phi$ и
  $\partial_r\partial_{\hat y_1}\Phi$ при $N=2,3$, $a=1,2,3$ (на конкретной нелинейной $G$). Все
  тесты прошли.
- `check_injectivity.py` (numpy и scipy, seed 20261021). Предложение 1(б) на карте с $n=3$,
  $s=1$, $w_1=3/2$, нелинейной $G$ и широким $\tilde K=[-1,1]\times[-4,4]$. Минимум отношения
  $|\Phi(p')-\Phi(p)|/|S(r)(p'-p)|$ по 200 000 парам с доводкой Нелдера–Мида равен $0.406$ при
  $r=10^{-2}$ и $0.624$–$0.626$ при $r=10^{-3}\dots10^{-6}$, то есть отделён от нуля. При $r=10^{-1}$ он
  стремится к $0$: при таком $r$ и $|\hat y_1|\le4$ карта вырождается. Это иллюстрирует, что
  $\rho_\Phi$ зависит от $R_K$.
- `check_gluing.py` (mpmath, 60 знаков, центральные разности). Предложение 3 на примере $n=2$,
  $U=x^3-3xy^2+(x^2+y^2)^2+xy^3$ с двумя полярными картами с разными угловыми параметризациями
  ($W_1\ne W_2$ на перекрытии: $|W_1-W_2|/r^2\approx0.029$). При $r=10^{-2}\dots10^{-8}$:
  $\lambda_{\min}(\operatorname{sym}DA)=0.920,\ 0.99921,\ 0.9999921,\ 0.99999992$;
  $\|DA-I\|/r\approx10.1$; $|A|/r\to1$; $\min_{U<0}A(U)/U\to3\ge d/2$; тождество
  $A(U)=dU+(1-\chi)U_+$ выполнено с точностью $10^{-60}r^3$. Добавочный член склейки
  $\|(W_1-W_2)\otimes\nabla\varphi_1\|/r\approx0.069$ стабилен, то есть он ровно порядка $r^e=r$.
- Рецензент R4: `experiments/reviewer/lemmaR/check_lemmaR.py` — построение поля в одной карте
  при $n=4$ с нелинейной $G$, в том числе контроль чувствительности при нарушении условия на $J$
  (отзыв R4, раздел «Эксперимент»).

## Пробелы

- В доказательствах леммы R, предложений 1 и 3 и следствий 2 и 4 пробелов не известно.
- Предложение 1(б), предложение 3, следствие 4 и формулировка пункта (f) леммы R добавлены при
  исправлении. R4 их не читал, и они требуют независимой проверки вместе со всем текстом.
- Теорема об обратной функции класса $C^2$ используется как стандартный факт, без ссылки на номер
  в учебнике.
- Вне доказательства: замечания 2(а) и 3(б) — [Эскиз]; что именно не выписано, сказано там же.

## Отличия от исходного текста

Математика леммы (построение поля и оценки) не менялась. Изменения:

1. **Условие (Φ)** (замечание 1 R4). Формулировка «$C^2$-диффеоморфизм $(0,\rho)\times\tilde K$ на
   открытое множество» некорректна, так как $\tilde K$ компактно. Теперь (Φ) — явное требование
   инъективности на $(0,\rho_\Phi)\times\tilde K^\circ$. Свойство диффеоморфизма на открытое
   множество выведено из него (предложение 1(а)). Неверная фраза «этого можно добиться, уменьшив
   $\rho$, когда $\tilde K$ лежит в достаточно малой окрестности $\{\hat y_{\ge1}=0\}$» удалена.
   Вместо неё доказана верная форма (предложение 1(б): достаточно инъективности $\omega$ на
   $\tilde K_0$, малость окрестности не нужна) и приведён контрпример к исходной фразе
   (предложение 1(в)).
2. **Гладкость $G$** (замечание 2 R4). $C^3$ заменено на $C^2$. Проверено: третьи производные $G$
   нигде не нужны. Используются $Q\in C^1$, ограниченность $D^2\Phi$, $\Gamma_{\varepsilon\varepsilon}$
   и $\frac d{d\varepsilon}D_{\mu_j}G$ на компактах, а для $A\in C^1$ — что $D\Phi\in C^1$.
   Явно описаны области: условие на $\mathcal D$, построение $\Omega_G$, $\varepsilon_G$ (шаг 0) и
   область, где верно разложение (R) (Д5).
3. **Шаг 1** исходного текста (замечание 3 R4). Положительность знаменателя доказана в
   окрестности $\mathcal V$ множества $\{|F|\le c_0\}\cap K$, а не только на носителе $\chi(F)$.
   Явно выбрано $\varepsilon_1$ вместо $\varepsilon_0$. Выписано определение $\hat W$ двумя формулами
   на открытом покрытии $K^\circ$, откуда класс $C^1$.
4. **Шаг 2** исходного текста (замечание 4 R4). Условие $0\le\chi\le1$ оговорено. Константы
   уточнены: $F<-c_0/2$, $|U|\ge c_0r^d/4$ вместо $F\le-c_0/4$, $|U|\ge c_0r^d/8$; обе версии верны.
5. **Описка про масштаб радиального блока** (замечание 5 R4) исправлена: радиальной координате
   отвечает масштаб $1$ в $S(r)$.
6. **Скобка после §2** (замечание 6 R4). Она заменена следствием 2 с точными условиями: $U\in C^2$
   около $\bar B_{\rho''}$, $U(0)=0$, $X\subset\mathcal O$. Лишнее условие «$K^{\circ\prime}$ отделено
   от края $K$» убрано.
7. **Несколько карт при $s\ge1$** (замечание 6 R4). Набросок R4 доказан в виде предложения 3 и
   следствия 4 при явных условиях (C1), (C2). Для этого в лемму R добавлен пункт (f) с оценками,
   которые уже были получены в её доказательстве.
8. **§5 исходного текста** (замечания 7–9 R4). «Теорема B — частный случай» отнесено к оценкам
   (замечание 3(а)). Вывод теоремы B через предложение 3 помечен [Эскиз]. П. 2 §5 помечен как
   план. Ссылки на непроверенные `toolkit.md`, лемму G и гипотезу П вынесены в замечание 4 с
   пометкой о пробелах (R7).
9. **Аналитичность** (замечание 10 R4). Добавлен раздел «Где работает аналитичность или
   изолированность».
10. **Обозначения.** Коэффициент радиальной части поля (в исходном тексте $c$, совпадало с
    размерностями блоков $c_i$) переименован в $Y_r$. Функция $P=eH+\varepsilon H_\varepsilon/N$
    (совпадала с обозначением проекторов) переименована в $H_+$. Масштабы $s_i$ (совпадали с
    размерностью $s$ углового блока) переименованы в $\sigma_i$. Порядки $o(1)$ заменены явной
    скоростью $r^\kappa$.

## Найденные проблемы

Ошибок в математике исходного текста не найдено, R4 тоже их не нашёл. Кроме недочётов, отмеченных
R4 и исправленных выше, найдено следующее (тоже исправлено):

1. В исходном тексте не указаны область определения $U$ и область, где верно разложение (R).
   Условие «$H\in C^2$ на $\tilde K\times[0,\varepsilon_0]$» не определяет производных на границе
   $\varepsilon=0$. Исправлено в (Д5); вариант с односторонней гладкостью — замечание 1.
2. Заключение исходной леммы (пункты 1–3) недостаточно для склейки по картам, предложенной R4:
   нужны оценки $|W^x|=O(r^{1+e})$, $\|DW^x\|=O(r^\kappa)$, формула $W(U)=-\chi(F)U_+$ и оценка
   строк блока $0$ матрицы $D\Phi^{-1}$. Они были в доказательстве, но не в формулировке.
   Добавлено как пункт (f).
3. В наброске склейки R4 предполагались сохранение блоков и линейность переходов по $\hat y_{\ge1}$.
   Это не нужно. Нужны общая радиальная структура (C1) и разбиение единицы, зависящее в каждой
   карте только от её угловой координаты (C2). Существование такого разбиения — содержательное
   условие на семейство карт.
4. В исходном §5 (Reg) для теоремы B отождествлено с леммой 4 работы 002. Там градиент берётся в
   индуцированной метрике на $L_C$, а в (Reg) — в евклидовой метрике карты. Нужна сравнимость
   метрик на компакте. Это тривиально, но не сказано.
