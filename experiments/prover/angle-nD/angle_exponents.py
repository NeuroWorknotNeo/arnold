# [Эксперимент] Оценка M(r) = sup{ <x,gradU>/(|x||gradU|) : U(x)<0, |x|=r } и показателя d
# в теореме 1(a) на примерах. Перебор по сетке (не доказательство).
import numpy as np, mpmath as mp
mp.mp.dps = 40

def M2(Uf, gf, r, a0, a1, N=40001):
    best = -2
    for al in np.linspace(a0, a1, N):
        xx, yy = mp.mpf(r)*mp.cos(al), mp.mpf(r)*mp.sin(al)
        if Uf(xx,yy) < 0:
            gx, gy = gf(xx,yy)
            g = (xx*gx+yy*gy)/(mp.mpf(r)*mp.sqrt(gx**2+gy**2))
            best = max(best, g)
    return best

# (i) U = (y-x^2)^2 - x^6 (искривлённый узкий рог), (ii) U = (y-x^2)(y-2x^2) (квазиоднородный),
# (iii) U = x^3 - 3 x y^2 + (x^2+y^2)^2  (невырожденная младшая форма u_3)
ex = {
 '(y-x^2)^2-x^6': (lambda X,Y: (Y-X**2)**2 - X**6,
                   lambda X,Y: (-4*X*(Y-X**2) - 6*X**5, 2*(Y-X**2)), lambda r: (r - 3*r**2, r + 3*r**2)),
 '(y-x^2)(y-2x^2)': (lambda X,Y: (Y-X**2)*(Y-2*X**2),
                   lambda X,Y: (-2*X*(Y-2*X**2) - 4*X*(Y-X**2), 2*Y - 3*X**2), lambda r: (0.5*r, 3*r)),
 'x^3-3xy^2+(x^2+y^2)^2': (lambda X,Y: X**3-3*X*Y**2+(X**2+Y**2)**2,
                   lambda X,Y: (3*X**2-3*Y**2+4*X*(X**2+Y**2), -6*X*Y+4*Y*(X**2+Y**2)), lambda r: (-np.pi, np.pi)),
}
for name,(Uf,gf,win) in ex.items():
    rs = [1e-1, 3e-2, 1e-2, 3e-3, 1e-3]
    Ms = []
    for r in rs:
        a0,a1 = win(r)
        Ms.append(M2(Uf,gf,r,a0,a1))
    print(name)
    for r,Mv in zip(rs,Ms): print("   r=%.0e  M(r)=% .6e" % (r, Mv))
    slopes = [ (mp.log(abs(Ms[i+1]))-mp.log(abs(Ms[i])))/(mp.log(rs[i+1])-mp.log(rs[i])) for i in range(len(rs)-1)]
    print("   наклоны log|M| / log r:", [mp.nstr(s,4) for s in slopes])
