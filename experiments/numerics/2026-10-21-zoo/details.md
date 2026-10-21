## K1: x^4+y^4-z^6

- U = `x**4 + y**4 - z**6`
- why: calibration: quasi-homogeneous (weights 3,3,2), u_4 = x^4+y^4 >= 0 vanishes on the z-axis
- lowest degree m = 4; forms: u_4=x**4 + y**4; u_6=-z**6
- isolation: μ=45 (Singular, локальный базис, конечен ⇒ изолирована и над ℂ); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['COMP 1 dim=0 : z,y,x']
- not a minimum: луч w=(0, 0, -1): U(tw) = -1·t^6 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=False ['zero direction (0, 0, 1): rank Hess = 0 < 2 (degenerate transverse part)']; B3=False ['u_{m+1} == 0']; l2=6
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: yes — U quasi-homogeneous with weights (3, 3, 2), degree 12; U(-6, -6, -6) < 0 (Euler field V = (1/d) sum a_i x_i d_i)
  - **Pa20-T6**: yes — weights (3, 3, 2), d=12, face has 3 monomials, tail wdeg_min=None (principal part no real crit. points, negative values, tail >= d + a_max)
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: yes — u_6 < 0 on the whole zero set of u_4 (l2 = 6 even)
  - **ThmB**: no — (B2) fails: zero direction (0, 0, 1): rank Hess = 0 < 2 (degenerate transverse part) | (B3) fails: u_{m+1} == 0
  - **N13***: no — u_4 is not c Q^2 with a quadratic form Q
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: yes — invariant plane with normal [-1, 1, 0], U|plane is not a local minimum (exact witness ('ray', (0, -8), 6, -262144)) -> n=2 theorem
- invariant planes/lines of the dynamics (exact search): [{'kind': 'plane', 'normal': [0, 0, 1], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'plane', 'normal': [-1, 1, 0], 'verdict': 'yes', 'note': "('ray', (0, -8), 6, -262144)"}, {'kind': 'plane', 'normal': [0, 1, 0], 'verdict': 'yes', 'note': "('ray', (0, -8), 6, -262144)"}, {'kind': 'plane', 'normal': [1, 1, 0], 'verdict': 'yes', 'note': "('ray', (0, -8), 6, -262144)"}, {'kind': 'plane', 'normal': [1, 0, 0], 'verdict': 'yes', 'note': "('ray', (0, -8), 6, -262144)"}, {'kind': 'line', 'direction': [1, -1, 0], 'verdict': 'no', 'note': 'U on the line = 2 t^4 + ...'}, {'kind': 'line', 'direction': [1, 0, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}, {'kind': 'line', 'direction': [1, 1, 0], 'verdict': 'no', 'note': 'U on the line = 2 t^4 + ...'}, {'kind': 'line', 'direction': [0, 1, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}, {'kind': 'line', 'direction': [0, 0, 1], 'verdict': 'yes', 'note': 'U on the line = -1 t^6 + ...'}]
- covered by known: ['QH-linear', 'Bu25-C1.4', 'SYM']; ours: []; soft: ['Pa20-T6']; NOT COVERED: False; (3.0 s)

## K2: Example 13

- U = `x**4 + 2*x**2*y**2 - 2*x**2*z**2 + x*y*z**4 + x*z**5 + y**4 - 2*y**2*z**2 + z**6/2 + z**4`
- why: calibration: circular gutter, effective potential with simple zeros; covered only by our Example-13 criterion
- lowest degree m = 4; forms: u_4=x**4 + 2*x**2*y**2 - 2*x**2*z**2 + y**4 - 2*y**2*z**2 + z**4; u_6=x*y*z**4 + x*z**5 + z**6/2
- isolation: μ=∞ (над ℂ не изолирована); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['COMP 1 dim=1 : x^2+y^2,z', 'COMP 2 dim=0 : 4*z^10-96*z^8+891*z^6-11232*z^4-36720*z^2-39744,-12596*z^9+579024*z^7-7883919*z^5+66932244*z^3+534794544*y+104214096*z,6524*z^9-158376*z^7+1460485*z^5-24979650*z^3+89132424*x-13897008*z']
- not a minimum: луч w=(-4, 3, 5): U(tw) = -24375/2·t^6 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=True ['Hess u_m != 0 on {x**2 + y**2 - z**2=0} (rank 1 = n-1-s): Morse-Bott']; B3=False ['u_{m+1} == 0']; l2=6
- naive restriction to the conic gutter (first form not vanishing identically on it): [{'degree': 6, 'zero': False, 'const': '1/2', 'factors': [('5*t**2 - 6*t + 5', 4, 0), ('9*t**4 - 92*t**3 + 86*t**2 - 28*t + 41', 1, 2)], 'deg_in_t': 12, 'inf_order': 0}]
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (1, 1, 1), d=4, face has 6 monomials, tail wdeg_min=6: principal part no certificate of absence of real critical points
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — u_6 has real zeros on {x**2 + y**2 - z**2=0} (or inconclusive): ideal saturation not the unit ideal
  - **ThmB**: no — (B3) fails: u_{m+1} == 0
  - **N13***: yes — circular 45-degree cone, W_6 simple zeros, negative at the gutter point (-4, 3, 5) [Эскиз, 003 Prop. 1]
  - **N13**: yes — U is exactly the polynomial of Example 13
  - **SYM**: no — exact search of ALL invariant planes and lines: plane [0, 0, 1]: no; line [0, 1, 0]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'plane', 'normal': [0, 0, 1], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'line', 'verdict': 'info', 'note': 'chart (1, pb, pc): family of invariant lines lying in a plane (linear:pc); that plane is tested by the plane search'}, {'kind': 'line', 'direction': [0, 1, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}]
- covered by known: []; ours: ['N13']; soft: ['N13*']; NOT COVERED: False; (26.4 s)

## K3: Theorem B example Q^2 + x z^4

- U = `x**4 + 2*x**2*y**2 - 2*x**2*z**2 + x*z**4 + y**4 - 2*y**2*z**2 + z**4`
- why: calibration: example of results/002 (has the reflection y -> -y, hence also covered by the n=2 reduction)
- lowest degree m = 4; forms: u_4=x**4 + 2*x**2*y**2 - 2*x**2*z**2 + y**4 - 2*y**2*z**2 + z**4; u_5=x*z**4
- isolation: μ=∞ (над ℂ не изолирована); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['COMP 1 dim=1 : x^2+y^2,z', 'COMP 2 dim=0 : 4*z^2+25,4*x+5,y']
- not a minimum: луч w=(-4, -3, -5): U(tw) = -2500·t^5 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=True ['Hess u_m != 0 on {x**2 + y**2 - z**2=0} (rank 1 = n-1-s): Morse-Bott']; B3=True ['0 regular value of u_5 on {x**2 + y**2 - z**2=0} (ideal (f,h,det[grad h,grad f,q]) has no real nonzero zero)']; l2=5
- naive restriction to the conic gutter (first form not vanishing identically on it): [{'degree': 5, 'zero': False, 'const': '-4', 'factors': [('t - 1', 1, 1), ('t + 1', 1, 1), ('5*t**2 - 6*t + 5', 4, 0)], 'deg_in_t': 10, 'inf_order': 0}]
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (1, 1, 1), d=4, face has 6 monomials, tail wdeg_min=5: principal part no certificate of absence of real critical points
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — l2 = 5 odd and Sigma = -Sigma: u_5(-w) = -u_5(w), so u_5 < 0 on all of Sigma is impossible
  - **ThmB**: yes — B1 (Sigma smooth submanifold), B2 (Morse-Bott), B3 (0 regular value of u_{m+1}|Sigma): Hess u_m != 0 on {x**2 + y**2 - z**2=0} (rank 1 = n-1-s): Morse-Bott | 0 regular value of u_5 on {x**2 + y**2 - z**2=0} (ideal (f,h,det[grad h,grad f,q]) has no real nonzero zero)
  - **N13***: yes — circular 45-degree cone, W_5 (m=5, odd) has only simple zeros on the gutter and takes negative values [Эскиз, 003 Prop. 1]
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: yes — invariant plane with normal [0, 1, 0], U|plane is not a local minimum (exact witness ('ray', (-8, -8), 5, -32768)) -> n=2 theorem
- invariant planes/lines of the dynamics (exact search): [{'kind': 'plane', 'normal': [0, 0, 1], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'plane', 'normal': [0, 1, 0], 'verdict': 'yes', 'note': "('ray', (-8, -8), 5, -32768)"}, {'kind': 'line', 'verdict': 'info', 'note': 'chart (1, pb, pc): family of invariant lines lying in a plane (linear:pc); that plane is tested by the plane search'}, {'kind': 'line', 'direction': [0, 1, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}]
- covered by known: ['SYM']; ours: ['ThmB']; soft: ['N13*']; NOT COVERED: False; (35.9 s)

## A1: Q^2 + effective potential, double zero from below

- U = `x**4 + 2*x**2*y**2 - 2*x**2*z**2 + x*y*z**4/2 + x*z**5 + y**4 - 2*y**2*z**2 - y*z**5/2 + z**7 - z**6 + z**4`
- why: W_6 on the gutter: G = (cos f - 1)(1+sin f/2) <= 0 with a DOUBLE zero at f=0; W_7 = z^7 (G7 = 1 > 0) keeps 0 isolated
- lowest degree m = 4; forms: u_4=x**4 + 2*x**2*y**2 - 2*x**2*z**2 + y**4 - 2*y**2*z**2 + z**4; u_6=x*y*z**4/2 + x*z**5 - y*z**5/2 - z**6; u_7=z**7
- isolation: μ=∞ (над ℂ не изолирована); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['COMP 1 dim=1 : x^2+y^2,z', 'COMP 2 dim=0 : 7*z^10-1568*z^9+130312*z^8-4835648*z^7+72820069*z^6-245402752*z^5+232743392*z^4-40145216*z^3-91929600*z^2+49886208*z-9289728,-376569332524554628406216941*z^9+84172311127629409485394950916*z^8-6970124150512470273968061324520*z^7+256815431279971058996251474267936*z^6-3795091315175451414094230802184695*z^5+11400900802500556785749057277057324*z^4-7267539708480608631822994808463600*z^3-1461367207578155593579904009840192*z^2+1663986327731523187920708415768704*y+4548070341228933308253216423767040*z-675574000735960168860472197636096,-20494561763699313004805475*z^9+4612646933418486121566863554*z^8-386386472149875097916331478848*z^7+14556670163089923412616261633584*z^6-227661418887346284965692028171457*z^5+923199996474387977647707340173574*z^4-1129802537542583226658314064659800*z^3+196657220548239981612126038958208*z^2+415996581932880796980177103942176*x+420720434219671219004182704814176*z-247251271724996936123279470675968']
- not a minimum: луч w=(-4, -3, -5): U(tw) = -8125/2·t^6 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=True ['Hess u_m != 0 on {x**2 + y**2 - z**2=0} (rank 1 = n-1-s): Morse-Bott']; B3=False ['u_{m+1} == 0']; l2=6
- naive restriction to the conic gutter (first form not vanishing identically on it): [{'degree': 6, 'zero': False, 'const': '-1/2', 'factors': [('t - 3', 2, 1), ('7*t**2 - 2*t + 7', 1, 0), ('5*t**2 - 6*t + 5', 4, 0)], 'deg_in_t': 12, 'inf_order': 0}]
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (1, 1, 1), d=4, face has 6 monomials, tail wdeg_min=6: principal part no certificate of absence of real critical points
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — u_6 has real zeros on {x**2 + y**2 - z**2=0} (or inconclusive): ideal saturation not the unit ideal
  - **ThmB**: no — (B3) fails: u_{m+1} == 0
  - **N13***: no — W_6|gutter has a multiple zero at w=(-1, 0, -1) (exact): not a regular value
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines: plane [0, 0, 1]: no; line [0, 1, 0]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'plane', 'normal': [0, 0, 1], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'line', 'verdict': 'info', 'note': 'chart (1, pb, pc): family of invariant lines lying in a plane (linear:pc); that plane is tested by the plane search'}, {'kind': 'line', 'direction': [0, 1, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}]
- covered by known: []; ours: []; soft: []; NOT COVERED: True; (38.2 s)

## A2: Q^2 + effective potential, double zero from above

- U = `x**4 + 2*x**2*y**2 - x**2*z**4 - 2*x**2*z**2 - x*y*z**4/3 + 3*x*z**5/2 + y**4 - 2*y**2*z**2 + y*z**5/3 - z**7 - z**6/2 + z**4`
- why: G = (1-cos f)(cos f + sin f/3 - 1/2): G >= 0 near the DOUBLE zero f=0, negative elsewhere; G7 = -1 < 0
- lowest degree m = 4; forms: u_4=x**4 + 2*x**2*y**2 - 2*x**2*z**2 + y**4 - 2*y**2*z**2 + z**4; u_6=-x**2*z**4 - x*y*z**4/3 + 3*x*z**5/2 + y*z**5/3 - z**6/2; u_7=-z**7
- isolation: μ=∞ (над ℂ не изолирована); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['COMP 1 dim=1 : x^2+y^2,z', 'COMP 2 dim=0 : 17920*z^10+171601920*z^9+411409772928*z^8+2638513927296*z^7+2738029035924*z^6+13355348887584*z^5+594829235448*z^4-3078559368099*z^3-6361231931712*z^2+1006274321856*z-19681740288,2185542434581737862654483142079191017809904640*z^9+20928942268167157353313451161611531445939590831360*z^8+50177777124525388706070258126795768946705009593457536*z^7+326111670558272848292759614825131461102876520798607680*z^6+365223898911120904208982657075871142576148321260026440*z^5+1681560080771034312558113125308131428586885373180495318*z^4+216348029684789791949320552408529126314988138779939848*z^3-334320124237997206281537699518913458127344658178181826*z^2+776274919376144746410082228671486344310728633054660367*y-825821664857432064763586343849719159030743707778565112*z+27857910605458359866755733806998676991344584180795072,114994703912835550663625188293680208119974400*z^9+1101167277392778131489651215526372512600652175360*z^8+2639853255508979753440505352905719935789911207385600*z^7+16427366307452331760994919829939985919676395271880064*z^6+16642868640070796520871241485111844818897752599710380*z^5+98519767384650943645598953066756786411293586489198416*z^4-10646694656050749341566563096187385238846298899198408*z^3-10064081050612398749827829416851178577921895571842255*z^2+110896417053734963772868889810212334901532661864951481*x-53404167477683606557809075052738884277555873676132757*z-982431794548295845507867843492380110228462573291424']
- not a minimum: луч w=(-4, -3, 5): U(tw) = -84375/2·t^6 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=True ['Hess u_m != 0 on {x**2 + y**2 - z**2=0} (rank 1 = n-1-s): Morse-Bott']; B3=False ['u_{m+1} == 0']; l2=6
- naive restriction to the conic gutter (first form not vanishing identically on it): [{'degree': 6, 'zero': False, 'const': '-1/6', 'factors': [('3*t + 1', 2, 1), ('33*t**2 - 2*t - 15', 1, 2), ('5*t**2 + 6*t + 5', 4, 0)], 'deg_in_t': 12, 'inf_order': 0}]
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (1, 1, 1), d=4, face has 6 monomials, tail wdeg_min=6: principal part no certificate of absence of real critical points
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — u_6 has real zeros on {x**2 + y**2 - z**2=0} (or inconclusive): ideal saturation not the unit ideal
  - **ThmB**: no — (B3) fails: u_{m+1} == 0
  - **N13***: no — W_6|gutter has a multiple zero at w=(-1, 0, -1) (exact): not a regular value
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines: plane [0, 0, 1]: no; line [0, 1, 0]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'plane', 'normal': [0, 0, 1], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'line', 'verdict': 'info', 'note': 'chart (1, pb, pc): family of invariant lines lying in a plane (linear:pc); that plane is tested by the plane search'}, {'kind': 'line', 'direction': [0, 1, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}]
- covered by known: []; ours: []; soft: []; NOT COVERED: True; (39.6 s)

