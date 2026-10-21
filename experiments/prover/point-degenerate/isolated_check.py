"""[Эксперимент] Нульмерность идеала (grad U) для примеров (sympy, базис Грёбнера, grevlex).
Нульмерность над C влечёт изолированность всех критических точек, в том числе 0."""
import sys, sympy as sp
x, y, z = sp.symbols('x y z')
k = sp.Rational(199, 100)
EX = {
 'Lambda': x**4 - k*x**2*y*z + y**2*z**2 + y**4 - z**8 + x*z**7,
 'SV': z**4*(y - x**2)**2 + x**6 + y**6 - z**12 + x*z**11,
 'SH': z**4*(y - x**2 - x*z)**2 + x**6 + y**6 - z**12 + x*z**11,
 'X': x**6 + y**6 + y**4*z**2 + x**2*y**2*z**2 - z**12 + x*z**11,
 'E': x**12 + y**12 + z**4*(x**2 - y*z**2)**2*(x**3 - y*z**4)**2 - z**24 + x*z**23,
 'R': (x**2 + y**2 - z**3)**2 - z**8 + x*z**8,
}
name = sys.argv[1]
U = EX[name]
G = sp.groebner([sp.diff(U, v) for v in (x, y, z)], x, y, z, order='grevlex')
print(name, 'zero-dimensional:', G.is_zero_dimensional)
