"""
check_global.py -- контроль глобальности дна: на r = 0.1, 0.03, 0.01 сравнить найденный m(r) с минимумом грубой сетки 1500x3000 по сфере (double).
Если сетка даёт значение МЕНЬШЕ найденного (с запасом 1e-9 относительного) -- печатаем CHECK!!.  Для r < 0.01 сетка бесполезна (тонкие рога).  [Эксперимент]
usage: python check_global.py ID ... -> check_global.txt (дописывает)
"""
import sys, os, json
from flib import *


def main(ids):
    lines = []
    for eid in ids:
        e = cat()[eid]
        P = Pot(e['U'])
        d = json.load(open(os.path.join(HERE, 'out', eid + '.json')))['radii']
        for rr in (0.1, 0.03, 0.01):
            lr = math.log10(rr)
            rec = min(d, key=lambda t: abs(t['logr'] - lr))
            if abs(rec['logr'] - lr) > 0.13:
                continue
            r = 10 ** rec['logr']
            m_found = float(rec['minima'][0]['m'])
            th = np.linspace(0, np.pi, 1500)
            ph = np.linspace(0, 2 * np.pi, 3000, endpoint=False)
            TH, PH = np.meshgrid(th, ph, indexing='ij')
            V = P.un(r * np.sin(TH) * np.cos(PH), r * np.sin(TH) * np.sin(PH), r * np.cos(TH)) + 0 * TH
            mg = float(V.min())
            flag = 'CHECK!!' if mg < m_found * (1 - 1e-9) and mg < 0 else 'ok'
            lines.append(f"{eid} r=10^{rec['logr']:g}: m_found={m_found:.6e}  grid_min={mg:.6e}  ratio grid/found={mg / m_found:.6f} {flag}")
            print(lines[-1], flush=True)
    open(os.path.join(HERE, 'check_global.txt'), 'a').write('\n'.join(lines) + '\n')


if __name__ == '__main__':
    main(sys.argv[1:])
