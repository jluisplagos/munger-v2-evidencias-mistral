"""Regenera INVENTARIO_Y_HUECOS.csv y las huellas de TODAS las fuentes PDF desde el ZIP base-4.14.

Uso: python3 -I inventario_desde_zip.py <ruta_al_zip_base_4_14> <salida_inventario.csv> <salida_huellas.csv>

Alcance POSITIVO (todo bajo la raiz munger_v2_r1/ del ZIP):
  - personaje_v2/empresas_v2/<empresa>/...
  - personaje_v2/empresas_v2_correcciones/<ensayo>/<expediente o fuentes>/...
  - contrastes/<contraste>/...
Alcance NEGATIVO (se declara en la fila del ZIP con su recuento): v6/, documentacion_reparacion/,
kit_pipeline_munger/, los archivos sueltos de la raiz de munger_v2_r1/, lo que cuelga de
personaje_v2/ fuera de empresas_v2 y empresas_v2_correcciones, y el archivo suelto de la raiz de
empresas_v2_correcciones/. Ningun PDF queda fuera del alcance (los 71 estan dentro).
Ademas se emite una fila por cada .bat del alcance con su SHA-256 (p. ej. el de Ahold, conservado
pero NO ejecutado). Las filas de hueco son literales fijas; la fila de la Release lleva el SHA-256
completo del ZIP pasado por argumento. La salida es determinista: con el mismo ZIP, los dos CSV
son byte a byte identicos.
"""
import collections, csv, hashlib, os, sys, zipfile

RAIZ = 'munger_v2_r1/'

MOTORES_V2 = {
    'Aarsleff': 'A',
    'Hermes': 'A',
    'Nike': 'A',
    'Rational': 'A',
    'Vidrala': 'A en v2.0; B (V6.4) en 4.14',
    'Viscofan': 'B (v2.2)',
}

HUECOS = [
    ('Ahold Delhaize (reserva nombrada en MATRIZ_ALCANCE_4_14 §3)', 'sin conservar',
     'SIN Excel de etapa 1 (insumo no entregado); el .bat de descargas SÍ está conservado (fila propia con SHA-256), NO ejecutado; no se fuerza el caso'),
    ('Empresa financiera real (banco/aseguradora) para motor C', 'ninguna conservada',
     'solo 2 fixtures sintéticos (v6/pruebas/fixtures/LEEME.txt); falta fuente oficial con huella'),
]


def clasifica(rest):
    if rest.endswith('.xlsx'):
        return 'xlsx'
    if rest.endswith('.pdf'):
        return 'pdf'
    if rest.endswith('.json'):
        return 'json'
    if rest.endswith(('.md', '.txt')):
        return 'docs'
    return 'otros'


def recurso_de(name):
    if name.startswith('personaje_v2/empresas_v2/'):
        parts = name.split('/')
        if len(parts) > 3:
            return 'empresas_v2', parts[2], MOTORES_V2.get(parts[2], '')
        if len(parts) == 3:
            return 'empresas_v2', '(raiz)', ''
    elif name.startswith('personaje_v2/empresas_v2_correcciones/'):
        parts = name.split('/')
        if len(parts) > 4:
            ensayo, seg = parts[2], parts[3]
            if seg == 'fuentes':
                return f'correcciones · {ensayo}', f'{ensayo}/fuentes', ''
            return f'correcciones · {ensayo}', seg, ''
        if len(parts) == 4:
            return f'correcciones · {parts[2]}', f'{parts[2]}/(raiz)', ''
    elif name.startswith('contrastes/'):
        parts = name.split('/')
        if len(parts) > 2:
            return 'contrastes', parts[1], ''
    return None


