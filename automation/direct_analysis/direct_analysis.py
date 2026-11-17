#!/usr/bin/env python3
"""Análisis directo en una sola pasada sobre un paquete de entrada declarado.

Personaje frente a análisis directo (REORIENTACION_UNIVERSO §10). El control de gasto
no se reimplementa: se configura y ejecuta critical_review.run de AUTO1 (tope
acumulado, reserva previa create-only, una sola llamada sin reintentos, estados de
coste y publicación en la rama de registro). Aquí solo se arma el paquete, se
comprueba su tamaño antes de llamar y se valida y presenta la salida.
"""
import argparse
import contextlib
import datetime
from decimal import Decimal
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'automation/coordination'))
import critical_review as cr  # noqa: E402  (importa también automation/claude_review/pilot.py)

pilot = cr.pilot

ENCARGO_PATH = 'automation/direct_analysis/ENCARGO_ANALISIS_DIRECTO.md'
CODE_PATHS = ('automation/direct_analysis/direct_analysis.py', ENCARGO_PATH,
              'automation/coordination/critical_review.py', 'automation/claude_review/pilot.py')
# Tarifas USD/MTok de la API de Anthropic (tabla de modelos consultada el 17-nov-2026;
# Fable 5.2 y Sonnet 5.5 coinciden con las ya registradas en AUTO1). Contexto: 1M.
MODELS = {
    'claude-opus-5-5': {'input': Decimal('4'), 'output': Decimal('20'), 'context': 1_000_000},
    'claude-fable-5-2': {'input': Decimal('8'), 'output': Decimal('40'), 'context': 1_000_000},
    'claude-sonnet-5-5': {'input': Decimal('2'), 'output': Decimal('10'), 'context': 1_000_000},
}
DEFAULT_MODEL = 'claude-opus-5-5'
EFFORTS = ('low', 'medium', 'high', 'xhigh', 'max')
PRICES_CHECKED = '2026-11-17'
# Salida máxima (pensamiento + respuesta). Igual que AUTO1, para caber en su plazo de
# stream de 720 s; agotarla deja un resultado pagado y no aceptado.
MAX_OUTPUT = 32768
HARD_MAX_USD = Decimal('5')  # techo del código; el tope acumulado lo fija la persona
MARGIN_TOKENS = 4096          # el mismo margen que critical_review.budget
MAX_FILE_BYTES = 1_500_000
MAX_FILES = 40
TASA = '9 %'
PROBABILIDADES = {'malo': '0,2', 'normal': '0,6', 'bueno': '0,2'}
OK_STATES = ('PREPARADO_SIN_API', 'AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION')

# --- Rutas prohibidas en el paquete (se comparan sin tildes y en minúsculas) ---------
FORBIDDEN_SEGMENTS = {'examen', 'automation', '.github', 'resultados_qwen', 'prompts_generados',
                      'revisiones_coordinador', 'revision_externa'}
FORBIDDEN_SUBSTRINGS = ('rubrica', 'critic', 'informe_critico', 'informe-critico', 'lectura_informe',
                        'contradictor', 'mecanismo_personaje', 'prompt', 'analisis_directo',
                        'analisis-directo', 'veredicto', 'dictamen', 'respuesta', 'salida')
# Salidas del personaje por nombre de archivo (sin extensión).
FORBIDDEN_STEMS = re.compile(
    r'(^|[_.-])fases?_?[abc]([_.-]|$)|^celdas_?[abc]([_.-]|$)|^citas_fase|^esquema_fase'
    r'|^(informe|precio)(_v\d+)?$|^(ficha|gramatica|diagnostico|estado_pipeline|auditoria)')
# Marcas de contenido que delatan la rúbrica o el informe crítico copiados con otro nombre.
FORBIDDEN_CONTENT = ('rubrica', 'informe critico', 'informe_critico')
PATH_CHARS = re.compile(r'[\w./ -]+')
# Los manifiestos viven en un único sitio conocido; no se envían en bruto al modelo.
MANIFEST = re.compile(r'automation/direct_analysis/paquetes/[a-z0-9][a-z0-9_-]{0,60}\.json')


