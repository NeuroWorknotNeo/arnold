# Особая точка $\Sigma$ при $n=3$: овраг у пересечения ветвей нулевого множества ведущей формы

- **Автор:** prover (агент), 21.10.2026. Задание главного агента: при $n=3$ доказать существование
  асимптотической траектории, когда дно оврага сходится по направлению к особой точке $\omega_0$
  множества $\Sigma=\{u_m=0\}\cap S^2$ (пересечению ветвей); разобрать модель
  $U=x^2y^2+\varepsilon z^2(x^4+y^4)-z^6+x^6+y^6$; обобщить на пересечение кратностей $2a,2b$.
- **Опирается на:**
  - [007] = [`results/007-gt3.md`](../../results/007-gt3.md): теорема A, лемма 1 (формулы (0.1), (1.1),
    (1.3)), лемма 2 [Проверено: R16, R17, 21.10.2026];
  - лемма M записки [`notes/prover/2026-10-21-morse-bott.md`](2026-10-21-morse-bott.md), §6.1 (автор —
    prover P11) [Проверено: R26, 21.10.2026,
    [`notes/reviewer/2026-10-21-morse-bott-Mb.md`](../reviewer/2026-10-21-morse-bott-Mb.md)]; в `results/`
    её пока нет;
  - [008] = [`results/008-class-K.md`](../../results/008-class-K.md), теорема K1 — только в замечании о
    примере S1 (§4.5).
  - Литература не используется.
- **Скрипты** [Эксперимент]: [`experiments/prover/singular-sigma/`](../../experiments/prover/singular-sigma/),
  перечень и выводы — §8.
- **Независимой проверки нет.** Всё помеченное [Доказано] ждёт рецензента.

## 0. Итог

| № | Утверждение | Статус |
|---|---|---|
| Теорема S | Любое $n\ge2$, $U\in C^2$. Полярная карта $q=r\omega(\theta)$ около луча $\omega_0$, поле $Y=\partial_r-\frac\kappa r\,\xi(\theta)\cdot\partial_\theta$. Если относительный избыток $\mathcal W=U/r^\beta+a_0$ коэрцитивен по углу и удовлетворяет неравенству Эйлера $-r\partial_r\mathcal W+\kappa\xi\cdot\nabla_\theta\mathcal W\ge\kappa\mu_0\mathcal W-o(1)$, то есть асимптотическая траектория. Сингулярные неотрицательные члены (весовой порядок $<\beta$) разрешены | [Доказано] (теорема A [007] + лемма M) |
| Предложение 3.1 | Модель: $0$ — изолированная критическая точка при любом $\varepsilon$; не минимум; при $\lvert\varepsilon\rvert\le1$ дно — в точности ось $z$; масштабы; крестообразная $\delta$-глубокая область | [Доказано] |
| Теорема 3.2 | Модель: асимптотическая траектория при **любом** $\varepsilon\in\mathbb R$, в конусе раствора $O(\sqrt\delta)$; то же для $U+V$ с любым $V=O(\lvert q\rvert^7)$ класса $C^2$ (симметрия не нужна) | [Доказано] (теорема S) |
| Предложение 3.3 | Модель при $\varepsilon\ge0$: картезианские срезы $\rho=z$, $Y=e_z$, проверенная лемма 2 [007] | [Доказано] |
| Следствие X | Нормальное пересечение ветвей кратностей $2a,2b$, «полюсное доминирование»: $u_j(\omega_0)<0$, эффективные потенциалы вдоль ветвей имеют в $\omega_0$ строгий минимум, младшие члены неотрицательны, опасных перекрёстных членов нет ($2k>m+j$) ⇒ асимптотическая траектория | [Доказано] |
| Следствие X′ | Любая особенность $\Sigma$ в $\omega_0$ (касание ветвей, касп, несколько ветвей), если $u_m\circ\omega$ монотонна вдоль квазиоднородного поля $\xi$ и выполнено полюсное доминирование без перекрёстных членов | [Доказано] |
| Примеры X1, X2, касп, касание | Принадлежность следствиям X, X′; изолированность | [Доказано]; у каспа и касания изолированность — через исключение (базис Грёбнера, sympy) [Эксперимент: точная выкладка] |
| Теорема II | Гиперболическое разрешение креста: $U_{\rm II}=x^2y^2+2xyz^3+\eta z^6+x^6+y^6$ ($0<\eta<1$) и $U_{\rm II}+O(\lvert q\rvert^7)$. Полюс не лежит в овраге, дно — у вершины гиперболы $xy=-z^3$. Нужна **свободная** поправка поля $Y$ | [Доказано] (теорема A + лемма M) |
| §5.4 | Общий случай II (опасный перекрёстный член, $2k\le m+j$) | [Эскиз] |
| §6 | Перечень подслучаев нормального пересечения при $a=b=1$ | I — [Доказано]; II — пример [Доказано], общий [Эскиз]; III–V — [Гипотеза], не разобраны |

**Главное.**

1. **Модель тривиальна, но по неустойчивой причине.** Ось $z$ инвариантна, и на ней есть явная
   асимптотическая траектория (замечание 3.4). Доказательство теоремы 3.2 этим не пользуется и
   переносится на любое возмущение порядка $\ge7$.
2. **Член $x^2y^2$ весового порядка $<\beta$ не мешает.** В полярной форме он даёт сингулярное
   слагаемое $r^{-2}c^4\theta_1^2\theta_2^2$ в $\mathcal W$. Оно нарушает условие (F) [007], но
   неотрицательно и даёт в неравенство Эйлера запас $(\beta-4)$ плюс $4\kappa$. Крест
   ($\delta$-глубокая область гиперболически узка поперёк ветвей) в доказательстве вообще не виден:
   нужна только оценка $\lvert\theta\rvert\le R_\theta(\delta)$.
3. **«Квартичный профиль вдоль ветвей» — свойство картезианских срезов.** В них профиль вдоль ветви
   равен $\varepsilon b^4+b^6$, и $G''+jG=0$ точно. В сферических срезах он квадратичный: $G''=6$.
   Сферические срезы канонически связаны с дном (минимумы $U$ на сферах) и работают при любом
   $\varepsilon$. Картезианские работают только при $\varepsilon\ge0$, но зато с проверенной леммой 2 и
   без $\kappa$-приёма.
4. **Случай I (полюсное доминирование) закрыт.** Следствие X — при нормальном пересечении любых
   кратностей $2a,2b$ (при $a$ или $b\ge2$ — с условием делимости перекрёстной части); следствие X′ — без
   перекрёстных членов при любой особенности $\Sigma$, у которой $u_m\circ\omega$ монотонна вдоль
   квазиоднородного поля (касание, касп, пучок ветвей). Поправки свободного поля здесь не нужны:
   хватает радиального поля с $\kappa$-сжатием (при каспе и касании — с квазиоднородными весами).
5. **Случай II (опасный перекрёстный член) требует свободного поля.** Глубина возникает при выделении
   полного квадрата вдоль семейства гипербол $xy=-z^3$. Поля с постоянными весами — картезианское $e_z$, радиальное и их
   $\kappa$-варианты — либо не сохраняют это семейство, либо сохраняют его с нулевым запасом. Поле
   $z\xi=(3-e)\frac{x\lvert y\rvert}{x+\lvert y\rvert}(1,-1)-ez^3\frac{(y,x)}{x^2+y^2}$ сохраняет семейство и даёт
   запас $2e$. Это лоскутное поле: на рукаве $x\gg\lvert y\rvert$ оно картезианское по $x$ и растягивает
   $y$ с темпом $3-e$, на другом рукаве наоборот. Член $\vartheta_3$ при этом порядка $0{,}6$, и
   проверенная лемма 2 [007] не подходит. Работает лемма M с условием $2\vartheta_3<\beta-\mu$.
6. **Аналитичность и изолированность в доказанных утверждениях не используются.** Это условия на
   конечную струю: хватает $U\in C^{j+1}$. С гладкими контрпримерами противоречия нет (§7). Обе
   гипотезы нужны в недоказанной части: что сходимость дна к особой точке всегда приводит к одному
   из разобранных подслучаев.

## 1. Постановка и что уточнено

**Постановка.** $n=3$, $U$ аналитична около $0$, $U(0)=0$, $\nabla U(0)=0$, $U=\sum_{k\ge m}u_k$,
$u_m\ge0$, $\Sigma=\{u_m=0\}\cap S^2$, $\omega_0\in\Sigma$ — особая точка $\Sigma$. Система
$\ddot q=-\nabla U(q)$. **Асимптотическая траектория** — решение $q(t)\ne0$, $t\ge0$, с $q,\dot q\to0$; из
неё следует неустойчивость по Ляпунову ([007], теорема A, шаг 6).

**Что уточнено.**

1. Гипотеза задания «дно сходится к $\omega_0$» в формулировках теорем не нужна. Теорема A требует
   только локального оврага около луча $\omega_0$, а не того, чтобы он был самым глубоким. Условия
   ниже — локальные условия на струю $U$ около луча $\mathbb R_+\omega_0$. Что дно действительно
   сходится к $\omega_0$, в примерах проверено отдельно: предложение 3.1(c) и [Эксперимент]
   `bottom.py`.
2. Модель рассмотрена при всех $\varepsilon\in\mathbb R$, а не только при малом $\varepsilon>0$.
3. Утверждение задания о квартичном профиле вдоль ветвей верно в картезианских срезах $z=\mathrm{const}$
   и неверно в сферических (п. 3 «Главного»). Оба варианта разобраны.
4. Обобщение (п. 2 задания) сделано в двух видах. Следствие X — нормальное пересечение кратностей
   $2a,2b$ с перекрёстными членами. Следствие X′ — произвольная квазиоднородная особенность без
   перекрёстных членов. Случай, когда перекрёстные члены опасны (II), — теорема II на примере и
   эскиз в общем виде.

**Обозначения.** $B_r=\{\lvert q\rvert<r\}$; $p,h,v_\perp,K_\perp,W,V,\lambda,\Xi$, условия (D1)–(D4), (A4),
(A5), (L0), (L1) — как в [007]. **Гномоническая карта** около $e_z$:
$$\omega(\theta)=c\,(\theta_1,\theta_2,1),\qquad c=c(\theta):=(1+\lvert\theta\rvert^2)^{-1/2},\qquad q=r\omega(\theta)\iff
\theta=(x/z,\ y/z),\ r=\lvert q\rvert\ (z>0).$$
В ней большие круги через $e_z$ — прямые через $0$, ветви $\{x=0\}$, $\{y=0\}$ — оси.

**Лемма M** (записка `morse-bott`, §6.1, [Проверено: R26]; формулировка с точностью до оформления). *Пусть
выполнено (D1), а на $D_\sigma=\{q\in\overline D:\ q\ne0,\ \rho(q)<\sigma\}$ — (L0), (L1) леммы 2 [007] и*

- *(L2) $W\ge-\delta\rho^\beta$ и $\beta W-\rho\,YW\ge\mu W-\varepsilon_1\delta\rho^\beta$, где $\mu\in(0,\beta)$, $\varepsilon_1\ge0$;*
- *(L3M) для всех $q\in D_\sigma$ и $w\perp Y(q)$:
  $\lvert\langle\nabla\rho-Y/h,w\rangle\rvert\le(\vartheta_1+\gamma_1)\lvert w\rvert$,
  $\rho\lvert\langle\nabla_YY,w\rangle\rvert\le(\vartheta_2+\gamma_2)\lvert w\rvert$,
  $\rho\langle w,D_wY\rangle\ge-\vartheta_3\lvert w\rvert^2$, где $\vartheta_i,\gamma_i\ge0$ — постоянные и
  $b':=\beta-\mu-2\vartheta_3>0$.*

