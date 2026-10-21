# Сверка §1–§2 KNOWN_RESULTS.md: задача 1971-4 и классические результаты

Автор: агент `literature`, 21.10.2026. Math-Net.Ru с сервера недоступен (connection refused), поэтому
P77, P20, Koz81 в оригинале не открывались. Книгу «Arnold's Problems» / «Задачи Арнольда» легально
прочитать не удалось (Springer — по подписке, Google Books отдаёт 429; сканирование Google Books не
продолжал). Ничего платного не скачивалось, теневых библиотек не использовалось.

Шкала сверки: **ПТ** — полный текст; **ПП** — полный текст препринта или обзора (не оригинал статьи);
**РЦ** — рецензия или аннотация zbMATH Open; **МД** — метаданные Crossref; **ВИ** — вторичный источник
(какой); **—** — не сверено.

Условие по знаку. Старая литература (Ляпунов, Четаев, Козлов, Негрини) пишет «функция сил»
U_force = −(потенциальная энергия). Фраза «не максимум функции сил» = «не минимум потенциальной
энергии». Ниже пишу в терминах потенциальной энергии, оговаривая это.

## 0. Главная находка: ошибки в библиографии

1. **[NLM79] — это Laloy, не Козлов и не «автор не установлен».** M. Laloy, *On the inversion of the
   Lagrange–Dirichlet theorem in the case of an analytic potential*, Int. J. Non-Linear Mech. 14:1
   (1979), 59–65, doi:10.1016/0020-7462(79)90029-5 (PII 0020746279900295). [Метаданные: Crossref,
   zbMATH Zbl id 3646366, MSC 70K20, 70H03, 70J30, 34D20.] Содержание статьи не удалось увидеть
   (аннотации нет ни в Crossref, ни в zbMATH). Поэтому утверждение из таблицы §2 «Пример [NLM79]: если
   ряд Маклорена имеет вид V₂+V_m+V_{m+1}+… и V₂+V_m не имеет локального минимума, существует
   асимптотическая траектория» **приписано не той статье**: эта формулировка взята из рецензии zbMATH
   на **[Koz86]** (Козлов, ПММ 50:6, 1986), см. §2.6.
2. **[AMM93] — склейка трёх разных работ.**
   - Moauro–Negrini: *V. Moauro, P. Negrini, On the inversion of Lagrange–Dirichlet theorem*,
     **Differential and Integral Equations 2:4 (1989), 471–478**, doi:10.57262/die/1371648438
     (Crossref, zbMATH 4176538, Rauch, BMP21, BP22, Alva–Garcia, список литературы Паламодова 2020
     [34]). Не J. Appl. Math. Mech. и не 1993.
   - PII 002189289190002C = **K. Peiffer, On inversion of the Lagrange–Dirichlet theorem, J. Appl. Math.
     Mech. 55:4 (1991), 436–441**, doi:10.1016/0021-8928(91)90002-C (Crossref). Содержание не видел.
   - doi:10.1007/BF00962611 = **M. Sofer, On the inversion of the Lagrange–Dirichlet stability theorem
     — mechanical and generalized systems, ZAMP 34:1 (1983), 1–12** (Crossref), не Moauro–Negrini.
   - Продолжение: C. Maffei, V. Moauro, P. Negrini, *On the inversion of the Lagrange–Dirichlet theorem
     in a case of nonhomogeneous potential*, Differential Integral Equations 4:4 (1991), 767–782,
     doi:10.57262/die/1371225014.
3. **[Tal80b] и [Tal80a]: путаница с названиями.** Верно: Taliaferro, *Stability for two dimensional
   analytic potentials*, JDE 35:2 (1980), 248–265, doi:10.1016/0022-0396(80)90042-X. Несмотря на
   название, по всем вторичным источникам результат — **неустойчивость** (см. §2.4). А KNOWN пишет
   «Устойчивость для двумерных аналитических потенциалов» — **неверно**.
4. **Koz86: год и страницы.** Английская версия: J. Appl. Math. Mech. 50:6, 719–725 (Crossref: 1986,
   zbMATH: 1986; часть авторов пишет 1987). Русский оригинал: ПММ 50:6 (1986), 928–937 (так в списке
   литературы Паламодова 2020 [33]). doi:10.1016/0021-8928(86)90079-1. [Koz86] = именно эта статья
   (PII 0021892886900791 совпадает по форме).
5. **Koz82** (одиночная работа Козлова): Асимптотические решения уравнений классической механики, ПММ
   46:4 (1982), 573–577; англ. JAMM 46:4, 454–457, doi:10.1016/0021-8928(82)90029-6. Не путать с [KP82].
6. **Alva–Garcia**: авторы и год. Qual. Theory Dyn. Syst. 16:2 (2017), 371–389, doi:10.1007/s12346-016-0196-x
   (online 29.03.2016); arXiv:1508.07427 (v2, 05.03.2016). Имена: Gerard John Alva Morales и Manuel
   Valentim de Pera Garcia (так в Crossref и zbMATH 6841286).
7. **Palamodov 1977**: FAA 11:4 (1977), 42–55 (рус.); англ. Funct. Anal. Appl. 11 (1977/78), 277–289,
   doi:10.1007/BF01077142 (zbMATH 3646342 даёт год 1978). Нейтральный вывод: годы 1977/1978 оба
   встречаются, оригинал — 1977.

## 1. Текст задачи 1971-4

**Английская формулировка, дословно** (три независимых цитирования одним и тем же текстом):

> «1971-4. Prove the instability of the equilibrium 0 of the analytic system ẍ = −∂U/∂x in the case
> where the isolated critical point 0 of the potential U is not a minimum.»

Источники цитаты, все **ПП** (открыты, pdftotext): Burgos–Maderna–Paternain, arXiv:1906.11962v3,
§1; Burgos–Paternain, arXiv:2208.01139v1, §1; Burgos, arXiv:2108.05829v4, §1. Во всех сказано:
[Ar] = V. I. Arnold, *Arnold's Problems*, Springer-Verlag 2002 (в BMP21 [Ar] датирована 2002; в
изд-ве Springer — 2004, Berlin–Heidelberg, ISBN 3-540-20748-1; Google Books: «Springer, 2004, 640 pp»;
KNOWN даёт doi:10.1007/b138219 — не проверял). Русский оригинал в этих статьях не цитируется.

**Комментарий.** [Литература: BMP21 = arXiv:1906.11962v3, §1, ПП, вторичная цитата] «For the
bibliography and comments related to the problem we highly recommend the comment section in [Ar],
pages 250-253. In that section, the authors recognize the fact that: “...The problem on the converse
of the Lagrange-Dirichlet theorem makes therefore sense only under one or another additional
assumptions (e.g., that of analyticity of the potential).”»

