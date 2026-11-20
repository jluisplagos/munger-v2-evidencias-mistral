"""Valida el registro y genera ESTADO.md; no verifica verdad económica ni Git remoto.

Uso: python3 coordinacion/cierre_v2/estado.py [--control CONTROL.json] [--salida ESTADO.md]
Solo Claude coordinador mantiene el registro; los autores publican ENTREGA.json.
"""
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
STAGES = {
    'entrega': {'PENDIENTE', 'PARCIAL', 'ENTREGADO'},
    'revision': {'PENDIENTE', 'LIMITADA', 'CORRECCIONES', 'CONFORME_CON_LIMITES', 'CONFORME'},
    'integracion': {'NO', 'PARCIAL', 'SI'},
    'pruebas_autor': {'NO_EJECUTADAS', 'DECLARADAS', 'EJECUTADAS'},
    'pruebas_externas': {'NO_EJECUTADAS', 'PARCIALES', 'REPRODUCIDAS'},
}
SHA = re.compile(r'[0-9a-f]{40}')


def validate(data):
    errors = []
    rows = data.get('tareas', [])
    ids = [x.get('id') for x in rows]
    if len(ids) != len(set(ids)) or any(not x for x in ids):
        errors.append('IDs ausentes o duplicados')
    for row in rows:
        key = row.get('id', '?')
        for name, allowed in STAGES.items():
            if row.get(name) not in allowed:
                errors.append(f'{key}: {name} no válido')
        for name in ['commit_origen', 'commit_destino', 'commit_revisado']:
            if row.get(name) is not None and not SHA.fullmatch(row[name]):
                errors.append(f'{key}: {name} necesita SHA completo')
        for dep in row.get('dependencias', []):
            if dep not in ids or dep == key:
                errors.append(f'{key}: dependencia inválida {dep}')
        if not row.get('autor') or not row.get('siguiente_accion'):
            errors.append(f'{key}: falta dueño o siguiente acción')
        if row.get('entrega') == 'ENTREGADO' and (not row.get('commit_origen') or not row.get('evidencia')):
            errors.append(f'{key}: entrega sin commit/evidencia')
        if row.get('integracion') != 'NO':
            if row.get('revision') not in {'LIMITADA', 'CONFORME_CON_LIMITES', 'CONFORME'}:
                errors.append(f'{key}: incorporación sin revisión aceptable')
            if not row.get('commit_destino') or not row.get('alcance_aceptado'):
                errors.append(f'{key}: incorporación sin destino/alcance')
            if row.get('commit_revisado') != row.get('commit_origen'):
                errors.append(f'{key}: revisión no corresponde al origen incorporado')
        request = row.get('solicitud_revision')
        if request and request.get('estado') == 'LISTA':
            for field in ['sha_autor', 'base_revisada', 'diff_rutas', 'criterios', 'revisor_asignado']:
                if not request.get(field):
                    errors.append(f'{key}: solicitud lista sin {field}')
            for field in ['sha_autor', 'base_revisada']:
                if request.get(field) and not SHA.fullmatch(request[field]):
                    errors.append(f'{key}: solicitud {field} necesita SHA completo')
    graph = {r['id']: r.get('dependencias', []) for r in rows}
    done, visiting = set(), set()

    def visit(key):
        if key in visiting:
            errors.append(f'ciclo de dependencias en {key}')
            return
        if key in done or key not in graph:
            return
        visiting.add(key)
        for dep in graph[key]:
            visit(dep)
        visiting.remove(key)
        done.add(key)
    for key in graph:
        visit(key)
    return errors


def cell(value):
    return str(value or '—').replace('|', '/').replace('\n', ' ')


def render(data):
    lines = ['# Estado único de Munger V2', '', f"Corte: {data['fecha_corte']}.", '',
             data['estado_global'], '',
             '**Fuente:** CONTROL.json. Este panel resume evidencia registrada; no observa sesiones privadas, no ejecuta agentes y no acredita por sí solo aptitud económica.', '',
             f"Candidata integrada: {data.get('candidata_integrada') or 'todavía no registrada'}. Mantenedor: {data['mantenedor']}.", '',
             '| ID | Dueño | Entregado | Revisado | Integrado | Pruebas autor / externas | Origen |',
             '|---|---|---|---|---|---|---|']
    for row in data['tareas']:
        lines.append('| ' + ' | '.join(cell(x) for x in [row['id'], row['autor'], row['entrega'], row['revision'], row['integracion'], row['pruebas_autor']+' / '+row['pruebas_externas'], (row.get('commit_origen') or '')[:7]])+' |')
    lines += ['', '## Próxima acción y dependencias por tarea', '']
    for row in data['tareas']:
        lines.append(f"- **{row['id']} · {row['tarea']}**: {row['siguiente_accion']}")
        if row.get('dependencias'):
            lines.append('  Dependencias: '+', '.join(row['dependencias'])+'.')
        if row.get('bloqueo'):
            lines.append('  Bloqueo/límite: '+row['bloqueo'])
    lines += ['', '## Solicitudes de revisión', '']
    requests = [(r['id'], r['solicitud_revision']) for r in data['tareas'] if r.get('solicitud_revision')]
    for key, request in requests:
        lines.append(f"- {key}: {request['estado']}; revisor asignado: {request.get('revisor_asignado', 'sin asignar')}; SHA: {request.get('sha_autor') or 'aún sin nueva entrega fijada'}.")
    lines += ['', '## Cómo se decide el cierre', '',
              'PROGRAMA.md fija los criterios: candidata trazable; datos/derivados y decisiones vigentes; pruebas y recorrido real; alcance por motor; manual, recuperación y traspaso. No se calcula porcentaje global. Un bloqueo económico puede permitir continuar trabajo técnico sin convertir el expediente en apto.', '',
              'Las pruebas antiguas solo se conservan cuando sus dependencias no cambian. Ninguna marca del plan de la interfaz sustituye la evidencia de un commit, prueba o revisión.', '']
    return '\n'.join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--control', type=Path, default=ROOT/'CONTROL.json')
    ap.add_argument('--salida', type=Path, default=ROOT/'ESTADO.md')
    args = ap.parse_args()
    data = json.loads(args.control.read_text())
    errors = validate(data)
    if errors:
        print(json.dumps({'valido': False, 'errores': errors}, ensure_ascii=False, indent=2))
        return 1
    args.salida.write_text(render(data))
    print(json.dumps({'valido': True, 'tareas': len(data['tareas']), 'salida': str(args.salida),
                      'alcance': 'coherencia del registro, no verdad económica ni ejecución de pruebas'}, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
