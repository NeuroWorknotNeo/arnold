# Сверка §5 KNOWN_RESULTS.md: тотальная неустойчивость, Паламодов, Burgos; новые работы

Дата: 21.10.2026. Автор: агент `literature`. Правила меток: CLAUDE.md.
Конспекты `notes/vlad-claude/*` не читались (сверка независимая).

## 0. Что удалось открыть, а что нет

| Источник | Статус доступа |
|---|---|
| Burgos, arXiv:2108.05829 v1–v4 (PDF) | полный текст прочитан (v4 целиком; v1, v3 — частично, сравнение лемм) |
| arXiv abs-страница 2108.05829 (история версий, комментарий) | открыта |
| Burgos, arXiv:2506.19135 v1 (PDF, 16 стр. в PDF) | введение, §1.1–1.2, формулировки Prop. 1.2, 1.3, Cor. 1.4, Prop. 11.1, Thm 11.4, список литературы прочитаны; доказательства не читались |
| Burgos–Paternain, arXiv:2208.01139 | введение прочитано |
| Enciso–Peralta-Salas, arXiv:2610.27893 | введение и список литературы прочитаны |
| Allaire–Rauch (HAL hal-01321566, препринт) | §1.7 и список литературы прочитаны |
| Паламодов 1977 (Math-Net faa2105) | **не открыт**: сервер www.mathnet.ru недоступен с машины агента (ECONNREFUSED 185.129.147.147:443; curl и WebFetch, также через прокси r.jina.ai) |
| Паламодов 2020 (Math-Net rm9945) | **не открыт**, та же причина. Зеркало journals.rcsi.science: метаданные и список литературы открыты, полный текст «Subscription Access», кнопка PDF отключена; обходить не стал. IOP (RMS): только аннотация |
| Паламодов 1995 (AMS Transl. (2) 168) | не открыт (платно); только библиографические данные из Crossref |
| Козлов–Трещёв 2018 (Mosc. Math. J. 18:4) | не открыт; есть только аннотация через поисковик и слайды |

Следствие: пункты 1 и 3 задания (дословные формулировки основной леммы [P77] и Определения 1, Гипотезы 1,
Теорем 2, 3, 5, 6, Примера 3 из [P20]) **выполнить не удалось**. Повторить, когда Math-Net снова будет
доступен (или владелец скачает PDF и положит в репозиторий; русские PDF свободные).

## 1. Паламодов 1977 (ФАН 11:4, 42–55)

Библиографические данные [Литература: Crossref, zbMATH Open id 3646342; сверено по метаданным, не по тексту]:
В. П. Паламодов, «Об устойчивости равновесия в потенциальном поле», Функц. анализ и его прил. 11:4 (1977), 42–55;
англ.: Funct. Anal. Appl. 11:4 (1977, октябрь по Crossref; zbMATH ставит год 1978), 277–289, doi:10.1007/BF01077142.
Название англ. версии: «Stability of equilibrium in a potential field». Собственная страница Паламодова
(math.tau.ac.il/~palamodo/index20+.pdf) называет эту работу иначе — «Instability of conservative systems with
analytic potential function, Funk. Anal. Appl. 11 N4, 277–288 (1977)» (так в списке; страницы 277–288, а не 289).

Что сказано о содержании во вторичных источниках:
- Burgos–Paternain 2022 (arXiv:2208.01139, введение): «V. P. Palamodov in [Pa2] and S. D. Taliaferro in [Ta]
  showed independently the instability of a non local minimum critical point of a real analytic potential in
  dimension two for a Newtonian kinetic term. Based on the previous Palamodov's work, this result was
  generalized by V. V. Kozlov in [Ko] for an arbitrary kinetic term.» Здесь [Pa2] = P77, [Ko] = Козлов,
  Russian Math. Surveys 36 (1981) 238–239. [Литература: arXiv:2208.01139, введение; полный текст статьи
  читался только во введении]
- Burgos 2021 v4: n = 2 следует из [P77] или Taliaferro, вместе с Козловым и Laloy–Peiffer (для нестрогих минимумов).
- Enciso–Peralta-Salas 2026: «For real-analytic potentials on R^2, Palamodov proved that a critical point that is
  not a local minimum defines an unstable equilibrium [P77]».

**Что именно сказано в тексте P77 (основная лемма, условия на поле v, гладкость, область, условия на u при n = 2) — не проверено.**

Вердикт по утверждению KNOWN_RESULTS §5 «Паламодов (1977)… Основная лемма: если на U^-_ρ есть непрерывное поле v,
гладкое вне конечного числа кривых, с ⟨v,u'⟩≤0 и ⟨v'ξ,ξ⟩≥c|ξ|²…»: **не удалось проверить** (текст не открывался).
Совместимое со вторичными источниками: n = 2 для аналитических потенциалов — да (подтверждено как факт,
но по цитированию, а не по тексту). Утверждение «если u аналитична **или бесконечно дифференцируема с
конечнократной критической точкой**» вторичными источниками не подтверждается и не опровергается.
Атрибуция: Burgos (2021 v4) приписывает общую теорему о тотальной неустойчивости и лемму-аналог (Lemma 4.1,
Theorem 2.1, Corollary 2.2) работе **1995 года**, а не 1977; «Corollary 2.2» там — как раз вывод (A)-подобного
утверждения. Пометка «[Т] прочитаны первые пять страниц» в KNOWN сама по себе ничего не сообщает о том, что
было доказано при n > 2.

