import random, itertools, time, json, sys, collections
import multiprocessing as mp
import sympy as sp
from sieve import classify, x, y, z

def monomials(deg):
    return [x**a*y**b*z**(deg-a-b) for a in range(deg+1) for b in range(deg+1-a)]

def rand_poly(degs, p, coeffs, rng):
    terms = []
    for d in degs:
        for m in monomials(d):
            if rng.random() < p: terms.append(rng.choice(coeffs)*m)
    return sp.expand(sum(terms, sp.Integer(0)))

Q = x**2 + y**2 - z**2
L4 = [x**2*y**2 + y**2*z**2 + z**2*x**2, (x**2-z**2)**2 + (y**2-z**2)**2, x**4 + y**4, z**2*(x**2+y**2) + x**4]

def make_family(name, N, seed):
    rng = random.Random(seed); out = []
    while len(out) < N:
        if name == 'A':   # generic sparse, degrees 2..6
            U = rand_poly(range(2, 7), 0.12, [-3,-2,-1,1,2,3], rng)
        elif name == 'B': # Hessian = 0 and U3 = 0, degrees 4..6
            U = rand_poly(range(4, 7), 0.12, [-3,-2,-1,1,2,3], rng)
        elif name == 'C': # gutter class (x^2+y^2-z^2)^2 + sparse W of degrees 5..8
            U = sp.expand(Q**2 + rand_poly(range(5, 9), 0.035, [-2,-1,1,2], rng))
        elif name == 'D': # psd quartic with finitely many zeros + sparse W of degrees 5..7
            U = sp.expand(rng.choice(L4) + rand_poly(range(5, 8), 0.04, [-2,-1,1,2], rng))
        if U != 0: out.append(str(U))
    return out

def work(s):
    t0 = time.time()
    try: v, why = classify(s)
    except Exception as e: v, why = 'ERROR', repr(e)[:200]
    return s, v, why, time.time() - t0

if __name__ == '__main__':
    sizes = {'A': 200, 'B': 200, 'C': 400, 'D': 240}
    only = sys.argv[2] if len(sys.argv) > 2 else 'ABCD'
    sizes = {k: v for k, v in sizes.items() if k in only}
    allres = {}
    with mp.Pool(int(sys.argv[1]) if len(sys.argv) > 1 else 4) as pool:
        for name, N in sizes.items():
            fam = make_family(name, N, seed={'A': 1, 'B': 2, 'C': 3, 'D': 4}[name])
            res = pool.map(work, fam, chunksize=4)
            allres[name] = res
            cnt = collections.Counter(v for _, v, _, _ in res)
            reasons = collections.Counter(why.split(']')[0] + ']' if why.startswith('[') else why.split(':')[0][:60]
                                          for _, v, why, _ in res)
            print('Family %s (N=%d):' % (name, N), dict(cnt), flush=True)
            print('   by reason:', dict(reasons.most_common(12)), flush=True)
    json.dump(allres, open('families_results_%s.json' % only, 'w'), indent=1)
