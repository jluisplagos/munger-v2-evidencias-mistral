#!/usr/bin/env python3
"""Lista propuesta de finalistas a partir de los informes del cribado ya publicados.

Mecánico y sin opinión: lee `report.json` de cada empresa cribada en las ejecuciones que se
declaran (rama de registro, `automation/coordination/reviews/cribado-<ejecución>-<slug>/`) y
aplica un criterio fijo sobre los resultados de los filtros que devolvió el modelo. No
revisa ni acepta esos resultados (siguen pendientes de revisión), no mira cifras ni el
veredicto, no prioriza y no es una recomendación. Sin red: lee del clon con `git show`.

Criterio (declarado aquí; cambiarlo es un cambio de código que se revisa):

- solo cuentan los informes en `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION` (respuesta con
  formato válido); los demás constan como «sin resultado utilizable»;
- nivel 1: `calidad`, `caja` y `balance` = `pasa`, y `precio` = `pasa` o `dudoso`;
- nivel 2: ninguno de `calidad`, `caja` y `balance` es `no_pasa` ni `no_aplica`, al menos
  dos de los tres son `pasa`, y `precio` = `pasa` o `dudoso`;
- `encaje` no cuenta (nunca elimina: el paquete no trae la cartera);
- el `veredicto_cribado` se muestra como información y no entra en el criterio.

Finalistas propuestos = nivel 1 + nivel 2. La lista es una propuesta para la persona
responsable, que decide.
"""
import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
REGISTRO = 'origin/automatizacion/claude-api-piloto-registro'
CARPETA = 'automation/coordination/reviews'
VALIDO = 'AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION'
FILTROS = ('calidad', 'caja', 'balance', 'precio', 'encaje')
TRES = ('calidad', 'caja', 'balance')
PRECIO_OK = ('pasa', 'dudoso')
CRITERIO = [
    'Solo cuentan los informes en ' + VALIDO + ' (respuesta con formato válido).',
    'Nivel 1: calidad, caja y balance = pasa, y precio = pasa o dudoso.',
    'Nivel 2: ninguno de calidad, caja y balance es no_pasa ni no_aplica; al menos dos de los tres son pasa; '
    'precio = pasa o dudoso.',
    'Encaje no cuenta (nunca elimina). El veredicto del cribado se muestra y no entra en el criterio.',
    'Finalistas propuestos = nivel 1 + nivel 2. Es una propuesta mecánica, no una recomendación.',
]


def nivel(filtros):
    r = {k: (filtros.get(k) or {}).get('resultado') for k in FILTROS}
    if r['precio'] not in PRECIO_OK:
        return None
    tres = [r[k] for k in TRES]
    if all(v == 'pasa' for v in tres):
        return 1
    if not any(v in ('no_pasa', 'no_aplica', None) for v in tres) and tres.count('pasa') >= 2:
        return 2
    return None


def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, check=True).stdout


def leer(registro, ejecuciones):
    filas = []
    nombres = git('ls-tree', '--name-only', f'{registro}:{CARPETA}').decode().split()
    for run in ejecuciones:
        for carpeta in sorted(n for n in nombres if n.startswith(f'cribado-{run}-')):
            slug = carpeta[len(f'cribado-{run}-'):]
            if slug.startswith('tanda-'):
                continue
            try:
                doc = json.loads(git('show', f'{registro}:{CARPETA}/{carpeta}/report.json'))
            except subprocess.CalledProcessError:
                filas.append({'ejecucion': run, 'slug': slug, 'estado': 'SIN_REPORT_JSON'})
                continue
            c = (doc.get('review') or {}).get('cribado') or {}
            f = c.get('filtros') or {}
            filas.append({'ejecucion': run, 'slug': slug, 'empresa': c.get('empresa') or slug,
                          'estado': doc.get('state'), 'carpeta': f'{CARPETA}/{carpeta}',
                          'filtros': {k: (f.get(k) or {}).get('resultado') for k in FILTROS},
                          'veredicto_cribado': c.get('veredicto_cribado'),
                          'dcf_plantilla_aplica': c.get('dcf_plantilla_aplica'),
                          'nivel': nivel(f) if doc.get('state') == VALIDO else None})
    return filas