- Из этой цитаты: комментарий написан **несколькими авторами** («the authors»), стр. 250–253
  (английского издания). Какие именно авторы и что ещё сказано об 1971-4 (результаты Козлова,
  Паламодова, Taliaferro и т. д.), — **не удалось установить**. Фразы вида «Арнольд сам прокомментировал
  статус» подтверждения не имеют.
- Rauch (Sém. Laurent Schwartz 2013–2014, exp. XII, §2.4, **ПП**): «In his 1976 talk on the Hilbert
  Problems, Arnold proposed his own problems. One is to prove that for x″ = −∇V(x), if V ∈ C^ω and x is
  an equilibrium that is not a local minimum, then the equilibrium is unstable. The conjecture is easy
  when d = 1. Taliaferro [10] proved the case d = 2 in 1980.» Ссылка [2] у Rauch: V. Arnold,
  *Mathematical developments arising from Hilbert problems*, Proc. Symp. Pure Math., AMS, 1976. Это
  версия без «изолированной»: **расхождение с 1971-4** (у Rauch просто «not a local minimum»). Открытая
  проблема для главного агента: сверить с самим текстом Арнольда 1976 (Proc. Symp. Pure Math. 28);
  я его не открывал.
- Burgos (arXiv:2108.05829v4) называет 1971-4 «the related open Arnold's conjecture» и приводит
  вопрос Ляпунова ([Ly], §25): «But, in establishing that this condition is sufficient, the theorem in
  question does not allow any conclusion about the necessity of the same condition. That is why the
  question arises: will the position of equilibrium be unstable if the force-function is not maximum?»
  (то же в BP22 с английским переводом книги Ляпунова, Ann. of Math. Studies 17, 1947).
- Burgos 2025 (arXiv:2506.19135v1, **ПТ**): «In [Ar], Arnold proposed the problem of instability of an
  isolated non-minimum critical point of a real analytic potential in Newtonian mechanics. Even this
  simplified version of the Lagrange-Dirichlet converse remains open.»
- Издания. Русское: «Задачи Арнольда», М.: ФАЗИС, 2000 (по описанию издателей; не открывал). Более
  поздних русских изданий не нашёл; Google Books упоминает «Arnold's Problems», Springer 2004
  (illustrated reprint, limited preview) и издание 2009 (no preview) — тип 2009 не установлен.

**Вердикт по §1:** формулировка 1971-4 — **подтверждено** (дословно, по трём ПП). «Точный русский
текст и комментарии в книге» — **не удалось проверить**; о комментарии известно только: стр. 250–253,
несколько авторов, цитата выше.

Вторичная оговорка: у Burgos «problem 1971-4» — Лагранжевая (n-мерная) задача A. Постановка для
«real-analytic U in neighbourhood of 0 ∈ ℝⁿ, Lyapunov instability» в PROBLEM.md — перефразировка
(в книге сказано только «instability»; смысл «по Ляпунову» взят из комментариев Burgos). [Гипотеза].

## 2. Построчная сверка таблицы §2

### 2.1 Лагранж (1788), Дирихле (1846)
- Лагранж, *Mécanique analytique*, 1788; Dirichlet, «Über die Stabilität des Gleichgewichts», J. Reine
  Angew. Math. 32 (1846), 85–88 (по спискам литературы BMP21, BP22, Паламодов 2020 [3]).
- Формулировка: [Литература: BP22, §1, ПП] «Theorem (J. L. Lagrange, L. G. Dirichlet). Every strict
  local minimum of the potential is a Lyapunov stable equilibrium point» (механическая лагранжиана
  L = Q − U). Taliaferro 1990, РЦ zbMATH 4114130: «If L is continuously differentiable and U assumes
  a strict local minimum at x = 0, then the Lagrange–Dirichlet theorem states that the origin for (1)
  is stable». Негрини 1995, Thm 1.1: h = 2 (C²).
- **Подтверждено** (с оговоркой: достаточно C¹ по Taliaferro 1990).

### 2.2 Ляпунов (1892 / 1897)
- Диссертация 1892 (Харьков; франц. перевод 1907, англ. Ann. of Math. Studies 17, 1947): вопрос о
  необходимости (§25, цитата выше). Статья A. M. Liapounoff, «Sur l'instabilité de l'équilibre dans
  certains cas où la fonction de forces n'est pas un maximum», J. Math. Pures Appl. (5) 3 (1897), 81–94
  (список Паламодова 2020 [5]; Alva–Garcia [L]; Garcia–Tal [4]).
- [Литература: Garcia–Tal, препринт RT-IME-USP 0101 (2001), §1, ПП] «Liapounof proved in 1897 that, if
  q₀ is not a local minimum of π and this fact is shown by the second order derivatives of π, then
  (q₀;0) is an unstable equilibrium of (1)» («jet of order 2 shows that π does not have a minimum»).
  Ляпунов гипотетически расширил это на джет порядка k (Alva–Garcia, intro; Garcia–Tal intro). Rauch §2.3:
  «if the hessian of V at an equilibrium has at least one strictly negative eigenvalue then there is
  instability by a theorem of Lyapunov».
- Вторая половина строки KNOWN («Если U имеет максимум, определяемый младшей формой U_m — тоже»):
  по тексту не подтверждено и **двусмысленно** («максимум» чего). Ни в одном открытом источнике не
  нашёл приписывания Ляпунову утверждения про младшую форму U_m. **Неточно**: оставить только
  утверждение про гессиан (Ляпунов 1897/1892) и вопрос в §25; про U_m — не удалось проверить.

### 2.3 Четаев
- N. G. Chetaev, «О неустойчивости равновесия в некоторых случаях, когда функция сил не есть максимум»,
  ПММ 16:1 (1952), 89–93 (так у Паламодова [18], BP22 [Ch]).
- [Литература: Негрини 1995, Thm 1.2, ПП; формулировка приведена там со своим доказательством]:
  «Consider the natural Lagrangian function L(q,q̇) = T^{(2)}(q,q̇) + U_{[k]}(q), U_{[k]} being a
  homogeneous function of degree k, k ≥ 3. Let q = 0 be not a maximum point for U_{[k]}; then it is an
  unstable stationary solution.» (U — функция сил; не максимум функции сил = U_pot принимает
  отрицательные значения.) Функция Четаева V = (q, ∂T/∂q̇). Изолированность критической точки не
  требуется (замечание Негрини).
- Alva–Garcia (intro): «a classical result of Cetaev (see [LHR]) establishes the instability of the origin
  when ⟨∇Π(q), q⟩ < 0 for all q in a connected component of Π⁻¹(−∞, 0)».
