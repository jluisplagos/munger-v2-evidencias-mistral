"""Sonda NUEVA propia de A3-R2 (no esta en la lista del informe): cabecera narrativa con
3 años no debe elegirse sobre la cabecera tabular real, y una cabecera partida en 3
líneas no debe dar OK. Uso: python3 -I -B s11_R2_sonda_nueva.py RUTA/scripts/verificar_contexto.py SALIDA.json"""
import importlib.util, json, sys
from pathlib import Path
mp = Path(sys.argv[1]).resolve(); sys.path.insert(0, str(mp.parent))
spec = importlib.util.spec_from_file_location('vc', mp)
V = importlib.util.module_from_spec(spec); spec.loader.exec_module(V)
out = []
def col(lines, row, declarado, valor):
    yb, cl, cy = V.find_header_block(lines, row)
    r = V.check_columna(row, lines, yb, cl, cy, declarado, 'ejercicio ' + declarado[:4], valor)
    return (r[0], f'{r[1]} | cabecera: {cl!r}')
def reg(nombre, obtenido, esperado, desc):
    est = obtenido[0]
    out.append({'sonda': nombre, 'descripcion': desc, 'esperado': sorted(esperado), 'obtenido': est,
                'detalle': str(obtenido[1])[:240], 'defecto': est not in esperado})
# R2g: frase con 3 años seguida de cabecera real de 2 años; 9.000 es 2024 -> OK por la real
reg('R2g_frase_con_tres_anios_no_suplanta_cabecera', col(['In 2023, 2024 and 2025 the Group grew.', '2025 2024', 'Revenue 10.000 9.000'], 2, '2024 (comparativo)', 9000), {'OK'},
    'La frase narrativa tiene 3 años pero muchas palabras; la cabecera tabular real es "2025 2024". 9.000 en columna 2024 -> OK.')
# R2h: cabecera partida en 3 líneas ('2025' '2024' 'Variation') con fila de 3 valores
reg('R2h_cabecera_partida_tres_lineas', col(['2025', '2024', 'Variation', 'Revenue 3.100 2.030 1.070'], 3, '2024 (comparativo)', 2030), {'NO_DECIDIBLE', 'CONFLICTO'},
    'Cabecera en 3 líneas; el valor 2030 está en la columna 2024 (pos 1 de 3 columnas reales). Con la fusión la fila alinea 3:1 y 2030 mapea a 2024 -> debería ser OK; si no alinea, NO_DECIDIBLE (nunca OK falso por desplazar).')
# R2i: tabla de una sola columna legitima sigue OK (control positivo F23)
reg('R2i_tabla_una_columna_legitima', col(['(Thousand of Euros) 2019', 'Cash 1.234'], 1, '2019 (ejercicio)', 1234), {'OK'},
    'Control positivo: cabecera de una sola columna "(Thousand of Euros) 2019" no es cabecera partida; 1.234 en 2019 -> OK.')
Path(sys.argv[2]).write_text(json.dumps({'modulo': str(mp), 'sondas': out}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
for s in out:
    print(f"[{'DEFECTO' if s['defecto'] else 'ok     '}] {s['sonda']}: obtenido={s['obtenido']} esperado={s['esperado']} | {s['detalle'][:170]}")
