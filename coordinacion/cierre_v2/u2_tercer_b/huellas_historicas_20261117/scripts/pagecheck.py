import sys
d=sys.argv[1]
checks=[('2025',[54,55],'Baa1'),('2025',[54,55],'5.5'),('2025',[270,271],'share-based'),('2025',[12,58],'9,551'),('2025',[43,50],'market share'),('2025',[69,76],'agentic'),('2025',[180],'566,744'),('2025',[210],'Share performance'),
('2022',[13],'magnitude of inflation'),('2021',[7],'2024'),('2023',[13,14],'relatively consistent'),('2024',[43,44],'Stop & Shop'),('2021',[191],'FreshDirect'),('2023',[212],'FreshDirect'),('2020',[99],'')]
cache={}
for y,pp,term in checks:
    if y not in cache: cache[y]=open(f'{d}/AD_annual-report-{y}.txt',encoding='utf-8',errors='replace').read().split('\f')
    pages=cache[y]
    res={p:(term.lower() in pages[p-1].lower()) for p in pp}
    where=[i+1 for i,x in enumerate(pages) if term and term.lower() in x.lower()][:12]
    print(f'AR{y} {pp} "{term}": en_pag_citada={res} ; aparece_en={where}')
