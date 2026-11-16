"""Comprueba estructura de la entrega; no valida cifras ni aprueba una inversión."""
import csv
import hashlib
import json
from pathlib import Path
import sys

TAREA = Path(__file__).resolve().parents[1]
REPO = TAREA.parents[1]


def main():
    cfg = json.loads((TAREA / 'entrada/configuracion.json').read_text(encoding='utf-8'))
    out = REPO / 'resultados'
    errors = []
    required = ['lectura_fuentes.jsonl', 'contraste_objetivos.csv', 'HALLAZGOS.md',
                'RESUMEN_PARA_CLAUDE.md', 'PUNTO_DE_RECUPERACION.md', 'MANIFIESTO_SHA256.txt']
    for name in required:
        if not (out / name).is_file() or not (out / name).stat().st_size:
            errors.append('falta o está vacío: ' + name)
    table = out / 'contraste_objetivos.csv'
    if table.is_file():
        rows = list(csv.DictReader(table.open(encoding='utf-8', newline='')))
        expected = {(e, c) for e in cfg['empresas'] for c in cfg['objetivos']}
        actual = [(r.get('empresa'), r.get('celda')) for r in rows]
        if len(actual) != 26 or set(actual) != expected:
            errors.append('se necesitan exactamente los 26 objetivos, sin duplicados ni sustituciones')
        allowed = {'COINCIDE_EN_REVISION_MISTRAL', 'DIFERENCIA', 'NO_ACREDITADO', 'HIPOTESIS_O_AUSENCIA'}
        for r in rows:
            if r.get('estado') not in allowed:
                errors.append('estado no válido: ' + str(r.get('estado')))
            if not r.get('evidencia_o_limite', '').strip():
                errors.append('objetivo sin evidencia ni límite: ' + str(r.get('celda')))
    observations = out / 'lectura_fuentes.jsonl'
    if observations.is_file():
        for i, line in enumerate(observations.read_text(encoding='utf-8').splitlines(), 1):
            try:
                row = json.loads(line)
                if not isinstance(row, dict) or not row.get('empresa') or not row.get('entrada'):
                    raise ValueError('se requieren empresa y entrada')
            except (ValueError, TypeError) as ex:
                errors.append(f'lectura_fuentes línea {i}: {ex}')
    manifest = out / 'MANIFIESTO_SHA256.txt'
    if manifest.is_file():
        listed = set()
        for line in manifest.read_text(encoding='utf-8').splitlines():
            try:
                h, name = line.split(maxsplit=1)
                p = out / name.lstrip('*')
                if not p.resolve().is_relative_to(out.resolve()) or not p.is_file():
                    raise ValueError('ruta no válida')
                if hashlib.sha256(p.read_bytes()).hexdigest() != h:
                    raise ValueError('huella distinta')
                listed.add(p.relative_to(out).as_posix())
            except (ValueError, OSError) as ex:
                errors.append('manifiesto: ' + str(ex))
        if not set(required[:-1]).issubset(listed):
            errors.append('el manifiesto no incluye todos los archivos requeridos')
    print(json.dumps({'estructura': 'FALLA' if errors else 'PASA', 'errores': errors,
                      'validacion_semantica': False, 'apto_para_dinero_real': False}, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
