"""E-R6: publica en Git (solo texto) extractos ACOTADOS de las paginas citadas.

Para cada cita de LECTURA_FUENTES.jsonl escribe extractos/<doc>_p<pagina>.txt con:
- cabecera con la huella del PDF (sha256, bytes), url_final, titulo, pagina, patron y linea;
- la ventana de texto que contiene la coincidencia (400 caracteres a cada lado, acotada).

Idempotente: reescribe los extractos desde cero en cada ejecucion.
Los PDF siguen fuera del Git (PROVISIONAL; upload a Release bloqueado con HTTP 401 en
uploads.github.com, documentado; no se reintenta ni se piden tokens). El almacen duradero
lo decide el usuario.
"""
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
TRABAJO = RAIZ / ".trabajo/elis_fuentes"
SALIDA = RAIZ / "resultados_cierre/elis_fuentes"
VENTANA = 400


def pagina_texto(fid, page):
    lines = (TRABAJO / "texto" / f"{fid}.txt").read_text(encoding="utf-8").splitlines()
    out, cur = [], None
    for ln in lines:
        m = re.match(r"\[PDF PAGE (\d+)\]", ln)
        if m:
            if cur == page:
                break
            cur = int(m.group(1))
            if cur == page:
                out = [ln]
                continue
        if cur == page:
            out.append(ln)
    return "\n".join(out)


def main():
    registros = [json.loads(l) for l in (SALIDA / "LECTURA_FUENTES.jsonl").read_text(encoding="utf-8").splitlines()]
    docs = {r["id"]: r for r in registros if r["tipo"] == "documento"}
    citas = [r for r in registros if r["tipo"] == "cita"]
    por_pagina = {}
    for c in citas:
        por_pagina.setdefault((c["documento"], c["pagina_pdf"]), []).append(c)
    destino = SALIDA / "extractos"
    destino.mkdir(parents=True, exist_ok=True)
    for viejo in destino.glob("*.txt"):
        viejo.unlink()
    n = 0
    for (fid, page), cs in sorted(por_pagina.items()):
        d = docs[fid]
        texto_pag = pagina_texto(fid, page)
        partes = [
            f"# extracto acotado de pagina citada - E-ELIS (corregido E-R6)",
            f"# documento={fid} titulo={d['titulo']}",
            f"# pagina_pdf={page} sha256_pdf={d['sha256']} bytes_pdf={d['bytes']}",
            f"# url_final={d['url_final']} http={d['http']} fecha_descarga={d['fecha_descarga']}",
            f"# tipo_evidencia={d['tipo_evidencia']} estado_preservacion=PROVISIONAL (PDF fuera de Git; upload 401 documentado)",
            "",
        ]
        for c in cs:
            p = c["patron"].replace(" ", r"\s+")
            m = re.search(p, texto_pag, re.IGNORECASE | re.DOTALL)
            if not m:
                raise AssertionError(f"la cita ya no esta en su pagina: {fid} p{page} /{c['patron']}/")
            a = max(0, m.start() - VENTANA)
            b = min(len(texto_pag), m.end() + VENTANA)
            partes.append(f"## cita pregunta={c['pregunta']} linea_txt={c['linea_txt']} patron={c['patron']}")
            partes.append(f"## hallazgo: {c['hallazgo']}")
            partes.append("---- ventana acotada (400 caracteres a cada lado) ----")
            partes.append(texto_pag[a:b])
            partes.append("")
        (destino / f"{fid}_p{page}.txt").write_text("\n".join(partes), encoding="utf-8")
        n += 1
    print(f"publicados {n} extractos de paginas citadas en {destino.relative_to(RAIZ)}/ (idempotente: reescritos desde cero)")


if __name__ == "__main__":
    main()
