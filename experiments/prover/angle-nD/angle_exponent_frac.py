# [Эксперимент] Пример с дробным показателем: рог вокруг полукубической параболы y = x^{3/2}.
# U = (y^2 - x^3)^2 - x^10. Ожидание: M(r) ~ C r^{1/2}, т.е. d = 1/2.
import mpmath as mp
mp.mp.dps = 50
U  = lambda X,Y: (Y**2 - X**3)**2 - X**10
gU = lambda X,Y: (-6*X**2*(Y**2-X**3) - 10*X**9, 4*Y*(Y**2-X**3))
def M(r, N=4001):
    r = mp.mpf(r); best = -2
    # рог: y = x^{3/2}(1+e), |e| < x^2/2 примерно; параметр: x, e -> точка, затем нормировка к |p| = r не нужна:
    # берём точку (x, y) в роге и считаем g; радиус ~ x. Максимум по e при фиксированном x.
    xx = r
    for k in range(N):
        e = (mp.mpf(2*k)/(N-1) - 1) * xx**2 * mp.mpf('0.7')
        yy = xx**mp.mpf(1.5)*(1+e)
        if U(xx,yy) < 0:
            gx, gy = gU(xx,yy)
            g = (xx*gx+yy*gy)/(mp.sqrt(xx**2+yy**2)*mp.sqrt(gx**2+gy**2))
            best = max(best, g)
    return best
rs = ['1e-2','1e-3','1e-4','1e-5','1e-6']
Ms = [M(r) for r in rs]
for r,m in zip(rs,Ms): print(" x=%s  max g = %s" % (r, mp.nstr(m,8)))
print(" наклоны:", [mp.nstr((mp.log(Ms[i+1])-mp.log(Ms[i]))/(mp.log(mp.mpf(rs[i+1]))-mp.log(mp.mpf(rs[i]))),5) for i in range(len(rs)-1)])
