# R40: Euler ratios for the W3 profile P = e^4 + sin(t) e^2 + sin(t)^2  [Experiment]
import numpy as np
t = np.linspace(-0.2, 0.2, 801); e = np.linspace(-1, 1, 801)
T, E = np.meshgrid(t, e)
P = E**4 + np.sin(T)*E**2 + np.sin(T)**2
Pt = np.cos(T)*E**2 + 2*np.sin(T)*np.cos(T)
Pe = 4*E**3 + 2*np.sin(T)*E
m = P > 1e-14
print("min P/(t^2+e^4) on grid:", (P[m]/(T[m]**2+E[m]**4)).min())
print("min (t P_t + e P_e/2)/P  (DE, w=1/2):", ((T*Pt+0.5*E*Pe)[m]/P[m]).min())
for k in [0.001, 0.05, 0.1, 0.2, 0.3]:
    r = ((k*T*Pt + 1.5*E*Pe)[m]/P[m]).min()
    r2 = ((k*T*Pt + 0.5*k*E*Pe)[m]/P[m]).min()
    print(f"kappa={k}: min (k t P_t + c e P_e)/P with c=3/2: {r:.4f};  with c2=kappa/2: {r2:.5f} (= {r2/k:.4f} kappa)")
# threshold kappa where the c2=c ratio becomes >= 0
ks = np.linspace(0.15, 0.35, 201)
for k in ks:
    if ((k*T*Pt + 1.5*E*Pe)[m]/P[m]).min() >= 0:
        print("c2=c: ratio >= 0 from kappa ~", round(k, 4)); break
print("(14-sqrt(192))*c =", (14-np.sqrt(192))*1.5)
# K = [-1/4,1/4]^2 (r_W = 1/4): (W1), (W2) with c2 = kappa/2, mu0 = 1; and m(r_W/2) for delta_0
t = np.linspace(-0.25, 0.25, 1001); e = np.linspace(-0.25, 0.25, 1001)
T, E = np.meshgrid(t, e)
P = E**4 + np.sin(T)*E**2 + np.sin(T)**2
Pt = np.cos(T)*E**2 + 2*np.sin(T)*np.cos(T)
Pe = 4*E**3 + 2*np.sin(T)*E
m = P > 1e-14
print("r_W=1/4: min (t P_t + e P_e/2)/P on K:", ((T*Pt+0.5*E*Pe)[m]/P[m]).min())
far = np.maximum(abs(T), abs(E)) >= 0.125 - 1e-12
print("r_W=1/4: m(r_W/2) =", P[far].min(), " delta_0 = m/8 =", P[far].min()/8, " (exact (3/4)(1/8)^4/8 =", 0.75*0.125**4/8, ")")
