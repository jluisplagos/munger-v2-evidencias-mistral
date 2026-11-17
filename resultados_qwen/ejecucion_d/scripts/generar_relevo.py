#!/usr/bin/env python3
"""Genera relevo/PAQUETES_RELEVO.json v5: un paquete COMPLETO y GENERADO por cada uno de
los 36 casos del banco (D4-R4, prioridad máxima del encargo D4).

Cada paquete lleva, según MECANISMO_PERSONAJE.md §4 y PLAN_DE_EJECUCION §2/§4:
- estado_inicial: expediente base (ruta relativa a la candidata), comando que lo deja
  bajo RUN_DIR, qué fixture del banco se carga en qué archivo del producto, registro
  inicial y precondiciones (Q1-028: aprobación de partida AUTÉNTICA de prueba, no el
  JSON del fixture);
- preparacion_comandos: comandos ejecutables en orden;
- fases: pasos del pipeline en orden con actor, modelo, esfuerzo, qué agente es nuevo y
  cuál continúa, código esperado en cada parada y artefacto de salida;
- entrada: texto exacto (entrada_usuario del banco) y a quién se entrega;
- artefacto_por_criterio: para cada uno de los 109 criterios del banco, archivo relativo
  al expediente, campo/sección, condición de CUMPLE y de FALLA, o NO_OBSERVABLE /
  ADAPTACION_PENDIENTE / DECISION_PENDIENTE con motivo;
- comando_relevo: el del personaje, ejecutable (preparar_caso_personaje.py + pipeline.py
  con flock); ninguno de los 36 queda en null.

Fuentes: banco + evidencias + MATRIZ + MAPA + relevos_casos.json (generado por
actualizar_relevos.py). Uso: python3 generar_relevo.py
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

EV = os.path.join(AUX, "evidencias")
BANCO = L.BANCO
OUT = os.path.join(AUX, "relevo", "PAQUETES_RELEVO.json")

RECORRIDO_PERSONAJE = {
    "fuente": "coordinacion/cierre_v2/pruebas_candidata/957af65/MECANISMO_PERSONAJE.md (comprobado 2026-11-17)",
    "mecanismo": "pipeline.py deja los pasos de agente (5, 6, 8, 10 en dos turnos, 13) con código 10 + ESPERANDO.md + prompts_generados/; la sesión orquesta un subagente por relevo según config_v2.json -> modelos; no hace falta API ni credencial",
    "modelos_config_v2": {"extraccion_v63": "sonnet/medio", "fase_a": "opus/alto", "fase_b": "opus/alto",
                          "fase_c": "opus/alto, 2 turnos con el MISMO agente", "verificacion": "opus/medio, agente NUEVO",
                          "auditoria": "auditor NUEVO"},
    "reglas": ["solo la salida del agente; sin internet ni memoria; sin pipeline/LibreOffice/Excel en los relevos de agente",
               "no simular respuestas de agente; --agentes-simulados solo vale para pruebas técnicas",
               "nunca copiar salidas entre expedientes reales; LibreOffice en secuencia con flock y perfil aislado"],
    "limite_conocido": "los expedientes de empresas_v2/ no conservan pdf/ ni texto/; la plantilla de la base materializada (ensayo 4.13/4.14 de Vidrala) sí conserva texto/",
}

VIAS_SIN_ARTEFACTO = ("NO_OBSERVABLE", "ADAPTACION_PENDIENTE", "DECISION_PENDIENTE")


def validar_paquetes(doc, casos_banco):
    """D4-R4: validación estricta de los paquetes. Devuelve lista de incumplimientos."""
    mal = []
    paquetes = doc.get("paquetes", [])
    if len(paquetes) != 36:
        mal.append(f"número de paquetes {len(paquetes)} != 36")
    por_id = {c["id"]: c for c in casos_banco}
    for p in paquetes:
        cid = p["caso"]
        caso = por_id.get(cid)
        ei = p.get("estado_inicial") or {}
        if not ei.get("expediente_base") or os.path.isabs(ei["expediente_base"]) or ei["expediente_base"].startswith("$"):
            mal.append(f"{cid}: estado_inicial.expediente_base no es ruta relativa a la candidata")
        if not ei.get("comando"):
            mal.append(f"{cid}: estado_inicial sin comando")
        if not ei.get("fixtures"):
            mal.append(f"{cid}: estado_inicial sin fixtures")
        else:
            for fx in ei["fixtures"]:
                if not fx.get("fixture_banco") or not fx.get("archivo_producto"):
                    mal.append(f"{cid}: fixture sin archivo del producto")
        if cid == "Q1-028" and "AUT" not in (ei.get("aprobacion_de_partida") or "").upper():
            mal.append("Q1-028: falta la aprobación de partida AUTÉNTICA de prueba (PLAN §2)")
        if not p.get("preparacion_comandos"):
            mal.append(f"{cid}: sin preparacion_comandos")
        fases = p.get("fases") or []
        if not fases:
            mal.append(f"{cid}: sin fases")
        for f in fases:
            for clave in ("paso", "fase", "agente", "modelo", "esfuerzo", "codigo_esperado", "salida"):
                if f.get(clave) in (None, "", []):
                    mal.append(f"{cid}: fase {f.get('orden')} sin {clave}")
            if isinstance(f.get("paso"), int) and f["paso"] in (5, 6, 8, 10, 13) and f.get("codigo_esperado") != [10]:
                mal.append(f"{cid}: paso de agente {f['paso']} debe parar con código 10")
        ent = p.get("entrada") or {}
        if ent.get("texto") != (caso or {}).get("entrada_usuario"):
            mal.append(f"{cid}: entrada.texto no es la entrada_usuario exacta del banco")
        if not ent.get("a_quien_se_entrega"):
            mal.append(f"{cid}: entrada sin destinatario")
        apc = p.get("artefacto_por_criterio") or []
        if caso and len(apc) != len(caso["criterios_observables"]):
            mal.append(f"{cid}: artefacto_por_criterio tiene {len(apc)} != {len(caso['criterios_observables'])} criterios del banco")
        for a in apc:
            if a.get("via") in VIAS_SIN_ARTEFACTO:
                if not a.get("motivo"):
                    mal.append(f"{cid}#{a.get('indice')}: {a.get('via')} sin motivo")
            else:
                for clave in ("artefacto", "campo", "condicion_cumple", "condicion_falla"):
                    if not a.get(clave):
                        mal.append(f"{cid}#{a.get('indice')}: falta {clave}")
                if a.get("artefacto") and os.path.isabs(a["artefacto"]):
                    mal.append(f"{cid}#{a.get('indice')}: artefacto con ruta absoluta")
        cmd = p.get("comando_relevo")
        if not cmd or "pipeline.py" not in cmd or cid not in cmd:
            mal.append(f"{cid}: comando_relevo no ejecutable del personaje (null o sin pipeline.py/caso)")
    return mal


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    casos = [json.loads(l) for l in open(os.path.join(BANCO, "casos_aceptacion.jsonl"), encoding="utf-8") if l.strip()]
    matriz = {r["id"]: r for r in csv.DictReader(open(os.path.join(AUX, "MATRIZ_EJECUCION.csv"), encoding="utf-8"))}
    mapa = {}
    with open(os.path.join(AUX, "MAPA_CRITERIOS_BANCO.csv"), encoding="utf-8") as f:
        for row in csv.DictReader(f):
            mapa.setdefault(row["caso"], []).append(row)
    relc = json.load(open(os.path.join(AQUI, "especificaciones", "relevos_casos.json"), encoding="utf-8"))["casos"]
    paquetes = []
    for c in casos:
        cid = c["id"]
        m = matriz[cid]
        rc = relc[cid]
        res_p = os.path.join(EV, cid, "resultado_ejecucion.json")
        res = json.load(open(res_p, encoding="utf-8")) if os.path.isfile(res_p) else None
        falta = []
        if m["estado_ejecucion"] in ("PARCIAL_COMPONENTE", "BLOQUEO_ENTORNO", "SOLO_OBSERVACIONES") or m["estado_ejecucion"].startswith("ERROR"):
            falta.append({"qué": "recorrido del personaje con agentes reales sobre el estado inicial preparado (entrada_usuario pegada; pasos 5/6/8/10/13 con los modelos de config_v2.json; fase C en dos turnos con el mismo agente; verificación con agente nuevo; auditoría APROBADO con auditor nuevo)",
                          "quién": "runtime del coordinador (Claude) con agentes configurados",
                          "necesita": "estado inicial preparado (preparar_caso_personaje.py) + CANDIDATA_DIR materializada; sin API"})
        if cid == "Q1-026":
            falta.append({"qué": "tras preparar el CAMBIO validado contra el banco (caja 95->90, deuda 300, deuda neta 210) sobre la base 4.14: recalcular el libro con soffice en secuencia (flock -x, perfil aislado) y auditoría nueva del material final",
                          "quién": "runtime del coordinador con soffice (flock, un solo proceso) + agente auditor nuevo",
                          "necesita": "base 4.14 (fase1_historia.py construir da 0 en la candidata); pdftotext solo si faltan textos"})
        if cid == "Q1-028":
            falta.append({"qué": "reaprobación NUEVA con auditor real tras el cambio de material (la aprobación de partida es una aprobación auténtica de prueba creada antes, no el fixture); deuda neta vigente 300+40-95=245 documentada como transformación pendiente de verificar",
                          "quién": "agente auditor nuevo (runtime del coordinador)",
                          "necesita": "expediente preparado con f5_028_aprobacion.json materializado como fuente de prueba"})
        if cid == "Q1-032":
            falta.append({"qué": "recuento 4 verificadas / 1 pendiente / 5 total del fixture f6_032_matriz.json sin doble conteo, y distinción estado de entradas vs estado de la conclusión",
                          "quién": "runtime del coordinador", "necesita": "expediente preparado con el universo de 5 materializado"})
        if cid in ("Q1-030", "Q1-035"):
            falta.append({"qué": "decisión de política del responsable (Q1-030 caducidad temporal; Q1-035 validación de motores)",
                          "quién": "usuario", "necesita": "decisión explícita; el banco no la fija ni el arnés la elige (PLAN §3)"})
        if not falta:
            falta.append({"qué": "revisión externa por otro contexto", "quién": "coordinador (Claude)", "necesita": "diff + reproducción de lo afectado"})
        criterios_banco = []
        for r in mapa.get(cid, []):
            arte = next((a for a in rc["artefacto_por_criterio"] if a["indice"] == int(r["criterio_indice"])), None)
            criterios_banco.append({"indice": int(r["criterio_indice"]), "criterio": r["criterio_banco"],
                                    "cobertura": r["cobertura"], "razon": r["razon"],
                                    "artefacto": (arte or {}).get("artefacto", r.get("artefacto", "")),
                                    "via": (arte or {}).get("via", "")})
        paquetes.append({
            "caso": cid, "familia": c["familia"], "control_banco": c["control"], "naturaleza": c["naturaleza"],
            "estado_ejecucion": m["estado_ejecucion"],
            "veredicto_componente": m["veredicto_componente"], "veredicto_caso": m["veredicto_caso"],
            "criterios_evaluados": m["criterios_evaluados"],
            "estado_inicial": rc["estado_inicial"],
            "preparacion_comandos": rc["preparacion_comandos"],
            "fases": rc["fases"],
            "entrada": rc["entrada"],
            "artefacto_por_criterio": rc["artefacto_por_criterio"],
            "criterios_banco": criterios_banco,
            "entrada_usuario": c["entrada_usuario"],
            "archivos_sinteticos": [a["ruta"] for a in c["archivos_sinteticos"]],
            "esperado_numerico": c.get("esperado_numerico"),
            "comando_relevo": rc["comando_relevo"],
            "motivo_sin_comando": None,
            "evidencia_componente": f"evidencias/{cid}/" if res else None,
            "precondiciones_simuladas": bool(res and res.get("precondiciones_simuladas")),
            "falta_para_caso_completo": falta,
        })
    doc = {
        "programa": "respuesta D4-R4 sobre c734ca1 (CORRECCION_D4)",
        "proposito": "paquetes COMPLETOS por caso para el runtime del coordinador: el coordinador ejecuta los 36 casos del personaje con subagentes sin interpretar nada",
        "regla": "una respuesta del arnés no es ejecución del producto; los agentes del personaje los ejecuta el runtime del coordinador con evidencia y versión (0/36 casos del personaje ejecutados por Mistral D)",
        "recorrido_personaje": RECORRIDO_PERSONAJE,
        "generado_por": "scripts/actualizar_relevos.py (datos) + scripts/generar_relevo.py (paquetes), desde banco @4745f38 + MAPA + MATRIZ + adaptaciones.json",
        "recuentos": json.load(open(os.path.join(EV, "recuentos.json"), encoding="utf-8")) if os.path.isfile(os.path.join(EV, "recuentos.json")) else {},
        "paquetes": paquetes,
    }
    mal = validar_paquetes(doc, casos)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    sin_comando = [p["caso"] for p in paquetes if not p["comando_relevo"]]
    n_crit = sum(len(p["artefacto_por_criterio"]) for p in paquetes)
    print(f"{OUT}: {len(paquetes)} paquetes · {n_crit} criterios con artefacto · sin comando: {sin_comando}")
    print(f"validación D4-R4: {len(mal)} incumplimientos" + (f" · {mal[:5]}" if mal else ""))
    return 1 if mal else 0


if __name__ == "__main__":
    sys.exit(main())