def fold(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c)).lower()


def check_path(path):
    """Ruta relativa del repo, sin '..', y fuera de lo que el análisis directo no puede ver."""
    if (not isinstance(path, str) or not path or len(path) > 300 or not PATH_CHARS.fullmatch(path)
            or PurePosixPath(path).is_absolute() or any(x in ('', '.', '..') for x in path.split('/'))):
        raise pilot.PilotError('RUTA_INVALIDA')
    folded = fold(path)
    parts = folded.split('/')
    stem = parts[-1].split('.')[0]
    if (set(parts[:-1]) & FORBIDDEN_SEGMENTS or parts[0] in FORBIDDEN_SEGMENTS
            or any(s in folded for s in FORBIDDEN_SUBSTRINGS) or FORBIDDEN_STEMS.search(stem)):
        raise pilot.PilotError('RUTA_PROHIBIDA_EN_EL_PAQUETE')
    return path


def git(root, *args):
    return subprocess.run(['git', *args], cwd=root, capture_output=True, check=True).stdout


def verify_code(root, code_sha):
    """El código y el encargo que se ejecutan son los bytes del SHA observado."""
    if not re.fullmatch(r'[0-9a-f]{40}', code_sha or ''):
        raise pilot.PilotError('SHA_INVALIDO')
    if git(root, 'rev-parse', 'HEAD').decode().strip() != code_sha:
        raise pilot.PilotError('SHA_NO_ES_EL_OBSERVADO')
    for path in CODE_PATHS:
        if (Path(root) / path).read_bytes() != git(root, 'show', f'{code_sha}:{path}'):
            raise pilot.PilotError('CODIGO_LOCAL_DISTINTO_DEL_SHA')
    return git(root, 'show', f'{code_sha}:{ENCARGO_PATH}').decode('utf-8')


def read_blob(root, commit, path):
    """Archivo regular de texto UTF-8 de un commit fijado; nunca enlaces ni submódulos."""
    if not re.fullmatch(r'[0-9a-f]{40}', commit):
        raise pilot.PilotError('COMMIT_NO_FIJADO')
    try:
        if git(root, 'cat-file', '-t', commit).strip() != b'commit':
            raise pilot.PilotError('COMMIT_NO_FIJADO')
        entry = git(root, 'ls-tree', '-z', commit, '--', path).split(b'\0')[0]
    except subprocess.CalledProcessError:
        raise pilot.PilotError('COMMIT_O_ARCHIVO_NO_ENCONTRADO') from None
    meta, _, name = entry.partition(b'\t')
    fields = meta.split()
    if name.decode('utf-8', 'replace') != path or len(fields) != 3:
        raise pilot.PilotError('ARCHIVO_NO_ENCONTRADO')
    if fields[0] not in (b'100644', b'100755') or fields[1] != b'blob':
        raise pilot.PilotError('NO_ES_ARCHIVO_REGULAR')
    if int(git(root, 'cat-file', '-s', fields[2].decode())) > MAX_FILE_BYTES:
        raise pilot.PilotError('ARCHIVO_DEMASIADO_GRANDE_NO_SE_RECORTA')
    raw = git(root, 'cat-file', 'blob', fields[2].decode())
    if b'\0' in raw:
        raise pilot.PilotError('ARCHIVO_NO_ES_TEXTO')
    try:
        return raw, raw.decode('utf-8')
    except UnicodeDecodeError:
        raise pilot.PilotError('ARCHIVO_NO_ES_TEXTO') from None


def _slug(value, code):
    if not isinstance(value, str) or not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,29}', value):
        raise pilot.PilotError(code)
    return value