- **Подтверждено** (деgree k ≥ 3; для k = 2 — Ляпунов). Уточнить в KNOWN: «однородный потенциал
  степени k ≥ 3»; критерий Четаева в общем виде — условие ⟨∇Π, q⟩ < 0 на компоненте {Π < 0}.

### 2.4 Hagedorn (1971) [Hag71]
- P. Hagedorn, Die Umkehrung der Stabilitätssätze von Lagrange–Dirichlet und Routh, ARMA 42:4 (1971),
  281–316, doi:10.1007/BF00282334 (МД, zbMATH 3352815; аннотации нет).
- [Литература: Негрини 1995, §3, Thm 3.1, ПП] «Hagedorn … considered a C² natural Lagrangian function,
  and assumed q = 0 to be a proper minimum for U [функция сил]. … Theorem 3.1. Let L ∈ C²(B_b × ℝⁿ, ℝ)
  be a natural Lagrangian function. Assume U(q) > 0 if q ∈ B_b∖{0}. Then there exists r ∈ (0, b) such
  that any point q₀ ∈ B_r is connected to q = 0 by a solution of the Lagrangian system, having an
  arbitrarily small positive energy E and entirely lying in B_b.» То есть это **строгий максимум
  потенциальной энергии** (метод Якоби–Мопертюи + Каратеодори). BP22 и Burgos 2025: «a local strict
  maximum of a smooth potential is Lyapunov unstable for any smooth kinetic term» (Hagedorn),
  «improved by Taliaferro [Ta2] for local maxima and by Sofer [So] …».
- **Вердикт: неверно (первая половина строки).** Утверждение «если младшая ненулевая форма U_m
  принимает отрицательные значения, равновесие неустойчиво» Hagedorn 1971 не доказывает (по Негрини
  это Четаев/Паламодов/Козлов–Паламодов/Козлов). Правка: Hagedorn 1971 — неустойчивость строгого
  локального максимума потенциала для C²-лагранжиана (C² потенциал и кинетика, любая гладкая кинетика).
  Вторая половина («строгий локальный максимум … при любой гладкой кинетике») — подтверждена по
  Негрини, BP22, Burgos 2025 (ВИ/ПП, не по оригиналу).

### 2.5 Taliaferro 1980: [Tal80a] (ARMA 73) и [Tal80b] (JDE 35)
- [Tal80a] S. D. Taliaferro, An inversion of the Lagrange–Dirichlet stability theorem, ARMA 73:2 (1980),
  183–190, doi:10.1007/BF00258236 (МД, zbMATH 3664467, MSC 70H03, 70F20; аннотации нет). Содержание
  — **максимумы потенциала** (Ureña 2020 в Ann. Mat. Pura Appl. по поиску; BP22: «This result was later
  improved by S. D. Taliaferro in [Ta2] for local maximums»; Негрини 1995, §3: «under the assumption of
  U ∈ C¹ only the instability result was successively obtained by Taliaferro [20] and later on by
  Mawhin and Hagedorn himself [21]»). Статус — **ВИ**; формулировку не видел. KNOWN: «Неустойчивость
  максимумов потенциала» — **подтверждено по ВИ** (минимальная гладкость C¹ — по Негрини).
- [Tal80b] JDE 35:2 (1980), 248–265. Аннотации нет (zbMATH 3618573, MSC 34D20). Формулировка по ВИ:
  BP22 §1 (ПП): «V. P. Palamodov in [Pa2] and S. D. Taliaferro in [Ta] showed independently the
  instability of a non local minimum critical point of a real analytic potential in dimension two for a
  Newtonian kinetic term.» Негрини 1995, Thm 2.1: «Let U ∈ C^ω(B_b, ℝ), B_b ⊂ ℝ². Assume q = 0 be a
  critical point for U, which is not a maximum; then it is an unstable equilibrium of the differential
  system q̈ = ∇U(q)» [функция сил; т. е. не минимум потенциальной энергии]. Rauch: «Taliaferro [10]
  proved the case d = 2 in 1980». Burgos (arXiv:2108.05829v4): «The Lagrange–Dirichlet converse for two
  degrees of freedom real analytic potentials follows from the results of Palamodov [Pa3] or Taliaferro
  [Ta] in conjunction with those of Kozlov [Ko1] and Laloy and Peiffer [LP]». Статус — ВИ (4 независимых
  автора), оригинал не открывал.
- **Вердикт: неверно** («Устойчивость для двумерных аналитических потенциалов»). Правка: «неустойчивость
  равновесия при n = 2, U аналитична, ньютоновская кинетика (T = |ẋ|²/2), критическая точка не является
  локальным минимумом (в то время как случай нестрогого минимума — Laloy–Peiffer)». «Точная
  формулировка не установлена» — осталась (изолированность/асимптотическая траектория: не видно).
- [Tal90] (в KNOWN отсутствует, нужен): S. D. Taliaferro, Instability of an equilibrium in a potential
  field, ARMA 109:2 (1990), 183–194, doi:10.1007/BF00405242 (МД, zbMATH 4114130, РЦ — **прочитана
  аннотация**). Аннотация: T, U ∈ C², U^{(i)}(x) = U_p^{(i)}(x) + O(‖x‖^{p+ε−i}) (i = 0, 1, 2; p > 0,
  0 < ε ≤ 1), U_p положительно однородна степени p и C³ вне нуля; «If, for some x ∈ ℝⁿ∖{0},
  U_p(x) < 0 then we will prove that there is a solution, x(t), of (1) such that ‖x(t)‖ + ‖x′(t)‖ → 0
  as t → 0⁺, when 0 < p < 2; and as t → −∞, when p ≥ 2. In particular … the origin for (1) is not
  stable.» (Rauch: «The differentiability hypothesis is radically reduced in [11]»; Негрини Thm 4.3.)
  Здесь гладкость C², аналитичности нет, n произвольно, нужна однородная ведущая часть.

### 2.6 Козлов 1979–1986
Выходные данные:
- [Koz81]: В. В. Козлов, Неустойчивость равновесия в потенциальном поле, УМН 36:1 (1981), 209–210;
  Russ. Math. Surv. 36:1 (1981), 238–239, doi:10.1070/RM1981v036n01ABEH002551 (zbMATH 3752280, 3720400;
  содержание не видел; iopscience — только метаданные). Второй номер: Russ. Math. Surv. 36:3 (1981),
  256–257, «On the instability of equilibrium in a potential field» (zbMATH 3887121, MSC 70C20;
  содержание недоступно), русский — УМН 36:3 (1981), 215–216 (по KNOWN; не проверено). Палaмодов 2020
  [25] цитирует другую работу Козлова 1981: ПММ 45:3 (1981), 570–572 («…с учётом сил вязкого трения»).