## 2. Паламодов 1995, «Stability of motion and algebraic geometry»

Библиография [Литература: Crossref doi:10.1090/trans2/168/02, сверено по метаданным]: V. P. Palamodov,
Stability of motion and algebraic geometry, в сб.: V. V. Kozlov (ed.), *Dynamical Systems in Classical
Mechanics*, Amer. Math. Soc. Transl. Ser. 2, vol. 168, 1995, pp. 5–20. (Т. е. это статья в сборнике под
редакцией Козлова; в KNOWN дано верно, но без названия сборника.)

Текст не доступен (AMS, платно). Что о ней пишут:
- Allaire–Rauch, ARMA 224 (2017), 233–268, §1.7 «Palamodov's outline of proof» [Литература: HAL-препринт
  hal-01321566, сверено по тексту препринта; формулировка в опубликованной версии не сверялась]: «Lyapunov
  conjectured that if V is real analytic and x is an equilibrium that is not a local minimum of V then the
  equilibrium is unstable. This was also on Arnold's 1976 list of problems [1]. See [10], [14], [17] for the case
  d ≤ 2. In 1995 Palamodov [15] outlined a very interesting proof. A detailed proof has never been published.
  If this conjecture were proved it would imply our instability theorems and also the instability of charged
  rigid bodies that we do not prove.»
- Burgos 2021 v4 (arXiv:2108.05829v4, введение) [Литература: полный текст]: «Palamodov announced the following
  instability Theorem: Theorem (Palamodov [Pa], Theorem 2.1). For any point x0 in M, there exists a neighborhood
  W of x0 and a positive function T defined on the interval (−∞, U(x0)) such that any motion with energy
  E < U(x0) starting at W cannot spend a time lapse greater than T(E) inside W. However, although the proof is
  illuminating and has very inspiring ideas, unfortunately it is not a complete argument. It is believed that the
  argument can be completed [Pa2] but technically speaking, it does not constitute a proof leaving the
  announced Theorem so far as a conjecture.» Здесь [Pa] = P95, [Pa2] = «Communication with V. P. Palamodov»
  (т. е. «считается, что аргумент можно довести до конца» — личное сообщение, а не публикация).
  Условия: M — вещественно-аналитическое многообразие, Q — положительно определённая гладкая квадратичная форма
  (риманова метрика), U вещественно-аналитична на M; теорема для любой точки x0 ∈ M (не обязательно критической).
  Следствие (Corollary 2.2 в [Pa]): «If a critical point x0 of the potential U belongs to the closure of the set
  {x ∈ M | U(x) < U(x0)}, then the equilibrium position x0 is unstable.»
- Burgos–Paternain 2022 (arXiv:2208.01139, введение): «In [Pa], V. P. Palamodov stated a total instability
  result for non minimum critical points of the potential whose proof is incomplete. This total instability
  conjecture would imply the Arnold's problem and the impossibility of Ureña's example in the class of real
  analytic potentials as well. All of these remain as open problems.» И далее: «our algorithm for the
  construction of a weakly logarithm field is inspired in the idea of V. P. Palamodov in [Pa]. Essentially, his
  idea consists in adding corrections to a given vector field along each step of a principalization of the
  potential and then coming back to the zeroth step with the corrected vector field satisfying the desired
  logarithmic properties.» [Литература: arXiv:2208.01139, введение]
- Палмодов 2020: в списке литературы (42 названия, см. §3) работа 1995 года **не значится**; об этом пишет и
  Burgos 2021 v4: «that paper does not mention the previous paper [Pa] where the Theorem was announced».
  Мои сведения о составе списка — из метаданных на journals.rcsi.science. [Литература: список литературы,
  rcsi.science; сам текст [P20] не читался]
- Козлов: явных высказываний о полноте P95 не найдено (текст не открывался).

Вердикт: KNOWN_RESULTS не содержит собственного утверждения о P95 (только «по [B21]; не сверено»).
Подтверждено вторичными источниками: P95 — заявленный (announced/outlined) результат без полного опубликованного
доказательства; формулировка теоремы — T(E)-форма. **«Не сверено» остаётся: полный текст не открывался.**
Пробел в P95 в публикациях не локализован ни у Burgos, ни у Allaire–Rauch.

## 3. Паламодов 2020 (УМН 75:3, 107–122; RMS 75:3, 495–508)

Библиография [Литература: Crossref/IOP/rcsi.science, метаданные]: В. П. Паламодов, «Об обращении теоремы
Лагранжа–Дирихле и неустойчивости консервативных систем», УМН 75:3(453) (2020), 107–122; англ.: «On inversion of
the Lagrange–Dirichlet theorem and instability of conservative systems», Russian Math. Surveys 75:3 (2020),
495–508, doi:10.1070/RM9945 (рус. DOI 10.4213/rm9945). Автор: Tel Aviv University. Аннотация (дословно):
«Problems related to instability of equilibria of natural systems in mechanics and inversions of the
Lagrange–Dirichlet theorem are discussed. Bibliography: 42 titles.» Ключевые слова: «Lagrange–Dirichlet theorem,
equilibrium, Liapounoff instability, total instability, classification of unstable critical points,
quasi-homogeneous potential functions».

