import sys,re,os,json
req={'CR':[r'(?i)consolidated income statement',r'(?i)\bnet sales\b',r'(?i)operating income',r'(?i)income taxes',r'(?i)net income'],
     'BAL':[r'(?i)consolidated balance sheet',r'(?i)total assets',r'(?i)total equity and liabilities'],
     'FLU':[r'(?i)consolidated statement of cash flows',r'(?i)net cash from operating activities',r'(?i)financing activities'],
     'PAT':[r'(?i)consolidated statement of changes in equity',r'(?i)dividends',r'(?i)share buyback'],
     'IFRS16_2018':[r'(?i)IFRS 16',r'(?i)restated',r'(?i)2018',r'(?i)lease liabilit']}
salida={}
for f in sys.argv[1:]:
    pages=open(f,encoding='utf-8',errors='replace').read().split('\f')
    res={}
    for k,ps in req.items():
        res[k]=[i+1 for i,t in enumerate(pages) if all(re.search(p,t) for p in ps)][:6]
    salida[os.path.basename(f)]=res
    print(os.path.basename(f), res)
