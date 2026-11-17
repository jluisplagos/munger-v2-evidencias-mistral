"""Sonda NUEVA propia de A3-R4 (no esta en la lista del informe): sin atajo de
«no reexpresado + valor suelto», rótulo completo, escala/perímetro comparados y
negación por polaridad. Uso: python3 -I -B s11_R4_sonda_nueva.py RUTA/scripts/verificar_contexto.py SALIDA.json"""
import importlib.util, json, sys, tempfile
from pathlib import Path
mp = Path(sys.argv[1]).resolve(); sys.path.insert(0, str(mp.parent))
spec = importlib.util.spec_from_file_location('vc', mp)
V = importlib.util.module_from_spec(spec); spec.loader.exec_module(V)
out = []
def reg(nombre, obtenido, esperado, desc):
    est = obtenido[0] if isinstance(obtenido, (list, tuple)) else obtenido
    out.append({'sonda': nombre, 'descripcion': desc, 'esperado': sorted(esperado), 'obtenido': est,
                'detalle': str(obtenido[1] if isinstance(obtenido, (list, tuple)) and len(obtenido) > 1 else '')[:240],
                'defecto': est not in esperado})
def reex(nombre, original, f, esperado, desc):
    with tempfile.TemporaryDirectory() as td:
        o = Path(td) / 'CF_2024.txt'; o.write_text(original, encoding='utf-8')
        V.TEXTO_CACHE['S11'] = {o.name: o}
        reg(nombre, V.check_reexpresion('S11', {}, f, ['2025', '2024'], ['2025', '2024']), esperado, desc)
base = {'archivo': 'CF_2025.txt', 'columna': '2024', 'periodo': 'ejercicio 2024', 'unidad': 'miles de euros', 'escala': '0.001', 'perimetro': 'estados consolidados'}
ORIG = '[PDF PAGE 1]\nConsolidated accounts 2024 (thousands of euros)\n2024 2023\nRevenue 10000 8000\n'
# R4g: nota de no-reexpresar + valor 28 suelto en otra parte -> NO_DECIDIBLE (sin atajo)
reex('R4g_sin_atajo_valor_suelto_con_nota', '[PDF PAGE 1]\nConsolidated accounts 2024 (thousands of euros)\nThe Group did not restate the comparative figures.\n[PDF PAGE 2]\nNote 28. Leases\n2024 2023\nLease liabilities 41.000 35.000\n',
     dict(base, cita='Right-of-use assets 28', valor_fuente=28, reexpresado='no: comparativo de 2024 (CF_2024 p. 1)'), {'NO_DECIDIBLE', 'CONFLICTO'},
     'La nota «did not restate» + el 28 suelto ya no acreditan: NO_DECIDIBLE.')
# R4h: negación con otra redacción («never restated») + diferencia -> CONFLICTO
reex('R4h_negacion_never_restated', ORIG, dict(base, cita='Revenue 9000', valor_fuente=9000, reexpresado='comparatives were never restated'), {'CONFLICTO'},
     'Negación por polaridad («never restated») con diferencia 9000 vs 10000 -> CONFLICTO, no OK.')
# R4i: rotulo completo igual pero fila distinta con mismo prefijo -> CONFLICTO (3g)
reex('R4i_fila_distinta_mismo_prefijo', '[PDF PAGE 1]\nConsolidated accounts 2024 (thousands of euros)\n2024 2023\nRevenue from discontinued operations 9000 8000\nRevenue 10000 9500\n',
     dict(base, cita='Revenue 9000', valor_fuente=9000, reexpresado='no reexpresado'), {'CONFLICTO'},
     'La fila «Revenue» correcta imprime 10000 en 2024; la de discontinuadas no debe casar -> CONFLICTO.')
# R4j (control positivo): igualdad con rótulo completo y misma escala -> NO_APLICA coherente
reex('R4j_control_igualdad_rotulo_completo', '[PDF PAGE 1]\nConsolidated accounts 2024 (thousands of euros)\n2024 2023\nRevenue 9000 8000\n',
     dict(base, cita='Revenue 9000', valor_fuente=9000, reexpresado='no reexpresado; igual al original'), {'NO_APLICA', 'OK'},
     'Control positivo: igualdad confirmada por rótulo completo en la columna 2024.')
Path(sys.argv[2]).write_text(json.dumps({'modulo': str(mp), 'sondas': out}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
for s in out:
    print(f"[{'DEFECTO' if s['defecto'] else 'ok     '}] {s['sonda']}: obtenido={s['obtenido']} esperado={s['esperado']} | {s['detalle'][:160]}")
