#!/usr/bin/env python3
"""Genera MATRIZ_EJECUCION.csv v3: una fila por cada uno de los 36 casos del banco.

v3 (D2-R1d/R3/R5 de CORRECCION_D2):
- el veredicto de componente se RECALCULA desde los criterios y las aserciones del
  resultado (harness 2.0/3.0, estado COMPONENTE_OK, criterios no vacíos y todos
  CUMPLE_COMPONENTE) Y la huella de la especificación usada coincide con la del disco;
  un resultado forjado con dos campos no da CUMPLE (sonda P4);
- Q1-026 (spec con `bloqueo_entorno`) queda BLOQUEO_ENTORNO y NO cuenta como
  componente CUMPLE (D2-R3);
- `preserva_sentido` y su justificación vienen de adaptaciones.json (dato), ya no es
  una constante "sí" escrita en el código; igual que observacion_compartida y
  veredicto_caso_fijo (D2-R5);
- sin evidencia no hay veredicto positivo; sin carpeta de evidencias, 36 filas y
  0 CUMPLE con exit 0 (control explícito, no un crash).

Uso: python3 generar_matriz.py   (escribe ../MATRIZ_EJECUCION.csv y ../evidencias/recuentos.json)
"""
import collections
import csv
import hashlib
import json
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
AUX = os.path.dirname(AQUI)
EV = os.path.join(AUX, "evidencias")
BANCO = os.environ.get("BANCO_DIR", "/workspace/banco_q1_v2/resultados_qwen/q1_v2/banco_revisado")

CAMPOS = ["id", "familia", "control_banco", "naturaleza", "precondiciones",
          "componente", "interfaz_real", "parte_automatizable", "parte_relevo_supervisado",
          "observables", "artefacto_estado", "adaptacion", "preserva_sentido", "preserva_sentido_justificacion",
          "estado_ejecucion", "veredicto_componente", "veredicto_caso", "criterios_evaluados", "criterios_banco_n",
          "observacion_compartida", "evidencia", "comandos_reproducibles", "sin_comprobar"]

ADAPTACIONES = os.path.join(AQUI, "especificaciones", "adaptaciones.json")


