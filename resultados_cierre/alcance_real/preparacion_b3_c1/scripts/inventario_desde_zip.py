"""Regenera INVENTARIO_Y_HUECOS.csv y las huellas de TODAS las fuentes PDF desde el ZIP base-4.14.

Uso: python3 -I inventario_desde_zip.py <ruta_al_zip_base_4_14> <salida_inventario.csv> <salida_huellas.csv>

Alcance declarado (todo bajo la raiz munger_v2_r1/ del ZIP):
  - personaje_v2/empresas_v2/<empresa>/...
  - personaje_v2/empresas_v2_correcciones/<ensayo>/<expediente o fuentes>/...
  - contrastes/<contraste>/...
Las filas de hueco (Ahold, empresa financiera) son declaraciones fijas; la fila de la Release
lleva el SHA-256 completo del ZIP pasado por argumento. La salida es determinista: dados el
mismo ZIP, los dos CSV son byte a byte identicos.
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
     'SIN Excel de etapa 1 ni .bat ejecutado (insumo no entregado); no se fuerza el caso'),
    ('Empresa financiera real (banco/aseguradora) para motor C', 'ninguna conservada',
     'solo 2 fixtures sinteticos (v6/pruebas/fixtures/LEEME.txt); falta fuente oficial con huella'),
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
    n_files = 0
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            name = info.filename
            if name.endswith('/') or not name.startswith(RAIZ):
                continue
            n_files += 1
            rel = name[len(RAIZ):]
            r = recurso_de(rel)
            if r is None:
                continue
            ubic, recurso, motor = r
            rows[(ubic, recurso)][clasifica(rel)] += 1
            rows[(ubic, recurso)]['__motor'] = motor
            if rel.endswith('.pdf'):
                huellas.append((rel, info.file_size, sha256_zip_member(z, name), recurso))

    with open(salida_inv, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['recurso', 'ubicacion', 'n_xlsx', 'n_json', 'n_docs', 'n_pdf', 'n_otros',
                    'motor_usado', 'hueco'])
        for (ubic, recurso) in sorted(rows):
            c = rows[(ubic, recurso)]
            w.writerow([recurso, ubic, c['xlsx'], c['json'], c['docs'], c['pdf'], c['otros'],
                        c.get('__motor', ''), ''])
        for recurso, ubic, hueco in HUECOS:
            w.writerow([recurso, ubic, '', '', '', '', '', '', hueco])
        w.writerow(['ZIP base-4.14 completo', 'release base-4.14', '', '', '', '', '', '',
                    f'{n_files} archivos; SHA-256 {zip_sha}'])

    with open(salida_huellas, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        for rel, size, sha, recurso in sorted(huellas):
            w.writerow([rel, size, sha, recurso])
        w.writerow([f'release/{zip_name}', zip_size, zip_sha, 'producto'])

    n_pdf = len(huellas)
    print(f'{salida_inv}: {len(rows)} recursos, {n_files} archivos en el ZIP')
    print(f'{salida_huellas}: {n_pdf} PDF con SHA-256 completo + release {zip_sha}')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
