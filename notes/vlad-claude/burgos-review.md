# Разбор препринта Burgos arXiv:2108.05829 (v4) и его статуса

Автор заметки: vlad-claude. Дата: 27.09.2026. Источник: TeX-исходник v4 с arXiv
(`https://arxiv.org/e-print/2108.05829v4`), страница `https://arxiv.org/abs/2108.05829`,
исходник arXiv:2506.19135v1.

## 1. Статус препринта [Литература: arXiv:2108.05829, сверено со страницей arXiv 27.09.2026]

История версий: v1 12.08.2021, v2 17.08.2021, v3 03.09.2021, v4 11.09.2021,
**v5 16.07.2022 — withdrawn**. Комментарий автора к v5 (дословно):

> There is a mistake in the proof. The second term of the last equation in Lemma 2.2 does
> not have the desired asymptotic behavior. I am grateful with V. P. Palamodov for pointing
> out this mistake

То есть сам автор признал доказательство ошибочным. Утверждение STATE.md и
problem/KNOWN_RESULTS.md «случай (A) заявлен доказанным» устарело.

Свежая работа того же автора, J. M. Burgos, *McGehee blowup for Lagrangian systems and
instability of equilibria*, arXiv:2506.19135v1 (23.06.2025; по KNOWN_RESULTS — JDE 454,
2026), во введении (строки 312–317 исходника) пишет дословно:

> In [Arnold], Arnold proposed the problem of instability of an isolated non-minimum
> critical point of a real analytic potential in Newtonian mechanics. Even this simplified
> version of the Lagrange-Dirichlet converse remains open.

и (стр. 253): Palamodov [УМН 75:3, 2020] доказал полную неустойчивость, **если первая
ненулевая струя $U$ не имеет критических точек, кроме нуля**; основной шаг — деформация
радиального поля в поле $V$ с $V(U)=U$. Стр. 261: «so far all of the instability criteria
either in the total or Lyapunov sense, require the generic hypothesis that zero is a
regular value of the function $f$» ($f$ — ограничение младшей формы на сферу, в
обозначениях статьи; сверить точно).

**Вывод:** по состоянию литературы, известной нам, случай (A) при $n\ge3$ **открыт**
(при $n=2$ закрыт: Козлов 1981 / Паламодов 1977 / Taliaferro 1980, Brunella 1998).

## 2. Схема доказательства v4

Обозначения: $U(x_0)=0$, метрика $\rho$ (для нас евклидова).

- **Лемма 2.1** (Спиваковский, частное сообщение). Монализация Хиронаки
  $\sigma:\tilde M\to M$ идеала $\mathfrak m_{x_0}\cdot(U)$: $\sigma^{-1}(U)$ локально
  мономиален, $E=\sigma^{-1}(\mathcal V(U))$, $\sigma^{-1}(x_0)$ — объединение компонент $E$.
  (Не проверял подробно; на первый взгляд стандартно.)
- **Лемма 2.2** (аналог леммы 4.1 Паламодова 1995). Существуют окрестность $W$, гладкое
  поле $V$ и функция $P\ge1$ на $W\setminus\mathcal V(U)$ такие, что $V(U)=PU$ и
  $\langle v,\nabla_vV\rangle=(1+o(1))\|v\|^2$ при $x\to x_0$.
  Конструкция: в карте $W_p$ около $p\in H=\sigma^{-1}(x_0)$ с $\tilde U=\pm w^d$ берётся
  поле Эйлера $\tilde V_p=\sum w_i\partial_{w_i}$, $\tilde V_p\tilde U=c_p\tilde U$; его
  образ $V_p$; затем склейка разбиением единицы $V=\sum f_pV_p$.
- **Вывод теоремы.** $F(t)=\langle\dot\gamma,V(\gamma)\rangle$ ограничена, а
  $\dot F\ge -\langle\nabla U,V\rangle=-PU\ge -E>0$ — противоречие.

Заметим: выводу нужно лишь $\langle v,\nabla_vV\rangle\ge0$ (а не $(1+o(1))\|v\|^2$),
ограниченность $V$ на $\{U\le E\}\cap\overline W$ и $V(U)\le U$ там.

## 3. Где ошибка: два независимых дефекта леммы 2.2 [Доказано]

### 3a. Локальная выкладка в карте неверна уже для морсовского седла

Утверждается: в координатах $w'$ на $\sigma(W_p-E)$
$\langle v,\nabla_vV_p\rangle=g_{ab}v^av^b+\tfrac12V_p(g_{ab})v^av^b$ и второй член
$=o(\|v\|^2)$, «так как $V_p\to0$». Но в координатах $w'$ сама метрика $g_{ab}$
вырождается при подходе к $x_0$, поэтому малость $V_p$ не даёт малости
$V_p(g_{ab})$ **относительно** $g_{ab}$.

