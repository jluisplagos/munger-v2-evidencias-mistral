#!/usr/bin/env python3
"""Regenera scripts/especificaciones/relevos_casos.json (datos de los relevos D4-R4).

Fuente única: el banco (casos_aceptacion.jsonl + fixtures) + MAPA_CRITERIOS_BANCO.csv
+ las especificaciones del arnés + adaptaciones.json. Nada se inventa a mano por caso:
lo específico de cada caso sale del banco (entrada_usuario, archivos_sinteticos,
criterios_observables, conductas_inaceptables, esperado_numerico, precondiciones) y
lo genérico (recorrido del personaje, modelos de config_v2.json) es común a los 36.

Cada caso queda con:
- estado_inicial: expediente base (ruta RELATIVA a la candidata), comando que lo deja
  bajo RUN_DIR, fixture del banco -> archivo del producto, registro inicial, y (Q1-028)
  la aprobación de partida como aprobación AUTÉNTICA de prueba (PLAN §2), no el JSON;
- preparacion_comandos: comandos ejecutables en orden;
- fases: pasos del pipeline en orden con actor, modelo, esfuerzo, si el agente es nuevo
  o continúa, código esperado en la parada y artefacto de salida;
- entrada: texto exacto (entrada_usuario del banco) y a quién se entrega;
- artefacto_por_criterio: uno por cada criterio del banco con archivo relativo al
  expediente, campo/sección, condición de CUMPLE y de FALLA, o NO_OBSERVABLE /
  ADAPTACION_PENDIENTE / DECISION_PENDIENTE con motivo;
- comando_relevo: comando ejecutable del personaje (preparar + pipeline con flock).

Uso: python3 -B scripts/actualizar_relevos.py
"""
import csv
import json
import os
import sys

sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
AUX = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
import lib_arnes as L  # noqa: E402

OUT = os.path.join(AQUI, "especificaciones", "relevos_casos.json")

EXP_BASE_DEFAULT = "munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_13/viscofan/Viscofan"
EXP_BASE_POR_CASO = {
    # D4-R3: Q1-026 sobre la base 4.14, en la que fase1_historia.py construir da 0
    "Q1-026": "munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/viscofan/Viscofan",
}

# Recorrido del personaje comprobado (MECANISMO_PERSONAJE.md, candidata 957af65):
# pipeline.py deja los pasos de agente con código 10 + ESPERANDO.md + prompts_generados/;
# el runtime lanza un subagente por relevo según config_v2.json -> modelos; sin API.
FASES = [
    {"orden": 1, "paso": 5, "fase": "extracción (extraccion_v63)",
     "agente": "subagente NUEVO por relevo", "modelo": "sonnet", "esfuerzo": "medio",
     "codigo_esperado": [10], "parada": "prompts_generados/05_*.md + ESPERANDO.md",
     "salida": "extracto_v63.md, fase1_v63.json, fase1_partes/, fase1_fuentes.json"},
    {"orden": 2, "paso": 6, "fase": "fase A",
     "agente": "subagente NUEVO", "modelo": "opus", "esfuerzo": "alto",
     "codigo_esperado": [10], "parada": "prompts_generados/06_*.md + ESPERANDO.md",
     "salida": "fase_a.json / fase_a.md, celdas_A.json"},
    {"orden": 3, "paso": 8, "fase": "fase B",
     "agente": "subagente NUEVO", "modelo": "opus", "esfuerzo": "alto",
     "codigo_esperado": [10], "parada": "prompts_generados/08_*.md + ESPERANDO.md",
     "salida": "fase_b.json / fase_b.md, celdas_B.json"},
    {"orden": 4, "paso": 10, "fase": "fase C, turno 1",
     "agente": "subagente NUEVO", "modelo": "opus", "esfuerzo": "alto",
     "codigo_esperado": [10], "parada": "prompts_generados/10_*.md + ESPERANDO.md",
     "salida": "fase_c.turno1.json"},
    {"orden": 5, "paso": 10, "fase": "fase C, turno 2 (MISMO agente que el turno 1: SendMessage a su id)",
     "agente": "CONTINÚA el mismo agente del turno 1", "modelo": "opus", "esfuerzo": "alto",
     "codigo_esperado": [10], "parada": "prompts_generados/10_turno2_*.md + ESPERANDO.md",
     "salida": "fase_c.json / fase_c.md, celdas_C.json"},
    {"orden": 6, "paso": 13, "fase": "verificación",
     "agente": "agente NUEVO (distinto del productor)", "modelo": "opus", "esfuerzo": "medio",
     "codigo_esperado": [10], "parada": "prompts_generados/13_*.md + ESPERANDO.md",
     "salida": "solicitud_auditoria.json; estado_pipeline.json -> solicitudes_auditoria (SA-…)"},
    {"orden": 7, "paso": "auditoría", "fase": "auditoría APROBADO del material fijado (cierre_v2.MATERIAL_FIJO)",
     "agente": "auditor NUEVO", "modelo": "opus", "esfuerzo": "medio/alto",
     "codigo_esperado": [10], "parada": "prompts_generados/13_auditoria_*.md + ESPERANDO.md",
     "salida": "auditoria.md que nombra la solicitud SA-… (no conocida ni por huella ni por contenido)"},
    {"orden": 8, "paso": 14, "fase": "cierre (ficha e informe oficiales solo con auditoría APROBADO)",
     "agente": "pipeline (mecánico)", "modelo": "-", "esfuerzo": "-",
     "codigo_esperado": [0, 4, 5, 6], "parada": "ninguna (termina)",
     "salida": "ficha.json, informe.md, publicaciones_resumen.json, estado_pipeline.json"},
]