def load_package(root, code_sha, manifest_path, empresa):
    """Lee el manifiesto versionado y cada archivo declarado, con su huella."""
    _slug(empresa, 'EMPRESA_INVALIDA')
    if not isinstance(manifest_path, str) or not MANIFEST.fullmatch(manifest_path):
        raise pilot.PilotError('MANIFIESTO_FUERA_DE_PAQUETES')
    raw_manifest, text = read_blob(root, code_sha, manifest_path)
    try:
        m = json.loads(text)
    except ValueError:
        raise pilot.PilotError('MANIFIESTO_JSON_INVALIDO') from None
    if not isinstance(m, dict) or set(m) != {'empresa', 'caso', 'fecha_corte', 'archivos'}:
        raise pilot.PilotError('MANIFIESTO_INVALIDO')
    if _slug(m['empresa'], 'MANIFIESTO_INVALIDO') != empresa:
        raise pilot.PilotError('MANIFIESTO_DE_OTRA_EMPRESA')
    if not isinstance(m['caso'], str) or not 1 <= len(m['caso']) <= 100 or not PATH_CHARS.fullmatch(m['caso']):
        raise pilot.PilotError('MANIFIESTO_INVALIDO')
    try:
        datetime.date.fromisoformat(m['fecha_corte'])
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', m['fecha_corte']):
            raise ValueError
    except (TypeError, ValueError):
        raise pilot.PilotError('FECHA_CORTE_INVALIDA') from None
    files = m['archivos']
    if not isinstance(files, list) or not 1 <= len(files) <= MAX_FILES:
        raise pilot.PilotError('MANIFIESTO_INVALIDO')
    sources, ids = [], set()
    for f in files:
        if isinstance(f, dict) and 'sha256' not in f:
            raise pilot.PilotError('PAQUETE_SIN_HUELLA_DECLARADA')
        if not isinstance(f, dict) or not {'id', 'ruta', 'sha256', 'descripcion'} <= set(f) \
                or set(f) - {'id', 'ruta', 'sha256', 'descripcion', 'commit'}:
            raise pilot.PilotError('ARCHIVO_DECLARADO_INVALIDO')
        if not isinstance(f['id'], str) or not re.fullmatch(r'[a-z][a-z0-9_]{0,40}', f['id']) or f['id'] in ids:
            raise pilot.PilotError('ID_ARCHIVO_INVALIDO')
        ids.add(f['id'])
        if not isinstance(f['descripcion'], str) or not 1 <= len(f['descripcion']) <= 300:
            raise pilot.PilotError('ARCHIVO_DECLARADO_INVALIDO')
        if not isinstance(f['sha256'], str) or not re.fullmatch(r'[0-9a-f]{64}', f['sha256']):
            raise pilot.PilotError('PAQUETE_SIN_HUELLA_DECLARADA')
        commit = f.get('commit', code_sha)
        if not isinstance(commit, str):
            raise pilot.PilotError('COMMIT_NO_FIJADO')
        raw, body = read_blob(root, commit, check_path(f['ruta']))
        if pilot.digest(raw) != f['sha256']:
            raise pilot.PilotError('HUELLA_DISTINTA_DE_LA_DECLARADA')
        if any(marker in fold(body) for marker in FORBIDDEN_CONTENT):
            raise pilot.PilotError('CONTENIDO_PROHIBIDO_EN_EL_PAQUETE')
        sources.append({'id': f['id'], 'path': f['ruta'], 'commit': commit, 'sha256': f['sha256'],
                        'bytes': len(raw), 'descripcion': f['descripcion'], 'text': body})
    return {'empresa': empresa, 'caso': m['caso'], 'fecha_corte': m['fecha_corte'],
            'tasa_descuento': TASA, 'probabilidades_partida': PROBABILIDADES,
            'manifiesto': {'ruta': manifest_path, 'sha256': pilot.digest(raw_manifest)},
            'sources': sources}


def build_bundle(package, encargo, task_id, code_sha):
    """La huella del paquete no depende del SHA del código ni de la tarea."""
    package = {**package, 'encargo_sha256': pilot.digest(encargo.encode('utf-8'))}
    return {**package, 'package_sha256': pilot.digest(pilot.canonical(package)),
            'task_id': task_id, 'repository': pilot.REPO, 'code_sha': code_sha}