## A3: Q^2 + effective potential, triple zero

- U = `x**4 + 2*x**2*y**2 - 2*x**2*z**2 + x*y**3*z**2/2 + y**4 + y**3*z**3 - 2*y**2*z**2 + y*z**6 + z**7 + z**4`
- why: G = sin^3 f (1+cos f/2): triple zeros (sign change with vanishing slope) at f = 0, pi; W_7 = z^7 resolves isolation; no symmetry
- lowest degree m = 4; forms: u_4=x**4 + 2*x**2*y**2 - 2*x**2*z**2 + y**4 - 2*y**2*z**2 + z**4; u_6=x*y**3*z**2/2 + y**3*z**3; u_7=y*z**6 + z**7
- isolation: μ=∞ (над ℂ не изолирована); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['(primary decomposition skipped: TimeoutExpired)']
- not a minimum: луч w=(-4, -3, 5): U(tw) = -2025·t^6 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=True ['Hess u_m != 0 on {x**2 + y**2 - z**2=0} (rank 1 = n-1-s): Morse-Bott']; B3=False ['u_{m+1} == 0']; l2=6
- naive restriction to the conic gutter (first form not vanishing identically on it): [{'degree': 6, 'zero': False, 'const': '1', 'factors': [('t + 3', 3, 1), ('3*t + 1', 3, 1), ('3*t**2 + 6*t + 7', 1, 0), ('5*t**2 + 6*t + 5', 2, 0)], 'deg_in_t': 12, 'inf_order': 0}]
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (1, 1, 1), d=4, face has 6 monomials, tail wdeg_min=6: principal part no certificate of absence of real critical points
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — u_6 has real zeros on {x**2 + y**2 - z**2=0} (or inconclusive): ideal saturation not the unit ideal
  - **ThmB**: no — (B3) fails: u_{m+1} == 0
  - **N13***: no — W_6|gutter has a multiple zero at w=(-1, 0, -1) (exact): not a regular value
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines: plane [0, 0, 1]: no; line [0, 1, 0]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'plane', 'normal': [0, 0, 1], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'line', 'verdict': 'info', 'note': 'chart (1, pb, pc): family of invariant lines lying in a plane (linear:pc); that plane is tested by the plane search'}, {'kind': 'line', 'direction': [0, 1, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}]
- covered by known: []; ours: []; soft: []; NOT COVERED: True; (52.6 s)

## A4: Q^2 + effective potential >= 0 with double zero, thin horn only from W_7

- U = `x**4 + 2*x**2*y**2 - 2*x**2*z**2 - x*y*z**4/2 - x*z**5 + y**4 - 2*y**2*z**2 + y*z**5/2 - z**7 + z**6 + z**4`
- why: G = (1-cos f)(1+sin f/2) >= 0 with a double zero at f=0: negative values only in a horn of angular width ~ r^(1/2) around the ray (1,0,1), where U = -t^7
- lowest degree m = 4; forms: u_4=x**4 + 2*x**2*y**2 - 2*x**2*z**2 + y**4 - 2*y**2*z**2 + z**4; u_6=-x*y*z**4/2 - x*z**5 + y*z**5/2 + z**6; u_7=-z**7
- isolation: μ=∞ (над ℂ не изолирована); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['COMP 1 dim=1 : x^2+y^2,z', 'COMP 2 dim=0 : 7*z^10+1568*z^9+133112*z^8+4998720*z^7+64741733*z^6-226674560*z^5+223331360*z^4-117156544*z^3+110380032*z^2-48559104*z+9289728,25649315811777632134814787*z^9+5753030727142008251327475852*z^8+489445419916964558127088618568*z^7+18459971031573091192011893005344*z^6+242572371294462841512897898123545*z^5-764170562954599580139014124996988*z^4+501770266302396826756259616981712*z^3-161937270112892903249750191901888*z^2+181026652834332152586597942141312*y+332929783008143527886607189717504*z-33194097287566509655060966490112,2311128761008512271717604*z^9+518446156108703893711094895*z^8+44118994685748973601399123972*z^7+1665099866707220444586562104376*z^6+21944921580009431272959570037664*z^5-66729222590381337149398419072259*z^4+64113330692328975387607218222772*z^3-29758388965339527391790700202912*z^2+22628331604291519073324742767664*x+26468835056893474163037243388944*z-12650918904085459920224496509952']
- not a minimum: луч w=(1, 0, 1): U(tw) = -1·t^7 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=True ['Hess u_m != 0 on {x**2 + y**2 - z**2=0} (rank 1 = n-1-s): Morse-Bott']; B3=False ['u_{m+1} == 0']; l2=6
- naive restriction to the conic gutter (first form not vanishing identically on it): [{'degree': 6, 'zero': False, 'const': '2', 'factors': [('t**2 + t + 1', 1, 0), ('t**2 + 1', 4, 0)], 'deg_in_t': 10, 'inf_order': 2}]
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (1, 1, 1), d=4, face has 6 monomials, tail wdeg_min=6: principal part no certificate of absence of real critical points
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — u_6 has real zeros on {x**2 + y**2 - z**2=0} (or inconclusive): ideal saturation not the unit ideal
  - **ThmB**: no — (B3) fails: u_{m+1} == 0
  - **N13***: no — W_6|gutter has a multiple zero at w=(-1, 0, -1) (exact): not a regular value
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines: plane [0, 0, 1]: no; line [0, 1, 0]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'plane', 'normal': [0, 0, 1], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'line', 'verdict': 'info', 'note': 'chart (1, pb, pc): family of invariant lines lying in a plane (linear:pc); that plane is tested by the plane search'}, {'kind': 'line', 'direction': [0, 1, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}]
- covered by known: []; ours: []; soft: []; NOT COVERED: True; (39.1 s)