**Определение 1, Гипотеза 1, Теоремы 2, 3, 5, 6, Пример 3 дословно — не удалось получить** (Math-Net недоступен,
rcsi-копия закрыта). Что известно из вторичных источников:
- Burgos 2021 v4: «the hipothesis of the previous Palamodov's Theorem/Conjecture is condensed in the notion of
  total instability ([Pa4], Section 3, Definition 1)». То есть Определение 1 находится в Разделе 3 и
  «сгущает» формулировку T(E) из P95. [Литература: arXiv:2108.05829v4, введение]
- Burgos 2025 (arXiv:2506.19135, введение): «In [Pa2], Palamodov proved that in the purely mechanical case, that
  is without magnetic potential, if the first non-zero jet of the potential at p has no critical point other
  than the origin, then the point p is totally unstable. The main step of the proof consists in deforming a
  radial vector field in configuration space such that the resulting vector field V verifies V(U) = U.»; а также:
  «Palamodov proved total instability for real analytic potential whose first non-zero jet has no critical
  points other than the origin [Pa2]». [Литература: arXiv:2506.19135, §1.1, §1.2; здесь [Pa2] = P20.]
  Это согласуется с Теоремой 3 в KNOWN (∇u_m ≠ 0 при x ≠ 0 ⇒ тотальная неустойчивость); различие: Burgos
  говорит «real analytic», KNOWN — «U = u_m + u_{m+1} + …» без указания аналитичности (нужно уточнить по
  тексту P20).
- Burgos 2025 и Burgos–Paternain: Гипотеза Паламодова о тотальной неустойчивости остаётся открытой.
- Козлов–Трещёв 2018: библиография [Литература: Crossref/rcsi]: V. V. Kozlov, D. V. Treschev, «Instability,
  asymptotic trajectories and dimension of the phase space», Mosc. Math. J. 18:4 (2018), 681–692. Аннотация
  (по поисковику, текст не открывался): для неустойчивого равновесия в R^n вопрос, существует ли ненулевое
  решение, стремящееся к равновесию при t → −∞; ответ зависит от чётности n и гладкости; при n ≤ 2 — всегда
  да (Пуанкаре–Бендиксон при n = 2). Слайды авторов (не сама статья): для нечётных n ≥ 3 существуют
  бездивергентные полиномиальные системы с изолированным неустойчивым равновесием без уходящих
  асимптотических траекторий (есть входящие); для чётных n ≥ 4 — ни тех, ни других. [не сверено с первоисточником]
  Утверждение KNOWN «для аналитических систем общего вида (не натуральных) асимптотического движения может не
  быть (Козлов–Трещёв, 2018)» **совместимо** с этим (контрпримеры — бездивергентные полиномиальные, т. е.
  аналитические, системы, не натуральные), но в P20 не сверено, как именно Паламодов его использует.
  Для натуральных систем гипотеза о существовании асимптотических движений (Козлов 1982) открыта; к статье
  КТ2018 это не относится — не сверено.
- Работа P20 цитирует Burgos–Maderna–Paternain 2019 («A note on Lyapunov instability in Newtonian dynamics»,
  2019, 8 pp.) — в её списке. Позднейшая публикация: Nonlinearity 34 (2021) 6719–6726. [rcsi.science; метаданные]

Вердикт по §5 «Паламодов (2020)»: **не удалось проверить** по тексту. Согласуется со вторичными источниками:
наличие понятия «total instability» (раздел 3, Опр. 1), результата о «no critical point other than the origin»,
открытость общей гипотезы. Не проверено: нумерация Теорем 2, 3, 5, 6, содержание Теорем 2 и 6, Пример 3,
содержание заявления о статусе P95, утверждение «[P20] называет это тотальной неустойчивостью при n = 2».
Отдельная неточность в KNOWN: «Этим кругом результатов пользуются Allaire и Rauch» — работа Allaire–Rauch
вышла в 2017 (ARMA 224), до P20 (2020), и опирается лишь на наброски P95 и P77 (см. §2): формулировка неверна.
Burgos 2025 пишет, что результат Паламодова «had implications for the work on the Earnshaw's Theorem by Allaire
and Rauch», что в хронологическом отношении тоже следует читать как «Allaire–Rauch заявляют: из гипотезы
следовали бы их теоремы» (AR §1.7), а не «AR используют P20».

## 4. Burgos, arXiv:2108.05829

[Литература: arXiv abs-страница 2108.05829, история отправки; полный текст v4]
- Название v4: «A proof of the Palamodov's total instability conjecture» (v3: «A proof of the Arnold-Palamodov's
  instability conjecture»; формулировки в аннотации v3 иные: «Palamodov's instability conjecture… Arnold… reduces
  the Lyapunov's conjecture…»).
- История версий (дословно из abs-страницы): v1 Thu, 12 Aug 2021 16:19:20 UTC; v2 Tue, 17 Aug 2021 13:00:48 UTC;
  v3 Fri, 3 Sep 2021 16:46:29 UTC; v4 Sat, 11 Sep 2021 05:52:18 UTC (9 KB); v5 Sat, 16 Jul 2022 01:06:43 UTC
  (1 KB), withdrawn. Примечание на abs-странице: «This paper has been withdrawn by Juan Manuel Burgos Mieres».
  Поле Comments: «There is a mistake in the proof. The second term of the last equation in Lemma 2.2 does not
  have the desired asymptotic behavior. I am grateful with V. P. Palamodov for pointing out this mistake».
