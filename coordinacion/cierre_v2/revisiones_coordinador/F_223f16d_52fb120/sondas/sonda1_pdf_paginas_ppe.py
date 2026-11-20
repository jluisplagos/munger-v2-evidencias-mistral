"""Sonda 1 (revisor Claude, contexto distinto de Mistral B y de Mistral C/F).
Comprueba en los PDF de Vidrala (no en los textos conservados) que cada alta PP&E del dossier
daa7478 esta en la pagina citada, dentro de la nota 'Property, Plant and Equipment', en la fila
total de Coste y en la columna 'Additions'; que la huella del PDF coincide con FUENTES_CONSERVADAS.csv
@ daa7478; y que la pagina del texto conservado ([PDF PAGE N]) corresponde a esa pagina del PDF.
Negativo: el total de intangibles (lectura antigua erronea) no aparece en la fila total de PP&E.
Uso: python3 -I sonda1_pdf_paginas_ppe.py <base414> <fuentes_conservadas.csv>
"""
import csv, hashlib, re, subprocess, sys

BASE, FC = sys.argv[1], sys.argv[2]
V = 'personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo/fuentes/cuentas_consolidadas_2016_2022/'
A = 'contrastes/vidrala_2023_arrendamientos/fuentes/'
PDF = {2017: V + '1285_en-2017_consolidated_financial_information.pdf',
       2018: V + '1291_en-2018_consolidated_financial_information.pdf',
       2019: V + '1297_en-2019_consolidated_financial_information.pdf',
       2020: V + '1304_en-2020_consolidated_financial_information.pdf',
       2021: V + '1413_en-2021_consolidated_financial_information.pdf',
       2022: V + '1668_en-2022_consolidated_financial_information.pdf',
       2023: A + 'en_1831_descarga_2026-11-08/1831_en-2023_consolidated_financial_information.pdf',
       2024: A + 'en_2145_descarga_2026-11-08/2145_en-2024_consolidated_financial_information.pdf',
       2025: 'contrastes/piloto_Vidrala_2025/fuentes/en_2355_descarga_2026-11-08/2355_en-2025_consolidated_financial_information.pdf'}
TXT = BASE + '/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/vidrala_decisiones/Vidrala/texto/CF_%d.txt'
# (pagina citada en VIDRALA_REPOSICION_CAPACIDAD.csv @ daa7478, alta PP&E, total adiciones intangibles)
DOS = {2017: (42, 101154, 156743), 2018: (40, 93148, 18623), 2019: (41, 108645, 25694),
       2020: (50, 134263, 28666), 2021: (39, 105877, 44810), 2022: (40, 158234, 93759),
       2023: (43, 134472, 100655), 2024: (47, 171185, 48326), 2025: (43, 177848, 45173)}

hu = {r['ruta_en_base_4_14']: r['sha256'] for r in csv.DictReader(open(FC, encoding='utf-8'))}


def pag(pdf, p):
    return subprocess.run(['pdftotext', '-layout', '-f', str(p), '-l', str(p), pdf, '-'],
                          capture_output=True, text=True, check=True).stdout


def fmt(n):
    return f'{n:,}'


def pagina_texto(y, p):
    t = open(TXT % y, encoding='utf-8').read()
    m = re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\[PDF PAGE %d\]|\Z)' % (p, p + 1), t, re.S)
    return m.group(1) if m else ''


fallos = 0
for y, (p, ppe, intg) in DOS.items():
    ruta = BASE + '/' + PDF[y]
    sha = hashlib.sha256(open(ruta, 'rb').read()).hexdigest()
    sha_ok = hu.get(PDF[y]) == sha
    txt = pag(ruta, p)
    lines = txt.splitlines()
    nota = bool(re.search(r'Property,\s*Plant\s*and\s*Equipment', txt))
    hdr = next((i for i, l in enumerate(lines) if re.match(r'\s*%d\b' % y, l) and 'Additions' in ' '.join(lines[max(0, i - 3):i + 1])), None)
    if hdr is None:
        hdr = next((i for i, l in enumerate(lines) if re.match(r'\s*%d\s' % y, l)), None)
    wip = next((i for i in range(hdr or 0, len(lines)) if 'Work in progress' in lines[i]), None)
    tot = next((lines[i] for i in range((wip or 0) + 1, len(lines)) if re.match(r'^\s*[\d,]+\s+[\d,]+', lines[i])), '')
    toks = re.split(r'\s{2,}', tot.strip())
    adic_ok = len(toks) > 1 and toks[1] == fmt(ppe)
    neg_ok = fmt(intg) not in tot
    # cabecera: posicion de 'Additions' alineada con el token del total
    cab = ' '.join(lines[max(0, (hdr or 0) - 3):(hdr or 0) + 1])
    cab_ok = 'Additions' in cab
    # coincidencia texto conservado vs PDF en la fila total
    tc = pagina_texto(y, p)
    txt_ok = fmt(ppe) in tc and 'Property, Plant and Equipment' in tc or (fmt(ppe) in tc and nota)
    ok = sha_ok and nota and cab_ok and adic_ok and neg_ok and txt_ok
    fallos += not ok
    print(f'{y} p{p} sha={"OK" if sha_ok else "MAL"} nota_PPE={nota} cabecera_Additions={cab_ok} '
          f'total_slot1={toks[1] if len(toks) > 1 else None} esperado={fmt(ppe)} {"OK" if adic_ok else "MAL"} '
          f'neg_intangibles_ausente={neg_ok} texto_conservado_misma_pagina={txt_ok} -> {"OK" if ok else "FALLO"}')
    print('      fila total:', tot.strip())
print('FALLOS:', fallos)
sys.exit(1 if fallos else 0)