## A5: Q^2 + odd W_5 with a double zero on the gutter

- U = `x**4 + 2*x**2*y**2 - 2*x**2*z**2 + x*y*z**3/2 + x*z**4 + y**4 - 2*y**2*z**2 - y*z**4/2 + z**6 - z**5 + z**4`
- why: W_5|gutter = (cos f - 1)(1+ sin f/2) z^5: not a regular value (touching zero), so B3 fails; next form W_6 = z^6
- lowest degree m = 4; forms: u_4=x**4 + 2*x**2*y**2 - 2*x**2*z**2 + y**4 - 2*y**2*z**2 + z**4; u_5=x*y*z**3/2 + x*z**4 - y*z**4/2 - z**5; u_6=z**6
- isolation: μ=∞ (над ℂ не изолирована); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['(primary decomposition skipped: TimeoutExpired)']
- not a minimum: луч w=(4, 3, 5): U(tw) = -1625/2·t^5 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=True ['Hess u_m != 0 on {x**2 + y**2 - z**2=0} (rank 1 = n-1-s): Morse-Bott']; B3=False ['g = u_5|{x**2 + y**2 - z**2=0} has a MULTIPLE zero at w=(-1, 0, -1): f=h=0 and dh|T = 0 there (exact)']; l2=5
- naive restriction to the conic gutter (first form not vanishing identically on it): [{'degree': 5, 'zero': False, 'const': '-1/2', 'factors': [('t - 3', 2, 1), ('7*t**2 - 2*t + 7', 1, 0), ('5*t**2 - 6*t + 5', 3, 0)], 'deg_in_t': 10, 'inf_order': 0}]
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (1, 1, 1), d=4, face has 6 monomials, tail wdeg_min=5: principal part no certificate of absence of real critical points
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — l2 = 5 odd and Sigma = -Sigma: u_5(-w) = -u_5(w), so u_5 < 0 on all of Sigma is impossible
  - **ThmB**: no — (B3) fails: g = u_5|{x**2 + y**2 - z**2=0} has a MULTIPLE zero at w=(-1, 0, -1): f=h=0 and dh|T = 0 there (exact)
  - **N13***: no — W_5|gutter has a multiple zero at w=(-1, 0, -1) (exact): not a regular value
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines: plane [0, 0, 1]: no; line [0, 1, 0]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'plane', 'normal': [0, 0, 1], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'line', 'verdict': 'info', 'note': 'chart (1, pb, pc): family of invariant lines lying in a plane (linear:pc); that plane is tested by the plane search'}, {'kind': 'line', 'direction': [0, 1, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}]
- covered by known: []; ours: []; soft: []; NOT COVERED: True; (46.1 s)

## A6: Example 13 rotated by a rational rotation

- U = `534227517444897*x**6/3640857352728781250 - 3770863505530488*x**5*y/1820428676364390625 - 484988464417023*x**5*z/364085735272878125 + 1186100771200092*x**4*y**2/364085735272878125 + 1571814524540709*x**4*y*z/72817147054575625 + 52300938240036*x**4*z**2/14563429410915125 + 1300108489729*x**4/1490902050625 + 27432333933820992*x**3*y**3/364085735272878125 - 9025998084576144*x**3*y**2*z/72817147054575625 - 687302340266592*x**3*y*z**2/14563429410915125 + 1958155127712*x**3*y/1490902050625 - 2327861567232*x**3*z**3/582537176436605 + 14667828672*x**3*z/59636082025 - 145582590003086592*x**2*y**4/364085735272878125 + 23126976256054752*x**2*y**3*z/72817147054575625 + 2992986299625984*x**2*y**2*z**2/14563429410915125 - 1680463695874*x**2*y**2/1490902050625 + 19255260640128*x**2*y*z**3/582537176436605 - 66890565888*x**2*y*z/59636082025 + 181790891520*x**2*z**4/116507435287321 + 105116101486*x**2*z**2/59636082025 + 800217915729472512*x*y**5/1820428676364390625 - 37875603650462208*x*y**4*z/72817147054575625 - 4976175526967808*x*y**3*z**2/14563429410915125 - 1820767607712*x*y**3/1490902050625 - 31252120495104*x*y**2*z**3/582537176436605 - 72330657216*x*y**2*z/59636082025 - 59626526720*x*y*z**4/116507435287321 + 67390295904*x*y*z**2/59636082025 + 32914944000*x*z**5/116507435287321 + 587125824*x*z**3/2385443281 + 955424534693796864*y**6/1820428676364390625 + 301350881059985664*y**5*z/364085735272878125 + 3356460480347136*y**4*z**2/14563429410915125 + 1124072809729*y**4/1490902050625 - 28362586392576*y**3*z**3/582537176436605 + 72468362496*y**3*z/59636082025 - 3631841771520*y**2*z**4/116507435287321 - 67579301486*y**2*z**2/59636082025 - 566574592000*y*z**5/116507435287321 - 3119653632*y*z**3/2385443281 - 29440000000*z**6/116507435287321 + 2083100881*z**4/2385443281`
- why: the same system in rotated orthonormal coordinates: tests that detection does not rely on the axis being z
- lowest degree m = 4; forms: u_4=1300108489729*x**4/1490902050625 + 1958155127712*x**3*y/1490902050625 + 14667828672*x**3*…; u_6=534227517444897*x**6/3640857352728781250 - 3770863505530488*x**5*y/1820428676364390625 - …
- isolation: μ=∞ (над ℂ не изолирована); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['COMP 1 dim=0 : 284592003781306556354765824*z^10-35257771272990638856672434688*z^8+716251637181367862758719240939*z^6-4601023925048752781930211624204*z^4+272904230214564821717473336032*z^2-62982451043731826427336093504,516009351916394173931875151676715943731934154969835800653333000899500882944*z^9-63869376901226786634134101313018144626359984307507889640741873276388030649856*z^7+1291851935002172119055133222301072825100557462789697704842623907444433673849821*z^5-8241220522733130667998461548460076263352403746482121437052699608800115061022644*z^3+282840235418644745470787966445687205343462548046195694115719383246348669704560*y-111094222739042290908181051086444894688525227338587895209524064780049756765376*z,-822336289425091966181774415010350125858763022246576459243359610205290753024*z^9+102037770688405267093354181169078260790638749848685227307835896120347840830976*z^7-2088115787268361503674846527221644384142051040226032681723180963199098759629441*z^5+13539840313443104560442831300372904854666380886170195900111293999909621184485024*z^3+848520706255934236412363899337061616030387644138587082347158149739046009113680*x-623706569887775674228216478640699735362838548024166832456245773376671667573504*z', 'COMP 2 dim=1 : 1181025*y^2+427200*y*z+80401*z^2,201*x-1068*y-200*z']
- not a minimum: луч w=(-4113, 5609, -3560): U(tw) = -44372948986382021484375/2·t^6 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=True ['Hess u_m != 0 on {1140223*x**2/1221025 + 858672*x*y/1221025 + 6432*x*z/48841 - 1060223*y**2/1221025 - 34176*y*z/48841 + 45641*z**2/48841=0} (rank 1 = n-1-s): Morse-Bott']; B3=False ['u_{m+1} == 0']; l2=6
- naive restriction to the conic gutter (first form not vanishing identically on it): [{'degree': 6, 'zero': False, 'const': '1/3640857352728781250', 'factors': [('5530541*t**2 + 9632560*t + 7929125', 4, 0), ('84868977506681*t**4 + 186607120585640*t**3 + 169142366269650*t**2 + 153270812744000*t + 62863298905625', 1, 2)], 'deg_in_t': 12, 'inf_order': 0}]
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (1, 1, 1), d=4, face has 15 monomials, tail wdeg_min=6: principal part has real critical points (exact)
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — u_6 has real zeros on {1140223*x**2/1221025 + 858672*x*y/1221025 + 6432*x*z/48841 - 1060223*y**2/1221025 - 34176*y*z/48841 + 45641*z**2/48841=0} (or inconclusive): ideal saturation not the unit ideal
  - **ThmB**: no — (B3) fails: u_{m+1} == 0
  - **N13***: yes — circular 45-degree cone, W_6 simple zeros, negative at the gutter point (-4113, 5609, -3560) [Эскиз, 003 Prop. 1]
  - **N13**: yes — U = c * U_13(R q) with R orthogonal (exact identity): Theorem 1 of 003 [Доказано, R8]
  - **SYM**: no — exact search of ALL invariant planes and lines: plane [-201, 1068, 200]: no; line [0, 50, -267]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'plane', 'normal': [-201, 1068, 200], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'line', 'verdict': 'info', 'note': 'chart (1, pb, pc): family of invariant lines lying in a plane (linear:1068*pb + 200*pc - 201); that plane is tested by the plane search'}, {'kind': 'line', 'direction': [0, 50, -267], 'verdict': 'no', 'note': 'U on the line = 5444816521 t^4 + ...'}]
