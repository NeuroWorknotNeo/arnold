# Пример 13: тотальная неустойчивость (вириальное поле, адаптированное к жёлобу)

vlad-claude-tg, 03.10.2026. Типографская версия: [`example13-proof.pdf`](example13-proof.pdf)
(исходник [`example13-proof.tex`](example13-proof.tex)). Проверочные скрипты:
[`experiments/vlad-claude-tg/example13/`](../../experiments/vlad-claude-tg/example13/).

**Статусы:** теорема 1 — **[Доказано]**, ждёт независимой проверки. Предложение 1 (обобщение) —
**[Эскиз]**: доказательство переносится, изменения перечислены. Численные проверки (§8) —
**[Эксперимент]**.

## Утверждение

**Теорема 1.** Пусть

$$U(x,y,z)=(x^2+y^2-z^2)^2+z^5x+z^4xy+\tfrac12 z^6 .$$

Существуют $\varepsilon>0$ и $C>0$, такие что любое движение системы $\ddot q=-\nabla U(q)$ с
энергией $h=\tfrac12|\dot q|^2+U(q)<0$, начинающееся в шаре $B_\varepsilon$, покидает $B_\varepsilon$ за
время не больше $C/|h|$. В частности, равновесие $q=0$ неустойчиво по Ляпунову.

Чем пример интересен. Гессиан нулевой, $U_3=0$. Старшая форма $U_4=Q^2\ge0$, где $Q=x^2+y^2-z^2$,
обращается в нуль на двух окружностях сферы (жёлоб), и $\nabla U_4=0$ на жёлобе. Форма $U_6$ на
жёлобе меняет знак, а $U_5\equiv0$. Поэтому не работают ни Ляпунов, ни критерии по первой ненулевой
форме (Козлов–Паламодов; Паламодов 2020, теоремы 3 и 6), ни негенерический критерий Burgos
(arXiv:2506.19135, следствие 1.4: нужно $U_6<0$ на всём жёлобе). Не работает и теорема B участника
vlad-claude ([`notes/vlad-claude/theoremB.md`](../vlad-claude/theoremB.md)): условие (B3) требует,
чтобы $u_{m+1}|_\Sigma=U_5|_\Sigma$ имело $0$ регулярным значением, а здесь $U_5\equiv0$. Изометрий,
сводящих задачу к $n=2$, нет: единственная нетривиальная — $q\mapsto-q$. Изолированность
критической точки в доказательстве не используется, она получается как следствие.

**Идея.** (1) Координаты, в которых конус $\{Q=0\}$ — поверхность $\{d=0\}$ и **точно**
$Q^2=4s^2d^2$. (2) Веса $s\mapsto\lambda s$, $d\mapsto\lambda^2 d$: главная часть $U$ равна
$4s^2d^2+\tfrac{s^6}{8}G(\varphi)$. (3) Взвешенное поле Эйлера $E=s\partial_s+2d\partial_d$:
$E(U)=6U+(\text{члены веса}\ge7)$ и $\operatorname{Sym}DE\approx\operatorname{diag}(1,1,2)$. (4) Две
поправки с **малыми фиксированными** коэффициентами чинят знак у границы «рога» $\{U<0\}$, где
$U\to0$. Поперечная поправка работает на боковых стенках рога, угловая — в его кончиках, где
$G'\ne0$. Единственное нетривиальное свойство примера: у $G$ нет кратных нулей.

## 1. Вириальная лемма

**Лемма 1** (по существу теорема 2 Паламодова [P77]; см. [P20] и лемму 1 в
[`notes/vlad-claude/toolkit.md`](../vlad-claude/toolkit.md)). Пусть $B$ — шар с центром $0$, $V$ —
ограниченное $C^1$-поле на $B\cap\{U<0\}$, $\alpha>0$ и