- Подтверждено: даты v1 (12.08.2021), v4 (11.09.2021), v5 (16.07.2022) и причина отзыва совпадают с KNOWN.
  Добавить: v2 — 17.08.2021, v3 — 03.09.2021.
- Лемма 2.2 по v4 (дословно): «Lemma 2.2. There is a neighborhood W of x0 in M, a smooth vector field V and a
  smooth real valued function P both defined on W − V(U) such that P ≥ 1, V(U) = P U and ⟨v, ∇_v V⟩ = (1 + o(1))‖v‖²
  for every vector v in T_x M with x in W − V(U) as the point x approaches to x0.» (Лемма — «analog of Lemma 4.1 in
  [Pa]».)
- Схема доказательства v4: Лемма 2.1 (приписана Spivakovsky): мономиализация Хиронаки σ пучка идеалов m_{x0}·I_U,
  прообраз I_U локально мономиален, E = σ^{-1}(V(U)), прообраз {x0} — объединение неприводимых компонент E.
  В Лемме 2.2: в карте Ũ = ± w_1^{d1}…w_n^{dn}, Ṽ_p = Σ w_i ∂_{w_i}, Ṽ_p(Ũ) = c_p Ũ; V = Σ f_p V_p
  (разбиение единицы по карточкам на H); ⟨v,∇_v V⟩ = Σ (f_p⟨v,∇_v V_p⟩ + v(f_p)⟨v,V_p⟩) = (1+o(1))‖v‖² —
  последнее равенство (второе слагаемое v(f_p)⟨v,V_p⟩) и есть то место, на которое указано в комментарии отзыва.
  Основной аргумент: F(t) = ⟨γ̇, V(γ)⟩ ограничена сверху по Коши–Буняковскому, но Ḟ ≥ −V(U) = −P U ≥ −E > 0,
  значит F не ограничена — противоречие. Т. е. Лемма 2.2 — единственный технический шаг; без неё доказательства нет.
  Идентификация «второго слагаемого» как v(f_p)⟨v,V_p⟩ — моя интерпретация; в комментарии автора это слово
  «second term» не расшифровано.
- Вердикт по §5 «Burgos (2021), отозвано»: **подтверждено** (даты, отзыв, лемма 2.2, указание Паламодова).
  Уточнить: в KNOWN говорится «монализация Хиронаки идеала m_{x0}(U)» — по тексту v4 идеал есть произведение
  m_{x0}·I_U (идеал U, помноженный на максимальный идеал точки x0), а не «m_{x0}(U)». Также «поля Эйлера Σ w_i∂_{w_i}
  в картах» — верно. Описание ошибки в KNOWN как «не та асимптотика» совпадает с комментарием автора.
  Содержательные разборы ошибки (седло U = x(y−3x) и т. д.) — отдельная проверка, здесь не оценивались.
- В v4 нет подтверждения тезиса «для (A) изолированность не нужна» и т. п.: вопрос не входил в сверку.

## 5. Burgos, arXiv:2506.19135 и журнальная версия

[Литература: arXiv:2506.19135v1, дословно]
- История: единственная версия v1, 23 Jun 2025 21:09:42 UTC; Comments: «52 pages, 5 figures»; Journal reference на
  arXiv: «Journal of Differential Equations, Volume 454, 2026».
- Журнальная версия (Crossref, OpenAlex; страница ScienceDirect недоступна): J. M. Burgos, «McGehee blowup for
  Lagrangian systems and instability of equilibria», J. Differential Equations 454 (2026), article 114005,
  doi:10.1016/j.jde.2025.114005 (онлайн 04.12.2025, выпуск — февраль 2026 по Crossref). Тексты arXiv v1 и
  журнала не сравнивались: **формулировки ниже — по arXiv v1, не сверено с журнальной версией**.
- Аннотация: «We prove that total instability is a generic phenomenon in the real analytic class of
  electromagnetic Lagrangian systems under a weak magnetism hypothesis. The main object in the proof is an
  adaptation of the McGehee blowup for these systems. Together with this result, new criteria for total
  instability are introduced for both generic and non-generic cases.»
- Лагранжиан: L(x,v) = g_x(v,v)/2 + µ_x(v) − U(x), g — вещественно-аналитическая риманова метрика, U и 1-форма µ
  вещественно-аналитичны. Условие слабого магнетизма: «d − l/2 ≥ 1, where l and d are the degree values of the
  first non-zero jet of the potential and magnetic potential respectively.» Энергия H = g(v,v)/2 + U, без
  ограничения U(p) = 0, точка z подкритична, если H(z) < 0.
- Определение (дословно): «A point p is totally unstable if there is a neighbourhood B ⊂ A of the point such that
  for any subcritical point z in TB, the positive orbit I+(z) is not contained in TB. That is, the orbit of any
  subcritical point in TB eventually escapes from this set in the future.»
  **Важно:** это определение отличается от формулировки KNOWN §5 (и от T(E)-формулировки Паламодова в
  Burgos 2021). У Burgos 2025 — «положительная орбита не лежит целиком в TB» (окрестность B в конфигурационном
  пространстве, орбита в фазовом пространстве; нет равномерной оценки времени T(E)). Это, вообще говоря, слабее
  оценки T(E) для времени пребывания (по определению T(E)-версии из неё следует выход, обратное неочевидно).
  Для вывода (A) обе версии достаточны.
