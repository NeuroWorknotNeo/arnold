# [Эксперимент] Стрельба по схеме теоремы A [GT3] для U_(8) = (Q0+z^3)^2 + x z^6 + x y z^5 + z^7/2 (s=1, j=7):
# из точек дна Psi(x0, theta=0, zeta=0) с энергией 0 и скоростью -lambda*Y интегрируем НАЗАД
# по времени до сечения s = sigma2; точки входа должны сходиться при x0 -> 0.
# Затем прямой прогон из предельной точки: s(t) против закона s^{-5/2} = s_in^{-5/2} + (5/2) sqrt(2 a0) t.
import numpy as np
from scipy.integrate import solve_ivp

a0 = -np.sqrt(2)*(2 - 3*np.sqrt(3))/64   # -G(omega*), G = sqrt2 (1 + 2cos phi + sin 2phi)/32, phi* = 5pi/6
PHI0 = 5*np.pi/6

def U(q):
    x, y, z = q
    P = x*x + y*y - z*z + z**3
    return P*P + x*z**6 + x*y*z**5 + z**7/2

def gradU(q):
    x, y, z = q
    P = x*x + y*y - z*z + z**3
    return np.array([4*x*P + z**6 + y*z**5, 4*y*P + x*z**5,
                     2*P*(-2*z + 3*z*z) + 6*x*z**5 + 5*x*y*z**4 + 3.5*z**6])

def s_of(q):
    R = np.hypot(q[0], q[1])
    return (R + q[2])/np.sqrt(2)

def floor_point(x0):
    # y*(s) на phi = pi из ряда (examples.py): eta* = s*y*, y* = sqrt2 s/8 + ... (верхняя полость, phi=pi:
    # для точности решаем d/deta U(P(s,pi,eta)) = 0 численно)
    phi = PHI0
    w = np.array([np.cos(phi), np.sin(phi), 1])/np.sqrt(2)
    n = np.array([-np.cos(phi), -np.sin(phi), 1])/np.sqrt(2)
    eta = 0.0
    for _ in range(60):   # Ньютон по eta
        h = 1e-7*x0**2
        f = lambda e: np.dot(gradU(x0*w + e*n), n)
        d = (f(eta + h) - f(eta - h))/(2*h)
        eta -= f(eta)/d
    return x0*w + eta*n, w, n

def rhs_back(t, Z):
    q, v = Z[:3], Z[3:]
    return np.concatenate([-v, gradU(q)])

def rhs(t, Z):
    q, v = Z[:3], Z[3:]
    return np.concatenate([v, -gradU(q)])

sigma2 = 0.12
entries = []
for x0 in [0.04, 0.02, 0.01, 0.006, 0.004]:
    q0, w, n = floor_point(x0)
    lam = np.sqrt(-2*U(q0))
    v0 = -lam*w            # Y ~ omega на дне (тета = 0), поправки O(x)
    ev = lambda t, Z: s_of(Z[:3]) - sigma2
    ev.terminal = True; ev.direction = 1
    sol = solve_ivp(rhs_back, [0, 1e9], np.concatenate([q0, v0]), method='DOP853',
                    rtol=1e-12, atol=1e-16, events=ev, max_step=np.inf)
    Ze = sol.y_events[0][0]
    entries.append(Ze)
    print('x0=%-6g  время назад до s=%.2f: %.4g, точка входа q=%s, E=%.2e' % (
        x0, sigma2, sol.t_events[0][0], np.array2string(Ze[:3], precision=10),
        0.5*np.dot(Ze[3:], Ze[3:]) + U(Ze[:3])))
for k in range(len(entries) - 1):
    print('  |q_k - q_last| =', np.linalg.norm(entries[k][:3] - entries[-1][:3]))

# прямой прогон из последней точки входа (скорость обращаем: назад -> вперёд)
Z0 = entries[-1].copy()
Z0[3:] = -Z0[3:]            # в обратном времени скорость была v_back = -v_forward? (rhs_back: q' = -v)
# в rhs_back переменная v — это скорость прямой задачи, поэтому её не трогаем:
Z0 = entries[-1].copy()
sol = solve_ivp(rhs, [0, 4e6], Z0, method='DOP853', rtol=1e-12, atol=1e-16, dense_output=True)
s_in = s_of(Z0[:3])
for t in [0, 1e3, 1e4, 5e4, 1e5, 3e5, 1e6, 3e6]:
    Z = sol.sol(t)
    pred = (s_in**-2.5 + 2.5*np.sqrt(2*a0)*t)**-0.4
    print('t=%-8g s(t)=%.6g  закон=%.6g  |q|=%.4g  phi-phi*=%.3e  y/|q|=%.4f' % (t, s_of(Z[:3]), pred,
          np.linalg.norm(Z[:3]), (np.arctan2(Z[1], Z[0]) % (2*np.pi)) - PHI0, Z[1]/np.linalg.norm(Z[:3])))
