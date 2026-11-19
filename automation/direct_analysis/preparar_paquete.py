#!/usr/bin/env python3
"""Prepara un paquete del análisis directo a partir de una receta declarada (sin API, sin red).

Herramienta local de quien hace el paquete; el workflow no la ejecuta. Cada archivo del
paquete sale de un insumo con huella fijada en la receta:

- `git`: copia byte a byte de un archivo de un commit fijado (p. ej. los datos verificados
  del expediente del producto o la etapa 1 de la rama de fuentes);
- `pdf`: PDF de la Release, pasado a texto página a página con `pdftotext -layout`
  (marca `[PDF PAGE n]`, el mismo método que los textos del producto), con una selección
  declarada de páginas y los espacios repetidos unidos;
- `texto_paginas`: lo mismo sobre un texto que ya tiene las marcas `[PDF PAGE n]`;
- `html`: comunicado HTML de la Release a texto (sin scripts ni estilos; cada fila de tabla
  en una línea, celdas separadas por « | »), entre dos frases literales declaradas;
- `xlsx_hoja`: una hoja del Excel evaluado en CSV con los valores guardados, solo lectura
  y filas vacías fuera (el método que reproduce los CSV de Ahold, Jumbo y Zoetis);
- `lineas`: las líneas declaradas de un texto, con una cabecera (p. ej. la cotización
  hasta la fecha de corte de una transcripción más larga).

Cualquier origen admite ediciones declaradas sobre la copia (`retirar`, `reemplazos`);
el original no se toca y la descripción del manifiesto lo dice.

Un insumo es un archivo de `--insumos` (`insumo`; con `miembro`, ese archivo dentro de
un ZIP cuya huella es `sha256_zip`) o, si el origen lleva `commit`, el
archivo `ruta` de ese commit del clon indicado con `--repo nombre=ruta`.

`construir` escribe los archivos y el manifiesto; `comprobar` los vuelve a generar en
memoria y los compara con los del repositorio (bytes y huellas del manifiesto). Ninguna de
las dos llama a la API ni cambia los controles del lanzador: el paquete se valida después
con `direct_analysis.py` en modo sin API.
"""
import argparse
import csv
import hashlib
import io
import json
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[2]
PAGE = re.compile(r'(?m)^(?=\[PDF PAGE \d+\])')
PAGE_NUM = re.compile(r'\[PDF PAGE (\d+)\]')


class RecetaError(Exception):
    pass


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


# --- Texto con marcas de página ----------------------------------------------------------
def pdf_a_texto(pdf):
    """Una llamada a pdftotext -layout por página, como el texto/ de los expedientes."""
    info = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True, check=True).stdout
    n = int(next(line.split()[1] for line in info.splitlines() if line.startswith('Pages:')))
    pages = []
    for p in range(1, n + 1):
        out = subprocess.run(['pdftotext', '-f', str(p), '-l', str(p), '-layout', str(pdf), '-'],
                             capture_output=True, check=True).stdout.decode('utf-8')
        pages.append(f'[PDF PAGE {p}]\n' + out.replace('\f', ''))
    return '\n'.join(pages) + '\n'


def rangos(spec):
    """'3-8,23-38' -> [3..8, 23..38] en orden y sin repetir."""
    out = []
    for part in spec.split(','):
        a, _, b = part.strip().partition('-')
        lo, hi = int(a), int(b or a)
        if lo < 1 or hi < lo:
            raise RecetaError('RANGO_DE_PAGINAS_INVALIDO:' + part)
        out += [p for p in range(lo, hi + 1) if p not in out]
    return out


def seleccionar(texto, paginas):
    partes = {int(PAGE_NUM.match(p).group(1)): p for p in PAGE.split(texto) if PAGE_NUM.match(p)}
    falta = [p for p in paginas if p not in partes]
    if falta:
        raise RecetaError('PAGINAS_INEXISTENTES:' + ','.join(map(str, falta)))
    return ''.join(partes[p] for p in paginas)


def compactar(texto):
    """Espacios repetidos unidos y como mucho una línea en blanco seguida (método de los paquetes)."""
    return re.sub(r'\n{3,}', '\n\n', re.sub(r' {2,}', ' ', texto))


def con_cabecera(cabecera, cuerpo):
    if not cabecera or '\n' in cabecera:
        raise RecetaError('CABECERA_INVALIDA')
    return cabecera + '\n\n' + cuerpo


