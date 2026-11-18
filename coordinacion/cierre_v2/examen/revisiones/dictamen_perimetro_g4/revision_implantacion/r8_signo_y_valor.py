"""Revisión de la implantación de P-FOSO · R8: signo y valor de la serie de intereses (rama f1/perimetro-foso @ 688df46), sin escribir en el
repositorio. ¿Qué pasa si la cifra de la fuente es la buena pero se declara con otro signo, o si «valor_fuente» no es el literal?
Uso: r8_signo_y_valor.py RAIZ_PERSONAJE_V2 COPIA_EXPEDIENTE"""
import copy, json, os, sys

PV, EXP = sys.argv[1:3]
sys.path.insert(0, os.path.join(PV, "scripts"))
sys.dont_write_bytecode = True
import perimetro_f1 as PF          # noqa: E402
import referencias_mecanicas as RM  # noqa: E402
import config_v2                    # noqa: E402

CFG = config_v2.cargar(os.path.join(PV, "config_v2_v631_f1.json"))
T = json.load(open(os.path.join(EXP, "datos_v63.json"), encoding="utf-8"))
T.pop("perimetro_f1", None)
D = json.load(open(os.path.join(EXP, "motor_a_f1.json"), encoding="utf-8"))
SI = "intereses_arrendamiento"


def ver(nombre, cambios, todos=False):
    d = copy.deepcopy(D)
    for y in (d["series"][SI] if todos else ["2025"]):
        d["series"][SI][y].update(cambios)
    pf = PF.desde_datos(copy.deepcopy(T), d, EXP)
    cf = pf["intereses_arrendamiento"]["comprobacion_fuentes"]
    rm = RM.calcular({**copy.deepcopy(T), "perimetro_f1": pf}, CFG)["palancas"]["roic_lp"]
    m = pf["roic_propio_pagado_el_alquiler_medio"]
    print(f"{nombre}: intereses 2025 usados {pf['por_anio']['2025'].get('intereses_arrendamiento')} · ROIC propio 2025 "
          f"{pf['por_anio']['2025'].get('roic_propio_pagado_el_alquiler')} · media {m if m is None else round(m, 6)} · utilizable {pf['roic_propio_utilizable']} · "
          f"comprobada {cf['comprobada']} · inválidas {cf['invalidas'][:1]} · incompletas {cf['incompletas'][:1]} · referencia BUENO {rm['BUENO']}")


ver("0 · serie correcta (valor_fuente −465, signo −1)", {})
ver("1 · signo +1 en 2025 (la cifra publicada es la buena; el interés entraría como ingreso)", {"signo": 1})
ver("2 · signo +1 en los cinco años", {"signo": 1}, todos=True)
ver("3 · valor_fuente −100 con el literal bueno «(465)»", {"valor_fuente": -100})
ver("4 · valor_fuente +465 con el literal «(465)» y signo +1", {"valor_fuente": 465, "signo": 1})
ver("5 · signo 0 en 2025", {"signo": 0})
ver("6 · tratamiento «ninguno» y signo −1 (como la serie buena)", {"tratamiento": "ninguno"})
