"""Sonda NUEVA propia de A3-R3 (no esta en la lista del informe): un año seguido de coma en
prosa no es importe, y un valor con forma de año sin puntuar sí ocupa su posición.
Uso: python3 -I -B s11_R3_sonda_nueva.py RUTA/scripts/verificar_contexto.py SALIDA.json"""
import importlib.util, json, sys
from pathlib import Path
mp = Path(sys.argv[1]).resolve(); sys.path.insert(0, str(mp.parent))
spec = importlib.util.spec_from_file_location('vc', mp)
V = importlib.util.module_from_spec(spec); spec.loader.exec_module(V)
out = []
def col(lines, row, declarado, valor):
    yb, cl, cy = V.find_header_block(lines, row)
    r = V.check_columna(row, lines, yb, cl, cy, declarado, 'ejercicio ' + declarado[:4], valor)
    return (r[0], f'{r[1]} | cabecera: {cl!r} | años bloque: {yb}')
def reg(nombre, obtenido, esperado, desc):
    est = obtenido[0]
    out.append({'sonda': nombre, 'descripcion': desc, 'esperado': sorted(esperado), 'obtenido': est,
                'detalle': str(obtenido[1])[:240], 'defecto': est not in esperado})
# R3g: 'Note 2024,' en la fila no debe contar como importe -> alinea 2:2 y 9.000 es 2024
reg('R3g_anio_con_coma_en_fila_no_es_importe', col(['2025 2024', 'Revenue 10.000 9.000 (note 2024,)'], 1, '2024 (comparativo)', 9000), {'OK'},
    'La fila trae "(note 2024,)": el token "2024," es un año en prosa, no un importe; 9.000 mapea a 2024 -> OK.')
# R3h: valor 2030 sin separador en la columna 2025 sí ocupa posición (control positivo)
reg('R3h_valor_2030_en_columna_2025', col(['2025 2024', 'Revenue 2030 1.070'], 1, '2025 (ejercicio)', 2030), {'OK'},
    'El importe 2030 (miles) está en la columna 2025 y se declara 2025=2030 -> OK por posición.')
# R3i: el mismo 2030 declarado como 2024 -> CONFLICTO (no desplaza)
reg('R3i_valor_2030_declarado_en_otra_columna', col(['2025 2024', 'Revenue 2030 1.070'], 1, '2024 (comparativo)', 2030), {'CONFLICTO'},
    'Declarado 2024=2030 pero 2030 está en la columna 2025 -> CONFLICTO.')
# R3j: año con coma en prosa cuenta como año del bloque (para versión)
yb, cl, cy = V.find_header_block(['Balance at December 31, 2024, and 2023,', '2024 2023', 'Revenue 10.000 9.000'], 2)
reg('R3j_anio_con_coma_cuenta_en_bloque', ('OK' if yb.count('2024') >= 2 else 'NO_CUENTA', f'años {yb}'), {'OK'},
    '"December 31, 2024," es un año del bloque además del "2024" de la cabecera (inverso de A2-R4).')
Path(sys.argv[2]).write_text(json.dumps({'modulo': str(mp), 'sondas': out}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
for s in out:
    print(f"[{'DEFECTO' if s['defecto'] else 'ok     '}] {s['sonda']}: obtenido={s['obtenido']} esperado={s['esperado']} | {s['detalle'][:170]}")
