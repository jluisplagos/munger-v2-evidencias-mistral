"""Copia insumos seleccionados y comprobados; no ejecuta ni modifica el producto."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import tempfile
import urllib.request
import urllib.parse
import zipfile

TAREA = Path(__file__).resolve().parents[1]
REPO = TAREA.parents[1]


def huella(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda: f.read(1024 * 1024), b''):
            h.update(b)
    return h.hexdigest()


def comprobar_destino():
    r = subprocess.run(['git', 'remote', 'get-url', 'origin'], cwd=REPO,
                       check=True, capture_output=True, text=True)
    remote = r.stdout.strip().removesuffix('/').removesuffix('.git')
    # El proveedor puede inyectar autenticación en HTTPS; nunca mostrarla.
    if remote.startswith('https://'):
        parsed = urllib.parse.urlsplit(remote)
        remote = 'https://' + (parsed.hostname or '') + parsed.path
    permitidos = {'https://github.com/jluisplagos/munger-v2-evidencias-mistral',
                  'git@github.com:jluisplagos/munger-v2-evidencias-mistral'}
    if remote not in permitidos:
        raise ValueError('origin no es el repositorio auxiliar autorizado; no se copia ningún insumo')


def ruta_segura(root, relative):
    p = PurePosixPath(relative)
    if p.is_absolute() or '..' in p.parts or not p.parts:
        raise ValueError('ruta de insumo no válida')
    dest = root.joinpath(*p.parts)
    if not dest.resolve().is_relative_to(root.resolve()):
        raise ValueError('la ruta sale del directorio de trabajo')
    return dest


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--zip', type=Path, help='ZIP original completo de la base 4.14')
    g.add_argument('--base-tree', type=Path, help='directorio munger_v2_r1 existente, solo lectura')
    g.add_argument('--download', action='store_true', help='descarga única del ZIP original')
    a = ap.parse_args()
    comprobar_destino()
    cfg = json.loads((TAREA / 'entrada/configuracion.json').read_text(encoding='utf-8'))
    idx = json.loads((TAREA / 'entrada/indice_fuentes.json').read_text(encoding='utf-8'))
    trabajo = REPO / '.trabajo'
    trabajo.mkdir(exist_ok=True)
    if trabajo.is_symlink():
        raise ValueError('.trabajo no puede ser un enlace simbólico')
    final = trabajo / 'insumos_m2'
    if final.exists():
        raise ValueError('ya existe .trabajo/insumos_m2; conservarlo y comprobarlo, no sobrescribir')
    archive = a.zip
    if a.download:
        archive = trabajo / 'base414.zip'
        if not archive.exists():
            needed = cfg['zip_bytes'] + sum(x['bytes'] for x in idx['archivos']) + 64 * 1024 * 1024
            if shutil.disk_usage(trabajo).free < needed:
                raise ValueError('espacio insuficiente para descargar y preparar la selección; no se inicia la descarga')
            tmp = trabajo / 'base414.zip.partial'
            request = urllib.request.Request(cfg['zip_url'], headers={'User-Agent': 'Munger-evidencia/1.0'})
            with urllib.request.urlopen(request, timeout=90) as src, tmp.open('wb') as dst:
                shutil.copyfileobj(src, dst, 1024 * 1024)
            tmp.replace(archive)
    if archive:
        if archive.stat().st_size != cfg['zip_bytes'] or huella(archive) != cfg['zip_sha256']:
            raise ValueError('el ZIP no coincide con la base fijada; no se extrae')
    # Se ignoran cachés y binarios en Git; la configuración solo se añade en el auxiliar.
    # En worktrees .git puede ser un archivo: usar git para obtener la ruta correcta.
    gitdir = subprocess.check_output(['git', 'rev-parse', '--git-path', 'info/exclude'], cwd=REPO, text=True).strip()
    exclude = Path(gitdir)
    if not exclude.is_absolute():
        exclude = REPO / exclude
    exclude.parent.mkdir(parents=True, exist_ok=True)
    old = exclude.read_text() if exclude.exists() else ''
    if '/.trabajo/' not in old.splitlines():
        exclude.write_text(old + '\n/.trabajo/\n', encoding='utf-8')
    with tempfile.TemporaryDirectory(prefix='preparacion-', dir=trabajo) as temporary:
        staging = Path(temporary) / 'insumos'
        staging.mkdir()
        if archive:
            with zipfile.ZipFile(archive) as z:
                for item in idx['archivos']:
                    dest = ruta_segura(staging, item['ruta'])
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    member = cfg['zip_root'] + '/' + item['ruta']
                    with z.open(member) as src, dest.open('wb') as dst:
                        shutil.copyfileobj(src, dst)
        else:
            root = a.base_tree.resolve()
            for item in idx['archivos']:
                src = ruta_segura(root, item['ruta'])
                dest = ruta_segura(staging, item['ruta'])
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, dest)
        for item in idx['archivos']:
            p = ruta_segura(staging, item['ruta'])
            if p.stat().st_size != item['bytes'] or huella(p) != item['sha256']:
                raise ValueError('insumo no conforme: ' + item['ruta'])
        staging.replace(final)
    print(json.dumps({'seleccion_conforme': len(idx['archivos']), 'directorio': str(final),
                      'producto_completo_verificado': False, 'pdf': len(idx['pdf_candidatos'])}, ensure_ascii=False))


if __name__ == '__main__':
    main()