- Теорема 1.1: «For any natural k ≥ 2, there is an open and dense subset A of the ideal I_k such that, for every
  potential germ in A and magnetic potential verifying the weak magnetism hypothesis, the point p is totally
  unstable.» (I_k = m^k в кольце ростков вещественно-аналитических функций).
- Prop. 1.2 (Total instability criterion) дословно: «Suppose that f is a Morse function and zero is a regular
  value. Then, the point p is totally unstable.» (f — ограничение на единичную сферу первого ненулевого струйного
  члена U; в тексте перед этим: «Denote by f the restriction to the unit sphere of the first non-zero jet of the
  potential U».)
- Пояснение автора: «Note that the definition of total instability does not require the point p to be critical…
  a strict minimum of the potential is totally unstable since the statement is vacuously true…».
- Дословно о соотношении с Паламодовым: «In the purely mechanical case, the total instability criterion,
  Proposition 1.2, is weaker than Palamodov's Theorem since it requires the generic additional hypothesis that f
  is Morse. However, it is the first total instability criterion that covers magnetism…» и «As our knowledge goes,
  so far all of the instability criteria either in the total or Lyapunov sense, require the generic hypothesis
  that zero is a regular value of the function f. In view of this, a non-generic instability criterion is
  important since it bounds the field of possibilities in which to look for a counterexample, if any, to any of
  the instability conjectures regarding real analytic mechanical systems.»
- Prop. 1.3 (Non-generic total instability criterion): U не однородный многочлен; U = U_{l1} + U_{l2} + …,
  g_ij = δ_ij + g_ij^{(m)} + …; d − l1/2 > µ = min{l2 − l1, m}; критериальная функция на сфере
  C(q) = −δ^µ_{l2−l1} (l2 − l1) U_{l2}(q) + δ^µ_m m U_{l1}(q) Σ g^{(m)}_{ij}(q) q^i q^j. Утверждение: «If C(q) > 0
  on every critical point q of f such that f(q) ≤ 0, then the point p is totally unstable.»
  Cor. 1.4: «In Newtonian mechanics, the point p is totally unstable if the second non-zero homogeneous term in
  the Maclaurin series of the potential is negative on the critical locus of the the first non-zero homogeneous
  term restricted to the unit sphere where the latter term is less than or equal to zero.»
  Уточнение к KNOWN: условия — U не однородный многочлен, l1 < l2 — вторая ненулевая однородная часть; критерий
  охватывает только критические точки f с f ≤ 0 (включая f = 0), на всех них U_{l2} < 0.
- Prop. 1.5: орбита, сходящаяся к (p,0), асимптотична к компоненте критического множества f, где f ≤ 0.
- Prop. 11.1 (Mechanical tightness): «Suppose that f is a Morse function and zero is a regular value. Then, there
  is a neighbourhood B of p in configuration space such that, for any orbit O+(z) in phase space verifying
  O+(z) ⊂ TB, H(z) ≤ 0, its omega-limit set contains (p, 0). In particular, H(z) = 0.» Theorem 11.4: «Total
  instability is generic»; доказательства не читались.
- Дословная фраза об открытости случая Арнольда (§1.2): «In [Ar], Arnold proposed the problem of instability of an
  isolated non-minimum critical point of a real analytic potential in Newtonian mechanics. Even this simplified
  version of the Lagrange-Dirichlet converse remains open. The case of a non-strict minimum of the potential was
  treated in [BMP] for Newtonian mechanics and in [BMP] for Lagrangian systems.» (в тексте дважды [BMP]; второй, по
  смыслу, [BP] = Burgos–Paternain, Proc. AMS 150 (2022) 4335–4348). Там же: «In dimension greater than two, the
  problem remains open and only partial results are known.»
- Вердикт по KNOWN §5 «Burgos (2025/2026)»: **подтверждено** (дословная цитата, Prop. 1.2, Prop. 1.3 / Cor. 1.4,
  фраза про «все известные критерии»). Неточности: (i) определение тотальной неустойчивости в B25 слабее/иное,
  чем в §5 KNOWN (см. выше); (ii) том и год журнала: J. Differential Equations 454 (2026), 114005 — подтверждено
  через Crossref и через ссылку в arXiv:2610.27893 («J. Differential Equations 454 (2026) 114005»); (iii) главный
  результат — теорема 1.1 для электромагнитных систем с условием слабого магнетизма d − l/2 ≥ 1; (iv)
  «Доказательства этих критериев доской не проверялись» — остаётся в силе: доказательства Burgos 2025 в моей
  сверке не читались; рецензирование статьи в JDE само по себе не есть проверка нашего агента.

## 6. Новые работы (2023–2026)

Метод: OpenAlex (cited-by для P77, P20, Brunella 1998, Ureña 2020, Burgos 2025, и др.), arXiv API (поиск по
аннотациям, в т. ч. отдельно по датам 27.09.2026–21.10.2026), поисковики. OpenAlex плохо индексирует arXiv и
российские журналы; Google Scholar «cited by», Semantic Scholar и zbMATH «cited by» в этой среде недоступны
(zbMATH Open API возвращает только метаданные без «cited by»). Поэтому список ниже **не исчерпывающий**.

