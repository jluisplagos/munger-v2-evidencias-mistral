#!/usr/bin/env python3
"""Genera MATRIZ_EJECUCION.csv v2: una fila por cada uno de los 36 casos del banco.

v2 (CORRECCION_D D-R1/D-R3): el estado y los veredictos se derivan SOLO de la
evidencia validada (evidencias/<id>/resultado_ejecucion.json con harness_version 2.0
y estado COMPONENTE_OK); sin evidencia no hay veredicto positivo. Se distingue
veredicto de componente (lo ejecutado por el arnés) de veredicto de caso (el caso
completo sigue pendiente si falta algún criterio, p. ej. la capa de agente).
Las observaciones compartidas se declaran y no se cuentan como ejecución propia.

Uso: python3 generar_matriz.py   (escribe ../MATRIZ_EJECUCION.csv y ../evidencias/recuentos.json)
"""
import csv
import glob
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
AUX = os.path.dirname(AQUI)
EV = os.path.join(AUX, "evidencias")
BANCO = os.environ.get("BANCO_DIR", "/workspace/banco_q1_v2/resultados_qwen/q1_v2/banco_revisado")

CAMPOS = ["id", "familia", "control_banco", "naturaleza", "precondiciones",
          "componente", "interfaz_real", "parte_automatizable", "parte_relevo_supervisado",
          "observables", "artefacto_estado", "adaptacion", "preserva_sentido",
          "estado_ejecucion", "veredicto_componente", "veredicto_caso", "criterios_evaluados",
          "observacion_compartida", "evidencia", "comandos_reproducibles", "sin_comprobar"]

# Casos con veredicto de caso fijo (política pendiente del responsable) o bloqueo de entorno.
VEREDICTO_CASO_FIJO = {
    "Q1-030": ("DECISION_PENDIENTE", "caducidad temporal por antigüedad: política no fijada (responsable)"),
    "Q1-035": ("DECISION_PENDIENTE", "validación de motores: política no fijada (responsable); estado coherente matriz/resumen desde esta fuente única"),
    "Q1-026": ("NO_OBSERVABLE", "cambiar_base preparar bloqueado por entorno: falta pdftotext (textos AR_2021..AR_2024 son PDF); error exacto en evidencias/Q1-026/cambiar_base_preparar.txt"),
}
# Observaciones compartidas: reutilizan la ejecución de otro caso (no acreditan criterios propios).
OBS_COMPARTIDA = {
    "Q1-028": "observación compartida con Q1-036 (retirada de aprobación al cambiar material auditado); no acredita reaprobación nueva ni el derivado 245",
    "Q1-032": "observación compartida con Q1-036 (ficha provisional: apta por entradas no); 1/321 NO prueba 4/1/5 del fixture -> recuento propio no observable aquí",
    "Q1-036": "",
}

ADAPTACIONES = os.path.join(AQUI, "especificaciones", "adaptaciones.json")