- covered by known: []; ours: ['N13']; soft: ['N13*']; NOT COVERED: False; (48.0 s)

## A7: m=6: Q^2 (x^2+y^2+z^2) + W_8

- U = `x**6 + 3*x**4*y**2 - x**4*z**2 + 3*x**2*y**4 - 2*x**2*y**2*z**2 - x**2*z**4 + x*y*z**6 + x*z**7 + y**6 - y**4*z**2 - y**2*z**4 + z**8/2 + z**6`
- why: u_6 = Q^2 |q|^2: gutter = circle, u_7 = 0, W_8 = Example-13 type potential; the Example-13 criterion is stated for u_4 = Q^2 only
- lowest degree m = 6; forms: u_6=x**6 + 3*x**4*y**2 - x**4*z**2 + 3*x**2*y**4 - 2*x**2*y**2*z**2 - x**2*z**4 + y**6 - y**4…; u_8=x*y*z**6 + x*z**7 + z**8/2
- isolation: μ=∞ (над ℂ не изолирована); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['COMP 1 dim=1 : x^2+y^2,z', 'COMP 2 dim=0 : 531441*z^18-104398632*z^16+4930769376*z^14-56199992832*z^12-393480962048*z^10-1252557455360*z^8-2298564575232*z^6-2638619869184*z^4-1777042718720*z^2-592705486848,-622269552025476063362487791889*z^17+123233056603950618382885732041696*z^15-5969100572676214684357794744734496*z^13+75164277782686344145116989711051520*z^11+348415898574620183021618079715557376*z^9+815374630026360364628245814319120384*z^7+992773747183528813092248231948058624*z^5+652376335936370938465686688947503104*z^3+103664114152249244643763017121529856*y+162221413872812824703572780957827072*z,-738595547864046537737827190967*z^17+144694009356758532936643184744184*z^15-6771750490378047731592987253541664*z^13+73881261530484941950914904930285056*z^11+614398150382854209866423906890915840*z^9+1717798188027052108615596469978398720*z^7+2637808060006209291549906138443022336*z^5+1922030118537547917507871889950769152*z^3+414656456608996978575052068486119424*x+584100136834777089277314189974568960*z']
- not a minimum: луч w=(-4, 3, 5): U(tw) = -609375/2·t^8 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=True ['Hess u_m != 0 on {x**2 + y**2 - z**2=0} (rank 1 = n-1-s): Morse-Bott']; B3=False ['u_{m+1} == 0']; l2=8
- naive restriction to the conic gutter (first form not vanishing identically on it): [{'degree': 8, 'zero': False, 'const': '1/2', 'factors': [('5*t**2 - 6*t + 5', 6, 0), ('9*t**4 - 92*t**3 + 86*t**2 - 28*t + 41', 1, 2)], 'deg_in_t': 16, 'inf_order': 0}]
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_6 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_6 >= 0 vanishes at nonzero points, which are critical points of u_6 (grad u_6 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (1, 1, 1), d=6, face has 10 monomials, tail wdeg_min=8: principal part no certificate of absence of real critical points
  - **Bu25-P1.2**: no — f = u_6|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — u_8 has real zeros on {x**2 + y**2 - z**2=0} (or inconclusive): ideal saturation not the unit ideal
  - **ThmB**: no — (B3) fails: u_{m+1} == 0
  - **N13***: no — u_4 is not of the form c Q^2
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines: plane [0, 0, 1]: no; line [0, 1, 0]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'plane', 'normal': [0, 0, 1], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'line', 'verdict': 'info', 'note': 'chart (1, pb, pc): family of invariant lines lying in a plane (linear:pc); that plane is tested by the plane search'}, {'kind': 'line', 'direction': [0, 1, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^6 + ...'}]
- covered by known: []; ours: []; soft: []; NOT COVERED: True; (37.6 s)

## C1: elliptic cone, simple zeros of the effective potential

- U = `x**4 + 4*x**2*y**2 - 2*x**2*z**2 + x*y*z**4 + x*z**5 + 4*y**4 - 4*y**2*z**2 + z**6/2 + z**4`
- why: gutter = ellipse; not circular, so the Example-13 construction is not stated for it
- lowest degree m = 4; forms: u_4=x**4 + 4*x**2*y**2 - 2*x**2*z**2 + 4*y**4 - 4*y**2*z**2 + z**4; u_6=x*y*z**4 + x*z**5 + z**6/2
- isolation: μ=∞ (над ℂ не изолирована); над ℝ: насыщение J:p^∞, p=x**2 + 2*y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['COMP 1 dim=1 : x^2+2*y^2,z', 'COMP 2 dim=0 : 3*z^10-140*z^8-462*z^6-128808*z^4-371520*z^2-393984,-64851*z^9+3811018*z^7-16274670*z^5+2253892140*z^3+26403496992*y+3369948624*z,113649*z^9-5414836*z^7-9337690*z^5-5576544072*z^3+17602331328*x-3208606272*z']
- not a minimum: луч w=(-1, 0, 1): U(tw) = -1/2·t^6 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=True ['Hess u_m != 0 on {x**2 + 2*y**2 - z**2=0} (rank 1 = n-1-s): Morse-Bott']; B3=False ['u_{m+1} == 0']; l2=6
- naive restriction to the conic gutter (first form not vanishing identically on it): [{'degree': 6, 'zero': False, 'const': '-1/2', 'factors': [('2*t**2 + 1', 4, 0), ('4*t**4 + 8*t**3 - 4*t**2 - 4*t - 3', 1, 2)], 'deg_in_t': 12, 'inf_order': 0}]
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (1, 1, 1), d=4, face has 6 monomials, tail wdeg_min=6: principal part no certificate of absence of real critical points
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — u_6 has real zeros on {x**2 + 2*y**2 - z**2=0} (or inconclusive): ideal saturation not the unit ideal
  - **ThmB**: no — (B3) fails: u_{m+1} == 0
  - **N13***: no — u_4 = c Q^2 but the cone Q=0 is not circular with aperture 90 degrees: eigenvalues of Q: [(1, 1), (2, 1), (-1, 1)]
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines: plane [0, 0, 1]: no; line [1, 0, 0]: no; line [0, 1, 0]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'plane', 'normal': [0, 0, 1], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'line', 'direction': [1, 0, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}, {'kind': 'line', 'direction': [0, 1, 0], 'verdict': 'no', 'note': 'U on the line = 4 t^4 + ...'}]
- covered by known: []; ours: []; soft: []; NOT COVERED: True; (35.5 s)

## C2: circular cone with aperture != 90 degrees

- U = `x**4 + 2*x**2*y**2 - 4*x**2*z**2 + x*y*z**4 + x*z**5 + y**4 - 4*y**2*z**2 + z**6/2 + 4*z**4`
- why: cone x^2+y^2=2z^2: circular but not the 45-degree cone of Example 13
- lowest degree m = 4; forms: u_4=x**4 + 2*x**2*y**2 - 4*x**2*z**2 + y**4 - 4*y**2*z**2 + 4*z**4; u_6=x*y*z**4 + x*z**5 + z**6/2
- isolation: μ=∞ (над ℂ не изолирована); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['COMP 1 dim=1 : x^2+y^2,z', 'COMP 2 dim=0 : 12*z^10-272*z^8+4017*z^6-5076*z^4-184464*z^2-1223424,1245900*z^9-7734656*z^7-28770927*z^5+4528316376*z^3+51433662096*y+24268797504*z,499740*z^9-22092304*z^7+238080285*z^5-4711014252*z^3+51433662096*x-4745792160*z']
- not a minimum: луч w=(-7, -1, 5): U(tw) = -19375/2·t^6 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=True ['Hess u_m != 0 on {x**2 + y**2 - 2*z**2=0} (rank 1 = n-1-s): Morse-Bott']; B3=False ['u_{m+1} == 0']; l2=6
- naive restriction to the conic gutter (first form not vanishing identically on it): [{'degree': 6, 'zero': False, 'const': '-1/2', 'factors': [('5*t**2 + 2*t + 10', 4, 0), ('59*t**4 + 288*t**3 - 104*t**2 - 656*t - 436', 1, 2)], 'deg_in_t': 12, 'inf_order': 0}]
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (1, 1, 1), d=4, face has 6 monomials, tail wdeg_min=6: principal part no certificate of absence of real critical points
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — u_6 has real zeros on {x**2 + y**2 - 2*z**2=0} (or inconclusive): ideal saturation not the unit ideal
  - **ThmB**: no — (B3) fails: u_{m+1} == 0
  - **N13***: no — u_4 = c Q^2 but the cone Q=0 is not circular with aperture 90 degrees: eigenvalues of Q: [(1, 2), (-2, 1)]
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines: plane [0, 0, 1]: no; line [0, 1, 0]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'plane', 'normal': [0, 0, 1], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'line', 'verdict': 'info', 'note': 'chart (1, pb, pc): family of invariant lines lying in a plane (linear:pc); that plane is tested by the plane search'}, {'kind': 'line', 'direction': [0, 1, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}]
- covered by known: []; ours: []; soft: []; NOT COVERED: True; (36.9 s)

## C3: elliptic cone, odd W_5 (Theorem B territory)

