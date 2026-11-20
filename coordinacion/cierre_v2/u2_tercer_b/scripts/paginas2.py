import sys,re,os
req={'CR':[r'(?i)consolidated income statement',r'(?i)net sales',r'(?i)operating income',r'(?i)income tax'],
     'BAL':[r'(?i)consolidated balance sheet',r'(?i)total assets',r'(?i)total equity'],
     'FLU':[r'(?i)consolidated statement of cash flows',r'(?i)operating activities',r'(?i)financing activities'],
     'PAT':[r'(?i)consolidated statement of changes in equity',r'(?i)dividends'],
     'N_IFRS16_2018':[r'(?i)IFRS 16',r'(?i)restat',r'(?i)2018']}
for f in sys.argv[1:]:
    pages=open(f,encoding='utf-8',errors='replace').read().split('\f')
    res=[]
    for k,ps in req.items():
        hits=[i+1 for i,t in enumerate(pages) if all(re.search(p,t[:400] if j==0 and k!='N_IFRS16_2018' else t) for j,p in enumerate(ps))]
        res.append(f"{k}={hits[:8]}")
    print(os.path.basename(f), '; '.join(res))
