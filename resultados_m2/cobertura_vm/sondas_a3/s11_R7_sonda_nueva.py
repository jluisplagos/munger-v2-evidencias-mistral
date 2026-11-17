"""Sonda NUEVA propia de A3-R7 (no esta en la lista del informe): la propagación lee el
estado de un operando derivado de su nodo (transitivo), no del jsonl (NO_APLICA).
Uso: python3 -I -B s11_R7_sonda_nueva.py RUTA/scripts SALIDA.json"""
import importlib.util, json, sys
from pathlib import Path
sdir = Path(sys.argv[1]).resolve(); sys.path.insert(0, str(sdir))
spec = importlib.util.spec_from_file_location('derivaciones', sdir / 'derivaciones.py')
D = importlib.util.module_from_spec(spec); spec.loader.exec_module(D)
out = []
def reg(nombre, obtenido, esperado, desc):
    out.append({'sonda': nombre, 'descripcion': desc, 'esperado': sorted(esperado), 'obtenido': obtenido,
                'defecto': obtenido not in esperado})
# R7a: D = f(E), E derivado, F (fuente de E) en PENDIENTE -> D debe ser PENDIENTE (no REVISADO)
mapa = {('V', 'F'): {'clase': 'dato_publicado', 'celda': 'F'},
        ('V', 'E'): {'clase': 'derivado', 'celda': 'E', 'derivacion': {'origenes': ['F'], 'formula': 'o["F"]'}},
        ('V', 'D'): {'clase': 'derivado', 'celda': 'D', 'derivacion': {'origenes': ['E'], 'formula': 'o["E"]'}}}
ctx = {('V', 'F'): {'estado_contextual': 'PENDIENTE_CONTEXTUAL'}}
nodo = {}
reg('R7a_derivado_pendiente_bloquea_a_dependiente', D.estado_operando('V', 'D', mapa, ctx, nodo), {'PENDIENTE_CONTEXTUAL'},
    'D=f(E), E=f(F), F en PENDIENTE_CONTEXTUAL: D debe propagar PENDIENTE (antes NO_APLICA->REVISADO).')
# R7b: F en CONFLICTO -> D CONFLICTO
ctx2 = {('V', 'F'): {'estado_contextual': 'CONFLICTO_CONTEXTUAL'}}
reg('R7b_derivado_conflicto_bloquea_a_dependiente', D.estado_operando('V', 'D', mapa, ctx2, {}), {'CONFLICTO_CONTEXTUAL'},
    'F en CONFLICTO: D debe ser CONFLICTO.')
# R7c (control positivo): F revisado -> D revisado
ctx3 = {('V', 'F'): {'estado_contextual': 'REVISADO_CONTEXTUAL'}}
reg('R7c_control_positivo_todo_revisado', D.estado_operando('V', 'D', mapa, ctx3, {}), {'REVISADO_CONTEXTUAL'},
    'Control positivo: F REVISADO -> D REVISADO.')
# R7d: E derivado cubierto en piloto -> REUTILIZADO_M1 aunque F esté pendiente
mapa_p = {('V', 'F'): {'clase': 'dato_publicado', 'celda': 'F'},
          ('V', 'E'): {'clase': 'derivado', 'celda': 'E', 'cubierta_en_piloto': True, 'derivacion': {'origenes': ['F'], 'formula': 'o["F"]'}},
          ('V', 'D'): {'clase': 'derivado', 'celda': 'D', 'derivacion': {'origenes': ['E'], 'formula': 'o["E"]'}}}
reg('R7d_piloto_reutilizado_m1', D.estado_operando('V', 'E', mapa_p, ctx, {}), {'REUTILIZADO_M1'},
    'E cubierto en piloto -> REUTILIZADO_M1 (alcance del piloto), aunque F esté pendiente.')
Path(sys.argv[2]).write_text(json.dumps({'modulo': 'derivaciones.py', 'sondas': out}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
for s in out:
    print(f"[{'DEFECTO' if s['defecto'] else 'ok     '}] {s['sonda']}: obtenido={s['obtenido']} esperado={s['esperado']}")
