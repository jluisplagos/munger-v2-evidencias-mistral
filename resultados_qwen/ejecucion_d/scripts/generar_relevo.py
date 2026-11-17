#!/usr/bin/env python3
"""Genera relevo/PAQUETES_RELEVO.json v3: un paquete por cada uno de los 36 casos para
el runtime del coordinador (Claude), con comando exacto de re-ejecución, criterios ya
cubiertos por componente y LO QUE FALTA con responsable y necesidad (D2-R4: nunca
«nada pendiente declarado» salvo decisión del usuario, que también se nombra).

Incluye el recorrido del personaje comprobado en 957af65 (MECANISMO_PERSONAJE.md):
fases/orden/modelos y qué se observa en cada criterio del banco (mapa_banco).

Fuente única: banco @SHA + evidencias/*/resultado_ejecucion.json + MATRIZ_EJECUCION.csv
+ MAPA_CRITERIOS_BANCO.csv.
Uso: python3 generar_relevo.py
"""
import csv
import json
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
AUX = os.path.dirname(AQUI)
EV = os.path.join(AUX, "evidencias")
BANCO = os.environ.get("BANCO_DIR", "/workspace/banco_q1_v2/resultados_qwen/q1_v2/banco_revisado")
OUT = os.path.join(AUX, "relevo", "PAQUETES_RELEVO.json")

RECORRIDO_PERSONAJE = {
    "fuente": "coordinacion/cierre_v2/pruebas_candidata/957af65/MECANISMO_PERSONAJE.md (comprobado 2026-11-17)",
    "mecanismo": "pipeline.py deja los pasos de agente con codigo 10 + ESPERANDO.md + prompts_generados/; la sesion orquesta un subagente por relevo segun config_v2.json -> modelos; no hace falta API ni credencial",
    "fases_en_orden": [
        {"paso": 5, "fase": "extraccion (extraccion_v63)", "modelo": "sonnet", "esfuerzo": "medio"},
        {"paso": 6, "fase": "fase A", "modelo": "opus", "esfuerzo": "alto"},
        {"paso": 8, "fase": "fase B", "modelo": "opus", "esfuerzo": "alto"},
        {"paso": 10, "fase": "fase C, turno 1 y turno 2 con el MISMO agente", "modelo": "opus", "esfuerzo": "alto"},
        {"paso": 13, "fase": "verificacion con agente NUEVO", "modelo": "opus", "esfuerzo": "medio"},
        {"fase": "auditoria APROBADO", "agente": "auditor nuevo, distinto del productor", "nota": "cierre_v2 retira aprobaciones al cambiar el material auditado"},
    ],
    "reglas": ["solo la salida del agente; sin internet ni memoria; sin pipeline/LibreOffice/Excel en los relevos de agente",
               "no simular respuestas de agente; --agentes-simulados solo vale para pruebas tecnicas",
               "nunca copiar salidas entre expedientes reales"],
    "limite_conocido": "los expedientes de empresas_v2/ no conservan pdf/ ni texto/; los de la base 4.14 (Vidrala, Viscofan, Elis) si conservan texto/",
}