- По ВИ: BP22 (§1, ПП): «Based on the previous Palamodov's work, this result [n = 2, non-minimum] was
  generalized by V. V. Kozlov in [Ko] for an arbitrary kinetic term», [Ko] = Kozlov, Instability of
  equilibrium in a potential field, Russ. Math. Surv. 36 (1981), 238–239. Burgos arXiv:2108.05829 тоже
  называет [Ko1] для n = 2. Статус — ВИ.
- **[Koz82]** (одна работа Козлова, JAMM 46 (1982) 454–457) и **[KP82]** (Dokl. 263:2 (1982) 285–289;
  англ. Sov. Math. Dokl. 25 (1982), 335–339; zbMATH 3795409, рецензия пустая). Негрини 1995, Thm 2.2,
  ПП: «Let L be a natural analytic Lagrangian function and assume that there exists a positive integer
  k, k ≥ 3, such that the Mac-Laurin expansion of U starts with an homogeneous polynomial U_{[k]} of
  degree k, having not a maximum at q = 0. Then this equilibrium is unstable.» (Козлов–Палaмодов;
  инструмент — формальное решение, затем сходимость; показано существование **асимптотического**
  движения.) zbMATH, рецензия на [Koz86]: «We proved earlier a claim … about the asymptotic motions for
  the special case when V₂ ≡ 0» (то есть [Koz82]: случай V₂ ≡ 0).
- **[Koz86]**, РЦ zbMATH 4026883 (прочитана): «An existence theorem is proved for asymptotic
  trajectories on the assumption that the Maclaurin series for the potential energy has the form
  V₂+V_m+V_{m+1}+… (V_s is a homogeneous form of degree s) and the function V₂+V_m does not have a
  local minimum at the equilibrium position. … The existence of a trajectory, asymptotic to the
  equilibrium position, naturally implies that this position is unstable in Lyapunov's sense.» Негрини
  1995, Thm 4.1 (ПП): L ∈ C^∞ natural, U = U_{[2]} + U_{[k]} + W, U_{[2]} negative semidefinite
  quadratic form [функция сил], U_{[k]} homogeneous of degree k, **restriction of U_{[k]} on the
  subspace K = {q: U_{[2]}(q) = 0} has not a maximum at q = 0**, W = o(|q|^k) ⇒ there exists a motion
  asymptotic to q = 0 (использует теорему Кузнецова о C^∞-системах). Rauch Thm 4.1 (ПП) формулирует
  более частный случай: «V ∈ C^∞, 0 critical, V ~ V_m + V_{m+1}+…, if the leading term V_m does not
  have a local minimum at 0, then the equilibrium (0,0) is unstable», с оговоркой, что Taliaferro 1990
  снижает требования к гладкости.
- **Вердикт по строке KNOWN:**
  - «[NLM79]» — **неверно** (автор Laloy; пример нужно приписать [Koz86], см. §0.1).
  - Формулировка «V₂+V_m не имеет локального минимума» — по рецензии zbMATH; у Негрини вместо этого —
    условие на ограничение U_k на ядро K формы U₂ (когда U₂ ≥ 0 как потенциальная энергия). Две
    формулировки не равнозначны дословно (граничные случаи V_m|_K ≥ 0 с нулями). **Неточно**: привести
    обе, пометить «оригинал не открывал»; указать гладкость C^∞ потенциала и кинетики.
  - «Для n = 2 и аналитического U без минимума — неустойчивость (Козлов, 1981)» — **подтверждено по
    ВИ** (BP22, Burgos 2021); добавить, что Козлов обобщает на произвольную кинетику результат
    Паламодова 1977 / Taliaferro 1980 (ньютоновская кинетика).
  - Для Козлова 1979 нет ничего: статьи 1979 года у Козлова в этой тематике нет (NLM79 — Laloy), поэтому
    «Kozlov (1979–1986)» → «Козлов 1981–1986».

### 2.7 Козлов–Паламодов (1982) [KP82]
- Dokl. Akad. Nauk SSSR 263:2 (1982), 285–289; англ. Soviet Math. Dokl. 25 (1982), 335–339 (zbMATH
  3795409; рецензия S. Sridhar пуста; поступила 22.09.1981, представил Колмогоров — по ВИ-поиску).
  Формулировка: Негрини Thm 2.2 (см. 2.6): аналитическая натуральная система, ведущая однородная
  форма U_k, k ≥ 3, не максимум функции сил ⇒ неустойчивость + асимптотические траектории. Ср. также
  [Burgos 2025, B25 intro] и «Kozlov–Palamodov» в BMP21 ([KP]). Степень сверки — ВИ (Негрини, ПП),
  оригинал не открывал.
- **Подтверждено** с добавлением формулировки (раньше «точная формулировка не установлена»).

### 2.8 Hagedorn–Mawhin (1992)
- ARMA 120:4 (1992), 327–335, doi:10.1007/BF00380318 (МД). РЦ zbMATH 410086: «The Lagrange–Dirichlet
  stability theorem is reformulated. In the setting of a Hilbert space the proof is made possible by
  the fact that the functional to be varied is strictly coercive.»; Rapp. Sémin. Math. Louvain (1992)
  zbMATH 832069: «…allows a simple and elementary treatment of the instability theorem with minimal
  regularity assumptions».
- Негрини 1995, Thm 3.3 (ПП): «Let L ∈ C¹(B_b × ℝⁿ, ℝ) be a natural Lagrangian and let q = 0 be a
  minimum point for the potential [функция сил]. Then, for any δ ∈ (0, b/2) [так в OCR], there exists a
  solution of the Lagrangian system starting from the initial datum (0, q₀), |q₀| ≤ b, and arriving at a
  finite time on the boundary ∂B_{b−δ}.» Это **максимум потенциальной энергии** (нестрогий разрешён),
  C¹, как и у Taliaferro 1980.
- **Подтверждено** (название и класс), добавить содержание: обращение для (нестрогих) локальных
  максимумов потенциала в классе C¹.