# --- Esquema de salida --------------------------------------------------------------
STR = {'type': 'string'}
NUM_NULL = {'anyOf': [{'type': 'number'}, {'type': 'null'}]}
BOOL_NULL = {'anyOf': [{'type': 'boolean'}, {'type': 'null'}]}
ESTADOS = ['concluido', 'pendiente_de_investigacion', 'pendiente_de_datos', 'modelo_no_aplicable', 'no_entregable']
CUBOS = ['Sí', 'Vigilar', 'No', 'Demasiado difícil']
ACCIONES = ['comprar', 'esperar', 'descartar', 'demasiado_dificil', 'ninguna']
TASAS = ('tasa_7', 'tasa_8', 'tasa_9', 'tasa_10', 'tasa_11')


def _obj(props):
    return {'type': 'object', 'additionalProperties': False, 'properties': props, 'required': list(props)}


_ESC = _obj({'valor_por_accion': NUM_NULL, 'probabilidad': {'type': 'number'}, 'razonamiento': STR})
_TASA = _obj({'precio_si': NUM_NULL, 'precio_actual_por_debajo': BOOL_NULL, 'comentario': STR})
SCHEMA = _obj({
    'resumen': STR,
    'estado': {'type': 'string', 'enum': ESTADOS},
    'cubo': {'type': 'string', 'enum': CUBOS},
    'accion': {'type': 'string', 'enum': ACCIONES},
    'moneda': STR,
    'precio_actual': _obj({'valor': NUM_NULL, 'fecha': STR, 'archivo_id': STR}),
    'escenarios': _obj({'malo': _ESC, 'normal': _ESC, 'bueno': _ESC}),
    'probabilidades_justificacion': STR,
    'precio_si': _obj({'valor': NUM_NULL, 'calculo': STR}),
    'sensibilidad_tasa': _obj({t: _TASA for t in TASAS}),
    'conclusion_razonada': STR,
    'que_la_haria_falsa': {'type': 'array', 'items': STR},
    'lo_que_no_se': {'type': 'array', 'items': STR},
    'citas': {'type': 'array', 'items': _obj({'archivo_id': STR, 'cita': STR, 'sostiene': STR})},
})


def check_schema(value, schema, where='$'):
    """Validador del subconjunto de JSON Schema usado arriba; no confía en el proveedor."""
    if 'anyOf' in schema:
        for option in schema['anyOf']:
            try:
                return check_schema(value, option, where)
            except pilot.PilotError:
                pass
        raise pilot.PilotError('ESQUEMA_INVALIDO:' + where)
    kind = schema['type']
    ok = {'object': isinstance(value, dict), 'array': isinstance(value, list),
          'string': isinstance(value, str), 'boolean': isinstance(value, bool), 'null': value is None,
          'number': isinstance(value, (int, float)) and not isinstance(value, bool)
          and math.isfinite(value)}[kind]
    if not ok or ('enum' in schema and value not in schema['enum']):
        raise pilot.PilotError('ESQUEMA_INVALIDO:' + where)
    if kind == 'object':
        if set(value) != set(schema['required']):
            raise pilot.PilotError('ESQUEMA_INVALIDO:' + where)
        for key, sub in schema['properties'].items():
            check_schema(value[key], sub, f'{where}.{key}')
    elif kind == 'array':
        for i, item in enumerate(value):
            check_schema(item, schema['items'], f'{where}[{i}]')
    return value


def precio_si_k3(values, probs, k=3):
    """Mayor P con sum p·max(V−P,0) ≥ k·sum p·max(P−V,0). Cálculo de control, informativo."""
    if any(v is None for v in values) or any(p < 0 for p in probs) or abs(sum(probs) - 1) > 1e-6:
        return None
    lo, hi = min(values), max(values)
    gain = lambda P: sum(p * max(v - P, 0) for v, p in zip(values, probs))  # noqa: E731
    loss = lambda P: sum(p * max(P - v, 0) for v, p in zip(values, probs))  # noqa: E731
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if gain(mid) >= k * loss(mid) else (lo, mid)
    return lo