def fuera_de(name):
    if recurso_de(name) is not None:
        return None
    top = name.split('/')[0]
    if top == 'v6':
        return 'v6/ (código del producto)'
    if top == 'documentacion_reparacion':
        return 'documentacion_reparacion/'
    if top == 'kit_pipeline_munger':
        return 'kit_pipeline_munger/'
    if top == 'personaje_v2':
        rest = name[len('personaje_v2/'):]
        if rest.startswith('empresas_v2_correcciones/') and '/' not in rest[len('empresas_v2_correcciones/'):]:
            return 'empresas_v2_correcciones/ (archivo suelto en la raíz)'
        return 'personaje_v2/ fuera de empresas_v2 y empresas_v2_correcciones'
    return 'raíz de munger_v2_r1/ (archivos sueltos)'


def sha256_zip_member(z, name):
    h = hashlib.sha256()
    with z.open(name) as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def main(zip_path, salida_inv, salida_huellas):
    zip_path = os.path.abspath(zip_path)
    with open(zip_path, 'rb') as f:
        zip_sha = hashlib.sha256()
        for chunk in iter(lambda: f.read(1 << 24), b''):
            zip_sha.update(chunk)
    zip_sha = zip_sha.hexdigest()
    zip_size = os.path.getsize(zip_path)
    zip_name = os.path.basename(zip_path)

    rows = collections.defaultdict(collections.Counter)
    huellas = []
    bats = []
    n_files = 0
    fuera = collections.Counter()
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            name = info.filename
            if name.endswith('/') or not name.startswith(RAIZ):
                continue
            n_files += 1
            rel = name[len(RAIZ):]
            r = recurso_de(rel)
            if r is None:
                fuera[fuera_de(rel)] += 1
                continue
            ubic, recurso, motor = r
            rows[(ubic, recurso)][clasifica(rel)] += 1
            rows[(ubic, recurso)]['__motor'] = motor
            if rel.endswith('.pdf'):
                huellas.append((rel, info.file_size, sha256_zip_member(z, name), recurso))
            elif rel.endswith('.bat'):
                bats.append((os.path.basename(rel), os.path.dirname(rel), sha256_zip_member(z, name)))

    n_dentro = sum(sum(c[k] for k in ('xlsx', 'json', 'docs', 'pdf', 'otros')) for c in rows.values())
    n_fuera = n_files - n_dentro
    detalle_fuera = '; '.join(f'{k}: {v}' for k, v in sorted(fuera.items()))

    with open(salida_inv, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['recurso', 'ubicacion', 'n_xlsx', 'n_json', 'n_docs', 'n_pdf', 'n_otros',
                    'motor_usado', 'hueco'])
        for (ubic, recurso) in sorted(rows):
            c = rows[(ubic, recurso)]
            w.writerow([recurso, ubic, c['xlsx'], c['json'], c['docs'], c['pdf'], c['otros'],
                        c.get('__motor', ''), ''])
        for recurso, ubic, sha in sorted(bats):
            w.writerow([recurso, ubic, '', '', '', '', '', '',
                        f'conservado en el ZIP; SHA-256 {sha}; NO ejecutado'])
        for recurso, ubic, hueco in HUECOS:
            w.writerow([recurso, ubic, '', '', '', '', '', '', hueco])
        w.writerow(['ZIP base-4.14 completo', 'release base-4.14', '', '', '', '', '', '',
                    f'{n_files} archivos en el ZIP; dentro del alcance: {n_dentro}; '
                    f'fuera (declarado): {n_fuera} [{detalle_fuera}]; SHA-256 {zip_sha}'])

    with open(salida_huellas, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        for rel, size, sha, recurso in sorted(huellas):
            w.writerow([rel, size, sha, recurso])
        w.writerow([f'release/{zip_name}', zip_size, zip_sha, 'producto'])

    print(f'{salida_inv}: {len(rows)} recursos + {len(bats)} .bat; {n_files} archivos en el ZIP '
          f'({n_dentro} dentro, {n_fuera} fuera declarado)')
    print(f'{salida_huellas}: {len(huellas)} PDF con SHA-256 completo + release {zip_sha}')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