*Положим $\Gamma:=\sqrt2\big[(a_2+\beta\delta)\sqrt{h_1/a_1}\,\gamma_1+\sqrt{2a_3/h_0}\,\gamma_2\big]$. Тогда выполнено (D4) и:
(1) если $4\sqrt\delta(\vartheta_1+\gamma_1)\le\sqrt{a_1/h_1}$, то в точках $\overline\Omega$ с $q\ne0$, $\rho<\sigma$
выполнено $\dot\rho\le-\frac12\sqrt{a_1/h_1}\,\rho^{\beta/2}<0$, то есть (A4); (2) в каждой точке множества из
(A5)*
$$\frac\rho\lambda\,\Xi\ \ge\ \delta\rho^\beta\Big[\mu-\varepsilon_1-\frac{\Gamma^2}{4b'\delta}-\frac{L_1\vartheta_1+L_2\vartheta_2}{\sqrt\delta}\Big],\qquad
L_1=2\big(a_2+\tfrac{\beta a_1}2\big)\sqrt{h_1/a_1},\quad L_2=2\sqrt{2a_3/h_0}. \tag{M}$$

## 2. Теорема S (полярный $\kappa$-приём со свободным угловым полем) — [Доказано]

### 2.1. Формулировка

**Теорема S.** Пусть $n\ge2$, $U\in C^2(B_{r_*})$, $U(0)=0$, $\nabla U(0)=0$. Пусть
$\omega:\overline{B_{\theta_0}}\to S^{n-1}$, $\overline{B_{\theta_0}}\subset\mathbb R^{n-1}$, — инъективное погружение класса $C^3$
(в окрестности замкнутого шара), $\omega(0)=\omega_0$; $\Pi(r,\theta):=r\,\omega(\theta)$. Пусть
$\xi\in C^1(\overline{B_{\theta_0}};\mathbb R^{n-1})$, $\lvert\xi(\theta)\rvert\le K\lvert\theta\rvert$ и $\lVert D\xi(\theta)\rVert\le K$. Пусть
$\beta>0$, $a_0>0$, $r_0\in(0,r_*]$, и для $0<r<r_0$, $\lvert\theta\rvert<\theta_0$
$$\mathcal W(r,\theta):=r^{-\beta}\,U\big(r\omega(\theta)\big)+a_0 .$$
Предположим, что есть $p>0$, $\lambda_0>0$, $\mu_0\in(0,1]$, $\kappa_0\in(0,\frac12]$ и функция
$\chi:(0,r_0)\to[0,\infty)$, $\chi(r)\to0$ при $r\to0$, такие, что при всех $0<r<r_0$, $\lvert\theta\rvert<\theta_0$,
$\kappa\in(0,\kappa_0]$:

- **(S1)** $\mathcal W(r,\theta)\ge\lambda_0\lvert\theta\rvert^{2p}-\chi(r)$;
- **(S2)** $-r\,\partial_r\mathcal W(r,\theta)+\kappa\,\xi(\theta)\cdot\nabla_\theta\mathcal W(r,\theta)\ge\kappa\mu_0\,\mathcal W(r,\theta)-\chi(r)$;
- **(S3)** $\mathcal W(r,0)\le\chi(r)$.

Тогда $\beta\ge2$, и найдётся $\delta_*>0$ такое, что при каждом $\delta\in(0,\delta_*]$ есть асимптотическая
траектория $q(t)=r(t)\,\omega(\theta(t))$, $t\ge0$. Для неё $r(t)$ строго убывает к $0$,
$-k_2r^{\beta/2}\le\dot r\le-k_1r^{\beta/2}$ с постоянными $0<k_1\le k_2$ и
$\lvert\theta(t)\rvert\le R_\theta(\delta):=(2\delta/\lambda_0)^{1/(2p)}$ при всех $t$. Равновесие неустойчиво по
Ляпунову.

**Пояснения.**

- (S2) аффинно по $\kappa$, поэтому достаточно проверить его при $\kappa\to0^+$ (то есть
  $-r\partial_r\mathcal W\ge-\chi$) и при $\kappa=\kappa_0$.
- $\mathcal W$ — относительный избыток над глубиной $-a_0r^\beta$. Слагаемое вида $r^{d-\beta}P(\theta)$ с
  $d<\beta$, $P\ge0$, $\xi\cdot\nabla P\ge0$ (член весового порядка $d<\beta$) входит в (S1) с плюсом, а
  в (S2) — с запасом $(\beta-d)r^{d-\beta}P$. Условие (F) [007] для него нарушено, но здесь не нужно.
- При $\xi=\theta$ поле $Y$ — радиальное с $\kappa$-сжатием к лучу $\omega_0$ по всем угловым
  направлениям, как в теореме Mb (одно угловое направление). Общее $\xi$ — «свободное поле»
  (записка ГА `notes/main-agent/2026-10-21-free-Y.md`) для угловых переменных.

### 2.2. Доказательство

1. **Константы.** $M_1:=\max\lVert D\omega\rVert$, $M_2:=\max\lVert D^2\omega\rVert$ (норма билинейного
   отображения), $M_3:=\max\lVert D\omega(\theta)^{-1}\rVert$ — максимумы по $\overline{B_{\theta_0}}$. Здесь
   $D\omega(\theta):\mathbb R^{n-1}\to T_{\omega(\theta)}S^{n-1}$ — изоморфизм, так как $\omega$ — погружение между
   многообразиями одной размерности. Положим $a_1=a_3:=a_0$, $a_2:=\beta a_0$, $h_0:=1$, $h_1:=\frac32$ и
   $$C_\Gamma:=\sqrt2\Big[\tfrac32\beta\sqrt{\tfrac32}\,M_1K+\sqrt2\,K\big(M_1+K(M_1+M_2)\big)\Big].$$
2. **$\beta\ge2$.** По (S3) $U(r\omega_0)=r^\beta(\mathcal W(r,0)-a_0)\le-\frac{a_0}2r^\beta$ при малых $r$. Так как
   $U\in C^2$, $U(0)=0$, $\nabla U(0)=0$, имеем $\lvert U(q)\rvert\le M\lvert q\rvert^2$. Отсюда $\frac{a_0}2r^\beta\le Mr^2$ при
   малых $r$, то есть $\beta\ge2$.
3. **Выбор $\delta_*$, $\kappa$, $\sigma$.** Пусть $\theta_1:=\theta_0/2$ и
   $$\delta_*:=\min\Big\{\frac{a_0}2,\ \frac{\lambda_0\theta_1^{2p}}4,\ \frac{\lambda_0}2,\ \frac{a_0}{6M_1^2K^2}\Big\}.$$
   Пусть $\delta\in(0,\delta_*]$ и $R_\theta:=(2\delta/\lambda_0)^{1/(2p)}$. Тогда $R_\theta\le1$ и
   $R_\theta\le(\theta_1^{2p}/2)^{1/(2p)}<\theta_1$. Положим
   $$\kappa:=\min\Big\{\kappa_0,\ \frac1{2M_1KM_3},\ \frac1{\sqrt2M_1K},\ \frac\beta{8M_2KM_3},\ \frac{\beta\mu_0\,\delta}{2C_\Gamma^2a_0R_\theta^2}\Big\}$$
   (дроби с нулевым знаменателем считаем равными $+\infty$). Выберем $\sigma\in(0,r_0)$ так, что
   $\chi_\sigma:=\sup_{0<r<\sigma}\chi(r)\le\min(\frac\delta2,\frac{\kappa\mu_0\delta}8)$.
4. **Данные теоремы A.** $\Pi$ — $C^3$-диффеоморфизм $(0,r_0)\times B_{\theta_0}$ на открытое множество
   $\mathcal G\subset B_{r_0}\setminus0$. Действительно, $\omega$ — инъективный локальный диффеоморфизм на
   открытое подмножество $S^{n-1}$, а $\Pi^{-1}(q)=(\lvert q\rvert,\omega^{-1}(q/\lvert q\rvert))$. Положим
   $\rho:=\lvert q\rvert$ (так что $\rho\circ\Pi=r$), $A(r):=a_0r^\beta$, $\sigma_0:=r_0$, и определим $Y$ на $\mathcal G$ как
   образ координатного поля $\partial_r-\frac\kappa r\xi(\theta)\cdot\partial_\theta$:
   $$Y\big(\Pi(r,\theta)\big)=D\Pi\Big(1,-\frac{\kappa}{r}\xi\Big)=\omega(\theta)-\kappa\,D\omega(\theta)\,\xi(\theta)=:y(\theta). \tag{2.1}$$
   $Y\in C^1(\mathcal G)$ и $Y\rho=\partial_r(r)=1$. Далее $W=U+A(\rho)$, то есть $W\circ\Pi=r^\beta\mathcal W$.
5. **Область $D$ и (D1)–(D3).** Пусть
   $\mathcal D:=\{(r,\theta):\ 0<r<\sigma,\ \lvert\theta\rvert<\theta_1,\ \mathcal W(r,\theta)<\delta\}$ и $D:=\Pi(\mathcal D)$. Это
   открытое множество, и $D\subset\mathcal G$.
   - (D1). На $D$ выполнено $\rho<\sigma$. Пусть $q=\lim\Pi(r_k,\theta_k)$, $(r_k,\theta_k)\in\mathcal D$. Перейдём к
     подпоследовательности: $r_k\to\bar r\in[0,\sigma]$, $\theta_k\to\bar\theta$, $\lvert\bar\theta\rvert\le\theta_1$. Если
     $\bar r=0$, то $q=0$. Иначе $q=\Pi(\bar r,\bar\theta)\in\mathcal G$, так как $\bar r<r_0$ и
     $\lvert\bar\theta\rvert<\theta_0$. Значит, $\overline D\setminus0\subset\mathcal G$. Далее,
     $\sup\{\lvert q\rvert:\ q\in D,\ \rho<s\}\le s$ и $\rho(q)=\lvert q\rvert\to0$.
   - (D2). Пусть $q\in\partial D\setminus0$ и $\rho(q)<\sigma$. По (D1) $q=\Pi(\bar r,\bar\theta)$ с $\bar r<\sigma$,
     $\lvert\bar\theta\rvert\le\theta_1$, и по непрерывности $\mathcal W(\bar r,\bar\theta)\le\delta$. Если $\lvert\bar\theta\rvert=\theta_1$, то по
     (S1) $\mathcal W\ge\lambda_0\theta_1^{2p}-\chi_\sigma\ge4\delta-\frac\delta2>\delta$ — противоречие. Значит,
     $\lvert\bar\theta\rvert<\theta_1$, и так как $q\notin D$ ($D$ открыто), $\mathcal W(\bar r,\bar\theta)\ge\delta$. Итак,
     $\mathcal W=\delta$, то есть $W(q)=\delta\rho^\beta$.
   - (D3). По (S3) $\mathcal W(r,0)\le\chi_\sigma<\delta$, так что $\Pi(r,0)\in D$ при всех $r<\sigma$.
6. **Оценка угла на $D_\sigma$.** Каждая точка $D_\sigma$ имеет вид $\Pi(r,\theta)$ с $0<r<\sigma$, $\lvert\theta\rvert\le\theta_1$ и
   $\mathcal W\le\delta$ (п. 5). По (S1) $\lambda_0\lvert\theta\rvert^{2p}\le\delta+\chi_\sigma\le2\delta$, то есть $\lvert\theta\rvert\le R_\theta$.
7. **(L0), (L1).** $A=a_0r^\beta$, $\lvert A'\rvert=\beta a_0r^{\beta-1}$ и $\delta\le a_0/2$. Так как $\lvert\omega\rvert\equiv1$, имеем
   $\langle\omega,D\omega\,v\rangle=0$ при всех $v$. Поэтому $h=\lvert y\rvert^2=1+\kappa^2\lvert D\omega\,\xi\rvert^2\in[1,\,1+\kappa^2M_1^2K^2R_\theta^2]\subset[1,\frac32]$.
8. **(L2).** $W\ge-\chi_\sigma r^\beta\ge-\delta\rho^\beta$ по (S1). В координатах
   $\rho\,YW=r\big(\partial_r-\frac\kappa r\xi\cdot\partial_\theta\big)(r^\beta\mathcal W)=r^\beta\big(\beta\mathcal W+r\partial_r\mathcal W-\kappa\xi\cdot\nabla_\theta\mathcal W\big)$,
   откуда по (S2)
   $$\beta W-\rho\,YW=r^\beta\big(-r\partial_r\mathcal W+\kappa\xi\cdot\nabla_\theta\mathcal W\big)\ge r^\beta\big(\kappa\mu_0\mathcal W-\chi_\sigma\big)=\mu W-\varepsilon_1\delta\rho^\beta$$
   с $\mu:=\kappa\mu_0\in(0,\beta)$ и $\varepsilon_1:=\chi_\sigma/\delta\le\kappa\mu_0/8$.
9. **(L3M).** Пусть $q=\Pi(r,\theta)\in D_\sigma$ ($\lvert\theta\rvert\le R_\theta$). Всякий $w\in\mathbb R^n$ однозначно записывается
   как $w=a\,\omega+\tau$, $\tau=D\omega(\theta)(r\alpha)\in T_{\omega}S^{n-1}$, то есть $w=D\Pi(a,\alpha)$. При этом
   $\lvert\tau\rvert\le\lvert w\rvert$ и $\lvert r\alpha\rvert\le M_3\lvert\tau\rvert$. Производные $Y$ — это производные $y(\theta)$ вдоль
   координатных кривых. Поток $Y$ в координатах — $\dot r=1$, $\dot\theta=-\kappa\xi/r$, а
   $Dy(\theta)v=D\omega\,v-\kappa\big[D^2\omega(\xi,v)+D\omega(D\xi\,v)\big]$. Отсюда
   $$r\,D_YY=-\kappa\big[D\omega\,\xi-\kappa D^2\omega(\xi,\xi)-\kappa D\omega(D\xi\,\xi)\big],\qquad
   r\langle w,D_wY\rangle=\lvert\tau\rvert^2-\kappa\big\langle w,D^2\omega(\xi,r\alpha)\big\rangle-\kappa\big\langle\tau,D\omega(D\xi\,r\alpha)\big\rangle. \tag{2.2}$$
   (Во второй формуле $\langle w,D\omega\,v\rangle=\langle\tau,D\omega\,v\rangle$, так как $D\omega\,v\perp\omega$.) [Эксперимент:
   `geom_checks.py` — (2.1), (2.2) и $\langle\omega,D\omega v\rangle=0$ для произвольной аналитической карты и
   нелинейного $\xi$, невязка $<4\cdot10^{-40}$.] Пусть $w\perp Y$.
   - $\nabla\rho=\omega$, поэтому $\langle\nabla\rho-Y/h,w\rangle=\langle\omega,w\rangle=\langle\omega-y,w\rangle=\kappa\langle D\omega\,\xi,w\rangle$ и
     $\lvert\cdot\rvert\le\kappa M_1KR_\theta\lvert w\rvert$: $\vartheta_1:=0$, $\gamma_1:=\kappa M_1KR_\theta$.
   - По (2.2) $\rho\lvert\langle\nabla_YY,w\rangle\rvert\le\kappa\big[M_1K\lvert\theta\rvert+\kappa M_2K^2\lvert\theta\rvert^2+\kappa M_1K^2\lvert\theta\rvert\big]\lvert w\rvert$. Так
     как $R_\theta\le1$ и $\kappa\le1$: $\vartheta_2:=0$, $\gamma_2:=\kappa R_\theta\big(M_1K+K^2(M_1+M_2)\big)$.
   - По (2.2) $r\langle w,D_wY\rangle\ge\lvert\tau\rvert^2(1-\kappa M_1KM_3)-\kappa M_2KR_\theta M_3\lvert\tau\rvert\lvert w\rvert\ge-\kappa M_2KM_3R_\theta\lvert w\rvert^2$
     (здесь $\kappa M_1KM_3\le\frac12$): $\vartheta_3:=\kappa M_2KM_3R_\theta\le\beta/8$.
10. **Применение леммы M.** $b'=\beta-\kappa\mu_0-2\vartheta_3\ge\beta-\frac12-\frac\beta4\ge\frac\beta2$ (так как $\beta\ge2$,
    $\kappa\mu_0\le\frac12\le\frac\beta4$). Поскольку $\delta\le a_0/2$, имеем $a_2+\beta\delta\le\frac32\beta a_0$, и
    $$\Gamma\le\sqrt2\Big[\tfrac32\beta a_0\sqrt{\tfrac3{2a_0}}\,\kappa M_1KR_\theta+\sqrt{2a_0}\,\kappa R_\theta\big(M_1K+K^2(M_1+M_2)\big)\Big]=C_\Gamma\sqrt{a_0}\,\kappa R_\theta,
    \qquad\frac{\Gamma^2}{4b'\delta}\le\frac{C_\Gamma^2a_0\kappa^2R_\theta^2}{2\beta\delta}\le\frac{\kappa\mu_0}4$$
    по выбору $\kappa$. Скобка в (M) не меньше $\kappa\mu_0-\frac{\kappa\mu_0}8-\frac{\kappa\mu_0}4>0$, то есть выполнено
    (A5). Условие п. (1) леммы M: $4\sqrt\delta\,\gamma_1\le2\sqrt\delta M_1K\le\sqrt{2a_0/3}=\sqrt{a_1/h_1}$ по выбору $\delta_*$;
    значит, выполнено (A4). Лемма M даёт также (D4).
11. **Вывод.** По теореме A [007] есть решение $(q(t),v(t))\in\overline\Omega$, $q(t)\ne0$, $q(t)\to0$, $v(t)\to0$. По
    шагу 5 доказательства теоремы A $\rho(q(t))=r(t)$ строго убывает и меньше $\sigma$, так что
    $q(t)\in D_\sigma$ и $\lvert\theta(t)\rvert\le R_\theta$ (п. 6). Оценка сверху на $\dot r$ — п. (1) леммы M с
    $k_1=\frac12\sqrt{2a_0/3}$. Оценка снизу: по (1.1) [007] $\dot r=-\lambda+\langle\nabla\rho-Y/h,v_\perp\rangle$. Здесь
    $\lambda^2h/2=A-V\le(a_0+\delta)r^\beta$ (так как $V\ge W\ge-\delta r^\beta$) и
    $\lvert v_\perp\rvert^2=2(V-W)\le4\delta r^\beta$, поэтому $\dot r\ge-\big(\sqrt{2(a_0+\delta)}+2\sqrt\delta\gamma_1\big)r^{\beta/2}$.
    Неустойчивость — шаг 6 теоремы A. $\square$

**Порядок выбора констант:** $\delta$ ($\le\delta_*$, зависит от данных) → $R_\theta$ → $\kappa$ (зависит от $\delta$) →
$\sigma$ (зависит от $\delta$, $\kappa$). Область $D$ от $\kappa$ не зависит. При $p=1$ последняя дробь в $\kappa$ от
$\delta$ не зависит ($R_\theta^2=2\delta/\lambda_0$); при $p>1$ получаем $\kappa\asymp\delta^{1-1/p}$, как в теореме Mb.

## 3. Модель

$$U_\varepsilon=x^2y^2+\varepsilon z^2(x^4+y^4)-z^6+x^6+y^6,\qquad\varepsilon\in\mathbb R .$$

$u_4=x^2y^2$, $\Sigma=\{x=0\}\cup\{y=0\}$ (два больших круга), особые точки $\pm e_z$. Нормальная кратность
каждой ветви равна $2$, но нормальный гессиан $D^2u_4(\omega)(n,n)=2x^2$ (на ветви $\{y=0\}$) обращается в нуль
в полюсе, так что условие Морса–Ботта там нарушено. $u_5=0$, $u_6=\varepsilon z^2(x^4+y^4)-z^6+x^6+y^6$.

### 3.1. Предложение 3.1 (изолированность, дно, масштабы) — [Доказано]

**(a)** Если $\nabla U_\varepsilon(q)=0$ и $1+2\varepsilon z^2>0$, то $q=0$. В частности, $0$ — изолированная
критическая точка при любом $\varepsilon$ (при $\varepsilon\ge0$ — единственная во всём $\mathbb R^3$).

**(b)** $0$ — не минимум: $U_\varepsilon(0,0,z)=-z^6$.

**(c)** При $\lvert\varepsilon\rvert\le1$: $U_\varepsilon(q)+\lvert q\rvert^6\ge x^2y^2+\lvert q\rvert^4(x^2+y^2)$. Поэтому минимум $U_\varepsilon$ на сфере
$\lvert q\rvert=r$ равен $-r^6$ и достигается **только** в точках $(0,0,\pm r)$: дно оврага — ось $z$, глубина
$-r^6$, $\beta=6$.

**(d)** В гномонической карте ($r=\lvert q\rvert$, $\theta=(x/z,y/z)$, $z>0$)
$$U_\varepsilon(r\omega(\theta))=r^4c^4\theta_1^2\theta_2^2+r^6c^6\big(-1+E(\theta)\big),\quad E:=\varepsilon(\theta_1^4+\theta_2^4)+\theta_1^6+\theta_2^6,$$
$$\mathcal W:=\frac{U_\varepsilon}{r^6}+1=\frac{c^4\theta_1^2\theta_2^2}{r^2}+\Lambda(\theta),\qquad\Lambda:=1-c^6+c^6E=3\lvert\theta\rvert^2+O(\lvert\theta\rvert^4). \tag{3.1}$$
Поэтому $\delta$-глубокая область $\{\mathcal W<\delta\}$ — **крест**:
$\{\Lambda(\theta)<\delta,\ \lvert\theta_1\theta_2\rvert<r\sqrt{\delta-\Lambda(\theta)}/c^2\}$. Его рукава идут вдоль ветвей: угловая длина
$\approx\sqrt{\delta/3}$, то есть конический масштаб, вес $1$. Поперёк ветви рукав гиперболически узок: на
расстоянии $\lvert\theta_1\rvert$ от полюса угловая полуширина равна $r\sqrt{\delta-\Lambda}/(c^2\lvert\theta_1\rvert)$, а линейная —
порядка $\lvert q\rvert^2\sqrt\delta/\lvert\theta_1\rvert$. Центр креста — квадрат $\lvert\theta_i\rvert\lesssim(r^2\delta)^{1/4}$.

**(e) Профили вдоль ветви.** На ветви $\{y=0\}$ ($\omega=(\sin\varphi,0,\cos\varphi)$, $\varphi$ — натуральный
параметр) $j=6$, $G=u_6\vert_\Sigma=\sin^6\varphi-\cos^6\varphi+\varepsilon\cos^2\varphi\sin^4\varphi$, $G(0)=-1$, $G''(0)=6$, и
$G''(0)+jG(0)=0$ **точно**. В картезианских срезах $z=\mathrm{const}$ профиль вдоль ветви равен
$-1+\varepsilon b^4+b^6$ ($b=x/z$): он квартичный при $\varepsilon>0$, а при $\varepsilon<0$ его минимум не в нуле.
Декартова карта развёртки (теорема K1 [008]) здесь не работает уже во втором порядке. В сферических
срезах профиль квадратичный: $\Lambda=3\lvert\theta\rvert^2+\dots$

*Доказательство.*

1. (a) $\nabla U_\varepsilon=\big(2x(y^2+2\varepsilon z^2x^2+3x^4),\ 2y(x^2+2\varepsilon z^2y^2+3y^4),\ 2z(\varepsilon(x^4+y^4)-3z^4)\big)$.
   - Если $x\ne0$ и $y\ne0$, то $y^2=-2\varepsilon z^2x^2-3x^4$ и $x^2=-2\varepsilon z^2y^2-3y^4$. Сумма даёт
     $(x^2+y^2)(1+2\varepsilon z^2)=-3(x^4+y^4)<0$, что невозможно при $1+2\varepsilon z^2>0$.
   - Если $x=0$, $y\ne0$, то $y^2(2\varepsilon z^2+3y^2)=0$ и $z(\varepsilon y^4-3z^4)=0$. При $z=0$ получаем $y=0$ —
     противоречие. При $z\ne0$ имеем $y^2=-\frac23\varepsilon z^2$ (нужно $\varepsilon<0$) и $\varepsilon y^4=3z^4$, то есть
     $\frac49\varepsilon^3=3$ и $\varepsilon>0$ — противоречие.
   - Случай $y=0$, $x\ne0$ симметричен.
   - Если $x=y=0$, то $-6z^5=0$.
   [Эксперимент: `model_checks.py`, разложение градиента и системы — sympy.]
2. (b) очевидно.
3. (c) Пусть $\lvert q\rvert=r$, $s:=x^2+y^2=r^2-z^2$. Тогда $U_\varepsilon+r^6=x^2y^2+B$, где
   $B:=\varepsilon z^2(x^4+y^4)+x^6+y^6+r^6-z^6$. Имеем $r^6-z^6=s(r^4+r^2z^2+z^4)$, а
   $\varepsilon z^2(x^4+y^4)\ge-z^2s^2\ge-r^2z^2s$ (так как $x^4+y^4\le s^2\le sr^2$). Значит,
   $B\ge s(r^4+z^4)\ge sr^4$, и $U_\varepsilon+r^6\ge x^2y^2+r^4(x^2+y^2)$, причём равенство нулю возможно лишь при
   $x=y=0$.
4. (d) Подстановка $x=rc\theta_1$, $y=rc\theta_2$, $z=rc$ [Эксперимент: `model_checks.py`, «полярная форма
   верна: True»]. Ряд $\Lambda$ — разложение $(1+t)^{-3}$. Описание креста — переписанное неравенство $\mathcal W<\delta$.
5. (e) прямое вычисление: $G=u_6(\sin\varphi,0,\cos\varphi)$, так как $u_5=0$ (поправка сдвига $\eta^*$ к $g_6$
   пропорциональна $(\partial_nu_5)^2=0$, [008] §3.3); далее $G''(0)=6$ и $G(0)=-1$.
   [Эксперимент: `bottom.py` — длина рукава $0{,}0579$ при прогнозе $\sqrt{\delta/3}=0{,}0577$ ($\delta=0{,}01$) и
   отношение полуширины к прогнозу $1{,}0009$ при $r=10^{-6}$.] $\square$

### 3.2. Теорема 3.2 (асимптотическая траектория в модели) — [Доказано]

**Теорема 3.2.** Для каждого $\varepsilon\in\mathbb R$ функция $U_\varepsilon$ удовлетворяет условиям теоремы S в
$\omega_0=e_z$ (и в $-e_z$) с гномонической картой, $\xi=\theta$ ($K=1$), $\beta=6$, $a_0=1$, $p=1$, $\lambda_0=2$,
$\mu_0=1$, $\kappa_0=\frac12$, $\chi\equiv0$, $\theta_0=\theta_0(\varepsilon):=\min\{\frac12,(9+\lvert\varepsilon\rvert)^{-1/2}\}$. Следовательно,
при каждом малом $\delta>0$ есть асимптотическая траектория в конусе $\lvert\theta\rvert\le\sqrt\delta$ вокруг луча
$\mathbb R_+e_z$, и равновесие неустойчиво по Ляпунову.

Более того, то же верно для $U=U_\varepsilon+V$, где $V\in C^2$ около $0$ — любая функция с
$\lvert V(q)\rvert\le C_V\lvert q\rvert^7$ и $\lvert\nabla V(q)\rvert\le C_V\lvert q\rvert^6$ (с $\chi(r)=C'r$). Симметрия, прямолинейность дна и
изолированность для этого не нужны.

*Доказательство.*

1. **(S1).** Пусть $t:=\lvert\theta\rvert^2\le t_0:=(9+\lvert\varepsilon\rvert)^{-1}$. Для $f(t)=(1+t)^{-3}$ имеем $f'''<0$ при $t\ge0$,
   поэтому по формуле Тейлора $f(t)\le1-3t+6t^2$, то есть $1-c^6\ge3t-6t^2$. Далее
   $\lvert E\rvert\le\lvert\varepsilon\rvert t^2+t^3$ и $c^6\le1$. Отсюда $\Lambda\ge3t-(7+\lvert\varepsilon\rvert)t^2\ge2t$, и
   $\mathcal W\ge\Lambda\ge2\lvert\theta\rvert^2$.
2. **(S3).** $\mathcal W(r,0)=0$.
3. **(S2).** Прямое дифференцирование [Эксперимент: `model_checks.py`, «тождество Эйлера (S2) для
   модели: True»] даёт
   $$\theta\cdot\nabla_\theta\big(c^4\theta_1^2\theta_2^2\big)=4c^6\theta_1^2\theta_2^2,\qquad
   -r\partial_r\mathcal W+\kappa\,\theta\cdot\nabla\mathcal W-\kappa\mathcal W=(2+4\kappa c^2-\kappa)\frac{c^4\theta_1^2\theta_2^2}{r^2}+\kappa\big(\theta\cdot\nabla\Lambda-\Lambda\big).$$
   Первое слагаемое $\ge0$ при $\kappa\le\frac12$. Для второго:
   $\theta\cdot\nabla(1-c^6)=6t(1+t)^{-4}\ge6t-24t^2$ (неравенство Бернулли),
   $\theta\cdot\nabla(c^6E)=c^6(\theta\cdot\nabla E-6tc^2E)$ и $\theta\cdot\nabla E=4E+2(\theta_1^6+\theta_2^6)$. Поэтому
   $$\theta\cdot\nabla\Lambda-\Lambda=6t(1+t)^{-4}-(1-c^6)+c^6\big[(3-6tc^2)E+2(\theta_1^6+\theta_2^6)\big]\ge6t-24t^2-3t-3\lvert E\rvert\ge3t-(27+3\lvert\varepsilon\rvert)t^2\ge0 .$$
   Здесь использованы $1-c^6\le3t$ (Бернулли), $0\le3-6tc^2\le3$ и $t\le t_0$. Итак, (S2) выполнено с
   $\mu_0=1$, $\chi\equiv0$ при всех $\kappa\in(0,\frac12]$.
   [Эксперимент: на сетке $\lvert\theta\rvert^2\le t_0$ при $\varepsilon\in\{-2,-1,-0{,}1,0,0{,}1,1,2\}$ минимум
   $(\Lambda-2t)/t$ равен $0{,}39$–$0{,}60$, а минимум $(\theta\cdot\nabla\Lambda-\Lambda)/t$ — $1{,}39$–$1{,}89$.]
4. Теорема S даёт траекторию. Для $-e_z$ — то же в карте $c(\theta_1,\theta_2,-1)$: $U_\varepsilon$ чётна по $z$.
5. **Возмущение.** Пусть $\mathcal W_V:=\mathcal W+r^{-6}V(r\omega)$. В конусе $\lvert\theta\rvert<\theta_0$ при $r<r_0$:
   $\lvert r^{-6}V\rvert\le C_Vr$;
   $\lvert r\partial_r(r^{-6}V(r\omega))\rvert=\lvert-6r^{-6}V+r^{-5}\langle\nabla V,\omega\rangle\rvert\le7C_Vr$;
   $\lvert\theta\cdot\nabla_\theta(r^{-6}V(r\omega))\rvert=r^{-5}\lvert\langle\nabla V,D\omega\,\theta\rangle\rvert\le M_1\theta_0C_Vr$.
   Поэтому (S1)–(S3) для $\mathcal W_V$ выполнены с $\chi(r)=C'r$, $C'=(1+7+\frac12M_1\theta_0)C_V$. $\square$

### 3.3. Предложение 3.3 (картезианское доказательство при $\varepsilon\ge0$) — [Доказано]

**Предложение 3.3.** Пусть $\varepsilon\ge0$, $0<\delta\le\frac18$, $0<\sigma<1$. Возьмём
$\mathcal G=\{0<z<1,\ x^2+y^2<z^2\}$, $\rho=z$, $Y=e_z$, $A(z)=z^6$ и
$D=\{q\in\mathcal G:\ z<\sigma,\ W<\delta z^6\}$, где $W=U_\varepsilon+z^6=x^2y^2+\varepsilon z^2(x^4+y^4)+x^6+y^6$. Тогда
выполнены условия леммы 2 [007] с $\mu=4$, $\varepsilon_1=0$, $\theta_1=\theta_2=\theta_3=0$, и теорема A [007] даёт
асимптотическую траекторию в конусе $x^2+y^2\le(4\delta)^{1/3}z^2$.

*Доказательство.*

1. $\nabla\rho=e_z=Y$, $h=1$, $DY=0$. Значит, $\lvert\nabla\rho-Y/h\rvert=0$, $\nabla_YY=0$, $D_wY=0$, и (L1), (L3)
   выполнены с $h_0=h_1=1$, $\theta_i=0$. (L0): $a_1=a_3=1$, $a_2=6$, $\delta\le\frac12$.
2. (L2): $W\ge0\ge-\delta\rho^6$ и
   $6W-z\partial_zW=6x^2y^2+4\varepsilon z^2(x^4+y^4)+6(x^6+y^6)\ge4W$ [Эксперимент: `model_checks.py`,
   «$6W-zW_z-4W=2x^6+2x^2y^2+2y^6$»].
3. (D1)–(D3). Если $q\in\overline D$, $q\ne0$, то $z>0$ (при $z=0$ из $x^2+y^2\le z^2$ следует $q=0$) и
   $(x^2+y^2)^3\le4(x^6+y^6)\le4W\le4\delta z^6$, то есть $x^2+y^2\le(4\delta)^{1/3}z^2<z^2$. Поэтому
   $\overline D\setminus0\subset\mathcal G$, и граница $D$ внутри $\{z<\sigma\}$ лежит в $\{W=\delta z^6\}$. Это (D1), (D2). (D3) —
   ось $z$ ($W=0$). Ещё $\lvert q\rvert\le\sqrt2z$.
4. Скобка в (3.1) [007] равна $\mu-\varepsilon_1=4>0$, условие п. 1 леммы 2 выполнено ($\theta_1=0$). $\square$

Как и в теореме 3.2, предложение 3.3 переносится на $U_\varepsilon+V$ с $V=O(\lvert q\rvert^7)$, $\nabla V=O(\lvert q\rvert^6)$
(тогда $\varepsilon_1=O(\sigma)/\delta$, и $\sigma$ берётся малым).

**Почему $Y=e_z$ работает без $\kappa$-приёма.** В картезианских срезах профиль
$F_0(b)=\varepsilon(b_1^4+b_2^4)+b_1^6+b_2^6$ (плюс сингулярный член $z^{-2}b_1^2b_2^2$) положительно однороден по
$b=(x,y)/z$, так что оператор $\beta-z\partial_z$ даёт запас по степени по $(x,y)$. При $\varepsilon<0$ в
картезианских срезах $W<0$ около $b_1^2=\frac23\lvert\varepsilon\rvert$: глубина в срезе $z=\mathrm{const}$ больше $z^6$, и
условие $W\ge-\delta\rho^\beta$ леммы 2 нарушено. Тогда нужны сферические срезы и теорема 3.2.

### 3.4. Замечания

- **Инвариантная ось** [Доказано, элементарно]. При $x=y=0$ имеем $\partial_xU=\partial_yU=0$, так что ось $z$
  инвариантна, и на ней $\ddot z=6z^5$. Решение с энергией $0$, $\dot z=-\sqrt2z^3$, то есть
  $z(t)=z_0(1+2\sqrt2z_0^2t)^{-1/2}$, — явная асимптотическая траектория. Это опирается на симметрию и
  ломается от возмущения (например, $U+xz^6+2y^2z^5$: дно уходит с оси вдоль ветви $\{y=0\}$ на угол
  $\theta_1=-r/6$, [Эксперимент: `bottom.py`, $6\theta_1/r=-1{,}000000$ при $r=10^{-6}$]). Теорема 3.2 это возмущение
  покрывает.
- **$\kappa$-сжатие нужно** [Эксперимент: `exit_model.py`]. При $\kappa=0$ (чисто радиальное поле) на лучах
  точно вдоль ветвей запас равен нулю: $\min\frac\rho\lambda\Xi/(\delta\rho^6)\approx10^{-23}$. Для возмущённой модели он
  отрицателен ($-0{,}17$ и $-0{,}036$). При $\kappa=0{,}05;0{,}2;0{,}5$ он равен $\approx2\kappa$ ($0{,}099$; $0{,}375$; $0{,}85$), что
  совпадает с главным членом $\kappa\,\theta\cdot\nabla\Lambda\approx2\kappa\Lambda$.

## 4. Обобщение: пересечение ветвей при полюсном доминировании

### 4.1. Следствие X (нормальное пересечение кратностей $2a,2b$) — [Доказано]

**Данные.** $n=3$, $U\in C^{j+1}$ около $0$ (например, аналитична), $U=\sum_{k=m}^ju_k+O(\lvert q\rvert^{j+1})$, $u_m\ge0$.
$\omega_0\in\Sigma$, $\omega:\overline{B_{\theta_0}}\to S^2$ — аналитическая карта (инъективное погружение около
замкнутого круга), $\omega(0)=\omega_0$, $p_k:=u_k\circ\omega$. Целые $a,b\ge1$, $P(\theta):=\theta_1^a\theta_2^b$.

- **(X0)** $p_m=P^2e$, где $e\in C^1(\overline{B_{\theta_0}})$, $e\ge e_0>0$.
- **(X1)** При $m<k<j$: $p_k=q_k+P\,n_k$, где $q_k,n_k\in C^1(\overline{B_{\theta_0}})$, $q_k\ge0$, $q_k(0)=0$,
  $\theta\cdot\nabla q_k\ge-C_qq_k$, и **$n_k\equiv0$ при $2k\le m+j$**.
- **(X2)** $p_j=-a_0+\Lambda_1(\theta_1)+\Lambda_2(\theta_2)+P\,n_j$, где $a_0>0$, $n_j\in C^1$, $\Lambda_i\in C^1$, и при
  $\lvert t\rvert<\theta_0$: $\Lambda_i(t)\ge\alpha_i\lvert t\rvert^{2p_i}$ ($\alpha_i,p_i>0$) и $t\Lambda_i'(t)\ge\Lambda_i(t)$.

**Следствие X.** При (X0)–(X2) выполнены условия теоремы S с $\beta=j$, $\xi=\theta$, $p=\max(p_1,p_2)$,
$\mu_0=1$ и $\chi(r)=C(r+r^\nu)$, где $\nu:=\min\{2k-m-j:\ m<k\le j,\ n_k\not\equiv0\}>0$ (если таких $k$ нет, то
$\chi=Cr$). Следовательно, есть асимптотическая траектория в конусе раствора $O(\delta^{1/(2p)})$ вокруг луча
$\omega_0$.

**Смысл условий.**

- (X0) означает, что около $\omega_0$ множество $\Sigma$ — две гладкие трансверсальные ветви
  $\omega(\{\theta_1=0\})$ и $\omega(\{\theta_2=0\})$, вдоль которых $u_m$ обращается в нуль ровно в порядках $2a$ и $2b$,
  включая сам $\omega_0$ ($e(0)>0$). Карта существует, если ветви гладкие и трансверсальны и
  $u_m\vert_{S^2}=A^{2a}B^{2b}e$ с локальными определяющими функциями $A,B$ ветвей и $e(\omega_0)>0$: тогда
  $\theta:=(A,B)$.
- (X2) — **эффективные потенциалы вдоль ветвей имеют строгий минимум в точке пересечения**, а
  $u_j(\omega_0)=-a_0<0$ («полюс лежит в овраге»). Для аналитической $\Lambda_i$ из строгого локального минимума
  в $0$ следуют $\Lambda_i(t)=\alpha_it^{2p_i}(1+O(t))$, $\alpha_i>0$, и, значит, обе оценки (X2) при малом $\theta_0$. При
  $a=b=1$ разложение (X2) существует всегда: $\Lambda_i(t):=p_j(te_i)+a_0$, а
  $p_j-p_j(\theta_1,0)-p_j(0,\theta_2)+p_j(0)$ обращается в нуль на обеих осях и потому делится на
  $\theta_1\theta_2$. При $a\ge2$ или $b\ge2$ делимость перекрёстной части на $\theta_1^a\theta_2^b$ — условие.
- (X1): младшие члены неотрицательны («поднимают» ветви, сужая овраг). Перекрёстные члены $P\,n_k$
  разрешены, только если $2k>m+j$: выделение полного квадрата
  $r^mP^2e+r^kPn_k=r^me\big(P+\frac{r^{k-m}n_k}{2e}\big)^2-\frac{r^{2k-m}n_k^2}{4e}$ даёт выигрыш порядка $r^{2k-m}$,
  который мельче глубины $r^j$. При $2k\le m+j$ этот член опасен (случай II, §5). При $a=b=1$ и
  аналитических $q_k$ условие $\theta\cdot\nabla q_k\ge-C_qq_k$ выполнено автоматически, если
  $q_k=A_k(\theta_1)+B_k(\theta_2)$ с $A_k,B_k\ge0$ (тогда $tA_k'\ge0$ около $0$).

*Доказательство.*

1. **Разложение.** Пусть $T(q):=U(q)-\sum_{k\le j}u_k(q)$. По формуле Тейлора для $U\in C^{j+1}$
   $\lvert T(q)\rvert\le C_T\lvert q\rvert^{j+1}$ и $\lvert\nabla T(q)\rvert\le C_T\lvert q\rvert^j$. Положим $R(r,\theta):=r^{-j}T(r\omega(\theta))$. Тогда
   $\lvert R\rvert\le C_Tr$,
   $\lvert r\partial_rR\rvert=\lvert-jR+r^{1-j}\langle\nabla T,\omega\rangle\rvert\le(j+1)C_Tr$ и
   $\lvert\nabla_\theta R\rvert=r^{1-j}\lvert D\omega^{\mathsf T}\nabla T\rvert\le M_1C_Tr$. С $a_0$ из (X2)
   $$\mathcal W=r^{m-j}eP^2+P\,N+\sum_{m<k<j}r^{k-j}q_k+\Lambda_1(\theta_1)+\Lambda_2(\theta_2)+R,\qquad N:=\sum_{m<k\le j}r^{k-j}n_k$$
   (при $2k\le m+j$ $n_k\equiv0$). При $r\le1$ имеем $\lvert N\rvert\le C_Nr^{k_n-j}$, где $k_n$ — наименьшее $k$ с
   $n_k\not\equiv0$, и $r^{j-m}N^2\le C_N^2r^\nu$.
2. **(S1).** $r^{m-j}eP^2+PN\ge-\frac{r^{j-m}N^2}{4e}\ge-\frac{C_N^2}{4e_0}r^\nu$, $q_k\ge0$. Кроме того,
   $\Lambda_1+\Lambda_2\ge\alpha(\theta_1^{2p}+\theta_2^{2p})\ge\alpha2^{-p}\lvert\theta\rvert^{2p}$ при $\lvert\theta\rvert<\min(1,\theta_0)$, где $\alpha=\min\alpha_i$,
   $p=\max p_i$; здесь $\lvert t\rvert^{2p_i}\ge\lvert t\rvert^{2p}$ при $\lvert t\rvert\le1$ и $\lvert\theta\rvert^{2p}\le2^p\max(\theta_1^{2p},\theta_2^{2p})$.
   Итак, (S1) выполнено с $\lambda_0=\alpha2^{-p}$.
3. **(S3).** $P(0)=0$, $q_k(0)=0$, $\Lambda_i(0)=0$, поэтому $\mathcal W(r,0)=R(r,0)\le C_Tr$.
4. **(S2)** при $\kappa\le\kappa_0:=\min\{\frac12,\frac1{C_q+1}\}$ и $\mu_0=1$. Разберём слагаемые
   $-r\partial_r\mathcal W+\kappa\theta\cdot\nabla\mathcal W-\kappa\mathcal W$ по частям.
   - $r^{m-j}eP^2$: так как $\theta\cdot\nabla P=(a+b)P$, имеем
     $\theta\cdot\nabla(eP^2)=P^2\big(2(a+b)e+\theta\cdot\nabla e\big)\ge0$ при $\lvert\theta\rvert\le2(a+b)e_0/\lVert\nabla e\rVert_\infty$ (уменьшаем
     $\theta_0$). Вклад не меньше $(j-m-\kappa)r^{m-j}eP^2\ge\frac{j-m}2r^{m-j}eP^2$.
   - $PN$: вклад равен $P\tilde N$, где
     $\tilde N=\sum_kr^{k-j}\big[(j-k)n_k+\kappa\big((a+b-1)n_k+\theta\cdot\nabla n_k\big)\big]$ и $\lvert\tilde N\rvert\le\tilde C_Nr^{k_n-j}$. По
     неравенству о средних
     $\lvert P\tilde N\rvert\le\frac{j-m}4r^{m-j}eP^2+\frac{r^{j-m}\tilde N^2}{(j-m)e_0}\le\frac{j-m}4r^{m-j}eP^2+\frac{\tilde C_N^2}{(j-m)e_0}r^\nu$.
   - $r^{k-j}q_k$: вклад равен $r^{k-j}\big[(j-k)q_k+\kappa(\theta\cdot\nabla q_k-q_k)\big]\ge r^{k-j}q_k\big(1-\kappa(C_q+1)\big)\ge0$.
   - $\Lambda_i$: вклад $\kappa(\theta_i\Lambda_i'-\Lambda_i)\ge0$ по (X2).
   - $R$: вклад $\ge-\big(\lvert r\partial_rR\rvert+\kappa\lvert\theta\rvert\lvert\nabla_\theta R\rvert+\kappa\lvert R\rvert\big)\ge-C_Rr$.

   Сумма не меньше $-\chi(r)$ с $\chi(r):=C_Rr+\frac{\tilde C_N^2}{(j-m)e_0}r^\nu+C_Tr+\frac{C_N^2}{4e_0}r^\nu$ (одна функция
   годится для (S1)–(S3)). Константы не зависят от $\kappa\in(0,\kappa_0]$.
5. Теорема S применима. $\square$

**Замечание X.1 (связь с эффективным потенциалом вдоль ветви)** [Эскиз]. Пусть $b=1$ (на ветви
$\{\theta_2=0\}$ условие Морса–Ботта выполнено вне $\omega_0$: нормальный гессиан $2\theta_1^{2a}e(\theta_1,0)>0$ при
$\theta_1\ne0$) и $q_k(\theta_1,0)\equiv0$ при $k<j$. Тогда $-a_0+\Lambda_1(\theta_1)=u_j(\omega(\theta_1,0))$ должен совпадать с
эффективным потенциалом $g_j$ леммы K1 [008] в точках ветви $\theta_1\ne0$. Довод: минимум
$\mathcal W(r,\theta_1,\cdot)$ по $\theta_2$ равен $\Lambda_1(\theta_1)+O(r^\nu+r)$ по п. 2 доказательства, а $g_k$ — коэффициенты
разложения минимума в слое. Строго я этого не выписывал: срезы $\{\lvert q\rvert=r\}$ и прямые слоя леммы K1
различаются. Для доказательства следствия X это не нужно. Если же $q_k(\theta_1,0)\not\equiv0$ при каком-то
$k<j$, то ветвь имеет свой, меньший $j$ с $G\ge0$ и нулём в $\omega_0$. Это каскад (как случай (d) теоремы
M), сходящийся к точке пересечения; он тоже покрыт следствием X (пример X1).

### 4.2. Следствие X′ (любая квазиоднородная особенность, без перекрёстных членов) — [Доказано]

**Следствие X′.** Пусть $n\ge2$, $U\in C^{j+1}$, $\omega$, $p_k$ — как выше, и $\xi\in C^1$ — поле с $\xi(0)=0$ и
$\lVert D\xi\rVert\le K$ (например, $\xi_w=(w_1\theta_1,\dots,w_{n-1}\theta_{n-1})$, $w_i>0$). Пусть

- **(X′0)** $p_m\ge0$ и $\xi\cdot\nabla p_m\ge-Cp_m$;
- **(X′1)** при $m<k<j$: $p_k\ge0$, $p_k(0)=0$, $\xi\cdot\nabla p_k\ge-Cp_k$;
- **(X′2)** $p_j(0)=-a_0<0$, и $\Lambda:=p_j+a_0$ удовлетворяет $\Lambda\ge\lambda_0\lvert\theta\rvert^{2p}$ и $\xi\cdot\nabla\Lambda\ge\mu_0\Lambda$.

Тогда выполнены условия теоремы S с этим $\xi$, $\beta=j$, $\chi=Cr$, и есть асимптотическая траектория.

*Доказательство.* $\mathcal W=r^{m-j}p_m+\sum_{m<k<j}r^{k-j}p_k+\Lambda+R$, где $R$ — как в п. 1 доказательства
следствия X (с $\lvert\xi\rvert\le K\lvert\theta\rvert$ в оценке вклада $R$). (S1): все слагаемые, кроме $\Lambda$ и $R$,
неотрицательны. (S3): $p_m(0)=0$ (так как $\omega_0\in\Sigma$), $p_k(0)=0$, $\Lambda(0)=0$. (S2) при
$\kappa\le\min\{\frac12,\frac1{2(C+\mu_0)}\}$: вклад $r^{k-j}p_k$ ($m\le k<j$) равен
$r^{k-j}\big[(j-k)p_k+\kappa(\xi\cdot\nabla p_k-\mu_0p_k)\big]\ge r^{k-j}p_k\big(1-\kappa(C+\mu_0)\big)\ge0$; вклад $\Lambda$ — $\kappa(\xi\cdot\nabla\Lambda-\mu_0\Lambda)\ge0$;
вклад $R$ — $\ge-C'r$. $\square$

**Достаточные условия.**

- (X′0) выполнено, если $p_m=e\prod_iF_i^{2a_i}$, $e(0)>0$, и каждая $F_i$ квазиоднородна относительно
  $\xi_w$: $\xi_w\cdot\nabla F_i=d_iF_i$. Тогда $\xi_w\cdot\nabla p_m=p_m\big(\sum2a_id_i+\xi_w\cdot\nabla e/e\big)\ge0$ около $0$.
  Сюда входят пучок прямых через $0$ ($\xi=\theta$), касп $\theta_2^2=\theta_1^3$ ($w=(2,3)$), касание
  $\{\theta_2=0\}\cup\{\theta_2=\theta_1^2\}$ ($w=(1,2)$), а также $e(0)=0$ при нормальном пересечении
  (например, $p_m=\theta_1^2\theta_2^2\lvert\theta\rvert^2$).
- (X′2) при невырожденном $\Lambda$ с гессианом $H\succ0$ выполнено, если $W_wH+HW_w-\mu_0H\succ0$,
  $W_w=\operatorname{diag}(w_i)$ (как в следствии 1 [007]). Для диагональной $H$ годится любое $\mu_0<2\min w_i$.

### 4.3. Примеры — принадлежность [Доказано]

Во всех примерах ниже $0$ — не минимум: $U(0,0,z)<0$ при $z>0$. Карта гномоническая, все
перечисленные $p_k$ получаются подстановкой $x=rc\theta_1$, $y=rc\theta_2$, $z=rc$.

| Пример | $U$ | $m,j$ | Данные | Следствие |
|---|---|---|---|---|
| Модель | $x^2y^2+\varepsilon z^2(x^4+y^4)-z^6+x^6+y^6$ | $4,6$ | $p_4=c^4\theta_1^2\theta_2^2$, $p_5=0$, $\Lambda_i=1-(1+t^2)^{-3}(1-\varepsilon t^4-t^6)$ | X ($a=b=1$) и теорема 3.2 |
| X1 | $x^2y^2+z(x^4+y^4)-z^6+x^6+y^6$ | $4,6$ | $q_5=c^5(\theta_1^4+\theta_2^4)\ge0$, $\theta\cdot\nabla q_5=q_5(4-5c^2\lvert\theta\rvert^2)\ge0$ | X: ветви приподняты, овраг узок и вдоль ветвей |
| X2 | $x^2y^2+xyz^4-z^7+x^8+y^8$ | $4,7$ | $p_6=c^6\theta_1\theta_2$ — перекрёстный, $2k=12>m+j=11$; $\Lambda_i=1-(1+t^2)^{-7/2}$ | X ($\nu=1$) |
| Касп | $(y^2z-x^3)^2-z^8+x^8+y^8$ | $6,8$ | $p_6=c^6(\theta_2^2-\theta_1^3)^2$, $\xi_w=(2\theta_1,3\theta_2)$, $\xi_w\cdot\nabla p_6=p_6\frac{6(2-\theta_2^2)}{1+\lvert\theta\rvert^2}$; $\Lambda=4\lvert\theta\rvert^2+\dots$, $\xi_w\cdot\nabla\Lambda=8\lvert\theta\rvert^2(2+\sin^2a)+\dots$ | X′ |
| Касание | $y^2(yz-x^2)^2-z^8+x^8+y^8$ | $6,8$ | $p_6=c^6\theta_2^2(\theta_2-\theta_1^2)^2$, $\xi_w=(\theta_1,2\theta_2)$, $\xi_w\cdot\nabla p_6=p_6\frac{2(\theta_1^2-2\theta_2^2+4)}{1+\lvert\theta\rvert^2}$; $\Lambda=4\lvert\theta\rvert^2+\dots$, $\xi_w\cdot\nabla\Lambda=8\lvert\theta\rvert^2(1+\sin^2a)+\dots$ | X′ |

(Здесь $\theta=\lvert\theta\rvert(\cos a,\sin a)$. Для X2 $\Lambda_i$ и перекрёстная часть $p_7$ — из $p_7=-c^7$. В каспе и касании
$U$ совпадает с суммой $r^6p_6+r^8p_8$, так что $R\equiv0$.)

*Изолированность.*

- **X1** [Доказано]: $\partial_zU=x^4+y^4-6z^5=0$ даёт $z\ge0$, а при $z=0$ — $x=y=0$. При $z>0$ из
  $\partial_xU=2x(y^2+2zx^2+3x^4)=0$ следует $x=0$, аналогично $y=0$, и тогда $\partial_zU=-6z^5\ne0$. Значит,
  $0$ — единственная критическая точка.
- **X2** [Доказано]: при $z=0$ $\partial_xU=2x(y^2+4x^6)=0$ даёт $x=0$, и $\partial_yU=8y^7=0$. При $z\ne0$
  $\partial_zU=z^3(4xy-7z^3)=0$ даёт $xy=\frac74z^3$, и тогда
  $x\,\partial_xU=2x^2y^2+xyz^4+8x^8=z^6\big(\frac{49}8+\frac74z\big)+8x^8>0$ при $\lvert z\rvert<\frac72$.
- **Касп, касание** [Эксперимент: точная выкладка sympy, `cusp_check.py`, `tangency_check.py`]:
  последний элемент лексикографического базиса Грёбнера идеала $(\partial_xU,\partial_yU,\partial_zU)$ равен
  $z^{16}(8z^4+1)\cdot h(z)$, где $h(0)\ne0$, а корни $h$ по модулю $\ge0{,}25$. Значит, около $0$ любая
  критическая точка имеет $z=0$. При $z=0$ градиент равен $(6x^5+8x^7,\,8y^7,\,\cdot)$ (касп) и
  $(4x^3(2x^4+y^2),\,2y(x^4+4y^6),\,\cdot)$ (касание), откуда $x=y=0$. Сведение к $z=0$ опирается на
  корректность вычисления базиса в sympy.
- Условия (X′0)–(X′2) в каспе и касании: формулы в таблице — точные тождества (sympy), а знаки около $0$
  следуют из них: $\xi_w\cdot\nabla p_6/p_6\to12$ (касп) и $\to8$ (касание), $\xi_w\cdot\nabla\Lambda-\Lambda\ge$ (положительно
  определённая квадратичная форма) $+O(\lvert\theta\rvert^4)$.

### 4.4. Строгий выход на примерах [Эксперимент]

`exit_cor.py` (X1, X2) и `exit_model.py` (модель). Строгий выход — по той же схеме, что в записке
`morse-bott`: (A5) проверяется прямым численным дифференцированием $V-\delta\rho^\beta$ вдоль поля
$(v,-\nabla U)$, а лучи берутся в том числе **точно** по ветвям. При $\kappa=0{,}2$ минимум
$\frac\rho\lambda\Xi/(\delta\rho^\beta)$ положителен: X1 — $0{,}61$ и $0{,}97$, X2 — $0{,}36$ и $0{,}38$. При $\kappa=0$ у X2 он равен
$-0{,}012$ и $\approx-4\cdot10^{-13}$ (на лучах вдоль ветвей запаса нет). У X1 и при $\kappa=0$ он положителен
($0{,}17$; $0{,}42$): при малых $r$ член $r^{-1}q_5$ делает овраг узким и вдоль ветвей.

### 4.5. Пример S1 полигона

$S1=(x^2-y^2)^2+x^5+2y^5+z(x^4+y^4)+z^6$. В полюсах $\pm e_z$ (особые точки $\Sigma$)
$U(0,0,\pm s)=s^6>0$, и там нет оврага. Значит, S1 — **не** пример этой записки, и следствия X, X′ к нему
не относятся. Дно лежит на гладкой дуге $x=y$. Там $j=5$, $G=g_5=\frac18\sin^4\varphi\,(3\sqrt2\sin\varphi+4\cos\varphi)$,
минимум $G(\varphi^*)=-0{,}5730$ в $\varphi^*=4{,}5465$, $G''+5G=0{,}3212>0$, $h_n=8\sin^2\varphi^*>0$
[Эксперимент: `s1_check.py`; совпадает с N4]. Теорема K1 [008] сформулирована для дуги около $\omega^*$ и
глобальной гладкости $\Sigma$ не требует. Поэтому у S1 есть асимптотическая траектория — при условии, что
численные значения $G'(\varphi^*)=0$ и $G''+5G>0$ верны (они получены с 40 знаками, но не интервальной
арифметикой).

## 5. Случай II: гиперболическое разрешение креста

### 5.1. Пример и что в нём иначе

$$U_{\rm II}=x^2y^2+2xyz^3+\eta z^6+x^6+y^6=H^2-(1-\eta)z^6+x^6+y^6,\qquad H:=xy+z^3,\quad0<\eta<1 .$$

$u_4=x^2y^2$ — то же нормальное пересечение в $e_z$, что в модели, но $u_5=2xyz^3$ — перекрёстный член с
$2k=10=m+j$, то есть опасный (следствие X не применимо). Значение в полюсе $u_6(e_z)=\eta>0$: **полюс в
овраг не входит**. Глубина $-(1-\eta)z^6$ возникает при выделении полного квадрата на гиперболе
$xy=-z^3$, которая разрешает крест.

**Предложение 5.1.** (a) [Доказано] $0$ — изолированная критическая точка $U_{\rm II}$ в шаре
$\lvert q\rvert<\big(\frac{1-\eta}{3\eta^2}\big)^{1/3}$, и не минимум. (b) [Эксперимент: `bottom.py`] Дно на сфере
$\lvert q\rvert=r$ — у вершины гиперболы: $\lvert\theta\rvert/\sqrt{2r}\to1$, $\theta_1\theta_2/(-r)\to1$ (при $r=10^{-6}$: $0{,}999999$,
$0{,}999998$). Дно сходится к $e_z$ со скоростью $r^{1/2}$ по углу, в двух квадрантах
$\{x>0,y<0\}$ и $\{x<0,y>0\}$.

*Доказательство (a).* $\partial_zU=6z^2(xy+\eta z^3)$.

- При $z=0$: $\partial_xU=2x(3x^4+y^2)=0$ даёт $x=0$, и $\partial_yU=6y^5=0$.
- При $z\ne0$: $xy=-\eta z^3$. Тогда $\frac x2\partial_xU=3x^6+x^2y^2+xyz^3=3x^6-\eta(1-\eta)z^6$, так что
  $3x^6=\eta(1-\eta)z^6$; аналогично $3y^6=\eta(1-\eta)z^6$. Значит, $\lvert x\rvert=\lvert y\rvert$ и $x^4=x^2y^2=\eta^2z^6$, откуда
  $x^6=\eta^3\lvert z\rvert^9$ и $\lvert z\rvert^3=\frac{1-\eta}{3\eta^2}$.

$U(0,0,z)=\eta z^6>0$, но в точке $(z^{3/2},-z^{3/2},z)$ имеем $U=-(1-\eta)z^6+2z^9<0$.
[Эксперимент: `u2_checks.py`. Без члена $\eta z^6$ ($\eta=0$) вся ось $z$ состоит из критических точек.] $\square$

**Почему не хватает полей из §§2–3.** Пусть $\rho=z$ и $Y=e_z+(\lambda_xx,\lambda_yy,0)/z$ с постоянными
$\lambda$. Тогда $zY(H)=(\lambda_x+\lambda_y)xy+3z^3$. Семейство $\{H=c\,z^3\}$ сохраняется только при
$\lambda_x+\lambda_y=3$, и тогда $\beta H^2-zY(H^2)=0$: запаса нет. Чтобы запас был, нужно $\lambda_x+\lambda_y<3$, но тогда
сдвинутое на $-z^3$ семейство гипербол не сохраняется. Кроме того, рукаву вдоль оси $x$ (профиль $x^6$)
нужно $\lambda_x<1$, а рукаву вдоль $y$ — $\lambda_y<1$, что несовместимо с $\lambda_x+\lambda_y\approx3$. При $Y=e_z$ строгого
выхода нет: $\min\frac\rho\lambda\Xi/(\delta\rho^6)=-20,-36,-54$ [Эксперимент: `exit_u2.py E`].

### 5.2. Теорема II — [Доказано]

**Теорема II.** Пусть $0<\eta<1$, $V\in C^2$ около $0$ и $\lvert V(q)\rvert\le C_V\lvert q\rvert^7$,
$\lvert\nabla V(q)\rvert\le C_V\lvert q\rvert^6$. Тогда у $\ddot q=-\nabla U$, $U:=U_{\rm II}+V$, есть асимптотическая траектория
$q(t)=(x,y,z)(t)$ в квадранте $\{x>0,\ y<0\}$ с $z(t)\downarrow0$, $-k_2z^3\le\dot z\le-k_1z^3$ и
$(xy+z^3)^2+x^6+y^6\le2\delta z^6$ при всех $t$, где $\delta>0$ можно взять сколь угодно малым. При $V\equiv0$ —
и в квадранте $\{x<0,y>0\}$ (симметрия $(x,y)\mapsto(-x,-y)$). Равновесие неустойчиво по Ляпунову.

**Поле.** В квадранте $x>0$, $y<0$ положим $g:=\frac{x\lvert y\rvert}{x+\lvert y\rvert}$, фиксируем $e\in(0,\frac12]$ и
$$Y=(\xi_1,\xi_2,1),\qquad z\,\xi=\underbrace{(3-e)\,g\,(1,-1)}_{z\xi^{(0)}}\ \underbrace{-\,e z^3\,\frac{(y,x)}{x^2+y^2}}_{z\zeta}. \tag{5.1}$$
Эквивалентно $z\xi^{(0)}=(\lambda_xx,\lambda_yy)$ с $\lambda_x=\frac{(3-e)\lvert y\rvert}{x+\lvert y\rvert}$ и $\lambda_y=\frac{(3-e)x}{x+\lvert y\rvert}$, $\lambda_x+\lambda_y=3-e$. На
рукаве $x\gg\lvert y\rvert$ получаем $\lambda_x\to0$, $\lambda_y\to3-e$: поле картезианское по $x$ и растягивает $y$. На
рукаве $\lvert y\rvert\gg x$ — наоборот. Поправка $\zeta$ направлена по $\nabla(xy)$ и добавляет $-ez^3$ к
$zY(xy)$. Выкладки [Эксперимент: `u2_checks.py`, все тождества — `0`/`True`]:
$$zY(H)=(3-e)H, \tag{5.2}$$
$$6W-zYW=2eH^2+6(1-\lambda_x)x^6+6(1-\lambda_y)y^6-6\big(x^5z\zeta_1+y^5z\zeta_2\big)+\big[6V-z(\xi\cdot\nabla_{xy}V+\partial_zV)\big], \tag{5.3}$$
где $W:=U+(1-\eta)z^6=H^2+x^6+y^6+V$.

*Доказательство.* Применяем теорему A [007] и лемму M с $\rho=z$, $\beta=6$, $A(z)=a_0z^6$, $a_0:=1-\eta$.

1. **Данные.** $\mathcal G:=\{0<z<r_1,\ 0<x<z,\ -z<y<0\}$, где $r_1$ мало ($U\in C^2(B_{2r_1})$). На $\mathcal G$
   функции $g$ и $\zeta$ гладкие ($x+\lvert y\rvert>0$, $x^2+y^2>0$), $Y\in C^\infty(\mathcal G)$, $Y\rho=1$, $\lvert q\rvert\le\sqrt3z$, так
   что $\lvert V\rvert\le C'z^7$ и $\lvert\nabla V\rvert\le C'z^6$. Пусть $\delta\in(0,\delta_*]$, $\delta_*:=\min\{\frac{a_0}2,\frac1{32}\}$, и
   $D:=\{q\in\mathcal G:\ z<\sigma,\ W(q)<\delta z^6\}$, где $\sigma\le\min(r_1,\delta/C')$ ещё уменьшится.
2. **(D1)–(D3).** Пусть $q\in\overline D$, $q\ne0$. Если $z=0$, то $x=y=0$ (из $0\le x\le z$, $\lvert y\rvert\le z$). Значит,
   $z>0$. Далее $H^2+x^6+y^6\le\delta z^6+C'z^7\le2\delta z^6$, откуда $x,\lvert y\rvert\le(2\delta)^{1/6}z<z$. Если бы $x=0$, то
   $W=z^6+y^6+V\ge z^6-C'z^7>\delta z^6$; так же при $y=0$. Итак, $\overline D\setminus0\subset\mathcal G$, и граница $D$
   в $\{z<\sigma\}$ лежит в $\{W=\delta z^6\}$. Это (D1), (D2), с $\sup\{\lvert q\rvert:\ q\in D,\ z<s\}\le\sqrt3s$ и
   $\rho\le\lvert q\rvert$. (D3): точки $(z^{3/2},-z^{3/2},z)$ лежат в $\mathcal G$, и в них
   $W=2z^9+V\le2z^9+C'z^7<\delta z^6$ при малом $z$.
3. **Оценки на $D_\sigma$.** $\lvert H\rvert\le\sqrt{2\delta}z^3\le\frac14z^3$, поэтому $x\lvert y\rvert=z^3-H\in[\frac34z^3,\frac54z^3]$, и
   $x^6+y^6\le2\delta z^6$. Отсюда:
   - $\lvert\xi^{(0)}\rvert=\sqrt2(3-e)g/z\le\frac{3}{\sqrt2}\frac{\sqrt{x\lvert y\rvert}}z\le2{,}4z^{1/2}$ (так как $x+\lvert y\rvert\ge2\sqrt{x\lvert y\rvert}$);
   - $\lvert\zeta\rvert=\frac{ez^2}{\sqrt{x^2+y^2}}\le\frac{ez^2}{\sqrt{2x\lvert y\rvert}}\le0{,}9e\,z^{1/2}$;
   - итак, $\lvert\xi\rvert\le3z^{1/2}$.
   - Матрица $D_{xy}(z\xi^{(0)})=(3-e)\begin{pmatrix}a&-b\\-a&b\end{pmatrix}$, $a=\frac{y^2}{(x+\lvert y\rvert)^2}$, $b=\frac{x^2}{(x+\lvert y\rvert)^2}$,
     $a+b\le1$. Её симметричная часть имеет собственные значения
     $\frac{3-e}2\big((a+b)\pm\sqrt{2(a^2+b^2)}\big)\ge-\frac{(3-e)(\sqrt2-1)}2$ [Эксперимент: минимум $-0{,}600608$ при
     $e=0{,}1$ на $2\cdot10^4$ точках, граница $-0{,}600610$], а норма не больше $3\sqrt2$.
   - $D_{xy}(z\zeta)=-ez^3D\frac{(y,x)}{x^2+y^2}$, где $D\frac{(y,x)}{x^2+y^2}=\frac1{(x^2+y^2)^2}\begin{pmatrix}-2xy&x^2-y^2\\y^2-x^2&-2xy\end{pmatrix}$ имеет
     норму $\frac1{x^2+y^2}$. Поэтому $\lVert D_{xy}(z\zeta)\rVert=\frac{ez^3}{x^2+y^2}\le\frac{ez^3}{2x\lvert y\rvert}\le e$.
   - $z\,\partial_z\xi=\partial_z(z\xi)-\xi=3\zeta-\xi=2\zeta-\xi^{(0)}$, так что $\lvert z\partial_z\xi\rvert\le4z^{1/2}$.
4. **(L0), (L1).** $a_1=a_3=a_0$, $a_2=6a_0$, $\delta\le a_0/2$; $h=1+\lvert\xi\rvert^2\in[1,1+9\sigma]\subset[1,\frac32]$.
5. **(L2).** $W\ge-C'z^7\ge-\delta z^6$. Оценим (5.3) снизу.
   - $\zeta$-члены: $x^5z\zeta_1=\frac{ex^5z^3\lvert y\rvert}{x^2+y^2}\le\frac e2x^4z^3$ и $y^5z\zeta_2=\frac{e\lvert y\rvert^5z^3x}{x^2+y^2}\le\frac e2y^4z^3$, поэтому
     $-6(\dots)\ge-3ez^3(x^4+y^4)\ge-6e(2\delta)^{2/3}z^7$.
   - Член с $V$: не меньше $-C''z^7$.
   - Часть с $x^6,y^6$ при $u:=x/\lvert y\rvert\ge4$: она равна $6\lvert y\rvert^6f(u)$,
     $f(u)=\frac{(u-2+e)u^6+1-(2-e)u}{1+u}$, и
     $(u-2+e)u^6+1-(2-e)u\ge\frac u2u^6-2u\ge\big(\frac12-\frac1{2048}\big)u^7$ (так как $u\ge4$). Отсюда
     $f\ge0{,}399u^6\ge0{,}398(u^6+1)$, и часть с $x^6,y^6$ не меньше $2{,}39(x^6+y^6)$. При $u\le\frac14$ — то же
     по симметрии $x\leftrightarrow\lvert y\rvert$ (она переставляет $\lambda_x$ и $\lambda_y$).
   - При $\frac14<u<4$: $\max(x,\lvert y\rvert)^2\le4x\lvert y\rvert\le5z^3$, поэтому $x^6+y^6\le250z^9$, и, так как
     $\lvert1-\lambda\rvert\le3$, часть с $x^6,y^6$ не меньше $-4500z^9$.

   С $\mu:=2e\le1$ получаем
   $6W-zYW\ge\mu(H^2+x^6+y^6)-(4500+500)z^9-6e(2\delta)^{2/3}z^7-C''z^7$. Так как $\mu W\le\mu(H^2+x^6+y^6)+C'z^7$,
   выполнено (L2) с $\varepsilon_1:=\big[5000\sigma^3+(6e(2\delta)^{2/3}+C''+C')\sigma\big]/\delta\to0$ при $\sigma\to0$.
6. **(L3M)** с $\gamma_1=\gamma_2=0$. Пусть $w\perp Y$, $\hat w=(w_x,w_y)$.
   - $\nabla\rho=e_z$ и $\langle e_z,w\rangle=w_z=-\xi\cdot\hat w$, поэтому $\vartheta_1:=3\sigma^{1/2}$.
   - $zD_YY=\big(D_{xy}(z\xi)\,\hat\xi+z\partial_z\xi,\ 0\big)$, где $\hat\xi:=(\xi_1,\xi_2)$, и
     $\lvert zD_YY\rvert\le(3\sqrt2+e)\lvert\xi\rvert+4z^{1/2}\le19\sigma^{1/2}$: $\vartheta_2:=19\sigma^{1/2}$.
   - $z\langle w,D_wY\rangle=\hat w^{\mathsf T}D_{xy}(z\xi)\,\hat w+w_z\,\hat w\cdot z\partial_z\xi\ge-\big[\frac{(3-e)(\sqrt2-1)}2+e+4\sigma^{1/2}\big]\lvert w\rvert^2$, так что
     $\vartheta_3\le0{,}63+e+4\sigma^{1/2}\le1{,}2$ при малом $\sigma$.
   - $b'=6-2e-2\vartheta_3\ge6-1-2{,}4>2$.
7. **Лемма M.** Скобка (M) равна $2e-\varepsilon_1-(L_1\vartheta_1+L_2\vartheta_2)/\sqrt\delta$, при $\sigma\to0$ (и фиксированном $\delta$) она
   стремится к $2e$; выберем $\sigma$ так, что она $\ge e$. Условие п. (1): $4\sqrt\delta\cdot3\sigma^{1/2}\le\sqrt{2a_0/3}$ — тоже
   малостью $\sigma$. Лемма M даёт (D4), (A4), (A5), а теорема A — траекторию в $\overline\Omega$. Тогда $q(t)\in D_\sigma$,
   откуда оценка $H^2+x^6+y^6\le2\delta z^6$ (п. 2). Оценки $\dot z$ — как в п. 11 доказательства теоремы S. $\square$

**[Эксперимент: `exit_u2.py`]** Минимум $\frac\rho\lambda\Xi/(\delta\rho^6)$ по точкам стенки (153–154 точки, $e=0{,}1$):

| $(\delta,\sigma)$ | $(0{,}05;0{,}02)$ | $(0{,}02;0{,}002)$ | $(0{,}01;2\cdot10^{-4})$ | $(0{,}01;2\cdot10^{-5})$ | $(0{,}01;2\cdot10^{-6})$ | $(0{,}005;2\cdot10^{-7})$ |
|---|---|---|---|---|---|---|
| $U_{\rm II}$ | $-0{,}89$ | $-0{,}083$ | $0{,}144$ | $0{,}194$ | $0{,}200$ | $0{,}200$ |
| $U_{\rm II}+0{,}3xz^6+0{,}5x^2yz^4$ | $-0{,}91$ | $-0{,}085$ | $0{,}144$ | — | — | — |

При $e=0{,}5$: $-0{,}32$; $0{,}65$; $0{,}93$; $1{,}00$. Предел равен запасу $\mu=2e$, как и предсказывает (5.3). Худшие
точки — у вершины гиперболы при $K_\perp>0$, где $\lvert\xi\rvert\sim z^{1/2}$ ещё не мало (член
$(L_1\vartheta_1+L_2\vartheta_2)/\sqrt\delta$). Сходимость медленная, $\propto\sigma^{1/2}$, как в п. 6.

### 5.3. Что даёт пример

Теорема II — первый случай, где **полюс не входит в овраг**, особая точка $\Sigma$ существенна (дно
сходится к ней), а ни $\kappa$-приём, ни картезианское поле, ни теорема 2 [007] не работают. Профиль в
весовых координатах $x=z^{3/2}b_1$, $y=z^{3/2}b_2$ равен $F_0=(b_1b_2+1)^2-1$. Его нули — вся гипербола
(некомпактна): условие (V) [007] нарушено, коэрцитивность вдоль гиперболы появляется только в
следующем масштабе (рукава). Свободное поле (5.1) решает обе задачи сразу. Член $\vartheta_3\approx0{,}63+e$ при
этом не мал, и лемма 2 [007] (нужно $4\vartheta_3<\mu$) не подходит, а лемма M (нужно $2\vartheta_3<\beta-\mu$) — подходит.

### 5.4. Общий случай II — [Эскиз]

Пусть $a=b=1$, $\varphi(r,\theta):=r^{-m}U(r\omega(\theta))=\sum_{i\ge0}r^i\varphi_i(\theta)$, $\varphi_0=\theta_1^2\theta_2^2e$,
$\varphi_i=c_i+A_i(\theta_1)+B_i(\theta_2)+\theta_1\theta_2n_i(\theta)$. Пусть $i_n:=\min\{i:\ n_i\not\equiv0\}$, $n_{i_n}(0)\ne0$, и
$2i_n\le i_c:=\min\{i:\ c_i\ne0\}$ (или $c_{2i_n}-\frac{n_{i_n}(0)^2}{4e(0)}<0$ при $2i_n=i_c$, как у $U_{\rm II}$). Тогда
$$\varphi=e\Big(\theta_1\theta_2+\frac{r^{i_n}n_{i_n}}{2e}+\dots\Big)^2-\frac{r^{2i_n}n_{i_n}^2}{4e}+\dots$$
и дно — около вершины деформированной гиперболы $\mathcal H(r,\theta):=\theta_1\theta_2+r^{i_n}\nu(\theta)+\dots=0$,
$\nu=n_{i_n}/(2e)$, на угловом расстоянии $\asymp r^{i_n/2}$. План доказательства по образцу теоремы II.

1. Поле $Y=\partial_r+\frac1r\big(\lambda_1\theta_1,\lambda_2\theta_2\big)+\frac1r\zeta$, где $\lambda_1+\lambda_2=i_n-e$, $\lambda_1=\Lambda(u)$ — функция
   отношения $u=\lvert\theta_1/\theta_2\rvert$ («лоскутное» поле, как $\lambda_x=(3-e)/(1+u)$). Поправка $\zeta\parallel\nabla_\theta\mathcal H$
   подбирается так, что $Y\mathcal H=\frac{i_n-e}r\mathcal H$ точно. Это даёт запас $2e$ для квадрата.
2. На рукаве $i$ профиль — эффективный потенциал ветви $i$ (уже **с** выигрышем $-r^{2i_n}n^2/4e$).
   Если он коэрцитивен только в сферических срезах, на рукаве нужно ещё $\kappa$-сжатие: $\lambda_1\to-\kappa$ вместо
   $\lambda_1\to0$. Тогда появляются перекрёстные члены $\gamma\sim\kappa R_\theta$, и выбор $\kappa(\delta)$ — как в теореме S.
3. Нужно проверить: (a) $\vartheta_3$: симметричная часть $D(\lambda_1\theta_1,\lambda_2\theta_2)$ содержит
   $\lambda'(u)\cosh(\log u)$; при $\lambda(u)=(i_n-e)/(1+u)$ она ограничена снизу величиной $-(i_n-e)(\sqrt2-1)/2$, и нужно
   $2\vartheta_3<\beta-\mu$; (b) зависимость $e,\nu$ от $\theta$ (гипербола не стандартная), члены $\partial_\theta\nu$ в
   $Y\mathcal H$; (c) переходная зона $\lvert\theta_1\rvert\sim\lvert\theta_2\rvert\sim r^{i_n/2}$, где ошибки малы, так как там
   $\lvert\theta\rvert\to0$; (d) члены $A_i,B_i$ с $i<2i_n$ (они должны быть $\ge0$, как в (X1)).

Ничего из этого, кроме примера $U_{\rm II}$, не выписано.

## 6. Перечень подслучаев нормального пересечения ($a=b=1$)

Обозначения §5.4: $c_i=\varphi_i(0)$ — значения в полюсе, $A_i,B_i$ — профили вдоль ветвей ($A_i(0)=B_i(0)=0$),
$n_i$ — перекрёстные коэффициенты. Предполагается, что овраг сходится к $\omega_0$: в каждом конусе вокруг
луча $\omega_0$ есть точки с $U<0$.

| Подслучай | Условие | Статус |
|---|---|---|
| **I.** Полюсное доминирование | $c_{i_c}<0$; $2i_n>i_c$; $A_i,B_i\ge0$ при $i<i_c$; $A_{i_c},B_{i_c}$ — строгий минимум в $0$ | [Доказано]: следствие X. Здесь (X1), (X2) — в точности эти условия, так как при аналитичности $tA_i'\ge0$ автоматически |
| **II.** Гиперболическое разрешение | $2i_n\le i_c$ (опасный перекрёстный член), $n_{i_n}(0)\ne0$, глубина $c_{2i_n}-n^2/4e<0$ на гиперболе | пример $U_{\rm II}+O(\lvert q\rvert^7)$ — [Доказано] (теорема II); общий — [Эскиз] (§5.4) |
| **III.** Дно подходит к $\omega_0$ вдоль ветви | некоторая $A_i$ ($i<\min(i_c,2i_n)$) знакопеременна около $0$, но минимум на сфере стремится к $\omega_0$ | [Гипотеза]: сводится к дну на ветви с вырождающимся нормальным гессианом ($h_n\asymp\theta_1^2$); не разобрано. Если сдвиг вызван членами порядка выше $i_c$, это уже случай I (возмущение в $R$, как у $U+xz^6+2y^2z^5$) |
| **IV.** Вырожденный профиль ветви | $A_{i_c}\equiv0$ (эффективный потенциал постоянен вдоль ветви в главном порядке) | [Гипотеза]: каскад по следующим порядкам, как случай (d) теоремы M, но у особой точки; не разобрано |
| **V.** Перекрёстный коэффициент исчезает в полюсе | $n_{i_n}(0)=0$, $2i_n\le i_c$ | если выигрыш $-r^{2i_n}n^2/4e$ максимален вдали от $\omega_0$, дно уходит на гладкие дуги (теоремы K, M); иначе — [Гипотеза] |

Кроме того, не разобраны:

- $a\ge2$ или $b\ge2$ без делимости перекрёстной части на $\theta_1^a\theta_2^b$ (нормальная кратность $\ge4$ вдоль
  ветви, ср. записку `normal-multiplicity`);
- перекрёстные члены при **неквазиоднородных** особенностях (касп, касание, три ветви) — следствие X′
  покрывает только полюсное доминирование без перекрёстных членов;
- особенности, у которых $u_m\circ\omega$ не монотонна ни вдоль какого квазиоднородного поля;
- $n\ge4$: теорема S и следствие X′ верны при любом $n$, но классификация не делалась.

## 7. Где работают аналитичность и изолированность

1. **В доказанных утверждениях — нигде.** Теорема S требует только $U\in C^2$ и неравенств (S1)–(S3).
   Следствия X, X′ — условия на конечную струю $j^jU$ плюс $U\in C^{j+1}$ для остатка $R=O(r)$ в $C^1$.
   Аналитичны лишь данные струи: $p_k$ — многочлены, суженные на аналитическую карту, а ветви $\Sigma$ —
   аналитические кривые. Теорема II — то же для струи $j^6U$. Изолированность нигде не предполагается.
2. **Почему нет противоречия с $C^\infty$-контрпримерами** (Пенлеве–Уинтнер, Лалуа; пример Уреньи —
   по `problem/KNOWN_RESULTS.md`, с первоисточниками не сверено). Там неустойчивость не определяется
   никакой конечной струёй: функции плоские. Здесь же условия — открытые условия на конечную струю,
   и возмущения высших порядков (даже гладкие) их не нарушают.
3. **Где они понадобятся** (в недоказанной части §6):
   - **аналитичность**: конечность порядков ($j<\infty$, конечный порядок минимума $\Lambda_i$), конечность
     многоугольника Ньютона перекрёстных коэффициентов $n_i$, дихотомии «$A_i\equiv0$ или знакоопределённа
     около $0$», ряды Пюизё для дна в подслучаях III–V;
   - **изолированность** — чтобы исключить бесконечный порядок. Ожидается ([Гипотеза], у особой точки не
     проверено): если $\varphi$ вдоль ветви плоская во всех порядках, то, как в предложении R записки
     `morse-bott`, ветвь дна состоит из критических точек. Для подслучаев I, II этого не требуется.

## 8. Эксперименты

Каталог `experiments/prover/singular-sigma/`, `~/venv/bin/python`, mpmath 40–50 знаков. Всё [Эксперимент].

| Скрипт | Что проверяет | Вывод (`*.out`) |
|---|---|---|
| `model_checks.py` | модель: градиент и разбор случаев, полярная форма (3.1), тождество Эйлера (S2), ряды $\Lambda$, оценки (S1), (S2) на сетке при $\varepsilon\in[-2,2]$, картезианское $6W-zW_z\ge4W$ | всё `True`; запасы $\ge0{,}39$ и $\ge1{,}39$ |
| `geom_checks.py` | формулы (2.1), (2.2) теоремы S для произвольной аналитической карты сферы и нелинейного $\xi$ | невязки $\le4\cdot10^{-40}$ |
| `exit_model.py` | (A5) для модели: S — сферические срезы, поле теоремы S; C — $\rho=z$, $Y=e_z$; SP, CP — с возмущением $xz^6+2y^2z^5$; $\varepsilon=0{,}1$ и $-0{,}5$ | `exit_S.out`, `exit_SP.out`, `exit_Sneg.out`, `exit_C.out`, `exit_CP.out`; при $\kappa>0$ $\min\approx2\kappa$, при $\kappa=0$ — $0$ (модель) или $<0$ (возмущение); C: $5{,}2$–$5{,}7$, CP: $0{,}98$; $3{,}49$ |
| `exit_cor.py` | (A5) для X1, X2 (следствие X) | `exit_X1.out`, `exit_X2.out` (§4.4) |
| `u2_checks.py` | $U_{\rm II}$: изолированность, тождества (5.2), (5.3), спектр $D_{xy}(z\xi^{(0)})$, функция $f(u)$ | `u2_checks.out` |
| `exit_u2.py` | (A5) для $U_{\rm II}$: F — поле (5.1), E — $Y=e_z$, FP — с возмущением | `exit_u2_F*.out`, `exit_u2_E.out`, `exit_u2_FP.out` (§5.2) |
| `bottom.py` | дно (минимум на сферах): модель (ось), модель с возмущением ($\theta_1=-r/6$ на ветви), $U_{\rm II}$ (вершина гиперболы, $\lvert\theta\rvert\approx\sqrt{2r}$); размеры креста | `bottom.out` |
| `cusp_check.py`, `tangency_check.py` | касп и касание: исключение по Грёбнеру, полярная форма, условия X′ | `cusp_check.out`, `tangency_check.out` |
| `s1_check.py` | пример S1: полюса не овраги; $G$, $G''+5G$ на дуге $x=y$ | `s1_check.out` |

Схема проверки (A5) — как в `experiments/prover/morse-bott/exit_mb.py`. Точки стенки
$W=(1-\tau)\delta\rho^\beta$, $K_\perp=\tau\delta\rho^\beta$, $\tau\in\{0,10^{-3},10^{-2},0{,}05,0{,}2,0{,}5\}$, 24 направления $v_\perp$;
$\Xi$ — `mpmath.diff` от $V-\delta\rho^\beta$ вдоль $(v,-\nabla U)$, без тождества (1.3) [007]. Это проверка в
конечном числе точек, а не доказательство.

## 9. Пробелы

1. **Опора.** Теорема S и теорема II опираются на лемму M (проверена R26, но в `results/` её нет) и на
   теорему A [007]. Предложение 3.3 — только на лемму 2 [007].
2. **Всё новое ждёт рецензента:** теорема S (особенно п. 9: формулы (2.2) и оценки $\gamma_1,\gamma_2,\vartheta_3$ при общем
   $\xi$; порядок выбора $\delta\to\kappa\to\sigma$), теорема 3.2, следствия X и X′ (п. 4: оценка перекрёстного
   члена через неравенство о средних), теорема II (п. 5: оценка (5.3) в трёх зонах $u$; п. 6: спектр
   $D(z\xi^{(0)})$).
3. **Классификация не завершена** (§6). Не доказано, что сходимость дна к особой точке $\Sigma$
   всегда приводит к подслучаю I или II. Подслучаи III–V, нормальная кратность $\ge4$ без делимости,
   перекрёстные члены у неквазиоднородных особенностей — открыты. Общий случай II — [Эскиз].
4. **Замечание X.1** (совпадение $\Lambda_i$ с эффективным потенциалом $g_j$ леммы K1) — [Эскиз].
5. **Изолированность** у каспа и касания установлена исключением через базис Грёбнера в sympy (точная
   арифметика, но вручную не пересчитано). У модели, X1, X2, $U_{\rm II}$ она доказана вручную.
6. **S1** покрыт теоремой K1 [008] при условии численных значений $G''+5G=0{,}3212$, $G'(\varphi^*)=0$
   (40 знаков, не интервально).
7. **Не утверждается** касание луча траекторией. В теореме S и следствиях X, X′ доказано лишь, что при
   каждом $\delta$ есть своя траектория в конусе раствора $O(\delta^{1/(2p)})$. В теореме II траектория остаётся в
   утолщённом L-образном овраге с $\lvert(x,y)\rvert\le2^{2/3}\delta^{1/6}z$, и не доказано, что она подходит к вершине
   гиперболы.

## 10. Статус

- Теорема S — **[Доказано]** (теорема A [007] + лемма M [P11, R26]); любое $n\ge2$, $U\in C^2$.
- Модель: предложение 3.1 — **[Доказано]**; теорема 3.2 (любое $\varepsilon$, устойчиво к $O(\lvert q\rvert^7)$) —
  **[Доказано]**; предложение 3.3 ($\varepsilon\ge0$, лемма 2 [007]) — **[Доказано]**.
- Следствие X (нормальное пересечение кратностей $2a,2b$, полюсное доминирование) — **[Доказано]**.
- Следствие X′ (квазиоднородная особенность, полюсное доминирование без перекрёстных членов) —
  **[Доказано]**. Примеры X1, X2 — **[Доказано]**; касп, касание — принадлежность **[Доказано]**,
  изолированность [Эксперимент: точная символьная выкладка].
- Теорема II ($U_{\rm II}+O(\lvert q\rvert^7)$, свободное поле) — **[Доказано]**.
- Общий случай II — **[Эскиз]**; подслучаи III–V — **[Гипотеза]**.
- Ничто из этого не проверено независимо.