def mechanical_checks(doc, bundle):
    """Avisos para la revisión humana; no aceptan ni rechazan el análisis."""
    notes = []
    esc = [doc['escenarios'][k] for k in ('malo', 'normal', 'bueno')]
    probs = [e['probabilidad'] for e in esc]
    if abs(sum(probs) - 1) > 1e-6:
        notes.append('Las probabilidades no suman 1.')
    if probs != [0.2, 0.6, 0.2] and not doc['probabilidades_justificacion'].strip():
        notes.append('Probabilidades distintas de 0,2/0,6/0,2 sin justificación.')
    recalculated = precio_si_k3([e['valor_por_accion'] for e in esc], probs)
    declared = doc['precio_si']['valor']
    if recalculated is not None and declared is not None:
        if abs(declared - recalculated) > 0.01 * max(abs(recalculated), 1e-9):
            notes.append('El precio de Sí declarado difiere más de un 1 % del recalculado con sus escenarios.')
    elif (recalculated is None) != (declared is None):
        notes.append('Precio de Sí y escenarios no son coherentes (uno falta y el otro no).')
    if doc['cubo'] == 'Sí' and (doc['estado'] != 'concluido' or doc['accion'] != 'comprar'):
        notes.append('Cubo «Sí» sin estado concluido y acción comprar.')
    texts = {s['id']: s['text'] for s in bundle['sources']}
    bad = [i for i, c in enumerate(doc['citas']) if c['archivo_id'] not in texts or not c['cita']
           or c['cita'] not in texts[c['archivo_id']]]
    if bad:
        notes.append(f'Citas no literales o de archivo inexistente: {bad}.')
    if doc['precio_actual']['valor'] is not None and doc['precio_actual']['archivo_id'] not in texts:
        notes.append('El precio actual no remite a un archivo del paquete.')
    return {'precio_si_recalculado_k3': recalculated, 'citas_total': len(doc['citas']),
            'citas_literales': len(doc['citas']) - len(bad), 'avisos': notes,
            'nota': 'Comprobaciones mecánicas informativas: no acreditan la calidad económica.'}


def validate(response, bundle):
    if response.get('stop_reason') != 'end_turn':
        raise pilot.PilotError('RESPUESTA_INCOMPLETA')
    raw = ''.join(x.get('text', '') for x in response.get('content', [])
                  if isinstance(x, dict) and x.get('type') == 'text').strip()
    fenced = re.fullmatch(r'```json\r?\n([\s\S]*)\r?\n```', raw)
    try:
        doc = json.loads(fenced.group(1) if fenced else raw)
    except (ValueError, RecursionError):
        raise pilot.PilotError('JSON_INVALIDO') from None
    check_schema(doc, SCHEMA)
    return {'analisis': doc, 'package_sha256': bundle['package_sha256'],
            'comprobaciones_mecanicas': mechanical_checks(doc, bundle)}


# --- Presentación ---------------------------------------------------------------------
def _block(text):
    """Texto del modelo como bloque de código indentado: nunca Markdown interpretable."""
    return ['    ' + line for line in str(text).splitlines() or ['']] + ['']


def _n(value):
    return '—' if value is None else (f'{value:.4f}'.rstrip('0').rstrip('.') if isinstance(value, float) else str(value))