### 2.9 Moauro–Negrini [AMM93] → [MN89] и Maffei–Moauro–Negrini 1991
- Выходные данные см. §0.2. Тексты открыть не удалось (Project Euclid блокирует автоматический доступ).
- По ВИ — Alva–Garcia (intro, arXiv:1508.07427, ПП): «Maffei, Moauro and Negrine in two notable works,
  [MN] and [MMN], they study the case where the jet showing that the origin is not a minimum, is an
  homogeneous polynomial. In fact, they prove more, the main result of these articles proves
  instability of the origin when, after an eventual change of coordinates, the potential energy has the
  form π(q₁,…,q_n) = ‖(q₁,…,q_r)‖² + π_s(q_{r+1},…,q_s) + R(q_{r+1},…,q_s), where 0 ≤ r < s, π_s is an
  homogeneous polynomial of degree s ≥ 2 which does not have a minimum at the origin, and R obeys
  lim R(q)/‖q‖^s = 0.» (в OCR индексы «q_{r+1..s}» искажены; смысл — квадрат по части переменных +
  однородная форма от остальных + o(|q|^s).) Garcia–Tal (препринт, §1): «if the k jet of π at q₀ is
  homogeneous and shows that π doesn't have a minimum at this point, then (q₀;0) is an unstable
  equilibrium for (1)»; сноска про требуемую гладкость класса C^{k+α} (OCR нечёткий) и что Taliaferro
  расширил однородный случай на более широкий класс потенциалов.
- Негрини 1995, Thm 4.4 (ПП): «Let L be a natural Lagrangian function, L ∈ C^h(B_b × ℝⁿ, ℝ), h > k > 2,
  h, k ∈ ℕ. Let U be the potential function: U(q) = U_{[k]}(q) + W(q). Here U_{[k]} is a homogeneous
  polynomial of degree k having not a maximum at q = 0, W(q) = o(|q|^k). Then the Lagrangian system has
  a motion asymptotic in the future to the origin.» Негрини сопоставляет это с [28] = Moauro–Negrini
  (1989) и «Later on in [29] [MMN 1991] an analogous of Theorem 4.1 [Козлов] under a weaker regularity
  assumption … L ∈ C^h (h ≥ k + m(k) + 3, m(k) the integral part of (k−3)/2 [OCR: «k−3 над 2»])».
  Негрини, как и OCR, ошибся в библиографии ([27] = Taliaferro 1989 ARMA 73): для Thm 4.3 нужен
  Taliaferro 1990 (Tal90). Сопоставление тем «Thm 4.4 = [MN89]» — моя интерпретация (в тексте Негрини
  оно по смыслу: «two similar results … independently obtained in [27] and [28]»). [Гипотеза]
- **Вердикт по строке KNOWN: неточно / неверные выходные данные.** Исправить: «Moauro–Negrini, DIE 2
  (1989), 471–478: естественная лагранжиана L ∈ C^h, h > k > 2 (по Негрини, Thm 4.4), U = U_k + W,
  U_k — однородный многочлен степени k без минимума потенциальной энергии, W = o(|q|^k) ⇒ асимптотическая
  траектория; обобщение (MMN 1991) на U = ‖x‖² + U_s(y) + R. Метод — по Негрини Thm 4.4: замена
  q = z(t)(e + Q), расширенная автономная система, устойчивое многообразие неподвижной точки.»
  Слова «инвариантные устойчивые многообразия» KNOWN по смыслу совпадают с этим описанием, остальное
  («J. Appl. Math. Mech.», «1993», «минус потенциал»/«силовая функция» — с PII Peiffer 1991) не
  подтверждено и не относится к Moauro–Negrini.

### 2.10 Garcia–Tal (2003)
- M. V. P. Garcia, F. A. Tal, J. Differential Equations 194:2 (2003), 364–381,
  doi:10.1016/S0022-0396(03)00167-0 (bronze OA на Elsevier; не скачивал). Прочитан препринт
  **RT-IIAP-0101 (IME-USP, июль 2001)** по ссылке в репозитории USP (свободный доступ,
  repositorio.usp.br/item/001195554) — это ПП, не журнальная версия.
- Аннотация препринта, дословно: «We consider Ω ⊂ ℝ² an open neighborhood of the origin and the
  Lagrangian L = T − π, where π: Ω → ℝ of class C² is the potential energy with a critical point at the
  origin and T: Ω × ℝ² → ℝ is the kinetic energy, of class C². We assume that π has jet of order k at
  the origin, and this jet shows that the potential energy does not have a minimum in Ω. With these
  hypotheses we prove that (0;0) is an unstable equilibrium according to Liapounoff for the Lagrange
  equations of L. We achieve this by proving that there is an asymptotic trajectory to the origin.»
- Определение: «We say that j^k f shows that f does not have a local minimum at 0 if, for every function
  g: Ω → ℝ such that j^k g = j^k f, 0 is not a local minimum of g.» Условия: π = P + R, P — k-джет,
  R = o(|q|^k) (π не обязана быть C^k), T положительно определена, класса C², n = 2. Основная
  лемма опирается на (Fact 1) кривую «вертикальных минимумов» P — алгебраическую, ряд Пюизё.
- Там же, §1: «Since Barone, Gorni and Zampieri proved in [2] that for every analytical function f
  without a minimum at q₀ there is an integer k such that j^k f shows that f doesn't have a minimum at
  this point, our result extends the Palamodov's result for systems with two degrees of freedom.
  Moreover we provide a positive answer for a conjecture posed by V. V. Kozlov in [3] concerning the
  existence of asymptotic trajectories to (q₀;0) for the analytic case, which was not proved by
  Palamodov in [8].» [3] = Kozlov, *Problemata nova*, Transl. AMS (2) 168 (1995), 141–171; [8] = Palamodov,
  Transl. AMS (2) 168 (1995), 5–20; [2] = Barone Netto, Gorni, Zampieri, *Local extrema of analytic
  functions*, NoDEA 3:3 (1996), 287–303.
- **Вердикт: подтверждено**, формулировка в KNOWN верна, но надо добавить: гладкость C² (потенциал
  и кинетика), потенциал имеет k-джет, доказательство даёт асимптотическую траекторию; n = 2.
  Зависимость от изолированности критической точки: нет (условие — «джет показывает отсутствие минимума»).
  Для журнальной версии отличий не проверял.

### 2.11 Alva–Garcia (2017)
- [AG17] ПП: arXiv:1508.07427v2 (прочитан полностью текст введения и теорем).
  Аннотация: «We study the stability of an equilibrium point in a conservative Hamiltonian system in the
  case that equilibrium is not a minimum of the potential energy and this fact is shown by a jet of
  this function. Thanks to a modification of a result of Krasovskii, we prove that for a large class of
  systems under these conditions equilibrium is unstable and there is an asymptotic trajectory to that
  point.»
