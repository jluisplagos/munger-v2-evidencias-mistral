"""Reproduce B1 y C1 con lecturas de la base; no importa código del producto/Mistral.

Uso: python3 -I REPRODUCIR_B_C.py --base-tree /ruta/munger_v2_r1
     [--entrega-b /ruta/resultados_m2/pm1] [--salida /ruta/resultado.json]

Sin entrega-b, lee el CSV del commit B congelado mediante git show (sin red).
Solo escribe la salida solicitada. No modifica fuentes ni resultados del autor.
"""
import argparse
import csv
from fractions import Fraction
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess


def precio_si(vector, probabilidades, k=3):
    # Bisección racional de G(P)-k L(P), derivada de su definición.
    values = [Fraction(str(x)) for x in vector]
    weights = [Fraction(str(x)) for x in probabilidades]
    if len(values) != len(weights) or sum(weights) != 1 or min(weights) < 0:
        raise ValueError('distribución inválida')
    lo, hi = min(values), max(values)
    for _ in range(160):
        mid = (lo + hi) / 2
        gain = sum(w * max(v - mid, 0) for v, w in zip(values, weights))
        loss = sum(w * max(mid - v, 0) for v, w in zip(values, weights))
        if gain - k * loss >= 0:
            lo = mid
        else:
            hi = mid
    return float(min((lo + hi) / 2, values[1]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-tree', type=Path, required=True)
    parser.add_argument('--entrega-b', type=Path)
    parser.add_argument('--salida', type=Path)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[2]
    rel = 'resultados_m2/pm1/VIDRALA_REPOSICION_CAPACIDAD.csv'
    if args.entrega_b:
        csv_text = (args.entrega_b / 'VIDRALA_REPOSICION_CAPACIDAD.csv').read_text()
    else:
        csv_text = subprocess.check_output([
            'git', 'show', 'b5a07e007785f0cd194cb6437fcb5cd7029cb79f:' + rel,
        ], cwd=repo, text=True)
    vid = args.base_tree / ('personaje_v2/empresas_v2_correcciones/'
                           '2026-11_Vidrala_ensayo_4_14/vidrala_decisiones/Vidrala/texto')
    observations = []
    for row in csv.DictReader(io.StringIO(csv_text)):
        match = re.fullmatch(r'(CF_\d{4}\.txt) p(\d+) l(\d+)-(\d+)', row['ppe_fuente'])
        if not match:
            raise ValueError('referencia de fuente no reconocida')
        filename, page, first, last = match.groups()
        path = vid / filename
        lines = path.read_text().splitlines()
        context = '\n'.join(lines[max(0, int(first) - 120):int(last)])
        observations.append({
            'anio': int(row['anio']), 'valor_etiquetado_PPE': row['adiciones_ppe_bruto_miles_eur'],
            'fuente': row['ppe_fuente'],
            'encabezado_Intangible_Assets_previo': 'Intangible Assets' in context,
            'linea': lines[int(first) - 1].strip(),
            'sha256_texto': hashlib.sha256(path.read_bytes()).hexdigest(),
        })

    paths = [
        'personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_13/viscofan/'
        'antecedentes/ejecucion_1_4_13/configuracion_v64_variantes.json',
        'personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_13/viscofan/'
        'Viscofan/configuracion_v64_variantes.json',
    ]
    vectors = []
    for relative in paths:
        data = json.loads((args.base_tree / relative).read_text())
        vectors.append(next(v['V'] for v in data['variantes'] if v['clave'] == 'perimetro_alternativo'))
    old_p, ref_p = ['0.25', '0.60', '0.15'], ['0.20', '0.60', '0.20']
    aa, ab = [precio_si(vectors[0], p) for p in (old_p, ref_p)]
    ba, bb = [precio_si(vectors[1], p) for p in (old_p, ref_p)]
    result = {
        'B1': observations,
        'C1': {
            'metodo_revisor': 'bisección racional; sin importar el oráculo del autor o el producto',
            'perimetro': 'Caja en ambas entregas', 'rutas': paths, 'vectores': vectors,
            'tabla_2x2': {'V412_p412': aa, 'V412_pref': ab, 'V413_p412': ba, 'V413_pref': bb},
            'delta_total': bb - aa,
            'efecto_p_orden1': ab - aa, 'efecto_p_orden2': bb - ba,
            'efecto_V_orden1': bb - ab, 'efecto_V_orden2': ba - aa,
        },
    }
    text = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.salida:
        args.salida.write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