def render(report, bundle, preflight):
    out = ['# Análisis directo · ' + bundle['caso'], '',
           'Estado de la ejecución: `' + report['state'] + '`', '',
           'Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.', '',
           '| Campo | Valor |', '|---|---|',
           f"| Empresa | {bundle['empresa']} |", f"| Fecha de corte | {bundle['fecha_corte']} |",
           f"| Tasa | {bundle['tasa_descuento']} |", f"| Tarea | {report['task_id']} |",
           f"| SHA del código | {report['code_sha']} |",
           f"| Huella del paquete (package_sha256) | {bundle['package_sha256']} |",
           f"| Huella del envío (bundle_sha256) | {report['bundle_sha256']} |",
           f"| Huella del encargo | {bundle['encargo_sha256']} |",
           f"| Modelo pedido / devuelto | {report['model_requested']} / {report.get('model_returned', '—')} |",
           f"| Esfuerzo | {report['effort_requested']} |",
           f"| Mensajes enviados | {report['api_messages_sent']} |",
           f"| Cota de entrada estimada antes de llamar | {preflight['input_tokens_upper_bound']} tokens |",
           f"| Reserva estimada antes de llamar | USD {preflight['reserve_upper_bound_usd']} (máximo de la ejecución USD {preflight['max_usd']}) |"]
    if 'budget' in report:
        out.append(f"| Reserva registrada | USD {report['budget']['reserved_usd']} |")
    usage = report.get('usage')
    if isinstance(usage, dict):
        out.append(f"| Uso de tokens | entrada {usage.get('input_tokens')}, salida {usage.get('output_tokens')} |")
    if 'cost_status' in report:
        out.append(f"| Coste | {report['cost_status']}; estimado USD {report['estimated_cost_usd']};"
                   f" cota {report.get('cost_upper_bound_usd', report['estimated_cost_usd'])} |")
    out += ['', '## Paquete de entrada', '', '| id | ruta | commit | sha256 | bytes |', '|---|---|---|---|---|']
    out += [f"| {s['id']} | {s['path']} | {s['commit'][:12]} | {s['sha256']} | {s['bytes']} |" for s in bundle['sources']]
    if 'error' in report:
        out += ['', 'Error: `' + report['error'] + '`']
    review = report.get('review')
    if review:
        a = review['analisis']
        out += ['', '## Salida del modelo (datos, sin acciones ejecutables)', '',
                f"Estado `{a['estado']}` · cubo `{a['cubo']}` · acción `{a['accion']}`", '',
                '| Escenario | Valor por acción | Probabilidad |', '|---|---|---|']
        out += [f"| {k} | {_n(a['escenarios'][k]['valor_por_accion'])} | {_n(a['escenarios'][k]['probabilidad'])} |"
                for k in ('malo', 'normal', 'bueno')]
        out += ['', f"Precio actual: {_n(a['precio_actual']['valor'])} · precio de Sí (k = 3): {_n(a['precio_si']['valor'])}"
                f" · recalculado: {_n(review['comprobaciones_mecanicas']['precio_si_recalculado_k3'])}", '',
                '| Tasa | Precio de Sí | Precio actual por debajo |', '|---|---|---|']
        out += [f"| {t[5:]} % | {_n(a['sensibilidad_tasa'][t]['precio_si'])} | {_n(a['sensibilidad_tasa'][t]['precio_actual_por_debajo'])} |"
                for t in TASAS]
        for title, key in (('Resumen', 'resumen'), ('Moneda', 'moneda'), ('Conclusión razonada', 'conclusion_razonada'),
                           ('Probabilidades', 'probabilidades_justificacion')):
            out += ['', '### ' + title, ''] + _block(a[key])
        for k in ('malo', 'normal', 'bueno'):
            out += ['### Escenario ' + k, ''] + _block(a['escenarios'][k]['razonamiento'])
        out += ['### Cálculo del precio de Sí', ''] + _block(a['precio_si']['calculo'])
        out += ['### Sensibilidad (comentarios)', ''] + _block('\n'.join(
            f"{t[5:]} %: {a['sensibilidad_tasa'][t]['comentario']}" for t in TASAS))
        out += ['### Qué haría falsa la conclusión', ''] + _block('\n'.join('- ' + x for x in a['que_la_haria_falsa']))
        out += ['### Lo que no sabe', ''] + _block('\n'.join('- ' + x for x in a['lo_que_no_se']))
        out += ['### Citas', ''] + _block('\n'.join(f"[{c['archivo_id']}] «{c['cita']}» → {c['sostiene']}" for c in a['citas']))
        out += ['### Comprobaciones mecánicas', ''] + _block(json.dumps(review['comprobaciones_mecanicas'], ensure_ascii=False, indent=2))
    return '\n'.join(out) + '\n'