def artefacto_criterio(caso, idx, crit, row):
    """Mapea un criterio del banco a un artefacto RELATIVO al expediente + campo +
    condiciones de CUMPLE/FALLA, o a NO_OBSERVABLE/ADAPTACION_PENDIENTE/DECISION_PENDIENTE."""
    t = crit.lower()
    conductas = caso.get("conductas_inaceptables") or []
    falla = conductas[idx] if idx < len(conductas) else (
        "se presenta como apto/verificado sin la evidencia que el criterio exige (PLAN §2/§4)")
    cumple = crit
    cob = row["cobertura"]
    if cob == "decision_usuario":
        return {"indice": idx, "criterio": crit, "via": "DECISION_PENDIENTE",
                "motivo": f"{row['razon']} — depende de política no fijada; escalar al responsable (PLAN §3); el arnés no elige política",
                "condicion_cumple": cumple, "condicion_falla": falla}
    if cob == "bloqueo_entorno":
        return {"indice": idx, "criterio": crit, "via": "ADAPTACION_PENDIENTE",
                "motivo": f"{row['razon']} — requiere herramientas del recorrido (soffice en secuencia con flock) y auditoría nueva; no es observable del componente",
                "condicion_cumple": cumple, "condicion_falla": falla}
    # artefacto del expediente según el observable del criterio
    if any(k in t for k in ("aprobaci", "reactiv", "retirada", "invalid")):
        art, campo = "publicaciones_resumen.json + historial_cierres/ + aprobaciones_retiradas.json", \
                     "entradas del resumen / RETIRADA.json / aprobaciones_retiradas"
    elif "auditor" in t:
        art, campo = "auditoria.md + material_auditoria.json + estado_pipeline.json", \
                     "auditoria.md nombra SA-…; material_auditoria.json; solicitudes_auditoria"
    elif any(k in t for k in ("recuento", "verificadas", "pendiente", "doble conteo")):
        art, campo = "verificacion_entradas.json + salida de `verificacion_entradas.py comprobar <exp> --json`", \
                     "entradas[].comprobacion.resultado; recuentos total/comprobadas/pendientes"
    elif any(k in t for k in ("precio", "capitalizaci")):
        art, campo = "precio.json", "precio histórico etiquetado con fecha y fuente / capitalización"
    elif any(k in t for k in ("exportado", "ficha", "informe", "salida", "apto", "apta")):
        art, campo = "ficha.json / informe.md (paso 14); ficha_provisional.json / informe_provisional.md (paso 11)", \
                     "estado del artefacto (apto / no admisible) y su etiquetado"
    elif any(k in t for k in ("pipeline", "bloqueo", "estado de la conclusi")):
        art, campo = "estado_pipeline.json", "estado y causa"
    elif any(k in t for k in ("deuda neta", "derivado", "concili", "fórmula", "formula", "operandos")):
        art, campo = "datos_v63.json + recalc/ + resultados.json", "derivados con operandos declarados"
    elif any(k in t for k in ("hipótesis", "hipotesis")):
        art, campo = "verificacion_entradas.json", "entradas[].hipotesis (fundamento, alternativas, límites)"
    else:
        art, campo = "verificacion_entradas.json", "entradas[celda].fuente / .comprobacion / .incidencia (matriz §4)"
    via = "asercion_componente_y_relevo" if cob == "asercion" else "relevo_personaje"
    out = {"indice": idx, "criterio": crit, "via": via, "artefacto": art, "campo": campo,
           "condicion_cumple": cumple, "condicion_falla": falla}
    if cob == "asercion" and row.get("asercion_arnes"):
        out["asercion_componente"] = row["asercion_arnes"]
        out["evidencia_componente"] = row.get("evidencia", "")
    else:
        out["motivo_sin_asercion"] = row.get("razon") or "observable en el recorrido del personaje (agentes), no en el componente"
    return out


