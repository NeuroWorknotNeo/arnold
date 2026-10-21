"""[Эксперимент] Нужны ли концевые куски: для каждого примера и r -- есть ли на дуге точки, где
tau = Delta_0 != 0 и наклон tau' лежит в [lamH, lamB] (точки касания (11) из [P77]).
Если на некотором интервале у конца дуги tau != 0 и tau' < lamH (или > lamB) без внутренних
точек касания, то Delta из [P77] (max/min по tau и внутренним касательным кускам) совпадает там с tau
и нарушает III: mu ~ 1 + tau'_alpha < 0.
Печатаем: минимальный наклон tau на участке у конца дуги, где tau != 0, и число точек касания на этом участке.
Запуск: ~/venv/bin/python -I p77_no_endpoints.py > p77_no_endpoints_out.txt
"""
import numpy as np
import importlib.util
spec = importlib.util.spec_from_file_location("c", "construct.py")
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)

for name, exf, al0 in c.CASES:
    U, phi = c.make(exf)
    for r in [1e-2, 1e-3]:
        d = c.build(U, phi, r, al0(r))
        if d["periodic"]:
            print(f"{name:55s} r={r:.0e}: periodic, no arc ends"); continue
        al = d["al"]; t = d["tp"] + d["tm"]
        sl = np.diff(t) / np.diff(al)
        lamH, lamB = d["lamH"], d["lamB"]
        out = []
        for end in ("a", "b"):
            if end == "a":
                nz = t != 0
                if not nz[0]:
                    out.append("a: tau(a)=0"); continue
                j = np.argmax(~nz) if (~nz).any() else len(t)   # первый нуль
                seg = sl[:max(j - 1, 1)]
            else:
                nz = t != 0
                if not nz[-1]:
                    out.append("b: tau(b)=0"); continue
                j = len(t) - np.argmax(~nz[::-1]) if (~nz).any() else 0
                seg = sl[j:]
            ok = np.sum((seg >= lamH) & (seg <= lamB))
            out.append(f"{end}: tau={t[0] if end=='a' else t[-1]:+.2e}, segment {seg.size} cells, "
                       f"slope range [{seg.min():.3g}, {seg.max():.3g}], cells with slope in [lamH,lamB]: {ok}")
        print(f"{name:55s} r={r:.0e}, lamH={lamH:.3g}: " + " | ".join(out))