- U = `x**4 + 4*x**2*y**2 - 2*x**2*z**2 + x*z**4 + 4*y**4 - 4*y**2*z**2 + 3*y*z**4 + z**6 + z**4`
- why: gutter ellipse, u_5 regular on it: Theorem B applies, no symmetry
- lowest degree m = 4; forms: u_4=x**4 + 4*x**2*y**2 - 2*x**2*z**2 + 4*y**4 - 4*y**2*z**2 + z**4; u_5=x*z**4 + 3*y*z**4; u_6=z**6
- isolation: μ=∞ (над ℂ не изолирована); над ℝ: насыщение J:p^∞, p=x**2 + 2*y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['COMP 1 dim=1 : x^2+2*y^2,z', 'COMP 2 dim=0 : 108*z^4-632*z^2-275,18*z^2+56*y+15,3*x-2*y']
- not a minimum: луч w=(-1, -2, -3): U(tw) = -567·t^5 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=True ['Hess u_m != 0 on {x**2 + 2*y**2 - z**2=0} (rank 1 = n-1-s): Morse-Bott']; B3=True ['0 regular value of u_5 on {x**2 + 2*y**2 - z**2=0} (ideal (f,h,det[grad h,grad f,q]) has no real nonzero zero)']; l2=5
- naive restriction to the conic gutter (first form not vanishing identically on it): [{'degree': 5, 'zero': False, 'const': '1', 'factors': [('10*t**2 - 18*t + 7', 1, 2), ('6*t**2 - 8*t + 3', 4, 0)], 'deg_in_t': 10, 'inf_order': 0}]
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (1, 1, 1), d=4, face has 6 monomials, tail wdeg_min=5: principal part no certificate of absence of real critical points
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — l2 = 5 odd and Sigma = -Sigma: u_5(-w) = -u_5(w), so u_5 < 0 on all of Sigma is impossible
  - **ThmB**: yes — B1 (Sigma smooth submanifold), B2 (Morse-Bott), B3 (0 regular value of u_{m+1}|Sigma): Hess u_m != 0 on {x**2 + 2*y**2 - z**2=0} (rank 1 = n-1-s): Morse-Bott | 0 regular value of u_5 on {x**2 + 2*y**2 - z**2=0} (ideal (f,h,det[grad h,grad f,q]) has no real nonzero zero)
  - **N13***: no — u_4 = c Q^2 but the cone Q=0 is not circular with aperture 90 degrees: eigenvalues of Q: [(1, 1), (2, 1), (-1, 1)]
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines: plane [0, 0, 1]: no; line [1, 0, 0]: no; line [0, 1, 0]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'plane', 'normal': [0, 0, 1], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'line', 'direction': [1, 0, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}, {'kind': 'line', 'direction': [0, 1, 0], 'verdict': 'no', 'note': 'U on the line = 4 t^4 + ...'}]
- covered by known: []; ours: ['ThmB']; soft: []; NOT COVERED: False; (36.5 s)

## D1: gutter to be searched: (Q - z m)^2 - z^8

- U = `x**4*z**2 - 2*x**4*z + x**4 + 4*x**3*y*z**2 - 4*x**3*y*z + 6*x**3*z**3 - 6*x**3*z**2 + 4*x**2*y**2*z**2 - 2*x**2*y**2*z + 2*x**2*y**2 + 12*x**2*y*z**3 + 9*x**2*z**4 + 2*x**2*z**3 - 2*x**2*z**2 - 4*x*y**3*z - 6*x*y**2*z**2 + 4*x*y*z**3 + 6*x*z**4 + y**4 - 2*y**2*z**2 - z**8 + z**4`
- why: m = x(x+2y)+3xz (m must involve z and be non-axial, otherwise principal axes of m give invariant planes). U_5 = -2 Q z m, U_6 = z^2 m^2 vanish/are >= 0 on the cone; negativity lives on the DEFORMED cone Q = z m (U = -z^8 there)
- lowest degree m = 4; forms: u_4=x**4 + 2*x**2*y**2 - 2*x**2*z**2 + y**4 - 2*y**2*z**2 + z**4; u_5=-2*x**4*z - 4*x**3*y*z - 6*x**3*z**2 - 2*x**2*y**2*z + 2*x**2*z**3 - 4*x*y**3*z - 6*x*y**…; u_6=x**4*z**2 + 4*x**3*y*z**2 + 6*x**3*z**3 + 4*x**2*y**2*z**2 + 12*x**2*y*z**3 + 9*x**2*z**4; u_8=-z**8
- isolation: μ=∞ (над ℂ не изолирована); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['COMP 1 dim=1 : x^2+y^2,z', 'COMP 2 dim=0 : 64*z^10+192*z^9-320*z^7-50*z^6+177*z^5+80*z^4-236*z^3+216*z^2-96*z+32,-704*z^12-2560*z^11-1600*z^10+2560*z^9+2150*z^8-637*z^7-1279*z^6+1798*z^5-1205*z^4+171*z^3+270*y,-1152*z^12-4160*z^11-2560*z^10+4160*z^9+3460*z^8-1036*z^7-2077*z^6+2969*z^5-2090*z^4+523*z^3-405*z^2+270*x']
- not a minimum: кривая γ(τ)=(415*tau**4/64 + 165*tau**3/32 + 5*tau…, 3*tau/5, tau): U(γ) = -1·τ^8 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=True ['Hess u_m != 0 on {x**2 + y**2 - z**2=0} (rank 1 = n-1-s): Morse-Bott']; B3=False ['u_5 == 0 on {x**2 + y**2 - z**2=0}']; l2=5
- naive restriction to the conic gutter (first form not vanishing identically on it): [{'degree': 5, 'zero': True}, {'degree': 6, 'zero': False, 'const': '16', 'factors': [('t - 1', 2, 1), ('t + 1', 2, 1), ('5*t**2 - 6*t + 5', 2, 0), ('13*t**2 + 2*t + 5', 2, 0)], 'deg_in_t': 12, 'inf_order': 0}]
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (1, 1, 1), d=4, face has 6 monomials, tail wdeg_min=5: principal part no certificate of absence of real critical points
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — l2 = 5 odd and Sigma = -Sigma: u_5(-w) = -u_5(w), so u_5 < 0 on all of Sigma is impossible
  - **ThmB**: no — (B3) fails: u_5 == 0 on {x**2 + y**2 - z**2=0}
  - **N13***: no — W_5 vanishes identically on the gutter: effective potential is not W_5; G == 0
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines: line [2, -1, 0]: no; line [0, 1, 0]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'line', 'direction': [2, -1, 0], 'verdict': 'no', 'note': 'U on the line = 25 t^4 + ...'}, {'kind': 'line', 'direction': [0, 1, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}]
- covered by known: []; ours: []; soft: []; NOT COVERED: True; (36.6 s)

## D2: Example 13 on a deformed cone

- U = `x**4*z**2 - 2*x**4*z + x**4 + 4*x**3*y*z**2 - 4*x**3*y*z + 6*x**3*z**3 - 6*x**3*z**2 + 4*x**2*y**2*z**2 - 2*x**2*y**2*z + 2*x**2*y**2 + 12*x**2*y*z**3 + 9*x**2*z**4 + 2*x**2*z**3 - 2*x**2*z**2 - 4*x*y**3*z - 6*x*y**2*z**2 + x*y*z**4 + 4*x*y*z**3 + x*z**5 + 6*x*z**4 + y**4 - 2*y**2*z**2 + z**6/2 + z**4`
- why: Q replaced by Q - z m: the gutter is a curved surface, effective potential as in Example 13
- lowest degree m = 4; forms: u_4=x**4 + 2*x**2*y**2 - 2*x**2*z**2 + y**4 - 2*y**2*z**2 + z**4; u_5=-2*x**4*z - 4*x**3*y*z - 6*x**3*z**2 - 2*x**2*y**2*z + 2*x**2*z**3 - 4*x*y**3*z - 6*x*y**…; u_6=x**4*z**2 + 4*x**3*y*z**2 + 6*x**3*z**3 + 4*x**2*y**2*z**2 + 12*x**2*y*z**3 + 9*x**2*z**4…
- isolation: μ=∞ (над ℂ не изолирована); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['(primary decomposition skipped: TimeoutExpired)']
- not a minimum: кривая γ(τ)=(-731*tau**4/320 - 153*tau**3/160 + 17…, 3*tau/5, tau): U(γ) = -39/50·τ^6 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=True ['Hess u_m != 0 on {x**2 + y**2 - z**2=0} (rank 1 = n-1-s): Morse-Bott']; B3=False ['u_5 == 0 on {x**2 + y**2 - z**2=0}']; l2=5
- naive restriction to the conic gutter (first form not vanishing identically on it): [{'degree': 5, 'zero': True}, {'degree': 6, 'zero': False, 'const': '1/2', 'factors': [('5*t**2 - 6*t + 5', 2, 0), ('6433*t**8 - 1496*t**7 + 828*t**6 - 15016*t**5 + 13478*t**4 - 13928*t**3 + 11132*t**2 - 2200*t + 1025', 1, 0)], 'deg_in_t': 12, 'inf_order': 0}]
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (1, 1, 1), d=4, face has 6 monomials, tail wdeg_min=5: principal part no certificate of absence of real critical points
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — l2 = 5 odd and Sigma = -Sigma: u_5(-w) = -u_5(w), so u_5 < 0 on all of Sigma is impossible
  - **ThmB**: no — (B3) fails: u_5 == 0 on {x**2 + y**2 - z**2=0}
  - **N13***: no — W_5 vanishes identically on the gutter: effective potential is not W_5; G == 0
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines: line [2, -1, 0]: no; line [0, 1, 0]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'line', 'direction': [2, -1, 0], 'verdict': 'no', 'note': 'U on the line = 25 t^4 + ...'}, {'kind': 'line', 'direction': [0, 1, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}]
- covered by known: []; ours: []; soft: []; NOT COVERED: True; (44.5 s)

## F1: flat gutter z=0 with a linear term in z (effective potential by completing the square)

