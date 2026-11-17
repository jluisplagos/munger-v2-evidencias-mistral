"""Sonda PROPIA de A4-R1 (variante no literal, distinta de las del informe s07):
polaridad de la reexpresion decidida por la DECLARACION (si/no), no por palabras
sueltas como 'sin' en la razon. Sintetica; no modifica nada.
Uso: python3 -I -B s12_A4_R1_sonda_polaridad.py RUTA/scripts SALIDA.json"""
import importlib.util, json, sys, tempfile
from pathlib import Path
sd = Path(sys.argv[1]).resolve(); sys.path.insert(0, str(sd))
def load(name):
    spec = importlib.util.spec_from_file_location(name + '_a4', sd / (name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
V = load('verificar_contexto')
out = {'scripts': sd.name, 'sondas': []}
def reg(nombre, obtenido, esperado, desc):
    est = obtenido[0] if isinstance(obtenido, (list, tuple)) else obtenido
    det = obtenido[1] if isinstance(obtenido, (list, tuple)) and len(obtenido) > 1 else ''
    out['sondas'].append({'sonda': nombre, 'descripcion': desc, 'esperado': sorted(esperado),
                          'obtenido': est, 'detalle': str(det)[:260], 'defecto': est not in esperado})

def reex(nombre, declared, esperado, desc, valor=9000, cita='Revenue 9.000'):
    with tempfile.TemporaryDirectory() as td:
        o = Path(td) / 'CF_2024.txt'
        o.write_text('[PDF PAGE 1]\nConsolidated accounts 2024 (thousands of euros)\n2024 2023\nRevenue 10.000 8.000\n', encoding='utf-8')
        V.TEXTO_CACHE['A4S'] = {o.name: o}
        V.C.CARPETA_EMPRESA['A4S'] = td
        f = {'archivo': 'CF_2025.txt', 'columna': '2024', 'periodo': 'ejercicio 2024',
             'unidad': 'miles de euros', 'perimetro': 'consolidado', 'escala': '0.001',
             'cita': cita, 'valor_fuente': valor, 'reexpresado': declared}
        reg(nombre, V.check_reexpresion('A4S', {}, f, ['2025', '2024'], ['2025', '2024']), esperado, desc)

reex('V1_afirmacion_con_sin_entre_parentesis', 'sí, 2024 reexpresado (sin Italia)', {'OK', 'NO_DECIDIBLE'},
     'Afirmacion con «sin» entre parentesis en la razon: la polaridad es positiva (antes invertia a CONFLICTO «declara no reexpresado»).')
reex('V2_no_restatement_was_made', 'no restatement of comparatives was made', {'CONFLICTO', 'NO_DECIDIBLE'},
     'Negacion «no restatement …» + diferencia 9.000 frente a 10.000: debe ser CONFLICTO, no OK falso.')
reex('V3_comparatives_were_not_restated', 'comparatives were not restated', {'CONFLICTO', 'NO_DECIDIBLE'},
     'Negacion «were not restated» + diferencia: CONFLICTO.')
reex('V4_afirmacion_sin_si_explicito', 'reexpresado por cambio de perimetro', {'OK', 'NO_DECIDIBLE'},
     'Mencion afirmativa sin «sí» inicial: afirmativa (no negada).')
reex('V5_control_no_reexpresado_e_igual', 'no reexpresado', {'NO_APLICA', 'NO_DECIDIBLE'},
     'Control: «no reexpresado» con el original imprimiendo el MISMO valor (10.000) no es contradiccion (NO_APLICA coherente).',
     valor=10000, cita='Revenue 10.000')

Path(sys.argv[2]).write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for s in out['sondas']:
    print(f"[{'DEFECTO' if s['defecto'] else 'ok     '}] {s['sonda']}: obtenido={s['obtenido']} esperado={s['esperado']}")
print('defectos:', sum(s['defecto'] for s in out['sondas']), 'de', len(out['sondas']))
