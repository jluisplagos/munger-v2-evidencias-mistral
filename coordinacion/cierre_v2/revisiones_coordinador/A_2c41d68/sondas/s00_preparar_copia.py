"""Revisor A (2c41d68). Prepara una copia aislada de reproduccion:
copia el arbol extraido de 2c41d68 a DEST y extrae a DEST/.trabajo/insumos_m2 los
insumos de indice_fuentes.json desde el ZIP base-4.14, verificando bytes y sha256
(misma logica que preparar_insumos.py --zip, sin su comprobacion de 'git remote',
porque la copia extraida con git archive no es un repositorio).
Uso: python3 -I s00_preparar_copia.py ENTREGA_EXTRAIDA DEST ZIP
"""
import hashlib, json, shutil, sys, zipfile
from pathlib import Path, PurePosixPath
src, dest, zp = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
def h(p):
    x = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            x.update(b)
    return x.hexdigest()
if dest.exists():
    raise SystemExit('DEST ya existe; no se sobrescribe')
shutil.copytree(src, dest)
tarea = dest / 'docs/programa_mistral_m2'
cfg = json.loads((tarea / 'entrada/configuracion.json').read_text(encoding='utf-8'))
idx = json.loads((tarea / 'entrada/indice_fuentes.json').read_text(encoding='utf-8'))
assert zp.stat().st_size == cfg['zip_bytes'], 'bytes ZIP'
assert h(zp) == cfg['zip_sha256'], 'sha ZIP'
final = dest / '.trabajo/insumos_m2'
final.mkdir(parents=True)
with zipfile.ZipFile(zp) as z:
    for it in idx['archivos']:
        p = PurePosixPath(it['ruta'])
        assert not p.is_absolute() and '..' not in p.parts
        d = final.joinpath(*p.parts)
        d.parent.mkdir(parents=True, exist_ok=True)
        with z.open(cfg['zip_root'] + '/' + it['ruta']) as a, open(d, 'wb') as b:
            shutil.copyfileobj(a, b)
bad = [it['ruta'] for it in idx['archivos'] if (final / it['ruta']).stat().st_size != it['bytes'] or h(final / it['ruta']) != it['sha256']]
print(json.dumps({'zip_sha256': cfg['zip_sha256'], 'insumos': len(idx['archivos']), 'no_conformes': bad}, ensure_ascii=False))
sys.exit(1 if bad else 0)
