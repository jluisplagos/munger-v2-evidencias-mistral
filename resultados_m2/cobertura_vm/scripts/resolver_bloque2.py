"""Bloque 2 (cierre v2): registro de resoluciones/bloqueos de la cola de pendientes.

Recorre cola_pendientes.json en orden de prioridad (grupo documento/pagina) y, para
cada fuente pendiente, registra por dimension el motivo exacto (del NO_DECIDIBLE) y
la clasificacion del bloqueo con lo que faltaria:
  - SIN_ORIGINAL: no hay texto del año original entre los 251 insumos fijados ->
    faltaría el documento original del ejercicio ese año (p. ej. CF_2016.txt).
  - AMBIGUEDAD_FILA_COLUMNA: el valor figura en el original pero no en la misma
    fila/columna mapeable 1:1 -> faltaría el desglose/fila exacta en el original.
  - NO_MAPEABLE_1a1: fila localizada pero columnas no alineables -> faltaría leer la
    tabla completa (fila partida en varias lineas) del original.
  - DIFERE_SIN_DECLARACION / DECLARA_NO_DIFIERE: faltaría declaración de reexpresión
    o puente de significado (nota del informe nuevo que explique el cambio).
  - NO_APLICA_ALCANCE_SIN_PUENTE: la declaración da razón de alcance pero no puente
    verificado -> faltaría el puente (componentes citados) verificado en el original.
  - NO_LOCALIZADA: partida no localizada en el original -> faltaría la partida en el
    texto del año original.
  - NO_TABULAR / CONTINUACION / UNIDAD: motivos de fila/columna/unidad.

No cambia estados: documenta evidencia y bloqueos precisos. Salida:
resultados/resoluciones_bloque2.json
"""
import json
import re
import sys
from pathlib import Path

# A3-R8: debe funcionar también con python3 -I (sin anteponer la carpeta del script)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun as C


def clasifica(dim, detalle):
    d = detalle or ''
    if 'no hay texto conservado' in d:
        m = re.search(r'año (20\d\d)', d)
        anio = m.group(1) if m else '?'
        return 'SIN_ORIGINAL', f'falta el documento original del ejercicio {anio} entre los 251 insumos fijados (selección parcial del ZIP base-4.14)'
    if 'no se puede mapear 1:1' in d:
        return 'NO_MAPEABLE_1a1', 'falta leer la tabla completa del original (fila partida en varias lineas o cabecera de otra tabla en la misma pagina)'
    if 'no en la misma fila/columna' in d or 'ambiguedad de fila/columna' in d:
        return 'AMBIGUEDAD_FILA_COLUMNA', 'el valor figura en el original pero no en la misma fila/columna 1:1; faltaria localizar la fila exacta del comparativo en el original'
    if 'falta puente' in d:
        return 'NO_APLICA_ALCANCE_SIN_PUENTE', 'la declaracion da razon de alcance pero no un puente verificado; faltaria el puente (componentes citados) comprobado en el original o la nota del informe nuevo'
    if 'sin declaracion de reexpresion' in d:
        return 'DIFERE_SIN_DECLARACION', 'el original y el comparativo difieren sin declaracion de reexpresion; faltaria puente de significado (cambio de clasificacion/perimetro no acredita reexpresion)'
    if 'posible reexpresion no declarada' in d:
        return 'DECLARA_NO_DIFIERE', 'declara no reexpresado pero el original imprime otro valor en esa columna; faltaria revisar la nota del informe nuevo (posible reexpresion no declarada)'
    if 'no se localiza en los textos' in d:
        return 'NO_LOCALIZADA', 'la partida no aparece en el texto conservado del año original; faltaria esa partida en el documento del ejercicio'
    if dim == 'columna':
        return 'NO_TABULAR', 'la pagina citada no es una tabla con columnas de años; faltaria la tabla con encabezado de ejercicios'
    if dim == 'fila':
        return 'CONTINUACION', 'fila de continuacion sin etiqueta propia; faltaria la etiqueta de la partida en la linea anterior'
    if dim == 'unidad':
        return 'UNIDAD_SIN_FRASE', 'sin frase de escala en la pagina, en la tabla ni en la cabecera; faltaria la nota de escala del estado'
    return 'OTRO', d[:120]


def main():
    cola = json.loads((C.RESULTADOS / 'cola_pendientes.json').read_text(encoding='utf-8'))
    contexto = {}
    for line in (C.RESULTADOS / 'verificacion_contexto.jsonl').read_text(encoding='utf-8').splitlines():
        r = json.loads(line)
        contexto[(r['empresa'], r['celda'])] = r

    grupos_out = []
    resumen_clas = {}
    for g in cola['cola']:
        entradas_out = []
        for it in g['entradas']:
            r = contexto.get((it['empresa'], it['celda'])) or {}
            dims_out = []
            for dim, v in (it.get('detalle_pendientes') or {}).items():
                detalle = v[1] if isinstance(v, list) and len(v) > 1 else (v if isinstance(v, str) else '')
                clas, faltaria = clasifica(dim, detalle)
                resumen_clas[clas] = resumen_clas.get(clas, 0) + 1
                dims_out.append({'dimension': dim, 'motivo': detalle, 'clasificacion': clas, 'que_faltaria': faltaria})
            entradas_out.append({
                'celda': it['celda'], 'id': it.get('id'), 'material_declarada': it['material_declarada'],
                'derivados_materiales_dependientes': it['derivados_materiales_dependientes'],
                'estado_contextual': r.get('estado_contextual'),
                'pendientes': dims_out,
            })
        grupos_out.append({
            'empresa': g['empresa'], 'archivo': g['archivo'], 'pagina': g['pagina'],
            'prioridad': g['prioridad'], 'n_pendientes': g['n_pendientes'],
            'entradas': entradas_out,
        })

    out = {
        'nota': 'Registro del bloque 2: cada pendiente queda con evidencia (resuelto por el código v3.2-v3.6) o con bloqueo preciso y lo que faltaria. No se fuerzan recuentos; una ausencia genuina permanece pendiente. Propuesta de evidencia de Mistral; revisión por Claude coordinador pendiente.',
        'total_grupos': len(grupos_out),
        'total_fuentes_pendientes': sum(g['n_pendientes'] for g in grupos_out),
        'total_derivados_pendientes': len(cola['derivados_pendientes']),
        'resumen_clasificaciones': resumen_clas,
        'grupos': grupos_out,
        'derivados_pendientes': cola['derivados_pendientes'],
    }
    C.dump_json(out, C.RESULTADOS / 'resoluciones_bloque2.json')
    print(json.dumps({'grupos': len(grupos_out),
                      'fuentes': out['total_fuentes_pendientes'],
                      'derivados': out['total_derivados_pendientes'],
                      'clasificaciones': resumen_clas}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
