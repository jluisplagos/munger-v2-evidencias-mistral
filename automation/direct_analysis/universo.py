#!/usr/bin/env python3
"""Paquetes del análisis directo para empresas del universo de etapa 1 (segunda vuelta).

Herramienta local, sin API y sin red: el workflow del análisis directo no la ejecuta. Para
cada empresa pedida lee la Release del universo con las mismas comprobaciones que el cribado
(`screening.open_release`: huella y tamaño del ZIP fijados, lista blanca de rutas, empresas
del examen excluidas) y escribe en `datos_analisis_directo/<slug>/etapa1/` su etapa 1 en
texto:

- `<Empresa>_respuesta.md` y, si existe, `<Empresa>_cambios_v2.md`, byte a byte;
- una hoja del `<Empresa>_evaluada.xlsx` por CSV (`<Empresa>_evaluada__<Hoja>.csv`), con el
  mismo lector en solo lectura que el cribado (`screening.read_xlsx`: valores guardados sin
  redondear, fechas a ISO, `#SIN_VALOR_CALCULADO` si una fórmula no guardó valor, primera
  columna = número de fila). Se escriben todas las hojas del libro, como en los paquetes del
  examen.

Y el manifiesto `automation/direct_analysis/paquetes/universo_<slug>.json`, con la fecha de
corte = «Fecha de análisis» de la hoja. El universo no trae fuentes oficiales ni datos
verificados: el paquete es solo la etapa 1, y la descripción lo dice.

Antes de escribir aplica las capas de ceguera del lanzador sobre cada texto (copia exacta,
menciones prohibidas, solape con material ciego). Una empresa que no las pasa queda como
NO_PREPARADA con el código y no se escribe nada suyo: el análisis directo no admite
excepciones (las de `excepciones_ceguera.json` son solo del cribado). Después, cada paquete
se comprueba con `direct_analysis.py` sin `--execute-api` (cota, reserva, huellas).
"""
import argparse
import datetime
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'automation/screening'))
import screening as sc  # noqa: E402  (importa direct_analysis, critical_review y pilot)

da, pilot = sc.da, sc.pilot
PREFIJO_MANIFIESTO = 'universo_'
DESCRIPCIONES = {
    'respuesta': 'Respuesta de etapa 1 (juicio heredado; tratar como hipótesis)',
    'cambios_v2': 'Cambios de la versión 1 a la 2 del libro de etapa 1, de la propia persona',
}


def nombre_hoja(hoja):
    """Nombre de archivo admitido por la lista blanca del lanzador ([\\w. -])."""
    limpio = re.sub(r'[^\w.-]+', '_', hoja.strip()).strip('_')
    if not limpio:
        raise pilot.PilotError('HOJA_SIN_NOMBRE_UTILIZABLE')
    return limpio


def fecha_iso(valor):
    if isinstance(valor, str):
        m = re.fullmatch(r'(\d{4}-\d{2}-\d{2})(?:[ T].*)?', valor.strip())
        if m:
            datetime.date.fromisoformat(m.group(1))
            return m.group(1)
        m = re.fullmatch(r'(\d{1,2})[/.-](\d{1,2})[/.-](\d{4})', valor.strip())
        if m:
            return datetime.date(int(m.group(3)), int(m.group(2)), int(m.group(1))).isoformat()
    raise pilot.PilotError('FECHA_DE_ANALISIS_NO_LEGIBLE')