- Условия: H = T + Π, Π: Ω → ℝ класса C², T = ½⟨B(q)p,p⟩ (B положительно определена), n любое.
  Класс H: (H1) j^ℓΠ ≥ 0 в окрестности нуля при ℓ ≤ s−1; (H2) j^sΠ показывает, что у Π нет минимума
  в нуле; (H3) существует компонента A* множества A_s = (j^sΠ)⁻¹(−∞,0) и ε > 0 с
  (A*∖{0}) ∩ B_ε ⊂ C_s° ∩ B_ε, где C_s = {q: R^s_Π(q) = ⟨∇j^sΠ(q), q⟩ < 0}. Theorem 1 (дословно):
  «If the potential energy of a conservative Hamiltonian system is of class H then it has the strict
  Cetaev's condition.» Proposition 8 (дословно): «Let H = T + Π be a Hamiltonian function defined in
  Ω × ℝⁿ, where the potential energy of class C², Π: Ω → ℝ, has a critical point at 0 ∈ Ω. If there
  are ε > 0 and a connected component C of Π⁻¹((−∞,0)) adherent to the origin such that
  ⟨∇Π(q), q⟩ < 0 for q ∈ (C∖{0}) ∩ B_ε then there is an asymptotic motion to 0 in equations (1).»
  Вывод — совместно: класс H ⇒ асимптотическая траектория ⇒ неустойчивость. Модификация теоремы
  Красовского (Prop. 7).
- Библ. данные: см. §0.6. **Вердикт: подтверждено**, но формулировка KNOWN «для большого класса систем»
  слишком расплывчата; нужно: C² потенциал, условия (H1)–(H3) на джет (не «джет показывает отсутствие
  минимума» вообще, а ещё и условия на радиальную производную и положительную полуопределённость младших
  джетов). Пример, который не покрывается: U = x⁴ + y⁴ − z⁶ (BP22; младший ненулевой джет x⁴+y⁴ имеет
  минимум). Класс H — условие (H1)–(H3), не чисто «джет без минимума».

### 2.12 Дополнительно: Паламодов 1977, 1992, 1995 (в §5, но влияет на §2)
- [P77] FAA 11:4 (1977), 42–55 (ПП не открывал; Негрини 1995 Thm 2.1 и две «леммы» перечислены выше).
  Негрини, Thm 2.1 (ВИ): n = 2, U аналитична, критическая точка не максимум функции сил ⇒ неустойчива.
  Первая лемма: на связной компоненте положительных значений U_ρ^+ , замыкание которой содержит 0,
  есть непрерывное поле u, C¹ вне конечного числа C^∞-кривых K, с ⟨u, ∂U/∂q⟩ ≥ 0 и
  (∂u_i/∂q_j) w_i w_j ≥ C|w|². Вторая лемма: «Let U be an analytic function in a two-dimension domain
  containing the origin q = 0. Then, for a suitable small ρ, U_ρ^+ cannot contain critical points of
  U.» — именно здесь работает аналитичность при n = 2.
- Негрини 1995, Thm 2.3 (ВИ): Palamodov, «On the instability of motion with several degrees of
  freedom», Preprint, Moscow (1992) — утверждение для натуральных аналитических систем любой
  размерности: «Let U(0) = 0 be not a maximum. Then there exists a neighborhood V₀ ⊂ B_b such that any
  motion starting in V₀ with arbitrarily small positive energy E leaves V₀ in a finite time τ(E).»
  Негрини принимает его как теорему и выводит Corollary 2.4 (C^∞-потенциал с критической точкой
  конечной кратности). Burgos 2021 (arXiv:2108.05829v4, intro): «although the proof is illuminating …
  unfortunately it is not a complete argument … leaving the announced Theorem so far as a conjecture»
  (по [Pa] = Transl. AMS 168 (1995), 5–20); Allaire–Rauch: «A detailed proof has never been published.»
  zbMATH 826088 (P95): «one gets an inversion of the Lagrange–Dirichlet theorem for any critical point
  where the analytic potential function does not have a minimum.» **BMP21** (v3, 2021) писал: «In [Pa],
  Palamodov completely solves the Arnold's problem … In particular, to prove the Lagrange–Dirichlet
  converse, only the case of a non strict local minimum critical point is left»; позднее тот же автор
  (arXiv:2108.05829, 2208.01139) считает результат только гипотезой. Для KNOWN: «ситуация со статусом
  Паламодова 1992/1995 в литературе противоречива; BMP21 и Негрини 1995 принимали теорему, Burgos 2021,
  Allaire–Rauch, Паламодов 2020 — нет (гипотеза 1)».

## 3. Пункт 3: n = 2

Утверждение KNOWN (конец §2): «Для n = 2 аналитический случай, по-видимому, разобран полностью:
Козлов, Taliaferro, для нестрогих минимумов — Laloy–Peiffer».

[Литература: BP22 = Burgos–Paternain, arXiv:2208.01139v1, §1, ПП, дословно] «For two degrees of
freedom, this problem was completely solved. Indeed, V. P. Palamodov in [Pa2] and S. D. Taliaferro in
[Ta] showed independently the instability of a non local minimum critical point of a real analytic
potential in dimension two for a Newtonian kinetic term. Based on the previous Palamodov's work, this
result was generalized by V. V. Kozlov in [Ko] for an arbitrary kinetic term. The remaining case of a non
strict local minimum was treated in [LP] by M. Laloy and K. Peiffer who showed the instability of such a
point for a real analytic potential. This completes the proof of the analytic Lagrange-Dirichlet
converse in dimension two.» (там же: [Pa2] = Palamodov, Funct. Anal. Appl. 11 (1977); [Ta] =
Taliaferro, JDE 35 (1980); [Ko] = Kozlov, RMS 36 (1981) 238–239; [LP] = Laloy–Peiffer, ARMA 78
(1982) 213–222.) Почти идентичная фраза — Burgos 2025 (arXiv:2506.19135v1, **ПТ**, §«instability
problem»): «In dimension two, the result follows from a collection of independent results [Pa], [Ta],
[Ko], [LP]. There is an elegant proof given by Brunella in [Br] …» Негрини 1995 (ПП): Thm 2.1
(Palamodov, затем независимо Taliaferro), «This problem [non-strict minimum] was solved in the case of
two degree of freedom by Laloy et al. [14]. The general case of any degree of freedom is still open.»

Что именно доказано (ВИ; оригиналы не открывались, кроме Brunella и Taliaferro-1990-аннотации):

