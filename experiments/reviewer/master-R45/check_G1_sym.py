"""Проверка (G1) леммы G: если <nu,Y> = 1, Y = nu/|nu|^2 + Y_T, Y_T ⟂ nu, h = |Y|^2, то
|nu - Y/h|^2 (1 + |nu|^2 |Y_T|^2) = |nu|^4 |Y_T|^2 (откуда |nu - Y/h| <= |nu|^2 |Y_T|).
[Эксперимент] рецензента R45; произвольные nu, Z в R^n (Y_T = Z - <Z,nu> nu/|nu|^2)."""
import sympy as sp

for n in (2, 3, 4):
    nu = sp.Matrix(sp.symbols(f'n1:{n+1}', real=True))
    Z = sp.Matrix(sp.symbols(f'z1:{n+1}', real=True))
    N2 = (nu.T * nu)[0]
    YT = Z - (Z.T * nu)[0] / N2 * nu
    Y = nu / N2 + YT
    h = (Y.T * Y)[0]
    d = nu - Y / h
    lhs = (d.T * d)[0] * (1 + N2 * (YT.T * YT)[0])
    rhs = N2**2 * (YT.T * YT)[0]
    print(n, 'nu.Y=1:', sp.simplify((nu.T * Y)[0] - 1) == 0,
          ' (G1) identity:', sp.simplify(lhs - rhs) == 0)
