# sensitivity test: wrong coefficient in s*eta0_ss must FAIL
import sympy as sp
s, th = sp.symbols('s theta', real=True)
N = sp.Integer(3); sig = sp.symbols('sigma', positive=True)
y0 = sp.Function('y0')
e0 = s*y0(s**(1/N), th)
a = (s*sp.diff(e0, s, 2)).subs(s, sig**N).doit()
good = sig/N*((1+1/N)*sp.diff(y0(sig, th), sig) + sig/N*sp.diff(y0(sig, th), sig, 2))
bad = sig/N*((1+2/N)*sp.diff(y0(sig, th), sig) + sig/N*sp.diff(y0(sig, th), sig, 2))
print('good:', sp.simplify(a-good)); print('bad :', sp.simplify(a-bad))
