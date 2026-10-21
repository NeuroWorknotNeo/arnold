# Check (3.1)-(3.3) with generic functions: compute, then replace all derivatives by independent jet symbols and cancel.
import sympy as sp
def check(n):
    q = sp.symbols('q1:%d'%(n+1)); v = sp.symbols('v1:%d'%(n+1))
    U = sp.Function('U')(*q); rho = sp.Function('rho')(*q)
    Z = [sp.Function('Z%d'%i)(*q) for i in range(n)]
    beta, delta = sp.symbols('beta delta', positive=True)
    Ap = sp.Symbol('Ap')  # value A'(rho(q)) at the point; chain rule handled manually
    grad = lambda f: sp.Matrix([sp.diff(f, qi) for qi in q])
    gr = grad(rho); Zm = sp.Matrix(Z); Y = Zm/(gr.dot(Zm)); vm = sp.Matrix(v)
    h = Y.dot(Y); pi = vm.dot(Y); vperp = vm - (pi/h)*Y
    gU = grad(U)
    def ddt(f):
        return sum(sp.diff(f, q[i])*v[i] for i in range(n)) + sum(sp.diff(f, v[i])*(-gU[i]) for i in range(n))
    DY = lambda w: sp.Matrix([sum(sp.diff(Y[j], q[i])*w[i] for i in range(n)) for j in range(n)])
    V0 = vm.dot(vm)/2 - pi**2/(2*h) + U
    rhodot = ddt(rho)
    Vdot = ddt(V0) + Ap*rhodot
    YW = gU.dot(Y) + Ap
    e31 = rhodot - (pi/h + gr.dot(vperp))
    rhs32 = (pi/h)*YW + Ap*gr.dot(vperp) - (pi/h)**2*vperp.dot(DY(Y)) - (pi/h)*vperp.dot(DY(vperp))
    e32 = Vdot - rhs32
    lam = -pi/h
    Xi = Vdot - beta*delta*rho**(beta-1)*rhodot
    T1 = (rho/lam)*(Ap - beta*delta*rho**(beta-1))*(gr - Y/h).dot(vperp)
    T2 = -lam*rho*vperp.dot(DY(Y)); T3 = rho*vperp.dot(DY(vperp))
    e33 = (rho/lam)*Xi - ((beta*delta*rho**beta - rho*YW) + T1 + T2 + T3)
    out = []
    for e in (e31, e32, e33):
        derivs = sorted(e.atoms(sp.Derivative), key=lambda d: -len(d.variables))
        sub = {d: sp.Symbol('D%d'%k) for k, d in enumerate(derivs)}
        e2 = e.xreplace(sub)
        funcs = e2.atoms(sp.core.function.AppliedUndef)
        e2 = e2.xreplace({f: sp.Symbol('F_'+str(f.func)) for f in funcs})
        out.append(sp.cancel(sp.together(e2)))
    return out
for n in (2, 3):
    print('n=', n, check(n), flush=True)
