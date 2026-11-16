"""Regenera INVENTARIO_Y_HUECOS.csv desde el listado de un ZIP base-4.14 materializado.
Uso: python3 -I inventario_desde_zip.py <ruta_al_listado_unzip_-l> <salida.csv>
Solo cuenta recursos bajo personaje_v2/empresas_v2 y empresas_v2_correcciones/.../2026-11_Vidrala_ensayo_4_14.
"""
import re, sys, collections, csv

def main(listado, salida):
    rows = collections.defaultdict(lambda: collections.Counter())
    for ln in open(listado, encoding='utf-8', errors='replace'):
        m = re.search(r'(munger_v2_r1/personaje_v2/empresas_v2/[^/]+)/(.+)$', ln)
        if m:
            emp, rest = m.groups()
            k = 'xlsx' if rest.endswith('.xlsx') else 'pdf' if rest.endswith('.pdf') else 'json' if rest.endswith('.json') else 'docs' if rest.endswith(('.md', '.txt')) else 'otros'
            rows[('empresas_v2', emp.split('/')[-1])][k] += 1
            continue
        m2 = re.search(r'(empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/(\w+)(?:_decisiones(?:_INVALIDO_perdio_analisis)?)?/)(.+)$', ln)
        if m2 and m2.group(2) in ('elis', 'elis_motor_A', 'vidrala', 'vidrala_decisiones', 'viscofan', 'viscofan_decisiones', 'documentacion_cierre_4_14'):
            k = 'xlsx' if m2.group(3).endswith('.xlsx') else 'pdf' if m2.group(3).endswith('.pdf') else 'json' if m2.group(3).endswith('.json') else 'docs' if m2.group(3).endswith(('.md', '.txt')) else 'otros'
            rows[('correcciones 4.14', m2.group(2))][k] += 1
    with open(salida, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['recurso', 'ubicacion', 'n_xlsx', 'n_json', 'n_docs', 'n_pdf', 'n_otros', 'motor_usado', 'hueco'])
        for (ubic, name) in sorted(rows):
            c = rows[(ubic, name)]
            w.writerow([name, ubic, c['xlsx'], c['json'], c['docs'], c['pdf'], c['otros'], '', ''])
    print(f'{salida}: {len(rows)} recursos')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
