"""A3-R8: actualiza los textos con recuentos desfasados DESDE las salidas generadas.

Reemplaza, con valores calculados de COBERTURA_677.csv / verificacion_contexto.jsonl /
resoluciones_bloque2.json / cola_pendientes.json, las líneas históricas que quedaron
mal (RESUMEN_PARA_CLAUDE.md §Recuentos, HALLAZGOS.md §10 dimensiones, y el motivo de
aux:AR2025_p27 en PUNTO_DE_RECUPERACION.md y RESUMEN_PARA_CLAUDE.md). Si un ancla no
aparece, falla en voz alta (no escribe a ciegas).
Uso: PYTHONPATH=.trabajo/pylibs python3 -B scripts/actualizar_textos_resumen.py
"""
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun as C

OUT = C.OUT
MOTIVO_OK = ('CF_2024 línea 414 imprime 2,001 en la MISMA fila y columna 2024 '
             '(Share-based payment 2,001 2,346); el rótulo completo confirma la fila y la '
             'reexpresión queda OK por igualdad (no reexpresado)')


def main():
    rows = list(csv.DictReader((OUT / 'COBERTURA_677.csv').open(encoding='utf-8')))
    est = Counter(r['estado_contextual'] for r in rows)
    ver = [json.loads(l) for l in (C.RESULTADOS / 'verificacion_contexto.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]
    dims = {}
    for d in ver:
        for k, v in (d.get('checks') or {}).items():
            dims.setdefault(k, Counter())[v[0]] += 1
    der = C.load_json(OUT / 'DERIVADOS.json')
    est_der = Counter(n['estado_contextual'] for n in der['nodos'])
    res = C.load_json(C.RESULTADOS / 'resoluciones_bloque2.json')
    sin_orig = (res.get('resumen_clasificaciones') or {}).get('SIN_ORIGINAL', 0)

    def dim(k):
        c = dims.get(k, Counter())
        parts = [f'{v} {s}' for s, v in (('OK', c.get('OK', 0)), ('ND', c.get('NO_DECIDIBLE', 0)),
                                        ('CONFLICTO', c.get('CONFLICTO', 0)), ('NA', c.get('NO_APLICA', 0)))]
        return '/'.join(p for p in parts if not p.startswith('0 '))

    csv_line = (f"{est.get('REVISADO_CONTEXTUAL',0)} REVISADO_CONTEXTUAL, {est.get('PENDIENTE_CONTEXTUAL',0)} PENDIENTE_CONTEXTUAL, "
                f"60 REUTILIZADO_M1, 106 NO_APLICA, {est.get('CONFLICTO_CONTEXTUAL',0)} CONFLICTO_CONTEXTUAL")
    dims_line = (f"columna {dim('columna')}; fila {dim('fila')}; perímetro {dim('perimetro')}; "
                 f"reexpresión {dim('reexpresion')}; signo {dim('signo')}; unidad {dim('unidad')}; versión {dim('version')}. "
                 f"Derivados: {est_der.get('REVISADO_CONTEXTUAL',0)} REVISADO / {est_der.get('PENDIENTE_CONTEXTUAL',0)} PENDIENTE / {est_der.get('REUTILIZADO_M1',0)} REUTILIZADO_M1.")

    cambios = []

    def patch(path, old_regex, new, count=1):
        p = OUT / path
        t = p.read_text(encoding='utf-8')
        t2, n = re.subn(old_regex, new, t, count=count, flags=re.MULTILINE)
        if n == 0:
            sys.exit(f'ANCLA NO ENCONTRADA en {path}: {old_regex[:80]}')
        p.write_text(t2, encoding='utf-8')
        cambios.append((path, n))

    # RESUMEN_PARA_CLAUDE.md §Recuentos: línea de estados contextuales vigente
    patch('RESUMEN_PARA_CLAUDE.md',
          r'198 REVISADO_CONTEXTUAL, 313 PENDIENTE_CONTEXTUAL, 60 REUTILIZADO_M1, 106 NO_APLICA, 0 CONFLICTO_CONTEXTUAL \(313 = 240 fuentes \+ 73 derivados pendientes con motivo preciso; ver `cola_pendientes\.json`\)\.',
          csv_line + ' (v4.0+A3; generado desde resultados/, ver `resultados/RECUENTOS_VIGENTES.md`; en 8b88fab eran 169/209/133/60/106 y los 133 CONFLICTO no eran 133 errores económicos: 104 dependían solo del artefacto de signo)')
    # RESUMEN_PARA_CLAUDE.md: motivo AR2025_p27 (línea del bloque 1)
    patch('RESUMEN_PARA_CLAUDE.md',
          r'caso real `aux:AR2025_p27_pagos_acciones_2024` = 2001 miles de euros → NO_DECIDIBLE\)',
          'caso real `aux:AR2025_p27_pagos_acciones_2024` = 2001 miles de euros; motivo corregido: ' + MOTIVO_OK + ')')
    # HALLAZGOS.md §10: línea de dimensiones desfasada
    patch('HALLAZGOS.md',
          r'- Dimensiones \(467 fuentes\): columna [^\n]*\. Derivados: [^\n]*\.',
          '- Dimensiones (467 fuentes, v4.0+A3 generado desde `resultados/verificacion_contexto.jsonl`): ' + dims_line + '.')
    # PUNTO_DE_RECUPERACION.md: motivo AR2025_p27 sin corregir
    patch('PUNTO_DE_RECUPERACION.md',
          r'→ NO_DECIDIBLE \(aparece en CF_2024\.txt pero no en la misma fila/columna 2024\)\.',
          '→ NO_DECIDIBLE en v3.1; motivo corregido (A3-R8): ' + MOTIVO_OK + '.')
    print(json.dumps({'cambios': cambios, 'csv_line': csv_line}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
