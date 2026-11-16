#!/usr/bin/env python3
"""Genera relevo/PAQUETES_RELEVO.json: un paquete por cada uno de los 36 casos para el
runtime del coordinador (Claude), con comando exacto de re-ejecución, criterios ya
cubiertos por componente y lo que falta (agente/personaje, runtime, política).

Fuente única: banco @4745f38 + evidencias/*/resultado_ejecucion.json + MATRIZ_EJECUCION.csv.
Uso: python3 generar_relevo.py
"""
import csv
import glob
import json
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
AUX = os.path.dirname(AQUI)
EV = os.path.join(AUX, "evidencias")
BANCO = os.environ.get("BANCO_DIR", "/workspace/banco_q1_v2/resultados_qwen/q1_v2/banco_revisado")
OUT = os.path.join(AUX, "relevo", "PAQUETES_RELEVO.json")

FALTA_AGENTE = ("recorrido del personaje con agente real (entrada_usuario pegada, fases A/B/C, "
                "verificación, auditoría APROBADO con agente nuevo) — no simulable por el arnés")
FALTA_RUNTIME = "runtime con pdftotext + soffice (recalculo del libro) + agentes configurados"


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    casos = [json.loads(l) for l in open(os.path.join(BANCO, "casos_aceptacion.jsonl"), encoding="utf-8") if l.strip()]
    matriz = {r["id"]: r for r in csv.DictReader(open(os.path.join(AUX, "MATRIZ_EJECUCION.csv"), encoding="utf-8"))}
    paquetes = []
    for c in casos:
        cid = c["id"]
        m = matriz[cid]
        res_p = os.path.join(EV, cid, "resultado_ejecucion.json")
        res = json.load(open(res_p, encoding="utf-8")) if os.path.isfile(res_p) else None
        spec = m["comandos_reproducibles"]
        falta = []
        if m["estado_ejecucion"] == "PARCIAL_COMPONENTE":
            falta.append(FALTA_AGENTE)
        if cid == "Q1-026":
            falta.append(FALTA_RUNTIME + " (bloqueo documentado en evidencias/Q1-026/)")
        if cid in ("Q1-030", "Q1-035"):
            falta.append("decisión de política del responsable (usuario), no del banco ni del arnés")
        if cid in ("Q1-031", "Q1-033"):
            falta.append("fase A/objetivo con agente real sobre fase1_v63.json (precio actual)")
        paquetes.append({
            "caso": cid, "familia": c["familia"], "control_banco": c["control"], "naturaleza": c["naturaleza"],
            "estado_ejecucion": m["estado_ejecucion"],
            "veredicto_componente": m["veredicto_componente"], "veredicto_caso": m["veredicto_caso"],
            "criterios_evaluados": m["criterios_evaluados"],
            "entrada_usuario": c["entrada_usuario"],
            "archivos_sinteticos": [a["ruta"] for a in c["archivos_sinteticos"]],
            "comando_relevo": ("python3 scripts/ejecutar_caso.py scripts/" + spec.split("scripts/")[-1]) if "especificaciones" in spec else None,
            "evidencia_componente": f"evidencias/{cid}/" if res else None,
            "precondiciones_simuladas": bool(res and res.get("precondiciones_simuladas")),
            "falta_para_caso_completo": falta or ["nada pendiente declarado"],
        })
    q26 = next(p for p in paquetes if p["caso"] == "Q1-026")
    q26["paquete_runtime"] = {
        "cambio": "evidencias/Q1-026/CAMBIO_Q1-026.json",
        "pasos": ["con pdftotext: extraer textos AR_2021..AR_2024 a texto/",
                  "python3 -I personaje_v2/scripts/cambiar_base.py preparar pruebas_d/CAMBIO_Q1-026.json (en copia aislada de la candidata)",
                  "actualizar verificacion_entradas.json de la copia nueva (caja 45.000, deuda 82.019 de la nota v2)",
                  "recalcular con soffice (secuencia, un solo proceso) y recalcular dependientes (deuda neta 37.019)",
                  "auditoría nueva del material final con agente auditor distinto"],
        "artefactos_esperados": ["expediente copia nuevo (origen intacto verificado: evidencias/Q1-026/origen_estado.txt)",
                                 "verificacion_entradas.json de la copia con la corrección sellada",
                                 "auditoria.md APROBADO del material nuevo (solo vía agente)"],
        "bloqueo_actual": "sin pdftotext los textos AR_2021..AR_2024 no existen en texto/ (error exacto en evidencias/Q1-026/cambiar_base_preparar.txt, exit 1)",
    }
    doc = {
        "programa": "coordinacion/cierre_v2 @ ec707a5 (PROMPT_MISTRAL_D) bloque 2",
        "proposito": "paquetes caso por caso para el runtime del coordinador (Claude): qué ya está ejecutado por componente con aserciones y qué falta de agente/runtime/política",
        "regla": "una respuesta del arnés no es ejecución del producto; los agentes del personaje los ejecuta el runtime del coordinador con evidencia y versión",
        "recuentos": json.load(open(os.path.join(EV, "recuentos.json"), encoding="utf-8")),
        "paquetes": paquetes,
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print(f"{OUT}: {len(paquetes)} paquetes")


if __name__ == "__main__":
    main()
