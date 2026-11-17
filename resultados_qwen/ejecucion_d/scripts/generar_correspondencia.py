#!/usr/bin/env python3
"""Genera MAPA_CRITERIOS_BANCO.csv (D2-R5): los 109 criterios observables del banco
@4745f38 mapeados a observables/aserciones del arnés, con «sin aserción» donde no la
haya y su relevo. Fuente única: banco + adaptaciones.json (cobertura_banco) + matriz.

Uso: python3 generar_correspondencia.py   (escribe ../MAPA_CRITERIOS_BANCO.csv)
"""
import csv
import json
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
AUX = os.path.dirname(AQUI)
EV = os.path.join(AUX, "evidencias")
BANCO = os.environ.get("BANCO_DIR", "/workspace/banco_q1_v2/resultados_qwen/q1_v2/banco_revisado")
AD = json.load(open(os.path.join(AQUI, "especificaciones", "adaptaciones.json"), encoding="utf-8"))["casos"]

CAMPOS = ["caso", "familia", "control_banco", "naturaleza", "criterio_indice", "criterio_banco",
          "observable", "artefacto", "asercion_arnes", "cobertura", "razon", "estado_ejecucion", "evidencia"]


def main():
    casos = [json.loads(l) for l in open(os.path.join(BANCO, "casos_aceptacion.jsonl"), encoding="utf-8") if l.strip()]
    matriz = {r["id"]: r for r in csv.DictReader(open(os.path.join(AUX, "MATRIZ_EJECUCION.csv"), encoding="utf-8"))}
    out = os.path.join(AUX, "MAPA_CRITERIOS_BANCO.csv")
    n_total = n_asercion = 0
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        for c in casos:
            cid = c["id"]
            a = AD[cid]
            m = matriz[cid]
            for i, texto in enumerate(c["criterios_observables"]):
                cob = a["cobertura_banco"][i]
                asercion = cob.get("asercion") or ""
                cobertura = cob.get("cobertura", "sin_asercion")
                n_total += 1
                if asercion and cobertura == "asercion":
                    n_asercion += 1
                observable = f"asercion {asercion}: ver criterios_evaluados de la matriz" if asercion else a["artefacto"]
                w.writerow({
                    "caso": cid, "familia": c["familia"], "control_banco": c["control"], "naturaleza": c["naturaleza"],
                    "criterio_indice": i, "criterio_banco": texto,
                    "observable": observable, "artefacto": a["artefacto"],
                    "asercion_arnes": asercion or "sin aserción",
                    "cobertura": cobertura, "razon": cob.get("razon", ""),
                    "estado_ejecucion": m["estado_ejecucion"], "evidencia": m["evidencia"],
                })
    print(f"{out}: {n_total} criterios del banco · con aserción: {n_asercion} · sin aserción: {n_total - n_asercion}")
    rec_p = os.path.join(EV, "recuentos.json")
    if os.path.isfile(rec_p):
        rec = json.load(open(rec_p, encoding="utf-8"))
        rec["criterios_banco"] = {"total": n_total, "con_asercion": n_asercion, "sin_asercion": n_total - n_asercion}
        json.dump(rec, open(rec_p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
