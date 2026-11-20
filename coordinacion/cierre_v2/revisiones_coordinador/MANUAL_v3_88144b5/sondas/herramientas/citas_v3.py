import re, subprocess, sys, os
import os; C=os.environ['CAND']; A=os.environ['AUX']; EREV=os.environ.get('EREV','88144b5')
def ls(repo, rev, pref=''):
    return subprocess.run(['git','-C',repo,'ls-tree','-r','--name-only',rev],capture_output=True,text=True).stdout.split('\n')
CF=ls(C,'3149128'); AF=ls(A,EREV)
F1P='docs/validacion_economica_paralela/frente_E_F1_elis/evidencias/preparacion/'
F1F=[f for f in ls(C,'03e7851') if f.startswith(F1P)]
cache={}
def show(repo,rev,p):
    k=(repo,rev,p)
    if k not in cache:
        r=subprocess.run(['git','-C',repo,'show',f'{rev}:{p}'],capture_output=True)
        cache[k]=r.stdout.decode('utf-8','replace').split('\n') if r.returncode==0 else None
    return cache[k]
AB={'PV2/':'munger_v2_r1/personaje_v2/','E414/':'munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/',
'E415/':'munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/'}
EAB={'EVID/':'','PRUEBAS/':'coordinacion/cierre_v2/pruebas_candidata/957af65/','TRASP/':'coordinacion/cierre_v2/traspaso/resultado_20261117/',
'REG/':'coordinacion/cierre_v2/traspaso/resultado_20261117/registro/','REVT/':'coordinacion/cierre_v2/traspaso/revision_20261117/','HERR/':'coordinacion/cierre_v2/herramientas/'}
def resolve(p):
    p=p.replace('E414/../','munger_v2_r1/personaje_v2/empresas_v2_correcciones/')
    for k,v in AB.items():
        if p.startswith(k): return (C,'3149128',v+p[len(k):])
    for k,v in EAB.items():
        if p.startswith(k): return (A,EREV,v+p[len(k):])
    if p.startswith('F1PREP/'): return (C,'03e7851',F1P+p[7:])
    if p.startswith('munger_v2_r1/') or p in CF: return (C,'3149128',p)
    q=p.lstrip('…/').lstrip('./')
    m=[f for f in CF if f.endswith('/'+q) or f==q]
    if len(m)==1: return (C,'3149128',m[0])
    m2=[f for f in AF if f.endswith('/'+q) or f==q]
    if len(m2)==1 and not m: return (A,EREV,m2[0])
    m3=[f for f in F1F if f.endswith('/'+q)]
    if len(m3)==1 and not m and not m2: return (C,'03e7851',m3[0])
    return ('AMBIG',len(m),len(m2),m[:3]+m2[:3])
src=sys.argv[1]; out=open(sys.argv[2],'w')
cit=re.compile(r'`([^`\s]+?):(\d+(?:-\d+)?(?:,\d+(?:-\d+)?)*)`|`:(\d+(?:-\d+)?(?:,\d+(?:-\d+)?)*)`|`([A-Za-z0-9_./…-]+\.(?:md|py|sh|json|txt|log|sha256))`')
prob=0
for ln,line in enumerate(open(src,encoding='utf-8'),1):
    last=None
    for m in cit.finditer(line):
        if m.group(4):
            last=m.group(4); continue
        if m.group(1) is not None:
            f=m.group(1); rng=m.group(2); last=f
        else:
            f=last; rng=m.group(3)
            if f is None: out.write(f'L{ln}: :{rng} sin archivo previo\n'); continue
        r=resolve(f)
        if r[0]=='AMBIG': out.write(f'L{ln}: {f}:{rng} -> AMBIGUO {r}\n'); prob+=1; continue
        repo,rev,p=r; txt=show(repo,rev,p)
        if txt is None: out.write(f'L{ln}: {f}:{rng} -> NO EXISTE {rev}:{p}\n'); prob+=1; continue
        n=len(txt)-(1 if txt and txt[-1]=='' else 0)
        for part in rng.split(','):
            a,b=(part.split('-')+[part])[:2]; a,b=int(a),int(b)
            if b>n or a<1 or a>b: out.write(f'L{ln}: {f}:{part} -> FUERA DE RANGO (n={n})\n'); prob+=1; continue
            out.write(f'L{ln}: {f}:{part} [{rev[:7]}:{p}]\n')
            for i in range(a,b+1): out.write(f'    {i}| {txt[i-1][:260]}\n')
print('problemas',prob)
