"""iso_sat2_p.py -- то же двойное насыщение, что iso_sat2.py (frontier), но над F_p (p = 32003): быстрый ПРЕДВАРИТЕЛЬНЫЙ индикатор.
Если K = (J:p1^inf):p2^inf (над F_p) не лежит в m, это сильный индикатор, но НЕ сертификат над Q (редукция по модулю p может отличаться от насыщения над Q).
usage: python iso_sat2_p.py ID [...]"""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '2026-10-21-zoo')); sys.path.insert(0, os.path.join(HERE, '..', '2026-10-21-frontier'))
import sympy as sp, sing, fcat
x, y, z = sp.symbols('x y z')
for eid in sys.argv[1:]:
    e = {t['id']: t for t in fcat.CAT}[eid]
    U = sp.sympify(e['U'], locals=dict(x=x, y=y, z=z))
    J = [sp.diff(U, v) for v in (x, y, z)]
    g = ','.join(sing.to_sing(t) for t in J)
    t0 = time.time()
    out = sing.run(sing.HEAD + f'''ring r=32003,(x,y,z),dp; ideal J={g}; ideal K1=sat(J,ideal(x2+y2+z2)); ideal K=sat(K1,ideal(x2+2y2+3z2));
    ideal SK=std(K); ideal mm=maxideal(1);
    print("UNIT=" + string(reduce(1,SK)==0));
    print("INM=" + string(size(reduce(SK,std(mm)))==0));''', timeout=3000)
    inm = 'INM=1' in out
    print(f"{eid} (F_32003): K {'лежит в m: изолированность НЕ подтверждена' if inm else 'НЕ лежит в m: индикатор изолированности (не сертификат над Q)'}; UNIT={'UNIT=1' in out}; {time.time()-t0:.0f} s", flush=True)
