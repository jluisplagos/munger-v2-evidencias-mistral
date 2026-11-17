"""Sonda NUEVA propia de A3-R6 (no esta en la lista del informe): formas de millones no
reconocidas antes ('EUR millions', '€ million', 'Millones de €') deben marcar escala
contraria. Uso: python3 -I -B s11_R6_sonda_nueva.py RUTA/scripts/verificar_contexto.py SALIDA.json"""
import importlib.util, json, sys
from pathlib import Path
mp = Path(sys.argv[1]).resolve(); sys.path.insert(0, str(mp.parent))
spec = importlib.util.spec_from_file_location('vc', mp)
V = importlib.util.module_from_spec(spec); spec.loader.exec_module(V)
out = []
def reg(nombre, obtenido, esperado, desc):
    est = obtenido[0]
    out.append({'sonda': nombre, 'descripcion': desc, 'esperado': sorted(esperado), 'obtenido': est,
                'detalle': str(obtenido[1])[:240], 'defecto': est not in esperado})
DOC_MILES = {'head': 'Consolidated financial statements 2025 (Thousands of euros)', 'miles': True, 'millones': False}
reg('R6a_EUR_millions', V.check_unidad(['Figures in EUR millions', 'Revenue 10.000'], 1, 'miles de euros', '0.001', 10000, 'Revenue 10.000', DOC_MILES), {'CONFLICTO', 'NO_DECIDIBLE'},
    'Página "Figures in EUR millions" con cabecera en miles: CONFLICTO (escala contraria).')
reg('R6b_euro_million_simbolo', V.check_unidad(['Amounts in € million', 'Revenue 10.000'], 1, 'miles de euros', '0.001', 10000, 'Revenue 10.000', DOC_MILES), {'CONFLICTO', 'NO_DECIDIBLE'},
    'Página "Amounts in € million" con cabecera en miles: CONFLICTO.')
reg('R6c_millones_de_euro_simbolo', V.check_unidad(['(Millones de €)', 'Ventas 10.000'], 1, 'miles de euros', '0.001', 10000, 'Ventas 10.000', DOC_MILES), {'CONFLICTO', 'NO_DECIDIBLE'},
    'Página "(Millones de €)" con cabecera en miles: CONFLICTO.')
reg('R6d_million_EUR_orden_inverso', V.check_unidad(['Amounts in million EUR', 'Revenue 10.000'], 1, 'miles de euros', '0.001', 10000, 'Revenue 10.000', DOC_MILES), {'CONFLICTO', 'NO_DECIDIBLE'},
    'Página "Amounts in million EUR" (orden inverso) con cabecera en miles: CONFLICTO.')
reg('R6e_control_positivo_miles', V.check_unidad(['(Miles de euros)', 'Ventas 10.000'], 1, 'miles de euros', '0.001', 10000, 'Ventas 10.000', None), {'OK'},
    'Control positivo: página en miles, unidad miles -> OK (no falso positivo de la ampliación).')
Path(sys.argv[2]).write_text(json.dumps({'modulo': str(mp), 'sondas': out}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
for s in out:
    print(f"[{'DEFECTO' if s['defecto'] else 'ok     '}] {s['sonda']}: obtenido={s['obtenido']} esperado={s['esperado']} | {s['detalle'][:150]}")