| Работа | Что | Что используется |
|---|---|---|
| Палaмодов 1977 | n = 2, U аналитична, точка принадлежит замыканию {U < U(p)} ⇒ неустойчивость (и «тотальная неустойчивость» — это лишь термин P20; в 1977 — «равновесие неустойчиво»). | аналитичность (лемма: нет критических точек в компоненте), ньютоновская (евклидова) кинетика для конструкции поля. Изолированность критической точки в формулировке Негрини **не** требуется. |
| Taliaferro 1980 | то же, независимо. | аналитичность, ньютоновская кинетика. |
| Козлов 1981 | то же для произвольной римановой кинетики (BP22: «arbitrary kinetic term»). | на основе Паламодова. Оригинал не видел. |
| Laloy–Peiffer 1982 | n = 2, аналитический U с **нестрогим** минимумом ⇒ неустойчивость. ARMA 78:3 (1982) 213–222, doi:10.1007/BF00280037 (МД; аннотации нет; ранее — Rapport Louvain 134, 1980, zbMATH 3696551). | точная формулировка не видел; **ВИ** (BP22, Burgos 2021, Негрини); KNOWN, §4: «если минимум нестрогий и достигается вдоль кривой через 0» — по ВИ не подтверждено. |
| Garcia–Tal 2003 | C² потенциал с джетом k, показывающим отсутствие минимума (n = 2) ⇒ асимптотическая траектория (+ BGZ 1996 для аналитических). | C²; не использует изолированность. |
| Brunella 1998 | Corollary (ПТ, дословно): «Consider the second order differential equation q̈ = −grad F where F is an analytic function on a neighbourhood V of 0 ∈ ℝ² such that 0 is an isolated critical point which is not a minimum nor a maximum. Then there exists initial conditions (q₀, q̇₀) ∈ V × ℝ² (resp. …) such that the corresponding solution tends to (0,0) as the time tends to +∞ (resp. −∞).» | **изолированная** критическая точка нужна; максимум отдельно (Мопертюи + Хопф–Ринов); теорема о векторном поле на аналитическом 3-многообразии с изолированной особенностью и звеном с эйлеровой характеристикой ≠ 0. Brunella пишет, что это «refinement of a (not too) particular case of a theorem of Palamodov [Pa]» ([Pa] = FAA 11 (1977)). |

**Вердикт: неточно.**
1. Кто: добавить Палaмодова (1977, независимо и раньше/одновременно с Taliaferro); у Козлова — обобщение на произвольную кинетику (по BP22).
2. Что: неустойчивость по Ляпунову (в зависимости от работы — ещё и асимптотическая траектория: Garcia–Tal, Brunella). Асимптотическая траектория при n = 2 (аналитический потенциал без минимума): Garcia–Tal (jet-условие + BGZ, пр. [GT03]) и Brunella (изолированная критическая точка, не min и не max).
3. Нужна ли изолированность: у Паламодова 1977/Taliaferro/Козлова — нет (по формулировке Negrini); у Brunella и в формулировке 1971-4 — да; у Garcia–Tal — нет.
4. Слова «по-видимому, разобран полностью» заменить на: «полностью разобран по ВИ (BP22, Burgos 2025), но оригиналы Козлова 1981, Taliaferro 1980, Laloy–Peiffer 1982 не сверены; см. ПП-цитату BP22». Самое важное: для Паламодова 1977 при n = 2 в P20 обзоре (по заметкам vlad-claude, не мной) идёт ссылка на тотальную неустойчивость в n = 2.

## 4. D'Acunto–Kurdyka [DK05]

- Выходные данные (ПТ — открытый PDF на сайте издателя IMPAN, CC-BY; Crossref): D. D'Acunto
  (Pisa), K. Kurdyka (Le Bourget-du-Lac), *Explicit bounds for the Łojasiewicz exponent in the gradient
  inequality for polynomials*, Annales Polonici Mathematici **87** (2005), **51–61**,
  doi:10.4064/ap87-0-5, MSC 32Bxx, 34Cxx; 32Sxx, 14P10.
- Дословно, аннотация (ПТ): «Let f: ℝⁿ → ℝ be a polynomial function of degree d with f(0) = 0 and
  ∇f(0) = 0. Łojasiewicz's gradient inequality states that there exist C > 0 and ϱ ∈ (0, 1) such that
  |∇f| ≥ C|f|^ϱ in a neighbourhood of the origin. We prove that the smallest such exponent ϱ is not
  greater than 1 − R(n, d)^{−1} with R(n, d) = d(3d − 3)^{n−1}.»
- Основная теорема (ПТ, §1): «**Main Theorem.** The Łojasiewicz exponent ϱ_f satisfies
  ϱ_f ≤ 1 − 1/(d(3d−3)^{n−1}). More precisely ϱ_f ≤ 1 − R(n, d)^{−1}, where
  R(n, d) = max{d(3d−4)^{n−1}, 2d(3d−3)^{n−2}}.» (для d ≥ 2, deg f = d, f(0) = 0; в тексте введения
  — для любого целого d ≥ 2 и любого многочлена от n переменных степени d с f(0)=0.) Определение:
  ϱ_f — инфимум показателей ϱ, при которых неравенство (1.1) |∇f(x)| ≥ C|f(x)|^ϱ выполнено
  в некоторой окрестности U начала с некоторой константой C > 0 (по Bochnak–Risler ϱ_f рационален и
  достигается). Оценка не требует изолированности критической точки; Gwoździewicz (изолированный
  нуль, т. е. строгий локальный экстремум) даёт 1 − 1/((d−1)ⁿ+1). Авторы сообщают, что ту же оценку
  независимо получил A. Gabrielov [Ga] (в более общей ситуации).
- **Вердикт: подтверждено** (формула и источник верны). Добавить: показатель — локальная характеристика
  (окрестность зависит от f; константа C не явная); d ≥ 2; уточнённая оценка с
  max{d(3d−4)^{n−1}, 2d(3d−3)^{n−2}} в основной теореме строго лучше (или равна) d(3d−3)^{n−1}.
  Формула в KNOWN совпадает с аннотацией. «изолированность и неотрицательность проверяются
  алгоритмически» — вне моей задачи.

## 5. Предлагаемые правки KNOWN_RESULTS.md (список, сам файл не правил)

1. §1: добавить дословную цитату комментария BMP21 (стр. 250–253, «…makes therefore sense only under one
   or another additional assumptions (e.g., that of analyticity of the potential)»); пометить, что авторы
   комментария и перечень упомянутых там результатов не установлены; русский текст не открыт.
   Добавить Rauch: Arnold, «Mathematical developments arising from Hilbert problems», Proc. Symp. Pure
   Math. (1976) как возможный исток (у Rauch формулировка без слова «isolated») — сверить.
2. §1, пометка [А] у цитаты — заменить на **[ПП]** (сверено по тексту arXiv:1906.11962v3,
   arXiv:2208.01139v1, arXiv:2108.05829v4).
