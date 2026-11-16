"""Sonda 9: busca en el listado del ZIP base-4.14 (y en el texto de sus archivos .md/.txt/.csv/.json)
(a) cualquier recurso de Ahold Delhaize (Excel de etapa 1, respuesta, PDF, extraccion);
(b) cualquier entidad financiera (banco/aseguradora) conservada; (c) fixtures del motor C;
(d) la lista de las 116 empresas de la etapa 1.
Uso: python3 -I sonda9_ahold_y_financieras_en_zip.py <zip>
"""
import collections, re, sys, zipfile

z = zipfile.ZipFile(sys.argv[1])
names = [i.filename for i in z.infolist() if not i.is_dir()]
print('archivos (sin directorios):', len(names))
ah = [n for n in names if re.search(r'ahold|koninklijke|delhaize', n, re.I)]
print('(a) rutas con Ahold/Koninklijke/Delhaize:', ah)
xl = [n for n in names if re.search(r'\.xls[xm]?$', n, re.I)]
emp = collections.Counter(re.sub(r'(_v\d+.*|_evaluada.*|_V\d.*)$', '', n.rsplit('/', 1)[-1]) for n in xl)
print('    xlsx totales:', len(xl), '; ninguno con Ahold en el nombre:', not any(re.search('ahold', n, re.I) for n in xl))
fin_pat = re.compile(r'\b(bank|banco|banca|bancaria|insurance|insurer|aseguradora|seguros|reaseguro|SFCR|Solvency II|CET1|Pillar 3|Pilar 3)\b', re.I)
fin_nombres = [n for n in names if fin_pat.search(n.rsplit('/', 1)[-1])]
print('(b) archivos cuyo nombre sugiere entidad financiera:', fin_nombres)
# empresas con expediente: carpetas de empresas_v2 y de correcciones
emps = sorted({m.group(1) for n in names for m in [re.match(r'munger_v2_r1/personaje_v2/empresas_v2/([^/]+)/', n)] if m})
print('    empresas en empresas_v2:', emps)
print('(c) fixtures motor C:', [n for n in names if re.search(r'fixtures/Fixture_motorC', n)])
hits = collections.Counter()
ahold_txt = []
for n in names:
    if not re.search(r'\.(md|txt|csv|json|bat)$', n):
        continue
    t = z.read(n).decode('utf-8', 'replace')
    if re.search(r'116 empresas', t):
        hits[n] += 1
    if re.search(r'ahold', t, re.I) and 'MANIFIESTO' not in n and 'CAMBIOS_ARCHIVOS' not in n:
        ahold_txt.append(n)
print('(d) archivos que mencionan "116 empresas" (sin listarlas):', len(hits))
print('    archivos de texto que mencionan Ahold:', ahold_txt)
bat = [n for n in names if n.endswith('descargar_fuentes_ahold.bat')]
for b in bat:
    t = z.read(b).decode('utf-8', 'replace')
    print('    .bat:', b)
    for l in t.splitlines():
        if l.startswith('REM  ') and ('carpeta' in l or 'faltan' in l):
            print('       ', l.strip())
