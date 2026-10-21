# [символьно] theoremC-draft, режим 4 (трубка вокруг луча θ0=π/2): мономы веса d=28/3 (грань) и 29/3 (пограничные)
# координаты как в k4_perp.py: ρ=(s+σ)/2, z=(s−σ)/2, θ=π/2+t; веса s:1, t:1/3, σ:4/3
import sympy as sp
s, t, sg, K = sp.symbols('s t sigma K')
rho = (s + sg)/2; z = (s - sg)/2
for name, (cx, cy) in (("x-вар.", (1, 0)), ("y-вар.", (0, 1))):
    xx = rho*sp.cos(sp.pi/2 + t); yy = rho*sp.sin(sp.pi/2 + t)
    q = s*sg
    U = q**4 + xx*z**8 + K*q*(cx*xx + cy*yy)*z**6
    # ряд по t до t^3
    Ut = sp.series(U, t, 0, 4).removeO()
    P = sp.Poly(sp.expand(Ut), s, t, sg)
    face, border = [], []
    for (a, bb, c), co in P.terms():
        w = sp.Rational(a) + sp.Rational(bb, 3) + sp.Rational(4*c, 3)
        if w == sp.Rational(28, 3): face.append((a, bb, c, co))
        if w == sp.Rational(29, 3): border.append((a, bb, c, co))
        if w < sp.Rational(28, 3): print("  !! вес меньше грани:", (a, bb, c, co))
    print(name, "грань:", face)
    print(name, "пограничные (вес 29/3):", border)