def make_writer(bundle, preflight):
    def write(output, report):
        output = Path(output)
        output.mkdir(parents=True, exist_ok=True)
        (output / 'report.json').write_bytes(pilot.canonical(report))
        (output / 'report.md').write_text(render(report, bundle, preflight), encoding='utf-8')
    return write


# --- Configuración de AUTO1 y comprobación previa del tamaño -------------------------
def parse_max_usd(raw):
    if not isinstance(raw, str) or not re.fullmatch(r'[0-9]{1,3}(\.[0-9]{1,6})?', raw.strip()):
        raise pilot.PilotError('COSTE_MAXIMO_INVALIDO')
    value = Decimal(raw.strip())
    if not 0 < value <= HARD_MAX_USD:
        raise pilot.PilotError('COSTE_MAXIMO_FUERA_DEL_TECHO_DEL_CODIGO')
    return value


@contextlib.contextmanager
def configured(task_id, model, effort, max_usd, bundle, encargo, preflight=None):
    """Configura critical_review como hace qwen_peer_review.configure y lo restaura al salir."""
    if model not in MODELS:
        raise pilot.PilotError('MODELO_NO_AUTORIZADO')
    if effort not in EFFORTS:
        raise pilot.PilotError('ESFUERZO_INVALIDO')
    info, original_budget = MODELS[model], cr.budget

    def budget(b, count):
        # Tras count_tokens y antes de reservar: el conteo real también cabe en el contexto.
        if type(count) is int and count + MAX_OUTPUT > info['context']:
            raise pilot.PilotError('PAQUETE_SUPERA_CONTEXTO_DEL_MODELO_NO_SE_RECORTA')
        return original_budget(b, count)

    holder = preflight if preflight is not None else {}
    values = dict(TASK=task_id, MODEL=model, EFFORT=effort, MAX_OUTPUT=MAX_OUTPUT, MAX_USD=max_usd,
                  INPUT_PRICE=info['input'], OUTPUT_PRICE=info['output'], SYSTEM=encargo, SCHEMA=SCHEMA,
                  validate=validate, write=make_writer(bundle, holder), budget=budget)
    saved = {k: getattr(cr, k) for k in values}
    try:
        for k, v in values.items():
            setattr(cr, k, v)
        yield holder
    finally:
        for k, v in saved.items():
            setattr(cr, k, v)


def preflight(bundle, holder=None):
    """Antes de cualquier llamada: cota de tokens por bytes (un token ocupa al menos un byte).

    Aborta si el paquete no cabe en el contexto o si la reserva supera el máximo de la
    ejecución. Nunca recorta el paquete. Usa la configuración activa de critical_review.
    """
    info = MODELS[cr.MODEL]
    payload_bytes = len(pilot.canonical(cr.payload(bundle)))
    bound = payload_bytes + MARGIN_TOKENS
    reserve = (Decimal(bound) * cr.INPUT_PRICE + Decimal(MAX_OUTPUT) * cr.OUTPUT_PRICE) / 1_000_000
    result = {'payload_bytes': payload_bytes, 'input_tokens_upper_bound': bound,
              'input_tokens_rough_estimate': math.ceil(payload_bytes / 3.5),
              'max_output_tokens': MAX_OUTPUT, 'context_tokens': info['context'],
              'reserve_upper_bound_usd': str(reserve), 'max_usd': str(cr.MAX_USD),
              'usd_per_mtok_input': str(cr.INPUT_PRICE), 'usd_per_mtok_output': str(cr.OUTPUT_PRICE),
              'prices_checked': PRICES_CHECKED}
    if holder is not None:
        holder.update(result)
    if bound + MAX_OUTPUT > info['context']:
        raise pilot.PilotError('PAQUETE_SUPERA_CONTEXTO_DEL_MODELO_NO_SE_RECORTA')
    if reserve > cr.MAX_USD:
        raise pilot.PilotError('COSTE_MAXIMO_INSUFICIENTE_NO_SE_RECORTA')
    return result


