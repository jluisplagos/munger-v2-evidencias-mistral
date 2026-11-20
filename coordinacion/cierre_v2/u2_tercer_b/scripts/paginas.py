import sys,re,os
pat={'cuenta_resultados':r'^\s*Consolidated income statement\s*$','balance':r'^\s*Consolidated balance sheet\s*$','flujos':r'^\s*Consolidated statement of cash flows\s*$','patrimonio':r'^\s*Consolidated statement of changes in equity\s*$','arrend':r'^\s*\d+\s+Leases\s*$','reexpresion_ifrs16':r'(?i)restat\w* .{0,40}IFRS 16|IFRS 16.{0,60}restat'}
for f in sys.argv[1:]:
    pages=open(f,encoding='utf-8',errors='replace').read().split('\f')
    out=[]
    for k,p in pat.items():
        hits=[i+1 for i,t in enumerate(pages) if re.search(p,t,re.M)]
        out.append(f"{k}={hits[:6]}")
    first=' '.join(pages[0].split())[:80]
    print(os.path.basename(f), len(pages)-1, '|', first, '|', '; '.join(out))
