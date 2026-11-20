"""Sonda 3: compara fuentes/huellas_fuentes_conservadas.csv (52fb120) con los bytes del ZIP base-4.14
y con FUENTES_CONSERVADAS.csv @ daa7478; cuenta los PDF del ZIP que no figuran en las huellas.
Uso: python3 -I sonda3_huellas_vs_zip.py <zip> <huellas.csv> <fuentes_conservadas_daa7478.csv>
"""
import csv, hashlib, sys, zipfile

ZP, HU, FC = sys.argv[1:4]
PRE = 'munger_v2_r1/'
z = zipfile.ZipFile(ZP)
nombres = {i.filename: i for i in z.infolist()}
filas = [r for r in csv.reader(open(HU, encoding='utf-8')) if r]
fc = {r['ruta_en_base_4_14']: r for r in csv.DictReader(open(FC, encoding='utf-8'))}
ok = mal = 0
pdfs_huella = set()
for ruta, by, sha, emp in filas:
    if not ruta.endswith('.pdf'):
        print('NO-PDF (fila de referencia):', ruta, by, sha, emp)
        continue
    pdfs_huella.add(ruta)
    info = nombres.get(PRE + ruta)
    if info is None:
        print('AUSENTE EN ZIP:', ruta); mal += 1; continue
    h = hashlib.sha256()
    with z.open(info) as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    s_ok = h.hexdigest() == sha and info.file_size == int(by)
    f_ok = ruta in fc and fc[ruta]['sha256'] == sha and fc[ruta]['bytes'] == by
    ok += s_ok; mal += not s_ok
    print(('OK ' if s_ok else 'MAL'), 'zip', ('fc_daa7478=OK' if f_ok else 'fc_daa7478=NO_FIGURA/DISTINTO'), emp, ruta)
print(f'PDF en huellas: {len(pdfs_huella)}; coinciden con el ZIP: {ok}; fallan: {mal}')
todos = sorted(n[len(PRE):] for n in nombres if n.lower().endswith('.pdf'))
fuera = [n for n in todos if n not in pdfs_huella]
print(f'PDF en el ZIP: {len(todos)}; sin huella en el paquete: {len(fuera)}')
for n in fuera:
    print('   sin huella:', n)
fc_pdf_si = [k for k, r in fc.items() if r['es_pdf_candidato'] == 'si']
print('filas es_pdf_candidato=si en FUENTES_CONSERVADAS daa7478:', len(fc_pdf_si),
      '; de ellas .pdf:', sum(k.endswith('.pdf') for k in fc_pdf_si),
      '; .pdf de FUENTES_CONSERVADAS ausentes de las huellas:', [k for k in fc if k.endswith('.pdf') and k not in pdfs_huella])
sys.exit(1 if mal else 0)