def sha256_archivo(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def spec_de(cid):
    for d in ("piloto", "bloque2"):
        p = os.path.join(AQUI, "especificaciones", d, cid + ".json")
        if os.path.isfile(p):
            return p
    return None


def main():
    os.makedirs(EV, exist_ok=True)
    casos = [json.loads(l) for l in open(os.path.join(BANCO, "casos_aceptacion.jsonl"), encoding="utf-8") if l.strip()]
    ad = json.load(open(ADAPTACIONES, encoding="utf-8"))["casos"]
    out = os.path.join(AUX, "MATRIZ_EJECUCION.csv")
    recuentos = {"casos": len(casos), "estado_ejecucion": {}, "veredicto_componente": {}, "veredicto_caso": {},
                 "naturaleza": {}, "con_ejecucion_propia": 0, "bloqueo_entorno": 0,
                 "con_observacion_compartida": 0, "sin_ejecutar": 0, "criterios_banco_total": 0}
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        for c in casos:
            cid = c["id"]
            a = ad[cid]
            res_p = os.path.join(EV, cid, "resultado_ejecucion.json")
            sp = spec_de(cid)
            spec = json.load(open(sp, encoding="utf-8")) if sp else None
            spec_sha = sha256_archivo(sp) if sp else None
            res = None
            if os.path.isfile(res_p):
                try:
                    res = json.load(open(res_p, encoding="utf-8"))
                except Exception:
                    res = None
            criterios_res = res.get("criterios", []) if res else []
            # D2-R1d: CUMPLE solo si el resultado es real (criterios + aserciones OK) y
            # la spec usada es la del disco (huella coincidente).
            componente_valido = bool(
                res and res.get("harness_version") in ("2.0", "3.0")
                and res.get("estado_caso") == "COMPONENTE_OK"
                and criterios_res and all(x.get("estado") == "CUMPLE_COMPONENTE" for x in criterios_res)
                and sp and res.get("spec_sha256") == spec_sha
            )
            bloqueo = bool(spec and spec.get("bloqueo_entorno"))
            criterios_txt = "; ".join(f"{x['id']}={x['estado']}" for x in criterios_res)
            if bloqueo and res:
                estado, vcomp = "BLOQUEO_ENTORNO", ""
                evidencia = f"evidencias/{cid}/resultado_ejecucion.json (bloqueo de entorno documentado; no cuenta como componente CUMPLE)"
                recuentos["bloqueo_entorno"] += 1
            elif componente_valido:
                estado, vcomp = "PARCIAL_COMPONENTE", "CUMPLE"
                evidencia = f"evidencias/{cid}/resultado_ejecucion.json (harness {res.get('harness_version')}, spec sha256 {spec_sha[:12]}…, aserciones OK)"
                recuentos["con_ejecucion_propia"] += 1
            elif res:
                estado, vcomp = f"ERROR ({res.get('estado_caso')})", ""
                evidencia = f"evidencias/{cid}/resultado_ejecucion.json (estado {res.get('estado_caso')})"
            else:
                estado, vcomp = "NO_EJECUTADO", ""
                evidencia = "sin evidencia de ejecución"
            fijo = a.get("veredicto_caso_fijo")
            if fijo:
                vcaso = f"{fijo['veredicto']} ({fijo['nota']})"
            elif bloqueo:
                vcaso = "NO_OBSERVABLE (bloqueo de entorno: faltan pdftotext/soffice/agente; paquete en relevo)"
            elif estado == "PARCIAL_COMPONENTE":
                vcaso = "sin veredicto de caso (pendiente de agente)"
            else:
                vcaso = "sin veredicto (no ejecutado)"
            obs = a.get("observacion_compartida", "")
            if obs:
                recuentos["con_observacion_compartida"] += 1
            if estado.startswith("NO_EJECUTADO") and not obs:
                recuentos["sin_ejecutar"] += 1
            recuentos["criterios_banco_total"] += len(c["criterios_observables"])
            w.writerow({
                "id": cid, "familia": c["familia"], "control_banco": c["control"], "naturaleza": c["naturaleza"],
                "precondiciones": c["precondiciones"],
                "componente": a["componente"], "interfaz_real": a["interfaz_real"],
                "parte_automatizable": a["automatizable"], "parte_relevo_supervisado": a["relevo"],
                "observables": " | ".join(a["observables"]), "artefacto_estado": a["artefacto"],
                "adaptacion": a["adaptacion"],
                "preserva_sentido": a.get("preserva_sentido", "sí"),
                "preserva_sentido_justificacion": a.get("preserva_sentido_justificacion", ""),
                "estado_ejecucion": estado,
                "veredicto_componente": vcomp,
                "veredicto_caso": vcaso,
                "criterios_evaluados": criterios_txt,
                "criterios_banco_n": len(c["criterios_observables"]),
                "observacion_compartida": obs or "-",
                "evidencia": evidencia,
                "comandos_reproducibles": (f"python3 scripts/ejecutar_caso.py scripts/{os.path.relpath(sp, AQUI)}" if sp else "pendiente de especificación ejecutable"),
                "sin_comprobar": a["sin_comprobar"],
            })
            recuentos["estado_ejecucion"][estado] = recuentos["estado_ejecucion"].get(estado, 0) + 1
            key_vc = vcomp or "sin veredicto de componente"
            recuentos["veredicto_componente"][key_vc] = recuentos["veredicto_componente"].get(key_vc, 0) + 1
    vc = collections.Counter()
    nat = collections.Counter()
    with open(out, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            vc[row["veredicto_caso"].split(" (")[0]] += 1
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
    print("  criterios del banco:", recuentos["criterios_banco_total"])


if __name__ == "__main__":
    main()
