"""Пример заявки: сколько времени траектории системы x'' = -grad U(x) проводят в шаре |x| < R.

U(x, y) = x^3 - 3 x y^2: 0 — изолированная критическая точка, не минимум (однородный потенциал,
неустойчивость здесь известна классически). Интегрирование — схема Штёрмера–Верле с шагом dt.
Результат — вычислительное свидетельство, а не доказательство.
"""

import argparse
import json
from pathlib import Path

import numpy as np


def grad_u(q):
    x, y = q[:, 0], q[:, 1]
    return np.stack([3 * x**2 - 3 * y**2, -6 * x * y], axis=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--samples", type=int, default=1000)
    ap.add_argument("--delta", type=float, default=1e-3, help="радиус начальных данных в фазовом пространстве")
    ap.add_argument("--radius", type=float, default=0.1, help="R: радиус шара, выход из которого фиксируем")
    ap.add_argument("--dt", type=float, default=1e-2)
    ap.add_argument("--tmax", type=float, default=2000.0)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--out", default="out")
    args = ap.parse_args()

    rng = np.random.default_rng(args.seed)
    z = rng.normal(size=(args.samples, 4))
    z *= args.delta / np.linalg.norm(z, axis=1, keepdims=True)
    q, p = z[:, :2].copy(), z[:, 2:].copy()
    exit_time = np.full(args.samples, np.inf)
    alive = np.ones(args.samples, dtype=bool)
    t = 0.0
    p -= 0.5 * args.dt * grad_u(q)
    while t < args.tmax and alive.any():
        q[alive] += args.dt * p[alive]
        p[alive] -= args.dt * grad_u(q[alive])
        t += args.dt
        left = alive & (np.linalg.norm(q, axis=1) > args.radius)
        exit_time[left] = t
        alive &= ~left

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    finite = exit_time[np.isfinite(exit_time)]
    summary = {
        "potential": "x^3 - 3xy^2",
        "samples": args.samples, "delta": args.delta, "radius": args.radius, "dt": args.dt, "tmax": args.tmax,
        "seed": args.seed, "escaped_fraction": float(np.isfinite(exit_time).mean()),
        "exit_time_quantiles": {q_: float(np.quantile(finite, q_)) for q_ in (0.1, 0.5, 0.9)} if finite.size else None,
        "note": "Численный эксперимент: не является доказательством неустойчивости.",
    }
    (out / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False))
    np.save(out / "exit_time.npy", exit_time)
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
