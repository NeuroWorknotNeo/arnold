"""
traj_c.py -- генерация и компиляция C-кода интегратора для  q'' = -grad U(q)  (Йошида 6-го порядка, long double),
обёртка на ctypes.  [Эксперимент]

Схема: композиция Йошида (7 подшагов) из лидирующей схемы 'прыжок лягушки' -- симплектическая при фиксированном шаге.
Шаг h выбирается кусочно-постоянным: на сегменте по радиусу (r меняется не более чем в 1.25 раза) h = eps / sqrt(4 ||Hess||_F)
в начале сегмента (запас 4 на рост жёсткости).  Строго симплектичность нарушается только при смене шага на границах
сегментов; контроль -- дрейф энергии E = v^2/2 + U относительно масштаба a0 r^beta.
"""
import os, ctypes, subprocess, hashlib
import sympy as sp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
x, y, z = sp.symbols('x y z')

C_TEMPLATE = r"""
#include <math.h>
#include <stdlib.h>
typedef long double LD;
static LD potU(const LD*q){ LD x=q[0],y=q[1],z=q[2];
%(U_CODE)s
 return U_; }
static void gradU(const LD*q, LD*g){ LD x=q[0],y=q[1],z=q[2];
%(G_CODE)s
}
static LD hessF(const LD*q){ LD x=q[0],y=q[1],z=q[2];
%(H_CODE)s
 return sqrtl(hF_); }

static const LD W1=-1.17767998417887100694641568096432L, W2=0.235573213359358133684793182978535L,
                W3=0.784513610477560146803100002433L;

static void leap(LD*q, LD*v, LD h){
  LD g[3]; gradU(q,g);
  v[0]-=0.5L*h*g[0]; v[1]-=0.5L*h*g[1]; v[2]-=0.5L*h*g[2];
  q[0]+=h*v[0]; q[1]+=h*v[1]; q[2]+=h*v[2];
  gradU(q,g);
  v[0]-=0.5L*h*g[0]; v[1]-=0.5L*h*g[1]; v[2]-=0.5L*h*g[2];
}
static void yos6(LD*q, LD*v, LD h){
  LD W0=1.0L-2.0L*(W1+W2+W3);
  leap(q,v,W3*h); leap(q,v,W2*h); leap(q,v,W1*h); leap(q,v,W0*h);
  leap(q,v,W1*h); leap(q,v,W2*h); leap(q,v,W3*h);
}
static LD rad(const LD*q){ return sqrtl(q[0]*q[0]+q[1]*q[1]+q[2]*q[2]); }

/* интегрирует вперёд по времени (направление задаёт знак dirsgn: -1 = обратное время, v в этом случае
   интерпретируется как реальная скорость, и интегрируется поток с v -> -v).
   mode 0: до первого r >= rstop (выход); mode 1: до r <= rstop (вход) или T>=Tmax.
   rec: nrec записей (t, r, U/(a0 r^beta), E/(a0 r^beta), |v|/sqrt(a0 r^beta)) в моменты t_k геометрически от t1 до Tmax.
   out: [q0..2, v0..2, T, maxdrift, nsteps, status, rfinal]   status: 0 = событие, 1 = лимит шагов, 2 = Tmax */
int integrate(const double*q0d, const double*v0d, int mode, double rstop_d, double Tmax_d, double eps_d,
              double a0_d, double beta_d, double nmax_d, int nrec, double t1_d, double*rec, double*out, double rescape_d){
  LD q[3]={q0d[0],q0d[1],q0d[2]}, v[3]={v0d[0],v0d[1],v0d[2]};
  LD eps=eps_d, a0=a0_d, beta=beta_d, rstop=rstop_d, Tmax=Tmax_d, rescape=rescape_d;
  LD t=0, h=0; long long n=0, nmax=(long long)nmax_d; LD segr=-1; LD maxdrift=0;
  LD E0=0.5L*(v[0]*v[0]+v[1]*v[1]+v[2]*v[2])+potU(q); LD E0n=fabsl(E0)/(a0*powl(rad(q),beta));
  int irec=0; LD t1=t1_d; LD lg=(nrec>1)? logl(Tmax/t1)/(nrec-1):0; LD nextrec=t1;
  int status=2;
  while(t<Tmax){
    LD r=rad(q);
    if(segr<0 || r>1.25L*segr || r<segr/1.25L){ segr=r; LD H=hessF(q); h=eps/sqrtl(4.0L*H+1e-300L); }
    if(n>=nmax){ status=1; break; }
    LD q_old[3]={q[0],q[1],q[2]}, v_old[3]={v[0],v[1],v[2]};
    yos6(q,v,h); t+=h; n++;
    LD r2=rad(q);
    if(nrec>0 && irec<nrec && t>=nextrec){
      LD sc=a0*powl(r2,beta); LD U=potU(q); LD E=0.5L*(v[0]*v[0]+v[1]*v[1]+v[2]*v[2])+U-E0;
      rec[5*irec+0]=(double)t; rec[5*irec+1]=(double)r2; rec[5*irec+2]=(double)(U/sc); rec[5*irec+3]=(double)(E/sc);
      rec[5*irec+4]=(double)(sqrtl(v[0]*v[0]+v[1]*v[1]+v[2]*v[2])/sqrtl(sc));
      irec++; nextrec=t1*expl(lg*irec);
    }
    if((n&255)==0){
      LD sc=a0*powl(r2,beta); LD E=0.5L*(v[0]*v[0]+v[1]*v[1]+v[2]*v[2])+potU(q)-E0;
      LD d=fabsl(E)/sc; if(d>maxdrift) maxdrift=d;
    }
    if(mode==0 && r2>=rstop){
      /* уточнить момент пересечения сферы r=rstop: бисекция по длине последнего шага */
      LD lo=0, hi=h;
      for(int it=0; it<80; it++){
        LD mid=0.5L*(lo+hi);
        LD qq[3]={q_old[0],q_old[1],q_old[2]}, vv[3]={v_old[0],v_old[1],v_old[2]};
        yos6(qq,vv,mid);
        if(rad(qq)<rstop) lo=mid; else hi=mid;
      }
      LD qq[3]={q_old[0],q_old[1],q_old[2]}, vv[3]={v_old[0],v_old[1],v_old[2]};
      yos6(qq,vv,hi);
      t = t - h + hi; q[0]=qq[0];q[1]=qq[1];q[2]=qq[2]; v[0]=vv[0];v[1]=vv[1];v[2]=vv[2];
      status=0; break;
    }
    if(mode==1 && (r2<=rstop || r2>=rescape)){ status=0; break; }
  }
  LD sc=a0*powl(rad(q),beta); LD E=0.5L*(v[0]*v[0]+v[1]*v[1]+v[2]*v[2])+potU(q)-E0;
  LD d=fabsl(E)/sc; if(d>maxdrift) maxdrift=d;
  for(int i=0;i<3;i++){ out[i]=(double)q[i]; out[3+i]=(double)v[i]; }
  out[6]=(double)t; out[7]=(double)maxdrift; out[8]=(double)n; out[9]=status; out[10]=(double)rad(q);
  out[11]=irec; out[12]=(double)E0n;
  return status;
}
double potential(const double*qd){ LD q[3]={qd[0],qd[1],qd[2]}; return (double)potU(q); }
"""


