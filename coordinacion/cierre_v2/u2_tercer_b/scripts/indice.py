import csv,sys,hashlib,os
log,html_dir,out=sys.argv[1:4]
cierre={2016:'2017-01-01 (52 sem.)',2017:'2017-12-31 (52 sem.)',2018:'2018-12-30 (52 sem.)',2019:'2019-12-29 (52 sem.)',2020:'2021-01-03 (53 sem.)',2021:'2022-01-02 (52 sem.)',2022:'2023-01-01 (52 sem.)',2023:'2023-12-31 (52 sem.)',2024:'2024-12-29 (52 sem.)',2025:'2025-12-28 (52 sem.)'}
flu={2016:116,2017:127,2018:93,2019:125,2020:149,2021:184,2022:194,2023:204,2024:263,2025:216}
rows=list(csv.DictReader(open(log,encoding='utf-8'),delimiter='\t'))
cols=['archivo','tipo','ejercicio','cierre_ejercicio','url','pagina_oficial_que_enlaza','fecha_descarga_utc','http','bytes','sha256','paginas','content_type','comprobacion_contenido','error','descripcion']
w=csv.DictWriter(open(out,'w',newline='',encoding='utf-8'),fieldnames=cols); w.writeheader()
for r in rows:
    n=r['archivo']; y=None
    for k in cierre:
        if f'report-{k}' in n: y=k
    if y:
        enl=f'https://aholddelhaize.com/investors/annual-reports/{y}/'; tipo='informe_anual'
        comp=(f'portada «Annual Report {y}»; cierre de ejercicio leido en el propio informe; PDF p. {flu[y]} contiene «Net cash from operating activities» (estado de flujos). No es verificacion de entradas.')
        if y==2019: comp+=' Nota 36 (PDF pp. 188-192): reexpresion NIIF 16 de 2018 y 1-ene-2018, con las diferencias frente al folleto del 25-mar-2019 (PDF p. 190, notas 1 y 2).'
        if y==2016: comp+=' Fusion efectiva el 24-jul-2016: 2016 incluye Delhaize solo desde esa fecha.'
    else:
        enl='descargar_fuentes_ahold.bat (base 4.14); no enlazado en /investors/annual-reports/2018/ ni /2019/ ni en /investors/quarterly-results/q4-2018/ ni /q1-2019/'; tipo='folleto_reexpresion_NIIF16'; comp=''
    w.writerow({'archivo':n,'tipo':tipo,'ejercicio':y or 2018,'cierre_ejercicio':cierre.get(y,''),'url':r['url'],'pagina_oficial_que_enlaza':enl,'fecha_descarga_utc':r['fecha_utc'],'http':r['http'],'bytes':r['bytes'],'sha256':r['sha256'],'paginas':r['paginas'],'content_type':r['content_type'],'comprobacion_contenido':comp,'error':r['error'],'descripcion':r['descripcion']})
# paginas html usadas para localizar los enlaces
for f in sorted(os.listdir(html_dir)):
    if not f.endswith('.html') or f in ('tmp.html','search.html','home.html','qr_2018.html','qr_2019.html','qr_q4-2018-results.html'): continue
    p=os.path.join(html_dir,f); b=open(p,'rb').read()
    url={'annual-reports.html':'https://aholddelhaize.com/investors/annual-reports/','qr.html':'https://aholddelhaize.com/investors/quarterly-results/','sbb.html':'https://aholddelhaize.com/investors/share-buyback-programs/'}.get(f)
    if f.startswith('ar_'): url=f'https://aholddelhaize.com/investors/annual-reports/{f[3:7]}/'
    if f.startswith('qr_'): url=f'https://aholddelhaize.com/investors/quarterly-results/{f[3:-5]}/'
    w.writerow({'archivo':'html/'+f,'tipo':'pagina_html_de_localizacion','url':url,'fecha_descarga_utc':'2026-11-17 (misma sesion)','http':'200','bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'descripcion':'pagina oficial leida para localizar los enlaces; contenido dinamico, puede cambiar'})