def informe(filas, registro_sha, ejecuciones, excluidas):
    fin = [x for x in filas if x.get('nivel')]
    lines = ['# Segunda vuelta del universo · finalistas propuestos (criterio mecánico)', '',
             f'- Rama de registro: `{REGISTRO}` en `{registro_sha}`.',
             f'- Ejecuciones del cribado leídas: {", ".join(ejecuciones)}. ' + excluidas,
             f'- Empresas leídas: {len(filas)}; con resultado utilizable: '
             f'{sum(1 for x in filas if x.get("estado") == VALIDO)}.',
             '- Resultados de los filtros tal como los devolvió el modelo en el cribado: **sin revisar ni aceptar**.',
             '- Generado por `automation/screening/finalistas.py` (sin API, sin red). No es una recomendación de '
             'compra ni una prioridad: decide la persona responsable.', '', '## Criterio', '']
    lines += [f'{i}. {c}' for i, c in enumerate(CRITERIO, 1)]
    lines += ['', '## Finalistas propuestos', '',
              '| Nivel | Empresa | Calidad | Caja | Balance | Precio | Veredicto del cribado (informativo) | Ejecución |',
              '|---|---|---|---|---|---|---|---|']
    for x in sorted(fin, key=lambda x: (x['nivel'], x['empresa'].lower())):
        f = x['filtros']
        lines.append(f"| {x['nivel']} | {x['empresa']} | {f['calidad']} | {f['caja']} | {f['balance']} | {f['precio']} "
                     f"| {x['veredicto_cribado']} | {x['ejecucion']} |")
    lines += ['', '## Todas las empresas leídas', '',
              '| Empresa | Estado | Calidad | Caja | Balance | Precio | Encaje | Veredicto del cribado | Nivel |',
              '|---|---|---|---|---|---|---|---|---|']
    for x in sorted(filas, key=lambda x: x.get('empresa', x['slug']).lower()):
        f = x.get('filtros') or {k: '—' for k in FILTROS}
        lines.append(f"| {x.get('empresa', x['slug'])} | {x['estado']} | {f['calidad']} | {f['caja']} | {f['balance']} "
                     f"| {f['precio']} | {f['encaje']} | {x.get('veredicto_cribado')} | {x.get('nivel') or '—'} |")
    return '\n'.join(lines) + '\n', fin


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--registro', default=REGISTRO)
    p.add_argument('--ejecuciones', required=True, help='ids de ejecución del cribado, separados por comas')
    p.add_argument('--nota-excluidas', default='', help='frase sobre las ejecuciones que no se leen')
    p.add_argument('--salida', type=Path, required=True, help='ruta base: escribe .md y .json')
    a = p.parse_args(argv)
    ejecuciones = [r.strip() for r in a.ejecuciones.split(',') if r.strip()]
    if not ejecuciones or not all(r.isdigit() for r in ejecuciones):
        print('EJECUCIONES_INVALIDAS', file=sys.stderr)
        return 2
    sha = git('rev-parse', a.registro).decode().strip()
    filas = leer(a.registro, ejecuciones)
    md, fin = informe(filas, sha, ejecuciones, a.nota_excluidas)
    a.salida.with_suffix('.md').write_text(md, encoding='utf-8')
    a.salida.with_suffix('.json').write_text(json.dumps(
        {'registro': a.registro, 'registro_sha': sha, 'ejecuciones': ejecuciones, 'criterio': CRITERIO,
         'finalistas': [{k: x[k] for k in ('empresa', 'slug', 'nivel', 'ejecucion', 'carpeta')} for x in
                        sorted(fin, key=lambda x: (x['nivel'], x['empresa'].lower()))],
         'empresas': filas}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(json.dumps({'leidas': len(filas), 'finalistas': [x['empresa'] for x in fin]}, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
