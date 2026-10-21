# [Эксперимент] Изолированность критической точки 0 у примеров записки
# notes/prover/2026-10-21-morse-bott-mult.md, §10 (для теорем записки она НЕ нужна).
# Критерий: идеал (dU/dx, dU/dy, dU/dz) в Q[x,y,z] нульмерен (базис Грёбнера grevlex содержит
# старшие члены — чистые степени каждой переменной). Тогда комплексных критических точек конечно
# много, и 0 изолирована (над C, а значит, и над R). Если идеал не нульмерен, ничего не утверждается.
# Запуск: python isolated.py NAME   (NAME из списка ниже)
import sys
import sympy as sp

x, y, z = sp.symbols('x y z')
rho2 = x**2 + y**2
f4 = 6*rho2**2 + 4*(x**2 - y**2)*rho2 - (x**4 - 6*x**2*y**2 + y**4)
EX = {
    'W1': (z - x**2)**4 + sp.Rational(3, 2)*x*rho2**2 - sp.Rational(1, 2)*x**3*rho2 + y*z**5,
    'W2': z**4 + z*f4 + x**6 + y*z**5,
    'W3': z**4 + z**2*y*rho2 - rho2**3 + y**2*rho2**2 + x*z**5 + y**7,
    'W4': (z**2 - rho2**2)**2 + z*x**8,
    'C1': (z + x*y)**4 - rho2**3 + x**7 + z**3*y**4,
    'C2': z**4 + z*rho2**2 + x**6*z + y**7,
    'D1': (z - x*y - x**3)**4 + y**2*rho2**2 + x**7,
    'D2': (z**2 - rho2**2)**2 + y**2*rho2**3 + x**9 + z**3*x**6,
    'D3': (z**2 - rho2**2)**2 + z**2*y**2*rho2**2 + x**11,
    'O2': z**4 - 2*z**2*y*rho2 - x**2*rho2**2 + x**7 + y**7,
    'W4i': (z**2 - rho2**2)**2 + z*x**8 + y**11,
}
name = sys.argv[1]
U = sp.expand(EX[name])
grad = [sp.expand(sp.diff(U, v)) for v in (x, y, z)]
G = sp.groebner(grad, x, y, z, order='grevlex')
lms = [sp.Poly(g, x, y, z).monoms(order='grevlex')[0] for g in G.exprs]
pure = {i: any(m[i] > 0 and all(m[k] == 0 for k in range(3) if k != i) for m in lms) for i in range(3)}
print(name, ': число элементов базиса', len(G.exprs), '; чистые степени x, y, z среди старших мономов:', pure)
print(name, ': идеал нульмерен =>', 'ИЗОЛИРОВАНА (над C и R)' if all(pure.values()) else 'не нульмерен (вывода нет)')