# --- HTML -------------------------------------------------------------------------------
class _Html(HTMLParser):
    SKIP = {'script', 'style', 'noscript', 'svg', 'head', 'template'}
    BLOCK = {'p', 'div', 'br', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table', 'section', 'article',
             'header', 'footer', 'ul', 'ol', 'thead', 'tbody'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip, self.row = [], 0, None

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
        elif tag == 'tr':
            self.row = []
        elif tag in ('td', 'th') and self.row is not None:
            self.row.append([])
        elif self.row is not None and self.row:
            self.row[-1].append(' ')
        elif tag in self.BLOCK:
            self.out.append('\n')

    def handle_endtag(self, tag):
        if tag in self.SKIP:
            self.skip = max(0, self.skip - 1)
        elif tag == 'tr' and self.row is not None:
            cells = [c for c in (re.sub(r'\s+', ' ', ''.join(x)).strip() for x in self.row) if c]
            if cells:
                self.out.append('\n' + ' | '.join(cells) + '\n')
            self.row = None
        elif tag in self.BLOCK and self.row is None:
            self.out.append('\n')

    def handle_data(self, data):
        if self.skip:
            return
        if self.row is not None:
            if self.row:
                self.row[-1].append(data)
        else:
            self.out.append(data)


def html_a_texto(raw, desde, hasta):
    p = _Html()
    p.feed(raw.decode('utf-8'))
    p.close()
    t = ''.join(p.out)
    t = re.sub(r'[ \t\xa0]+', ' ', t)
    t = re.sub(r' *\n *', '\n', t)
    t = re.sub(r'\n{2,}', '\n', t)
    i = t.find(desde)
    j = t.find(hasta, i + 1) if i >= 0 else -1
    if i < 0 or j < 0:
        raise RecetaError('LIMITES_DEL_HTML_NO_ENCONTRADOS')
    return t[i:j + len(hasta)].strip() + '\n'


# --- Excel ------------------------------------------------------------------------------
def xlsx_hoja_csv(raw, hoja):
    import openpyxl  # solo en el equipo de quien prepara el paquete
    wb = openpyxl.load_workbook(io.BytesIO(raw), read_only=True, data_only=True)
    if hoja not in wb.sheetnames:
        raise RecetaError('HOJA_NO_ENCONTRADA:' + hoja)
    buf = io.StringIO()
    w = csv.writer(buf)
    for row in wb[hoja].iter_rows(values_only=True):
        if all(v is None or v == '' for v in row):
            continue
        w.writerow(['' if v is None else v for v in row])
    return buf.getvalue()


# --- Receta -----------------------------------------------------------------------------
def leer_insumo(origen, insumos, repos):
    if 'commit' in origen:  # archivo de un commit fijado (tipo git, o insumo de texto versionado)
        repo = repos.get(origen['repo'])
        if repo is None:
            raise RecetaError('REPO_NO_INDICADO:' + origen['repo'])
        raw = subprocess.run(['git', '-C', str(repo), 'show', f"{origen['commit']}:{origen['ruta']}"],
                             capture_output=True, check=True).stdout
    else:
        path = Path(insumos) / origen['insumo']
        if not path.is_file() or path.is_symlink():
            raise RecetaError('INSUMO_NO_ENCONTRADO:' + origen['insumo'])
        raw = path.read_bytes()
        if 'miembro' in origen:  # un archivo dentro de un ZIP de la Release (p. ej. la del universo)
            if sha256(raw) != origen['sha256_zip']:
                raise RecetaError('HUELLA_DEL_ZIP_DISTINTA:' + origen['insumo'])
            with zipfile.ZipFile(io.BytesIO(raw)) as zf:
                raw = zf.read(origen['miembro'])
    if sha256(raw) != origen['sha256']:
        raise RecetaError('HUELLA_DEL_INSUMO_DISTINTA:' + origen.get('insumo', origen.get('ruta', '')))
    return raw


def editar(raw, o):
    """Ediciones declaradas en la receta sobre una copia (nunca sobre el original).

    `retirar`: tramos desde la frase `desde` (incluida) hasta la frase `hasta` (excluida),
    cada frase una sola vez en el texto. `reemplazos`: cambios literales `de` -> `a` con el
    número exacto de apariciones (`veces`).
    """
    if not o.get('retirar') and not o.get('reemplazos'):
        return raw
    t = raw.decode('utf-8')
    for r in o.get('retirar', ()):
        if t.count(r['desde']) != 1 or t.count(r['hasta']) != 1 or t.index(r['desde']) > t.index(r['hasta']):
            raise RecetaError('TRAMO_A_RETIRAR_NO_UNICO:' + r['desde'][:40])
        t = t[:t.index(r['desde'])] + t[t.index(r['hasta']):]
    for r in o.get('reemplazos', ()):
        if t.count(r['de']) != r['veces']:
            raise RecetaError('REEMPLAZO_CON_OTRO_NUMERO_DE_APARICIONES:' + r['de'][:40])
        t = t.replace(r['de'], r['a'])
    return t.encode('utf-8')


def generar(archivo, insumos, repos, cache):
    return editar(_generar(archivo, insumos, repos, cache), archivo['origen'])


def _generar(archivo, insumos, repos, cache):
    o = archivo['origen']
    key = (o.get('miembro') or o.get('insumo') or o.get('ruta'), o['sha256'])
    raw = cache.get(key)
    if raw is None:
        raw = cache[key] = leer_insumo(o, insumos, repos)
    tipo = o['tipo']
    if tipo == 'git':
        return raw
    if tipo == 'pdf':
        texto = cache.get(key + ('txt',))
        if texto is None:
            p = Path(insumos) / o['insumo']
            texto = cache[key + ('txt',)] = pdf_a_texto(p)
        cuerpo = seleccionar(texto, rangos(o['paginas'])) if o.get('paginas') else texto
        return con_cabecera(o['cabecera'], compactar(cuerpo)).encode('utf-8')
    if tipo == 'texto_paginas':
        cuerpo = seleccionar(raw.decode('utf-8'), rangos(o['paginas'])) if o.get('paginas') else raw.decode('utf-8')
        return con_cabecera(o['cabecera'], compactar(cuerpo)).encode('utf-8')
    if tipo == 'html':
        return con_cabecera(o['cabecera'], html_a_texto(raw, o['desde'], o['hasta'])).encode('utf-8')
    if tipo == 'xlsx_hoja':
        return xlsx_hoja_csv(raw, o['hoja']).encode('utf-8')
    if tipo == 'lineas':
        lineas = raw.decode('utf-8').splitlines()
        sel = [lineas[n - 1] for n in rangos(o['lineas']) if n <= len(lineas)]
        if len(sel) != len(rangos(o['lineas'])):
            raise RecetaError('LINEAS_INEXISTENTES')
        return con_cabecera(o['cabecera'], '\n'.join(sel) + '\n').encode('utf-8')
    raise RecetaError('TIPO_DE_ORIGEN_DESCONOCIDO:' + tipo)


def cargar_receta(path):
    receta = json.loads(Path(path).read_text(encoding='utf-8'))
    if set(receta) - {'paquete', 'empresa', 'caso', 'fecha_corte', 'notas', 'archivos'}:
        raise RecetaError('RECETA_CON_CLAVES_DESCONOCIDAS')
    if not re.fullmatch(r'[a-z0-9][a-z0-9_-]{0,60}', receta['paquete']):
        raise RecetaError('NOMBRE_DE_PAQUETE_INVALIDO')
    prefix = f"datos_analisis_directo/{receta['empresa']}/"
    for a in receta['archivos']:
        if not a['ruta'].startswith(prefix) or '..' in PurePosixPath(a['ruta']).parts:
            raise RecetaError('RUTA_FUERA_DE_LA_EMPRESA:' + a['ruta'])
    return receta


def manifiesto(receta, datos):
    archivos = []
    for a in receta['archivos']:
        entry = {'id': a['id'], 'ruta': a['ruta'], 'sha256': sha256(datos[a['ruta']]),
                 'descripcion': a['descripcion']}
        archivos.append(entry)
    doc = {'empresa': receta['empresa'], 'caso': receta['caso'], 'fecha_corte': receta['fecha_corte'],
           'archivos': archivos}
    return (json.dumps(doc, ensure_ascii=False, indent=1) + '\n').encode('utf-8')


def ruta_manifiesto(receta):
    return f"automation/direct_analysis/paquetes/{receta['paquete']}.json"


def construir(receta, insumos, repos, root=ROOT, escribir=True):
    cache, datos = {}, {}
    for a in receta['archivos']:
        datos[a['ruta']] = generar(a, insumos, repos, cache)
    datos[ruta_manifiesto(receta)] = manifiesto(receta, datos)
    if escribir:
        for ruta, raw in datos.items():
            p = Path(root) / ruta
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(raw)
    return datos


def comprobar(receta, insumos, repos, root=ROOT):
    diferentes = []
    for ruta, raw in construir(receta, insumos, repos, root, escribir=False).items():
        p = Path(root) / ruta
        if not p.is_file() or p.read_bytes() != raw:
            diferentes.append(ruta)
    return diferentes


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('accion', choices=('construir', 'comprobar'))
    ap.add_argument('receta', type=Path)
    ap.add_argument('--insumos', type=Path, required=True, help='carpeta con los assets de la Release')
    ap.add_argument('--repo', action='append', default=[], help='nombre=ruta de un clon (para origen git)')
    a = ap.parse_args(argv)
    repos = dict(r.split('=', 1) for r in a.repo)
    try:
        receta = cargar_receta(a.receta)
        if a.accion == 'construir':
            datos = construir(receta, a.insumos, repos)
            for ruta, raw in datos.items():
                print(f'{sha256(raw)}  {len(raw):>8}  {ruta}')
            return 0
        diff = comprobar(receta, a.insumos, repos)
        print('IGUAL' if not diff else 'DISTINTO:\n' + '\n'.join(diff))
        return 0 if not diff else 1
    except (RecetaError, subprocess.CalledProcessError, KeyError, ValueError) as err:
        print(f'ERROR {type(err).__name__}: {err}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