**Заявлено ли решение (A) или её частей (n = 3, многочлены): нет, ни в одной найденной работе.**

После 27.09.2026:
1. A. Enciso, D. Peralta-Salas, «Stability and instability for particle dynamics in magnetic fields», arXiv:2610.27893
   v1, 20 Oct 2026, math.DS. [Литература: arXiv, введение и формулировки прочитаны] Уравнение Ньютона–Лоренца
   ẍ = ẋ × B(x) в R^3 (без потенциала!). Thm 1: B ∈ C¹, B(0) ≠ 0 ⇒ (0,0) Ляпунов-неустойчиво. Thm 2: B
   вещественно-аналитично, B(0) = 0, 0 — изолированный нуль ⇒ (0,0) Ляпунов-неустойчиво (без условия div B = 0;
   использует теорему Брунеллы о существовании силовой линии, сходящейся к изолированному нулю аналитического поля
   в R^3). Thm 3: существует компактно-носительное бездивергентное C^∞-поле B, плоское в изолированном нуле,
   с Ляпунов-устойчивым равновесием. К (A) не относится напрямую. Фраза введения: «The Lagrange–Dirichlet theorem
   gives stability at strict local minima, but its converse is false for smooth potentials [Laloy 1976]. For
   real-analytic potentials on R², Palamodov proved that a critical point that is not a local minimum defines an
   unstable equilibrium [P77]. For real-analytic potentials on R³, the corresponding assertion remains open; see
   [Burgos–Paternain 2022] for partial results.» — независимое свидетельство (на 20.10.2026), что случай R³ открыт.
   Заметим: их ссылка [4] — Burgos–Paternain (arXiv:2208.01139), которая сама о нестрогих минимумах; то есть
   «partial results» — в смысле нестрогих минимумов и общего положения.
Других работ по теме с датой после 27.09.2026 не обнаружено (arXiv API по аннотациям: math.DS 27.09–21.10.2026 —
в списке только п. 1 по теме).

2023–2026 (до 27.09.2026):
2. J. M. Burgos, McGehee blowup…, J. Differential Equations 454 (2026) 114005; arXiv:2506.19135 (23.06.2025) — см. §5.
3. В. В. Козлов, «Неустойчивость равновесий в соленоидальном силовом поле», Матем. заметки 113:1 (2023) (рус., doi:10.4213/mzm13884); англ.:
   Math. Notes 113 (2023) 220–227, doi:10.1134/S000143462301025X. [по аннотации, через OpenAlex]. Аннотация: «We
   discuss the conjecture that an isolated equilibrium of a mechanical system in a solenoidal force field is
   unstable. A number of statements confirming this conjecture under additional general position conditions
   guaranteeing that the equilibrium is isolated are proved. More precisely, we prove that there exist phase
   trajectories asymptotically leaving the equilibrium state.» (Не потенциальное поле; эта статья цитирует
   Brunella 1998 — связана с асимптотическими траекториями; (A) не решает.)
4. В. В. Козлов, «Об устойчивости равновесий в псевдоримановом пространстве», УМН 80:1 (2025), 51–74; англ.: Russian
   Math. Surveys 80:1 (2025), 51–74, doi:10.4213/rm10228e. [по аннотации] В аннотации: для нелинейных аналитических
   систем с двумя степенями свободы максимум и минимум потенциала неустойчивы в псевдоевклидовом случае;
   многомерные результаты — линейные. К (A) не относится.
5. В. В. Козлов, «Тождество Лагранжа и динамика в потенциальном поле Якоби», Regular and Chaotic Dynamics 30:6 (2025)
   887–907, doi:10.1134/S1560354725060012. [по аннотации] Однородный потенциал степени −2; к (A) не относится.
   (Цитирует P20 по OpenAlex, но по теме — другой вопрос.)
6. J. M. Burgos, «Strong degenerate constraining in Lagrangian dynamics», Nonlinearity 36:10 (2023), 5358–5377,
   doi:10.1088/1361-6544/acf17d. [по аннотации] Сильное ограничение связей в вырожденном случае; цитирует BP21; (A)
   не относится.
7. F. E. Udwadia, R. M. Bulatovic, «On the Equations of Motion for Constrained Systems and Their Stability», J. Appl.
   Mech. 93:8 (2026), doi:10.1115/1.4071975 [по аннотации]: цитирует P77 (по OpenAlex) в контексте устойчивости
   систем со связями; (A) не относится.
Для контекста: Burgos–Paternain, «On the Lyapunov instability in Lagrangian dynamics», Proc. Amer. Math. Soc. 150
(2022) 4335–4348, doi:10.1090/proc/15972 (arXiv:2108.05074) — то есть опубликовано; Burgos–Maderna–Paternain,
Nonlinearity 34 (2021) 6719–6726, doi:10.1088/1361-6544/ac1a1a. Burgos–Paternain, «On the Lagrange–Dirichlet
converse in dimension three», arXiv:2208.01139 (1 Aug 2022): «Theorem 1.1. Consider a mechanical system on a three
dimensional real analytic manifold with a real analytic potential. Then, there is an open and dense subset of the
set of non strict local minimums of the potential such that every one of its points is a Lyapunov unstable
equilibrium point.» (Не случай (A): это нестрогие минимумы.) Журнальная публикация BP22 в найденных базах не
обнаружена (на arXiv v1 от 2022-08-01).
В arXiv:2208.01139 есть пример, подчёркнутый авторами: U = x⁴ + y⁴ − z⁶, начало — изолированная критическая
точка не минимум, но минимум первой струи; «none of the mentioned results apply for the potential U» (о результатах
до 2022 года). Для текущей картины это стоит проверить на более новых критериях (Burgos 2025: здесь первая
струя x⁴+y⁴ — на сфере f = x⁴+y⁴ ≥ 0 с критическими точками f > 0, нужно проверить Prop. 1.2, f не регулярна на 0?).
[Эта фраза — замечание, а не результат литературы; проверка — задача для numerics/prover.]