(i) $\langle\nabla U,V\rangle\le\alpha U$; (ii) $\langle DV(q)\xi,\xi\rangle\ge-\tfrac\alpha2|\xi|^2$ для всех
$\xi\in\mathbb R^3$.

Тогда любая траектория с $h<0$, начинающаяся в $B$, покидает $B$ за время не больше
$2M/(\alpha|h|)$, где $M=\sup|V|\cdot(2\sup_B|U|)^{1/2}$.

*Доказательство.* На траектории $U\le h<0$. Для $F=\langle\dot q,V(q)\rangle$ имеем $|F|\le M$ и
$\dot F=-\langle\nabla U,V\rangle+\langle DV\dot q,\dot q\rangle\ge-\alpha U-\tfrac\alpha2|\dot q|^2=\alpha|h|$. $\square$

## 2. Координаты, согласованные с жёлобом

В области $\{z>0,\ \rho>0\}$, где $\rho=\sqrt{x^2+y^2}$, $x=\rho\cos\varphi$, $y=\rho\sin\varphi$,
положим

$$s=\frac{\rho+z}{\sqrt2},\qquad d=\frac{\rho-z}{\sqrt2};\qquad \rho=\frac{s+d}{\sqrt2},\quad z=\frac{s-d}{\sqrt2}.$$

В каждой меридиональной полуплоскости $(s,d)$ — повёрнутые декартовы координаты, поэтому
$|dq|^2=ds^2+dd^2+\rho^2d\varphi^2$. Ортонормированный репер:
$e_s=(e_\rho+e_z)/\sqrt2$, $n=(e_\rho-e_z)/\sqrt2$, $e_\varphi$; при этом $\partial_s=e_s$,
$\partial_d=n$, $\partial_\varphi=\rho e_\varphi=(-y,x,0)$. Тождества:

$$q=s\,e_s+d\,n,\qquad \nabla d=n,\qquad Dn=\frac{1}{\sqrt2\,\rho}\,e_\varphi\otimes e_\varphi .\tag{1}$$

Верхняя полость конуса — это $\{d=0\}$, и на ней $s=|q|$.

**Лемма 2.** В этих координатах

$$U=4s^2d^2+\sum_{j=0}^{6}a_j(\varphi)\,s^{6-j}d^j,\qquad a_0=\tfrac18G(\varphi),\quad a_1=-\tfrac18\sin2\varphi-\tfrac12\cos\varphi-\tfrac38,$$

где $G(\varphi)=\cos\varphi\,(1+\sin\varphi)+\tfrac12$, а все $a_j$ — тригонометрические многочлены.

*Доказательство.* $Q=\rho^2-z^2=(\rho-z)(\rho+z)=2sd$, откуда $Q^2=4s^2d^2$. Далее
$U_6=z^4\bigl(z\rho\cos\varphi+\rho^2\sin\varphi\cos\varphi+\tfrac12z^2\bigr)$ — однородный
многочлен степени 6 от $(s,d)$. При $d=0$ имеем $z=\rho=s/\sqrt2$ и $U_6=\tfrac{s^6}{8}G$.
Коэффициент $a_1$ получен прямым разложением и проверен символьно. $\square$

**Лемма 3** (эффективный потенциал). $G'(\varphi)=-(2\sin\varphi-1)(1+\sin\varphi)$.
Критические точки: $\varphi=\pi/6,\ 5\pi/6,\ 3\pi/2$, значения $\tfrac12+\tfrac{3\sqrt3}{4}$,
$\tfrac12-\tfrac{3\sqrt3}{4}\approx-0.799$, $\tfrac12$. Поэтому **$G$ и $G'$ не имеют общих нулей**.
$G<0$ ровно на дуге $(\varphi_-,\varphi_+)\ni5\pi/6$, где $\varphi_-\approx1.828$,
$\varphi_+\approx3.600$, и нули $\varphi_\pm$ простые.

