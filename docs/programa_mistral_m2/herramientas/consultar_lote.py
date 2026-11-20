"""Muestra un lote acotado del registro histórico, sin afirmaciones de revisión heredadas."""
import argparse
import json
from pathlib import Path


def main():
    tarea = Path(__file__).resolve().parents[1]
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--empresa', required=True, choices=['Vidrala', 'Viscofan'])
    ap.add_argument('--inicio', type=int, default=0)
    ap.add_argument('--limite', type=int, default=20)
    ap.add_argument('--solo-nuevas', action='store_true')
    ap.add_argument('--solo-derivados', action='store_true')
    a = ap.parse_args()
    if a.inicio < 0 or not 1 <= a.limite <= 30:
        ap.error('inicio debe ser no negativo; limite entre 1 y 30')
    data = json.loads((tarea / 'entrada/registro_base.json').read_text(encoding='utf-8'))
    rows = data[a.empresa]['entradas']
    if a.solo_nuevas:
        rows = [r for r in rows if not r['cubierta_en_piloto']]
    if a.solo_derivados:
        rows = [r for r in rows if r['clase'] == 'derivado']
    selected = rows[a.inicio:a.inicio + a.limite]
    print(json.dumps({'empresa': a.empresa, 'filas_filtradas': len(rows),
                      'inicio': a.inicio, 'mostradas': len(selected),
                      'entradas_declaradas_no_acreditadas': selected}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