Не обнаружено: работ, цитирующих Burgos 2025 и содержащих новые результаты об устойчивости/неустойчивости
потенциального равновесия, кроме Enciso–Peralta-Salas (OpenAlex показывает 0 цитирований JDE-версии на момент
запроса, но индекс неполный).

## 7. Поправки к библиографии KNOWN_RESULTS (найдены попутно, Crossref)

- [NLM79] — автор установлен: M. Laloy, «On the inversion of the Lagrange–Dirichlet theorem in the case of an analytic
  potential», Int. J. Non-Linear Mech. 14:1 (1979), 59–65, doi:10.1016/0020-7462(79)90029-5.
- [AMM93] — это K. Peiffer, «On inversion of the Lagrange–Dirichlet theorem», J. Appl. Math. Mech. (ПММ) 55:4
  (1991), 436–441, doi:10.1016/0021-8928(91)90002-C. Ссылка на doi:10.1007/BF00962611 в KNOWN **неверна**: это
  M. Sofer, «On the inversion of the Lagrange–Dirichlet stability theorem — mechanical and generalized systems»,
  ZAMP 34:1 (1983), 1–12. Работа Moauro–Negrini — Differential Integral Equations 2:4 (1989), 471–478 (по списку
  литературы Burgos 2021 и Паламодова 2020).
- [Koz86] — V. V. Kozlov, «Asymptotic motions and the inversion of the Lagrange–Dirichlet theorem», J. Appl. Math.
  Mech. 50:6 (1986), 719–725, doi:10.1016/0021-8928(86)90079-1 (Burgos пишет 1987); русский оригинал: ПММ 50:6 (1986),
  928–937 (по списку P20).
- [BMP21] Nonlinearity 34:10 (2021) 6719–6726, doi:10.1088/1361-6544/ac1a1a — подтверждено.
- [BP21] опубликовано: Proc. Amer. Math. Soc. 150 (2022), 4335–4348, doi:10.1090/proc/15972.
- [P95] Дополнить: в сб. V. V. Kozlov (ed.), *Dynamical Systems in Classical Mechanics*, AMS Transl. (2) 168 (1995),
  pp. 5–20, doi:10.1090/trans2/168/02.
- [P77] Крит. замечание: английская версия 277–289 (по Crossref/zbMATH; на странице Паламодова — 277–288).
- [Koz81]: Козлов, «Неустойчивость равновесия в потенциальном поле», УМН 36:1 (1981), 215–216 (по Burgos: Russian
  Math. Surveys 36 (1981), 238–239 — англ.). Страницы по списку P20 (Козлов, «Неустойчивость равновесия в потенциальном
  поле с учётом сил вязкого трения», ПММ 45:3 (1981), 570–572) — другая работа. Выяснить, какая именно работа Козлова
  обобщает n = 2 на произвольную кинетическую энергию, по тексту не удалось.

## 8. Итог: вердикты по пунктам §5 KNOWN_RESULTS

| Утверждение §5 | Вердикт |
|---|---|
| Определение полной неустойчивости (T(E), «по [B21]») | подтверждено как формулировка Паламодова в Burgos 2021 (Thm Palamodov [P95] Theorem 2.1, дословно); но B25 использует другое, более слабое определение («орбита не лежит в TB»); нужно оговорить обе |
| Из полной неустойчивости следует (A) (рассуждение) | математически верно при любом из двух определений (при нестрогом минимуме не охватывается) — математика не литература; ссылка Burgos 2021: Corollary 2.2 из [P95] |
| Паламодов 1977: основная лемма и n = 2 | не удалось проверить (текст не открыт); n = 2 подтверждено по вторичным источникам; формулировка леммы, «или C^∞ с конечнократной критической точкой» не проверены; общая теорема о тотальной неустойчивости у Burgos приписана P95, а не P77 |
| Паламодов 1995 | сказано «не сверено»; подтверждено вторичными: «announced/outlined; detailed proof never published» (Allaire–Rauch §1.7, Burgos) |
| Паламодов 2020: Опр. 1, Гип. 1, Теор. 2, 3, 5, 6, Пример 3 | не удалось проверить; подтверждены (вторично) раздел 3, понятие, результат типа Теоремы 3 (jet without critical points other than origin); пометка «[Т] прочитан полностью» в KNOWN относится к прежнему участнику, мной не проверена |
| Козлов–Трещёв 2018 | неточно/не сверено: референс: Mosc. Math. J. 18:4 (2018), 681–692; тема подтверждена; точная ссылка в P20 не проверена |
| «Этим кругом результатов пользуются Allaire и Rauch» | **неточно**: AR 2017 раньше P20; AR лишь указывают, что из гипотезы Паламодова следовали бы их теоремы (§1.7) |
| Burgos 2021: v1…v5, отзыв, Лемма 2.2 | подтверждено; уточнить: v2, v3; идеал m_{x0}·I_U; точная цитата поля Comments |
| Burgos 2025: JDE, цитата, Prop. 1.2, Prop. 1.3 | подтверждено (по arXiv v1); JDE 454 (2026), art. 114005; журнальный текст не сверялся |

