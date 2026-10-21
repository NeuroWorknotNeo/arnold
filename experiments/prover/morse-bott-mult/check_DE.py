# [Эксперимент] Пример W3 записки notes/prover/2026-10-21-morse-bott-mult.md, §10:
# профиль P(tau,e) = e^4 + sin(tau) e^2 + sin(tau)^2 (k = 1). Проверяется на сетке
#   (а) P >= 0.26 (tau^2 + e^4) при |tau| <= 0.2, |e| <= 1;
#   (б) условие (DE) с w = 1/2, mu_0 = 1:  tau P_tau + (1/2) e P_e - P >= 0 там же;
#   (в) «наивный» вес нормали: kappa tau P_tau + c e P_e - kappa*mu P при c = 3/2 — минимум отношения к P
#       (отрицателен при малых kappa, т.е. поле Mb без свободного нормального веса не годится).
import mpmath as mp
mp.mp.dps = 30
P = lambda t, e: e**4 + mp.sin(t)*e**2 + mp.sin(t)**2
Pt = lambda t, e: mp.cos(t)*e**2 + 2*mp.sin(t)*mp.cos(t)
Pe = lambda t, e: 4*e**3 + 2*mp.sin(t)*e
n = 201
pts = [(mp.mpf('0.2')*(2*i/(n - 1) - 1), mp.mpf(2*j/(n - 1) - 1)) for i in range(n) for j in range(n)]
pts = [(t, e) for (t, e) in pts if not (t == 0 and e == 0)]
ra = min(P(t, e)/(t**2 + e**4) for t, e in pts)
rb = min((t*Pt(t, e) + e*Pe(t, e)/2)/P(t, e) for t, e in pts)
print('(а) min P/(tau^2+e^4) на |tau|<=0.2, |e|<=1:', mp.nstr(ra, 8))
print('(б) min (tau P_tau + e P_e/2)/P там же:', mp.nstr(rb, 8), ' (нужно >= mu_0 = 1)')
for kap in (0.05, 0.1, 0.2, 0.3):
    rc = min((kap*t*Pt(t, e) + mp.mpf(3)/2*e*Pe(t, e))/P(t, e) for t, e in pts)
    print('(в) kappa = %-5s min (kappa tau P_tau + c e P_e)/P = %s' % (kap, mp.nstr(rc, 6)))