*Доказательство.* $G'=1-\sin\varphi-2\sin^2\varphi$. Значения в критических точках ненулевые. Вне
$(\pi/2,3\pi/2)$ имеем $\cos\varphi\ge0$, откуда $G\ge\tfrac12$. $\square$

## 3. Где живёт $\{U<0\}$

**Лемма 4.** Пусть $A=\max_{|q|=1}|U_6|$ (из явного вида $A\le2$) и $0<|q|=r<1/\sqrt A$. Если
$U(q)<0$ и $z\ge0$, то $z>0$, $\rho>0$ и $|d|<\sqrt{2A}\,s^2$. Если $z<0$, то то же верно для $-q$.

*Доказательство.* Из $U<0$ получаем $Q^2<Ar^6$. При $z,\rho\ge0$ верно $|Q|=|\rho-z|(\rho+z)\ge|\rho-z|\,r$,
откуда $|\rho-z|<\sqrt A\,r^2<r$. Значит, $\rho,z>0$, $|d|<\sqrt{A/2}\,r^2$ и $s^2\ge r^2/2$. Для
$z<0$ используем чётность $U(-q)=U(q)$. $\square$

Положим $C_0=\sqrt{2A}$ и $N_+=\{z>0,\ \rho>0,\ |d|<2C_0s^2\}$, $N_-=-N_+$. При малом $\varepsilon$
имеем $B_\varepsilon\cap\{U<0\}\subset N_+\cup N_-$.

**Перемасштабирование.** В $N_+$ положим $\eta=d/s^2$, $|\eta|<2C_0$. Тогда

$$U=s^6\,\widetilde U(s,\varphi,\eta),\qquad \widetilde U=4\eta^2+\sum_{j=0}^6a_j(\varphi)s^j\eta^j=\widetilde U_0(\varphi,\eta)+s\,R(s,\varphi,\eta),\qquad \widetilde U_0=4\eta^2+\tfrac18G(\varphi),\tag{2}$$

где $R$ — многочлен от $(s,\eta)$ с тригонометрическими коэффициентами. При фиксированном $s$

$$\partial_dU=s^4\,\widetilde U_\eta,\qquad \partial_\varphi U=s^6\,\widetilde U_\varphi .\tag{3}$$

## 4. Вириальное поле

На $N_+$ при $\kappa=\tfrac1{100}$, $\kappa'=\tfrac1{50}$ положим

$$V=\frac16\bigl(s\,\partial_s+2d\,\partial_d\bigr)-\kappa\,\frac{\partial_dU}{s^2}\,\partial_d-\kappa'\,\frac{\partial_\varphi U}{s^6}\,\partial_\varphi ,$$

а на $N_-$ положим $V(q)=-V(-q)$. По (1) первое слагаемое равно $\tfrac16(q+d\,n)$. Поле гладкое на
$N_\pm$, и $|V|\le C|q|$. Так как $\nabla U$ нечётен, условия для $N_-$ следуют из условий для $N_+$.

**Лемма 5** (условие (i)). При $\alpha=\tfrac12$ существует $\varepsilon_1>0$, такое что
$\langle\nabla U,V\rangle\le\alpha U$ на $N_+\cap\{U<0\}\cap B_{\varepsilon_1}$.

*Доказательство.* Поле $E=s\partial_s+2d\partial_d$ действует на одночлены как
$E(s^ad^b)=(a+2b)s^ad^b$. Значит,

$$\langle\nabla U,V\rangle=U+g-K,\qquad g=\tfrac16\sum_{j\ge1}j\,a_js^{6-j}d^j,\qquad K=\kappa\frac{(\partial_dU)^2}{s^2}+\kappa'\frac{(\partial_\varphi U)^2}{s^6}.$$

По (2), (3) получаем $g=s^7\hat g$, где $\hat g=\tfrac16\sum_{j\ge1}ja_js^{j-1}\eta^j$, и