def preparar_empresa(release, empresa, blind):
    """{ruta: bytes} del paquete de una empresa y su manifiesto; PilotError si no se puede."""
    if empresa not in release.companies:
        raise pilot.PilotError('EMPRESA_NO_ESTA_EN_LA_RELEASE')
    if empresa in sc.EXCLUIDAS:
        raise pilot.PilotError(sc.EXCLUIDA)
    slug = sc.slug(empresa)
    da._slug(slug, 'EMPRESA_INVALIDA')
    base = f'{da.DATA_ROOT}/{slug}/etapa1'
    files = release.companies[empresa]
    salida, archivos = {}, []
    for kind in ('respuesta', 'cambios_v2'):
        if kind in files:
            raw = sc._member(release.zip, files[kind], sc.MAX_MD_BYTES)
            sc._text(raw, kind)
            ruta = f"{base}/{files[kind].filename.rsplit('/', 1)[1]}"
            salida[ruta] = raw
            archivos.append({'id': kind, 'ruta': ruta, 'descripcion': DESCRIPCIONES[kind]})
    libro = sc._member(release.zip, files['libro'], sc.MAX_XLSX_BYTES)
    hojas = sc.read_xlsx(libro)
    for hoja, (texto, _faltan) in hojas.items():
        ruta = f'{base}/{empresa}_evaluada__{nombre_hoja(hoja)}.csv'
        if ruta in salida:
            raise pilot.PilotError('HOJAS_CON_EL_MISMO_NOMBRE_DE_ARCHIVO')
        salida[ruta] = texto.encode('utf-8')
        archivos.append({'id': 'hoja_' + re.sub(r'[^a-z0-9]+', '_', da.fold(hoja)).strip('_')[:35],
                         'ruta': ruta, 'descripcion': f'Excel de etapa 1 en texto (CSV, valores guardados), hoja {hoja}'})
    for a in archivos:
        da.check_path(a['ruta'], slug)
        da._meta_text(a['descripcion'], 300)
        source = {'id': a['id'], 'text': salida[a['ruta']].decode('utf-8')}
        codes = sc.blind_codes(source, blind)
        if codes:
            raise pilot.PilotError(codes[0])
    if 'Análisis' not in hojas:
        raise pilot.PilotError('HOJA_AUSENTE_EN_EL_LIBRO:hoja_analisis')
    fecha = fecha_iso(sc.sheet_date([{'id': 'hoja_analisis', 'text': hojas['Análisis'][0]}]))
    caso = da._meta_text(f'{empresa}, etapa 1 del universo (hoja del {fecha})', 100)
    manifiesto = {'empresa': slug, 'caso': caso, 'fecha_corte': fecha,
                  'archivos': [{**a, 'sha256': pilot.digest(salida[a['ruta']])} for a in archivos]}
    salida[f'automation/direct_analysis/paquetes/{PREFIJO_MANIFIESTO}{slug.replace("-", "_")}.json'] = (
        json.dumps(manifiesto, ensure_ascii=False, indent=1) + '\n').encode('utf-8')
    return salida


def preparar(release, empresas, blind):
    hechos, fallos = {}, {}
    for empresa in empresas:
        try:
            hechos[empresa] = preparar_empresa(release, empresa, blind)
        except pilot.PilotError as err:
            fallos[empresa] = 'NO_PREPARADA:' + str(err)
    return hechos, fallos


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--release', type=Path, required=True, help='universo_etapa1.zip.zip descargado de la Release')
    p.add_argument('--empresas', required=True, help='nombres de carpeta de la Release, separados por comas')
    p.add_argument('--escribir', action='store_true', help='escribe los archivos (sin esto, solo informa)')
    a = p.parse_args(argv)
    try:
        release = sc.open_release(a.release)
        names = [n.strip() for n in a.empresas.split(',') if n.strip()]
        code_sha = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, capture_output=True, text=True,
                                  check=True).stdout.strip()
        blind = da.blind_material(ROOT, [code_sha])
        hechos, fallos = preparar(release, names, blind)
    except (pilot.PilotError, subprocess.CalledProcessError, OSError) as err:
        print(str(err), file=sys.stderr)
        return 2
    for empresa, datos in hechos.items():
        for ruta, raw in datos.items():
            if a.escribir:
                destino = ROOT / ruta
                destino.parent.mkdir(parents=True, exist_ok=True)
                destino.write_bytes(raw)
            print(f'{empresa}\t{pilot.digest(raw)}\t{len(raw)}\t{ruta}')
    for empresa, motivo in fallos.items():
        print(f'{empresa}\t{motivo}')
    return 0 if hechos and not fallos else (1 if hechos else 2)


if __name__ == '__main__':
    sys.exit(main())