- U = `x**5*y + x**4*z + x**2*z**2 + 2*x*y**3*z + y**6 + y**2*z**2 + z**4`
- why: u_4 = z^2 |q|^2: gutter = equator; u_5 = z f_4 vanishes on it; G = W_6 - f_4^2/4 is not a polynomial restriction
- lowest degree m = 4; forms: u_4=x**2*z**2 + y**2*z**2 + z**4; u_5=x**4*z + 2*x*y**3*z; u_6=x**5*y + y**6
- isolation: μ=51 (Singular, локальный базис, конечен ⇒ изолирована и над ℂ); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['COMP 1 dim=0 : z,y,x', 'COMP 2 dim=0 : 5467500000000*z^12+10738170000000*z^10-7313716800000*z^9-882760194000*z^8+2034246936128*z^7-1753806857184*z^6+1016413046784*z^5-396129362328*z^4+214963205616*z^3-101098761984*z^2+22741359120*z-1803328029,-24482730496144951114149785953917880895457404404481960561542214657625000000000*z^11-8366577039776769257972118883663390524126932019694936479292015732192500000000*z^10-50829356989140903414205239404773670330355281463476694965091306766465500000000*z^9+15464088845524223029700124237971776209754273487318263088965546580638575000000*z^8+9508227390152607703716521399599523652383384457842442634969429618125771900000*z^7-5824243525145035511292110607239084520572457650982591763155859013993462585200*z^6+5833991255053086272317410971560017602410754102932273180868003691949513130112*z^5-2542810184728429391955627133963625408267891948039823131614591190563691905500*z^4+883870241500715381862391920200325252245902132334457819556358368236748930416*z^3+1836923822864729078100581353068197737671047446448583912799272096945281496*y^2-654290095212837188391707204003115102090101254752746485415321685057066562632*z^2+225385883582071219337156420407867570705765864805086518428359972063046711112*z-22944576421099152744477758225845802729406324860769475237573426315865583333,-29837698349127852370878471454477964126040909190700766523634071463671875000000*y*z^11-14654273419025351564395765626290416740301131614788027894484105666036250000000*y*z^10-64591484565509615142656986895847579799447414632616928473603501764263437500000*y*z^9+8884060966797030747828198143374669536760941407170984744700482566431805000000*y*z^8+11856128241736920416011135221143755632742143787287958772586525822377624362500*y*z^7-5409100247929923162054439071223329954682579863017239038835823899577405171000*y*z^6+6435428626076611805790964419701265323685193806677020014991095957472482120612*y*z^5-2203472354579642776922612586476157049517385642597404097279337078947861356280*y*z^4+834396979770738328560798747302525132575360731111533921420012512384664627271*y*z^3-694425283008666594814080143550699645769455234477089653799887193953902807060*y*z^2+181348316444756606727834378945564409527464388707057938240842043360412637864*y*z+459230955716182269525145338267049434417761861612145978199818024236320374*x-9088548379070964913419503812684098153123640762699935435282773408544659412*y']
- not a minimum: луч w=(-7, 1, 0): U(tw) = -16806·t^6 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=True ['Hess u_m != 0 on {z=0} (rank 1 = n-1-s): Morse-Bott']; B3=False ['u_5 == 0 on {z=0}']; l2=5
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (1, 1, 1), d=4, face has 3 monomials, tail wdeg_min=5: principal part has real critical points (exact); weights (1, 1, 2), d=6, face has 6 monomials, tail wdeg_min=8: principal part has real critical points (exact)
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — l2 = 5 odd and Sigma = -Sigma: u_5(-w) = -u_5(w), so u_5 < 0 on all of Sigma is impossible
  - **ThmB**: no — (B3) fails: u_5 == 0 on {z=0}
  - **N13***: no — u_4 is not c Q^2 with a quadratic form Q
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines: line [0, 1, 0]: no; line [0, 0, 1]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'line', 'direction': [0, 1, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^6 + ...'}, {'kind': 'line', 'direction': [0, 0, 1], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}]
- covered by known: []; ours: []; soft: []; NOT COVERED: True; (72.0 s)

## M1: (z - x^2)^4 + x^5 + y^5

- U = `x**8 + x**6*y - 4*x**6*z + x**5 + 6*x**4*z**2 - 4*x**2*z**3 + x*y**6 + y**5 + z**4`
- why: gutter z=0 of multiplicity 4, quasi-homogeneous only after the non-linear change z -> z - x^2; negativity along a PARABOLA
- lowest degree m = 4; forms: u_4=z**4; u_5=x**5 - 4*x**2*z**3 + y**5; u_6=6*x**4*z**2; u_7=x**6*y - 4*x**6*z + x*y**6; u_8=x**8
- isolation: μ=48 (Singular, локальный базис, конечен ⇒ изолирована и над ℂ); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['COMP 1 dim=0 : z,y,x', 'COMP 2 dim=0 : z-1,y-1,x+1', 'COMP 3 dim=0 : z-1,y+1,x-1', 'COMP 4 dim=0 : 7*z+5,7*y^2+5,x-y', 'COMP 5 dim=0 : z^4+z^3+z^2+z+1,z^2+y,-z^3+x', 'COMP 6 dim=0 : z^4+z^3+z^2+z+1,-z^2+y,z^3+x', 'COMP 7 dim=0 : 2401*z^4-1715*z^3+1225*z^2-875*z+625,343*z^3+175*y^2-245*z^2+175*z-125,7*y*z+5*x']
- not a minimum: луч w=(-7, -6, 0): U(tw) = -24583·t^5 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=False ['Hess u_m == 0 on {z=0} (multiplicity >= 4: degenerate)']; B3=True ['0 regular value of u_5 on {z=0} (ideal (f,h,det[grad h,grad f,q]) has no real nonzero zero)']; l2=5
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (4, 4, 5), d=20, face has 3 monomials, tail wdeg_min=23: principal part is fine but the tail is TOO LARGE (23 < d + a_min=24)
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — l2 = 5 odd and Sigma = -Sigma: u_5(-w) = -u_5(w), so u_5 < 0 on all of Sigma is impossible
  - **ThmB**: no — (B2) fails: Hess u_m == 0 on {z=0} (multiplicity >= 4: degenerate)
  - **N13***: no — u_4 is not c Q^2 with a quadratic form Q
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines: line [0, 0, 1]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'line', 'direction': [0, 0, 1], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}]
- covered by known: []; ours: []; soft: []; NOT COVERED: True; (4.7 s)

## M2: z^4 + z (x^4+y^4) + x^6 : quasi-homogeneous principal part, tail in the gap

- U = `x**6 + x**4*z + x**3*y*z + x*z**5 + y**4*z + 2*y*z**5 + z**4`
- why: principal part (weights 3,3,4) has no critical points, but the tail x^6 has weighted degree 18 < d + a_min = 19
- lowest degree m = 4; forms: u_4=z**4; u_5=x**4*z + x**3*y*z + y**4*z; u_6=x**6 + x*z**5 + 2*y*z**5
- isolation: μ=59 (Singular, локальный базис, конечен ⇒ изолирована и над ℂ); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['(primary decomposition skipped: TimeoutExpired)']
- not a minimum: кривая γ(τ)=(tau**3, 0, -tau**4/2): U(γ) = -7/16·τ^16 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=False ['Hess u_m == 0 on {z=0} (multiplicity >= 4: degenerate)']; B3=False ['u_5 == 0 on {z=0}']; l2=5
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (3, 3, 4), d=16, face has 4 monomials, tail wdeg_min=18: principal part is fine but the tail is TOO LARGE (18 < d + a_min=19); weights (1, 1, 2), d=6, face has 4 monomials, tail wdeg_min=8: principal part has real critical points (exact)
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — l2 = 5 odd and Sigma = -Sigma: u_5(-w) = -u_5(w), so u_5 < 0 on all of Sigma is impossible
  - **ThmB**: no — (B2) fails: Hess u_m == 0 on {z=0} (multiplicity >= 4: degenerate) | (B3) fails: u_5 == 0 on {z=0}
  - **N13***: no — u_4 is not c Q^2 with a quadratic form Q
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines:  (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): []
- covered by known: []; ours: []; soft: []; NOT COVERED: True; (93.9 s)

## P1: x^4+y^4-z^6 + tail x^3z^2+2y^3z^2 (in the gap of Palamodov Thm 6)

