"""Sonda NUEVA propia de A3-R1 (no esta en la lista del informe): el signo impreso
negativo no debe igualarse a un valor declarado positivo, y el signo con signo
debe mapear por posicion. Uso: python3 -I -B s11_R1_sonda_nueva.py RUTA/scripts/verificar_contexto.py SALIDA.json"""
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
# R1f: declarado POSITIVO 9000 pero impreso (9.000) negativo -> CONFLICTO real (no OK)
reg('R1f_signo_impreso_negativo_no_iguala_a_positivo', col(['2025 2024', 'Cash (10.000) (9.000)'], 1, '2024 (comparativo)', 9000), {'CONFLICTO'},
    'Valor declarado +9000 en columna 2024 pero impreso "(9.000)" (negativo): debe ser CONFLICTO, no OK.')
# R1g: U+2212 en la columna equivocada -> CONFLICTO por posicion, no por signo
reg('R1g_unicode_menos_columna_equivocada', col(['2025 2024', 'Inventories −47.708 −7.660'], 1, '2025 (ejercicio)', -7660), {'CONFLICTO'},
    'Declarado 2025 = -7660 pero el valor -7.660 esta en la columna 2024: CONFLICTO por posicion.')
# R1h (control positivo): U+2212 en su columna -> OK
reg('R1h_unicode_menos_en_su_columna', col(['2025 2024', 'Inventories −47.708 −7.660'], 1, '2024 (comparativo)', -7660), {'OK'},
    'Control positivo: -7.660 impreso con U+2212 en la columna 2024 declarada -> OK.')
Path(sys.argv[2]).write_text(json.dumps({'modulo': str(mp), 'sondas': out}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
for s in out:
    print(f"[{'DEFECTO' if s['defecto'] else 'ok     '}] {s['sonda']}: obtenido={s['obtenido']} esperado={s['esperado']} | {s['detalle'][:160]}")