3. §2, строка Ляпунова: убрать/пометить «не подтверждено» вторую фразу про максимум, определяемый
   младшей формой; оставить гессиан (1892/1897) и ссылку на J. Math. Pures Appl. (5) 3 (1897) 81–94.
4. §2, Четаев: «однородный потенциал степени k ≥ 3», источник — Chetaev, ПММ 16:1 (1952), 89–93 [Негрини
   1995, Thm 1.2]; общий критерий — ⟨∇Π, q⟩ < 0 на компоненте {Π < 0}.
5. §2, Hagedorn 1971: заменить на «неустойчивость **строгого локального максимума** потенциальной энергии
   для C²-лагранжиана (методы Якоби–Мопертюи, Каратеодори)»; первую фразу (про младшую форму U_m)
   удалить; ВИ: Негрини 1995, Thm 3.1.
6. §2, Taliaferro 1980: [Tal80a] ARMA 73 — максимумы потенциала (минимум C¹); [Tal80b] JDE 35 —
   **неустойчивость** (не «устойчивость») при n = 2, аналитическом U без минимума (ньютоновская кинетика);
   [Tal90] ARMA 109:2, 183–194 — добавить в таблицу и библиографию (C²-потенциал, ведущая однородная
   часть степени p, асимптотическая траектория при t → 0⁺ (p<2) или t → −∞ (p ≥ 2)).
7. §2, Козлов: заменить «[NLM79]» ссылкой на [Koz86] и рецензию zbMATH 4026883; формулировку
   «V₂+V_m не имеет локального минимума» дополнить версией Негрини (restriction on ker V₂). Не
   приписывать пример NLM79. Год Koz86: «1986 (англ. JAMM 50:6, 719–725; русск. ПММ 50:6, 928–937)».
   Строку «Kozlov (1979–1986)» → «Козлов (1981–1986)». Добавить: Koz82 (JAMM 46:4, 454–457; случай V₂ ≡ 0),
   FAA 16:4 (1982), 72–73 (гипотеза о существовании асимптотических движений; англ. FAA 16 (1983), 303–304).
8. §2, KP82: добавить формулировку Негрини Thm 2.2 (аналитическая натуральная система; ведущая
   однородная форма степени k ≥ 3 без максимума функции сил ⇒ неустойчивость + асимптотические
   движения).
9. §2, HM92: добавить «обращение для (нестрогих) максимумов потенциала, C¹; вариационный метод
   (минимизация коэрцитивного функционала в гильбертовом пространстве)».
10. §2, AMM93: заменить на **Moauro–Negrini, Differential Integral Equations 2:4 (1989), 471–478,
    doi:10.57262/die/1371648438** + Maffei–Moauro–Negrini, DIE 4:4 (1991), 767–782,
    doi:10.57262/die/1371225014; убрать JAMM 1991/1993 и ZAMP-doi (чужие работы: Peiffer JAMM 55:4
    (1991) 436–441; Sofer ZAMP 34 (1983) 1–12). Формулировка по ВИ (Alva–Garcia, Негрини Thm 4.4):
    U = ‖x‖² + U_s(y) + R с R = o(|y|^s); C^h-лагранжиан, h > k > 2.
11. §2, GT03: добавить гладкость C² (потенциал, кинетика), k-джет, n = 2, асимптотическая траектория;
    ссылка на Barone Netto–Gorni–Zampieri, NoDEA 3:3 (1996), 287–303 (для аналитических U нет минимума
    ⇒ существует k, при котором k-джет показывает отсутствие минимума); doi журнала указать.
12. §2, AG17: гладкость C², условия класса H (H1)–(H3), формулировка Theorem 1/Prop. 8; пример
    x⁴+y⁴−z⁶ не покрыт; авторы Alva Morales и Garcia.
13. §2, последнее утверждение (n = 2): переписать по BP22 дословно; добавить Паламодова 1977; указать,
    что Козлов 1981 — обобщение на произвольную кинетику; Brunella 1998 требует изолированной точки,
    не min и не max; Garcia–Tal — C² + джет.
14. §6 п. 3 / библиография DK05: выходные данные подтверждены (87 (2005), 51–61, doi:10.4064/ap87-0-5);
    добавить условие d ≥ 2, уточнённую оценку R = max{d(3d−4)^{n−1}, 2d(3d−3)^{n−2}} и определение ϱ_f.
15. Библиография: поправить [Hag71] (doi 10.1007/BF00282334), [Tal80b] (doi 10.1016/0022-0396(80)90042-X),
    [Koz86], [AG17], [AMM93], [NLM79] (= Laloy 1979, doi 10.1016/0020-7462(79)90029-5), [HM92] OK,
    [LP82] OK, [GT03] doi 10.1016/S0022-0396(03)00167-0. Добавить [Laloy76]: M. Laloy, On equilibrium
    instability for conservative and partially dissipative systems, Int. J. Non-Linear Mech. 11 (1976),
    295–301, doi:10.1016/0020-7462(76)90015-9 (zbMATH 3524786) — пример Лалуа.
16. §5/[P95]: добавить расхождение статуса: Негрини 1995 (Thm 2.3, преприн́т Паламодова 1992) и
    BMP21 v3 принимали теорему, Burgos 2021 (arXiv:2108.05829v4), Allaire–Rauch, Паламодов 2020 — нет.
    Рецензия zbMATH 826088 (Khmelevskaja-Plotnikova) на [P95] формулирует результат как «inversion
    … for any critical point where the analytic potential function does not have a minimum» и называет
    три открытые задачи.

## 6. Что осталось не сверено

- Оригинальный текст 1971-4 по-русски и комментарий 250–253 (авторы).
- Оригиналы: Козлов 1981 (УМН 36:1 и 36:3), Taliaferro 1980 ×2, Laloy 1979, Laloy–Peiffer 1982,
  Moauro–Negrini 1989, MMN 1991, Palamodov 1977 (Math-Net.Ru недоступен), Peiffer 1991, Sofer 1983,
  Lyapunov 1897.
- Тексты Garcia–Tal 2003 (журнал; читал препринт 2001) и Alva–Garcia 2017 (читал arXiv v2).
- Файлы, использованные для ПП: pdftotext от arXiv (1906.11962v3, 2208.01139v1, 2108.05829v4,
  2108.05074v3, 2506.19135v1, 1508.07427v2), Negrini Resenhas IME-USP 2:1 (1995), 83–114 (открытый
  PDF, journals.usp.br), Rauch exp. XII (centre-mersenne), Brunella AIF 48:5 (numdam/centre-mersenne),
  D'Acunto–Kurdyka (impan.pl, CC-BY), Garcia–Tal RT-IIAP-0101 (repositorio.usp.br).
