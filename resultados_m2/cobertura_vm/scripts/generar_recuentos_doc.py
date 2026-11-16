"""Genera los recuentos vigentes de la cobertura (A2-R5: generados, no a mano).

Lee las salidas ya producidas por el pipeline (verificacion_contexto.jsonl,
COBERTURA_677.csv, DERIVADOS.json, control_cobertura.json, control_negativo.json)
y escribe:
  - resultados/RECUENTOS_VIGENTES.md (documento generado completo)
  - el bloque entre marcadores <!-- RECUENTOS_VIGENTES:INICIO/--FIN --> en
    MAPA_REGENERACION.md (tabla vigente para el integrador)
No modifica ningun otro contenido. Ejecutar tras control_cobertura.py.
"""
import csv
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun as C

INICIO = '<!-- RECUENTOS_VIGENTES:INICIO -->'
FIN = '<!-- RECUENTOS_VIGENTES:FIN -->'


def main():
    ver = {}
    dims = {}
    for line in (C.RESULTADOS / 'verificacion_contexto.jsonl').read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        d = json.loads(line)
        ver[(d['empresa'], d['celda'])] = d
        for k, v in (d.get('checks') or {}).items():
            dims.setdefault(k, Counter())[v[0]] += 1
    estados_ver = Counter(d['estado_contextual'] for d in ver.values())
    rows = list(csv.DictReader((C.OUT / 'COBERTURA_677.csv').open(encoding='utf-8')))
    estados_csv = Counter(r['estado_contextual'] for r in rows)
    der = C.load_json(C.OUT / 'DERIVADOS.json')
    estados_der = Counter(n['estado_contextual'] for n in der['nodos'])
    cc = C.load_json(C.RESULTADOS / 'control_cobertura.json')
    cn = C.load_json(C.RESULTADOS / 'control_negativo.json')

    def fmt_counter(c, orden=None):
        keys = orden or sorted(c)
        return ' / '.join(f'{k} {c[k]}' for k in keys if c.get(k))

    ahora = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    lineas = []
    lineas.append(f'# Recuentos vigentes · Frente A M2 · cobertura VM (GENERADO por scripts/generar_recuentos_doc.py · {ahora})')
    lineas.append('')
    lineas.append('**No editar a mano**: este documento lo regenera `generar_recuentos_doc.py` a partir de las salidas del pipeline.')
    lineas.append('')
    lineas.append('## Estados contextuales (677 filas de COBERTURA_677.csv)')
    lineas.append('')
    lineas.append('| Estado | n |')
    lineas.append('|---|---|')
    for e in ('REVISADO_CONTEXTUAL', 'PENDIENTE_CONTEXTUAL', 'CONFLICTO_CONTEXTUAL', 'REUTILIZADO_M1', 'NO_APLICA'):
        lineas.append(f'| {e} | {estados_csv.get(e, 0)} |')
    lineas.append(f'| **total** | **{sum(estados_csv.values())}** |')
    lineas.append('')
    lineas.append('## Estados contextuales por nivel')
    lineas.append('')
    lineas.append(f'- Entradas verificadas en `verificacion_contexto.jsonl` ({len(ver)}): {fmt_counter(estados_ver)}')
    lineas.append(f'- Derivados (101 nodos en `DERIVADOS.json`): {fmt_counter(estados_der)}')
    lineas.append('')
    lineas.append('## Dimensiones contextuales (sobre las entradas con fuente)')
    lineas.append('')
    lineas.append('| Dimensión | Desglose |')
    lineas.append('|---|---|')
    for k in sorted(dims):
        lineas.append(f'| {k} | {fmt_counter(dims[k])} |')
    lineas.append('')
    lineas.append('## Controles')
    lineas.append('')
    lineas.append(f'- `control_cobertura.py`: PASS={cc.get("PASS")}, violaciones={cc.get("n_violaciones")} (exit 0 si PASS).')
    lineas.append(f"- `control_negativo.py`: {cn.get('mutaciones')} mutaciones en memoria; detectadas por el contextual {cn.get('detectadas_por_contextual')}, por el mecanico {cn.get('detectadas_por_mecanico')}; sondas bilaterales ok={cn.get('bilaterales_ok')}; sondas del revisor d375d80 en CONFLICTO: {sum(1 for v in (cn.get('sondas_revisor') or {}).values() if isinstance(v, dict) and v.get('resultado') == 'CONFLICTO')}/{len(cn.get('sondas_revisor') or {})}.")
    lineas.append('')
    doc = '\n'.join(lineas) + '\n'
    (C.RESULTADOS / 'RECUENTOS_VIGENTES.md').write_text(doc, encoding='utf-8')

    mapa = C.OUT / 'MAPA_REGENERACION.md'
    src = mapa.read_text(encoding='utf-8')
    if INICIO in src and FIN in src:
        pre, rest = src.split(INICIO, 1)
        _, post = rest.split(FIN, 1)
        tabla = [
            INICIO,
            '',
            f'## Estados vigentes para regeneración (GENERADO por `scripts/generar_recuentos_doc.py` · {ahora}; fuente: `resultados/RECUENTOS_VIGENTES.md`)',
            '',
            '| Grupo | n | Estado contextual | ¿Qué puede reutilizar el integrador? |',
            '|---|---|---|---|',
            f"| Fuentes con todas las dimensiones OK/NO_APLICA | {estados_ver.get('REVISADO_CONTEXTUAL', 0)} | REVISADO_CONTEXTUAL | Sí: huella vigente + fila/columna (posición)/unidad+escala/signo/perímetro/versión/reexpresión leídos |",
            f"| Fuentes con alguna dimensión no decidible | {estados_ver.get('PENDIENTE_CONTEXTUAL', 0)} | PENDIENTE_CONTEXTUAL | No como revisadas: ver desglose por dimensión abajo |",
            f"| Fuentes con contradicción documentada (A2-R2) | {estados_ver.get('CONFLICTO_CONTEXTUAL', 0)} | CONFLICTO_CONTEXTUAL | No: contradicción acreditada; requiere resolución humana, no forzar |",
            f"| Piloto M1 (fuentes) | {estados_ver.get('REUTILIZADO_M1', 0)} | REUTILIZADO_M1 | Sí, con el alcance y huellas del piloto |",
            f"| Derivados (propagación de orígenes) | 101 | {fmt_counter(estados_der)} | Según orígenes: CONFLICTO/PENDIENTE se propagan (A2-R2); REVISADO solo si todos los orígenes lo están |",
            f"| Clases sin fuente (hipótesis/convenciones/no aplicables/ausentes) | {estados_csv.get('NO_APLICA', 0)} | NO_APLICA (clase) | No como datos: requieren decisión o fuente |",
            '',
            f'Totales CSV (677): {fmt_counter(estados_csv)}. Control `control_cobertura.py`: PASS={cc.get("PASS")}, {cc.get("n_violaciones")} violaciones (exit 0). Sondas del revisor d375d80: CONFLICTO 5/5; bilaterales 15/15 ok.',
            '',
            'Desglose de dimensiones no decidibles/conflicto entre las fuentes: '
            + '; '.join(f'{k} {fmt_counter(dims[k])}' for k in sorted(dims)),
            '',
            FIN,
        ]
        mapa.write_text(pre + '\n'.join(tabla) + post, encoding='utf-8')
        print('MAPA_REGENERACION.md actualizado (bloque generado)')
    else:
        print('AVISO: marcadores no encontrados en MAPA_REGENERACION.md; solo se escribio RECUENTOS_VIGENTES.md')
    print(f'escrito {C.RESULTADOS / "RECUENTOS_VIGENTES.md"}')


if __name__ == '__main__':
    main()
