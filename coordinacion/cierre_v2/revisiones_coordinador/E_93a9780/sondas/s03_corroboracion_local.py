"""S03 · Para las 21 citas NO OBSERVABLES (documento ausente de esta maquina), busca el mismo texto
literal (normalizado) en los PDF de Elis que si estan en la base 4.14 local. Un hallazgo es solo
CORROBORACION INDIRECTA (otro documento, otra pagina): no verifica la cita en su documento declarado.
Tambien busca las 7 citas del URD 2025 en otros documentos (para saber si eran ya conocidas).

Uso: python3 -I s03_corroboracion_local.py <dir_elis_decisiones> <LECTURA_FUENTES.jsonl> <salida.json>
"""
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import norm, sha256  # noqa: E402

base, jsonl, salida = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
pdfs = sorted(base.rglob("*.pdf"))
textos = {}
for p in pdfs:
    r = subprocess.run(["pdftotext", str(p), "-"], capture_output=True, text=True, encoding="utf-8", errors="replace")
    textos[p] = [norm(pg) for pg in r.stdout.split("\f")]
docs_meta = {str(p.relative_to(base)): {"sha256": sha256(p), "paginas_extraidas": len(textos[p])} for p in pdfs}
regs = [json.loads(l) for l in open(jsonl, encoding="utf-8") if l.strip()]
citas = [r for r in regs if r["tipo"] == "cita"]
out = {"documentos_locales": docs_meta, "citas": []}
for i, c in enumerate(citas, 1):
    q = norm(c["cita"])
    # citas largas o truncadas: probar tambien los primeros 60 caracteres
    claves = [q] + ([q[:60]] if len(q) > 80 else [])
    hits = []
    for p, pags in textos.items():
        for n, t in enumerate(pags, 1):
            for k in claves:
                if k in t:
                    hits.append({"doc": str(p.relative_to(base)), "pagina_pdf": n, "clave": "completa" if k == q else "primeros_60"})
                    break
    out["citas"].append({"n": i, "pregunta": c["pregunta"], "documento_declarado": c["documento"],
                         "pagina_declarada": c["pagina_pdf"], "cita": c["cita"][:120], "en_otros_locales": hits})
    hs = "; ".join(f"{h['doc'].split('/')[-1]} p{h['pagina_pdf']} ({h['clave']})" for h in hits) or "-"
    print(f"{i:2d} {c['pregunta']} {c['documento']} p{c['pagina_pdf']}: {hs}")
Path(salida).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