def main():
    casos = [json.loads(l) for l in open(os.path.join(L.BANCO, "casos_aceptacion.jsonl"), encoding="utf-8") if l.strip()]
    mapa = {}
    with open(os.path.join(AUX, "MAPA_CRITERIOS_BANCO.csv"), encoding="utf-8") as f:
        for r in csv.DictReader(f):
            mapa.setdefault(r["caso"], {})[int(r["criterio_indice"])] = r
    ad = json.load(open(os.path.join(AQUI, "especificaciones", "adaptaciones.json"), encoding="utf-8"))["casos"]
    relc = json.load(open(OUT, encoding="utf-8"))["casos"] if os.path.isfile(OUT) else {}
    nuevos = {}
    for c in casos:
        cid = c["id"]
        exp_base = EXP_BASE_POR_CASO.get(cid, EXP_BASE_DEFAULT)
        fixtures = []
        for a in c["archivos_sinteticos"]:
            fixtures.append({
                "fixture_banco": a["ruta"],
                "archivo_producto": f"fuentes_sinteticas/{os.path.basename(a['ruta'])}",
                "formato": a["formato"],
                "contenido_breve": a.get("contenido_breve", ""),
                "como_se_carga": "vía soportada del producto/arnés: materializar como fuente de prueba en fuentes_sinteticas/ con marcas [PDF PAGE n] (escribir_fuente) y referenciarla desde verificacion_entradas.json; NUNCA como registro oficial (PLAN §2)",
            })
        estado_inicial = {
            "expediente_base": exp_base,
            "comando": f"python3 -I scripts/preparar_caso_personaje.py {cid}   # copia \"$CANDIDATA_DIR/{exp_base}\" a \"$RUN_DIR/{cid}/Viscofan\", archiva heredados en _heredados/ y genera el registro plantilla",
            "ruta_trabajo": f"$RUN_DIR/{cid}/Viscofan",
            "fixtures": fixtures,
            "registro_inicial": f"python3 -I \"$CANDIDATA_DIR/munger_v2_r1/personaje_v2/scripts/verificacion_entradas.py\" plantilla \"$RUN_DIR/{cid}/Viscofan\"",
            "precondiciones": c["precondiciones"],
            "via_producto": ad[cid].get("adaptacion", ""),
        }
        if cid == "Q1-028":
            estado_inicial["aprobacion_de_partida"] = (
                "APROBACIÓN AUTÉNTICA DE PRUEBA creada antes por el producto (auditoría APROBADO del material "
                "inicial con agente auditor), NO el JSON del fixture: PLAN §2 — en pruebas de vigencia no se carga "
                "f5_028_aprobacion.json como si fuera una auditoría válida; el fixture solo se materializa como "
                "fuente de prueba en fuentes_sinteticas/")
        entrada = {
            "texto": c["entrada_usuario"],
            "fuente": "banco casos_aceptacion.jsonl campo entrada_usuario (texto íntegro, PLAN §2.2)",
            "a_quien_se_entrega": "al subagente del paso 5 (extraccion_v63) vía el prompt generado prompts_generados/05_*.md; el runtime pega entrada_usuario íntegro en la sesión del agente",
        }
        apc = [artefacto_criterio(c, i, crit, mapa.get(cid, {}).get(i, {"cobertura": "sin_asercion", "razon": "", "asercion_arnes": "", "evidencia": ""}))
               for i, crit in enumerate(c["criterios_observables"])]
        comando = (f"python3 -I scripts/preparar_caso_personaje.py {cid} && "
                   f"flock -x \"$RUN_DIR/{cid}.lock\" python3 -I \"$CANDIDATA_DIR/munger_v2_r1/personaje_v2/scripts/pipeline.py\" \"$RUN_DIR/{cid}/Viscofan\"")
        nuevos[cid] = {
            "estado_inicial": estado_inicial,
            "preparacion_comandos": f"python3 -I scripts/preparar_caso_personaje.py {cid}",
            "fases": [dict(f) for f in FASES],
            "entrada": entrada,
            "artefacto_por_criterio": apc,
            "comando_relevo": comando,
            "esperado_numerico": c.get("esperado_numerico"),
        }
    doc = {
        "nota": ("datos de los 36 relevos D4-R4, GENERADOS por scripts/actualizar_relevos.py desde el banco + "
                 "MAPA_CRITERIOS_BANCO.csv + adaptaciones.json: estado inicial (expediente base relativo a la "
                 "candidata, comando bajo RUN_DIR, fixture->archivo del producto, registro), fases del pipeline "
                 "con actor/modelo/esfuerzo/código esperado en la parada, entrada exacta, artefacto por criterio "
                 "(109) con condición de CUMPLE/FALLA o NO_OBSERVABLE/ADAPTACION_PENDIENTE/DECISION_PENDIENTE, "
                 "y comando_relevo ejecutable del personaje"),
        "recorrido_fuente": "coordinacion/cierre_v2/pruebas_candidata/957af65/MECANISMO_PERSONAJE.md §1-§4 (comprobado 2026-11-17)",
        "casos": nuevos,
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    sin = [cid for cid, c in nuevos.items() if not c["comando_relevo"] or not c["estado_inicial"] or not c["fases"] or len(c["artefacto_por_criterio"]) != len(next(x for x in casos if x["id"] == cid)["criterios_observables"])]
    n_crit = sum(len(c["artefacto_por_criterio"]) for c in nuevos.values())
    print(f"{OUT}: {len(nuevos)} casos · {n_crit} criterios con artefacto · incompletos: {sin}")


if __name__ == "__main__":
    main()
