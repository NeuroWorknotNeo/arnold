# Морс–Ботт при $n=3$: асимптотическая траектория вне класса $\mathcal K$ (случаи (b), (c), (d))

- **Автор:** prover (агент), 21.10.2026. Задание главного агента: доказать существование
  асимптотической траектории (и тем самым (A)) при $n=3$ для всех аналитических $U$ жёсткого ядра,
  у которых $\Sigma$ — многообразие Морса–Ботта, закрыв случаи (b), (c), (d) из §10.2 записки P9.
- **Опирается на:**
  - [007] = `results/007-gt3.md`: теорема A, лемма 1, лемма 2, теорема 2
    [Проверено: R16, R17, 21.10.2026];
  - [008] = `results/008-class-K.md` [Проверено: R20–R24, 21.10.2026]: данные (S) и определения
    $R,g_k,j,G,\hat G$ (раздел «Данные (S) и редуцированная функция», §3.2), (U1), (1.1), лемма K1
    (§2), лемма K2 (§3, формулы (3.1), (3.2)), лемма K3 (§6, формулы (6.1), (6.2), (6.4); там же
    сказано, что она верна для замкнутой кривой с периодическим $\theta$), теорема K0 (доказательство —
    §4), предложение K4 (a), (c) и следствие K4′ (доказательство — §11). В [008] обозначения
    другие: $T\to\ell$, $k\to k_g$, $\varepsilon\to\epsilon$, $P\to\Pi$, нормальная компонента $Y$: $\psi\to\nu$.
    Здесь сохранены обозначения первой редакции записки. Первоисточник [008] — записка P9
    (`notes/prover/2026-10-21-gt3-hardcore.md`); в первой редакции этой записки ссылки шли на её
    нумерацию.
  - [002] = `results/002-theorem-B.md`, §2.1(f), §2.2 (аналитичность $\Sigma$; используется через [008]);
  - литература: подготовительная теорема Вейерштрасса и теорема Ньютона–Пюизё (только в лемме V).
  - **Теорема 2′ и теорема K2 [008] здесь не используются**: случай (a) передоказан (теорема Mb при
    $p=1$).
- **Проверка:** первую редакцию прочитали рецензенты R26 (§6,
  `notes/reviewer/2026-10-21-morse-bott-Mb.md`), R27 (§5, `...-Md.md`), R28 (§1–§4, §7–§8,
  `...-M.md`): ошибок нет. Эта редакция учитывает их замечания (перечень — §12). Главное изменение
  (З1 R28): **изолированность не нужна**, теорема M доказана при условии «$0$ — не точка локального
  минимума».
- **Скрипты** [Эксперимент]: `experiments/prover/morse-bott/` (список и выводы — §9.4).

## 0. Итог

| № | Утверждение | Статус |
|---|---|---|
| Лемма N | Нормальная форма и трубка вдоль **всей** замкнутой компоненты $\Sigma_0$ (периодический вариант лемм K1–K3 [008]) | [Доказано] (сведение к [008]) |
| Предложение R | Полнота разбора: если $0$ не локальный минимум, то реализуется (P) точечная компонента с отрицательным старшим коэффициентом, или на кривой-компоненте (a/b), (c) или (d) | [Доказано] |
| Лемма M | Вариант леммы 2 [007]: перекрёстные члены $T_1,T_2$ с постоянными оценками гасятся через $\beta K_\perp$, а для $T_3$ достаточно $2\vartheta_3<\beta-\mu$ | [Доказано] (новое) |
| Теорема Mb | Случаи (a)+(b): у $G$ строгий локальный минимум конечного порядка $2p$, $p\ge1$, со значением $<0$ ⇒ асимптотическая траектория; поворот $\kappa=\kappa(\delta)\asymp\delta^{1-1/p}$ | [Доказано] (теорема A + лемма M) |
| Теорема Mc | Случай (c): $G\equiv\mathrm{const}<0$ на $\Sigma_0$ ⇒ асимптотическая траектория; трубка вокруг всего конуса, $\theta$ периодична | [Доказано] (проверенные теорема A + лемма 2) |
| Лемма V | Дно углового оврага: ветвь Пюизё угловых минимумов (глобальных в окне $\lvert\theta-\theta_0\rvert\le\tau_0$), глубина $-as^\gamma$, профиль $Q_V$ из многоугольника Ньютона | [Доказано] (с теоремами Вейерштрасса и Ньютона–Пюизё) |
| Теорема Md | Случай (d), каскад: карта, следующая за дном, принадлежит (GT3) с $C_1=0$ и $(V_0)$ ⇒ асимптотическая траектория, касающаяся луча | [Доказано] (проверенная теорема 2 [007]) |
| **Теорема M** | $n=3$, $u_m\ge0$, $\Sigma$ Морса–Ботта, $0$ — не точка локального минимума ⇒ асимптотическая траектория; в частности, (A) | [Доказано] (опора — [007], [008]) |
| Лемма I | Критерий изолированности (для примеров) | [Доказано] (опора — K4 [008]) |
| §9 | Примеры C1, C2, D1, D2s, D2, D3, B: классификация, дно оврага, строгий выход | выкладки [Эксперимент] |

**Главное.**

1. **(A) при $n=3$ для $\Sigma$ Морса–Ботта** (теорема M), причём изолированность не нужна: достаточно,
   чтобы $0$ не был точкой локального минимума. Опора — проверенные [007] (теорема A, леммы 1–2,
   теорема 2) и [008] (леммы K1–K3, теорема K0, предложение K4) и новые лемма M, теоремы Mb, Mc,
   Md, лемма V этой записки (проверены R26–R28 в первой редакции).
2. **(c)** проще, чем казалось: в трубке вокруг всего конуса над $\Sigma_0$ с $\rho=s$, $Y=\Psi_s$
   все кривизны карты стремятся к нулю, а запас Эйлера $\mu=2c$ даёт нормальное направление.
   Угловых стенок нет, так что угловой запас не нужен. Хватает проверенной леммы 2 [007].
3. **(d)**: угловой овраг узкий, его угловая ширина $s^\alpha\to0$, $\alpha>0$. Поэтому в карте,
   следующей за дном, поворот поля $Y$ имеет порядок $x^\alpha\lvert b\rvert\to0$, и **$C_1=0$**: все
   члены кривизны уходят в $\omega(x)$. Кривая карта и «(V0) при $C_1>0$», которые предполагались в
   §10.2 записки P9, не нужны. Вырожденный угловой минимум закрывается проверенным условием $(V_0)$
   теоремы 2. Попутно траектория касается луча $\mathbb R_+\omega(\theta_0)$.