def main():
    casos = [json.loads(l) for l in open(os.path.join(BANCO, "casos_aceptacion.jsonl"), encoding="utf-8") if l.strip()]
    ad = json.load(open(ADAPTACIONES, encoding="utf-8"))["casos"]
    out = os.path.join(AUX, "MATRIZ_EJECUCION.csv")
    recuentos = {"casos": len(casos), "estado_ejecucion": {}, "veredicto_componente": {}, "veredicto_caso": {},
                 "naturaleza": {}, "con_ejecucion_propia": 0, "con_observacion_compartida": 0, "sin_ejecutar": 0}
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        for c in casos:
            cid = c["id"]
            a = ad[cid]
            res_p = os.path.join(EV, cid, "resultado_ejecucion.json")
            spec = next((f"especificaciones/{d}/{cid}.json" for d in ("piloto", "bloque2")
                         if os.path.isfile(os.path.join(AQUI, "especificaciones", d, cid + ".json"))), None)
            res = None
            if os.path.isfile(res_p):
                try:
                    res = json.load(open(res_p, encoding="utf-8"))
                except Exception:
                    res = None
            if res and res.get("harness_version") == "2.0" and res.get("estado_caso") == "COMPONENTE_OK":
                estado = "PARCIAL_COMPONENTE"
                vcomp = "CUMPLE"
                criterios = "; ".join(f"{x['id']}={x['estado']}" for x in res.get("criterios", []))
                evidencia = f"evidencias/{cid}/resultado_ejecucion.json (harness 2.0, aserciones OK)"
                recuentos["con_ejecucion_propia"] += 1
            elif cid in VEREDICTO_CASO_FIJO and not res:
                estado = "NO_EJECUTADO"
                vcomp = ""
                criterios = ""
                evidencia = "sin evidencia de ejecución (bloqueo de entorno documentado)" if cid == "Q1-026" else "sin evidencia"
            else:
                estado = "NO_EJECUTADO" if not res else f"ERROR ({res.get('estado_caso')})"
                vcomp = ""
                criterios = "; ".join(f"{x['id']}={x['estado']}" for x in (res or {}).get("criterios", []))
                evidencia = f"evidencias/{cid}/resultado_ejecucion.json (estado {res.get('estado_caso')})" if res else "sin evidencia"
                if cid == "Q1-026":
                    estado = "NO_EJECUTADO (bloqueo de entorno)"
            if cid in VEREDICTO_CASO_FIJO:
                vcaso, nota_caso = VEREDICTO_CASO_FIJO[cid]
            elif estado == "PARCIAL_COMPONENTE":
                vcaso = ""  # sin veredicto de caso: falta la capa de agente (y a veces política)
                nota_caso = "caso completo pendiente de criterios de agente/relevo"
            else:
                vcaso = ""
                nota_caso = ""
            obs = OBS_COMPARTIDA.get(cid, "")
            if obs:
                recuentos["con_observacion_compartida"] += 1
            if estado.startswith("NO_EJECUTADO") and not obs:
                recuentos["sin_ejecutar"] += 1
            w.writerow({
                "id": cid, "familia": c["familia"], "control_banco": c["control"], "naturaleza": c["naturaleza"],
                "precondiciones": c["precondiciones"],
                "componente": a["componente"], "interfaz_real": a["interfaz_real"],
                "parte_automatizable": a["automatizable"], "parte_relevo_supervisado": a["relevo"],
                "observables": " | ".join(a["observables"]), "artefacto_estado": a["artefacto"],
                "adaptacion": a["adaptacion"], "preserva_sentido": "sí",
                "estado_ejecucion": estado,
                "veredicto_componente": vcomp,
                "veredicto_caso": (vcaso + (f" ({nota_caso})" if nota_caso else "")) if vcaso else ("sin veredicto de caso (pendiente de agente)" if estado == "PARCIAL_COMPONENTE" else "sin veredicto (no ejecutado)"),
                "criterios_evaluados": criterios,
                "observacion_compartida": obs or "-",
                "evidencia": evidencia,
                "comandos_reproducibles": (f"python3 scripts/ejecutar_caso.py scripts/{spec}" if spec else "pendiente de especificación ejecutable"),
                "sin_comprobar": a["sin_comprobar"] + ((" · " + nota_caso) if nota_caso else ""),
            })
            recuentos["estado_ejecucion"][estado] = recuentos["estado_ejecucion"].get(estado, 0) + 1
            key_vc = vcomp or "sin veredicto de componente"
            recuentos["veredicto_componente"][key_vc] = recuentos["veredicto_componente"].get(key_vc, 0) + 1
            vc = w.writerow  # noqa: F841
    # veredicto_caso desde el CSV recién escrito (fuente única)
    import collections
    vc = collections.Counter()
    nat = collections.Counter()
    with open(out, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            v = row["veredicto_caso"]
            clave = v.split(" (")[0]
            vc[clave] += 1
            nat[row["naturaleza"]] += 1
    recuentos["veredicto_caso"] = dict(vc)
    recuentos["naturaleza"] = dict(nat)
    with open(os.path.join(EV, "recuentos.json"), "w", encoding="utf-8") as f:
        json.dump(recuentos, f, ensure_ascii=False, indent=1)
    print(f"{out}: {len(casos)} filas · recuentos en evidencias/recuentos.json")
    print("  estados:", recuentos["estado_ejecucion"])
    print("  veredicto_componente:", recuentos["veredicto_componente"])
    print("  veredicto_caso:", recuentos["veredicto_caso"])
    print("  naturaleza:", recuentos["naturaleza"])


if __name__ == "__main__":
    main()
