"""Sondas dirigidas de especificación F1; importes ficticios, no valoración de Elis.

python3 -B sondas_f1_v3.py --frente FRENTE --libro ELIS.xlsx --salida SONDAS.json
Autor fijado: 716cbd6794b7fcde8b3862c9d1e7acdaf516d262 (código de fd474d3).
No ejecuta pipeline, no adopta decisiones ni modifica libros.
"""
import argparse
from fractions import Fraction as F
import importlib.util
import json
from pathlib import Path
import openpyxl

p = argparse.ArgumentParser()
p.add_argument('--frente', type=Path, required=True)
p.add_argument('--libro', type=Path, required=True)
p.add_argument('--salida', type=Path, required=True)
a = p.parse_args()
spec = importlib.util.spec_from_file_location('autor_f1', a.frente / 'scripts/controles_sinteticos_f1.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

# Oráculo de caja completo: beneficio sostenible 68 perpetuo; gasto temporal 7
# hasta H inclusive. r=10%, g=0 son supuestos SINTÉTICOS, no parámetros de Elis.
r, g, gasto, caja = F(1, 10), F(0), F(7), F(68)
plans = []
for H in [5, 10, 11, 12]:
    extra = lambda t, V, H=H: gasto if t <= H else F(0)
    esc = m.Escenario(trans_v=gasto, trans=extra)
    flows, f11, V = m.motor_sintetico(F(7, 10), esc.f(F(20)), F(0), F(1), F(1), g, extra)
    # Gordon es la estructura vigente del terminal, Motor!BG=BF/(r-g).
    pv_especificado = sum(x / (1+r)**t for t, x in enumerate(flows, 1)) + f11/(r-g)/(1+r)**10
    pv_caja = caja/r - sum(gasto/(1+r)**t for t in range(1, H+1))
    # Los once flujos que ve el banco del autor coinciden aun si falla el valor
    # después del año 11. Se documenta el alcance exacto de esa coincidencia.
    cj, c11 = m.caja_sintetica(esc, F(0), F(0))
    assert flows == cj and f11 == c11
    plans.append({'H': H, 'flujos_1_10': [float(x) for x in flows], 'flujo_11': float(f11),
                  'PV_si_se_inserta_X11_en_Gordon': float(pv_especificado),
                  'PV_de_la_caja_con_horizonte_finito': float(pv_caja),
                  'diferencia': float(pv_especificado-pv_caja),
                  'coincide_caja_hasta_11': True, 'coincide_PV': pv_especificado==pv_caja})
assert plans[0]['coincide_PV'] and plans[1]['coincide_PV']
assert not plans[2]['coincide_PV'] and not plans[3]['coincide_PV']
assert plans[2]['PV_si_se_inserta_X11_en_Gordon'] == plans[3]['PV_si_se_inserta_X11_en_Gordon']

book = openpyxl.load_workbook(a.libro, read_only=True, data_only=True)
formula = openpyxl.load_workbook(a.libro, read_only=True, data_only=False)
dg, dgf = book['Diagnóstico V6'], formula['Diagnóstico V6']
cop = json.loads((a.frente / 'resultados/copia_investigacion_f1.json').read_text())
signs=[]
for n, col in [('MALO','B'),('NORMAL','C'),('BUENO','D')]:
    published=cop['P4_ROIC_terminal'][n]['salto_del_libro (fila 178: ROIC − rentabilidad marginal), puntos']
    actual=dg[f'{col}178'].value*100
    signs.append({'escenario':n,'fila_178_formula':dgf[f'{col}178'].value,'salto_libro_puntos':actual,'salto_rotulado_del_libro_en_copia':published,'signo_contrario':actual*published<0})
book.close();formula.close()
# Lógica escrita A0: E2/decisión 1a exigen ambos ceros; V-F1a usa ambos positivos.
guard=[]
for rou, pagos in [(10,12),(10,0),(0,12),(0,0)]:
    admitido=rou==0 and pagos==0
    dispara=rou>0 and pagos>0
    guard.append({'ROU':rou,'C49':pagos,'A0_admitido_segun_E2_y_1a':admitido,'V_F1a_dispara_segun_E5':dispara,'caso_no_admitido_sin_ese_bloqueo':not admitido and not dispara})
out={'naturaleza':'sondas de especificación, no defectos de producción ni datos de Elis',
     'horizontes_temporales':plans,'salto_terminal_signo':signs,'logica_A0':guard}
a.salida.write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(out,ensure_ascii=False,indent=2))
