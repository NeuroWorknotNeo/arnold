# Пример 13: символьная и численная проверка

vlad-claude-tg, 03.10.2026. Сопровождает [`notes/vlad-claude-tg/example13-proof.md`](../../../notes/vlad-claude-tg/example13-proof.md).
Статус всего ниже — **[Эксперимент]**: это свидетельство, а не доказательство.

## Вопрос

Для $U=(x^2+y^2-z^2)^2+z^5x+z^4xy+\tfrac12z^6$:

- верны ли формулы координатного представления и тождества из доказательства;
- изолирована ли критическая точка $0$;
- выполняются ли условия вириальной леммы для поля
  $V=\tfrac16(s\partial_s+2d\partial_d)-\kappa s^{-2}(\partial_dU)\partial_d-\kappa's^{-6}(\partial_\varphi U)\partial_\varphi$
  при $\kappa=0.01$, $\kappa'=0.02$, $\alpha=0.5$;
- уходят ли траектории с отрицательной энергией.

## Файлы и метод

| Файл | Что делает |
|---|---|
| `symbolic_check.py` | SymPy: $Q^2=4s^2d^2$; однородность $U-4s^2d^2$; $a_0=G/8$, $a_1$; тождество $\tfrac16E(U)-U=\tfrac16\sum ja_js^{6-j}d^j$; $\widetilde U(0,\varphi,\eta)$; результант числителей $G$ и $G'$ при $t=\tan(\varphi/2)$; нули $G$ |
| `isolated_check.py` | Корни системы для критических точек в переменных $a=x/z$, $b=y/z$; минимум $\lvert\nabla U\rvert/r^5$ на сферах (400 000 случайных точек, seed 0) |
| `numeric_check.py` | Случайные точки $\{U<0\}$ на сферах $r=0.5\ldots0.005$ (seed 1, по 20 000 точек); отношение $\langle\nabla U,V\rangle/U$; $\lambda_{\min}(\operatorname{Sym}DV)$ по центральным разностям с шагом $10^{-7}r$ |
| `trajectories.py` | РК4, шаг $0.02/\lvert q\rvert$; по 200 траекторий из $\lvert q_0\rvert=0.05,\ 0.02,\ 0.01$; энергия $h\in(U(q_0),0.1U(q_0))$; выход за сферу $\lvert q\rvert=0.3$; seed 7 |
| `trajectories_fine.py` | То же с шагом $0.004/\lvert q\rvert$, по 100 траекторий из $\lvert q_0\rvert=0.02,\ 0.01$ |

## Как воспроизвести

```bash
pip install numpy sympy
python symbolic_check.py
python isolated_check.py
python numeric_check.py
python trajectories.py        # ~10 минут
python trajectories_fine.py   # ~15 минут
```

## Результаты

- `symbolic_check.py`: все тождества верны; результант $=-23552\ne0$; нули $G$ в точках
  $\varphi\approx1.8278$ и $3.5999$ простые ($G'\approx-1.838$ и $1.051$); $\min G\approx-0.799$ при
  $\varphi=5\pi/6$.
- `isolated_check.py`: единственный вещественный корень $(a,b)\approx(1.154,-1.758)$,
  $a^2+b^2\approx4.42\ne1$; отношение $\min\lvert\nabla U\rvert/r^5$ на сферах $r=0.1\ldots0.003$
  ограничено снизу (от $0.19$ до $2.0$).
- `numeric_check.py`: $\min\langle\nabla U,V\rangle/U\ge1.000$ (нужно $\ge0.5$),
  $\min\lambda_{\min}(\operatorname{Sym}DV)$ от $0.151$ до $0.160$ (нужно $\ge-0.25$),
  $\max\lvert d\rvert/s^2\approx0.16$ при всех радиусах.
- `trajectories.py`: все 600 траекторий ушли; $\dot F\ge2.0\,\alpha\lvert h\rvert$. При $\lvert q_0\rvert=0.01$
  дрейф энергии велик относительно $\lvert h\rvert\sim10^{-12}$, поэтому эти данные ненадёжны.
- `trajectories_fine.py`: все 200 траекторий ушли; дрейф энергии $\le3\%$ от $\lvert h\rvert$.

## Что это не доказывает

Численная проверка условий на конечной выборке точек не заменяет леммы 5 и 6. Моделирование
траекторий на конечном времени ничего не говорит о строгой неустойчивости.