$$\langle\nabla U,V\rangle-\alpha U=s^6\,\Phi,\qquad \Phi=(1-\alpha)\widetilde U+s\hat g-\kappa\widetilde U_\eta^2-\kappa'\widetilde U_\varphi^2 .$$

Множество $K_0=\{\widetilde U_0\le0\}$ компактно, и на нём

$$\Phi(0,\varphi,\eta)=(1-\alpha)\widetilde U_0-64\kappa\eta^2-\tfrac{\kappa'}{64}G'(\varphi)^2<0 .$$

Действительно, при $\widetilde U_0<0$ отрицателен первый член. При $\widetilde U_0=0$ два последних
члена одновременно обращаются в нуль только при $\eta=0$ и $G'(\varphi)=0$, но тогда $G(\varphi)=0$,
что противоречит лемме 3. По компактности $\Phi(0,\cdot)\le-c$ на $\{\widetilde U_0\le\delta,\ |\eta|\le2C_0\}$
при некоторых $c,\delta>0$. Кроме того, $|\widetilde U-\widetilde U_0|\le C_1s$ и
$|\Phi(s,\cdot)-\Phi(0,\cdot)|\le C_2s$. Поэтому при $s<\min(\delta/C_1,\,c/(2C_2))$ из $\widetilde U<0$
следует $\Phi<-c/2$. Наконец, $s\le|q|$. $\square$

**Лемма 6** (условие (ii)). Существует $\varepsilon_2>0$, такое что
$\operatorname{Sym}DV\ge\tfrac1{12}I$ на $N_+\cap B_{\varepsilon_2}$.

*Доказательство.* Все $O(\cdot)$ равномерны по $N_+$ при $s\to0$; используем $|\eta|<2C_0$ и
$\rho=s(1+s\eta)/\sqrt2$.

*Главная часть.* По (1) $D(q+dn)=I+n\otimes n+\tfrac{d}{\sqrt2\rho}e_\varphi\otimes e_\varphi$ —
симметричная матрица с собственными значениями $1$, $2$ и $1+O(s)$.

*Поправка $Z_1=-\kappa f_1n$, $f_1=s^{-2}\partial_dU=s^2\widetilde U_\eta$.* Имеем
$D(f_1n)=n\otimes\nabla f_1+f_1Dn$. Так как $\partial_d=s^{-2}\partial_\eta$ и
$\partial_s\eta|_d=-2\eta/s$, получаем $\partial_df_1=\widetilde U_{\eta\eta}=8+O(s^2)$,
$\partial_sf_1=2s\widetilde U_\eta+s^2\widetilde U_{\eta s}-2s\eta\widetilde U_{\eta\eta}=O(s)$,
$\rho^{-1}\partial_\varphi f_1=\rho^{-1}s^2\widetilde U_{\eta\varphi}=O(s^2)$ и $f_1Dn=O(s)$. Итак,
$DZ_1=-\kappa(8+O(s^2))\,n\otimes n+O(s)$.

*Поправка $Z_2=-\kappa'f_2\partial_\varphi$, $f_2=s^{-6}\partial_\varphi U=\widetilde U_\varphi$.* Поле
$\partial_\varphi$ — поле вращений, $D\partial_\varphi$ антисимметрична, поэтому
$\|\operatorname{Sym}DZ_2\|\le\kappa'|\rho\nabla f_2|$. Из (2): $\widetilde U_{\varphi\eta}=a_1's+O(s^2)$,
$\widetilde U_{\varphi s}=a_1'\eta+O(s)$, $\widetilde U_{\varphi\varphi}=G''/8+O(s)$. Отсюда
$\rho\,\partial_df_2=a_1'/\sqrt2+O(s)$, $\partial_\varphi f_2=G''/8+O(s)$,
$\rho\,\partial_sf_2=O(s)$. Поскольку $|G''|=|\cos\varphi(1+4\sin\varphi)|\le3$ и
$|a_1'|=|-\tfrac14\cos2\varphi+\tfrac12\sin\varphi|\le\tfrac34$, получаем
$\|\operatorname{Sym}DZ_2\|\le0.91\,\kappa'+O(s)$.

*Итог.* В репере $(e_s,e_\varphi,n)$

$$\operatorname{Sym}DV\ge\operatorname{diag}\bigl(\tfrac16,\tfrac16,\tfrac13-8\kappa\bigr)-0.91\kappa'-O(s)\ge\tfrac1{12}I$$

при малом $s$. $\square$

**Доказательство теоремы 1.** Возьмём $\varepsilon<\min(1/\sqrt A,\varepsilon_1,\varepsilon_2)$ так, что
$B_\varepsilon\cap\{U<0\}\subset N_+\cup N_-$. По леммам 5 и 6 выполнены условия леммы 1 с
$\alpha=\tfrac12$. Отсюда каждая траектория с $h<0$ из $B_\varepsilon$ покидает $B_\varepsilon$ за время
не больше $4M/|h|$. Точки $q_0\to0$ с $U(q_0)<0$ существуют: на луче $\varphi=5\pi/6$ верхней полости
конуса $U=\tfrac{s^6}{8}G(5\pi/6)<0$. $\square$

*Замечание.* Поле $V$ не класса $C^1$ в нуле (его производная однородна нулевой степени), поэтому
теорема 2 Паламодова в форме «поле класса $C^1$ вплоть до точки» буквально не применяется. Лемме 1
это не нужно.

## 5. Связь с заметками vlad-claude

- **Теорема B** ([`theoremB.md`](../vlad-claude/theoremB.md),
  [`theoremB-proof.md`](../vlad-claude/theoremB-proof.md)) покрывает общий конус Морса–Ботта, но с
  эффективным потенциалом $u_{m+1}|_\Sigma$ (вес $3/2$ после сдвига). Здесь конус круговой, а
  эффективный потенциал берётся первой ненулевой степени $m\ge5$, с весами $(1,(m-2)/2)$. Пример 13
  ($m=6$) находится вне условия (B3).
- **Лемма R** ([`toolkit.md`](../vlad-claude/toolkit.md)). Пример 13 — один режим с блоками
  «радиальный и угловой» (масштаб $r$) и «нормальный» (масштаб $r^2$), $e=1$. По определению леммы R
  $J=\{\text{нормальный}\}$, и условие (Reg) нарушается в кончиках рога ($\eta=0$, $G=0$). Здесь это
  обойдено угловой поправкой $Z_2$ по **толстому** блоку. Её производная по нормали имеет порядок
  $O(\kappa')$, а не $o(1)$, и гасится выбором малого $\kappa'$, а не малостью $r$. Её вклад в $V(U)$
  равен $-\kappa'(\partial_\varphi U)^2/s^6\le0$, то есть всегда помогает. **[Эскиз]** Вероятно,
  (Reg) в лемме R можно ослабить до «$|F|\ge c_0$, или $|\nabla_JF|\ge c_0$, или
  $|\nabla_{J'}F|\ge c_0$ по толстым блокам $J'$, для которых $s_jr^{e}/s_i=O(1)$», с поправками
  по $J'$ с малыми фиксированными коэффициентами. Проверено только на этом примере.

## 6. Обобщение: жёлоб с регулярным эффективным потенциалом

**Предложение 1** [Эскиз]. Пусть $U=(x^2+y^2-z^2)^2+W$, где $W$ аналитична около нуля,
$W=W_m+W_{m+1}+\dots$, $m\ge5$, и
$G_\pm(\varphi)=W_m\bigl(\tfrac{\cos\varphi}{\sqrt2},\tfrac{\sin\varphi}{\sqrt2},\pm\tfrac1{\sqrt2}\bigr)$.
Если $0$ — регулярное значение $G_+$ и $G_-$ и хотя бы одна из них где-то отрицательна, то $0$
тотально неустойчива. Если же $G_\pm>0$, то $0$ — строгий минимум.

*Схема.* Веса $s:1$, $d:w$, где $w=\tfrac{m-2}2>1$. Подстановка $d=s^w\eta$ даёт
$\widetilde U=U/s^m=4\eta^2+G_+(\varphi)+O(s^\mu)$ с $\mu=\min(1,\tfrac{m-4}2)$. Все остальные члены
имеют вес больше $m$, поскольку $w>1$. Поле:
$V=\tfrac1m(s\partial_s+wd\partial_d)-\kappa s^{-2}(\partial_dU)\partial_d-\kappa's^{-m}(\partial_\varphi U)\partial_\varphi$;
$Z_1(U)=-\kappa s^m\widetilde U_\eta^2$, так как $2(m-w)-2=m$. Леммы 4–6 повторяются с заменой
$O(s)$ на $O(s^\mu)$, включая дробные степени при $m=5$. Нижняя полость: $s=(\rho-z)/\sqrt2$,
$d=(\rho+z)/\sqrt2$. Подробно не выписано.

## 7. Где метод перестаёт работать

- **Кратный нуль $G$** ($G=G'=0$). Обе поправки в кончике вырождаются, $\Phi(0,\varphi_0,0)=0$.
  Нужно следующее взвешенное раздутие в кончике.
- **Жёлоб надо «искать».** Члены, линейные по $d$ и сравнимые по весу с главными (например,
  $U=(Q-z\,m(q))^2-z^8$). Нужен шаг типа Ньютона–Пюизё (ср. сдвиг в теореме B).
- **Вырожденная или особая поперечная структура**: старшая форма зануляется на жёлобе в порядке
  выше второго, или жёлоб — особая кривая (например, $U_4=x^2y^2$).

## 8. Проверка вычислений [Эксперимент]

Скрипты и README: [`experiments/vlad-claude-tg/example13/`](../../experiments/vlad-claude-tg/example13/).

- `symbolic_check.py` (SymPy): $Q^2=4s^2d^2$; однородность $U-4s^2d^2$; формулы для $a_0,a_1$;
  тождество $\tfrac16E(U)-U=\tfrac16\sum ja_js^{6-j}d^j$; $\widetilde U(0,\varphi,\eta)=4\eta^2+G/8$.
  Результант числителей $G$ и $G'$ при $t=\tan(\varphi/2)$ равен $-23552\ne0$.
- `isolated_check.py`: изолированность критической точки. Единственный вещественный корень системы
  по $a=x/z$, $b=y/z$ равен $(a,b)\approx(1.154,-1.758)$, $a^2+b^2\approx4.42\ne1$.
- `numeric_check.py`: $2\cdot10^4$ случайных точек $\{U<0\}$ на сферах радиусов от $0.5$ до $0.005$.
  Получено $\min\langle\nabla U,V\rangle/U\ge1.000$ (нужно $\ge0.5$) и
  $\min\lambda_{\min}(\operatorname{Sym}DV)\in[0.151,0.160]$.
- `trajectories.py`, `trajectories_fine.py`: траектории с $h<0$ из «рога». Грубый прогон — 600
  траекторий (при $|q_0|=0.01$ шаг грубоват, дрейф энергии велик относительно крошечного $|h|$).
  Прогон с шагом в 5 раз мельче — 200 траекторий, дрейф $\le3\%$ от $|h|$. Все траектории покинули
  шар радиуса $0.3$, вдоль них $\dot F\ge2.0\,\alpha|h|$.

## Литература

- [P77] В. П. Паламодов, Об устойчивости равновесия в потенциальном поле, Функц. анализ 11:4 (1977).
- [P20] В. П. Паламодов, Об обращении теоремы Лагранжа–Дирихле и неустойчивости консервативных
  систем, УМН 75:3 (2020).
- [B25] J. M. Burgos, McGehee blowup for Lagrangian systems and instability of equilibria,
  arXiv:2506.19135.
