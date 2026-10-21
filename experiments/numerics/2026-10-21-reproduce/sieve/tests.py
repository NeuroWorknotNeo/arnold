import time
from sieve import classify
tests = [
 ("x**2 - y**2 + z**4",                          "Lyapunov"),
 ("x**2 + y**2 - z**4",                          "Pa20-T5 (corank 1)"),
 ("x**2 + y**4 - z**4",                          "Ko86 (corank 2)"),
 ("x**3 + y**4 + z**4",                          "KP82 (odd form)"),
 ("x**4 + y**4 - z**4",                          "Pa20-T3"),
 ("x**4 + y**4 - z**6",                          "Pa20-T6 (quasi-homogeneous)"),
 ("(x**2+y**2-z**2)**2 - z**6",                  "Bu25 / N13"),
 ("(x**2+y**2-z**2)**2 + x*z**5",                "N13 (circular gutter)"),
 ("(x**2+y**2-z**2)**2 + z**5*x + z**4*x*y + z**6/2", "N13 (Example 13)"),
 ("(x**2+y**2-z**2 - z*(x**2+x*y))**2 - z**8",   "Example 14: gutter must be corrected -> suspicious"),
 ("(x**2+y**2-z**2)**2 + z**4*(z-x)**2 - z**8",  "double zero, but symmetric -> SYM"),
 ("(x**2+y**2-z**2)**2 + y**2*z**4 + x*y*z**5/10 - z**8", "double zero of effective potential, no symmetry -> suspicious"),
 ("(x**2-y**2)**2 + z**4 + x**5",                "point-horn with quartic transverse part"),
 ("x**2*y**2 + y**2*z**2 + z**2*x**2 + x*y*z*(x+y+z)**2", "critical axes -> nonisolated"),
 ("x**2*y**2 + y**2*z**2 + z**2*x**2 + x**5 + y**5 + z**5", "finite zeros of U4 -> point-horns"),
 ("(x**2+y**2+z**2)**2",                          "strict min"),
]
for s, expect in tests:
    t0 = time.time()
    try:
        v, why = classify(s)
    except Exception as e:
        v, why = 'ERROR', repr(e)
    print("%-55s | expect: %-45s | %-16s %s   (%.1fs)" % (s, expect, v, why, time.time()-t0), flush=True)
