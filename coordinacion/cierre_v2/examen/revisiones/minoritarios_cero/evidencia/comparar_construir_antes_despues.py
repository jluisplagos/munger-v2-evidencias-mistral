import json, os, shutil, subprocess, sys
OLD="/dev/shm/rz/old_scripts/munger_v2_r1/personaje_v2/scripts/fase1_historia.py"
NEW="/dev/shm/rz/new_scripts/munger_v2_r1/personaje_v2/scripts/fase1_historia.py"
base="/home/user/e_work/wt_mincero/munger_v2_r1"
def diffs(a,b,p=""):
    out=[]
    if isinstance(a,dict) and isinstance(b,dict):
        for k in sorted(set(a)|set(b), key=str):
            if k not in a or k not in b: out.append((p+"/"+str(k), a.get(k,"<falta>"), b.get(k,"<falta>")))
            else: out+=diffs(a[k],b[k],p+"/"+str(k))
    elif isinstance(a,list) and isinstance(b,list) and len(a)==len(b):
        for i,(x,y) in enumerate(zip(a,b)): out+=diffs(x,y,p+f"[{i}]")
    elif a!=b or type(a)!=type(b): out.append((p,a,b))
    return out
for rel in sys.argv[1:]:
    src=os.path.join(base,rel); res={}
    for tag,scr in (("old",OLD),("new",NEW)):
        dst=f"/dev/shm/rz/{tag}/x"; shutil.rmtree(f"/dev/shm/rz/{tag}",ignore_errors=True); shutil.copytree(src,dst,symlinks=True)
        r=subprocess.run([sys.executable,"-B",scr,"construir",dst],capture_output=True,text=True)
        j=json.load(open(dst+"/fase1_v63.json")) if r.returncode==0 and os.path.exists(dst+"/fase1_v63.json") else None
        md=open(dst+"/historia_revision.md",encoding="utf-8").read().splitlines() if os.path.exists(dst+"/historia_revision.md") else []
        res[tag]=(r.returncode,(r.stdout+r.stderr)[-200:],j,md)
    (ro,eo,jo,mo),(rn,en,jn,mn)=res["old"],res["new"]
    print(f"== {rel}: rc old={ro} new={rn}")
    if True:
        if eo!=en: print("   salida distinta:\n    old:",eo.replace("\n"," | "),"\n    new:",en.replace("\n"," | "))
        elif ro or rn: print("   ambos:",eo.replace("\n"," | ")[-150:])
    if jo is not None and jn is not None:
        for p,a,b in diffs(jo,jn):
            sa,sb=repr(a),repr(b)
            print(f"   JSON {p}: {sa[:300]} -> {sb[:300]}")
    ml=[l for l in mo if l not in mn]; nl=[l for l in mn if l not in mo]
    for l in ml: print("   MD-:",l[:300])
    for l in nl: print("   MD+:",l[:300])
shutil.rmtree("/dev/shm/rz/old",ignore_errors=True); shutil.rmtree("/dev/shm/rz/new",ignore_errors=True)
