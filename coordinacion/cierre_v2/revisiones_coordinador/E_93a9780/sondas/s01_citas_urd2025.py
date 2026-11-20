"""S01 · Comprueba en su pagina PDF las citas de LECTURA_FUENTES.jsonl cuyo documento esta presente
en la base 4.14 local (solo urd2025), tras confirmar que la huella local coincide con la declarada.
Las citas de documentos ausentes se marcan NO_OBSERVABLE.

Uso: python3 -I s01_citas_urd2025.py <pdf_urd2025_base414> <LECTURA_FUENTES.jsonl> <salida.json>
Extractores: pdftotext -layout (principal) y pdftotext sin -layout (segundo extractor, orden de lectura),
porque el maquetado a dos columnas parte frases en -layout.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import norm, pagina, sha256  # noqa: E402

pdf, jsonl, salida = sys.argv[1], sys.argv[2], sys.argv[3]
regs = [json.loads(l) for l in open(jsonl, encoding="utf-8") if l.strip()]
docs = {r["id"]: r for r in regs if r["tipo"] == "documento"}
citas = [r for r in regs if r["tipo"] == "cita"]

sha_local = sha256(pdf)
sha_decl = docs["urd2025"]["sha256"]
bytes_local = Path(pdf).stat().st_size
res = {"urd2025": {"sha256_local": sha_local, "sha256_declarado": sha_decl, "coincide": sha_local == sha_decl,
                   "bytes_local": bytes_local, "bytes_declarado": int(docs["urd2025"]["bytes"])},
       "citas": []}
print("URD2025 local sha256", sha_local, "== declarado:", sha_local == sha_decl, "| bytes", bytes_local)
assert sha_local == sha_decl, "huella del URD 2025 local distinta de la declarada: no se comprueba nada"

for i, c in enumerate(citas, 1):
    item = {"n": i, "pregunta": c["pregunta"], "documento": c["documento"], "pagina_pdf": c["pagina_pdf"],
            "cita": c["cita"]}
    if c["documento"] != "urd2025":
        item["veredicto"] = "NO_OBSERVABLE (documento no presente en esta maquina)"
        res["citas"].append(item)
        print(f"{i:2d} {c['pregunta']} {c['documento']} p{c['pagina_pdf']}: NO_OBSERVABLE")
        continue
    assert c["sha256_doc"] == sha_decl
    p = c["pagina_pdf"]
    objetivo = norm(c["cita"])
    en_layout = objetivo in norm(pagina(pdf, p, True))
    en_raw = objetivo in norm(pagina(pdf, p, False))
    # pagina vecina: descarta que la cita este en otra pagina y no en la declarada
    otras = [q for q in (p - 1, p + 1) if objetivo in norm(pagina(pdf, q, False))]
    ok = en_layout or en_raw
    item.update({"en_pagina_layout": en_layout, "en_pagina_raw": en_raw, "tambien_en_vecinas": otras,
                 "veredicto": "VERIFICADA_EN_PAGINA" if ok else "NO_ENCONTRADA_EN_PAGINA"})
    res["citas"].append(item)
    print(f"{i:2d} {c['pregunta']} urd2025 p{p}: layout={en_layout} raw={en_raw} vecinas={otras} -> {item['veredicto']}")

n_obs = sum(1 for x in res["citas"] if x["documento"] == "urd2025")
n_ok = sum(1 for x in res["citas"] if x["veredicto"] == "VERIFICADA_EN_PAGINA")
res["resumen"] = {"citas_total": len(citas), "observables": n_obs, "verificadas": n_ok,
                  "no_observables": len(citas) - n_obs}
print("RESUMEN", res["resumen"])
Path(salida).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