FALTA_AGENTE = ("recorrido del personaje con agente real (entrada_usuario pegada, pasos 5/6/8/10/13 con los modelos "
                "de config_v2.json, fase C en dos turnos con el mismo agente, verificacion con agente nuevo, "
                "auditoria APROBADO con auditor nuevo) — no simulable por el arnés")


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    casos = [json.loads(l) for l in open(os.path.join(BANCO, "casos_aceptacion.jsonl"), encoding="utf-8") if l.strip()]
    matriz = {r["id"]: r for r in csv.DictReader(open(os.path.join(AUX, "MATRIZ_EJECUCION.csv"), encoding="utf-8"))}
    mapa = {}
    with open(os.path.join(AUX, "MAPA_CRITERIOS_BANCO.csv"), encoding="utf-8") as f:
        for row in csv.DictReader(f):
            mapa.setdefault(row["caso"], []).append(row)
    ad = json.load(open(os.path.join(AQUI, "especificaciones", "adaptaciones.json"), encoding="utf-8"))["casos"]
    paquetes = []
    for c in casos:
        cid = c["id"]
        m = matriz[cid]
        res_p = os.path.join(EV, cid, "resultado_ejecucion.json")
        res = json.load(open(res_p, encoding="utf-8")) if os.path.isfile(res_p) else None
        spec = m["comandos_reproducibles"]
        comando = ("python3 scripts/ejecutar_caso.py scripts/" + spec.split("scripts/")[-1]) if "especificaciones" in spec else None
        falta = []
        if m["estado_ejecucion"] == "PARCIAL_COMPONENTE":
            falta.append({"qué": FALTA_AGENTE, "quién": "runtime del coordinador (Claude) con agentes configurados", "necesita": "candidata 957af65 materializada + config_v2.json; sin API"})
        if m["estado_ejecucion"] == "BLOQUEO_ENTORNO":
            falta.append({"qué": "cambiar_base completo + recálculo del libro (deuda neta 300-90=210) + auditoría nueva del material final",
                          "quién": "runtime del coordinador con pdftotext + soffice (secuencia, flock) + agente auditor nuevo",
                          "necesita": "pdftotext (AR_2021..AR_2024 son PDF) y LibreOffice; OJO: el stderr también muestra errores de ipal/AR_2019/AR_2020 que pdftotext solo no resuelve (evidencias/Q1-026/errores_bloqueo.json)"})
        if cid == "Q1-028":
            falta.append({"qué": "reaprobación NUEVA con auditor real (la observación compartida con Q1-036 solo muestra la retirada) y deuda neta vigente 300+40-95=245 documentada como transformación pendiente de verificar",
                          "quién": "agente auditor nuevo (runtime del coordinador)", "necesita": "expediente con la transformación vigente (arrendamientos 40, deuda 300, caja 95 del fixture f5_028_aprobacion.json)"})
        if cid == "Q1-032":
            falta.append({"qué": "recuento 4 verificadas / 1 pendiente / 5 total del fixture f6_032_matriz.json sin doble conteo (el universo real es 321: 1/321 no lo prueba)",
                          "quién": "runtime del coordinador", "necesita": "expediente de prueba con universo de 5 soportado o registrar NO_OBSERVABLE; ficha provisional que distinga estado de entradas vs estado de la conclusión"})
        if cid in ("Q1-030", "Q1-035"):
            falta.append({"qué": "decisión de política del responsable (Q1-030 caducidad temporal; Q1-035 validación de motores)",
                          "quién": "usuario", "necesita": "decisión explícita; el banco no la fija ni el arnés la elige"})
        if cid in ("Q1-031", "Q1-033"):
            falta.append({"qué": "fase A/objetivo con agente real sobre fase1_v63.json (precio histórico 14,20 EUR etiquetado vs actual ausente)",
                          "quién": "agente real (runtime del coordinador)", "necesita": "fase1_v63.json del expediente de prueba; sin simular respuesta"})
        if not falta:
            falta.append({"qué": "revisión externa por otro contexto", "quién": "coordinador (Claude)", "necesita": "diff + reproducción de lo afectado"})
        paquetes.append({
            "caso": cid, "familia": c["familia"], "control_banco": c["control"], "naturaleza": c["naturaleza"],
            "estado_ejecucion": m["estado_ejecucion"],
            "veredicto_componente": m["veredicto_componente"], "veredicto_caso": m["veredicto_caso"],
            "criterios_evaluados": m["criterios_evaluados"],
            "entrada_usuario": c["entrada_usuario"],
            "archivos_sinteticos": [a["ruta"] for a in c["archivos_sinteticos"]],
            "esperado_numerico": c.get("esperado_numerico"),
            "comando_relevo": comando,
            "motivo_sin_comando": None if comando else "sin especificación ejecutable del arnés: el caso requiere agente/política, no un comando de componente",
            "evidencia_componente": f"evidencias/{cid}/" if res else None,
            "precondiciones_simuladas": bool(res and res.get("precondiciones_simuladas")),
            "falta_para_caso_completo": falta,
            "criterios_banco": [{"indice": r["criterio_indice"], "criterio": r["criterio_banco"],
                                 "asercion": r["asercion_arnes"], "cobertura": r["cobertura"], "razon": r["razon"]}
                                for r in mapa.get(cid, [])],
        })
    q26 = next(p for p in paquetes if p["caso"] == "Q1-026")
    q26["paquete_runtime"] = {
        "cambio": "evidencias/Q1-026/CAMBIO_Q1-026.json (coherente con el banco f5_026: caja 95->90, deuda 300, evidencia restaurada)",
        "pasos": ["con pdftotext: extraer textos AR_2021..AR_2024 a texto/ (OJO: también hay errores de ipal/AR_2019/AR_2020 en errores_bloqueo.json que pdftotext solo no resuelve)",
                  "preparar el CAMBIO en una copia aislada bajo RUN_DIR (nunca dentro de la candidata): python3 -I personaje_v2/scripts/cambiar_base.py preparar <CAMBIO_abs>",
                  "actualizar verificacion_entradas.json de la copia nueva con la corrección sellada (caja 90, deuda 300 de f5_026_nota.txt)",
                  "recalcular con soffice en secuencia (flock -x, un solo proceso, perfil aislado) y recalcular los dependientes: deuda neta 300-90=210",
                  "auditoría nueva del material final con agente auditor distinto"],
        "artefactos_esperados": ["expediente copia nuevo (origen intacto verificado: evidencias/Q1-026/origen_estado.txt)",
                                 "verificacion_entradas.json de la copia con la corrección sellada",
                                 "resultado del recálculo con deuda neta 210",
                                 "auditoria.md APROBADO del material nuevo (solo vía agente)"],
        "bloqueo_actual": "sin pdftotext/soffice en este entorno: cambiar_base preparar exit 1 (error exacto en evidencias/Q1-026/cambiar_base_preparar.txt y errores_bloqueo.json)",
    }
    doc = {
        "programa": "coordinacion/cierre-v2 (PROMPT_MISTRAL_D) respuesta D2-R4 sobre 1ac661b",
        "proposito": "paquetes caso por caso para el runtime del coordinador (Claude): qué ya está ejecutado por componente con aserciones y qué falta de agente/runtime/política, con responsable y necesidad",
        "regla": "una respuesta del arnés no es ejecución del producto; los agentes del personaje los ejecuta el runtime del coordinador con evidencia y versión",
        "recorrido_personaje": RECORRIDO_PERSONAJE,
        "recuentos": json.load(open(os.path.join(EV, "recuentos.json"), encoding="utf-8")),
        "paquetes": paquetes,
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print(f"{OUT}: {len(paquetes)} paquetes")


if __name__ == "__main__":
    main()