4. **(a)+(b)**: теорема 2′ [008] к (b) не применима, так как $(V_1')$ требует
   $Q\ge\lambda_0\lvert b\rvert^2$. Вместо неё служит лемма M: перекрёстный член
   $\sim\kappa\lvert\theta\rvert\sqrt{K_\perp}\rho^{\beta/2}$ гасится неравенством о средних с
   $\beta K_\perp$, остаток $\kappa^2R_\theta^2$ сравнивается с запасом $\kappa\delta$, отсюда
   $\kappa\asymp\delta/R_\theta^2\asymp\delta^{1-1/p}$. Члены кривизны $T_2$, $T_3$ при $p\ge3$
   оценку не ломают (замечание 6.3).
5. **Аналитичность** работает в трёх местах: конечность $j$ на той компоненте, где $U<0$ (аналитическая
   $R\not\equiv0$ имеет конечный порядок), конечный порядок минимума $G$, ряды Пюизё дна в (d).
   **Изолированность не используется** (З1 R28, §8): теорема M верна для любой неминимальной
   критической точки из этого класса, изолированной или нет.

## 1. Постановка и что уточнено

**Постановка.** $n=3$; $U$ вещественно-аналитична в окрестности $0$, $U(0)=0$, $\nabla U(0)=0$,
$U=\sum_{k\ge m}u_k$, $u_m\not\equiv0$, $m\ge2$, $u_m\ge0$ (отсюда $m$ чётно). $\Sigma=\{u_m=0\}\cap S^2$.

- **(K1)** $\Sigma$ — гладкое компактное подмногообразие $S^2$ (компоненты — точки и замкнутые
  кривые; $\Sigma=\varnothing$ допускается);
- **(K2)** (Морс–Ботт) $D^2u_m(\omega)$ положительно определена на $N_\omega=(\mathbb R\omega\oplus T_\omega\Sigma)^\perp$
  для всех $\omega\in\Sigma$.

«Не минимум» означает: в любой окрестности $0$ есть точки с $U<0$. (Если $U\ge0$ около
изолированной критической точки, то это строгий минимум: точка с $U=0$ рядом была бы точкой
минимума, то есть критической.)

**Что уточнено в задании.**

1. **Изолированность не требуется** (З1 R28). В задании и в первой редакции стояло «$0$ —
   изолированная критическая точка и не минимум». Изолированность использовалась только для того,
   чтобы $j<\infty$ было на **всех** компонентах. Но в доказательстве участвует одна компонента — та,
   в трубке которой $U<0$, — и на ней $j<\infty$ следует из самих отрицательных значений и
   аналитичности (предложение R, п. 2). Поэтому теорема M сформулирована для любой критической точки
   $0$ из класса, не являющейся локальным минимумом. Задача (A) — частный случай.
2. Жёсткое ядро ($m\ge4$) не требуется: всё доказано при $m\ge2$ (случай $m=2$ известен из
   литературы, [008], замечание 2).
3. Разбор случаев сделан по **глобальному минимуму** $G$ на компоненте (предложение R), а не по
   точке. Случаи (a) и (b) объединены: строгий локальный минимум конечного порядка $2p$, $p\ge1$
   (теорема Mb). Новая теорема Mb не опирается на теорему 2′ [008] и при $p=1$ заново доказывает
   теорему K2 [008].
4. В (d) не требуется, чтобы $G$ была неотрицательна на всей $\Sigma_0$: достаточно $G\ge0$ около
   нуля $\theta_0$ и отрицательных значений $\hat G$ в сколь угодно малых окрестностях $(0,\theta_0)$.
5. Лемма E (`results/009-euler-field.md`, `notes/prover/2026-10-21-euler-field.md`) **не нужна**: в
   (d) поперечный профиль распадается в сумму одномерного углового профиля и невырожденного
   нормального квадрата (формула (5.6)), и взвешенное неравенство Эйлера проверяется прямо.
6. Дополнение ГА о поле $Y=\partial_x\Phi+Z$ разобрано в замечании 6.4.
7. Ссылки переведены с записки P9 на нумерацию [008] (З2 R28).

## 2. Обозначения и нормальная форма вдоль замкнутой компоненты

### 2.1. Данные

Пусть $\Sigma_0$ — компонента-кривая $\Sigma$ длины $L$. По (K1), (K2) $\Sigma_0$ — аналитическая замкнутая
кривая ([002], §2.1(f), §2.2; [008], §1). Это видно и прямо (З4 R28): около $\omega_0\in\Sigma_0$ функция
$f=\langle\nabla u_m,n(\omega_0)\rangle|_{S^2}$ аналитична, равна нулю на $\Sigma$ ($\nabla u_m=0$ на $Z$) и
$\partial_nf(\omega_0)=h_n(\omega_0)>0$, так что $\{f=0\}$ — аналитическая кривая, с которой $\Sigma_0$ локально
совпадает. Пусть $\omega:\mathbb R\to\Sigma_0$ —
натуральная $L$-периодическая аналитическая параметризация, $T=\omega'$, $n=\omega\times T$, $k(\theta)$ —
геодезическая кривизна. Тогда [008, (6.1)]

$$\omega'=T,\qquad T'=-\omega+k\,n,\qquad n'=-k\,T. \tag{2.1}$$

Так как $u_m\ge0$ и $u_m(\omega)=0$, то $\nabla u_m(\omega)=0$ на $\Sigma$. По (K2)
$h_n(\theta):=D^2u_m(\omega(\theta))(n,n)>0$. Обозначим $h_*:=\min h_n>0$, $\bar k:=\max\lvert k\rvert$,
$\lambda_H:=h_*$. Как в [008, (U1), (1.1)], для $\lvert s\rvert<R_0/3$, $\lvert y\rvert<1$
$$\varphi(s,\theta,y):=\sum_{k\ge m}s^{k-m}u_k\big(\omega(\theta)+y\,n(\theta)\big),\qquad
U\big(s(\omega(\theta)+y\,n(\theta))\big)=s^m\varphi(s,\theta,y). \tag{2.2}$$

### 2.2. Лемма N (нормальная форма вдоль всей $\Sigma_0$) [Доказано, сведение к [008]]

**Лемма N.** Найдутся $s_1>0$, $y_1\in(0,1)$, $t_1>0$ с $y_1\le t_1$ и $\bar kt_1\le\frac12$ такие,
что:

- **(N1)** при $\lvert s\rvert<s_1$, $\theta\in\mathbb R$ функция $\varphi(s,\theta,\cdot)$ на
  $(-y_1,y_1)$ удовлетворяет $\partial_y^2\varphi\ge\lambda_H/2$ и имеет единственную критическую точку
  $y^*(s,\theta)\in(-y_1/2,y_1/2)$; это точка глобального минимума на $(-y_1,y_1)$. Функция $y^*$
  аналитична на $(-s_1,s_1)\times\mathbb R$, $L$-периодична по $\theta$, $y^*(0,\theta)=0$.
- **(N2)** $R(s,\theta):=\varphi(s,\theta,y^*(s,\theta))$ аналитична, $L$-периодична, $R(0,\cdot)=0$.
  Числа $g_k$, $j=j(\Sigma_0)$, функции $G=g_j$ и $\hat G$ определены как в [008] (раздел «Данные (S) и
  редуцированная функция», §3.2). Если $j<\infty$,
  то $R=s^{j-m}\hat G$, где $\hat G$ аналитична, $L$-периодична и $\hat G(0,\cdot)=G$. Положим
  $\eta^*:=s\,y^*$ и
  $M(s,\theta,\tau):=\int_0^1(1-\lambda)\,\partial_y^2\varphi(s,\theta,y^*+\lambda\tau)\,d\lambda$. Функция $M$
  аналитична при $\lvert s\rvert<s_1$, $\theta\in\mathbb R$, $\lvert\tau\rvert<y_1/2$, причём $M\ge\lambda_H/4$,
  $M(0,\theta,0)=\frac12h_n(\theta)$, и при $0<s<s_1$, $\lvert\zeta\rvert<\frac{y_1}2s$
  $$U\Big(s\,\omega(\theta)+\big(\eta^*(s,\theta)+\zeta\big)n(\theta)\Big)=s^j\hat G(s,\theta)+s^{m-2}\zeta^2M\big(s,\theta,\zeta/s\big). \tag{2.3}$$
- **(N3)** $P(s,\theta,\eta):=s\,\omega(\theta)+\eta\,n(\theta)$ — аналитический диффеоморфизм множества
  $\{s>0,\ \theta\in\mathbb R/L\mathbb Z,\ \lvert\eta\rvert<t_1s\}$ на открытое подмножество
  $\mathbb R^3\setminus0$. При этом $P_s=\omega$, $P_\theta=(s-k\eta)T$, $P_\eta=n$, $\lvert P\rvert^2=s^2+\eta^2$, и
  функция $s\circ P^{-1}$ имеет градиент $\omega(\theta)$.
- **(N4)** при $0<s<s_1$, $\lvert y\rvert<y_1$: $U\big(s(\omega(\theta)+y\,n(\theta))\big)\ge s^mR(s,\theta)=:F_{\rm fl}(s,\theta)$.

*Доказательство.*

1. (N1). Доказательство леммы K1 [008, §2] использует только аналитичность данных и условия
   $u_m(\omega)=0$, $\nabla u_m(\omega)=0$, $H(\theta)=h_n(\theta)>0$ в каждой точке, но не инъективность
   $\omega$. Применим его с $\Lambda'=\mathbb R$ и $\Lambda=[0,L]$ и получим $s_1,y_1$ и все утверждения при
   $\theta\in\Lambda''\supset[0,L]$. Так как $\varphi(s,\theta+L,y)=\varphi(s,\theta,y)$, утверждения о
   выпуклости и о единственности критической точки переносятся на все $\theta$. Единственность даёт
   $y^*(s,\theta+L)=y^*(s,\theta)$.
2. (N2). Аналитичность и периодичность $R$ и $\hat G$ следуют из (N1) и [008, §3.2]. Формула (2.3) —
   это доказательство леммы K2 [008, §3]: формула Тейлора с интегральным остатком в точке $y^*$, где
   $\partial_y\varphi=0$, даёт $\varphi(s,\theta,y^*+\tau)=R+\tau^2M(s,\theta,\tau)$ при $\lvert\tau\rvert<y_1/2$.
   Отрезок $[y^*,y^*+\tau]$ лежит в $(-y_1,y_1)$. Подставляем $\tau=\zeta/s$ в (2.2):
   $s^m(R+\zeta^2s^{-2}M)=s^j\hat G+s^{m-2}\zeta^2M$. Оценка $M\ge\lambda_H/4$ следует из (N1), а
   $M(0,\theta,0)=\frac12\partial_y^2\varphi(0,\theta,0)=\frac12h_n(\theta)$.
3. (N3). Это лемма K3 [008, §6]; там сказано, что она верна и для замкнутой кривой с периодическим
   $\theta$. Подробнее: Отображение
   $E(\theta,t)=(\omega+tn)/\sqrt{1+t^2}$ аналитично на $(\mathbb R/L\mathbb Z)\times\mathbb R$, в точках
   $(\theta,0)$ его дифференциал имеет столбцы $T,n$ (ранг 2) и $E(\cdot,0)=\omega$ инъективно ($\Sigma_0$
   вложена). Локальный гомеоморфизм, инъективный на компакте $(\mathbb R/L\mathbb Z)\times\{0\}$, инъективен
   на некоторой его окрестности $(\mathbb R/L\mathbb Z)\times[-t_1,t_1]$. Дальше дословно как в [008, §6]:
   из $P=s\sqrt{1+t^2}\,E(\theta,\eta/s)$ следует инъективность $P$, а производные (2.1) дают
   $P_s,P_\theta,P_\eta$. Они попарно ортогональны и ненулевые, так как $s-k\eta\ge s/2$. Для
   ортогональной системы координат $\nabla s=P_s/\lvert P_s\rvert^2=\omega$. В доказательстве леммы K1
   [008] сначала выбирается $y_1$ (годится и любое меньшее), затем $s_1$ по $y_1$. Поэтому можно
   считать $y_1\le t_1$: выберем $t_1$ здесь, а затем $y_1$ и $s_1$ в п. 1.
4. (N4) — глобальная минимальность $y^*$ из (N1) и (2.2) при $s>0$. $\square$

### 2.3. Карта с дном и малые величины

Выберем $s_2\in(0,s_1)$ так, что $\lvert\eta^*(s,\theta)\rvert\le\frac{y_1}4s$ при $0<s<s_2$. Положим

$$\Psi(s,\theta,\zeta):=P\big(s,\theta,\eta^*(s,\theta)+\zeta\big)=s\,\omega(\theta)+\eta\,n(\theta),\qquad \eta:=\eta^*+\zeta,\qquad \varepsilon:=\frac{k(\theta)\eta}{s}. \tag{2.4}$$

На $\{0<s<s_2,\ \theta\in\mathbb R/L\mathbb Z,\ \lvert\zeta\rvert<\frac{y_1}4s\}$ это аналитический
диффеоморфизм на открытое множество (композиция $P$ и $(s,\theta,\zeta)\mapsto(s,\theta,\eta^*+\zeta)$).
Координата $s$ у $\Psi$ та же, что у $P$, поэтому $\nabla s=\omega(\theta)$. Как в [008, (6.4)]:

$$\Psi_s=\omega+\eta^*_s\,n,\qquad \Psi_\theta=s(1-\varepsilon)T+\eta^*_\theta\,n,\qquad \Psi_\zeta=n. \tag{2.5}$$

[Эксперимент: `frames_mb.py`, тождества для многочленов $k(\theta)$, $\eta^*(s,\theta)$ общего вида —
`True`.]

**Малые величины.** Функция $y^*$ аналитична, периодична и $y^*(0,\cdot)=0$. Поэтому равномерно по
$\theta$: $\eta^*=O(s^2)$, $\eta^*_s=O(s)$, $\eta^*_\theta=O(s^2)$, $\eta^*_{ss}=O(1)$, $\eta^*_{s\theta}=O(s)$,
$\eta^*_{\theta\theta}=O(s^2)$. Если ещё $\lvert\zeta\rvert\le Cs^{c_0}$ с $c_0>1$, то
$\varepsilon=O(s^{\min(1,c_0-1)})$, $s\varepsilon_s=k\eta^*_s-\varepsilon$, $\varepsilon_\theta=(k'\eta+k\eta^*_\theta)/s$, и
$$\nu(\sigma):=\sup_{0<s<\sigma}\Big(\lvert\varepsilon\rvert+\lvert s\varepsilon_s\rvert+\lvert\varepsilon_\theta\rvert+\lvert\eta^*_s\rvert+\frac{\lvert\eta^*_\theta\rvert}s+s\lvert\eta^*_{ss}\rvert+\lvert\eta^*_{s\theta}\rvert+\frac{\lvert\eta^*_{\theta\theta}\rvert}s\Big)\xrightarrow[\sigma\to0]{}0 \tag{2.6}$$
(супремум и по $\theta$, и по $\zeta$ из указанной области).

**Нормальная форма в масштабе.** Пусть $j<\infty$ и $c:=\frac{j-m+2}2\ge\frac32$. Положим

$$F(\sigma,\theta,e):=\hat G(\sigma^2,\theta)+e^2M\big(\sigma^2,\theta,\sigma^{j-m}e\big). \tag{2.7}$$

$F$ аналитична при малых $\lvert\sigma\rvert$, $\theta\in\mathbb R$, $\lvert e\rvert\le1$, и по (2.3)
($s^{m-2}(s^ce)^2=s^j$, $s^{c-1}=\sigma^{j-m}$ при $\sigma=s^{1/2}$)

$$U\big(\Psi(s,\theta,s^ce)\big)=s^jF(s^{1/2},\theta,e),\qquad F(0,\theta,e)=G(\theta)+\tfrac12h_n(\theta)e^2. \tag{2.8}$$

**Функция дна.** $F_{\rm fl}=s^mR=s^j\hat G$, и по (N4) $U\ge s^j\hat G(s,\theta)$ в трубке
$\{s(\omega+yn):\ 0<s<s_1,\ \lvert y\rvert<y_1\}$.

## 3. Предложение R (полнота разбора случаев) [Доказано]

**Предложение R.** Пусть выполнены условия §1 и $0$ — не точка локального минимума $U$
(изолированность **не** предполагается). Тогда $\Sigma\ne\varnothing$, и верно хотя бы одно из следующего.

- **(P)** Есть точечная компонента $\{\omega\}\subset\Sigma$, у которой функция $R_\omega$ (данные (S) [008]
  с $d=0$) не равна нулю тождественно и имеет отрицательный старший коэффициент.
- Есть кривая-компонента $\Sigma_0$ с $j=j(\Sigma_0)<\infty$, для которой $G=g_j|_{\Sigma_0}$
  удовлетворяет одному из условий:
  - **(a/b)** $\min G<0$, $G\not\equiv\mathrm{const}$; тогда в точке $\theta_0$ глобального минимума
    $G(\theta_0+\theta)-G(\theta_0)=a\theta^{2p}(1+O(\theta))$, $a>0$, $p\ge1$ ((a) — это $p=1$, (b) — это $p\ge2$);
  - **(c)** $G\equiv\mathrm{const}<0$;
  - **(d)** $\min G=0$, и есть $\theta_0$ с $G(\theta_0)=0$ и точки $(s_k,\theta_k)\to(0,\theta_0)$, $s_k>0$,
    с $\hat G(s_k,\theta_k)<0$.

*Доказательство.*

1. *$\Sigma\ne\varnothing$* (З6 R28). Иначе $u_m\ge c\lvert q\rvert^m$ с $c>0$ и $\lvert U-u_m\rvert\le C\lvert q\rvert^{m+1}$, так что
   $U>0$ в проколотой окрестности $0$, и $0$ — строгий минимум.
2. *Отрицательные значения и $j<\infty$.* По предложению K4(c) [008] (критерий минимума; трубки
   $y_1\le t_1$ — как там) $0$ — локальный минимум тогда и только тогда, когда $F_{\rm fl}\ge0$ при малых
   $s>0$ на всех кривых-компонентах и $R_\omega(s)\ge0$ при малых $s>0$ во всех точечных компонентах.
   Компонент конечное число (компактное многообразие). Значит, есть либо точечная компонента
   $\{\omega\}$ и $s_k\downarrow0$ с $R_\omega(s_k)<0$, либо кривая-компонента $\Sigma_0$ и $(s_k,\theta_k)$, $s_k\downarrow0$,
   с $F_{\rm fl}(s_k,\theta_k)=s_k^mR(s_k,\theta_k)<0$. В обоих случаях $R\not\equiv0$ на этой компоненте. По
   аналитичности отсюда $j<\infty$ (З1 R28): если бы все $g_k\equiv0$, то при каждом $\theta$ аналитическая
   на $(-s_1,s_1)$ функция $R(\cdot,\theta)$ имела бы в $0$ все производные нулевыми и была бы $\equiv0$.
   **Изолированность здесь не нужна**: конечность $j$ на остальных компонентах не используется.
3. *Точечная компонента.* $R_\omega\not\equiv0$ аналитична, $R_\omega(s_k)<0$ при $s_k\downarrow0$, поэтому её
   старший коэффициент $g_{j(\omega)}(\omega)$ отрицателен — это (P).
4. *Кривая-компонента.* $s_k^j\hat G(s_k,\theta_k)<0$. По компактности $\mathbb R/L\mathbb Z$ после перехода к
   подпоследовательности $\theta_k\to\theta_*$, и $G(\theta_*)=\lim\hat G(s_k,\theta_k)\le0$ (непрерывность $\hat G$).
   - Если $\min G<0$ и $G\not\equiv\mathrm{const}$, то в точке $\theta_0$ глобального минимума аналитическая
     $G-G(\theta_0)\ge0$ имеет нуль конечного порядка (иначе $G\equiv\mathrm{const}$ по аналитичности на
     связной $\Sigma_0$), чётного, с положительным старшим коэффициентом. Это (a/b).
   - Если $G\equiv\mathrm{const}<0$, это (c).
   - Если $\min G=0$, то $G(\theta_*)=0$, и это (d) с $\theta_0=\theta_*$ и той же последовательностью
     (поднятой в $\mathbb R$ около $\theta_0$).
   - $\min G>0$ невозможно: противоречит $G(\theta_*)\le0$.
   - $G\equiv0$ невозможно по определению $j$. $\square$

**Замечание 3.1.** В первой редакции шаг 2 опирался на изолированность: при $R\equiv0$ поверхность дна
$\{\Psi(s,\theta,0)\}$ состоит из критических точек ([008], §3.5; K4(b)), а изолированность это исключает.
Этот довод верен, но не нужен (З1 R28): компонента, на которой $U<0$, сама даёт $R\not\equiv0$. Проверка
на неизолированном примере (R28): $U=z^2-x^4$ ($m=2$, $\Sigma$ — окружность $z=0$, $G=-\cos^4\theta$, случай
(a)); асимптотическая траектория $x(t)=1/(\sqrt2\,t+C)$ по оси $x$ есть, хотя вся ось $y$ состоит из
критических точек.

## 4. Случай (c): теорема Mc [Доказано]

**Теорема Mc.** Пусть $\Sigma_0$ — кривая-компонента, $j<\infty$ и $G\equiv-a_0<0$ на $\Sigma_0$. Тогда
у $\ddot q=-\nabla U(q)$ есть асимптотическая траектория вида $q(t)=\Psi\big(s(t),\theta(t),s(t)^ce(t)\big)$, где
$s(t)$ строго убывает к $0$, $-k_2s^{j/2}\le\dot s\le-k_1s^{j/2}$ ($0<k_1\le k_2$), а
$\lvert e(t)\rvert\le2\sqrt{2\delta/h_*}$ при всех $t$; здесь $\delta>0$ можно взять сколь угодно малым.
Об угле $\theta(t)$ ничего не утверждается.

*Доказательство.* Применяем теорему A и лемму 2 [007] (обе проверены). Открытое множество
теоремы A обозначаем $\mathcal G$, чтобы не путать с $G$.

1. *Данные.* $\beta:=j$. Уменьшим $s_2$ так, чтобы $s_2^{c-1}<y_1/4$ и $\sqrt2s_2<r$ (радиус шара $B_r$, где
   $U$ аналитична), и положим $\mathcal G:=\{\Psi(s,\theta,s^ce):\ 0<s<s_2,\ \theta\in\mathbb R/L\mathbb Z,\ \lvert e\rvert<1\}$.
   Тогда $\lvert\zeta\rvert=s^c\lvert e\rvert<\frac{y_1}4s$, так что это открытое множество из §2.3, и $\mathcal G\subset B_r\setminus0$.
   Далее $\rho:=s\circ\Psi^{-1}$, $Y:=\Psi_s\circ\Psi^{-1}$, $A(r):=a_0r^j$ на $(0,\sigma_0)$, $\sigma_0:=s_2$. Поле $Y$
   аналитично и $Y\rho=1$. Число $\sigma$ теоремы A — это $\sigma_*$ из п. 3 (З5 R28).
2. *Тождество Эйлера.* Пусть $W=U+A(\rho)$ и $g(s,\theta,\zeta):=W(\Psi(s,\theta,\zeta))=s^j\big(F(s^{1/2},\theta,\zeta s^{-c})+a_0\big)$.
   Поле $Y$ в координатах $(s,\theta,\zeta)$ — это $\partial_s$, поэтому
   $(\rho\,YW)\circ\Psi=s\,\partial_sg=jW+s^j\big[\tfrac\sigma2\partial_\sigma F-ce\,\partial_eF\big]$ и
   $$\beta W-\rho\,YW=s^j\big[c\,e\,\partial_eF-\tfrac\sigma2\partial_\sigma F\big]\qquad(\sigma=s^{1/2},\ e=\zeta s^{-c}). \tag{4.1}$$
3. *Область.* $F_0(\theta,e):=F(0,\theta,e)=-a_0+\frac12h_n(\theta)e^2$, $Q:=F_0+a_0=\frac12h_n(\theta)e^2$. Пусть
   $0<\delta\le\min(a_0/2,\ h_*/32)$, $\Omega:=\{(\theta,e):\ Q<4\delta\}$. На $\Omega$
   $\lvert e\rvert<R_e:=2\sqrt{2\delta/h_*}\le\frac12$. Положим
   $$\chi(\sigma):=\sup\big\{\lvert F-F_0\rvert+\lvert\partial_eF-\partial_eF_0\rvert+\lvert\sigma'\partial_\sigma F\rvert:\ 0<\sigma'\le\sigma,\ \theta\in\mathbb R,\ \lvert e\rvert\le1\big\},$$
   где $F$ и производные берутся в точке $(\sigma',\theta,e)$. По аналитичности, периодичности и
   компактности $\chi(\sigma)\to0$. Выберем $\sigma_*\in(0,s_2)$ с $\chi(\sigma_*^{1/2})<\delta$ (дальше
   $\sigma_*$ ещё уменьшится), обозначим $\chi:=\chi(\sigma_*^{1/2})$ и положим
   $$\mathcal D:=\{(s,\theta,e):\ 0<s<\sigma_*,\ (\theta,e)\in\Omega,\ F(s^{1/2},\theta,e)+a_0<\delta\},\qquad D:=\{\Psi(s,\theta,s^ce):\ (s,\theta,e)\in\mathcal D\}.$$
   $D$ открыто и $D\subset\mathcal G$.
4. *(D1).* $\rho<\sigma_*$ на $D$. Пусть $q=\lim\Psi(s_k,\theta_k,s_k^ce_k)$ с $(s_k,\theta_k,e_k)\in\mathcal D$. По
   подпоследовательности $s_k\to\bar s\in[0,\sigma_*]$, $\theta_k\to\bar\theta$ в $\mathbb R/L\mathbb Z$,
   $e_k\to\bar e$, $\lvert\bar e\rvert\le R_e<1$. Если $\bar s>0$, то $q=\Psi(\bar s,\bar\theta,\bar s^c\bar e)\in\mathcal G$.
   Если $\bar s=0$, то $\lvert q\rvert=\lim\sqrt{s_k^2+\eta_k^2}=0$. Значит, $\overline D\setminus\{0\}\subset\mathcal G$.
   Далее, $\lvert\Psi\rvert^2=s^2+\eta^2\le2s^2$, поэтому $\sup\{\lvert q\rvert:\ q\in D,\ \rho<s\}\le\sqrt2s\to0$, и
   $\rho(q)\le\lvert q\rvert$.
5. *(D2).* Пусть $q\in\partial D\setminus\{0\}$, $\rho(q)<\sigma_*$. Тогда $q\in\mathcal G$,
   $q=\Psi(\bar s,\bar\theta,\bar s^c\bar e)$, и $(\bar s,\bar\theta,\bar e)$ лежит в замыкании $\mathcal D$, но не в
   $\mathcal D$ (координаты — гомеоморфизм). Поэтому $\bar s<\sigma_*$, $Q(\bar\theta,\bar e)\le4\delta$,
   $F+a_0\le\delta$, и либо $Q(\bar\theta,\bar e)=4\delta$, либо $F+a_0\ge\delta$. В первом случае
   $F+a_0\ge Q-\chi>3\delta$, что противоречит $F+a_0\le\delta$. Итак, $F+a_0=\delta$, то есть
   $W(q)=\delta\rho^j$.
6. *(D3).* $(s,\theta,0)\in\mathcal D$ при $s<\sigma_*$: $Q=0$ и $F(s^{1/2},\theta,0)+a_0\le\chi<\delta$, так что
   $W<\delta\rho^j$.
7. *(L0)–(L2) леммы 2 на $D_\sigma$.* (L0): $a_1=a_3=a_0$, $a_2=ja_0$, $\delta\le a_0/2$. (L1):
   $h=\lvert\Psi_s\rvert^2=1+\eta^{*2}_s\in[1,\frac32]$. (L2): в точках $D_\sigma$ имеем
   $(\theta,e)\in\overline\Omega$ и $Q\ge0$, поэтому $W=s^j\big((F-F_0)+Q\big)\ge-\chi s^j\ge-\delta\rho^j$. По (4.1)
   и $ce\,\partial_eQ=2cQ$:
   $$\beta W-\rho YW\ge s^j\big[2cQ-cR_e\chi-\chi/2\big]\ge2c\,W-s^j\big(cR_e+\tfrac12+2c\big)\chi .$$
   Значит, (L2) выполнено с $\mu:=2c=j-m+2\in(0,\beta]$ и $\varepsilon_1:=(cR_e+\frac12+2c)\chi/\delta$.
8. *(L3).* Пусть $w\perp Y$ и $w=w_\omega\omega+w_TT+w_nn$. Из $\langle Y,w\rangle=w_\omega+\eta^*_sw_n=0$
   следует $\lvert\langle\nabla\rho-Y/h,w\rangle\rvert=\lvert\langle\omega,w\rangle\rvert\le\lvert\eta^*_s\rvert\,\lvert w\rvert$.
   Вектор $\nabla\rho-Y/h$ сам ортогонален $Y$, поэтому $\vartheta_1:=\sup\lvert\eta^*_s\rvert$ годится в (L3).
   Далее, $\nabla_YY=\partial_s(Y\circ\Psi)=\eta^*_{ss}n$, так что $\vartheta_2:=\sup s\lvert\eta^*_{ss}\rvert$.
   Для $s\langle w,D_wY\rangle$ (вывод прямо, З7 R28): разложим $w=a^s\Psi_s+a^\theta\Psi_\theta+a^\zeta\Psi_\zeta$; по
   (2.5) $a^s=w_\omega$, $a^\theta=w_T/(s(1-\varepsilon))$. Поле $Y\circ\Psi=\omega(\theta)+\eta^*_s(s,\theta)n(\theta)$ не зависит
   от $\zeta$, и по (2.1) $\partial_s(Y\circ\Psi)=\eta^*_{ss}n$, $\partial_\theta(Y\circ\Psi)=(1-k\eta^*_s)T+\eta^*_{s\theta}n$. Поэтому
   $D_wY=w_\omega\eta^*_{ss}n+\frac{w_T}{s(1-\varepsilon)}\big[(1-k\eta^*_s)T+\eta^*_{s\theta}n\big]$ и
   $$s\langle w,D_wY\rangle=\frac{(1-\eta^*_sk)\,w_T^2}{1-\varepsilon}+s\eta^*_{ss}w_\omega w_n+\frac{\eta^*_{s\theta}w_Tw_n}{1-\varepsilon}\ge-\big(s\lvert\eta^*_{ss}\rvert+2\lvert\eta^*_{s\theta}\rvert\big)\lvert w\rvert^2,$$
   если $\lvert\varepsilon\rvert\le\frac14$ и $\lvert\eta^*_sk\rvert\le1$ (это совпадает с (6.7) при $\kappa=0$; символьная
   проверка — `frames_mb.py`). Значит,
   $\vartheta_3:=\sup(s\lvert\eta^*_{ss}\rvert+2\lvert\eta^*_{s\theta}\rvert)$. Здесь $\vartheta_i$ — это константы
   $\theta_i$ условия (L3) [007] (переобозначены, чтобы не путать с углом). Все супремумы берутся по
   $s<\sigma_*$ и не превосходят $2\nu(\sigma_*)\to0$ по (2.6).
9. *Выбор $\sigma_*$.* При фиксированном $\delta$ величины $\varepsilon_1$, $(L_1\vartheta_1+L_2\vartheta_2)/\sqrt\delta$, $4\vartheta_3$
   стремятся к $0$ при $\sigma_*\to0$. Выберем $\sigma_*$ так, чтобы их сумма была $\le\mu/2$ и
   $4\vartheta_1\sqrt\delta\le\sqrt{2a_0/3}$. Тогда по лемме 2 [007] выполнены (D4), (A4) и (A5) (скобка
   в (3.1) [007] не меньше $\mu/2$). Теорема A [007] даёт решение $(q(t),v(t))\in\overline\Omega$ (множество
   теоремы A), $q(t)\ne0$, $q,v\to0$. Оценки $\dot s$ — из п. 1 леммы 2 [007]; оценка $e(t)$ — из
   $(\theta,e)\in\overline\Omega$. $\square$

**Замечание 4.1.** Теорема Mc по существу не использует постоянство $G$ сверх того, что
$Q=F_0+a_0$ не зависит от угла при $e=0$. При непостоянной $G$ член $\beta x^\beta(G-\min G)$ в
$\beta W$ не компенсируется в (4.1): у $\theta$ вес $0$. Поэтому для непостоянной $G$ нужны угловые
стенки (теоремы Mb, Md).

## 5. Случай (d): каскад

### 5.1. Лемма V (дно углового оврага) [Доказано]

**Лемма V.** Пусть $f(s,\tau)$ вещественно-аналитична в окрестности $(0,0)\in\mathbb R^2$,
$f(0,\tau)=g(\tau)$, где $g(0)=0$, $g\ge0$ около $0$, $g\not\equiv0$ (так что $g=g_{2q}\tau^{2q}+\dots$,
$g_{2q}>0$, $q\ge1$), и пусть $f(s_k,\tau_k)<0$ для некоторых $s_k\downarrow0$, $\tau_k\to0$. Тогда есть
$\tau_0>0$, $s_3>0$, чётное $N\in\mathbb N$, натуральное $A$, чётное натуральное $\Gamma$ (З2 R27), число $a>0$, функция $T$,
аналитическая около $0$ с $T(0)=0$, и многочлен $Q_V(b)=\sum_{k\in K_*}c_kb^k$, $K_*\subset\{2,\dots,2q\}$,
$c_k\ne0$, такие, что:

1. при $s\in(0,s_3)$ точка $\tau_v(s):=T(s^{1/N})\in(-\tau_0,\tau_0)$ — точка глобального минимума
   $f(s,\cdot)$ на $[-\tau_0,\tau_0]$, $\partial_\tau f(s,\tau_v(s))=0$ и $f(s,\tau_v(s))<0$;
2. для любого $B>0$ функция $\hat\Phi(t,b):=t^{-\Gamma}f\big(t^N,T(t)+t^Ab\big)$ продолжается до
   вещественно-аналитической на $\{\lvert t\rvert<t_2\}\times\{\lvert b\rvert<B\}$ при некотором $t_2=t_2(B)>0$, и
   $\hat\Phi(0,b)=-a+Q_V(b)$;
3. $Q_V\ge0$ на $\mathbb R$; младшая степень $k_0:=\min K_*$ чётна и $c_{k_0}>0$.

В терминах $s$: глубина дна $f(s,\tau_v(s))=-as^\gamma(1+o(1))$, $\gamma=\Gamma/N>0$, угловая ширина
оврага $s^\alpha$, $\alpha=A/N>0$.

*Доказательство.*

1. *Полярная кривая.* $\partial_\tau f(0,\tau)=g'(\tau)$ имеет в $0$ нуль порядка ровно $2q-1$. По
   подготовительной теореме Вейерштрасса [Литература: напр. Krantz–Parks, *A Primer of Real
   Analytic Functions*, 2-е изд., 2002, §6.1; Brieskorn–Knörrer, *Plane Algebraic Curves*, 1986, §8.2;
   с первоисточниками не сверено] около $(0,0)$ $\partial_\tau f=u\cdot P$, где $u(0,0)\ne0$ и
   $P=\tau^{2q-1}+\sum_{i<2q-1}p_i(s)\tau^i$, $p_i(0)=0$. Утверждение теоремы: для голоморфной в
   окрестности $0\in\mathbb C^2$ функции $F$ с $F(0,\tau)=\tau^d\cdot$(единица) разложение $F=uP$ с
   единицей $u$ и многочленом Вейерштрасса $P$ степени $d$ существует и единственно в некотором
   полидиске. Из единственности и вещественности коэффициентов $f$ следует, что $u$ и $p_i$
   вещественны (сопряжение переводит разложение в разложение). По теореме Ньютона–Пюизё
   [Литература: Brieskorn–Knörrer, §8.3; C.T.C. Wall, *Singular Points of Plane Curves*, 2004,
   Thm 2.1.1; не сверено] найдутся $N_1\in\mathbb N$ и голоморфные около $0$ функции $T_1,\dots,T_{2q-1}$,
   $T_i(0)=0$, такие, что $P(t^{N_1},\tau)=\prod_i(\tau-T_i(t))$ при малых $\lvert t\rvert$.
2. *Вещественные корни.* Пусть $I_{\mathbb R}$ — множество тех $i$, у которых все коэффициенты Тейлора
   $T_i$ вещественны. При $i\notin I_{\mathbb R}$ функция $\operatorname{Im}T_i(t)$ на вещественных $t$ — ненулевой
   сходящийся ряд, поэтому она $\ne0$ при $0<t<t_3$. Значит, при $0<s<t_3^{N_1}$ вещественные корни
   $P(s,\cdot)$ — это ровно $T_i(s^{1/N_1})$, $i\in I_{\mathbb R}$.
3. *Выбор $\tau_0$.* $g>0$ на $[-\tau_1,\tau_1]\setminus0$ при малом $\tau_1$ ($0$ — изолированный нуль). Выберем
   $\tau_0\le\tau_1$ и $s_4\in(0,t_3^{N_1}]$ (З1 R27) так, что разложение $\partial_\tau f=uP$ верно и $u\ne0$ на
   $[0,s_4]\times[-\tau_0,\tau_0]$, $f(s,\pm\tau_0)\ge\frac12\min(g(\tau_0),g(-\tau_0))>0$ и
   $\lvert T_i(s^{1/N_1})\rvert<\tau_0$ при $s\in[0,s_4]$. Тогда при $s\in(0,s_4)$ минимум $m(s)$ функции
   $f(s,\cdot)$ на $[-\tau_0,\tau_0]$ достигается в $\pm\tau_0$ или в одной из точек $T_i(s^{1/N_1})$,
   $i\in I_{\mathbb R}$.
4. *Выбор ветви.* Функции $v_i(t):=f(t^{N_1},T_i(t))$, $i\in I_{\mathbb R}$, вещественно-аналитичны около $0$, и
   $v_i(0)=0$. Разность двух из них либо $\equiv0$, либо знакопостоянна на $(0,t_5)$. Поэтому есть
   $i_*\in I_{\mathbb R}$ и $t_5>0$ с $v_{i_*}\le v_i$ на $(0,t_5)$ для всех $i\in I_{\mathbb R}$. При больших $k$
   $m(s_k)\le f(s_k,\tau_k)<0$, значит, $m(s_k)=\min_iv_i(s_k^{1/N_1})=v_{i_*}(s_k^{1/N_1})<0$. Поэтому
   $v_{i_*}\not\equiv0$ и $v_{i_*}(t)=-at^{\Gamma_1}(1+O(t))$ с $a>0$, $\Gamma_1\ge1$. При малых $t>0$ имеем
   $v_{i_*}(t)<0<f(s,\pm\tau_0)$, так что $m(s)=v_{i_*}(s^{1/N_1})$ достигается в
   $\tau_v(s)=T_{i_*}(s^{1/N_1})$. Это п. 1 (пока с $N_1$).
5. *Многоугольник Ньютона.* Пусть $\tilde f(t,\tau'):=f(t^{N_1},T_{i_*}(t)+\tau')$. Эта функция аналитична около
   $(0,0)$, $\tilde f(t,0)=v_{i_*}(t)$, $\partial_{\tau'}\tilde f(t,0)=0$, и
   $\tilde f(t,\tau')=\tilde f(t,0)+\sum_{k\ge2}a_k(t)\tau'^k$. Так как $T_{i_*}(0)=0$, то
   $a_k(0)=g^{(k)}(0)/k!$: $a_k(0)=0$ при $k<2q$ и $a_{2q}(0)=g_{2q}>0$. Пусть $\nu_k=\operatorname{ord}_ta_k$;
   тогда $\nu_{2q}=0$ и $\nu_k\ge1$ при $2\le k<2q$. Функция $E(A'):=\min_{2\le k\le2q}(\nu_k+kA')$ на
   $[0,\infty)$ непрерывна и строго возрастает, $E(0)=0<\Gamma_1$, $E(\infty)=\infty$. Значит, есть
   единственное $A'_*>0$ с $E(A'_*)=\Gamma_1$, и оно рационально со знаменателем $\le2q$. При $k>2q$
   $\nu_k+kA'_*>2qA'_*\ge E(A'_*)$. Итак, $\nu_k+kA'_*\ge\Gamma_1$ при всех $k\ge2$, с равенством ровно при
   $k\in K_*\ne\varnothing$, $K_*\subset\{2,\dots,2q\}$.
6. *Целые показатели.* Положим $\ell:=2\cdot(2q)!$, $N:=\ell N_1$, $T(t):=T_{i_*}(t^\ell)$, $\Gamma:=\ell\Gamma_1$,
   $A:=\ell A'_*\in\mathbb N$. Замена $t\mapsto t^\ell$ умножает $\nu_k$, $\Gamma_1$ и $A'_*$ на $\ell$, так что
   п. 5 верен с $\nu_k\ell$, $\Gamma$, $A$. $N$ чётно, $\Gamma$ чётно.
7. *Функция $\hat\Phi$.* Пусть $f(t^N,T(t)+\tau')=\sum f_{ik}t^i\tau'^k$ — ряд, абсолютно сходящийся при
   $\lvert t\rvert<t_6$, $\lvert\tau'\rvert<\tau_6$. Коэффициент $f_{ik}\ne0$ только если $k=0$, $i\ge\Gamma$ или
   $k\ge2$, $i\ge\nu_k\ell$. В обоих случаях $i+kA\ge\Gamma$. Поэтому
   $t^{-\Gamma}f(t^N,T(t)+t^Ab)=\sum f_{ik}t^{i+kA-\Gamma}b^k$ — степенной ряд по $(t,b)$ с
   неотрицательными показателями. Он сходится абсолютно при $0<\lvert t\rvert<t_2$, $\lvert b\rvert<B$, если
   $t_2<t_6$ и $t_2^AB<\tau_6$: мажоранта равна $\lvert t\rvert^{-\Gamma}\sum\lvert f_{ik}\rvert\lvert t\rvert^i(\lvert t\rvert^AB)^k$.
   Его сумма $\hat\Phi$ аналитична, и $\hat\Phi(0,b)=f_{\Gamma0}+\sum_{k\in K_*}f_{\nu_k\ell,k}b^k=-a+Q_V(b)$,
   где $c_k:=f_{\nu_k\ell,k}\ne0$ — старший коэффициент $a_k$. Это п. 2.
8. *$Q_V\ge0$.* При малом $t>0$ и $\lvert b\rvert\le B$ точка $T(t)+t^Ab$ лежит в $[-\tau_0,\tau_0]$, и по п. 1
   $f(t^N,T(t)+t^Ab)\ge f(t^N,T(t))$, то есть $\hat\Phi(t,b)\ge\hat\Phi(t,0)$. При $t\to0$ получаем
   $Q_V(b)\ge Q_V(0)=0$ при $\lvert b\rvert\le B$, а $B$ любое. $Q_V$ — ненулевой многочлен без членов
   степеней $0$ и $1$, $Q_V\ge0$; значит, его младшая степень $k_0$ чётна и $c_{k_0}>0$. $\square$

### 5.2. Теорема Md (каскад) [Доказано]

**Теорема Md.** Пусть $\Sigma_0$ — кривая-компонента, $j<\infty$, $\theta_0\in\mathbb R$, $G\ge0$ около
$\theta_0$, $G(\theta_0)=0$, и $\hat G(s_k,\theta_k)<0$ для некоторых $s_k\downarrow0$, $\theta_k\to\theta_0$. Условия леммы V
для $f(s,\tau):=\hat G(s,\theta_0+\tau)$ выполнены: $f$ аналитична около $(0,0)$ по (N2), $f(0,\cdot)=G(\theta_0+\cdot)\ge0$, и
$G\not\equiv0$ около $\theta_0$, так как $G=g_j\not\equiv0$ на $\Sigma_0$ (определение $j$) и аналитична на связной $\Sigma_0$
(З3 R27). Пусть
$N,A,\Gamma,a,T,Q_V,k_0$ — из леммы V для этой $f$, $\alpha=A/N$,
$\gamma=\Gamma/N$, и
$$\beta:=j+\gamma,\qquad c_1:=1+\alpha,\qquad c_2:=c':=\frac{\beta-m+2}2>1 .$$
Тогда при подходящих $s_0,r_0$ карта
$$\Phi(x,u,\zeta):=\Psi\Big(x,\ \theta_0+\tau_v(x)+\frac ux,\ \zeta\Big),\qquad b=(b_1,e)=\big(u\,x^{-c_1},\ \zeta\,x^{-c_2}\big), \tag{5.1}$$
задаёт принадлежность $U$ классу (GT3) [007] с $n=3$, весами $(c_1,c_2)$, этим $N$, $C_1=0$ и
условием $(V_0)$ (при $k_0=2$ выполнено и $(V_1)$). По теореме 2 [007] есть асимптотическая
траектория $q(t)=\Phi(x(t),u(t),\zeta(t))$ с $x(t)\downarrow0$, $x(t)\asymp t^{-2/(\beta-2)}$ (здесь $\beta=j+\gamma>m\ge2$), и
$b(t)$ в компакте. Она **касается луча**: $q(t)/\lvert q(t)\rvert\to\omega(\theta_0)$.

Срезы $\{x=\mathrm{const}\}$ — полярные ($s=x$), $u$ — длина дуги от дна оврага по окружности радиуса
$x$ развёртки, $\zeta$ — нормальное смещение от дна $\eta^*$.

*Доказательство.* Обозначим $\vartheta(x,u):=\theta_0+\tau_v(x)+u/x$; в $\mathcal N$ имеем
$u/x=x^\alpha b_1$. Положим $\tilde\kappa:=x\,\partial_x\vartheta=x\tau_v'(x)-x^\alpha b_1$. Так как
$\tau_v(x)=T(x^{1/N})$ и $T(0)=0$, то $x\tau_v'=\frac1Nx^{1/N}T'(x^{1/N})=O(x^{1/N})$ и
$x^2\tau_v''=O(x^{1/N})$. Поэтому равномерно на $\mathcal N=\{0<x<s_0,\ \lvert b\rvert<r_0\}$ (при любом
фиксированном $r_0$)
$$\tilde\kappa\to0,\qquad x^2\partial_x^2\vartheta=x^2\tau_v''+2x^\alpha b_1\to0,\qquad \vartheta-\theta_0\to0,\qquad \lvert\zeta\rvert\le r_0x^{c'}. \tag{5.2}$$

1. *$(\Phi0)$.* $L(x,u,\zeta):=(x,\vartheta(x,u),\zeta)$ — гладкий диффеоморфизм
   $(0,s_0)\times\mathbb R^2$ на себя с обратным $(s,\theta,\zeta)\mapsto(s,\ s(\theta-\theta_0-\tau_v(s)),\ \zeta)$. При
   малом $s_0$ точки $L(\mathcal N)$ лежат в области §2.3 с $\lvert\vartheta-\theta_0\rvert<L/4$, где $\Psi$
   инъективна (лемма N, (N3)). Значит, $\Phi=\Psi\circ L$ — $C^\infty$-диффеоморфизм $\mathcal N$ на открытое
   множество. По (N3) $x\le\lvert\Phi\rvert=\sqrt{x^2+\eta^2}\le2x$: $c_0=1$, $\omega_0(x)=2x$.
2. *Производные* (проверены символьно, `frames_mb.py`, блок «D»):
   $$\Phi_x=\omega+\tilde\kappa(1-\varepsilon)T+\Big(\eta^*_s+\frac{\tilde\kappa\,\eta^*_\theta}x\Big)n,\qquad \Phi_u=(1-\varepsilon)T+\frac{\eta^*_\theta}xn,\qquad\Phi_\zeta=n, \tag{5.3}$$
   $$x\Phi_{xx}=x\eta^*_{ss}n+2\tilde\kappa\,\Psi_{s\theta}+\frac{\tilde\kappa^2}x\Psi_{\theta\theta}+x\vartheta_{xx}\Psi_\theta,\qquad
   x\,\partial_u\Phi_x=(\varepsilon-k\eta^*_s)T+\Big(\eta^*_{s\theta}-\frac{\eta^*_\theta}x\Big)n+\frac{\tilde\kappa}x\Psi_{\theta\theta},\qquad
   x\,\partial_\zeta\Phi_x=-\tilde\kappa kT, \tag{5.4}$$
   где $\Psi_{s\theta}=(1-k\eta^*_s)T+\eta^*_{s\theta}n$,
   $\Psi_{\theta\theta}=-(k'\eta+2k\eta^*_\theta)T+(s-k\eta)(-\omega+kn)+\eta^*_{\theta\theta}n$ — в точке $(x,\vartheta,\zeta)$.
   Отсюда $\lvert\Psi_{\theta\theta}\rvert\le C_\Psi x$ и $\lvert\Psi_\theta\rvert\le2x$ при малом $s_0$.
3. *$(\Phi1)$.* В ортонормированном репере $(\omega,T,n)$ матрица столбцов $J=(\Phi_x,\Phi_u,\Phi_\zeta)$
   равна $I+E$, где элементы $E$ по модулю не больше
   $\nu_1(x):=\sup(\lvert\tilde\kappa\rvert(1+\lvert\varepsilon\rvert)+\lvert\eta^*_s\rvert+\lvert\tilde\kappa\eta^*_\theta\rvert/x+\lvert\varepsilon\rvert+\lvert\eta^*_\theta\rvert/x)\to0$
   по (5.2), (2.6). Тогда $B=J^{\mathsf T}J=I+E+E^{\mathsf T}+E^{\mathsf T}E$ и
   $\lVert B-I\rVert\le6\nu_1+9\nu_1^2\le\frac12$ при малом $s_0$, и $\lvert B_{xu}\rvert\le\lVert B-I\rVert\le6\nu_1+9\nu_1^2\to0$.
4. *$(\Phi2)$ с $C_1=0$.* По (5.4) и (5.2)
   $x\lvert\Phi_{xx}\rvert\le x\lvert\eta^*_{ss}\rvert+2\lvert\tilde\kappa\rvert(1+\lvert\eta^*_{s\theta}\rvert+\bar k\lvert\eta^*_s\rvert)+C_\Psi\tilde\kappa^2+2\lvert x^2\vartheta_{xx}\rvert\to0$.
5. *$(\Phi3)$ с $C_1=0$.* По (5.4) $x\lvert\partial_j\Phi_x\rvert\to0$ равномерно для $j\in\{x,u,\zeta\}$. Для
   $w=D\Phi\,\xi$ из $B\ge\frac12I$ следует $\lvert\xi\rvert\le\sqrt2\lvert w\rvert$, и
   $x\lvert D_wY\rvert=x\lvert\sum_j\xi_j\partial_j\Phi_x\rvert\le\sqrt6\,\max_jx\lvert\partial_j\Phi_x\rvert\,\lvert w\rvert$. Итак,
   $x\langle w,D_wY\rangle\ge-\omega(x)\lvert w\rvert^2$ с $\omega(x)\to0$. Возьмём одно $\omega(x)$ — сумму
   полученных в пп. 3–5 оценок.
6. *(F).* По (2.3) с $s=x=t^N$, $\theta=\vartheta=\theta_0+T(t)+t^Ab_1$, $\zeta=x^{c'}e$:
   $$U\circ\Phi=x^j\hat G(x,\vartheta)+x^{m-2}x^{2c'}e^2M(x,\vartheta,x^{c'-1}e)=x^\beta\Big[\hat\Phi(t,b_1)+e^2M\big(t^N,\theta_0+T(t)+t^Ab_1,\ t^{N(c'-1)}e\big)\Big]=:x^\beta F(t,b), \tag{5.5}$$
   так как $x^j\hat G(x,\vartheta)=x^jf(t^N,T(t)+t^Ab_1)=x^jt^\Gamma\hat\Phi=x^\beta\hat\Phi$ и
   $m-2+2c'=\beta$. Число $N(c'-1)=\frac{N(j-m)+\Gamma}2$ натуральное ($N$, $\Gamma$ чётны). Значит, $F$
   аналитична в окрестности $\{0\}\times\overline{B_{r_0}}$ (лемма V, п. 2 с $B>r_0$; аналитичность $M$), а по
   компактности — на $(-\epsilon_F,\epsilon_F)\times B_{r_0+\epsilon_F}$ при некотором $\epsilon_F>0$. **Выбор $s_0$** (З4 R27):
   $s_0\le1$, $s_0<s_2$, $r_0s_0^{c'-1}<y_1/4$, $s_0^{1/N}<\min(\epsilon_F,t_2(B))$ и малость из пп. 1, 3–5. Тогда (2.3)
   и (5.5) верны на всём $\mathcal N$. Поэтому $F,\nabla_bF$ непрерывны вплоть до $t=0$ и
   $\sup_K\lvert t\partial_tF\rvert=O(t)$. Переменная
   $s$ теоремы 2 [007] — это $t=x^{1/N}$. Предельный профиль:
   $$F_0(b_1,e)=-a+Q_V(b_1)+\tfrac12h_n(\theta_0)e^2,\qquad Q(b):=F_0(b)-F_0(0)=Q_V(b_1)+\tfrac12h_n(\theta_0)e^2. \tag{5.6}$$
7. *$(V_0)$.* $F_0(0)=-a<0$. Выберем $r_2>0$ так, что при $\lvert b_1\rvert\le r_2$:
   $Q_V(b_1)\ge\frac{c_{k_0}}2b_1^{k_0}$ и $b_1Q_V'(b_1)\ge\frac{k_0}2Q_V(b_1)\ge Q_V(b_1)$. Это возможно, так как
   $Q_V=c_{k_0}b_1^{k_0}(1+O(b_1))$ и $b_1Q_V'=k_0c_{k_0}b_1^{k_0}(1+O(b_1))$. Положим $r_0:=r_2$. При
   $0<\delta\le\delta_2$ из $Q(b)<\delta$, $b\in B_{r_0}$ следуют $\lvert b_1\rvert<(2\delta/c_{k_0})^{1/k_0}$ и
   $\lvert e\rvert<\sqrt{2\delta/h_n(\theta_0)}$. При малом $\delta_2$ отсюда $b\in B_{r_0/2}$, так что
   $\{Q<\delta\}\cap B_{r_0}\subset B_{r_0/2}$, и компонента $\Omega_b\ni0$ этого множества имеет
   $\overline{\Omega_b}\subset\overline{B_{r_0/2}}\subset B_{r_0}$. $Q\ge0$ всюду. На $\overline{\Omega_b}$:
   $$c_1b_1\partial_{b_1}Q+c_2e\,\partial_eQ=(1+\alpha)b_1Q_V'(b_1)+c'h_n(\theta_0)e^2\ge Q_V(b_1)+\tfrac12h_n(\theta_0)e^2=Q,$$
   так как $c'>1$. Итак, $(V_0)$ выполнено с $\delta\in(0,\min(a/2,\delta_2)]$ и $\mu=1\le\beta$. При
   $k_0=2$ ещё $Q\ge\min(c_{k_0}/2,h_n(\theta_0)/2)\lvert b\rvert^2$ на $B_{r_0}$ (здесь $c_{k_0}$ — коэффициент $Q_V$, не
   вес), и неравенство Эйлера выше верно на всём $B_{r_0}$, то есть выполнено и $(V_1)$ с $r_1=r_0/2$.
8. *Вывод.* $(\Phi0)$–$(\Phi3)$ с $C_1=0$, (F) и $(V_0)$ выполнены. По теореме 2 [007] есть
   асимптотическая траектория с указанными свойствами, причём $b(t)$ лежит в компакте
   $\overline{\Omega'_b}\subset B_{r_0}$. Касание: $q=x\,\omega(\vartheta)+\eta\,n(\vartheta)$, где
   $\vartheta-\theta_0=\tau_v(x)+x^\alpha b_1\to0$ и $\lvert\eta\rvert\le\lvert\eta^*\rvert+r_0x^{c'}=o(x)$. Значит,
   $q/\lvert q\rvert\to\omega(\theta_0)$. $\square$

**Замечание 5.1** (почему здесь $C_1=0$, а в (a)/(b) нет). Поворот поля $Y=\Phi_x$ относительно
радиального направления равен $\tilde\kappa=x\tau_v'-x^\alpha b_1$. В узком овраге ($\alpha>0$) он стремится к
нулю **равномерно** по $\lvert b\rvert<r_0$, и вместе с ним уходят все члены кривизны (нормальная кривизна
конуса входит через $\tilde\kappa^2\Psi_{\theta\theta}/x$). Запас Эйлера по углу (вес $c_1=1+\alpha$ против
веса $1$ продольного направления) при этом сохраняется: при фиксированной длине дуги $u$ и убывающем
$x$ масштабированное смещение $b_1=u/x^{1+\alpha}$ растёт, то есть траектория «взбирается» на стенку
сужающегося оврага. В (a)/(b) овраг широкий ($\alpha=0$), и такой поворот имеет порядок $\lvert b\rvert$.

**Замечание 5.2** (численная проверка леммы V). Для D2 ($G\approx2\tau^4$, $g_7'(\pi)\ne0$) лемма V
предсказывает $\tau_v\approx-(s/64)^{1/3}$, $\gamma=1$, $\alpha=1/4$, $Q_V=2b^4$ ($k_0=4$, вырожденный
угловой минимум) и поправки $-2s^{1/12}b^3+0{.}75s^{1/6}b^2$ к профилю. Это подтверждается до
$s=10^{-8}$ (§9.3) [Эксперимент].

## 6. Случаи (a) и (b): лемма M и теорема Mb

### 6.1. Лемма M (перекрёстные члены с постоянными оценками) [Доказано]

Обозначения теоремы A и леммы 2 [007]; $\vartheta_1,\vartheta_2,\vartheta_3$ — это константы $\theta_1,\theta_2,\theta_3$
условия (L3) [007], переобозначенные. Через $L_1=2(a_2+\frac{\beta a_1}2)\sqrt{h_1/a_1}$ и
$L_2=2\sqrt{2a_3/h_0}$ обозначены константы (3.1) [007].

**Лемма M.** Пусть выполнено (D1), а на $D_\sigma=\{q\in\overline D:\ q\ne0,\ \rho(q)<\sigma\}$ —
(L0), (L1) леммы 2 [007] и

- **(L2)** $W\ge-\delta\rho^\beta$ и $\beta W-\rho\,YW\ge\mu W-\varepsilon_1\delta\rho^\beta$, где $\mu\in(0,\beta)$, $\varepsilon_1\ge0$;
- **(L3M)** для всех $q\in D_\sigma$ и $w\perp Y(q)$:
  $\lvert\langle\nabla\rho-Y/h,w\rangle\rvert\le(\vartheta_1+\gamma_1)\lvert w\rvert$,
  $\rho\lvert\langle\nabla_YY,w\rangle\rvert\le(\vartheta_2+\gamma_2)\lvert w\rvert$,
  $\rho\langle w,D_wY\rangle\ge-\vartheta_3\lvert w\rvert^2$, где $\vartheta_i,\gamma_i\ge0$ — постоянные и
  $b':=\beta-\mu-2\vartheta_3>0$.

Положим $\Gamma:=\sqrt2\big[(a_2+\beta\delta)\sqrt{h_1/a_1}\,\gamma_1+\sqrt{2a_3/h_0}\,\gamma_2\big]$. Тогда выполнено
(D4), и

1. если $4\sqrt\delta(\vartheta_1+\gamma_1)\le\sqrt{a_1/h_1}$, то в точках $\overline\Omega$ с $q\ne0$,
   $\rho<\sigma$: $\dot\rho\le-\frac12\sqrt{a_1/h_1}\,\rho^{\beta/2}<0$, то есть выполнено (A4);
2. в каждой точке множества из (A5)
   $$\frac\rho\lambda\,\Xi\ \ge\ \delta\rho^\beta\Big[\mu-\varepsilon_1-\frac{\Gamma^2}{4b'\delta}-\frac{L_1\vartheta_1+L_2\vartheta_2}{\sqrt\delta}\Big]. \tag{6.1}$$
   В частности, (A5) выполнено, если скобка положительна.

*Доказательство.*

1. (D4) и оценки $K_\perp\le2\delta\rho^\beta$, $\lvert v_\perp\rvert\le2\sqrt\delta\rho^{\beta/2}$,
   $\lambda\ge\sqrt{a_1/h_1}\rho^{\beta/2}$ на $\overline\Omega\cap\{0<\rho<\sigma\}$ — дословно пп. 1–2 доказательства
   леммы 2 [007]. Там используется только (L0), (L1) и $W\ge-\delta\rho^\beta$. По (1.1) [007]
   $\dot\rho=-\lambda+\langle\nabla\rho-Y/h,v_\perp\rangle$, и так как $v_\perp\perp Y$, то
   $\lvert\langle\nabla\rho-Y/h,v_\perp\rangle\rvert\le(\vartheta_1+\gamma_1)2\sqrt\delta\rho^{\beta/2}\le\frac12\sqrt{a_1/h_1}\rho^{\beta/2}$.
   Это п. 1.
2. Точка множества из (A5): $V=\delta\rho^\beta$, $K:=K_\perp=\delta\rho^\beta-W\in[0,2\delta\rho^\beta]$,
   $\lvert v_\perp\rvert=\sqrt{2K}$, $\sqrt{a_1/h_1}\rho^{\beta/2}\le\lambda\le\sqrt{2a_3/h_0}\rho^{\beta/2}$ (п. 3 леммы 2
   [007]). Главный член (1.3) [007]:
   $\beta\delta\rho^\beta-\rho YW=\beta K+(\beta W-\rho YW)\ge\beta K+\mu W-\varepsilon_1\delta\rho^\beta$.
3. $\lvert T_1\rvert\le\frac\rho\lambda(a_2+\beta\delta)\rho^{\beta-1}(\vartheta_1+\gamma_1)\sqrt{2K}
   \le(a_2+\beta\delta)\sqrt{h_1/a_1}\,\rho^{\beta/2}\big[\vartheta_1\cdot2\sqrt\delta\rho^{\beta/2}+\gamma_1\sqrt2\sqrt K\big]$.
   При $\delta\le a_1/2$ первое слагаемое не больше $L_1\vartheta_1\sqrt\delta\rho^\beta$.
4. $\lvert T_2\rvert=\lambda\rho\lvert\langle v_\perp,\nabla_YY\rangle\rvert\le\sqrt{2a_3/h_0}\,\rho^{\beta/2}(\vartheta_2+\gamma_2)\sqrt{2K}
   \le L_2\vartheta_2\sqrt\delta\rho^\beta+\sqrt{2a_3/h_0}\,\gamma_2\sqrt2\sqrt K\rho^{\beta/2}$.
   Итак, $\lvert T_1\rvert+\lvert T_2\rvert\le(L_1\vartheta_1+L_2\vartheta_2)\sqrt\delta\rho^\beta+\Gamma\sqrt K\rho^{\beta/2}$.
5. $T_3=\rho\langle v_\perp,D_{v_\perp}Y\rangle\ge-\vartheta_3\lvert v_\perp\rvert^2=-2\vartheta_3K$.
6. Сумма по (1.3) [007]:
   $\frac\rho\lambda\Xi\ge(\beta-2\vartheta_3)K+\mu W-\Gamma\sqrt K\rho^{\beta/2}-\big[\varepsilon_1+\frac{L_1\vartheta_1+L_2\vartheta_2}{\sqrt\delta}\big]\delta\rho^\beta$.
   Так как
   $b'K-\Gamma\sqrt K\rho^{\beta/2}+\frac{\Gamma^2}{4b'}\rho^\beta=\big(\sqrt{b'K}-\frac{\Gamma\rho^{\beta/2}}{2\sqrt{b'}}\big)^2\ge0$, то
   $(\beta-2\vartheta_3)K-\Gamma\sqrt K\rho^{\beta/2}\ge\mu K-\frac{\Gamma^2}{4b'}\rho^\beta$. Наконец
   $\mu K+\mu W=\mu\delta\rho^\beta$ (знак $W$ не важен). Это (6.1). $\square$

**Сравнение с леммой 2 [007]** (З4 R26). Условия лемм несравнимы: лемма M требует $\mu<\beta$ и
$2\vartheta_3<\beta-\mu$, а лемма 2 допускает, например, $\mu=0{.}9\beta$, $\vartheta_3=0{.}1\beta$, где лемма M неприменима.
Верно так: при $2\vartheta_3<\beta-\mu$ член $T_3$ не отнимает от запаса $\mu\delta\rho^\beta$ (он поглощается членом
$\beta K_\perp$). Новое в лемме M: перекрёстные члены $\gamma_i$ входят в скобку квадратично, как
$\Gamma^2/\delta$, а не как $\gamma_i/\sqrt\delta$.

### 6.2. Теорема Mb (отрицательный минимум конечного порядка) [Доказано]

**Теорема Mb.** Пусть $\Sigma_0$ — кривая-компонента, $j<\infty$, $\theta_0\in\mathbb R$ (далее $\theta_0=0$
сдвигом параметра), $G(0)=-a_0<0$ и
$$\Lambda(\theta):=G(\theta)-G(0)=a\,\theta^{2p}\big(1+O(\theta)\big),\qquad a>0,\ p\ge1 .$$
Пусть $c=\frac{j-m+2}2$. Тогда найдётся $\delta_1>0$ такое, что для каждого $\delta\in(0,\delta_1]$ есть
асимптотическая траектория $q(t)=\Psi\big(s(t),\theta(t),s(t)^ce(t)\big)$ с $s(t)\downarrow0$,
$-k_2s^{j/2}\le\dot s\le-k_1s^{j/2}$, $\lvert\theta(t)\rvert\le R_\theta(\delta):=(8\delta/a)^{1/(2p)}$,
$\lvert e(t)\rvert\le4\sqrt{\delta/h_n(0)}$. В частности, $q(t)$ лежит в конусе раствора $O(\delta^{1/(2p)})$
вокруг луча $\mathbb R_+\omega(0)$ и касается конуса $Z=\{u_m=0\}$.

*Доказательство.* Теорема A [007] с полем $Y_\kappa:=\Psi_s-\frac{\kappa\theta}s\Psi_\theta$ и лемма M.

1. *Выбор $r_1$.* Возьмём $r_1\in(0,\min(1,L/4))$ так, что при $\lvert\theta\rvert\le r_1$:
   (r1) $\Lambda(\theta)\ge\frac a2\theta^{2p}$ и $\theta\Lambda'(\theta)\ge\Lambda(\theta)$; это возможно, так как
   $\theta\Lambda'-\Lambda=(2p-1)a\theta^{2p}(1+O(\theta))$;
   (r2) $h_n(\theta)\ge\frac12h_n(0)$ и $\lvert\theta h_n'(\theta)\rvert\le h_n(\theta)$.
2. *Профиль и неравенство Эйлера.* По (2.8) $F_0(\theta,e)=G(\theta)+\frac12h_n(\theta)e^2$,
   $Q:=F_0+a_0=\Lambda(\theta)+\frac12h_n(\theta)e^2\ge0$ при $\lvert\theta\rvert\le r_1$. Для $\kappa\in(0,\frac12]$ и
   $\lvert\theta\rvert\le r_1$:
   $$\kappa\theta\partial_\theta Q+ce\,\partial_eQ=\kappa\theta\Lambda'+\tfrac\kappa2\theta h_n'e^2+ch_ne^2\ge\kappa\Lambda+\big(c-\tfrac\kappa2\big)h_ne^2\ge\kappa Q, \tag{6.2}$$
   так как $c-\frac\kappa2\ge\frac32-\frac14\ge\frac\kappa2$.
3. *Множество $\Omega_\delta$.* Пусть $\Omega_\delta:=\{(\theta,e):\ \lvert\theta\rvert<r_1,\ \lvert e\rvert<r_1,\ Q<4\delta\}$. На
   квадрате $Q\ge\frac a2\theta^{2p}+\frac{h_n(0)}4e^2$, поэтому
   $\Omega_\delta\subset\{\lvert\theta\rvert<R_\theta,\ \lvert e\rvert<R_e\}$, где $R_\theta=(8\delta/a)^{1/(2p)}$,
   $R_e=4\sqrt{\delta/h_n(0)}$. Выберем $\delta_0\le a_0/2$ так, что $R_\theta,R_e\le r_1/2$ при
   $\delta\le\delta_0$. Тогда $\overline{\Omega_\delta}$ лежит внутри квадрата, и на $\partial\Omega_\delta$ $Q=4\delta$:
   граничная точка не принадлежит $\Omega_\delta$, но лежит внутри квадрата, поэтому $Q\ge4\delta$, а по
   непрерывности $Q\le4\delta$.
4. *Данные теоремы A.* $\beta:=j$, $A(r):=a_0r^j$ на $(0,\sigma_0)$, $\sigma_0:=s_2$, где, как в теореме Mc, п. 1,
   $s_2^{c-1}<y_1/4$ и $\sqrt2s_2<r$ (З1 R26);
   $\mathcal G:=\{\Psi(s,\theta,s^ce):\ 0<s<s_2,\ \lvert\theta\rvert<r_1,\ \lvert e\rvert<1\}\subset B_r\setminus0$ (открыто, $\Psi$ на нём
   инъективна, так как $2r_1<L$); число $\sigma$ теоремы A — это $\sigma_*$; $\rho:=s\circ\Psi^{-1}$, $Y:=Y_\kappa\circ\Psi^{-1}$, где
   $$Y_\kappa=\Psi_s-\frac{\kappa\theta}s\Psi_\theta=\omega-\kappa\theta(1-\varepsilon)T+\psi\,n,\qquad \psi:=\eta^*_s-\frac{\kappa\theta\eta^*_\theta}s, \tag{6.3}$$
   — формула (10.2) [008], проверена заново в `frames_mb.py`. $Y\rho=1$, так как $Y_\kappa s=1$. Функция
   $\chi(\sigma)$ — как в теореме Mc, но с супремумом по $\lvert\theta\rvert\le r_1$, $\lvert e\rvert\le1$ и со
   слагаемым $\lvert\partial_\theta F-\partial_\theta F_0\rvert$. $F$ аналитична в окрестности компакта
   $[0,\sigma_0^{1/2}]\times[-r_1,r_1]\times[-1,1]$ (по (2.7), так как $\sigma^{j-m}\lvert e\rvert<y_1/2$), откуда $\chi(\sigma)\to0$
   (З2 R26). Область
   $$\mathcal D:=\{(s,\theta,e):\ 0<s<\sigma_*,\ (\theta,e)\in\Omega_\delta,\ F(s^{1/2},\theta,e)+a_0<\delta\},\qquad D:=\Psi(\{(s,\theta,s^ce):\ (s,\theta,e)\in\mathcal D\})$$
   **не зависит от $\kappa$**; от $\kappa$ зависит только $Y$. (D1)–(D3) проверяются дословно как в
   пп. 4–6 доказательства теоремы Mc: предельные точки $(\bar\theta,\bar e)$ лежат в
   $\overline{\Omega_\delta}\subset\{\lvert\theta\rvert\le r_1/2,\ \lvert e\rvert\le r_1/2\}$, то есть внутри области карты, а граница по
   $\theta$ — часть $\partial\Omega_\delta$, где $Q=4\delta$.
5. *(L0), (L1), (L2).* (L0): $a_1=a_3=a_0$, $a_2=ja_0$, $\delta\le a_0/2$. (L1): по (6.3)
   $h=1+\kappa^2\theta^2(1-\varepsilon)^2+\psi^2\in[1,\frac32]$ при $\lvert\varepsilon\rvert,\lvert\psi\rvert\le\frac14$ (малое $s_2$),
   $h_0=1$, $h_1=\frac32$. (L2): как в теореме Mc, но теперь $Y_\kappa$ в координатах
   $(s,\theta,\zeta)$ — это $\partial_s-\frac{\kappa\theta}s\partial_\theta$, и
   $$\beta W-\rho\,YW=s^j\big[\kappa\theta\,\partial_\theta F+c\,e\,\partial_eF-\tfrac\sigma2\partial_\sigma F\big]. \tag{6.4}$$
   По (6.2) правая часть не меньше $s^j[\kappa Q-(\kappa r_1+c+\frac12)\chi]$. Так как
   $\kappa W\le\kappa s^j(Q+\chi)$, (L2) выполнено с $\mu:=\kappa<\beta$ и $\varepsilon_1:=(c+2)\chi/\delta$; кроме того,
   $W\ge-\chi s^j\ge-\delta\rho^j$.
6. *(L3M).* Пусть $q\in D_\sigma$ (там $\lvert\theta\rvert\le R_\theta$, $\lvert e\rvert\le R_e$, $s<\sigma_*$), $w\perp Y$,
   $w=w_\omega\omega+w_TT+w_nn$. Из $\langle Y,w\rangle=0$:
   $w_\omega=\kappa\theta(1-\varepsilon)w_T-\psi w_n$. Отсюда
   - $\lvert\langle\nabla\rho-Y/h,w\rangle\rvert=\lvert w_\omega\rvert\le(\frac54\kappa R_\theta+\lvert\psi\rvert)\lvert w\rvert$:
     $\gamma_1:=\frac54\kappa R_\theta$, $\vartheta_1:=\sup\lvert\psi\rvert$;
   - по формуле (проверена символьно, `frames_mb.py`)
     $$s\,D_YY=-\kappa^2\theta^2(1-\varepsilon)\,\omega+\kappa\theta\big[s\varepsilon_s-1+\kappa(1-\varepsilon)-\kappa\theta\varepsilon_\theta+\psi k\big]T+\big[s\psi_s+\kappa^2\theta^2(1-\varepsilon)k-\kappa\theta\psi_\theta\big]n \tag{6.5}$$
     главный перекрёстный член $-\kappa(1-\kappa)\theta\,w_T$, квадратичные члены не больше
     $\frac54\kappa^2\theta^2(1+\bar k)\lvert w\rvert$, остальные — не больше
     $(\lvert\varepsilon\rvert+\lvert s\varepsilon_s\rvert+\lvert\varepsilon_\theta\rvert+\lvert\psi\rvert\bar k+\lvert s\psi_s\rvert+\lvert\psi_\theta\rvert)\lvert w\rvert$
     (использовано $\kappa\lvert\theta\rvert\le1$). Итак, $\gamma_2:=\kappa R_\theta+\frac54\kappa^2R_\theta^2(1+\bar k)$, а
     $\vartheta_2$ — супремум последней скобки;
   - по формуле (6.7) ниже: главный член $(\frac1{1-\varepsilon}-\kappa)w_T^2\ge0$, член 4 не больше
     $(\frac54\kappa^2\theta^2+\kappa\lvert\theta\rvert\lvert\psi\rvert)\lvert w\rvert^2$, а члены 2, 3, 5, 6, 7 — малые величины
     (2.6), умноженные на $\lvert w\rvert^2$. Значит,
     $\vartheta_3:=\frac54\kappa^2R_\theta^2+\vartheta_3'$ (на деле хватает $\vartheta_3:=\vartheta_3'$: после подстановки $w_\omega$
     член 4 равен $\kappa^2\theta^2(1-\varepsilon)w_T^2-\kappa\theta\psi\,w_Tw_n$, и первая часть неотрицательна, З3 R26), где
     $\vartheta_3':=\sup\big(\lvert s\varepsilon_s\rvert+\lvert s\psi_s\rvert+\lvert\psi\rvert+2(\lvert\varepsilon_\theta\rvert+\lvert\psi\rvert\bar k+\lvert\psi_\theta\rvert)+\bar k(\lvert\eta^*_s\rvert+2\lvert\eta^*_\theta\rvert/s)\big)$.

   Величины $\vartheta_1,\vartheta_2,\vartheta_3'$ стремятся к $0$ при $\sigma_*\to0$ **равномерно по
   $\kappa\in(0,\frac12]$**: $\lvert\psi\rvert\le\lvert\eta^*_s\rvert+\lvert\eta^*_\theta\rvert/s$,
   $s\psi_s=s\eta^*_{ss}-\kappa\theta(\eta^*_{s\theta}-\eta^*_\theta/s)$,
   $\psi_\theta=\eta^*_{s\theta}-\kappa\eta^*_\theta/s-\kappa\theta\eta^*_{\theta\theta}/s$, и всё оценивается через $\nu$ из (2.6).
7. *Выбор констант.* Пусть $C_\Gamma:=\frac{15\sqrt3}8j+4$. Выберем $\delta_1\le\delta_0$ так, что при
   $\delta\le\delta_1$: $\frac54R_\theta(1+\bar k)\le1$, $\frac54R_\theta^2\le\frac18$ и
   $5R_\theta\sqrt\delta\le\frac14\sqrt{2a_0/3}$. Для $\delta\in(0,\delta_1]$ положим
   $$\kappa=\kappa(\delta):=\min\Big\{\frac12,\ \frac{j\,\delta}{2C_\Gamma^2a_0R_\theta(\delta)^2}\Big\}=\min\Big\{\frac12,\ \frac j{2C_\Gamma^2a_0}\Big(\frac a8\Big)^{1/p}\delta^{1-1/p}\Big\}. \tag{6.6}$$
   Тогда $\gamma_2\le2\kappa R_\theta$, и при $\delta\le a_0/2$
   $\Gamma\le\sqrt2\big[\frac32ja_0\sqrt{\frac3{2a_0}}\cdot\frac54\kappa R_\theta+\sqrt{2a_0}\cdot2\kappa R_\theta\big]=C_\Gamma\sqrt{a_0}\,\kappa R_\theta$.
   Наконец выберем $\sigma_*$ так, что $\vartheta_3'\le\frac18$, $\varepsilon_1+(L_1\vartheta_1+L_2\vartheta_2)/\sqrt\delta\le\kappa/4$ и
   $4\sqrt\delta\,\vartheta_1\le\frac14\sqrt{2a_0/3}$. Тогда $\vartheta_3\le\frac14$, $b'=j-\kappa-2\vartheta_3\ge j-1\ge\frac j2$,
   $$\frac{\Gamma^2}{4b'\delta}\le\frac{C_\Gamma^2a_0\kappa^2R_\theta^2}{2j\delta}\le\frac\kappa4,$$
   и скобка в (6.1) не меньше $\kappa-\frac\kappa4-\frac\kappa4=\frac\kappa2>0$. Условие п. 1 леммы M
   выполнено: $4\sqrt\delta(\vartheta_1+\gamma_1)\le\frac14\sqrt{2a_0/3}+5\sqrt\delta\kappa R_\theta\le\frac12\sqrt{a_0/h_1}$.
8. *Вывод.* Лемма M даёт (D4), (A4), (A5), а теорема A [007] — решение в $\overline\Omega$, $q(t)\to0$,
   $v(t)\to0$. Оценки $\dot s$ — как в лемме 2 [007], п. 1 (с $\vartheta_1+\gamma_1$ вместо $\theta_1$). Оценки
   $\theta(t)$, $e(t)$ — из $(\theta,e)\in\overline{\Omega_\delta}$. Касание конуса $Z$: расстояние до $Z$ не больше
   $\lvert\eta\rvert\le\lvert\eta^*\rvert+R_es^c=O(s^{\min(2,c)})$. $\square$

**Порядок выбора констант** корректен: $r_1$ зависит только от $G,h_n$; $\delta_0,\delta_1$ — от
$r_1,a,a_0,h_n(0),\bar k$; $\kappa$ — от $\delta$; $\sigma_*$ — от $\delta,\kappa$. Область $D$ и функция $\chi$
от $\kappa$ не зависят, а малые величины $\vartheta_1,\vartheta_2,\vartheta_3'$ равномерны по $\kappa$.

### 6.3. Формула для $s\langle w,D_wY_\kappa\rangle$ и члены кривизны при $p\ge3$

Для произвольного $w=w_\omega\omega+w_TT+w_nn$ (не только $w\perp Y$) верно тождество

$$
\begin{aligned}
s\langle w,D_wY_\kappa\rangle={}&\underbrace{\Big(\frac1{1-\varepsilon}-\kappa\Big)w_T^2}_{1}+\underbrace{\kappa\theta\,s\varepsilon_s\,w_\omega w_T}_{2}+\underbrace{s\psi_s\,w_\omega w_n}_{3}+\underbrace{\kappa\theta\,w_\omega w_T}_{4}\\
&+\underbrace{\frac{(\kappa\theta\varepsilon_\theta-\psi k)\,w_T^2}{1-\varepsilon}}_{5}+\underbrace{\frac{\psi_\theta\,w_Tw_n}{1-\varepsilon}}_{6}\underbrace{-\kappa\theta k\,w_T\Big(w_\omega\eta^*_s+\frac{w_T\eta^*_\theta}{s(1-\varepsilon)}\Big)}_{7}.
\end{aligned} \tag{6.7}
$$

[Эксперимент: `frames_mb.py`, «s<w,D_wY> = сумма 7 членов: True» для многочленов $k(\theta)$, $\eta^*(s,\theta)$
общего вида; вывод — разложение $w=a^s\Psi_s+a^\theta\Psi_\theta+a^\zeta\Psi_\zeta$ с $a^s=w_\omega$,
$a^\theta=w_T/(s(1-\varepsilon))$, $a^\zeta=w_n-w_\omega\eta^*_s-w_T\eta^*_\theta/(s(1-\varepsilon))$ и производные (10.4) [008].]

В оценке $(\Phi3)$ в [008] (§10.2, п. 5 доказательства теоремы K2) стоит член $\approx4\kappa\bar k\lvert b\rvert$. В (6.7) члены
$\mp\kappa\theta k\,w_Tw_n$ из $a^\theta\partial_\theta Y$ и $a^\zeta\partial_\zeta Y$ **сокращаются**, и линейных по
$\kappa\theta$ членов с немалыми коэффициентами, кроме $4$ (квадратичного после подстановки
$w_\omega=O(\kappa\theta)+O(\psi)$), не остаётся; члены 2, 5, 7 линейны по $\kappa\theta$, но с малыми множителями
$s\varepsilon_s$, $\varepsilon_\theta$, $\eta^*$ (З7 R26). Для доказательства это не важно: лемме M нужно только $2\vartheta_3<\beta-\mu$.

**Члены кривизны при вырожденном минимуме** (п. 2 задания) [Доказано, это часть доказательства
теоремы Mb]. Масштабы: $R_\theta\asymp\delta^{1/(2p)}$, $\kappa\asymp\delta^{1-1/p}$, так что $\kappa R_\theta^2\asymp\delta$.

- $T_2$: кривизна конуса даёт в $\gamma_2$ квадратичный член $\frac54\kappa^2R_\theta^2(1+\bar k)$. Он
  входит в $\Gamma^2/\delta$ как $\kappa^4R_\theta^4/\delta\asymp\kappa^2\delta\ll\kappa$ — при любом $p$.
- $T_3$: $\vartheta_3=\frac54\kappa^2R_\theta^2+o(1)$, а нужно только $2\vartheta_3<\beta-\mu$. Даже с грубой
  оценкой [008] ($\vartheta_3\approx4\kappa\bar kR_\theta$) и учётом $T_3\ge-4\vartheta_3\delta\rho^\beta$ по лемме 2
  получилось бы $16\kappa\bar kR_\theta\ll\kappa$ при малом $\delta$ — тоже при любом $p$.
- Ломает оценку при $p\ge2$ другое: линейная оценка перекрёстных членов в духе леммы 2,
  $L_1\gamma_1/\sqrt\delta\asymp\kappa\delta^{1/(2p)-1/2}$; её отношение к запасу $\mu=\kappa$ равно
  $\delta^{1/(2p)-1/2}\to\infty$ при $\delta\to0$ (а при $p=1$ — константа, которая не обязана быть малой).
  Её и заменяет неравенство о средних в лемме M. При фиксированном $\kappa$ и $p\ge2$ ломается не
  только оценка, но и само (A5) для поля $Y_\kappa$: на модели R26 критическое $\kappa$, выше которого (A5)
  нарушается, ведёт себя как $\kappa_{\rm crit}\approx5{.}4\,\delta^{1/2}$ ($p=2$) и $\approx10{.}9\,\delta^{2/3}$ ($p=3$)
  [Эксперимент: `experiments/reviewer/morse-bott-R26/`, З8 R26]. Так что порядок $\kappa\asymp\delta^{1-1/p}$ в
  (6.6) точен, а константа (6.6) примерно в $10^3$ раз меньше критической. По той же причине не применима теорема 2′ [008]: там $\lvert b\rvert\le\sqrt{Q/\lambda_0}$, а при
  $p\ge2$ этого нет.

**Сравнение с теоремой K2 [008].** При $p=1$ из (6.6) $\kappa$ не зависит от $\delta$,
$\kappa=\min\{\frac12,\frac{ja}{16C_\Gamma^2a_0}\}$ с $a=G''(0)/2$, — того же вида, что (U3) [008]. Теорема Mb
при $p=1$ даёт K2 без теоремы 2′.

### 6.4. Замечание о поле $Y=\partial_x\Phi+Z$ (дополнение ГА)

Главный агент предложил ([Эскиз] ГА) брать $Y=\partial_x\Phi+Z$ с поперечной поправкой $Z$:
теорема A и лемма 2 требуют только $Y\rho=1$. В этой записке это сделано так.

- В теоремах Mb, Mc поле задано прямо в координатах $(s,\theta,\zeta)$: $Y_\kappa=\Psi_s+Z$,
  $Z=-\frac{\kappa\theta}s\Psi_\theta$. Это частный случай предложения ГА с полем $\xi=\kappa\theta\partial_\theta+ce\,\partial_e$
  на $b$-пространстве: по (6.4) оператор Эйлера равен $\xi F-\frac\sigma2\partial_\sigma F$, то есть $\xi F$ с точностью до
  члена $O(\chi)$ (З6 R26).
- Замечание ГА о $T_3$ (учитывать $T_3\ge-2\vartheta_3K_\perp$ через $\beta K_\perp$) я проверил и использовал в лемме M
  (п. 6 доказательства) в форме $2\vartheta_3<\beta-\mu$. Это не то же, что «$\vartheta_3<\beta/2$» из замечания ГА:
  условия совпадают, только если $\mu$ можно взять сколь угодно малым, а уменьшение $\mu$ в (L2) при $W<0$
  не бесплатно — оно добавляет $(\mu-\mu')$ к $\varepsilon_1$ (З5 R26).
- Для (d) обобщение не понадобилось: в карте, следующей за дном, $C_1=0$, и вырожденный угловой
  минимум закрывается проверенным $(V_0)$ теоремы 2. Поперечный профиль (5.6) — сумма одномерного
  углового и невырожденного нормального, так что поле Эйлера с весами $(1+\alpha,c')$ годится, и
  лемма E не нужна.
- Общую лемму с произвольным полем $\xi$ я не формулировал и не доказывал.

## 7. Итоговая теорема M

**Теорема M.** Пусть $n=3$, $U$ вещественно-аналитична в окрестности $0$, $U(0)=0$,
$U=\sum_{k\ge m}u_k$, $m\ge2$, $u_m\ge0$, $u_m\not\equiv0$ (тогда $\nabla U(0)=0$), и
$\Sigma=\{u_m=0\}\cap S^2$ удовлетворяет (K1), (K2). Если $0$ — не точка локального минимума $U$, то у
$\ddot q=-\nabla U(q)$ есть асимптотическая траектория, и равновесие $q=0$ неустойчиво по Ляпунову.
Изолированность критической точки не предполагается. В частности, задача (A) решена при $n=3$ для
всех $U$, у которых младшая форма неотрицательна, а её нулевое множество на сфере — многообразие
Морса–Ботта.

**Статус:** [Доказано]. Опора — [007] и [008] (проверены). Доказательства леммы N, предложения R,
теорем Mb, Mc, Md, лемм M, V прочитаны R26–R28 в первой редакции (ошибок нет). Усиление «без
изолированности» предложено R28 (З1) и состоит в удалении одного шага из предложения R; теоремы Mb,
Mc, Md и K0 изолированности не требуют (это видно из их формулировок и доказательств, см. §8).

*Доказательство.* По предложению R $\Sigma\ne\varnothing$ и реализуется один из случаев:

- (P): асимптотическая траектория по теореме K0 [008] (условия: $u_m(\omega)=0$, $\nabla u_m(\omega)=0$,
  $D^2u_m(\omega)|_{\omega^\perp}\succ0$ по (K2), так как $N_\omega=\omega^\perp$, $j<\infty$, $g_j(\omega)<0$);
- (a/b): теорема Mb в точке $\theta_0$ глобального минимума $G$;
- (c): теорема Mc;
- (d): теорема Md.

Асимптотическая траектория даёт неустойчивость по Ляпунову (теорема A [007], шаг 6:
обратимость). $\square$

**Схема зависимостей** (с дополнениями З7 R28).
- Теорема M ← предложение R ← лемма N ← леммы K1–K3 [008]; предложение R использует ещё
  предложение K4(a), (c) [008] (критерий минимума; для точечных компонент — лемма K1, п. 2);
- (P) ← теорема K0 [008] ← следствие 2 [007];
- теорема Mb ← лемма M ← лемма 1, теорема A [007]; формулы (6.3), (6.5), (6.7);
- теорема Mc ← лемма 2, теорема A [007]; формула для $s\langle w,D_wY\rangle$ при $\kappa=0$ выведена в п. 8;
- теорема Md ← лемма V (Вейерштрасс, Ньютон–Пюизё) и теорема 2 [007].

## 8. Где работают аналитичность и изолированность

1. **Изолированность не используется** (З1 R28). В предложении R нужна только компонента, в трубке
   которой $U<0$; на ней $R\not\equiv0$ из самих отрицательных значений. Теоремы K0, Mb, Mc, Md —
   утверждения о существовании траектории при условиях на струю; изолированности в их формулировках
   и доказательствах нет (R26, R27 проверяли Mb, Md и отметили это в отзывах). Поэтому теорема M
   верна и для неизолированных неминимальных критических точек этого класса (пример R28:
   $U=z^2-x^4$). Требование CLAUDE.md «аналитичность или изолированность должна реально работать»
   выполнено через аналитичность (п. 2).
2. **Аналитичность.**
   - (i) **Конечность $j$** на компоненте, где $U<0$: аналитическая $R\not\equiv0$ имеет конечный порядок
     по $s$ (предложение R, п. 2), и вдоль дна $U\approx s^jG$. Для $C^\infty$ это ломается: $R$ может
     быть плоской и ненулевой ($R=-e^{-1/s}$), и тогда нет ни $j$, ни эффективного потенциала. Здесь
     проходит граница с гладкими примерами: у примеров Пенлеве–Уинтнера и Лалуа все однородные
     части нулевые ([008], замечание 1; по `problem/KNOWN_RESULTS.md`, с первоисточниками не сверено).
   - (ii) **Дихотомия (a/b)/(c):** аналитическая $G$ на окружности либо постоянна, либо её минимумы
     изолированы и имеют конечный порядок $2p$. В теореме Mb используется только (r1):
     $\Lambda\ge\frac a2\theta^{2p}$, $\theta\Lambda'\ge\Lambda$. [Эскиз, R26 §7] Доказательство Mb прошло бы и для гладкой $\Lambda$
     со строгим минимумом и $\theta\Lambda'\ge\Lambda$ (с $R_\theta$ из обращения $\Lambda$); «негладкость» Mb
     — в условии $G(\theta_0)<0$ на конечной струе.
   - (iii) **Каскад (d):** подготовительная теорема Вейерштрасса и ряды Пюизё для полярной кривой
     $\partial_\theta\hat G=0$; сравнимость конечного числа ветвей (лемма V, п. 4: одна ветвь минимума сразу
     для всех малых $s$); конечный порядок глубины $v_{i_*}$ (степенной закон $-as^\gamma$, $F_0(0)<0$);
     конечный многоугольник Ньютона и полиномиальный профиль $Q_V$; аналитичность $F$ по $t=x^{1/N}$.
     [Гипотеза] Для $C^\infty$-функции $\hat G$ минимизатор может бесконечно часто перескакивать с ветви
     на ветвь, глубина может быть плоской, а профиль — не иметь степенного масштаба; тогда ни (F), ни
     $(V_0)$ не получаются.
   - (iv) Нормальная форма (2.3) с аналитическими $y^*$, $M$ даёт (F) с непрерывным продолжением в
     $s=0$ (во всех трёх теоремах).
3. **Чего здесь нет.** Теоремы Mb, Mc, Md не утверждают неустойчивость для гладкого $U$ без условий
   конечного типа. Пример Уреньи (по `problem/KNOWN_RESULTS.md`, не сверено) с ними не конфликтует:
   утверждается лишь существование одной асимптотической траектории, а не тотальная
   неустойчивость.

## 9. Примеры и эксперименты

### 9.1. Лемма I (изолированность по старшим коэффициентам) [Доказано; опора — K4 [008]]

**Лемма I.** Пусть $n=3$, выполнены (K1), (K2), на каждой кривой-компоненте $j<\infty$ и каждый нуль
$\theta_*$ функции $G=g_j|_{\Sigma_0}$ либо регулярен ($G'(\theta_*)\ne0$), либо $g_{j+1}(\theta_*)\ne0$, а в точечных
компонентах $j(\omega)<\infty$. Тогда $0$ — изолированная критическая точка $U$.

*Доказательство.* По предложению K4(b), (c) [008] и следствию K4′ (точечные компоненты) достаточно
показать, что у $F_{\rm fl}=s^j\hat G$ нет критических точек при малых $s>0$. Критичность означает
$\partial_\theta\hat G=0$ и $j\hat G+s\partial_s\hat G=0$. Пусть $(s_k,\theta_k)$ — критические точки, $s_k\to0$,
$\theta_k\to\bar\theta$. Тогда $jG(\bar\theta)=0$ и $G'(\bar\theta)=0$, так что $\bar\theta$ — нерегулярный нуль, и
$g_{j+1}(\bar\theta)\ne0$. Пусть $r\ge2$ — порядок нуля $G$ в $\bar\theta$ ($G\not\equiv0$). Около $\bar\theta$
$\lvert G'(\bar\theta+\tau)\rvert\ge c\lvert\tau\rvert^{r-1}$ и $\lvert G(\bar\theta+\tau)\rvert\le C\lvert\tau\rvert^r$. Из
$\partial_\theta\hat G=G'+O(s)=0$ следует $\lvert\theta_k-\bar\theta\rvert\le C's_k^{1/(r-1)}$, откуда
$G(\theta_k)=O(s_k^{r/(r-1)})=o(s_k)$. Тогда
$0=j\hat G+s\partial_s\hat G=jG(\theta_k)+(j+1)s_kg_{j+1}(\theta_k)+O(s_k^2)=(j+1)s_kg_{j+1}(\bar\theta)+o(s_k)\ne0$ —
противоречие. $\square$

### 9.2. Примеры

Везде $Q_0=x^2+y^2-z^2$, $u_4=Q_0^2$ (у C2, D3 сдвиг $z^3$ даёт $u_5=2Q_0z^3$), $\Sigma=\Sigma_+\cup\Sigma_-$ (окружности $z=\pm\lvert q\rvert/\sqrt2$),
$\omega_\pm(\varphi)=\pm\frac1{\sqrt2}(\cos\varphi,\sin\varphi,1)$, натуральный параметр $\theta=\varphi/\sqrt2$, $k=1$,
$h_n=8$. Ряды $g_k$ — точная арифметика sympy (`examples_mb.py`, функция `fiber_series` из
`experiments/prover/gt3-hardcore/reduced.py`). Числа $g_k$ получены программой [Эксперимент]; типы
случаев и изолированность выводятся из них по лемме I, следствию K4′ [008] или вручную.

| Пример | $U$ | $\Sigma_+$: $j$, $G$ | случай на $\Sigma_+$ | $\Sigma_-$ | изолированность | рад. Четаев |
|---|---|---|---|---|---|---|
| C1 | $Q_0^2-z^6+xz^6$ | $6$, $-\frac18$ | (c) | (c), $G=-\frac18$ | вручную (ниже) | выполнено (числ.) |
| C2 | $(Q_0+z^3)^2-z^7+xyz^6$ | $7$, $-\frac{\sqrt2}{16}$ | (c) | $G=+\frac{\sqrt2}{16}>0$ | K4′ [008] | **нарушено** |
| D1 | $Q_0^2+y^2z^4+xz^6+xyz^5$ | $6$, $\frac{\sin^2\varphi}8$; $g_7(\pi)=-\frac{\sqrt2}{16}$ | (d) у $\varphi=\pi$, $k_0=2$, $\alpha=\frac12$ | (d) у $\varphi=0$ | лемма I | выполнено (числ.) |
| D2s | $Q_0^2+4y^4z^2+xz^6$ | $6$, $\frac{\sin^4\varphi}2$; $g_7(\pi)=-\frac{\sqrt2}{16}$ | (d), $k_0=4$, $\alpha=\frac14$, $\tau_v\equiv0$ | (d) у $\varphi=0$ | вручную; лемма I | не считалось |
| D2 | $Q_0^2+4y^4z^2+xz^6+xyz^5$ | то же, $g_7'(\pi)\ne0$ | (d), $k_0=4$, $\alpha=\frac14$, $\tau_v\approx-(s/64)^{1/3}$ | (d) | лемма I | выполнено (числ.) |
| D3 | $(Q_0+z^3)^2+y^2z^6+xz^8$ | $8$, $\frac{\sin^2\varphi}{16}$; $g_9(\pi)=-\frac{\sqrt2}{32}$ | (d), $k_0=2$, $\beta=9$ | (d) у $\varphi=0$ | лемма I | **нарушено** |
| B | $Q_0^2-z^6+4y^4z^2+xyz^5$ | $6$, $\frac{\sin^4\varphi}2-\frac18$ | (b), $p=2$ у $\varphi=0,\pi$ | (b) | K4′ [008] | выполнено (числ.) |

Пояснения.

- **C1.** $\partial_yU=4yQ_0$; при $y\ne0$ из $Q_0=0$ и $\partial_xU=4xQ_0+z^6=0$ следует $z=0$, тогда
  $x^2+y^2=0$ — противоречие. При $y=0$: $\partial_zU=z(-4Q_0-6z^4+6xz^4)$. Если $z=0$, то
  $\partial_xU=4x^3=0$. Если $z\ne0$, то $Q_0=\frac32z^4(x-1)$, и $\partial_xU=0$ даёт $6x(x-1)=-z^2$, то есть
  $x=O(z^2)$. Но тогда $Q_0=x^2-z^2=-z^2(1+O(z^2))\ne\frac32z^4(x-1)$ при малом $z\ne0$. Итак, $0$
  изолирована [Доказано].
- **D2s.** $\partial_yU=4y(Q_0+4y^2z^2)$. При $y\ne0$: $Q_0=-4y^2z^2$, $\partial_xU=-16xy^2z^2+z^6=0$, и либо $z=0$
  (тогда $Q_0=x^2+y^2=0$ — противоречие), либо $z^4=16xy^2$, $x>0$. Тогда
  $\partial_zU=z(16y^2z^2+8y^4+6xz^4)>0$ — противоречие. При $y=0$ $U=Q_0^2+xz^6$ — как в C1 без $-z^6$:
  $z\ne0$ даёт $x^2-z^2=\frac32xz^4$ и $6x^2z^4+z^6=0$, то есть $z=0$. Итак, $0$ изолирована [Доказано].
- **D1, D2, D3** — по лемме I: нули $G$ на $\Sigma_\pm$ — $\varphi=0,\pi$ (порядка 2 или 4), а там
  $g_{j+1}=\pm\frac{\sqrt2}{16}$ (D1, D2) или $\pm\frac{\sqrt2}{32}$ (D3), то есть $\ne0$ (выписанные $g_k$ —
  `examples_mb.out`, `examples_D3.out`).
- **C2, B** — по следствию K4′ [008]: $0$ — регулярное значение $G$ на обеих окружностях (у C2
  $G\equiv\pm\frac{\sqrt2}{16}$; у B $G=0$ при $\sin^2\varphi=\frac12$, где $G'=2\sin^3\varphi\cos\varphi\ne0$).
- **Не минимум**: во всех примерах есть кривая-компонента с отрицательными значениями
  $F_{\rm fl}$ (C, B: $G<0$; D: $F_{\rm fl}(s,\pi)=s^{j+1}(g_{j+1}(\pi)+O(s))<0$).
- **C2 и D3** — примеры с искривлённым дном ($y^*=\frac{\sqrt2}8s+\dots$), в которых радиальное
  условие Четаева нарушено (§9.4) [Эксперимент], так что классический критерий
  $\langle\nabla U,q\rangle<0$ на $\{U<0\}$ к ним не применим. Неустойчивость для них дают теоремы Mc и Md.
  Другие известные критерии (класс $\mathcal H$, Паламодов 2020, MN89) я не сверял.

### 9.3. Дно каскадного оврага (лемма V) [Эксперимент]

`valley_mb.py`: $F_{\rm fl}(s,\varphi)=\min_\eta U(s\omega+\eta n)$ считается точно (Ньютон по $\eta$, mpmath, 40
знаков), $f=F_{\rm fl}/s^6$. Глобальный минимум $f(s,\cdot)$ на $\lvert\varphi-\pi\rvert<0{.}5$ — сетка и золотое
сечение. Столбцы: $\tau_v=\theta_v-\pi/\sqrt2$; $d/(-as)$ при $a=\frac{\sqrt2}{16}$; отношение профиля
$(f(s,\theta_v+s^\alpha b)-f(s,\theta_v))/s$ к прогнозу $Q_V(b)$ при $b=\frac12,1,2$.

| $s$ | D1: $\tau_v$ (прогноз $-s/4$) | D1: $d/(-as)$ | D1: $P/Q_V$ | D2s: $P/Q_V$ | D2: $\tau_v$ (прогноз $-(s/64)^{1/3}$) | D2: $P/Q_V$ |
|---|---|---|---|---|---|---|
| $10^{-2}$ | $-2{.}491\cdot10^{-3}$ | 1.0018 | 1.002, 0.997, 0.977 | 0.985, 0.879, 0.579 | $-0{.}0524$ ($-0{.}0539$) | 0.35, 0.46, 0.45 |
| $10^{-4}$ | $-2{.}49991\cdot10^{-5}$ | 1.00002 | 1.000, 1.000, 1.000 | 0.998, 0.987, 0.948 | $-0{.}01154$ ($-0{.}01160$) | 0.40, 0.61, 0.75 |
| $10^{-6}$ | $-2{.}5\cdot10^{-7}$ | 1.0000002 | 1.000, 1.000, 1.000 | 1.000, 0.999, 0.995 | $-0{.}002497$ ($-0{.}0025$) | 0.52, 0.72, 0.85 |
| $10^{-8}$ | $-2{.}5\cdot10^{-9}$ | 1.0 | 1.0, 1.0, 1.0 | 1.000, 1.000, 0.999 | $-0{.}000538$ ($-0{.}000539$) | 0.64, 0.80, 0.90 |

Наклон $\log\lvert d\rvert$ по $\log s$ равен $1{.}0000\pm0{.}0003$ ($\gamma=1$) у всех трёх. У D2 сходимость
профиля медленная, как и предсказывает многоугольник Ньютона: поправка
$-2s^{1/12}b^3+0{.}75s^{1/6}b^2$ при $s=10^{-8}$ даёт отношения $0{.}639$, $0{.}802$, $0{.}897$, а
наблюдается $0{.}639$, $0{.}802$, $0{.}896$ (прогноз пересчитан вручную по
$G(\theta_0+\tau)\approx2\tau^4$: $f(s,\tau_v+\tau')-f(s,\tau_v)\approx12\tau_v^2\tau'^2+8\tau_v\tau'^3+2\tau'^4$).

### 9.4. Строгий выход (A5) и радиальное условие Четаева [Эксперимент]

`exit_mb.py`: $\Xi=\frac d{dt}(V-\delta\rho^\beta)$ считается прямым численным дифференцированием вдоль поля
$(v,-\nabla U)$ в $\mathbb R^3$, без тождества (1.3) [007]. Точки стенки $W=(1-\tau)\delta\rho^\beta$ берутся на
лучах из $b=0$ в $b$-координатах карты, $K_\perp=\tau\delta\rho^\beta$,
$\tau\in\{0,10^{-3},10^{-2},0{.}05,0{.}2,0{.}5\}$, 24 направления $v_\perp\perp Y$, 30 значений $s$.
Печатается $\min\frac\rho\lambda\Xi/(\delta\rho^\beta)$; $\eta^*$ — ряд до $s^4$. Положительность означает строгий
выход в проверенных точках. Это не доказательство.

| Область | $(\delta,\sigma)=(0{.}02,\,0{.}01)$ | $(0{.}005,\,0{.}001)$ | ожидаемый запас |
|---|---|---|---|
| Теорема Mc, C2, $Y=\Psi_s$, $\theta$ периодична | 5.0004 | 5.0001 | $\mu=2c=5$ |
| Теорема Md, D2s ($k_0=4$, $(V_0)$) | 4.706 | 4.801 | $\min((1+\alpha)k_0,2c')=5$ |
| Теорема Md, D1 ($\tau_c=-s/4$) | 3.006 | 3.004 | $(1+\alpha)\cdot2=3$ |
| Теорема Md, D3 (60 знаков) | 3.027 | 3.016 | $3$ |
| Теорема Mb, B, $\kappa=0$ | **−0.0088** | **−0.00047** | 0: нет выхода |
| Теорема Mb, B, $\kappa=0{.}003$ | 0.0023 | 0.0111 | $\le4\kappa$ |
| Теорема Mb, B, $\kappa=0{.}02$ | 0.065 | 0.077 | $\le4\kappa$ |
| Теорема Mb, B, $\kappa=0{.}1$ | 0.348 | 0.365 | $\le4\kappa$ |

Выводы. (1) В (c) и (d) запас равен весу Эйлера и от $\sigma$ не зависит. (2) В (b) при $\kappa=0$ выхода
нет, и поворот $\kappa>0$ действительно нужен. Значение (6.6) для B ($j=6$, $a_0=\frac18$, $a=2$, $p=2$):
$\kappa(\delta)\approx0{.}0217\sqrt\delta$, то есть $0{.}0031$ при $\delta=0{.}02$; при $\kappa=0{.}003$ выход уже
строгий. (3) Для D3 при $s\sim10^{-6}$ (значения $U\sim10^{-55}$) 30 знаков недостаточно: получался ложный
минимум $-35{.}6$. При 60 знаках (`DPS=60`) он исчезает.

`chetaev_mb.py` (3000 случайных точек около дна при $s=10^{-2},10^{-3},10^{-4}$, только точки с $U<0$):
у C2 доля точек $\{U<0\}$ с $\langle\nabla U,q\rangle>0$ равна $50/158$, $65/150$, $75/177$, а
$\max\langle\nabla U,q\rangle/\lvert U\rvert$ доходит до $2\cdot10^4$. У D3 — $13/26$, $1/3$, $2/3$ (точек мало: овраг узкий),
отношение до $4\cdot10^6$. У C1, D1, D2, B нарушений нет: $\max\langle\nabla U,q\rangle/\lvert U\rvert\approx-\beta$ ($-6$ у C1, B;
$-7$ у D1, D2; $\beta$ — показатель глубины).

`frames_mb.py`: все тождества (2.5), (5.3), (5.4), (6.3), (6.5), (6.7) — `True` для многочленов
$k(\theta)$, $\eta^*(s,\theta)$, $\tau(x)$ общего вида (`frames_mb.out`).

## 10. Пробелы

1. **Литература в лемме V.** Подготовительная теорема Вейерштрасса (с вещественностью множителей) и
   теорема Ньютона–Пюизё для многочлена Вейерштрасса над сходящимися рядами — стандартные; ссылки
   даны по памяти, с первоисточниками не сверены (R27, З5: форма применения верна, книги не
   открывались).
2. **Проверка.** Первую редакцию прочитали R26–R28, ошибок нет. Правки этой редакции (§12)
   редакционные, кроме усиления «без изолированности» (З1 R28), которое сводится к удалению шага.
   Текст в целом (и правки) независимо не перечитан.
3. **Не утверждается:** касание траекторией луча в случаях (a), (b) (только конус раствора
   $O(\delta^{1/(2p)})$) и в (c) (угол $\theta(t)$ не контролируется, предельного направления может не быть).
   В (d) касание луча доказано.
4. **Вне рамок:** не-Морс–Ботт (вырожденная нормальная форма, $u_8=Q_0^4$), особое $\Sigma$ ($u_4=x^2y^2$),
   $n\ge4$. Здесь ничего не доказано.
5. **Примеры (§9) рецензентами не проверялись.** Числа $g_k$ получены программой (точная арифметика;
   вручную пересчитаны только $g_6$, $g_7$ у D1/D2). Изолированность C1, D2s доказана вручную; D1, D2,
   D3 — по лемме I; C2, B — по K4′ [008]. Для теоремы M изолированность примеров не нужна, она нужна
   только для того, чтобы примеры относились к задаче (A). Нарушение радиального условия Четаева у
   C2, D3 показано только численно.

## 11. Статус

- Лемма N, предложение R: **[Доказано]** (опора — леммы K1–K3, предложение K4 [008]); прочитаны R28.
- Лемма M: **[Доказано]** (новое; опора — лемма 1 и пп. 1–3 доказательства леммы 2 [007]); прочитана
  R26.
- Теорема Mb (случаи (a)+(b)): **[Доказано]** (теорема A [007] + лемма M + лемма N); прочитана R26. От
  теоремы 2′ [008] не зависит.
- Теорема Mc (случай (c)): **[Доказано]** (теорема A и лемма 2 [007] + лемма N); прочитана R28.
- Лемма V: **[Доказано]** при стандартных теоремах Вейерштрасса и Ньютона–Пюизё (не сверены с
  источником); прочитана R27.
- Теорема Md (случай (d)): **[Доказано]** (теорема 2 [007] + лемма V + лемма N); прочитана R27.
- **Теорема M** ($n=3$, $u_m\ge0$, $\Sigma$ Морса–Ботта, $0$ — не локальный минимум ⇒ асимптотическая
  траектория; в частности, (A) в этом классе): **[Доказано]**. Доказательства первой редакции
  прочитаны R26–R28 (ошибок нет). Это проверка агентами, не человеком.
- Лемма I: **[Доказано]** (опора — K4 [008]); рецензентом не читалась. Примеры §9: классификация — из
  точных рядов (компьютерная выкладка); дно оврага, строгий выход, Четаев — **[Эксперимент]**.

## 12. Правки по отзывам R26–R28 (вторая редакция)

**R28** (`notes/reviewer/2026-10-21-morse-bott-M.md`: лемма N, предложение R, теорема Mc, теорема M, §8).

- З1: изолированность убрана из предложения R и теоремы M; $j<\infty$ выводится из отрицательных
  значений и аналитичности (предложение R, п. 2); старый шаг 1 перенесён в замечание 3.1; переписаны
  §0 («Главное», п. 1, 5), §1 (уточнение 1), §7, §8.
- З2: ссылки на записку P9 переведены на нумерацию [008] (шапка, §1–§9).
- З3: ссылка на K0′(b) больше не нужна (шаг удалён); где упоминается — [008], §3.5.
- З4: в §2.1 добавлены [002], [008, §1] и однострочный вывод аналитичности $\Sigma_0$.
- З5: в теореме Mc, п. 1 явно $\sigma_0=s_2$, $\sigma=\sigma_*$, условия на $s_2$ ($s_2^{c-1}<y_1/4$, $\mathcal G\subset B_r$).
- З6: в предложение R добавлен случай $\Sigma=\varnothing$ (п. 1).
- З7: в теореме Mc, п. 8 формула для $s\langle w,D_wY\rangle$ при $\kappa=0$ выведена прямо; схема зависимостей
  §7 дополнена; утверждения о $C^\infty$ в §8 помечены [Эскиз]/[Гипотеза].

**R27** (`...-Md.md`: лемма V, теорема Md).

- З1: в лемме V, п. 3 добавлено $s_4\le t_3^{N_1}$.
- З2: в формулировку леммы V добавлено «$\Gamma$ чётно».
- З3: в теореме Md явно проверены условия леммы V, в том числе $G\not\equiv0$ около $\theta_0$.
- З4: в теореме Md, п. 6 зафиксирован выбор $s_0$.
- З6: в §0 «глобальные угловые минимумы» уточнено: глобальные в окне $\lvert\theta-\theta_0\rvert\le\tau_0$.
- Попутно: оговорка «при $\beta>2$» заменена на $\beta=j+\gamma>m\ge2$; в $(V_1)$ указано $r_1=r_0/2$.

**R26** (`...-Mb.md`: лемма M, теорема Mb, §6.3–§6.4).

- З1: в теореме Mb, п. 4 явно $s_2^{c-1}<y_1/4$, $\mathcal G\subset B_r$, $\sigma=\sigma_*$.
- З2: в п. 4 добавлено, что $F$ аналитична в окрестности компакта, откуда $\chi\to0$.
- З3: в п. 6 отмечено, что хватает $\vartheta_3=\vartheta_3'$.
- З4: фраза «лемма M усиливает лемму 2» заменена корректным сравнением (условия несравнимы).
- З5: в замечании 6.4 уточнено отличие условия $2\vartheta_3<\beta-\mu$ от «$\vartheta_3<\beta/2$».
- З6: в замечании 6.4 «оператор Эйлера равен $\xi F$» — с точностью до $-\frac\sigma2\partial_\sigma F=O(\chi)$.
- З7: в §6.3 «линейных членов не остаётся» уточнено: с немалыми коэффициентами.
- З8: в §6.3 добавлен численный порог $\kappa_{\rm crit}\asymp\delta^{1-1/p}$ из эксперимента R26.
