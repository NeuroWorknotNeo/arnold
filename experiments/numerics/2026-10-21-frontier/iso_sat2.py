"""
iso_sat2.py -- двойное насыщение: K = (J : p1^inf) : p2^inf, p1 = x^2+y^2+z^2, p2 = x^2+2y^2+3z^2 (обе положительно определены).
Вещественные критические точки q != 0 лежат в V(K) (p1 p2 > 0 в q); комплексные изотропные прямые {x^2+y^2=0, z=0} ⊂ V(p1) и {x^2+2y^2=0, z=0} ⊂ V(p2)
выбрасываются. Если K не лежит в максимальном идеале m, то 0 не принадлежит V(K) и вещественно изолирована.  [Эксперимент: точно, Singular]
usage: python iso_sat2.py ID ... -> iso_sat2.txt
"""
import sys, os, time, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '2026-10-21-zoo'))
import sympy as sp, sing, fcat
x, y, z = sp.symbols('x y z')
for eid in sys.argv[1:]:
    e = {t['id']: t for t in fcat.CAT}[eid]
    U = sp.sympify(e['U'], locals=dict(x=x, y=y, z=z))
    J = [sp.diff(U, v) for v in (x, y, z)]
    g = ','.join(sing.to_sing(t) for t in J)
    t0 = time.time()
    out = sing.run(sing.HEAD + f'''ring r=0,(x,y,z),dp; ideal J={g}; ideal K1=sat(J,ideal(x2+y2+z2)); ideal K=sat(K1,ideal(x2+2y2+3z2));
    ideal SK=std(K); ideal mm=maxideal(1);
    print("UNIT=" + string(reduce(1,SK)==0));
    print("INM=" + string(size(reduce(SK,std(mm)))==0));''', timeout=20000)
    inm = 'INM=1' in out
    line = f"{eid}: K=(J:p1^inf):p2^inf  {'содержится в m (изолированность над R НЕ сертифицирована)' if inm else 'НЕ содержится в m  =>  0 изолирована над R (сертификат)'}; UNIT={'UNIT=1' in out}; {time.time()-t0:.0f} s"
    print(line, flush=True)
    open(os.path.join(HERE, 'iso_sat2.txt'), 'a').write(line + '\n')
