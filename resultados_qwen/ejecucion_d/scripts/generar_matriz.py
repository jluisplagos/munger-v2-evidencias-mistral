#!/usr/bin/env python3
"""Genera MATRIZ_EJECUCION.csv v4: una fila por cada uno de los 36 casos del banco.

v4 (D3-R1 inv.2 / D3-R3 de CORRECCION_D3):
- la matriz REEVALÚA las aserciones de cada especificación sobre la evidencia
  publicada (no confía en campos del resultado): un resultado forjado (M2), con las
  salidas del producto vaciadas (N2a) o de otra candidata/banco (N2b) no da CUMPLE;
- exige harness 4.0, estado COMPONENTE_OK, errores vacíos, spec_sha256 coincidente,
  candidata_sha == esperado y banco_casos_sha256 == el del BANCO_DIR actual;
- la clasificación de Q1-026 sale de su resultado (ERROR_ENTORNO o COMPONENTE_OK
  reevaluado OK con spec de bloqueo_entorno), no de una constante;
- `preserva_sentido` y su justificación vienen de adaptaciones.json (dato);
- sin evidencia no hay veredicto positivo; sin carpeta de evidencias, 36 filas y
  0 CUMPLE con exit 0.

Uso: python3 generar_matriz.py   (escribe ../MATRIZ_EJECUCION.csv y ../evidencias/recuentos.json)
"""
import collections
import csv
import hashlib
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
AUX = os.path.dirname(AQUI)
EV = os.environ.get("EVIDENCIAS_DIR", os.path.join(AUX, "evidencias"))  # D4-R1 E3: la matriz respeta EVIDENCIAS_DIR
BANCO = os.environ.get("BANCO_DIR", "/workspace/banco_q1_v2/resultados_qwen/q1_v2/banco_revisado")
SHA_CANDIDATA_ESPERADO = os.environ.get("SHA_CANDIDATA_ESPERADO", "957af652cdc3bef3d67e8623c9572138bac685e9")

sys.path.insert(0, AQUI)
import ejecutar_caso as EC  # noqa: E402  (para reevaluar aserciones con el mismo código)
import lib_arnes as L  # noqa: E402

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


class CasoReeval:
    """Objeto mínimo para reevaluar aserciones desde la matriz."""

    def __init__(self, cid, ev_dir, archivos_producto):
        self.id = cid
        self.ev_dir = ev_dir
        self.errores = []
        self.archivos_producto = set(archivos_producto)


def reevaluar_criterios(spec, res, ev_dir):
    """Reevalúa cada criterio de la spec sobre la evidencia publicada. Devuelve
    (estados_reevaluados, ok)."""
    archivos = set(res.get("archivos_producto") or [])
    for p in res.get("pasos", []):
        if p.get("guardado_en"):
            archivos.add(p["guardado_en"])
    for paso in spec.get("pasos", []):
        if paso.get("op") == "copiar_artefacto" and paso.get("guardar"):
            archivos.add(paso["guardar"])
    caso = CasoReeval(spec["id"], ev_dir, archivos)
    estados = {}
    for c in spec.get("criterios", []):
        oks = [EC.evaluar_afirmacion(caso, a)[0] for a in c.get("afirma", [])]
        ok_all = bool(oks) and all(oks)
        if c.get("no_discriminante"):
            estados[c["id"]] = "OBSERVACION_NO_DISCRIMINANTE" if ok_all else "FALLA_COMPONENTE"
        else:
            estados[c["id"]] = "CUMPLE_COMPONENTE" if ok_all else "FALLA_COMPONENTE"
    ok = not caso.errores and all(
        (e == "CUMPLE_COMPONENTE") or (e == "OBSERVACION_NO_DISCRIMINANTE")
        for e in estados.values())
    return estados, ok


def main():
    os.makedirs(EV, exist_ok=True)
    casos = [json.loads(l) for l in open(os.path.join(BANCO, "casos_aceptacion.jsonl"), encoding="utf-8") if l.strip()]
    banco_sha = sha256_archivo(os.path.join(BANCO, "casos_aceptacion.jsonl"))
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
            criterios_txt = "; ".join(f"{x['id']}={x['estado']}" for x in criterios_res)
            bloqueo_spec = bool(spec and spec.get("bloqueo_entorno"))
            # D3-R1 inv.2: reevaluación real de las aserciones sobre la evidencia
            reeval_ok = False
            reeval_estados = {}
            if res and spec:
                reeval_estados, reeval_ok = reevaluar_criterios(spec, res, os.path.join(EV, cid))
            ids_res = [x.get("id") for x in criterios_res]
            ids_spec = [x.get("id") for x in (spec.get("criterios", []) if spec else [])]
            base_valida = bool(
                res and res.get("harness_version") == L.HARNESS_VERSION
                and res.get("estado_caso") == "COMPONENTE_OK"
                and not res.get("errores") and not res.get("afirmaciones_fallidas")
                and sp and res.get("spec_sha256") == spec_sha
                and res.get("candidata_sha") == SHA_CANDIDATA_ESPERADO
                and res.get("banco_casos_sha256") == banco_sha
                and ids_res == ids_spec
                and reeval_ok
                and all(x.get("estado") == reeval_estados.get(x.get("id")) for x in criterios_res)
            )
            if bloqueo_spec and res and res.get("estado_caso") == "ERROR_ENTORNO":
                estado, vcomp = "BLOQUEO_ENTORNO", ""
                evidencia = f"evidencias/{cid}/resultado_ejecucion.json (ERROR_ENTORNO: bloqueo documentado; no cuenta como CUMPLE)"
                recuentos["bloqueo_entorno"] += 1
            elif bloqueo_spec and base_valida:
                estado, vcomp = "BLOQUEO_ENTORNO", ""
                evidencia = (f"evidencias/{cid}/resultado_ejecucion.json (bloqueo de entorno reevaluado OK; "
                            f"ningún criterio del banco observado; no cuenta como CUMPLE)")
                recuentos["bloqueo_entorno"] += 1
            elif base_valida:
                estado, vcomp = "PARCIAL_COMPONENTE", "CUMPLE"
                evidencia = (f"evidencias/{cid}/resultado_ejecucion.json (harness {L.HARNESS_VERSION}, "
                            f"spec sha256 {spec_sha[:12]}…, aserciones reevaluadas OK)")
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
            elif estado == "BLOQUEO_ENTORNO":
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
