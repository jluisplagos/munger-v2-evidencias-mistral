#!/usr/bin/env python3
"""Genera MATRIZ_EJECUCION.csv: exactamente una fila por cada uno de los 36 casos del banco.

Fuentes: banco_revisado/casos_aceptacion.jsonl (normativo) + especificaciones/adaptaciones.json.
Uso: python3 generar_matriz.py  (escribe ../MATRIZ_EJECUCION.csv)
"""
import csv
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
AUX = os.path.dirname(AQUI)
BANCO = os.environ.get("BANCO_DIR", "/workspace/banco_q1_v2/resultados_qwen/q1_v2/banco_revisado")

CAMPOS = ["id", "familia", "control_banco", "naturaleza", "precondiciones",
          "componente", "interfaz_real", "parte_automatizable", "parte_relevo_supervisado",
          "observables", "artefacto_estado", "adaptacion", "preserva_sentido",
          "estado_ejecucion", "veredicto", "evidencia", "comandos_reproducibles", "sin_comprobar"]


def main():
    casos = [json.loads(l) for l in open(os.path.join(BANCO, "casos_aceptacion.jsonl"), encoding="utf-8") if l.strip()]
    ad = json.load(open(os.path.join(AQUI, "especificaciones", "adaptaciones.json"), encoding="utf-8"))["casos"]
    out = os.path.join(AUX, "MATRIZ_EJECUCION.csv")
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        for c in casos:
            a = ad[c["id"]]
            w.writerow({
                "id": c["id"],
                "familia": c["familia"],
                "control_banco": c["control"],
                "naturaleza": c["naturaleza"],
                "precondiciones": c["precondiciones"],
                "componente": a["componente"],
                "interfaz_real": a["interfaz_real"],
                "parte_automatizable": a["automatizable"],
                "parte_relevo_supervisado": a["relevo"],
                "observables": " | ".join(a["observables"]),
                "artefacto_estado": a["artefacto"],
                "adaptacion": a["adaptacion"],
                "preserva_sentido": "sí",
                "estado_ejecucion": a["estado"],
                "veredicto": a["veredicto"] or "sin veredicto (no ejecutado)",
                "evidencia": a["evidencia"] or "-",
                "comandos_reproducibles": next(
                    (f"python3 scripts/ejecutar_caso.py scripts/especificaciones/{d}/{c['id']}.json"
                     for d in ("piloto", "bloque2")
                     if os.path.isfile(os.path.join(AQUI, "especificaciones", d, c["id"] + ".json"))),
                    "pendiente de especificación ejecutable"),
                "sin_comprobar": a["sin_comprobar"],
            })
    print(f"{out}: {len(casos)} filas")


if __name__ == "__main__":
    main()