- U = `x**4 + x**3*z**2 + x*z**6 + y**4 + 2*y**3*z**2 + 3*y*z**6 - z**6`
- why: quasi-homogeneous principal part (3,3,2), d=12; tail x^3 z^2 of weighted degree 13 < d + a_min = 14
- lowest degree m = 4; forms: u_4=x**4 + y**4; u_5=x**3*z**2 + 2*y**3*z**2; u_6=-z**6; u_7=x*z**6 + 3*y*z**6
- isolation: μ=45 (Singular, локальный базис, конечен ⇒ изолирована и над ℂ); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['COMP 1 dim=0 : z,y,x', 'COMP 2 dim=0 : 4675*z^6+2790*z^4+1323*z^2+108,935*z^4-195*z^2+1296*y-252,z^2+x', 'COMP 3 dim=0 : 551956200025*z^12-167334687630*z^10+373730817969*z^8+11273109444*z^6+44236917504*z^4+12170870784*z^2+764411904,1249442828844907198759407475*z^10-537274591210533139289647770*z^8+933498694374501430545607611*z^6-47034755781385115572566228*z^4+107056995057888761320662528*z^2+91073782662715547320320000*y-3829927410163477737455616,-257741159720206892674825*z^10+124668455236022999263890*z^8-198531567087095932516377*z^6+23686530928180803544896*z^4-24919583010214291352496*z^2+4169026916323038360000*x-3446951316607880921088']
- not a minimum: луч w=(0, 0, -1): U(tw) = -1·t^6 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=False ['zero direction (0, 0, 1): rank Hess = 0 < 2 (degenerate transverse part)']; B3=False ['u_5(zero direction (0, 0, 1)) = 0']; l2=5
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (3, 3, 2), d=12, face has 3 monomials, tail wdeg_min=13: principal part is fine but the tail is TOO LARGE (13 < d + a_min=14)
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — l2 = 5 odd and Sigma = -Sigma: u_5(-w) = -u_5(w), so u_5 < 0 on all of Sigma is impossible
  - **ThmB**: no — (B2) fails: zero direction (0, 0, 1): rank Hess = 0 < 2 (degenerate transverse part) | (B3) fails: u_5(zero direction (0, 0, 1)) = 0
  - **N13***: no — u_4 is not c Q^2 with a quadratic form Q
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines: plane [0, 0, 1]: no; line [1, -1, 0]: no; line [1, 0, 0]: no; line [1, 1, 0]: no; line [0, 1, 0]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'plane', 'normal': [0, 0, 1], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'line', 'direction': [1, -1, 0], 'verdict': 'no', 'note': 'U on the line = 2 t^4 + ...'}, {'kind': 'line', 'direction': [1, 0, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}, {'kind': 'line', 'direction': [1, 1, 0], 'verdict': 'no', 'note': 'U on the line = 2 t^4 + ...'}, {'kind': 'line', 'direction': [0, 1, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}]
- covered by known: []; ours: []; soft: []; NOT COVERED: True; (1.2 s)

## P2: four zero directions, nondegenerate: Theorem B territory

- U = `x**4 - 2*x**2*z**2 + x*y*z**3 + 2*x*z**4 + y**4 - 2*y**2*z**2 + 2*z**4`
- why: u_4 vanishes at 8 points of the sphere with nondegenerate transverse Hessian; u_5 != 0 at all of them
- lowest degree m = 4; forms: u_4=x**4 - 2*x**2*z**2 + y**4 - 2*y**2*z**2 + 2*z**4; u_5=x*y*z**3 + 2*x*z**4
- isolation: μ=31 (Singular, локальный базис, конечен ⇒ изолирована и над ℂ); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['COMP 1 dim=0 : z,y,x', 'COMP 2 dim=0 : z^4+1440*z^2+6400,-z^3+640*y+240*z,7*z^2+160*x+240', 'COMP 3 dim=0 : 32805*z^8-28094688*z^6-155130368*z^4-70803456*z^2+14745600,-154322560395*z^7+132328397101392*z^5+589714292521216*z^3+375525839142912*y-53854882787328*z,-4046004675*z^6+3477131925840*z^4+3130830471424*z^2+93881459785728*x+39378700308480']
- not a minimum: луч w=(-1, -1, -1): U(tw) = -3·t^5 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=True []; B3=True []; l2=5
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (1, 1, 1), d=4, face has 5 monomials, tail wdeg_min=5: principal part has real critical points (exact)
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — l2 = 5 odd and Sigma = -Sigma: u_5(-w) = -u_5(w), so u_5 < 0 on all of Sigma is impossible
  - **ThmB**: yes — B1 (Sigma smooth submanifold), B2 (Morse-Bott), B3 (0 regular value of u_{m+1}|Sigma): 
  - **N13***: no — u_4 is not c Q^2 with a quadratic form Q
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines: plane [0, 0, 1]: no; line [1, -1, 0]: no; line [1, 0, 0]: no; line [1, 1, 0]: no; line [0, 1, 0]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'plane', 'normal': [0, 0, 1], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'line', 'direction': [1, -1, 0], 'verdict': 'no', 'note': 'U on the line = 2 t^4 + ...'}, {'kind': 'line', 'direction': [1, 0, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}, {'kind': 'line', 'direction': [1, 1, 0], 'verdict': 'no', 'note': 'U on the line = 2 t^4 + ...'}, {'kind': 'line', 'direction': [0, 1, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}]
- covered by known: []; ours: ['ThmB']; soft: []; NOT COVERED: False; (16.1 s)

## P3: four zero directions, u_5 vanishes at two of them

- U = `x**4 - 2*x**2*z**2 + x*z**4 + y**4 - 2*y**2*z**2 - z**6 - z**5 + 2*z**4`
- why: B3 fails at two zero directions (1,+-1,1)
- lowest degree m = 4; forms: u_4=x**4 - 2*x**2*z**2 + y**4 - 2*y**2*z**2 + 2*z**4; u_5=x*z**4 - z**5; u_6=-z**6
- isolation: μ=33 (Singular, локальный базис, конечен ⇒ изолирована и над ℂ); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['COMP 1 dim=0 : z,y,x', 'COMP 2 dim=0 : 2*z+3,2*y-3,4*x-3', 'COMP 3 dim=0 : 2*z+3,2*y+3,4*x-3', 'COMP 4 dim=0 : 108*z^2+108*z-85,y+z,288*x+126*z-85', 'COMP 5 dim=0 : 108*z^2+108*z-85,y-z,288*x+126*z-85', 'COMP 6 dim=0 : 216*z^6+540*z^5-278*z^4-975*z^3+292*z^2+400*z-128,y,540*z^5+1512*z^4+385*z^3-1626*z^2+232*x-680*z+448']
- not a minimum: луч w=(-1, -1, 1): U(tw) = -2·t^5 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=True []; B3=False ['u_5(zero direction (1, 1, 1)) = 0', 'u_5(zero direction (1, -1, 1)) = 0']; l2=5
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (1, 1, 1), d=4, face has 5 monomials, tail wdeg_min=5: principal part has real critical points (exact)
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — l2 = 5 odd and Sigma = -Sigma: u_5(-w) = -u_5(w), so u_5 < 0 on all of Sigma is impossible
  - **ThmB**: no — (B3) fails: u_5(zero direction (1, 1, 1)) = 0; u_5(zero direction (1, -1, 1)) = 0
  - **N13***: no — u_4 is not c Q^2 with a quadratic form Q
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines: plane [0, 0, 1]: no; plane [0, 1, 0]: no; line [1, -1, 0]: no; line [1, 0, 0]: no; line [1, 1, 0]: no; line [0, 1, 0]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'plane', 'normal': [0, 0, 1], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'plane', 'normal': [0, 1, 0], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'line', 'direction': [1, -1, 0], 'verdict': 'no', 'note': 'U on the line = 2 t^4 + ...'}, {'kind': 'line', 'direction': [1, 0, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}, {'kind': 'line', 'direction': [1, 1, 0], 'verdict': 'no', 'note': 'U on the line = 2 t^4 + ...'}, {'kind': 'line', 'direction': [0, 1, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^4 + ...'}]
- covered by known: []; ours: []; soft: []; NOT COVERED: True; (17.4 s)

## P4: three axes, u_5 = x^5+y^5 vanishes on the third axis

- U = `x**5 + x**4*y + x**4*z + x**2*y**2 + x**2*z**2 + x*y**4 + x*z**5 + y**5 + y**2*z**2 + 2*y*z**5 + z**6`
- why: B3 fails at the z-axis directions (u_5(e_z) = 0), but U < 0 along the other two axes
- lowest degree m = 4; forms: u_4=x**2*y**2 + x**2*z**2 + y**2*z**2; u_5=x**5 + x**4*y + x**4*z + x*y**4 + y**5; u_6=x*z**5 + 2*y*z**5 + z**6
- isolation: μ=31 (Singular, локальный базис, конечен ⇒ изолирована и над ℂ); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['(primary decomposition skipped: TimeoutExpired)']
- not a minimum: луч w=(-1, 0, 0): U(tw) = -1·t^5 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=True []; B3=False ['u_5(zero direction (0, 0, 1)) = 0']; l2=5
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (2, 3, 3), d=10, face has 3 monomials, tail wdeg_min=11: principal part has real critical points (exact); weights (2, 2, 1), d=6, face has 3 monomials, tail wdeg_min=7: principal part has real critical points (exact); weights (3, 2, 3), d=10, face has 3 monomials, tail wdeg_min=11: principal part has real critical points (exact); weights (1, 1, 1), d=4, face has 3 monomials, tail wdeg_min=5: principal part has real critical points (exact)
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — l2 = 5 odd and Sigma = -Sigma: u_5(-w) = -u_5(w), so u_5 < 0 on all of Sigma is impossible
  - **ThmB**: no — (B3) fails: u_5(zero direction (0, 0, 1)) = 0
  - **N13***: no — u_4 is not c Q^2 with a quadratic form Q
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines:  (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): []
- covered by known: []; ours: []; soft: []; NOT COVERED: True; (51.3 s)

## Z1: mixed zero set: equator + poles

- U = `x**5 + x**4*y + x**4*z + x**2*z**2 + x*y**4 + x*z**4 + y**5 + y**2*z**2 + 2*y*z**4 + z**5`
- why: u_4 = z^2 (x^2+y^2): Sigma = great circle z=0 (Hessian rank 1) UNION two poles (rank 2): components of different dimension, outside the statement of Theorem B
- lowest degree m = 4; forms: u_4=x**2*z**2 + y**2*z**2; u_5=x**5 + x**4*y + x**4*z + x*y**4 + x*z**4 + y**5 + 2*y*z**4 + z**5
- isolation: μ=39 (Singular, локальный базис, конечен ⇒ изолирована и над ℂ); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['(primary decomposition skipped: TimeoutExpired)']
- not a minimum: луч w=(-7, -6, 0): U(tw) = -48061·t^5 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=False ['components of different dimension (curve and points)']; B2=True ['Hess u_m != 0 on {z=0} (rank 1 = n-1-s): Morse-Bott']; B3=True ['0 regular value of u_5 on {z=0} (ideal (f,h,det[grad h,grad f,q]) has no real nonzero zero)']; l2=5
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (3, 3, 2), d=10, face has 3 monomials, tail wdeg_min=11: principal part has real critical points (exact); weights (2, 2, 3), d=10, face has 6 monomials, tail wdeg_min=11: principal part has real critical points (exact)
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — l2 = 5 odd and Sigma = -Sigma: u_5(-w) = -u_5(w), so u_5 < 0 on all of Sigma is impossible
  - **ThmB**: no — (B1) fails: components of different dimension (curve and points)
  - **N13***: no — u_4 is not c Q^2 with a quadratic form Q
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines:  (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): []
- covered by known: []; ours: []; soft: []; NOT COVERED: True; (31.4 s)

## S1: singular gutter: two crossing great circles

- U = `x**5 + x**4*z + x**4 - 2*x**2*y**2 + 2*y**5 + y**4*z + y**4 + z**6`
- why: u_4 = (x^2-y^2)^2: Sigma = two great circles meeting at the poles: not a submanifold; x^5+2y^5 and z(x^4+y^4) keep 0 isolated and break all reductions
- lowest degree m = 4; forms: u_4=x**4 - 2*x**2*y**2 + y**4; u_5=x**5 + x**4*z + 2*y**5 + y**4*z; u_6=z**6
- isolation: μ=53 (Singular, локальный базис, конечен ⇒ изолирована и над ℂ); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['(primary decomposition skipped: TimeoutExpired)']
- not a minimum: луч w=(-7, -7, -6): U(tw) = -79233·t^5 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=False ['components {x - y=0} and {x + y=0} may intersect']; B2=None ['Hess u_m rank on {x - y=0} inconclusive', 'Hess u_m rank on {x + y=0} inconclusive']; B3=False ['g = u_5|{x - y=0} has a MULTIPLE zero at w=(0, 0, -1): f=h=0 and dh|T = 0 there (exact)', 'g = u_5|{x + y=0} has a MULTIPLE zero at w=(0, 0, -1): f=h=0 and dh|T = 0 there (exact)']; l2=5
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_4 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_4 >= 0 vanishes at nonzero points, which are critical points of u_4 (grad u_4 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (3, 3, 2), d=12, face has 4 monomials, tail wdeg_min=14: principal part has real critical points (exact)
  - **Bu25-P1.2**: no — f = u_4|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — l2 = 5 odd and Sigma = -Sigma: u_5(-w) = -u_5(w), so u_5 < 0 on all of Sigma is impossible
  - **ThmB**: no — (B1) fails: components {x - y=0} and {x + y=0} may intersect | (B2) inconclusive: Hess u_m rank on {x - y=0} inconclusive; Hess u_m rank on {x + y=0} inconclusive | (B3) fails: g = u_5|{x - y=0} has a MULTIPLE zero at w=(0, 0, -1): f=h=0 and dh|T = 0 there (exact); g = u_5|{x + y=0} has a MULTIPLE zero at w=(0, 0, -1): f=h=0 and dh|T = 0 there (exact)
  - **N13***: no — u_4 is not c Q^2 with a quadratic form Q
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines: plane [0, 1, 0]: no; plane [1, 0, 0]: no; line [0, 0, 1]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'plane', 'normal': [0, 1, 0], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'plane', 'normal': [1, 0, 0], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'line', 'direction': [0, 0, 1], 'verdict': 'no', 'note': 'U on the line = 1 t^6 + ...'}]
- covered by known: []; ours: []; soft: []; NOT COVERED: True; (25.9 s)

## T1: cubic gutter, m=6

- U = `x**6 + 2*x**4*z**2 - 2*x**3*y**2*z + x**2*z**4 - 2*x*y**2*z**3 + y**8/8 + y**4*z**2 + y*z**7 - z**8`
- why: u_6 = C^2, C = y^2 z - x^3 - x z^2 a smooth real cubic: gutter is an elliptic curve (not a conic); u_7 = 0, W_8 = y^8/8 - z^8
- lowest degree m = 6; forms: u_6=x**6 + 2*x**4*z**2 - 2*x**3*y**2*z + x**2*z**4 - 2*x*y**2*z**3 + y**4*z**2; u_8=y**8/8 + y*z**7 - z**8
- isolation: μ=209 (Singular, локальный базис, конечен ⇒ изолирована и над ℂ); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['(primary decomposition skipped: TimeoutExpired)']
- not a minimum: луч w=(0, 0, -1): U(tw) = -1·t^8 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=True ['Hess u_m != 0 on {-x**3 - x*z**2 + y**2*z=0} (rank 1 = n-1-s): Morse-Bott']; B3=False ['u_{m+1} == 0']; l2=8
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — u_6 >= 0 (explicit SOS), so the lowest form has no negative values
  - **Koz86**: no — u_2 = 0 (the criterion needs the quadratic part u_2 >= 0, u_2 != 0)
  - **FGT08***: no — u_2 = 0 (Hessian is zero, kernel of dimension 3)
  - **Pa20-T3**: no — u_6 >= 0 vanishes at nonzero points, which are critical points of u_6 (grad u_6 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (4, 3, 6), d=24, face has 4 monomials, tail wdeg_min=28: principal part has real critical points (exact); weights (1, 1, 1), d=6, face has 6 monomials, tail wdeg_min=8: principal part has real critical points (exact); weights (4, 3, 2), d=16, face has 4 monomials, tail wdeg_min=17: principal part has real critical points (exact)
  - **Bu25-P1.2**: no — f = u_6|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — u_8 has real zeros on {-x**3 - x*z**2 + y**2*z=0} (or inconclusive): ideal saturation not the unit ideal
  - **ThmB**: no — (B3) fails: u_{m+1} == 0
  - **N13***: no — u_4 is not of the form c Q^2
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines: line [1, 0, 0]: no; line [0, 1, 0]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'line', 'direction': [1, 0, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^6 + ...'}, {'kind': 'line', 'direction': [0, 1, 0], 'verdict': 'no', 'note': 'U on the line = 1/8 t^8 + ...'}]
- covered by known: []; ours: []; soft: []; NOT COVERED: True; (41.4 s)

## H1: corank 1, curved valley

- U = `-x**7 + x**6 + x**4 - 2*x**3*z - 2*x**2*y + y**2 + z**2`
- why: u_2 = y^2+z^2, kernel = x-axis; the valley is the twisted cubic (x, x^2, x^3)
- lowest degree m = 2; forms: u_2=y**2 + z**2; u_3=-2*x**2*y; u_4=x**4 - 2*x**3*z; u_6=x**6; u_7=-x**7
- isolation: μ=6 (Singular, локальный базис, конечен ⇒ изолирована и над ℂ); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['COMP 1 dim=0 : -x^3+z,-x^2+y,x']
- not a minimum: кривая γ(τ)=(tau, tau**2, tau**3): U(γ) = -1·τ^7 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=True []; B3=False ['u_3(zero direction (1, 0, 0)) = 0']; l2=3
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — m = 2: covered by the Lyapunov / Koz86 columns
  - **Koz86**: no — u_3|ker u_2 == 0 for the first form u_3 (literal hypothesis V_2 + V_m + ...)
  - **FGT08***: maybe — Hessian >= 0 with kernel of dimension 1 <= 2: covered by FGT08/Pa20-T5 IF their hypotheses are as recorded in KNOWN_RESULTS (not verified at the source)
  - **Pa20-T3**: no — u_2 >= 0 vanishes at nonzero points, which are critical points of u_2 (grad u_2 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (1, 2, 2), d=4, face has 4 monomials, tail wdeg_min=5: principal part has real critical points (exact)
  - **Bu25-P1.2**: no — f = u_2|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — l2 = 3 odd and Sigma = -Sigma: u_3(-w) = -u_3(w), so u_3 < 0 on all of Sigma is impossible
  - **ThmB**: no — (B3) fails: u_3(zero direction (1, 0, 0)) = 0
  - **N13***: no — u_4 is not of the form c Q^2
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines: plane [1, 0, 0]: no; line [0, 0, 1]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'plane', 'normal': [1, 0, 0], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'line', 'verdict': 'info', 'note': 'all lines of the plane {x=0} are invariant; that plane is tested by the plane search'}, {'kind': 'line', 'direction': [0, 0, 1], 'verdict': 'no', 'note': 'U on the line = 1 t^2 + ...'}]
- covered by known: []; ours: []; soft: ['FGT08*']; NOT COVERED: False; (9.5 s)

## H2: corank 2, cuspidal valley

- U = `2*x**4 - 2*x**2*y**3 - 2*x**2*z - y**7 + y**6 + z**2`
- why: u_2 = z^2, kernel = the plane z=0; reduced 2D potential (x^2-y^3)^2 - y^7 (cusp)
- lowest degree m = 2; forms: u_2=z**2; u_3=-2*x**2*z; u_4=2*x**4; u_5=-2*x**2*y**3; u_6=y**6; u_7=-y**7
- isolation: μ=17 (Singular, локальный базис, конечен ⇒ изолирована и над ℂ); над ℝ: насыщение J:p^∞, p=x**2 + y**2 + z**2, K⊄𝔪 ✓; components of V(grad U): ['COMP 1 dim=0 : -x^2+z,y,x', 'COMP 2 dim=0 : -x^2+z,7*y-6,x']
- not a minimum: кривая γ(τ)=(tau**3, tau**2, tau**6): U(γ) = -1·τ^14 + …
- hard core: u_m>=0 by explicit SOS: True; zero set complete over C: True; B1=True []; B2=True ['Hess u_m != 0 on {z=0} (rank 1 = n-1-s): Morse-Bott']; B3=False ['u_3 == 0 on {z=0}']; l2=3
- criteria:
  - **Lyapunov**: no — u_2 is not negative somewhere (u_2 >= 0 or u_2 = 0)
  - **KP82**: no — m = 2: covered by the Lyapunov / Koz86 columns
  - **Koz86**: no — u_3|ker u_2 == 0 for the first form u_3 (literal hypothesis V_2 + V_m + ...)
  - **FGT08***: maybe — Hessian >= 0 with kernel of dimension 2 <= 2: covered by FGT08/Pa20-T5 IF their hypotheses are as recorded in KNOWN_RESULTS (not verified at the source)
  - **Pa20-T3**: no — u_2 >= 0 vanishes at nonzero points, which are critical points of u_2 (grad u_2 = 0 at a minimum)
  - **QH-linear**: no — U is not quasi-homogeneous in the linear coordinates (exponents do not lie on a hyperplane with positive normal)
  - **Pa20-T6**: no — weights (3, 2, 6), d=12, face has 5 monomials, tail wdeg_min=14: principal part has real critical points (exact)
  - **Bu25-P1.2**: no — f = u_2|S >= 0 with zeros: 0 is a critical (minimal) value of f, not a regular value
  - **Bu25-C1.4**: no — l2 = 3 odd and Sigma = -Sigma: u_3(-w) = -u_3(w), so u_3 < 0 on all of Sigma is impossible
  - **ThmB**: no — (B3) fails: u_3 == 0 on {z=0}
  - **N13***: no — u_4 is not of the form c Q^2
  - **N13**: no — U is not (a rotation/scaling of) the Example-13 polynomial
  - **SYM**: no — exact search of ALL invariant planes and lines: plane [0, 1, 0]: no; plane [1, 0, 0]: no; line [0, 1, 0]: no; line [0, 0, 1]: no (U restricted is a local minimum / positive on each)
- invariant planes/lines of the dynamics (exact search): [{'kind': 'plane', 'normal': [0, 1, 0], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'plane', 'normal': [1, 0, 0], 'verdict': 'no', 'note': 'f >= 0 in the floating-point scan at radii 0.1..0.003 and no exact witness: 0 looks like a minimum of the restriction'}, {'kind': 'line', 'direction': [0, 1, 0], 'verdict': 'no', 'note': 'U on the line = 1 t^6 + ...'}, {'kind': 'line', 'direction': [0, 0, 1], 'verdict': 'no', 'note': 'U on the line = 1 t^2 + ...'}]
- covered by known: []; ours: []; soft: ['FGT08*']; NOT COVERED: False; (10.7 s)