class DirectHTTP(cr.StreamingHTTP):
    """El transporte SSE de AUTO1 sin cambios; solo amplía la lista de modelos autorizados.

    pilot.HTTP.__init__ admite únicamente Sonnet 5.5 y Fable 5.2; aquí se valida contra
    MODELS (con sus tarifas). El cuerpo de cada llamada sigue ligado a self.model.
    """
    def __init__(self, github_token='', api_key='', model=DEFAULT_MODEL):
        if model not in MODELS:
            raise pilot.PilotError('MODELO_NO_AUTORIZADO')
        self.github_token, self.api_key, self.model = github_token, api_key, model


def task_id_for(empresa, run_id):
    if not isinstance(run_id, str) or not re.fullmatch(r'[0-9]{1,20}', run_id):
        raise pilot.PilotError('RUN_ID_INVALIDO')
    return f'analisis-directo-{_slug(empresa, "EMPRESA_INVALIDA")}-{run_id}'


def execute(http, bundle, encargo, model, effort, max_usd, output, live=False, receipt=None):
    """Comprobación previa y, solo si pasa, critical_review.run (una llamada como máximo)."""
    with configured(bundle['task_id'], model, effort, max_usd, bundle, encargo) as holder:
        try:
            preflight(bundle, holder)
        except pilot.PilotError as err:
            write_abort(output, bundle, holder, str(err))
            raise
        return cr.run(http, bundle, output, receipt=receipt, execute=live)


def write_abort(output, bundle, holder, code):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    lines = ['# Análisis directo · ' + bundle['caso'], '', 'Abortado antes de llamar: `' + code + '`', '',
             'Ninguna llamada a Anthropic, ninguna reserva. El paquete no se recorta.', '']
    lines += [f'- {k}: {v}' for k, v in holder.items()]
    (output / 'report.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    (output / 'preflight.json').write_bytes(pilot.canonical({'error': code, **holder}))


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--empresa', required=True)
    p.add_argument('--package', required=True, help='manifiesto JSON versionado en el repo')
    p.add_argument('--model', default=DEFAULT_MODEL)
    p.add_argument('--effort', default='high')
    p.add_argument('--max-usd', required=True)
    p.add_argument('--run-id', required=True)
    p.add_argument('--code-sha', required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--execute-api', action='store_true')
    a = p.parse_args(argv)
    try:
        max_usd = parse_max_usd(a.max_usd)
        task_id = task_id_for(a.empresa, a.run_id)
        encargo = verify_code(ROOT, a.code_sha)
        bundle = build_bundle(load_package(ROOT, a.code_sha, a.package, a.empresa), encargo, task_id, a.code_sha)
        http = DirectHTTP(os.getenv('GH_TOKEN', ''), os.getenv('ANTHROPIC_API_KEY', ''), model=a.model)
        report = execute(http, bundle, encargo, a.model, a.effort, max_usd, a.output, live=a.execute_api)
        print(json.dumps({k: report.get(k) for k in ('task_id', 'state', 'api_messages_sent', 'estimated_cost_usd', 'error')}))
        # YA_RESERVADO_SIN_NUEVA_LLAMADA (p. ej. «Re-run» de la misma ejecución) sale con 1:
        # no hay análisis nuevo y no debe parecer un éxito.
        return 0 if report['state'] in OK_STATES else 1
    except (pilot.PilotError, subprocess.CalledProcessError, OSError) as err:
        print(str(err) if isinstance(err, pilot.PilotError) else 'GIT_O_ARCHIVO_NO_VERIFICABLE', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
