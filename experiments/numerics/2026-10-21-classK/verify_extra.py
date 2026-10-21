"""verify_extra.py -- brute-force checks (mpmath dps 60) for the two non-K cases with explicit next-order data:
 A4: at the zero omega_0=(1,0,1)/sqrt2 of G (G>=0, G''>0):  min_eta U /s^7 -> g_7(omega_0) = -sqrt2/16 (cascade);
 D1: G=g_8 = -1/16 constant: min_eta U/s^8 -> -1/16 at several points of Sigma+ (and at the point of min g_9: next order).
[Experiment]"""
import sympy as sp, mpmath as mp
from verify import num_funcs, newton_fibre
import comps
from comps import x, y, z, t
mp.mp.dps = 60
def nu_of(f, w):
    return mp.matrix(sp.lambdify((x, y, z), [sp.diff(f, v) for v in (x, y, z)], 'mpmath')(*w))
f, g, H = num_funcs('A4')
w = mp.matrix([1, 0, 1])/mp.sqrt(2); nu = nu_of(comps.Q, w); nu = nu/mp.norm(nu)
print('A4 at omega_0=(1,0,1)/sqrt2: min_eta U/s^7 divided by (-sqrt2/16):')
for s in ['1e-2', '1e-3', '1e-4', '1e-5']:
    s = mp.mpf(s); val, eta = newton_fibre(f, g, H, w, [nu], s)
    print('   s=%s  ratio=%s   (U/s^6 = %s)' % (mp.nstr(s, 3), mp.nstr(val/s**7/(-mp.sqrt(2)/16), 10), mp.nstr(val/s**6, 6)))
f, g, H = num_funcs('D1')
for phi in [0, 1, 2.5, 4]:
    w = mp.matrix([mp.cos(phi), mp.sin(phi), 1])/mp.sqrt(2); nu = nu_of(comps.Q, w); nu = nu/mp.norm(nu)
    row = []
    for s in ['1e-2', '1e-3', '1e-4', '1e-5']:
        s = mp.mpf(s); val, eta = newton_fibre(f, g, H, w, [nu], s)
        row.append(mp.nstr(val/s**8*(-16), 8))
    print('D1 phi=%s: min_eta U/(s^8 (-1/16)) at s=1e-2..1e-5:' % phi, row)
