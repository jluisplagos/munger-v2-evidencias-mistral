"""S04 · ENTREGA.json frente a la plantilla y coherencia de huellas/bytes/paginas de los 12 documentos
(11 nuevos + URD 2025) entre FUENTES_Y_BUSQUEDA.csv, LECTURA_FUENTES.jsonl y ENTREGA.json.
Busca en esta maquina (sin red) cualquier copia de los 11 PDF por tamano y huella.

Uso: python3 -I s04_entrega_y_preservacion.py <dir_entrega> <PLANTILLA_ENTREGA.json> <raiz_busqueda>... -- <salida.json>
"""
import csv
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import sha256  # noqa: E402

args = sys.argv[1:]
salida = args[args.index("--") + 1]
args = args[:args.index("--")]
ent_dir, plantilla, raices = Path(args[0]), json.load(open(args[1], encoding="utf-8")), args[2:]
E = json.load(open(ent_dir / "ENTREGA.json", encoding="utf-8"))
out = {}

# 1. campos frente a plantilla
kp, ke = set(plantilla), set(E)
out["campos_faltan"] = sorted(kp - ke)
out["campos_extra"] = sorted(ke - kp)
out["campos_nulos"] = sorted(k for k in kp & ke if E[k] in (None, [], "") and k not in ("candidata_producto_sha", "banco_sha", "revision_por_otro_contexto", "precondiciones_simuladas"))
out["claves_prueba_faltan"] = [sorted(set(plantilla["pruebas"][0]) - set(p)) for p in E["pruebas"]]
out["pruebas"] = [{k: p[k] for k in ("comando", "exit_esperado", "exit_observado", "resultado")} for p in E["pruebas"]]
out["apto_dinero_real"] = E["apto_dinero_real"]
out["apto_igual_plantilla"] = E["apto_dinero_real"] == plantilla["apto_dinero_real"]
out["integrado_en_producto"] = E["integrado_en_producto"]
out["revision_por_otro_contexto"] = E["revision_por_otro_contexto"]
txtE = json.dumps(E, ensure_ascii=False).lower()
out["menciones_autoaprobacion"] = [m for m in re.findall(r"[^.;]{0,60}(?:aprobad|aceptad|autoaprueb|conforme)[^.;]{0,60}", txtE)]
out["sha_por_archivo_en_ENTREGA"] = bool(re.search(r"[0-9a-f]{64}", json.dumps(E["fuentes_y_preservacion"])))
out["hashes_64_en_ENTREGA"] = sorted(set(re.findall(r"[0-9a-f]{64}", json.dumps(E))))

# 2. coherencia CSV / JSONL
regs = [json.loads(l) for l in open(ent_dir / "LECTURA_FUENTES.jsonl", encoding="utf-8") if l.strip()]
docs = {r["id"]: r for r in regs if r["tipo"] == "documento"}
citas = [r for r in regs if r["tipo"] == "cita"]
filas = [r for r in csv.DictReader(open(ent_dir / "FUENTES_Y_BUSQUEDA.csv", encoding="utf-8")) if r["estado"].startswith("DESCARGADO")]
csvd = {r["nombre"]: r for r in filas}
tabla = []
for fid, d in docs.items():
    c = csvd.get(fid)
    m = re.search(r"(\d+) pags", c["notas"]) if c else None
    tabla.append({"id": fid, "sha256": d["sha256"], "bytes": d["bytes"], "paginas": d["paginas_pdf"],
                  "url_final": d["url_final"],
                  "csv_sha_igual": bool(c and c["sha256"] == d["sha256"]), "csv_bytes_igual": bool(c and c["bytes"] == d["bytes"]),
                  "csv_paginas_igual": bool(m and m.group(1) == d["paginas_pdf"]), "csv_url_igual": bool(c and c["ruta_o_recurso"] == d["url_final"]),
                  "en_ENTREGA_json": d["sha256"] in out["hashes_64_en_ENTREGA"],
                  "n_citas": sum(1 for x in citas if x["documento"] == fid),
                  "citas_sha_igual": all(x["sha256_doc"] == d["sha256"] for x in citas if x["documento"] == fid),
                  "citas_pag_en_rango": all(1 <= int(x["pagina_pdf"]) <= int(d["paginas_pdf"]) for x in citas if x["documento"] == fid),
                  "estado_preservacion": d["estado_preservacion"][:24]})
out["documentos"] = tabla
out["n_documentos"], out["n_citas"], out["n_registros"] = len(docs), len(citas), len(regs)
out["csv_sin_jsonl"] = sorted(set(csvd) - set(docs))

# 3. busqueda local de los 11 por tamano y huella
objetivo = {int(d["bytes"]): (fid, d["sha256"]) for fid, d in docs.items() if fid != "urd2025"}
encontrados = {fid: [] for fid, _ in objetivo.values()}
urd = []
for raiz in raices:
    for dp, dn, fn in os.walk(raiz):
        if dp.startswith("/proc"):
            dn[:] = []
            continue
        for f in fn:
            p = os.path.join(dp, f)
            try:
                st = os.lstat(p)
            except OSError:
                continue
            if not os.path.isfile(p) or os.path.islink(p):
                continue
            if st.st_size in objetivo:
                fid, sh = objetivo[st.st_size]
                if sha256(p) == sh:
                    encontrados[fid].append(p)
            if st.st_size == int(docs["urd2025"]["bytes"]) and sha256(p) == docs["urd2025"]["sha256"]:
                urd.append(p)
out["copias_locales_11"] = encontrados
out["copias_locales_urd2025"] = len(urd)
Path(salida).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
for k in ("campos_faltan", "campos_extra", "campos_nulos", "claves_prueba_faltan", "apto_dinero_real", "apto_igual_plantilla",
          "integrado_en_producto", "revision_por_otro_contexto", "sha_por_archivo_en_ENTREGA", "n_documentos", "n_citas", "n_registros", "csv_sin_jsonl"):
    print(k, "=", out[k])
print("menciones_autoaprobacion =", out["menciones_autoaprobacion"])
print("hashes en ENTREGA.json =", out["hashes_64_en_ENTREGA"])
for p in out["pruebas"]:
    print("prueba:", p)
print("id | bytes | pags | sha16 | csv(sha,bytes,pags,url) | en ENTREGA | citas | citas sha/pag ok | copias locales")
for t in tabla:
    print(t["id"], "|", t["bytes"], "|", t["paginas"], "|", t["sha256"][:16], "|", t["csv_sha_igual"], t["csv_bytes_igual"], t["csv_paginas_igual"], t["csv_url_igual"],
          "|", t["en_ENTREGA_json"], "|", t["n_citas"], "|", t["citas_sha_igual"], t["citas_pag_en_rango"], "|",
          len(encontrados.get(t["id"], [])) if t["id"] != "urd2025" else f"urd2025 copias={len(urd)}")