**Контрпример.** $n=2$, $U=x(y-3x)$ (невырожденное седло). Раздутие нуля,
карта $x=w_1$, $y=w_1(w_2+3)$: $\tilde U=w_1^2w_2$ — мономиально, и точка $p=(0,0)$ этой
карты лежит в $H=\{w_1=0\}=\sigma^{-1}(0)$. (Во второй карте $x=u_1u_2,\ y=u_2$:
$\tilde U=u_2^2u_1(1-3u_1)$ — тоже мономиально около $u_1=0$; так что одно раздутие —
допустимая монализация $\mathfrak m\cdot(U)$.) Поле
$\tilde V_p=w_1\partial_{w_1}+w_2\partial_{w_2}$ в исходных координатах:
$$V_p=x\,\partial_x+(2y-3x)\,\partial_y,\qquad V_p(U)=3U,$$
$$\langle v,\nabla_vV_p\rangle=v_1^2-3v_1v_2+2v_2^2,$$
при $v=(4,3)$ это $-2<0$ **в любой точке**, в частности сколь угодно близко к $0$.
Форма $\operatorname{sym}DV_p=\begin{pmatrix}1&-3/2\\-3/2&2\end{pmatrix}$ знаконеопределена
(определитель $-1/4$). Значит, утверждение
$\langle v,\nabla_vV_p\rangle=(1+o(1))\|v\|^2$ ложно. Для карты со сдвигом $a$ вместо 3
получаем $\operatorname{sym}DV_p=\begin{pmatrix}1&-a/2\\-a/2&2\end{pmatrix}$, положительно
определена лишь при $a^2<8$. Проверка: `experiments/vlad-claude/burgos-lemma22/check.py`
(sympy; выкладка элементарна и приведена здесь полностью).

Прямо в координатах $w$: $g_{11}=1+(w_2+3)^2$, $g_{12}=w_1(w_2+3)$, $g_{22}=w_1^2$,
а $\tfrac12V(g_{12})\to\tfrac32w_1$, $\tfrac12V(g_{22})=w_1^2$ — того же порядка, что $g$.

### 3b. Член от разбиения единицы (его и называет автор)

$\langle v,\nabla_vV\rangle=\sum_p\big(f_p\langle v,\nabla_vV_p\rangle+v(f_p)\langle
v,V_p\rangle\big)$. Носители $f_p$ — образы карт $\sigma(W_p-E)$, т. е. «секторы» около
$x_0$, угловой размер которых не стремится к нулю; поэтому $|\nabla f_p(x)|\sim1/|x|$, а
$|V_p(x)|\sim|x|$ (для карт первого раздутия; после нескольких раздутий масштабы
анизотропны). Второй член — $O(\|v\|^2)$, но не $o(\|v\|^2)$, и знака не имеет. Это
согласуется с комментарием автора к v5.

## 4. Что остаётся от метода (для дальнейшей работы)

Метод сводит полную неустойчивость к **лемме о поле** [Гипотеза, открыто]:

> (L) существуют окрестность $W\ni x_0$ и $C^1$-поле $V$ на $W\cap\{U<0\}$, ограниченное,
> с $\operatorname{sym}DV\succeq0$ (для евклидовой метрики; в общем случае
> $\langle v,\nabla_vV\rangle\ge0$) и $\langle\nabla U,V\rangle\le U$ на $W\cap\{U<0\}$.

[Доказано] (L) ⇒ полная неустойчивость ⇒ (A): это ровно вывод из §2 статьи; он корректен
(проверил: $F$ ограничена, $\dot F\ge -\langle\nabla U,V\rangle\ge -U\ge -E$ вдоль движения
энергии $E<0$, лежащего в $\{U\le E\}$).

Примеры, где (L) верна: однородный $U$ ($V=x$); квазиоднородный $U$ с весами $\alpha_i>0$
($V=\sum\alpha_ix_i\partial_i$, $\operatorname{sym}DV=\operatorname{diag}(\alpha)\succ0$,
$V(U)=dU$, $d>0$, и $dU\le U$ при $U<0$, если нормировать $d\ge1$). Паламодов 2020
(по [B25]) — деформация радиального поля при невырожденной младшей струе.

Трудность: положительность $\operatorname{sym}DV$ не сохраняется ни при нелинейной замене
координат (§3a), ни при склейке (§3b). Нужен способ склеивать «монотонные» поля.
Идея для проверки: брать $V=\nabla\varphi$ с выпуклой $\varphi$ (тогда
$\operatorname{sym}DV=D^2\varphi\succeq0$ автоматически, а максимум выпуклых функций
выпукл — склейка через $\max$/сглаженный максимум сохраняет выпуклость!). Требование:
$\langle\nabla U,\nabla\varphi\rangle\le U$ на $\{U<0\}$.