def _code(expr, name):
    reps, red = sp.cse(expr)
    lines = []
    for s, e in reps:
        lines.append(f" LD {sp.ccode(s)} = {sp.ccode(e)};")
    return lines, red


def ld(s):
    # long double literals: add L; степени -> произведения (pow() считает в double)
    import re
    s = re.sub(r'pow\((\w+), (\d+)\)', lambda m: '(' + '*'.join([m.group(1)] * int(m.group(2))) + ')', s)
    assert 'pow(' not in s, s
    return re.sub(r'(?<![\w.])(\d+\.\d+|\d+\.)(?![\w])', lambda m: m.group(1) + 'L', s)


def build(Ustr, tag):
    U = sp.expand(sp.sympify(Ustr, locals={'x': x, 'y': y, 'z': z}))
    g = [sp.diff(U, v) for v in (x, y, z)]
    H = [[sp.diff(gi, v) for v in (x, y, z)] for gi in g]
    h6 = [H[0][0], H[0][1], H[0][2], H[1][1], H[1][2], H[2][2]]

    def block(exprs, outs):
        reps, red = sp.cse(exprs)
        L = [f" LD {sp.ccode(s)} = {ld(sp.ccode(e))};" for s, e in reps]
        for o, e in zip(outs, red):
            L.append(f" {o} = {ld(sp.ccode(e))};")
        return "\n".join(L)

    U_code = "LD U_;\n" + block([U], ["U_"])
    G_code = block(g, ["g[0]", "g[1]", "g[2]"])
    H_code = "LD h_[6];\n" + block(h6, ["h_[0]", "h_[1]", "h_[2]", "h_[3]", "h_[4]", "h_[5]"]) + \
        "\n LD hF_ = h_[0]*h_[0]+h_[3]*h_[3]+h_[5]*h_[5]+2*(h_[1]*h_[1]+h_[2]*h_[2]+h_[4]*h_[4]);\n" 
    src = C_TEMPLATE % dict(U_CODE=U_code, G_CODE=G_code, H_CODE=H_code)
    d = os.path.join(HERE, 'build')
    os.makedirs(d, exist_ok=True)
    cpath = os.path.join(d, f'{tag}.c')
    sopath = os.path.join(d, f'{tag}.so')
    open(cpath, 'w').write(src)
    subprocess.check_call(['gcc', '-O2', '-shared', '-fPIC', '-o', sopath, cpath, '-lm'])
    lib = ctypes.CDLL(sopath)
    dp = ctypes.POINTER(ctypes.c_double)
    lib.integrate.argtypes = [dp, dp, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double,
                              ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_double,
                              dp, dp, ctypes.c_double]
    lib.integrate.restype = ctypes.c_int
    lib.potential.argtypes = [dp]
    lib.potential.restype = ctypes.c_double
    return lib


def _p(a):
    a = np.ascontiguousarray(a, dtype=np.float64)
    return a, a.ctypes.data_as(ctypes.POINTER(ctypes.c_double))


def integrate(lib, q0, v0, mode, rstop, Tmax, eps, a0, beta, nmax, nrec=0, t1=1.0, rescape=1e9):
    qa, qp = _p(q0)
    va, vp = _p(v0)
    out = np.zeros(13)
    rec = np.zeros(max(1, 5 * nrec))
    _, op = _p(out)
    _, rp = _p(rec)
    lib.integrate(qp, vp, mode, rstop, Tmax, eps, a0, beta, float(nmax), nrec, t1, rp, op, rescape)
    return out, rec[:5 * int(out[11])].reshape(-1, 5) if nrec else None


def potential(lib, q):
    qa, qp = _p(q)
    return lib.potential(qp)
