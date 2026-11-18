"""Revalida fuera de línea la salida en bruto de una ejecución ya pagada. Sin red, sin API.

Uso: python3 -I automation/direct_analysis/revalidar.py REPORT.json SOURCES.json SALIDA_DIR

Aplica el validador actual (`validate`) a `raw_model_output` del informe publicado en el
registro (rama de AUTO1) con el paquete publicado (`sources.json`). El resultado no es una
aceptación: queda REVALIDADO_FUERA_DE_LINEA_PENDIENTE_DECISION_HUMANA, con la huella del
informe original y del código que revalida. No toca la reserva ni el tope.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parent / 'coordination'), str(HERE.parent / 'claude_review')]
import direct_analysis as da  # noqa: E402
import critical_review as cr  # noqa: E402
import pilot  # noqa: E402

ESTADO = 'REVALIDADO_FUERA_DE_LINEA_PENDIENTE_DECISION_HUMANA'


ERRORES_DE_FORMA = ('JSON_INVALIDO',)


def revalidar(report, bundle):
    # R1: solo rescata rechazos de forma; un rechazo de contenido (ESQUEMA_INVALIDO, etc.) no.
    if report.get('error') not in ERRORES_DE_FORMA:
        raise pilot.PilotError('SOLO_SE_REVALIDAN_RECHAZOS_DE_FORMA')
    # R2: el paquete tiene que ser exactamente el enviado en esa ejecución.
    if pilot.digest(pilot.canonical(bundle)) != report.get('bundle_sha256'):
        raise pilot.PilotError('PAQUETE_DISTINTO_DEL_ENVIADO')
    if report.get('stop_reason') != 'end_turn' or not isinstance(report.get('raw_model_output'), str):
        raise pilot.PilotError('SIN_SALIDA_COMPLETA_QUE_REVALIDAR')
    response = {'stop_reason': 'end_turn', 'content': [{'type': 'text', 'text': report['raw_model_output']}]}
    with da.configured(report['task_id'], report['model_requested'], report['effort_requested'],
                       da.Decimal('5'), bundle, ''):
        review = da.validate(response, bundle)
    return review


def main(argv=None):
    a = argv if argv is not None else sys.argv[1:]
    if len(a) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    rep_raw, src_raw = Path(a[0]).read_bytes(), Path(a[1]).read_bytes()
    report, bundle = json.loads(rep_raw), json.loads(src_raw)
    out = Path(a[2]); out.mkdir(parents=True, exist_ok=True)
    try:
        code = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=HERE, text=True).strip()
        sucio = subprocess.check_output(['git', 'status', '--porcelain', '--', 'automation'], cwd=HERE, text=True).strip()
        if sucio:
            code += '+cambios_sin_confirmar'
    except (OSError, subprocess.CalledProcessError):
        code = None
    base = {'estado': ESTADO, 'task_id': report.get('task_id'), 'coste_original_usd': report.get('estimated_cost_usd'),
            'error_original': report.get('error'), 'report_sha256': hashlib.sha256(rep_raw).hexdigest(),
            'sources_sha256': hashlib.sha256(src_raw).hexdigest(), 'codigo_que_revalida': code,
            'accepted': False, 'integrated': False, 'product_executed': False,
            'nota': 'No es aceptación ni aptitud. La decide la persona responsable.'}
    try:
        base['review'] = revalidar(report, bundle)
        base['resultado'] = 'VALIDO_CON_EL_VALIDADOR_ACTUAL'
    except pilot.PilotError as err:
        base['resultado'] = 'SIGUE_INVALIDO'
        base['error'] = str(err)
    (out / 'revalidacion.json').write_bytes(pilot.canonical(base))
    print(json.dumps({k: base.get(k) for k in ('estado', 'resultado', 'error', 'task_id')}, ensure_ascii=False))
    return 0 if base['resultado'] == 'VALIDO_CON_EL_VALIDADOR_ACTUAL' else 1


if __name__ == '__main__':
    sys.exit(main())
