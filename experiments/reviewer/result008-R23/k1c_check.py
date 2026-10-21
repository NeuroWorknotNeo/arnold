"""R23: все точки (K3) примера 3 и знак G''+7G в них (принадлежность K^1_C). [Эксперимент, точно]"""
import sympy as sp
ph = sp.Symbol('phi', real=True)
Gp = sp.sqrt(2)/32*(1+2*sp.cos(ph)+sp.sin(2*ph))
Gm = sp.sqrt(2)/32*(2*sp.cos(ph)-sp.sin(2*ph)-1)
for name, G, pts in (('G+', Gp, [sp.pi/6, 5*sp.pi/6, 3*sp.pi/2]), ('G-', Gm, [sp.pi/2, 7*sp.pi/6, 11*sp.pi/6])):
    for p in pts:
        g = sp.nsimplify(sp.simplify(G.subs(ph, p)))
        g2nat = sp.simplify(2*sp.diff(G, ph, 2).subs(ph, p))   # natural parameter theta = phi/sqrt2
        g3 = sp.simplify(sp.diff(G, ph, 3).subs(ph, p))
        print(name, p, ' G =', g, float(g), ' G\'\'(nat) =', g2nat, float(g2nat), " G'''=", g3,
              ' G\'\'+7G =', sp.simplify(g2nat+7*g), float(g2nat+7*g))