## 9. Предлагаемые правки KNOWN_RESULTS.md (сам файл не правился)

1. §5, «Полная неустойчивость»: добавить, что у Burgos 2025 (arXiv:2506.19135, §1.1) определение другое:
   «there is a neighbourhood B ⊂ A of the point such that for any subcritical point z in TB, the positive orbit
   I+(z) is not contained in TB», без равномерной оценки времени T(E); пометить [Литература: B25, дословно].
   T(E)-форму приписывать Palamodov 1995, Theorem 2.1 (по цитате в Burgos 2021 v4), а не только [B21].
2. §5, «Паламодов (1977)»: пометить как [не сверено с первоисточником] всё содержание (основная лемма, условия на
   поле v, класс C^∞ с конечнократной критической точкой): в этой сверке текст не открывался; Math-Net недоступен.
   Убрать «[Т]» или оговорить, что это пометка прежних участников. Добавить: в Burgos 2021 общая теорема о
   тотальной неустойчивости и Corollary 2.2 приписаны работе 1995 года [P95], а для n = 2 — работе 1977 года.
3. §5, «Паламодов (2020)»: пометить Определение 1, Гипотезу 1, Теоремы 2, 3, 5, 6, Пример 3 как не сверенные с
   первоисточником в этой ревизии. Уточнить, что по Burgos 2025 аналитичность в Теореме 3 указана («real analytic
   potential whose first non-zero jet has no critical points other than the origin»); по Burgos 2021 Определение 1
   находится в разделе 3 статьи.
4. §5, фраза «Этим кругом результатов пользуются Allaire и Rauch…»: заменить на «Allaire–Rauch (ARMA 224, 2017,
   §1.7) отмечают, что из гипотезы Паламодова (набросок: P95) следовали бы их теоремы об электростатике и
   неустойчивость заряженных твёрдых тел; полного доказательства не опубликовано» [Литература: AR, HAL-препринт].
5. §5, Козлов–Трещёв 2018: добавить точную ссылку Mosc. Math. J. 18:4 (2018), 681–692 и пометить [не сверено с
   первоисточником] (аннотация и слайды авторов), что утверждается только про общие (не натуральные) аналитические
   системы в размерности n ≥ 3: контрпримеры — бездивергентные полиномиальные системы (по слайдам авторов).
6. §5, Burgos 2021: «идеал m_{x0}(U)» → «идеал m_{x0}·I_U (максимальный идеал точки, умноженный на идеал,
   порождённый U)» (по v4 Lemma 2.1); добавить даты v2 (17.08.2021) и v3 (03.09.2021) и дословный Comment:
   «There is a mistake in the proof. The second term of the last equation in Lemma 2.2 does not have the desired
   asymptotic behavior. I am grateful with V. P. Palamodov for pointing out this mistake». Отметить, что идентификация
   «второго слагаемого» с v(f_p)⟨v,V_p⟩ — интерпретация доски, а не слова автора.
7. §5, Burgos 2025: ссылка J. Differential Equations 454 (2026), 114005, doi:10.1016/j.jde.2025.114005; указать
   главный результат — Thm 1.1 (общность тотальной неустойчивости для электромагнитных систем при d − l/2 ≥ 1);
   для Cor. 1.4 добавить условия: U не однородный многочлен, первая и вторая ненулевые однородные части U_{l1}, U_{l2},
   критерий требует U_{l2} < 0 во всех критических точках f с f ≤ 0 (метрика евклидова; в общем виде — функция
   C(q) из Prop. 1.3). Пометить, что журнальная версия с arXiv v1 не сверялась.
8. §6/«Что известно»: добавить новую работу Enciso–Peralta-Salas, arXiv:2610.27893 (20.10.2026) — магнитные поля;
   не решает (A); независимое подтверждение, что для аналитических потенциалов в R³ утверждение «remains open»
   (по состоянию на 20.10.2026).
9. Библиография: исправить [NLM79] (Laloy 1979), [AMM93] (Peiffer, ПММ 55:4, 1991; doi:10.1007/BF00962611 — это
   Sofer 1983, а не Moauro–Negrini), [Koz86] (JAMM 50:6, pp. 719–725), [P95] (сборник, doi:10.1090/trans2/168/02),
   [BP21] (Proc. AMS 150 (2022) 4335–4348), [BMP21] (doi:10.1088/1361-6544/ac1a1a), [B25] (art. 114005,
   doi:10.1016/j.jde.2025.114005).
10. Открытая задача для следующей сверки: получить PDF Паламодова 1977 и 2020 (русский, Math-Net, свободный
    доступ) — либо когда Math-Net снова доступен с сервера, либо через владельца; затем дословно выписать Опр. 1,
    Гипотезу 1, Теоремы 2, 3, 5, 6 и Пример 3, а также что Паламодов пишет о пробеле в P95.
