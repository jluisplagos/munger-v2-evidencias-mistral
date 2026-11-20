import importlib.util, random, itertools, sys
from fractions import Fraction
def carga(n,p):
    s=importlib.util.spec_from_file_location(n,p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
O=carga("viejo","/dev/shm/rv/old_scripts/munger_v2_r1/personaje_v2/scripts/fase1_historia.py")
N=carga("nuevo","/dev/shm/rv/new_scripts/munger_v2_r1/personaje_v2/scripts/fase1_historia.py")
random.seed(7)
casos=["", "-", "–", "—", " ", "0", "(0)", "-0", "12a", "1,2,3", "4 573,7", "(4 573,7)", "1.031", "1,031", "11.37", "(130,8)", "+5", "1.234.567,89", "1.234,5", "007", "1.23", "1.234", "12.34", "(1.234)", "−1.234", "( 1.234 )", "1 234", "12 345 678", "1.2345"]
for _ in range(20000):
    n=random.randint(0,10**10); s=f"{n:,}"
    if random.random()<.5: s=s.replace(",",".")
    if random.random()<.3: s=s+random.choice([".",","])+str(random.randint(0,99)).zfill(random.choice([1,2]))
    if random.random()<.3: s="("+s+")"
    elif random.random()<.2: s="-"+s
    if random.random()<.1: s=s.replace(",", " ").replace(".", " ")
    casos.append(s)
dif=0; difex=0
for s in casos:
    try: a=("ok",O.numero(s))
    except Exception as e: a=("err",type(e).__name__)
    try: b=("ok",N.numero(s))
    except Exception as e: b=("err",type(e).__name__)
    if a!=b or (a[0]=="ok" and repr(a[1])!=repr(b[1])):
        dif+=1; print("numero distinto",repr(s),a,b)
    try: c=("ok",N.numero_exacto(s))
    except Exception as e: c=("err",type(e).__name__)
    if (b[0]!=c[0]) or (b[0]=="ok" and float(c[1])!=b[1]):
        difex+=1; print("exacto distinto",repr(s),b,c)
print("casos",len(casos),"numero distinto",dif,"numero_exacto≠numero",difex)
# cero negativo en numero
print("numero('-0') viejo/nuevo:",repr(O.numero("-0")),repr(N.numero("-0")), "exacto:",N.numero_exacto("-0"))
# redondear frente a verificacion_entradas._round_frac
sys.path.insert(0,"/dev/shm/rv/new_scripts/munger_v2_r1/personaje_v2/scripts")
import verificacion_entradas as VE
m=0
for _ in range(20000):
    x=Fraction(random.randint(-10**9,10**9),10**random.randint(0,8)); n=random.randint(0,6)
    if float(VE._round_frac(x,n))!=N.redondear(x,n): m+=1
print("redondear ≠ VE._round_frac:",m)
# float de entrada: redondear(float) toma repr
for x,n in ((7.03515,4),(61.15855,4),(0.1+0.2,1),(1e-7,4),(-1e-7,4),(123456789.12345,4),(2.0004999999999997,3)):
    print("redondear",repr(x),n,"->",N.redondear(x,n),"| round py:",round(x,n))
