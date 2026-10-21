"""Проверка контрпримера к выкладке леммы 2.2 arXiv:2108.05829v4 (см.
notes/vlad-claude/burgos-review.md, §3a). Запуск: python3 check.py"""
import sympy as sp

x, y, w1, w2, v1, v2, a = sp.symbols('x y w1 w2 v1 v2 a', real=True)
# карта раздутия нуля: x = w1, y = w1*(w2 + a); поле Эйлера w1 d/dw1 + w2 d/dw2
X, Y = w1, w1 * (w2 + a)
J = sp.Matrix([[X.diff(w1), X.diff(w2)], [Y.diff(w1), Y.diff(w2)]])
V = sp.simplify((J * sp.Matrix([w1, w2])).subs({w1: x, w2: y / x - a}))
print('V =', V.T)
S = sp.simplify((V.jacobian([x, y]) + V.jacobian([x, y]).T) / 2)
print('sym DV =', S, ' det =', sp.factor(S.det()))
U = x * (y - 3 * x)
grad = sp.Matrix([U.diff(x), U.diff(y)])
print('V(U)/U при a=3:', sp.simplify((V.T * grad)[0].subs(a, 3) / U))
q = sp.expand((sp.Matrix([v1, v2]).T * S * sp.Matrix([v1, v2]))[0].subs(a, 3))
print('<v, D_v V> при a=3:', q, '; при v=(4,3):', q.subs({v1: 4, v2: 3}))
